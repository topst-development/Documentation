# 1. Introduction
This document provides guidelines for building the TOPST D3-G SDK, including setting up the host environment, building the SDK, using the firmware downloader, and downloading Ubuntu.  

This document includes information on the following: 
- Setting Host Environment  
- Image Build Guide  
- Firmware Download Guide 
- Connecting the D3-G with a PC
<br/><br/>

# 2. Setting Host Environment
This chapter provides instructions on how to set up the host PC environment, with separate guides for setting up on Windows PC and Ubuntu PC.
</br>

## 2.1 Windows Environment 
This document provides instructions on how to set up WSL (Windows Subsystem for Linux) to use Linux on a Windows PC.
Since TOPST D3 Linux SDK is based on the Yocto Project, Linux version of TOPST D3 SDK follows the Yocto project.
You can install another version of Linux, but in this document, TOPST D3 Linux SDK is described based on Ubuntu 22.04.
If the host OS is Ubuntu, please proceed to Section 2.2.
</br>

### 2.1.1 Install WSL2 Ubuntu
1. Excute Windows PowerShell with "**Run with administrator privileges**"
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

6. You may choose any user name during the Ubuntu installation
</br>

### 2.1.2 Accessing Ubuntu via WSL2
Open the Windows Command Prompt and enter the following command to access Ubuntu.
When you access Ubuntu, it starts in the /mnt/c/Users/[user name] directory by default.
```
wsl  // access ubuntu 
ls   // check contents in your directory
```
Refer to the figure 1.1 below to check the result (may vary depending on the user).
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20D3-G/Software/1.1%20wsl%20linux.png" width="500"></p>
<p align="center"><strong>Figure 1.1 WSL2 Screenshot </strong></p>

<br/>

### 2.1.3 Install SSH and Samba

After entering Ununtu, you can use additional utilities such as SSH and Samba for more convenient development environment. SSH and Samba allows you to execute commands on remote computers and copy files to other computers.
 - The following steps require the Host PC to be connected to the network. check your network condition as following commands
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
After downloading SSH and Samba, you should set each program to your environment.
</br>

### 2.1.4 Install Utilities

Install the utilities at once. To use Yocto Project, the following utilities must be installed on Host PC(individual computer or development server).

Use the following command to install Utilities.

```
$ sudo apt-get install -y gawk wget git diffstat unzip texinfo gcc-multilib build-essential chrpath

$ sudo apt-get install -y socat cpio python3 python3-pip python3-pexpect xz-utils debianutils

$ sudo apt-get install -y iputils-ping python3-git python3-jinja2 libegl1-mesa libsdl1.2-dev pylint

$ sudo apt-get install -y xterm zstd ncftp curl git-lfs vim zip
```

<br/>

### 2.1.5 Install Repo

You can download TOPST D3 SDK through Android Repo.  
To install Repo, refer to the following website: https://source.android.com/source/downloading.html.  
If Repo is already installed, you can use it without re-installing.  
Before installing Repo, the installed Python version (3.6 or higher) should be properly set.

Use the following command to install repo.
```
$ sudo apt-get install repo
```

If you see the error messange '/usr/bin/env 'python' no such file or directory', use the following command that allows the file 'python' to point to 'python3'.

```
$ sudo ln -sf /usr/bin/python3 /usr/bin/python
```
If there is a Repo error, Use the following command to download the latest version and put it directly into the /usr/bin/ folder.

```
$ mkdir -p ~/bin

$ curl http://commondatastorage.googleapis.com/git-repo-downloads/repo > ~/bin/repo

$ chmod a+x ~/bin/repo

$ sudo mv ~/bin/repo /usr/bin/repo
```
Please proceed to **Chapter 3: Image Build Guide**.

<br/><br/>

## 2.2 Linux Environment
This section explains the setup process for Ubuntu as the host OS.
</br>

### 2.2.1 Setting Environment
The following steps are to be executed in the Ubuntu terminal. (Shortcut: Ctrl+Alt+T)

### 2.2.2 Install SSH and Samba

After starting terminal in Ununtu, you can use additional utilities such as SSH and Samba for more convenient development environment. SSH and Samba allows you to execute commands on remote computers and copy files to other computers.
 - The following steps require the Host PC to be connected to the network. check your network condition as following commands
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
After downloading SSH and Samba, you should set each program to your environment.

