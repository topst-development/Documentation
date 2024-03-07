# 1 Build Guide

## 1.1 TOPST

is based on Yocto Project 3.1 Dunfell. Therefore, the Yocto Project environment must be set on the host PC to use TOPST D3 SDK. To download SDK, source-mirror, and tools, you must install utilities.

Figure 3.1 shows the task process of Yocto Project. You can download source from upstream based on metadata and perform build. After the build is completed, package, image, and SDK are provided as results.

<div style="display: flex; justify-content: center;">
    <img src="https://github.com/Topst-Dev/Documentation/assets/144076415/daa02968-b0b5-4ff2-8dd0-65edd6393f45" width="500" height="350" style="margin: auto;">
</div>
<p align="center"><strong>Figure 3.1 Yocto Project Task Process</strong></p>

There are two ways to download and build TOPST D3 SDK as follows:

- ***autolinux*** (python script to automatically download and build the SDK)
- Manual operation

However, this document only describes ***autolinux***.

### 1.1.1 Composition of TOPST

After TOPST is downloaded, you can check the following items.

|  | Item |  | Description |
| --- | --- | --- | --- |
| poky | Meta |  | Yocto Project 3.1 Dunfell build system |
|  | meta-poky |  |  |
|  | meta-yocto-bsp |  |  |
|  | meta-arm |  | Support Arm toolchain Layer |
|  | meta-qt5 |  | Support Qt5 5.6.3 Layer |
|  | meta-gplv2 |  | Support packages to avoid GPLv3 license |
|  | meta-telechips-bsp |  | Support Telechips BSP Layer |
|  | meta-telechips | meta-core | Recipes that require modification from Open Source Software (OSS) used by Telechips TOPST D3 SDK or recipes that are not in Yocto Project 3.1 |
|  |  | meta-extra | OSS Layer that is added by Telechips |
|  |  | meta-qt5 | Support Qt5 to support Telechips GUI application |
|  |  | meta-ivi | Configuration package and example programs of In-vehicle Infotainment (IVI) |
|  |  | meta-subcore | Configuration package and example programs on sub-core |
|  | download_web.sh |  | Script for downloading source-mirror, tools, and FWDN |
| boot-firmware |  | prebuilt | Boot-firmware files 
|   |   |   |Tools to make images for boot-firmware 
|   |   |   |Each boot-firmware for TOPST |
|  |  | fwdn | FWDN execute file 
|   |   |   |VTC driver 
|   |   |   |Source code |
|  |  | mktcimg | mktcimg execute file source code |
| tools |  |  |   -  gcc-linaro-7.2.1-2017.11-x86_64_arm-eabi.tar.xz
|   |   |   |-  x86_64-buildtools-extended-nativesdk-standalone-3.0+snapshot-20200315.sh
|   |   |   |-  x86_64-buildtools-nativesdk-standalone-3.1.sh |
| cr5-bsp |  | scripts | Debug script for JTAG debugger such as TRACE32 |
|  |  | source | Source code
|   |   |   |-  app.drivers: Application drivers. These drivers do not access hardware directly.
|   |   |   |-  app.sample: Sample applications
|   |   |   |-  build: Build environment & utilities
|   |   |   |-  core: Assembly core files
|   |   |   |-  dev.drivers: Device drivers
|   |   |   |-  os: Operating System
|   |   |   |-  sal: System Adaptation Layer |
|  |  | tools | Tools for FWDN & FW upgrade |

### 1.1.2 autolinux

***autolinux*** was developed by Telechips to make it easy to download and build SDK. ***autolinux*** does not provide all settings and functions, so you should set detailed configurations.

### 1.1.2.1 Get autolinux with Git

The following code shows how to get ***autolinux*** with Git.

```bash
$ git clone https://git.huconn.com/linux_ivi_mirror/script/build-autolinux.git topst

$ cd topst
```

---

### 1.1.2.2 Composition of autolinux

| File |  | Description |
| --- | --- | --- |
| autolinux |  | Python script to automatically download and build the SDK |
| README |  | Document that describes autolinux |
| classes | feature.py | Python class for SDK features |
|  | features/common.py | File that defines supported common features |
|  | features/ivi.py | File that defines supported TOPST D3 SDK features |
| doc | variable.txt | Document that describes the variables used in autolinux |
| script | build_configure.sh | Shell script to execute configure in autolinux |
|  | build_image.sh | Shell script to execute BitBake in autolinux |
|  | devtool.sh | Shell script to execute devtool in autolinux |
| template | sdk.py | File that defines supported SDKs, source mirror, and build tool paths |
|  | tcc805x_linux_ivi.py | File that defines supported machines and manifests for TOPST D3 SDK |

### 1.1.2.3 autolinux Usage

