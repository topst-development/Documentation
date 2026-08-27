# D3-G Kurzanleitung
---

## 1.1 D3-G-Board und Host-PC im USB-Boot-Modus verbinden
---
Der Firmware Downloader (FWDN) schreibt über die USB-Verbindung mit dem Host-PC ein ROM-Image auf das D3-G. 

Das D3-G verfügt über eine Boot-Modus-Taste und unterstützt zwei Arten von Boot-Modi. Diese Anleitung konzentriert sich auf den FWDN-Modus.

- USB-Boot-Modus (FWDN-Modus) : Wird verwendet, um mit dem FWDN-Werkzeug auf Ihrem Host-PC ein ROM-Image zu schreiben 

- eMMC-Boot-Modus : Wird verwendet, um das D3-G mit einem ROM-Image zu booten, das auf einem eMMC-Gerät gespeichert ist 

**Hinweis**: Der USB-Type-C-FWDN-Anschluss wird für den Firmware Downloader (FWDN) verwendet. 



Um FWDN zu verwenden, verbinden Sie das D3-G-Board wie folgt mit dem Host-PC: 

1. Prüfen Sie, ob der VTC-Treiber auf dem Host-PC installiert ist. Falls der VTC-Treiber nicht installiert ist, installieren Sie ihn wie in Kapitel 1.2 beschrieben.  

2. Halten Sie ein USB-Type-C-Kabel bereit. 

3. Um in den USB-Boot-Modus zu wechseln, schließen Sie das Netzkabel an das D3-G-Board an, während Sie den FWDN-Schalter gedrückt halten.

4. Schließen Sie das USB-Type-C-Kabel an den USB-Type-C-FWDN-Anschluss des D3-G-Boards und an den Host-PC an. 

<p align="center">
    <img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20D3-G/Hardware/connect%20to%20d3g%20to%20host%20pc%20using%20c%20type.png">
</p>
<p align="center"><strong>Abbildung 1.1 Verbindung des D3-G-Boards mit dem Host-PC über ein USB-Type-C-Kabel </strong></p>

<br/><br/>

