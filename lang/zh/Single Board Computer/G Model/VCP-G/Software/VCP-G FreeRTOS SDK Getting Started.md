# 1. 简介
---
本文档提供了搭建 VCP-G SDK 软件开发环境的指南，说明所需的工具、配置和工具链。

</br></br></br></br>

# 2. 设置主机环境
---
## 2.1 安装 Ubuntu
---
建议在 Ubuntu 22.04 上搭建开发环境。该 Ubuntu 版本提供稳定的平台和广泛的社区支持，可确保与 VCP-G 及相关工具链的兼容性和易用性。

Linux 发行版版本：  
- Ubuntu 22.04 (LTS)

</br></br></br>

## 2.2 安装 WSL2 Ubuntu（仅限 Windows 环境）
---
**注意：** 如果使用 Ubuntu 主机，可以跳过 WSL2 的安装。  

1.	依次点击 **控制面板 -> 程序 -> 启用或关闭 Windows 功能 -> 启用虚拟机平台和 Hyper-V** 来设置 Windows 功能。
2.	以 **“以管理员权限运行”.** 的方式执行 Windows Powershell。
3.	启用 WSL2 系统。
    ```
    dism.exe /online /enable-feature /featurename:Microsoft-Windows-Subsystem-Linux /all /norestart
    ```
4.	启用虚拟机功能。
    ```
    dism.exe /online /enable-feature /featurename:VirtualMachinePlatform /all /norestart
    ```
5.	将 WSL 的默认版本设置为 2（WSL2）。
    ```
    wsl --set-default-version 2
    ```
