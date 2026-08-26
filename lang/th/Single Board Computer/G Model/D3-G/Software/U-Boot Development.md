# 1. บทนำ
---
เอกสารนี้ให้แนวทางสำหรับการกู้คืนระบบฝังตัวด้วย U-Boot การบูตด้วย initramfs และการรีเซ็ตรหัสผ่าน root

คู่มือนี้ครอบคลุมหัวข้อต่อไปนี้:

- หลักการกู้คืนด้วย U-Boot

- การบูตโดยใช้ USB และ initramfs

- การเมานต์พาร์ทิชัน eMMC

- ขั้นตอนการรีเซ็ตรหัสผ่าน root

<br/><br/><br/><br/>

# 2. หลักการกู้คืนด้วย U-Boot
---
แทนที่จะบูตจากระบบไฟล์บน eMMC ระบบจะถูกเริ่มต้นผ่านอิมเมจ initramfs โดยใช้ U-Boot วิธีนี้มีประโยชน์อย่างยิ่งเมื่อระบบไฟล์รูทเสียหายหรือไม่สามารถเข้าถึงได้ หลังจากระบบบูตเข้าสู่ initramfs แล้ว จะมีการเมานต์ระบบไฟล์รูทบน eMMC ทำให้ผู้ดูแลระบบสามารถดำเนินการกู้คืน เช่น การแก้ไขไฟล์หรือการรีเซ็ตข้อมูลรับรองได้
</br><br/><br/><br/>

# 3. การบูตด้วย U-Boot และ initramfs
---
U-Boot เป็นบูตโหลดเดอร์ที่โหลดอิมเมจที่บูตได้ (เช่น initramfs และ dtb) เข้าสู่หน่วยความจำและสั่งประมวลผลเพื่อเริ่มต้นระบบ 

ในสถานการณ์การกู้คืน U-Boot ช่วยให้ระบบบูตด้วย initramfs แทนระบบไฟล์รูท จึงเป็นสภาพแวดล้อมอิสระสำหรับการเข้าถึงระบบ

<br/><br/><br/>

## 3.1 การเตรียม USB สำหรับบูต
---
- ฟอร์แมตแฟลชไดรฟ์ USB เป็น ext4

- ไปยังไดเรกทอรีต่อไปนี้ซึ่งเป็นที่เก็บผลลัพธ์การบิลด์ YP ของ D3-G:

     : {build/d3-g-topst-main/tmp/deploy/images/d3-g-topst-main}

- คัดลอกไฟล์สองไฟล์ต่อไปนี้ไปยังแฟลชไดรฟ์ USB

  -  Image-initramfs--5.10.205-r0-d3-g-topst-main-{build_date}.bin

  -  tcc8050-topst-d3-g--5.10.205-r0-d3-g-topst-main-{build_date}.dtb


## 3.2 ขั้นตอนการบูตในโหมด U-Boot
---
เสียบ USB เข้ากับ D3-G แล้วเปิดเครื่อง เข้าสู่โหมด U-Boot และรันคำสั่งต่อไปนี้:

**หากต้องการเข้าสู่โหมด u-boot ให้เปิดเครื่องแล้วกด enter ภายใน 3 วินาที**

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
บูตอิมเมจเคอร์เนล Linux ในสภาพแวดล้อม u-boot ด้วยคำสั่ง booti 0x20000000 - 0x30000000
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

# 4. การรีเซ็ตรหัสผ่าน root
---
เมื่อเข้าสู่เชลล์ของ initramfs แล้ว ให้ทำตามขั้นตอนด้านล่างเพื่อเมานต์ eMMC และรีเซ็ตรหัสผ่าน root ที่จัดเก็บไว้


## 4.1 การเมานต์พาร์ทิชัน eMMC
---
เมานต์พาร์ทิชันระบบไฟล์รูท (โดยทั่วไปคือ /dev/mmcblk0p3) ไปยังจุดเมานต์ชั่วคราว:

**โปรดตรวจสอบพาร์ทิชันที่ถูกต้องด้วย lsblk หรือ blkid ทุกครั้ง**
```
$ mkdir -p /mnt/part3
$ mount /dev/mmcblk0p3 /mnt/part3
```

## 4.2 การแก้ไขไฟล์ shadow
---
รหัสผ่าน root ถูกจัดเก็บในรูปแบบแฮชในไฟล์ /etc/shadow หากต้องการล้างรหัสผ่าน ให้ดำเนินการดังนี้:

```
$ sed -i 's/###root passwd signature###//g' /mnt/part3/etc/shadow
```

## 4.3 การสรุปและรีบูต
---
เพื่อให้แน่ใจว่าการเปลี่ยนแปลงถูกเขียนลงดิสก์ ให้ดำเนินการดังนี้:

```
$ sync
$ reboot
```
ขณะนี้ท่านสามารถเข้าสู่ระบบในฐานะ root ได้โดยไม่ต้องใช้รหัสผ่าน และใช้ passwd เพื่อตั้งรหัสผ่านใหม่

```
$ passwd
New password:
Retype new password:
passwd: password updated successfully
```