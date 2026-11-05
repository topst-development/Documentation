---
title: TOPST Imager 用户指南
description: 了解如何在 Windows 或 Linux 上为 TOPST 开发板安装操作系统镜像。
---

# TOPST Imager 用户指南

TOPST Imager 是用于在 TOPST 开发板上安装操作系统或固件的应用程序。
无需熟悉计算机或电子设备。请结合本指南和应用中的提示，逐步操作。

> **重要：** 烧录可能会清除开发板 eMMC 中的所有内容。开始前请备份所需文件。

## 1. 常用术语

| 应用中的术语 | 简单说明 |
| --- | --- |
| Board | 要安装操作系统的 TOPST 设备。 |
| Image | 要安装到开发板的操作系统文件。 |
| Flashing | 将镜像文件写入开发板的过程。 |
| Boot mode | 允许计算机向开发板安装镜像的特殊状态。 |
| FWDN | 安装镜像的内部工具，无需手动运行。 |
| COM port | 计算机用于识别通过 USB 连接的开发板的名称。 |
| eMMC | 开发板内置的存储器。 |

## 2. 支持的开发板和镜像文件

| 开发板 | 自定义镜像格式 | 所需连接 |
| --- | --- | --- |
| TOPST D3-G | `.fai` | FWDN USB Type-C 数据线 |
| TOPST AI-G | `.fai` | FWDN USB Type-C 数据线和以太网线 |
| TOPST VCP-G | `.rom` | FWDN USB Type-C 数据线 |

> 仅充电的 USB 线无法使用。请使用**支持数据传输的 USB Type-C 线**。

## 3. 开始前的准备

- 要烧录的 TOPST 开发板及其电源适配器
- 支持数据传输的 USB Type-C 线
- 已连接互联网的计算机
- 使用 AI-G 时所需的以太网线
- 足够下载和解压官方镜像的计算机存储空间
- 开发板上重要数据的备份

烧录期间，请勿关闭开发板、拔掉 USB 或以太网线、关闭 TOPST Imager、关闭计算机或让计算机进入睡眠状态。

## 4. 基本流程

Windows 和 Linux 的基本流程相同。

1. 启动 TOPST Imager。
2. 选择开发板。
3. 选择操作系统或 **Custom Image**。
4. 选择要安装的版本。
5. 按应用提示完成连接并进入启动模式。
6. 开始烧录。
7. 等待出现 **Complete** 画面。

可以单击项目后选择 **Next**，也可以双击项目进入下一步。

---

# Windows 使用说明

## 5. 在 Windows 上安装 TOPST Imager

### 5.1 支持的系统

- Windows 10 64 位或更新版本
- Windows 11 64 位

### 5.2 安装应用

1. 从 TOPST 官方网站下载 Windows 版 `TOPST Imager.exe`。
2. 双击下载的文件。
3. 阅读并接受许可协议。
4. 如有需要，勾选桌面快捷方式。
5. 选择 **Install**。
6. 安装完成后选择 **Launch TOPST Imager**，然后结束安装向导。

如 Windows 显示保护提示，请先确认安装程序来自 TOPST 官方网站。无法确认来源时，请勿运行。

默认安装位置：

```text
%LOCALAPPDATA%\Programs\TOPST Imager
```

## 6. 语言和显示主题

1. 选择窗口左下角的 **App Options**。
2. 选择所需语言。
3. 选择 **Save**。

> 截图中的红框和数字是为本指南添加的，实际应用中不会显示。

![选择 TOPST Imager 的语言和支持选项](https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/Quick%20Guide/TOPST%20Imager%20App%20Options.png)

1. **Language：** 选择语言。
2. **Ask the Community：** 需要帮助时打开 TOPST 社区。
3. **Save：** 应用所选语言。

支持韩语、英语、日语、简体中文、繁体中文、泰语和德语。浅色或深色外观自动跟随 Windows 系统主题。

## 7. 安装官方镜像

### 7.1 选择开发板

1. 核对开发板图片和名称。
2. 单击所需开发板。
3. 确认选中项的颜色已改变。
4. 选择 **Next**。

![选择 D3-G 开发板和 Next 按钮](https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/Quick%20Guide/TOPST%20Imager%20Board%20Selection.png)

1. 选择所需的**开发板项目**。
2. 确认选中后选择 **Next**。

选错时，选择 **Back** 返回重选。

### 7.2 选择操作系统和版本

1. 选择操作系统，然后选择 **Next**。
2. 选择要安装的版本。
3. 核对发布日期和文件大小。

