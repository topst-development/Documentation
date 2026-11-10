# TOPST Imager 用户指南

TOPST Imager 用于在 TOPST 开发板上安装操作系统或固件。无需编程或电子知识。请保持本指南打开，并逐个画面操作。

> **重要：** 烧录可能会清除开发板 eMMC 中的所有内容。开始前请备份所需文件。

> **关于截图：** 红框和带数字的圆圈仅为本指南添加，不会在 TOPST Imager 中显示。截图使用 Windows 浅色主题；Linux 和深色主题的操作方式相同。

## 1. 画面中的术语

| 术语 | 简单说明 |
| --- | --- |
| Board / Device | 要安装镜像的 TOPST 产品。 |
| Image | 包含操作系统或固件的文件。 |
| Flashing | 将所选镜像写入开发板。 |
| Firmware Download Mode / Boot Mode | 用于烧录的特殊开发板状态。 |
| FWDN | TOPST Imager 在后台运行的工具，无需自行启动。 |
| COM port | AI-G 和 VCP-G 使用的 USB 串口连接。Linux 显示为 `/dev/ttyUSB...` 或 `/dev/ttyACM...`。 |
| eMMC | 开发板内置存储器。 |

## 2. 支持的开发板

| 开发板 | 自定义镜像 | 烧录时使用的连接 |
| --- | --- | --- |
| TOPST D3-G | `.fai` | 开发板电源和 FWDN USB Type-C 数据线 |
| TOPST AI-G | `.fai` | 开发板电源、FWDN USB Type-C 数据线和以太网线 |
| TOPST VCP-G | `.rom` | 开发板电源和 FWDN USB Type-C 数据线 |

请使用支持**数据传输**的 USB Type-C 线。仅充电线无法使用。

## 3. 开始前准备

- 正确的 TOPST 开发板和电源适配器
- USB Type-C 数据线
- 使用 AI-G 时的以太网线
- 使用官方镜像时可连接互联网的计算机
- 能同时存放下载压缩文件和解压包的足够磁盘空间
- 开发板上重要数据的备份

烧录期间：

- 不要关闭开发板或计算机。
- 不要拔掉 USB 或以太网线。
- 不要关闭 TOPST Imager。
- 不要让计算机进入睡眠。

## 4. 应用选项

选择主窗口左下角的 **App Options**。

![TOPST Imager 应用选项](https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/Quick%20Guide/TOPST%20Imager%20App%20Options.png)