```bash
**$ ./autolinux --help**

usage: autolinux [-h] -c COMMAND [COMMAND ...] [-V] [-f FEATURES [FEATURES ...]] [-sf SUBFEATURES [SUBFEATURES ...]]

Linux SDK Configurations

optional arguments:

-h, --help            show this help message and exit

General Command:

-c COMMAND [COMMAND ...], --command COMMAND [COMMAND ...]

General Command to use autolinux(required option)

configure [option] [name]: setup the newer build environment

save [name] : save autolinux.config file to .config/

load [name] : load configure file from .config/

clean [option]: move current built files to recycle directory. recycle dir:build/delete

old : delete current built files and recycle directory.

all : Delete entire build directory including build history. After clean all, rebuilding for the first time has a long build time.

build [option]: build SDK Image, choose the name of the image to build

'args'    : extra command strings

Ex) autolinux -c build main

Ex) autolinux -c build main clean

Ex) autolinux -c build "linux-telechips -C compile"

Ex) autolinux -c build "linux-telechips -C clean"

sub 'args': building on sub-core, available only when the with-subcore option is enabled

Ex) autolinux -c build sub

Ex) autolinux -c build sub clean

Ex) autolinux -c build sub "linux-telechips -C compile"

Ex) autolinux -c build sub "linux-telechips -C clean"

cr5 'args': building on cr5-core, available only when the with-cr5core option is enabled

Ex) autolinux -c build cr5

Ex) autolinux -c build cr5 clean

devtool 'args' : devtool package to develop easily

Ex) autolinux -c devtool 'modify linux-telechips'

make_fai : make SDdata.fai for fwdn

fwdn : firmware download

info : show information of current configuration'

modify option: modify specific configure at current set-up

feature            : modify features

sub-feature        : modify subcore features

image              : modify image

-V, --version         print version and exit

Configuration Options:

-f FEATURES [FEATURES ...], --features FEATURES [FEATURES ...]

enter the feature list

ex) -f with-subcore gpu-vz meta-update

-sf SUBFEATURES [SUBFEATURES ...], --sub-features SUBFEATURES [SUBFEATURES ...]

enter the subfeature list

ex) -sf rvc gpu-vz meta-update
```

---

### 1.1.2.4 Download and Configure SDK

TOPST D3 SDK is downloaded at initial configuration.

You can set up the initial configuration by using a **configure** command. If you execute the **configure** command, the initial configuration is progressed as the following step.

**Note:** Each step is activated only when there is at least one selectable option.

The following configurations must be set:

- **Choose a core to build.**
- **Choose the features** to build.

When the configuration is completed, the setup is saved as “autolinux.config”.

