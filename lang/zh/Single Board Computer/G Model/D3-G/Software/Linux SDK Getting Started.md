# 1. 简介
---
本文档提供构建 D3-G SDK 的指南，包括设置主机环境、构建 SDK、使用固件下载器以及下载 Ubuntu。  

本文档包含以下内容： 
- 设置主机环境  
- 镜像构建指南  
- 固件下载指南 
- 将 D3-G 开发板与 PC 连接

<br/><br/><br/><br/>

# 2. 设置主机环境
---
本章说明如何设置主机 PC 环境，并分别提供 Windows 和 Ubuntu 的指南。
</br><br/><br/>

## 2.1 Windows 环境 
---
本文档介绍如何设置 Windows Subsystem for Linux (WSL)，以便在 Windows PC 上使用 Linux。
D3-G Linux SDK 基于 Yocto Project，因此 D3-G SDK 的 Linux 版本遵循 Yocto Project。
您也可以安装其他版本的 Linux，但本文档介绍的是基于 Ubuntu 22.04 的 D3-G Linux SDK。
如果您的主机操作系统是 Ubuntu，请转至第 2.2 章。

</br><br/>

### 2.1.1 安装 WSL2 Ubuntu
1. 以"**以管理员身份运行**"方式执行 Windows PowerShell。
2. 启用 WSL2 系统。
    ```
    dism.exe /online /enable-feature /featurename:Microsoft-Windows-Subsystem-Linux /all /norestart
    ```
3. 启用虚拟机功能。
    ```
    dism.exe /online /enable-feature /featurename:VirtualMachinePlatform /all /norestart
    ```
4. 将 WSL 2 设置为默认版本。
    ```
    wsl --set-default-version 2
    ```