<br/>

### 2.2.3 Install Utilities

Install the utilities at once. To use Yocto Project, the following utilities **must** be installed on Host PC(individual computer or development server).
****
Use the following command to install Utilities.

```
$ sudo apt-get install -y gawk wget git diffstat unzip texinfo gcc-multilib build-essential chrpath

$ sudo apt-get install -y socat cpio python3 python3-pip python3-pexpect xz-utils debianutils

$ sudo apt-get install -y iputils-ping python3-git python3-jinja2 libegl1-mesa libsdl1.2-dev pylint

$ sudo apt-get install -y xterm zstd ncftp curl git-lfs vim zip
```

<br/>

### 2.2.4 Install Repo

You can download TOPST D3 SDK through Android Repo.  
To install Repo, refer to the following website: https://source.android.com/source/downloading.html.  
If Repo is already installed, you can use it without re-installing.  
Before installing Repo, the installed Python version (3.6 or higher) should be properly set.

Use the following command to install repo.
```
$ sudo apt-get install repo
```

If you see the error messange '/usr/bin/env 'python' no such file or directory', use the following command that allows the file 'python' to point to 'python3'.

```
$ sudo ln -sf /usr/bin/python3 /usr/bin/python
```
If there is a Repo error, Use the following command to download the latest version and put it directly into the /usr/bin/ folder.

```
$ mkdir -p ~/bin

$ curl http://commondatastorage.googleapis.com/git-repo-downloads/repo > ~/bin/repo

$ chmod a+x ~/bin/repo

$ sudo mv ~/bin/repo /usr/bin/repo
```
<br/>


### 2.2.5 Udev Rules for Telechips USB Device
After you excute following command, You don't need to use 'sudo' command when you download FWDN in Linux.
```
$ echo "SUBSYSTEM==\"usb\", ATTR{idVendor}==\"140e\", MODE=\"0666\", OWNER=\"${USER}\"" | sudo tee /etc/udev/rules.d/99-topst.rules
$ sudo udevadm control --reload-rules && sudo udevadm trigger
```
Please proceed to **Chapter 3: Image Build Guide**.

<br/><br/>

# 3. Image Build Guide
This section provides guidance based on the Ubuntu OS installed on the host PC (regardless of whether it is WSL or a local Ubuntu installation). The image to be uploaded to the D3-G is built using the Yocto Project, and therefore the process must be carried out in the Ubuntu environment.
</br></br>

## 3.1 SDK Build Prepration

TOPST D3 Linux SDK is based on Yocto Project 3.1 Dunfell. Therefore, the Yocto Project environment must be set on the host PC to use TOPST D3 Linux SDK. To download SDK, source-mirror, and tools, you must install utilities. To build the image smoothly, the user's PC must have **at least 60 GB of available storage** and **a minimum of 16 GB of RAM**.
</br>   

## 3.2 Yocto Project  

The Yocto Project is an open source project focuses on embedded Linux development.  
It uses a combination of Open Embedded project, which is Poky, and ***bitbake*** as the build system to make Linux images.  
By using Yocto Project, you can simultaneously build the bootloader, kernel, and rootfs.  

<br/>

## 3.3 Task Process of Yocto Project

Figure 1 shows the task process of Yocto Project. You can download source from upstream based on metadata and build it. After the build is completed, package, image, and SDK are provided as results.

<p align="center">
    <img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20D3-G/Software/2.1%20yocto%20project%20task%20process.png", width="700">
</p>
<p align="center"><strong>Figure 1 Yocto Project Task Process</strong></p>

<br/>

## 3.4 Composition of TOPST D3-G SDK
The following are the components of the Yocto Project we have configured.
Figure 2 shows composition of TOSPT D3-G SDK.


