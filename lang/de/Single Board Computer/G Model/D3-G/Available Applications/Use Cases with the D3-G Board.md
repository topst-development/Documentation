# 1. Einführung 
---
In diesem Dokument werden Beispiele für die Verwendung des D3-G beschrieben.   
Dieses Dokument enthält die folgenden Informationen:
- Eingabegerät
  - Tastatur 
  - Maus
- Videoausgabe
- Kameraanschluss
  - MIPI CSI
  - USB-Webcam
- Speicheranschluss
  - SD-Karte
  - SATA HDD
  - NVMe M.2 SSD
  - USB-Speicher
- Ethernet-Verbindung
- 40-Pin-GPIO-Header
  - Verfügbare Sensoren und Geräte

<br/><br/><br/><br/>


# 2. Eingabegerät
---
Das D3-G unterstützt zwei USB-Anschlüsse für den Anschluss von Eingabegeräten.
Es verfügt über einen USB 2.0 Type-A-Anschluss und einen USB 3.0 Type-A-Anschluss, sodass Sie eine Maus oder eine Tastatur anschließen können, um das D3-G direkt zu steuern. 

**Hinweis**: Der USB Type-C-Anschluss am D3-G ist für Firmware-Downloads reserviert und kann nicht zum Anschließen von Eingabegeräten verwendet werden.

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20D3-G/Software/input%20device.png" width="500"></p>
<p align="center"><strong>Abbildung 2.1 Eingabegerät an das D3-G-Board anschließen </strong></p><br/><br/><br/><br/>


# 3. Videoausgabe
---
Das D3-G unterstützt FHD-Monitore ausschließlich über seinen DisplayPort-Ausgang (DP).
Es unterstützt außerdem die Multi-Display-Ausgabe über eine Daisy-Chain-Konfiguration, sodass gleichzeitig bis zu zwei FHD-Monitore und ein HD-Monitor angeschlossen werden können.

**Hinweis**: Für die Verwendung von HDMI ist ein separater aktiver Konverter-Adapter erforderlich.
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20D3-G/Software/monitor.png" width="500"></p>
<p align="center"><strong>Abbildung 3.1 Monitor an das D3-G-Board anschließen </strong></p>

<br/><br/><br/><br/>

# 4. Kameraanschluss
---
Das D3-G unterstützt Kamerafunktionen und bietet damit Flexibilität für verschiedene Anwendungen.
Sie können je nach den Anforderungen Ihres Projekts entweder eine MIPI-CSI-Kamera oder eine USB-Webcam anschließen.

<br/><br/><br/>

## 4.1 USB-Webcam
---
Das D3-G unterstützt USB-Webcams mit Auflösungen bis zu Full HD (FHD).
Sie können die Webcam mit den folgenden Schritten testen:


#### Schritt 1. Schließen Sie die USB-Kamera an einen USB-Anschluss des Boards an.
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20D3-G/Software/webcam.png" width="400"></p>
<p align="center"><strong>Abbildung 4.1 Webcam an das D3-G-Board anschließen</strong></p><br/>

#### Schritt 2. Schließen Sie die Eingabegeräte (Maus und Tastatur) sowie den Monitor an das D3-G an.
   
#### Schritt 3. Booten Sie das D3-G.

#### Schritt 4. Prüfen Sie die verfügbaren /dev/video-Geräte.
```
$ ls /dev/video*
```

#### Schritt 5. Überprüfen Sie die Videoausgabe mit OpenCV (oder vutils).
```
$ touch webcam.py
$ chmod a+x webcam.py
```
```
# You can edit the script file using vim or nano editor
# This is a Python camera application using OpenCV
import cv2

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("\\@@ Camera open failed!")
    exit()

print("Press 'q' to exit the camera window.")

cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

while True:
    ret, frame = cap.read()
    if not ret:
        print("\\@@ Failed to read frame")
        break

    cv2.imshow("Camera Feed", frame)

    # pressed 'q' key, escape
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
```
```
# Run the script
$ python3 webcam.py
```

<br/><br/><br/>

## 4.2 MIPI CSI
---
CSI steht für Camera Serial Interface, eine von der MIPI Alliance definierte Standardschnittstelle zum Anschließen von Kameramodulen an Host-Prozessoren.
Sie ermöglicht die schnelle und energiesparende Übertragung von Bilddaten von der Kamera zum Prozessor.

Das D3-G verfügt über zwei MIPI-CSI-Kanäle (ch0 und ch1), sodass Sie Kameramodule anschließen können, die Verbindungen über Flat Flexible Cable (FFC) unterstützen.
Derzeit unterstützt das D3-G nur die Module ArduCam (5 MP) und Raspberry Pi v1 Camera (5 MP). 

**Hinweis**: Derzeit unterstützt das D3-G nicht die gleichzeitige Verwendung von CSI-Kanal 0 und CSI-Kanal 1.

<br/><br/>

### 4.2.1 ArduCam
ArduCam ist ein vielseitiges Kameramodul, das für eingebettete Systeme und IoT-Anwendungen entwickelt wurde. Es unterstützt verschiedene Bildsensoren und Schnittstellen, darunter MIPI CSI, wodurch es sich für die Integration mit Entwicklungsboards wie dem D3-G eignet.
Das vom D3-G unterstützte 5-MP-ArduCam-Modul bietet eine ordentliche Bildqualität und wird häufig für einfache Computer-Vision-Aufgaben, für Streaming und für kamerabasierte KI-Anwendungen verwendet. Durch die Kompatibilität mit FFC-Kabeln lässt es sich einfach an die CSI-Schnittstelle des D3-G-Boards anschließen. 

Die technischen Daten des ArduCam-Moduls sind wie folgt.

| Spezifikation                     | Beschreibung                                |
| ------------------------ | ------------------------------------------- |
| Sensor                   | OV5647 (5 Megapixel)                        |
| Auflösung                | 2592 × 1944 (Full 5 MP)                      |
| Unterstützte Ausgabeformate | RAW, YUV, JPEG (sensorabhängig)          |
| Schnittstelle            | MIPI CSI-2                                  |
| Bildrate                 | Bis zu 30fps bei 1080p, 60fps bei 720p      |
| Objektivfassung          | Objektiv mit Fixfokus (Standard)            |
| Sichtfeld (FOV)          | Ungefähr 54° – 70° (je nach Modell)               |
| Anschlussart             | Flat Flexible Cable (FFC)                   |
| Betriebsspannung         | 3.3V (typisch)                              |
| Formfaktor               | Kompakte Platine, ungefähr 25 mm x 24 mm                   |
| Kompatibilität           | Raspberry Pi und D3-G (über MIPI-CSI-2-Anschluss)  |
| Zusätzliche Merkmale     | Geringer Stromverbrauch, Plug-and-Play-Modul |


Sie können die ArduCam mit den folgenden Schritten testen:
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20D3-G/Software/arducam.png" width="400"></p>
<p align="center"><strong>Abbildung 4.2 ArduCam </strong></p><br/>

#### Schritt 1. Schließen Sie die ArduCam an MIPI CSI 0 des D3-G-Boards an, wie in Abbildung 4.3 dargestellt.
 
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20D3-G/Software/rasp%20v1%20cam%20to%20d3g.png" width="500"></p>
<p align="center"><strong>Abbildung 4.3 ArduCam an das D3-G-Board anschließen</strong></p> <br/>

#### Schritt 2. Nachdem die ArduCam angeschlossen ist, können Sie den Videostream mit dem folgenden GStreamer-Befehl auf dem D3-G-Board überprüfen:
```
$ gst-launch-1.0 v4l2src device=/dev/video0 io-mode=2 ! video/x-raw,format=NV12,width=1920,height=1280,framerate=30/1 ! videoconvert ! waylandsink fullscreen=true
```

Dieser Befehl erfasst Video von der über CSI angeschlossenen ArduCam, konvertiert es für die Anzeige und stellt es im Vollbildmodus über den Wayland-Displayserver dar.  
Stellen Sie sicher, dass das Kameramodul fest angeschlossen ist, bevor Sie den Befehl ausführen. Wenn kein Video erscheint, prüfen Sie die Kabelverbindung und überprüfen Sie, ob /dev/video0 vom System korrekt erkannt wird.

<br/><br/>

### 4.2.2 Raspberry Pi v1 Camera
Das Raspberry Pi v1 Camera Module ist eine kompakte 5-MP-Kamera, die von der Raspberry Pi Foundation entwickelt wurde. Sie basiert auf dem Bildsensor OmniVision OV5647 und wird über eine MIPI-CSI-2-Schnittstelle mit einem Flat Flexible Cable (FFC) an das Host-Board angeschlossen.

Ursprünglich für die Raspberry-Pi-Serie entwickelt, ist dieses Modul auch mit dem D3-G kompatibel und damit eine zuverlässige Wahl für einfache Kameraanwendungen wie Bildaufnahme, Videoaufzeichnung und Computer-Vision-Projekte.

Die technischen Daten des Raspberry Pi v1 Kameramoduls sind wie folgt.

| Spezifikation                | Beschreibung                             |
| ------------------- | ---------------------------------------- |
| Sensor              | OmniVision OV5647                        |
| Auflösung           | 2592 × 1944 (5 MP)                        |
| Ausgabeformate      | RAW, YUV, JPEG                           |
| Schnittstelle       | MIPI CSI-2                               |
| Bildrate            | 1080p30, 720p60, VGA90                   |
| Objektiv            | Fixfokus                                 |
| Sichtfeld (FOV)     | Bis zu 54°                                    |
| Kabeltyp            | FFC (15-polig)                           |
| Board-Abmessungen   | 25 mm x 24 mm                              |
| Kompatibilität      | Raspberry Pi und D3-G (über MIPI-CSI-2-Anschluss) |

Sie können die Raspberry Pi v1 Camera mit den folgenden Schritten testen:

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20D3-G/Software/rasp%20v1%20cam.jpg" width="400"></p>
<p align="center"><strong>Abbildung 4.4. Raspberry Pi v1 Camera </strong></p><br/>

#### Schritt 1. Schließen Sie die Raspberry Pi v1 Camera an MIPI CSI 1 des D3-G-Boards an, wie in Abbildung 4.5 dargestellt.
 
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20D3-G/Software/rasp%20v1%20cam%20to%20d3g.png" width="500"></p>
<p align="center"><strong>Abbildung 4.5 Raspberry Pi v1 Camera an das D3-G-Board anschließen</strong></p> <br/>

#### Schritt 2. Nachdem die Raspberry Pi Kamera angeschlossen ist, können Sie den Videostream mit dem folgenden GStreamer-Befehl auf dem D3-G überprüfen:
```
$ gst-launch-1.0 v4l2src device=/dev/video0 io-mode=2 ! video/x-raw,format=NV12,width=1920,height=1280,framerate=30/1 ! videoconvert ! waylandsink fullscreen=true
```

Dieser Befehl erfasst Video von der über CSI angeschlossenen Raspberry Pi Kamera, konvertiert es für die Anzeige und stellt es im Vollbildmodus über den Wayland-Displayserver dar.  
Stellen Sie sicher, dass das Kameramodul fest angeschlossen ist, bevor Sie den Befehl ausführen. Wenn kein Video erscheint, prüfen Sie die Kabelverbindung und überprüfen Sie, ob /dev/video0 vom System korrekt erkannt wird.

<br/><br/><br/><br/>

# 5. Speicheranschluss
---
In diesem Kapitel wird beschrieben, wie Sie das D3-G an verschiedene Speichergeräte anschließen. Zu den unterstützten Speicheroptionen gehören USB-Laufwerke, SD-Karten und externer Speicher über PCIe.

<br/><br/><br/>

## 5.1 USB-Laufwerk
---
Das D3-G unterstützt USB-Speichergeräte über seine USB 2.0- und USB 3.0-Type-A-Anschlüsse.
So schließen Sie ein USB-Laufwerk an:

### Schritt 1. Stecken Sie das USB-Laufwerk in einen der verfügbaren USB-Type-A-Anschlüsse am D3-G.
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20D3-G/Software/usb%20storage%20connection%20with%20d3g.png" width="500"></p>
<p align="center"><strong>Abbildung 5.1 USB-Speicher an das D3-G-Board anschließen</strong></p> <br/>

### Schritt 2. Nach dem Anschließen wird das Gerät je nach Systemzustand typischerweise als /dev/sda1, /dev/sdb1 usw. erkannt.

<br/>

### Schritt 3. Sie können das USB-Laufwerk mit dem folgenden Befehl manuell einhängen:
   ```
   $ sudo mount /dev/sda1 /mnt
   ```

<br/><br/><br/>

## 5.2 SD-Karte
---
Das D3-G verfügt über einen microSD-Kartensteckplatz, der standardmäßige SDHC/SDXC-Karten unterstützt.
So verwenden Sie eine SD-Karte mit dem D3-G:

<br/>

### Schritt 1. Setzen Sie die microSD-Karte in den SD-Kartensteckplatz des D3-G-Boards ein.
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20D3-G/Software/sd%20card%20connect%20with%20d3g.png" width="500"></p>
<p align="center"><strong>Abbildung 5.2 SD-Karte an das D3-G-Board anschließen</strong></p> <br/>

### Schritt 2. Nach dem Einsetzen erkennt das System die SD-Karte typischerweise als /dev/mmcblk1p1 oder als ähnlichen Geräteknoten.
  ```
  $ ls /dev/mmcblk*
  ```
<br/>