## 1.2 Installation des VTC-Treibers (Windows/Ubuntu)
Installieren Sie den Vendor Telechips Certification (VTC) Treiber (zu finden unter [Telechips-Treiber](https://drive.google.com/file/d/1muQnY8kuKxDsy3p3FUiQqcG34Zjk-mnR/view?usp=sharing)) auf dem Host-PC, indem Sie ihn als Administrator ausführen. Wenn Sie das USB-Kabel wie oben gezeigt im FWDN-Modus anschließen, wird der Telechips-VTC-USB-Treiber wie in Abbildung 1.2 und Abbildung 1.3 dargestellt eingerichtet.

<p align="center">
    <img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20D3-G/Software/USB%20Connection%20in%20Windows%20Environment.png", width="700">
</p>
<p align="center"><strong>Abbildung 1.2 USB-Verbindung in der Windows-Umgebung</strong></p>

<p align="center">
    <img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20D3-G/Software/USB%20Connection%20in%20Linux%20System.png", width="700">
</p>
<p align="center"><strong>Abbildung 1.3 USB-Verbindung in der Linux-Umgebung</strong></p>  

**Hinweis**: Verwenden Sie den VTC-Treiber V5.0.0.14 oder höher. Um die Version zu prüfen, sehen Sie im Geräte-Manager der Windows-Umgebung nach.  

<br/><br/><br/>

## 1.3 FWDN in der Windows-Umgebung

### 1.3.1 D3-G Yocto
---
1. Rufen Sie die Downloads-Seite auf

2. Laden Sie das D3-G-Yocto-Image herunter
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/Quick%20Guide/Download%20D3-G%20v1.2.0%20Yocto%20Image.png" width="550"></p>
<p align="center"><strong>Abbildung 1.4 D3-G-Yocto-Image herunterladen</strong></p> <br/>

3. Klicken Sie auf fwdn.bat. Die Datei „fwdn.bat“ ist eine ausführbare Datei, die die Firmware automatisch mit ***FWDN V8*** herunterlädt. 
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/Quick%20Guide/Click%20fwdn.bat.png" width="550"></p>
<p align="center"><strong>Abbildung 1.5 Klicken Sie auf fwdn.bat</strong></p> <br/>

```
C:\output_d3g.fwdn>fwdn.exe --fwdn boot-firmware\fwdn.json
[main:30] FWDN V8 v1.4.6 - 2021.12.13 13:42:37
[FWDN_V8::LoadFWDNRom:403] Start to load FWDN rom
[FWDN_V8::LoadMCERT:592] C:\output_d3g.fwdn\boot-firmware\mcert.bin
[FWDN_V8::LoadHSM:609] C:\output_d3g.fwdn\boot-firmware\hsm.cs.bin
[FWDN_V8::SendFWDNHeader:634] C:\output_d3g.fwdn\boot-firmware\fwdn.rom - Header
[FWDN_V8::SendFWDNBody_V8:537] C:\output_d3g.fwdn\boot-firmware\fwdn.rom - Body
[FWDN_V8::LoadFWDNRom:414] Complete to load FWDN rom
[FWDN_V8::GetFWDNRomVersion:1526] fwdn.rom version : 21.9.29
[FWDN_V8::GetFileAndWriteCommand:748] C:\output_d3g.fwdn\boot-firmware\dram_params.bin
[FWDN_V8::PrintDeviceInfo:1183] --------------Device info-------------
[FWDN_V8::PrintDeviceInfo:1184]

----- Detail of Storages -----
#### eMMC Info ####
Manufacture ID: 0x15
OEM: 0x100
Name: 8GTF4
User Capacity: 7.3 GiB (7818182656 Byte)
Boot Capacity: 4 MiB (4194304 Byte)
RPMB Capacity: 512 KiB (524288 Byte)
Speed Mode: HS200
#### SNOR Info ####
Manufacture ID: 0xc2
Device ID: 0x2016
Name: MXIC-MX25L3233F
Sector Size: 4 KiB (4096 Byte)
Total Capacity: 4 MiB (4194304 Byte)
4Byte Address Mode: Unsupported

----- Summary of Storages -----
eMMC : O
SNOR : O
UFS : X
- O : Init success
- X : Init failed or not exist

----- Summary of DRAM Init -----
DRAM Init : Success (Result 0x0 )
DRAM Size : 4096MB

[FWDN_V8::PrintDeviceInfo:1185] --------------------------------------
[main:142] Complete FWDN
[FWDNLogger::PrintCurTime:111] 24/04/25-09:57:47

C:\output_d3g.fwdn>fwdn.exe --storage emmc --low-format
[main:30] FWDN V8 v1.4.6 - 2021.12.13 13:42:37
[FWDN_V8::GetFWDNRomVersion:1526] fwdn.rom version : 21.9.29
[FWDN_V8::LowformatCommand:1352] Start low-format
[FWDN_V8::LowformatCommand:1353] low-format can take a long time
[FWDN_V8::LowformatCommand:1382] Complete low-format
[main:142] Complete FWDN
[FWDNLogger::PrintCurTime:111] 24/04/25-09:57:50

C:\output_d3g.fwdn>fwdn.exe -w boot-firmware\boot.single.json
[main:30] FWDN V8 v1.4.6 - 2021.12.13 13:42:37
[FWDN_V8::GetFWDNRomVersion:1526] fwdn.rom version : 21.9.29
[main:117] Start write command
[FWDN_V8::GetFileAndWriteCommand:748] C:\output_d3g.fwdn\boot-firmware\bconf.single.bin
[FWDN_V8::GetFileAndWriteCommand:748] C:\output_d3g.fwdn\boot-firmware\bconf.single.bin
[FWDN_V8::GetFileAndWriteCommand:748] C:\output_d3g.fwdn\boot-firmware\mcert.bin
[FWDN_V8::GetFileAndWriteCommand:748] C:\output_d3g.fwdn\boot-firmware\mcert.bin
[FWDN_V8::GetFileAndWriteCommand:748] C:\output_d3g.fwdn\boot-firmware\dram_params.bin
[FWDN_V8::GetFileAndWriteCommand:748] C:\output_d3g.fwdn\boot-firmware\dram_params.bin
[FWDN_V8::GetFileAndWriteCommand:748] C:\output_d3g.fwdn\boot-firmware\hsm.cs.bin
[FWDN_V8::GetFileAndWriteCommand:748] C:\output_d3g.fwdn\boot-firmware\hsm.cs.bin
[FWDN_V8::GetFileAndWriteCommand:748] C:\output_d3g.fwdn\boot-firmware\scfw.rom
[FWDN_V8::GetFileAndWriteCommand:748] C:\output_d3g.fwdn\boot-firmware\scfw.rom
[FWDN_V8::GetFileAndWriteCommand:748] C:\output_d3g.fwdn\boot-firmware\optee.rom
[FWDN_V8::GetFileAndWriteCommand:748] C:\output_d3g.fwdn\boot-firmware\optee.rom
[FWDN_V8::GetFileAndWriteCommand:748] C:\output_d3g.fwdn\boot-firmware\ca72_bl1.rom
[FWDN_V8::GetFileAndWriteCommand:748] C:\output_d3g.fwdn\boot-firmware\ca72_bl1.rom
[FWDN_V8::GetFileAndWriteCommand:748] C:\output_d3g.fwdn\boot-firmware\ca53_bl1.rom
[FWDN_V8::GetFileAndWriteCommand:748] C:\output_d3g.fwdn\boot-firmware\ca53_bl1.rom
[FWDN_V8::GetFileAndWriteCommand:748] C:\output_d3g.fwdn\boot-firmware\ca72_bl2.rom
[FWDN_V8::GetFileAndWriteCommand:748] C:\output_d3g.fwdn\boot-firmware\ca72_bl2.rom
[FWDN_V8::GetFileAndWriteCommand:748] C:\output_d3g.fwdn\boot-firmware\ca53_bl2.rom
[FWDN_V8::GetFileAndWriteCommand:748] C:\output_d3g.fwdn\boot-firmware\ca53_bl2.rom
[main:125] Complete write command
[main:142] Complete FWDN
[FWDNLogger::PrintCurTime:111] 24/04/25-09:57:53
100% [||||||||||||||||||||||||||||||] 859264/859264
C:\output_d3g.fwdn>fwdn.exe -w "output_d3g.fai" --storage emmc --area user
[main:30] FWDN V8 v1.4.6 - 2021.12.13 13:42:37
[FWDN_V8::GetFWDNRomVersion:1526] fwdn.rom version : 21.9.29
[main:117] Start write command
[FWDN_V8::GetFileAndWriteCommand:748] output_d3g.fai
[main:125] Complete write command
[main:142] Complete FWDN
[FWDNLogger::PrintCurTime:111] 24/04/25-10:05:21
100% [||||||||||||||||||||||||||||||] 7238688960/7238688960
** When writing FAI files without low-format, there may be garbage values in partition where data is not written.
```

### 1.3.2 D3-G Ubuntu Desktop
---
1. Rufen Sie die Downloads-Seite auf

2. Laden Sie das D3-G-Ubuntu-Desktop-Image herunter
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/Quick%20Guide/Download%20D3-G%20v1.2.0%20Ubuntu%20Desktop%20Image.png" width="550"></p>
<p align="center"><strong>Abbildung 1.6 D3-G-Ubuntu-Desktop-Image herunterladen</strong></p> <br/>

3. Klicken Sie auf fwdn.bat. Die Datei „fwdn.bat“ ist eine ausführbare Datei, die die Firmware automatisch mit ***FWDN V8*** herunterlädt. 
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/Quick%20Guide/Click%20fwdn_ubuntu.bat.png" width="550"></p>
<p align="center"><strong>Abbildung 1.7 Klicken Sie auf fwdn.bat</strong></p> <br/>

```
C:\d3g-ubuntu.fwdn>fwdn.exe --fwdn boot-firmware\fwdn.json
[main:30] FWDN V8 v1.4.11 - 2022.11.14 13:47:30
[FWDN_V8::GetFWDNRomVersion:1588] fwdn.rom version : 23.5.22
[main:156] Complete FWDN
[FWDNLogger::PrintCurTime:112] 25/06/25-10:32:29

C:\d3g-ubuntu.fwdn>fwdn.exe --storage emmc --low-format
[main:30] FWDN V8 v1.4.11 - 2022.11.14 13:47:30
[FWDN_V8::GetFWDNRomVersion:1588] fwdn.rom version : 23.5.22
[FWDN_V8::LowformatCommand:1370] Start low-format
[FWDN_V8::LowformatCommand:1371] low-format can take a long time
[FWDN_V8::LowformatCommand:1400] Complete low-format
[main:156] Complete FWDN
[FWDNLogger::PrintCurTime:112] 25/06/25-10:32:29

C:\d3g-ubuntu.fwdn>fwdn.exe -w boot-firmware\boot.single.json
[main:30] FWDN V8 v1.4.11 - 2022.11.14 13:47:30
[FWDN_V8::GetFWDNRomVersion:1588] fwdn.rom version : 23.5.22
[main:131] Start write command
[FWDN_V8::GetFileAndWriteCommand:762] C:\d3g-ubuntu.fwdn\boot-firmware\.\prebuilt\bconf.single.bin
[FWDN_V8::GetFileAndWriteCommand:762] C:\d3g-ubuntu.fwdn\boot-firmware\.\prebuilt\bconf.single.bin
[FWDN_V8::GetFileAndWriteCommand:762] C:\d3g-ubuntu.fwdn\boot-firmware\.\prebuilt\mcert.bin
[FWDN_V8::GetFileAndWriteCommand:762] C:\d3g-ubuntu.fwdn\boot-firmware\.\prebuilt\mcert.bin
[FWDN_V8::GetFileAndWriteCommand:762] C:\d3g-ubuntu.fwdn\boot-firmware\.\prebuilt\dram_params.bin
[FWDN_V8::GetFileAndWriteCommand:762] C:\d3g-ubuntu.fwdn\boot-firmware\.\prebuilt\dram_params.bin
[FWDN_V8::GetFileAndWriteCommand:762] C:\d3g-ubuntu.fwdn\boot-firmware\.\prebuilt\hsm.cs.bin
[FWDN_V8::GetFileAndWriteCommand:762] C:\d3g-ubuntu.fwdn\boot-firmware\.\prebuilt\scfw.rom
[FWDN_V8::GetFileAndWriteCommand:762] C:\d3g-ubuntu.fwdn\boot-firmware\.\prebuilt\scfw.rom
[FWDN_V8::GetFileAndWriteCommand:762] C:\d3g-ubuntu.fwdn\boot-firmware\.\prebuilt\optee.rom
[FWDN_V8::GetFileAndWriteCommand:762] C:\d3g-ubuntu.fwdn\boot-firmware\.\prebuilt\optee.rom
[FWDN_V8::GetFileAndWriteCommand:762] C:\d3g-ubuntu.fwdn\boot-firmware\.\prebuilt\subcore_optee.rom
[FWDN_V8::GetFileAndWriteCommand:762] C:\d3g-ubuntu.fwdn\boot-firmware\.\prebuilt\subcore_optee.rom
[FWDN_V8::GetFileAndWriteCommand:762] C:\d3g-ubuntu.fwdn\boot-firmware\.\prebuilt\ca72_bl1.rom
[FWDN_V8::GetFileAndWriteCommand:762] C:\d3g-ubuntu.fwdn\boot-firmware\.\prebuilt\ca72_bl1.rom
[FWDN_V8::GetFileAndWriteCommand:762] C:\d3g-ubuntu.fwdn\boot-firmware\.\prebuilt\ca53_bl1.rom
[FWDN_V8::GetFileAndWriteCommand:762] C:\d3g-ubuntu.fwdn\boot-firmware\.\prebuilt\ca53_bl1.rom
[FWDN_V8::GetFileAndWriteCommand:762] C:\d3g-ubuntu.fwdn\boot-firmware\.\prebuilt\ca72_bl2.rom
[FWDN_V8::GetFileAndWriteCommand:762] C:\d3g-ubuntu.fwdn\boot-firmware\.\prebuilt\ca72_bl2.rom
[FWDN_V8::GetFileAndWriteCommand:762] C:\d3g-ubuntu.fwdn\boot-firmware\.\prebuilt\ca53_bl2.rom
[FWDN_V8::GetFileAndWriteCommand:762] C:\d3g-ubuntu.fwdn\boot-firmware\.\prebuilt\ca53_bl2.rom
[main:139] Complete write command
[main:156] Complete FWDN
[FWDNLogger::PrintCurTime:112] 25/06/25-10:32:29
100[||||||||||||||||||||||||||||||] 864768/864768
C:\d3g-ubuntu.fwdn>fwdn.exe -w "d3g.fai" --storage emmc --area user
[main:30] FWDN V8 v1.4.11 - 2022.11.14 13:47:30
[FWDN_V8::GetFWDNRomVersion:1588] fwdn.rom version : 23.5.22
[main:131] Start write command
[FWDN_V8::GetFileAndWriteCommand:762] d3g.fai
100% [||||||||||||||||||||||||||||||] 4291763824/4291763824
** When writing FAI files without low-format, there may be garbage values in partition where data is not written.
```

### 1.3.3 D3-G Ubuntu Headless
---
1. Rufen Sie die Downloads-Seite auf

2. Laden Sie das D3-G-Ubuntu-Headless-Image herunter
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/Quick%20Guide/Download%20D3-G%20Ubuntu%20Headless%20Image.png" width="550"></p>
<p align="center"><strong>Abbildung 1.8 D3-G-Ubuntu-Headless-Image herunterladen</strong></p> <br/>

3. Klicken Sie auf fwdn.bat. Die Datei „fwdn.bat“ ist eine ausführbare Datei, die die Firmware automatisch mit ***FWDN V8*** herunterlädt. 
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/Quick%20Guide/Click%20fwdn_ubuntu_headless.bat.png" width="550"></p>
<p align="center"><strong>Abbildung 1.9 Klicken Sie auf fwdn.bat</strong></p> <br/>

```
C:\d3g-ubuntu-headless>fwdn.exe --fwdn boot-firmware\fwdn.json
[main:30] FWDN V8 v1.4.11 - 2022.11.14 13:47:30
[FWDN_V8::GetFWDNRomVersion:1588] fwdn.rom version : 23.5.22
[main:156] Complete FWDN
[FWDNLogger::PrintCurTime:112] 25/06/25-10:28:35

C:\d3g-ubuntu-headless>fwdn.exe --storage emmc --low-format
[main:30] FWDN V8 v1.4.11 - 2022.11.14 13:47:30
[FWDN_V8::GetFWDNRomVersion:1588] fwdn.rom version : 23.5.22
[FWDN_V8::LowformatCommand:1370] Start low-format
[FWDN_V8::LowformatCommand:1371] low-format can take a long time
[FWDN_V8::LowformatCommand:1400] Complete low-format
[main:156] Complete FWDN
[FWDNLogger::PrintCurTime:112] 25/06/25-10:28:36

C:\d3g-ubuntu-headless>fwdn.exe -w boot-firmware\boot.single.json
[main:30] FWDN V8 v1.4.11 - 2022.11.14 13:47:30
[FWDN_V8::GetFWDNRomVersion:1588] fwdn.rom version : 23.5.22
[main:131] Start write command
[FWDN_V8::GetFileAndWriteCommand:762] C:\d3g-ubuntu-headless\boot-firmware\.\prebuilt\bconf.single.bin
[FWDN_V8::GetFileAndWriteCommand:762] C:\d3g-ubuntu-headless\boot-firmware\.\prebuilt\bconf.single.bin
[FWDN_V8::GetFileAndWriteCommand:762] C:\d3g-ubuntu-headless\boot-firmware\.\prebuilt\mcert.bin
[FWDN_V8::GetFileAndWriteCommand:762] C:\d3g-ubuntu-headless\boot-firmware\.\prebuilt\mcert.bin
[FWDN_V8::GetFileAndWriteCommand:762] C:\d3g-ubuntu-headless\boot-firmware\.\prebuilt\dram_params.bin
[FWDN_V8::GetFileAndWriteCommand:762] C:\d3g-ubuntu-headless\boot-firmware\.\prebuilt\dram_params.bin
[FWDN_V8::GetFileAndWriteCommand:762] C:\d3g-ubuntu-headless\boot-firmware\.\prebuilt\hsm.cs.bin
[FWDN_V8::GetFileAndWriteCommand:762] C:\d3g-ubuntu-headless\boot-firmware\.\prebuilt\hsm.cs.bin
[FWDN_V8::GetFileAndWriteCommand:762] C:\d3g-ubuntu-headless\boot-firmware\.\prebuilt\scfw.rom
[FWDN_V8::GetFileAndWriteCommand:762] C:\d3g-ubuntu-headless\boot-firmware\.\prebuilt\scfw.rom
[FWDN_V8::GetFileAndWriteCommand:762] C:\d3g-ubuntu-headless\boot-firmware\.\prebuilt\optee.rom
[FWDN_V8::GetFileAndWriteCommand:762] C:\d3g-ubuntu-headless\boot-firmware\.\prebuilt\optee.rom
[FWDN_V8::GetFileAndWriteCommand:762] C:\d3g-ubuntu-headless\boot-firmware\.\prebuilt\subcore_optee.rom
[FWDN_V8::GetFileAndWriteCommand:762] C:\d3g-ubuntu-headless\boot-firmware\.\prebuilt\subcore_optee.rom
[FWDN_V8::GetFileAndWriteCommand:762] C:\d3g-ubuntu-headless\boot-firmware\.\prebuilt\ca72_bl1.rom
[FWDN_V8::GetFileAndWriteCommand:762] C:\d3g-ubuntu-headless\boot-firmware\.\prebuilt\ca72_bl1.rom
[FWDN_V8::GetFileAndWriteCommand:762] C:\d3g-ubuntu-headless\boot-firmware\.\prebuilt\ca53_bl1.rom
[FWDN_V8::GetFileAndWriteCommand:762] C:\d3g-ubuntu-headless\boot-firmware\.\prebuilt\ca53_bl1.rom
[FWDN_V8::GetFileAndWriteCommand:762] C:\d3g-ubuntu-headless\boot-firmware\.\prebuilt\ca72_bl2.rom
[FWDN_V8::GetFileAndWriteCommand:762] C:\d3g-ubuntu-headless\boot-firmware\.\prebuilt\ca72_bl2.rom
[FWDN_V8::GetFileAndWriteCommand:762] C:\d3g-ubuntu-headless\boot-firmware\.\prebuilt\ca53_bl2.rom
[FWDN_V8::GetFileAndWriteCommand:762] C:\d3g-ubuntu-headless\boot-firmware\.\prebuilt\ca53_bl2.rom
[main:139] Complete write command
[main:156] Complete FWDN
[FWDNLogger::PrintCurTime:112] 25/06/25-10:28:36
100[||||||||||||||||||||||||||||||] 864768/864768
C:\d3g-ubuntu-headless>fwdn.exe -w "d3g.fai" --storage emmc --area user
[main:30] FWDN V8 v1.4.11 - 2022.11.14 13:47:30
[FWDN_V8::GetFWDNRomVersion:1588] fwdn.rom version : 23.5.22
[main:131] Start write command
[FWDN_V8::GetFileAndWriteCommand:762] d3g.fai
100% [||||||||||||||||||||||||||||||] 2594119280/2594119280
** When writing FAI files without low-format, there may be garbage values in partition where data is not written.
```

<br/><br/><br/>

## 1.4 FWDN in der Linux-Umgebung

### 1.4.1 Extrahieren des D3-G-Images
---
Extrahieren Sie das D3-G-Image, das Sie in Abschnitt 1.3 heruntergeladen haben, auf Ihrem Linux-System.

<br/><br/><br/>

### 1.4.2 Udev-Regeln für das Telechips-USB-Gerät
---
Nachdem Sie die folgenden Befehle ausgeführt haben, müssen Sie beim Herunterladen mit FWDN unter Linux den Befehl 'sudo' nicht mehr verwenden.
```
$ echo "SUBSYSTEM==\"usb\", ATTR{idVendor}==\"140e\", MODE=\"0666\", OWNER=\"${USER}\"" | sudo tee /etc/udev/rules.d/99-topst.rules
$ sudo udevadm control --reload-rules && sudo udevadm trigger
```
<br/><br/><br/>

### 1.4.3 Flashen des D3-G-Images mit fwdn.sh
---
Um das D3-G-Image unter Linux herunterzuladen, führen Sie den folgenden Befehl aus: "./fwdn.sh".

```
$ ./fwdn.sh
```

Das D3-G ist nun startbereit. Weitere Informationen zum Beginn der Kommunikation mit dem Gerät finden Sie in Kapitel 1.5.


<br/><br/><br/><br/>

## 1.5 Verbinden des D3-G-Boards mit einem Host-PC
---
In diesem Kapitel wird beschrieben, wie Sie den Host-PC über UART mit dem D3-G-Board verbinden, um Firmware herunterzuladen und seriell zu kommunizieren.

<br/><br/><br/>

## 1.6 Verbindung des D3-G-Boards über UART 
---
Führen Sie die folgenden Schritte aus und überprüfen Sie über die UART-Verbindung, ob der Firmware-Download erfolgreich abgeschlossen wurde. 

1. Installieren Sie in der Windows-Umgebung den Treiber für den seriellen Anschluss (zum Beispiel CP210x Windows Driver) und den Treiber PL2303_prolific. 
2. Installieren Sie einen Terminal-Emulator wie Tera Term oder PuTTY. 
3. Verbinden Sie den Host-PC mit dem UART-Pin auf dem D3-G-Board. Verwenden Sie ein USB-zu-TTL-Kabel. 
4. Schließen Sie das schwarze Kabel an den GND-Pin an. 
5. Schließen Sie das weiße Kabel (RXD) an den TX-Pin der UART-Pins und das grüne Kabel (TXD) an den RX-Pin der UART-Pins an.
6. Starten Sie die Terminal-Emulator-Anwendung.
7. Öffnen Sie den Geräte-Manager auf Ihrem PC und prüfen Sie die Portnummer, die für UART verwendet wird.
8. Geben Sie die im Geräte-Manager ermittelte Portnummer in das Feld Serial line des Terminal-Emulators ein. Setzen Sie **Speed** (bps) auf 115200 und **Flow control auf None.**
9. Schließen Sie das Netzkabel an. Anschließend bootet das D3-G im standardmäßigen eMMC-Boot-Modus.


 
<p align="center">
    <img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20D3-G/Software/USB%20to%20TTL%20Connection.png", width="700">
</p>
<p align="center"><strong>Abbildung 1.6 UART-Verbindung mit dem Host-PC</strong></p><br/>  
