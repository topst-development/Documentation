# Build Guide

## TOPST AI SDK

TOPST AI SDK is based on Yocto Project 4.0 kirkstone. Therefore, the
Yocto Project environment must be set on the host PC to use

TOPST AI SDK. To download SDK, source-mirror, and tools, you must
install utilities.

Figure 3.1 shows the task process of Yocto Project. You can download
source from upstream based on metadata and perform build.

After the build is completed, package, image, and SDK are provided as
results.

<img src="https://github.com/topst-development/Documentation/blob/Tsolutions/TOPST-AI/Software/media/Build guide.image1.png"
style="width:7.27639in;height:3.56458in"
alt="텍스트, 스크린샷, 폰트, 도표이(가) 표시된 사진 자동 생성된 설명" />

Figure 3 1 Yocto Project Task Process

## Composition of TOPST AI SDK

After TOPST AI SDK is downloaded, you can check the following items.

Table 1.1 Composition of TOPST AI SDK

<table>
<colgroup>
<col style="width: 13%" />
<col style="width: 14%" />
<col style="width: 13%" />
<col style="width: 57%" />
</colgroup>
<tbody>
<tr class="odd">
<td colspan="3"><strong>Item</strong></td>
<td><strong>Description</strong></td>
</tr>
<tr class="even">
<td rowspan="11">poky</td>
<td colspan="2">meta</td>
<td rowspan="3">Yocto Project 4.0 kirkstone build system</td>
</tr>
<tr class="odd">
<td colspan="2">meta-poky</td>
</tr>
<tr class="even">
<td colspan="2">meta-yocto-bsp</td>
</tr>
<tr class="odd">
<td colspan="2">meta-arm</td>
<td>Support Arm toolchain Layer</td>
</tr>
<tr class="even">
<td colspan="2">meta-qt5</td>
<td>Support Qt5 5.6.3 Layer</td>
</tr>
<tr class="odd">
<td colspan="2">meta-gplv2</td>
<td>Support packages to avoid GPLv3 license</td>
</tr>
<tr class="even">
<td rowspan="4">meta-telechips</td>
<td>meta-core</td>
<td><p>Recipes that require modification from Open Source Software
(OSS)</p>
<p>used by TOPST AI SDK or recipes that are not in Yocto Project
4.0</p></td>
</tr>
<tr class="odd">
<td>meta-extra</td>
<td>OSS Layer that is added</td>
</tr>
<tr class="even">
<td>meta-qt5</td>
<td>Support Qt5 to support Telechips GUI application</td>
</tr>
<tr class="odd">
<td>meta-nn</td>
<td>Configuration package and example programs of TOPST AI</td>
</tr>
<tr class="even">
<td colspan="2">download.sh</td>
<td>Script for downloading source-mirror, tools</td>
</tr>
<tr class="odd">
<td rowspan="3">boot-firmware</td>
<td colspan="2">prebuilt</td>
<td><p>Boot-firmware files</p>
<p>Tools to make images for boot-firmware</p></td>
</tr>
<tr class="even">
<td colspan="2">fwdn_nd.exe</td>
<td>FWDN execute file</td>
</tr>
<tr class="odd">
<td colspan="2">tools/mktcimg</td>
<td>mktcimg execute file source code</td>
</tr>
<tr class="even">
<td colspan="3">tools</td>
<td><p>x86_64-buildtools-extended-nativesdk-standalone-4.0.sh</p>
<p>x86_64-buildtools-nativesdk-standalone-4.0.sh</p></td>
</tr>
</tbody>
</table>

## Download And Build TOPST AI SDK

### Get TOPST AI with Git

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><strong>$ repo init -u
ssh://sgit.telechips.com/nd_cs_pre/manifest.git -m
tcc750x_linux_nn_0.9.0.xml</strong></p>
<p>Downloading Repo source from
https://gerrit.googlesource.com/git-repo</p>
<p>... A new version of repo (2.40) is available.</p>
<p>... You should upgrade soon:</p>
<p>cp /home/topst_ND/SDK_build/.repo/repo/repo /home/
topst_ND/.bin/repo</p>
<p>Your identity is: user_id&lt;user_id @tsolus.com&gt;</p>
<p>If you want to change this, please re-run 'repo init' with
--config-name</p>
<p>repo has been initialized in /home/topst_ND/SDK_build</p>
<p><strong>$ repo sync</strong></p>
<p>... A new version of repo (2.40) is available.</p>
<p>... You should upgrade soon:</p>
<p>cp /home/topst_ND/SDK_build/.repo/repo/repo
/home/topst_ND/.bin/repo</p>
<p>Fetching: 100% (12/12), done in 1m14.010s</p>
<p>Updating files: 100% (819/819), done.</p>
<p>Checking out: 100% (12/12), done in 6.056s</p>
<p>repo sync has finished successfully.</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