### Schritt 3. Um die SD-Karte manuell einzuhängen, verwenden Sie den folgenden Befehl:
```
$ sudo mount /dev/mmcblk1p1 /mnt 
```
### Schritt 4. Nach dem Einhängen können Sie auf die Inhalte der SD-Karte im Verzeichnis /mnt zugreifen.

<br/><br/><br/>

## 5.3 SATA HDD
---

Das D3-G unterstützt die Verwendung von SATA-Speichergeräten wie HDDs oder SSDs über seinen PCIe-Steckplatz mit einem kompatiblen SATA-Controller.

<br/>

#### Schritt 1. Schließen Sie das PCIe-zu-SATA-Modul an

Um eine SATA-HDD über PCIe mit dem D3-G zu verwenden, müssen Sie zunächst ein PCIe-zu-SATA-Adaptermodul an den PCIe-Steckplatz des D3-G anschließen.

Schließen Sie anschließend die HDD an das SATA-Modul an und stellen Sie sicher, dass die HDD über eine externe 12V-Stromversorgung mit Strom versorgt wird.

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20D3-G/Software/sata.png" width="500"></p>
<p align="center"><strong>Abbildung 5.3 PCIe des D3-G-Boards an das SATA-Modul anschließen </strong></p><br/>

#### Schritt 2. Booten Sie das D3-G 
Beobachten Sie nach dem Booten des D3-G das Boot-Log, um zu überprüfen, ob das PCIe-Gerät vom System erkannt wird.
Achten Sie auf Meldungen wie **telechips-pcie: Link up**, die anzeigen, dass die PCIe-Verbindung erfolgreich hergestellt wurde.

```
Starting kernel ...

[    1.191696] telechips-pcie 11000000.pcie: invalid resource
[    1.230423] telechips-pcie 11000000.pcie: Link up
[    1.693516] debugfs: Directory '16680000.udma' with parent 'dmaengine' already present!
[    1.702282] debugfs: Directory '16681000.udma' with parent 'dmaengine' already present!
[    1.711022] debugfs: Directory '16682000.udma' with parent 'dmaengine' already present!
[    1.719799] debugfs: Directory '16683000.udma' with parent 'dmaengine' already present!
[    1.728562] debugfs: Directory '16684000.udma' with parent 'dmaengine' already present!
[    1.737308] debugfs: Directory '16685000.udma' with parent 'dmaengine' already present!
[    1.746084] debugfs: Directory '16686000.udma' with parent 'dmaengine' already present!
[    1.754824] debugfs: Directory '16687000.udma' with parent 'dmaengine' already present!
 
...
Ubuntu 22.04.5 LTS TOPST ttyAMA0

TOPST login: 
```

<br/>

#### Schritt 3. Erkennung der SATA-HDD prüfen
```
root@TOPST:~# lspci
00:00.0 PCI bridge: Synopsys, Inc. Device 8040 (rev 01)
01:00.0 SATA controller: ASMedia Technology Inc. Device 1064 (rev 02)
```
Wenn der Befehl **lspci** nicht verfügbar ist, installieren Sie pciutils mit dem folgenden Befehl.

```
$ sudo apt-get install pciutils
```

<br/>

#### Schritt 4. Die SATA-HDD einhängen
```
$ fdisk /dev/sda
Welcome to fdisk (util-linux 2.37.4).
Changes will remain in memory only, until you decide to write them.
Be careful before using the write command.

Command (m for help): 
```

Geben Sie die folgenden Tasten der Reihe nach in der fdisk-Eingabeaufforderung ein:

- o — Eine neue leere DOS-Partitionstabelle erstellen (optional, löscht die vorhandene Tabelle)

- n — Eine neue Partition hinzufügen

- p — Eine primäre Partition auswählen

- 1 — Die Partitionsnummer auf 1 setzen

- Enter drücken — Den Standardwert für den ersten Sektor übernehmen

- Enter drücken — Den Standardwert für den letzten Sektor übernehmen (nutzt die gesamte Festplatte)

- w — Die Partitionstabelle schreiben und beenden

```
$ mkfs.ext4 /dev/sda1

$ mkdir -p /mnt/sata

$ mount /dev/sda1 /mnt/sata
```

<br/>

#### Schritt 5. Ausführungsergebnis
Diese Ausgabe bestätigt, dass die SATA-SSD-Partition (/dev/sdb1) erfolgreich mit dem Dateisystem ext4 formatiert und unter /mnt/sata eingehängt wurde.
Der Befehl **df -h** zeigt, dass das Gerät nun erkannt wird und vom System verwendet werden kann.

```
$ df -h

Filesystem      Size  Used Avail Use% Mounted on
/dev/mmcblk0p4   29G  4.0G   25G  14% /
tmpfs           100M     0  100M   0% /dev/shm
tmpfs           592M  976K  591M   1% /run
tmpfs           5.0M  4.0K  5.0M   1% /run/lock
tmpfs           1.5G  4.0K  1.5G   1% /tmp
tmpfs           1.5G     0  1.5G   0% /var/volatile
tmpfs           296M  4.0K  296M   1% /run/user/0
/dev/sdb1       234G   28K  222G   1% /mnt/sata
```

<br/><br/><br/>

## 5.4 NVMe M.2 SSD
---
Das D3-G unterstützt den direkten Anschluss von NVMe-M.2-SSDs über seinen PCIe-Steckplatz.
<br/>

#### Schritt 1. Die SSD anschließen
- NVMe SSD (M.2 PCIe): Setzen Sie die NVMe-M.2-SSD in den PCIe-Steckplatz des D3-G ein. 

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20D3-G/Software/M.2%20SSD%20connection.png" width="600"></p>
<p align="center"><strong>Abbildung 5.4 NVMe-M.2-SSD an das D3-G-Board anschließen</strong></p><br/>

#### Schritt 2. Booten Sie das D3-G
Beobachten Sie nach dem Ausführen des Befehls **reboot** das Boot-Log, um zu überprüfen, ob das PCIe-Gerät vom System erkannt wird.
Achten Sie auf Meldungen wie **telechips-pcie: Link up**, die anzeigen, dass die PCIe-Verbindung erfolgreich hergestellt wurde.

```
$ reboot
...
Starting kernel ...

[    1.191696] telechips-pcie 11000000.pcie: invalid resource
[    1.230423] telechips-pcie 11000000.pcie: Link up
[    1.693516] debugfs: Directory '16680000.udma' with parent 'dmaengine' already present!
[    1.702282] debugfs: Directory '16681000.udma' with parent 'dmaengine' already present!
[    1.711022] debugfs: Directory '16682000.udma' with parent 'dmaengine' already present!
[    1.719799] debugfs: Directory '16683000.udma' with parent 'dmaengine' already present!
[    1.728562] debugfs: Directory '16684000.udma' with parent 'dmaengine' already present!
[    1.737308] debugfs: Directory '16685000.udma' with parent 'dmaengine' already present!
[    1.746084] debugfs: Directory '16686000.udma' with parent 'dmaengine' already present!
[    1.754824] debugfs: Directory '16687000.udma' with parent 'dmaengine' already present!
 
...
Ubuntu 22.04.5 LTS TOPST ttyAMA0

TOPST login: 
```

<br/>

#### Schritt 3. Erkennung der SSD prüfen
```
root@TOPST:~# lspci
00:00.0 PCI bridge: Synopsys, Inc. Device 8040 (rev 01)
01:00.0 Non-Volatile memory controller: Solid State Storage Technology Corporation Device 1007 (rev 03)
```
Wenn der Befehl **lspci** nicht verfügbar ist, installieren Sie pciutils mit dem folgenden Befehl.

```
$ sudo apt-get install pciutils
```

<br/>

#### Schritt 4. Die SSD einhängen
```
$ fdisk /dev/nvme0n1
Welcome to fdisk (util-linux 2.37.4).
Changes will remain in memory only, until you decide to write them.
Be careful before using the write command.

Command (m for help): 
```

Geben Sie die folgenden Tasten der Reihe nach in der fdisk-Eingabeaufforderung ein:

- o — Eine neue leere DOS-Partitionstabelle erstellen (optional, löscht die vorhandene Tabelle)

- n — Eine neue Partition hinzufügen

- p — Eine primäre Partition auswählen

- 1 — Die Partitionsnummer auf 1 setzen

- Enter drücken — Den Standardwert für den ersten Sektor übernehmen

- Enter drücken — Den Standardwert für den letzten Sektor übernehmen (nutzt die gesamte Festplatte)

- w — Die Partitionstabelle schreiben und beenden

```
$ mkfs.ext4 /dev/nvme0n1p1

$ mkdir -p /mnt/nvme

$ mount /dev/nvme0n1p1 /mnt/nvme
```

<br/>

#### Schritt 5. Ausführungsergebnis
Diese Ausgabe bestätigt, dass das NVMe SSD-Gerät (/dev/nvme0n1p1) erfolgreich vom System erkannt und unter /mnt/nvme eingehängt wurde.
```
$ df -h

Filesystem      Size  Used Avail Use% Mounted on
/dev/mmcblk0p4   29G  4.0G   25G  14% /
tmpfs           100M     0  100M   0% /dev/shm
tmpfs           592M  976K  591M   1% /run
tmpfs           5.0M  4.0K  5.0M   1% /run/lock
tmpfs           1.5G  4.0K  1.5G   1% /tmp
tmpfs           1.5G     0  1.5G   0% /var/volatile
tmpfs           296M  4.0K  296M   1% /run/user/0
/dev/nvme0n1p1  234G   28K  222G   1% /mnt/nvme
```
<br/><br/><br/><br/>


# 6. Ethernet-Verbindung
---
Das D3-G unterstützt Ethernet-Konnektivität über seinen integrierten J2C-Ethernet-Anschluss. Dadurch kann das D3-G über standardmäßige TCP/IP-Protokolle mit lokalen Netzwerken oder dem Internet kommunizieren. Ethernet wird häufig für die Bereitstellung von Anwendungen verwendet, die Fernzugriff, Datenstreaming oder Software-Updates erfordern.

<br/><br/><br/>

## 6.1 Netzwerkverbindung über einen Router
---
Bei dieser Methode wird das D3-G über einen Standardrouter mit einem lokalen Netzwerk verbunden. Das D3-G kann eine IP-Adresse automatisch über DHCP beziehen oder mit einer statischen IP-Adresse konfiguriert werden.

<br/><br/>

### 6.1.1 Netzwerk-Konfigurationsdatei erstellen

1. Dynamische IP über DHCP
Wenn Ihr Netzwerk einen DHCP-Server bereitstellt (zum Beispiel einen Router oder einen Windows-PC mit aktiviertem ICS), ist keine Bearbeitung von Dateien erforderlich. Das System bezieht automatisch eine IP-Adresse, sobald das Ethernet-Kabel angeschlossen ist.

Sie können das Kabel einfach einstecken und das Netzwerk sofort nutzen. Fahren Sie mit Kapitel 6.1.3 Netzwerkverbindung überprüfen fort.

2. Konfiguration einer statischen IP
Wenn Sie eine statische IP-Adresse vergeben möchten (zum Beispiel bei einer direkten PC-Verbindung oder wenn kein DHCP-Server verfügbar ist), bearbeiten Sie dieselbe Datei mit dem folgenden Inhalt:
```
$ vi /etc/systemd/network/20-wired.network

[Match]
Name=eth0

[Network]
Address=192.168.137.2/24
Gateway=192.168.137.1
DNS=8.8.8.8
```

Damit wird die IP-Adresse auf 192.168.137.2 gesetzt, 192.168.137.1 als Gateway verwendet (üblich bei Windows ICS) und der Google DNS konfiguriert.

<br/><br/>

### 6.1.2 Netzwerkdienst neu starten
Übernehmen Sie die neue Netzwerkkonfiguration, indem Sie den Dienst systemd-networkd neu starten:

```
sudo systemctl restart systemd-networkd
```

<br/><br/>

### 6.1.3 Netzwerkverbindung überprüfen
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20D3-G/Software/router%20connection.png"width="500"></p>
<p align="center"><strong>Abbildung 6.1 Netzwerkverbindung über einen Router</strong></p>

Testen Sie die Internetverbindung, indem Sie den öffentlichen DNS-Server von Google anpingen:

```
$ ping 8.8.8.8
PING 8.8.8.8 (8.8.8.8): 56 data bytes
64 bytes from 8.8.8.8: seq=0 ttl=113 time=30.208 ms
64 bytes from 8.8.8.8: seq=1 ttl=113 time=38.143 ms
64 bytes from 8.8.8.8: seq=2 ttl=113 time=30.969 ms
64 bytes from 8.8.8.8: seq=3 ttl=113 time=33.586 ms
 
```

<br/><br/><br/>

## 6.2 Netzwerkfreigabe mit dem Host-PC
---
Sie können die Internetverbindung Ihres PCs mit dem D3-G teilen, ohne einen Router zu verwenden, indem Sie die in Windows-Betriebssystemen verfügbare Funktion Internet Connection Sharing (ICS) nutzen.

<br/><br/>

### 6.2.1 Netzwerkkonfiguration des Host-PCs
- Systemsteuerung → Netzwerk und Internet → Netzwerkverbindung → Ethernet einrichten
 
1. Suchen Sie den mit dem Internet verbundenen Netzwerkadapter (zum Beispiel Wi-Fi), klicken Sie mit der rechten Maustaste darauf und wählen Sie **Eigenschaften**.

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20AI-G/Available%20Applications/ethernet1.png" width="600"></p>
<p align="center"><strong>Abbildung 6.2 Eigenschaften auswählen</strong></p><br/>
 
