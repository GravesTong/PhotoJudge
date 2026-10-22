# Changelog

本文件记录 PhotoJudge（摄判官）各版本的显著变更。遵循 [Keep a Changelog](https://keepachangelog.com/zh-CN/1.0.0/) 与 [语义化版本](https://semver.org/lang/zh-CN/)。

## [未发布]

### 计划中（v1.0）
- 视觉分析层实例化：模型多模态读照片自动产出 vision input
- CI / 单元测试 / 文档站点
- 题材权重正式固化
- 多图批量报告的完整演示

## [0.2.0] - 2026-10-22

### 新增
- `rules/` 六维打分规则填充完成，共 72 条（构图15/曝光14/对焦10/色彩10/内容12/后期11），依据四类公开来源交叉综合
- `engine/annotate.py`：图像标注能力，支持三分线、主体位置、过曝/死黑提示，以及**问题文字标注**（白字细黑边、字号随图自适应）
- `docs/report-schema.json` 补入 `issue_marks`（问题标注）字段
- `docs/report-batch-schema.json`：多图（≥2）批量诊断输出契约（排行 + 统计 + 每张独立报告）
- 开源配套文档：CONTRIBUTING / CODE_OF_CONDUCT / SECURITY / CHANGELOG / Issue & PR 模板 / 发布流程

### 变更
- 冲突收敛：7 处冲突收敛为引用规则，K6 并入 PPC-009（`rules/conflicts.md`）
- 权重表标注"依据库核验"（人像 30/25/20/15/10、风光 30/25/25/10/10）
- 引擎规则加载改为宽松逐行解析，零第三方依赖（规避严格 YAML 对中文冒号/全角引号解析失败）

### 修复
- 修复 `annotate.py` 默认字体过小、无描边在明暗背景下不可读的问题

## [0.1.0] - 2026-10-21

### 新增
- 产品框架定稿：六维诊断、题材权重默认值、输出结构、硬约束
- Skill 骨架：SKILL.md、规则占位、输出模板、架构说明、LICENSE（MIT）
- `engine/score.py` 打分引擎：题材加权、影响扣分、问题排序、报告 JSON 输出，`--demo` 可运行
- JSON schema + 纯黑背景 HTML 报告模板（标注图内嵌）输出契约
