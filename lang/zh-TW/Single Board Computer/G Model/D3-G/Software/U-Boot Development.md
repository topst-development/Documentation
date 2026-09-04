# 1. 簡介
---
本文件說明如何使用 U-Boot 復原嵌入式系統、以 initramfs 開機，以及重設 root 密碼。

本指南涵蓋下列主題：

- U-Boot 復原原理

- 使用 USB 與 initramfs 開機

- 掛載 eMMC 分割區

- root 密碼重設程序

<br/><br/><br/><br/>

# 2. U-Boot 復原原理
---
系統並非從 eMMC 檔案系統開機，而是透過 U-Boot 使用 initramfs 映像檔啟動。當根檔案系統毀損或無法存取時，此方式特別有用。系統以 initramfs 啟動後，即可掛載 eMMC 根檔案系統，讓管理者執行修改檔案或重設認證資訊等復原作業。
</br><br/><br/><br/>

# 3. 使用 U-Boot 與 initramfs 開機
---
U-Boot 是一種開機載入程式，可將可開機映像檔（例如 initramfs 與 dtb）載入記憶體並執行，以初始化系統。 

在復原情境中，它可讓系統以 initramfs 取代根檔案系統開機，提供獨立的系統存取環境。

<br/><br/><br/>

## 3.1 準備可開機的 USB
---
- 將 USB 隨身碟格式化為 ext4

- 前往下列存放 D3-G YP 建置輸出的目錄：

     : {build/d3-g-topst-main/tmp/deploy/images/d3-g-topst-main}

- 將下列兩個檔案複製到 USB 隨身碟

  -  Image-initramfs--5.10.205-r0-d3-g-topst-main-{build_date}.bin

  -  tcc8050-topst-d3-g--5.10.205-r0-d3-g-topst-main-{build_date}.dtb


## 3.2 U-Boot 模式的開機步驟
---
請將 USB 插入 D3-G 並開機。進入 U-Boot 模式後執行下列指令：

**若要進入 u-boot 模式，請在裝置開機後 3 秒內按下 Enter 鍵。**

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
在 u-boot 環境中透過 booti 0x20000000 - 0x30000000 啟動 Linux 核心映像檔。
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

# 4. 重設 Root 密碼
---
進入 initramfs shell 後，請依下列步驟掛載 eMMC 並重設已儲存的 root 密碼。


## 4.1 掛載 eMMC 分割區
---
請將根檔案系統分割區（通常為 /dev/mmcblk0p3）掛載至暫時的掛載點：

**請務必使用 lsblk 或 blkid 確認正確的分割區。**
```
$ mkdir -p /mnt/part3
$ mount /dev/mmcblk0p3 /mnt/part3
```

## 4.2 修改 shadow 檔案
---
root 密碼以雜湊形式儲存於 /etc/shadow 檔案中。若要清除密碼：

```
$ sed -i 's/###root passwd signature###//g' /mnt/part3/etc/shadow
```

## 4.3 完成並重新開機
---
為確保變更已寫入磁碟：

```
$ sync
$ reboot
```
現在您可以不需密碼即以 root 身分登入，並使用 passwd 設定新密碼。

```
$ passwd
New password:
Retype new password:
passwd: password updated successfully
```