![选择官方操作系统或自定义镜像](https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/Quick%20Guide/TOPST%20Imager%20OS%20Selection.png)

1. 使用官方镜像时，选择所需的**操作系统**。
2. 使用计算机中已有的文件时，选择 **Use Custom Image**。
3. 确认后选择 **Next**。

![选择操作系统版本和 Flashing 按钮](https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/Quick%20Guide/TOPST%20Imager%20Version%20Selection.png)

1. 选择**版本**并核对下载大小和发布日期。
2. 正确后选择 **Flashing**。

- **Download size：** 从互联网下载的压缩文件大小。
- **Extracted size：** 解压后预计占用的计算机空间。

不一定必须使用最新版本。没有其他说明时，请选择推荐版本或最新稳定版。

### 7.3 确认清除警告

烧录前，应用会警告开发板的 eMMC 内容可能被清除。

1. 再次核对开发板和镜像。
2. 确认开发板上没有需要保留的数据。
3. 准备好后选择确认按钮。

![带有 Cancel 和 Confirm 按钮的 eMMC 清除警告](https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/Quick%20Guide/TOPST%20Imager%20eMMC%20Erase%20Warning.png)

1. 尚未准备好或需要重新检查时，选择 **Cancel**。
2. 理解 eMMC 内容可能被清除后，才选择 **Confirm**。

不确定时选择 **Cancel**。在此处取消不会清除开发板。

## 8. 烧录 D3-G

### 8.1 第 1 步：安装驱动

1. 选择 **Install Driver**。
2. Windows 请求管理员权限时，核对消息并选择 **Yes**。
3. 按 VTC 驱动安装程序的提示完成全部步骤。
4. 返回 TOPST Imager。
5. 选择 **Driver Installation Complete**。

![D3-G VTC 驱动安装说明](https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/Quick%20Guide/TOPST%20Imager%20D3-G%20Driver%20Installation.png)

1. 先选择 **Install Driver** 启动安装程序。
2. 完成所有步骤后再选择 **Driver Installation Complete**。

通常每台计算机只需安装一次。

### 8.2 第 2 步：进入启动模式并检测开发板

请观察开发板图片和闪烁标记。

1. **按下 BOOT 按钮。**
2. 保持按住 BOOT。
3. **按下并松开 RESET 按钮。**
4. 松开 BOOT。
5. 确认 USB Type-C 线与计算机和开发板连接牢固。
6. 检查应用是否检测到开发板。

![D3-G 启动模式与开发板检测画面](https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/Quick%20Guide/TOPST%20Imager%20D3-G%20Boot%20Mode.png)

1. 对照图片和闪烁标记完成启动模式操作。
2. 更改连接后选择 **Check Again**。
3. 检测成功后 **Continue Flashing** 可用。

Windows 设备管理器中可能显示类似 `Telechips TCCxxxx VTC USB Driver` 的名称。

### 8.3 第 3 步：烧录镜像

1. 选择 **Start Flashing**。
2. 查看下载、解压和烧录进度。
3. 等待完成画面出现。

## 9. 烧录 AI-G

AI-G 同时使用 USB 和以太网连接。

### 9.1 第 1 步：设置以太网

1. 用以太网线连接计算机与 AI-G。
2. 选择连接 AI-G 的以太网适配器。
3. 按提示将计算机地址设为 `192.168.0.8/24`。
4. 确认网络设置完成。

请选择**连接 AI-G 的有线以太网适配器**，而不是 Wi-Fi。

### 9.2 第 2 步：进入启动模式并选择 COM 端口

1. 观察动画并按下 BOOT。
2. 按住 BOOT 时按下并松开 RESET。
3. 松开 BOOT。
4. 选择新检测到的 AI-G USB COM 端口。
5. 再次检查电源、USB Type-C 线和以太网线。

如果有多个 COM 端口，可暂时拔下 AI-G USB 线。消失的端口就是 AI-G 端口。重新连接后再次进入启动模式再继续。

### 9.3 第 3 步：烧录镜像

1. 选择 **Start Flashing**。
2. 等待进度达到 100%。
3. 完成画面出现后重启开发板。

## 10. 烧录 VCP-G

### 10.1 第 1 步：进入启动模式

1. 查看画面中的开发板图片。
2. 按住 BOOT。
3. 按下并松开 RESET。
4. 松开 BOOT。
5. 选择 **Next**。

### 10.2 第 2 步：选择 COM 端口

