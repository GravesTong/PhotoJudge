# 后期建议（Post-processing）打分规则

> 维度前缀：PPC ｜ 条目数：11
> 来源：《摄影六维打分规则依据库》维度六 P1–P11（E:\doubao\摄影\摄影六维打分规则依据库.md）
> 说明：本文件仅搬运依据库已有内容，未新增/改写规则结论；"多来源支撑"按依据库原文保留全部来源 URL。`weight_hint` 未逐条填充——题材权重见 rules/README.md 权重表与依据库③节。`conflicts` 仅在该条目与依据库④节冲突点相关时标注。

## P1. 先裁后调工作流

```yaml
id: PPC-001
rule: 先裁后调——构图歪、地平线斜、多余边幅，第一步裁剪拉直再做影调颜色。
why: 裁剪决定最终画幅和视觉重心；先调色再裁=浪费像素在废区域。
how: 电脑 LR Library/Develop 用 Crop 工具（快捷键 R）拖框+Straighten 工具拉地平线；手机 Edit>Crop/Straighten。三分法对齐地平线；竖幅人像 2:3/3:4，横幅风景 16:9。
source:
  - Adobe LR 通用工作流（通识）：https://learn.adobe.com/lightroom-classic/help/image-tone-color.html ；https://helpx.adobe.com/lightroom/mobile/adjust-light-and-color/correct-lens-distortions.html
evidence: Adobe 通识 → 可作工作流硬规则。
```

## P2. 影调五滑块（Exposure/Contrast/Highlights/Shadows/Whites/Blacks）

```yaml
id: PPC-002
rule: 曝光度控制整体亮度（+1.00≈开大光圈一档）；对比度主要影响中间调；高光只控最亮区域（左压救回死白）；阴影只控最暗区域（右拉提亮暗部）；白色色阶设定"最白点"、黑色色阶设定"最黑点"。
why: 对应直方图不同区段；Highlights 救天空/皮肤亮部溢出，Shadows 救逆光黑脸，Whites/Blacks 定裁切点。
how: 电脑 LR Classic/LR 桌面版 Basic 面板；手机 LR 移动端 Edit>Light。欠曝整体偏暗 Exposure +0.3~+1.0；发灰 Contrast +10~+30；天空过曝 Highlights 左拉 -30~-80；逆光黑脸 Shadows 右拉 +30~+70；画面发飘缺黑位 Blacks 左拉 -10~-30。对应醒图"光感/对比度/高光/阴影/白色/黑色"，VSCO Exposure/Contrast/Highlights/Shadows 同名同义。
source:
  - Adobe《Work with image tone and color》（已查证）：https://learn.adobe.com/lightroom-classic/help/image-tone-color.html
  - Adobe LR 移动端 Adjust light（已查证）：https://helpx.adobe.com/lightroom/mobile/adjust-light-and-color/adjust-light-in-photos.html
evidence: Adobe 已查证 → 硬支撑；醒图/VSCO 对应关系为通识（见 P10）。
```

## P3. Auto Tone 与直方图裁切预览

```yaml
id: PPC-003
rule: 一键 Auto 让 LR 自动分配五滑块，最大化影调跨度并最小化高光/阴影裁切；调五滑块时必须盯直方图两端裁切提示，电脑端 Alt(Opt)+拖滑块可单独查看哪一通道被裁。
why: 算法基于直方图两端裁切情况同时动五滑块；裁切=像素被压成纯黑或纯白、细节永久丢失。
how: 电脑 Basic 面板点 Auto；手机 Light 面板有 Auto 入口；先 Auto 再手动微调。拖 Highlights/Whites 时看右侧白三角，拖 Blacks 时看左侧黑三角；手机端双指长按画面调出直方图（iOS）或开 HDR Mode（Android）。
source:
  - Adobe《Work with image tone and color》（已查证）：https://learn.adobe.com/lightroom-classic/help/image-tone-color.html
  - Adobe LR 移动端 Adjust light（已查证）：https://helpx.adobe.com/lightroom/mobile/adjust-light-and-color/adjust-light-in-photos.html
evidence: Adobe 已查证 → 硬支撑。
```

## P4. Texture/Clarity/Dehaze 质感三件套

