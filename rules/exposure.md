# 曝光（Exposure）打分规则

> 维度前缀：EXP ｜ 条目数：14
> 来源：《摄影六维打分规则依据库》维度二 E1–E14（E:\doubao\摄影\摄影六维打分规则依据库.md）
> 说明：本文件仅搬运依据库已有内容，未新增/改写规则结论；"多来源支撑"按依据库原文保留全部来源 URL。`weight_hint` 未逐条填充——题材权重见 rules/README.md 权重表与依据库③节。`conflicts` 仅在该条目与依据库④节冲突点相关时标注。

## E1. 曝光三要素分工与此消彼长

```yaml
id: EXP-001
rule: 光圈 F 数值越小越大（进光多、背景虚）；快门越快定格瞬间、越慢留运动轨迹；ISO 越高越亮但噪点越多。固定曝光量下，动一个必须补另一个。
why: 到达传感器的总光量=孔径×时间×灵敏度；三者是一个守恒系统。
how: 背景虚不掉→光圈开大（数值调小）；运动糊→快门加快；夜拍黑→先开大光圈+慢快门，最后才提 ISO。
source:
  - wuwu 曝光三要素（一方称）：https://www.iesdouyin.com/share/video/7613983721556938027 ；https://www.iesdouyin.com/share/video/7543083922037493030
  - NYIP 曝光三要素此消彼长（通识）：https://www.ithome.com/0/908/478.htm ；https://book.douban.com/subject/1007928/blockquotes
evidence: NYIP 通识 + wuwu 一方称 → 基础常识，可作硬规则。
```

## E2. 光圈参考值：人像大光圈 vs 风光小光圈

```yaml
id: EXP-002
rule: 人像虚化用 f/1.8~f/4 左右；人文纪实用 f/5.6；风光/建筑/产品要全局清晰用 f/8~f/11（保底 f/8），不要盲目收到 f/22/f/32。
why: 收到极限小光圈会产生镜头吃光/衍射，画质反而下滑；f/8 左右是大多数镜头锐度最佳区间。
how: 脸清晰但背景还清楚→光圈再开大一档；风光全糊/边角发软→检查是否误收 f/22，回到 f/8~f/11；长曝流水才用 f/16~f/22。
source:
  - wuwu 光圈参考值（一方称）：https://www.iesdouyin.com/share/video/7613983721556938027 ；https://www.iesdouyin.com/share/video/7654921655570943278
  - NYIP 光圈越小景深越大（已查证）：https://book.douban.com/subject/1007928/blockquotes （第3课）
  - 佳能《入门篇04》风光 F8（已查证）：https://m.canon.com.cn/special/ds_abcbook/beginner04.html
  - 索尼《拍摄活力风景照》A模式 F8（已查证）：https://www.sony.com/zh-cn/electronics/support/e-mount-body-ilce-7-series/ilce-7m4/articles/00199911
  - 索尼香港 CURATORS 专业风景 F7.1–F11（已查证）：https://www.sony.com.hk/campaigns/landscape/
evidence: 佳能/索尼/NYIP 已查证 + wuwu 一方称 → 多源硬支撑；但佳能长曝 f/22 与 wuwu"别盲目 f/22"存在场景差异（见冲突节 K1）。
conflicts: 见 conflicts.md K1
```

## E3. 安全快门与防抖

