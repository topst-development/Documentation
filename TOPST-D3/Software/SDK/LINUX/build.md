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
    <th colspan="2">File</th>
    <th>Description</th>
  </tr>
  <tr>
    <td colspan="2">easy-setup.sh</td>
    <td>Python script to automatically download and build the SDK</td>
  </tr>
  <tr>
    <td colspan="2">stitch-fai.sh</td>
    <td>Document that describes <strong>autolinux</strong></td>
  </tr>
  <tr>
    <td rowspan="5">tools</td>
    <td>README.md</td>
    <td>Python class for SDK features</td>
  </tr>
  <tr>
    <td>easy-setup.sh</td>
    <td>File that defines supported common features</td>
  </tr>
  <tr>
    <td>mktcimg</td>
    <td>File that defines supported TOPST D3 SDK features</td>
  </tr>
  <tr>
    <td>partition.list</td>
    <td>File that defines supported TOPST D3 SDK features</td>
  </tr>
  <tr>
    <td>stitch-fai.sh</td>
    <td>File that defines supported TOPST D3 SDK features</td>
  </tr>
  <tr>
    <td rowspan="9">poky</td>
    <td>meta-arm</td>
    <td>Shell script to execute <strong>configure</strong> in <strong>autolinux</strong></td>
  </tr>
  <tr>
    <td>meta-qt5</td>
    <td>Shell script to execute <strong>BitBake</strong> in <strong>autolinux</strong></td>
  </tr>
  <tr>
    <td>meta-telechips-bsp</td>
    <td>Shell script to execute <strong>devtool</strong> in <strong>autolinux</strong></td>
  </tr>
  <tr>
  <tr>
    <td>meta-topst-subcore</td>
    <td>Shell script to execute <strong>BitBake</strong> in <strong>autolinux</strong></td>
  </tr>
  <tr>
    <td>meta-gplv2</td>
    <td>Shell script to execute <strong>BitBake</strong> in <strong>autolinux</strong></td>
  </tr>
  <tr>
    <td>meta-telechips</td>
    <td>Shell script to execute <strong>BitBake</strong> in <strong>autolinux</strong></td>
  </tr>
  <tr>
    <td>meta-topst</td>
    <td>Shell script to execute <strong>BitBake</strong> in <strong>autolinux</strong></td>
  </tr>
  <tr>
    <td>poky</td>
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
$ ./autolinux -c make_fai

Read configuration from autolinux.config

Loading cache: 100% |#############################################################| Time: 0:00:00

Loaded 1775 entries from dependency cache.

Parsing recipes: 100% |###########################################################| Time: 0:00:01

Parsing of 1119 .bb files complete (1113 cached, 6 parsed). 1781 targets, 271 skipped, 0 masked, 0 errors.

NOTE: Resolving any missing task queue dependencies

Build Configuration:

BB_VERSION           = "1.46.0"

BUILD_SYS            = "x86_64-linux"

NATIVELSBSTRING      = "universal"

TARGET_SYS           = "aarch64-telechips-linux"

MACHINE              = "tcc8050-main"

DISTRO               = "poky-telechips-systemd"

DISTRO_VERSION       = "3.1.15"

TUNE_FEATURES        = "aarch64 cortexa72 crc crypto"

TARGET_FPU           = ""

LINUX_VERSION        = "5.4.159"

KBUILD_DEFCONFIG     = "tcc805x_linux_ivi_defconfig"

TCMODE               = "default"

INVITE_PLATFORM      = " qt-examples with-subcore support-4k-video network qt5 qt5/wayland drm network qt5/wayland micom fw-update genivi drm"

IMAGE_FEATURES       = " debug-tweaks ssh-server-openssh tools-debug eclipse-debug"

SDKIMAGE_FEATURES    = "dev-pkgs"

GCCVERSION           = "arm-9.2"

GLIBCVERSION         = "2.31%"

meta

meta-poky

meta-gplv2           = "HEAD:30fd0418f476edce3aa62fde66ed9c1de8926c8b"

meta-arm-toolchain   = "HEAD:1cfb0a1d773dd6eac3f387fd68ded7c907402d08"

