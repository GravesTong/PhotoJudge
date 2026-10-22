# -*- coding: utf-8 -*-
"""PhotoJudge 图像标注：在照片原图上叠加诊断标记，忠于原图，不重绘、不改变原图像素。

读取诊断报告 JSON 的 `annotations` 字段，在原图上绘制：
- 三分线网格（rule_of_thirds）
- 主体位置标记（subject_point，归一化 0–1）
- 地平线参考线（horizon，含倾斜角提示）
- 过曝/死黑区提示（overexposure_mask / underexposure_mask）
- 问题标注（issue_marks：白字细黑边，字号随图自适应，标到对应位置）

用法：
    python annotate.py 原图.jpg --annotations 报告.json --output 标注图.jpg
"""
import argparse
import json
import os

from PIL import Image, ImageDraw, ImageFont

GOLD = (255, 215, 0, 170)      # 三分线
RED = (255, 60, 60, 230)       # 主体标记
BLUE = (0, 160, 255, 200)      # 地平线
WHITE = (255, 255, 255, 255)   # 文字
BLACK = (0, 0, 0, 255)         # 文字描边

_FONT_CANDIDATES = (
    r"C:\Windows\Fonts\msyh.ttc",    # 微软雅黑
    r"C:\Windows\Fonts\msyhbd.ttc",
    r"C:\Windows\Fonts\simhei.ttf",  # 黑体
    r"C:\Windows\Fonts\arial.ttf",
    "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
)


def _load_font(size):
    """按优先级加载系统字体，全部失败退回 PIL 默认字体。"""
    for path in _FONT_CANDIDATES:
        if os.path.exists(path):
            try:
                return ImageFont.truetype(path, size)
            except Exception:
                continue
    return ImageFont.load_default()


def _text(draw, pos, s, font, stroke):
    """白字 + 细黑描边，保证任意明暗背景都能看清。"""
    draw.text(pos, s, font=font, fill=WHITE, stroke_width=stroke, stroke_fill=BLACK)


def draw_annotations(image_path, annotations, out_path):
    im = Image.open(image_path).convert("RGB")
    w, h = im.size
    draw = ImageDraw.Draw(im, "RGBA")

    # 动态字号：随图宽自适应，控制在 18–44px
    font_size = max(18, min(44, int(w * 0.032)))
    font = _load_font(font_size)
    stroke = max(2, font_size // 14)  # 细黑边

    # 1. 三分线网格
    if annotations.get("rule_of_thirds"):
        for i in (1, 2):
            x, y = w * i / 3, h * i / 3
            draw.line([(x, 0), (x, h)], fill=GOLD, width=2)
            draw.line([(0, y), (w, y)], fill=GOLD, width=2)

    # 2. 主体位置标记（归一化坐标 -> 像素）
    sp = annotations.get("subject_point")
    if sp and len(sp) == 2:
        px, py = int(sp[0] * w), int(sp[1] * h)
        r = max(12, font_size // 2)
        draw.ellipse([(px - r, py - r), (px + r, py + r)], outline=RED, width=3)
        draw.line([(px - r - 8, py), (px + r + 8, py)], fill=RED, width=2)
        draw.line([(px, py - r - 8), (px, py + r + 8)], fill=RED, width=2)

    # 3. 地平线参考线
    horizon = annotations.get("horizon")
    if horizon:
        y0 = int(h * 0.5)
        draw.line([(0, y0), (w, y0)], fill=BLUE, width=3)
        if horizon.get("rotated"):
            _text(draw, (10, 10), "地平线倾斜需校正", font, stroke)

    # 4. 过曝/死黑提示条
    for key, tag in (("overexposure_mask", "过曝区"), ("underexposure_mask", "死黑区")):
        if annotations.get(key) is True:
            _text(draw, (10, h - font_size - 8), tag, font, stroke)

    # 5. 问题标注：白字细黑边，标到对应位置（位置下方一个针脚点）
    for mark in annotations.get("issue_marks", []):
        pos = mark.get("position", [0.5, 0.5])
        if len(pos) != 2:
            continue
        px, py = int(pos[0] * w), int(pos[1] * h)
        r = max(5, font_size // 8)
        draw.ellipse([(px - r, py - r), (px + r, py + r)],
                     fill=WHITE, outline=BLACK, width=max(2, stroke))
        label = mark.get("label") or mark.get("rule_id", "")
        bbox = draw.textbbox((0, 0), label, font=font)
        tw = bbox[2] - bbox[0]
        th = bbox[3] - bbox[1]
        tx = max(0, min(w - tw, int(px - tw / 2)))
        ty = py - r - th - 8
        if ty < 0:  # 顶部放不下则放到点下方
            ty = py + r + 8
        _text(draw, (tx, ty), label, font, stroke)

    im.save(out_path, "JPEG", quality=92)
    print(f"标注图已生成：{out_path} ({w}x{h})")


def main():
    ap = argparse.ArgumentParser(description="PhotoJudge 图像标注")
    ap.add_argument("image", help="原图路径")
    ap.add_argument("--annotations", required=True, help="诊断报告 JSON 路径（取 annotations 字段）")
    ap.add_argument("--output", required=True, help="输出标注图路径")
    args = ap.parse_args()

    with open(args.annotations, encoding="utf-8") as f:
        report = json.load(f)
    ann = report.get("annotations", {})
    draw_annotations(args.image, ann, args.output)


if __name__ == "__main__":
    main()
