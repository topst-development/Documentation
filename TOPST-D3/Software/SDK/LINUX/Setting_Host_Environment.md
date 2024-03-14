#  Setting Host Environment

## 1.1 Ubuntu Installation

Since TOPST D3 Linux SDK is based on the Yocto Project, Linux version of TOPST D3 SDK follows the Yocto project.

You can install another version of Linux, but in this document, TOPST D3 Linux SDK is described based on Ubuntu ([https://releases.ubuntu.com](https://releases.ubuntu.com/)).

Linux distribution version:

- Ubuntu 18.04 (LTS)
- Ubuntu 20.04 (LTS)
- Ubuntu 22.04 (LTS)

<p align="center">
    <img src="https://github.com/Topst-Dev/Documentation/assets/161264431/4c025c5b-9709-4242-b053-fdb3742e01d1">
</p>
<p align="center"><strong>Figure 1.1 Ubuntu Installation</strong></p>

## 1.2 Virtual Machine Installation

After Downloading of Ubuntu completed, Install virtual machines, such as ***VMware*** and ***Virtualbox***, to create an Ubuntu development environment.

### 1.2.1 Create Virtual Server

1. Select one of the Ubuntu versions described in Chapter 1.1.
<p align="center">
   <img src="https://github.com/Topst-Dev/Documentation/assets/144076415/366bbdfa-6b1f-4fc7-a168-e7c3d8542d41" width="500" height="400">
</p>
<p align="center"><strong>Figure 1.2 Select Ubuntu image</strong></p>  

2. Enter the name and password you want.  
<p align="center">
   <img src="https://github.com/Topst-Dev/Documentation/assets/144076415/59a33d1f-2634-4cd5-9ac7-081d7365bf59" width="500" height="400">
</p>
<p align="center"><strong>Figure 1.3 Enter the name and password</strong></p>  

3. Enter the name of the virtual machine you want.
<p align="center">
   <img src="https://github.com/Topst-Dev/Documentation/assets/144076415/366bbdfa-6b1f-4fc7-a168-e7c3d8542d41" width="500" height="400">
</p>
<p align="center"><strong>Figure 1.4 Enter the Virtual machine name</strong>  
    
4. Recommended capacity is 150 GB or more, 8 GB RAM, and 16 processors.

It is recommended that network adapter is set as Bridged.

<p align="center">
    <img src="https://github.com/Topst-Dev/Documentation/assets/144076415/366bbdfa-6b1f-4fc7-a168-e7c3d8542d41" width="500" height="400">
    <img src="https://github.com/Topst-Dev/Documentation/assets/144076415/59a33d1f-2634-4cd5-9ac7-081d7365bf59" width="500" height="400">
</p>

<p align="center">
    <img src="https://github.com/Topst-Dev/Documentation/assets/144076415/9ac6858f-c4c7-4c6d-907f-6aada1d59b96" width="500" height="400">
    <img src="https://github.com/Topst-Dev/Documentation/assets/144076415/5bc3cd34-d465-4698-81e0-bf7d00e17c98" width="500" height="400">
</p>

<p align="center">
    <img src="https://github.com/Topst-Dev/Documentation/assets/144076415/9625271c-2d11-42a9-9ac1-ed178de9f399" width="500" height="400">
    <img src="https://github.com/Topst-Dev/Documentation/assets/144076415/ff96ad69-39c2-445d-87b9-f5cdf8c3e8ee" width="500" height="400">
</p>
<p align="center"><strong>Figure 1.2 VMware Settings for Virtual Server</strong></p>

## 1.3 Setting Linux Environment

### 1.3.1 Install SSH and Samba

but you can use SSH and Samba to work in a much more convenient environment. SSH and Samba allows you to execute commands on remote computers and copy files to other computers.

If SSH and Samba are already installed or you will not use them, you can skip this chapter.

```bash
sudo apt install -y net-tools openssh-server samba
```


After downloading SSH and Samba, you should set each program to your environment.

### 1.3.2 Utilities

Install the utilities at once. To use Yocto Project, the following utilities must be installed on Host System (inpidual computer or development server).

```bash
sudo apt-get install -y gawk wget git diffstat unzip texinfo gcc-multilib build-essential chrpath

sudo apt-get install -y socat cpio python3 python3-pip python3-pexpect xz-utils debianutils

sudo apt-get install -y iputils-ping python3-git python3-jinja2 libegl1-mesa libsdl1.2-dev pylint

sudo apt-get install -y xterm zstd ncftp curl git-lfs vim
```


### 1.3.3 Install Repo

You can download TOPST D3 SDK through Android Repo.

To install Repo, refer to the following website: https://source.android.com/source/downloading.html.

If Repo is already installed, you can use it without re-installing.

Before installing Repo, the installed Python version (3.6 or higher) should be properly set.

```bash
sudo ln -sf /usr/bin/python3 /usr/bin/python

sudo apt-get install repo
```


If there is a Repo error, download the latest version and put it directly into the /usr/bin/ folder.

```bash
mkdir -p ~/bin

curl http://commondatastorage.googleapis.com/git-repo-downloads/repo > ~/bin/repo

chmod a+x ~/bin/repo

sudo mv ~/bin/repo /usr/bin/repo
```
