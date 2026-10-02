# คู่มือฉบับย่อ AI-G
---

## 1.1 โหมดบูตผ่าน USB (โหมด FWDN) 
---
ท่านสามารถถ่ายโอนอิมเมจที่บิลด์แล้วไปยัง AI-G ได้โดยใช้ ***FWDN*** ทั้งนี้ AI-G รองรับ ***FWDN*** ผ่าน Ethernet และ UART 

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20AI-G/Software/Linux%20SDK/3.%20connect%20host%20pc%20to%20topst%20ai-g.png" ></p>
<p align="center"><strong>รูปที่ 1.1 การเชื่อมต่อระหว่างเครื่อง PC โฮสต์กับ AI-G สำหรับ FWDN</strong></p><br/>

หากต้องการใช้ ***FWDN V8*** ให้เชื่อมต่อบอร์ด AI-G เข้ากับเครื่อง PC โฮสต์ตามขั้นตอนต่อไปนี้ 

1. ตรวจสอบว่าได้ติดตั้งไดรเวอร์ VTC บนเครื่อง PC โฮสต์แล้ว หากยังไม่ได้ติดตั้งไดรเวอร์ VTC ให้ติดตั้งตามที่แสดงในบทที่ 1.2

2. เตรียมสาย USB Type-C จำนวน 1 เส้น และสาย Ethernet จำนวน 1 เส้น 

3. หากต้องการเข้าสู่โหมดบูตผ่าน USB ให้เชื่อมต่อสาย USB Type-C เข้ากับพอร์ต USB Type-C FWDN บนบอร์ด AI-G และเครื่อง PC โฮสต์ 

4. เชื่อมต่อสาย Ethernet (RJ45) เข้ากับพอร์ต Ethernet บนบอร์ด AI-G และเครื่อง PC โฮสต์ 

5. เชื่อมต่อสายไฟเข้ากับบอร์ด AI-G ในขณะที่กดสวิตช์ FWDN ค้างไว้ 

<br/><br/><br/>

## 1.2 วิธีติดตั้งไดรเวอร์ VCP

