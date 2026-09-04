# คู่มือฉบับย่อ D3-G
---

## 1.1 การเชื่อมต่อบอร์ด D3-G กับเครื่อง PC โฮสต์ด้วยโหมดบูต USB
---
Firmware Downloader (FWDN) เขียนอิมเมจ ROM ลงใน D3-G ผ่านการสื่อสาร USB กับเครื่อง PC โฮสต์ 

D3-G มีปุ่ม Boot Mode หนึ่งปุ่มและรองรับโหมดการบูตสองประเภท คู่มือนี้เน้นอธิบายโหมด FWDN เป็นหลัก

- USB Boot Mode (FWDN Mode) : ใช้สำหรับเขียนอิมเมจ ROM โดยใช้เครื่องมือ FWDN บนเครื่อง PC โฮสต์ของคุณ 

- eMMC Boot Mode : ใช้สำหรับบูต D3-G โดยใช้อิมเมจ ROM ที่จัดเก็บอยู่ในอุปกรณ์ eMMC 

**หมายเหตุ**: พอร์ต USB Type-C FWDN ใช้สำหรับเฟิร์มแวร์ดาวน์โหลดเดอร์ (FWDN) 



หากต้องการใช้ FWDN ให้เชื่อมต่อบอร์ด D3-G เข้ากับเครื่อง PC โฮสต์ดังนี้: 

1. ตรวจสอบว่ามีการติดตั้งไดรเวอร์ VTC บนเครื่อง PC โฮสต์แล้ว หากยังไม่ได้ติดตั้งไดรเวอร์ VTC ให้ติดตั้งตามที่แสดงในบทที่ 1.2  

2. เตรียมสาย USB Type-C หนึ่งเส้น 

3. หากต้องการเข้าสู่โหมดบูต USB ให้เชื่อมต่อสายไฟเข้ากับบอร์ด D3-G ขณะกดสวิตช์ FWDN ค้างไว้

4. เชื่อมต่อสาย USB Type-C เข้ากับพอร์ต USB Type-C FWDN บนบอร์ด D3-G และเครื่อง PC โฮสต์ 

<p align="center">
    <img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20D3-G/Hardware/connect%20to%20d3g%20to%20host%20pc%20using%20c%20type.png">
</p>
<p align="center"><strong>รูปที่ 1.1 การเชื่อมต่อบอร์ด D3-G กับเครื่อง PC โฮสต์โดยใช้สาย USB C-Type </strong></p>

<br/><br/>

