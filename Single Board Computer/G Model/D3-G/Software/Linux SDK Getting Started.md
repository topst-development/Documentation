# 1. Introduction
---
This document provides guidelines for building the D3-G SDK, including setting up the host environment, building the SDK, using the firmware downloader, and downloading Ubuntu.  

This document includes information on the following: 
- Setting Host Environment  
- Image Build Guide  
- Firmware Download Guide 
- Connecting the D3-G board with a PC

<br/><br/><br/><br/>

# 2. Setting Host Environment
---
This chapter provides instructions on how to set up the host PC environment, with separate guides for Windows and Ubuntu.
</br><br/><br/>

## 2.1 Windows Environment 
---
This document describes how to set up Windows Subsystem for Linux (WSL) to use Linux on a Windows PC.
The D3-G Linux SDK is based on the Yocto Project, so Linux version of D3-G SDK follows the Yocto project.
You can install another version of Linux, but this document describes, the D3-G Linux SDK based on Ubuntu 22.04.
If your host OS is Ubuntu, proceed to Chapter 2.2.

</br><br/>

### 2.1.1 Install WSL2 Ubuntu
1. Execute Windows PowerShell with "**Run with administrator privileges**".
2. Enable the WSL2 System.
    ```
    dism.exe /online /enable-feature /featurename:Microsoft-Windows-Subsystem-Linux /all /norestart
    ```
3. Enable the Virtual Machine feature.
    ```
    dism.exe /online /enable-feature /featurename:VirtualMachinePlatform /all /norestart
    ```
4. Set WSL 2 to the default version.
    ```
    wsl --set-default-version 2
    ```
