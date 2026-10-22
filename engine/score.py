# -*- coding: utf-8 -*-
"""PhotoJudge（摄判官）打分引擎：把"视觉分析命中的规则"转成结构化诊断报告。

输入（vision input JSON）：由视觉分析层（模型多模态读照片）产出——
  哪些规则问题被命中、每维亮点、题材与用途。
输出：符合 docs/report-schema.json 的诊断报告 JSON。

用法：
    python score.py path/to/vision-input.json [--output path/to/report.json]
    python score.py --demo          # 跑内置示例
"""
import argparse
import json
import os
import sys

from load_rules import dimension_name, load_rules

# 题材权重（已固化，依据库③节论证）。key 为维度前缀；PPC 不参与加权。
WEIGHTS = {
    "portrait": {"COMP": 30, "EXP": 25, "FOC": 20, "COL": 15, "SUB": 10},
    "landscape": {"EXP": 30, "COMP": 25, "COL": 25, "FOC": 10, "SUB": 10},
    "other": {"COMP": 20, "EXP": 20, "FOC": 20, "COL": 20, "SUB": 20},
}
OTHER_SUBJECTS = {"food", "street", "pet", "selfie"}  # 归入 "other" 均衡权重

# 影响程度 -> 每维扣分（从 10 分起扣）
IMPACT_PENALTY = {"high": 2.5, "medium": 1.5, "low": 0.5}
DEFAULT_PENALTY = 0.5

# 维度打分顺序（用于输出稳定排序）
DIM_ORDER = ["COMP", "EXP", "FOC", "COL", "SUB"]


def _penalty(impact):
    return IMPACT_PENALTY.get(impact, DEFAULT_PENALTY)


def _level(total):
    if total >= 9:
        return "优秀"
    if total >= 7:
        return "良好"
    if total >= 5:
        return "及格"
    if total >= 3:
        return "不及格"
    return "严重问题"


def _resolve_weights(subject):
    if subject in WEIGHTS:
        return WEIGHTS[subject]
    if subject in OTHER_SUBJECTS:
        return WEIGHTS["other"]
    return WEIGHTS["other"]


def _group_matches(matches):
    """按维度前缀分组命中的问题。"""
    groups = {}
    for m in matches or []:
        rid = m.get("rule_id", "")
        dim = rid.split("-")[0]
        groups.setdefault(dim, []).append(m)
    return groups


def build_report(vision_input, rules):
    photo = vision_input.get("photo", {})
    subject = photo.get("subject", "other")
    if subject in OTHER_SUBJECTS:
        subject = "other"
    weights = _resolve_weights(subject)
    matches = vision_input.get("matches", [])
    highlights = vision_input.get("highlights", [])

    groups = _group_matches(matches)
    highlight_map = {}
    for h in highlights or []:
        rid = h.get("rule_id", "")
        dim = rid.split("-")[0]
        highlight_map.setdefault(dim, []).append(h)

    # 每维打分（参与加权的前五维）
    dim_scores = {}
    for dim in DIM_ORDER:
        base = 10.0
        for m in groups.get(dim, []):
            base -= _penalty(m.get("impact"))
        dim_scores[dim] = max(round(base, 1), 0)

    # 后期建议维度：不参与加权，单独评分
    ppc_base = 10.0
    for m in groups.get("PPC", []):
        ppc_base -= _penalty(m.get("impact"))
    ppc_score = max(round(ppc_base, 1), 0)

    # 加权总评分
    weighted_sum = sum(dim_scores[d] * weights[d] for d in DIM_ORDER)
    total_score = round(weighted_sum / 100.0, 1)

    # 问题清单（跨维度，按 impact 排序：high > medium > low）
    issues = []
    for m in sorted(matches or [], key=lambda x: 0 if x.get("impact") == "high"
                    else (1 if x.get("impact") == "medium" else 2)):
        rid = m.get("rule_id", "")
        rule = rules.get(rid, {})
        dim = rid.split("-")[0]
        issues.append({
            "rule_id": rid,
            "dimension": dim,
            "impact": m.get("impact", "low"),
            "reason": m.get("note") or rule.get("why", ""),
            "action": rule.get("how", ""),
            "conflicts": rule.get("conflicts"),
        })

    # 后期方案（针对可修复问题，取 PPC 规则动作；手机/电脑口径按规则内容）
    edits = []
    for m in matches or []:
        rid = m.get("rule_id", "")
        rule = rules.get(rid, {})
        if rid.split("-")[0] == "PPC":
            edits.append({
                "issue": rid,
                "mobile": rule.get("mobile", None),
                "desktop": rule.get("how", ""),
            })

    # 维度明细
    dims = []
    for dim in DIM_ORDER:
        dims.append({
            "id": dim,
            "name": dimension_name(dim),
            "score": dim_scores[dim],
            "max": 10,
            "highlights": [h.get("note", "") for h in highlight_map.get(dim, [])],
            "issues": [m.get("rule_id", "") for m in groups.get(dim, [])],
        })
    dims.append({
        "id": "PPC",
        "name": dimension_name("PPC"),
        "score": ppc_score,
        "max": 10,
        "highlights": [h.get("note", "") for h in highlight_map.get("PPC", [])],
        "issues": [m.get("rule_id", "") for m in groups.get("PPC", [])],
    })

    report = {
        "schema_version": "1.0",
        "photo": {
            "id": photo.get("id", ""),
            "subject": subject,
            "purpose": photo.get("purpose", ""),
        },
        "weights": {
            "composition": weights["COMP"],
            "exposure": weights["EXP"],
            "focus": weights["FOC"],
            "color": weights["COL"],
            "subject": weights["SUB"],
        },
        "total": {
            "score": total_score,
            "max": 10,
            "level": _level(total_score),
            "summary": _summarize(total_score, issues),
        },
        "dimensions": dims,
        "issues": issues,
        "edits": edits,
        "annotations": _annotations(vision_input),
        "sources": {
            "rules_referenced": sorted({m.get("rule_id", "") for m in matches or []}),
            "conflicts_referenced": sorted({
                r.get("conflicts") for r in (rules.get(m.get("rule_id", ""), {})
                                             for m in matches or [])
                if r.get("conflicts")
            }),
            "note": "规则来自 rules/，原始来源见各条目 source 字段",
        },
    }
    return report


