# 1. Einführung
---
Dieses Dokument enthält Richtlinien für die Einrichtung einer Software-Entwicklungsumgebung für das VCP-G SDK. Es beschreibt die erforderlichen Werkzeuge, Konfigurationen und die Toolchain.

</br></br></br></br>

# 2. Einrichten der Host-Umgebung
---
## 2.1 Ubuntu installieren
---
Es wird empfohlen, Ihre Entwicklungsumgebung unter Ubuntu 22.04 einzurichten. Diese Ubuntu-Version bietet eine stabile Plattform mit breiter Community-Unterstützung und gewährleistet Kompatibilität und einfache Handhabung mit dem VCP-G und der zugehörigen Toolchain.

Version der Linux-Distribution:  
- Ubuntu 22.04 (LTS)

</br></br></br>

## 2.2 WSL2 Ubuntu installieren (nur Windows-Umgebung)
---
**Hinweis:** Wenn Sie einen Ubuntu-Host verwenden, können Sie die Installation von WSL2 überspringen.  

1.	Stellen Sie die Windows-Features ein, indem Sie auf **Systemsteuerung -> Programme -> Windows-Features aktivieren/deaktivieren -> Plattform für virtuelle Computer & Hyper-V aktivieren** klicken.
2.	Starten Sie Windows Powershell mit **„Als Administrator ausführen“.**
3.	Aktivieren Sie das WSL2-System.
    ```
    dism.exe /online /enable-feature /featurename:Microsoft-Windows-Subsystem-Linux /all /norestart
    ```
4.	Aktivieren Sie die Funktion für virtuelle Computer.
    ```
    dism.exe /online /enable-feature /featurename:VirtualMachinePlatform /all /norestart
    ```
5.	Legen Sie WSL auf die Standardversion 2 (WSL2) fest.
    ```
    wsl --set-default-version 2
    ```
