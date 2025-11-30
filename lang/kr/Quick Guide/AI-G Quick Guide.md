# AI-G 퀵 가이드
---

## 1.1 USB 부팅 모드 (FWDN 모드) 
---
***FWDN***을 사용하여 빌드된 이미지를 AI-G로 전송할 수 있습니다. AI-G는 이더넷과 UART를 사용하여 ***FWDN***을 제공합니다. 

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20AI-G/Software/Linux%20SDK/3.%20connect%20host%20pc%20to%20topst%20ai-g.png" ></p>
<p align="center"><strong>그림 1.1 FWDN을 위한 호스트 PC와 AI-G 간의 연결</strong></p><br/>

***FWDN V8***을 사용하려면 다음과 같이 AI-G 보드를 호스트 PC에 연결하십시오. 

1. 호스트 PC에 VTC 드라이버가 설치되어 있는지 확인합니다. VTC 드라이버가 설치되어 있지 않으면 4.2.1장에 표시된 대로 설치하십시오.  

2. USB Type-C 케이블 하나와 이더넷 케이블 하나를 준비합니다. 

3. USB 부팅 모드로 진입하려면 USB Type-C 케이블을 AI-G 보드의 USB Type-C FWDN 포트와 호스트 PC에 연결합니다. 

4. 이더넷 케이블(RJ45)을 AI-G 보드의 이더넷 포트와 호스트 PC에 연결합니다. 

5. FWDN 스위치를 누른 상태에서 전원 케이블을 AI-G 보드에 연결합니다. 

<br/><br/><br/>

## 1.2 VCP 드라이버 설치 방법

