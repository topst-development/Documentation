# 1. 소개
---
이 문서는 호스트 환경 설정, SDK 빌드, 펌웨어 다운로더 사용 및 Ubuntu 다운로드를 포함하여 D3-G SDK를 빌드하기 위한 가이드라인을 제공합니다.
 
이 문서는 다음 정보를 포함합니다:
- 호스트 환경 설정
- 이미지 빌드 가이드
- 펌웨어 다운로드 가이드
- D3-G 보드와 PC 연결
 
<br/><br/><br/><br/>
 
# 2. 호스트 환경 설정
---
이 장에서는 Windows와 Ubuntu에 대한 별도의 가이드를 통해 호스트 PC 환경을 설정하는 방법에 대한 지침을 제공합니다.
</br><br/><br/>
 
## 2.1 Windows 환경
---
이 문서에서는 Windows PC에서 Linux를 사용하기 위해 WSL(Windows Subsystem for Linux)을 설정하는 방법에 대해 설명합니다.
D3-G Linux SDK는 Yocto Project를 기반으로 하므로 D3-G SDK의 Linux 버전은 Yocto 프로젝트를 따릅니다.
다른 버전의 Linux를 설치할 수 있지만, 이 문서에서는 Ubuntu 22.04 기반의 D3-G Linux SDK에 대해 설명합니다.
호스트 OS가 Ubuntu인 경우 2.2장으로 진행하십시오.
 
</br><br/>
 
### 2.1.1 WSL2 Ubuntu 설치
1. "**관리자 권한으로 실행**"으로 Windows PowerShell을 실행합니다.
2. WSL2 시스템을 활성화합니다.
    ```
    dism.exe /online /enable-feature /featurename:Microsoft-Windows-Subsystem-Linux /all /norestart
    ```
3. 가상 머신 기능을 활성화합니다.
    ```
    dism.exe /online /enable-feature /featurename:VirtualMachinePlatform /all /norestart
    ```
4. WSL 2를 기본 버전으로 설정합니다.
    ```
    wsl --set-default-version 2
    ```
