# 1. Einführung
---
Dieses Dokument enthält Richtlinien für die Wiederherstellung des eingebetteten Systems mit U-Boot, das Booten mit initramfs und das Zurücksetzen des Root-Passworts.

Diese Anleitung behandelt die folgenden Themen:

- Funktionsprinzip der U-Boot-Wiederherstellung

- Booten mit USB und initramfs

- Einhängen von eMMC-Partitionen

- Vorgehensweise zum Zurücksetzen des Root-Passworts

<br/><br/><br/><br/>

# 2. Funktionsprinzip der U-Boot-Wiederherstellung
---
Anstatt vom eMMC-Dateisystem zu booten, wird das System über ein initramfs-Image mit U-Boot gestartet. Dieser Ansatz ist besonders nützlich, wenn das Root-Dateisystem beschädigt oder nicht zugänglich ist. Nachdem das System in initramfs gebootet wurde, wird das eMMC-Root-Dateisystem eingehängt, sodass Administratoren Wiederherstellungsaufgaben durchführen können, etwa das Ändern von Dateien oder das Zurücksetzen von Anmeldedaten.
</br><br/><br/><br/>

# 3. Booten mit U-Boot und initramfs
---
U-Boot ist ein Bootloader, der bootfähige Images (wie initramfs und dtb) in den Speicher lädt und ausführt, um das System zu initialisieren. 

In Wiederherstellungsszenarien ermöglicht er es, das System mit initramfs anstelle des Root-Dateisystems zu booten und stellt so eine unabhängige Umgebung für den Systemzugriff bereit.

<br/><br/><br/>

## 3.1 Bootfähigen USB-Speicher vorbereiten
---
- Formatieren Sie einen USB-Speicherstick als ext4

- Wechseln Sie in das folgende Verzeichnis, in dem sich die YP-Build-Ausgabe des D3-G befindet:

     : {build/d3-g-topst-main/tmp/deploy/images/d3-g-topst-main}

- Kopieren Sie die folgenden zwei Dateien auf einen USB-Speicherstick

  -  Image-initramfs--5.10.205-r0-d3-g-topst-main-{build_date}.bin

  -  tcc8050-topst-d3-g--5.10.205-r0-d3-g-topst-main-{build_date}.dtb


## 3.2 Boot-Schritte im U-Boot-Modus
---
Stecken Sie den USB-Speicher in das D3-G und schalten Sie es ein. Wechseln Sie in den U-Boot-Modus und führen Sie die folgenden Befehle aus:

**Um in den u-boot-Modus zu gelangen, schalten Sie das Gerät ein und drücken Sie innerhalb von 3 Sekunden die Eingabetaste.**

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
Booten Sie das Linux-Kernel-Image in der u-boot-Umgebung mit booti 0x20000000 - 0x30000000.
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

# 4. Zurücksetzen des Root-Passworts
---
Sobald Sie sich in der initramfs-Shell befinden, führen Sie die folgenden Schritte aus, um eMMC einzuhängen und das gespeicherte Root-Passwort zurückzusetzen.


## 4.1 eMMC-Partition einhängen
---
Hängen Sie die Partition des Root-Dateisystems (üblicherweise /dev/mmcblk0p3) an einem temporären Einhängepunkt ein:

**Überprüfen Sie unbedingt die richtige Partition mit lsblk oder blkid.**
```
$ mkdir -p /mnt/part3
$ mount /dev/mmcblk0p3 /mnt/part3
```

## 4.2 shadow-Datei ändern
---
Das Root-Passwort wird in gehashter Form in der Datei /etc/shadow gespeichert. So löschen Sie das Passwort:

```
$ sed -i 's/###root passwd signature###//g' /mnt/part3/etc/shadow
```

## 4.3 Abschließen und neu starten
---
So stellen Sie sicher, dass die Änderungen auf den Datenträger geschrieben werden:

```
$ sync
$ reboot
```
Sie können sich jetzt ohne Passwort als root anmelden und mit passwd ein neues Passwort festlegen.

```
$ passwd
New password:
Retype new password:
passwd: password updated successfully
```