```bash
**$ ./autolinux -c configure**

The command is configure or Add configuration options(sdk,core,manifest)

Configure Start

Choose a core to build

1.tcc8050-main

2.tcc8050-sub

**Choose core(1-2): 1**

Choose the Features at tcc8050-main

- 1. network Install network packages
- 2. ssh-server-openssh Install openssh with network packages
- 3. meta-micom Enable Micom
- 4. meta-update Enable Update
- 5. with-subcore Booting with sub-core
- 6. with-cr5core Booting with cr5-core
- 7. support-4k-video Support 4k Video Contents

0.Exit

**Choose Features enable/disable (1-7): 0**

Choose the Features at tcc8050-sub

- 1. meta-micom Enable Micom
- 2. meta-update Enable Update

0.Exit

**Choose Features enable/disable (1-2): 0**

Downloading Repo source from https://gerrit.googlesource.com/git-repo

Your identity is:

If you want to change this, please re-run 'repo init' with --config-name

repo has been initialized in PATH

If this is not the directory in which you want to initialize repo, please run:

rm -r .repo

and try again.

remote: Total 0 (delta 0), reused 0 (delta 0), pack-reused 0

Fetching: 100% (10/10), done in 6.387s

NOT Garbage collecting:   0% (0/10), done in 0.041s

Checking out: 100% (10/10), done in 1.438s

repo sync has finished successfully.

**Do you want to use sstate? (y/n) : y**

/poky/download_web.sh buildTools

Start buildtools downloading... Please wait !

~/tools ~/TOPST

/tools

tools

- -2022-10-14 11:20:04-- https://TOPST-dl.huconn.com/share/AP/tools/x86_64-buildtools-nativesdk-standalone-3.1.sh

Resolving TOPST-dl.huconn.com (TOPST-dl.huconn.com)... 119.201.71.25

Connecting to TOPST-dl.huconn.com (TOPST-dl.huconn.com)|119.201.71.25|:443... connected.

HTTP request sent, awaiting response... 200 OK

Length: 25682188 (24M) [application/octet-stream]

Saving to: 'x86_64-buildtools-nativesdk-standalone-3.1.sh'

x86_64-buildtools-native 100%[===============================>]  24.49M  49.5MB/s    in 0.5s

2022-10-14 11:20:04 (49.5 MB/s) - 'x86_64-buildtools-nativesdk-standalone-3.1.sh' saved [25682188/25682188]

- -2022-10-14 11:20:04-- https://TOPST-dl.huconn.com/share/AP/tools/x86_64-buildtools-extended-nativesdk-standalone-3.0+snapshot-20200315.sh

Resolving TOPST-dl.huconn.com (TOPST-dl.huconn.com)... 119.201.71.25

Connecting to TOPST-dl.huconn.com (TOPST-dl.huconn.com)|119.201.71.25|:443... connected.

HTTP request sent, awaiting response... 200 OK

Length: 48369100 (46M) [application/octet-stream]

Saving to: 'x86_64-buildtools-extended-nativesdk-standalone-3.0+snapshot-20200315.sh'

x86_64-buildtools-extend 100%[===============================>]  46.13M  50.4MB/s    in 0.9s

2022-10-14 11:20:05 (50.4 MB/s) - 'x86_64-buildtools-extended-nativesdk-standalone-3.0+snapshot-20200315.sh' saved [48369100/48369100]

- -2022-10-14 11:20:05-- https://TOPST-dl.huconn.com/share/AP/tools/gcc-linaro-7.2.1-2017.11-x86_64_arm-eabi.tar.xz

Resolving TOPST-dl.huconn.com (TOPST-dl.huconn.com)... 119.201.71.25

Connecting to TOPST-dl.huconn.com (TOPST-dl.huconn.com)|119.201.71.25|:443... connected.

HTTP request sent, awaiting response... 200 OK

Length: 274983024 (262M) [application/octet-stream]

Saving to: 'gcc-linaro-7.2.1-2017.11-x86_64_arm-eabi.tar.xz'

gcc-linaro-7.2.1-2017.11 100%[===============================>] 262.24M  49.2MB/s    in 5.5s

2022-10-14 11:20:11 (47.9 MB/s) - ‘gcc-linaro-7.2.1-2017.11-x86_64_arm-eabi.tar.xz’ saved [274983024/274983024]

~/TOPST

done

Install buildtools for CA72/CA53

Build tools installer version 3.1

=================================

You are about to install the SDK to "/TOPST/buildtools". Proceed [Y/n]? Extracting SDK...........done

Setting it up...done

SDK has been successfully set up and is ready to be used.

Each time you wish to use the SDK in a new shell session, you need to source the environment setup script e.g.

$ . /buildtools/environment-setup-x86_64-pokysdk-linux

Install buildtools for CR5

.

.

.

done

Enabled with-subcore, The autolinux script make new configuration files of Sub-core automatically

=================================================================================

SDK=tcc805x_linux_ivi

MANIFEST=tcc8050_linux_ivi_TOPST_0.1.0.xml

DATE=2022/04/08

MACHINE=tcc8050-main

VERSION=release

FEATURES=network,ssh-server-openssh,meta-micom,meta-update,with-subcore,with-cr5core,support-4k-video

SUBFEATURES=meta-micom,meta-update

=================================================================================

Time taken in 0:03:32.689284

**$ ls**

autolinux         boot-firmware  buildtools  cr5-bsp  poky    script    tools

autolinux.config  build          classes     doc      README  template
```

---

### 1.1.2.5 Build TOPST

You can use the **BitBake** command to build on per-target basis. These targets differ for each package that is included in the build.

| Command | Core | Created image |  |  | Description |
| --- | --- | --- | --- | --- | --- |
|  |  | Bootloader | Kernel | File system |  |
| main | Main (CA72) | U-Boot 2020.01 | 5.4.159 | automotive-linux-platform-image | ivi-image + demo applications |
| sub | Sub (CA53) |  |  | telechips-subcore-image | minimal root filesystem |
| ubuntu | Main (CA72) | - | - | ubuntu-image | Ubuntu 22.04 TLS |

In addition to the default image above, the image below is included in the system. If necessary, you can build with the below image.

See the following table for field methods.

| Core | File system | Description |
| --- | --- | --- |
| Main (CA72) | telechips-ivi-image-minimal | minimal root filesystem |
|  | telechips-ivi-image-multimedia | ivi-image-minimal + GStreamer |
|  | telechips-ivi-image | ivi-image-multimedia + Qt |
|  | automotive-linux-platform-image | ivi-image + demo applications |
| Sub (CA53) | telechips-subcore-image | minimal root filesystem |

If the environment for ***BitBake*** execution is not set up, run the command below

- Main core

```bash
$ source poky/oe-init-build-env build/tcc8050-main
```

---

- Sub-core

```bash
$ source poky/oe-init-build-env build/tcc8050-sub
```

---

If the environment is set up to run ***BitBake***, enter the command below to build the image.

The filesystem build image (.ext4) is created in the following path:

- {TOPST_PATH}/build/tcc8050-main/tmp/deploy/images/tcc8050-main

