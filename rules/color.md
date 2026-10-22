# 色彩与白平衡（Color & White Balance）打分规则

> 维度前缀：COL ｜ 条目数：10
> 来源：《摄影六维打分规则依据库》维度四 X1–X10（E:\doubao\摄影\摄影六维打分规则依据库.md）
> 说明：本文件仅搬运依据库已有内容，未新增/改写规则结论；"多来源支撑"按依据库原文保留全部来源 URL。`weight_hint` 未逐条填充——题材权重见 rules/README.md 权重表与依据库③节。`conflicts` 仅在该条目与依据库④节冲突点相关时标注。

## X1. 白平衡 K 值原理与 Temp 滑块

```yaml
id: COL-001
rule: 相机 K 值高（7000-9000K）画面偏暖、低（3000K）偏冷；而光线色温相反（蜡烛 2000K 暖、阴天 7000K 冷）。相机 K=光线 K 时白色还原成白；相机 K>光线 K 画面偏暖，相机 K<光线 K 画面偏冷。
why: 白平衡本质是"补"环境色；环境偏暖（钨丝灯）相机也设暖 K 才能中和。
how: 人脸发黄（钨丝灯/黄昏）把相机 K 调到与环境一致（≈3000K）中和；后期电脑 LR Basic 面板 Temp 滑块左拉变冷（加蓝）、右拉变暖（加黄），手机 Color>Custom>Temp。室内白炽灯下偏黄→左拉；阴天/阴影下偏蓝→右拉。醒图"色温"同名；VSCO 有 Kelvin/WB。
source:
  - wuwu 白平衡 K 值（一方称）：https://www.iesdouyin.com/share/video/7611868236681923878 ；https://www.iesdouyin.com/share/video/7633749416767180086
  - Adobe《Work with image tone and color》Temp（已查证）：https://learn.adobe.com/lightroom-classic/help/image-tone-color.html
  - Adobe LR 移动端 Adjust colors（已查证）：https://helpx.adobe.com/lightroom/mobile/adjust-light-and-color/adjust-colors.html
evidence: Adobe 已查证 + wuwu 一方称 → 多源支撑。
```

## X2. 保留现场氛围色：别用 AWB

```yaml
id: COL-002
rule: 环境≈3000K 的日出/黄昏，若相机也设 3000K 会被 AWB 还原成中性白、丢掉暖调；要保留暖色须相机 K 高于环境（设 4000-5000K）；拍夜景氛围时把白平衡从自动切到"日光"，让画面保留暖黄灯光调。
why: AWB 自动抹平氛围色；手动 K 才能把"现场感动"留住。
how: 日落拍出来惨白/偏蓝时，建议前期 K 手动设 5000-7000 而非 AWB；夜景白平衡→日光档（约 5200K），不要后期再拉暖；如要冷调都市感则改用荧光灯/白炽灯档。
source:
  - wuwu 日出暖色保留（一方称）：https://www.iesdouyin.com/share/video/7611868236681923878 ；https://www.iesdouyin.com/share/video/7681576051171986723
  - 佳能《黄昏-F8+日光白平衡》（已查证）：https://www.canon.com.cn/special/shootingmode/2-4.html
  - 佳能《夜景-日光白平衡造氛围》（已查证）：https://www.canon.com.cn/special/nightscape/1_1.html
  - 索尼香港 CURATORS 日落色温 5000-6000K（已查证）：https://www.sony.com.hk/campaigns/landscape/
evidence: 佳能/索尼已查证 + wuwu 一方称 → 多源硬支撑。
```

## X3. Tint 绿品红轴与白平衡偏移

```yaml
id: COL-003
rule: 色温只解决蓝-黄轴；绿-品红轴由灯管混合光、阴影漫反射造成，必须 Tint 单独修——左拉加绿、右拉加品红。机内白平衡偏移小光标：上=G 绿、右=A 红、下=M 洋红、左=B 蓝；斜向叠加出 8 色风格。
why: 色温只能控冷暖大方向，偏移才能在不偏色的基础上做风格化"色彩升华"。
how: 照片发绿（树荫下、荧光灯下）→右拉加品红；发紫→左拉加绿。想要日系小清新往左上偏+略降色温；港风往右上偏；复古怀旧往右下偏。电脑 LR Basic 面板 Tint；手机 Color>Custom>Tint。
source:
  - wuwu 白平衡偏移（一方称）：https://www.iesdouyin.com/share/video/7644498734198074533 ；https://www.iesdouyin.com/share/video/7611868236681923878
  - Adobe《Work with image tone and color》Tint（已查证）：https://learn.adobe.com/lightroom-classic/help/image-tone-color.html
  - Adobe LR 移动端 Adjust colors（已查证）：https://helpx.adobe.com/lightroom/mobile/adjust-light-and-color/adjust-colors.html
evidence: Adobe 已查证 + wuwu 一方称 → 多源支撑。
```