2. Wählen Sie die Registerkarte „Freigabe“ aus.

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20AI-G/Available%20Applications/ethernet2.png" width="400"></p>
<p align="center"><strong>Abbildung 6.3 Registerkarte „Freigabe“ auswählen</strong></p><br/>

3. Aktivieren Sie das Kontrollkästchen „Anderen Benutzern im Netzwerk gestatten, die Internetverbindung dieses Computers zu verwenden“.
 
4. Wählen Sie im Dropdown-Menü „Heimnetzwerkverbindung“ den Ethernet-Adapter aus, mit dem sich das D3-G verbinden soll (zum Beispiel „Ethernet“).

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20AI-G/Available%20Applications/ethernet3.png" width="400"></p>
<p align="center"><strong>Abbildung 6.4 Ethernet-Adapter auswählen</strong></p><br/>
 
5. Klicken Sie auf **OK**, um die Einstellungen zu speichern.

<br/><br/>

### 6.2.2 Netzwerkkonfigurationsdatei erstellen 
1. Dynamische IP über DHCP
Wenn Ihr Netzwerk einen DHCP-Server bereitstellt (zum Beispiel einen Router oder einen Windows-PC mit aktiviertem ICS), ist keine Bearbeitung von Dateien erforderlich. Das System bezieht automatisch eine IP-Adresse, sobald das Ethernet-Kabel angeschlossen ist.

Sie können einfach das Kabel einstecken und das Netzwerk sofort verwenden. Fahren Sie mit Kapitel 6.2.4 Netzwerkverbindung überprüfen fort.

2. Konfiguration einer statischen IP
Wenn Sie eine statische IP-Adresse vergeben möchten (zum Beispiel bei einer direkten PC-Verbindung oder wenn kein DHCP-Server verfügbar ist), bearbeiten Sie dieselbe Datei mit dem folgenden Inhalt:
```
$ vi /etc/systemd/network/20-wired.network

[Match]
Name=eth0

[Network]
Address=192.168.137.2/24
Gateway=192.168.137.1
DNS=8.8.8.8
```
Damit wird die IP-Adresse auf 192.168.137.2 gesetzt, 192.168.137.1 als Gateway verwendet (üblich bei Windows ICS) und der Google DNS konfiguriert.

<br/><br/>

### 6.2.3 Netzwerkdienst neu starten
Übernehmen Sie die neue Netzwerkkonfiguration, indem Sie den Dienst systemd-networkd neu starten:

```
sudo systemctl restart systemd-networkd
```

<br/><br/>

### 6.2.4 Netzwerkverbindung überprüfen
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20D3-G/Software/host%20pc%20ethernet%20connection.png"width="500"></p>
<p align="center"><strong>Abbildung 6.5 Netzwerkfreigabe mit dem Host-PC</strong></p>
<br/>

Testen Sie die Internetverbindung, indem Sie den öffentlichen DNS-Server von Google anpingen:

```
$ ping 8.8.8.8
PING 8.8.8.8 (8.8.8.8): 56 data bytes
64 bytes from 8.8.8.8: seq=0 ttl=113 time=30.208 ms
64 bytes from 8.8.8.8: seq=1 ttl=113 time=38.143 ms
64 bytes from 8.8.8.8: seq=2 ttl=113 time=30.969 ms
64 bytes from 8.8.8.8: seq=3 ttl=113 time=33.586 ms
```

<br/><br/><br/><br/>

# 7. 40-Pin-GPIO-Header
---
Das D3-G verfügt über einen 40-Pin-GPIO-Header, der flexible I/O-Möglichkeiten für verschiedene Hardware-Projekte bietet.
Dieser Header ist mit General-Purpose-Input/Output-Operationen (GPIO) kompatibel und kann zum Anschluss von Sensoren, LEDs, Tastern und anderen Peripheriegeräten verwendet werden.

Jeder Pin unterstützt je nach Konfiguration mehrere Funktionen wie digitale I/O, PWM, I2C, SPI und UART.

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/d3g/Assets/TOPST%20D3-G/Software/d3-g%20gpio%2040pinmap.png" width="800"></p>
<p align="center"><strong>Abbildung 7.1 Pinbelegung des 40-Pin-GPIO-Headers des D3-G </strong></p> <br/>

**Hinweis**: Weitere Informationen zu den Pin-Funktionen und Spannungspegeln finden Sie im offiziellen Pinout-Diagramm, bevor Sie externe Hardware anschließen.

<br/><br/><br/>

## 7.1 GPIO Digitale Ein-/Ausgabe
---
Das D3-G unterstützt digitale Ein- und Ausgabe (GPIO) über seinen 40-Pin-Header, sodass Sie mit externen Geräten wie Tastern, LEDs und Sensoren interagieren können. 

### 7.1.1 LED
---
Eines der einfachsten und häufigsten Beispiele für einen GPIO-Ausgang ist die Ansteuerung einer LED.  
In diesem Abschnitt wird gezeigt, wie Sie mit dem D3-G einen LED-Sensor anschließen und verwenden.

#### Schritt 1. Hardware-Anforderungen
- D3-G-Board (x1)
- Breadboard (x1)
- LED (x1)
- Jumperkabel Stecker auf Buchse (x2)
- DC-5V-Netzteil (x1)
- USB-zu-TTL-Seriellkabel (x1)

#### Schritt 2. Beispielschaltung
- LED
    - (+)-Pin an Pin 12 des D3-G-Boards angeschlossen.
    - (-)-Pin an Pin 14 angeschlossen, der auf dem D3-G-Board als GND dient.  
    
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20D3-G/Software/led.png"></p>

<p align="center"><strong>Abbildung 7.2 Schaltplan der D3-G-GPIO-LED </strong></p> <br/>

##### Schritt 2.1 Pinbelegung
Die folgende Tabelle zeigt die Pinbelegung.

<div align="center">
  <p><strong>Tabelle 7.1 Pinbelegung der D3-G-LED</strong></p>
  <table>
      <tr>
          <th colspan="3">Pin-Name</th>
          <th>D3-G</th>
          <th>GPIO</th>
      </tr>
      <tr>
          <td colspan="3">LED-(+)-Pin</td>
          <td>12</td>
          <td>89</td>
      </tr>
      <tr>
          <td colspan="3">LED-(-)-Pin</td>
          <td>14</td>
          <td>GND</td>
      </tr>
  </table>
</div>

#### Schritt 3. Ausführung
Um die an GPIO89 des D3-G-Boards angeschlossene LED zu betreiben, führen Sie den folgenden Code aus:

```
import time
import os
  
def export_gpio(pin, direction: str):
    # If the pin is already active, unexport it.
    if os.path.exists(f"/sys/class/gpio/gpio{pin}"):
        with open("/sys/class/gpio/unexport", "w") as f:
            f.write(str(pin))
  
    # Export the pin to activate it.
    with open("/sys/class/gpio/export", "w") as f:
        f.write(str(pin))
  
    # Set the pin direction.
    with open(f"/sys/class/gpio/gpio{pin}/direction", "w") as f:
        f.write(direction)

def read_gpio_value(pin: int):
    gpio_value_path = f"/sys/class/gpio/gpio{pin}/value"
    with open(gpio_value_path, "r") as f:
        return f.read().strip()

def write_gpio_value(pin: int, value: int):
    gpio_value_path = f"/sys/class/gpio/gpio{pin}/value"
    with open(gpio_value_path, "w") as f:
        f.write(str(value))

def unexport_gpio(pin: int):
    with open("/sys/class/gpio/unexport", "w") as f:
        f.write(str(pin))

  
def main():
    print("""\
                        +--------+
                    3P3-|-1    2-|-5P0
       I2C_SDA / GPIO82-|-3    4-|-5P0
       I2C_SCL / GPIO81-|-5    6-|-GND
                 GPIO83-|-7    8-|-GPIO87 / UT_TXD
                    GND-|-9   10-|-GPIO88 / UT_RXD
                 GPIO84-|-11  12-|-GPIO89 / PWM 0
                 GPIO85-|-13  14-|-GND
                 GPIO86-|-15  16-|-GPIO90
                    3P3-|-17  18-|-GPIO65
     SPIO_MOSI / GPIO63-|-19  20-|-GND
     SPIO_MISO / GPIO64-|-21  22-|-GPIO66
     SPIO_SCLK / GPIO61-|-23  24-|-GPIO62 / SPIO_CS0
                    GND-|-25  26-|-GPIO67 / SPIO_CS1
              RESERVED0-|-27  28-|-RESERVED1
                GPIO112-|-29  30-|-GND
                GPIO113-|-31  32-|-GPIO115 / PWM 2
         PWM1 / GPIO114-|-33  34-|-GND
    SPI1_MISO / GPIO121-|-35  36-|-GPIO119 / SPI1_CS0
                GPIO117-|-37  38-|-GPIO120 / SPI1_MOSI
                    GND-|-39  40-|-GPIO118 / SPI1_SCLK
                        +--------+""")
  
    LED_PIN = 89  # LED connected to GPIO 89
  
    try:
        # Setup the GPIO pins
        export_gpio(LED_PIN, direction="out")
        print("GPIO pins initialized.")
        
        count = 0
        while (count < 10):
            write_gpio_value(LED_PIN, 1)  # Turn on the LED
            print("LED ON.")
            count += 1
            time.sleep(1.0)  # Polling delay
            write_gpio_value(LED_PIN, 0)  # Turn off the LED
            print("LED OFF.")
            time.sleep(1.0)  # Polling delay
 
        write_gpio_value(LED_PIN, 0)  # Turn off the LED
 
    except KeyboardInterrupt:
        print("Program interrupted by user.")
  
    finally:
        unexport_gpio(LED_PIN) # unexport LED pin
        print("GPIO pins unexported.")
        print("Program terminated.")

if __name__ == "__main__":
    main()
```

#### Schritt 4. Ausführungsergebnis
Führen Sie den Code mit dem folgenden Befehl aus.

```
$ python3 led_test.py
```

Dieses Skript konfiguriert GPIO89 als digitalen Ausgang und wechselt dessen Zustand alle 1 Sekunde.
Bei der Ausführung blinkt die an GPIO89 angeschlossene LED 10-mal, wobei sie jeweils 1 Sekunde lang leuchtet und dann 1 Sekunde lang ausgeschaltet ist. Nach 10 Zyklen wird das Skript beendet und der Export des GPIO automatisch aufgehoben.

Um das Skript vorzeitig zu beenden, drücken Sie **[Ctrl+C]**.
In beiden Fällen wird der Pin ordnungsgemäß freigegeben und bereinigt.

**Hinweis**: Dieser Aufbau geht von einer direkten LED-Verbindung aus. Für einen sicheren und langfristigen Betrieb wird dringend empfohlen, einen strombegrenzenden Widerstand (zum Beispiel 220Ω) in Reihe zur LED zu verwenden, um eine übermäßige Stromaufnahme zu verhindern und den GPIO-Pin vor möglichen Schäden zu schützen.

<br/><br/><br/><br/>

### 7.1.2 Taster
---
Ein Taster ist ein einfaches Eingabegerät, das häufig verwendet wird, um die Verarbeitung digitaler Eingaben über GPIO zu demonstrieren.
In diesem Abschnitt wird gezeigt, wie Sie ein einfaches Tastermodul an das D3-G anschließen und verwenden.

#### Schritt 1. Hardware-Anforderungen
- D3-G-Board (x1)
- Breadboard (x1)
- Taster (x1)
- Jumperkabel Stecker auf Buchse (x2)
- DC-5V-Netzteil (x1)
- USB-zu-TTL-Seriellkabel (x1)

#### Schritt 2. Beispielschaltung
- Tasterschalter
    - Ein Anschlussbein des Tasters ist mit Pin 10 des D3-G-Boards verbunden.
    - Das gegenüberliegende Bein oberhalb des Tasters ist mit dem 3.3V-Pin verbunden.

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20D3-G/Software/button_circuit.png"></p> 
<p align="center"><strong>Abbildung 7.3 Schaltplan des D3-G-GPIO-Tasters</strong></p>

##### Schritt 2.1 Pinbelegung
Die folgende Tabelle zeigt die Pinbelegung.

<div align="center">
  <p><strong>Tabelle 7.2 Pinbelegung des D3-G-Tasters</strong></p>
  <table>
      <tr>
          <th colspan="3">Pin-Name</th>
          <th>D3-G</th>
          <th>GPIO</th>
      </tr>
      <tr>
          <td colspan="3">Ein Anschlussbein des Tasters</td>
          <td>10</td>
          <td>88</td>
      </tr>
  </table>
</div>

#### Schritt 3. Ausführung
Um die an GPIO88 des D3-G-Boards angeschlossene Tastereingabe zu überwachen, führen Sie den folgenden Code aus:

