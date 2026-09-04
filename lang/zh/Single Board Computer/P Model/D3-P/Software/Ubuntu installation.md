# 1. 简介
本文档介绍如何在 TOPST D3（开放平台开发板）的主核心（CA72）中开发 Ubuntu 环境。除开发板上提供的原生 Ubuntu 映像外，本文档还介绍如何开发您自己的专用 Ubuntu 环境。用户创建的 ubuntu 文件系统可以通过 **_FWDN_** 工具下载到主核心（CA72）的文件系统区域。

本文档按以下顺序进行说明：
* Ubuntu 文件系统创建指南
* FWDN 指南
* 启动后的 Ubuntu GUI 画面 
  
<br><br>

# 2. Ubuntu 文件系统创建指南

本章介绍如何在 Host PC 上为主核心（CA72）安装 Ubuntu 文件系统。

有关用户的开发环境，请参考“Documentation/TOPST-D3/Software/SDK/LINUX”。

<br><br>

## 2.1. 使用 Git 获取 Ubuntu
Git 提供的 Ubuntu 版本如下所示，为 Ubuntu 22.04.2 LTS (Jammy Jellyfish)。

```
$ git clone https://gitlab.com/topst.ai/topst-d3-ubuntu.git
```

<br><br>

# 3. 执行脚本


运行 'populate_ubuntu.sh'。
```
$ sudo ./populate_ubuntu.sh 
[!] Prepare workspace
[!] Initial debian bootstraping
I: Retrieving InRelease 
I: Checking Release signature
I: Valid Release signature (key id F6ECB3762474EDA9D21B7022871920D1991BC93C)
I: Retrieving Packages 
I: Validating Packages 
I: Resolving dependencies of required packages...
I: Resolving dependencies of base packages...
I: Checking component main on http://ports.ubuntu.com/ubuntu-ports...
I: Retrieving adduser 3.118ubuntu5
I: Validating adduser 3.118ubuntu5
I: Retrieving apt 2.4.5
I: Validating apt 2.4.5
I: Retrieving apt-utils 2.4.5
I: Validating apt-utils 2.4.5
I: Retrieving base-files 12ubuntu4
I: Validating base-files 12ubuntu4
I: Retrieving base-passwd 3.5.52build1
I: Validating base-passwd 3.5.52build1
I: Retrieving bash 5.1-6ubuntu1
I: Validating bash 5.1-6ubuntu1
I: Retrieving bsdutils 1:2.37.2-4ubuntu3
I: Validating bsdutils 1:2.37.2-4ubuntu3
I: Retrieving ca-certificates 20211016
I: Validating ca-certificates 20211016
I: Retrieving console-setup 1.205ubuntu3
I: Validating console-setup 1.205ubuntu3
I: Retrieving console-setup-linux 1.205ubuntu3
I: Validating console-setup-linux 1.205ubuntu3
I: Retrieving coreutils 8.32-4.1ubuntu1
I: Validating coreutils 8.32-4.1ubuntu1
I: Retrieving cron 3.0pl1-137ubuntu3
I: Validating cron 3.0pl1-137ubuntu3
I: Retrieving dash 0.5.11+git20210903+057cd650a4ed-3build1
I: Validating dash 0.5.11+git20210903+057cd650a4ed-3build1
I: Retrieving dbus 1.12.20-2ubuntu4

                   ㆍ
                   ㆍ
                   ㆍ
```
您可以在下面查看 etx4 文件。
```
$ ls
populate_ubuntu.sh  src  ubuntu.ext4
```


