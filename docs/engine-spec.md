# PhotoJudge 引擎规范（Engine Spec）

> 说明"照片 → 诊断报告"的最小可用闭环如何工作：视觉分析 → 规则匹配 → 打分 → 生成报告 → 视觉标注。交付标准为纯黑背景 HTML 报告（标注原图内嵌，模板 `output/report-template.html`）；数据契约见 `docs/report-schema.json`。

## 一、输入

- 一张或多张照片（本地 / URL）。
- 可选题材（`portrait`/`landscape`/`food`/`street`/`pet`/`selfie`/`other`）与用途（`social`/`print`/`contest`/`record`）。用户未给题材时按 `other` 均衡权重。
- **输出随输入数量变化**：单张 → 输出单图 report（`report-schema.json`）；多张（N≥2）→ 每张独立诊断，外层包一个批量汇总容器（`report-batch-schema.json`，见 §三 输出）。

## 二、六步闭环

```
① 视觉分析    读照片，六维各提取"客观判据"（不评好不好看，只判结构事实）
② 规则匹配    对每个维度，扫描 rules/<dimension>.md 条目，判断命中"问题"或"亮点"
③ 打分        每维按命中情况给 0–10，按题材权重加权 → 总评分 + 等级
④ 问题清单    汇总所有"问题"条目，按影响（high/medium/low）排序
⑤ 后期方案    对可修复问题，从 PPC 规则给手机/电脑双口径动作
⑥ 视觉标注    对可客观定位的问题，在原图叠加标记（忠于真实位置）
```

### ① 视觉分析（读照片，提取判据）

只提取规则可判定的**客观结构事实**，不判断主观审美。按六维分别提取：

| 维度 | 提取的判据示例 |
|---|---|
| 构图 COMP | 主体坐标、是否在三分点；地平线倾斜角；竖线/栏杆是否穿过人物头颈；裁切是否卡关节 |
| 曝光 EXP | 直方图是否左右贴边（过曝/死黑）；白场景是否发灰；逆光人脸亮度 |
| 对焦 FOC | 人像是否对眼（合焦位置）；快门是否低于焦距倒数；是否手抖模糊 |
| 色彩 COL | 人脸是否偏黄/蓝/绿；白色是否还原；日落氛围是否被 AWB 抹平 |
| 内容 SUB | 一句话能否说清主体；是否有干扰物；脸占比；是否军姿式三面同平面 |
| 后期 PPC | 片灰时是压高光提阴影还是拉饱和；是否用 Vibrance 而非 Saturation |

> 判据取自 rules/ 各维度条目的 `rule` 与 `why`，做到"可解释"：每个判断都能定位到具体规则。

### ①a 视觉输入接口（vision input，视觉分析层 → 打分引擎）

视觉分析层把判据结构化为一份 **vision input JSON**，交给打分引擎（`engine/score.py`）生成报告：

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

- `matches`：判定命中的规则**问题**。`rule_id` 必须存在于 `rules/`（如 `COMP-002`）；`impact` ∈ `high/medium/low`；`note` 为面向该照片的具体判据。
- `highlights`：判定做对的规则（`rule_id` + `note`）。
- `annotations`：可客观定位的标注参数，原样透传到报告。
- 打分引擎按 `rule_id` 从 `rules/` 取 `why`/`how`，生成可解释的 `reason` 与可执行的 `action`。

### ② 规则匹配

对每个维度，将①提取的判据与该维规则文件（如 `rules/composition.md`）逐条比对：

- 命中规则描述的"问题情形" → 记入该维 `issues`（引用 `rule_id`）。
- 命中规则描述的"正确做法" → 记入该维 `highlights`。
- 若条目带 `conflicts`（如 `见 conflicts.md Kx`）→ 在报告中标注冲突提示，给出多来源不同口径，不强行选一。

### ③ 打分