```
import os
import time
BUTTON_PIN = 88  # button sensor GPIO pin
 
def export_gpio(pin: int, direction: str):
    # If the pin is already active, unexport it.
    if os.path.exists(f"/sys/class/gpio/gpio{pin}"):
        with open("/sys/class/gpio/unexport", "w") as f:
            f.write(str(pin))
  
    # Export the pin to activate it.
    with open("/sys/class/gpio/export", "w") as f:
        f.write(str(pin))
  
    # Set the pin direction.
    with open(f"/sys/class/gpio/gpio{pin}/direction", "w") as f:
        f.write(direction)

def read_gpio_value(pin: int):
    gpio_value_path = f"/sys/class/gpio/gpio{pin}/value"
    with open(gpio_value_path, "r") as f:
        return f.read().strip()

def write_gpio_value(pin: int, value: int):
    gpio_value_path = f"/sys/class/gpio/gpio{pin}/value"
    with open(gpio_value_path, "w") as f:
        f.write(str(value))

def unexport_gpio(pin: int):
    with open("/sys/class/gpio/unexport", "w") as f:
        f.write(str(pin))
def main():
    # initialize GPIO pins
    export_gpio(BUTTON_PIN, "in")  
    print("gpio pins initialized.")
 
    try:
        while True:
            sensor_value = read_gpio_value(BUTTON_PIN)
 
            if sensor_value == "0":  
                print("button pressed.")
            else:    
                print("button released.")
 
            time.sleep(0.5)  # 500ms delay

    except KeyboardInterrupt:
        print("Program interrupted by user.")
 
    finally:
        unexport_gpio(BUTTON_PIN)  # unexport the GPIO pin
        print("GPIO pins unexported.")
        print("Program terminated.")
         
if __name__ == "__main__":
    main()
```

#### Schritt 4. Ausführungsergebnis
Führen Sie den Code mit dem folgenden Befehl aus.
```
$ python3 test_button.py
```
Dieses Skript konfiguriert GPIO88 als digitalen Eingang und überwacht dessen Wert kontinuierlich in Echtzeit.
Bei der Ausführung wird durch Drücken des an GPIO88 angeschlossenen Tasters eine Meldung ausgegeben, die anzeigt, dass der Taster gedrückt wurde.

Um das Skript zu beenden, drücken Sie **[Ctrl+C]**.
Wenn das Skript beendet wird, wird der Export von GPIO88 automatisch aufgehoben und der Pin bereinigt.

**Hinweis**: GPIO88 wird hier als Beispiel verwendet. Sie können jeden verfügbaren GPIO-Pin des D3-G gemäß der Pinbelegung des 40-Pin-Headers verwenden.
Siehe das offizielle Pinbelegungsdiagramm und wählen Sie eine GPIO-Nummer, die zu Ihrer Hardware-Konfiguration passt.

<br/><br/><br/><br/>

### 7.1.3 Berührungssensor
---
Ein Berührungssensor kann verwendet werden, um eine Berührung durch den Menschen als digitales Eingangssignal über GPIO zu erkennen.
In diesem Abschnitt wird gezeigt, wie Sie ein einfaches Berührungssensormodul mit dem D3-G anschließen und dessen Eingang auslesen.

#### Schritt 1. Hardware-Anforderungen
- D3-G-Board (x1)
- Touch-Sensor (x1)
- Buchse-auf-Buchse-Jumperkabel (x3)
- DC-5V-Netzteil (x1)
- USB-zu-TTL-Seriellkabel (x1)

#### Schritt 2. Beispielschaltung
- Berührungssensor
    - Der SIG-Pin des Berührungssensors ist mit Pin 88 des D3-G-Boards verbunden.
    - Der VCC-Pin des Berührungssensors ist mit 3.3V des D3-G-Boards verbunden.
    - Der GND-Pin des Berührungssensors ist mit GND des D3-G-Boards verbunden.


<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20D3-G/Software/touch%20circuit.png"></p>
<p align="center"><strong>Abbildung 7.4 Schaltplan des D3-G-GPIO-Berührungssensors</strong></p>

##### Schritt 2.1 Pinbelegung
Die folgende Tabelle zeigt die Pinbelegung.

<div align="center">
  <p><strong>Tabelle 7.3 Pinbelegung des D3-G-Berührungssensors</strong></p>
  <table>
      <tr>
          <th colspan="3">Pin-Name</th>
          <th>D3-G</th>
          <th>GPIO</th>
      </tr>
      <tr>
          <td colspan="3">SIG</td>
          <td>10</td>
          <td>88</td>
      </tr>
      <tr>
          <td colspan="3">VCC</td>
          <td>1</td>
          <td>3.3</td>
      </tr>
      <tr>
          <td colspan="3">GND</td>
          <td>20</td>
          <td>GND</td>
      </tr>
  </table>
</div>

#### Schritt 3. Ausführung
Um den an GPIO88 des D3-G-Boards angeschlossenen Berührungssensor zu überwachen, führen Sie einfach den folgenden Code aus:
```
import os
import time
 
# GPIO pin numbers setting
TOUCH_SENSOR_PIN = 88  # sensor GPIO pin
 
def export_gpio(pin: int, direction: str):
    # If the pin is already active, unexport it.
    if os.path.exists(f"/sys/class/gpio/gpio{pin}"):
        with open("/sys/class/gpio/unexport", "w") as f:
            f.write(str(pin))
  
    # Export the pin to activate it.
    with open("/sys/class/gpio/export", "w") as f:
        f.write(str(pin))
  
    # Set the pin direction.
    with open(f"/sys/class/gpio/gpio{pin}/direction", "w") as f:
        f.write(direction)

def read_gpio_value(pin: int):
    gpio_value_path = f"/sys/class/gpio/gpio{pin}/value"
    with open(gpio_value_path, "r") as f:
        return f.read().strip()

def write_gpio_value(pin: int, value: int):
    gpio_value_path = f"/sys/class/gpio/gpio{pin}/value"
    with open(gpio_value_path, "w") as f:
        f.write(str(value))

def unexport_gpio(pin: int):
    with open("/sys/class/gpio/unexport", "w") as f:
        f.write(str(pin))
def main():
    # initialize GPIO pins
    export_gpio(TOUCH_SENSOR_PIN, "in")  # touch sensor pin direction "in"
    print("gpio pins initialized.")
 
    try:
        while True:
            # button sensor value read
            # If the sensor value is 0, it means an touch detected.
            # If the sensor value is 1, it means no touch released.
            sensor_value = read_gpio_value(TOUCH_SENSOR_PIN)
 
            if sensor_value == "1":  
                print("touch detected.")
            else:    
                print("touch released.")
 
            time.sleep(0.5)  # 500ms delay

    except KeyboardInterrupt:
        print("program interrupted by user.")
 
    finally:
        unexport_gpio(TOUCH_SENSOR_PIN)  # unexport the GPIO pin
        print("GPIO pins unexported.")
        print("program terminated.")
         
if __name__ == "__main__":
    main()
```

#### Schritt 4. Ausführungsergebnis
Führen Sie den Code mit dem folgenden Befehl aus.

```
$ python3 touch_test.py
```

Dieses Skript konfiguriert GPIO88 als digitalen Eingang und überwacht dessen Wert kontinuierlich in Echtzeit.

Bei der Ausführung führt eine Berührung des Sensors dazu, dass im Terminal eine Meldung wie die folgende ausgegeben wird:
```
touch detected.
```
Wenn der Sensor nicht berührt wird, lautet die Ausgabe:
```
touch released.
```
Um das Skript zu beenden, drücken Sie **[Ctrl+C]**.
Wenn das Skript beendet wird, wird der Export von GPIO88 automatisch aufgehoben und der Pin bereinigt.

**Hinweis**: GPIO88 wird hier als Beispiel verwendet. Sie können jeden verfügbaren GPIO-Pin des D3-G gemäß der Pinbelegung des 40-Pin-Headers verwenden.
Siehe das offizielle Pinbelegungsdiagramm und wählen Sie eine GPIO-Nummer, die zu Ihrer Hardware-Konfiguration passt.

<br/><br/><br/><br/>

### 7.1.4 Vibrationserkennungssensor
---
Ein Vibrationssensor kann verwendet werden, um physische Erschütterungen oder Vibrationen zu erkennen und ein digitales Eingangssignal über GPIO auszugeben.
In diesem Abschnitt wird gezeigt, wie Sie ein einfaches Vibrationssensormodul mit dem D3-G anschließen und dessen Eingang erfassen.

#### Schritt 1. Hardware-Anforderungen
- D3-G-Board (x1)
- Vibrationserkennungssensor (x1)
- Jumperkabel Buchse-Buchse (x4)
- DC-5V-Netzteil (x1)
- USB-zu-TTL-Seriellkabel (x1)

#### Schritt 2. Beispielschaltung
- Vibrationserkennungssensor
    - Der VCC-Pin des Vibrationserkennungssensors ist mit dem 3.3V-Pin des D3-G-Boards verbunden.
    - Der GND-Pin des Vibrationserkennungssensors ist mit GND des D3-G-Boards verbunden.
    - Der DO-Pin des Vibrationserkennungssensors ist mit Pin 88 des D3-G-Boards verbunden.

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20D3-G/Software/vibr%20circuit.png"></p>
<p align="center"><strong>Abbildung 7.5 Schaltplan des D3-G-GPIO-Vibrationserkennungssensors</strong></p>

##### Schritt 2.1 Pinbelegung
Die folgende Tabelle zeigt die Pinbelegung.

<div align="center">
  <p><strong>Tabelle 7.4 Pinbelegung des D3-G-Vibrationserkennungssensors</strong></p>
  <table>
      <tr>
          <th colspan="3">Pin-Name</th>
          <th>D3-G</th>
          <th>GPIO</th>
      </tr>
      <tr>
          <td colspan="3">VCC</td>
          <td>1</td>
          <td>3.3V</td>
      </tr>
      <tr>
          <td colspan="3">GND</td>
          <td>20</td>
          <td>GND</td>
      </tr>
      <tr>
          <td colspan="3">DO</td>
          <td>10</td>
          <td>88</td>
      </tr>
  </table>
</div>

#### Schritt 3. Ausführung
Um den an GPIO88 des D3-G-Boards angeschlossenen Vibrationssensor zu überwachen, führen Sie den folgenden Code aus:
```
import os
import time
VIBRATION_SENSOR_PIN = 88  # VIBRATION_SENSOR sensor GPIO pin
 
def export_gpio(pin: int, direction: str):
    # If the pin is already active, unexport it.
    if os.path.exists(f"/sys/class/gpio/gpio{pin}"):
        with open("/sys/class/gpio/unexport", "w") as f:
            f.write(str(pin))
  
    # Export the pin to activate it.
    with open("/sys/class/gpio/export", "w") as f:
        f.write(str(pin))
  
    # Set the pin direction.
    with open(f"/sys/class/gpio/gpio{pin}/direction", "w") as f:
        f.write(direction)

def read_gpio_value(pin: int):
    gpio_value_path = f"/sys/class/gpio/gpio{pin}/value"
    with open(gpio_value_path, "r") as f:
        return f.read().strip()

def write_gpio_value(pin: int, value: int):
    gpio_value_path = f"/sys/class/gpio/gpio{pin}/value"
    with open(gpio_value_path, "w") as f:
        f.write(str(value))

def unexport_gpio(pin: int):
    with open("/sys/class/gpio/unexport", "w") as f:
        f.write(str(pin))
def main():
    # initialize GPIO pins
    export_gpio(VIBRATION_SENSOR_PIN, "in")  # vibration sensor pin direction "in"
    print("gpio pins initialized.")
 
    try:
        while True:
            sensor_value = read_gpio_value(VIBRATION_SENSOR_PIN)
 
            if sensor_value == "0":  # vibration detected
                print("vibration detected.")
            else:    # no vibration detected
                print("no vibration detected.")
 
            time.sleep(0.5)  # 500ms delay

    except KeyboardInterrupt:
        print("Program interrupted by user.")
 
    finally:
        unexport_gpio(VIBRATION_SENSOR_PIN)  # unexport the GPIO pin
        print("GPIO pins unexported.")
        print("Program terminated.")
         
if __name__ == "__main__":
    main()
```

#### Schritt 4. Ausführungsergebnis
Führen Sie den Code mit dem folgenden Befehl aus.

```
$ python3 vibration_test.py
```

Dieses Skript konfiguriert GPIO88 als digitalen Eingang und überwacht dessen Wert kontinuierlich in Echtzeit.
Bei der Ausführung führen vom Sensor erkannte Vibrationen oder Erschütterungen dazu, dass im Terminal eine Meldung wie die folgende ausgegeben wird:
```
vibration detected.
```
Wenn keine Vibration vorliegt, lautet die Ausgabe:
```
no vibration detected.
```
Um das Skript zu beenden, drücken Sie **[Ctrl+C]**.
Bei Beendigung wird der Export von GPIO88 automatisch aufgehoben und der Pin bereinigt.

**Hinweis**: GPIO88 wird hier als Beispiel verwendet. Sie können je nach Verdrahtung Ihres Sensors und Layout des Headers jeden anderen verfügbaren GPIO-Pin verwenden. Siehe die Pinbelegung des D3-G, bevor Sie eine GPIO-Nummer auswählen.

<br/><br/><br/><br/>

### 7.1.5 Infrarotsensor (SZH-SSBH-002)
---
Ein Infrarotsensor kann verwendet werden, um nahe gelegene Hindernisse zu erkennen, indem er reflektiertes Infrarotlicht erfasst und ein digitales Signal über GPIO ausgibt.
In diesem Abschnitt wird gezeigt, wie Sie den Infrarotsensor SZH-SSBH-002 mit dem D3-G anschließen und dessen Eingang auslesen.

#### Schritt 1. Hardware-Anforderungen
- D3-G-Board (x1)
- Breadboard (x1)
- Infrarotsensor (x1)
- Stecker-auf-Buchse-Jumperkabel (x5)
- DC-5V-Netzteil (x1)
- USB-zu-TTL-Seriellkabel (x1)

#### Schritt 2. Beispielschaltung
- Infrarotsensor
    - Der VCC-Pin des Infrarotsensors ist mit dem 3.3V-Pin des D3-G-Boards verbunden.
    - Der GND-Pin des Infrarotsensors ist mit GND des D3-G-Boards verbunden.
    - Der OUT-Pin des Infrarotsensors ist mit Pin 89 des D3-G-Boards verbunden.