## X4. 白平衡吸管/中性灰点

```yaml
id: COL-004
rule: 用白平衡吸管点画面中"应该是中性灰/白/黑"的区域，LR 自动把该点校成中性色，其余颜色联动校正。
why: 以已知中性灰为锚点反推整体偏色；选对灰点=一键校色。
how: 电脑 Basic 面板点吸管图标再点灰墙/白衬衫/灰路面；手机 Color 面板点 White balance selector 图标，拖动圆圈到中性灰区域后 Done。
source:
  - Adobe《How to remove color casts》（已查证）：https://helpx.adobe.com/ae_en/lightroom-cc/how-to/remove-color-cast.html
  - Adobe LR 移动端 Adjust colors（已查证）：https://helpx.adobe.com/lightroom/mobile/adjust-light-and-color/adjust-colors.html
evidence: Adobe 已查证 → 硬支撑。
```

## X5. 机内色彩预设：照片风格 vs 创意风格

```yaml
id: COL-005
rule: 佳能"照片风格 Picture Style"：人像=平滑肤色+锐度稍低+色调略偏红；风光=鲜艳蓝绿+高锐度高对比。索尼"创意风格 Creative Style"（新机型叫 Creative Look）：Standard/Vivid/Landscape；Vivid 档自动加饱和加对比适合花卉春色，Landscape 档可再把饱和度、对比度各+2。
why: 两种场景对肤色和天草色的需求相反，厂商预设已内置对应曲线；自动档无法做到。
how: 佳能 MENU→照片风格→人像/风光；索尼 MENU→Creative Style→Landscape/Vivid；拍小清新/人像时切回 Standard 或 Portrait 档避免肤色过饱和；官方警告过饱和会像油画。
source:
  - 佳能 R3 说明书《照片风格选择》（已查证）：https://cam.start.canon/zh/C010/manual/html/UG-03_Shooting-1_0180.html
  - 佳能《人像专业技巧-照片风格设为人像》（已查证）：https://www.canon.com.cn/special/canon_portrait/1.html
  - 索尼《拍摄活力风景照》Creative Style Landscape（已查证）：https://www.sony.com/zh-cn/electronics/support/e-mount-body-ilce-7-series/ilce-7m4/articles/00199911
  - 索尼帮助指南《创意风格-Vivid》（已查证）：http://support.d-imaging.sony.co.jp/wi-fi/dsc/2013-3/4530335111/cs/contents/TP0000244319.html ；https://www.sonystyle.com.cn/minisite/cross/video/4k/level1_2.htm
evidence: 佳能/索尼已查证 → 硬支撑；两家命名差异见冲突节 K4。
conflicts: 见 conflicts.md K4
```

## X6. 先影调后色调

```yaml
id: COL-006
rule: 影调=高光/阴影/中间调三大面的明暗结构；调色第一步永远先调光（曝光/对比度/高光/阴影/白色/黑色），影调稳了再动颜色；照片灰不是颜色差，是高光发灰没层次、阴影闷成一团。
why: 影调是骨架、色调是灵魂；PS 里把饱和度拉到零看到的黑白灰层次就是影调。
how: 片灰/不通透时先别拉饱和度，先压高光、提阴影、加对比；硬调=反差大（街拍/时尚），软调=压高光提阴影（日系治愈）。
source:
  - wuwu 先影调后色调（一方称）：https://www.iesdouyin.com/share/video/7637033888895831350
  - Adobe 影调五滑块工作流（已查证）：https://learn.adobe.com/lightroom-classic/help/image-tone-color.html
evidence: Adobe 已查证 + wuwu 一方称 → 多源支撑。
```

## X7. Vibrance vs Saturation

