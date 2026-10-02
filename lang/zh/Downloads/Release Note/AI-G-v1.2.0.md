# AI-G 发行说明 - v1.2.0

## 已更新的仓库

- [tc-nn-app](https://github.com/topst-development/tc-nn-app)
- [libtc-ndnpu](https://github.com/topst-development/libtc-ndnpu)
- [tc-compiled-nn](https://github.com/topst-development/tc-compiled-nn)
- [meta-topst](https://github.com/topst-development/meta-topst)

## 新功能

- 将 `tcnnapp` 的默认目标检测模型和 `tcnputestapp` 的默认测试模型从 YOLOv5s 更改为 YOLOv8s。

## 改进

- 改进了应用程序的内存清理、输入输出范围检查和初始化错误提示。
- 更新了 MobileNetV2 模型的二进制文件和元数据。
- Windows 固件下载脚本现使用 PowerShell 查询 COM 端口。

## 使用说明

- 默认模型目录为 `/usr/share/yolov8s_quantized/`。`tcnnapp` 的第二个默认模型目录为 `/usr/share/mobilenetv2_10_quantized/`。
- 随附的 YOLOv8s 模型不包含 `sample/input.ia.bin`。缺少此文件时，`tcnputestapp` 会使用全零输入并输出 `Input file not found. Using zero padding.`。此测试用于检查 NPU 的运行和性能，不用于评估模型精度。
- 预构建固件包包含 Windows 用的 `fwdn_ai.bat` 和 Linux 用的 `fwdn_ai.sh`。

## 固件

- [AIG-TOPST-Yocto-image-v1.2.0-r01](https://topst-downloads.s3.ap-northeast-2.amazonaws.com/Yocto/v1.2.0/aig-yp4-v1.2.0-r01.zip)