```yaml
id: EXP-003
rule: 手持快门不低于镜头焦距倒数（50mm≥1/50s）；NYIP 推荐更严格的两倍倒数（100mm≥1/200s）；夜景点光源下要再快一级。
why: 手抖在长焦端被放大；低于临界速度，机震会让整张照片虚；IS 镜头防抖只补手抖、不补被摄体动。
how: 开防抖、靠墙、肘贴身体；长焦端务必把快门提到 1/(2×焦距)以上；达不到就升 ISO 或开大光圈，不要指望 IS 定格走动的人。
source:
  - wuwu 慢门稳定（一方称）：https://www.iesdouyin.com/share/video/7591417639923174699 ；https://www.iesdouyin.com/share/video/7677416789143211283
  - NYIP 手持快门速度底线（已查证）：https://book.douban.com/subject/1007928/blockquotes （第50页）
  - 佳能《夜景手持抓拍》安全快门（已查证）：https://www.canon.com.cn/special/nightscape/1_1.html
  - 佳能《防抖的条件》（已查证）：https://www.canon.com.cn/special/singlefocal/1-2.html
evidence: NYIP/佳能已查证 + wuwu 一方称 → 多源支撑；但 NYIP 两倍倒数与 wuwu/佳能一倍倒数存在口径差异（见冲突节 K2）。
conflicts: 见 conflicts.md K2
```

## E4. 快门速度凝固动态

```yaml
id: EXP-004
rule: 凝固运动所需快门取决于物体速度、运动方向、相机距离、焦距四因素；横跑的人用 1/500s 以上，迎面走来可放慢。
why: 物体越快、越横向横穿、离得越近、焦距越长，成像位移越大，需要越快的快门。
how: 人物/动物发虚时先看快门；抓拍动态提到 1/500 以上；飞鸟 1/2000、跑跳小孩 1/500、行人纪实 1/200。
source:
  - wuwu 快门参考值（一方称）：https://www.iesdouyin.com/share/video/7593633343787453738 ；https://www.iesdouyin.com/share/video/7632469418425124250
  - NYIP 快门速度选择四因素（已查证）：https://book.douban.com/subject/1007928/blockquotes （3.16）
evidence: NYIP 已查证 + wuwu 一方称 → 多源支撑。
```

## E5. 测光模式分工

```yaml
id: EXP-005
rule: 日常/平光用矩阵（评价/多重）测光；半身人像用中央重点保肤色；逆光/剪影/大光比用点测光，点在人脸或高光背景上，测完锁曝光。
why: 矩阵在大光比下会强行折中导致发灰；点测光保证局部准确。
how: 逆光人脸发黑却背景亮时切点测光对人脸；日常发灰时检查是否误用点测。
source:
  - wuwu 测光三档（一方称）：https://www.iesdouyin.com/share/video/7649686062482099510
  - 索尼帮助指南《测光模式》（已查证）：https://helpguide.sony.net/ilc/1420/v1/zh-tw/print.html ；https://www.sony.com/electronics/support/res/manuals/4408/44086889M.pdf
  - NYIP 从最重要影调测光（已查证）：https://book.douban.com/subject/1007928/blockquotes （第5课）
evidence: 索尼/NYIP 已查证 + wuwu 一方称 → 多源支撑。
```

## E6. 18%灰原理与白加黑减

```yaml
id: EXP-006
rule: 反射式测光表默认把一切还原成 18% 中灰；拍雪/白墙/白婚纱要加曝光补偿 +1~+1.5（甚至+2），拍黑猫/黑衣/夜景暗部要减 -1~-1.5。
why: 不加白场景会拍成灰雪，不减黑场景会拍成灰黑。
how: 雪景发灰/黑衣服发灰时直接给 +1.5 / -1.5 档补偿建议，而非后期拉；无法靠近主体时用灰板/手背替代测光。
source:
  - NYIP《Gray Cards》（已查证）：https://www.nyip.edu/photo-articles/cameras-and-gear/incident-and-gray-card-readings
  - NYIP 替代测光/灰板法（已查证）：https://book.douban.com/subject/1007928/blockquotes （第5课）
  - wuwu 白加黑减（一方称）：https://www.iesdouyin.com/share/video/7687186805476707603
evidence: NYIP 已查证 + wuwu 一方称 → 多源硬支撑。
```

## E7. 直方图判曝光与裁切预览

