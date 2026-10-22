# conflicts.md — 来源间口径差异与收敛结论

> 状态：**已收敛**（7 处，K1–K5、K7–K8）。
> 原 K6（醒图/VSCO 与 LR 滑块映射为通识）已删除并并入规则 `PPC-009`（见该条目 source/evidence），故不再单列。
> 以下口径不一致处已按各自性质收敛为明确引用规则，不再标注"待确认"：**条件分支**（按场景/设备走不同区间）· **命名并存**（同时输出两家叫法）· **设备边界**（注明厂商行为或设备能力差异）。
> 来源：《摄影六维打分规则依据库》④节（E:\doubao\摄影\摄影六维打分规则依据库.md），原文内容保留，仅收敛状态。

## K1. 风光小光圈：佳能 f/8 vs wuwu"别盲目 f/22" vs 索尼 f/7.1–f/11

- **佳能口径**：风光要鲜锐收 f/8 左右（https://m.canon.com.cn/special/ds_abcbook/beginner04.html）；长曝流水用最小光圈 f/22+ISO100（https://www.canon.com.cn/special/shootingmode/2-7.html）。
- **索尼口径**：A 模式 F8 左右（https://www.sony.com/zh-cn/electronics/support/e-mount-body-ilce-7-series/ilce-7m4/articles/00199911）；专业风景教学 M 模式 F7.1–F11（https://www.sony.com.hk/campaigns/landscape/）。
- **wuwu 口径**：风光 f/11-f/13（保底 f/8），不要盲目收到 f/22/f/32，会产生衍射画质下滑（https://www.iesdouyin.com/share/video/7613983721556938027 ）。
- **收敛结论**：区分场景——"常规风光全清晰"用 f/8~f/11；"长曝流水拉丝"才用 f/16~f/22（故意逼慢门，牺牲画质换动态模糊）。引擎引用时按照片场景走分支，两条口径都保留。

**状态：已确认（条件分支）。**

## K2. 手持安全快门：NYIP 两倍焦距倒数 vs wuwu/佳能一倍焦距倒数

- **NYIP 口径**：手持快门不应慢于焦距毫米数两倍的倒数（如 100mm 不慢于 1/200s）（https://book.douban.com/subject/1007928/blockquotes 第50页）。
- **wuwu/佳能口径**：手持快门不低于镜头焦距倒数（50mm≥1/50s）；夜景点光源下再快一级（https://www.iesdouyin.com/share/video/7591417639923174699 ；https://www.canon.com.cn/special/nightscape/1_1.html）。
- **收敛结论**：分设备给区间——无防抖长焦按 NYIP 两倍倒数（保守）；带 IS 防抖镜头按 wuwu/佳能一倍倒数 + 夜景再快一级。引擎引用时按镜头有无防抖走分支。

**状态：已确认（条件分支）。**

## K3. 静止/运动对焦命名：佳能 One-Shot/AI Servo vs 索尼 AF-S/AF-C/AF-A

- **佳能口径**：One-Shot（静止）/AI Servo（运动）（https://www.canon.com.cn/supports/download/simsdetail/8201702600.html）。
- **索尼口径**：AF-S（静止）/AF-C（运动）/AF-A（自动切换）（https://service.sony.com.cn/content/casch/Enjoyment/di-basic/03.html）。
- **收敛结论**：功能等价但命名不同——佳能无 AF-A 自动档；索尼眼部 AF 是独立菜单开关，佳能眼部检测集成在 One-Shot/Servo 中。引擎输出"怎么改"时**同时给两家命名**，用户按机型取用。

**状态：已确认（命名并存）。**

## K4. 机内色彩预设名：佳能"照片风格 Picture Style" vs 索尼"创意风格 Creative Style"

- **佳能口径**：照片风格 标准/人像/风光（https://cam.start.canon/zh/C010/manual/html/UG-03_Shooting-1_0180.html）。
- **索尼口径**：创意风格 Standard/Vivid/Landscape，新机型叫 Creative Look（https://www.sony.com/zh-cn/electronics/support/e-mount-body-ilce-7-series/ilce-7m4/articles/00199911 ；http://support.d-imaging.sony.co.jp/wi-fi/dsc/2013-3/4530335111/cs/contents/TP0000244319.html）。
- **收敛结论**：品牌命名不同——人像档：佳能"人像"vs 索尼无对应（靠 Portrait 档+眼部 AF）；风光档两家都叫 Landscape/Picture Style 风光但参数曲线不同。引擎**同时给两家预设名**。

**状态：已确认（命名并存）。**

## K5. 人像自动档：佳能有"人像模式转盘" vs 索尼无对应教学

- **佳能口径**：模式转盘"人像"自动档=自动大光圈+提亮曝光+优化肌肤色泽（https://m.canon.com.cn/special/ds_abcbook/beginner06.html）。
- **索尼口径**：无对应"人像自动档"教学，靠 Creative Style/眼部 AF 组合实现。
- **收敛结论**：引擎遇到"佳能自动人像模式拍出来偏亮偏柔肤"时，**识别为厂商预设行为**，不应判为"曝光过曝"。

**状态：已确认（设备边界）。**

## K7. 阴影残留色偏 Camera Calibration 仅电脑口径

- **Adobe 口径**：LR Classic Develop>Camera Calibration>Shadows Tint（已查证，https://learn.adobe.com/lightroom-classic/help/image-tone-color.html）。
- **手机端**：LR 移动端无此面板，需导出到电脑修。
- **收敛结论**：引擎输出后期建议时，遇"阴影泛绿/品红残留"**注明"需电脑 LR 修，手机端无对应功能"**。

**状态：已确认（设备边界）。**

## K8. 锐化 Masking 仅电脑口径

- **Adobe 口径**：Detail>Masking 按住 Alt 拖看边缘（已查证，https://helpx.adobe.com/lightroom-cc/web/edit-photos/apply-effects/adjust-details.html）。
- **手机端**：LR 移动端简化版无 Masking。
- **收敛结论**：人像磨皮/锐化建议 Masking 70~90 时，手机端**给"降低锐化数量"替代方案**并注明。

**状态：已确认（设备边界）。**

---

> 说明：以上 7 处口径差异已收敛为明确引用规则（条件分支 / 命名并存 / 设备边界），引擎按收敛结论引用即可，无需再等待外部来源。原 K6 已并入 `PPC-009`，不构成悬空引用。
