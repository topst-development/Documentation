# 1. Introduction
---
This document provides guidelines for setting up a software development environment for the VCP-G SDK. It outlines the required tools, configurations, and toolchain.

</br></br></br></br>

# 2. Setting Host Environment
---
## 2.1 Install Ubuntu
---
It is recommended to set up your development environment on Ubuntu 22.04. This Ubuntu version offers a stable platform with wide community support, ensuring compatibility and ease of use with the VCP-G and associated toolchain.

Linux distribution version:  
- Ubuntu 22.04 (LTS)

</br></br></br>

## 2.2 Install WSL2 Ubuntu (Windows Environment Only)
---
**Note:** If you using Ubuntu host, you can skip installing WSL2.  

1.	Set Windows Features by clicking **Control Panel -> Programs -> Windows Features On/Off -> Enable Virtual Machine Platform & Hyper-V**.
2.	Execute Windows Powershell with **“Run with administrator privileges”.**
3.	Enable the WSL2 System.
    ```
    dism.exe /online /enable-feature /featurename:Microsoft-Windows-Subsystem-Linux /all /norestart
    ```
4.	Enable the Virtual Machine feature.
    ```
    dism.exe /online /enable-feature /featurename:VirtualMachinePlatform /all /norestart
    ```
5.	Set WSL to the default version of 2 (WSL2).
    ```
    wsl --set-default-version 2
    ```
