# 1. 소개
---
이 문서는 VCP-G SDK를 위한 소프트웨어 개발 환경 구성 지침을 제공합니다. 필요한 도구, 설정 및 툴체인을 설명합니다.

</br></br></br></br>

# 2. 호스트 환경 설정
---
## 2.1 Ubuntu 설치
---
개발 환경은 Ubuntu 22.04에서 구성하는 것을 권장합니다. 이 Ubuntu 버전은 폭넓은 커뮤니티 지원과 안정적인 플랫폼을 제공하여 VCP-G 및 관련 툴체인과의 호환성과 사용 편의성을 보장합니다.

Linux 배포판 버전:  
- Ubuntu 22.04 (LTS)

</br></br></br>

## 2.2 WSL2 Ubuntu 설치 (Windows 환경 전용)
---
**참고:** Ubuntu 호스트를 사용하는 경우 WSL2 설치를 건너뛸 수 있습니다.  

1.	**제어판 -> 프로그램 -> Windows 기능 켜기/끄기 -> 가상 머신 플랫폼 및 Hyper-V 사용**을 클릭하여 Windows 기능을 설정합니다.
2.	Windows Powershell을 **“관리자 권한으로 실행”.** 으로 실행합니다.
3.	WSL2 시스템을 활성화합니다.
    ```
    dism.exe /online /enable-feature /featurename:Microsoft-Windows-Subsystem-Linux /all /norestart
    ```
4.	가상 머신 기능을 활성화합니다.
    ```
    dism.exe /online /enable-feature /featurename:VirtualMachinePlatform /all /norestart
    ```
5.	WSL의 기본 버전을 2(WSL2)로 설정합니다.
    ```
    wsl --set-default-version 2
    ```
