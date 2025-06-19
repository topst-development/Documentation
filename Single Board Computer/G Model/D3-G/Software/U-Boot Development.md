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
Instead of boot from the eMMC file system, the system is started via an initramfs image using U-Boot. This approach is especially useful when the root file system is corrupted or inaccessible. After the system is booted into initramfs, the eMMC root file system is mounted, allowing administrators to perform recovery tasks, such as modifying files or resetting credentials.
</br><br/><br/><br/>

# 3. Booting with U-Boot and initramfs
---
U-Boot is a bootloader that loads bootable images (such as initramfs and dtb) into memory and executes them to initialize the system. 

In recovery scenarios, it allows the system to boot with initramfs instead of the root file system, providing an independent environment for system access.

<br/><br/><br/>

## 3.1 Prepare Bootable USB
---
- Format a USB memory stick as ext4

- Navigate to the following directory where the D3-G YP build output is located:

     : {build/d3-g-topst-main/tmp/deploy/images/d3-g-topst-main}

- Copy the following two files to a USB memory stick

  -  Image-initramts--5.10.205-r0-d3-g-topst-main-{build_date}.bin

  -  tcc8050-topst-d3-g--5.10.205-r0-d3-g-topst-main-{build_data}.dtb


## 3.2 Boot Steps in U-Boot Mode
---
Insert the USB into the D3-G and power it on. Enter U-Boot mode and execute the following commands:

**To enter u-boot mode, power on the device and press enter within 3 seconds.**

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
=> ext4load usb 0:1 0x20000000 /Image-initramts--5.10.205-r0-d3-g-topst-main-{build_date}.bin
21069832 bytes read in 678 ms (29.6 MiB/s)
=> ext4load usb 0:1 0x30000000 /tcc8050-topst-d3-g--5.10.205-r0-d3-g-topst-main-{build_data}.dtb
97110 bytes read in 5 ms (18.5 MiB/s)
=> booti 0x20000000 - 0x30000000
```
Boot the Linux kernel image in the u-boot environment via booti 0x20000000 - 0x30000000.
```
[8.560615] IPVS: Registered protocols ()
[8.565843] IPVS: Connection hash table configured (size=4096, memory=32Kbytes)
[8.575847] IPVS: ipvs loaded.
[8.581231] NET: Registered protocol family 10
[8.590681] Segment Routing with IPv6
[8.593723] sit: IPv6, IPv4 and MPLS over IPv4 tunneling driver
[8.601037] NET: Registered protocol family 17
[8.608263] Bridge firewalling registered
[8.614380] Loading compiled-in X.509 certificates
[8.621180] debug_vm_pgtable: [debug_vm_pgtable        ]: Validating architecture page table helpers
[8.630343] Btrfs loaded, crc32c=crc32c-generic
[8.648452] cfg80211: Loading compiled-in X.509 certificates for regulatory database
[8.660142] cfg80211: Loaded X.509 cert 'sforshee: 00b28dd47aef9cea7'
[8.668043] platform regulatory.0: Direct firmware load for regulatory.db failed with error -2
[8.679621] cfg80211: failed to load regulatory.db
[8.694746] ALSA device list:
[8.694746]   #0: TCC805x EVM Card
[8.703987] tcc-uart-p[011 16600000.serial: no DMA platform data
[8.705060] [INFO][PL011][UART0] baud_rate 115200, uart_clk 24000000
[8.715421] Freeing unused kernel memory: 4160K
[8.715536] scsi 0:0:0:0: Direct-Access     SanDisk  Cruzer Blade     1.00 PQ: 0 ANSI: 6
[8.733979] sd 0:0:0:0: Attached scsi generic sg0 type 0
[8.734972] sd 0:0:0:0: [sda] 60088320 512-byte logical blocks: (30.8 GB/28.7 GiB)
[8.752128] sd 0:0:0:0: [sda] Write Protect is off
[8.759421] sd 0:0:0:0: [sda] Mode Sense: 43 00 00 00
[8.764487] sd 0:0:0:0: [sda] Write cache: disabled, read cache: enabled, doesn't support DPO or FUA
[8.774482] Run /init as init process
[8.785700] ======= set rootfs partition failed ======
/bin/sh: can't access tty; job control turned off
[    8.801293] sd 0:0:0:0: [sda] Attached SCSI removable disk
```

<br/><br/><br/><br/>

# 4. Resetting Root Password
---
Once you are in the initramfs shell, follow the steps below to mount eMMC and reset the stored root password.


## 4.1 Mount eMMC Partition
---
Mount the root filesystem partition (commonly /dev/mmcblk0p3) to a temporary mount point:

**Be sure to verify the correct partition using lsblk or blkid.**
```
$ mkdir -p /mnt/part3
$ mount /dev/mmcblk0p3 /mnt/part3
```

## 4.2 Modify shadow File
---
The root password is stored in hashed form in the /etc/shadow file. To clear the password:

```
$ sed -i 's/###root passwd signagure###//g' /mnt/part4/etc/shadow
```

## 4.3 Finalize and Reboot
---
To ensure changes are written to disk:

```
$ sync
$ reboot
```
You can now log in as root without a password and use passwd to set a new one.

```
$ passwd
New password:
Retype new password:
passwd: password updated successfully
```