**Table 1 Composition of TOPST SDK:**
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
      <td colspan="3"style="text-align: center; vertical-align: middle;">easy-setup_ai-g.sh</td>
      <td>Python script to automatically download and build the AI-G SDK</td>
    </tr>
    <tr>
      <td colspan="3"style="text-align: center; vertical-align: middle;">easy-setup_d3-g.sh</td>
      <td>Python script to automatically download and build the D3-G SDK</td>
    </tr>
    <tr>
      <td colspan="3"style="text-align: center; vertical-align: middle;">stitch-fai_ai-g.sh</td>
      <td>Script for making ai-g fai images (minimal + Sample Application)</td>
    </tr>
    <tr>
      <td colspan="3"style="text-align: center; vertical-align: middle;">stitch-fai_d3-g.sh</td>
      <td>Script for making d3-g fai images (minimal + Sample Application)</td>
    </tr>
    <tr>
      <td colspan="3"style="text-align: center; vertical-align: middle;">boot-firmware_ai-g</td>
      <td rowspan="6">Tools related to the build process and <strong>FWDN</strong></td>
    </tr>
     <tr>
      <td colspan="3"style="text-align: center; vertical-align: middle;">boot-firmware_d3-g</td>
    </tr>
     <tr>
      <td colspan="3"style="text-align: center; vertical-align: middle;">boot-firmware_d5-g</td>
    </tr>
    <tr>
      <td colspan="3"style="text-align: center; vertical-align: middle;">fwdn v8_ai-g</td>
    </tr>
    <tr>
      <td colspan="3"style="text-align: center; vertical-align: middle;">fwdn v8</td>
    </tr>
    <tr>
      <td colspan="3"style="text-align: center; vertical-align: middle;">mktcimg</td>
    </tr>
    <tr>
      <td rowspan="8"style="text-align: center; vertical-align: middle;">poky</td>
      <td colspan="2"style="text-align: center; vertical-align: middle;">poky</td>
      <td>Yocto Project 4.0 Kirkstone build system</td>
    </tr>
    <tr>
      <td colspan="2"style="text-align: center; vertical-align: middle;">meta-openembedded</td>
      <td>Support OE-Core Layer</td>
    </tr>
    <tr>
      <td colspan="2"style="text-align: center; vertical-align: middle;">meta-arm</td>
      <td>Support ARM toolchain Layer</td>
    </tr>
    <tr>
      <td colspan="2"style="text-align: center; vertical-align: middle;">meta-topst-bsp</td>
      <td>Support TOPST BSP Layer</td>
    </tr>
    <tr>
      <td colspan="2"style="text-align: center; vertical-align: middle;">meta-gplv2</td>
      <td>Support packages that avoid GPLv3 license</td>
    </tr>
    <tr>
      <td>meta-telechips</td>
      <td>meta-core</td>
      <td>
        Recipes that require modification from Open-Source Software (OSS) used by Telechips TOPST AI-G SDK or recipes that are not in Yocto Project 4.0
      </td>
    </tr>
    <tr>
      <td colspan="2"style="text-align: center; vertical-align: middle;">meta-topst</td>
      <td>TOPST recipe</td>
    </tr>
  </tbody>
</table>
<br/>
<br/>

## 3.5 Ready to build
The following sections provide instructions on how to configure the Yocto Project to build the D3-G image.
<br/>

### 3.5.1 Set User Email and User Name in .gitconfig
To download TOPST D3-G from the TOSPT official git, configure your email and name.
1. Enter the following command.
```
vi ~/.gitconfig
```
2. Enter the following information
```
    email = User email
    name = User name
```

### 3.5.2 Get TOPST-D3 with Git
Below is our Yocto configuration XML file. You can download the repository to get started.

```
$ mkdir topst_sdk
$ cd topst_sdk

$ repo init -u git@gitlab.com:topst-private-release/manifests.git -m linux_yp4.0_topst_1.0.0.xml
Downloading Repo source from https://gerrit.googlesource.com/git-repo

... A new version of repo (2.54) is available.
... New version is available at: /home/sooyong/topst_dev/.repo/repo/repo
... The launcher is run from: /usr/bin/repo
!!! The launcher is not writable.  Please talk to your sysadmin or distro
!!! to get an update installed.


Your identity is: sooyong <adrenalin7237@gmail.com>
If you want to change this, please re-run 'repo init' with --config-name

repo has been initialized in /home/sooyong/topst_dev
```