```yaml
id: PPC-004
rule: Texture 只增强/减弱中等大小细节（皮肤毛孔、树叶），不改颜色和影调；Clarity 通过增加局部（中间调边缘）对比增加"厚度感"，拉太高会出 halo；Dehaze 右拉穿透雾气增加对比与饱和度，左拉模拟加雾。
why: Texture 作用中尺度纹理不产生光晕；Clarity 作用中间调边缘局部对比；Dehaze 本质是同时压暗中间调并提对比。
how: 电脑/手机均在 Effects 面板。皮肤人像 Texture 左拉 -10~-30 磨皮；花草/羽毛 Texture 右拉 +15~+40；风景/建筑 Clarity 右拉 +15~+40，人像皮肤 Clarity 左拉 -5~-15 或负 Clarity 做柔焦；霾天/雾景 Dehaze 右拉 +10~+35，想要胶片朦胧感左拉 -10~-30。调 Clarity 时放大到 100% 检查 halo。醒图"结构"≈Texture；VSCO 无直接对应（近似 Clarity）。
source:
  - Adobe《Add effects and improve detail》（已查证）：https://www.adobe.com/learn/lightroom-cc/web/apply-clarity-dehaze-sharpen-lightroom-cc
  - Adobe LR 移动端 Adjust effects（已查证）：https://helpx.adobe.com/si/lightroom/mobile/adjust-light-and-color/adjust-effects-in-lightroom-for-mobile.html
  - Adobe LR 桌面 Edit photos using presets（已查证）：https://helpx.adobe.com/sg/lightroom/desktop/edit-photos/edit-photos.html
evidence: Adobe 已查证 → 硬支撑。
```

## P5. 锐化四参数与蒙版

```yaml
id: PPC-005
rule: 锐化数量 Amount 控制边缘加重强度（RAW 默认 40~70，JPEG 20~40）；半径 Radius 控制边缘过渡带宽度（人像 0.8~1.0，建筑/风景 1.2~1.6）；细节 Detail 控制是否连高频纹理一起锐化（皮肤人像 15~30，风光/毛发 50~80）；蒙版 Masking 让锐化只落在真边缘上（人像推荐 70~90）。
why: 锐化是在边缘两侧加亮/暗对比制造"清晰感"；拉太高噪点也会被锐化出来；半径>2 会让物体外轮廓出现白边。
how: 电脑 Detail>Sharpening 展开四参数，按住 Alt 拖 Masking 看白色区域才会被锐化；手机 LR 移动端 Detail 简化版无 Masking，需电脑操作。先点 1:1 放大再拖。
source:
  - Adobe《Adjust details》（已查证）：https://helpx.adobe.com/lightroom-cc/web/edit-photos/apply-effects/adjust-details.html
  - Adobe Learn《Add effects》（已查证）：https://www.adobe.com/learn/lightroom-cc/web/apply-clarity-dehaze-sharpen-lightroom-cc
evidence: Adobe 已查证 → 硬支撑；Masking 仅电脑口径。
conflicts: 见 conflicts.md K8
```

## P6. 明度/颜色降噪

```yaml
id: PPC-006
rule: 明度降噪消除高 ISO 产生的颗粒感；颜色降噪消除高 ISO 产生的彩色噪点（红绿蓝小斑点）。
why: 照片在高 ISO/暗光下出现彩色/灰色颗粒；LR 降噪=模糊低对比区域；彩色噪点比明度噪点更影响观感。
how: 电脑/手机 Detail>Noise Reduction。暗光/高 ISO 照片明度降噪右拉 15~40；夜景/高 ISO 颜色降噪右拉 25~60；彩色噪点明显时优先于明度降噪开；子项 Detail 拉高保纹理、Contrast 拉高保对比。
source:
  - Adobe《Adjust details》（已查证）：https://helpx.adobe.com/lightroom-cc/web/edit-photos/apply-effects/adjust-details.html
evidence: Adobe 已查证 → 硬支撑。
```

## P7. 镜头配置校正与去色差

```yaml
id: PPC-007
rule: 一键启用镜头配置文件校正几何畸变和暗角，基于 EXIF 自动匹配镜头；一键去除高对比边缘的紫边/绿边（蓝黄/红绿色散）；profile 不准时手动 Distortion Correction 和 Lens Vignetting 滑块微调。
why: 广角桶形畸变、长焦枕形畸变、大光圈暗角都是镜头光学特性；镜头色差=不同波长光聚焦点不一致，在树枝对天空、头发对亮背景处出现紫边绿边。
how: 电脑 Develop>Lens Corrections>Enable Profile Corrections + Remove Chromatic Aberration；手机 Edit>Optics 两个开关。所有 RAW 推荐默认开；去不干净用 Defringe/Fringe Selector 点紫边；桶形畸变（直线外鼓）右拉，暗角重右拉提亮边缘。
source:
  - Adobe LR 移动端 Correct lens distortion（已查证）：https://helpx.adobe.com/lightroom/mobile/adjust-light-and-color/correct-lens-distortions.html
  - Adobe《What is chromatic aberration》（已查证）：https://www.adobe.com/nz/creativecloud/photography/discover/chromatic-aberration.html
evidence: Adobe 已查证 → 硬支撑。
conflicts: 见 conflicts.md K7
```

## P8. Tone Curve 参数曲线与点曲线