```bash
$ bitbake telechips-ivi-image-minimal

Loading cache: 100% |#####################################################################################################################################################| Time: 0:00:00

Loaded 1785 entries from dependency cache.

Parsing recipes: 100% |###################################################################################################################################################| Time: 0:00:00

Parsing of 1125 .bb files complete (1123 cached, 2 parsed). 1787 targets, 273 skipped, 0 masked, 0 errors.

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

INVITE_PLATFORM      = " with-subcore gpu-vz support-4k-video network v4l-utils dp2hdmi network qt5/wayland micom genivi drm"

IMAGE_FEATURES       = " debug-tweaks ssh-server-openssh tools-debug eclipse-debug"

SDKIMAGE_FEATURES    = "dev-pkgs"

GCCVERSION           = "arm-9.2"

GLIBCVERSION         = "2.31%"

meta

meta-poky

meta-gplv2           = "HEAD:4ffa4d710a84f38c6e77772c57ca5e5d11a68639"

meta-arm-toolchain   = "HEAD:1cfb0a1d773dd6eac3f387fd68ded7c907402d08"

meta-telechips-bsp   = "HEAD:963e80119e3537633c2455c2758ff9cd4cdad3df"

meta-qt5             = "HEAD:e3c49254dfa17fe2ebd3367a2adc7bf6016d718c"

meta-core

meta-extra

meta-qt5

meta-micom           = "HEAD:c32df1b739f9d6b02c31a0f0e80d5c43e827028d"

meta-update          = "HEAD:694c45c2b3d275326254be8daa9217b9096cd68d"

meta-ivi

meta-genivi          = "HEAD:bc3d2746144e98d72b1950e40a369050431ee86e"

meta-mingw           = "HEAD:c32df1b739f9d6b02c31a0f0e80d5c43e827028d"

Initialising tasks: 100% |################################################################################################################################################| Time: 0:00:00

Sstate summary: Wanted 132 Found 130 Missed 2 Current 878 (98% match, 99% complete)

NOTE: Executing Tasks

WARNING: telechips-ivi-image-minimal-1.0-r0 do_rootfs: [log_check] telechips-ivi-image-minimal: found 1 warning message in the logfile:

[log_check] Warning: truncating password to 8 characters

NOTE: Tasks Summary: Attempted 3399 tasks of which 3387 didn't need to be rerun and all succeeded.

NOTE: Writing buildhistory

NOTE: Writing buildhistory took: 1 seconds

Summary: There was 1 WARNING message shown.
```

---

Check the built filesystem image.

```bash
~/topst/build/tcc8050-main$ cd tmp/deploy/images/tcc8050-main/

~/topst/build/tcc8050-main/tmp/deploy/images/tcc8050-main$ ls

automotive-linux-platform-image-tcc8050-main-20230719075654.rootfs.ext4      automotive-linux-platform-image-tcc8050-main.ext4

automotive-linux-platform-image-tcc8050-main-20230719075654.rootfs.manifest  automotive-linux-platform-image-tcc8050-main.manifest

automotive-linux-platform-image-tcc8050-main-20230719075654.rootfs.squashfs  automotive-linux-platform-image-tcc8050-main.squashfs

automotive-linux-platform-image-tcc8050-main-20230719075654.testdata.json    automotive-linux-platform-image-tcc8050-main.testdata.json
```

---

Then, download the build filesystem image to the TOPST D3 (Open platform board). (Refer to Chapter 4.3.1.)

Enter the options below when downloading:

- Enter the part you want to install: all, main, sub, mcu, QUIT

    : **main**

- Enter the part you want to install on main-core?: all, bootloader, kernel, filesystem, dtb, home

    : **filesystem**

### 1.1.3 Optional Build

Each core can be built separately. If you enter the core name to build as the last parameter, an image of that core is created.

### 1.1.3.1 Main Core Build

As described in Chapter 3.1.2.5, the options below create the U-Boot, kernel, and automatic-linux-platform-image file system for the main core.

Refer to Chapter 4 for download instructions.

| Command | Core | Created image |  |  | Description |
| --- | --- | --- | --- | --- | --- |
|  |  | Bootloader | Kernel | File system |  |
| main | Main (CA72) | U-Boot 2020.01 | 5.4.159 | automotive-linux-platform-image | ivi-image + demo applications |

The main core build image is created in the following path:

- {TOPST_PATH}/build/tcc8050-main/tmp/deploy/images/tcc8050-main