<p align="center">
  <img src="https://raw.githubusercontent.com/topst-development/Documentation/d3g/Assets/TOPST%20D3-G/Software/szh-ssbh-002_circuit.png">
</p> 
<p align="center"><strong>Abbildung 7.6 Versuchsschaltung des IR-Sensors</strong></p>

##### Schritt 2.1 Pinbelegung
Die folgende Tabelle zeigt die Pinbelegung.

<div align="center">
  <p><strong>Tabelle 7.5 Pinbelegung des D3-G-IR-Sensors</strong></p>
  <table>
      <tr>
          <th colspan="3">Pin-Name</th>
          <th>D3-G</th>
          <th>GPIO</th>
      </tr>
      <tr>
          <td colspan="3">VCC</td>
          <td>1</td>
          <td>3.3V</td>
      </tr>
      <tr>
          <td colspan="3">GND</td>
          <td>6</td>
          <td>GND</td>
      </tr>
      <tr>
          <td colspan="3">OUT</td>
          <td>12</td>
          <td>89</td>
      </tr>
  </table>
</div>

#### Schritt 3. Ausführung
Um den an GPIO89 des D3-G-Boards angeschlossenen IR-Sensor zu überwachen, führen Sie den folgenden Code aus:

```
import os
import time
 
# GPIO pin numbers setting
IR_SENSOR_PIN = 89  # IR sensor GPIO pin
 
def export_gpio(pin: int, direction: str):
    # If the pin is already active, unexport it.
    if os.path.exists(f"/sys/class/gpio/gpio{pin}"):
        with open("/sys/class/gpio/unexport", "w") as f:
            f.write(str(pin))
  
    # Export the pin to activate it.
    with open("/sys/class/gpio/export", "w") as f:
        f.write(str(pin))
  
    # Set the pin direction.
    with open(f"/sys/class/gpio/gpio{pin}/direction", "w") as f:
        f.write(direction)

def read_gpio_value(pin: int):
    gpio_value_path = f"/sys/class/gpio/gpio{pin}/value"
    with open(gpio_value_path, "r") as f:
        return f.read().strip()

def write_gpio_value(pin: int, value: int):
    gpio_value_path = f"/sys/class/gpio/gpio{pin}/value"
    with open(gpio_value_path, "w") as f:
        f.write(str(value))

def unexport_gpio(pin: int):
    with open("/sys/class/gpio/unexport", "w") as f:
        f.write(str(pin))
def main():
    # initialize GPIO pins
    export_gpio(IR_SENSOR_PIN, "in")  # IR sensor pin direction "in"
    print("gpio pins initialized.")
 
    try:
        while True:
            sensor_value = read_gpio_value(IR_SENSOR_PIN)
 
            if sensor_value == "0":  # obstacle detected
                print("obstacle detected.")
            else: 
                print("No obstacle detected.")
 
            time.sleep(0.5)  # 500ms delay

    except KeyboardInterrupt:
        print("program interrupted by user.")
 
    finally:
        unexport_gpio(IR_SENSOR_PIN)  # unexport the GPIO pin
        print("GPIO pins unexported.")
        print("program terminated.")
         
if __name__ == "__main__":
    main()
```

#### Schritt 4. Ausführungsergebnis
Führen Sie den Code mit dem folgenden Befehl aus.
```
$ python3 ir_test.py
```
Dieses Skript konfiguriert GPIO89 als digitalen Eingang und überwacht dessen Zustand kontinuierlich, um Hindernisse zu erkennen.
Wenn ein Objekt vor dem IR-Sensor erkannt wird, zeigt das Terminal Folgendes an:
```
obstacle detected.
```
Wenn kein Objekt erkannt wird, zeigt es Folgendes an:
```
no obstacle detected.
```
Um das Skript zu beenden, drücken Sie **[Ctrl+C]**.
Wenn das Skript beendet wird, wird der Export von GPIO89 automatisch aufgehoben und der Pin bereinigt.

**Hinweis**: GPIO89 wird in diesem Skript als Beispiel verwendet.
Sie können jeden verfügbaren GPIO-Pin gemäß dem 40-Pin-Header des D3-G verwenden. Siehe das offizielle Pinbelegungsdiagramm für eine korrekte Pin-Auswahl.

<br/><br/><br/><br/>

### 7.1.6 Fotowiderstand (SZH-SSBH-011)
---
Ein Fotowiderstand kann verwendet werden, um die Umgebungshelligkeit zu erfassen und ein digitales Signal über GPIO auszugeben, wenn die Lichtintensität einen bestimmten Schwellenwert überschreitet.
In diesem Abschnitt wird gezeigt, wie Sie das Fotowiderstandsmodul SZH-SSBH-011 mit dem D3-G anschließen und dessen Eingang auslesen.

#### Schritt 1. Hardware-Anforderungen
- D3-G-Board (x1)
- Fotowiderstandsmodul (SZH-SSBH-011) (x1)
- LED (x1)
- 220Ω-Widerstand (x1)
- Breadboard (x1)
- Stecker-auf-Buchse-Jumperkabel (x7)
- DC-5V-Netzteil (x1)
- USB-zu-TTL-Seriellkabel (x1)

#### Schritt 2. Beispielschaltung
- Fotowiderstand (SZH-SSBH-011)
    - Der VCC-Pin des Fotowiderstands ist mit dem 3.3V-Pin des D3-G-Boards verbunden.
    - Der GND-Pin des Fotowiderstands ist mit GND des D3-G-Boards verbunden.
    - Der DO-Pin des Fotowiderstands ist mit Pin 89 des D3-G-Boards verbunden.
- LED
    - Der (+)-Pin der LED ist mit GND des D3-G-Boards verbunden.
    - Der (-)-Pin der LED ist mit Pin 83 des D3-G-Boards verbunden.

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20D3-G/Software/circuit.png"></p>
<p align="center"><strong>Abbildung 7.7 Versuchsschaltung des Fotowiderstands</strong></p>

##### Schritt 2.1 Pinbelegung
Die folgende Tabelle zeigt die Pinbelegung.

<div align="center">
  <p><strong>Tabelle 7.6 Pinbelegung des D3-G-Fotowiderstands</strong></p>
  <table>
      <tr>
          <th colspan="3">Pin-Name</th>
          <th>D3-G</th>
          <th>GPIO</th>
      </tr>
      <tr>
          <td colspan="3">VCC</td>
          <td>1</td>
          <td>3.3V</td>
      </tr>
      <tr>
          <td colspan="3">GND</td>
          <td>6</td>
          <td>GND</td>
      </tr>
      <tr>
          <td colspan="3">DO</td>
          <td>12</td>
          <td>89</td>
      </tr>
  </table>
</div>


<div align="center">
  <p><strong>Tabelle 7.7 Pinbelegung der D3-G-LED</strong></p>
  <table>
      <tr>
          <th colspan="3">Pin-Name</th>
          <th>D3-G</th>
          <th>GPIO</th>
      </tr>
      <tr>
          <td colspan="3">(+)</td>
          <td>7</td>
          <td>83</td>
      </tr>
      <tr>
          <td colspan="3">(-)</td>
          <td>14</td>
          <td>GND</td>
      </tr>
  </table>
</div>

### Schritt 3. Ausführung
Führen Sie das folgende Python-Skript aus, um die Helligkeit mit dem CDS-Sensor zu überwachen und die LED entsprechend zu steuern:

```
import os
import time
LED_PIN = 83           # LED GPIO pin
CDS_SENSOR_PIN = 89    # szh-ssbh-011 CDS sensor GPIO pin

def export_gpio(pin, direction: str):
    # If the pin is already active, unexport it.
    if os.path.exists(f"/sys/class/gpio/gpio{pin}"):
        with open("/sys/class/gpio/unexport", "w") as f:
            f.write(str(pin))
  
    # Export the pin to activate it.
    with open("/sys/class/gpio/export", "w") as f:
        f.write(str(pin))
  
    # Set the pin direction.
    with open(f"/sys/class/gpio/gpio{pin}/direction", "w") as f:
        f.write(direction)

def read_gpio_value(pin: int):
    gpio_value_path = f"/sys/class/gpio/gpio{pin}/value"
    with open(gpio_value_path, "r") as f:
        return f.read().strip()

def write_gpio_value(pin: int, value: int):
    gpio_value_path = f"/sys/class/gpio/gpio{pin}/value"
    with open(gpio_value_path, "w") as f:
        f.write(str(value))

def unexport_gpio(pin: int):
    with open("/sys/class/gpio/unexport", "w") as f:
        f.write(str(pin))

def main():
    # initialize GPIO pins
    export_gpio(LED_PIN, "out")          # LED pin direction "out"
    export_gpio(CDS_SENSOR_PIN, "in")     # CDS sensor pin direction "in"
    print("gpio pins initialized.")

    try:
        while True:
            sensor_value = read_gpio_value(CDS_SENSOR_PIN)
            print("sensor value: {}".format(sensor_value))
            if sensor_value == "0": # light detected
                print("brightness detected. Turning on the LED.")
                write_gpio_value(LED_PIN, 1)  # turn on the LED
            else:
                print("no brightness detected. Turning off the LED.")
                write_gpio_value(LED_PIN, 0)  # turn off the LED

            time.sleep(0.5)  #  500ms delay

    except KeyboardInterrupt:
        print("program interrupted by user.")

    finally:
        unexport_gpio(LED_PIN)          # unexport LED pin
        unexport_gpio(CDS_SENSOR_PIN)   # unexport CDS sensor pin
        print("GPIO pins unexported.")
        print("program terminated.")

if __name__ == "__main__":
    main()
```

### Schritt 4. Ausführungsergebnis
Führen Sie den Code mit dem folgenden Befehl aus.
```
$ python3 CDS_test.py
```
Dieses Skript konfiguriert GPIO89 als Eingang für den Fotowiderstandssensor und GPIO83 als Ausgang für die LED.
Wenn Umgebungslicht erkannt wird, gibt das Terminal Folgendes aus:
```
sensor value: 0
brightness detected. Turning on the LED.
```
und die LED schaltet sich EIN.
Wenn kein Licht erkannt wird, gibt es Folgendes aus:
```
sensor value: 1
no brightness detected. Turning off the LED.
```
und die LED schaltet sich AUS.
Um das Skript zu beenden, drücken Sie **[Ctrl+C]**.
Wenn das Skript beendet wird, wird der Export beider GPIO-Pins automatisch aufgehoben und sie werden bereinigt.

**Hinweis**: GPIO83 und GPIO89 werden in diesem Beispiel verwendet. Sie können jeden verfügbaren GPIO-Pin gemäß dem Layout des 40-Pin-Headers des D3-G verwenden. Siehe das offizielle Pinbelegungsdiagramm für eine korrekte Pin-Auswahl.

<br/><br/><br/><br/>

### 7.1.7 Luftverschmutzungssensor
---
Ein Luftverschmutzungssensor kann verwendet werden, um das Vorhandensein schädlicher Gase oder von Feinstaub in der Umgebung zu überwachen und ein digitales Signal über GPIO auszugeben.
In diesem Abschnitt wird gezeigt, wie Sie einen Luftverschmutzungssensor mit dem D3-G anschließen und dessen Eingang auslesen.

#### Schritt 1. Hardware-Anforderungen
- D3-G-Board (x1)
- Luftverschmutzungs-(Gas-)Sensormodul (x1)
- Breadboard (x1)
- Stecker-auf-Buchse-Jumperkabel (x3)
- DC-5V-Netzteil (x1)
- USB-zu-TTL-Seriellkabel (x1)

#### Schritt 2. Beispielschaltung
- Luftverschmutzungssensor
    - Der VCC-Pin des Luftverschmutzungssensors ist mit dem 3.3V-Pin des D3-G-Boards verbunden.
    - Der GND-Pin des Luftverschmutzungssensors ist mit GND des D3-G-Boards verbunden.
    - Der DO-Pin des Luftverschmutzungssensors ist mit Pin 88 des D3-G-Boards verbunden.

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20D3-G/Software/gas%20circuit.png"></p>
<p align="center"><strong>Abbildung 7.8 Versuchsschaltung des Luftverschmutzungssensors</strong></p>

##### Schritt 2.1 Pinbelegung
Die folgende Tabelle zeigt die Pinbelegung.

<div align="center">
  <p><strong>Tabelle 7.8 Pinbelegung des D3-G-Luftverschmutzungssensors</strong></p>
  <table>
      <tr>
          <th colspan="3">Pin-Name</th>
          <th>D3-G</th>
          <th>GPIO</th>
      </tr>
      <tr>
          <td colspan="3">VCC</td>
          <td>1</td>
          <td>3.3V</td>
      </tr>
      <tr>
          <td colspan="3">GND</td>
          <td>20</td>
          <td>GND</td>
      </tr>
      <tr>
          <td colspan="3">DO</td>
          <td>10</td>
          <td>88</td>
      </tr>
  </table>
</div>

#### Schritt 3. Ausführung
Führen Sie das folgende Python-Skript aus, um die Gaserkennung über den Pin GPIO88 zu überwachen:

