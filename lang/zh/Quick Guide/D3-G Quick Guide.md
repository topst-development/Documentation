# D3-G 快速指南
---

## 1.1 使用 USB 启动模式连接 D3-G 开发板与主机 PC
---
Firmware Downloader (FWDN) 通过与主机 PC 的 USB 通信将 ROM 镜像写入 D3-G。 

D3-G 具有一个 Boot Mode 按钮，并支持两种启动模式。本指南主要介绍 FWDN 模式。

- USB Boot Mode (FWDN Mode) : 用于通过主机 PC 上的 FWDN 工具写入 ROM 镜像 

- eMMC Boot Mode : 用于通过存储在 eMMC 设备中的 ROM 镜像启动 D3-G 

**注意**: USB Type-C FWDN 端口用于固件下载器 (FWDN)。 



要使用 FWDN，请按以下方式将 D3-G 开发板连接到主机 PC： 

1. 检查主机 PC 上是否已安装 VTC 驱动程序。如果未安装 VTC 驱动程序，请按第 1.2 章所述进行安装。  

2. 准备一根 USB Type-C 线缆。 

3. 要进入 USB 启动模式，请在按住 FWDN 开关的同时将电源线连接到 D3-G 开发板。

4. 将 USB Type-C 线缆连接到 D3-G 开发板上的 USB Type-C FWDN 端口和主机 PC。 

<p align="center">
    <img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20D3-G/Hardware/connect%20to%20d3g%20to%20host%20pc%20using%20c%20type.png">
</p>
<p align="center"><strong>图 1.1 使用 USB C-Type 线缆连接 D3-G 开发板与主机 PC </strong></p>

<br/><br/>