```bash
$ ./autolinux -c build main

Read configuration from autolinux.config

NOTE: Your conf/bblayers.conf has been automatically updated.

Parsing recipes: 100% |###################################################################################################################################################| Time: 0:00:13

Parsing of 1125 .bb files complete (0 cached, 1125 parsed). 1787 targets, 273 skipped, 0 masked, 0 errors.

NOTE: Resolving any missing task queue dependencies

Build Configuration:

BB_VERSION           = "1.46.0"

BUILD_SYS            = "x86_64-linux"

NATIVELSBSTRING      = "ubuntu-20.04"

TARGET_SYS           = "aarch64-telechips-linux"

MACHINE              = "tcc8050-main"

DISTRO               = "poky-telechips-systemd"

DISTRO_VERSION       = "3.1.15"

TUNE_FEATURES        = "aarch64 cortexa72 crc crypto"

TARGET_FPU           = ""

LINUX_VERSION        = "5.4.159"

KBUILD_DEFCONFIG     = "tcc805x_linux_ivi_defconfig"

TCMODE               = "default"

INVITE_PLATFORM      = " with-subcore gpu-vz support-4k-video network v4l-utils dp2hdmi USB-WEBCAM USB-WiFi-MT7601U network qt5/wayland micom genivi drm"

IMAGE_FEATURES       = " debug-tweaks ssh-server-openssh tools-debug eclipse-debug"

SDKIMAGE_FEATURES    = "dev-pkgs"

GCCVERSION           = "arm-9.2"

GLIBCVERSION         = "2.31%"

meta

meta-poky

meta-gplv2           = "HEAD:4ffa4d710a84f38c6e77772c57ca5e5d11a68639"

meta-arm-toolchain   = "HEAD:1cfb0a1d773dd6eac3f387fd68ded7c907402d08"

meta-telechips-bsp   = "HEAD:9e1e25477b915c7fe71acc40b30a0d7d73f8f16d"

meta-qt5             = "HEAD:e3c49254dfa17fe2ebd3367a2adc7bf6016d718c"

meta-core

meta-extra

meta-qt5

meta-micom           = "HEAD:c32df1b739f9d6b02c31a0f0e80d5c43e827028d"

meta-update          = "HEAD:694c45c2b3d275326254be8daa9217b9096cd68d"

meta-ivi

meta-genivi          = "HEAD:e5f31f7583813022cbc140c60cf2e0178e92bdbe"

meta-mingw           = "HEAD:c32df1b739f9d6b02c31a0f0e80d5c43e827028d"

NOTE: Fetching uninative binary shim http://downloads.yoctoproject.org/releases/uninative/3.5/x86_64-nativesdk-libc-3.5.tar.xz;sha256sum=e8047a5748e6f266165da141eb6d08b23674f30e477b0e5505b6403d50fbc4b2 (will check PREMIRRORS first)

Initialising tasks: 100% |################################################################################################################################################| Time: 0:00:02

Sstate summary: Wanted 1847 Found 1779 Missed 68 Current 0 (96% match, 0% complete)

NOTE: Executing Tasks

WARNING: automotive-linux-platform-image-1.0-r0 do_rootfs: [log_check] automotive-linux-platform-image: found 1 warning message in the logfile:

[log_check] Warning: truncating password to 8 characters

NOTE: Tasks Summary: Attempted 5781 tasks of which 4430 didn't need to be rerun and all succeeded.

NOTE: Writing buildhistory

NOTE: Writing buildhistory took: 3 seconds

Summary: There was 1 WARNING message shown.

automotive-linux-platform-image building on tcc8050-main

=================================================================================

Built Path : /home/topst/build/tcc8050-main

=================================================================================
```

---

### 1.1.3.2 Sub-core Build

As described in Chapter 3.1.2.5, the options below create the u-boot, kernel, and telechips-subcore-image file system for the sub-core.

Refer to Chapter 4 for download instructions.

| Command | Core | Created image |  |  | Description |
| --- | --- | --- | --- | --- | --- |
|  |  | Bootloader | Kernel | File system |  |
| sub | Sub (CA53) | U-Boot 2020.01 | 5.4.159 | telechips-subcore-image | minimal root filesystem |

The sub-core build image is created in the following path:

- {TOPST_PATH}/build/tcc8050-sub/tmp/deploy/images/tcc8050-sub

