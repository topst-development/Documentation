# Environment Setting 

## Ubuntu Installation

Since TOPST is based on the Yocto Project, the supported Linux version
follows the Yocto.

You can install another version of Linux, but in this document, TOPST is
described based on Ubuntu.

Linux distribution version:

- Ubuntu 20.04 (LTS) and above

- <https://releases.ubuntu.com/20.04/>

You can download it by clicking "64-bit PC (AMD64) desktop image" as
shown in figure 2.1.

<img src="https://github.com/topst-development/Documentation/blob/Tsolutions/TOPST-AI/Software/media/Enviroment Setting.image1.png"
style="width:5.42479in;height:3.48958in" />

Figure 1.1 Ubuntu Installation

## Virtual Machine Installation

Install virtual machines, such as VMware and Virtualbox, to create an
Ubuntu development environment.

### Create Virtual Server

This section describes how to use virtualbox.

1.  Download VirtualBox and install
    (<https://www.virtualbox.org/wiki/Downloads>)

<img src="https://github.com/topst-development/Documentation/blob/Tsolutions/TOPST-AI/Software/media/Enviroment Setting.image2.png"
style="width:3.768in;height:1.18559in" />

Figure 1.2 Download VirtualBox for Virtual Server

2.  Download Ubuntu image in Chapter 2.1 described.

3.  Run “Oracle VM VirtualBox”

4.  Click “New Icon” as shown in Figure 2.3

<img src="https://github.com/topst-development/Documentation/blob/Tsolutions/TOPST-AI/Software/media/Enviroment Setting.image3.png"
style="width:2.17708in;height:0.62708in" />

Figure 1.3 Create New Virtual Machine

### Configuration Virtual Machine

1.  Fill in the appropriate details:

- Name: If you include the word Ubuntu in your name the Type and Version
  will auto-update.

- Machine Folder: This is where your virtual machines will be stored so
  you can resume working on them whenever you like.

- ISO Image: Here you need to add a link to the ISO you downloaded from
  the Ubuntu website.

<img src="https://github.com/topst-development/Documentation/blob/Tsolutions/TOPST-AI/Software/media/Enviroment Setting.image4.png"
style="width:5.64583in;height:2.75069in"
alt="텍스트, 스크린샷, 식물, 웹 페이지이(가) 표시된 사진 자동 생성된 설명" />

Figure 1.4 Configuration Virtual Machine(1)

5.  Create a user profile.

> To enable the automatic install, we need to prepopulate our username
> and password here in addition to our machine name so that it can be
> configured automatically during first boot.

The default credentials are:

- Username: vboxuser

- Password: changeme

It is important to change these values since the defaults will create a
user without sudo access.

Ensure your Hostname has no spaces to proceed!

<img src="https://github.com/topst-development/Documentation/blob/Tsolutions/TOPST-AI/Software/media/Enviroment Setting.image5.png"
style="width:5.64567in;height:2.75197in" />

Figure 1.5 Configuration Virtual Machine(2)

> It is also recommended to check the Guest Additions box to install the
> default Guest Additions ISO that is downloaded as part of VirtualBox.
> Guest additions enables a number of quality of life features such as
> changing resolution and dynamic screen resizing so it is highly
> recommended!

6.  Define the Virtual Machine’s resources (Processors and Memory)

> In the next section we can specifiy how much of our host machine’s
> memory and processors the virtual machine can use. For good
> performance it’s recommended to provide your VM with around 8GB of RAM
> (althought 4GB will still be usable) and 4 CPUs. Try to remain in the
> green areas of each slider to prevent issues with your machine running
> both the VM and the host OS.

<img src="https://github.com/topst-development/Documentation/blob/Tsolutions/TOPST-AI/Software/media/Enviroment Setting.image6.png"
style="width:5.64514in;height:2.75139in"
alt="텍스트, 스크린샷, 웹 페이지, 소프트웨어이(가) 표시된 사진 자동 생성된 설명" />

**Figure 1.6 Configuration Virtual Machine(3)**

7.  Define the Virtual Machine’s resources (Hard disk)

> Then we need to specify the size of the hard disc for the virtual
> machine. For Ubuntu we recommend around 25 GB as a minimum.(SDK Build
> Size is 80GB.) By default the hard disk will scale dynamically as more
> memory is required up to the defined limit. If you want to
> pre-allocate the full amount, check the ‘Pre-allocate Full Size’ check
> box. This will improve performance but may take up unnecessary space.

<img src="https://github.com/topst-development/Documentation/blob/Tsolutions/TOPST-AI/Software/media/Enviroment Setting.image7.png"
style="width:5.64514in;height:2.75139in"
alt="텍스트, 스크린샷, 웹 페이지, 소프트웨어이(가) 표시된 사진 자동 생성된 설명" />

**Figure 1.7 Configuration Virtual Machine(4)**

8.  Check the summary of your machine settings and click finish.

<img src="https://github.com/topst-development/Documentation/blob/Tsolutions/TOPST-AI/Software/media/Enviroment Setting.image8.png"
style="width:5.64567in;height:2.75197in"
alt="텍스트, 스크린샷, 소프트웨어, 웹 페이지이(가) 표시된 사진 자동 생성된 설명" />

Figure 1.8 Configuration Virtual Machine(5)

9.  If the configuration is complete, launch the virtual machine.

    <img src="https://github.com/topst-development/Documentation/blob/Tsolutions/TOPST-AI/Software/media/Enviroment Setting.image9.png"
    style="width:5.68546in;height:1.64583in" />

    Figure 1.9 Configuration Virtual Machine(6)

## Setting Linux Environment

### Install SSH and Samba 

Working in a Linux environment is slow, but you can use SSH and Samba to
work in a much more convenient environment. SSH and

Samba allows you to execute commands on remote computers and copy files
to other computers.

If SSH and Samba are already installed or you will not use them, you can
skip this chapter.

| \$ sudo apt-get install -y net-tools openssh-server samba |
|-----------------------------------------------------------|

After downloading SSH and Samba, you should set each program to your
environment.

### Install Utilities for Yocto Project 

Install the utilities at once. To use Yocto Project, the following
utilities must be installed on Host System (individual computer or

development server).

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>$ sudo apt-get install -y gawk wget git-core diffstat unzip
texinfo gcc-multilib</p>
<p>$ sudo apt-get install -y build-essential chrpath socat cpio python3
python3-pip python3-pexpect</p>
<p>$ sudo apt-get install -y xz-utils debianutils iputils-ping
python3-git python3-jinja2 libegl1-mesa libsdl1.2-dev pylint3
xterm</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

### Install Repo

You can download TOPST AI SDK through Repo.

To install the repo, refer to the following website:
<https://source.android.com/source/downloading.html>

If repo is already installed, you can use it without re-installation.

Before installing repo, the installed Python version (3.6 or higher)
should be properly set.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>$ sudo ln -sf /usr/bin/python3 /usr/bin/python</p>
<p>$ sudo apt-get install repo</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

If there is a repo error, download the latest version and put it
directly into /usr/bin/ the folder.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>$ mkdir -p ~/bin</p>
<p>$ curl
http://commondatastorage.googleapis.com/git-repo-downloads/repo &gt;
~/bin/repo</p>
<p>$ chmod a+x ~/bin/repo</p>
<p>$ sudo mv ~/bin/repo /usr/bin/repo</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>