호스트 PC에서 관리자 권한으로 실행하여 Vendor Telechips Certification (VTC) 드라이버([VCP driver](https://drive.google.com/file/d/1muQnY8kuKxDsy3p3FUiQqcG34Zjk-mnR/view?usp=sharing)에서 찾을 수 있음)를 설치합니다. 위와 같이 FWDN 모드에서 USB를 연결하면 그림 1.2와 같이 Telechips VTC USB 드라이버가 설정됩니다.

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20AI-G/Software/Linux%20SDK/4.%20VTC.png" width="550"></p>
<p align="center"><strong>그림 1.2 COM 포트 확인</strong></p><br/>

<br/><br/>

## 1.3 이더넷 설정

호스트 PC 네트워크 구성 

- 제어판 → 네트워크 및 인터넷 → 네트워크 연결 → FWDN용 이더넷 장치 속성 설정 
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20AI-G/Software/Linux%20SDK/5.%20network_setting.png"></p>
<p align="center"><strong>그림 1.3 FWDN용 이더넷 장치 속성 설정</strong></p><br/>
<br/><br/><br/>

## 1.4 WMIC 추가
FWDN을 실행하기 전에 AI-G 보드의 FWDN 포트에 연결된 포트를 알기 위해 WMIC를 설치해야 합니다.

1. 설정 열기: 시작 메뉴에서 설정을 엽니다.
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20AI-G/Software/Linux%20SDK/8.%20Open%20Settings%20from%20Start%20menu.png"></p>
<p align="center"><strong>그림 1.4 시작 메뉴에서 설정 열기</strong></p>  <br/>

2. 시스템 선택: 시스템 메뉴로 이동합니다.
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20AI-G/Software/Linux%20SDK/9.%20Go%20to%20the%20System%20menu.png"></p>
<p align="center"><strong>그림 1.5 시스템 메뉴로 이동</strong></p>  <br/>

3. 선택적 기능: 선택적 기능 메뉴를 클릭합니다.
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20AI-G/Software/Linux%20SDK/10.%20Click%20the%20Selective%20Features%20menu.png"></p>
<p align="center"><strong>그림 1.6 선택적 기능 메뉴 클릭</strong></p>  <br/>

4. 기능 보기: **선택적 기능 추가** 옆의 **기능 보기** 버튼을 클릭합니다.
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20AI-G/Software/Linux%20SDK/11.%20Click%20the%20View%20Features%20button%20next%20to%20Add%20optional%20Features.png"></p>
<p align="center"><strong>그림 1.7 선택적 기능 추가 옆의 기능 보기 버튼 클릭</strong></p>  <br/>

5. WMIC 검색: 검색 상자에 **"WMIC"**를 입력합니다.
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20AI-G/Software/Linux%20SDK/12.%20Type%20WMIC%20in%20the%20search%20box.png"></p>
<p align="center"><strong>그림 1.8 검색 상자에 WMIC 입력</strong></p>  <br/>

6. 설치: WMIC 항목을 선택하고 **"다음"** 버튼을 클릭하여 설치를 완료합니다.
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20AI-G/Software/Linux%20SDK/13.%20Select%20the%20WMIC%20item%20and%20click%20the%20Next%20button%20to%20complete%20the%20installation.png"></p>
<p align="center"><strong>그림 1.9 WMIC 항목을 선택하고 다음 버튼을 클릭하여 설치 완료</strong></p>  <br/>

## 1.5 Windows 환경에서 FWDN 실행
1. 다운로드 페이지로 이동

2. AI-G Yocto 이미지 다운로드
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/Quick%20Guide/Download%20AI-G%20Image.png" width="550"></p>
<p align="center"><strong>그림 1.10 AI-G Yocto 이미지 다운로드</strong></p> <br/>

3. fwdn_aig.bat를 클릭합니다. "fwdn_aig.bat"는 ***FWDN V8***을 사용하여 펌웨어를 자동으로 다운로드하는 실행 파일입니다. 
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/Quick%20Guide/Click%20fwdn_aig.bat.png" width="550"></p>
<p align="center"><strong>그림 1.11 fwdn_aig.bat 클릭</strong></p> <br/>

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

## 1.6 Linux 환경에서 FWDN 실행

### 1.6.1 AI-G 이미지 추출
---
1.5절에서 다운로드한 AI-G 이미지를 Linux 시스템에 추출합니다.
<br/><br/><br/>

### 1.6.2 Telechips USB 장치에 대한 Udev 규칙
---
다음 명령을 실행하면 Linux에서 FWDN을 다운로드할 때 더 이상 'sudo' 명령을 사용할 필요가 없습니다.
```
$ echo "SUBSYSTEM==\"usb\", ATTR{idVendor}==\"140e\", MODE=\"0666\", OWNER=\"${USER}\"" | sudo tee /etc/udev/rules.d/99-topst.rules
$ sudo udevadm control --reload-rules && sudo udevadm trigger
```
<br/><br/><br/>

### 1.6.3 fwdn.sh로 AI-G 이미지 플래싱

Linux 환경에서는 다음 명령을 입력하여 AI-G 이미지를 다운로드할 수 있습니다. 

```
./fwdn.sh 
```
***FWDN***이 완료되면 FWDN 포트에서 USB Type-C 케이블을 제거하고 전원 케이블을 제거하십시오. 

<br/><br/><br/>



## 1.7 UART를 통한 AI-G 보드 연결
--- 
다음 단계를 수행하고 UART 연결을 사용하여 펌웨어 다운로드가 성공적으로 완료되었는지 확인하십시오.  

1. Windows 환경에 직렬 포트 드라이버(예: CP210x Windows 드라이버) 및 PL2303_prolific 드라이버를 설치합니다.
2. Tera Term 또는 PuTTY와 같은 터미널 에뮬레이터를 설치합니다. 
3. 호스트 PC와 AI-G 보드의 UART 핀을 연결합니다. USB to TTL 케이블을 사용하십시오. 
4. 검은색 케이블을 GND 핀에 연결합니다. 
5. 흰색 케이블(RXD)을 UART 핀의 TX 핀에 연결하고 녹색 케이블(TXD)을 UART 핀의 RX 핀에 연결합니다.
6. 터미널 에뮬레이터 애플리케이션을 실행합니다.
7. PC에서 장치 관리자를 열고 UART에 사용 중인 포트 번호를 확인합니다.
8. 장치 관리자에서 확인된 포트 번호를 터미널 에뮬레이터의 **직렬 라인** 필드에 입력합니다. **속도** (bps)를 115200으로 설정하고 **흐름 제어를 없음**으로 설정합니다.
9. 전원 케이블을 연결합니다. 그러면 AI-G가 기본 eMMC 부팅 모드로 부팅됩니다.


 
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20AI-G/Software/Linux%20SDK/6.%20connetc%20host%20pc%20to%20ai-g%20with%20uart%20cable.png"></p>
<p align="center"><strong>그림 1.12 호스트 PC와의 UART 연결</strong></p>  <br/>


아래 그림 1.13은 성공적인 로그인을 보여줍니다.  

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20AI-G/Software/Linux%20SDK/7.%20connenct%20screen.png" width="550"></p>
<p align="center"><strong>그림 1.13 연결된 화면 (ID와 비밀번호는 topst입니다)</strong></p> <br/>

<br/><br/>
