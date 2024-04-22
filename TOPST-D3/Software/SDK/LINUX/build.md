# 2. Build Guide

<br/><br/>

## 2.1 TOPST D3 Linux SDK Build Prepration

TOPST D3 Linux SDK is based on Yocto Project 3.1 Dunfell. Therefore, the Yocto Project environment must be set on the host PC to use TOPST D3 Linux SDK. To download SDK, source-mirror, and tools, you must install utilities.  

<br/><br/>

## 2.2 Yocto Project  

The Yocto Project is an open source project focuses on embedded Linux development.  
It uses a combination of Open Embedded project, which is Poky, and ***bitbake*** as the build system to make Linux images.  
By using Yocto Project, you can simultaneously build the bootloader, kernel, and rootfs.  

<br/><br/>

## 2.3 Task Process

Figure 2.1 shows the task process of Yocto Project. You can download source from upstream based on metadata and build it. After the build is completed, package, image, and SDK are provided as results.

<p align="center">
    <img src="https://github.com/Topst-Dev/Documentation/assets/144076415/daa02968-b0b5-4ff2-8dd0-65edd6393f45" width="750" height="400">
</p>
<p align="center"><strong>Figure 2.1 Yocto Project Task Process</strong></p>

There is one ways to download and build TOPST D3 Linux SDK as follows:

- Manual operation


<br/><br/>

### 2.4.2 Composition of TOPST D3 SDK

<br/>

<table align="center">
  <tr>
    <th colspan="3">File</th>
    <th>Description</th>
  </tr>
  <tr>
    <td colspan="3">easy-setup.sh</td>
    <td>Python script to automatically download and build the SDK</td>
  </tr>
  <tr>
    <td colspan="3">stitch-fai.sh</td>
    <td>Script for making fai image(minimal + GStreamer + Qt)</td>
  </tr>
  <tr>
    <td rowspan="7">tools</td>
    <td colspan="2">README.md</td>
    <td rowspan="7">Tools related build</td>
  </tr>
  <tr>
    <td colspan="2">easy-setup.sh</td>
  </tr>
  <tr>
    <td colspan="2">mktcimg</td>
  </tr>
  <tr>
    <td colspan="2">stitch-fai.sh</td>
  </tr>
  <tr>
    <td colspan="2">fwdn</td>
  </tr>
  <tr>
    <td colspan="2">partition.dual.list</td>
  </tr>
  <tr>
    <td colspan="2">partition.single.list</td>
  </tr>
  <tr>
    <td rowspan="14">yocto</td>
    <td colspan="2">poky</td>
    <td>Yocto Project 1.1 Dunfell build system</td>
  </tr>
  <tr>
    <td colspan="2">meta-arm</td>
    <td>Support Arm toolchain Layer</td>
  </tr>
  <tr>
    <td colspan="2">meta-qt5</td>
    <td>Support Qt5 5.6.3 Layer</td>
  </tr>
  <tr>
    <td colspan="2">meta-telechips-bsp</td>
    <td>Support Telechips BSP Layer</td>
  </tr>
  <tr>
  <tr>
    <td colspan="2">meta-gplv2</td>
    <td>Support packages to avoid GPLv3 license</td>
  </tr>
  <tr>
    <td rowspan="5">meta-telechips</td> 
    <td>meta-core</td>
    <td>Recipes that require modification from Open Source Software (OSS) used by Telechips TOPST D3 SDK or recipes that are not in Yocto Project 3.1</td>
  </tr>
  <tr>
    <td>meta-extra</td>
    <td>OSS Layer that is added by Telechips</td>
  </tr>
  <tr>
    <td>meta-qt5</td>
    <td>Support Qt5 to support Telechips GUI application</td>
  </tr>
  <tr>
    <td>meta-ivi</td>
    <td>Configuration package and example programs of In-vehicle Infotainment (IVI)</td>
  </tr>
  <tr>
    <td>meta-subcore</td>
    <td>Configuration package and example programs on sub-core</td>
  </tr>
  <tr>
    <td colspan="2">meta-topst</td>
    <td>Maincore recipe</td>
  </tr>  
  <tr>
    <td colspan="2">meta-topst-subcore</td>
    <td>Subcore recipe</td>
  </tr>
</table>

<br/>

### 2.4.1 Create and regist SSH Key

```
$ ssh-keygen
$ cat ~/.ssh/id_rsa.pub
ssh-rsa AAAA ... MYFI4PP8kik= ben@topst
```
<br/>