```
import os
import time
GAS_SENSOR_PIN = 88  # gas sensor GPIO pin
 
def export_gpio(pin: int, direction: str):
    # If the pin is already active, unexport it.
    if os.path.exists(f"/sys/class/gpio/gpio{pin}"):
        with open("/sys/class/gpio/unexport", "w") as f:
            f.write(str(pin))
  
    # Export the pin to activate it.
    with open("/sys/class/gpio/export", "w") as f:
        f.write(str(pin))
  
    # Set the pin direction.
    with open(f"/sys/class/gpio/gpio{pin}/direction", "w") as f:
        f.write(direction)

def read_gpio_value(pin: int):
    gpio_value_path = f"/sys/class/gpio/gpio{pin}/value"
    with open(gpio_value_path, "r") as f:
        return f.read().strip()

def write_gpio_value(pin: int, value: int):
    gpio_value_path = f"/sys/class/gpio/gpio{pin}/value"
    with open(gpio_value_path, "w") as f:
        f.write(str(value))

def unexport_gpio(pin: int):
    with open("/sys/class/gpio/unexport", "w") as f:
        f.write(str(pin))
def main():
    # initialize GPIO pins
    export_gpio(GAS_SENSOR_PIN, "in")  # gas sensor pin direction "in"
    print("gpio pins initialized.")
 
    try:
        while True:
            # gas sensor value read
            sensor_value = read_gpio_value(GAS_SENSOR_PIN)
 
            if sensor_value == "0":  # gas detected
                print("gas detected.")
            else:
                print("no gas detected.")
 
            time.sleep(0.5)  # 500ms delay

    except KeyboardInterrupt:
        print("program interrupted by user.")
 
    finally:
        unexport_gpio(GAS_SENSOR_PIN)  # unexport the GPIO pin
        print("GPIO pins unexported.")
        print("program terminated.")
         
if __name__ == "__main__":
    main()
```

#### Schritt 4. Ausführungsergebnis
Führen Sie den Code mit dem folgenden Befehl aus.
```
$ python3 gas_sensor_test.py
```
Dieses Skript konfiguriert GPIO88 als digitalen Eingang und überwacht kontinuierlich den Status der Gaserkennung.
Wenn die Gaskonzentration den Schwellenwert des Sensors erreicht, zeigt das Terminal Folgendes an:
```
gas detected.
```
Wenn kein Gas erkannt wird, zeigt das Terminal Folgendes an:
```
no gas detected.
```
Um das Skript zu beenden, drücken Sie **[Ctrl+C]**.
Wenn das Skript beendet wird, wird der Export von GPIO88 automatisch aufgehoben und der Pin bereinigt.

**Hinweis**: GPIO88 wird hier als Beispiel verwendet. Sie können jeden verfügbaren GPIO-Pin gemäß dem Layout des 40-Pin-Headers des D3-G verwenden. Siehe das offizielle Pinbelegungsdiagramm für eine korrekte Pin-Auswahl.

<br/><br/><br/><br/>

### 7.1.8 Ultraschallsensor
---
Ein Ultraschallsensor kann verwendet werden, um die Entfernung zu nahe gelegenen Objekten zu messen, indem er Ultraschallwellen aussendet und das reflektierte Signal empfängt und anschließend ein digitales (oder impulsbasiertes) Signal über GPIO ausgibt.
In diesem Abschnitt wird gezeigt, wie Sie einen Ultraschallsensor mit dem D3-G anschließen und dessen Eingang auslesen.

#### Schritt 1. Hardware-Anforderungen
- D3-G-Board (x1)
- Ultraschallsensor (x1)
- Buchse-auf-Buchse-Jumperkabel (x4)
- DC-5V-Netzteil (x1)
- USB-zu-TTL-Seriellkabel (x1)

#### Schritt 2. Beispielschaltung
- Ultraschallsensor
    - Der VCC-Pin des Ultraschallsensors ist mit dem 5V-Pin des D3-G-Boards verbunden.
    - Der GND-Pin des Ultraschallsensors ist mit GND des D3-G-Boards verbunden.
    - Der TRIG-Pin des Ultraschallsensors ist mit Pin 82 des D3-G-Boards verbunden.
    - Der ECHO-Pin des Ultraschallsensors ist mit Pin 88 des D3-G-Boards verbunden.

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20D3-G/Software/ultra%20circuit.png"></p>
<p align="center"><strong>Abbildung 7.9 Versuchsschaltung des Ultraschallsensors</strong></p>

##### Schritt 2.1 Pinbelegung
Die folgende Tabelle zeigt die Pinbelegung.

<div align="center">
  <p><strong>Tabelle 7.9 Pinbelegung des D3-G-Ultraschallsensors</strong></p>
  <table>
      <tr>
          <th colspan="3">Pin-Name</th>
          <th>D3-G</th>
          <th>GPIO</th>
      </tr>
      <tr>
          <td colspan="3">VCC</td>
          <td>2</td>
          <td>5V</td>
      </tr>
      <tr>
          <td colspan="3">GND</td>
          <td>6</td>
          <td>GND</td>
      </tr>
      <tr>
          <td colspan="3">TRIG</td>
          <td>3</td>
          <td>82</td>
      </tr>
      <tr>
          <td colspan="3">ECHO</td>
          <td>10</td>
          <td>88</td>
      </tr>
  </table>
</div>

#### Schritt 3. Ausführung
Führen Sie das folgende Python-Skript aus, um die Entfernung mit dem Ultraschallsensor zu messen:
```
import os
import time

TRIG_PIN = 82  
ECHO_PIN = 88  

def export_gpio(pin: int, direction: str):
    if os.path.exists(f"/sys/class/gpio/gpio{pin}"):
        with open("/sys/class/gpio/unexport", "w") as f:
            f.write(str(pin))
    with open("/sys/class/gpio/export", "w") as f:
        f.write(str(pin))
    with open(f"/sys/class/gpio/gpio{pin}/direction", "w") as f:
        f.write(direction)

def write_gpio_value(pin: int, value: int):
    with open(f"/sys/class/gpio/gpio{pin}/value", "w") as f:
        f.write(str(value))

def read_gpio_value(pin: int) -> str:
    with open(f"/sys/class/gpio/gpio{pin}/value", "r") as f:
        return f.read().strip()

def unexport_gpio(pin: int):
    with open("/sys/class/gpio/unexport", "w") as f:
        f.write(str(pin))

def get_distance_cm():
    write_gpio_value(TRIG_PIN, 0)
    time.sleep(0.00002)  
    write_gpio_value(TRIG_PIN, 1)
    time.sleep(0.00001)  
    write_gpio_value(TRIG_PIN, 0)

    start = time.time()
    while read_gpio_value(ECHO_PIN) == "0":
        start = time.time()
    end = start
    while read_gpio_value(ECHO_PIN) == "1":
        end = time.time()
    duration = end - start
    distance = (duration * 34300) / 2  # cm
    return round(distance, 2)

def main():
    export_gpio(TRIG_PIN, "out")
    export_gpio(ECHO_PIN, "in")
    print("GPIO pins initialized.")

    try:
        while True:
            distance = get_distance_cm()
            print(f"Distance: {distance} cm")
            time.sleep(1)

    except KeyboardInterrupt:
        print("Program interrupted by user.")

    finally:
        unexport_gpio(TRIG_PIN)
        unexport_gpio(ECHO_PIN)
        print("GPIO pins unexported.")
        print("Program terminated.")

if __name__ == "__main__":
    main()
```

#### Schritt 4. Ausführungsergebnis
Führen Sie den Code mit dem folgenden Befehl aus.
```
$ python3 ultrasonic_sensor_test.py
```
Dieses Skript konfiguriert GPIO82 als digitalen Ausgang zum Auslösen des Ultraschallimpulses und GPIO88 als digitalen Eingang zum Empfangen des Echos.
Wenn das Skript läuft, wird die Entfernung zum nächstgelegenen Objekt vor dem Sensor jede Sekunde ausgegeben, zum Beispiel:
```
Distance: 23.45 cm
Distance: 24.12 cm
...
```
Um das Skript zu beenden, drücken Sie **[Ctrl+C]**.
Wenn das Skript beendet wird, wird der Export von GPIO82 und GPIO88 automatisch aufgehoben und die Pins werden bereinigt.

**Hinweis**: GPIO82 und GPIO88 werden als Beispiele verwendet. Sie können jeden verfügbaren GPIO-Pin gemäß dem Layout des 40-Pin-Headers des D3-G verwenden. Siehe das offizielle Pinbelegungsdiagramm für eine korrekte Pin-Auswahl. Stellen Sie außerdem sicher, dass der Spannungspegel Ihres ECHO-Pins für das D3-G unbedenklich ist (einige Module geben 5V aus und benötigen möglicherweise einen Spannungsteiler oder Pegelwandler).

<br/><br/><br/><br/>

## 7.2 I2C
---
Das D3-G bietet I2C-Kommunikation über den 40-Pin-GPIO-Header und kann dadurch mit verschiedenen Peripheriegeräten wie Sensoren, Displays und Erweiterungsmodulen verbunden werden.
Inter-integrated Circuit (I2C) ist ein Zweidraht-Kommunikationsprotokoll, das aus einer Datenleitung (SDA) und einer Taktleitung (SCL) besteht und es mehreren Geräten ermöglicht, über einen gemeinsamen Bus zu kommunizieren.

Die I2C-Kommunikation folgt einer Master-Slave-Architektur, bei der ein Master-Gerät die Kommunikation steuert und bis zu 127 Slave-Geräte am selben Bus angeschlossen werden können.
Die SDA-Leitung wird sowohl zum Senden als auch zum Empfangen von Daten verwendet, während die SCL-Leitung das Timing der Datenübertragung synchronisiert. Dieses synchrone Kommunikationsmodell ermöglicht es Geräten, Informationen koordiniert und taktgesteuert auszutauschen.

<br/><br/><br/><br/>

### 7.2.1 1602A-LCD-Display
---
Das 1602A-LCD ist ein Zeichendisplay-Modul, das häufig in eingebetteten Systemen verwendet wird.
Auf dem D3-G können die SDA- und SCL-Leitungen des LCD mit GPIO-Pins verbunden werden, die für I2C konfiguriert sind. Nach dem Anschließen kann das LCD über die Linux-I2C-Tools oder eigene Software gesteuert werden.

#### Schritt 1. Hardware-Anforderungen
- D3-G-Board (x1)
- 1602A-I2C-LCD-Modul (x1)
- Buchse-auf-Buchse-Jumperkabel (x4)
- DC-5V-Netzteil (x1)
- USB-zu-TTL-Seriellkabel (x1)  

Stellen Sie sicher, dass das LCD-Modul über ein I2C-Backpack verfügt

#### Schritt 2. Beispielschaltung
- I2C-LCD-Modul
    - Der GND-Pin des I2C-LCD-Moduls ist mit dem GND-Pin des D3-G-Boards verbunden.
    - Der VCC-Pin des I2C-LCD-Moduls ist mit 5V des D3-G-Boards verbunden.
    - Der SDA-Pin des I2C-LCD-Moduls ist mit Pin 82 des D3-G-Boards verbunden.
    - Der SCL-Pin des I2C-LCD-Moduls ist mit Pin 81 des D3-G-Boards verbunden.

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20D3-G/Software/lcd_circuit.png"></p>
<p align="center"><strong>Abbildung 7.10 Schaltplan des D3-G-I2C-LCD-Moduls  </strong></p>

##### Schritt 2.1 Pinbelegung
Die folgende Tabelle zeigt die Pinbelegung.

<div align="center">
  <p><strong>Tabelle 7.10 Pinbelegung des D3-G-I2C-LCD-Moduls</strong></p>
  <table>
      <tr>
          <th colspan="3">Pin-Name</th>
          <th>D3-G</th>
          <th>GPIO</th>
      </tr>
      <tr>
          <td colspan="3">GND</td>
          <td>20</td>
          <td>GND</td>
      </tr>
      <tr>
          <td colspan="3">VCC</td>
          <td>2</td>
          <td>5V</td>
      </tr>
      <tr>
          <td colspan="3">SDA</td>
          <td>3</td>
          <td>82</td>
      </tr>
      <tr>
          <td colspan="3">SCL</td>
          <td>5</td>
          <td>81</td>
      </tr>
  </table>
</div>

#### Schritt 3. Ausführung
Installieren Sie zunächst die erforderlichen Python-Bibliotheken:
```
$ pip install RPLCD smbus2
```
Verwenden Sie anschließend den folgenden Python-Code, um Text auf das LCD zu schreiben:
```
import smbus2
import time
from RPLCD.i2c import CharLCD
 
# I2C bus num
I2C_BUS = 3
LCD_ADDRESS = 0x27

lcd = CharLCD(i2c_expander='PCF8574', address=LCD_ADDRESS, port=I2C_BUS,
              cols=16, rows=2, dotsize=8,
              charmap='A00', auto_linebreaks=True,
              backlight_enabled=True)
 
def display_text(text):
    lcd.clear()
    lcd.write_string(text)

def main():
    while True:
        user_input = input("Enter text to display on LCD: ")
        display_text(user_input)
        time.sleep(4)
        lcd.clear()
if __name__ == "__main__":
    main()
```

#### Schritt 4. Ausführungsergebnis
Führen Sie den Code mit dem folgenden Befehl aus.
```
$ python3 lcd_test.py
```
Dieses Skript initialisiert ein I2C-basiertes 1602A-LCD mit der RPLCD-Bibliothek und zeigt den vom Benutzer eingegebenen Text auf dem Bildschirm an.
Wenn Sie das Skript ausführen, werden Sie aufgefordert, eine Zeichenkette einzugeben. Dieser Text wird 4 Sekunden lang auf dem LCD angezeigt und anschließend gelöscht. Zum Beispiel:
```
Enter text to display on LCD: Hello D3-G!
```
Das LCD zeigt Folgendes an:
```
Hello D3-G!
```
und wird nach 4 Sekunden gelöscht.

