# 对焦与清晰度（Focus & Sharpness）打分规则

> 维度前缀：FOC ｜ 条目数：10
> 来源：《摄影六维打分规则依据库》维度三 F1–F10（E:\doubao\摄影\摄影六维打分规则依据库.md）
> 说明：本文件仅搬运依据库已有内容，未新增/改写规则结论；"多来源支撑"按依据库原文保留全部来源 URL。`weight_hint` 未逐条填充——题材权重见 rules/README.md 权重表与依据库③节。`conflicts` 仅在该条目与依据库④节冲突点相关时标注。

## F1. 景深三要素：光圈/焦距/摄距

```yaml
id: FOC-001
rule: 光圈越小景深越大；焦距越短（广角）景深越大、焦距越长（长焦）景深越浅；相机离被摄体越远景深越大、越靠近越浅。
why: 小孔径下光线锥更窄；广角成像放大率低；近摄时放大率急剧上升，毫米级前后差就走出清晰带。
how: 要背景虚化不仅靠大光圈，用长焦+近距离更明显；要大景深可用广角端；拍特写/微距必须精确对焦。
source:
  - NYIP 光圈越小景深越大（已查证）：https://book.douban.com/subject/1007928/blockquotes （第3课）
  - NYIP 焦距越短景深越大（已查证）：https://book.douban.com/subject/1007928/blockquotes （第3课）；https://m.book118.com/try_down/238130060043006121.pdf
  - NYIP 摄距越远景深越大（已查证）：https://book.douban.com/subject/1007928/blockquotes （第3课）
  - 佳能《焦距/距离/光圈关系》（已查证）：https://m.canon.com.cn/special/canon_portrait/16.html
evidence: NYIP/佳能已查证 → 硬支撑。
```

## F2. 前深后浅不对称：焦点放前景1/3

```yaml
id: FOC-002
rule: 任意光圈下，焦点后方的景深大约是焦点前方景深的 2 倍；拍前后都要清楚的合影/风光时，把对焦点放在前景三分之一深处，而不是正中。
why: 几何光学上弥散圆随距离非线性增长，远景一侧容许范围更大。
how: 别把焦点打在最远的背景上；风光/集体照对前景 1/3 处合焦。
source:
  - NYIP 前景深与后景深不对称（已查证）：https://book.douban.com/subject/1007928/blockquotes （第3课）；https://m.book118.com/try_down/238130060043006121.pdf
evidence: NYIP 已查证 → 硬支撑。
```

## F3. 浅景深防跑焦：极致大光圈缩一档+连拍

```yaml
id: FOC-003
rule: f/1.2/f/1.4/f/1.8 这类极致大光圈直接拍极易跑焦，应在最大光圈基础上缩小一档（f/1.2→f/1.4、f/1.4→f/1.8）；大光圈虚化人像景深极浅，手持必须用连拍多拍几张。
why: 极致大光圈景深只有头发丝厚，手一抖/呼吸就脱焦；细微前后移动就会让眼部脱焦。
how: 眼睛清楚但脸颊/耳朵虚时，建议 f/1.8 收 f/2.8；驱动模式设高速连拍，一组动作连拍 3-5 张再选片。
source:
  - wuwu 跑焦规避（一方称）：https://www.iesdouyin.com/share/video/7613983721556938027
  - 佳能《人像-景深窄需连拍》（已查证）：https://www.canon.com.cn/special/canon_portrait/1.html
evidence: 佳能已查证 + wuwu 一方称 → 多源支撑。
```

## F4. 人像眼部合焦原则

```yaml
id: FOC-004
rule: 人像摄影的合焦原则是对准被摄者眼部；相机会自动检测人脸/眼部并对眼对焦（眼部 AF）。
why: 眼部是人像视觉重心，眼部不实整张人像即失败；浅景深下对焦点差几厘米就脱焦。
how: 用单次对焦+眼部位置对合后锁定再构图；或切 MF 微调；索尼用户 MENU→人脸/眼部 AF→开；佳能用户用单次对焦对眼+眼部检测。
source:
  - 佳能《定焦-眼部合焦原则》（已查证）：https://www.canon.com.cn/special/singlefocal/2-1.html
  - 索尼中国服务《对焦设置-眼部AF》（已查证）：https://service.sony.com.cn/content/casch/Enjoyment/di-basic/03.html
  - 索尼 ILCE-9M3《对焦人眼》（已查证）：http://support.d-imaging.sony.co.jp/support/ilc/autofocus/ilce9m3/zh-hans/12.php
evidence: 佳能/索尼已查证 → 硬支撑。
```

## F5. 单次对焦 vs 连续追焦

