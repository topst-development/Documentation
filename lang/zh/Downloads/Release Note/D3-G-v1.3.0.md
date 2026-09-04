# D3-G 发行说明 - v1.3.0

## 已更新的仓库
- [isp-server](https://github.com/topst-development/isp-server/tree/feature/d3g-ov5647)
- [isp-frontend](https://github.com/topst-development/isp-frontend/tree/feature/d3g)
- [kernel-5.10](https://github.com/topst-development/kernel-5.10/tree/release/d3/1.3.0)
- [meta-topst](https://github.com/topst-development/meta-topst/tree/release/1.3.0)
- [meta-topst-bsp](https://github.com/topst-development/meta-topst-bsp/tree/release/1.3.0)
- [manifests](https://github.com/topst-development/manifests/tree/release/1.3.0)

## 新增功能
- 支持 vulkan 驱动程序
- 支持基本的摄像头 isp 调优工具
- 通过构建配置支持 PIv2 摄像头
- 在 Ubuntu 桌面版本中支持 firefox-esr (extended support release)

## 改进
- 提升了 pcie 数据传输速度
- 稳定了启动过程中 pcie 块设备的检测

## 已知问题
- 插入 sdcard 时，热重启有时会耗时较长（大约 40 秒）。
- 连接到 MIPI 的外部摄像头目前最高支持 30fps（下一个版本将支持最高 60fps）

## 指南
 - VLC Player
   - 播放内容前，应在首选项中将视频输出设置为 'X11 video output(XCB)'。
 - Vulkan 驱动程序
   - 运行 'vkcube' 命令以执行 vulkan 示例。
   - 请参阅 [https://github.com/krh/vkcube.git](https://github.com/krh/vkcube.git) 以了解如何编写您自己的 vulkan 应用程序。