6.	在 Microsoft Store 中搜索 Ubuntu 22.04 LTS 并下载。

    * 如果需要下载 Linux 内核更新包，请从[此处](https://learn.microsoft.com/ko-kr/windows/wsl/install-manual)下载最新的软件包。
7.	在 WSL 列表中确认 Ubuntu 22.04。
    ```
    wsl --list -online
    ```
8.	安装 Ubuntu 22.04。
    ```
    wsl --install Ubuntu-22.04
    ```
9.	在 Windows 搜索框中搜索 WSL2 并执行。 

</br></br></br>

## 2.3 设置 Linux 环境
---
要在主机 PC 上搭建 Linux 环境，请按以下步骤操作：  

1. 执行 WSL2（仅限 Windows 环境）  
    如果使用 Windows，请在 Windows PowerShell 中执行以下命令之一来启动 WSL2。  
    ```
    wsl
    ```
    ```
    ubuntu
    ```

2.	更新软件包列表  
在安装任何新软件之前，请更新可用软件包列表，以确保获取最新的版本和依赖项。以下命令会从软件源获取最新的可用软件包列表。
    ```
    sudo apt update && /
    sudo apt upgrade
    ```

3.	安装常用开发工具  
    输入以下命令安装常用开发工具：
    ```
    sudo apt install build-essential git
    ```

**注意：** 该命令会同时安装 build-essential 软件包和 git。

</br></br></br></br>

# 3. 工具链
---
VCP-G 使用 **gcc-linaro-7.2.1-2017.11-x86_64_arm-eabi** 工具链。  
该工具链针对 ARM 架构进行了优化，可确保与 VCP-G 上的 TCC7045 芯片兼容。

</br></br></br>

## 3.1 安装并设置工具链
---
请按以下步骤下载、解压并设置工具链：  
1. 下载工具链  
   输入 **wget** 命令从 Linaro 网站下载工具链：
    ```
    wget https://releases.linaro.org/components/toolchain/binaries/7.2-2017.11/arm-eabi/gcc-linaro-7.2.1-2017.11-x86_64_arm-eabi.tar.xz
    ```
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/Download%20Toolchain.png"></p>
    <p align="center"><strong>图 3.1 下载工具链</strong></p>
    
2. 解压工具链  
    下载完成后，解压 .tar.xz 文件的内容。
    ```
    tar -xvf gcc-linaro-7.2.1-2017.11-x86_64_arm-eabi.tar.xz
    ```
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/Extract%20Toolchain.png"></p>
    <p align="center"><strong>图 3.2 解压工具链</strong></p>
    
3. 将工具链移动到 /opt  
    /opt 目录是 Linux 上可选软件的标准存放位置。请将解压后的工具链移动到该目录。
    ```
    sudo mv gcc-linaro-7.2.1-2017.11-x86_64_arm-eabi /opt/
    ```
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/Move%20Toolchain.png"></p>
    <p align="center"><strong>图 3.3 移动工具链</strong></p>

</br></br></br>

## 3.2 验证工具链
---
确认工具链已正确安装。  
1. 进入工具链目录
    ```
    cd /opt/gcc-linaro-7.2.1-2017.11-x86_64_arm-eabi
    ```
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/Navigate%20to%20Toolchain%20Directory.png"></p>
    <p align="center"><strong>图 3.4 进入工具链目录</strong></p>
    
2. 检查已安装的 GCC 编译器版本
    ```
    ./bin/arm-eabi-gcc --version
    ```
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/Check%20Version%20of%20Installed%20GCC%20Compiler.png"></p>
    <p align="center"><strong>图 3.5 检查已安装的 GCC 编译器版本</strong></p>

成功安装 GCC 编译器后，请验证已安装的 GCC 编译器版本是否与 **gcc-linaro-7.2.1-2017.11.** 一致。

</br></br></br></br>

# 4. 克隆源代码
---
本章介绍如何使用 Git 克隆源代码。

</br></br></br>

## 4.1 克隆 VCP-G 源代码
---
要获取 VCP-G 的源代码，请输入 **git clone** 命令。该命令会在本地计算机上创建远程仓库的副本，使您可以直接处理代码。

请按以下步骤克隆 VCP-G 源代码：
1. 打开终端  
    在 Ubuntu 22.04 系统上启动终端应用程序。

2. 进入目标目录  
    选择保存源代码的合适位置。例如，如果要将仓库保存在主目录中，请使用以下命令。
    ```
    cd ~
    ```
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/Navigate%20to%20Desired%20Directory.png"></p>
    <p align="center"><strong>图 4.1 进入目标目录</strong></p>

3. 克隆仓库  
    使用以下命令从提供的 git 地址克隆 VCP-G 源代码。
    ```
    git clone https://github.com/topst-development/FreeRTOS-VCP.git topst-vcp
    ```
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/Figure%204.2%20Clone%20Repository.png"></p>
    <p align="center"><strong>图 4.2 克隆仓库</strong></p>

4. 进入克隆的目录  
    克隆完成后，使用以下命令进入包含源代码的目录。
    ```
    cd topst-vcp
    ```
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/Navigate%20to%20Cloned%20Directory.png"></p>
    <p align="center"><strong>图 4.3 进入克隆的目录</strong></p>

现在，VCP-G 源代码已可在本地用于构建和开发。

</br></br></br>

## 4.2 源代码结构
---
克隆完成后，输入 **ls** 命令列出目录内容，并查看关键文件以了解源代码结构。
```
ls

build  documents  easy-setup_vcp.sh  LICENSE  scripts  sources  tools
```

</br></br></br></br>

# 5. 构建指南
---
## 5.1 执行 easy-setup_vcp-g.sh
---
运行 ./easy-setup_vcp-g.sh 脚本后，会显示以下画面。

**警告**：重新运行 ./easy-setup_vcp-g.sh 时请注意，如果选择 yes，已构建的源码将被删除。
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20AI-G/Software/Linux%20SDK/license1.png"></p>
<p align="center"><strong>图 5.1 最终用户许可协议</strong></p>

滚动到屏幕底部并阅读此声明。阅读此声明后，按右箭头键和 [Enter]。
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20AI-G/Software/Linux%20SDK/license2.png"></p>
<p align="center"><strong>图 5.2 转到 'Proceed to confirm'</strong></p>


随后可以看到以下画面。 
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20AI-G/Software/Linux%20SDK/license3.png" ></p>
<p align="center"><strong>图 5.3 接受画面 </strong></p>
按 [Enter] 选择 Accept 后，即可使用以下命令进行构建。

</br></br></br>

## 5.2 Makefile 与构建系统
---
Makefile 是许多构建系统的关键组成部分，其中包含供 **make** 工具编译和链接程序的规则与指令。利用 Makefile 可以实现构建过程自动化，确保一致性和效率。

</br></br></br>

## 5.3 启动构建过程
---
要构建源代码，请按以下步骤操作：  
1. 进入构建目录。
    ```
    cd build/tcc70xx/gcc/
    ```
2. 运行 **make** 命令。  
    ```
    make
    ```
    **make** 命令会读取当前目录中的 Makefile 并执行构建过程。
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/Run%20make%20Command.png"></p>
    <p align="center"><strong>图 5.4 运行 make 命令 </strong></p>
    
3. 验证构建输出  
    构建过程完成后，终端中应列出以下输出文件。
    - output/tcc70xx_pflash_boot.rom
    - output/tcc70xx_pflash_boot_2M_ECC.rom
    - output/tcc70xx_pflash_boot_3M_ECC.rom
    - output/tcc70xx_pflash_boot_4M_ECC.rom
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/Verify%20Build%20Output.png"></p>
    <p align="center"><strong>图 5.5 验证构建输出</strong></p>
   
    要查看输出文件列表，请使用以下命令：
    ```
    ls output/ -al
    ```
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/Build%20Output%20File.png"></p>
    <p align="center"><strong>图 5.6 构建输出文件</strong></p>

</br></br></br></br>

# 6. 固件下载
---
本章介绍如何在基于 Linux 的开发环境中将 ***FWDN*** 下载到 VCP-G。

</br></br></br>

## 6.1 准备 VCP-G
---
开始下载之前，请确保 VCP-G 放置稳固且不受任何潜在干扰。确保所有开关和连接器易于操作，并且 3.3V 电源线连接正确。

</br></br></br>

## 6.2 将硬件连接到主机 PC
---
如果使用 Ubuntu 主机，请直接进入步骤 3。  
1. 下载 usbipd-win  
    在 WSL2 中使用 USB 需要 usbipd-win 项目。   
    请从以下链接下载 usbipd-win：https://learn.microsoft.com/ko-kr/windows/wsl/connect-usb#attach-a-usb-device。
2. 运行 PowerShell，将 VCP-G（在 Windows 中被识别为 COM 端口）连接到 WSL2  
    请在 Windows PowerShell（而非 Linux）中执行以下命令。
    ```
    usbipd list
    ```
    ```
    usbipd bind --busid <busid>
    ```
    ```
    usbipd attach --wsl --busid <busid>
    ```
3. 连接 USB Type-C 线缆  
    使用 USB Type-C 线缆将 VCP-G 开发板连接到开发主机 PC。
4. 验证 USB 连接  
    在 WSL2 中执行以下命令。
    ```
    sudo apt-get install usbutils && lsusb
    ```
    ```
    sudo dmesg | grep tty
    ```
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/Verify%20USB%20Connection.png"></p>
    <p align="center"><strong>图 6.1 验证 USB 连接</strong></p>

如果显示图 6.1 所示的输出，则表示连接已成功建立。

</br></br></br>

## 6.3 将软件下载到 VCP-G
---

### 6.3.1 在 Windows 环境中执行 FWDN
1. 将开发板设置为下载模式  
   按住 FWDN 开关的同时，将电源线连接到 VCP-G 开发板。
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/Set%20Board%20to%20Download%20Mode.png"></p>
    <p align="center"><strong>图 6.2 将开发板设置为下载模式</strong></p>

2. 将 tcc70xx_pflash_boot_2M_ECC.rom 复制到 fwdn_vcp 文件夹
```
cp ~/topst-vcp/build/tcc70xx/gcc/output/tcc70xx_pflash_boot_2M_ECC.rom ~/topst-vcp/tools/fwdn_vcp/
```

3. 将 fwdn_vcp 文件夹复制到 C 盘
```
cp -r ~/topst-vcp/tools/fwdn_vcp /mnt/c/
```

4. 点击 fwdn_vcp.bat  
    使用 ***FWDN*** 将构建好的软件下载到 VCP-G 上的 4 MB 闪存中。

    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/Click%20fwdn_vcp.bat.png"></p>
    <p align="center"><strong>图 6.3 点击 fwdn_vcp.bat</strong></p>
```
[main:27] FWDN VCP v0.1.1 - 2022.8.12 11:38:19
Com port num : 10
[FWDNWindowsUART::OpenPort:34] Complete open port(\\.\COM10)
[ProtocolCB::StartVCPFWDN:45] Complete to receive start res
[FWDN_VCP::LoadFwdnFW:144] Complete to send start msg
[ProtocolCB::CheckResPacket:172] Complete to receive ack for cmd(0xFFFF0000(RECEIVE_HSM_CMD))
[FWDN_VCP::WriteFile:284] Complete to send command(0xFFFF0000(RECEIVE_HSM_CMD))
[ProtocolCB::SendFile:151] Complete to send file
[ProtocolCB::CheckResPacket:172] Complete to receive ack for cmd(0xFFFF0000(RECEIVE_HSM_CMD))
[FWDN_VCP::WriteFile:295] Complete to send file - .\tcc70xx_pflash_boot_2M_ECC.rom
[FWDN_VCP::LoadFwdnFW:163] Complete to send hsm
[ProtocolCB::CheckResPacket:172] Complete to receive ack for cmd(0xFFFF0001(RECEIVE_FWDN_CMD))
[FWDN_VCP::WriteFile:284] Complete to send command(0xFFFF0001(RECEIVE_FWDN_CMD))
[ProtocolCB::SendFile:126] uiRemainSize = 43136
[ProtocolCB::SendFile:151] Complete to send file
[ProtocolCB::CheckResPacket:172] Complete to receive ack for cmd(0xFFFF0001(RECEIVE_FWDN_CMD))
[FWDN_VCP::WriteFile:295] Complete to send file - .\vcp_fwdn.rom
[FWDN_VCP::LoadFwdnFW:173] Complete to send fwdn
[FWDN_VCP::LoadFwdnFW:179] Complete to load FWDN F/W
RM=00000000
MT
MR0=0000a042
MR1=00020018
MR2=00000000
[ProtocolFW::CheckResPacket:260] Complete to receive ack for cmd(0xAAAA0016(VERSION_CMD))
[FWDN_VCP::GetDeviceVersion:77]  FWDN Firmware Version(20230728)
[ProtocolFW::CheckResPacket:260] Complete to receive ack for cmd(0xAAAA0014(STORAGE_INFO_CMD))
[FWDN_VCP::InfoStorage:56]
#### SNOR Info ####
Manufacture ID: 0x9d
Device ID: 0x6015
Name: ISSI-IS25LP016D
Sector Size: 4 KiB (4096 Byte)
Total Capacity: 2 MiB (2097152 Byte)
4Byte Address Mode: Unsupported
#### EFLASH Info ####
DCYCRDCON 0x1e0002
DCYCWRCON 0x20100
Sector Size: 8 KiB
Page Size: 2 KiB

-----Storage init info-----
O : Init success
X : Init failed or not exist
SNOR : O
eFlash : O

[ProtocolFW::CheckResPacket:260] Complete to receive ack for cmd(0xAAAA0017(CHIP_INFO_CMD))
[FWDN_VCP::GetChipInfo:121] ---chip info---
Chip Number : 0x57045
Dual Bank : false
Expand Flash : true
ECC : true
[FWDN_VCP::PrintBankInfo:468] ---bank info---
bank - 0
eFlash offset : 0x0
eFlash size : 2097152 byte
SNOR offset : 0x0
SNOR size : 2097152 byte
[FWDN_VCP::PrintStorageOption:451] ---storage info---
eflash
offset : 0x0
size : 2097152 byte
[ProtocolFW::CheckResPacket:260] Complete to receive ack for cmd(0xAAAA0011(WRITE_CMD))
[FWDN_VCP::WriteFile:284] Complete to send command(0xAAAA0011(WRITE_CMD))
 100% [||||||||||||||||||||||||||||||] 2097152/2097152
```

5. 复位开发板  
    下载过程完成后，断开电源线并重新连接。
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/Reset%20the%20Board.png"></p>
    <p align="center"><strong>图 6.4 复位开发板</strong></p>

### 6.3.2 在 Linux 环境下执行 FWDN
1. 将开发板设置为下载模式  
   按住 FWDN 开关的同时，将电源线连接到 VCP-G 开发板。
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/Set%20Board%20to%20Download%20Mode.png"></p>
    <p align="center"><strong>图 6.5 将开发板设置为下载模式</strong></p>
    
2. 执行下载命令  
   使用 ***FWDN*** 将构建好的软件下载到 VCP-G 上的 4 MB 闪存中。
    ```
    sudo ~/topst-vcp/tools/fwdn_vcp/fwdn --fwdn ~/topst-vcp/tools/fwdn_vcp/vcp_fwdn.rom -w output/tcc70xx_pflash_boot_2M_ECC.rom
    ```
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/Execute%20Download%20Command.png"></p>
    <p align="center"><strong>图 6.6 执行下载命令</strong></p>
    
3. 复位开发板  
    下载过程完成后，断开电源线并重新连接。
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/Reset%20the%20Board.png"></p>
    <p align="center"><strong>图 6.7 复位开发板</strong></p>

</br></br></br>

## 6.4 验证开发板上的软件
---
将软件下载到开发板后，请按以下步骤验证其是否正常运行。
1. 安装 minicom  
    ```
    sudo apt install minicom
    ```
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/Install%20Minicom.png"></p>
    <p align="center"><strong>图 6.8 安装 minicom</strong></p>
2. 打开串口连接  
    使用以下命令建立串口连接。
    ```
    minicom -D /dev/ttyUSB0 -b 115200 -8
    ```
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/Open%20Serial%20Connection.png"></p>
    <p align="center"><strong>图 6.9 打开串口连接</strong></p>

完成步骤 1 和步骤 2 后，终端上会显示以下输出。如果连接成功，开发板会响应操作，即可确认软件已下载到 VCP-G 并正常运行。
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/Figure%206.7%20Open%20Serial%20Connection.png"></p>
<p align="center"><strong>图 6.10 打开串口连接</strong></p>

</br></br></br>

## 6.5 常见问题排查
---
本章提供使用 VCP-G 时遇到的常见问题的解决方法。

**问题：** ***FWDN*** 报告没有访问 ttyUSB0 设备的权限。  
**解决方法：** 该问题在您的用户账户（**$USER**）不具备访问串口设备所需权限时发生。要解决此问题，请将该用户账户添加到 dialout 组中。

1. 修改用户组权限  
    执行以下命令。
    ```
    sudo usermod -aG dialout $USER
    ```
2. 注销并重新登录  
    注销当前会话并重新登录以使更改生效。之后，请再次尝试访问 ttyUSB0 设备。
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/Modify%20User%20Group%20Permissions.png"></p>
    <p align="center"><strong>图 6.11 修改用户组权限 </strong></p>

**问题：** 使用 minicom 时，与 VCP-G 无法正常通信或出现异常行为。  
**解决方法：** 该问题可能在 minicom 的默认流控制设置为 **hardware** 时发生。为使其正常工作，必须将硬件流控制设置为 No。 
1. 启动 minicom  
    使用以下命令。
    ```
    minicom -D /dev/ttyUSB0 -b 115200 -8
    ```
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/Launch%20Minicom.png"></p>
    <p align="center"><strong>图 6.12 启动 minicom</strong></p>
2. 进入设置界面  
    在 minicom 中，按 **[Ctrl+A]**，然后按 **[o]** 打开设置菜单。
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/Access%20Set%20up%20Screen.png"></p>
    <p align="center"><strong>图 6.13 进入设置界面</strong></p>
3. 进入 Serial port setup  
    在选项中选择 **Serial port setup**。
4. 修改流控制  
    在串口设置中，按 **[F]** 将硬件流控制设置为 **No**。
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/Modify%20Flow%20Control.png"></p>
    <p align="center"><strong>图 6.14 修改流控制</strong></p>
5. 退出并保存  
    退出设置并保存配置。此时 minicom 应能与 VCP-G 正常通信。
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/Save%20and%20Exit.png"></p>
    <p align="center"><strong>图 6.15 保存并退出</strong></p>

**注意：** 如果您使用 minicom 以外的其他串口通信工具，请同样将其流控制设置为 **No**，以确保正常工作。
</br></br></br></br>

# 7. 参考资料
---
- 有关更多详细信息，请联系 TOPST：topst@topst.ai

**注意：** 参考文档可根据合同条款在可提供时提供。如果参考
文档无法提供，则可就与您的开发直接相关的内容提供指导。