6.	Search for Ubuntu 22.04 LTS in Microsoft Store and download it.

    * If you need to download the Linux kernel update package, download the latest package [here](https://learn.microsoft.com/ko-kr/windows/wsl/install-manual).
7.	Check Ubuntu 22.04 in the WSL list.
    ```
    wsl --list -online
    ```
8.	Install Ubuntu 22.04.
    ```
    wsl --install Ubuntu-22.04
    ```
9.	Search for WSL2 in the Windows search box and execute it. 

</br></br></br>

## 2.3 Setting Linux Environment
---
To set up a Linux environment on your host PC, follow these steps:  

1. Execute WSL2 (Windows Environment Only)  
    If you are using Windows, start WSL2 by executing one of the following commands in Windows PowerShell.  
    ```
    wsl
    ```
    ```
    ubuntu
    ```

2.	Update Package List  
Before installing any new software, update the list of available packages to ensure you get the latest versions and dependencies. The following command fetches the latest list of available packages from the repositories.
    ```
    sudo apt update && /
    sudo apt upgrade
    ```

3.	Install Common Development Tools  
    Install common development tools by entering the following command:
    ```
    sudo apt install build-essential git
    ```

**Note:** This command installs both the build-essential package and git.

</br></br></br></br>

# 3. Toolchain
---
The VCP-G uses the **gcc-linaro-7.2.1-2017.11-x86_64_arm-eabi** toolchain.  
This toolchain is optimized for the ARM architecture and ensures compatibility with the TCC7045 chip on the VCP-G.

</br></br></br>

## 3.1 Install and Set Up Toolchain
---
Follow these steps to download, extract, and set up the toolchain:  
1. Download the Toolchain  
   Enter **wget** command to download the toolchain from the Linaro website:
    ```
    wget https://releases.linaro.org/components/toolchain/binaries/7.2-2017.11/arm-eabi/gcc-linaro-7.2.1-2017.11-x86_64_arm-eabi.tar.xz
    ```
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/Download%20Toolchain.png"></p>
    <p align="center"><strong>Figure 3.1 Download Toolchain</strong></p>
    
2. Extract the Toolchain  
    After the download is complete, extract the contents of the .tar.xz file.
    ```
    tar -xvf gcc-linaro-7.2.1-2017.11-x86_64_arm-eabi.tar.xz
    ```
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/Extract%20Toolchain.png"></p>
    <p align="center"><strong>Figure 3.2 Extract Toolchain</strong></p>
    
3. Move the Toolchain to /opt  
    The /opt directory is a standard location for optional software on Linux. Move the extracted toolchain to this directory.
    ```
    sudo mv gcc-linaro-7.2.1-2017.11-x86_64_arm-eabi /opt/
    ```
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/Move%20Toolchain.png"></p>
    <p align="center"><strong>Figure 3.3 Move Toolchain</strong></p>

</br></br></br>

## 3.2 Verify Toolchain
---
To ensure that the toolchain is installed correctly.  
1. Navigate to the Toolchain Directory
    ```
    cd /opt/gcc-linaro-7.2.1-2017.11-x86_64_arm-eabi
    ```
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/Navigate%20to%20Toolchain%20Directory.png"></p>
    <p align="center"><strong>Figure 3.4 Navigate to Toolchain Directory</strong></p>
    
2. Check the Version of the Installed GCC Compiler
    ```
    ./bin/arm-eabi-gcc --version
    ```
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/Check%20Version%20of%20Installed%20GCC%20Compiler.png"></p>
    <p align="center"><strong>Figure 3.5 Check Version of Installed GCC Compiler</strong></p>

After successfully installing the GCC Compiler, verify the installed GCC compiler version to ensure it matches **gcc-linaro-7.2.1-2017.11.**

</br></br></br></br>

# 4. Clone Source Code
---
This chapter describes how to clone the source code using Git.

</br></br></br>

## 4.1 Clone VCP-G Source Code
---
To obtain the source code for the VCP-G, enter the **git clone** command. This command creates a copy of the remote repository on your local machine, allowing you to work with the code directly.

Follow these steps to clone the VCP-G source code:
1. Open Terminal  
    Launch the terminal application on your Ubuntu 22.04 system.

2. Navigate to the desired directory  
    Choose a suitable location to save the source code. For example, if you want to save the repository in the home directory, use the following command.
    ```
    cd ~
    ```
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/Navigate%20to%20Desired%20Directory.png"></p>
    <p align="center"><strong>Figure 4.1 Navigate to Desired Directory</strong></p>

3. Clone the Repository  
    Use the following command to clone the VCP-G source code from the provided git address.
    ```
    git clone https://github.com/topst-development/FreeRTOS-VCP.git topst-vcp
    ```
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/Figure%204.2%20Clone%20Repository.png"></p>
    <p align="center"><strong>Figure 4.2 Clone Repository</strong></p>

4. Navigate to the Cloned Directory  
    After the cloning process is complete, use the following command to navigate to the directory containing the source code.
    ```
    cd topst-vcp
    ```
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/Navigate%20to%20Cloned%20Directory.png"></p>
    <p align="center"><strong>Figure 4.3 Navigate to Cloned Directory</strong></p>

The VCP-G source code is now available locally for building and development.

</br></br></br>

## 4.2 Source Code Structure
---
After cloning, enter the **ls** command to list the directory contents and review key files to understand the source code structure.
```
ls

build  documents  easy-setup_vcp.sh  LICENSE  scripts  sources  tools
```

</br></br></br></br>

# 5. Build Guide
---
## 5.1 Execute easy-setup_vcp-g.sh
---
If you run ./easy-setup_vcp-g.sh script, you can see the following screen.

**Caution**: If you re-run ./easy-setup_vcp-g.sh, be careful as the built sources will be deleted if you select yes.
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20AI-G/Software/Linux%20SDK/license1.png"></p>
<p align="center"><strong>Figure 5.1 End User License Agreement</strong></p>

Scroll down to the bottom of the screen and read this notice. After you read this notice, press the right arrow key and [Enter].
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20AI-G/Software/Linux%20SDK/license2.png"></p>
<p align="center"><strong>Figure 5.2 Go To 'Proceed to confirm'</strong></p>


Then you can see the following screen. 
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20AI-G/Software/Linux%20SDK/license3.png" ></p>
<p align="center"><strong>Figure 5.3 Accept Screen </strong></p>
If you select Accept by pressing [Enter], you can build by using the following command.

</br></br></br>

## 5.2 Makefiles and Build Systems
---
A Makefile is a key component of many build systems. It contains rules and directives for the **make** utility to compile and link programs. By utilizing a Makefile, you can automate the build process, ensuring consistency and efficiency.

</br></br></br>

## 5.3 Initiate Build Process
---
To build the source code, follow these steps:  
1. Navigate to the build directory.
    ```
    cd build/tcc70xx/gcc/
    ```
2. Run the **make** command.  
    ```
    make
    ```
    The **make** command reads the Makefile in the current directory and executes the build process.
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/Run%20make%20Command.png"></p>
    <p align="center"><strong>Figure 5.4 Run make Command </strong></p>
    
3. Verify the Build Output  
    After the build process is completed, the following output files should be listed in the terminal.
    - output/tcc70xx_pflash_boot.rom
    - output/tcc70xx_pflash_boot_2M_ECC.rom
    - output/tcc70xx_pflash_boot_3M_ECC.rom
    - output/tcc70xx_pflash_boot_4M_ECC.rom
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/Verify%20Build%20Output.png"></p>
    <p align="center"><strong>Figure 5.5 Verify Build Output</strong></p>
   
    To check the list of output files, use the following command:
    ```
    ls output/ -al
    ```
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/Build%20Output%20File.png"></p>
    <p align="center"><strong>Figure 5.6 Build Output File</strong></p>

</br></br></br></br>

# 6. Firmware Download
---
This chapter describes how to download ***FWDN*** to the VCP-G in a Linux-based development environment.

</br></br></br>

## 6.1 Prepare VCP-G
---
Before beginning the download process, ensure that the VCP-G is in a stable position and free from any potential disturbances. Ensure that all switches and connectors are easily accessible and the 3.3V power cable is connected correctly.

</br></br></br>

## 6.2 Connect Hardware to Host PC
---
If you use Ubuntu host, proceed directly to step 3.  
1. Download usbipd-win  
    usbipd-win project is required to use USB in WSL2.   
    Download usbipd-win from https://learn.microsoft.com/ko-kr/windows/wsl/connect-usb#attach-a-usb-device.
2. Run PowerShell and attach the VCP-G (recognized as a COM port in Windows) to WSL2  
    Execute the following commands in Windows PowerShell (not Linux).
    ```
    usbipd list
    ```
    ```
    usbipd bind --busid <busid>
    ```
    ```
    usbipd attach --wsl --busid <busid>
    ```
3. Connect USB Type-C Cable  
    Use a USB Type-C cable to connect the VCP-G board to the development host PC.
4. Verify USB Connection  
    In WSL2, execute the following commands.
    ```
    sudo apt-get install usbutils && lsusb
    ```
    ```
    sudo dmesg | grep tty
    ```
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/Verify%20USB%20Connection.png"></p>
    <p align="center"><strong>Figure 6.1 Verify USB Connection</strong></p>

If the output displayed in Figure 6.1 appears, the connection is successfully established.

</br></br></br>

## 6.3 Download Software on VCP-G
---

### 6.3.1 Execute FWDN in Windows Environment
1. Set the Board to Download Mode  
   Connect the power cable to the VCP-G board while pressing the FWDN switch.
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/Set%20Board%20to%20Download%20Mode.png"></p>
    <p align="center"><strong>Figure 6.2 Set Board to Download Mode</strong></p>

2. Copy tcc70xx_pflash_boot_2M_ECC.rom to fwdn_vcp folder
```
cp ~/topst-vcp/build/tcc70xx/gcc/output/tcc70xx_pflash_boot_2M_ECC.rom ~/topst-vcp/tools/fwdn_vcp/
```

3. Copy fwdn_vcp folder to C Drive
```
cp -r ~/topst-vcp/tools/fwdn_vcp /mnt/c/
```

4. Click fwdn_vcp.bat  
    Use ***FWDN*** to download the built software to the 4 MB flash on the VCP-G.

    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/Click%20fwdn_vcp.bat.png"></p>
    <p align="center"><strong>Figure 6.3 Click fwdn_vcp.bat</strong></p>
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

5. Reset the board  
    After the download process is completed, disconnect and reconnect the power cable.
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/Reset%20the%20Board.png"></p>
    <p align="center"><strong>Figure 6.4 Reset Board</strong></p>

### 6.3.2 Execute FWDN in Linux Environment
1. Set the Board to Download Mode  
   Connect the power cable to the VCP-G board while pressing the FWDN switch.
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/Set%20Board%20to%20Download%20Mode.png"></p>
    <p align="center"><strong>Figure 6.5 Set Board to Download Mode</strong></p>
    
2. Execute the Download Command  
   Use ***FWDN*** to download the built software to the 4 MB flash on the VCP-G.
    ```
    sudo ~/topst-vcp/tools/fwdn_vcp/fwdn --fwdn ~/topst-vcp/tools/fwdn_vcp/vcp_fwdn.rom -w output/tcc70xx_pflash_boot_2M_ECC.rom
    ```
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/Execute%20Download%20Command.png"></p>
    <p align="center"><strong>Figure 6.6 Execute Download Command</strong></p>
    
3. Reset the board  
    After the download process is completed, disconnect and reconnect the power cable.
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/Reset%20the%20Board.png"></p>
    <p align="center"><strong>Figure 6.7 Reset Board</strong></p>

</br></br></br>

## 6.4 Verify Software on Board
---
After downloading the software to the board, follow these steps to verify that it is operating correctly.
1. Install minicom  
    ```
    sudo apt install minicom
    ```
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/Install%20Minicom.png"></p>
    <p align="center"><strong>Figure 6.8 Install minicom</strong></p>
2. Open a Serial Connection  
    Use the following command to initiate a serial connection.
    ```
    minicom -D /dev/ttyUSB0 -b 115200 -8
    ```
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/Open%20Serial%20Connection.png"></p>
    <p align="center"><strong>Figure 6.9 Open Serial Connection</strong></p>

After completing steps 1 and 2, the following output appears on the terminal. If the connection is successful, the board should respond to interactions, confirming that the software is downloaded and is operating correctly on the VCP-G.
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/Figure%206.7%20Open%20Serial%20Connection.png"></p>
<p align="center"><strong>Figure 6.10 Open Serial Connection</strong></p>

</br></br></br>

## 6.5 Troubleshooting Common Issues
---
This chapter provides solutions to common issues encountered while working with the VCP-G.

**Issue:** The ***FWDN*** reports a lack of permission to access the ttyUSB0 device.  
**Solution:** This issue occurs when your user account (**$USER**) does not have the necessary permissions to access serial devices. To resolve this, add the user account to the dialout group.

1. Modify User Group Permissions  
    Execute the following command.
    ```
    sudo usermod -aG dialout $USER
    ```
2. Log Out and Log Back In  
    Log out of the current session and log back in to apply the changes. After this, try accessing the ttyUSB0 device again.
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/Modify%20User%20Group%20Permissions.png"></p>
    <p align="center"><strong>Figure 6.11 Modify User Group Permissions </strong></p>

**Issue:** When using minicom, there is no proper communication or irregular behavior with the VCP-G.  
**Solution:** This issue may occur if minicom’s default flow control setting is set to **hardware**. The hardware flow control must be set to No for proper operation. 
1. Start minicom  
    Use the following command.
    ```
    minicom -D /dev/ttyUSB0 -b 115200 -8
    ```
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/Launch%20Minicom.png"></p>
    <p align="center"><strong>Figure 6.12 Launch minicom</strong></p>
2. Access the Setup Screen  
    While in minicom, press **[Ctrl+A]** then press **[o]** to open the setup menu.
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/Access%20Set%20up%20Screen.png"></p>
    <p align="center"><strong>Figure 6.13 Access Setup Screen</strong></p>
3. Navigate to Serial Port Setup  
    Select **Serial port setup** from the options.
4. Modify Flow Control  
    Inside the serial port setup, press **[F]** to set the hardware flow control to **No**.
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/Modify%20Flow%20Control.png"></p>
    <p align="center"><strong>Figure 6.14 Modify Flow Control</strong></p>
5. Exit and Save  
    Exit the setup and save the configuration. minicom should now communicate properly with the VCP-G.
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/Save%20and%20Exit.png"></p>
    <p align="center"><strong>Figure 6.15 Save and Exit</strong></p>

**Note:** If you are using a different serial communication tool other than minicom, ensure its flow control setting is also set to **No** for proper operation.
</br></br></br></br>

# 7. References
---
- Contact TOPST for more details: topst@topst.ai

**Note:** Reference documents can be provided whenever available, depending on the terms of a contract. If the reference
documents are unavailable, the contents directly related to your development can be guided.
