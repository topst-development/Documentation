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
$ git clone git@github.com:topst-development/ubuntu-rootfs
```

<br><br>

## 2.2. Procedure to create Ubuntu Root File System

The following describes the script to create the Ubuntu file system.

If you run the following script without setting the options, you can create an image based on the options that are already set.

1. Set the configuration to create the Ubuntu image.
2. Install Linux emulator on Linux Host PC.
3. Create the root file system directory.
4. Install Bootstrap.
5. Install Prebuild package.
6. Configure the root file system.
7. Install **<code>Weston GUI Launcher.</code></strong>
8. Create the Ubuntu Ext4 image.

<br><br>

## 2.3 create_ubuntu_jammy_arm64_rootfs.sh 

<br>

### 2.3.1. Script Usage 

The following is a description of script options.


```
$ ./create_ubuntu_jammy_arm64_rootfs.sh  --help
  
  Usage: create_ubuntu_jammy_arm64_rootfs.sh [options]"
  Options:"
   --help              Display this help message"
   --arch=ARCH         Architecture (arm64, armhf, amd64, i386)"
   --release=RELEASE   Ubuntu release (focal, bionic, xenial)"
   --mirror=MIRROR     Ubuntu mirror"
   --apt-file=APT_FILE Apt source list file"
   --prebuilt-fstab=PREBUILT_FSTAB Prebuilt fstab file"
   --image-size=IMAGE_SIZE Image size (in bytes)"
   --image-name=IMAGE_NAME Image name"
   --launcher=LAUNCHER_NAME (default is weston)
```

<br>

### 2.3.2. Default Settings for Options

The following is a description of script options. The default option is set to be the same as the option provided by the Ubuntu image.

**Caution:** The root file system partition size and image size of the TOPST system must be the same. Do not change the Ubuntu image size.


```
ARCH=${ARCH:-arm64}
RELEASE=${RELEASE:-jammy}
DEFAULT_MIRROR=http://ports.ubuntu.com/ubuntu-ports/
MIRROR=${MIRROR:-$DEFAULT_MIRROR}
DATE_TIME=$(date "+%Y%m%d-%H%M")
APT_DIR=apt
APT_FILE=${APT_FILE:-sources.list.ubuntu.port}
BUILD_DIR=build
TARGET_DIR="${BUILD_DIR}/rootfs"
# image size is 5GB
IMAGE_SIZE=${IMAGE_SIZE:-5368709120}
IMAGE_NAME=${IMAGE_NAME:-ubuntu-${RELEASE}-${ARCH}-${DATE_TIME}.img}
PREBUILT_FSTAB="fstab/fstab.ubuntu-jammy-arm64"
PREBUILT_DEB="prebuilt-deb"
```

<br>

### 2.3.3. Install Emulator on Linux Host PC

Install the emulator on the Host PC.


```
REQUIRED_PACKAGES="debootstrap qemu-user-static binfmt-support"

for package in $REQUIRED_PACKAGES; do
    if ! dpkg -s $package >/dev/null 2>&1; then
        echo "Installing $package..."
        sudo apt-get update
        sudo apt-get install -y $package
    fi
done
```

<br>

### 2.3.4. Create the Root File System Directory

Create the root file system directory.


```
BUILD_DIR=build
TARGET_DIR="${BUILD_DIR}/rootfs"

mkdir -p $TARGET_DIR
```

### 2.3.5. Run debootstrap

Install the Debian bootstrap in the root file system directory that you want to create.


```
RELEASE=${RELEASE:-jammy}
TARGET_DIR="${BUILD_DIR}/rootfs"
DEFAULT_MIRROR=http://ports.ubuntu.com/ubuntu-ports/
QEMU_ARCH=aarch64

# Run the first stage of debootstrap
sudo debootstrap --arch $ARCH --foreign $RELEASE $TARGET_DIR $DEFAULT_MIRROR

# Copy the qemu-aarch64-static binary to the rootfs
sudo cp /usr/bin/qemu-$QEMU_ARCH-static $TARGET_DIR/usr/bin

# Run the second stage of debootstrap
sudo chroot $TARGET_DIR /debootstrap/debootstrap --second-stage
```

<br>

### 2.3.6. Install Prebuilt Packages from .deb Files

Install the generated package (kernel and module) compiled from “_TOPST Development User Guide_”.


```
PREBUILT_DEB="prebuilt-deb"
TARGET_DIR="build/rootfs"

