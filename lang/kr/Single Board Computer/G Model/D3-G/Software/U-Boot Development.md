# 1. 소개
---
이 문서는 U-Boot를 사용하여 임베디드 시스템을 복구하고, initramfs로 부팅하며, 루트 비밀번호를 재설정하는 방법에 대한 가이드라인을 제공합니다.

이 가이드는 다음 주제를 다룹니다:

- U-Boot 복구 원리

- USB 및 initramfs를 사용한 부팅

- eMMC 파티션 마운트

- 루트 비밀번호 재설정 절차

<br/><br/><br/><br/>

# 2. U-Boot 복구 원리
---
eMMC 파일 시스템에서 부팅하는 대신 U-Boot를 사용하여 initramfs 이미지를 통해 시스템을 시작합니다. 이 접근 방식은 루트 파일 시스템이 손상되었거나 액세스할 수 없을 때 특히 유용합니다. 시스템이 initramfs로 부팅된 후 eMMC 루트 파일 시스템이 마운트되어 관리자가 파일 수정 또는 자격 증명 재설정과 같은 복구 작업을 수행할 수 있습니다.
</br><br/><br/><br/>

# 3. U-Boot 및 initramfs로 부팅
---
U-Boot는 부팅 가능한 이미지(예: initramfs 및 dtb)를 메모리에 로드하고 실행하여 시스템을 초기화하는 부트로더입니다.

복구 시나리오에서 루트 파일 시스템 대신 initramfs로 시스템을 부팅할 수 있어 시스템 액세스를 위한 독립적인 환경을 제공합니다.

<br/><br/><br/>

## 3.1 부팅 가능한 USB 준비
---
- USB 메모리 스틱을 ext4로 포맷합니다.

- D3-G YP 빌드 결과물이 있는 다음 디렉토리로 이동합니다:

     : {build/d3-g-topst-main/tmp/deploy/images/d3-g-topst-main}

- 다음 두 파일을 USB 메모리 스틱에 복사합니다.

  -  Image-initramfs--5.10.205-r0-d3-g-topst-main-{build_date}.bin

  -  tcc8050-topst-d3-g--5.10.205-r0-d3-g-topst-main-{build_date}.dtb


## 3.2 U-Boot 모드에서의 부팅 단계
---
USB를 D3-G에 삽입하고 전원을 웁니다. U-Boot 모드로 진입하여 다음 명령을 실행합니다:

**u-boot 모드로 진입하려면 전원을 켜고 3초 이내에 Enter 키를 누르십시오.**

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
booti 0x20000000 - 0x30000000을 통해 u-boot 환경에서 Linux 커널 이미지를 부팅합니다.
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

# 4. 루트 비밀번호 재설정
---
initramfs 셸에 진입하면 아래 단계에 따라 eMMC를 마운트하고 저장된 루트 비밀번호를 재설정하십시오.


## 4.1 eMMC 파티션 마운트
---
루트 파일 시스템 파티션(일반적으로 /dev/mmcblk0p3)을 임시 마운트 지점에 마운트합니다:

**lsblk 또는 blkid를 사용하여 올바른 파티션을 확인하십시오.**
```
$ mkdir -p /mnt/part3
$ mount /dev/mmcblk0p3 /mnt/part3
```

## 4.2 shadow 파일 수정
---
루트 비밀번호는 /etc/shadow 파일에 해시된 형태로 저장됩니다. 비밀번호를 지우려면:

```
$ sed -i 's/###root passwd signature###//g' /mnt/part3/etc/shadow
```

## 4.3 마무리 및 재부팅
---
변경 사항이 디스크에 기록되도록 하려면:

```
$ sync
$ reboot
```
이제 비밀번호 없이 root로 로그인하고 passwd를 사용하여 새 비밀번호를 설정할 수 있습니다.

```
$ passwd
New password:
Retype new password:
passwd: password updated successfully
```