# 1. 簡介
---
本文件提供建置 D3-G SDK 的指引，包含設定主機環境、建置 SDK、使用韌體下載工具，以及下載 Ubuntu。  

本文件包含以下資訊： 
- 設定主機環境  
- 映像檔建置指南  
- 韌體下載指南 
- 將 D3-G 開發板與 PC 連接

<br/><br/><br/><br/>

# 2. 設定主機環境
---
本章說明如何設定主機 PC 環境，並分別提供 Windows 與 Ubuntu 的指引。
</br><br/><br/>

## 2.1 Windows 環境 
---
本文件說明如何設定 Windows Subsystem for Linux（WSL），以便在 Windows PC 上使用 Linux。
D3-G Linux SDK 以 Yocto Project 為基礎，因此 D3-G SDK 的 Linux 版本會依循 Yocto Project。
您可以安裝其他版本的 Linux，但本文件說明的是以 Ubuntu 22.04 為基礎的 D3-G Linux SDK。
若您的主機作業系統為 Ubuntu，請直接前往第 2.2 章。

</br><br/>

### 2.1.1 安裝 WSL2 Ubuntu
1. 以「**以系統管理員權限執行**」方式執行 Windows PowerShell。
2. 啟用 WSL2 系統。
    ```
    dism.exe /online /enable-feature /featurename:Microsoft-Windows-Subsystem-Linux /all /norestart
    ```
3. 啟用虛擬機器功能。
    ```
    dism.exe /online /enable-feature /featurename:VirtualMachinePlatform /all /norestart
    ```
4. 將 WSL 2 設為預設版本。
    ```
    wsl --set-default-version 2
    ```
