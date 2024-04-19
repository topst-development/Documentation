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
    <td>Document that describes <strong>autolinux</strong></td>
  </tr>
  <tr>
    <td rowspan="5">tools</td>
    <td colspan="2">README.md</td>
    <td>Python class for SDK features</td>
  </tr>
  <tr>
    <td colspan="2">easy-setup.sh</td>
    <td>File that defines supported common features</td>
  </tr>
  <tr>
    <td colspan="2">mktcimg</td>
    <td>File that defines supported TOPST D3 SDK features</td>
  </tr>
  <tr>
    <td colspan="2">partition.list</td>
    <td>File that defines supported TOPST D3 SDK features</td>
  </tr>
  <tr>
    <td colspan="2">stitch-fai.sh</td>
    <td>File that defines supported TOPST D3 SDK features</td>
  </tr>
  <tr>
    <td rowspan="14">poky</td>
    <td colspan="2">meta-arm</td>
    <td>Shell script to execute <strong>configure</strong> in <strong>autolinux</strong></td>
  </tr>
  <tr>
    <td colspan="2">meta-qt5</td>
    <td>Support Arm toolchain Layerin <strong>autolinux</strong></td>
  </tr>
  <tr>
    <td colspan="2">meta-telechips-bsp</td>
    <td>Support Telechips BSP Layer</td>
  </tr>
  <tr>
  <tr>
    <td colspan="2">meta-topst-subcore</td>
    <td>Shell script to execute <strong>BitBake</strong> in <strong>autolinux</strong></td>
  </tr>
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
    <td>Shell script to execute <strong>BitBake</strong> in <strong>autolinux</strong></td>
  </tr>
  <tr>
    <td colspan="2">poky</td>
    <td>Shell script to execute <strong>BitBake</strong> in <strong>autolinux</strong></td>
  </tr>
    
</table>

<br/>


### 2.4.1 Get TOPST-D3 with Git

```
$ mkdir topst
$ cd topst
$ repo init -u https://gitlab.com/topst.ai/manifests -m topst-d3-pre-v0.1.xml
$ repo sync
```

<br/>



### 2.4.3 Execute Build Script

```
$ ./easy-setup.sh 
[+] Please execute the following command to initiate the build process

	source yocto/poky/oe-init-build-env build-main
	bitbake topst

	or

	source yocto/poky/oe-init-build-env build-sub
	bitbake topst-subcore
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

You can also run generated qemu images with a command like 'runqemu qemux86'

Other commonly useful commands are:
 - 'devtool' and 'recipetool' handle common recipe tasks
 - 'bitbake-layers' handles common layer tasks
 - 'oe-pkgdata-util' handles common target package tasks
Warning: source-mirror not exist!!
         The build to be slowler or fail because will be download source code from upstream before build.


$ bitbake topst
```
<br/>


### 2.5.4 “Make fai” for Automotive Platform

This option creates a binary into one image for platform image. The following is a list of images that are created with this option.
<br/>

<table>
    <tr>
        <th rowspan="2">Command</th>
        <th colspan="4">Into SD Data.fai</th>
        <th rowspan="2">Description</th>
    </tr>
    <tr>
        <th>Core</th>
        <th>Bootloader</th>
        <th>Kernel</th>
        <th>File system</th>
    </tr>
    <tr>
        <td rowspan="2">make_fai</td>
        <td>Main (CA72)</td>
        <td rowspan="2">U-boot 2020.01</td>
        <td rowspan="2">5.4.159</td>
        <td>automotive-linux-platform-image</td>
        <td>ivi-image + demo applications</td>
    </tr>
    <tr>
        <td>Sub (CA53)</td>
        <td>telechips-subcore-image</td>
        <td>minimal root filesystem</td>
    </tr>
</table>  

<br/>

The “SD Data.fai” build image is created in the following path:

- {TOPST_PATH}/build/tcc8050-main/tmp/deploy/fwdn

```

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