def _annotations(vision_input):
    """透传视觉分析层给出的标注参数（若提供）。"""
    return vision_input.get("annotations", {})


def _summarize(total_score, issues):
    top = issues[0] if issues else None
    if not top:
        return f"整体 {_level(total_score)}（{total_score}/10），无明显扣分点，可保持。"
    return (f"整体 {_level(total_score)}（{total_score}/10）。"
            f"最该先改：{top.get('rule_id')}——{top.get('reason', '')}")


def _demo_input():
    return {
        "photo": {"id": "demo-portrait.jpg", "subject": "portrait", "purpose": "social"},
        "matches": [
            {"rule_id": "COMP-002", "impact": "medium", "note": "主体居中偏呆板，未落三分点"},
            {"rule_id": "EXP-001", "impact": "high", "note": "天空高光溢出"},
            {"rule_id": "FOC-001", "impact": "medium", "note": "人像对焦落在鼻尖而非眼睛"},
            {"rule_id": "PPC-009", "impact": "low", "note": "手机端需补校色流程"},
        ],
        "highlights": [
            {"rule_id": "SUB-003", "note": "主体突出，背景干净"},
        ],
        "annotations": {
            "rule_of_thirds": True,
            "overexposure_mask": True,
        },
    }


def main():
    parser = argparse.ArgumentParser(description="PhotoJudge 打分引擎")
    parser.add_argument("input", nargs="?", help="视觉判据 JSON 文件路径")
    parser.add_argument("--output", help="输出报告 JSON 路径")
    parser.add_argument("--demo", action="store_true", help="运行内置示例")
    args = parser.parse_args()

    rules = load_rules()

    if args.demo:
        vision = _demo_input()
    else:
        if not args.input:
            parser.error("需要提供输入 JSON 文件，或使用 --demo")
        with open(args.input, encoding="utf-8") as f:
            vision = json.load(f)

    report = build_report(vision, rules)

    out = args.output
    if not out:
        out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "report-output.json")
    with open(out, "w", encoding="utf-8") as f:
        json.dump(report, f, ensure_ascii=False, indent=2)

    print(f"总评分：{report['total']['score']}/10（{report['total']['level']}）")
    print(f"题材权重：{report['weights']}")
    print("问题清单：")
    for i in report["issues"]:
        print(f"  [{i['impact']}] {i['rule_id']} {i['reason']}")
    print(f"报告已写入：{out}")


if __name__ == "__main__":
    sys.exit(main())