After you create SSH Key, register your SSH Key in [GITLAB](https://gitlab.com/-/user_settings/ssh_keys). 

<p algin="center"><img src="https://github.com/topst-development/Documentation/assets/161264431/1b888871-d8a7-4adb-9d33-d6c839168e00"></p>
<p align="center"><strong>Figure 2.2 Register SSH Key</strong></p>

<br/>

### 2.4.2 Create SSH config

```
$ vi ~/.ssh/config

Host gitlab.com
    User git
    IdentityFile ~/.ssh/id_rsa
    UpdateHostKeys yes
```
<br/>


### 2.4.3 Get TOPST-D3 with Git

```
$ mkdir topst
$ cd topst

$ repo init -u https://gitlab.com/topst.ai/manifests -m topst-d3-pre-v0.1.xml
Downloading Repo source from https://gerrit.googlesource.com/git-repo

... A new version of repo (2.45) is available.
... New version is available at: /home/ben/topst/.repo/repo/repo
... The launcher is run from: /usr/bin/repo
!!! The launcher is not writable.  Please talk to your sysadmin or distro
!!! to get an update installed.


Your identity is: Seonguk Nam <topstdeveloper@gmail.com>
If you want to change this, please re-run 'repo init' with --config-name

repo has been initialized in /home/ben/topst

$ repo sync

... A new version of repo (2.45) is available.
... New version is available at: /home/ben/topst/.repo/repo/repo
... The launcher is run from: /usr/bin/repo
!!! The launcher is not writable.  Please talk to your sysadmin or distro
!!! to get an update installed.

Fetching: 100% (9/9), done in 13.638s
Checking out: 100% (9/9), done in 0.510s
repo sync has finished successfully.
```

<br/>



### 2.4.4 Execute Build Script

```
$ ./easy-setup.sh 
[+] Please execute the following command to initiate the build process

	source yocto/poky/oe-init-build-env build-main
	bitbake topst

[!] Will you use subcore? (yes/no) no
```
```
$ source yocto/poky/oe-init-build-env build-main

### Shell environment set up for builds. ###

You can now run 'bitbake <target>'

Common targets are:
    core-image-minimal
    core-image-sato
    meta-toolchain
    meta-ide-support

TOPST common targets are:
    topst-minimal
    topst-multimedia    (minimal + GStreamer)
    topst               (minimal + GStreamer + Qt)

Other commonly useful commands are:
 - 'devtool' and 'recipetool' handle common recipe tasks
 - 'bitbake-layers' handles common layer tasks
 - 'oe-pkgdata-util' handles common target package tasks
Warning: source-mirror not exist!!
         The build to be slowler or fail because will be download source code from upstream before build.


$ bitbake topst
```
<br/>


### 2.5.5 Make FWDN Image

This option creates a binary into one image for TOPST D3 platform image. The following is a list of images that are created with this option.

<br/>

The output.fwdn.win.zip including “Output.fai” build image and fwdn tools is created in the following path:

- {TOPST_PATH}/

```
$ ./stitch-fai.sh -f
```

<br/><br/>

### 2.6 Composition of TOPST D3 Linux SDK

After autolinux build is completed, you can check the following items.

<br/>

<table align="center">
  <tr>
    <th></th>
    <th colspan="2">Item</th>
    <th colspan="1">Description</th>
  </tr>
  <tr>
    <td rowspan="13">poky</td>
    <td colspan="2">Meta</td>
    <td rowspan="3">Yocto Project 1.1 Dunfell build system</td>
  </tr>
  <tr>
    <td colspan="2">meta-poky</td>
  </tr>
  <tr>
    <td colspan="2">meta-yocto-bsp</td>
  </tr>
  <tr>
    <td colspan="2">meta-arm</td>
    <td>Support Arm toolchain Layer</td>
  </tr>
  <tr>
    <td colspan="2">meta-qt5</td>
    <td>Support Qt5 5.6.3 Layer</td>
  </tr>
  <tr>
    <td colspan="2">meta-gplv2</td>
    <td>Support packages to avoid GPLv3 license</td>
  </tr>
  <tr>
    <td colspan="2">meta-telechips-bsp</td>
    <td>Support Telechips BSP Layer</td>
  </tr>
  <tr>
    <td rowspan="5">meta-telechips</td>
    <td>meta-core</td>
    <td>Recipes that require modification from Open Source Software (OSS) used by Telechips TOPST D3 SDK or recipes that are not in Yocto Project 3.1</td>
  </tr>
  <tr>
    <td>meta-extra</td>
    <td>OSS Layer that is added by Telechips</td>
  </tr>
  <tr>
    <td>meta-qt5</td>
    <td>Support Qt5 to support Telechips GUI application</td>
  </tr>
  <tr>
    <td>meta-ivi</td>
    <td>Configuration package and example programs of In-vehicle Infotainment (IVI)</td>
  </tr>
  <tr>
    <td>meta-subcore</td>
    <td>Configuration package and example programs on sub-core</td>
  </tr>
  <tr>
    <td colspan="2">download_web.sh</td>
    <td>Script for downloading source-mirror, tools, and FWDN</td>
  </tr>
  <tr>
    <td  rowspan="3">boot-firmware</td>
    <td colspan="2">prebuilt</td>
    <td>Boot-firmware files<br>Tools to make images for boot-firmware<br>Each boot-firmware for TOPST</td>
  </tr>
  <tr>
    <td rowspan="2">tools</td>
    <td>fwdn</td>
    <td>FWDN execute file<br>VTC driver<br>Source code</td>
  </tr>
  <tr>
    <td>mktcimg</td>
    <td>mktcimg execute file source code</td>
  </tr>
  <tr>
    <td colspan="3">tools</td>
    <td><li>gcc-linaro-7.2.1-2017.11-x86_64_arm-eabi.tar.xz<li>x86_64-buildtools-extended-nativesdk-standalone-3.0+snapshot-20200315.sh<li>x86_64-buildtools-nativesdk-standalone-3.1.sh</td>
  </tr>
  <tr>
    <td colspan="2" rowspan="3">cr5-bsp</td>
    <td>scripts</td>
    <td>Debug script for JTAG debugger such as <strong>TRACE32</strong></td>
  </tr>
  <tr>
    <td>source</td>
    <td>Source code<li>app.drivers: Application drivers. These drivers do not access hardware directly.<li>app.sample: Sample applications<li>build: Build environment & utilities<li>core: Assembly core files<li>dev.drivers: Device drivers<li>os: Operating System<li>sal: System Adaptation Layer</td>
  </tr>
  <tr>
    <td>tools</td>
    <td>Tools for FWDN & FW upgrade</td>
  </tr>
</table>