```
$ repo sync

... A new version of repo (2.54) is available.
... New version is available at: /home/sooyong/topst_dev/.repo/repo/repo
... The launcher is run from: /usr/bin/repo
!!! The launcher is not writable.  Please talk to your sysadmin or distro
!!! to get an update installed.

Fetching: 100% (14/14), done in 33.045s
boot-firmware_ai-g: Shared project bsp/boot-firmware found, disabling pruning.
fwdn_v8: Shared project tools/fwdn_v8 found, disabling pruning.
Checking out:  57% (8/14), done in 0.898s
Checking out:  42% (6/14), done in 0.365s
repo sync has finished successfully.
```

<br/><br/>

## 3.6 Execute topst-build.sh 
If you run ./easy-setup_d3-g.sh script, you can see the following screen. 

Caution: If you re-run ./easy-setup_d3-g.sh, be careful as the built sources will be deleted if you select yes.
```
./easy-setup_d3-g.sh
```
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20AI-G/Software/Linux%20SDK/license1.png"></p>
<p align="center"><strong>Figure 3 End User License Agreement</strong></p>
<br/>
Scroll down to the bottom of the screen and read this notice. After you read this notice, press the right arrow key and [Enter].
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20AI-G/Software/Linux%20SDK/license2.png"></p>
<p align="center"><strong>Figure 4 Go To 'Proceed to confirm'</strong></p>
<br/>

Then you can see the following screen. 
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20AI-G/Software/Linux%20SDK/license3.png" ></p>
<p align="center"><strong>Figure 5 Accept Screen </strong></p>
<br/>

The build image is created in the following path:

- {TOPST_PATH}/build/d3-g-topst-main/tmp/deploy/images/d3-g-topst-main

topst-build.sh is a shell script that sets up the core environment required to build TOPST images for D3-G and AI-G boards. Execute the following commands. By selecting option 2, you are now ready to install the main OS on the D3-G.



```
$ . poky/meta-topst/topst-build.sh 
Choose MACHINE
  1. ai-g-topst
  2. d3-g-topst-main
  3. d3-g-topst-sub
  4. d5-g-topst-main
  5. d5-g-topst-sub
select number(1-5) => 2
machine(d3-g-topst-main) selected.
You had no conf/local.conf file. This configuration file has therefore been
created for you from /home/sooyong/topst_dev/poky/meta-topst/template/d3-g-topst-main/local.conf.sample
You may wish to edit it to, for example, select a different MACHINE (target
hardware). See conf/local.conf for more information as common configuration
options are commented.

You had no conf/bblayers.conf file. This configuration file has therefore been
created for you from /home/sooyong/topst_dev/poky/meta-topst/template/d3-g-topst-main/bblayers.conf.sample
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


You can also run generated TOSPT images on TOPST board

Other commonly useful commands are:
 - 'devtool' and 'recipetool' handle common recipe tasks
 - 'bitbake-layers' handles common layer tasks
 - 'oe-pkgdata-util' handles common target package tasks

```

Run the following command to start building the main OS.
```
$ bitbake telechips-topst-image
```

## 3.7 Make FWDN Image

This option creates a binary into one image for TOPST D3 platform image.

The **output.fwdn.zip** including **'output.fai' build image** and **fwdn tools** is created in the following path:

-  ~/topst-sdk/

