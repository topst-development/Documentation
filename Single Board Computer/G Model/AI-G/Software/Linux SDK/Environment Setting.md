# 1. Introduction

This document provides guidelines for building the TOPST AI-G SDK, including setting up the host environment, building the SDK, using the firmware downloader, connecting the AI-G with a PC

This document includes information on the following: 
- Setting Host Environment  
- Image Build Guide  
- Firmware Download Guide 
- Connecting the AI-G with a PC
<br/><br/>

# 2. Setting Host Environment (Windows)
This chapter provides instructions on how to set up the host PC environment, with separate guides for setting up on Windows PC and Ubuntu PC.
<br>

## 2.1 Windows Environment 
This document provides instructions on how to set up WSL (Windows Subsystem for Linux) to use Linux on a Windows PC.
Since TOPST AI-G Linux SDK is based on the Yocto Project, Linux version of TOPST AI-G SDK follows the Yocto project.
You can install another version of Linux, but in this document, TOPST AI-G Linux SDK is described based on Ubuntu 22.04.
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
4. Set WSL 2 to the default version
    ```
    wsl --set-default-version 2
    ```
5. Search for Ubuntu 22.04.3 LTS in Microsoft Store and download it.

    * If you need to download the Linux kernel update package, download the latest package [here](https://learn.microsoft.com/ko-kr/windows/wsl/install-manual).

6. You may choose any user name during the Ubuntu installation

<br/><br/>


### 2.1.2 Accessing Ubuntu via WSL2
Open the Windows Command Prompt and enter the following command to access Ubuntu. When you access Ubuntu, it starts in the /mnt/c/Users/[user name] directory by default.
```
wsl  // access ubuntu 
ls   // check contents in your directory
```
Refer to the figure 1.1 below to check the result (may vary depending on the user).
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20AI-G/Software/Linux%20SDK/1.%20wsl%20linux.png" width="500"></p>
<p align="center"><strong>Figure 1 WSL2 Screenshot </strong></p>

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

<br/>

### 2.1.4 Install Utilities 

Install the utilities at once. To use Yocto Project, the following
utilities must be installed on Host PC(individual computer or development server).

Use the following command to install Utilities.

```
$ sudo apt-get install -y gawk wget git diffstat unzip texinfo gcc-multilib build-essential chrpath

$ sudo apt-get install -y socat cpio python3 python3-pip python3-pexpect xz-utils debianutils

$ sudo apt-get install -y iputils-ping python3-git python3-jinja2 libegl1-mesa libsdl1.2-dev pylint

$ sudo apt-get install -y xterm zstd ncftp curl git-lfs vim zip
```

<br/>

### 2.1.5 Install Repo

You can download TOPST AI-G SDK through Android Repo.  
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
<br/>

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

Install the utilities at once. To use Yocto Project, the following utilities must be installed on Host PC(individual computer or development server).

Use the following command to install Utilities.

```
$ sudo apt-get install -y gawk wget git diffstat unzip texinfo gcc-multilib build-essential chrpath

$ sudo apt-get install -y socat cpio python3 python3-pip python3-pexpect xz-utils debianutils

$ sudo apt-get install -y iputils-ping python3-git python3-jinja2 libegl1-mesa libsdl1.2-dev pylint

$ sudo apt-get install -y xterm zstd ncftp curl git-lfs vim zip
```

<br/>

### 2.2.4 Install Repo

You can download TOPST AI-G SDK through Android Repo.  
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
This section provides guidance based on the Ubuntu OS installed on the host PC (regardless of whether it is WSL or a local Ubuntu installation). The image to be uploaded to the AI-G is built using the Yocto Project, and therefore the process must be carried out in the Ubuntu environment.

<br/>

## 3.1 SDK Build Prepration

TOPST AI-G SDK is based on Yocto Project 4.0 kirkstone. Therefore, the Yocto Project environment must be set on the host PC to use TOPST AI-G SDK. To download SDK, source-mirror, and tools, you must install utilities. To build the image smoothly, the user's PC must have **at least 60 GB of available storage** and **a minimum of 16 GB of RAM**.

<br/>

## 3.2 Yocto Project

The Yocto Project is an open-source project that focuses on embedded Linux development. 
It uses a combination of Poky, which is a part of the Open Embedded project, and bitbake as the build system to make Linux images. 
By using Yocto Project, you can simultaneously build the bootloader, kernel, and rootfs. 

<br/>

## 3.3 Task Process of Yocto Project

Figure 2 shows the task process of the Yocto Project. You can download the source code from upstream repositories based on metadata and then build it. After the build is completed, package, image, and SDK are provided as results. 


<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20AI-G/Software/Linux%20SDK/2.%20Yocto%20Project.png" ></p>

<p align="center"><strong>Figure 2 Yocto Project Task Process</strong></p>

<br/>

## 3.4 Composition of TOPST SDK

The following are the components of the Yocto Project we have configured. Table 1 shows composition of TOSPT AI-G SDK.

<br/>

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
      <td colspan="3"style="text-align: center; vertical-align: middle;">fwdn_v8_ai-g</td>
    </tr>
    <tr>
      <td colspan="3"style="text-align: center; vertical-align: middle;">fwdn_v8</td>
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



## 3.5 Ready to build
The following sections provide instructions on how to configure the Yocto Project to build the AI-G image.

<br/>

### 3.5.1 Set User Email and User Name in .gitconfig
To download TOPST AI-G from the TOSPT official git, configure your email and name.
1. Enter the following command.
```
vi ~/.gitconfig
```
2. Enter the following information
```
    email = User email
    name = User name
```

### 3.5.2 Get TOPST AI-G with Git

```
$ mkdir topst-sdk
$ cd topst-sdk

$ repo init -u git@gitlab.com:topst-private-release/manifests.git -m linux_yp4.0_topst_1.0.0.xml

Downloading Repo source from https://gerrit.googlesource.com/git-repo

... A new version of repo (2.54) is available.
... New version is available at: /home/topst/topst-sdk/.repo/repo/repo
... The launcher is run from: /usr/bin/repo
!!! The launcher is not writable.  Please talk to your sysadmin or distro
!!! to get an update installed.


Your identity is: TopstDeveloper <topstdeveloper@gmail.com>
If you want to change this, please re-run 'repo init' with --config-name

repo has been initialized in /home/topst/topst-sdk


$ repo sync

... A new version of repo (2.54) is available.
... New version is available at: /home/topst/topst-sdk/.repo/repo/repo
... The launcher is run from: /usr/bin/repo
!!! The launcher is not writable.  Please talk to your sysadmin or distro
!!! to get an update installed.

Fetching: 100% (14/14), done in 32.836s
boot-firmware_ai-g: Shared project bsp/boot-firmware found, disabling pruning.
fwdn_v8: Shared project tools/fwdn_v8 found, disabling pruning.
Checking out:  57% (8/14), done in 0.764s
Checking out:  42% (6/14), done in 0.344s
repo sync has finished successfully.
```
<br/><br/>

## 3.6 Execute Build Script  
If you run ./easy-setup_ai-g.sh script, you can see the following screen. 


Caution: If you re-run ./easy-setup_ai-g.sh, be careful as the built sources will be deleted if you select yes. 

```
$ ./easy-setup_ai-g.sh
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

- {TOPST_PATH}/build/ai-g-topst/tmp/deploy/images/ai-g-topst-main

```
topst-build.sh is a shell script that sets up the core environment required to build TOPST images for D3-G and AI-G boards. Execute the following commands. By selecting option 1, you are now ready to install the main OS on the AI-G.

$ . poky/meta-topst/topst-build.sh

Choose MACHINE
  1. ai-g-topst
  2. d3-g-topst-main
  3. d3-g-topst-sub
  4. d5-g-topst-main
  5. d5-g-topst-sub
select number(1-5) => 1
machine(ai-g-topst) selected.
You had no conf/local.conf file. This configuration file has therefore been
created for you from /home/topst/topst-sdk/poky/meta-topst/template/ai-g-topst/local.conf.sample
You may wish to edit it to, for example, select a different MACHINE (target
hardware). See conf/local.conf for more information as common configuration
options are commented.

You had no conf/bblayers.conf file. This configuration file has therefore been
created for you from /home/topst/topst-sdk/poky/meta-topst/template/ai-g-topst/bblayers.conf.sample
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
    telechips-topst-ai-image

    meta-toolchain-topst(Application Development Toolkit)


You can also run generated TOSPT images on TOPST board

Other commonly useful commands are:
 - 'devtool' and 'recipetool' handle common recipe tasks
 - 'bitbake-layers' handles common layer tasks
 - 'oe-pkgdata-util' handles common target package tasks

```


Now, you can build AI-G image following command. 

```
$ bitbake telechips-topst-ai-image
```

<br/>

## 3.7 Make FWDN Image

This option combines binaries into an image for the TOPST AI-G platform.  

The “output.fwdn.zip” including the output.fai build image and FWDN tool is created in the following path: 

- ~/topst-sdk/

```
$ cd ~/topst-sdk/ && \ 

$ ./stitch-fai_ai-g.sh -f
```
If you see the following log, it means the “output.fwdn.zip” file is created. 
```
$ ls
output_nd.fwdn.zip  boot-firmware_d5-g  easy-setup_d3-g.sh  mktcimg             stitch-fai_d3-g.sh
boot-firmware_ai-g  build               fwdn_v8             poky                tools
boot-firmware_d3-g  easy-setup_ai-g.sh  fwdn_v8_ai-g        stitch-fai_ai-g.sh
```
<br/>

```
$ bitbake telechips-topst-ai-image -f -c make_fai

Loading cache: 100% |#############################################################################################| Time: 0:00:00
Loaded 3949 entries from dependency cache.
Parsing recipes: 100% |###########################################################################################| Time: 0:00:03
Parsing of 2512 .bb files complete (2511 cached, 1 parsed). 3950 targets, 478 skipped, 0 masked, 0 errors.
WARNING: No recipes in default available for:
  /home/eadweard/topst-sdk/poky/meta-topst/recipes-browser/cog/cog_0.16.%.bbappend
NOTE: Resolving any missing task queue dependencies

Build Configuration:
BB_VERSION           = "2.0.0"
BUILD_SYS            = "x86_64-linux"
NATIVELSBSTRING      = "universal"
TARGET_SYS           = "aarch64-telechips-linux"
MACHINE              = "ai-g-topst"
DISTRO               = "poky-telechips-systemd"
DISTRO_VERSION       = "4.0.17"
TUNE_FEATURES        = "aarch64 armv8a crc cortexa53"
TARGET_FPU           = ""
LINUX_VERSION        = "5.10.223"
KBUILD_DEFCONFIG     = "tcc750x_defconfig"
IMAGE_FEATURES       = " debug-tweaks ssh-server-openssh package-management"
GCCVERSION           = "arm-11.2"
GLIBCVERSION         = "2.35"
TOPST_FEATURES       = " multimedia network pcie-host camera display"
meta
meta-poky            = "HEAD:6d1a878bbf24c66f7186b270f823fcdf82e35383"
meta-gplv2           = "HEAD:d2f8b5cdb285b72a4ed93450f6703ca27aa42e8a"
meta-arm-toolchain   = "HEAD:d7b7b6fb6c7c5545e718e44f38853d1718ce5446"
meta-oe
meta-python
meta-networking      = "HEAD:8bb16533532b6abc2eded7d9961ab2a108fd7a5b"
meta-topst-bsp       = "HEAD:8d7785a718d887ee77e38e40c357185e6a5b8357"
meta-topst           = "HEAD:15cf8d6b41b6921adf17d7bc6b05ab156c91b56a"

NOTE: Tainting hash to force rebuild of task /home/eadweard/topst-sdk/poky/meta-topst/recipes-telechips-topst/images/telechips-topst-ai-image.bb, do_make_fai
WARNING: /home/eadweard/topst-sdk/poky/meta-topst/recipes-telechips-topst/images/telechips-topst-ai-image.bb:do_make_fai is tainted from a forced run
Initialising tasks: 100% |########################################################################################| Time: 0:00:02
Sstate summary: Wanted 151 Local 151 Mirrors 0 Missed 0 Current 1333 (100% match, 100% complete)
NOTE: Executing Tasks
NOTE: Tasks Summary: Attempted 3570 tasks of which 3569 didn't need to be rerun and all succeeded.
NOTE: Writing buildhistory
NOTE: Writing buildhistory took: 2 seconds

Summary: There were 2 WARNING messages.


$ ls /build/ai-g-topst/tmp/deploy/fwdn
boot-firmware   SD_Data.fai  SD_Data.gpt.back
partition.list  SD_Data.gpt  SD_Data.gpt.prim


```

Finally, you can check **'SD_Data.fai'**.

<br/><br/>

# 4. Firmware Download

This chapter describes how to download ***FWDN*** to the TOPST AI-G and login the Linux console.  
The ***FWDN V8*** is a PC tool for downloading firmware in Windows 10(11) 64-bit and Linux environments. This chapter describes the case of downloading in Windows and Linux environments.

## 4.1 Firmware Download Sequence

The downloading sequence of ***FWDN*** is as follows:

1. Set the boot mode switch to USB boot mode.
2. Open Windows prompt or Linux console and test ***FWDN V8***.
3. Connect ***FWDN V8*** to board.
4. Download fai file.

<br/>

## 4.2 Connect TOPST AI-G and Host PC with USB Boot 

You can transfer the built image to TCC750x by using FWDN. TCC750x provides FWDN by using Ethernet and UART. 

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20AI-G/Software/Linux%20SDK/3.%20connect%20host%20pc%20to%20topst%20ai-g.png" ></p>
<p align="center"><strong>Figure 6 Connection between Host PC and TOPST AI-G for FWDN</strong></p>

To use FWDN V8, connect the TOPST AI-G to the Host PC as follows: 

1. Check that VTC driver is installed on the Host PC. If the VTC driver is not installed, install it as shown in Chapter 4.2.1.  

2. Prepare one USB Type-C cable and one Ethernet Cable. 

3. To enter USB Boot mode, connect the USB Type-C cable to the USB Type-C FWDN Port on the TOPST AI-G and the Host PC. 

4. Connect the Ethernet Cable (RJ45) to the Ethernet port on the TOPST AI-G and the Host PC. 

5. Connect the power cable to the TOPST AI-G while pressing the FWDN switch. 

<br/>

### 4.2.1 How to install VCP Driver

Install the Vendor Telechips Certification (VTC) driver (found on [telechips driver](https://drive.google.com/file/d/1muQnY8kuKxDsy3p3FUiQqcG34Zjk-mnR/view?usp=sharing)) on the host PC by running as administrator. When you connect the USB in the FWDN mode as shown above, the Telechips VTC USB driver is set as shown in the Figure 4

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20AI-G/Software/Linux%20SDK/4.%20VTC.png" width="550"></p>
<p align="center"><strong>Figure 7 Check COM Port</strong></p>
<br/>

### 4.2.2 Connect Ethernet and Uart Port Between TOPST AI-G And Host PC

Host PC Network Configuration 

Control Panel → Network and Internet → Network Connectivity → Set Ethernet device properties for FWDN 
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20AI-G/Software/Linux%20SDK/5.%20network_setting.png"></p>
<p align="center"><strong>Figure 8 Setting Ethernet Device Properties for FWDN</strong></p>
<br/><br/>

## 4.3 Ready to Download FWDN
Before executing FWDN, you must first transfer the image and FWDN tool you created after the build from Ubuntu (WSL2) to the Windows Environment. 

1. Unzip "output_nd.fwdn.zip"
```
$ cd ~/topst-sdk/ && \ 
$ mkdir images && \ 
$ mv ./output_nd.fwdn.zip ./images && \ 
$ cd images && \ 
$ unzip output_nd.fwdn.zip &&
```

2. Copy "images" folder to Windows C drive. 
```
$ cd .. && \ 
$ cp -r ./images /mnt/c/ 
```
<br/>

## 4.4 FWDN in Windows Environment
1. Execute Windows PowerShell and go to “C:\images”.  
```
$ cd C:\images 
```
2. Enter .\fwdn_nd.bat command to start the firmware download. The “fwdn_nd.bat” is an executable file that automatically downloads firmware by using FWDN V8. 

```
./fwdn_nd.bat
```

<br/>

## 4.5 Execute FWDN in Linux Environment 

In a Linux environment, you can download TOPST AI-G image by entering the following command. 

```
./fwdn.sh 
```
After FWDN is completed, remove the USB Type-C cable from the FWDN port and remove the power cable. 


<br/>


# 5. Connecting the AI-G with a host PC
This chapter provides instructions on how to set up the host PC environment, with separate guides for setting up on Windows PC and Ubuntu PC.
<br/>

## 5.1 AI-G Connection with UART 

Perform the following steps and verify that the firmware download is successfully completed by using the UART connection. 

1. Install the serial port driver (CP210x Universal Windows Driver) and PL2303_prolific driver in the Windows environment. (CP210x Universal Windows Driver: Download link, PL2303_prolific Driver: Download link) 

2. Install a terminal emulator such as Tera Term or PuTTY. 
3. Connect the Host PC and UART Pin on the TOPST AI-G. Use a USB to TTL Cable. 
4. Connect the black cable to GND pin. 
5. Connect the RXD cable to TX pin of A72 UART pins and TXD cable to RX pin of UART pins. 

 
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20AI-G/Software/Linux%20SDK/6.%20connetc%20host%20pc%20to%20ai-g%20with%20uart%20cable.png"></p>
<p align="center"><strong>Figure 9 UART Connection with host PC</strong></p>  


The figure 10 below shows a successful login.  
Both the username and password for login are set to **root**.

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20AI-G/Software/Linux%20SDK/7.%20connenct%20screen.png" width="550"></p>
<p align="center"><strong>Figure 10 Connected Screen (ID and Password are topst)</strong></p>  





