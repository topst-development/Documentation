# 1. 소개
본 문서는 TOPST D3(오픈 플랫폼 보드)의 메인 코어(CA72)에서 Ubuntu 환경을 개발하는 방법을 설명합니다. 보드에서 제공되는 기본 Ubuntu 이미지 외에, 본 문서에서는 사용자만의 특화된 Ubuntu 환경을 개발하는 방법을 설명합니다. 사용자가 생성한 ubuntu 파일 시스템은 **_FWDN_** 도구를 사용하여 메인 코어(CA72)의 파일 시스템 영역에 다운로드할 수 있습니다.

본 문서는 다음 순서로 설명합니다:
* Ubuntu 파일 시스템 생성 가이드
* FWDN 가이드
* 부팅된 Ubuntu GUI 화면 
  
<br><br>

# 2. Ubuntu 파일 시스템 생성 가이드

본 장에서는 Host PC에서 메인 코어(CA72)용 Ubuntu 파일 시스템을 설치하는 방법을 설명합니다.

사용자의 개발 환경에 대해서는 “Documentation/TOPST-D3/Software/SDK/LINUX”를 참조하십시오.

<br><br>

## 2.1. Git으로 Ubuntu 가져오기
Git에서 제공하는 Ubuntu 버전은 아래와 같이 Ubuntu 22.04.2 LTS (Jammy Jellyfish)입니다.

```
$ git clone https://gitlab.com/topst.ai/topst-d3-ubuntu.git
```

<br><br>

# 3. 스크립트 실행


'populate_ubuntu.sh'를 실행합니다.
```
$ sudo ./populate_ubuntu.sh 
[!] Prepare workspace
[!] Initial debian bootstraping
I: Retrieving InRelease 
I: Checking Release signature
I: Valid Release signature (key id F6ECB3762474EDA9D21B7022871920D1991BC93C)
I: Retrieving Packages 
I: Validating Packages 
I: Resolving dependencies of required packages...
I: Resolving dependencies of base packages...
I: Checking component main on http://ports.ubuntu.com/ubuntu-ports...
I: Retrieving adduser 3.118ubuntu5
I: Validating adduser 3.118ubuntu5
I: Retrieving apt 2.4.5
I: Validating apt 2.4.5
I: Retrieving apt-utils 2.4.5
I: Validating apt-utils 2.4.5
I: Retrieving base-files 12ubuntu4
I: Validating base-files 12ubuntu4
I: Retrieving base-passwd 3.5.52build1
I: Validating base-passwd 3.5.52build1
I: Retrieving bash 5.1-6ubuntu1
I: Validating bash 5.1-6ubuntu1
I: Retrieving bsdutils 1:2.37.2-4ubuntu3
I: Validating bsdutils 1:2.37.2-4ubuntu3
I: Retrieving ca-certificates 20211016
I: Validating ca-certificates 20211016
I: Retrieving console-setup 1.205ubuntu3
I: Validating console-setup 1.205ubuntu3
I: Retrieving console-setup-linux 1.205ubuntu3
I: Validating console-setup-linux 1.205ubuntu3
I: Retrieving coreutils 8.32-4.1ubuntu1
I: Validating coreutils 8.32-4.1ubuntu1
I: Retrieving cron 3.0pl1-137ubuntu3
I: Validating cron 3.0pl1-137ubuntu3
I: Retrieving dash 0.5.11+git20210903+057cd650a4ed-3build1
I: Validating dash 0.5.11+git20210903+057cd650a4ed-3build1
I: Retrieving dbus 1.12.20-2ubuntu4

                   ㆍ
                   ㆍ
                   ㆍ
```
아래에서 etx4 파일을 확인할 수 있습니다.
```
$ ls
populate_ubuntu.sh  src  ubuntu.ext4
```