5. 在 Microsoft Store 中搜索 Ubuntu 22.04.3 LTS 并下载。

    * 如果需要下载 Linux 内核更新包，请从[此处](https://learn.microsoft.com/ko-kr/windows/wsl/install-manual)下载最新的软件包。

6. 在 Ubuntu 安装过程中可任意选择用户名。
</br><br/>

### 2.1.2 通过 WSL2 访问 Ubuntu
打开 Windows 命令提示符并输入以下命令以访问 Ubuntu。
访问 Ubuntu 时，默认从 /mnt/c/Users/[username] 目录启动。
```
wsl  // access ubuntu 
ls   // check contents in your directory
```
请参考图 2.1 检查结果（结果可能因系统而异）。
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20D3-G/Software/1.1%20wsl%20linux.png" width="500"></p>
<p align="center"><strong>图 2.1 WSL2 屏幕截图 </strong></p>

<br/><br/>

### 2.1.3 设置区域设置

在 WSL 上运行 Ubuntu 后，应设置区域设置以确保语言和地区配置正确。建议使用 en_US.UTF-8。请执行以下命令以使用 en_US.UTF-8。 

```
sudo locale-gen en_US.UTF-8 && sudo update-locale LANG=en_US.UTF-8 
```

设置区域设置后，可以使用以下命令检查区域设置类型。 

```
echo 'LANG=en_US.UTF-8' | sudo tee -a /etc/default/locale && \  

echo 'LC_ALL=en_US.UTF-8' | sudo tee -a /etc/default/locale 
```
<br/><br/>

### 2.1.4 安装 SSH 和 Samba

进入 Ubuntu 后，您可以使用 SSH 和 Samba 等附加实用工具，以获得更便捷的开发环境。SSH 和 Samba 可让您在远程计算机上执行命令，并将文件复制到其他计算机。
 - 以下步骤要求主机 PC 已连接到网络。请使用以下命令检查网络状态。
  ```
  $ sudo apt-get update
  $ sudo apt-get install -y net-tools
  $ ifconfig 
  ```

如果已安装 SSH 和 Samba，或者不打算使用它们，可以跳过本章。

使用以下命令安装 net-tools、SSH 和 Samba。

```
$ sudo apt-get update 
$ sudo apt install -y net-tools openssh-server samba
```
安装 SSH 和 Samba 后，请根据您的环境需要配置各个程序。
</br><br/>

### 2.1.5 安装实用工具

使用以下命令一次性安装所有必需的实用工具。要使用 Yocto Project，必须在主机 PC（个人计算机或开发服务器）上安装以下实用工具。


```
$ sudo apt-get install -y gawk wget git diffstat unzip texinfo gcc-multilib build-essential chrpath

$ sudo apt-get install -y socat cpio python3 python3-pip python3-pexpect xz-utils debianutils

$ sudo apt-get install -y iputils-ping python3-git python3-jinja2 libegl1-mesa-dev libsdl1.2-dev pylint

$ sudo apt-get install -y xterm zstd ncftp curl git-lfs vim zip lz4
```

<br/><br/>

### 2.1.6 安装 Repo

如果已安装 Repo，则无需重新安装即可使用。  
安装 Repo 之前，请确认已安装 Python 3.6 或更高版本。

使用以下命令安装 Repo。
```
$ sudo apt-get install repo
```

如果出现错误消息 '/usr/bin/env 'python' no such file or directory'，请使用以下命令将 'python' 链接到 'python3'。

```
$ sudo ln -sf /usr/bin/python3 /usr/bin/python
```
如果出现 Repo 错误，请使用以下命令下载最新版本并将其放入 /usr/bin/ 文件夹。

```
$ mkdir -p ~/bin

$ curl http://commondatastorage.googleapis.com/git-repo-downloads/repo > ~/bin/repo

$ chmod a+x ~/bin/repo

$ sudo mv ~/bin/repo /usr/bin/repo
```
请转到 **第 3 章：镜像构建指南**。

<br/><br/><br/>

## 2.2 Linux 环境
---
本章说明使用 Ubuntu 作为主机操作系统时的设置流程。
</br><br/>

### 2.2.1 设置环境
以下各章（2.2.2 至 2.2.5）必须在 Ubuntu 终端中执行。要打开终端，请使用快捷键 [Ctrl + Alt + T]。
<br/><br/>

### 2.2.2 设置区域设置

在 WSL 上运行 Ubuntu 后，应设置区域设置以确保语言和地区配置正确。建议使用 en_US.UTF-8。请执行以下命令以使用 en_US.UTF-8。 

```
sudo locale-gen en_US.UTF-8 && sudo update-locale LANG=en_US.UTF-8 
```

设置区域设置后，可以使用以下命令检查区域设置类型。 

```
echo 'LANG=en_US.UTF-8' | sudo tee -a /etc/default/locale && \  

echo 'LC_ALL=en_US.UTF-8' | sudo tee -a /etc/default/locale 
```
<br/><br/>

### 2.2.3 安装 SSH 和 Samba

进入 Ubuntu 后，您可以使用 SSH 和 Samba 等附加实用工具，以获得更便捷的开发环境。SSH 和 Samba 可让您在远程计算机上执行命令，并将文件复制到其他计算机。
 - 以下步骤要求主机 PC 已连接到网络。请使用以下命令检查网络状态
  ```
  $ sudo apt-get update
  $ sudo apt-get install -y net-tools
  $ ifconfig 
  ```

如果已安装 SSH 和 Samba，或者不打算使用它们，可以跳过本章。

使用以下命令安装 SSH 和 Samba。

```
$ sudo apt-get update 
$ sudo apt install -y openssh-server samba
```
安装 SSH 和 Samba 后，请根据您的环境需要配置各个程序。

<br/><br/>

### 2.2.4 安装实用工具

使用以下命令一次性安装所有必需的实用工具。要使用 Yocto Project，**必须**在主机 PC（个人计算机或开发服务器）上安装以下实用工具。
****


```
$ sudo apt-get install -y gawk wget git diffstat unzip texinfo gcc-multilib build-essential chrpath

$ sudo apt-get install -y socat cpio python3 python3-pip python3-pexpect xz-utils debianutils

$ sudo apt-get install -y iputils-ping python3-git python3-jinja2 libegl1-mesa-dev libsdl1.2-dev pylint

$ sudo apt-get install -y xterm zstd ncftp curl git-lfs vim zip lz4
```

<br/><br/>

### 2.2.5 安装 Repo

您可以通过 Android Repo 下载 D3-G SDK。  
要安装 Repo，请参考以下网站：https://source.android.com/source/downloading.html.  
如果已安装 Repo，则无需重新安装即可使用。  
安装 Repo 之前，请确认已安装 Python 3.6 或更高版本。

使用以下命令安装 Repo。
```
$ sudo apt-get install repo
```

如果出现错误消息 '/usr/bin/env 'python' no such file or directory'，请使用以下命令将 'python' 链接到 'python3'。

```
$ sudo ln -sf /usr/bin/python3 /usr/bin/python
```
如果出现 Repo 错误，请使用以下命令下载最新版本并将其放置到 /usr/bin/ 文件夹中。

```
$ mkdir -p ~/bin

$ curl http://commondatastorage.googleapis.com/git-repo-downloads/repo > ~/bin/repo

$ chmod a+x ~/bin/repo

$ sudo mv ~/bin/repo /usr/bin/repo
```

<br/><br/>

### 2.2.6 Telechips USB 设备的 Udev Rules
执行以下命令后，在 Linux 中下载 FWDN 时不再需要使用 'sudo' 命令。
```
$ echo "SUBSYSTEM==\"usb\", ATTR{idVendor}==\"140e\", MODE=\"0666\", OWNER=\"${USER}\"" | sudo tee /etc/udev/rules.d/99-topst.rules
$ sudo udevadm control --reload-rules && sudo udevadm trigger
```
请转到 **第 3 章：镜像构建指南**。

<br/><br/><br/><br/>

# 3. 镜像构建指南
---
本章基于主机 PC 上安装的 Ubuntu OS 进行说明（无论是 WSL 还是本地安装的 Ubuntu）。要上传到 D3-G 的镜像使用 Yocto Project 构建，因此构建过程必须在 Ubuntu 环境中执行。
</br></br>

## 3.1 SDK 构建准备
---
D3-G Linux SDK 基于 Yocto Project 4.0 Kirkstone 。因此，要使用 D3-G Linux SDK，必须在主机 PC 上配置 Yocto Project 环境。要下载 SDK、source-mirror 和工具，需要安装所需的实用程序。为了顺利构建镜像，您的 PC 必须具有**至少 60 GB 的可用存储空间**和**至少 16 GB 的 RAM**。

</br><br/>  

## 3.2 Yocto Project  
---
Yocto Project 是一个专注于嵌入式 Linux 开发的开源项目。  
它将 Open Embedded 项目（即 Poky）与 ***bitbake*** 组合作为构建系统，用于制作 Linux 镜像。  
使用 Yocto Project，您可以同时构建引导加载程序、内核和 rootfs。  

<br/><br/>

## 3.3 Yocto Project 的任务流程
---
图 3.1 显示了 Yocto Project 的任务流程。您可以根据元数据从上游下载源代码并进行构建。构建完成后，将提供软件包、镜像和 SDK 作为结果。

<p align="center">
    <img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20D3-G/Software/2.1%20yocto%20project%20task%20process.png", width="700">
</p>
<p align="center"><strong>图 3.1 Yocto Project 任务流程</strong></p>

<br/><br/>

## 3.4 D3-G SDK 的组成
---
以下是我们配置的 Yocto Project 的组成部分。
表 3.1 显示了 D3-G SDK 的组成。



**表 3.1 D3-G SDK 的组成**
<table border="1" cellspacing="0" cellpadding="5">
  <colgroup>
    <col style="width: 10%">
    <col style="width: 10%">
    <col style="width: 10%">
    <col style="width: 56%">
  </colgroup>
  <thead>
    <tr>
      <th colspan="3"style="text-align: center; vertical-align: middle;"><strong>项目</strong></th>
      <th style="text-align: center; vertical-align: middle;" ><strong>说明</strong></th>
    </tr>
  </thead>
  <tbody>
  <tr>
      <td colspan="3"style="text-align: center; vertical-align: middle;">easy-setup.sh</td>
      <td>自动下载并构建 SDK 的 Python 脚本</td>
    </tr>
    <tr>
      <td colspan="3"style="text-align: center; vertical-align: middle;">stitch-fai-ai.sh</td>
      <td>用于创建 AI-G fai 镜像的脚本 (minimal + 示例应用程序)</td>
    </tr>
    <tr>
      <td colspan="3"style="text-align: center; vertical-align: middle;">stitch-fai-d3.sh</td>
      <td>用于创建 D3-G fai 镜像的脚本 (minimal + 示例应用程序)</td>
    </tr>
    <tr>
      <td colspan="3"style="text-align: center; vertical-align: middle;">mktcimg</td>
      <td rowspan="2">与构建过程和 <strong>FWDN</strong> 相关的工具</td>
    </tr>
    <tr>
      <td colspan="3"style="text-align: center; vertical-align: middle;">tools</td>
    </tr>
    <tr>
      <td rowspan="8"style="text-align: center; vertical-align: middle;">poky</td>
      <td colspan="2"style="text-align: center; vertical-align: middle;">poky</td>
      <td>Yocto Project 4.0 Kirkstone 构建系统</td>
    </tr>
    <tr>
      <td colspan="2"style="text-align: center; vertical-align: middle;">meta-openembedded</td>
      <td>支持 OE-Core 的层</td>
    </tr>
    <tr>
      <td colspan="2"style="text-align: center; vertical-align: middle;">meta-arm</td>
      <td>支持 ARM 工具链的层</td>
    </tr>
    <tr>
      <td colspan="2"style="text-align: center; vertical-align: middle;">meta-topst-bsp</td>
      <td>支持 TOPST BSP 的层</td>
    </tr>
    <tr>
      <td colspan="2"style="text-align: center; vertical-align: middle;">meta-gplv2</td>
      <td>包含规避 GPLv3 许可证的软件包的层</td>
    </tr>
    <tr>
      <td colspan="2"style="text-align: center; vertical-align: middle;">meta-topst</td>
      <td>TOPST 配方</td>
    </tr>
  </tbody>
</table>
<br/><br/><br/>


## 3.5 构建准备
---
以下章节介绍如何配置 Yocto Project 以构建 D3-G 镜像。

<br/><br/>

### 3.5.1 在 .gitconfig 中设置用户邮箱和用户名
要从 TOPST 官方 git 下载 D3-G SDK，请配置您的电子邮件和姓名。
1. 输入以下命令。
```
vi ~/.gitconfig
```
2. 输入以下信息
```
[user]
    email = User email
    name = User name
```

<br/><br/>

### 3.5.2 从 Git 获取 D3-G

1. 创建名为 **topst-sdk** 的新目录，并将当前目录切换到 **topst-sdk**。

```
$ mkdir topst-sdk
$ cd topst-sdk
```

2. 执行以下命令以初始化仓库。

```
$ repo init -u https://github.com/topst-development/manifests.git -b release/1.3.0 -m linux_yp4.0_topst.xml
```

执行该命令后，将显示以下输出。

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

3. 执行以下命令以同步仓库。

```
$ repo sync
```

执行该命令后，将显示以下输出。

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

## 3.6 执行 topst-build.sh 
---
如果运行 ./easy-setup.sh 脚本，您将看到以下画面。 

**注意：如果重新运行 ./easy-setup.sh，请注意选择 yes 时已构建的源代码将被删除。**
```
./easy-setup.sh
```
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20AI-G/Software/Linux%20SDK/license1.png"></p>
<p align="center"><strong>图 3.2 最终用户许可协议</strong></p>

滚动到屏幕底部并阅读此声明。阅读此声明后，按右箭头键和 [Enter]。
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20AI-G/Software/Linux%20SDK/license2.png"></p>
<p align="center"><strong>图 3.3 转到 'Proceed to confirm'</strong></p>


随后可以看到以下画面。 
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20AI-G/Software/Linux%20SDK/license3.png" ></p>
<p align="center"><strong>图 3.4 接受画面 </strong></p>


构建镜像在以下路径中生成:

- {TOPST_PATH}/build/d3-g-topst-main/tmp/deploy/images/d3-g-topst-main

topst-build.sh 是用于设置构建 D3-G 和 AI-G 镜像所需核心环境的 shell 脚本。执行以下命令，并选择选项 2 以准备在 D3-G 上安装主 OS 的构建环境。



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

运行以下命令开始构建主 OS。
```
$ bitbake telechips-topst-image
```

<br/><br/><br/>

## 3.7 制作 Firmware Downloader (FWDN) 镜像 
---
此选项将各二进制文件合并为 D3-G 平台镜像的单个镜像。

包含 **'output_d3g.fai' 构建镜像**和 **FWDN 工具**的 **output_d3g.fwdn.zip** 文件将在以下路径中创建：

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

如果看到以下日志，则表示已创建 "output_d3g.fwdn.zip" 文件。 
```
$ ls
build  easy-setup.sh  mktcimg  output_d3g.fwdn.zip  poky  stitch-fai-ai.sh  stitch-fai-d3.sh  tools
```

</br></br><br/><br/>

# 4. 固件下载
---
本章介绍如何使用 ***FWDN*** 将固件下载到 D3-G 并登录 Linux 控制台。  
***FWDN V8*** 是一款用于在 Windows 10(11) 64 位和 Linux 环境中下载固件的 PC 工具。本章介绍在 Windows 和 Linux 环境中下载的情况。

<br/><br/><br/>

## 4.1 固件下载顺序
---
***FWDN*** 的下载顺序如下:

1. 将启动模式开关设置为 USB 启动模式。
2. 打开 Windows 命令提示符或 Linux 控制台。
3. 将 ***FWDN V8*** 连接到开发板。
4. 下载 fai 文件。

<br/><br/><br/>

## 4.2 使用 USB 启动模式连接 D3-G 开发板与主机 PC
---
Firmware Downloader (FWDN) 通过与主机 PC 的 USB 通信将 ROM 镜像写入 D3-G。 

D3-G 有一个 Boot Mode 按钮，支持两种类型的启动模式。本指南重点介绍 FWDN 模式。

- USB Boot Mode (FWDN Mode)：用于通过主机 PC 上的 FWDN 工具写入 ROM 镜像 

- eMMC Boot Mode：用于使用存储在 eMMC 设备中的 ROM 镜像启动 D3-G 

**注意**：USB Type-C FWDN 端口用于 firmware downloader (FWDN)。 



要使用 FWDN，请按以下方式将 D3-G 开发板连接到主机 PC： 

1. 确认主机 PC 上已安装 VTC 驱动程序。如果未安装 VTC 驱动程序，请按第 4.2.1 章所述进行安装。  

2. 准备一根 USB Type-C 线缆。 

3. 要进入 USB 启动模式，请在按住 FWDN 开关的同时将电源线连接到 D3-G 开发板。
   - 有关详细信息，请参见侧边栏 Hardware 部分下的 **"2. Boot Mode"**。

4. 将 USB Type-C 线缆连接到 D3-G 开发板上的 USB Type-C FWDN 端口和主机 PC。 

<p align="center">
    <img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20D3-G/Hardware/connect%20to%20d3g%20to%20host%20pc%20using%20c%20type.png">
</p>
<p align="center"><strong>图 4.1 使用 USB C-Type 线缆连接 D3-G 开发板与主机 PC </strong></p>

<br/><br/>

### 4.2.1 VTC 驱动程序安装方法 (Windows/Ubuntu)
在主机 PC 上以管理员身份运行以安装 Vendor Telechips Certification (VTC) 驱动程序（可在 [telechips driver](https://drive.google.com/file/d/1muQnY8kuKxDsy3p3FUiQqcG34Zjk-mnR/view?usp=sharing) 中找到）。如上所示在 FWDN 模式下连接 USB 时，Telechips VTC USB 驱动程序将按图 4.2 和图 4.3 所示进行设置。

<p align="center">
    <img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20D3-G/Software/USB%20Connection%20in%20Windows%20Environment.png", width="700">
</p>
<p align="center"><strong>图 4.2 Windows 环境中的 USB 连接</strong></p>

<p align="center">
    <img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20D3-G/Software/USB%20Connection%20in%20Linux%20System.png", width="700">
</p>
<p align="center"><strong>图 4.3 Linux 环境中的 USB 连接</strong></p>  

**注意**：请使用 V5.0.0.14 或更高版本的 VTC 驱动程序。要检查版本，请在 Windows 环境中确认设备管理器。  

<br/><br/><br/>

## 4.3 准备下载 FWDN
---
执行 FWDN 之前，请将在 Ubuntu (WSL2) 环境中创建的镜像和工具传输到 Windows 环境。


1. 解压 "output_d3g.fwdn.zip"。   
    ```
    $ cd ~/topst-sdk
    $ mkdir images
    $ mv ./output_d3g.fwdn.zip ./images
    $ cd images
    $ unzip output_d3g.fwdn.zip
    ```
2. 将 "images" 文件夹复制到 Windows C 盘。  
    ```
    $ cd ..
    $ cp -r ./images /mnt/c/
    ```

<br/><br/><br/>

## 4.4 Windows 环境中的 FWDN
---
1. 执行 Powershell 并转到 "C:\images\"。
```
$ cd C:\images 
```

2. 输入 **.\fwdn.bat** 命令以开始固件下载。“fwdn.bat”是使用 FWDN V8 自动下载固件的可执行文件。 

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

## 4.5  Linux 环境中的 FWDN
---
要在 Linux 中下载 D3-G 镜像，请执行以下命令："./fwdn.sh"。

```
$ ./fwdn.sh
```

现在您已准备好启动 D3-G。请参阅第 5 章以开始与设备通信。


<br/><br/><br/><br/>

# 5. 将 D3-G 开发板与主机 PC 连接
---
本章介绍如何通过 UART 将主机 PC 连接到 D3-G 开发板，以进行固件下载和串行通信。

<br/><br/><br/>

## 5.1 使用 UART 连接 D3-G 开发板 
---
请按照以下步骤操作，并使用 UART 连接验证固件下载是否成功完成。 

1. 在 Windows 环境中安装串口驱动程序（例如 CP210x Windows Driver）和 PL2303_prolific 驱动程序。 
2. 安装 Tera Term 或 PuTTY 等终端仿真器。 
3. 连接主机 PC 与 D3-G 开发板上的 UART 引脚。请使用 USB-to-TTL 线缆。 
4. 将黑色线缆连接到 GND 引脚。 
5. 将白色线缆(RXD)连接到 UART 引脚中的 TX 引脚，将绿色线缆(TXD)连接到 UART 引脚中的 RX 引脚。
6. 运行终端仿真器应用程序。
7. 在 PC 上打开设备管理器，检查分配给 UART 设备的端口号。
8. 在终端仿真器中，将确认的端口号输入 Serial line 字段。将 **Speed** (bps) 设置为 115200，将 **Flow control** 设置为 **None**。
9. 连接电源线。然后，D3-G 开发板将以默认的 eMMC 启动模式启动。


 
<p align="center">
    <img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20D3-G/Software/USB%20to%20TTL%20Connection.png", width="700">
</p>
<p align="center"><strong>图 5.1 与主机 PC 的 UART 连接</strong></p><br/>  


图 5.2 显示了成功登录的画面。  
登录的用户名和密码均设置为 **root**。

<p align="center">
    <img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20D3-G/Software/d3-g%20login%20as%20root.png", width="700">
</p>
<p align="center"><strong>图 5.2 已连接画面 (ID 和密码为 topst)</strong></p><br/>

<br/><br/><br/>

# 6. Ubuntu OS 分区大小调整
---
我们还提供 Ubuntu OS。
按照本章的说明，您可以下载 Ubuntu 镜像，将其上传到开发板，并扩展分配的 eMMC 存储容量。

<br/><br/><br/>

## 6.1 下载 Ubuntu 镜像
---
D3-G 的官方系统基于 Ubuntu 22.04。  
您可以在此处下载镜像文件。  

<img src="https://github.com/topst-development/Documentation/assets/161264431/83d93c78-6437-4f96-a0bf-23f22da1aba1">  

**下载 :**  
-	[点击此处下载](https://drive.google.com/file/d/1oc2qwaXUt6-QDME3s5WXKVHzAg4xqVyc/view?usp=drive_link)
<br>
-	有关更多信息，请访问我们的 [github 页面](https://github.com/topst-development)。

**发行说明 :**  

|Ver|   日期   |
|:-:|:--------:|
|1.0|2024.04.25|  

TOPST 团队还在准备其他官方 OS 版本。  
有关其他 OS 版本发布的信息，请参阅 TOPST 社区。  

<br/><br/><br/>

## 6.2 将固件上传到 D3-G
---
运行“fwdn_ubuntu.batch”文件。 
有关如何将 Ubuntu 镜像上传到 D3-G，请参阅第 5 章。
完成 FWDN 后，从 FWDN 端口拔下 USB Type-C 线缆并拔下电源线。 

<br/><br/><br/>

## 6.3 调整 eMMC 存储大小 (仅限 D3-G)
---
登录并启动开发板后，建议首先调整 eMMC 存储的大小。
请按照以下步骤调整 eMMC 存储大小。

1. 要修改分区大小和布局，请使用以下命令。
     ```
     $ parted
     ```

2. 扩展 GUID Partition Table(GPT)。 
    ```
    $ rescue
    $ Fix 
    $ 0 
    $ 100%
    ```
3. 使用 p (print) 命令检查分区类型是否为 ext4。 
   ```
   $ p
   ```
4. 调整分区 4 的大小。
    ```
    $ resizepart 4
    $ Yes
    $ 100%
    ```
5. 重新启动开发板。
6. 调整分区 4 上的 ext4 文件系统大小。
    ```
    $ resize2fs /dev/mmcblk0p4
    ```
7. 使用以下命令检查更改后的分区大小。
   ```
   $ df -h
   ```

调整大小后，您可以确认可用空间为 27GB。

<br/><br/><br/><br/>

# 7. 参考资料
---
- 有关更多详细信息，请联系 TOPST：topst@topst.ai

**注意：** 参考文档可根据合同条款在可提供时提供。如果参考
文档无法提供，则可就与您的开发直接相关的内容提供指导。
