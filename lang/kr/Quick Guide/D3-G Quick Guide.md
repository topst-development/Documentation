# D3-G 퀵 가이드
---

## 1.1 USB 부팅 모드로 D3-G 보드와 호스트 PC 연결
---
펌웨어 다운로더(FWDN)는 호스트 PC와의 USB 통신을 통해 D3-G에 ROM 이미지를 씁니다.

D3-G에는 하나의 부팅 모드 버튼이 있으며 두 가지 유형의 부팅 모드를 지원합니다. 이 가이드는 FWDN 모드에 중점을 둡니다.

- USB 부팅 모드(FWDN 모드): 호스트 PC에서 FWDN 도구를 사용하여 ROM 이미지를 쓰는 데 사용됩니다.

- eMMC 부팅 모드: eMMC 장치에 저장된 ROM 이미지를 사용하여 D3-G를 부팅하는 데 사용됩니다.

**참고**: USB Type-C FWDN 포트는 펌웨어 다운로더(FWDN)에 사용됩니다.



FWDN을 사용하려면 다음과 같이 D3-G 보드를 호스트 PC에 연결하십시오.

1. 호스트 PC에 VTC 드라이버가 설치되어 있는지 확인합니다. VTC 드라이버가 설치되어 있지 않으면 1.2장에 표시된 대로 설치하십시오.

2. USB Type-C 케이블 하나를 준비합니다.

3. USB 부팅 모드로 진입하려면 FWDN 스위치를 누른 상태에서 D3-G 보드에 전원 케이블을 연결합니다.

4. USB Type-C 케이블을 D3-G 보드의 USB Type-C FWDN 포트와 호스트 PC에 연결합니다.

<p align="center">
    <img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20D3-G/Hardware/connect%20to%20d3g%20to%20host%20pc%20using%20c%20type.png">
</p>
<p align="center"><strong>그림 1.1 USB C-Type 케이블을 사용하여 D3-G 보드와 호스트 PC 연결 </strong></p>

<br/><br/>