```
$ cd ~/topst-sdk/ && \ 

$ ./stitch-fai_d3-g.sh -f

Filesystem too small for a journal
[mktcimg] v1.2.1 - Nov 15 2021 19:33:18
location : bl3_ca72_a 
location : 4096 sector(2097152 byte)
location : build-main/tmp/deploy/images/tcc8050-main/ca72_bl3.rom 
location : boot 
location : 122880 sector(62914560 byte)
location : build-main/tmp/deploy/images/tcc8050-main/tc-boot-tcc8050-main.img 
location : system 
location : 11534336 sector(5905580032 byte)
location : build-main/tmp/deploy/images/tcc8050-main/topst-tcc8050-main.ext4 
location : dtb 
location : 400 sector(204800 byte)
location : build-main/tmp/deploy/images/tcc8050-main/tcc8050-linux-topst-d3-pre-v0.1.dtb 
location : env 
location : 2048 sector(1048576 byte)
location : misc 
location : 2048 sector(1048576 byte)
location : splash 
location : 81920 sector(41943040 byte)
location : home 
location : 3516416 sector(1800404992 byte)
location : /home/ben/topst/.stitch_XXRNlst/home-directory.ext4 
location : data 
location : 2048 sector(1048576 byte)
location : /home/ben/topst/.stitch_XXRNlst/user-data.ext4 
path : build-main/tmp/deploy/images/tcc8050-main/ca72_bl3.rom 
uuid : 372cbca7-25e2-480b-b8ec-2736ed1f02d0 , part-name : bl3_ca72_a 
uuid : b12c0ebc-2802-4d04-92ae-a52bbc3082e5 , part-name : boot 
uuid : bbd5770e-1f3d-4bc6-ac17-4abeecf14a1e , part-name : system 
uuid : 541d9405-8d40-43cf-9255-74fc5c0fbef7 , part-name : dtb 
uuid : d71a2a08-9ffe-4690-8b27-c6c371f5b4a8 , part-name : env 
uuid : e9e9b9f3-27b9-4822-9ab5-bb09554dfde2 , part-name : misc 
uuid : 49578c16-ea11-4f27-bc82-c1f9a60ce33b , part-name : splash 
uuid : 2cf93985-4ae4-4ea0-bc67-6c991ac8eb7d , part-name : home 
uuid : ccc4aaaa-92a1-4e02-b55d-215a0ad92d29 , part-name : data 
crc32 of header : f33d4c30 
crc32 of partition array : a65980dc 
idx : 0  bl3_ca72_a 
idx : 1  boot 
idx : 2  system 
idx : 3  dtb 
idx : 7  home 
idx : 8  data 
crc32 of header : f33d4c30 
crc32 of partition array : 61f17e08 
Complete to make fai file

===== arguments info =====

--storage_size : 7818182656
--parttype : gpt
--area_name : "SD Data"
--outfile : /home/ben/topst/.stitch_XXRNlst/output.fai
--gptfile : /home/ben/topst/.stitch_XXRNlst/output.gpt
--fplist : /home/ben/topst/.stitch_XXRNlst/partition.single.list
--sector_size : 512
--sparse_fill : 0

===========================

[+] Packaging FWDN binaries
  adding: output.fai (deflated 97%)
  adding: VtcUsbPort.dll (deflated 64%)
  adding: boot-firmware/ (stored 0%)
  adding: fwdn (deflated 63%)
  adding: fwdn.bat (deflated 40%)
  adding: fwdn.exe (deflated 57%)
  adding: fwdn.sh (deflated 44%)
  adding: output.gpt (deflated 98%)
  adding: output.gpt.back (deflated 97%)
  adding: output.gpt.prim (deflated 97%)
  adding: boot-firmware/bconf.dual.bin (deflated 94%)
  adding: boot-firmware/bconf.single.bin (deflated 93%)
  adding: boot-firmware/boot.dual.json (deflated 86%)
  adding: boot-firmware/boot.single.json (deflated 86%)
  adding: boot-firmware/ca53_bl1.rom (deflated 51%)
  adding: boot-firmware/ca53_bl2.rom (deflated 50%)
  adding: boot-firmware/ca72_bl1.rom (deflated 51%)
  adding: boot-firmware/ca72_bl2.rom (deflated 49%)
  adding: boot-firmware/dram_params.bin (deflated 78%)
  adding: boot-firmware/fwdn.json (deflated 41%)
  adding: boot-firmware/fwdn.rom (deflated 46%)
  adding: boot-firmware/hsm.bin (deflated 51%)
  adding: boot-firmware/hsm.cs.bin (deflated 13%)
  adding: boot-firmware/mcert.bin (deflated 96%)
  adding: boot-firmware/optee.rom (deflated 92%)
  adding: boot-firmware/scfw.rom (deflated 53%)

```

Finally, you can check **'output.fwdn.zip'**.

Please proceed to **Chapter 4: Firmware Download**.

</br></br>

# 4. Firmware Download
This chapter describes how to download ***FWDN*** to the TOPST D3-G and login the Linux console.  
The ***FWDN V8*** is a PC tool for downloading firmware in Windows 10(11) 64-bit and Linux environments. This chapter describes the case of downloading in Windows and Linux environments.

