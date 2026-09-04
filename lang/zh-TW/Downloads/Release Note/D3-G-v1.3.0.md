# D3-G 版本資訊 - v1.3.0

## 更新的儲存庫
- [isp-server](https://github.com/topst-development/isp-server/tree/feature/d3g-ov5647)
- [isp-frontend](https://github.com/topst-development/isp-frontend/tree/feature/d3g)
- [kernel-5.10](https://github.com/topst-development/kernel-5.10/tree/release/d3/1.3.0)
- [meta-topst](https://github.com/topst-development/meta-topst/tree/release/1.3.0)
- [meta-topst-bsp](https://github.com/topst-development/meta-topst-bsp/tree/release/1.3.0)
- [manifests](https://github.com/topst-development/manifests/tree/release/1.3.0)

## 新增功能
- 支援 vulkan 驅動程式
- 支援基本的攝影機 isp 調校工具
- 可透過建置組態支援 PIv2 攝影機
- 在 Ubuntu 桌面版本中支援 firefox-esr（延伸支援版本）

## 改善項目
- 提升 pcie 資料傳輸速度
- 穩定開機期間的 pcie 區塊裝置偵測

## 已知問題
- 插入 sdcard 時，暖開機有時會耗時較久（約 40 秒）。
- 連接至 MIPI 的外接攝影機目前最高支援 30fps（下一版本將支援至 60fps）

## 指南
 - VLC Player
   - 播放內容之前，請在偏好設定中將視訊輸出設為 'X11 video output(XCB)'。
 - Vulkan 驅動程式
   - 請執行 'vkcube' 指令以執行 vulkan 範例。
   - 請參閱 [https://github.com/krh/vkcube.git](https://github.com/krh/vkcube.git)，以瞭解如何撰寫您自己的 vulkan 應用程式。
