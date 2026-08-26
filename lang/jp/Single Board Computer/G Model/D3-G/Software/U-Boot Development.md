# 1. はじめに
---
本書では、U-Boot を使用した組み込みシステムの復旧、initramfs による起動、および root パスワードのリセットに関するガイドラインを説明します。

本ガイドでは、次の項目を扱います:

- U-Boot 復旧の原理

- USB と initramfs を使用した起動

- eMMC パーティションのマウント

- root パスワードのリセット手順

<br/><br/><br/><br/>

# 2. U-Boot 復旧の原理
---
eMMC ファイルシステムから起動する代わりに、U-Boot を使用して initramfs イメージ経由でシステムを起動します。この方法は、ルートファイルシステムが破損している場合やアクセスできない場合に特に有効です。システムが initramfs で起動した後、eMMC のルートファイルシステムをマウントすることで、管理者はファイルの変更や認証情報のリセットなどの復旧作業を実行できます。
</br><br/><br/><br/>

# 3. U-Boot と initramfs による起動
---
U-Boot は、起動可能なイメージ (initramfs や dtb など) をメモリにロードして実行し、システムを初期化するブートローダです。 

復旧のシナリオでは、ルートファイルシステムの代わりに initramfs でシステムを起動できるようにし、システムにアクセスするための独立した環境を提供します。

<br/><br/><br/>

## 3.1 起動可能な USB の準備
---
- USB メモリスティックを ext4 でフォーマットします

- D3-G の YP ビルド出力が配置されている次のディレクトリに移動します:

     : {build/d3-g-topst-main/tmp/deploy/images/d3-g-topst-main}

- 次の 2 つのファイルを USB メモリスティックにコピーします

  -  Image-initramfs--5.10.205-r0-d3-g-topst-main-{build_date}.bin

  -  tcc8050-topst-d3-g--5.10.205-r0-d3-g-topst-main-{build_date}.dtb


## 3.2 U-Boot モードでの起動手順
---
USB を D3-G に挿入して電源を入れます。U-Boot モードに入り、次のコマンドを実行してください:

**u-boot モードに入るには、デバイスの電源を入れてから 3 秒以内に enter キーを押してください。**

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
u-boot 環境で booti 0x20000000 - 0x30000000 により Linux カーネルイメージを起動します。
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

# 4. root パスワードのリセット
---
initramfs のシェルに入ったら、以下の手順に従って eMMC をマウントし、保存されている root パスワードをリセットしてください。


## 4.1 eMMC パーティションのマウント
---
ルートファイルシステムのパーティション (通常は /dev/mmcblk0p3) を一時的なマウントポイントにマウントします:

**lsblk または blkid を使用して、正しいパーティションであることを必ず確認してください。**
```
$ mkdir -p /mnt/part3
$ mount /dev/mmcblk0p3 /mnt/part3
```

## 4.2 shadow ファイルの変更
---
root パスワードは /etc/shadow ファイルにハッシュ化された形式で保存されています。パスワードを消去するには、次を実行します:

```
$ sed -i 's/###root passwd signature###//g' /mnt/part3/etc/shadow
```

## 4.3 仕上げと再起動
---
変更内容をディスクに確実に書き込むには、次を実行します:

```
$ sync
$ reboot
```
これで、パスワードなしで root としてログインでき、passwd を使用して新しいパスワードを設定できます。

```
$ passwd
New password:
Retype new password:
passwd: password updated successfully
```