- 每维：从 10 分起，按命中"问题"的规则数量与严重度扣分（具体扣分粒度建议：每条 high 扣 2–3、medium 扣 1–2、low 扣 0.5–1；可按规则 `evidence` 等级微调，已查证>通识>一方称）。
- 总评分 = Σ(维度分 × 该维题材权重) / 100（后期维度 PPC 不参与加权）。
- 等级映射：≥9 优秀 / 7–8.9 良好 / 5–6.9 及格 / 3–4.9 不及格 / <3 严重问题。
- 权重表：人像 构图30/曝光25/对焦20/色彩15/内容10；风光 曝光30/构图25/色彩25/对焦10/内容10；其他 五维各20。**默认值，依据库核验**，可配置。

### ④ 问题清单

- 汇总各维 `issues`，按 `impact`（high→medium→low）排序，同影响按维度顺序。
- 每条含：`rule_id` / `reason`（依据规则 why）/ `action`（依据规则 how）/ 冲突提示。

### ⑤ 后期方案

- 对每个"可修复"问题，从 `rules/post-processing.md`（PPC）取对应动作。
- 必须同时给手机（醒图/VSCO/LR 移动端）与电脑（LR/PS）口径；无手机口径的条目（如锐化蒙版、Camera Calibration）置 null 并在文案注明。

### ⑥ 视觉标注

- 仅对可**客观定位**的问题给标注，坐标归一化 0–1，忠于原图真实位置，不重绘、不改变原图像素。
- 标注类型：三分线网格、主体位置点、地平线倾斜角（是否需校正）、过曝区/死黑区高亮、建议裁切框、**问题文字标注（`issue_marks`，白字细黑边、字号随图自适应，标到问题对应位置）**。
- 使用图像标注能力在原图上叠加，输出到 `annotations` 字段。

## 三、输出

- 交付标准：**单文件纯黑背景 HTML 诊断报告**（标注原图以 base64 内嵌，图和报告一体、不分开）。
  - **HTML**（人可读交付）：`output/report-template.html` 渲染，给用户看。
  - **JSON**（机器可读）：`docs/report-schema.json` 定义，供程序消费。
- 两格式字段一一对应，用同一份数据生成，避免口径分裂。

### 多张照片（批量）输出

一次上传 **N≥2 张**时，每张照片独立走完整六步闭环、生成独立报告（**完全复用单图契约**），再在外层包一个批量汇总容器 `report-batch-schema.json`：

```json
{
  "schema_version": "1.0",
  "mode": "batch",
  "count": 3,
  "subject": "portrait",
  "purpose": "social",
  "summary": "3 张中 A 最优（9.5 优秀）；C 问题最多，共同短板是曝光。",
  "ranking": [
    { "rank": 1, "photo": "A.jpg", "score": 9.5, "level": "优秀", "top_issue": null },
    { "rank": 2, "photo": "B.jpg", "score": 7.3, "level": "良好", "top_issue": "EXP-011" },
    { "rank": 3, "photo": "C.jpg", "score": 5.1, "level": "及格", "top_issue": "EXP-007" }
  ],
  "stats": { "best": "A.jpg", "worst": "C.jpg", "avg": 7.3 },
  "reports": [ /* 每张独立单图 report，逐项符合 report-schema.json */ ],
  "annotated_artifacts": { "A.jpg": "A-annotated.jpg", "B.jpg": "B-annotated.jpg" }
}
```

要点：
- **单张/多张口径一致**：批量里的每张 report 与单独诊断一张时完全同构，程序可无差别消费。
- **选片优先**：`ranking` 按总分降序 + 每张 `top_issue`，让用户一眼看到哪张最好、每张最该改什么。
- **题材共用可覆盖**：批量级 `subject`/`purpose` 给默认权重，单张可在自身 `photo` 字段覆盖。
- **标注图**：每张生成独立标注图，路径映射进 `annotated_artifacts`。

## 四、硬约束（从 SKILL.md 继承）

- 评分可解释：每个扣分点给"为什么 + 怎么改"。
- 不评判主观审美/风格好坏。
- 不做"AI 生成图 vs 真实照片"鉴定。
- 视觉标注忠于原图真实位置。
- 后期参数口径区分手机与电脑。

## 五、当前状态与后续

- [x] 闭环逻辑定义（本文档）
- [x] 输出契约（schema + 模板）
- [ ] 在运行环境中落地：视觉分析调用多模态能力、规则匹配执行、标注能力接入
- [ ] 权重固化：按依据库③节论证定稿题材权重