Um das Skript zu beenden, drücken Sie **[Ctrl+C]**.

**Hinweis** : GPIO82 und GPIO81 werden auf dem D3-G standardmäßig für I2C verwendet.
Stellen Sie sicher, dass die I2C-Adresse (0x27) mit Ihrem spezifischen LCD-Modul übereinstimmt. Verwenden Sie bei Bedarf **i2cdetect -y 3**, um I2C-Geräte zu suchen.

<br/><br/><br/><br/>

## 7.3 SPI
---
Das D3-G unterstützt die Kommunikation über Serial Peripheral Interface (SPI) über einen 40-Pin-GPIO-Header und ermöglicht so den Datenaustausch zwischen externen Geräten und dem D3-G.

SPI ist ein synchrones serielles Kommunikationsprotokoll, das Vollduplex-Kommunikation ermöglicht - das heißt, Daten können gleichzeitig gesendet und empfangen werden. Es verwendet vier Hauptleitungen: Master Out Slave In (MOSI), Master In Slave Out (MISO), Serial Clock (SCLK) und Chip Select (CS).

Im Gegensatz zu I2C, das gemeinsame Leitungen für mehrere Geräte verwendet, benötigt SPI für jedes Slave-Gerät eine eigene CS-Leitung. Diese Eins-zu-viele-Struktur macht SPI schnell und einfach zu implementieren, kann jedoch mehr physische Verdrahtung erfordern, wenn mehrere Geräte beteiligt sind.

<br/><br/><br/><br/>

### 7.3.1 Dot-Matrix
---
Ein 8x8-Dot-Matrix-Display wird häufig für einfache Text- oder Musterausgaben in eingebetteten Systemen verwendet. Auf dem D3-G kann das Dot-Matrix-Modul über SPI mit einem Treiberchip wie dem MAX7219 gesteuert werden.

Der MAX7219 übernimmt die Zeilen- und Spaltenabtastung intern, sodass der Mikrocontroller das gesamte Display mit nur wenigen SPI-Signalen steuern kann: MOSI (DIN), SCLK und CS (LOAD). Nach dem Anschließen kann das Display über SPI-Kommunikation mittels benutzerdefinierter Skripte oder Bibliotheken gesteuert werden.

#### Schritt 1. Hardware-Anforderungen
- D3-G-Board (x1)
- Dot-Matrix (x1)
- Stecker-auf-Buchse-Jumperkabel (x4)
- DC-5V-Netzteil (x1)
- USB-zu-TTL-Seriellkabel (x1)

#### Schritt 2. Beispielschaltung
- Dot-Matrix
    - Der VCC-Pin der Dot-Matrix ist mit dem 5V-Pin des D3-G-Boards verbunden.
    - Der GND-Pin der Dot-Matrix ist mit dem GND-Pin des D3-G-Boards verbunden.
    - Der DIN-Pin der Dot-Matrix ist mit Pin 120 des D3-G-Boards verbunden.
    - Der CS-Pin der Dot-Matrix ist mit Pin 119 des D3-G-Boards verbunden.
    - Der CLK-Pin der Dot-Matrix ist mit Pin 118 des D3-G-Boards verbunden.

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20D3-G/Software/dot%20circuit.png"></p>
<p align="center"><strong>Abbildung 7.11 Schaltplan des D3-G-Dot-Matrix-Moduls  </strong></p>

##### Schritt 2.1 Pinbelegung
Die folgende Tabelle zeigt die Pinbelegung.
<div align="center">
  <p><strong>Tabelle 7.11 Pinbelegung der D3-G-Dot-Matrix</strong></p>
  <table>
      <tr>
          <th colspan="3">Pin-Name</th>
          <th>D3-G</th>
          <th>GPIO</th>
      </tr>
      <tr>
          <td colspan="3">VCC</td>
          <td>2</td>
          <td>5V</td>
      </tr>
      <tr>
          <td colspan="3">GND</td>
          <td>6</td>
          <td>GND</td>
      </tr>
      <tr>
          <td colspan="3">DIN</td>
          <td>19</td>
          <td>63</td>
      </tr>
      <tr>
          <td colspan="3">CS</td>
          <td>24</td>
          <td>62</td>
      </tr>
      <tr>
          <td colspan="3">CLK</td>
          <td>23</td>
          <td>61</td>
      </tr>
  </table>
</div>

#### Schritt 3. Ausführung
Das folgende Python-Skript zeigt, wie Sie den MAX7219 direkt über /dev/spidev3.0 mit Low-Level-fcntl-Aufrufen steuern. Diese Methode eignet sich für Geräte ohne externe SPI-Bibliotheken:
```
#!/usr/bin/env python3
 
import os
import fcntl
import time
from ctypes import Structure, addressof, create_string_buffer, c_uint64, c_uint32, c_uint16, c_uint8
 
SPI_MODE = 0
SPI_SPEED_HZ = 5000000
SPI_BITS_PER_WORD = 8
 
SPI_IOC_RD_MODE = 0x80016b01
SPI_IOC_WR_MODE = 0x40016b01
SPI_IOC_RD_BITS_PER_WORD = 0x80016b03
SPI_IOC_WR_BITS_PER_WORD = 0x40016b03
SPI_IOC_WR_MAX_SPEED_HZ = 0x40046b04
SPI_IOC_MESSAGE_1 = 0x40206b00
 
class spi_ioc_transfer(Structure):
    _fields_ = [
        ("tx_buf", c_uint64),
        ("rx_buf", c_uint64),
        ("len", c_uint32),
        ("speed_hz", c_uint32),
        ("delay_usecs", c_uint16),
        ("bits_per_word", c_uint8),
        ("cs_change", c_uint8),
        ("pad", c_uint32)
    ]
 
def spi_transfer(fd, tx_data):
    tx_buffer = create_string_buffer(bytes(tx_data))
    rx_buffer = create_string_buffer(len(tx_data))
 
    xfer = spi_ioc_transfer(
        tx_buf=addressof(tx_buffer),
        rx_buf=addressof(rx_buffer),
        len=len(tx_data),
        delay_usecs=0,
        speed_hz=SPI_SPEED_HZ,
        bits_per_word=SPI_BITS_PER_WORD,
        cs_change=0
    )
 
    fcntl.ioctl(fd, SPI_IOC_MESSAGE_1, xfer)
 
    return list(rx_buffer)
 
def MAX7219_write(fd, address, data):
    spi_transfer(fd, [address, data])
 
def MAX7219_init(fd):
    MAX7219_write(fd, 0x09, 0x00)  # Decoding mode: none
    MAX7219_write(fd, 0x0A, 0x03)  # Intensity: 3 (range 0-15)
    MAX7219_write(fd, 0x0B, 0x07)  # Scan limit: 8 LEDs
    MAX7219_write(fd, 0x0C, 0x01)  # Power on
    MAX7219_write(fd, 0x0F, 0x00)  # Display test: off
 
NUMBER_CODE = [
    [0x3C, 0x42, 0x42, 0x42, 0x42, 0x42, 0x42, 0x3C],  # 0
    [0x10, 0x30, 0x50, 0x10, 0x10, 0x10, 0x10, 0x7C],  # 1
    [0x3E, 0x02, 0x02, 0x3E, 0x20, 0x20, 0x3E, 0x00],  # 2
    [0x00, 0x7C, 0x04, 0x04, 0x7C, 0x04, 0x04, 0x7C],  # 3
    [0x08, 0x18, 0x28, 0x48, 0xFE, 0x08, 0x08, 0x08],  # 4
    [0x3C, 0x20, 0x20, 0x3C, 0x04, 0x04, 0x3C, 0x00],  # 5
    [0x3C, 0x20, 0x20, 0x3C, 0x24, 0x24, 0x3C, 0x00],  # 6
    [0x3E, 0x22, 0x04, 0x08, 0x08, 0x08, 0x08, 0x08],  # 7
    [0x00, 0x3E, 0x22, 0x22, 0x3E, 0x22, 0x22, 0x3E],  # 8
    [0x3E, 0x22, 0x22, 0x3E, 0x02, 0x02, 0x02, 0x3E]   # 9
]
 
ALPHABET_CODE = {
    'A': [0x08, 0x14, 0x22, 0x3E, 0x22, 0x22, 0x22, 0x22],
    'B': [0x3C, 0x22, 0x22, 0x3E, 0x22, 0x22, 0x3C, 0x00],
    'C': [0x3C, 0x40, 0x40, 0x40, 0x40, 0x40, 0x3C, 0x00],
    'D': [0x7C, 0x42, 0x42, 0x42, 0x42, 0x42, 0x7C, 0x00],
    'E': [0x7C, 0x40, 0x40, 0x7C, 0x40, 0x40, 0x40, 0x7C],
    'F': [0x7C, 0x40, 0x40, 0x7C, 0x40, 0x40, 0x40, 0x40],
    'G': [0x3C, 0x40, 0x40, 0x40, 0x40, 0x44, 0x44, 0x3C],
    'H': [0x44, 0x44, 0x44, 0x7C, 0x44, 0x44, 0x44, 0x44],
    'I': [0x7C, 0x10, 0x10, 0x10, 0x10, 0x10, 0x10, 0x7C],
    'J': [0x3C, 0x08, 0x08, 0x08, 0x08, 0x08, 0x48, 0x30],
    'K': [0x40, 0x40, 0x40, 0x40, 0x40, 0x40, 0x40, 0x7C],
    'L': [0x40, 0x40, 0x40, 0x40, 0x40, 0x40, 0x40, 0x7C],
    'M': [0x00, 0x42, 0x62, 0x52, 0x4A, 0x46, 0x42, 0x00],
    'N': [0x00, 0x42, 0x62, 0x52, 0x4A, 0x46, 0x42, 0x00],
    'O': [0x3C, 0x42, 0x42, 0x42, 0x42, 0x42, 0x42, 0x3C],
    'P': [0x3C, 0x42, 0x42, 0x3E, 0x02, 0x02, 0x02, 0x3E],
    'Q': [0x3C, 0x42, 0x42, 0x42, 0x42, 0x42, 0x42, 0x3C],
    'R': [0x08, 0x14, 0x22, 0x3E, 0x22, 0x22, 0x22, 0x22],
    'S': [0x7C, 0x40, 0x40, 0x7C, 0x40, 0x40, 0x40, 0x7C],
    'T': [0x7C, 0x10, 0x10, 0x10, 0x10, 0x10, 0x10, 0x7C],
    'U': [0x3C, 0x08, 0x08, 0x08, 0x08, 0x08, 0x48, 0x30],
    'V': [0x40, 0x40, 0x40, 0x40, 0x40, 0x40, 0x40, 0x7C],
    'W': [0x00, 0x41, 0x41, 0x41, 0x49, 0x2a, 0x2a, 0x14],
    'X': [0x40, 0x40, 0x40, 0x40, 0x40, 0x40, 0x40, 0x7C],
    'Y': [0x7C, 0x40, 0x40, 0x7C, 0x40, 0x40, 0x40, 0x7C],
    'Z': [0x7C, 0x40, 0x40, 0x7C, 0x40, 0x40, 0x40, 0x7C],
    'Smile': [0x3c, 0x42, 0xa5, 0x81, 0xa5, 0x99, 0x42, 0x3c],
    'dance0': [0x10, 0x28, 0x10, 0x10, 0xfe, 0x10, 0x28, 0x28],
    'dance1': [0x10, 0x28, 0x92, 0x54, 0x38, 0x10, 0x28, 0x44],
    'angry': [0x00, 0x00, 0xe7, 0x00, 0x00, 0x00, 0x3c, 0x00],
    'Good': [0x30, 0x30, 0x30, 0x3c, 0x32, 0x3c, 0x32, 0x3c]
}
 
 
def main():
    print('*' * 50)
    fd = os.open('/dev/spidev3.0', os.O_RDWR)
 
    fcntl.ioctl(fd, SPI_IOC_RD_BITS_PER_WORD, bytes([SPI_BITS_PER_WORD]))
    fcntl.ioctl(fd, SPI_IOC_WR_BITS_PER_WORD, bytes([SPI_BITS_PER_WORD]))
    fcntl.ioctl(fd, SPI_IOC_WR_MODE, bytes([SPI_MODE]))
    fcntl.ioctl(fd, SPI_IOC_WR_MAX_SPEED_HZ, SPI_SPEED_HZ.to_bytes(4, byteorder='little'))
 
    MAX7219_init(fd)
 
    try:
        while True:
            input_str = input("Enter a number, an uppercase letter (0-9, A-Z), 'Smile', 'Dance', 'Angry', 'Good', 'Nice', 'Emotion': ")
            if input_str.isdigit() and 0 <= int(input_str) <= 9:
                num = int(input_str)
                for col in range(8):
                    MAX7219_write(fd, col + 1, NUMBER_CODE[num][col])
                    time.sleep(0.1)
            elif input_str.isalpha() and input_str.isupper() and len(input_str) == 1:
                char = input_str
                for col in range(8):
                    MAX7219_write(fd, col + 1, ALPHABET_CODE[char][col])
                    time.sleep(0.1)
            elif input_str == 'Smile':
                smile_pattern = ALPHABET_CODE['Smile']
                for col in range(8):
                    MAX7219_write(fd, col + 1, smile_pattern[col])
                    time.sleep(0.1)
            elif input_str == 'Dance': 
                for _ in range(10):
                    for col in range(8):
                        MAX7219_write(fd, col + 1, ALPHABET_CODE['dance0'][col])
                    time.sleep(0.5)
                    for col in range(8):
                        MAX7219_write(fd, col + 1, ALPHABET_CODE['dance1'][col])
                    time.sleep(0.5)
            elif input_str == 'Angry': 
                angry_pattern = ALPHABET_CODE['angry']
                for col in range(8):
                    MAX7219_write(fd, col + 1, angry_pattern[col])
                    time.sleep(0.1)
            elif input_str == 'Good':
                good_pattern = ALPHABET_CODE['Good']
                for col in range(8):
                    MAX7219_write(fd, col + 1, good_pattern[col])
                    time.sleep(0.1)
            elif input_str == 'Nice':
                for _ in range(3):
                    for col in range(8):
                        MAX7219_write(fd, col + 1, ALPHABET_CODE['N'][col])
                    time.sleep(0.5)
                    for col in range(8):
                        MAX7219_write(fd, col + 1, ALPHABET_CODE['I'][col])
                    time.sleep(0.5)
                    for col in range(8):
                        MAX7219_write(fd, col + 1, ALPHABET_CODE['C'][col])
                    time.sleep(0.5)
                    for col in range(8):
                        MAX7219_write(fd, col + 1, ALPHABET_CODE['E'][col])
                    time.sleep(0.5)
            elif input_str == 'Emotion':
                for _ in range (6):
                    for col in range(8):
                        MAX7219_write(fd, col + 1, ALPHABET_CODE['Smile'][col])
                    time.sleep(0.5)
                    for col in range(8):
                        MAX7219_write(fd, col + 1, ALPHABET_CODE['angry'][col])
                    time.sleep(0.5)
            else:
                   print("Invalid input. Please enter a number (0-9), an uppercase letter (A-Z), 'Smile', 'Dance', 'Angry', 'Good', 'Nice', 'Emotion'.")
 
    except KeyboardInterrupt:
        os.close(fd)
    finally:
        os.close(fd)
 
if __name__ == "__main__":
    main()
```