## 1.2 如何安装 VTC 驱动程序 (Windows/Ubuntu)
以管理员身份运行，在主机 PC 上安装 Vendor Telechips Certification (VTC) 驱动程序（可在 [telechips 驱动程序](https://drive.google.com/file/d/1muQnY8kuKxDsy3p3FUiQqcG34Zjk-mnR/view?usp=sharing) 处获取）。如上所示在 FWDN 模式下连接 USB 后，Telechips VTC USB 驱动程序将按图 1.2 和图 1.3 所示进行设置。

<p align="center">
    <img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20D3-G/Software/USB%20Connection%20in%20Windows%20Environment.png", width="700">
</p>
<p align="center"><strong>图 1.2 Windows 环境下的 USB 连接</strong></p>

<p align="center">
    <img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20D3-G/Software/USB%20Connection%20in%20Linux%20System.png", width="700">
</p>
<p align="center"><strong>图 1.3 Linux 环境下的 USB 连接</strong></p>  

**注意**: 请使用 V5.0.0.14 或更高版本的 VTC 驱动程序。要检查版本，请在 Windows 环境下查看设备管理器。  

<br/><br/><br/>

## 1.3 Windows 环境下的 FWDN

### 1.3.1 D3-G Yocto
---
1. 转到下载页面

2. 下载 D3-G Yocto 镜像
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/Quick%20Guide/Download%20D3-G%20v1.2.0%20Yocto%20Image.png" width="550"></p>
<p align="center"><strong>图 1.4 下载 D3-G Yocto 镜像</strong></p> <br/>

3. 单击 fwdn.bat。“fwdn.bat”是使用 ***FWDN V8*** 自动下载固件的可执行文件。 
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/Quick%20Guide/Click%20fwdn.bat.png" width="550"></p>
<p align="center"><strong>图 1.5 单击 fwdn.bat</strong></p> <br/>

```
C:\output_d3g.fwdn>fwdn.exe --fwdn boot-firmware\fwdn.json
[main:30] FWDN V8 v1.4.6 - 2021.12.13 13:42:37
[FWDN_V8::LoadFWDNRom:403] Start to load FWDN rom
[FWDN_V8::LoadMCERT:592] C:\output_d3g.fwdn\boot-firmware\mcert.bin
[FWDN_V8::LoadHSM:609] C:\output_d3g.fwdn\boot-firmware\hsm.cs.bin
[FWDN_V8::SendFWDNHeader:634] C:\output_d3g.fwdn\boot-firmware\fwdn.rom - Header
[FWDN_V8::SendFWDNBody_V8:537] C:\output_d3g.fwdn\boot-firmware\fwdn.rom - Body
[FWDN_V8::LoadFWDNRom:414] Complete to load FWDN rom
[FWDN_V8::GetFWDNRomVersion:1526] fwdn.rom version : 21.9.29
[FWDN_V8::GetFileAndWriteCommand:748] C:\output_d3g.fwdn\boot-firmware\dram_params.bin
[FWDN_V8::PrintDeviceInfo:1183] --------------Device info-------------
[FWDN_V8::PrintDeviceInfo:1184]

----- Detail of Storages -----
#### eMMC Info ####
Manufacture ID: 0x15
OEM: 0x100
Name: 8GTF4
User Capacity: 7.3 GiB (7818182656 Byte)
Boot Capacity: 4 MiB (4194304 Byte)
RPMB Capacity: 512 KiB (524288 Byte)
Speed Mode: HS200
#### SNOR Info ####
Manufacture ID: 0xc2
Device ID: 0x2016
Name: MXIC-MX25L3233F
Sector Size: 4 KiB (4096 Byte)
Total Capacity: 4 MiB (4194304 Byte)
4Byte Address Mode: Unsupported

----- Summary of Storages -----
eMMC : O
SNOR : O
UFS : X
- O : Init success
- X : Init failed or not exist

----- Summary of DRAM Init -----
DRAM Init : Success (Result 0x0 )
DRAM Size : 4096MB

[FWDN_V8::PrintDeviceInfo:1185] --------------------------------------
[main:142] Complete FWDN
[FWDNLogger::PrintCurTime:111] 24/04/25-09:57:47

C:\output_d3g.fwdn>fwdn.exe --storage emmc --low-format
[main:30] FWDN V8 v1.4.6 - 2021.12.13 13:42:37
[FWDN_V8::GetFWDNRomVersion:1526] fwdn.rom version : 21.9.29
[FWDN_V8::LowformatCommand:1352] Start low-format
[FWDN_V8::LowformatCommand:1353] low-format can take a long time
[FWDN_V8::LowformatCommand:1382] Complete low-format
[main:142] Complete FWDN
[FWDNLogger::PrintCurTime:111] 24/04/25-09:57:50

C:\output_d3g.fwdn>fwdn.exe -w boot-firmware\boot.single.json
[main:30] FWDN V8 v1.4.6 - 2021.12.13 13:42:37
[FWDN_V8::GetFWDNRomVersion:1526] fwdn.rom version : 21.9.29
[main:117] Start write command
[FWDN_V8::GetFileAndWriteCommand:748] C:\output_d3g.fwdn\boot-firmware\bconf.single.bin
[FWDN_V8::GetFileAndWriteCommand:748] C:\output_d3g.fwdn\boot-firmware\bconf.single.bin
[FWDN_V8::GetFileAndWriteCommand:748] C:\output_d3g.fwdn\boot-firmware\mcert.bin
[FWDN_V8::GetFileAndWriteCommand:748] C:\output_d3g.fwdn\boot-firmware\mcert.bin
[FWDN_V8::GetFileAndWriteCommand:748] C:\output_d3g.fwdn\boot-firmware\dram_params.bin
[FWDN_V8::GetFileAndWriteCommand:748] C:\output_d3g.fwdn\boot-firmware\dram_params.bin
[FWDN_V8::GetFileAndWriteCommand:748] C:\output_d3g.fwdn\boot-firmware\hsm.cs.bin
[FWDN_V8::GetFileAndWriteCommand:748] C:\output_d3g.fwdn\boot-firmware\hsm.cs.bin
[FWDN_V8::GetFileAndWriteCommand:748] C:\output_d3g.fwdn\boot-firmware\scfw.rom
[FWDN_V8::GetFileAndWriteCommand:748] C:\output_d3g.fwdn\boot-firmware\scfw.rom
[FWDN_V8::GetFileAndWriteCommand:748] C:\output_d3g.fwdn\boot-firmware\optee.rom
[FWDN_V8::GetFileAndWriteCommand:748] C:\output_d3g.fwdn\boot-firmware\optee.rom
[FWDN_V8::GetFileAndWriteCommand:748] C:\output_d3g.fwdn\boot-firmware\ca72_bl1.rom
[FWDN_V8::GetFileAndWriteCommand:748] C:\output_d3g.fwdn\boot-firmware\ca72_bl1.rom
[FWDN_V8::GetFileAndWriteCommand:748] C:\output_d3g.fwdn\boot-firmware\ca53_bl1.rom
[FWDN_V8::GetFileAndWriteCommand:748] C:\output_d3g.fwdn\boot-firmware\ca53_bl1.rom
[FWDN_V8::GetFileAndWriteCommand:748] C:\output_d3g.fwdn\boot-firmware\ca72_bl2.rom
[FWDN_V8::GetFileAndWriteCommand:748] C:\output_d3g.fwdn\boot-firmware\ca72_bl2.rom
[FWDN_V8::GetFileAndWriteCommand:748] C:\output_d3g.fwdn\boot-firmware\ca53_bl2.rom
[FWDN_V8::GetFileAndWriteCommand:748] C:\output_d3g.fwdn\boot-firmware\ca53_bl2.rom
[main:125] Complete write command
[main:142] Complete FWDN
[FWDNLogger::PrintCurTime:111] 24/04/25-09:57:53
100% [||||||||||||||||||||||||||||||] 859264/859264
C:\output_d3g.fwdn>fwdn.exe -w "output_d3g.fai" --storage emmc --area user
[main:30] FWDN V8 v1.4.6 - 2021.12.13 13:42:37
[FWDN_V8::GetFWDNRomVersion:1526] fwdn.rom version : 21.9.29
[main:117] Start write command
[FWDN_V8::GetFileAndWriteCommand:748] output_d3g.fai
[main:125] Complete write command
[main:142] Complete FWDN
[FWDNLogger::PrintCurTime:111] 24/04/25-10:05:21
100% [||||||||||||||||||||||||||||||] 7238688960/7238688960
** When writing FAI files without low-format, there may be garbage values in partition where data is not written.
```

### 1.3.2 D3-G Ubuntu Desktop
---
1. 转到下载页面

2. 下载 D3-G Ubuntu Desktop 镜像
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/Quick%20Guide/Download%20D3-G%20v1.2.0%20Ubuntu%20Desktop%20Image.png" width="550"></p>
<p align="center"><strong>图 1.6 下载 D3-G Ubuntu Desktop 镜像</strong></p> <br/>

3. 单击 fwdn.bat。“fwdn.bat”是使用 ***FWDN V8*** 自动下载固件的可执行文件。 
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/Quick%20Guide/Click%20fwdn_ubuntu.bat.png" width="550"></p>
<p align="center"><strong>图 1.7 单击 fwdn.bat</strong></p> <br/>

```
C:\d3g-ubuntu.fwdn>fwdn.exe --fwdn boot-firmware\fwdn.json
[main:30] FWDN V8 v1.4.11 - 2022.11.14 13:47:30
[FWDN_V8::GetFWDNRomVersion:1588] fwdn.rom version : 23.5.22
[main:156] Complete FWDN
[FWDNLogger::PrintCurTime:112] 25/06/25-10:32:29

C:\d3g-ubuntu.fwdn>fwdn.exe --storage emmc --low-format
[main:30] FWDN V8 v1.4.11 - 2022.11.14 13:47:30
[FWDN_V8::GetFWDNRomVersion:1588] fwdn.rom version : 23.5.22
[FWDN_V8::LowformatCommand:1370] Start low-format
[FWDN_V8::LowformatCommand:1371] low-format can take a long time
[FWDN_V8::LowformatCommand:1400] Complete low-format
[main:156] Complete FWDN
[FWDNLogger::PrintCurTime:112] 25/06/25-10:32:29

C:\d3g-ubuntu.fwdn>fwdn.exe -w boot-firmware\boot.single.json
[main:30] FWDN V8 v1.4.11 - 2022.11.14 13:47:30
[FWDN_V8::GetFWDNRomVersion:1588] fwdn.rom version : 23.5.22
[main:131] Start write command
[FWDN_V8::GetFileAndWriteCommand:762] C:\d3g-ubuntu.fwdn\boot-firmware\.\prebuilt\bconf.single.bin
[FWDN_V8::GetFileAndWriteCommand:762] C:\d3g-ubuntu.fwdn\boot-firmware\.\prebuilt\bconf.single.bin
[FWDN_V8::GetFileAndWriteCommand:762] C:\d3g-ubuntu.fwdn\boot-firmware\.\prebuilt\mcert.bin
[FWDN_V8::GetFileAndWriteCommand:762] C:\d3g-ubuntu.fwdn\boot-firmware\.\prebuilt\mcert.bin
[FWDN_V8::GetFileAndWriteCommand:762] C:\d3g-ubuntu.fwdn\boot-firmware\.\prebuilt\dram_params.bin
[FWDN_V8::GetFileAndWriteCommand:762] C:\d3g-ubuntu.fwdn\boot-firmware\.\prebuilt\dram_params.bin
[FWDN_V8::GetFileAndWriteCommand:762] C:\d3g-ubuntu.fwdn\boot-firmware\.\prebuilt\hsm.cs.bin
[FWDN_V8::GetFileAndWriteCommand:762] C:\d3g-ubuntu.fwdn\boot-firmware\.\prebuilt\scfw.rom
[FWDN_V8::GetFileAndWriteCommand:762] C:\d3g-ubuntu.fwdn\boot-firmware\.\prebuilt\scfw.rom
[FWDN_V8::GetFileAndWriteCommand:762] C:\d3g-ubuntu.fwdn\boot-firmware\.\prebuilt\optee.rom
[FWDN_V8::GetFileAndWriteCommand:762] C:\d3g-ubuntu.fwdn\boot-firmware\.\prebuilt\optee.rom
[FWDN_V8::GetFileAndWriteCommand:762] C:\d3g-ubuntu.fwdn\boot-firmware\.\prebuilt\subcore_optee.rom
[FWDN_V8::GetFileAndWriteCommand:762] C:\d3g-ubuntu.fwdn\boot-firmware\.\prebuilt\subcore_optee.rom
[FWDN_V8::GetFileAndWriteCommand:762] C:\d3g-ubuntu.fwdn\boot-firmware\.\prebuilt\ca72_bl1.rom
[FWDN_V8::GetFileAndWriteCommand:762] C:\d3g-ubuntu.fwdn\boot-firmware\.\prebuilt\ca72_bl1.rom
[FWDN_V8::GetFileAndWriteCommand:762] C:\d3g-ubuntu.fwdn\boot-firmware\.\prebuilt\ca53_bl1.rom
[FWDN_V8::GetFileAndWriteCommand:762] C:\d3g-ubuntu.fwdn\boot-firmware\.\prebuilt\ca53_bl1.rom
[FWDN_V8::GetFileAndWriteCommand:762] C:\d3g-ubuntu.fwdn\boot-firmware\.\prebuilt\ca72_bl2.rom
[FWDN_V8::GetFileAndWriteCommand:762] C:\d3g-ubuntu.fwdn\boot-firmware\.\prebuilt\ca72_bl2.rom
[FWDN_V8::GetFileAndWriteCommand:762] C:\d3g-ubuntu.fwdn\boot-firmware\.\prebuilt\ca53_bl2.rom
[FWDN_V8::GetFileAndWriteCommand:762] C:\d3g-ubuntu.fwdn\boot-firmware\.\prebuilt\ca53_bl2.rom
[main:139] Complete write command
[main:156] Complete FWDN
[FWDNLogger::PrintCurTime:112] 25/06/25-10:32:29
100[||||||||||||||||||||||||||||||] 864768/864768
C:\d3g-ubuntu.fwdn>fwdn.exe -w "d3g.fai" --storage emmc --area user
[main:30] FWDN V8 v1.4.11 - 2022.11.14 13:47:30
[FWDN_V8::GetFWDNRomVersion:1588] fwdn.rom version : 23.5.22
[main:131] Start write command
[FWDN_V8::GetFileAndWriteCommand:762] d3g.fai
100% [||||||||||||||||||||||||||||||] 4291763824/4291763824
** When writing FAI files without low-format, there may be garbage values in partition where data is not written.
```

### 1.3.3 D3-G Ubuntu Headless
---
1. 转到下载页面

2. 下载 D3-G Ubuntu Headless 镜像
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/Quick%20Guide/Download%20D3-G%20Ubuntu%20Headless%20Image.png" width="550"></p>
<p align="center"><strong>图 1.8 下载 D3-G Ubuntu Headless 镜像</strong></p> <br/>

3. 单击 fwdn.bat。“fwdn.bat”是使用 ***FWDN V8*** 自动下载固件的可执行文件。 
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/Quick%20Guide/Click%20fwdn_ubuntu_headless.bat.png" width="550"></p>
<p align="center"><strong>图 1.9 单击 fwdn.bat</strong></p> <br/>

```
C:\d3g-ubuntu-headless>fwdn.exe --fwdn boot-firmware\fwdn.json
[main:30] FWDN V8 v1.4.11 - 2022.11.14 13:47:30
[FWDN_V8::GetFWDNRomVersion:1588] fwdn.rom version : 23.5.22
[main:156] Complete FWDN
[FWDNLogger::PrintCurTime:112] 25/06/25-10:28:35

C:\d3g-ubuntu-headless>fwdn.exe --storage emmc --low-format
[main:30] FWDN V8 v1.4.11 - 2022.11.14 13:47:30
[FWDN_V8::GetFWDNRomVersion:1588] fwdn.rom version : 23.5.22
[FWDN_V8::LowformatCommand:1370] Start low-format
[FWDN_V8::LowformatCommand:1371] low-format can take a long time
[FWDN_V8::LowformatCommand:1400] Complete low-format
[main:156] Complete FWDN
[FWDNLogger::PrintCurTime:112] 25/06/25-10:28:36

C:\d3g-ubuntu-headless>fwdn.exe -w boot-firmware\boot.single.json
[main:30] FWDN V8 v1.4.11 - 2022.11.14 13:47:30
[FWDN_V8::GetFWDNRomVersion:1588] fwdn.rom version : 23.5.22
[main:131] Start write command
[FWDN_V8::GetFileAndWriteCommand:762] C:\d3g-ubuntu-headless\boot-firmware\.\prebuilt\bconf.single.bin
[FWDN_V8::GetFileAndWriteCommand:762] C:\d3g-ubuntu-headless\boot-firmware\.\prebuilt\bconf.single.bin
[FWDN_V8::GetFileAndWriteCommand:762] C:\d3g-ubuntu-headless\boot-firmware\.\prebuilt\mcert.bin
[FWDN_V8::GetFileAndWriteCommand:762] C:\d3g-ubuntu-headless\boot-firmware\.\prebuilt\mcert.bin
[FWDN_V8::GetFileAndWriteCommand:762] C:\d3g-ubuntu-headless\boot-firmware\.\prebuilt\dram_params.bin
[FWDN_V8::GetFileAndWriteCommand:762] C:\d3g-ubuntu-headless\boot-firmware\.\prebuilt\dram_params.bin
[FWDN_V8::GetFileAndWriteCommand:762] C:\d3g-ubuntu-headless\boot-firmware\.\prebuilt\hsm.cs.bin
[FWDN_V8::GetFileAndWriteCommand:762] C:\d3g-ubuntu-headless\boot-firmware\.\prebuilt\hsm.cs.bin
[FWDN_V8::GetFileAndWriteCommand:762] C:\d3g-ubuntu-headless\boot-firmware\.\prebuilt\scfw.rom
[FWDN_V8::GetFileAndWriteCommand:762] C:\d3g-ubuntu-headless\boot-firmware\.\prebuilt\scfw.rom
[FWDN_V8::GetFileAndWriteCommand:762] C:\d3g-ubuntu-headless\boot-firmware\.\prebuilt\optee.rom
[FWDN_V8::GetFileAndWriteCommand:762] C:\d3g-ubuntu-headless\boot-firmware\.\prebuilt\optee.rom
[FWDN_V8::GetFileAndWriteCommand:762] C:\d3g-ubuntu-headless\boot-firmware\.\prebuilt\subcore_optee.rom
[FWDN_V8::GetFileAndWriteCommand:762] C:\d3g-ubuntu-headless\boot-firmware\.\prebuilt\subcore_optee.rom
[FWDN_V8::GetFileAndWriteCommand:762] C:\d3g-ubuntu-headless\boot-firmware\.\prebuilt\ca72_bl1.rom
[FWDN_V8::GetFileAndWriteCommand:762] C:\d3g-ubuntu-headless\boot-firmware\.\prebuilt\ca72_bl1.rom
[FWDN_V8::GetFileAndWriteCommand:762] C:\d3g-ubuntu-headless\boot-firmware\.\prebuilt\ca53_bl1.rom
[FWDN_V8::GetFileAndWriteCommand:762] C:\d3g-ubuntu-headless\boot-firmware\.\prebuilt\ca53_bl1.rom
[FWDN_V8::GetFileAndWriteCommand:762] C:\d3g-ubuntu-headless\boot-firmware\.\prebuilt\ca72_bl2.rom
[FWDN_V8::GetFileAndWriteCommand:762] C:\d3g-ubuntu-headless\boot-firmware\.\prebuilt\ca72_bl2.rom
[FWDN_V8::GetFileAndWriteCommand:762] C:\d3g-ubuntu-headless\boot-firmware\.\prebuilt\ca53_bl2.rom
[FWDN_V8::GetFileAndWriteCommand:762] C:\d3g-ubuntu-headless\boot-firmware\.\prebuilt\ca53_bl2.rom
[main:139] Complete write command
[main:156] Complete FWDN
[FWDNLogger::PrintCurTime:112] 25/06/25-10:28:36
100[||||||||||||||||||||||||||||||] 864768/864768
C:\d3g-ubuntu-headless>fwdn.exe -w "d3g.fai" --storage emmc --area user
[main:30] FWDN V8 v1.4.11 - 2022.11.14 13:47:30
[FWDN_V8::GetFWDNRomVersion:1588] fwdn.rom version : 23.5.22
[main:131] Start write command
[FWDN_V8::GetFileAndWriteCommand:762] d3g.fai
100% [||||||||||||||||||||||||||||||] 2594119280/2594119280
** When writing FAI files without low-format, there may be garbage values in partition where data is not written.
```

<br/><br/><br/>

## 1.4 Linux 环境下的 FWDN

### 1.4.1 解压 D3-G 镜像
---
在您的 Linux 系统上解压在第 1.3 节中下载的 D3-G 镜像。

<br/><br/><br/>

### 1.4.2 Telechips USB 设备的 Udev 规则
---
执行以下命令后，在 Linux 中下载 FWDN 时不再需要使用 'sudo' 命令。
```
$ echo "SUBSYSTEM==\"usb\", ATTR{idVendor}==\"140e\", MODE=\"0666\", OWNER=\"${USER}\"" | sudo tee /etc/udev/rules.d/99-topst.rules
$ sudo udevadm control --reload-rules && sudo udevadm trigger
```
<br/><br/><br/>

### 1.4.3 使用 fwdn.sh 烧录 D3-G 镜像
---
要在 Linux 中下载 D3-G 镜像，请执行以下命令："./fwdn.sh"。

```
$ ./fwdn.sh
```

现在您已准备好启动 D3-G。请参阅第 1.5 章以开始与设备进行通信。


<br/><br/><br/><br/>

## 1.5 将 D3-G 开发板与主机 PC 连接
---
本章介绍如何通过 UART 将主机 PC 连接到 D3-G 开发板，以进行固件下载和串行通信。

<br/><br/><br/>

## 1.6 使用 UART 连接 D3-G 开发板 
---
请按照以下步骤操作，并使用 UART 连接验证固件下载是否已成功完成。 

1. 在 Windows 环境中安装串行端口驱动程序（例如 CP210x Windows Driver）和 PL2303_prolific 驱动程序。 
2. 安装终端仿真器，例如 Tera Term 或 PuTTY。 
3. 连接主机 PC 与 D3-G 开发板上的 UART 引脚。请使用 USB-to-TTL 线缆。 
4. 将黑色线缆连接到 GND 引脚。 
5. 将白色线缆 (RXD) 连接到 UART 引脚中的 TX 引脚，将绿色线缆 (TXD) 连接到 UART 引脚中的 RX 引脚。
6. 运行终端仿真器应用程序。
7. 在您的 PC 上打开设备管理器，检查 UART 正在使用的端口号。
8. 将在设备管理器中确认的端口号输入终端仿真器的 Serial line 字段。将 **Speed** (bps) 设置为 115200，并将 **Flow control 设置为 None。**
9. 连接电源线。然后，D3-G 将以默认的 eMMC 启动模式启动。


 
<p align="center">
    <img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20D3-G/Software/USB%20to%20TTL%20Connection.png", width="700">
</p>
<p align="center"><strong>图 1.6 与主机 PC 的 UART 连接</strong></p><br/>  