## 4.1 Firmware Download Sequence

The downloading sequence of ***FWDN*** is as follows:

1. Set the boot mode switch to USB boot mode.
2. Open Windows prompt or Linux console and test ***FWDN V8***.
3. Connect ***FWDN V8*** to board.
4. Download fai file.

<br/>

## 4.2 Connect TOPST D3 and Host PC with USB Boot
Firmware Downloader (FWDN) writes a ROM image to the TOPST D3-G through USB communication on the Host PC. 

The TOPST D3-G has one Boot Mode button and supports two types of boot modes. In this guide, we focus on the FWDN mode.

- USB Boot Mode (FWDN Mode) : Used to write a ROM image by using the FWDN program on your Host PC 

- eMMC Boot Mode : Used to boot the TOPST D3-G by using a ROM image that is stored in an eMMC device 

**Note**: USB Type-C FWDN port is used for firmware downloader (FWDN). 

<br/>

To use FWDN, connect the TOPST D3-G to the Host PC as follows: 

1. Check that VTC driver is installed on the Host PC. If the VTC driver is not installed, install it as shown in Chapter 1.2.1.  

2. Prepare one USB Type-C cable. 

3. To enter USB Boot mode, connect the power cable to the TOPST D3-G while pressing the FWDN switch.
   - For more details, please refer to the **"Hardware/Boot Mode" chapter.**

4. Connect the USB Type-C cable to the USB Type-C FWDN Port on the TOPST D3-G and the Host PC. 

<p align="center">
    <img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20D3-G/Hardware/connect%20to%20d3g%20to%20host%20pc%20using%20c%20type.png">
</p>
<p align="center"><strong>Figure 6 Connection to D3-G to Host PC Using USB C-Type Cable </strong></p>

<br/>

