# 贡献指南（Contributing Guide）

欢迎为 **PhotoJudge（摄判官）** 贡献代码、规则、文档或示例。请先阅读本指南与 [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md)。

## 目录

- [项目结构速览](#项目结构速览)
- [贡献类型](#贡献类型)
- [开发环境](#开发环境)
- [规则贡献规范](#规则贡献规范)
- [提交流程](#提交流程)
- [Issue 与 PR 规范](#issue-与-pr-规范)
- [编码与提交约定](#编码与提交约定)

## 项目结构速览

```
rules/          六维打分规则（composition/exposure/focus/color/subject/post-processing）
engine/         打分引擎（load_rules / score / annotate）
docs/           架构、引擎规范、报告 schema、发布流程
examples/       示例输入与输出
output/         报告 Markdown 模板
```

## 贡献类型

| 类型 | 说明 | 入口 |
|---|---|---|
| 新增/修订规则 | 补充某维度打分规则或修正口径 | `rules/<维度>.md` + 说明依据 |
| 引擎功能 | 打分逻辑、标注、批量、CLI | `engine/` |
| 文档 | README、指南、schema | 对应 `.md` |
| 示例 | 演示输入/输出 | `examples/` |
| 报告问题 | 缺陷、疑问、建议 | GitHub Issue |

## 开发环境

- Python 3.8+；运行引擎无需第三方依赖；标注需 Pillow。
- 本地快速验证：
  ```bash
  cd engine
  python score.py --demo                 # 内置示例
  python score.py vision-input.json --output out.json
  python annotate.py 原图.jpg --annotations out.json --output 标注图.jpg
  ```

## 规则贡献规范

PhotoJudge 的差异化在"**可解释 + 可溯源**"，因此新增/修改规则必须满足：

1. **可解释**：每条含 `id`、`rule`（问题/情形描述）、`why`（为什么）、`how`（怎么改）、`weight_hint`（建议权重）、`source`（来源 URL/出处）、`evidence`（证据等级：已查证 / 通识 / 一方称）、`conflicts`（如有冲突）。
2. **可溯源**：`source` 必须是可查证的公开来源；`evidence=一方称` 的条目应标注"参考建议"，不作为硬扣分。
3. **双口径**：后期相关 `how` 尽量同时给手机（醒图/VSCO/LR 移动端）与电脑（LR/PS）口径；无手机口径的注明。
4. **不评判主观审美**：规则只判可客观描述的结构事实，不评"好不好看"。
5. **冲突如实分列**：来源口径不一致时写入 `rules/conflicts.md`，不强行统一。

> 依据库总源见 `摄影六维打分规则依据库.md`；拆分口径见 `rules/README.md`。

## 提交流程

1. **先开 Issue**：说明你想做什么（新规则/修 bug/新功能），维护者确认方向后再动手，避免返工。
2. **Fork + 分支**：从最新 `main` 切分支，命名如 `feat/add-exposure-rule`、`fix/score-bug`。
3. **小步提交**：一次 PR 聚焦一件事。
4. **补测试/示例**：引擎改动尽量附上可运行的示例输入与期望输出。
5. **提交 PR**：使用 [PULL_REQUEST_TEMPLATE](.github/PULL_REQUEST_TEMPLATE.md)，关联对应 Issue。

## Issue 与 PR 规范

- Bug 报告请用 [bug_report 模板](.github/ISSUE_TEMPLATE/bug_report.yml)：环境、复现步骤、期望/实际结果、日志。
- 新功能请用 [feature_request 模板](.github/ISSUE_TEMPLATE/feature_request.yml)：场景、期望、替代方案。
- 安全漏洞**不要**通过 Issue 公开提交，见 [SECURITY.md](SECURITY.md)。

## 编码与提交约定

- Python 遵循 PEP 8；核心脚本尽量零第三方依赖（标注除外）。
- 提交信息用中文或英文均可，但需简洁描述做了什么与为什么。
- 中文文档为主；代码注释可中英混用，保持可读。
- 遵守 [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md)。