ติดตั้งไดรเวอร์ Vendor Telechips Certification (VTC) (ดูได้ที่ [ไดรเวอร์ VCP](https://drive.google.com/file/d/1muQnY8kuKxDsy3p3FUiQqcG34Zjk-mnR/view?usp=sharing)) บนเครื่อง PC โฮสต์โดยเรียกใช้ในฐานะผู้ดูแลระบบ เมื่อท่านเชื่อมต่อ USB ในโหมด FWDN ตามที่แสดงข้างต้น ไดรเวอร์ Telechips VTC USB จะถูกตั้งค่าดังแสดงในรูปที่ 1.2

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20AI-G/Software/Linux%20SDK/4.%20VTC.png" width="550"></p>
<p align="center"><strong>รูปที่ 1.2 ตรวจสอบพอร์ต COM</strong></p><br/>

<br/><br/>

## 1.3 การตั้งค่า Ethernet

การกำหนดค่าเครือข่ายของเครื่อง PC โฮสต์ 

- แผงควบคุม → เครือข่ายและอินเทอร์เน็ต → การเชื่อมต่อเครือข่าย → ตั้งค่าคุณสมบัติของอุปกรณ์ Ethernet สำหรับ FWDN 
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20AI-G/Software/Linux%20SDK/5.%20network_setting.png"></p>
<p align="center"><strong>รูปที่ 1.3 การตั้งค่าคุณสมบัติของอุปกรณ์ Ethernet สำหรับ FWDN</strong></p><br/>
<br/><br/><br/>

## 1.4 ตรวจสอบพอร์ต COM สำหรับ FWDN

สคริปต์ `fwdn_ai.bat` ใน AI-G v1.2.0 ใช้ PowerShell เพื่อแสดงรายการพอร์ต COM

เชื่อมต่อบอร์ดในโหมด FWDN ตามขั้นตอนในหัวข้อ 1.1 ตรวจสอบพอร์ต COM ของอุปกรณ์ Telechips VTC ใน Device Manager หรือเรียกใช้คำสั่งต่อไปนี้ใน PowerShell:

```powershell
Get-CimInstance Win32_PnPEntity | Where-Object { $_.Name -match '\(COM[0-9]+\)' } | Select-Object -ExpandProperty Name
```

คำสั่งนี้แสดงอุปกรณ์ COM ทั้งหมดที่ตรวจพบ ให้ระบุพอร์ต COM ของอุปกรณ์ Telechips VTC ที่แสดงในหัวข้อ 1.2

## 1.5 การเรียกใช้ FWDN ในสภาพแวดล้อม Windows

1. ดาวน์โหลด[แพ็กเกจเฟิร์มแวร์ AI-G v1.2.0](https://topst-downloads.s3.ap-northeast-2.amazonaws.com/Yocto/v1.2.0/aig-yp4-v1.2.0-r01.zip) (`aig-yp4-v1.2.0-r01.zip`)

2. แตกไฟล์ ZIP แล้วเปิด PowerShell ในโฟลเดอร์ที่มีไฟล์ `fwdn_ai.bat`

3. เรียกใช้คำสั่งต่อไปนี้:

```powershell
.\fwdn_ai.bat
```

เมื่อข้อความ `Input USB Port Number` ปรากฏ ให้ป้อนเฉพาะหมายเลขพอร์ต COM สำหรับ FWDN ที่ตรวจสอบในหัวข้อ 1.4 (เช่น ป้อน `44` สำหรับ `COM44`)

บันทึกด้านล่างเป็นตัวอย่างจากแพ็กเกจเฟิร์มแวร์รุ่นก่อนหน้า ชื่อไฟล์ปฏิบัติการ เวอร์ชัน หมายเลขพอร์ต COM และระยะเวลาอาจแตกต่างกัน

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

## 1.6 การเรียกใช้ FWDN ในสภาพแวดล้อม Linux

### 1.6.1 การแตกไฟล์อิมเมจ AI-G
---
แตกไฟล์อิมเมจ AI-G ที่ท่านดาวน์โหลดไว้ในหัวข้อ 1.5 บนระบบ Linux ของท่าน
<br/><br/><br/>

### 1.6.2 กฎ Udev สำหรับอุปกรณ์ USB ของ Telechips
---
หลังจากที่ท่านเรียกใช้คำสั่งต่อไปนี้แล้ว ท่านไม่จำเป็นต้องใช้คำสั่ง 'sudo' อีกต่อไปเมื่อดาวน์โหลด FWDN ใน Linux
```
$ echo "SUBSYSTEM==\"usb\", ATTR{idVendor}==\"140e\", MODE=\"0666\", OWNER=\"${USER}\"" | sudo tee /etc/udev/rules.d/99-topst.rules
$ sudo udevadm control --reload-rules && sudo udevadm trigger
```
<br/><br/><br/>

### 1.6.3 การแฟลชอิมเมจ AI-G ด้วย fwdn_ai.sh

ในโฟลเดอร์ที่แตกไฟล์แล้วและมี `fwdn_ai.sh` ให้เพิ่มสิทธิ์ในการเรียกใช้ไฟล์ไบนารี FWDN ที่มาพร้อมแพ็กเกจ แล้วเรียกใช้สคริปต์:

```bash
chmod +x ./fwdn_ai
bash ./fwdn_ai.sh
```
หลังจาก ***FWDN*** เสร็จสมบูรณ์แล้ว ให้ถอดสาย USB Type-C ออกจากพอร์ต FWDN และถอดสายไฟออก 

<br/><br/><br/>



## 1.7 การเชื่อมต่อบอร์ด AI-G ด้วย UART
--- 
ดำเนินการตามขั้นตอนต่อไปนี้ และตรวจสอบว่าการดาวน์โหลดเฟิร์มแวร์เสร็จสมบูรณ์แล้วโดยใช้การเชื่อมต่อ UART  

1. ติดตั้งไดรเวอร์พอร์ตอนุกรม (เช่น CP210x Windows Driver) และไดรเวอร์ PL2303_prolific ในสภาพแวดล้อม Windows
2. ติดตั้งโปรแกรมจำลองเทอร์มินัล เช่น Tera Term หรือ PuTTY 
3. เชื่อมต่อเครื่อง PC โฮสต์กับพิน UART บนบอร์ด AI-G โดยใช้สาย USB to TTL 
4. เชื่อมต่อสายสีดำเข้ากับพิน GND 
5. เชื่อมต่อสายสีขาว (RXD) เข้ากับพิน TX ของพิน UART และเชื่อมต่อสายสีเขียว (TXD) เข้ากับพิน RX ของพิน UART
6. เรียกใช้แอปพลิเคชันจำลองเทอร์มินัล
7. เปิด Device Manager บนเครื่อง PC ของท่าน แล้วตรวจสอบหมายเลขพอร์ตที่ใช้งานสำหรับ UART
8. ป้อนหมายเลขพอร์ตที่ตรวจสอบแล้วใน Device Manager ลงในช่อง **Serial line** ของโปรแกรมจำลองเทอร์มินัล ตั้งค่า **Speed** (bps) เป็น 115200 และ **Flow control เป็น None**
9. เชื่อมต่อสายไฟ จากนั้น AI-G จะทำการบูตในโหมดบูตจาก eMMC ซึ่งเป็นค่าเริ่มต้น

 
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20AI-G/Software/Linux%20SDK/6.%20connetc%20host%20pc%20to%20ai-g%20with%20uart%20cable.png"></p>
<p align="center"><strong>รูปที่ 1.4 การเชื่อมต่อ UART กับเครื่อง PC โฮสต์</strong></p>  <br/>


รูปที่ 1.5 ด้านล่างแสดงการเข้าสู่ระบบที่สำเร็จ

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20AI-G/Software/Linux%20SDK/7.%20connenct%20screen.png" width="550"></p>
<p align="center"><strong>รูปที่ 1.5 หน้าจอที่เชื่อมต่อแล้ว (ID และรหัสผ่านคือ topst)</strong></p> <br/>

<br/><br/>