1. 选择 VCP-G 的 USB COM 端口。
2. 如果未列出，重新连接 USB Type-C 线。
3. 刷新列表并选择正确端口。

### 10.3 第 3 步：烧录镜像

1. 选择 **Start Flashing**。
2. 等待进度达到 100%。
3. 完成画面出现后重启开发板。

## 11. 安装自定义镜像

此选项用于安装官方目录中没有的本地镜像文件。

1. 在操作系统选择画面单击 **Custom Image**。
2. 选择 **Next** 或双击该项目。
3. 将文件拖入虚线区域，或选择 **Browse for FAI Image** / **Browse for ROM Image** 来选取文件。
4. 检查所选文件名。
5. 选择 **Next**，并按对应开发板的连接提示操作。

D3-G 和 AI-G 使用 `.fai`，VCP-G 使用 `.rom`，请勿选错格式。
文件已在本机，因此烧录画面不会显示下载和解压步骤。

## 12. Windows 故障排除

### 检测不到开发板

1. 确认开发板已通电。
2. 确认 USB 线不是仅充电线。
3. 确认连接到 FWDN USB Type-C 端口。
4. 重新执行进入启动模式的步骤。
5. D3-G 需确认 VTC 驱动已安装。

### 没有 COM 端口

1. 拔下并重新连接 USB 线。
2. 检查开发板电源。
3. 重新进入启动模式。
4. 刷新 COM 端口列表。

### AI-G 网络错误

1. 检查计算机和 AI-G 之间的以太网线。
2. 确认选择有线适配器而非 Wi-Fi。
3. 确认计算机地址为 `192.168.0.8/24`。
4. 按应用提示从第 1 步重新开始。

### 出现 `Failed open port` 或 `GetLastError : 22`

检查 FWDN USB Type-C 线，重新连接，然后从启动模式步骤重新操作。

### 下载没有进展

1. 检查互联网连接。
2. 检查计算机剩余空间。
3. 稍等后选择 **Retry**。

### 烧录中想返回上一步

烧录开始后返回会出现取消确认窗口。取消前请确认开发板处于安全状态，并遵循屏幕提示。

### 需要错误相关帮助