```yaml
id: FOC-005
rule: 拍静止主体（静物、风光、摆拍人像）用单次自动对焦（佳能 One-Shot / 索尼 AF-S），半按合焦后锁定；拍运动主体（跑动儿童、宠物、体育）用连续自动对焦（佳能 AI Servo / 索尼 AF-C），半按期间持续追焦；不确定时用索尼 AF-A 自动切换。
why: 静止主体只需要一次合焦；运动主体距离一直在变，单次对焦会在按快门时已经脱焦。
how: AF 模式拨杆切 ONE SHOT/SERVO 或 Fn→AF-S/AF-C；伺服模式没有合焦提示音，对焦点变蓝即代表在追踪。
source:
  - 佳能支持页《自动对焦操作》（已查证）：https://www.canon.com.cn/supports/download/simsdetail/8201702600.html
  - 佳能 R5 Mark II AF 设置指南（已查证）：https://cam.start.canon/zh/C017/guide/html/AF-04_Action_0060.html
  - 索尼中国服务《对焦设置》（已查证）：https://service.sony.com.cn/content/casch/Enjoyment/di-basic/03.html
  - 索尼 ILCE-7CM2 教程（已查证）：https://support.d-imaging.sony.co.jp/support/tutorial/ilc/ilce-7cm2/zh-hans/07.php
evidence: 佳能/索尼已查证 → 硬支撑；两家命名差异见冲突节 K3。
conflicts: 见 conflicts.md K3
```

## F6. 对焦区域分工与 Tracking 追踪

```yaml
id: FOC-006
rule: 广域=风景/建筑等大场景；区域/区=运动抓拍；中间对焦=肖像；自由点=很小的被摄体；拍轨迹不规则的运动主体（儿童、宠物、飞鸟）用"跟踪（Tracking）"+AF-C，把对焦框先放到主体上再半按。
why: 对焦范围越大越省事但精度越低；范围越小越精准但构图容错小；Tracking 让框跟着主体走。
how: 拍景用广域、拍单人肖像切中间或自由点、拍动体用区域+Tracking；拍人时不要全程挂广域。
source:
  - 索尼中国服务《对焦区域四档》（已查证）：https://service.sony.com.cn/content/casch/Enjoyment/di-basic/03.html
  - 索尼 ZV-1 教程《跟踪不规则移动》（已查证）：https://support.d-imaging.sony.co.jp/support/tutorial/dc/zv-1/zh-Hans/02.php
evidence: 索尼已查证 → 硬支撑（仅索尼侧，佳能对应区域命名未采集）。
```

## F7. DMF/MF 手动兜底+峰值放大

```yaml
id: FOC-007
rule: AF 困难的场合（微距、低反差）用 DMF（AF 后手动微调）或纯 MF；MF 时开峰值显示+自动放大辅助。
why: 自动对焦对低反差/极近主体会拉风箱；峰值+放大让人眼直接判断合焦位置。
how: 对焦模式切 DMF/MF；MENU→对焦→峰值显示→开（选颜色+等级）；MENU→MF 自动放大→开。
source:
  - 索尼中国服务《DMF/MF》（已查证）：https://service.sony.com.cn/content/casch/Enjoyment/di-basic/03.html
evidence: 索尼已查证 → 硬支撑。
```

## F8. 后键对焦 AF-ON

```yaml
id: FOC-008
rule: 把 AF-ON 键设为"测光+AF-C 连续对焦+眼睛检测+高速连拍"；拍静止物按快门即可，抓拍移动主体时长按 AF-ON 锁定人脸跟焦，松开回单次。
why: 半按快门同时对焦+测光在快速抓拍时容易对不上、被前景路人干扰；后键把对焦和测光解绑。
how: 抓拍小孩/宠物总跑焦时建议设后键对焦+AF-C+眼睛检测。
source:
  - wuwu AF-ON（一方称）：https://www.iesdouyin.com/share/video/7636344181635534122
evidence: 仅 wuwu 一方称 → 薄弱，但为进阶用户通识。
```

## F9. 对焦包围/景深合成

```yaml
id: FOC-009
rule: 暗光大光圈（f/1.8/f/2.8）景深只有一小块清楚时，开机内对焦包围：固定光圈、设对焦增量、设张数、开曝光平滑+深度合成，焦点对物体最低点按一次快门，相机会拍多张不同焦平面后期合成前后都清晰。
why: 微距/近物/暗光人像景深太薄，靠收光圈会衍射掉画质。
how: 前后只清楚一小块时，微距/产品类建议用对焦包围；普通人像不需要，建议收 f/2.8。
source:
  - wuwu 对焦包围（一方称）：https://www.iesdouyin.com/share/video/7678549220525214985 ；https://www.iesdouyin.com/share/video/7681517595777977627
evidence: 仅 wuwu 一方称 → 薄弱。
```

## F10. 用景深叙事：浅景深隔离主体

```yaml
id: FOC-010
rule: 景深不是技术指标而是叙事工具——浅景深把观众从杂乱背景"拉"回主体，深景深让环境一起交代主题；背景乱时开大光圈虚化，环境人像想交代场景时收小光圈让背景也可辨。
why: 人眼优先注意清晰区域；虚化背景等于在画面里做"减法"。
how: 背景乱时优先建议换长焦端或开大光圈，而非指望后期 P 掉；环境人像想交代场景时收小光圈让背景也可辨。
source:
  - NYIP 用景深突出/隔离主体（已查证）：https://book.douban.com/subject/1007928/blockquotes （第118页）
  - wuwu 去杂乱（一方称）：https://www.iesdouyin.com/share/video/7681248699423476465 ；https://www.iesdouyin.com/share/video/7657475752950025522
  - 佳能《人像-大光圈长焦虚化》（已查证）：https://www.canon.com.cn/special/canon_portrait/1.html
evidence: NYIP/佳能已查证 + wuwu 一方称 → 多源支撑。
```
