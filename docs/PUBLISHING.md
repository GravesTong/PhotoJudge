# 发布流程（Publishing Guide）

本文说明 PhotoJudge 如何打版本、发 Release，供维护者使用。

## 版本策略

遵循 [语义化版本](https://semver.org/lang/zh-CN/)：

- **主版本（major）**：破坏性变更 / 输出契约不兼容。
- **次版本（minor）**：新增能力，向后兼容（如新增维度、批量、标注类型）。
- **补丁（patch）**：向后兼容的缺陷修复。

当前主线在 **v0.x**，任何行为变化都允许，但应在 CHANGELOG 与 Release Notes 中注明。

## 发布流程（Checklist）

### 1. 代码与自检
- [ ] 主干 `main` 处于可发布状态（引擎示例跑通、文档一致）。
- [ ] 更新 [CHANGELOG.md](../CHANGELOG.md)：把 "未发布" 中的条目移入新版本。
- [ ] 核对 README 的版本徽章、快速开始、目录结构。

### 2. 打标签
```bash
git tag v0.2.0
git push origin v0.2.0
```
- Tag 必须与 CHANGELOG 版本号一致。
- 可选：`git tag -a v0.2.0 -m "..."` 打附注标签。

### 3. 发布 Release Notes
在 GitHub Releases 创建对应 tag 的 release，内容包括：
- **标题**：`v0.2.0` + 一句话（如"规则库填充完成 + 图像标注能力"）。
- **高亮**：本次最主要的新能力 / 修复（面向用户，简短）。
- **完整变更**：链接到 CHANGELOG 对应段落。
- **安装/升级说明**：如有破坏性变更，明确说明迁移步骤。

### 4. 附带产物（可选）
- 打包 `engine/` 运行示例或示例报告到 `examples/`。
- 如需示例照片，使用无版权风险的自产/公开示例，不附第三方受版权照片。

## 分支与热修复

- 日常开发直接向 `main` 提 PR。
- 重大版本可维护 `release/<major>.<minor>` 分支做稳定化。
- 线上安全漏洞：见 [SECURITY.md](../SECURITY.md)，修复后按补丁版发布并出安全公告。

## 兼容性承诺

- 输出契约（`docs/report-schema.json` / `report-batch-schema.json`）变更必须升 `schema_version` 并在 CHANGELOG 注明。
- 规则条目 `id` 一经发布尽量保持稳定；重命名需在 CHANGELOG 提供映射表。