```yaml
id: EXP-007
rule: 直方图横轴左=暗部、中=灰部、右=亮部；山峰贴最左=暗部细节丢（加曝光），贴最右=亮部过曝（减曝光）；别信屏幕亮度，信直方图。
why: 屏幕调亮调暗会误导肉眼；直方图客观记录 0-255 级亮度；裁切=像素被压成纯黑或纯白、细节永久丢失。
how: 过曝/欠曝时拍后按 INFO/DISP 看直方图；高调片允许右侧亮部过曝但主体（人脸）不能撞墙；电脑端 Alt(Opt)+拖滑块可单独查看哪一通道被裁。
source:
  - wuwu 直方图（一方称）：https://www.iesdouyin.com/share/video/7679633335630482722
  - Adobe《Work with image tone and color》裁切预览（已查证）：https://learn.adobe.com/lightroom-classic/help/image-tone-color.html
  - Adobe LR 移动端 Adjust light（已查证）：https://helpx.adobe.com/lightroom/mobile/adjust-light-and-color/adjust-light-in-photos.html
evidence: Adobe 已查证 + wuwu 一方称 → 多源支撑。
```

## E8. 高调/低调影调曝光

```yaml
id: EXP-008
rule: 拍高调（亮场景+主体亮）曝光补偿 +1.5~+2，主体/人脸不能过曝；拍低调（暗场景+主体亮或灰）曝光补偿 -1~-1.5，该黑就黑。
why: 影调由明暗占比决定，不是后期拉出来的；前期曝光故意偏离 0 档。
how: 想清新却灰蒙蒙→前期加 +2；想情绪却灰不溜秋→前期压 -1.5 并让暗部焦死。
source:
  - wuwu 影调曝光（一方称）：https://www.iesdouyin.com/share/video/7670819564439047451 ；https://www.iesdouyin.com/share/video/7688966742340586778
evidence: 仅 wuwu 一方称 → 薄弱。
```

## E9. 高反差场景应对（包围曝光/补光）

```yaml
id: EXP-009
rule: 场景光比超过约 7 档（亮部比暗部亮 128 倍），任何单一曝光都无法同时保住两端；对策是补光缩光比、按高光测光保亮部暗部交后期、或包围曝光拍多张合成。
why: 传感器动态范围有限；强行直出必丢一端细节。
how: 天空过曝白云死白、地面死黑时，建议包围曝光拍 3 张后期 LR/PS 合成，而非单张硬拉；人像可用补光，风光只能靠合成或渐变镜。
source:
  - NYIP 高反差场景曝光处理（已查证）：https://book.douban.com/subject/1007928/blockquotes （第5课）
  - wuwu 曝光合成（一方称）：https://www.iesdouyin.com/share/video/7455951699698535714
evidence: NYIP 已查证 + wuwu 一方称 → 多源支撑。
```

## E10. 追随拍摄摇拍

```yaml
id: EXP-010
rule: 用较慢快门（1/20~1/50s）+跟随运动物体同步转动相机，可让主体相对清晰、背景拉出运动模糊线；对焦模式选 AF-C。
why: 相对运动为零时成像清晰；背景与相机有相对运动所以被拖虚，反而强化速度感。
how: 运动片全糊时区分——定格不了=快门太慢；想要动感拉丝=改用摇拍参数；按下快门后继续平滑跟随一段，不要拍完立刻停。
source:
  - wuwu 摇拍/追焦（一方称）：https://www.iesdouyin.com/share/video/7612202795986341126 ；https://www.iesdouyin.com/share/video/7628083527187238163
  - NYIP 追随拍摄摇拍（已查证）：https://book.douban.com/subject/1007928/blockquotes （3.16）
evidence: NYIP 已查证 + wuwu 一方称 → 多源支撑。
```

## E11. 逆光补光与反光板