meta-telechips-bsp   = "HEAD:e0642c6a1abc62fea568acc1c5880370310ecc9a"

meta-qt5             = "HEAD:e3c49254dfa17fe2ebd3367a2adc7bf6016d718c"

meta-core

meta-extra

meta-qt5

meta-micom           = "HEAD:f9fe4aacace14edba13952abc324e5c624be74a4"

meta-update          = "HEAD:db8b3a0828982aec33d09c52e03849bf0a4e100d"

meta-ivi

meta-genivi          = "HEAD:1f1a669114ebe05c7863f52d6314bc64fa770c0a"

meta-mingw           = "HEAD:f9fe4aacace14edba13952abc324e5c624be74a4"

NOTE: Tainting hash to force rebuild of task /poky/meta-telechips/meta-ivi/recipes-applications/images/automotive-linux-platform-image.bb, do_make_fai

WARNING: /poky/meta-telechips/meta-ivi/recipes-applications/images/automotive-linux-platform-image.bb:do_make_fai is tainted from a forced run

Initialising tasks: 100% |########################################################| Time: 0:00:01

Sstate summary: Wanted 3 Found 1 Missed 2 Current 36 (33% match, 94% complete)

NOTE: Executing Tasks

NOTE: Tasks Summary: Attempted 299 tasks of which 282 didn't need to be rerun and all succeeded.

NOTE: Writing buildhistory

NOTE: Writing buildhistory took: 1 seconds

Summary: There was 1 WARNING message shown.

~/build/TOPST/boot-firmware/tools/snor_mkimage ~/build/TOPST

Get r5_fw.rom

make snor image ..................

MCERT file: (../../prebuilt/mcert.bin)

HSM binary file: (../../prebuilt/hsm.cs.bin)

R5-BL1 binary file: (../../prebuilt/r5_bl1-snor.rom)

update binary file: (../../prebuilt/r5_sub_fw.rom)

MICOM binary file: (./r5_fw.rom)

SNOR ROM size: (4 MByte)

R5 UART port enable: (0)

R5 UART port for debug: (14)

Output file: (../../../build/tcc8050-main/tmp/deploy/fwdn/cr5_snor.rom)

<<SNOR_MAP: 0x00002000 ++0x00002000>>

[Make SFMC Read CMD Header...]

Header Size: 8192 byte

(0) FAST READ CMD Set for Chipboot (SPI)

Code:        0x000000E0

Timing:      0x00140300

Delay_s:     0x00000500

Dc_clk:      0x00000000

Run_mode:    0x00000011

Read_cmd:    0x840000EB 0x4A000001 0x86000000 0x46002000 0x2A000000

CMD CRC:     0x8E83D588

CMD address: 0x00002000

write_sfmc_init_header - success

<<SNOR_MAP: 0x00004000 ++0x00002000>>

[Write Master Certificate...]

write_master_certificate - success

<<SNOR_MAP: 0x00006000 ++0x00010000>>

[Write HSM F/W Image ...]

write_hsm_image - success

<<SNOR_MAP: 0x00016000 ++0x00100000>>

[Write R5-BL1 Image ...]

write_r5_bl1_image - success

<<SNOR_MAP: 0x00116000 ++0x00010000>>

[Write Micom SubFW Image ...]

MICOM Sub f/w size: 0x7a00

MICOM Sub f/w target addr: 0x00116200

write_micom_sub_fw_image - success

<<SNOR_MAP: 0x001ff000 ++0x00200000>>

[Write Secure Micom FW Image ...]

MICOM ROM size: 0x6fc00

<<SNOR_MAP: 0x00000000 ++0x00002000>>

[Make SNOR ROM Header...]

SNOR ROM Header CRC: 0x91DEA89B

write_rom_header - success

SNOR ROM Header CRC: 0x5B90D383

write_rom_header - success

Total Image Size: 4194304 byte

create_final_rom - success

~/{YOURPATH}

=================================================================================

FWDN Path : /build/tcc8050-main/tmp/deploy/fwdn

FWDN tool PATH : /boot-firmware/tools/fwdn

=================================================================================

Time taken in 0:00:35.981413
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