echo "Install prebuilt packages from .deb files"
sudo cp "$PREBUILT_DEB"/*.deb "$TARGET_DIR/tmp/"
sudo chroot "$TARGET_DIR" /bin/bash -c "dpkg -i --force-depends --force-bad-version /tmp/*.deb"

# Exception : Happend the module is removed by dependency checking when apt update.
sudo chroot "$TARGET_DIR" /bin/sh -c "sed -i 's/Depends: kernel-5.4.159-tcc/#Depends: kernel-5.4.159-tcc/g'  /var/lib/dpkg/status"

# systemd modules-load
sudo cp $PREBUILT_DEB/etc/modules-load.d/* $TARGET_DIR/etc/modules-load.d/
```

<br>

### 2.3.7. Configure rootfs

Set the following system functions to the root file system:

* Set up a source list for Advanced Package Tool (APT)
* Set up a name server to set a domain for a computer
* Set the user password
* Enable the SSH daemon
* Configure the Ethernet MAC Address
* Configure Netplan with Dynamic Host Configuration Protocol (DHCP)

```
APT_DIR=apt
APT_FILE="sources.list.ubuntu.port"
TARGET_DIR="build/rootfs"
RELEASE="-jammy"

# Add apt source list to the root filesystem
sudo cp $APT_DIR/$APT_FILE $TARGET_DIR/etc/apt/sources.list

# Configure the rootfs
sudo chroot $TARGET_DIR /bin/sh -c "echo 'nameserver 8.8.8.8' > /etc/resolv.conf"
sudo chroot $TARGET_DIR /bin/sh -c "echo 'nameserver 8.8.4.4' >> /etc/resolv.conf"
sudo chroot $TARGET_DIR /bin/sh -c "echo '$RELEASE' > /etc/hostname"
sudo chroot $TARGET_DIR /bin/sh -c "echo '127.0.1.1    $RELEASE' >> /etc/hosts"

# Configure the root password
sudo chroot $TARGET_DIR /bin/sh -c "echo 'root:root' | chpasswd"

# Add user named 'tospt' and make them a sudoer
sudo chroot $TARGET_DIR /bin/bash -c "useradd -m -G sudo -s /bin/bash topst"
sudo chroot $TARGET_DIR /bin/bash -c "echo 'topst:topst' | chpasswd"

# Install the openssh-server package
sudo chroot $TARGET_DIR /bin/sh -c "apt-get update && apt-get install -y \
openssh-server"

# Enable root login via ssh
sudo chroot $TARGET_DIR /bin/sh -c "sed -i 's/#PermitRootLogin \
prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config"

## Configure MAC Address
ip link set dev \$interface down
ip link set dev \$interface address \$prefix_mac
ip link set dev \$interface up

## Configure Netplan for dhcp
NETPLAN_CONFIG="99-default.yaml"
NETPLAN_DIR="/etc/netplan"
MAC_ADDR=$(openssl rand -hex 6 | sed 's/\(..\)/\1:/g; s/.$//')
sudo chroot $TARGET_DIR /bin/sh -c "cat > $NETPLAN_DIR/$NETPLAN_CONFIG << EOF
network:
version: 2
ethernets:
eth0:
dhcp4: true
optional: true
EOF"
```

<br>

### 2.3.8. Install Wayland Launcher

TOPST provides the GUI Launcher by using Weston Wayland.

```
echo "Install Weston-Wayland"
sudo cp application/install-weston.sh $TARGET_DIR/root
sudo chroot $TARGET_DIR /bin/bash -c "/root/install-weston.sh"
sudo rm -rf $TARGET_DIR/root/install-weston.sh
sudo cp application/TOPST-background.png $TARGET_DIR/usr/share/weston/
```

<br>

### 2.3.9. Create Ext4 Image

Create a root file system image with the settings shown above in Chapters 2.3.1 to 2.3.8. Use the generated image as the root file system when using the main core (CA72).


```
echo "Creating $IMAGE_NAME with size $IMAGE_SIZE bytes"
dd if=/dev/zero of=$IMAGE_NAME bs=1 count=0 seek=$IMAGE_SIZE
sudo mkfs.ext4 -F $IMAGE_NAME
```
<br><br>

# 3. Execute Script

```
$ ./create_ubuntu_jammy_arm64_rootfs.sh
Creating the rootfs directory
Running debootstrap first stage
[sudo] password for ben: 
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
                   ㆍ
                   ㆍ
                   ㆍ
```


<br><br>

# 4. FWDN Guide

You can download Ubuntu images by using the **_FWDN_** Command Line Interface (CLI) tool in your Windows Host PC environment as shown below.

For more information on **_FWDN_**, refer to “Frimware_Download.md".

<br><div align="center">
    <img src="https://github.com/Topst-Dev/Documentation/assets/16188136/b5edc72b-c1b5-4762-a758-243aed1cb921" alt="Figure 1.1 TOPST Debugging Board" >
    <p><strong>Figure 4.1 FWDN CLI</strong></p>
</div><br>

<br><br>


# 5. Booted Ubuntu GUI Screen

When you boot after downloading, you will see the screen of the Weston Wayland Launcher loaded with the Ubuntu image as shown below.

* Description: Ubuntu 22.04.2 LTS
* Release: 22.04
* Codename: jammy


<br><div align="center">
    <img src="https://github.com/Topst-Dev/Documentation/assets/16188136/0633a9c2-af8f-472e-97c3-26b34a5c5aa4" alt="Figure 1.1 TOPST Debugging Board" >
    <p><strong>Figure 5.1 Ubuntu Launcher</strong></p>
</div><br>
