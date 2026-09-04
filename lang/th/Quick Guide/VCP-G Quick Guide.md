# คู่มือฉบับย่อ VCP-G
---

### 1.1 การเรียกใช้ FWDN ในสภาพแวดล้อม Windows
1. ตั้งค่าบอร์ดให้อยู่ในโหมดดาวน์โหลด
   เชื่อมต่อสายไฟเข้ากับบอร์ด VCP-G ขณะกดสวิตช์ FWDN
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/Set%20Board%20to%20Download%20Mode.png"></p>
    <p align="center"><strong>รูปที่ 1.1 การตั้งค่าบอร์ดให้อยู่ในโหมดดาวน์โหลด</strong></p>
2. ไปที่หน้าดาวน์โหลด

3. ดาวน์โหลดอิมเมจ Yocto VCP-G
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/Quick%20Guide/Download%20VCP-G%20Image.png" width="550"></p>
    <p align="center"><strong>รูปที่ 1.2 การดาวน์โหลดอิมเมจ VCP-G</strong></p> <br/>

4. คลิก fwdn_vcp.bat โดย “fwdn_vcp.bat” เป็นไฟล์ปฏิบัติการที่ดาวน์โหลดเฟิร์มแวร์โดยอัตโนมัติด้วย ***FWDN V8*** 
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/Quick%20Guide/Click%20fwdn_vcp.bat.png" width="550"></p>
    <p align="center"><strong>รูปที่ 1.3 การคลิก fwdn_vcp.bat</strong></p> <br/>
```
[main:27] FWDN VCP v0.1.1 - 2022.8.12 11:38:19
Com port num : 10
[FWDNWindowsUART::OpenPort:34] Complete open port(\\.\COM10)
[ProtocolFW::CheckResPacket:260] Complete to receive ack for cmd(0xAAAA0013(FW_PING))
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

4. รีเซ็ตบอร์ด
   หลังจากกระบวนการดาวน์โหลดเสร็จสิ้น ให้ถอดและเสียบสายไฟใหม่
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/Reset%20the%20Board.png"></p>
    <p align="center"><strong>รูปที่ 1.4 การรีเซ็ตบอร์ด</strong></p>

</br></br></br>

### 1.2 การเรียกใช้ FWDN ในสภาพแวดล้อม Linux
ในสภาพแวดล้อม Linux คุณสามารถดาวน์โหลดอิมเมจ AI-G ได้โดยป้อนคำสั่งต่อไปนี้ 

```
./fwdn.sh 
```

</br></br></br>