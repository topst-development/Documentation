# 1. Introduction
---
This document provides guidelines for recovering the embedded system using U-Boot, booting with initramfs, and resetting the root password.

This guide covers the following topics:

- U-Boot Recovery Principle

- Booting using USB and initramfs

- Mounting eMMC partitions

- Root password reset procedure

<br/><br/><br/><br/>

# 2. U-Boot Recovery Principle
---
Instead of booting from the eMMC file system, the system is started via an initramfs image using U-Boot. This approach is especially useful when the root file system is corrupted or inaccessible. After the system is booted into initramfs, the eMMC root file system is mounted, allowing administrators to perform recovery tasks, such as modifying files or resetting credentials.
</br><br/><br/><br/>

# 3. Booting with U-Boot and initramfs
---
U-Boot is a bootloader that loads bootable images (such as initramfs and dtb) into memory and executes them to initialize the system. 

In recovery scenarios, it allows the system to boot with initramfs instead of the root file system, providing an independent environment for system access.

<br/><br/><br/>

## 3.1 Prepare Bootable USB
- Format a USB memory stick as ext4

- Copy the following files to the USB:

  -  initramfs (built for D3-G)

  -  d3g.dtb (compiled device tree blob)

## 3.2 Boot Steps in U-Boot Mode

Insert the USB into the D3-G and power it on. Enter U-Boot mode and execute the following commands:

```
=>
=>
=> usb start
starting USB...
Bus ehci@11A00000: USB EHCI 1.00
Bus ehci_mux@11900000: USB EHCI 1.00
Bus dwc3: Register 2000140 NbrPorts 2
Starting the controller
USB XHCI 1.10
scanning bus ehci@11A00000 for devices... 1 USB Device(s) found
scanning bus ehci_mux@11900000 for devices... 1 USB Device(s) found
scanning bus dwc3 for devices... 2 USB Device(s) found
       scanning usb for storage devices... 1 Storage Device(s) found
=> usb storage
  Device 0: Vendor: SanDisk Rev: 1.00 Prod: Cruzer Blade
            Type: Removable Hard Disk
            Capacity: 29340.0 MB = 28.6 GB (60088320 x 512)
=> ext4load usb 0:1 0x20000000 /initramfs
21069832 bytes read in 678 ms (29.6 MiB/s)
=> ext4load usb 0:1 0x30000000 /d3g.dtb
97110 bytes read in 5 ms (18.5 MiB/s)
=> booti 0x20000000 - 0x30000000
```

<br/><br/><br/><br/>

# 4. Resetting Root Password
---
Once in the initramfs shell, follow the steps below to reset the root password stored in the eMMC.


## 4.1 Mount eMMC Partition
Mount the root filesystem partition (commonly /dev/mmcblk0p4) to a temporary mount point:

```
$ mkdir -p /mnt/part4
$ mount /dev/mmcblk0p4 /mnt/part4
```

## 4.2 Modify shadow File

The root password is stored in hashed form in the /etc/shadow file. To clear the password:

```
$ sed -i 's/$1$U8sW0tMW$vLdJQg290HdAcqkJe1`dMM1//g' /mnt/part4/etc/shadow
```

## 4.3 Finalize and Reboot
To ensure changes are written to disk:

```
$ sync
$ reboot
```
You can now log in as root without a password and use passwd to set a new one.