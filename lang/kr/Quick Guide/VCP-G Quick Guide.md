# VCP-G 퀵 가이드
---

### 1.1 Windows 환경에서 FWDN 실행
1. 보드를 다운로드 모드로 설정
   FWDN 스위치를 누른 상태에서 전원 케이블을 VCP-G 보드에 연결합니다.
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/Set%20Board%20to%20Download%20Mode.png"></p>
    <p align="center"><strong>그림 1.1 보드를 다운로드 모드로 설정</strong></p>
2. 다운로드 페이지로 이동

3. Yocto VCP-G 이미지 다운로드
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/Quick%20Guide/Download%20VCP-G%20Image.png" width="550"></p>
    <p align="center"><strong>그림 1.2 VCP-G 이미지 다운로드</strong></p> <br/>

4. fwdn_vcp.bat를 클릭합니다. "fwdn_vcp.bat"는 ***FWDN V8***을 사용하여 펌웨어를 자동으로 다운로드하는 실행 파일입니다. 
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/Quick%20Guide/Click%20fwdn_vcp.bat.png" width="550"></p>
    <p align="center"><strong>그림 1.3 fwdn_vcp.bat 클릭</strong></p> <br/>
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

4. 보드 재설정
   다운로드 과정이 완료되면 전원 케이블을 분리했다가 다시 연결하십시오.
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/Reset%20the%20Board.png"></p>
    <p align="center"><strong>그림 1.4 보드 재설정</strong></p>

</br></br></br>

### 1.2 Linux 환경에서 FWDN 실행
Linux 환경에서는 다음 명령을 입력하여 AI-G 이미지를 다운로드할 수 있습니다. 

```
./fwdn.sh 
```

</br></br></br>