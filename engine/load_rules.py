# -*- coding: utf-8 -*-
"""PhotoJudge 规则加载器：解析 rules/ 下 6 个维度文件的 ```yaml 块为规则对象。

说明：rules 的 YAML 块是"模板化文本"，含中文标点、全角引号、URL、分号等，
不保证是严格 YAML，故不使用 PyYAML，改用针对该受控结构的宽松逐行解析器，
实现零第三方依赖、对中文内容健壮。

用法：
    from load_rules import load_rules
    rules = load_rules()   # {rule_id: {...}}，含推断出的 dimension 字段
"""
import os
import re

RULES_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "rules")
RULE_FILES = [
    "composition.md",
    "exposure.md",
    "focus.md",
    "color.md",
    "subject.md",
    "post-processing.md",
]
DIMENSION_NAMES = {
    "COMP": "构图",
    "EXP": "曝光",
    "FOC": "对焦与清晰度",
    "COL": "色彩与白平衡",
    "SUB": "内容与主体",
    "PPC": "后期建议",
}
_FIELD_RE = re.compile(r"^([A-Za-z_]+):\s*(.*)$")
_LIST_ITEM_RE = re.compile(r"^\s+-\s+(.*)$")


def _extract_yaml_blocks(text):
    """提取文本中的 ```yaml ... ``` 代码块。"""
    return re.findall(r"```yaml\n(.*?)```", text, re.S)


def _parse_yaml_block(block):
    """宽松解析单个 ```yaml 块为 dict。

    支持结构：
      key: value                      -> 标量字段
      key:                            -> 后接缩进列表的字段
        - item                        -> 列表项（追加到当前 key）
      以空白开头且非列表项的行         -> 当前标量字段的续行（拼接）
    忽略空行与注释。
    """
    d = {}
    current_key = None
    current_is_list = False
    for raw in block.split("\n"):
        line = raw.rstrip()
        if not line.strip():
            continue
        if line.lstrip().startswith("#"):
            continue
        m_list = _LIST_ITEM_RE.match(line)
        if m_list:
            if not current_is_list:
                d[current_key] = []
                current_is_list = True
            d[current_key].append(m_list.group(1).strip())
            continue
        m_field = _FIELD_RE.match(line)
        if m_field:
            current_key = m_field.group(1)
            value = m_field.group(2).strip()
            if value:
                d[current_key] = value
            else:
                # 值为空：可能是列表字段头，也可能是空字符串，先置占位
                d[current_key] = None
                current_is_list = False
            continue
        # 续行：追加到当前标量字段
        if current_key is not None and not current_is_list:
            prev = d.get(current_key)
            if prev:
                d[current_key] = f"{prev}{line.strip()}"
    # 清理占位 null（列表字段头会因后续列表项被替换为列表，这里兜底）
    for k in list(d.keys()):
        if d[k] is None:
            d.pop(k)
    return d


def load_rules():
    """加载全部规则，返回 {rule_id: rule_dict}。"""
    rules = {}
    for fname in RULE_FILES:
        path = os.path.join(RULES_DIR, fname)
        with open(path, encoding="utf-8") as f:
            text = f.read()
        for block in _extract_yaml_blocks(text):
            d = _parse_yaml_block(block)
            if not d or "id" not in d:
                continue
            rid = d["id"]
            d.setdefault("dimension", rid.split("-")[0])
            # source 归一化为列表
            if "source" in d and not isinstance(d["source"], list):
                d["source"] = [d["source"]]
            rules[rid] = d
    return rules


def dimension_name(prefix):
    return DIMENSION_NAMES.get(prefix, prefix)


if __name__ == "__main__":
    rules = load_rules()
    print(f"加载规则 {len(rules)} 条")
    for prefix in ["COMP", "EXP", "FOC", "COL", "SUB", "PPC"]:
        n = sum(1 for rid in rules if rid.startswith(prefix))
        print(f"  {prefix} ({dimension_name(prefix)}): {n} 条")