```yaml
id: EXP-011
rule: 逆光光比大时，M 档+点测高光背景锁死参数不动，人物暗部用反光板控制（板举高模特头顶约 45° 斜往下反弹）；室外人像原则上用逆光或侧光，避免顺光在脸上留硬阴影。
why: 先对人脸测光会导致背景过曝；不改变主光方向就能缩小面部光比，保住暗部眼神和皮肤层次。
how: 逆光脸黑成剪影时要求反光板斜上方补；脸比背景还亮是补过了，板退远；没有反光板可用白墙、白色 T 恤代替。
source:
  - wuwu 逆光补光（一方称）：https://www.iesdouyin.com/share/video/7660766139529645312 ；https://www.iesdouyin.com/share/video/7668627357791538451
  - NYIP 反光板补阴影（已查证）：https://book.douban.com/annotation/151016907/ （9.9）
  - 佳能《人像专业技巧-场景1》逆光侧光（已查证）：https://www.canon.com.cn/special/canon_portrait/1.html
evidence: NYIP/佳能已查证 + wuwu 一方称 → 多源支撑。
```

## E12. 长曝流水与三脚架夜景

```yaml
id: EXP-012
rule: 拍瀑布/溪流丝绢效果用镜头最小光圈（f/16~f/22）+固定最低 ISO 100，逼出数秒慢门；上三脚架拍夜景时光圈收 f/8 左右发挥镜头分辨力，ISO 以 100 为基准。
why: 机震被三脚架消除后，慢门不再是问题；低 ISO 换干净画面才是重点。
how: Av 模式→f/16~f/22，ISO 锁 100（需在 C.Fn 里关掉"高光色调优先"才能选到 ISO 100）；上三脚架+快门线或 2 秒延时释放。
source:
  - 佳能《不同典型光圈值-F22和低感光度》（已查证）：https://www.canon.com.cn/special/shootingmode/2-7.html
  - 佳能《夜景-岸边绚丽灯光》三脚架 F8+ISO100（已查证）：https://m.canon.com.cn/special/nightscape/2_1.html
  - 索尼 UK《Shooting Sunrise》小光圈+三脚架（已查证）：https://www.sony.co.uk/alphauniverse/alpha-academy/articles/top-tips-shooting-sunrise
evidence: 佳能/索尼已查证 → 硬支撑；与 wuwu E2"别盲目 f/22"的差异见冲突节 K1。
conflicts: 见 conflicts.md K1
```

## E13. 手持夜景升 ISO 换快门

```yaml
id: EXP-013
rule: 手持夜景时不断提高 ISO，直到快门速度达到安全值（示例 ISO1600 换得 1/30s）；昏暗室内/夜景人像用大光圈定焦（f/1.4~f/2）手持换 1/30s 以上快门。
why: 手持状态下手抖是第一矛盾，宁可接受高 ISO 噪点也不能糊片；大光圈镜头仅凭少量光线就能得到 1/30 秒。
how: P 或 Av 模式下手动设 ISO 上限（如 3200），快门低于 1/焦距即继续升 ISO；暗光环境换 f/1.4~f/2 定焦，避免用狗头套机端最大 f/5.6 硬拍。
source:
  - 佳能《手持夜景升ISO》（已查证）：https://www.canon.com.cn/special/nightscape/1_1.html
  - 佳能《定焦-昏暗场所抓拍》（已查证）：https://www.canon.com.cn/special/singlefocal/2-2.html
evidence: 佳能已查证 → 硬支撑。
```

## E14. 星空参数（500法则）

```yaml
id: EXP-014
rule: 14-35mm 广角、f/2.8 起步；快门按 500÷焦距（20mm≈25s，超了星星脱尾）；ISO 1600-6400 以 3200 为基础；色温手动 4000K、拍 RAW、MF 拧无穷远、2 秒延时。
why: 星空要最大进光+最长不脱尾曝光；宁可轻微欠曝不可过曝（过曝星星细节拉不回）。
how: 星星拖成线→快门超了 500 法则；星星糊成一团→MF 没拧准无穷远。
source:
  - wuwu 星空（一方称）：https://www.iesdouyin.com/share/video/7677416789143211283
evidence: 仅 wuwu 一方称 → 薄弱，但 500 法则为天文摄影通识。
```