### 4.2.1 How to install VTC Driver (Windows/Ubuntu)
Install the Vendor Telechips Certification (VTC) driver (found on [telechips driver](https://drive.google.com/file/d/1muQnY8kuKxDsy3p3FUiQqcG34Zjk-mnR/view?usp=sharing)) on the host PC by running as administrator. When you connect the USB in the FWDN mode as shown above, the Telechips VTC USB driver is set as shown in the Figure 3.2 and Figure 3.3.

<p align="center">
    <img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20D3-G/Software/USB%20Connection%20in%20Windows%20Environment.png", width="700">
</p>
<p align="center"><strong>Figure 7 USB Connection in Windows Environment</strong></p>

<p align="center">
    <img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20D3-G/Software/USB%20Connection%20in%20Linux%20System.png", width="700">
</p>
<p align="center"><strong>Figure 8 USB Connection in Linux Environment</strong></p>  

**Note**: Use the VTC Driver V5.0.0.14 or higher. To check the version, confirm the device manager in Windows environment.  

<br/><br/>

## 4.3 Ready to Download FWDN
Before executing FWDN, you must first transfer the image and FWDN tool you created after the build from Ubuntu (WSL2) to the Windows Environment.


1. Unzip "output.fwdn.zip" 
    ```
    $ cd ~/topst-sdk/ && \ 
    $ mkdir images && \
    $ mv ./output.fwdn.zip ./images && \
    $ cd images && \
    $ unzip output.fwdn.zip && \
    ```
2. Copy "images" folder to Windows C drive.
    ```
    $ cd .. && \
    $ cp -r /images /mnt/c/ && \
    ```

<br/>

## 4.4 FWDN in Windows Environment

1. Excute Powershell and go to "C:\images\".
```
$ cd C:\images 
```

2. Enter **.\fwdn.bat** command to start the download. The “fwdn.bat” is an executable file that automatically downloads firmware by using FWDN V8. 

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
C:\images>fwdn.exe -w "output.fai" --storage emmc --area user
[main:30] FWDN V8 v1.4.6 - 2021.12.13 13:42:37
[FWDN_V8::GetFWDNRomVersion:1526] fwdn.rom version : 21.9.29
[main:117] Start write command
[FWDN_V8::GetFileAndWriteCommand:748] output.fai
[main:125] Complete write command
[main:142] Complete FWDN
[FWDNLogger::PrintCurTime:111] 24/04/25-10:05:21
100% [||||||||||||||||||||||||||||||] 7238688960/7238688960
** When writing FAI files without low-format, there may be garbage values in partition where data is not written.
```
<br/>

## 4.5  FWDN in Linux Environment

In a Linux environment, you can download TOPST image with command "./fwdn.sh".

```
$ ./fwdn.sh
```

You’re now all set to boot the D3-G. Please refer to Chapter 4 to start communicating with the device.

Please proceed to **Chapter 5: Connecting the D3-G with a host PC**.
<br/><br/>

# 5. Connecting the D3-G with a host PC

This chapter provides instructions on how to set up the host PC environment, with separate guides for setting up on Windows PC and Ubuntu PC.
<br/>

## 5.1 D3-G Connection with UART 

Perform the following steps and verify that the firmware download is successfully completed by using the UART connection. 

1. Install the serial port driver (CP210x Universal Windows Driver) and PL2303_prolific driver in the Windows environment. (CP210x Universal Windows Driver: Download link, PL2303_prolific Driver: Download link) 

2. Install a terminal emulator such as Tera Term or PuTTY. 
3. Connect the Host PC and the A72 UART Pin on the TOPST D3-G. Use a USB to TTL Cable. 
4. Connect the black cable to GND pin. 
5. Connect the RXD cable to TX pin of A72 UART pins and TXD cable to RX pin of UART pins. 

 
<p align="center">
    <img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20D3-G/Software/USB%20to%20TTL%20Connection.png", width="700">
</p>
<p align="center"><strong>Figure 9 UART Connection with host PC</strong></p>  


The figure 10 below shows a successful login.  
Both the username and password for login are set to **root**.

<p align="center">
    <img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20D3-G/Software/d3-g%20login%20as%20root.png", width="700">
</p>
<p align="center"><strong>Figure 10 Connected Screen (ID and Password are topst)</strong></p>  

<br/><br/>

# 6. Ubuntu OS partition resize
We also provide an Ubuntu OS.
By following this section, you can download the Ubuntu image, upload it to the board, and expand the allocated eMMC storage capacity.
<br/>

## 6.1 Download Ubuntu Image
Official of TOPST D3-G is based on Ubuntu 22.04.  
You can download the image file here.  

<img src="https://github.com/topst-development/Documentation/assets/161264431/83d93c78-6437-4f96-a0bf-23f22da1aba1">  

**Download :**  
-	[Download Link here](https://drive.google.com/file/d/1hDoKRjrKDnP5lGk1c1pXN73kgdZN4TGv/view?usp=sharing)
<br>
-	For more information, please visit our github page (경로 추가)

**Release note :**  

|Ver|   Date   |
|:-:|:--------:|
|1.0|2024.04.25|  

TOPST team is also preparing other official OS versions.  
For information on releases of other OS, please refer to the TOPST community.  
<br/>

## 6.2 Firmware upload to D3-G
Run “fwdn_ubuntu.batch” file. 
Refer to Section 5 to upload the Ubuntu image to the D3-G board.
After FWDN is completed, remove the USB Type-C cable from the FWDN port and remove the power cable. 
<br/>

## 6.3 Resize eMMC storage (Only D3-G)
When you log in after booting the board, you must resize the eMMC storage first.
Follow the steps below for eMMC Storage resizing.

1. To resize partitions by modifying size and layout on the disk, use the following command.
     ```
     $ parted
     ```

2. Extend GUID Partition Table(GPT). 
    ```
    $ rescue
    $ Fix 
    $ 0 
    $ 100%
    ```
3. Check that ext4 is partition by using the p (print) 
   ```
   $ p
   ```
4. Resize partition 4
    ```
    $ resizepart 4
    $ Yes
    $ 100%
    ```
5. Reboot 
6. Resize the ext4 filesystem on partition 4.
    ```
    $ resize2fs /dev/mmcblk0p4
    ```
7. Check the changed partition size by using the following command.
   ```
   $ df -h
   ```

You can confirm that the available space is 27GB after resizing.
<br/><br/>

# 7. References
- Contact TOPST for more details: topst@topst.ai

**Note:** Reference documents can be provided whenever available, depending on the terms of a contract. If the reference
documents are unavailable, the contents directly related to your development can be guided.
