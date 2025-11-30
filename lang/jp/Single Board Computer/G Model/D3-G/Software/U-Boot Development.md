# 1. はじめに
---
このドキュメントでは、U-Bootを使用した組み込みシステムの回復、initramfsを使用した起動、およびrootパスワードのリセットに関するガイドラインを提供します。

このガイドでは、次のトピックについて説明します。

- U-Boot回復の原則

- USBとinitramfsを使用した起動

- eMMCパーティションのマウント

- rootパスワードのリセット手順

<br/><br/><br/><br/>

# 2. U-Boot回復の原則
---
eMMCファイルシステムから起動する代わりに、システムはU-Bootを使用してinitramfsイメージを介して起動されます。このアプローチは、ルートファイルシステムが破損しているかアクセスできない場合に特に役立ちます。システムがinitramfsで起動した後、eMMCルートファイルシステムがマウントされ、管理者はファイルの変更や資格情報のリセットなどの回復タスクを実行できます。
</br><br/><br/><br/>

# 3. U-Bootとinitramfsを使用した起動
---
U-Bootは、起動可能なイメージ (initramfsやdtbなど) をメモリにロードし、それらを実行してシステムを初期化するブートローダーです。

回復シナリオでは、ルートファイルシステムの代わりにinitramfsを使用してシステムを起動できるため、システムアクセスのための独立した環境が提供されます。

<br/><br/><br/>

## 3.1 起動可能なUSBの準備
---
- USBメモリスティックをext4としてフォーマットします

- D3-G YPビルド出力がある次のディレクトリに移動します。

     : {build/d3-g-topst-main/tmp/deploy/images/d3-g-topst-main}

- 次の2つのファイルをUSBメモリスティックにコピーします

  -  Image-initramfs--5.10.205-r0-d3-g-topst-main-{build_date}.bin

  -  tcc8050-topst-d3-g--5.10.205-r0-d3-g-topst-main-{build_date}.dtb


## 3.2 U-Bootモードでの起動手順
---
USBをD3-Gに挿入し、電源を入れます。U-Bootモードに入り、次のコマンドを実行します。

**u-bootモードに入るには、デバイスの電源を入れ、3秒以内にEnterキーを押します。**

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
booti 0x20000000 - 0x30000000を介してu-boot環境でLinuxカーネルイメージを起動します。
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

# 4. rootパスワードのリセット
---
initramfsシェルに入ったら、次の手順に従ってeMMCをマウントし、保存されているrootパスワードをリセットします。


## 4.1 eMMCパーティションのマウント
---
ルートファイルシステムパーティション (通常は /dev/mmcblk0p3) を一時的なマウントポイントにマウントします。

**lsblkまたはblkidを使用して、正しいパーティションを確認してください。**
```
$ mkdir -p /mnt/part3
$ mount /dev/mmcblk0p3 /mnt/part3
```

## 4.2 shadowファイルの変更
---
rootパスワードは、ハッシュ形式で /etc/shadow ファイルに保存されます。パスワードをクリアするには:

```
$ sed -i 's/###root passwd signature###//g' /mnt/part3/etc/shadow
```

## 4.3 完了と再起動
---
変更がディスクに書き込まれるようにするには:

```
$ sync
$ reboot
```
これで、パスワードなしでrootとしてログインし、passwdを使用して新しいパスワードを設定できます。

```
$ passwd
New password:
Retype new password:
passwd: password updated successfully
```