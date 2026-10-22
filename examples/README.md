# Examples（示例）

本目录提供可直接参考/复用的示例输入与输出，帮助理解 PhotoJudge 的数据契约与运行方式。

## 输入示例

- [`vision-input.example.json`](vision-input.example.json)：一份完整的视觉判据输入（vision input），展示了 `photo` / `matches` / `highlights` / `annotations`（含 `issue_marks`）字段的写法。
- 更多真实判据输入见 `../engine/`（如 `test-photo-vision-input.json`、`poor-vision-input.json`）。

## 输出示例

- 单图报告 JSON：`../engine/test-photo-report.json`（9.5/10 优秀示例）、`../engine/poor-report.json`（7.3/10，曝光硬伤示例）。
- 报告模板：`../output/report-template.md`。
- 标注图：`../engine/test-photo-annotated.jpg`、`../engine/poor-annotated.jpg`（问题文字标注示例）。

## 快速试跑

```bash
cd ../engine
python score.py --demo                        # 引擎内置示例
python score.py ../examples/vision-input.example.json --output report.json
python annotate.py 你的照片.jpg --annotations report.json --output 标注图.jpg
```

## 如何产出你自己的 vision input

1. 读照片，按六维（构图/曝光/对焦/色彩/内容/后期）提取**客观结构判据**；
2. 对每个命中"问题情形"的规则，写入 `matches`（`rule_id` 须存在于 `../rules/`）；
3. 对每个做对的点写入 `highlights`；
4. 对可客观定位的问题，在 `annotations.issue_marks` 给坐标（0–1 归一化）与简短标签。

> 规则条目与 `rule_id` 见 `../rules/<维度>.md`；判据须可解释、可溯源。
