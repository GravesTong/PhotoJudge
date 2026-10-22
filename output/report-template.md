# 照片诊断报告 — PhotoJudge（摄判官）

> 本模板与 `docs/report-schema.json` 字段一一对应，同一份报告以 JSON（机器可读）与 Markdown（人可读）双格式输出。
> 规则依据：`rules/` 六维打分规则（COMP/EXP/FOC/COL/SUB/PPC）。打分与输出流程见 `docs/engine-spec.md`。

## 一、总评

- **总评分**：`<score>/10`（**`<level>`**）
- **一句话总结**：`<summary>` —— 给用户最核心的结论和最该改的一件事。

## 二、分项评分

| 维度 | 分项分 | 亮点 | 问题 |
|---|---|---|---|
| 构图（COMP） | `<x>/10` | `<highlights>` | `<issues>` |
| 曝光（EXP） | `<x>/10` | … | … |
| 对焦与清晰度（FOC） | `<x>/10` | … | … |
| 色彩与白平衡（COL） | `<x>/10` | … | … |
| 内容与主体（SUB） | `<x>/10` | … | … |
| 后期建议（PPC） | `<x>/10` | … | … |

> 权重（本张按 `<subject>` 题材）：构图 `<w>` / 曝光 `<w>` / 对焦 `<w>` / 色彩 `<w>` / 内容 `<w>`（后期维度不参与权重）。

## 三、问题清单（按影响优先级排序）

1. **`<rule_id>：<问题>`**（影响：`<高/中/低>`）
   - 为什么：`<reason>`（依据 `rules/<dimension>.md` 该条目）
   - 怎么改：`<action>`
   - 冲突提示：`<conflicts，如有>`
2. ……

## 四、后期方案（手机 / 电脑双口径）

| 问题 | 手机端（醒图/VSCO/LR移动端） | 电脑端（LR/PS） |
|---|---|---|
| `<issue>` | `<mobile>` | `<desktop>` |

> 无手机口径的条目（如锐化蒙版、Camera Calibration）已注明，仅给电脑口径。

## 五、视觉标注

- 原图叠加（忠于原图真实位置，不重绘）：
  - 三分线网格：`<on/off>`
  - 主体位置：`<坐标>`
  - 地平线：倾斜 `<angle>°`，`<是否需校正>`
  - 过曝区 / 死黑区高亮：`<on/off>`
  - 建议裁切框：`<x,y,w,h>`

## 附：JSON 结构（机器可读）

```json
{
  "schema_version": "1.0",
  "photo": { "id": "", "subject": "portrait", "purpose": "social" },
  "weights": { "composition": 30, "exposure": 25, "focus": 20, "color": 15, "subject": 10 },
  "total": { "score": 0, "max": 10, "level": "及格", "summary": "" },
  "dimensions": [
    { "id": "COMP", "name": "构图", "score": 0, "max": 10, "highlights": [], "issues": [] }
  ],
  "issues": [
    { "rule_id": "COMP-002", "dimension": "COMP", "impact": "high", "reason": "", "action": "", "conflicts": null }
  ],
  "edits": [
    { "issue": "COMP-002", "mobile": "", "desktop": "" }
  ],
  "annotations": {
    "rule_of_thirds": true,
    "subject_point": [0.33, 0.33],
    "horizon": { "angle": 0, "rotated": false },
    "overexposure_mask": true,
    "underexposure_mask": false,
    "crop_box": { "x": 0, "y": 0, "width": 1, "height": 1 }
  },
  "sources": {
    "rules_referenced": ["COMP-002"],
    "conflicts_referenced": [],
    "note": "规则来自 rules/，原始来源见各条目 source 字段"
  }
}
```

完整字段定义见 `docs/report-schema.json`。