6.	Microsoft Store에서 Ubuntu 22.04 LTS를 검색하여 다운로드합니다.

    * Linux 커널 업데이트 패키지를 다운로드해야 하는 경우 [여기](https://learn.microsoft.com/ko-kr/windows/wsl/install-manual)에서 최신 패키지를 다운로드하십시오.
7.	WSL 목록에서 Ubuntu 22.04를 확인합니다.
    ```
    wsl --list -online
    ```
8.	Ubuntu 22.04를 설치합니다.
    ```
    wsl --install Ubuntu-22.04
    ```
9.	Windows 검색창에서 WSL2를 검색하여 실행합니다. 

</br></br></br>

## 2.3 Linux 환경 설정
---
호스트 PC에 Linux 환경을 구성하려면 다음 단계를 따르십시오.  

1. WSL2 실행 (Windows 환경 전용)  
    Windows를 사용하는 경우 Windows PowerShell에서 다음 명령 중 하나를 실행하여 WSL2를 시작합니다.  
    ```
    wsl
    ```
    ```
    ubuntu
    ```

2.	패키지 목록 업데이트  
새 소프트웨어를 설치하기 전에 사용 가능한 패키지 목록을 업데이트하여 최신 버전과 의존성을 확보하십시오. 다음 명령은 저장소에서 사용 가능한 최신 패키지 목록을 가져옵니다.
    ```
    sudo apt update && /
    sudo apt upgrade
    ```

3.	공통 개발 도구 설치  
    다음 명령을 입력하여 공통 개발 도구를 설치합니다.
    ```
    sudo apt install build-essential git
    ```

**참고:** 이 명령은 build-essential 패키지와 git을 모두 설치합니다.

</br></br></br></br>

# 3. 툴체인
---
VCP-G는 **gcc-linaro-7.2.1-2017.11-x86_64_arm-eabi** 툴체인을 사용합니다.  
이 툴체인은 ARM 아키텍처에 최적화되어 있으며 VCP-G의 TCC7045 칩과의 호환성을 보장합니다.

</br></br></br>

## 3.1 툴체인 설치 및 설정
---
다음 단계에 따라 툴체인을 다운로드하고 압축을 해제한 후 설정하십시오.  
1. 툴체인 다운로드  
   Linaro 웹사이트에서 툴체인을 다운로드하려면 **wget** 명령을 입력합니다.
    ```
    wget https://releases.linaro.org/components/toolchain/binaries/7.2-2017.11/arm-eabi/gcc-linaro-7.2.1-2017.11-x86_64_arm-eabi.tar.xz
    ```
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/Download%20Toolchain.png"></p>
    <p align="center"><strong>그림 3.1 툴체인 다운로드</strong></p>
    
2. 툴체인 압축 해제  
    다운로드가 완료되면 .tar.xz 파일의 내용을 압축 해제합니다.
    ```
    tar -xvf gcc-linaro-7.2.1-2017.11-x86_64_arm-eabi.tar.xz
    ```
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/Extract%20Toolchain.png"></p>
    <p align="center"><strong>그림 3.2 툴체인 압축 해제</strong></p>
    
3. 툴체인을 /opt로 이동  
    /opt 디렉터리는 Linux에서 선택적 소프트웨어를 설치하는 표준 위치입니다. 압축 해제한 툴체인을 이 디렉터리로 이동합니다.
    ```
    sudo mv gcc-linaro-7.2.1-2017.11-x86_64_arm-eabi /opt/
    ```
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/Move%20Toolchain.png"></p>
    <p align="center"><strong>그림 3.3 툴체인 이동</strong></p>

</br></br></br>

## 3.2 툴체인 확인
---
툴체인이 올바르게 설치되었는지 확인합니다.  
1. 툴체인 디렉터리로 이동
    ```
    cd /opt/gcc-linaro-7.2.1-2017.11-x86_64_arm-eabi
    ```
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/Navigate%20to%20Toolchain%20Directory.png"></p>
    <p align="center"><strong>그림 3.4 툴체인 디렉터리로 이동</strong></p>
    
2. 설치된 GCC 컴파일러 버전 확인
    ```
    ./bin/arm-eabi-gcc --version
    ```
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/Check%20Version%20of%20Installed%20GCC%20Compiler.png"></p>
    <p align="center"><strong>그림 3.5 설치된 GCC 컴파일러 버전 확인</strong></p>

GCC 컴파일러 설치가 완료되면 설치된 GCC 컴파일러 버전이 **gcc-linaro-7.2.1-2017.11.** 과 일치하는지 확인하십시오.

</br></br></br></br>

# 4. 소스 코드 클론
---
이 장에서는 Git을 사용하여 소스 코드를 클론하는 방법을 설명합니다.

</br></br></br>

## 4.1 VCP-G 소스 코드 클론
---
VCP-G의 소스 코드를 받으려면 **git clone** 명령을 입력하십시오. 이 명령은 원격 저장소의 사본을 로컬 컴퓨터에 생성하여 코드를 직접 다룰 수 있게 합니다.

다음 단계에 따라 VCP-G 소스 코드를 클론하십시오.
1. 터미널 열기  
    Ubuntu 22.04 시스템에서 터미널 애플리케이션을 실행합니다.

2. 원하는 디렉터리로 이동  
    소스 코드를 저장할 적절한 위치를 선택합니다. 예를 들어 홈 디렉터리에 저장소를 저장하려면 다음 명령을 사용합니다.
    ```
    cd ~
    ```
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/Navigate%20to%20Desired%20Directory.png"></p>
    <p align="center"><strong>그림 4.1 원하는 디렉터리로 이동</strong></p>

3. 저장소 클론  
    다음 명령을 사용하여 제공된 git 주소에서 VCP-G 소스 코드를 클론합니다.
    ```
    git clone https://github.com/topst-development/FreeRTOS-VCP.git topst-vcp
    ```
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/Figure%204.2%20Clone%20Repository.png"></p>
    <p align="center"><strong>그림 4.2 저장소 클론</strong></p>

4. 클론한 디렉터리로 이동  
    클론이 완료되면 다음 명령을 사용하여 소스 코드가 있는 디렉터리로 이동합니다.
    ```
    cd topst-vcp
    ```
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/Navigate%20to%20Cloned%20Directory.png"></p>
    <p align="center"><strong>그림 4.3 클론한 디렉터리로 이동</strong></p>

이제 VCP-G 소스 코드를 로컬에서 빌드 및 개발에 사용할 수 있습니다.

</br></br></br>

## 4.2 소스 코드 구조
---
클론 후 **ls** 명령을 입력하여 디렉터리 내용을 나열하고 주요 파일을 확인하여 소스 코드 구조를 파악하십시오.
```
ls

build  documents  easy-setup_vcp.sh  LICENSE  scripts  sources  tools
```

</br></br></br></br>

# 5. 빌드 가이드
---
## 5.1 easy-setup_vcp-g.sh 실행
---
./easy-setup_vcp-g.sh 스크립트를 실행하면 다음 화면이 표시됩니다.

**주의**: ./easy-setup_vcp-g.sh를 다시 실행할 때 yes를 선택하면 빌드된 소스가 삭제되므로 주의하십시오.
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20AI-G/Software/Linux%20SDK/license1.png"></p>
<p align="center"><strong>그림 5.1 최종 사용자 라이선스 계약</strong></p>

화면 하단까지 스크롤하여 이 고지 사항을 읽으십시오. 고지 사항을 읽은 후 오른쪽 화살표 키와 [Enter]를 누르십시오.
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20AI-G/Software/Linux%20SDK/license2.png"></p>
<p align="center"><strong>그림 5.2 'Proceed to confirm'으로 이동</strong></p>


그러면 다음 화면을 볼 수 있습니다. 
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20AI-G/Software/Linux%20SDK/license3.png" ></p>
<p align="center"><strong>그림 5.3 Accept 화면 </strong></p>
[Enter]를 눌러 Accept를 선택하면 다음 명령으로 빌드할 수 있습니다.

</br></br></br>

## 5.2 Makefile 및 빌드 시스템
---
Makefile은 많은 빌드 시스템의 핵심 구성 요소입니다. 여기에는 프로그램을 컴파일하고 링크하기 위한 **make** 유틸리티용 규칙과 지시문이 포함되어 있습니다. Makefile을 활용하면 빌드 과정을 자동화하여 일관성과 효율성을 확보할 수 있습니다.

</br></br></br>

## 5.3 빌드 프로세스 시작
---
소스 코드를 빌드하려면 다음 단계를 따르십시오.  
1. 빌드 디렉터리로 이동합니다.
    ```
    cd build/tcc70xx/gcc/
    ```
2. **make** 명령을 실행합니다.  
    ```
    make
    ```
    **make** 명령은 현재 디렉터리의 Makefile을 읽고 빌드 프로세스를 실행합니다.
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/Run%20make%20Command.png"></p>
    <p align="center"><strong>그림 5.4 make 명령 실행 </strong></p>
    
3. 빌드 결과 확인  
    빌드 프로세스가 완료되면 터미널에 다음 출력 파일이 표시되어야 합니다.
    - output/tcc70xx_pflash_boot.rom
    - output/tcc70xx_pflash_boot_2M_ECC.rom
    - output/tcc70xx_pflash_boot_3M_ECC.rom
    - output/tcc70xx_pflash_boot_4M_ECC.rom
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/Verify%20Build%20Output.png"></p>
    <p align="center"><strong>그림 5.5 빌드 결과 확인</strong></p>
   
    출력 파일 목록을 확인하려면 다음 명령을 사용합니다.
    ```
    ls output/ -al
    ```
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/Build%20Output%20File.png"></p>
    <p align="center"><strong>그림 5.6 빌드 출력 파일</strong></p>

</br></br></br></br>

# 6. 펌웨어 다운로드
---
이 장에서는 Linux 기반 개발 환경에서 ***FWDN***을 VCP-G에 다운로드하는 방법을 설명합니다.

</br></br></br>

## 6.1 VCP-G 준비
---
다운로드를 시작하기 전에 VCP-G가 안정된 위치에 있고 외부 간섭이 없는지 확인하십시오. 모든 스위치와 커넥터에 쉽게 접근할 수 있고 3.3V 전원 케이블이 올바르게 연결되어 있는지 확인하십시오.

</br></br></br>

## 6.2 하드웨어를 호스트 PC에 연결
---
Ubuntu 호스트를 사용하는 경우 3단계로 바로 진행하십시오.  
1. usbipd-win 다운로드  
    WSL2에서 USB를 사용하려면 usbipd-win 프로젝트가 필요합니다.   
    다음 링크에서 usbipd-win을 다운로드합니다: https://learn.microsoft.com/ko-kr/windows/wsl/connect-usb#attach-a-usb-device.
2. PowerShell을 실행하여 VCP-G(Windows에서 COM 포트로 인식됨)를 WSL2에 연결  
    Linux가 아닌 Windows PowerShell에서 다음 명령을 실행합니다.
    ```
    usbipd list
    ```
    ```
    usbipd bind --busid <busid>
    ```
    ```
    usbipd attach --wsl --busid <busid>
    ```
3. USB Type-C 케이블 연결  
    USB Type-C 케이블을 사용하여 VCP-G 보드를 개발용 호스트 PC에 연결합니다.
4. USB 연결 확인  
    WSL2에서 다음 명령을 실행합니다.
    ```
    sudo apt-get install usbutils && lsusb
    ```
    ```
    sudo dmesg | grep tty
    ```
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/Verify%20USB%20Connection.png"></p>
    <p align="center"><strong>그림 6.1 USB 연결 확인</strong></p>

그림 6.1에 표시된 출력이 나타나면 연결이 정상적으로 완료된 것입니다.

</br></br></br>

## 6.3 VCP-G에 소프트웨어 다운로드
---

### 6.3.1 Windows 환경에서 FWDN 실행
1. 보드를 다운로드 모드로 설정  
   FWDN 스위치를 누른 상태에서 VCP-G 보드에 전원 케이블을 연결합니다.
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/Set%20Board%20to%20Download%20Mode.png"></p>
    <p align="center"><strong>그림 6.2 보드를 다운로드 모드로 설정</strong></p>

2. tcc70xx_pflash_boot_2M_ECC.rom을 fwdn_vcp 폴더로 복사
```
cp ~/topst-vcp/build/tcc70xx/gcc/output/tcc70xx_pflash_boot_2M_ECC.rom ~/topst-vcp/tools/fwdn_vcp/
```

3. fwdn_vcp 폴더를 C 드라이브로 복사
```
cp -r ~/topst-vcp/tools/fwdn_vcp /mnt/c/
```

4. fwdn_vcp.bat 클릭  
    ***FWDN***을 사용하여 빌드된 소프트웨어를 VCP-G의 4 MB 플래시에 다운로드합니다.

    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/Click%20fwdn_vcp.bat.png"></p>
    <p align="center"><strong>그림 6.3 fwdn_vcp.bat 클릭</strong></p>
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

5. 보드를 리셋합니다  
    다운로드 과정이 완료되면 전원 케이블을 분리한 후 다시 연결합니다.
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/Reset%20the%20Board.png"></p>
    <p align="center"><strong>그림 6.4 보드 리셋</strong></p>

### 6.3.2 Linux 환경에서 FWDN 실행
1. 보드를 다운로드 모드로 설정  
   FWDN 스위치를 누른 상태에서 VCP-G 보드에 전원 케이블을 연결합니다.
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/Set%20Board%20to%20Download%20Mode.png"></p>
    <p align="center"><strong>그림 6.5 보드를 다운로드 모드로 설정</strong></p>
    
2. 다운로드 명령 실행  
   ***FWDN***을 사용하여 빌드된 소프트웨어를 VCP-G의 4 MB 플래시에 다운로드합니다.
    ```
    sudo ~/topst-vcp/tools/fwdn_vcp/fwdn --fwdn ~/topst-vcp/tools/fwdn_vcp/vcp_fwdn.rom -w output/tcc70xx_pflash_boot_2M_ECC.rom
    ```
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/Execute%20Download%20Command.png"></p>
    <p align="center"><strong>그림 6.6 다운로드 명령 실행</strong></p>
    
3. 보드를 리셋합니다  
    다운로드 과정이 완료되면 전원 케이블을 분리한 후 다시 연결합니다.
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/Reset%20the%20Board.png"></p>
    <p align="center"><strong>그림 6.7 보드 리셋</strong></p>

</br></br></br>

## 6.4 보드에서 소프트웨어 확인
---
소프트웨어를 보드에 다운로드한 후 다음 단계에 따라 정상적으로 동작하는지 확인합니다.
1. minicom 설치  
    ```
    sudo apt install minicom
    ```
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/Install%20Minicom.png"></p>
    <p align="center"><strong>그림 6.8 minicom 설치</strong></p>
2. 시리얼 연결 열기  
    다음 명령을 사용하여 시리얼 연결을 시작합니다.
    ```
    minicom -D /dev/ttyUSB0 -b 115200 -8
    ```
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/Open%20Serial%20Connection.png"></p>
    <p align="center"><strong>그림 6.9 시리얼 연결 열기</strong></p>

1단계와 2단계를 완료하면 터미널에 다음과 같은 출력이 나타납니다. 연결에 성공하면 보드가 입력에 응답하며, 이를 통해 소프트웨어가 VCP-G에 다운로드되어 정상적으로 동작하고 있음을 확인할 수 있습니다.
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/Figure%206.7%20Open%20Serial%20Connection.png"></p>
<p align="center"><strong>그림 6.10 시리얼 연결 열기</strong></p>

</br></br></br>

## 6.5 일반적인 문제 해결
---
이 장에서는 VCP-G를 사용할 때 발생하는 일반적인 문제에 대한 해결 방법을 제공합니다.

**문제:** ***FWDN***이 ttyUSB0 장치에 접근할 권한이 없다고 보고합니다.  
**해결 방법:** 이 문제는 사용자 계정(**$USER**)에 시리얼 장치에 접근할 수 있는 권한이 없을 때 발생합니다. 이를 해결하려면 사용자 계정을 dialout 그룹에 추가하십시오.

1. 사용자 그룹 권한 수정  
    다음 명령을 실행합니다.
    ```
    sudo usermod -aG dialout $USER
    ```
2. 로그아웃 후 다시 로그인  
    현재 세션에서 로그아웃한 후 다시 로그인하여 변경 사항을 적용합니다. 그런 다음 ttyUSB0 장치에 다시 접근해 보십시오.
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/Modify%20User%20Group%20Permissions.png"></p>
    <p align="center"><strong>그림 6.11 사용자 그룹 권한 수정 </strong></p>

**문제:** minicom을 사용할 때 VCP-G와 통신이 정상적으로 이루어지지 않거나 동작이 불규칙합니다.  
**해결 방법:** 이 문제는 minicom의 기본 흐름 제어 설정이 **hardware**로 되어 있는 경우에 발생할 수 있습니다. 정상적으로 동작하려면 하드웨어 흐름 제어를 No로 설정해야 합니다. 
1. minicom 시작  
    다음 명령을 사용합니다.
    ```
    minicom -D /dev/ttyUSB0 -b 115200 -8
    ```
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/Launch%20Minicom.png"></p>
    <p align="center"><strong>그림 6.12 minicom 실행</strong></p>
2. 설정 화면 접근  
    minicom 실행 중에 **[Ctrl+A]**를 누른 다음 **[o]**를 눌러 설정 메뉴를 엽니다.
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/Access%20Set%20up%20Screen.png"></p>
    <p align="center"><strong>그림 6.13 설정 화면 접근</strong></p>
3. Serial Port Setup으로 이동  
    옵션에서 **Serial port setup**을 선택합니다.
4. 흐름 제어 수정  
    시리얼 포트 설정에서 **[F]**를 눌러 하드웨어 흐름 제어를 **No**로 설정합니다.
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/Modify%20Flow%20Control.png"></p>
    <p align="center"><strong>그림 6.14 흐름 제어 수정</strong></p>
5. 종료 및 저장  
    설정을 종료하고 구성을 저장합니다. 이제 minicom이 VCP-G와 정상적으로 통신합니다.
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/Save%20and%20Exit.png"></p>
    <p align="center"><strong>그림 6.15 저장 후 종료</strong></p>

**참고:** minicom 이외의 다른 시리얼 통신 도구를 사용하는 경우, 정상적인 동작을 위해 해당 도구의 흐름 제어 설정도 **No**로 지정하십시오.
</br></br></br></br>

# 7. 참고 자료
---
- 자세한 내용은 TOPST에 문의하십시오: topst@topst.ai

**참고:** 참조 문서는 계약 조건에 따라 제공이 가능한 경우 제공될 수 있습니다. 참조
문서를 이용할 수 없는 경우에는 개발과 직접 관련된 내용을 안내받을 수 있습니다.