6.	Suchen Sie im Microsoft Store nach Ubuntu 22.04 LTS und laden Sie es herunter.

    * Wenn Sie das Linux-Kernel-Updatepaket herunterladen müssen, laden Sie das neueste Paket [hier](https://learn.microsoft.com/ko-kr/windows/wsl/install-manual) herunter.
7.	Prüfen Sie Ubuntu 22.04 in der WSL-Liste.
    ```
    wsl --list -online
    ```
8.	Installieren Sie Ubuntu 22.04.
    ```
    wsl --install Ubuntu-22.04
    ```
9.	Suchen Sie im Windows-Suchfeld nach WSL2 und führen Sie es aus. 

</br></br></br>

## 2.3 Linux-Umgebung einrichten
---
Um eine Linux-Umgebung auf Ihrem Host-PC einzurichten, führen Sie die folgenden Schritte aus:  

1. WSL2 ausführen (nur Windows-Umgebung)  
    Wenn Sie Windows verwenden, starten Sie WSL2, indem Sie einen der folgenden Befehle in Windows PowerShell ausführen.  
    ```
    wsl
    ```
    ```
    ubuntu
    ```

2.	Paketliste aktualisieren  
Bevor Sie neue Software installieren, aktualisieren Sie die Liste der verfügbaren Pakete, um sicherzustellen, dass Sie die neuesten Versionen und Abhängigkeiten erhalten. Der folgende Befehl ruft die neueste Liste der verfügbaren Pakete aus den Repositories ab.
    ```
    sudo apt update && /
    sudo apt upgrade
    ```

3.	Gängige Entwicklungswerkzeuge installieren  
    Installieren Sie gängige Entwicklungswerkzeuge, indem Sie den folgenden Befehl eingeben:
    ```
    sudo apt install build-essential git
    ```

**Hinweis:** Dieser Befehl installiert sowohl das Paket build-essential als auch git.

</br></br></br></br>

# 3. Toolchain
---
Der VCP-G verwendet die Toolchain **gcc-linaro-7.2.1-2017.11-x86_64_arm-eabi**.  
Diese Toolchain ist für die ARM-Architektur optimiert und gewährleistet die Kompatibilität mit dem TCC7045-Chip auf dem VCP-G.

</br></br></br>

## 3.1 Toolchain installieren und einrichten
---
Führen Sie die folgenden Schritte aus, um die Toolchain herunterzuladen, zu entpacken und einzurichten:  
1. Toolchain herunterladen  
   Geben Sie den Befehl **wget** ein, um die Toolchain von der Linaro-Website herunterzuladen:
    ```
    wget https://releases.linaro.org/components/toolchain/binaries/7.2-2017.11/arm-eabi/gcc-linaro-7.2.1-2017.11-x86_64_arm-eabi.tar.xz
    ```
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/Download%20Toolchain.png"></p>
    <p align="center"><strong>Abbildung 3.1 Toolchain herunterladen</strong></p>
    
2. Toolchain entpacken  
    Nachdem der Download abgeschlossen ist, entpacken Sie den Inhalt der .tar.xz-Datei.
    ```
    tar -xvf gcc-linaro-7.2.1-2017.11-x86_64_arm-eabi.tar.xz
    ```
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/Extract%20Toolchain.png"></p>
    <p align="center"><strong>Abbildung 3.2 Toolchain entpacken</strong></p>
    
3. Toolchain nach /opt verschieben  
    Das Verzeichnis /opt ist unter Linux ein Standardspeicherort für optionale Software. Verschieben Sie die entpackte Toolchain in dieses Verzeichnis.
    ```
    sudo mv gcc-linaro-7.2.1-2017.11-x86_64_arm-eabi /opt/
    ```
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/Move%20Toolchain.png"></p>
    <p align="center"><strong>Abbildung 3.3 Toolchain verschieben</strong></p>

</br></br></br>

## 3.2 Toolchain überprüfen
---
So stellen Sie sicher, dass die Toolchain korrekt installiert ist.  
1. Zum Toolchain-Verzeichnis navigieren
    ```
    cd /opt/gcc-linaro-7.2.1-2017.11-x86_64_arm-eabi
    ```
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/Navigate%20to%20Toolchain%20Directory.png"></p>
    <p align="center"><strong>Abbildung 3.4 Zum Toolchain-Verzeichnis navigieren</strong></p>
    
2. Version des installierten GCC-Compilers prüfen
    ```
    ./bin/arm-eabi-gcc --version
    ```
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/Check%20Version%20of%20Installed%20GCC%20Compiler.png"></p>
    <p align="center"><strong>Abbildung 3.5 Version des installierten GCC-Compilers prüfen</strong></p>

Überprüfen Sie nach der erfolgreichen Installation des GCC-Compilers die installierte GCC-Compiler-Version und vergleichen Sie sie mit **gcc-linaro-7.2.1-2017.11.**

</br></br></br></br>

# 4. Quellcode klonen
---
In diesem Kapitel wird beschrieben, wie der Quellcode mit Git geklont wird.

</br></br></br>

## 4.1 VCP-G-Quellcode klonen
---
Um den Quellcode für den VCP-G zu erhalten, geben Sie den Befehl **git clone** ein. Dieser Befehl erstellt eine Kopie des Remote-Repositorys auf Ihrem lokalen Rechner, sodass Sie direkt mit dem Code arbeiten können.

Führen Sie die folgenden Schritte aus, um den VCP-G-Quellcode zu klonen:
1. Terminal öffnen  
    Starten Sie die Terminal-Anwendung auf Ihrem Ubuntu-22.04-System.

2. Zum gewünschten Verzeichnis navigieren  
    Wählen Sie einen geeigneten Speicherort für den Quellcode. Wenn Sie das Repository beispielsweise im Home-Verzeichnis speichern möchten, verwenden Sie den folgenden Befehl.
    ```
    cd ~
    ```
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/Navigate%20to%20Desired%20Directory.png"></p>
    <p align="center"><strong>Abbildung 4.1 Zum gewünschten Verzeichnis navigieren</strong></p>

3. Repository klonen  
    Verwenden Sie den folgenden Befehl, um den VCP-G-Quellcode von der angegebenen Git-Adresse zu klonen.
    ```
    git clone https://github.com/topst-development/FreeRTOS-VCP.git topst-vcp
    ```
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/Figure%204.2%20Clone%20Repository.png"></p>
    <p align="center"><strong>Abbildung 4.2 Repository klonen</strong></p>

4. Zum geklonten Verzeichnis navigieren  
    Nachdem der Klonvorgang abgeschlossen ist, verwenden Sie den folgenden Befehl, um zu dem Verzeichnis zu navigieren, das den Quellcode enthält.
    ```
    cd topst-vcp
    ```
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/Navigate%20to%20Cloned%20Directory.png"></p>
    <p align="center"><strong>Abbildung 4.3 Zum geklonten Verzeichnis navigieren</strong></p>

Der VCP-G-Quellcode steht nun lokal für den Build und die Entwicklung zur Verfügung.

</br></br></br>

## 4.2 Struktur des Quellcodes
---
Geben Sie nach dem Klonen den Befehl **ls** ein, um den Verzeichnisinhalt aufzulisten und die wichtigsten Dateien zu prüfen, um die Struktur des Quellcodes zu verstehen.
```
ls

build  documents  easy-setup_vcp.sh  LICENSE  scripts  sources  tools
```

</br></br></br></br>

# 5. Build-Anleitung
---
## 5.1 easy-setup_vcp-g.sh ausführen
---
Wenn Sie das Skript ./easy-setup_vcp-g.sh ausführen, wird der folgende Bildschirm angezeigt.

**Achtung**: Wenn Sie ./easy-setup_vcp-g.sh erneut ausführen, seien Sie vorsichtig, da die erstellten Quellen gelöscht werden, wenn Sie yes auswählen.
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20AI-G/Software/Linux%20SDK/license1.png"></p>
<p align="center"><strong>Abbildung 5.1 Endbenutzer-Lizenzvertrag</strong></p>

Scrollen Sie zum unteren Rand des Bildschirms und lesen Sie diesen Hinweis. Nachdem Sie diesen Hinweis gelesen haben, drücken Sie die Rechtspfeiltaste und [Enter].
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20AI-G/Software/Linux%20SDK/license2.png"></p>
<p align="center"><strong>Abbildung 5.2 Zu 'Proceed to confirm' wechseln</strong></p>


Anschließend wird der folgende Bildschirm angezeigt. 
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20AI-G/Software/Linux%20SDK/license3.png" ></p>
<p align="center"><strong>Abbildung 5.3 Accept-Bildschirm </strong></p>
Wenn Sie Accept durch Drücken von [Enter] auswählen, können Sie den Build mit dem folgenden Befehl durchführen.

</br></br></br>

## 5.2 Makefiles und Build-Systeme
---
Ein Makefile ist eine zentrale Komponente vieler Build-Systeme. Es enthält Regeln und Anweisungen für das Dienstprogramm **make** zum Kompilieren und Linken von Programmen. Durch die Verwendung eines Makefiles können Sie den Build-Prozess automatisieren und so Konsistenz und Effizienz sicherstellen.

</br></br></br>

## 5.3 Build-Prozess starten
---
Führen Sie die folgenden Schritte aus, um den Quellcode zu erstellen:  
1. Navigieren Sie zum Build-Verzeichnis.
    ```
    cd build/tcc70xx/gcc/
    ```
2. Führen Sie den Befehl **make** aus.  
    ```
    make
    ```
    Der Befehl **make** liest das Makefile im aktuellen Verzeichnis und führt den Build-Prozess aus.
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/Run%20make%20Command.png"></p>
    <p align="center"><strong>Abbildung 5.4 Befehl make ausführen </strong></p>
    
3. Build-Ausgabe überprüfen  
    Nachdem der Build-Prozess abgeschlossen ist, sollten die folgenden Ausgabedateien im Terminal aufgelistet werden.
    - output/tcc70xx_pflash_boot.rom
    - output/tcc70xx_pflash_boot_2M_ECC.rom
    - output/tcc70xx_pflash_boot_3M_ECC.rom
    - output/tcc70xx_pflash_boot_4M_ECC.rom
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/Verify%20Build%20Output.png"></p>
    <p align="center"><strong>Abbildung 5.5 Build-Ausgabe überprüfen</strong></p>
   
    Um die Liste der Ausgabedateien zu prüfen, verwenden Sie den folgenden Befehl:
    ```
    ls output/ -al
    ```
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/Build%20Output%20File.png"></p>
    <p align="center"><strong>Abbildung 5.6 Build-Ausgabedatei</strong></p>

</br></br></br></br>

# 6. Firmware-Download
---
In diesem Kapitel wird beschrieben, wie ***FWDN*** in einer Linux-basierten Entwicklungsumgebung auf den VCP-G heruntergeladen wird.

</br></br></br>

## 6.1 VCP-G vorbereiten
---
Stellen Sie vor Beginn des Download-Vorgangs sicher, dass sich der VCP-G in einer stabilen Position befindet und frei von möglichen Störungen ist. Stellen Sie sicher, dass alle Schalter und Anschlüsse leicht zugänglich sind und das 3.3V-Stromkabel korrekt angeschlossen ist.

</br></br></br>

## 6.2 Hardware mit dem Host-PC verbinden
---
Wenn Sie einen Ubuntu-Host verwenden, fahren Sie direkt mit Schritt 3 fort.  
1. usbipd-win herunterladen  
    Das Projekt usbipd-win ist erforderlich, um USB in WSL2 zu verwenden.   
    Laden Sie usbipd-win von https://learn.microsoft.com/ko-kr/windows/wsl/connect-usb#attach-a-usb-device herunter.
2. PowerShell ausführen und den VCP-G (in Windows als COM-Port erkannt) an WSL2 anhängen  
    Führen Sie die folgenden Befehle in Windows PowerShell aus (nicht in Linux).
    ```
    usbipd list
    ```
    ```
    usbipd bind --busid <busid>
    ```
    ```
    usbipd attach --wsl --busid <busid>
    ```
3. USB-Type-C-Kabel anschließen  
    Verwenden Sie ein USB-Type-C-Kabel, um das VCP-G-Board mit dem Entwicklungs-Host-PC zu verbinden.
4. USB-Verbindung überprüfen  
    Führen Sie in WSL2 die folgenden Befehle aus.
    ```
    sudo apt-get install usbutils && lsusb
    ```
    ```
    sudo dmesg | grep tty
    ```
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/Verify%20USB%20Connection.png"></p>
    <p align="center"><strong>Abbildung 6.1 USB-Verbindung überprüfen</strong></p>

Wenn die in Abbildung 6.1 dargestellte Ausgabe erscheint, ist die Verbindung erfolgreich hergestellt.

</br></br></br>

## 6.3 Software auf den VCP-G herunterladen
---

### 6.3.1 FWDN in einer Windows-Umgebung ausführen
1. Board in den Download-Modus versetzen  
   Schließen Sie das Stromkabel an das VCP-G-Board an, während Sie den FWDN-Schalter gedrückt halten.
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/Set%20Board%20to%20Download%20Mode.png"></p>
    <p align="center"><strong>Abbildung 6.2 Board in den Download-Modus versetzen</strong></p>

2. tcc70xx_pflash_boot_2M_ECC.rom in den Ordner fwdn_vcp kopieren
```
cp ~/topst-vcp/build/tcc70xx/gcc/output/tcc70xx_pflash_boot_2M_ECC.rom ~/topst-vcp/tools/fwdn_vcp/
```

3. Ordner fwdn_vcp auf Laufwerk C kopieren
```
cp -r ~/topst-vcp/tools/fwdn_vcp /mnt/c/
```

4. Auf fwdn_vcp.bat klicken  
    Verwenden Sie ***FWDN***, um die erstellte Software auf den 4 MB großen Flash-Speicher des VCP-G herunterzuladen.

    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/Click%20fwdn_vcp.bat.png"></p>
    <p align="center"><strong>Abbildung 6.3 Auf fwdn_vcp.bat klicken</strong></p>
```
[main:27] FWDN VCP v0.1.1 - 2022.8.12 11:38:19
Com port num : 10
[FWDNWindowsUART::OpenPort:34] Complete open port(\\.\COM10)
[ProtocolCB::StartVCPFWDN:45] Complete to receive start res
[FWDN_VCP::LoadFwdnFW:144] Complete to send start msg
[ProtocolCB::CheckResPacket:172] Complete to receive ack for cmd(0xFFFF0000(RECEIVE_HSM_CMD))
[FWDN_VCP::WriteFile:284] Complete to send command(0xFFFF0000(RECEIVE_HSM_CMD))
[ProtocolCB::SendFile:151] Complete to send file
[ProtocolCB::CheckResPacket:172] Complete to receive ack for cmd(0xFFFF0000(RECEIVE_HSM_CMD))
[FWDN_VCP::WriteFile:295] Complete to send file - .\tcc70xx_pflash_boot_2M_ECC.rom
[FWDN_VCP::LoadFwdnFW:163] Complete to send hsm
[ProtocolCB::CheckResPacket:172] Complete to receive ack for cmd(0xFFFF0001(RECEIVE_FWDN_CMD))
[FWDN_VCP::WriteFile:284] Complete to send command(0xFFFF0001(RECEIVE_FWDN_CMD))
[ProtocolCB::SendFile:126] uiRemainSize = 43136
[ProtocolCB::SendFile:151] Complete to send file
[ProtocolCB::CheckResPacket:172] Complete to receive ack for cmd(0xFFFF0001(RECEIVE_FWDN_CMD))
[FWDN_VCP::WriteFile:295] Complete to send file - .\vcp_fwdn.rom
[FWDN_VCP::LoadFwdnFW:173] Complete to send fwdn
[FWDN_VCP::LoadFwdnFW:179] Complete to load FWDN F/W
RM=00000000
MT
MR0=0000a042
MR1=00020018
MR2=00000000
[ProtocolFW::CheckResPacket:260] Complete to receive ack for cmd(0xAAAA0016(VERSION_CMD))
[FWDN_VCP::GetDeviceVersion:77]  FWDN Firmware Version(20230728)
[ProtocolFW::CheckResPacket:260] Complete to receive ack for cmd(0xAAAA0014(STORAGE_INFO_CMD))
[FWDN_VCP::InfoStorage:56]
#### SNOR Info ####
Manufacture ID: 0x9d
Device ID: 0x6015
Name: ISSI-IS25LP016D
Sector Size: 4 KiB (4096 Byte)
Total Capacity: 2 MiB (2097152 Byte)
4Byte Address Mode: Unsupported
#### EFLASH Info ####
DCYCRDCON 0x1e0002
DCYCWRCON 0x20100
Sector Size: 8 KiB
Page Size: 2 KiB

-----Storage init info-----
O : Init success
X : Init failed or not exist
SNOR : O
eFlash : O

[ProtocolFW::CheckResPacket:260] Complete to receive ack for cmd(0xAAAA0017(CHIP_INFO_CMD))
[FWDN_VCP::GetChipInfo:121] ---chip info---
Chip Number : 0x57045
Dual Bank : false
Expand Flash : true
ECC : true
[FWDN_VCP::PrintBankInfo:468] ---bank info---
bank - 0
eFlash offset : 0x0
eFlash size : 2097152 byte
SNOR offset : 0x0
SNOR size : 2097152 byte
[FWDN_VCP::PrintStorageOption:451] ---storage info---
eflash
offset : 0x0
size : 2097152 byte
[ProtocolFW::CheckResPacket:260] Complete to receive ack for cmd(0xAAAA0011(WRITE_CMD))
[FWDN_VCP::WriteFile:284] Complete to send command(0xAAAA0011(WRITE_CMD))
 100% [||||||||||||||||||||||||||||||] 2097152/2097152
```

5. Board zurücksetzen  
    Nachdem der Download-Vorgang abgeschlossen ist, trennen Sie das Stromkabel und schließen Sie es wieder an.
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/Reset%20the%20Board.png"></p>
    <p align="center"><strong>Abbildung 6.4 Board zurücksetzen</strong></p>

### 6.3.2 FWDN in einer Linux-Umgebung ausführen
1. Board in den Download-Modus versetzen  
   Schließen Sie das Stromkabel an das VCP-G-Board an, während Sie den FWDN-Schalter gedrückt halten.
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/Set%20Board%20to%20Download%20Mode.png"></p>
    <p align="center"><strong>Abbildung 6.5 Board in den Download-Modus versetzen</strong></p>
    
2. Download-Befehl ausführen  
   Verwenden Sie ***FWDN***, um die erstellte Software auf den 4 MB großen Flash-Speicher des VCP-G herunterzuladen.
    ```
    sudo ~/topst-vcp/tools/fwdn_vcp/fwdn --fwdn ~/topst-vcp/tools/fwdn_vcp/vcp_fwdn.rom -w output/tcc70xx_pflash_boot_2M_ECC.rom
    ```
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/Execute%20Download%20Command.png"></p>
    <p align="center"><strong>Abbildung 6.6 Download-Befehl ausführen</strong></p>
    
3. Board zurücksetzen  
    Nachdem der Download-Vorgang abgeschlossen ist, trennen Sie das Stromkabel und schließen Sie es wieder an.
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/Reset%20the%20Board.png"></p>
    <p align="center"><strong>Abbildung 6.7 Board zurücksetzen</strong></p>

</br></br></br>

## 6.4 Software auf dem Board überprüfen
---
Nachdem Sie die Software auf das Board heruntergeladen haben, führen Sie die folgenden Schritte aus, um zu überprüfen, ob sie korrekt funktioniert.
1. minicom installieren  
    ```
    sudo apt install minicom
    ```
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/Install%20Minicom.png"></p>
    <p align="center"><strong>Abbildung 6.8 minicom installieren</strong></p>
2. Serielle Verbindung öffnen  
    Verwenden Sie den folgenden Befehl, um eine serielle Verbindung herzustellen.
    ```
    minicom -D /dev/ttyUSB0 -b 115200 -8
    ```
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/Open%20Serial%20Connection.png"></p>
    <p align="center"><strong>Abbildung 6.9 Serielle Verbindung öffnen</strong></p>

Nach Abschluss der Schritte 1 und 2 erscheint die folgende Ausgabe im Terminal. Wenn die Verbindung erfolgreich ist, sollte das Board auf Interaktionen reagieren, was bestätigt, dass die Software heruntergeladen wurde und auf dem VCP-G korrekt funktioniert.
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/Figure%206.7%20Open%20Serial%20Connection.png"></p>
<p align="center"><strong>Abbildung 6.10 Serielle Verbindung öffnen</strong></p>

</br></br></br>

## 6.5 Fehlerbehebung bei häufigen Problemen
---
Dieses Kapitel enthält Lösungen für häufige Probleme, die bei der Arbeit mit dem VCP-G auftreten.

**Problem:** ***FWDN*** meldet fehlende Berechtigungen für den Zugriff auf das Gerät ttyUSB0.  
**Lösung:** Dieses Problem tritt auf, wenn Ihr Benutzerkonto (**$USER**) nicht über die erforderlichen Berechtigungen für den Zugriff auf serielle Geräte verfügt. Fügen Sie zur Behebung das Benutzerkonto der Gruppe dialout hinzu.

1. Berechtigungen der Benutzergruppe ändern  
    Führen Sie den folgenden Befehl aus.
    ```
    sudo usermod -aG dialout $USER
    ```
2. Abmelden und wieder anmelden  
    Melden Sie sich von der aktuellen Sitzung ab und wieder an, um die Änderungen zu übernehmen. Versuchen Sie danach erneut, auf das Gerät ttyUSB0 zuzugreifen.
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/Modify%20User%20Group%20Permissions.png"></p>
    <p align="center"><strong>Abbildung 6.11 Berechtigungen der Benutzergruppe ändern </strong></p>

**Problem:** Bei der Verwendung von minicom findet keine ordnungsgemäße Kommunikation mit dem VCP-G statt oder es tritt unregelmäßiges Verhalten auf.  
**Lösung:** Dieses Problem kann auftreten, wenn die Standardeinstellung für die Flusskontrolle von minicom auf **hardware** gesetzt ist. Die Hardware-Flusskontrolle muss für den ordnungsgemäßen Betrieb auf No gesetzt werden. 
1. minicom starten  
    Verwenden Sie den folgenden Befehl.
    ```
    minicom -D /dev/ttyUSB0 -b 115200 -8
    ```
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/Launch%20Minicom.png"></p>
    <p align="center"><strong>Abbildung 6.12 minicom starten</strong></p>
2. Setup-Bildschirm aufrufen  
    Drücken Sie in minicom **[Ctrl+A]** und anschließend **[o]**, um das Setup-Menü zu öffnen.
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/Access%20Set%20up%20Screen.png"></p>
    <p align="center"><strong>Abbildung 6.13 Setup-Bildschirm aufrufen</strong></p>
3. Zu Serial Port Setup navigieren  
    Wählen Sie **Serial port setup** aus den Optionen.
4. Flusskontrolle ändern  
    Drücken Sie im Serial Port Setup **[F]**, um die Hardware-Flusskontrolle auf **No** zu setzen.
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/Modify%20Flow%20Control.png"></p>
    <p align="center"><strong>Abbildung 6.14 Flusskontrolle ändern</strong></p>
5. Beenden und speichern  
    Beenden Sie das Setup und speichern Sie die Konfiguration. minicom sollte nun ordnungsgemäß mit dem VCP-G kommunizieren.
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/Save%20and%20Exit.png"></p>
    <p align="center"><strong>Abbildung 6.15 Speichern und beenden</strong></p>

**Hinweis:** Wenn Sie ein anderes serielles Kommunikationswerkzeug als minicom verwenden, stellen Sie sicher, dass dessen Einstellung für die Flusskontrolle ebenfalls auf **No** gesetzt ist, damit es ordnungsgemäß funktioniert.
</br></br></br></br>

# 7. Referenzen
---
- Kontaktieren Sie TOPST für weitere Einzelheiten: topst@topst.ai

**Hinweis:** Referenzdokumente können, sofern verfügbar, je nach Vertragsbedingungen bereitgestellt werden. Wenn die Referenzdokumente
nicht verfügbar sind, können die Inhalte, die sich direkt auf Ihre Entwicklung beziehen, erläutert werden.