5. Search for Ubuntu 22.04.3 LTS in Microsoft Store and download it.

    * If you need to download the Linux kernel update package, download the latest package [here](https://learn.microsoft.com/ko-kr/windows/wsl/install-manual).

6. Choose any username during the Ubuntu installation.
</br><br/>

### 2.1.2 Accessing Ubuntu via WSL2
Open the Windows Command Prompt and enter the following command to access Ubuntu.
When you access Ubuntu, it starts in the /mnt/c/Users/[username] directory by default.
```
wsl  // access ubuntu 
ls   // check contents in your directory
```
Refer to Figure 2.1 to check the result (results may vary depending on your system).
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20D3-G/Software/1.1%20wsl%20linux.png" width="500"></p>
<p align="center"><strong>Figure 2.1 WSL2 Screenshot </strong></p>

<br/><br/>

### 2.1.3 Set Locale

After executing Ubuntu on WSL, you should set the locale to ensure proper language and regional settings. It is recommended to use en_US.UTF-8. Execute the following commands to use en_US.UTF-8. 

```
sudo locale-gen en_US.UTF-8 && sudo update-locale LANG=en_US.UTF-8 
```

After setting locale, you can check the locale type by using the following commands. 

```
echo 'LANG=en_US.UTF-8' | sudo tee -a /etc/default/locale && \  

echo 'LC_ALL=en_US.UTF-8' | sudo tee -a /etc/default/locale 
```
<br/><br/>

### 2.1.4 Install SSH and Samba

After entering Ubuntu, you can use additional utilities such as SSH and Samba for more convenient development environment. SSH and Samba allows you to execute commands on remote computers and copy files to other computers.
 - The following steps require the Host PC to be connected to the network. Check your network condition by using the following commands.
  ```
  $ sudo apt-get update
  $ sudo apt-get install -y net-tools
  $ ifconfig 
  ```

If SSH and Samba are already installed or you will not use them, you can skip this chapter.

Use the following command to install net-tools, SSH, Samba.

```
$ sudo apt-get update 
$ sudo apt install -y net-tools openssh-server samba
```
After installing SSH and Samba, configure each program as needed for your environment.
</br><br/>

### 2.1.5 Install Utilities

Use the following commands to install all required utilities at once. To use Yocto Project, the following utilities must be installed on the Host PC  (individual computer or development server).


```
$ sudo apt-get install -y gawk wget git diffstat unzip texinfo gcc-multilib build-essential chrpath

$ sudo apt-get install -y socat cpio python3 python3-pip python3-pexpect xz-utils debianutils

$ sudo apt-get install -y iputils-ping python3-git python3-jinja2 libegl1-mesa libsdl1.2-dev pylint

$ sudo apt-get install -y xterm zstd ncftp curl git-lfs vim zip
```

<br/><br/>

### 2.1.6 Install Repo

You can download the D3-G SDK through Android Repo.  
To install Repo, refer to the following website: https://source.android.com/source/downloading.html.  
If Repo is already installed, you can use it without re-installing.  
Before installing Repo, ensure that Python version 3.6 or higher is installed.

Use the following command to install Repo.
```
$ sudo apt-get install repo
```

If you see the error message '/usr/bin/env 'python' no such file or directory', use the following command to link 'python' to 'python3'.

```
$ sudo ln -sf /usr/bin/python3 /usr/bin/python
```
If there is a Repo error, use the following commands to download the latest version and place it in the /usr/bin/ folder.

```
$ mkdir -p ~/bin

$ curl http://commondatastorage.googleapis.com/git-repo-downloads/repo > ~/bin/repo

$ chmod a+x ~/bin/repo

$ sudo mv ~/bin/repo /usr/bin/repo
```
Proceed to **Chapter 3: Image Build Guide**.

<br/><br/><br/>

## 2.2 Linux Environment
---
This chapter explains the setup process for Ubuntu as the host OS.
</br><br/>

### 2.2.1 Setting Environment
The following chapters (2.2.2 to 2.2.5) must be executed in the Ubuntu terminal. To open the terminal, use the shortcut: [Ctrl + Alt + T].
<br/><br/>

### 2.2.2 Set Locale

After executing Ubuntu on WSL, you should set the locale to ensure proper language and regional settings. It is recommended to use en_US.UTF-8. Execute the following commands to use en_US.UTF-8. 

```
sudo locale-gen en_US.UTF-8 && sudo update-locale LANG=en_US.UTF-8 
```

After setting locale, you can check the locale type by using the following commands. 

```
echo 'LANG=en_US.UTF-8' | sudo tee -a /etc/default/locale && \  

echo 'LC_ALL=en_US.UTF-8' | sudo tee -a /etc/default/locale 
```
<br/><br/>

### 2.2.3 Install SSH and Samba

After entering Ubuntu, you can use additional utilities such as SSH and Samba for more convenient development environment. SSH and Samba allows you to execute commands on remote computers and copy files to other computers.
 - The following steps require the Host PC to be connected to the network. Check your network condition by using the following commands
  ```
  $ sudo apt-get update
  $ sudo apt-get install -y net-tools
  $ ifconfig 
  ```

If SSH and Samba are already installed or you will not use them, you can skip this chapter.

Use the following command to install SSH, Samba.

```
$ sudo apt-get update 
$ sudo apt install -y openssh-server samba
```
After installing SSH and Samba, configure each program as needed for your environment.

<br/><br/>

### 2.2.4 Install Utilities

Use the following commands to install all required utilities at once. To use Yocto Project, the following utilities **must** be installed on the Host PC (individual computer or development server).
****


```
$ sudo apt-get install -y gawk wget git diffstat unzip texinfo gcc-multilib build-essential chrpath

$ sudo apt-get install -y socat cpio python3 python3-pip python3-pexpect xz-utils debianutils

$ sudo apt-get install -y iputils-ping python3-git python3-jinja2 libegl1-mesa libsdl1.2-dev pylint

$ sudo apt-get install -y xterm zstd ncftp curl git-lfs vim zip
```

<br/><br/>

### 2.2.5 Install Repo

You can download the D3-G SDK through Android Repo.  
To install Repo, refer to the following website: https://source.android.com/source/downloading.html.  
If Repo is already installed, you can use it without re-installing.  
Before installing Repo, ensure that Python version 3.6 or higher is installed.

Use the following command to install Repo.
```
$ sudo apt-get install repo
```

If you see the error message '/usr/bin/env 'python' no such file or directory', use the following command to link 'python' to 'python3'.

```
$ sudo ln -sf /usr/bin/python3 /usr/bin/python
```
If there is a Repo error, use the following command to download the latest version and place it in the /usr/bin/ folder.

```
$ mkdir -p ~/bin

$ curl http://commondatastorage.googleapis.com/git-repo-downloads/repo > ~/bin/repo

$ chmod a+x ~/bin/repo

$ sudo mv ~/bin/repo /usr/bin/repo
```

<br/><br/>

### 2.2.6 Udev Rules for Telechips USB Device
After you execute the following commands, you no longer need to use 'sudo' command when downloading FWDN in Linux.
```
$ echo "SUBSYSTEM==\"usb\", ATTR{idVendor}==\"140e\", MODE=\"0666\", OWNER=\"${USER}\"" | sudo tee /etc/udev/rules.d/99-topst.rules
$ sudo udevadm control --reload-rules && sudo udevadm trigger
```
Proceed to **Chapter 3: Image Build Guide**.

<br/><br/><br/><br/>

# 3. Image Build Guide
---
This chapter provides guidance based on the Ubuntu OS installed on the host PC (regardless of whether it is WSL or a local Ubuntu installation). The image to be uploaded to the D3-G is built using the Yocto Project, so the build process must be performed in the Ubuntu environment.
</br></br>

## 3.1 SDK Build Preparation
---
The D3-G Linux SDK is based on Yocto Project 3.1 Dunfell. Therefore, you must configure the Yocto Project environment on the host PC to use the D3-G Linux SDK. To download SDK, source-mirror, and tools, you need to install the required utilities. To build the image smoothly, your PC must have **at least 60 GB of available storage** and **a minimum of 16 GB of RAM**.

</br><br/>  

## 3.2 Yocto Project  
---
The Yocto Project is an open source project that focuses on embedded Linux development.  
It uses a combination of Open Embedded project, which is Poky, and ***bitbake*** as the build system to make Linux images.  
By using Yocto Project, you can simultaneously build the bootloader, kernel, and rootfs.  

<br/><br/>

## 3.3 Task Process of Yocto Project
---
Figure 3.1 shows the task process of Yocto Project. You can download source from upstream based on metadata and build it. After the build is completed, package, image, and SDK are provided as results.

<p align="center">
    <img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20D3-G/Software/2.1%20yocto%20project%20task%20process.png", width="700">
</p>
<p align="center"><strong>Figure 3.1 Yocto Project Task Process</strong></p>

<br/><br/>

## 3.4 Composition of D3-G SDK
---
The following are the components of the Yocto Project we have configured.
Table 3.1 shows composition of the D3-G SDK.



**Table 3.1 Composition of D3-G SDK**
<table border="1" cellspacing="0" cellpadding="5">
  <colgroup>
    <col style="width: 10%">
    <col style="width: 10%">
    <col style="width: 10%">
    <col style="width: 56%">
  </colgroup>
  <thead>
    <tr>
      <th colspan="3"style="text-align: center; vertical-align: middle;"><strong>Item</strong></th>
      <th style="text-align: center; vertical-align: middle;" ><strong>Description</strong></th>
    </tr>
  </thead>
  <tbody>
  <tr>
      <td colspan="3"style="text-align: center; vertical-align: middle;">easy-setup.sh</td>
      <td>Python script to automatically download and build SDK</td>
    </tr>
    <tr>
      <td colspan="3"style="text-align: center; vertical-align: middle;">stitch-fai-ai.sh</td>
      <td>Script for creating AI-G fai images (minimal + Sample Application)</td>
    </tr>
    <tr>
      <td colspan="3"style="text-align: center; vertical-align: middle;">stitch-fai-d3.sh</td>
      <td>Script for creating D3-G fai images (minimal + Sample Application)</td>
    </tr>
    <tr>
      <td colspan="3"style="text-align: center; vertical-align: middle;">mktcimg</td>
      <td rowspan="2">Tools related to the build process and <strong>FWDN</strong></td>
    </tr>
    <tr>
      <td colspan="3"style="text-align: center; vertical-align: middle;">tools</td>
    </tr>
    <tr>
      <td rowspan="8"style="text-align: center; vertical-align: middle;">poky</td>
      <td colspan="2"style="text-align: center; vertical-align: middle;">poky</td>
      <td>Yocto Project 4.0 Kirkstone build system</td>
    </tr>
    <tr>
      <td colspan="2"style="text-align: center; vertical-align: middle;">meta-openembedded</td>
      <td>Layer that supports OE-Core</td>
    </tr>
    <tr>
      <td colspan="2"style="text-align: center; vertical-align: middle;">meta-arm</td>
      <td>Layer that supports ARM toolchain</td>
    </tr>
    <tr>
      <td colspan="2"style="text-align: center; vertical-align: middle;">meta-topst-bsp</td>
      <td>Layer that supports TOPST BSP</td>
    </tr>
    <tr>
      <td colspan="2"style="text-align: center; vertical-align: middle;">meta-gplv2</td>
      <td>Layer that includes packages avoiding the GPLv3 license</td>
    </tr>
    <tr>
      <td colspan="2"style="text-align: center; vertical-align: middle;">meta-topst</td>
      <td>TOPST recipe</td>
    </tr>
  </tbody>
</table>
<br/><br/><br/>


## 3.5 Ready to build
---
The following chapters describes how to configure the Yocto Project to build the D3-G image.

<br/><br/>

### 3.5.1 Set User Email and User Name in .gitconfig
To download the D3-G SDK from the official TOPST git, configure your email and name.
1. Enter the following command.
```
vi ~/.gitconfig
```
2. Enter the following information
```
[user]
    email = User email
    name = User name
```

<br/><br/>

### 3.5.2 Get D3-G from Git

1. Create a new directory named **topst-sdk** and change the current directory to **topst-sdk**.

```
$ mkdir topst-sdk
$ cd topst-sdk
```

2. Execute the following command to initialize the repository.

```
$ repo init -u https://github.com/topst-development/manifests.git -m linux_yp4.0_topst.xml
```

After running the command, the following output is displayed.

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

3. Execute the following command to synchronize the repository.

```
$ repo sync
```

After running the command, the following output is displayed.

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

## 3.6 Execute topst-build.sh 
---
If you run the ./easy-setup.sh script, you can see the following screen. 

**Caution: If you re-run ./easy-setup.sh, be careful as the built sources will be deleted if you select yes.**
```
./easy-setup.sh
```
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20AI-G/Software/Linux%20SDK/license1.png"></p>
<p align="center"><strong>Figure 3.2 End User License Agreement</strong></p>

Scroll down to the bottom of the screen and read this notice. After you read this notice, press the right arrow key and [Enter].
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20AI-G/Software/Linux%20SDK/license2.png"></p>
<p align="center"><strong>Figure 3.3 Go To 'Proceed to confirm'</strong></p>


Then you can see the following screen. 
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20AI-G/Software/Linux%20SDK/license3.png" ></p>
<p align="center"><strong>Figure 3.4 Accept Screen </strong></p>


The build image is created in the following path:

- {TOPST_PATH}/build/d3-g-topst-main/tmp/deploy/images/d3-g-topst-main

topst-build.sh is a shell script that sets up the core environment required to build images for D3-G and AI-G. Execute the following commands, and select option 2 to prepare the build environment for installing the main OS on the D3-G.



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

Run the following command to start building the main OS.
```
$ bitbake telechips-topst-image
```

<br/><br/><br/>

## 3.7 Make Firmware Downloader (FWDN) Image 
---
This option combines the binaries into a single image for the D3-G platform image.

The **output_d3g.fwdn.zip** file, which includes the **'output_d3g.fai' build image** and **FWDN tools**, is created in the following path:

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

If you see the following log, it means the "output_d3g.fwdn.zip" file is created. 
```
$ ls
build  easy-setup.sh  mktcimg  output_d3g.fwdn.zip  poky  stitch-fai-ai.sh  stitch-fai-d3.sh  tools
```

</br></br><br/><br/>

# 4. Firmware Download
---
This chapter describes how to use ***FWDN*** to download firmware to the D3-G and login to the Linux console.  
***FWDN V8*** is a PC tool for downloading firmware in both Windows 10(11) 64-bit and Linux environments. This chapter describes the case of downloading in Windows and Linux environments.

<br/><br/><br/>

## 4.1 Firmware Download Sequence
---
The downloading sequence of ***FWDN*** is as follows:

1. Set the boot mode switch to USB boot mode.
2. Open a Windows prompt or Linux console.
3. Connect ***FWDN V8*** to the board.
4. Download the fai file.

<br/><br/><br/>

## 4.2 Connect D3-G board and Host PC with USB Boot Mode
---
Firmware Downloader (FWDN) writes a ROM image to the D3-G through USB communication with the Host PC. 

The D3-G has one Boot Mode button and supports two types of boot modes. This guide focuses on the FWDN mode.

- USB Boot Mode (FWDN Mode) : Used to write a ROM image by using the FWDN tool on your Host PC 

- eMMC Boot Mode : Used to boot the D3-G by using a ROM image that is stored in an eMMC device 

**Note**: The USB Type-C FWDN port is used for firmware downloader (FWDN). 



To use FWDN, connect the D3-G board to the Host PC as follows: 

1. Check that VTC driver is installed on the Host PC. If the VTC driver is not installed, install it as shown in Chapter 4.2.1.  

2. Prepare one USB Type-C cable. 

3. To enter USB boot mode, connect the power cable to the D3-G board while pressing the FWDN switch.
   - For more details, see **"2. Boot Mode"** under the Hardware section of the sidebar.

4. Connect the USB Type-C cable to the USB Type-C FWDN port on the D3-G board and the Host PC. 

<p align="center">
    <img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20D3-G/Hardware/connect%20to%20d3g%20to%20host%20pc%20using%20c%20type.png">
</p>
<p align="center"><strong>Figure 4.1 Connection to D3-G Board to Host PC Using USB C-Type Cable </strong></p>

<br/><br/>

### 4.2.1 How to install VTC Driver (Windows/Ubuntu)
Install the Vendor Telechips Certification (VTC) driver (found on [telechips driver](https://drive.google.com/file/d/1muQnY8kuKxDsy3p3FUiQqcG34Zjk-mnR/view?usp=sharing)) on the host PC by running as administrator. When you connect the USB in the FWDN mode as shown above, the Telechips VTC USB driver is set as shown in Figure 4.2 and Figure 4.3.

<p align="center">
    <img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20D3-G/Software/USB%20Connection%20in%20Windows%20Environment.png", width="700">
</p>
<p align="center"><strong>Figure 4.2 USB Connection in Windows Environment</strong></p>

<p align="center">
    <img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20D3-G/Software/USB%20Connection%20in%20Linux%20System.png", width="700">
</p>
<p align="center"><strong>Figure 4.3 USB Connection in Linux Environment</strong></p>  

**Note**: Use the VTC Driver V5.0.0.14 or higher. To check the version, confirm the device manager in Windows environment.  

<br/><br/><br/>

## 4.3 Ready to Download FWDN
---
Before executing FWDN, transfer the image and tools created in the Ubuntu (WSL2) environment to the Windows environment.


1. Unzip "output_d3g.fwdn.zip".   
    ```
    $ cd ~/topst-sdk
    $ mkdir images
    $ mv ./output_d3g.fwdn.zip ./images
    $ cd images
    $ unzip output_d3g.fwdn.zip
    ```
2. Copy "images" folder to Windows C drive.  
    ```
    $ cd ..
    $ cp -r ./images /mnt/c/
    ```

<br/><br/><br/>

## 4.4 FWDN in Windows Environment
---
1. Execute Powershell and go to "C:\images\".
```
$ cd C:\images 
```

2. Enter **.\fwdn.bat** command to start the firmware download. The “fwdn.bat” is an executable file that automatically downloads firmware by using FWDN V8. 

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

## 4.5  FWDN in Linux Environment
---
To download the D3-G image in Linux, execute the following command: "./fwdn.sh".

```
$ ./fwdn.sh
```

You’re ready to boot the D3-G. Refer to Chapter 5 to start communicating with the device.


<br/><br/><br/><br/>

# 5. Connecting the D3-G board with a host PC
---
This chapter explains how to connect the host PC to the D3-G board through UART for firmware download and serial communication.

<br/><br/><br/>

## 5.1 D3-G board Connection with UART 
---
Follow these steps and verify that the firmware download is successfully completed by using the UART connection. 

1. Install the serial port driver (for example, CP210x Universal Windows Driver) and PL2303_prolific driver in the Windows environment. 
2. Install a terminal emulator such as Tera Term or PuTTY. 
3. Connect the Host PC and UART Pin on the D3-G board. Use a USB-to-TTL cable. 
4. Connect the black cable to the GND pin. 
5. Connect the white cable (RXD) to TX pin of the UART pins and the green cable (TXD) to RX pin of UART pins.
6. Run the terminal emulator application.
7. Open Device Manager on your PC and check the port number assigned to the UART device.
8. In the terminal emulator, enter the verified port number into the Serial line field. Set **Speed** (bps) to 115200 and **Flow control** to **None.**
9. Connect the power cable. Then, the D3-G board boots in the default eMMC boot mode.


 
<p align="center">
    <img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20D3-G/Software/USB%20to%20TTL%20Connection.png", width="700">
</p>
<p align="center"><strong>Figure 5.1 UART Connection with Host PC</strong></p><br/>  


Figure 5.2 shows a successful login.  
Both the username and password for login are set to **root**.

<p align="center">
    <img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20D3-G/Software/d3-g%20login%20as%20root.png", width="700">
</p>
<p align="center"><strong>Figure 5.2 Connected Screen (ID and Password are topst)</strong></p><br/>

<br/><br/><br/>

# 6. Ubuntu OS partition resize
---
We also provide an Ubuntu OS.
By following this chapter, you can download the Ubuntu image, upload it to the board, and expand the allocated eMMC storage capacity.

<br/><br/><br/>

## 6.1 Download Ubuntu Image
---
Official of D3-G is based on Ubuntu 22.04.  
You can download the image file here.  

<img src="https://github.com/topst-development/Documentation/assets/161264431/83d93c78-6437-4f96-a0bf-23f22da1aba1">  

**Download :**  
-	[Download Link here](https://drive.google.com/file/d/1oc2qwaXUt6-QDME3s5WXKVHzAg4xqVyc/view?usp=drive_link)
<br>
-	For more information, visit our [github page](https://github.com/topst-development).

**Release note :**  

|Ver|   Date   |
|:-:|:--------:|
|1.0|2024.04.25|  

TOPST team is also preparing other official OS versions.  
For information on releases of other OS, refer to the TOPST community.  

<br/><br/><br/>

## 6.2 Firmware Upload to D3-G
---
Run the “fwdn_ubuntu.batch” file. 
Refer to Chapter 5 for how to upload the Ubuntu image to the D3-G.
After completing FWDN, remove the USB Type-C cable from the FWDN port and remove the power cable. 

<br/><br/><br/>

## 6.3 Resize eMMC Storage (Only D3-G)
---
After logging in and booting the board, it is recommended to resize the eMMC storage first.
Follow the steps below for eMMC Storage resizing.

1. To modify the partition size and layout, use the following command.
     ```
     $ parted
     ```

2. Extend the GUID Partition Table(GPT). 
    ```
    $ rescue
    $ Fix 
    $ 0 
    $ 100%
    ```
3. Use the p (print) command to check that the partition type is ext4. 
   ```
   $ p
   ```
4. Resize partition 4.
    ```
    $ resizepart 4
    $ Yes
    $ 100%
    ```
5. Reboot the board.
6. Resize the ext4 filesystem on partition 4.
    ```
    $ resize2fs /dev/mmcblk0p4
    ```
7. Check the changed partition size by using the following command.
   ```
   $ df -h
   ```

You can confirm that the available space is 27GB after resizing.

<br/><br/><br/><br/>

# 7. References
---
- Contact TOPST for more details: topst@topst.ai

**Note:** Reference documents can be provided whenever available, depending on the terms of a contract. If the reference
documents are unavailable, the contents directly related to your development can be guided.
