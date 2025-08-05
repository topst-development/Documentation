# AI-G Quick Guide
---

## 1.1 USB Boot Mode (FWDN Mode) 
---
You can transfer the built image to AI-G by using ***FWDN***. AI-G provides ***FWDN*** by using Ethernet and UART. 

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20AI-G/Software/Linux%20SDK/3.%20connect%20host%20pc%20to%20topst%20ai-g.png" ></p>
<p align="center"><strong>Figure 1.1 Connection Between Host PC and AI-G for FWDN</strong></p><br/>

To use ***FWDN V8***, connect the AI-G board to the Host PC as follows: 

1. Check that VTC driver is installed on the Host PC. If the VTC driver is not installed, install it as shown in Chapter 4.2.1.  

2. Prepare one USB Type-C cable and one Ethernet Cable. 

3. To enter USB Boot mode, connect the USB Type-C cable to the USB Type-C FWDN Port on the AI-G board and the Host PC. 

4. Connect the Ethernet Cable (RJ45) to the Ethernet port on the AI-G board and the Host PC. 

5. Connect the power cable to the AI-G board while pressing the FWDN switch. 

<br/><br/><br/>

## 1.2 How to install VCP Driver

Install the Vendor Telechips Certification (VTC) driver (found on [VCP driver](https://drive.google.com/file/d/1muQnY8kuKxDsy3p3FUiQqcG34Zjk-mnR/view?usp=sharing)) on the host PC by running as administrator. When you connect the USB in the FWDN mode as shown above, the Telechips VTC USB driver is set as shown in Figure 1.2.

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20AI-G/Software/Linux%20SDK/4.%20VTC.png" width="550"></p>
<p align="center"><strong>Figure 1.2 Check COM Port</strong></p><br/>

<br/><br/>

## 1.3 Set Up Ethernet

Host PC Network Configuration 

- Control Panel → Network and Internet → Network Connectivity → Set Ethernet device properties for FWDN 
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20AI-G/Software/Linux%20SDK/5.%20network_setting.png"></p>
<p align="center"><strong>Figure 1.3 Setting Ethernet Device Properties for FWDN</strong></p><br/>
<br/><br/><br/>

## 1.4 Add WMIC
Before FWDN, WMIC must be installed to know the port connected to the FWDN port of the AI-G board.

1. Open Settings: Open Settings from the Start menu.
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20AI-G/Software/Linux%20SDK/8.%20Open%20Settings%20from%20Start%20menu.png"></p>
<p align="center"><strong>Figure 1.4 Open Settings from Start menu</strong></p>  <br/>

2. Select System: Go to the System menu.
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20AI-G/Software/Linux%20SDK/9.%20Go%20to%20the%20System%20menu.png"></p>
<p align="center"><strong>Figure 1.5 Go to the System menu</strong></p>  <br/>

3. Selective Features: Click the Selective Features menu.
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20AI-G/Software/Linux%20SDK/10.%20Click%20the%20Selective%20Features%20menu.png"></p>
<p align="center"><strong>Figure 1.6 Click the Selective Features menu</strong></p>  <br/>

4. View Features: Click the **View Features** button next to **Add Optional Features**.
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20AI-G/Software/Linux%20SDK/11.%20Click%20the%20View%20Features%20button%20next%20to%20Add%20optional%20Features.png"></p>
<p align="center"><strong>Figure 1.7 Click the View Features button next to Add Optional Features</strong></p>  <br/>

5. WMIC Search: Type **"WMIC"** in the search box.
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20AI-G/Software/Linux%20SDK/12.%20Type%20WMIC%20in%20the%20search%20box.png"></p>
<p align="center"><strong>Figure 1.8 Type WMIC in the search box</strong></p>  <br/>

6. Install: Select the WMIC item and click the **"Next"** button to complete the installation.
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20AI-G/Software/Linux%20SDK/13.%20Select%20the%20WMIC%20item%20and%20click%20the%20Next%20button%20to%20complete%20the%20installation.png"></p>
<p align="center"><strong>Figure 1.9 Select the WMIC item and click the next button to complete the installation</strong></p>  <br/>

## 1.5 Execute FWDN in Windows Environment
1. Go to Downloads Page

2. Download AI-G Yocto Image
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/Quick%20Guide/Download%20AI-G%20Image.png" width="550"></p>
<p align="center"><strong>Figure 1.10 Download AI-G Yocto Image</strong></p> <br/>

3. Click fwdn_aig.bat. The “fwdn_aig.bat” is an executable file that automatically downloads firmware by using ***FWDN V8***. 
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/Quick%20Guide/Click%20fwdn_aig.bat.png" width="550"></p>
<p align="center"><strong>Figure 1.11 Click fwdn_aig.bat</strong></p> <br/>

```
TOPST AI-G FWDN Batch File

Find Port.
Silicon Labs CP210x USB to UART Bridge(COM44)

Input USB Port Number : 44


Step 1. Connect between Host PC and TOPST AI-G
[FWDNLogger::PrintCurTime:100] 25/06/12-16:11:36
[main:24] FWDN N-Dolphin v1.0.1 - 2024.9.24 16:18:11
[main:92] Start FWDN
[FWDN_ND::ImageSend:442] Complete to send MCERT image
[FWDN_ND::ImageSend:442] Complete to send HSM image
[FWDN_ND::ImageSend:442] Complete to send FWDN_BL1 image
[FWDN_ND::ImageSend:442] Complete to send FWDN_DRAM_PARAMETER image
[FWDN_ND::ImageSend:442] Complete to send FWDN_BL2 image
[FWDN_ND::ImageSend:442] Complete to send FWDN_BL3 image
[FWDN_ND::InfoDevice:123] ############## Device Info ##############
[PrintIP:527] ip      : 192.168.0.100
[PrintIP:527] mask    : 255.255.255.0
[PrintIP:527] gateway : 0.0.0.0
[FWDN_ND::InfoDevice:132] port : 8080
[FWDN_ND::InfoDevice:135]
mmc0_user: 7818182656 byte block_size: 512 byte
mmc0_boot0: 4194304 byte block_size: 512 byte
mmc0_boot1: 4194304 byte block_size: 512 byte
snor1: 0 byte
snor2: 0 byte
fw_version: tcc750x_v0.0.111
fw_build_id: g90e2b777
fw_build_date: 2024-09-24-17:11:42+0900

----- Firmware Information -----
VERSION    : tcc750x_v0.0.111
BUILD ID   : g90e2b777
BUILD DATE : 2024-09-24-17:11:42+0900

----- Detail of Storages -----
#### eMMC Info ####
Manufacture ID: 0x15
OEM: 0x100
Name: 0x8GTF4
User Capacity: 7.3 GiB (7818182656 Byte)
Boot Capacity: 4 MiB (4194304 Byte)
RPMB Capacity: 512 KiB (524288 Byte)
Speed Mode: HS200
#### SNOR Info ####

----- Summary of Storages -----
eMMC : O
SNOR : X
- O : Init success
- X : Init failed or not exist

----- Summary of DRAM Init -----
DRAM Init : Success
DRAM Size : TBD MB

----- PMU Status -----
PMU_USER   : 0x0
PMU_SIC_USER   : 0x80
PMU_CONFIG : 0x0
* BM : PMU_CONFIG[1:0]
-  0 : USB BOOT
-  1 : SNOR BOOT
-  2 : eMMC BOOT
-  3 : eMMC with SIC BOOT

--------------------------------

[FWDN_ND::LoadFwdnFW:676] TCP Ready OK
[main:156] Complete FWDN, Total Time = 18424 ms
[main:162] **Notification : For more detailed FWDN Log, use the -g or --debug option.

Step 2. Low-format
[FWDNLogger::PrintCurTime:100] 25/06/12-16:11:55
[main:24] FWDN N-Dolphin v1.0.1 - 2024.9.24 16:18:11
[main:92] Start FWDN
[FWDN_ND::InfoDevice:123] ############## Device Info ##############
[PrintIP:527] ip      : 192.168.0.100
[PrintIP:527] mask    : 255.255.255.0
[PrintIP:527] gateway : 0.0.0.0
[FWDN_ND::InfoDevice:132] port : 8080
[FWDN_ND::InfoDevice:135]
mmc0_user: 7818182656 byte block_size: 512 byte
mmc0_boot0: 4194304 byte block_size: 512 byte
mmc0_boot1: 4194304 byte block_size: 512 byte
snor1: 0 byte
snor2: 0 byte
fw_version: tcc750x_v0.0.111
fw_build_id: g90e2b777
fw_build_date: 2024-09-24-17:11:42+0900

----- Firmware Information -----
VERSION    : tcc750x_v0.0.111
BUILD ID   : g90e2b777
BUILD DATE : 2024-09-24-17:11:42+0900

----- Detail of Storages -----
#### eMMC Info ####
Manufacture ID: 0x15
OEM: 0x100
Name: 0x8GTF4
User Capacity: 7.3 GiB (7818182656 Byte)
Boot Capacity: 4 MiB (4194304 Byte)
RPMB Capacity: 512 KiB (524288 Byte)
Speed Mode: HS200
#### SNOR Info ####

----- Summary of Storages -----
eMMC : O
SNOR : X
- O : Init success
- X : Init failed or not exist

----- Summary of DRAM Init -----
DRAM Init : Success
DRAM Size : TBD MB

----- PMU Status -----
PMU_USER   : 0x0
PMU_SIC_USER   : 0x80
PMU_CONFIG : 0x0
* BM : PMU_CONFIG[1:0]
-  0 : USB BOOT
-  1 : SNOR BOOT
-  2 : eMMC BOOT
-  3 : eMMC with SIC BOOT

--------------------------------

[ParseStorageSize:558] 1
[ParseStorageSize:583] 7818182656,7818182656
[FWDN_ND::LoadFwdnFW:676] TCP Ready OK
[FWDN_ND::LowformatCommand:1495] Lowformat Start(eMMC)
[main:156] Complete FWDN, Total Time = 1755 ms
[main:162] **Notification : For more detailed FWDN Log, use the -g or --debug option.

Step 3. Download boot-firmware
[FWDNLogger::PrintCurTime:100] 25/06/12-16:11:57
[main:24] FWDN N-Dolphin v1.0.1 - 2024.9.24 16:18:11
[main:92] Start FWDN
[FWDN_ND::InfoDevice:123] ############## Device Info ##############
[PrintIP:527] ip      : 192.168.0.100
[PrintIP:527] mask    : 255.255.255.0
[PrintIP:527] gateway : 0.0.0.0
[FWDN_ND::InfoDevice:132] port : 8080
[FWDN_ND::InfoDevice:135]
mmc0_user: 7818182656 byte block_size: 512 byte
mmc0_boot0: 4194304 byte block_size: 512 byte
mmc0_boot1: 4194304 byte block_size: 512 byte
snor1: 0 byte
snor2: 0 byte
fw_version: tcc750x_v0.0.111
fw_build_id: g90e2b777
fw_build_date: 2024-09-24-17:11:42+0900

----- Firmware Information -----
VERSION    : tcc750x_v0.0.111
BUILD ID   : g90e2b777
BUILD DATE : 2024-09-24-17:11:42+0900

----- Detail of Storages -----
#### eMMC Info ####
Manufacture ID: 0x15
OEM: 0x100
Name: 0x8GTF4
User Capacity: 7.3 GiB (7818182656 Byte)
Boot Capacity: 4 MiB (4194304 Byte)
RPMB Capacity: 512 KiB (524288 Byte)
Speed Mode: HS200
#### SNOR Info ####

----- Summary of Storages -----
eMMC : O
SNOR : X
- O : Init success
- X : Init failed or not exist

----- Summary of DRAM Init -----
DRAM Init : Success
DRAM Size : TBD MB

----- PMU Status -----
PMU_USER   : 0x0
PMU_SIC_USER   : 0x80
PMU_CONFIG : 0x0
* BM : PMU_CONFIG[1:0]
-  0 : USB BOOT
-  1 : SNOR BOOT
-  2 : eMMC BOOT
-  3 : eMMC with SIC BOOT

--------------------------------

[FWDN_ND::LoadFwdnFW:676] TCP Ready OK
[main:121] Start Write
[FWDN_ND::GetFileAndWriteCommand:1388] C:\output_aig.fwdn\boot-firmware\.\prebuilt\bconf.bin
[FWDN_ND::GetFileAndWriteCommand:1388] C:\output_aig.fwdn\boot-firmware\.\prebuilt\bconf.bin
[FWDN_ND::GetFileAndWriteCommand:1388] C:\output_aig.fwdn\boot-firmware\.\prebuilt\mcert.bin
[FWDN_ND::GetFileAndWriteCommand:1388] C:\output_aig.fwdn\boot-firmware\.\prebuilt\mcert.bin
[FWDN_ND::GetFileAndWriteCommand:1388] C:\output_aig.fwdn\boot-firmware\.\prebuilt\dram_params.bin
[FWDN_ND::GetFileAndWriteCommand:1388] C:\output_aig.fwdn\boot-firmware\.\prebuilt\dram_params.bin
[FWDN_ND::GetFileAndWriteCommand:1388] C:\output_aig.fwdn\boot-firmware\.\prebuilt\hsm.bin
[FWDN_ND::GetFileAndWriteCommand:1388] C:\output_aig.fwdn\boot-firmware\.\prebuilt\hsm.bin
[FWDN_ND::GetFileAndWriteCommand:1388] C:\output_aig.fwdn\boot-firmware\.\prebuilt\ca53_bl1.rom
[FWDN_ND::GetFileAndWriteCommand:1388] C:\output_aig.fwdn\boot-firmware\.\prebuilt\ca53_bl1.rom
[FWDN_ND::GetFileAndWriteCommand:1388] C:\output_aig.fwdn\boot-firmware\.\prebuilt\ca53_bl2.rom
[FWDN_ND::GetFileAndWriteCommand:1388] C:\output_aig.fwdn\boot-firmware\.\prebuilt\ca53_bl2.rom
[FWDN_ND::GetFileAndWriteCommand:1388] C:\output_aig.fwdn\boot-firmware\.\prebuilt\optee.rom
[FWDN_ND::GetFileAndWriteCommand:1388] C:\output_aig.fwdn\boot-firmware\.\prebuilt\optee.rom
[main:156] Complete FWDN, Total Time = 3307 ms
[main:162] **Notification : For more detailed FWDN Log, use the -g or --debug option.
100%[||||||||||||||||||||||||||||||] 328064/328064
Step 4. Download FAI file (system image)
[FWDNLogger::PrintCurTime:100] 25/06/12-16:12:00
[main:24] FWDN N-Dolphin v1.0.1 - 2024.9.24 16:18:11
[main:92] Start FWDN
[FWDN_ND::InfoDevice:123] ############## Device Info ##############
[PrintIP:527] ip      : 192.168.0.100
[PrintIP:527] mask    : 255.255.255.0
[PrintIP:527] gateway : 0.0.0.0
[FWDN_ND::InfoDevice:132] port : 8080
[FWDN_ND::InfoDevice:135]
mmc0_user: 7818182656 byte block_size: 512 byte
mmc0_boot0: 4194304 byte block_size: 512 byte
mmc0_boot1: 4194304 byte block_size: 512 byte
snor1: 0 byte
snor2: 0 byte
fw_version: tcc750x_v0.0.111
fw_build_id: g90e2b777
fw_build_date: 2024-09-24-17:11:42+0900

----- Firmware Information -----
VERSION    : tcc750x_v0.0.111
BUILD ID   : g90e2b777
BUILD DATE : 2024-09-24-17:11:42+0900

----- Detail of Storages -----
#### eMMC Info ####
Manufacture ID: 0x15
OEM: 0x100
Name: 0x8GTF4
User Capacity: 7.3 GiB (7818182656 Byte)
Boot Capacity: 4 MiB (4194304 Byte)
RPMB Capacity: 512 KiB (524288 Byte)
Speed Mode: HS200
#### SNOR Info ####

----- Summary of Storages -----
eMMC : O
SNOR : X
- O : Init success
- X : Init failed or not exist

----- Summary of DRAM Init -----
DRAM Init : Success
DRAM Size : TBD MB

----- PMU Status -----
PMU_USER   : 0x0
PMU_SIC_USER   : 0x80
PMU_CONFIG : 0x0
* BM : PMU_CONFIG[1:0]
-  0 : USB BOOT
-  1 : SNOR BOOT
-  2 : eMMC BOOT
-  3 : eMMC with SIC BOOT

--------------------------------

[ParseStorageSize:558] 1
[ParseStorageSize:583] 7818182656,7818182656
[FWDN_ND::LoadFwdnFW:676] TCP Ready OK
[main:121] Start Write
[FWDN_ND::GetFileAndWriteCommand:1388] output_aig.fai
[main:156] Complete FWDN, Total Time = 71367 ms
[main:162] **Notification : For more detailed FWDN Log, use the -g or --debug option.
100%[||||||||||||||||||||||||||||||] 356166304/356166304
TOPST AI-G FWDN is complete!
```
<br/><br/>

## 1.6 Execute FWDN in Linux Environment

### 1.6.1 Extracting the AI-G Image
---
Extract the AI-G image that you downloaded in Section 1.5 on your Linux system.
<br/><br/><br/>

### 1.6.2 Udev Rules for Telechips USB Device
---
After you execute the following commands, you no longer need to use 'sudo' command when downloading FWDN in Linux.
```
$ echo "SUBSYSTEM==\"usb\", ATTR{idVendor}==\"140e\", MODE=\"0666\", OWNER=\"${USER}\"" | sudo tee /etc/udev/rules.d/99-topst.rules
$ sudo udevadm control --reload-rules && sudo udevadm trigger
```
<br/><br/><br/>

### 1.6.3 Flashing the AI-G Image with fwdn.sh

In a Linux environment, you can download AI-G image by entering the following command. 

```
./fwdn.sh 
```
After ***FWDN*** is completed, remove the USB Type-C cable from the FWDN port and remove the power cable. 

<br/><br/><br/>



## 1.7 AI-G board Connection with UART
--- 
Perform the following steps and verify that the firmware download is successfully completed by using the UART connection.  

1. Install the serial port driver (for example, CP210x Universal Windows Driver) and PL2303_prolific driver in the Windows environment.
2. Install a terminal emulator such as Tera Term or PuTTY. 
3. Connect the Host PC and UART Pin on the AI-G board. Use a USB to TTL Cable. 
4. Connect the black cable to GND pin. 
5. Connect the white cable (RXD) to TX pin of the UART pins and the green cable (TXD) to RX pin of UART pins.
6. Run the terminal emulator application.
7. Open Device Manager on your PC and check the port number that is being used for UART.
8. Enter the Verified Port number in Device Manager into **Serial line** field in the terminal emulator. Set **Speed** (bps) to 115200 and **Flow control to None.**
9. Connect the power cable. Then, the AI-G boots in the default eMMC boot mode.

 
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20AI-G/Software/Linux%20SDK/6.%20connetc%20host%20pc%20to%20ai-g%20with%20uart%20cable.png"></p>
<p align="center"><strong>Figure 1.12 UART Connection with Host PC</strong></p>  <br/>


Figure 1.13 below shows a successful login.  

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20AI-G/Software/Linux%20SDK/7.%20connenct%20screen.png" width="550"></p>
<p align="center"><strong>Figure 1.13 Connected Screen (ID and Password are topst)</strong></p> <br/>

<br/><br/>