5. Microsoft Store에서 Ubuntu 22.04.3 LTS를 검색하여 다운로드합니다.
 
    * Linux 커널 업데이트 패키지를 다운로드해야 하는 경우 [여기](https://learn.microsoft.com/ko-kr/windows/wsl/install-manual)에서 최신 패키지를 다운로드하십시오.
 
6. Ubuntu 설치 중 사용자 이름을 선택하십시오.
</br><br/>
 
### 2.1.2 WSL2를 통해 Ubuntu 액세스
Windows 명령 프롬프트를 열고 다음 명령을 입력하여 Ubuntu에 액세스합니다.
Ubuntu에 액세스하면 기본적으로 /mnt/c/Users/[username] 디렉토리에서 시작됩니다.
```
wsl  // ubuntu 액세스
ls   // 디렉토리 내용 확인
```
결과를 확인하려면 그림 2.1을 참조하십시오(시스템에 따라 결과가 다를 수 있음).
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20D3-G/Software/1.1%20wsl%20linux.png" width="500"></p>
<p align="center"><strong>그림 2.1 WSL2 스크린샷 </strong></p>
 
<br/><br/>
 
### 2.1.3 로케일 설정
 
WSL에서 Ubuntu를 실행한 후 적절한 언어 및 지역 설정을 보장하기 위해 로케일을 설정해야 합니다. en_US.UTF-8을 사용하는 것이 좋습니다. en_US.UTF-8을 사용하려면 다음 명령을 실행하십시오.
 
```
sudo locale-gen en_US.UTF-8 && sudo update-locale LANG=en_US.UTF-8 
```
 
로케일을 설정한 후 다음 명령을 사용하여 로케일 유형을 확인할 수 있습니다.
 
```
echo 'LANG=en_US.UTF-8' | sudo tee -a /etc/default/locale && \  
 
echo 'LC_ALL=en_US.UTF-8' | sudo tee -a /etc/default/locale 
```
<br/><br/>
 
### 2.1.4 SSH 및 Samba 설치
 
Ubuntu에 진입한 후 보다 편리한 개발 환경을 위해 SSH 및 Samba와 같은 추가 유틸리티를 사용할 수 있습니다. SSH 및 Samba를 사용하면 원격 컴퓨터에서 명령을 실행하고 다른 컴퓨터로 파일을 복사할 수 있습니다.
 - 다음 단계는 호스트 PC가 네트워크에 연결되어 있어야 합니다. 다음 명령을 사용하여 네트워크 상태를 확인하십시오.
  ```
  $ sudo apt-get update
  $ sudo apt-get install -y net-tools
  $ ifconfig 
  ```
 
SSH 및 Samba가 이미 설치되어 있거나 사용하지 않을 경우 이 장을 건너뛸 수 있습니다.
 
다음 명령을 사용하여 net-tools, SSH, Samba를 설치하십시오.
 
```
$ sudo apt-get update 
$ sudo apt install -y net-tools openssh-server samba
```
SSH 및 Samba를 설치한 후 환경에 필요에 따라 각 프로그램을 구성하십시오.
</br><br/>
 
### 2.1.5 유틸리티 설치
 
다음 명령을 사용하여 필요한 모든 유틸리티를 한 번에 설치하십시오. Yocto Project를 사용하려면 호스트 PC(개별 컴퓨터 또는 개발 서버)에 다음 유틸리티가 설치되어 있어야 합니다.
 
 
```
$ sudo apt-get install -y gawk wget git diffstat unzip texinfo gcc-multilib build-essential chrpath
 
$ sudo apt-get install -y socat cpio python3 python3-pip python3-pexpect xz-utils debianutils
 
$ sudo apt-get install -y iputils-ping python3-git python3-jinja2 libegl1-mesa-dev libsdl1.2-dev pylint
 
$ sudo apt-get install -y xterm zstd ncftp curl git-lfs vim zip lz4
```
 
<br/><br/>
 
### 2.1.6 Repo 설치
 
Repo가 이미 설치되어 있는 경우 다시 설치하지 않고 사용할 수 있습니다.
Repo를 설치하기 전에 Python 버전 3.6 이상이 설치되어 있는지 확인하십시오.
 
다음 명령을 사용하여 Repo를 설치하십시오.
```
$ sudo apt-get install repo
```
 
'/usr/bin/env 'python' no such file or directory' 오류 메시지가 표시되면 다음 명령을 사용하여 'python'을 'python3'에 연결하십시오.
 
```
$ sudo ln -sf /usr/bin/python3 /usr/bin/python
```
Repo 오류가 발생하면 다음 명령을 사용하여 최신 버전을 다운로드하고 /usr/bin/ 폴더에 배치하십시오.
 
```
$ mkdir -p ~/bin
 
$ curl http://commondatastorage.googleapis.com/git-repo-downloads/repo > ~/bin/repo
 
$ chmod a+x ~/bin/repo
 
$ sudo mv ~/bin/repo /usr/bin/repo
```
**3장: 이미지 빌드 가이드**로 진행하십시오.
 
<br/><br/><br/>
 
## 2.2 Linux 환경
---
이 장에서는 호스트 OS로 Ubuntu를 설정하는 과정을 설명합니다.
</br><br/>
 
### 2.2.1 환경 설정
다음 장(2.2.2 ~ 2.2.5)은 Ubuntu 터미널에서 실행해야 합니다. 터미널을 열려면 바로 가기 키 [Ctrl + Alt + T]를 사용하십시오.
<br/><br/>
 
### 2.2.2 로케일 설정
 
WSL에서 Ubuntu를 실행한 후 적절한 언어 및 지역 설정을 보장하기 위해 로케일을 설정해야 합니다. en_US.UTF-8을 사용하는 것이 좋습니다. en_US.UTF-8을 사용하려면 다음 명령을 실행하십시오.
 
```
sudo locale-gen en_US.UTF-8 && sudo update-locale LANG=en_US.UTF-8 
```
 
로케일을 설정한 후 다음 명령을 사용하여 로케일 유형을 확인할 수 있습니다.
 
```
echo 'LANG=en_US.UTF-8' | sudo tee -a /etc/default/locale && \  
 
echo 'LC_ALL=en_US.UTF-8' | sudo tee -a /etc/default/locale 
```
<br/><br/>
 
### 2.2.3 SSH 및 Samba 설치
 
Ubuntu에 진입한 후 보다 편리한 개발 환경을 위해 SSH 및 Samba와 같은 추가 유틸리티를 사용할 수 있습니다. SSH 및 Samba를 사용하면 원격 컴퓨터에서 명령을 실행하고 다른 컴퓨터로 파일을 복사할 수 있습니다.
 - 다음 단계는 호스트 PC가 네트워크에 연결되어 있어야 합니다. 다음 명령을 사용하여 네트워크 상태를 확인하십시오.
  ```
  $ sudo apt-get update
  $ sudo apt-get install -y net-tools
  $ ifconfig 
  ```
 
SSH 및 Samba가 이미 설치되어 있거나 사용하지 않을 경우 이 장을 건너뛸 수 있습니다.
 
다음 명령을 사용하여 SSH, Samba를 설치하십시오.
 
```
$ sudo apt-get update 
$ sudo apt install -y openssh-server samba
```
SSH 및 Samba를 설치한 후 환경에 필요에 따라 각 프로그램을 구성하십시오.
 
<br/><br/>
 
### 2.2.4 유틸리티 설치
 
다음 명령을 사용하여 필요한 모든 유틸리티를 한 번에 설치하십시오. Yocto Project를 사용하려면 호스트 PC(개별 컴퓨터 또는 개발 서버)에 다음 유틸리티가 **반드시** 설치되어 있어야 합니다.
****
 
 
```
$ sudo apt-get install -y gawk wget git diffstat unzip texinfo gcc-multilib build-essential chrpath
 
$ sudo apt-get install -y socat cpio python3 python3-pip python3-pexpect xz-utils debianutils
 
$ sudo apt-get install -y iputils-ping python3-git python3-jinja2 libegl1-mesa-dev libsdl1.2-dev pylint
 
$ sudo apt-get install -y xterm zstd ncftp curl git-lfs vim zip lz4
```
 
<br/><br/>
 
### 2.2.5 Repo 설치
 
Android Repo를 통해 D3-G SDK를 다운로드할 수 있습니다.
Repo를 설치하려면 다음 웹사이트를 참조하십시오: https://source.android.com/source/downloading.html.
Repo가 이미 설치되어 있는 경우 다시 설치하지 않고 사용할 수 있습니다.
Repo를 설치하기 전에 Python 버전 3.6 이상이 설치되어 있는지 확인하십시오.
 
다음 명령을 사용하여 Repo를 설치하십시오.
```
$ sudo apt-get install repo
```
 
'/usr/bin/env 'python' no such file or directory' 오류 메시지가 표시되면 다음 명령을 사용하여 'python'을 'python3'에 연결하십시오.
 
```
$ sudo ln -sf /usr/bin/python3 /usr/bin/python
```
Repo 오류가 발생하면 다음 명령을 사용하여 최신 버전을 다운로드하고 /usr/bin/ 폴더에 배치하십시오.
 
```
$ mkdir -p ~/bin
 
$ curl http://commondatastorage.googleapis.com/git-repo-downloads/repo > ~/bin/repo
 
$ chmod a+x ~/bin/repo
 
$ sudo mv ~/bin/repo /usr/bin/repo
```
 
<br/><br/>
 
### 2.2.6 Telechips USB 장치용 Udev 규칙
다음 명령을 실행한 후에는 Linux에서 FWDN을 다운로드할 때 더 이상 'sudo' 명령을 사용할 필요가 없습니다.
```
$ echo "SUBSYSTEM==\"usb\", ATTR{idVendor}==\"140e\", MODE=\"0666\", OWNER=\"${USER}\"" | sudo tee /etc/udev/rules.d/99-topst.rules
$ sudo udevadm control --reload-rules && sudo udevadm trigger
```
**3장: 이미지 빌드 가이드**로 진행하십시오.
 
<br/><br/><br/><br/>
 
# 3. 이미지 빌드 가이드
---
이 장에서는 호스트 PC에 설치된 Ubuntu OS(WSL이든 로컬 Ubuntu 설치이든 관계없이)를 기반으로 지침을 제공합니다. D3-G에 업로드할 이미지는 Yocto Project를 사용하여 빌드되므로 빌드 프로세스는 Ubuntu 환경에서 수행해야 합니다.
</br></br>
 
## 3.1 SDK 빌드 준비
---
D3-G Linux SDK는 Yocto Project 4.0 Kirkstone을 기반으로 합니다. 따라서 D3-G Linux SDK를 사용하려면 호스트 PC에 Yocto Project 환경을 구성해야 합니다. SDK, 소스 미러 및 도구를 다운로드하려면 필요한 유틸리티를 설치해야 합니다. 이미지를 원활하게 빌드하려면 PC에 **최소 60GB의 사용 가능한 스토리지**와 **최소 16GB의 RAM**이 있어야 합니다.
 
</br><br/>  
 
## 3.2 Yocto Project  
---
Yocto Project는 임베디드 Linux 개발에 중점을 둔 오픈 소스 프로젝트입니다.
Poky인 Open Embedded 프로젝트와 빌드 시스템인 ***bitbake***를 결합하여 Linux 이미지를 만듭니다.
Yocto Project를 사용하면 부트로더, 커널 및 rootfs를 동시에 빌드할 수 있습니다.
 
<br/><br/>
 
## 3.3 Yocto Project 작업 프로세스
---
그림 3.1은 Yocto Project의 작업 프로세스를 보여줍니다. 메타데이터를 기반으로 업스트림에서 소스를 다운로드하고 빌드할 수 있습니다. 빌드가 완료되면 패키지, 이미지 및 SDK가 결과로 제공됩니다.
 
<p align="center">
    <img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20D3-G/Software/2.1%20yocto%20project%20task%20process.png", width="700">
</p>
<p align="center"><strong>그림 3.1 Yocto Project 작업 프로세스</strong></p>
 
<br/><br/>
 
## 3.4 D3-G SDK 구성
---
다음은 우리가 구성한 Yocto Project의 구성 요소입니다.
표 3.1은 D3-G SDK의 구성을 보여줍니다.
 
 
 
**표 3.1 D3-G SDK 구성**
<table border="1" cellspacing="0" cellpadding="5">
  <colgroup>
    <col style="width: 10%">
    <col style="width: 10%">
    <col style="width: 10%">
    <col style="width: 56%">
  </colgroup>
  <thead>
    <tr>
      <th colspan="3"style="text-align: center; vertical-align: middle;"><strong>항목</strong></th>
      <th style="text-align: center; vertical-align: middle;" ><strong>설명</strong></th>
    </tr>
  </thead>
  <tbody>
  <tr>
      <td colspan="3"style="text-align: center; vertical-align: middle;">easy-setup.sh</td>
      <td>SDK를 자동으로 다운로드하고 빌드하는 Python 스크립트</td>
    </tr>
    <tr>
      <td colspan="3"style="text-align: center; vertical-align: middle;">stitch-fai-ai.sh</td>
      <td>AI-G fai 이미지 생성 스크립트 (minimal + Sample Application)</td>
    </tr>
    <tr>
      <td colspan="3"style="text-align: center; vertical-align: middle;">stitch-fai-d3.sh</td>
      <td>D3-G fai 이미지 생성 스크립트 (minimal + Sample Application)</td>
    </tr>
    <tr>
      <td colspan="3"style="text-align: center; vertical-align: middle;">mktcimg</td>
      <td rowspan="2">빌드 프로세스 및 <strong>FWDN</strong> 관련 도구</td>
    </tr>
    <tr>
      <td colspan="3"style="text-align: center; vertical-align: middle;">tools</td>
    </tr>
    <tr>
      <td rowspan="8"style="text-align: center; vertical-align: middle;">poky</td>
      <td colspan="2"style="text-align: center; vertical-align: middle;">poky</td>
      <td>Yocto Project 4.0 Kirkstone 빌드 시스템</td>
    </tr>
    <tr>
      <td colspan="2"style="text-align: center; vertical-align: middle;">meta-openembedded</td>
      <td>OE-Core를 지원하는 레이어</td>
    </tr>
    <tr>
      <td colspan="2"style="text-align: center; vertical-align: middle;">meta-arm</td>
      <td>ARM 툴체인을 지원하는 레이어</td>
    </tr>
    <tr>
      <td colspan="2"style="text-align: center; vertical-align: middle;">meta-topst-bsp</td>
      <td>TOPST BSP를 지원하는 레이어</td>
    </tr>
    <tr>
      <td colspan="2"style="text-align: center; vertical-align: middle;">meta-gplv2</td>
      <td>GPLv3 라이선스를 피하는 패키지가 포함된 레이어</td>
    </tr>
    <tr>
      <td colspan="2"style="text-align: center; vertical-align: middle;">meta-topst</td>
      <td>TOPST 레시피</td>
    </tr>
  </tbody>
</table>
<br/><br/><br/>
 
 
## 3.5 빌드 준비
---
다음 장에서는 D3-G 이미지를 빌드하기 위해 Yocto Project를 구성하는 방법을 설명합니다.
 
<br/><br/>
 
### 3.5.1 .gitconfig에서 사용자 이메일 및 사용자 이름 설정
공식 TOPST git에서 D3-G SDK를 다운로드하려면 이메일과 이름을 구성하십시오.
1. 다음 명령을 입력하십시오.
```
vi ~/.gitconfig
```
2. 다음 정보를 입력하십시오
```
[user]
    email = User email
    name = User name
```
 
<br/><br/>
 
### 3.5.2 Git에서 D3-G 가져오기
 
1. **topst-sdk**라는 새 디렉토리를 만들고 현재 디렉토리를 **topst-sdk**로 변경합니다.
 
```
$ mkdir topst-sdk
$ cd topst-sdk
```
 
2. 다음 명령을 실행하여 리포지토리를 초기화합니다.
 
```
$ repo init -u https://github.com/topst-development/manifests.git -b release/1.2.0 -m linux_yp4.0_topst.xml
```
 
명령을 실행한 후 다음 출력이 표시됩니다.
 
```
Downloading Repo source from https://gerrit.googlesource.com/git-repo
 
... A new version of repo (2.54) is available.
... New version is available at: /home/topst/topst-sdk/.repo/repo/repo
... The launcher is run from: /usr/bin/repo
!!! The launcher is not writable.  Please talk to your sysadmin or distro
!!! to get an update installed.
 
 
Your identity is: TopstDeveloper <topstdeveloper@gmail.com>
If you want to change this, please re-run 'repo init' with --config-name
 
repo has been initialized in /home/topst/topst-sdk
```
 
3. 다음 명령을 실행하여 리포지토리를 동기화합니다.
 
```
$ repo sync
```
 
명령을 실행한 후 다음 출력이 표시됩니다.
 
```
... A new version of repo (2.54) is available.
... New version is available at: /home/topst/topst-sdk/.repo/repo/repo
... The launcher is run from: /usr/bin/repo
!!! The launcher is not writable.  Please talk to your sysadmin or distro
!!! to get an update installed.
 
Fetching: 100% (12/12), done in 33.103s
Checking out:  25% (3/12), done in 0.863s
Checking out:  75% (9/12), done in 0.415s
repo sync has finished successfully.
```
 
<br/><br/><br/>
 
## 3.6 topst-build.sh 실행
---
./easy-setup.sh 스크립트를 실행하면 다음 화면을 볼 수 있습니다.
 
**주의: ./easy-setup.sh를 다시 실행하는 경우 yes를 선택하면 빌드된 소스가 삭제되므로 주의하십시오.**
```
./easy-setup.sh
```
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20AI-G/Software/Linux%20SDK/license1.png"></p>
<p align="center"><strong>그림 3.2 최종 사용자 라이선스 계약</strong></p>
 
화면 하단으로 스크롤하여 이 공지 사항을 읽으십시오. 이 공지 사항을 읽은 후 오른쪽 화살표 키와 [Enter]를 누르십시오.
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20AI-G/Software/Linux%20SDK/license2.png"></p>
<p align="center"><strong>그림 3.3 '계속 진행하여 확인'으로 이동</strong></p>
 
 
그러면 다음 화면을 볼 수 있습니다.
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20AI-G/Software/Linux%20SDK/license3.png" ></p>
<p align="center"><strong>그림 3.4 수락 화면 </strong></p>
 
 
빌드 이미지는 다음 경로에 생성됩니다:
 
- {TOPST_PATH}/build/d3-g-topst-main/tmp/deploy/images/d3-g-topst-main
 
topst-build.sh는 D3-G 및 AI-G용 이미지를 빌드하는 데 필요한 핵심 환경을 설정하는 셸 스크립트입니다. 다음 명령을 실행하고 옵션 2를 선택하여 D3-G에 메인 OS를 설치하기 위한 빌드 환경을 준비하십시오.
 
 
 
```
$ source poky/meta-topst/topst-build.sh 
Choose MACHINE
  1. ai-g-topst
  2. d3-g-topst-main
  3. d3-g-topst-sub
  4. d5-g-topst-main
  5. d5-g-topst-sub
select number(1-5) => 2
machine(d3-g-topst-main) selected.
You had no conf/local.conf file. This configuration file has therefore been
created for you from /home/topst/topst-sdk/poky/meta-topst/template/d3-g-topst-main/local.conf.sample
You may wish to edit it to, for example, select a different MACHINE (target
hardware). See conf/local.conf for more information as common configuration
options are commented.

You had no conf/bblayers.conf file. This configuration file has therefore been
created for you from /home/topst/topst-sdk/poky/meta-topst/template/d3-g-topst-main/bblayers.conf.sample
To add additional metadata layers into your configuration please add entries
to conf/bblayers.conf.

The Yocto Project has extensive documentation about OE including a reference
manual which can be found at:
    https://docs.yoctoproject.org

For more information about OpenEmbedded see the website:
    https://www.openembedded.org/

Yocto Project common targets are:
    core-image-minimal
    core-image-sato
    meta-toolchain
    adt-installer
    meta-ide-support


Telechips common targets are:
    telechips-topst-image-minimal
    telechips-topst-image-multimedia
    telechips-topst-image

    meta-toolchain-topst(Application Development Toolkit)


You can also run generated TOPST images on D3-G board

Other commonly useful commands are:
 - 'devtool' and 'recipetool' handle common recipe tasks
 - 'bitbake-layers' handles common layer tasks
 - 'oe-pkgdata-util' handles common target package tasks

```
 
다음 명령을 실행하여 메인 OS 빌드를 시작하십시오.
```
$ bitbake telechips-topst-image
```
 
<br/><br/><br/>

## 3.7 펌웨어 다운로더(FWDN) 이미지 만들기
---
이 옵션은 바이너리를 D3-G 플랫폼 이미지용 단일 이미지로 결합합니다.
 
**'output_d3g.fai' 빌드 이미지**와 **FWDN 도구**가 포함된 **output_d3g.fwdn.zip** 파일은 다음 경로에 생성됩니다:
 
-  ~/topst-sdk
 
```
$ cd ~/topst-sdk
 
$ ./stitch-fai-d3.sh -f
Filesystem too small for a journal
[mktcimg] v1.2.1 - Nov 15 2021 19:33:18
location : bl3_ca72_a
location : 4096 sector(2097152 byte)
location : build/d3-g-topst-main/tmp/deploy/images/d3-g-topst-main/ca72_bl3.rom
location : boot
location : 122880 sector(62914560 byte)
location : build/d3-g-topst-main/tmp/deploy/images/d3-g-topst-main/tc-boot-d3-g-topst-main.img
location : system
location : 33554432 sector(17179869184 byte)
location : build/d3-g-topst-main/tmp/deploy/images/d3-g-topst-main/telechips-topst-image-d3-g-topst-main.ext4
location : dtb
location : 400 sector(204800 byte)
location : build/d3-g-topst-main/tmp/deploy/images/d3-g-topst-main/tcc8050-topst-d3-g.dtb
path : build/d3-g-topst-main/tmp/deploy/images/d3-g-topst-main/ca72_bl3.rom
uuid : 7eb23c82-ccc0-44ce-8237-3315fc34e3f5 , part-name : bl3_ca72_a
uuid : 1c76ef36-314d-4548-8207-5ab1d1376ca2 , part-name : boot
uuid : b32eb80f-e014-4f17-b140-77bf3e137ba0 , part-name : system
uuid : 429d8444-87b0-4c1d-8b3f-278dec2616f3 , part-name : dtb
crc32 of header : 2a7c0194
crc32 of partition array : b181e432
idx : 0  bl3_ca72_a
idx : 1  boot
idx : 2  system
idx : 3  dtb
crc32 of header : 2a7c0194
crc32 of partition array : 990446d3
Complete to make fai file
 
===== arguments info =====
 
--storage_size : 17818182656
--parttype : gpt
--area_name : "SD Data"
--outfile : /home/topst/topst-sdk/.stitch_tOPE26E/output_d3g.fai
--gptfile : /home/topst/topst-sdk/.stitch_tOPE26E/output_d3g.gpt
--fplist : /home/topst/topst-sdk/.stitch_tOPE26E/partition.single.list
--sector_size : 512
--sparse_fill : 0
 
===========================
 
[+] Packaging FWDN binaries
  adding: boot-firmware/ (stored 0%)
  adding: boot-firmware/boot.dual.json (deflated 87%)
  adding: boot-firmware/prebuilt/ (stored 0%)
  adding: boot-firmware/prebuilt/subcore_optee.rom (deflated 93%)
  adding: boot-firmware/prebuilt/mcert.bin (deflated 96%)
  adding: boot-firmware/prebuilt/fwdn.rom (deflated 49%)
  adding: boot-firmware/prebuilt/bconf.dual.bin (deflated 95%)
  adding: boot-firmware/prebuilt/ca72_bl1.rom (deflated 53%)
  adding: boot-firmware/prebuilt/dram_params.bin (deflated 81%)
  adding: boot-firmware/prebuilt/hsm.cs.bin (deflated 13%)
  adding: boot-firmware/prebuilt/ca72_bl2.rom (deflated 54%)
  adding: boot-firmware/prebuilt/ca53_bl1.rom (deflated 53%)
  adding: boot-firmware/prebuilt/optee.rom (deflated 93%)
  adding: boot-firmware/prebuilt/ca53_bl2.rom (deflated 52%)
  adding: boot-firmware/prebuilt/hsm.bin (deflated 49%)
  adding: boot-firmware/prebuilt/bconf.single.bin (deflated 93%)
  adding: boot-firmware/prebuilt/scfw.rom (deflated 57%)
  adding: boot-firmware/prebuilt/tcc8050_snor.cs.rom (deflated 93%)
  adding: boot-firmware/boot.single.json (deflated 87%)
  adding: boot-firmware/fwdn.json (deflated 50%)
  adding: fwdn (deflated 69%)
  adding: fwdn.bat (deflated 40%)
  adding: fwdn.exe (deflated 62%)
  adding: fwdn.sh (deflated 40%)
  adding: output_d3g.fai (deflated 73%)
  adding: output_d3g.gpt (deflated 99%)
  adding: output_d3g.gpt.back (deflated 98%)
  adding: output_d3g.gpt.prim (deflated 98%)
  adding: VtcUsbPort.dll (deflated 68%)
 
```
 
다음 로그가 표시되면 "output_d3g.fwdn.zip" 파일이 생성된 것입니다.
```
$ ls
build  easy-setup.sh  mktcimg  output_d3g.fwdn.zip  poky  stitch-fai-ai.sh  stitch-fai-d3.sh  tools
```
 
</br></br><br/><br/>
 
# 4. 펌웨어 다운로드
---
이 장에서는 ***FWDN***을 사용하여 펌웨어를 D3-G에 다운로드하고 Linux 콘솔에 로그인하는 방법을 설명합니다.
***FWDN V8***은 Windows 10(11) 64비트 및 Linux 환경 모두에서 펌웨어를 다운로드하기 위한 PC 도구입니다. 이 장에서는 Windows 및 Linux 환경에서 다운로드하는 경우를 설명합니다.
 
<br/><br/><br/>
 
## 4.1 펌웨어 다운로드 순서
---
***FWDN***의 다운로드 순서는 다음과 같습니다:
 
1. 부트 모드 스위치를 USB 부트 모드로 설정합니다.
2. Windows 프롬프트 또는 Linux 콘솔을 엽니다.
3. ***FWDN V8***을 보드에 연결합니다.
4. fai 파일을 다운로드합니다.
 
<br/><br/><br/>
 
## 4.2 USB 부트 모드로 D3-G 보드와 호스트 PC 연결
---
펌웨어 다운로더(FWDN)는 호스트 PC와의 USB 통신을 통해 ROM 이미지를 D3-G에 씁니다.
 
D3-G에는 하나의 부트 모드 버튼이 있으며 두 가지 유형의 부트 모드를 지원합니다. 이 가이드는 FWDN 모드에 중점을 둡니다.
 
- USB 부트 모드 (FWDN 모드) : 호스트 PC의 FWDN 도구를 사용하여 ROM 이미지를 쓰는 데 사용됩니다.
 
- eMMC 부트 모드 : eMMC 장치에 저장된 ROM 이미지를 사용하여 D3-G를 부팅하는 데 사용됩니다.
 
**참고**: USB Type-C FWDN 포트는 펌웨어 다운로더(FWDN)에 사용됩니다.
 
 
 
FWDN을 사용하려면 다음과 같이 D3-G 보드를 호스트 PC에 연결하십시오:
 
1. 호스트 PC에 VTC 드라이버가 설치되어 있는지 확인하십시오. VTC 드라이버가 설치되어 있지 않은 경우 4.2.1장에 표시된 대로 설치하십시오.
 
2. USB Type-C 케이블 하나를 준비하십시오.
 
3. USB 부트 모드로 진입하려면 FWDN 스위치를 누른 상태에서 전원 케이블을 D3-G 보드에 연결하십시오.
   - 자세한 내용은 사이드바의 하드웨어 섹션 아래 **"2. 부트 모드"**를 참조하십시오.
 
4. USB Type-C 케이블을 D3-G 보드의 USB Type-C FWDN 포트와 호스트 PC에 연결하십시오.
 
<p align="center">
    <img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20D3-G/Hardware/connect%20to%20d3g%20to%20host%20pc%20using%20c%20type.png">
</p>
<p align="center"><strong>그림 4.1 USB C-Type 케이블을 사용하여 D3-G 보드를 호스트 PC에 연결 </strong></p>
 
<br/><br/>
 
### 4.2.1 VTC 드라이버 설치 방법 (Windows/Ubuntu)
호스트 PC에서 관리자 권한으로 실행하여 Vendor Telechips Certification (VTC) 드라이버([telechips driver](https://drive.google.com/file/d/1muQnY8kuKxDsy3p3FUiQqcG34Zjk-mnR/view?usp=sharing)에서 찾을 수 있음)를 설치하십시오. 위와 같이 FWDN 모드에서 USB를 연결하면 그림 4.2 및 그림 4.3과 같이 Telechips VTC USB 드라이버가 설정됩니다.
 
<p align="center">
    <img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20D3-G/Software/USB%20Connection%20in%20Windows%20Environment.png", width="700">
</p>
<p align="center"><strong>그림 4.2 Windows 환경에서의 USB 연결</strong></p>
 
<p align="center">
    <img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20D3-G/Software/USB%20Connection%20in%20Linux%20System.png", width="700">
</p>
<p align="center"><strong>그림 4.3 Linux 환경에서의 USB 연결</strong></p>  
 
**참고**: VTC 드라이버 V5.0.0.14 이상을 사용하십시오. 버전을 확인하려면 Windows 환경의 장치 관리자에서 확인하십시오.
 
<br/><br/><br/>
 
## 4.3 FWDN 다운로드 준비
---
FWDN을 실행하기 전에 Ubuntu(WSL2) 환경에서 생성된 이미지와 도구를 Windows 환경으로 전송하십시오.
 
 
1. "output_d3g.fwdn.zip" 압축을 풉니다.
    ```
    $ cd ~/topst-sdk
    $ mkdir images
    $ mv ./output_d3g.fwdn.zip ./images
    $ cd images
    $ unzip output_d3g.fwdn.zip
    ```
2. "images" 폴더를 Windows C 드라이브로 복사합니다.
    ```
    $ cd ..
    $ cp -r ./images /mnt/c/
    ```
 
<br/><br/><br/>
 
## 4.4 Windows 환경에서의 FWDN
---
1. Powershell을 실행하고 "C:\images\"로 이동합니다.
```
$ cd C:\images 
```
 
2. **.\fwdn.bat** 명령을 입력하여 펌웨어 다운로드를 시작합니다. “fwdn.bat”는 FWDN V8을 사용하여 펌웨어를 자동으로 다운로드하는 실행 파일입니다.
 
```
.\fwdn.bat
 
C:\images>fwdn.exe --fwdn boot-firmware\fwdn.json
[main:30] FWDN V8 v1.4.6 - 2021.12.13 13:42:37
[FWDN_V8::LoadFWDNRom:403] Start to load FWDN rom
[FWDN_V8::LoadMCERT:592] C:\images\boot-firmware\mcert.bin
[FWDN_V8::LoadHSM:609] C:\images\boot-firmware\hsm.cs.bin
[FWDN_V8::SendFWDNHeader:634] C:\images\boot-firmware\fwdn.rom - Header
[FWDN_V8::SendFWDNBody_V8:537] C:\images\boot-firmware\fwdn.rom - Body
[FWDN_V8::LoadFWDNRom:414] Complete to load FWDN rom
[FWDN_V8::GetFWDNRomVersion:1526] fwdn.rom version : 21.9.29
[FWDN_V8::GetFileAndWriteCommand:748] C:\images\boot-firmware\dram_params.bin
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
 
C:\images>fwdn.exe --storage emmc --low-format
[main:30] FWDN V8 v1.4.6 - 2021.12.13 13:42:37
[FWDN_V8::GetFWDNRomVersion:1526] fwdn.rom version : 21.9.29
[FWDN_V8::LowformatCommand:1352] Start low-format
[FWDN_V8::LowformatCommand:1353] low-format can take a long time
[FWDN_V8::LowformatCommand:1382] Complete low-format
[main:142] Complete FWDN
[FWDNLogger::PrintCurTime:111] 24/04/25-09:57:50
 
C:\images>fwdn.exe -w boot-firmware\boot.single.json
[main:30] FWDN V8 v1.4.6 - 2021.12.13 13:42:37
[FWDN_V8::GetFWDNRomVersion:1526] fwdn.rom version : 21.9.29
[main:117] Start write command
[FWDN_V8::GetFileAndWriteCommand:748] C:\images\boot-firmware\bconf.single.bin
[FWDN_V8::GetFileAndWriteCommand:748] C:\images\boot-firmware\bconf.single.bin
[FWDN_V8::GetFileAndWriteCommand:748] C:\images\boot-firmware\mcert.bin
[FWDN_V8::GetFileAndWriteCommand:748] C:\images\boot-firmware\mcert.bin
[FWDN_V8::GetFileAndWriteCommand:748] C:\images\boot-firmware\dram_params.bin
[FWDN_V8::GetFileAndWriteCommand:748] C:\images\boot-firmware\dram_params.bin
[FWDN_V8::GetFileAndWriteCommand:748] C:\images\boot-firmware\hsm.cs.bin
[FWDN_V8::GetFileAndWriteCommand:748] C:\images\boot-firmware\hsm.cs.bin
[FWDN_V8::GetFileAndWriteCommand:748] C:\images\boot-firmware\scfw.rom
[FWDN_V8::GetFileAndWriteCommand:748] C:\images\boot-firmware\scfw.rom
[FWDN_V8::GetFileAndWriteCommand:748] C:\images\boot-firmware\optee.rom
[FWDN_V8::GetFileAndWriteCommand:748] C:\images\boot-firmware\optee.rom
[FWDN_V8::GetFileAndWriteCommand:748] C:\images\boot-firmware\ca72_bl1.rom
[FWDN_V8::GetFileAndWriteCommand:748] C:\images\boot-firmware\ca72_bl1.rom
[FWDN_V8::GetFileAndWriteCommand:748] C:\images\boot-firmware\ca53_bl1.rom
[FWDN_V8::GetFileAndWriteCommand:748] C:\images\boot-firmware\ca53_bl1.rom
[FWDN_V8::GetFileAndWriteCommand:748] C:\images\boot-firmware\ca72_bl2.rom
[FWDN_V8::GetFileAndWriteCommand:748] C:\images\boot-firmware\ca72_bl2.rom
[FWDN_V8::GetFileAndWriteCommand:748] C:\images\boot-firmware\ca53_bl2.rom
[FWDN_V8::GetFileAndWriteCommand:748] C:\images\boot-firmware\ca53_bl2.rom
[main:125] Complete write command
[main:142] Complete FWDN
[FWDNLogger::PrintCurTime:111] 24/04/25-09:57:53
100% [||||||||||||||||||||||||||||||] 859264/859264
C:\images>fwdn.exe -w "output_d3g.fai" --storage emmc --area user
[main:30] FWDN V8 v1.4.6 - 2021.12.13 13:42:37
[FWDN_V8::GetFWDNRomVersion:1526] fwdn.rom version : 21.9.29
[main:117] Start write command
[FWDN_V8::GetFileAndWriteCommand:748] output_d3g.fai
[main:125] Complete write command
[main:142] Complete FWDN
[FWDNLogger::PrintCurTime:111] 24/04/25-10:05:21
100% [||||||||||||||||||||||||||||||] 7238688960/7238688960
** 로우 포맷 없이 FAI 파일을 쓸 때 데이터가 기록되지 않은 파티션에 가비지 값이 있을 수 있습니다.
```
 
<br/><br/><br/>
 
## 4.5 Linux 환경에서의 FWDN
---
Linux에서 D3-G 이미지를 다운로드하려면 다음 명령을 실행하십시오: "./fwdn.sh".
 
```
$ ./fwdn.sh
```
 
D3-G를 부팅할 준비가 되었습니다. 장치와의 통신을 시작하려면 5장을 참조하십시오.
 
 
<br/><br/><br/><br/>
 
# 5. 호스트 PC와 D3-G 보드 연결
---
이 장에서는 펌웨어 다운로드 및 시리얼 통신을 위해 UART를 통해 호스트 PC를 D3-G 보드에 연결하는 방법을 설명합니다.
 
<br/><br/><br/>
 
## 5.1 UART를 통한 D3-G 보드 연결
---
다음 단계에 따라 UART 연결을 사용하여 펌웨어 다운로드가 성공적으로 완료되었는지 확인하십시오.
 
1. Windows 환경에서 시리얼 포트 드라이버(예: CP210x Windows Driver) 및 PL2303_prolific 드라이버를 설치합니다.
2. Tera Term 또는 PuTTY와 같은 터미널 에뮬레이터를 설치합니다.
3. 호스트 PC와 D3-G 보드의 UART 핀을 연결합니다. USB-to-TTL 케이블을 사용하십시오.
4. 검은색 케이블을 GND 핀에 연결합니다.
5. 흰색 케이블(RXD)을 UART 핀의 TX 핀에 연결하고 녹색 케이블(TXD)을 UART 핀의 RX 핀에 연결합니다.
6. 터미널 에뮬레이터 애플리케이션을 실행합니다.
7. PC에서 장치 관리자를 열고 UART 장치에 할당된 포트 번호를 확인합니다.
8. 터미널 에뮬레이터에서 확인된 포트 번호를 시리얼 라인 필드에 입력합니다. **Speed** (bps)를 115200으로 설정하고 **Flow control**을 **None**으로 설정합니다.
9. 전원 케이블을 연결합니다. 그러면 D3-G 보드가 기본 eMMC 부트 모드로 부팅됩니다.
 
 
 
<p align="center">
    <img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20D3-G/Software/USB%20to%20TTL%20Connection.png", width="700">
</p>
<p align="center"><strong>그림 5.1 호스트 PC와의 UART 연결</strong></p><br/>  
 
 
그림 5.2는 성공적인 로그인을 보여줍니다.
로그인을 위한 사용자 이름과 비밀번호는 모두 **root**로 설정되어 있습니다.
 
<p align="center">
    <img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20D3-G/Software/d3-g%20login%20as%20root.png", width="700">
</p>
<p align="center"><strong>그림 5.2 연결된 화면 (ID 및 비밀번호는 topst)</strong></p><br/>
 
<br/><br/><br/>
 
# 6. Ubuntu OS 파티션 크기 조정
---
우리는 Ubuntu OS도 제공합니다.
이 장을 따라 Ubuntu 이미지를 다운로드하고 보드에 업로드하고 할당된 eMMC 스토리지 용량을 확장할 수 있습니다.
 
<br/><br/><br/>
 
## 6.1 Ubuntu 이미지 다운로드
---
D3-G의 공식 OS는 Ubuntu 22.04를 기반으로 합니다.
여기에서 이미지 파일을 다운로드할 수 있습니다.
 
<img src="https://github.com/topst-development/Documentation/assets/161264431/83d93c78-6437-4f96-a0bf-23f22da1aba1">  
 
**다운로드 :**  
-	[다운로드 링크 여기](https://drive.google.com/file/d/1oc2qwaXUt6-QDME3s5WXKVHzAg4xqVyc/view?usp=drive_link)
<br>
-	자세한 내용은 [github 페이지](https://github.com/topst-development)를 방문하십시오.
 
**릴리스 노트 :**  
 
|버전|   날짜   |
|:-:|:--------:|
|1.0|2024.04.25|  
 
TOPST 팀은 다른 공식 OS 버전도 준비하고 있습니다.
다른 OS 릴리스에 대한 정보는 TOPST 커뮤니티를 참조하십시오.  
 
<br/><br/><br/>
 
## 6.2 D3-G에 펌웨어 업로드
---
“fwdn_ubuntu.batch” 파일을 실행하십시오.
Ubuntu 이미지를 D3-G에 업로드하는 방법은 5장을 참조하십시오.
FWDN을 완료한 후 FWDN 포트에서 USB Type-C 케이블을 제거하고 전원 케이블을 제거하십시오.
 
<br/><br/><br/>
 
## 6.3 eMMC 스토리지 크기 조정 (D3-G만 해당)
---
로그인하고 보드를 부팅한 후 먼저 eMMC 스토리지 크기를 조정하는 것이 좋습니다.
eMMC 스토리지 크기 조정을 위해 아래 단계를 따르십시오.
 
1. 파티션 크기 및 레이아웃을 수정하려면 다음 명령을 사용하십시오.
     ```
     $ parted
     ```
 
2. GUID 파티션 테이블(GPT)을 확장합니다.
    ```
    $ rescue
    $ Fix 
    $ 0 
    $ 100%
    ```
3. p (print) 명령을 사용하여 파티션 유형이 ext4인지 확인합니다.
   ```
   $ p
   ```
4. 파티션 4의 크기를 조정합니다.
    ```
    $ resizepart 4
    $ Yes
    $ 100%
    ```
5. 보드를 재부팅합니다.
6. 파티션 4의 ext4 파일 시스템 크기를 조정합니다.
    ```
    $ resize2fs /dev/mmcblk0p4
    ```
7. 다음 명령을 사용하여 변경된 파티션 크기를 확인합니다.
   ```
   $ df -h
   ```
 
크기 조정 후 사용 가능한 공간이 27GB임을 확인할 수 있습니다.
 
<br/><br/><br/><br/>
 
# 7. 참고 문헌
---
- 자세한 내용은 TOPST에 문의하십시오: topst@topst.ai
 
**참고:** 참조 문서는 계약 조건에 따라 가능한 경우 제공될 수 있습니다. 참조 문서를 사용할 수 없는 경우 개발과 직접 관련된 내용을 안내받을 수 있습니다.
