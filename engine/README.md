# engine/ — PhotoJudge 打分引擎（可运行）

把"视觉分析命中的规则"转成结构化诊断报告。确定性部分（规则匹配、加权打分、问题排序、报告输出）由本引擎代码完成，保证可解释、可复现；感知部分（读照片提判据）由模型多模态/视觉能力作为输入接口提供。

## 文件

| 文件 | 作用 |
|---|---|
| `load_rules.py` | 解析 `rules/` 六个维度文件的 ```yaml 块为规则对象。宽松解析器，零第三方依赖，兼容中文标点/全角引号/URL。 |
| `score.py` | 主程序：读视觉判据 JSON → 输出诊断报告 JSON（符合 `docs/report-schema.json`）。 |
| `report-output.json` | 内置示例运行产物（`--demo`）。 |

## 运行

```bash
# 内置示例
python score.py --demo

# 用真实视觉判据
python score.py path/to/vision-input.json --output path/to/report.json
```

## 输入：视觉判据 JSON（vision input）

由视觉分析层（模型读照片）产出，交给 `score.py`：

```json
{
  "photo": { "id": "xxx.jpg", "subject": "portrait", "purpose": "social" },
  "matches": [
    { "rule_id": "EXP-001", "impact": "high",   "note": "天空高光溢出" },
    { "rule_id": "COMP-002", "impact": "medium", "note": "主体居中呆板" }
  ],
  "highlights": [
    { "rule_id": "SUB-003", "note": "主体突出，背景干净" }
  ],
  "annotations": {
    "rule_of_thirds": true,
    "overexposure_mask": true
  }
}
```

字段说明：
- `matches`：视觉分析判定命中的规则**问题**。`rule_id` 必须存在（如 `COMP-002`，可对照 `rules/`）；`impact` ∈ `high/medium/low`；`note` 是面向照片的具体判据说明。
- `highlights`：判定做对的规则（同样给 `rule_id` + `note`）。
- `annotations`：可客观定位的标注参数，原样透传到报告。

## 打分口径

- 每维从 10 分起，按命中问题的 `impact` 扣分：high −2.5 / medium −1.5 / low −0.5，下限 0。
- 总评分 = Σ(五维分 × 题材权重) / 100；后期建议维度（PPC）不参与加权。
- 题材权重见 `score.py` 的 `WEIGHTS`（人像 30/25/20/15/10，风光 30/25/25/10/10，其他 20×5），可配置。
- 等级映射：≥9 优秀 / 7–8.9 良好 / 5–6.9 及格 / 3–4.9 不及格 / <3 严重问题。

## 输出

诊断报告 JSON，符合 `docs/report-schema.json`。每条问题带 `rule_id / dimension / impact / reason / action / conflicts`，`action` 取自对应规则的 `how`（可执行修改动作）。