## 1.2 วิธีติดตั้งไดรเวอร์ VTC (Windows/Ubuntu)
ติดตั้งไดรเวอร์ Vendor Telechips Certification (VTC) (มีให้ที่ [ไดรเวอร์ telechips](https://drive.google.com/file/d/1muQnY8kuKxDsy3p3FUiQqcG34Zjk-mnR/view?usp=sharing)) บนเครื่อง PC โฮสต์โดยเรียกใช้ในฐานะผู้ดูแลระบบ เมื่อคุณเชื่อมต่อ USB ในโหมด FWDN ตามที่แสดงข้างต้น ไดรเวอร์ Telechips VTC USB จะถูกตั้งค่าดังที่แสดงในรูปที่ 1.2 และรูปที่ 1.3

<p align="center">
    <img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20D3-G/Software/USB%20Connection%20in%20Windows%20Environment.png", width="700">
</p>
<p align="center"><strong>รูปที่ 1.2 การเชื่อมต่อ USB ในสภาพแวดล้อม Windows</strong></p>

<p align="center">
    <img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20D3-G/Software/USB%20Connection%20in%20Linux%20System.png", width="700">
</p>
<p align="center"><strong>รูปที่ 1.3 การเชื่อมต่อ USB ในสภาพแวดล้อม Linux</strong></p>  

**หมายเหตุ**: ใช้ไดรเวอร์ VTC เวอร์ชัน V5.0.0.14 ขึ้นไป หากต้องการตรวจสอบเวอร์ชัน ให้ยืนยันที่ตัวจัดการอุปกรณ์ในสภาพแวดล้อม Windows  

<br/><br/><br/>

## 1.3 FWDN ในสภาพแวดล้อม Windows

### 1.3.1 D3-G Yocto
---
1. ไปที่หน้าดาวน์โหลด

2. ดาวน์โหลดอิมเมจ D3-G Yocto
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/Quick%20Guide/Download%20D3-G%20v1.2.0%20Yocto%20Image.png" width="550"></p>
<p align="center"><strong>รูปที่ 1.4 ดาวน์โหลดอิมเมจ D3-G Yocto</strong></p> <br/>

3. คลิก fwdn.bat โดย “fwdn.bat” เป็นไฟล์ปฏิบัติการที่ดาวน์โหลดเฟิร์มแวร์โดยอัตโนมัติด้วย ***FWDN V8*** 
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/Quick%20Guide/Click%20fwdn.bat.png" width="550"></p>
<p align="center"><strong>รูปที่ 1.5 คลิก fwdn.bat</strong></p> <br/>

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
1. ไปที่หน้าดาวน์โหลด

2. ดาวน์โหลดอิมเมจ D3-G Ubuntu Desktop
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/Quick%20Guide/Download%20D3-G%20v1.2.0%20Ubuntu%20Desktop%20Image.png" width="550"></p>
<p align="center"><strong>รูปที่ 1.6 ดาวน์โหลดอิมเมจ D3-G Ubuntu Desktop</strong></p> <br/>

3. คลิก fwdn.bat โดย “fwdn.bat” เป็นไฟล์ปฏิบัติการที่ดาวน์โหลดเฟิร์มแวร์โดยอัตโนมัติด้วย ***FWDN V8*** 
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/Quick%20Guide/Click%20fwdn_ubuntu.bat.png" width="550"></p>
<p align="center"><strong>รูปที่ 1.7 คลิก fwdn.bat</strong></p> <br/>

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
1. ไปที่หน้าดาวน์โหลด

2. ดาวน์โหลดอิมเมจ D3-G Ubuntu Headless
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/Quick%20Guide/Download%20D3-G%20Ubuntu%20Headless%20Image.png" width="550"></p>
<p align="center"><strong>รูปที่ 1.8 ดาวน์โหลดอิมเมจ D3-G Ubuntu Headless</strong></p> <br/>

3. คลิก fwdn.bat โดย “fwdn.bat” เป็นไฟล์ปฏิบัติการที่ดาวน์โหลดเฟิร์มแวร์โดยอัตโนมัติด้วย ***FWDN V8*** 
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/Quick%20Guide/Click%20fwdn_ubuntu_headless.bat.png" width="550"></p>
<p align="center"><strong>รูปที่ 1.9 คลิก fwdn.bat</strong></p> <br/>

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

## 1.4 FWDN ในสภาพแวดล้อม Linux

### 1.4.1 การแตกไฟล์อิมเมจ D3-G
---
แตกไฟล์อิมเมจ D3-G ที่คุณดาวน์โหลดในหัวข้อ 1.3 บนระบบ Linux ของคุณ

<br/><br/><br/>

### 1.4.2 กฎ Udev สำหรับอุปกรณ์ USB ของ Telechips
---
หลังจากที่คุณรันคำสั่งต่อไปนี้ คุณไม่จำเป็นต้องใช้คำสั่ง 'sudo' อีกต่อไปเมื่อดาวน์โหลด FWDN ใน Linux
```
$ echo "SUBSYSTEM==\"usb\", ATTR{idVendor}==\"140e\", MODE=\"0666\", OWNER=\"${USER}\"" | sudo tee /etc/udev/rules.d/99-topst.rules
$ sudo udevadm control --reload-rules && sudo udevadm trigger
```
<br/><br/><br/>

### 1.4.3 การแฟลชอิมเมจ D3-G ด้วย fwdn.sh
---
หากต้องการดาวน์โหลดอิมเมจ D3-G ใน Linux ให้รันคำสั่งต่อไปนี้: "./fwdn.sh"

```
$ ./fwdn.sh
```

คุณพร้อมที่จะบูต D3-G แล้ว โปรดดูบทที่ 1.5 เพื่อเริ่มการสื่อสารกับอุปกรณ์


<br/><br/><br/><br/>

## 1.5 การเชื่อมต่อบอร์ด D3-G กับเครื่อง PC โฮสต์
---
บทนี้อธิบายวิธีเชื่อมต่อเครื่อง PC โฮสต์เข้ากับบอร์ด D3-G ผ่าน UART สำหรับการดาวน์โหลดเฟิร์มแวร์และการสื่อสารแบบอนุกรม

<br/><br/><br/>

## 1.6 การเชื่อมต่อบอร์ด D3-G ด้วย UART 
---
ทำตามขั้นตอนเหล่านี้และตรวจสอบว่าการดาวน์โหลดเฟิร์มแวร์เสร็จสมบูรณ์แล้วโดยใช้การเชื่อมต่อ UART 

1. ติดตั้งไดรเวอร์พอร์ตอนุกรม (ตัวอย่างเช่น CP210x Windows Driver) และไดรเวอร์ PL2303_prolific ในสภาพแวดล้อม Windows 
2. ติดตั้งโปรแกรมจำลองเทอร์มินัล เช่น Tera Term หรือ PuTTY 
3. เชื่อมต่อเครื่อง PC โฮสต์กับพิน UART บนบอร์ด D3-G โดยใช้สาย USB-to-TTL 
4. เชื่อมต่อสายสีดำเข้ากับพิน GND 
5. เชื่อมต่อสายสีขาว (RXD) เข้ากับพิน TX ของพิน UART และสายสีเขียว (TXD) เข้ากับพิน RX ของพิน UART
6. เรียกใช้แอปพลิเคชันโปรแกรมจำลองเทอร์มินัล
7. เปิดตัวจัดการอุปกรณ์บน PC ของคุณและตรวจสอบหมายเลขพอร์ตที่ใช้สำหรับ UART
8. ป้อนหมายเลขพอร์ตที่ตรวจสอบแล้วในตัวจัดการอุปกรณ์ลงในช่อง Serial line ในโปรแกรมจำลองเทอร์มินัล ตั้งค่า **Speed** (bps) เป็น 115200 และ **ตั้งค่า Flow control เป็น None**
9. เชื่อมต่อสายไฟ จากนั้น D3-G จะบูตในโหมดบูต eMMC เริ่มต้น


 
<p align="center">
    <img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20D3-G/Software/USB%20to%20TTL%20Connection.png", width="700">
</p>
<p align="center"><strong>รูปที่ 1.6 การเชื่อมต่อ UART กับเครื่อง PC โฮสต์</strong></p><br/>  
