# 1. Introduction
This document describes how to develop the Ubuntu environment in the main core (CA72) of the TOPST D3 (Open platform board). In addition to the native Ubuntu image provided on the board, this document describes how to develop your own specialized Ubuntu environment. User-created ubuntu file systems can be downloaded to the file system area of the main core (CA72) by using the **_FWDN_** tool.

This document is described in the following order:
* Ubuntu File System Creation Guide
* FWDN Guide
* Booted Ubuntu GUI Screen 
  
<br><br>

# 2. Ubuntu File System Creation Guide

This chapter describes how to install the Ubuntu file system for the main core (CA72) on the Host PC.

Refer to “Documentation/TOPST-D3/Software/SDK/LINUX” for the user's development environment.

<br><br>

## 2.1. Get Ubuntu with Git
The Ubuntu version provided by Git is Ubuntu 22.04.2 LTS (Jammy Jellyfish) as shown below.

```
$ git clone https://gitlab.com/topst.ai/topst-d3-ubuntu.git
```

<br><br>

# 3. Execute Script

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