```bash
$ ./autolinux -c build sub

Read configuration from autolinux.config

NOTE: Your conf/bblayers.conf has been automatically updated.

Parsing recipes: 100% |###################################################################################################################################################| Time: 0:00:13

Parsing of 1114 .bb files complete (0 cached, 1114 parsed). 1774 targets, 282 skipped, 0 masked, 0 errors.

WARNING: No recipes available for:

/home/topst/poky/meta-telechips/meta-subcore/recipes-kernel/linux-libc-headers/linux-libc-headers_4.14.bbappend

/home/topst/poky/meta-telechips/meta-subcore/recipes-str/tc-str-manager/tc-str-manager_1.%.bbappend

NOTE: Resolving any missing task queue dependencies

Build Configuration:

BB_VERSION           = "1.46.0"

BUILD_SYS            = "x86_64-linux"

NATIVELSBSTRING      = "ubuntu-20.04"

TARGET_SYS           = "aarch64-telechips-linux"

MACHINE              = "tcc8050-sub"

DISTRO               = "poky-telechips-systemd"

DISTRO_VERSION       = "3.1.15"

TUNE_FEATURES        = "aarch64 cortexa53 crc"

TARGET_FPU           = ""

LINUX_VERSION        = "5.4.159"

KBUILD_DEFCONFIG     = "tcc805x_a53_subcore_defconfig"

TCMODE               = "default"

INVITE_PLATFORM      = " gpu-vz qt-examples  qt5/eglfs micom"

IMAGE_FEATURES       = " debug-tweaks read-only-rootfs"

SDKIMAGE_FEATURES    = "dev-pkgs"

GCCVERSION           = "arm-9.2"

GLIBCVERSION         = "2.31%"

SUBCORE_APPS         = " rvc"

meta

meta-poky            = "HEAD:4ffa4d710a84f38c6e77772c57ca5e5d11a68639"

meta-qt5             = "HEAD:e3c49254dfa17fe2ebd3367a2adc7bf6016d718c"

meta-gplv2           = "HEAD:4ffa4d710a84f38c6e77772c57ca5e5d11a68639"

meta-arm-toolchain   = "HEAD:1cfb0a1d773dd6eac3f387fd68ded7c907402d08"

meta-telechips-bsp   = "HEAD:963e80119e3537633c2455c2758ff9cd4cdad3df"

meta-qt5

meta-core

meta-extra           = "HEAD:c32df1b739f9d6b02c31a0f0e80d5c43e827028d"

meta-subcore         = "HEAD:eaece0170244f5ed69bf35438a92fb6fd3cfddd7"

meta-micom           = "HEAD:c32df1b739f9d6b02c31a0f0e80d5c43e827028d"

meta-ivi             = "HEAD:bc3d2746144e98d72b1950e40a369050431ee86e"

meta-update          = "HEAD:694c45c2b3d275326254be8daa9217b9096cd68d"

Initialising tasks: 100% |################################################################################################################################################| Time: 0:00:01

Sstate summary: Wanted 1112 Found 1102 Missed 10 Current 0 (99% match, 0% complete)

NOTE: Executing Tasks

NOTE: Tasks Summary: Attempted 3748 tasks of which 2939 didn't need to be rerun and all succeeded.

NOTE: Writing buildhistory

NOTE: Writing buildhistory took: 2 seconds

Summary: There was 1 WARNING message shown.

telechips-subcore-image building on tcc8050-sub

=================================================================================

Built Path : /home/topst/build/tcc8050-sub

=================================================================================
```

---

### 1.1.3.3 MCU Build

The following is the image information that is generated during the build.

Refer to Chapter 4 for download instructions.

| Command | Core | Created image | Description |
| --- | --- | --- | --- |
| cr5 | MCU (R5) | Cr5_Snor.rom | MCU BSP Image (FreeRTOS) |

The MCU build image is created in the following path:

- {TOPST_PATH}/cr5-bsp/sources/build/tcc805x/gcc/tcc805x-freertos-debug

