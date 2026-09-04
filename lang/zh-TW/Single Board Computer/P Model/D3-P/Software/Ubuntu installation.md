# 1. 簡介
本文件說明如何在 TOPST D3（開放平台開發板）的主核心（CA72）上建置 Ubuntu 環境。除了開發板上提供的原生 Ubuntu 映像檔之外，本文件也說明如何建置您專屬的特製 Ubuntu 環境。使用者自行建立的 Ubuntu 檔案系統可透過 **_FWDN_** 工具下載至主核心（CA72）的檔案系統區域。

本文件依下列順序說明：
* Ubuntu 檔案系統建立指南
* FWDN 指南
* 開機後的 Ubuntu GUI 畫面 
  
<br><br>

# 2. Ubuntu 檔案系統建立指南

本章說明如何在主機 PC 上為主核心（CA72）安裝 Ubuntu 檔案系統。

關於使用者的開發環境，請參考「Documentation/TOPST-D3/Software/SDK/LINUX」。

<br><br>

## 2.1. 透過 Git 取得 Ubuntu
Git 提供的 Ubuntu 版本為 Ubuntu 22.04.2 LTS（Jammy Jellyfish），如下所示。

```
$ git clone https://gitlab.com/topst.ai/topst-d3-ubuntu.git
```

<br><br>

# 3. 執行指令碼


請執行 'populate_ubuntu.sh'。
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
您可以依下列方式確認 etx4 檔案。
```
$ ls
populate_ubuntu.sh  src  ubuntu.ext4
```