## 1.2 VTC 드라이버 설치 방법 (Windows/Ubuntu)
호스트 PC에서 관리자 권한으로 실행하여 Vendor Telechips Certification (VTC) 드라이버([telechips driver](https://drive.google.com/file/d/1muQnY8kuKxDsy3p3FUiQqcG34Zjk-mnR/view?usp=sharing)에서 찾을 수 있음)를 설치합니다. 위와 같이 FWDN 모드에서 USB를 연결하면 그림 1.2 및 그림 1.3과 같이 Telechips VTC USB 드라이버가 설정됩니다.

<p align="center">
    <img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20D3-G/Software/USB%20Connection%20in%20Windows%20Environment.png", width="700">
</p>
<p align="center"><strong>그림 1.2 Windows 환경에서의 USB 연결</strong></p>

<p align="center">
    <img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20D3-G/Software/USB%20Connection%20in%20Linux%20System.png", width="700">
</p>
<p align="center"><strong>그림 1.3 Linux 환경에서의 USB 연결</strong></p>  

**참고**: VTC 드라이버 V5.0.0.14 이상을 사용하십시오. 버전을 확인하려면 Windows 환경의 장치 관리자에서 확인하십시오.  

<br/><br/><br/>

## 1.3 Windows 환경에서의 FWDN

### 1.3.1 D3-G Yocto
---
1. 다운로드 페이지로 이동

2. D3-G Yocto 이미지 다운로드
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/Quick%20Guide/Download%20D3-G%20v1.2.0%20Yocto%20Image.png" width="550"></p>
<p align="center"><strong>그림 1.4 D3-G Yocto 이미지 다운로드</strong></p> <br/>

3. fwdn.bat를 클릭합니다. "fwdn.bat"는 ***FWDN V8***을 사용하여 펌웨어를 자동으로 다운로드하는 실행 파일입니다. 
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/Quick%20Guide/Click%20fwdn.bat.png" width="550"></p>
<p align="center"><strong>그림 1.5 fwdn.bat 클릭</strong></p> <br/>

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
1. 다운로드 페이지로 이동

2. D3-G Ubuntu Desktop 이미지 다운로드
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/Quick%20Guide/Download%20D3-G%20v1.2.0%20Ubuntu%20Desktop%20Image.png" width="550"></p>
<p align="center"><strong>그림 1.6 D3-G Ubuntu Desktop 이미지 다운로드</strong></p> <br/>

3. fwdn.bat를 클릭합니다. "fwdn.bat"는 ***FWDN V8***을 사용하여 펌웨어를 자동으로 다운로드하는 실행 파일입니다. 
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/Quick%20Guide/Click%20fwdn_ubuntu.bat.png" width="550"></p>
<p align="center"><strong>그림 1.7 fwdn.bat 클릭</strong></p> <br/>

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
1. 다운로드 페이지로 이동

2. D3-G Ubuntu Headless 이미지 다운로드
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/Quick%20Guide/Download%20D3-G%20Ubuntu%20Headless%20Image.png" width="550"></p>
<p align="center"><strong>그림 1.8 D3-G Ubuntu Headless 이미지 다운로드</strong></p> <br/>

3. fwdn.bat를 클릭합니다. "fwdn.bat"는 ***FWDN V8***을 사용하여 펌웨어를 자동으로 다운로드하는 실행 파일입니다. 
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/Quick%20Guide/Click%20fwdn_ubuntu_headless.bat.png" width="550"></p>
<p align="center"><strong>그림 1.9 fwdn.bat 클릭</strong></p> <br/>

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

## 1.4 Linux 환경에서의 FWDN

### 1.4.1 D3-G 이미지 추출
---
1.3절에서 다운로드한 D3-G 이미지를 Linux 시스템에 추출합니다.

<br/><br/><br/>

### 1.4.2 Telechips USB 장치에 대한 Udev 규칙
---
다음 명령을 실행하면 Linux에서 FWDN을 다운로드할 때 더 이상 'sudo' 명령을 사용할 필요가 없습니다.
```
$ echo "SUBSYSTEM==\"usb\", ATTR{idVendor}==\"140e\", MODE=\"0666\", OWNER=\"${USER}\"" | sudo tee /etc/udev/rules.d/99-topst.rules
$ sudo udevadm control --reload-rules && sudo udevadm trigger
```
<br/><br/><br/>

### 1.4.3 fwdn.sh로 D3-G 이미지 플래싱
---
Linux에서 D3-G 이미지를 다운로드하려면 다음 명령을 실행하십시오: "./fwdn.sh".

```
$ ./fwdn.sh
```

이제 D3-G를 부팅할 준비가 되었습니다. 장치와 통신을 시작하려면 1.5장을 참조하십시오.


<br/><br/><br/><br/>

## 1.5 D3-G 보드와 호스트 PC 연결
---
이 장에서는 펌웨어 다운로드 및 직렬 통신을 위해 UART를 통해 호스트 PC를 D3-G 보드에 연결하는 방법을 설명합니다.

<br/><br/><br/>

## 1.6 UART를 통한 D3-G 보드 연결 
---
다음 단계를 수행하고 UART 연결을 사용하여 펌웨어 다운로드가 성공적으로 완료되었는지 확인하십시오. 

1. Windows 환경에 직렬 포트 드라이버(예: CP210x Windows 드라이버) 및 PL2303_prolific 드라이버를 설치합니다. 
2. Tera Term 또는 PuTTY와 같은 터미널 에뮬레이터를 설치합니다. 
3. 호스트 PC와 D3-G 보드의 UART 핀을 연결합니다. USB-to-TTL 케이블을 사용하십시오. 
4. 검은색 케이블을 GND 핀에 연결합니다. 
5. 흰색 케이블(RXD)을 UART 핀의 TX 핀에 연결하고 녹색 케이블(TXD)을 UART 핀의 RX 핀에 연결합니다.
6. 터미널 에뮬레이터 애플리케이션을 실행합니다.
7. PC에서 장치 관리자를 열고 UART에 사용 중인 포트 번호를 확인합니다.
8. 장치 관리자에서 확인된 포트 번호를 터미널 에뮬레이터의 직렬 라인 필드에 입력합니다. **속도** (bps)를 115200으로 설정하고 **흐름 제어를 없음**으로 설정합니다.
9. 전원 케이블을 연결합니다. 그러면 D3-G가 기본 eMMC 부팅 모드로 부팅됩니다.


 
<p align="center">
    <img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20D3-G/Software/USB%20to%20TTL%20Connection.png", width="700">
</p>
<p align="center"><strong>그림 1.6 호스트 PC와의 UART 연결</strong></p><br/>  