#### Schritt 4. Ausführungsergebnis
Führen Sie den Code mit dem folgenden Befehl aus.
```
$ python3 dot_matrix_test.py
```
Dieses Skript initialisiert das über SPI angeschlossene MAX7219-Dot-Matrix-Display und fordert Sie zur Eingabe eines Wertes auf. Je nach Eingabe wird ein bestimmtes Muster auf der 8x8-LED-Matrix angezeigt.

Wenn das Skript läuft, sehen Sie Folgendes:
```
Enter a number, an uppercase letter (0-9, A-Z), 'Smile', 'Dance', 'Angry', 'Good', 'Nice', 'Emotion':
```
Beispiele:
- Die Eingabe von A zeigt den Buchstaben A an.
- Die Eingabe von Smile zeigt ein Smiley-Muster an.
- Die Eingabe von Dance löst abwechselnde Tanzanimationen aus.
- Die Eingabe von Nice animiert die Buchstaben N-I-C-E nacheinander.

Um das Skript zu beenden, drücken Sie **[Ctrl+C]**.
Bei Beendigung wird das SPI-Gerät sicher geschlossen und die LED-Matrix wird nicht mehr aktualisiert.

**Hinweis**: Stellen Sie sicher, dass /dev/spidev3.0 vorhanden ist und die Verdrahtung mit der Pinbelegungstabelle übereinstimmt. Versorgen Sie das MAX7219-Modul außerdem mit einer stabilen 5V-Quelle.

<br/><br/><br/><br/>

## 7.4 PWM
---
Pulsweitenmodulation (PWM) wird verwendet, um Geräte wie LEDs, Motoren und Summer durch Variation der Breite des Impulssignals zu steuern. Das D3-G unterstützt PWM über die sysfs-Schnittstelle in Linux.

### 7.4.1 LED-Helligkeitssteuerung
---
Dieses Beispiel zeigt die Steuerung der Helligkeit einer LED mittels PWM auf dem D3-G.

#### Schritt 1. Hardware-Anforderungen
- D3-G-Board (x1)
- LED (x1)
- Jumperkabel Stecker auf Buchse (x2)
- Breadboard
- DC-5V-Netzteil (x1)
- USB-zu-TTL-Seriellkabel (x1)

#### Schritt 2. Beispielschaltung
- LED
    - Der (+)-Pin der LED ist mit Pin 89 auf dem D3-G-Board verbunden.
    - Der (-)-Pin der LED ist mit dem GND-Pin auf dem D3-G-Board verbunden.

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20D3-G/Software/led.png"></p>
<p align="center"><strong>Abbildung 7.12 D3-G LED-Schaltplan  </strong></p>

##### Schritt 2.1 Pinbelegung
Die folgende Tabelle zeigt die Pinbelegung.

<div align="center">
  <p><strong>Tabelle 7.12 Pinbelegung der D3-G LED</strong></p>
  <table>
      <tr>
          <th colspan="3">Pin-Name</th>
          <th>D3-G</th>
          <th>GPIO</th>
      </tr>
      <tr>
          <td colspan="3">( + )</td>
          <td>12</td>
          <td>89</td>
      </tr>
      <tr>
          <td colspan="3">( – )</td>
          <td>14</td>
          <td>GND</td>
      </tr>
  </table>
</div>

#### Schritt 3. Ausführung
Um die LED (PWM), die mit GPIO89 auf dem D3-G-Board verbunden ist, zu betreiben, führen Sie den folgenden Code aus:
```
import time

PWM_CHIP = "pwmchip0"
PWM_CHANNEL = "pwm0"
PWM_PATH = f"/sys/class/pwm/{PWM_CHIP}/{PWM_CHANNEL}"
EXPORT_PATH = f"/sys/class/pwm/{PWM_CHIP}/export"
UNEXPORT_PATH = f"/sys/class/pwm/{PWM_CHIP}/unexport"

PERIOD = 1000000  # 1ms = 1kHz
STEP = 10000
SLEEP = 0.01

def pwm_setup():
    try:
        with open(EXPORT_PATH, "w") as f:
            f.write("0")
    except Exception:
        pass  # Already exported
    time.sleep(0.1)

    with open(f"{PWM_PATH}/period", "w") as f:
        f.write(str(PERIOD))
        f.flush()

    with open(f"{PWM_PATH}/enable", "w") as f:
        f.write("1")
        f.flush()

def pwm_cleanup():
    try:
        with open(f"{PWM_PATH}/enable", "w") as f:
            f.write("0")
            f.flush()
        with open(UNEXPORT_PATH, "w") as f:
            f.write("0")
    except Exception as e:
        print("PWM cleanup failed:", e)

try:
    pwm_setup()
    print("Starting LED PWM control (press Ctrl+C to stop)")

    while True:
        for duty in range(0, PERIOD, STEP):
            with open(f"{PWM_PATH}/duty_cycle", "w") as f:
                f.write(str(min(duty, PERIOD - 1)))
                f.flush()
            time.sleep(SLEEP)

        for duty in range(PERIOD, 0, -STEP):
            with open(f"{PWM_PATH}/duty_cycle", "w") as f:
                f.write(str(min(duty, PERIOD - 1)))
                f.flush()
            time.sleep(SLEEP)

except KeyboardInterrupt:
    print("\nStopped by user.")

finally:
    pwm_cleanup()
    print("PWM disabled and cleaned up.")
```

#### Schritt 4. Ausführungsergebnis
Führen Sie den Code mit dem folgenden Befehl aus.
```
$ python3 led_pwm.py
```
Dieses Skript initialisiert PWM am LED-Pin und lässt die Helligkeit der LED kontinuierlich auf- und abblenden.

Sobald das Skript ausgeführt wurde, sehen Sie eine Ausgabe wie:
```
Starting LED PWM control (press Ctrl+C to stop)
```
Die LED wird wiederholt allmählich heller und dann dunkler und simuliert so einen „Atem“-Effekt.

Um das Skript zu beenden, drücken Sie **[Ctrl+C]**.

**Hinweis**: Stellen Sie sicher, dass der PWM-Kanal nicht bereits in Verwendung ist und dass das D3-G Hardware-PWM auf dem ausgewählten GPIO unterstützt. Wenn PWM nicht aktiviert wird, überprüfen Sie die Einstellungen export, period und duty_cycle in /sys/class/pwm/.

<br/><br/><br/><br/>

### 7.4.2 Mini-Servomotor
---
Ein Mini-Servomotor kann verwendet werden, um präzise Winkelbewegungen auf Basis eines Pulsweitenmodulations-Signals (PWM) über GPIO zu steuern.
In diesem Abschnitt wird gezeigt, wie Sie einen Mini-Servomotor mit dem D3-G anschließen und steuern.

#### Schritt 1. Hardware-Anforderungen
- D3-G-Board (x1)
- Servomotor (x1)
- Stecker-auf-Buchse-Jumperkabel (x3)
- DC-5V-Netzteil (x1)
- USB-zu-TTL-Seriellkabel (x1)

#### Schritt 2. Beispielschaltung
- Servomotor
    - Der VCC-Pin des Servomotors ist mit 5V auf dem D3-G-Board verbunden.
    - Der GND-Pin des Servomotors ist mit GND auf dem D3-G-Board verbunden.
    - Der SIG-Pin des Servomotors ist mit Pin 89 auf dem D3-G-Board verbunden.

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20D3-G/Software/motor_circuit.png"p>
<p align="center"><strong>Abbildung 7.13 D3-G Servomotor-Schaltplan  </strong></p>

##### Schritt 2.1 Pinbelegung
Die folgende Tabelle zeigt die Pinbelegung.

<div align="center">
  <p><strong>Tabelle 7.13 Pinbelegung des D3-G Servomotors</strong></p>
  <table>
      <tr>
          <th colspan="3">Pin-Name</th>
          <th>D3-G</th>
          <th>GPIO</th>
      </tr>
      <tr>
          <td colspan="3">VCC</td>
          <td>2</td>
          <td>5V</td>
      </tr>
      <tr>
          <td colspan="3">GND</td>
          <td>20</td>
          <td>GND</td>
      </tr>
      <tr>
          <td colspan="3">SIG</td>
          <td>12</td>
          <td>89</td>
      </tr>
  </table>
</div>

#### Schritt 3. Ausführung
Das folgende Python-Skript zeigt, wie Sie einen Mini-Servomotor direkt mittels PWM über die sysfs-Schnittstelle auf dem D3-G steuern. Diese Methode erfordert keine externen Bibliotheken und ermöglicht eine feingranulare Steuerung der winkelbasierten Positionierung.
```
import time
import os

PWM_CHIP = "pwmchip0"
PWM_CHANNEL = "pwm0"
PWM_PATH = f"/sys/class/pwm/{PWM_CHIP}/{PWM_CHANNEL}"
EXPORT_PATH = f"/sys/class/pwm/{PWM_CHIP}/export"
UNEXPORT_PATH = f"/sys/class/pwm/{PWM_CHIP}/unexport"

PERIOD = 20_000_000  # 20ms (50Hz)

def angle_to_duty(angle):
    pulse_width = 1_000_000 + (angle / 180) * 1_000_000
    return int(pulse_width)

def pwm_setup():
    if not os.path.exists(PWM_PATH):
        with open(EXPORT_PATH, "w") as f:
            f.write("0")
        time.sleep(0.1)
    with open(f"{PWM_PATH}/period", "w") as f:
        f.write(str(PERIOD))
    with open(f"{PWM_PATH}/enable", "w") as f:
        f.write("1")

def pwm_set_angle(angle):
    duty = angle_to_duty(angle)
    with open(f"{PWM_PATH}/duty_cycle", "w") as f:
        f.write(str(duty))

def pwm_cleanup():
    try:
        with open(f"{PWM_PATH}/enable", "w") as f:
            f.write("0")
        with open(UNEXPORT_PATH, "w") as f:
            f.write("0")
    except Exception as e:
        print("PWM cleanup failed:", e)

if __name__ == "__main__":
    pwm_setup()

    try:
        while True:
            user_input = input("Enter 1 (CW) or 0 (CCW), q to quit: ").strip()
            if user_input == 'q':
                break
            elif user_input == '1':
                pwm_set_angle(180)  
                time.sleep(0.5)
            elif user_input == '0':
                pwm_set_angle(0)   
                time.sleep(0.5)
            else:
                print("Invalid input. Use 0, 1, or q.")
    except KeyboardInterrupt:
        print("\nInterrupted by user.")
    finally:
        pwm_cleanup()
        print("PWM cleaned up.")
```

#### Schritt 4. Ausführungsergebnis
Führen Sie den Code mit dem folgenden Befehl aus.
```
$ python3 motor_test.py
```
Dieses Skript verwendet PWM, um einen Mini-Servomotor zu steuern, indem der Tastgrad auf Basis des Zielwinkels angepasst wird.
Nach der Ausführung werden Sie zur Eingabe aufgefordert:
```
Enter 1 (CW) or 0 (CCW), q to quit:
```
Die Eingabe von 1 dreht den Servo im Uhrzeigersinn auf 180°, und die Eingabe von 0 dreht den Servo gegen den Uhrzeigersinn auf 0°. Sie können dies beliebig oft wiederholen.

Um das Skript zu beenden, geben Sie **[q]** ein oder drücken Sie **[Ctrl+C]**. Das Skript deaktiviert daraufhin den PWM-Kanal und hebt dessen Export auf.

**Hinweis**: Stellen Sie sicher, dass Ihr Servomotor ein 50 Hz PWM-Signal unterstützt und für einen sicheren Betrieb im Impulsbereich von 1 ms bis 2 ms arbeitet.