```yaml
id: PPC-008
rule: 参数曲线分 Highlights/Lights/Darks/Shadows 四段独立控制点，比五滑块更精细；点曲线可分别对 Red/Green/Blue 通道单独拉做胶片色。
why: 横轴=原影调、纵轴=输出影调；S 曲线（高光上拉+暗部下压）=加对比；反 S=柔焦；蓝通道曲线上抬=全图加蓝。
how: 电脑 Develop>Tone Curve 拉四个区域滑块或 Channel 选 Red/Green/Blue 加点；手机 Light>Curve 加点拖动。
source:
  - Adobe《Work with image tone and color》（已查证）：https://learn.adobe.com/lightroom-classic/help/image-tone-color.html
evidence: Adobe 已查证 → 硬支撑。
```

## P9. LR 移动端面板与醒图/VSCO 滑块映射

```yaml
id: PPC-009
rule: LR 移动端 Edit 面板分组=Light/Color/Effects/Detail/Optics，与桌面版 Basic/Color/Effects/Detail/Lens Corrections 一一对应，同名滑块方向也一致；移动版少了 Masking、Curve 分通道、Camera Calibration 等高级项。醒图"调节"与 LR Light 面板基本同名同义（亮度≈Exposure、光感≈中间调提亮、对比度、高光、阴影、白色、黑色、色温、色调、饱和度、自然饱和度、结构≈Texture、锐化）；VSCO 工具条同名（Exposure/Contrast/Highlights/Shadows/Temp/Tint/Saturation）。
why: Adobe 官方设计就是桌面移动互通；手机修图 App 普遍沿用 LR 命名；但醒图"光感"是 LR 没有的中间调提亮项，VSCO Film 预设会在滑块基础上叠加胶片颗粒和色偏。
how: 手机校色流程=Edit>Light（五滑块）→Color（Temp/Tint/Vibrance/Saturation）→Color>Mix（HSL）→Effects（Texture/Clarity/Dehaze）→Detail（Sharpen/Noise）→Optics（Lens 校正）。给新手建议时，手机=醒图/VSCO 同名滑块直接用；电脑=LR 五滑块+HSL+Detail。
source:
  - Adobe LR 移动端四条官方页（已查证 LR 侧）：https://helpx.adobe.com/lightroom/mobile/adjust-light-and-color/adjust-light-in-photos.html ；https://helpx.adobe.com/lightroom/mobile/adjust-light-and-color/adjust-colors.html ；https://helpx.adobe.com/si/lightroom/mobile/adjust-light-and-color/adjust-effects-in-lightroom-for-mobile.html ；https://helpx.adobe.com/lightroom/mobile/adjust-light-and-color/correct-lens-distortions.html
  - 醒图/VSCO 官方文档未检索到，映射为通识/一方称。
evidence: LR 侧 Adobe 已查证；醒图/VSCO 映射为通识 → 双口径成立，但手机侧对应关系强度弱于电脑侧。
```

## P10. PS 色阶/曲线补充口径

```yaml
id: PPC-010
rule: PS 色阶（Levels）=直方图两端三角滑块对齐到有像素处；PS 曲线（Curves）=与 LR Tone Curve 完全同源的输入-输出曲线。
why: 色阶是 LR Whites/Blacks 的手动版；曲线与 LR 点曲线同算法；PS 适合像素级局部处理（人像精修），LR 适合批量全局调。
how: 电脑 PS>图像>调整>色阶/曲线；本引擎"后期建议"维度给出 LR 口径即可，PS 作为电脑端补充口径；手机端无 PS。
source:
  - Adobe Photoshop 帮助（Levels/Curves）未在本次精读范围内 → 通识。
evidence: 通识 → 电脑端补充口径。
```

## P11. 万能调色口诀与题材后期方向

```yaml
id: PPC-011
rule: "色彩淡加饱和，画面暗拉曝光；人像黄降色温，画面灰加对比；不清晰调锐化，要质感颗粒度，要复古加褪色。"扫街后期别一通乱拉饱和对比——色彩淡一点、明暗差距别拉太大、多留柔和灰调、整体稍偏冷。
why: 这是后期检查清单，不是滤镜参数；街头招牌本就五颜六色，调浓烈反而廉价轻浮，统一灰冷调才有故事感。
how: 点评后期时按七项逐条核：饱和度/曝光/色温/对比度/锐化/颗粒/褪色。手机=醒图/VSCO，电脑=LR/ACR/PS 通用。街拍"颜色花哨/廉价"时按灰冷调方向调；色彩实在乱的直接转黑白（Saturation -100）。
source:
  - wuwu 万能调色口诀（一方称）：https://www.iesdouyin.com/share/video/7569154581888896299
  - wuwu 扫街后期（一方称）：https://www.iesdouyin.com/share/video/7654791448855874879
  - Adobe Vibrance/Saturation（已查证）：https://learn.adobe.com/lightroom-classic/help/image-tone-color.html
evidence: Adobe 已查证 + wuwu 一方称 → 多源支撑。
```