5. 在 Microsoft Store 中搜尋 Ubuntu 22.04.3 LTS 並下載。

    * 若您需要下載 Linux 核心更新套件，請於[此處](https://learn.microsoft.com/ko-kr/windows/wsl/install-manual)下載最新的套件。

6. 在 Ubuntu 安裝過程中可自行選擇任意使用者名稱。
</br><br/>

### 2.1.2 透過 WSL2 存取 Ubuntu
開啟 Windows 命令提示字元並輸入以下命令以存取 Ubuntu。
存取 Ubuntu 時，預設會從 /mnt/c/Users/[username] 目錄開始。
```
wsl  // access ubuntu 
ls   // check contents in your directory
```
請參考圖 2.1 確認結果（結果可能因系統而異）。
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20D3-G/Software/1.1%20wsl%20linux.png" width="500"></p>
<p align="center"><strong>圖 2.1 WSL2 螢幕擷圖 </strong></p>

<br/><br/>

### 2.1.3 設定語言環境

在 WSL 上執行 Ubuntu 後，您應設定語言環境以確保正確的語言與地區設定。建議使用 en_US.UTF-8。請執行以下命令以使用 en_US.UTF-8。 

```
sudo locale-gen en_US.UTF-8 && sudo update-locale LANG=en_US.UTF-8 
```

設定語言環境後，您可以使用以下命令檢查語言環境類型。 

```
echo 'LANG=en_US.UTF-8' | sudo tee -a /etc/default/locale && \  

echo 'LC_ALL=en_US.UTF-8' | sudo tee -a /etc/default/locale 
```
<br/><br/>

### 2.1.4 安裝 SSH 與 Samba

進入 Ubuntu 後，您可以使用 SSH 與 Samba 等額外工具，讓開發環境更加便利。SSH 與 Samba 可讓您在遠端電腦上執行命令，並將檔案複製到其他電腦。
 - 以下步驟需要主機 PC 已連接網路。請使用以下命令檢查您的網路狀態。
  ```
  $ sudo apt-get update
  $ sudo apt-get install -y net-tools
  $ ifconfig 
  ```

若已安裝 SSH 與 Samba，或您不打算使用它們，可以略過本章。

請使用以下命令安裝 net-tools、SSH 與 Samba。

```
$ sudo apt-get update 
$ sudo apt install -y net-tools openssh-server samba
```
安裝 SSH 與 Samba 後，請依您的環境需求設定各個程式。
</br><br/>

### 2.1.5 安裝工具程式

請使用以下命令一次安裝所有必要的工具程式。若要使用 Yocto Project，主機 PC（個人電腦或開發伺服器）上必須安裝以下工具程式。


```
$ sudo apt-get install -y gawk wget git diffstat unzip texinfo gcc-multilib build-essential chrpath

$ sudo apt-get install -y socat cpio python3 python3-pip python3-pexpect xz-utils debianutils

$ sudo apt-get install -y iputils-ping python3-git python3-jinja2 libegl1-mesa-dev libsdl1.2-dev pylint

$ sudo apt-get install -y xterm zstd ncftp curl git-lfs vim zip lz4
```

<br/><br/>

### 2.1.6 安裝 Repo

若已安裝 Repo，您無須重新安裝即可直接使用。  
安裝 Repo 前，請確認已安裝 Python 3.6 或更新版本。

請使用以下命令安裝 Repo。
```
$ sudo apt-get install repo
```

若出現錯誤訊息 '/usr/bin/env 'python' no such file or directory'，請使用以下命令將 'python' 連結至 'python3'。

```
$ sudo ln -sf /usr/bin/python3 /usr/bin/python
```
若發生 Repo 錯誤，請使用以下命令下載最新版本並放入 /usr/bin/ 資料夾。

```
$ mkdir -p ~/bin

$ curl http://commondatastorage.googleapis.com/git-repo-downloads/repo > ~/bin/repo

$ chmod a+x ~/bin/repo

$ sudo mv ~/bin/repo /usr/bin/repo
```
請前往**第 3 章：映像檔建置指南**。

<br/><br/><br/>

## 2.2 Linux 環境
---
本章說明以 Ubuntu 作為主機作業系統的設定流程。
</br><br/>

### 2.2.1 設定環境
以下章節（2.2.2 至 2.2.5）必須在 Ubuntu 終端機中執行。若要開啟終端機，請使用快速鍵：[Ctrl + Alt + T]。
<br/><br/>

### 2.2.2 設定語言環境

在 WSL 上執行 Ubuntu 後，您應設定語言環境以確保正確的語言與地區設定。建議使用 en_US.UTF-8。請執行以下命令以使用 en_US.UTF-8。 

```
sudo locale-gen en_US.UTF-8 && sudo update-locale LANG=en_US.UTF-8 
```

設定語言環境後，您可以使用以下命令檢查語言環境類型。 

```
echo 'LANG=en_US.UTF-8' | sudo tee -a /etc/default/locale && \  

echo 'LC_ALL=en_US.UTF-8' | sudo tee -a /etc/default/locale 
```
<br/><br/>

### 2.2.3 安裝 SSH 與 Samba

進入 Ubuntu 後，您可以使用 SSH 與 Samba 等額外工具，讓開發環境更加便利。SSH 與 Samba 可讓您在遠端電腦上執行命令，並將檔案複製到其他電腦。
 - 以下步驟需要主機 PC 已連接網路。請使用以下命令檢查您的網路狀態
  ```
  $ sudo apt-get update
  $ sudo apt-get install -y net-tools
  $ ifconfig 
  ```

若已安裝 SSH 與 Samba，或您不打算使用它們，可以略過本章。

請使用以下命令安裝 SSH 與 Samba。

```
$ sudo apt-get update 
$ sudo apt install -y openssh-server samba
```
安裝 SSH 與 Samba 後，請依您的環境需求設定各個程式。

<br/><br/>

### 2.2.4 安裝工具程式

請使用以下命令一次安裝所有必要的工具程式。若要使用 Yocto Project，主機 PC（個人電腦或開發伺服器）上**必須**安裝以下工具程式。
****


```
$ sudo apt-get install -y gawk wget git diffstat unzip texinfo gcc-multilib build-essential chrpath

$ sudo apt-get install -y socat cpio python3 python3-pip python3-pexpect xz-utils debianutils

$ sudo apt-get install -y iputils-ping python3-git python3-jinja2 libegl1-mesa-dev libsdl1.2-dev pylint

$ sudo apt-get install -y xterm zstd ncftp curl git-lfs vim zip lz4
```

<br/><br/>

### 2.2.5 安裝 Repo

您可以透過 Android Repo 下載 D3-G SDK。  
若要安裝 Repo，請參考以下網站：https://source.android.com/source/downloading.html。  
若已安裝 Repo，您無須重新安裝即可直接使用。  
安裝 Repo 前，請確認已安裝 Python 3.6 或更新版本。

請使用以下命令安裝 Repo。
```
$ sudo apt-get install repo
```

若出現錯誤訊息 '/usr/bin/env 'python' no such file or directory'，請使用以下命令將 'python' 連結至 'python3'。

```
$ sudo ln -sf /usr/bin/python3 /usr/bin/python
```
若發生 Repo 錯誤，請使用以下命令下載最新版本並放入 /usr/bin/ 資料夾。

```
$ mkdir -p ~/bin

$ curl http://commondatastorage.googleapis.com/git-repo-downloads/repo > ~/bin/repo

$ chmod a+x ~/bin/repo

$ sudo mv ~/bin/repo /usr/bin/repo
```

<br/><br/>

### 2.2.6 Telechips USB 裝置的 Udev 規則
執行以下命令後，在 Linux 中下載 FWDN 時就不再需要使用 'sudo' 命令。
```
$ echo "SUBSYSTEM==\"usb\", ATTR{idVendor}==\"140e\", MODE=\"0666\", OWNER=\"${USER}\"" | sudo tee /etc/udev/rules.d/99-topst.rules
$ sudo udevadm control --reload-rules && sudo udevadm trigger
```
請前往**第 3 章：映像檔建置指南**。

<br/><br/><br/><br/>

# 3. 映像檔建置指南
---
本章以主機 PC 上安裝的 Ubuntu 作業系統為基礎提供說明（無論是 WSL 或本機安裝的 Ubuntu）。要上傳至 D3-G 的映像檔是使用 Yocto Project 建置，因此建置流程必須在 Ubuntu 環境中執行。
</br></br>

## 3.1 SDK 建置準備
---
D3-G Linux SDK 以 Yocto Project 4.0 Kirkstone 為基礎。因此，若要使用 D3-G Linux SDK，您必須在主機 PC 上設定 Yocto Project 環境。若要下載 SDK、source-mirror 與工具，您需要安裝必要的工具程式。為了順利建置映像檔，您的 PC 必須具備**至少 60 GB 的可用儲存空間**與**至少 16 GB 的 RAM**。

</br><br/>  

## 3.2 Yocto Project  
---
Yocto Project 是一個專注於嵌入式 Linux 開發的開放原始碼專案。  
它結合了 Open Embedded 專案（即 Poky）與 ***bitbake*** 作為建置系統，用以製作 Linux 映像檔。  
使用 Yocto Project，您可以同時建置 bootloader、kernel 與 rootfs。  

<br/><br/>

## 3.3 Yocto Project 的工作流程
---
圖 3.1 顯示 Yocto Project 的工作流程。您可以依據 metadata 從上游下載原始碼並進行建置。建置完成後，會產出套件、映像檔與 SDK 作為結果。

<p align="center">
    <img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20D3-G/Software/2.1%20yocto%20project%20task%20process.png", width="700">
</p>
<p align="center"><strong>圖 3.1 Yocto Project 工作流程</strong></p>

<br/><br/>

## 3.4 D3-G SDK 的組成
---
以下是我們所設定的 Yocto Project 元件。
表 3.1 顯示 D3-G SDK 的組成。



**表 3.1 D3-G SDK 的組成**
<table border="1" cellspacing="0" cellpadding="5">
  <colgroup>
    <col style="width: 10%">
    <col style="width: 10%">
    <col style="width: 10%">
    <col style="width: 56%">
  </colgroup>
  <thead>
    <tr>
      <th colspan="3"style="text-align: center; vertical-align: middle;"><strong>項目</strong></th>
      <th style="text-align: center; vertical-align: middle;" ><strong>說明</strong></th>
    </tr>
  </thead>
  <tbody>
  <tr>
      <td colspan="3"style="text-align: center; vertical-align: middle;">easy-setup.sh</td>
      <td>自動下載並建置 SDK 的 Python 指令碼</td>
    </tr>
    <tr>
      <td colspan="3"style="text-align: center; vertical-align: middle;">stitch-fai-ai.sh</td>
      <td>用於建立 AI-G fai 映像檔的指令碼（minimal + 範例應用程式）</td>
    </tr>
    <tr>
      <td colspan="3"style="text-align: center; vertical-align: middle;">stitch-fai-d3.sh</td>
      <td>用於建立 D3-G fai 映像檔的指令碼（minimal + 範例應用程式）</td>
    </tr>
    <tr>
      <td colspan="3"style="text-align: center; vertical-align: middle;">mktcimg</td>
      <td rowspan="2">與建置流程及 <strong>FWDN</strong> 相關的工具</td>
    </tr>
    <tr>
      <td colspan="3"style="text-align: center; vertical-align: middle;">tools</td>
    </tr>
    <tr>
      <td rowspan="8"style="text-align: center; vertical-align: middle;">poky</td>
      <td colspan="2"style="text-align: center; vertical-align: middle;">poky</td>
      <td>Yocto Project 4.0 Kirkstone 建置系統</td>
    </tr>
    <tr>
      <td colspan="2"style="text-align: center; vertical-align: middle;">meta-openembedded</td>
      <td>支援 OE-Core 的層</td>
    </tr>
    <tr>
      <td colspan="2"style="text-align: center; vertical-align: middle;">meta-arm</td>
      <td>支援 ARM 工具鏈的層（Layer）</td>
    </tr>
    <tr>
      <td colspan="2"style="text-align: center; vertical-align: middle;">meta-topst-bsp</td>
      <td>支援 TOPST BSP 的層</td>
    </tr>
    <tr>
      <td colspan="2"style="text-align: center; vertical-align: middle;">meta-gplv2</td>
      <td>包含避開 GPLv3 授權之套件的層</td>
    </tr>
    <tr>
      <td colspan="2"style="text-align: center; vertical-align: middle;">meta-topst</td>
      <td>TOPST recipe</td>
    </tr>
  </tbody>
</table>
<br/><br/><br/>


## 3.5 建置前準備
---
以下章節說明如何設定 Yocto Project 以建置 D3-G 映像檔。

<br/><br/>

### 3.5.1 在 .gitconfig 中設定使用者電子郵件與使用者名稱
若要從官方 TOPST git 下載 D3-G SDK，請設定您的電子郵件與名稱。
1. 請輸入以下指令。
```
vi ~/.gitconfig
```
2. 請輸入以下資訊
```
[user]
    email = User email
    name = User name
```

<br/><br/>

### 3.5.2 從 Git 取得 D3-G

1. 建立名為 **topst-sdk** 的新目錄，並將目前目錄切換至 **topst-sdk**。

```
$ mkdir topst-sdk
$ cd topst-sdk
```

2. 請執行以下指令以初始化儲存庫。

```
$ repo init -u https://github.com/topst-development/manifests.git -b release/1.3.0 -m linux_yp4.0_topst.xml
```

執行該指令後，會顯示以下輸出。

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

3. 請執行以下指令以同步儲存庫。

```
$ repo sync
```

執行該指令後，會顯示以下輸出。

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

## 3.6 執行 topst-build.sh 
---
執行 ./easy-setup.sh 腳本後，您會看到以下畫面。 

**注意：若重新執行 ./easy-setup.sh，請留意，一旦選擇 yes，已建置的原始碼將會被刪除。**
```
./easy-setup.sh
```
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20AI-G/Software/Linux%20SDK/license1.png"></p>
<p align="center"><strong>圖 3.2 使用者授權合約</strong></p>

請向下捲動至畫面底部並閱讀此聲明。閱讀完畢後，請按右方向鍵，然後按 [Enter]。
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20AI-G/Software/Linux%20SDK/license2.png"></p>
<p align="center"><strong>圖 3.3 前往 'Proceed to confirm'</strong></p>


接著會看到以下畫面。 
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20AI-G/Software/Linux%20SDK/license3.png" ></p>
<p align="center"><strong>圖 3.4 接受畫面 </strong></p>


建置的映像檔會產生於以下路徑：

- {TOPST_PATH}/build/d3-g-topst-main/tmp/deploy/images/d3-g-topst-main

topst-build.sh 是一個 shell 腳本，用於設定建置 D3-G 與 AI-G 映像檔所需的核心環境。請執行以下命令，並選擇選項 2，以準備在 D3-G 上安裝主要作業系統的建置環境。



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

請執行以下命令以開始建置主要作業系統。
```
$ bitbake telechips-topst-image
```

<br/><br/><br/>

## 3.7 製作韌體下載工具（FWDN）映像檔 
---
此選項會將各個二進位檔合併為單一映像檔，作為 D3-G 平台映像檔。

包含 **'output_d3g.fai' 建置映像檔**與 **FWDN 工具**的 **output_d3g.fwdn.zip** 檔案會建立於以下路徑：

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

若您看到以下記錄，表示已建立 "output_d3g.fwdn.zip" 檔案。 
```
$ ls
build  easy-setup.sh  mktcimg  output_d3g.fwdn.zip  poky  stitch-fai-ai.sh  stitch-fai-d3.sh  tools
```

</br></br><br/><br/>

# 4. 韌體下載
---
本章說明如何使用 ***FWDN*** 將韌體下載至 D3-G，並登入 Linux 主控台。  
***FWDN V8*** 是一款 PC 工具，可在 Windows 10(11) 64 位元與 Linux 環境中下載韌體。本章說明在 Windows 與 Linux 環境中下載的情況。

<br/><br/><br/>

## 4.1 韌體下載流程
---
***FWDN*** 的下載流程如下：

1. 將開機模式開關設為 USB 開機模式。
2. 開啟 Windows 命令提示字元或 Linux 主控台。
3. 將 ***FWDN V8*** 連接至開發板。
4. 下載 fai 檔案。

<br/><br/><br/>

## 4.2 以 USB 開機模式連接 D3-G 開發板與主機 PC
---
韌體下載工具（FWDN）會透過與主機 PC 的 USB 通訊，將 ROM 映像檔寫入 D3-G。 

D3-G 具有一個開機模式按鈕，並支援兩種開機模式。本指南著重於 FWDN 模式。

- USB 開機模式（FWDN 模式）：用於在主機 PC 上使用 FWDN 工具寫入 ROM 映像檔 

- eMMC 開機模式：用於使用儲存在 eMMC 裝置中的 ROM 映像檔啟動 D3-G 

**註**：USB Type-C FWDN 連接埠用於韌體下載工具（FWDN）。 



若要使用 FWDN，請依下列方式將 D3-G 開發板連接至主機 PC： 

1. 請確認主機 PC 已安裝 VTC 驅動程式。若尚未安裝 VTC 驅動程式，請依第 4.2.1 章所述進行安裝。  

2. 請準備一條 USB Type-C 傳輸線。 

3. 若要進入 USB 開機模式，請在按住 FWDN 開關的同時，將電源線連接至 D3-G 開發板。
   - 詳細資訊請參閱側邊欄 Hardware 區段下的 **"2. Boot Mode"**。

4. 請將 USB Type-C 傳輸線連接至 D3-G 開發板上的 USB Type-C FWDN 連接埠與主機 PC。 

<p align="center">
    <img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20D3-G/Hardware/connect%20to%20d3g%20to%20host%20pc%20using%20c%20type.png">
</p>
<p align="center"><strong>圖 4.1 使用 USB C-Type 傳輸線連接 D3-G 開發板與主機 PC </strong></p>

<br/><br/>

### 4.2.1 如何安裝 VTC 驅動程式（Windows/Ubuntu）
請以系統管理員身分在主機 PC 上執行並安裝 Vendor Telechips Certification（VTC）驅動程式（可於 [telechips driver](https://drive.google.com/file/d/1muQnY8kuKxDsy3p3FUiQqcG34Zjk-mnR/view?usp=sharing) 取得）。當您依上述方式以 FWDN 模式連接 USB 時，Telechips VTC USB 驅動程式的設定會如圖 4.2 與圖 4.3 所示。

<p align="center">
    <img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20D3-G/Software/USB%20Connection%20in%20Windows%20Environment.png", width="700">
</p>
<p align="center"><strong>圖 4.2 Windows 環境中的 USB 連接</strong></p>

<p align="center">
    <img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20D3-G/Software/USB%20Connection%20in%20Linux%20System.png", width="700">
</p>
<p align="center"><strong>圖 4.3 Linux 環境中的 USB 連接</strong></p>  

**註**：請使用 VTC Driver V5.0.0.14 或更新版本。若要查看版本，請在 Windows 環境中確認裝置管理員。  

<br/><br/><br/>

## 4.3 準備下載 FWDN
---
執行 FWDN 前，請將在 Ubuntu（WSL2）環境中建立的映像檔與工具傳輸至 Windows 環境。


1. 請解壓縮 "output_d3g.fwdn.zip"。   
    ```
    $ cd ~/topst-sdk
    $ mkdir images
    $ mv ./output_d3g.fwdn.zip ./images
    $ cd images
    $ unzip output_d3g.fwdn.zip
    ```
2. 請將 "images" 資料夾複製到 Windows C 磁碟機。  
    ```
    $ cd ..
    $ cp -r ./images /mnt/c/
    ```

<br/><br/><br/>

## 4.4 Windows 環境中的 FWDN
---
1. 請執行 Powershell 並前往 "C:\images\"。
```
$ cd C:\images 
```

2. 請輸入 **.\fwdn.bat** 命令以開始下載韌體。“fwdn.bat” 是一個可執行檔，會使用 FWDN V8 自動下載韌體。 

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
** When writing FAI files without low-format, there may be garbage values in partition where data is not written.
```

<br/><br/><br/>

## 4.5  Linux 環境中的 FWDN
---
若要在 Linux 中下載 D3-G 映像檔，請執行以下命令："./fwdn.sh"。

```
$ ./fwdn.sh
```

您已準備好啟動 D3-G。請參考第 5 章以開始與裝置進行通訊。


<br/><br/><br/><br/>

# 5. 將 D3-G 開發板與主機 PC 連接
---
本章說明如何透過 UART 將主機 PC 連接至 D3-G 開發板，以進行韌體下載與序列通訊。

<br/><br/><br/>

## 5.1 使用 UART 連接 D3-G 開發板 
---
請依照以下步驟，並透過 UART 連線確認韌體下載已成功完成。 

1. 請在 Windows 環境中安裝序列埠驅動程式（例如 CP210x Windows Driver）與 PL2303_prolific 驅動程式。 
2. 請安裝終端機模擬器，例如 Tera Term 或 PuTTY。 
3. 請將主機 PC 與 D3-G 開發板上的 UART 腳位連接。請使用 USB-to-TTL 傳輸線。 
4. 請將黑色線接到 GND 腳位。 
5. 請將白色線（RXD）連接至 UART 腳位中的 TX 腳位，並將綠色線（TXD）連接至 UART 腳位中的 RX 腳位。
6. 請執行終端機模擬器應用程式。
7. 請在您的 PC 上開啟裝置管理員，並查看指派給 UART 裝置的連接埠編號。
8. 請在終端機模擬器中，將確認過的連接埠編號輸入 Serial line 欄位。將 **Speed**（bps）設為 115200，並將 **Flow control** 設為 **None.**
9. 請連接電源線。接著，D3-G 開發板會以預設的 eMMC 開機模式啟動。


 
<p align="center">
    <img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20D3-G/Software/USB%20to%20TTL%20Connection.png", width="700">
</p>
<p align="center"><strong>圖 5.1 與主機 PC 的 UART 連接</strong></p><br/>  


圖 5.2 顯示登入成功的畫面。  
登入的使用者名稱與密碼皆設定為 **root**。

<p align="center">
    <img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20D3-G/Software/d3-g%20login%20as%20root.png", width="700">
</p>
<p align="center"><strong>圖 5.2 連線畫面（ID 與密碼皆為 topst）</strong></p><br/>

<br/><br/><br/>

# 6. Ubuntu OS 分割區容量調整
---
我們同時也提供 Ubuntu 作業系統。
依照本章的說明，您可以下載 Ubuntu 映像檔、將其上傳至開發板，並擴充已配置的 eMMC 儲存容量。

<br/><br/><br/>

## 6.1 下載 Ubuntu 映像檔
---
D3-G 的官方版本以 Ubuntu 22.04 為基礎。  
您可以在此處下載映像檔。  

<img src="https://github.com/topst-development/Documentation/assets/161264431/83d93c78-6437-4f96-a0bf-23f22da1aba1">  

**下載：**  
-	[下載連結在此](https://drive.google.com/file/d/1oc2qwaXUt6-QDME3s5WXKVHzAg4xqVyc/view?usp=drive_link)
<br>
-	如需更多資訊，請造訪我們的 [github 頁面](https://github.com/topst-development)。

**版本資訊：**  

|版本|   日期   |
|:-:|:--------:|
|1.0|2024.04.25|  

TOPST 團隊也正在準備其他官方作業系統版本。  
如需其他作業系統版本的發布資訊，請參考 TOPST 社群。  

<br/><br/><br/>

## 6.2 將韌體上傳至 D3-G
---
請執行 “fwdn_ubuntu.batch” 檔案。 
如需將 Ubuntu 映像檔上傳至 D3-G 的方式，請參考第 5 章。
完成 FWDN 後，請將 USB Type-C 傳輸線從 FWDN 連接埠拔除，並拔掉電源線。 

<br/><br/><br/>

## 6.3 調整 eMMC 儲存容量（僅限 D3-G）
---
登入並啟動開發板後，建議先調整 eMMC 儲存容量。
請依照以下步驟調整 eMMC 儲存容量。

1. 若要修改分割區大小與配置，請使用以下命令。
     ```
     $ parted
     ```

2. 請擴充 GUID 分割表（GPT）。 
    ```
    $ rescue
    $ Fix 
    $ 0 
    $ 100%
    ```
3. 請使用 p（print）命令確認分割區類型為 ext4。 
   ```
   $ p
   ```
4. 請調整分割區 4 的大小。
    ```
    $ resizepart 4
    $ Yes
    $ 100%
    ```
5. 請重新啟動開發板。
6. 請調整分割區 4 上的 ext4 檔案系統大小。
    ```
    $ resize2fs /dev/mmcblk0p4
    ```
7. 請使用以下命令確認變更後的分割區大小。
   ```
   $ df -h
   ```

您可以確認調整後的可用空間為 27GB。

<br/><br/><br/><br/>

# 7. 參考資料
---
- 如需更多詳細資訊，請聯絡 TOPST：topst@topst.ai

**註：**參考文件可依合約條款於可提供時提供。若參考
文件無法提供，則可就與您的開發直接相關的內容提供指引。