```bash
$ ./autolinux -c build cr5

Read configuration from autolinux.config

~/topst/cr5-bsp/sources/build/tcc805x/gcc ~/topst

compile: /home/topst/cr5-bsp/sources/app.sample/app.base/main.c

compile: /home/topst/cr5-bsp/sources/app.sample/app.can.demo/can_demo.c

compile: /home/topst/cr5-bsp/sources/app.sample/app.console/console.c

compile: /home/topst/cr5-bsp/sources/app.sample/app.fwug/fwug.c

compile: /home/topst/cr5-bsp/sources/app.sample/app.key/key_adc.c

compile: /home/topst/cr5-bsp/sources/app.sample/app.key/key_gpio.c

compile: /home/topst/cr5-bsp/sources/app.sample/app.key/key_i2c.c

compile: /home/topst/cr5-bsp/sources/app.sample/app.key/key.c

compile: /home/topst/cr5-bsp/sources/app.sample/app.system.monitoring/system_monitoring.c

compile: /home/topst/cr5-bsp/sources/app.sample/app.boot.ctrl/bootctrl.c

compile: /home/topst/cr5-bsp/sources/app.sample/app.reset.demo/reset_demo.c

compile: /home/topst/cr5-bsp/sources/app.sample/test.app.adc/adc_test.c

compile: /home/topst/cr5-bsp/sources/app.sample/test.app.dse/dse_test.c

compile: /home/topst/cr5-bsp/sources/app.sample/test.app.fmu/fmu_test.c

compile: /home/topst/cr5-bsp/sources/app.sample/test.app.gdma/gdma_test.c

compile: /home/topst/cr5-bsp/sources/app.sample/test.app.gic/gic_test.c

compile: /home/topst/cr5-bsp/sources/app.sample/test.app.gpio/gpio_test.c

compile: /home/topst/cr5-bsp/sources/app.sample/test.app.gpsb/gpsb_test.c

compile: /home/topst/cr5-bsp/sources/app.sample/test.app.hsm/hsm_test.c

compile: /home/topst/cr5-bsp/sources/app.sample/test.app.i2c/i2c_test.c

compile: /home/topst/cr5-bsp/sources/app.sample/test.app.ictc/ictc_test.c

compile: /home/topst/cr5-bsp/sources/app.sample/test.app.lin/lin_test.c

compile: /home/topst/cr5-bsp/sources/app.sample/test.app.pdm/pdm_test.c

compile: /home/topst/cr5-bsp/sources/app.sample/test.app.pmio/pmio_test.c

compile: /home/topst/cr5-bsp/sources/app.sample/test.app.timer/timer_test.c

compile: /home/topst/cr5-bsp/sources/app.sample/test.app.wdt/wdt_test.c

compile: /home/topst/cr5-bsp/sources/app.sample/app.mptool/mptool.c

compile: /home/topst/cr5-bsp/sources/app.drivers/ipc/common/ipc_os.c

compile: /home/topst/cr5-bsp/sources/app.drivers/ipc/common/ipc_buffer.c

compile: /home/topst/cr5-bsp/sources/app.drivers/ipc/common/ipc_cmd.c

compile: /home/topst/cr5-bsp/sources/app.drivers/ipc/common/ipc_ctl.c

compile: /home/topst/cr5-bsp/sources/app.drivers/ipc/common/ipc_parser.c

compile: /home/topst/cr5-bsp/sources/app.drivers/ipc/common/ipc_api.c

compile: /home/topst/cr5-bsp/sources/app.drivers/ipc/ipc.c

compile: /home/topst/cr5-bsp/sources/app.drivers/lin/lin.c

compile: /home/topst/cr5-bsp/sources/app.drivers/sdm/sdm.c

compile: /home/topst/cr5-bsp/sources/app.drivers/hsm/tcc805x/hsm_manager.c

compile: /home/topst/cr5-bsp/sources/dev.drivers/adc/tcc805x/adc.c

compile: /home/topst/cr5-bsp/sources/dev.drivers/can/can.c

compile: /home/topst/cr5-bsp/sources/dev.drivers/can/can_drv.c

compile: /home/topst/cr5-bsp/sources/dev.drivers/can/can_msg.c

compile: /home/topst/cr5-bsp/sources/dev.drivers/can/can_par.c

compile: /home/topst/cr5-bsp/sources/dev.drivers/can/tcc805x/can_porting.c

compile: /home/topst/cr5-bsp/sources/dev.drivers/clock/tcc805x/clock_dev.c

compile: /home/topst/cr5-bsp/sources/dev.drivers/common/debug.c

compile: /home/topst/cr5-bsp/sources/dev.drivers/common/tcc805x/bsp.c

compile: /home/topst/cr5-bsp/sources/dev.drivers/fmu/tcc805x/fmu.c

compile: /home/topst/cr5-bsp/sources/dev.drivers/gdma/tcc805x/gdma.c

compile: /home/topst/cr5-bsp/sources/dev.drivers/gic/tcc805x/gic.c

compile: /home/topst/cr5-bsp/sources/dev.drivers/gpio/tcc805x/gpio.c

compile: /home/topst/cr5-bsp/sources/dev.drivers/i2c/i2c.c

compile: /home/topst/cr5-bsp/sources/dev.drivers/i2c/tcc805x/i2c_reg.c

compile: /home/topst/cr5-bsp/sources/dev.drivers/ictc/ictc.c

compile: /home/topst/cr5-bsp/sources/dev.drivers/mailbox/tcc805x/mbox_phy.c

compile: /home/topst/cr5-bsp/sources/dev.drivers/mailbox/common/mbox_dev.c

compile: /home/topst/cr5-bsp/sources/dev.drivers/mailbox/mbox.c

compile: /home/topst/cr5-bsp/sources/dev.drivers/mpu/tcc805x/mpu.c

compile: /home/topst/cr5-bsp/sources/dev.drivers/pdm/pdm.c

compile: /home/topst/cr5-bsp/sources/dev.drivers/pmio/tcc805x/pmio_dev.c

compile: /home/topst/cr5-bsp/sources/dev.drivers/gpsb/gpsb.c

compile: /home/topst/cr5-bsp/sources/dev.drivers/gpsb/tcc805x/gpsb_reg.c

compile: /home/topst/cr5-bsp/sources/dev.drivers/timer/timer.c

compile: /home/topst/cr5-bsp/sources/dev.drivers/uart/tcc805x/uart.c

compile: /home/topst/cr5-bsp/sources/dev.drivers/udma/tcc805x/udma.c

compile: /home/topst/cr5-bsp/sources/dev.drivers/watchdog/wdt.c

compile: /home/topst/cr5-bsp/sources/dev.drivers/dse/tcc805x/dse.c

compile: /home/topst/cr5-bsp/sources/dev.drivers/midf/tcc805x/midf.c

compile: /home/topst/cr5-bsp/sources/dev.drivers/pmu/pmu_reset.c

compile: /home/topst/cr5-bsp/sources/os/freertos/tasks.c

compile: /home/topst/cr5-bsp/sources/os/freertos/list.c

compile: /home/topst/cr5-bsp/sources/os/freertos/queue.c

compile: /home/topst/cr5-bsp/sources/os/freertos/event_groups.c

compile: /home/topst/cr5-bsp/sources/os/freertos/timers.c

compile: /home/topst/cr5-bsp/sources/os/freertos/stream_buffer.c

compile: /home/topst/cr5-bsp/sources/os/freertos/portable/ARM_CR5/port.c

compile: /home/topst/cr5-bsp/sources/os/freertos/portable/MemMang/heap_5.c

compile: /home/topst/cr5-bsp/sources/sal/sal_api.c

compile: /home/topst/cr5-bsp/sources/sal/sal_freertos/sal_freertos_impl.c

compile: /home/topst/cr5-bsp/sources/core//GCC/startup.S

compile: /home/topst/cr5-bsp/sources/core//GCC/vector.S

compile: /home/topst/cr5-bsp/sources/core//GCC/vfp_init.S

compile: /home/topst/cr5-bsp/sources/core//GCC/arm_a.S

compile: /home/topst/cr5-bsp/sources/os/freertos/portable/ARM_CR5//GCC/portASM.S

compile: /home/topst/cr5-bsp/sources/os/freertos/portable/ARM_CR5//GCC/freertos.S

compile: /home/topst/cr5-bsp/sources/sal/sal.S

- -------------Make TC Image Format-----------------------------

./mkimg.sh TOOL_PATH=/home/topst/cr5-bsp/tools INPUT_PATH=/home/topst/cr5-bsp/sources/build/tcc805x/gcc/tcc805x-freertos-debug OUTPUT_PATH=/home/topst/cr5-bsp/sources/build/tcc805x/gcc/tcc805x-freertos-debug TARGET_ADDRESS=0x00000000 IMAGE_VERSION=0.0.0

/home/topst/cr5-bsp/sources/build/tcc805x/gcc/tcc805x-freertos-debug/r5_fw.rom was generated successfully

- --------------------------------------------------------------

Finished ...

~/{TOPST_PATH}

building on tcc8050-sub

=================================================================================

Built Path : /home/topst/cr5-bsp/sources/build/tcc805x/gcc/tcc805x-freertos-debug

=================================================================================

~/topst/boot-firmware/tools/snor_mkimage ~/topst

Get r5_fw.rom

MCERT file: (../../prebuilt/mcert.bin)

HSM binary file: (../../prebuilt/hsm.cs.bin)

R5-BL1 binary file: (../../prebuilt/r5_bl1-snor.rom)

update binary file: (../../prebuilt/r5_sub_fw.rom)

MICOM binary file: (./r5_fw.rom)

SNOR ROM size: (4 MByte)

R5 UART port enable: (0)

R5 UART port for debug: (46)

Output file: (../../../cr5-bsp/sources/build/tcc805x/gcc/tcc805x-freertos-debug/cr5_snor.rom)

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

MICOM ROM size: 0x6fec0

<<SNOR_MAP: 0x00000000 ++0x00002000>>

[Make SNOR ROM Header...]

SNOR ROM Header CRC: 0xDFAA5453

write_rom_header - success

SNOR ROM Header CRC: 0x5B90D383

write_rom_header - success

Total Image Size: 4194304 byte

create_final_rom - success

~/{TOPST_PATH}
```

---

### 1.1.3.4 “Make fai” for Automotive Platform

This option creates a binary of the main core and sub-core into one image for automotive platform image. The following is a list of images that are created with this option.

Refer to Chapter 4 for download instructions.

| Command | Into SD Data.fai |  |  |  | Description |
| --- | --- | --- | --- | --- | --- |
|  | Core | Bootloader | Kernel | File system |  |
| make_fai | Main (CA72) | U-Boot 2020.01 | 5.4.159 | automotive-linux-platform-image | ivi-image + demo applications |
|  | Sub (CA53) |  |  | telechips-subcore-image | minimal root filesystem |

The “SD Data.fai” build image is created in the following path:

- {TOPST_PATH}/build/tcc8050-main/tmp/deploy/fwdn

```bash
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

---

### 1.1.3.5 Ubuntu File System Build

The TOPST system is configured with the following images by default.

If you want to create and insert Ubuntu images, refer to “*TOPST D3 Linux SDK-Install Guide for Ubuntu*” to build and download the Ubuntu images.

| Core | Created image | Description |
| --- | --- | --- |
| Main (CA72) | ubuntu-jammy-arm64-xx.img | Ubuntu 22.04 TLS |