```yaml
id: COL-007
rule: 自然饱和度 Vibrance 只增强已经偏淡的颜色，对高饱和色和肤色保护，不会过饱和；饱和度 Saturation 对所有颜色一视同仁地增减，范围 -100（黑白）到 +100（翻倍）。
why: LR 智能算法：低饱和颜色多提、高饱和颜色少提；肤色被识别为受保护区间。+50 后所有颜色等比例变艳，肤色也会橙红，易脏。
how: 照片寡淡时 Vibrance 右拉 +15~+40；人像推荐用 Vibrance 而非 Saturation；做黑白片直接 Saturation 拉 -100；正常调色建议 Saturation ±20 以内。手机=醒图"自然饱和度"/VSCO Saturation（近似但不智能保护肤色）；电脑=LR Color>Vibrance/Saturation。
source:
  - Adobe Vibrance（已查证）：https://learn.adobe.com/lightroom-classic/help/image-tone-color.html ；https://helpx.adobe.com/lightroom/mobile/adjust-light-and-color/adjust-colors.html
  - wuwu 饱和度按题材分（一方称）：https://www.iesdouyin.com/share/video/7618882836954664233
evidence: Adobe 已查证 + wuwu 一方称 → 多源支撑。
```

## X8. HSL 分色调整

```yaml
id: COL-008
rule: HSL 把颜色分红/橙/黄/绿/浅绿/蓝/紫/品红 8 个区间，每个区间独立偏移色相 Hue、调饱和度 Saturation、压明亮度 Luminance，只动该颜色系。
why: 例如红色物体太抢戏，只压 Red 饱和度；与全局 Saturation 区别在于选择性。
how: 天空太蓝→蓝通道 Hue 右拉偏青；肤色太黄→橙 Hue 左拉偏红；大红唇太艳→红 -20；天空太亮→蓝 Luminance -20~-40；脸偏黑→橙 +10~+20。电脑 HSL>Hue/Saturation/Luminance；手机 Color>Mix>选色>对应项。可用 Targeted Adjustment（TAT）直接在画面上拖。
source:
  - Adobe HSL（已查证）：https://learn.adobe.com/lightroom-classic/help/image-tone-color.html ；https://helpx.adobe.com/lightroom/mobile/adjust-light-and-color/adjust-colors.html
evidence: Adobe 已查证 → 硬支撑。
```

## X9. 颜色分级与分通道曲线做胶片色

```yaml
id: COL-009
rule: Color Grading 分别给 Shadows/Midtones/Highlights 三个影调区上色轮，做胶片色/青橙色调；点曲线可分别对 Red/Green/Blue 通道单独拉，做暗部偏蓝等色调映射。
why: 分离色调=阴影染一色、高光染另一色；蓝通道曲线上抬=全图加蓝；暗部点上抬=阴影偏蓝（典型胶片 teal-orange）。
how: 公式：阴影往青/蓝、高光往暖橙=teal-orange；Blending 右拉柔化，Balance>0 偏高光。"阴影加蓝、高光加暖"=胶片感公式。电脑 Develop>Color Grading 三色轮/Tone Curve>Channel；手机 Color>Grading/Curve。
source:
  - Adobe Color Grading（已查证）：https://learn.adobe.com/lightroom-classic/help/image-tone-color.html ；https://helpx.adobe.com/lightroom/mobile/adjust-light-and-color/adjust-colors.html
  - wuwu 白平衡偏移风格化（一方称）：https://www.iesdouyin.com/share/video/7644498734198074533
evidence: Adobe 已查证 + wuwu 一方称 → 多源支撑。
```

## X10. 阴影残留色偏单独修

```yaml
id: COL-010
rule: 调完 Temp/Tint 后阴影区仍泛绿或品红时，用 Camera Calibration 面板的 Shadows Tint 单独修阴影色偏。
why: 整体 WB 解决中间调，阴影处的色偏由镜头滤镜/传感器响应曲线造成，需要单独通道。
how: 电脑 LR Classic Develop>Camera Calibration>Shadows Tint；手机端无此面板，需导出到电脑修。
source:
  - Adobe《Work with image tone and color》Camera Calibration（已查证）：https://learn.adobe.com/lightroom-classic/help/image-tone-color.html
evidence: Adobe 已查证 → 硬支撑（手机端无对应口径，注明）。
```