1. 复制错误窗口中的详细信息。
2. 从 **App Options** 打开日志文件夹。
3. 准备错误消息和日志文件。
4. 在 [TOPST 社区](https://community.topst.ai/)提问。

Windows 上的常见日志位置：

```text
%LOCALAPPDATA%\Telechips\TOPST Imager\logs\topst-imager.log
```

---

# Linux 使用说明

## 13. Linux 使用前准备

画面和基本流程与 Windows 相同，但准备工作不同。开发板、操作系统和版本按钮的位置与上面的 Windows 截图相同。Linux 会跳过 D3-G 的 Windows 驱动安装画面，直接进入启动模式和开发板检测。

- 不要安装 Windows VTC 驱动。
- D3-G 需要 Linux USB 权限。
- AI-G 和 VCP-G 需要串口权限。
- 发行包必须包含 Linux FWDN 可执行文件。
- 解压官方镜像需要 `unzip` 或 `bsdtar`。

不熟悉命令行时，请管理员或开发人员完成下面的 **Linux 管理员设置**。一次性设置完成后，普通用户可按屏幕提示操作。

## 14. 在 Linux 上安装和运行

以下示例使用 Ubuntu。

### 14.1 解压安装包

1. 从官方网站下载适合计算机的 Linux 包。
2. 打开下载文件夹。
3. 打开终端并执行：

```bash
cd ~/Downloads
tar -xzf TOPST-Imager-<version>-Linux-<architecture>.tar.gz
```

将 `<version>` 和 `<architecture>` 替换为实际文件名中的值。输入文件名前几个字符后可按 `Tab` 自动补全。

### 14.2 运行应用

进入解压后的文件夹并运行：

```bash
cd TOPST-Imager-<version>-Linux-<architecture>
chmod +x topst-imager
./topst-imager
```

如果提示缺少 `Qt` 库，则当前包不含 Qt 运行时。普通用户应向发行方索取**包含 Qt 6.12 运行时的 Linux 包**，而不要尝试手动安装。

## 15. Linux 管理员设置

通常只需执行一次。

### 15.1 安装解压工具

```bash
sudo apt update
sudo apt install unzip
```

### 15.2 AI-G 和 VCP-G 串口权限

```bash
sudo usermod -aG dialout "$USER"
```

执行后注销并重新登录，或重启计算机。

### 15.3 D3-G USB 权限

1. 将 D3-G 以启动模式连接。
2. 在终端查找 USB ID：

```bash
lsusb
```

3. 使用检测到的厂商 ID 和产品 ID 创建 `/etc/udev/rules.d/99-topst.rules`。

```text
SUBSYSTEM=="usb", ATTR{idVendor}=="VENDOR_ID", ATTR{idProduct}=="PRODUCT_ID", MODE="0666"
```

4. 重新加载规则：

```bash
sudo udevadm control --reload-rules
sudo udevadm trigger
```

不要随意填写 `VENDOR_ID` 和 `PRODUCT_ID`。不清楚 D3-G 的正确值时，请联系 TOPST 支持。

### 15.4 检查 Linux FWDN 文件

发行包的以下位置必须包含无扩展名的 Linux 可执行文件：

```text
tools/fwdn_d3/fwdn_d3
tools/fwdn_ai/fwdn_ai
tools/fwdn_vcp/fwdn_vcp
```

如果文件存在，请赋予执行权限：

```bash
chmod +x tools/fwdn_d3/fwdn_d3
chmod +x tools/fwdn_ai/fwdn_ai
chmod +x tools/fwdn_vcp/fwdn_vcp
```

缺少这些文件时，Linux 无法烧录。不能使用 Windows `.exe` 文件代替。

## 16. 在 Linux 上烧录 D3-G

Linux 不使用 Windows VTC 驱动安装步骤。

1. 选择 D3-G 镜像。
2. 观看动画并按下 BOOT。
3. 按住 BOOT 时按下并松开 RESET。
4. 松开 BOOT。
5. 检查是否检测到开发板。
6. 开始烧录并等待完成。

未检测到时，检查 USB 权限规则、Type-C 线、电源和启动模式。

## 17. 在 Linux 上烧录 AI-G

TOPST Imager 不会在 Linux 上自动修改以太网地址。请在 Ubuntu 设置中手动配置。

1. 打开 **设置 → 网络**。
2. 打开连接 AI-G 的有线网络设置。
3. 将 IPv4 方法设为**手动**。
4. 地址输入 `192.168.0.8`。
5. 子网掩码输入 `255.255.255.0`；如果使用前缀长度则输入 `24`。
6. 如无其他说明，网关和 DNS 留空。
7. 应用设置后关闭并重新开启有线连接。
8. 返回 TOPST Imager，检查以太网状态。
9. 按屏幕提示进入启动模式。
10. 选择 AI-G 的 `/dev/ttyUSB...` 或 `/dev/ttyACM...` 端口。
11. 开始烧录。

## 18. 在 Linux 上烧录 VCP-G

1. 按屏幕提示进入启动模式。
2. 选择 `/dev/ttyUSB...` 或 `/dev/ttyACM...` 格式的端口。
3. 确认端口正确后开始烧录。
4. 等待完成画面。

没有端口时，请确认已加入 `dialout` 组，并已注销后重新登录。

## 19. Linux 故障排除

### 出现 `Permission denied`

- AI-G 或 VCP-G：确认用户属于 `dialout` 组。
- D3-G：确认 udev USB 权限规则已生效。
- FWDN 文件：确认已通过 `chmod +x` 赋予执行权限。

### 找不到 Linux FWDN 文件

检查发行文件夹的 `tools/fwdn_*` 中是否有 Linux 可执行文件。Windows `.exe` 无法在 Linux 上运行。

### 没有开发板端口

执行以下命令列出端口：

```bash
ls /dev/ttyUSB* /dev/ttyACM* 2>/dev/null
```

比较连接 USB 前后的列表。新出现的端口通常就是开发板端口。

### 未跟随浅色或深色主题

应用使用 Linux 桌面通过 Qt 提供的主题信息。某些环境可能不会立即生效，请尝试重启应用。

## 20. 烧录完成后

1. 确认显示成功消息。
2. 等待 TOPST Imager 完成所有工作。
3. 安全关闭开发板电源。
4. 拔掉 FWDN 线，或重新连接为日常使用所需的线缆。
5. 开机并确认新操作系统正常启动。

官方镜像会下载并解压到临时文件夹。烧录成功后，下载文件和解压文件夹会自动删除。

## 21. 请牢记三件事

1. **确认选择了正确的开发板和镜像。**
2. **烧录时不要断电或拔线。**
3. **出现错误时，按屏幕列表从上到下逐项检查。**

需要帮助时，请准备错误消息和日志文件，在 [TOPST 社区](https://community.topst.ai/)提问。