### Download And Install Build Tools 

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>$ <strong>poky/download.sh</strong></p>
<p>This may take a long time depending on your network environment.</p>
<p>Continue? (Y/n) =&gt; <strong>Y</strong></p>
<p>Start tools downloading...done</p>
<p>Create source-mirror directory</p>
<p>Start source mirror downloading...done</p>
<p>$ <strong>ls</strong></p>
<p>boot-firmware fwdn-v8 mktcimg poky rtpm source-mirror tc-nn-toolkit
tools</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>$ <strong>pwd</strong></p>
<p>/home/topst_ND/SDK_build</p>
<p>$
<strong>./tools/x86_64-buildtools-nativesdk-standalone-4.0.sh</strong></p>
<p>Build tools installer version 4.0</p>
<p>=================================</p>
<p>Enter target directory for SDK (default: /opt/poky/4.0):
<strong>/home/topst_ND/SDK_build/buildtools</strong></p>
<p>You are about to install the SDK to
"/home/topst_ND/SDK_build/buildtools". Proceed [Y/n]?
<strong>Y</strong></p>
<p>Extracting SDK...........done</p>
<p>Setting it up...done</p>
<p>SDK has been successfully set up and is ready to be used.</p>
<p>Each time you wish to use the SDK in a new shell session, you need to
source the environment setup script e.g.</p>
<p>$ .
/home/topst_ND/SDK_build/buildtools/environment-setup-x86_64-pokysdk-linux</p>
<p>$ <strong>ls buildtools/</strong></p>
<p>environment-setup-x86_64-pokysdk-linux sysroots
version-x86_64-pokysdk-linux</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

### Execute Build Script

The build image is created in the following path:

- {TOPST_PATH}/build/tcc7500-main/tmp/deploy/images/tcc7500-main

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><strong>$ source
poky/meta-telechips/meta-nn/nn-build.sh</strong></p>
<p>Choose MACHINE</p>
<p>1. tcc7500-main</p>
<p>select number(1-1) =&gt; <strong>1</strong></p>
<p>machine(tcc7500-main) selected.</p>
<p>You had no conf/local.conf file. This configuration file has
therefore been</p>
<p>created for you from
/home/topst_ND/SDK_build/poky/meta-telechips/meta-nn/template/tcc750x/local.conf.sample</p>
<p>You may wish to edit it to, for example, select a different MACHINE
(target</p>
<p>hardware). See conf/local.conf for more information as common
configuration</p>
<p>options are commented.</p>
<p>You had no conf/bblayers.conf file. This configuration file has
therefore been</p>
<p>created for you from
/home/topst_ND/SDK_build/poky/meta-telechips/</p>
<p>meta-nn/template/tcc750x/bblayers.conf.sample</p>
<p>To add additional metadata layers into your configuration please add
entries</p>
<p>to conf/bblayers.conf.</p>
<p>The Yocto Project has extensive documentation about OE including a
reference</p>
<p>manual which can be found at:</p>
<p>https://docs.yoctoproject.org</p>
<p>For more information about OpenEmbedded see the website:</p>
<p>https://www.openembedded.org/</p>
<p>Yocto Project common targets are:</p>
<p>core-image-minimal</p>
<p>core-image-sato</p>
<p>meta-toolchain</p>
<p>adt-installer</p>
<p>meta-ide-support</p>
<p><strong>Telechips nn targets are:</strong></p>
<p><strong>telechips-nn-image (telechips-nn-image-minimal + qt + Sample
Application)</strong></p>
<p><strong>telechips-nn-image-python (telechips-nn-image +
python3)</strong></p>
<p><strong>telechips-nn-image-minimal</strong></p>
<p>meta-toolchain-telechips-nn(Application Development Toolkit)</p>
<p>You can also run generated Telechips images on Telechips EVB
Boards(eg. tcc7500)</p>
<p>Other commonly useful commands are:</p>
<p>- 'devtool' and 'recipetool' handle common recipe tasks</p>
<p>- 'bitbake-layers' handles common layer tasks</p>
<p>- 'oe-pkgdata-util' handles common target package tasks</p>
<p><strong>$ bitbake telechips-nn-image</strong></p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