1. **Language：** 选择语言后立即切换画面，以便预览。
2. **TOPST Imager User Guide：** 在浏览器中打开本用户指南。
3. **Ask the Community：** 打开 [TOPST 社区](https://community.topst.ai/)。
4. **Save：** 保存所选语言。选择 **Cancel**、按 `Esc` 或点击窗口外部，会恢复打开窗口前使用的语言。

支持韩语、英语、日语、简体中文、繁体中文、泰语和德语。浅色或深色外观自动跟随操作系统主题。

---

# Windows

## 5. 安装 TOPST Imager

### 5.1 系统要求

- Windows 10 64 位或更新版本
- Windows 11 64 位

### 5.2 安装

1. 下载官方 TOPST Imager Windows 安装程序。
2. 双击安装程序。
3. 阅读并接受许可协议。
4. 选择 **Install**。
5. 完成后选择 **Launch TOPST Imager**。

启动应用或 VTC 驱动安装程序时，Windows 可能请求管理员权限。请确认文件来自官方 TOPST 发行包后再选择 **Yes**。

## 6. 选择开发板、操作系统和版本

### 6.1 选择开发板

![选择 TOPST 开发板](https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/Quick%20Guide/TOPST%20Imager%20Board%20Selection.png)

1. 选择与手中产品一致的开发板。
2. 确认该行高亮并显示 **Selected**，然后选择 **Next**。

也可双击开发板继续。选错时选择 **Back** 返回重选。

### 6.2 选择操作系统

![选择官方操作系统或自定义镜像](https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/Quick%20Guide/TOPST%20Imager%20OS%20Selection.png)

1. 选择 TOPST 提供的操作系统。
2. 使用计算机中的文件时选择 **Use Custom Image**。
3. 选择 **Next** 或双击所选行。

### 6.3 选择版本

![选择镜像版本](https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/Quick%20Guide/TOPST%20Imager%20Version%20Selection.png)

1. 选择所需版本，检查说明、发布日期、下载大小和解压大小。
2. 选择 **Flashing**。

- **Download size** 是从互联网传输的压缩文件大小。
- **Extracted size** 是解压后预计所需的磁盘空间。

除非项目要求特定版本，否则使用最新稳定版或推荐版本。

### 6.4 确认清除数据

![确认 eMMC 清除警告](https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/Quick%20Guide/TOPST%20Imager%20eMMC%20Erase%20Warning.png)

1. 需要重新检查开发板、镜像或备份时，选择 **Cancel**。
2. 只有理解所选开发板的 eMMC 数据可能被删除后，才选择 **Confirm**。

此时选择 **Cancel** 不会清除开发板。

## 7. 在 Windows 上烧录 D3-G

Windows 上的 D3-G 烧录设置分为三步。

### 第 1 步：安装 VTC 驱动

![安装 D3-G VTC 驱动](https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/Quick%20Guide/TOPST%20Imager%20D3-G%20Driver%20Installation.png)

1. 选择 **Install Driver**。
2. 批准 Windows 管理员请求。
3. 完成 VTC 驱动安装程序。
4. 返回 TOPST Imager。
5. 选择 **Driver Installation Complete**。

通常每台 Windows 计算机只需安装一次。取消管理员请求就不会安装驱动；准备好后再次选择 **Install Driver**。

### 第 2 步：进入启动模式并检测开发板

![进入 D3-G 启动模式并检测开发板](https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/Quick%20Guide/TOPST%20Imager%20D3-G%20Boot%20Mode.png)

1. 按启动模式动画的闪烁标记操作。
2. 按住 **BOOT**。
3. 按住 BOOT 时按下并松开 **RESET**。
4. 松开 BOOT。
5. 牢固连接 FWDN USB Type-C 数据线。
6. 状态未自动刷新时选择 **Check Again**。
7. 状态变为已连接后选择 **Start Flashing**。

Windows 设备管理器的通用串行总线控制器下，可能显示类似 `Telechips TCCxxxx VTC USB Driver` 的名称。

### 第 3 步：烧录

官方镜像分别显示以下进度：

1. 下载
2. 解压
3. 烧录

各项进度从 0% 到 100%。请等待 **Complete** 画面后再断开连接。

## 8. 在 Windows 上烧录 AI-G

AI-G 烧录设置分为三步。

### 第 1 步：设置以太网

1. 用以太网线直接连接计算机和 AI-G。
2. 选择连接 AI-G 的有线适配器，而非 Wi-Fi。
3. 出现提示时允许应用设置临时地址 `192.168.0.8/24`。
4. 网络就绪后继续。

操作完成或取消后，TOPST Imager 会恢复临时更改的 Windows 网络设置。

### 第 2 步：启动模式与 COM 端口

1. 按屏幕启动模式动画操作。
2. 按住 **BOOT**。
3. 按下并松开 **RESET**。
4. 松开 BOOT。
5. 选择 AI-G 的 COM 端口。
6. 检查电源、USB Type-C 数据线和以太网线。
7. 继续烧录。

存在多个 COM 端口时，可暂时拔下 AI-G USB 线。消失的端口通常属于 AI-G。重新连接、再次进入启动模式，然后选择该端口。

### 第 3 步：烧录

等待达到 100% 并出现 **Complete** 画面。

## 9. 在 Windows 上烧录 VCP-G

VCP-G 烧录设置分为两步。

### 第 1 步：启动模式与 COM 端口

启动模式指南和 COM 端口选择在同一画面。

1. 按动画将 VCP-G 设为 Firmware Download Mode。
2. 按指南要求按下并松开 **RESET**。
3. 选择 VCP-G 的 COM 端口。
4. 再次检查电源及 FWDN USB Type-C 数据线。
5. 继续烧录。

### 第 2 步：烧录

等待达到 100% 并出现 **Complete** 画面。

## 10. 在 Windows 上使用自定义镜像

1. 先选择正确的开发板。
2. 在操作系统画面单击 **Use Custom Image**。
3. 选择 **Next** 或双击 **Use Custom Image**。
4. 将文件拖入放置区域，或选择浏览按钮。
5. 检查文件名后继续。

使用正确格式：

- D3-G: `.fai`
- AI-G: `.fai`
- VCP-G: `.rom`

文件已在本机，因此 **Download** 和 **Extraction** 进度行会隐藏。对应开发板的驱动、网络、启动模式、COM 端口和烧录步骤仍然适用。

---

# Linux

## 11. Linux 要求

当前发行包支持 **x86_64 Linux**。Windows `.exe` FWDN 文件不能在 Linux 使用。

发行应用必须包含以下 Linux 可执行工具：

```text
tools/fwdn_d3/fwdn_d3
tools/fwdn_ai/fwdn_ai
tools/fwdn_vcp/fwdn_vcp
```

计算机还需要：

- 用于官方 ZIP 包的 `unzip`
- 用于管理员确认窗口的 `policykit-1`
- 用于 AI-G 和 VCP-G 临时串口访问的 `acl`

Ubuntu 管理员可执行：

```bash
sudo apt update
sudo apt install unzip policykit-1 acl
```

**不要**用 `sudo` 运行 TOPST Imager 或 FWDN。应用仅在需要授予所选串口设备临时访问权限时请求管理员权限。

## 12. 安装并启动 Linux 包

压缩文件名可能随版本变化。`.tar.gz` 包示例：

```bash
cd ~/Downloads
tar -xzf TOPST-Imager-<version>-Linux-x86_64.tar.gz
cd TOPST-Imager-<version>-Linux-x86_64
chmod +x topst-imager
./topst-imager
```

请使用下载包的实际文件和文件夹名称。用户包应包含 Qt 运行时；若缺少 Qt 库，请下载完整官方 Linux 包，而不要以 root 运行。

## 13. 在 Linux 上选择镜像

开发板、操作系统、版本、自定义镜像和 eMMC 警告画面，与第 6 节和第 10 节的 Windows 画面相同。

## 14. 在 Linux 上烧录 D3-G

不显示 Windows VTC 驱动安装步骤，因此 Linux 上分为两步。

### 第 1 步：启动模式与开发板检测

1. 按住 **BOOT**。
2. 按下并松开 **RESET**。
3. 松开 BOOT。
4. 连接 FWDN USB Type-C 数据线。
5. 必要时选择 **Check Again**。
6. 检测到 D3-G 后继续。

Linux 直接检测 D3-G FWDN USB 设备。未检测到时，请检查数据线、电源、启动模式，以及 Linux 包提供且已安装的 udev 规则。

### 第 2 步：烧录

等待下载、解压和烧录完成。自定义 `.fai` 镜像仅显示烧录进度。

## 15. 在 Linux 上烧录 AI-G

AI-G 烧录设置分为三步。

### 第 1 步：设置以太网

Linux 以太网地址不会自动更改，请在网络设置中配置：

1. 打开 **设置 → 网络**。
2. 打开连接 AI-G 的有线连接。
3. 将 IPv4 设为**手动**。
4. 地址：`192.168.0.8`
5. 子网掩码：`255.255.255.0`，或前缀长度 `24`
6. 除非网络管理员另有要求，否则网关和 DNS 留空。
7. 应用更改，重新连接有线网络，返回 TOPST Imager。

### 第 2 步：启动模式、COM 端口和临时访问

1. 按启动模式动画操作。
2. 选择 AI-G 端口，例如 `/dev/ttyUSB0`。
3. 端口不可写时选择 **Grant Temporary Access**。
4. 批准 Linux 管理员窗口。
5. 权限就绪后烧录按钮可用。

临时权限仅作用于所选串口设备，在烧录后、取消后或离开烧录画面后释放。无需将用户永久加入 `dialout` 组。

### 第 3 步：烧录

等待 **Complete** 画面。

## 16. 在 Linux 上烧录 VCP-G

与 Windows 一样，烧录设置分为两步。

### 第 1 步：启动模式、COM 端口和临时访问

1. 按启动模式指南操作。
2. 选择 VCP-G 端口，例如 `/dev/ttyUSB0`。
3. 如果显示 **Grant Temporary Access**，请选择并批准管理员窗口。
4. 所选端口可访问后继续。

### 第 2 步：烧录

等待达到 100% 并出现 **Complete** 画面。自定义 `.rom` 镜像仅显示烧录进度。

## 17. 下载、重试和临时文件

使用官方镜像时，应用会：

1. 创建临时工作文件夹。
2. 下载 ZIP 包。
3. 解压到临时文件夹。
4. 运行对应开发板的 FWDN 可执行文件。
5. 烧录成功或取消后删除下载及解压的临时数据。

下载时断网，请保持应用打开并重新联网。应用会自动重试，服务器支持时从部分下载处续传。状态以所选应用语言显示。

某些可恢复的烧录错误会临时保留准备好的包，便于返回指定设置步骤而无需重新下载。

## 18. 出现错误窗口时

应用检测到已知 FWDN 错误后会立即打开错误窗口。如显示三秒倒计时，请阅读消息；倒计时后应用返回所需恢复步骤。检查所列项目后选择 **OK**。

### D3-G 连接错误

检查：

1. 开发板电源连接
2. FWDN USB Type-C 数据线连接
3. 是否进入 Firmware Download Mode

应用返回 D3-G 启动模式步骤。

### AI-G 连接或同步错误

检查：

1. 开发板电源连接
2. 是否进入 Firmware Download Mode
3. COM 端口选择是否正确

如消息为 `Failed open port`，检查 FWDN USB Type-C 数据线和所选端口。如为 `TCP Socket Open Fail`，检查以太网线、适配器和 `192.168.0.8/24` 设置。

### VCP-G 连接错误

检查：

1. 开发板电源连接
2. 是否进入 Firmware Download Mode
3. COM 端口选择是否正确

出现 `GetLastError : 22` 时，检查 FWDN USB Type-C 连接。

### 没有 COM 端口

1. 检查电源。
2. 重新连接 USB 数据线。
3. 再次进入 Firmware Download Mode。
4. 刷新端口列表。
5. Linux 上选择端口后选择 **Grant Temporary Access**。

### 烧录完全失败

如错误为 `Failed to write in eFlash` 或 `Failed FWDN`，请按消息从第一个烧录设置步骤重新开始。写入仍在进行时不要断开开发板。

## 19. 日志文件

求助时提供完整错误消息、开发板名称、所选镜像版本、操作系统和日志文件。

Windows 日志位置：

```text
%LOCALAPPDATA%\Telechips\TOPST Imager\logs\topst-imager.log
```

常见 Linux 日志位置：

```text
~/.local/share/Telechips/TOPST Imager/logs/topst-imager.log
```

需要更多帮助时，使用 **App Options → Ask the Community** 或访问 [TOPST 社区](https://community.topst.ai/)。

## 20. 烧录完成后

1. 确认 **Complete** 画面可见。
2. 等待应用说明操作已完成。
3. 安全关闭开发板电源。
4. 拔掉 FWDN 线，或恢复正常使用的接线。
5. 开机并检查新操作系统是否启动。

记住三条规则：

1. 仔细选择开发板和镜像。
2. 烧录时绝不拔线或断电。
3. 出现错误时，从上到下检查所有列出项目。
