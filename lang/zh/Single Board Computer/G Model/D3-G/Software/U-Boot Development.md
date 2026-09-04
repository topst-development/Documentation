# 1. 简介
---
本文档提供了使用 U-Boot 恢复嵌入式系统、通过 initramfs 启动以及重置 root 密码的指南。

本指南涵盖以下主题：

- U-Boot 恢复原理

- 使用 USB 和 initramfs 启动

- 挂载 eMMC 分区

- root 密码重置步骤

<br/><br/><br/><br/>

# 2. U-Boot 恢复原理
---
系统不从 eMMC 文件系统启动，而是通过 U-Boot 使用 initramfs 映像启动。当根文件系统损坏或无法访问时，该方法尤其有用。系统启动进入 initramfs 后，挂载 eMMC 根文件系统，管理员即可执行修改文件或重置凭据等恢复操作。
</br><br/><br/><br/>

# 3. 使用 U-Boot 和 initramfs 启动
---
U-Boot 是一种引导加载程序，它将可启动映像（例如 initramfs 和 dtb）加载到内存中并执行，以初始化系统。 

在恢复场景中，它使系统能够以 initramfs 而非根文件系统启动，从而提供一个独立的系统访问环境。

<br/><br/><br/>

## 3.1 准备可启动 USB
---
- 将 USB 存储盘格式化为 ext4

- 进入 D3-G YP 构建输出所在的以下目录：

     : {build/d3-g-topst-main/tmp/deploy/images/d3-g-topst-main}

- 将以下两个文件复制到 USB 存储盘

  -  Image-initramfs--5.10.205-r0-d3-g-topst-main-{build_date}.bin

  -  tcc8050-topst-d3-g--5.10.205-r0-d3-g-topst-main-{build_date}.dtb


## 3.2 U-Boot 模式下的启动步骤
---
将 USB 插入 D3-G 并接通电源。进入 U-Boot 模式并执行以下命令：

**要进入 u-boot 模式，请接通设备电源并在 3 秒内按下 enter 键。**

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
=> ext4load usb 0:1 0x20000000 /Image-initramfs--5.10.205-r0-d3-g-topst-main-{build_date}.bin
21069832 bytes read in 678 ms (29.6 MiB/s)
=> ext4load usb 0:1 0x30000000 /tcc8050-topst-d3-g--5.10.205-r0-d3-g-topst-main-{build_date}.dtb
97110 bytes read in 5 ms (18.5 MiB/s)
=> booti 0x20000000 - 0x30000000
```
在 u-boot 环境中通过 booti 0x20000000 - 0x30000000 启动 Linux 内核映像。
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

# 4. 重置 root 密码
---
进入 initramfs shell 后，请按照以下步骤挂载 eMMC 并重置已存储的 root 密码。


## 4.1 挂载 eMMC 分区
---
将根文件系统分区（通常为 /dev/mmcblk0p3）挂载到临时挂载点：

**请务必使用 lsblk 或 blkid 确认正确的分区。**
```
$ mkdir -p /mnt/part3
$ mount /dev/mmcblk0p3 /mnt/part3
```

## 4.2 修改 shadow 文件
---
root 密码以哈希形式存储在 /etc/shadow 文件中。要清除该密码，请执行：

```
$ sed -i 's/###root passwd signature###//g' /mnt/part3/etc/shadow
```

## 4.3 完成并重启
---
为确保更改写入磁盘，请执行：

```
$ sync
$ reboot
```
现在您可以无需密码以 root 身份登录，并使用 passwd 设置新密码。

```
$ passwd
New password:
Retype new password:
passwd: password updated successfully
```