### Make FWDN Image

This option creates a binary into one image for TOPST AI platform image.
The following is a list of images that are created with this option.

Refer to Chapter 4 for download instructions.

|             |                      |          |                    |                             |
|-------------|----------------------|----------|--------------------|-----------------------------|
| **Command** | **Into SD Data.fai** |          |                    | **Description**             |
|             | Bootloader           | Kernel   | File system        |                             |
| make_fai    | U-Boot 2022.01       | 5.10.177 | telechips-nn-image | ai-image + demo application |

The “SD Data.fai” build image is created in the following path:

- {TOPST_AI_PATH}/build/tcc7500-main/tmp/deploy/fwdn

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><strong>$ bitbake telechips-nn-image -f -c make_fai</strong></p>
<p>Loading cache: 100% |##########################################Time:
0:00:00</p>
<p>Loaded 2835 entries from dependency cache.</p>
<p>WARNING: No recipes in default available for:</p>
<p>/home/topst_ND/SDK_build/poky/meta-telechips/meta-nn/recipes-applications/tc-update-engine/tc-update-engine_1.0.0.bbappend</p>
<p>NOTE: Resolving any missing task queue dependencies</p>
<p>Build Configuration:</p>
<p>BB_VERSION = "2.0.0"</p>
<p>BUILD_SYS = "x86_64-linux"</p>
<p>NATIVELSBSTRING = "universal"</p>
<p>TARGET_SYS = "aarch64-telechips-linux"</p>
<p>MACHINE = "tcc7500-main"</p>
<p>DISTRO = "poky-telechips-systemd"</p>
<p>DISTRO_VERSION = "4.0.8"</p>
<p>TUNE_FEATURES = "aarch64 armv8a crc cortexa53"</p>
<p>TARGET_FPU = ""</p>
<p>LINUX_VERSION = "5.10.177"</p>
<p>KBUILD_DEFCONFIG = "tcc750x_defconfig"</p>
<p>TCC_BSP_FEATURES = " display network multimedia camera"</p>
<p>IMAGE_FEATURES = " debug-tweaks ssh-server-openssh"</p>
<p>GCCVERSION = "arm-9.2"</p>
<p>GLIBCVERSION = "2.35%"</p>
<p>meta</p>
<p>meta-poky</p>
<p>meta-gplv2 = "HEAD:d3d4f87e5b59bcab816766215e7f05de7176348e"</p>
<p>meta-arm-toolchain =
"HEAD:76c923a43573596de227d2071e13581ccf2aee2b"</p>
<p>meta-telechips-bsp =
"HEAD:36de8b9b296c90996c39ae17215154f75f2de64e"</p>
<p>meta-qt5 = "HEAD:9ca6dcc6db66bedd3bba6a658d7145bea63f809f"</p>
<p>meta-core</p>
<p>meta-extra</p>
<p>meta-qt5</p>
<p>meta-python = "HEAD:77c034786cf3e7f7e3edb8baa50d448a7590cef0"</p>
<p>meta-nn = "HEAD:7d6f5965413dc8f7fdfe3974bb1f03efe623bbde"</p>
<p>Initialising tasks: 100%
|###################################################| Time: 0:00:00</p>
<p>Sstate summary: Wanted 0 Local 0 Mirrors 0 Missed 0 Current 75 (0%
match, 100% complete)</p>
<p>NOTE: Executing Tasks</p>
<p>NOTE: Tasks Summary: Attempted 328 tasks of which 327 didn't need to
be rerun and all succeeded.</p>
<p>NOTE: Writing buildhistory</p>
<p>NOTE: Writing buildhistory took: 1 seconds</p>
<p>Summary: There were 2 WARNING messages.</p>
<p><strong>$ ls -l tmp/deploy/fwdn</strong></p>
<p><em><strong>SD_Data.fai</strong></em> SD_Data.gpt SD_Data.gpt.back
SD_Data.gpt.prim <em><strong>boot-firmware</strong></em>
partition.list</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

# 
