## Unterstützte Kameramodule
<div align="center">
    <table>
        <tr>
            <td colspan="8" align="center"><strong>Board</strong></td>
            <td align="center"><strong>Modell</strong></td>
            <td align="center"><strong>Sensor</strong></td>
            <td align="center"><strong>Sensorauflösung</strong></td>
            <td align="center"><strong>Standardauflösung</strong></td>
            <td align="center"><strong>Bildrate</strong></td>
            <td align="center"><strong>Standard-Videopfad</strong></td>
            <td align="center"><strong>Anmerkung</strong></td>
        </tr>
        <tr>
            <td rowspan="4" align="center"><strong>D3-G</strong></td>
            <td colspan="8">Arducam OV5647</td>
            <td>OV5647</td>
            <td>2592x1944 Pixel(5MP)</td>
            <td>1296x972</td>
            <td>30FPS</td>
            <td>/dev/video0</td>
            <td>Standardmäßig ausgewählte Kamera</td>
        </tr>
        <tr>
            <td colspan="8">Raspberry Pi Camera v1</td>
            <td>OV5647</td>
            <td>2592x1944 Pixel(5MP)</td>
            <td>1296x972</td>
            <td>30FPS</td>
            <td>/dev/video0</td>
            <td>Standardmäßig ausgewählte Kamera</td>
        </tr>
        <tr>
            <td colspan="8">Raspberry Pi Camera v2</td>
            <td>IMX219</td>
            <td>3280x2464 Pixel(8MP)</td>
            <td>1640x1232</td>
            <td>30FPS</td>
            <td>/dev/video0</td>
            <td>Standardmäßig deaktiviert. Zur Aktivierung siehe die nachfolgende Anleitung.</td>
        </tr>
        <tr>
            <td colspan="8">SEKONIX CXD5700</td>
            <td>CXD5700</td>
            <td>1920x1080 Pixel(2MP)</td>
            <td>1920x1080</td>
            <td>30FPS</td>
            <td>/dev/video0,1,2,3</td>
            <td>Standardmäßig deaktiviert. Zur Aktivierung siehe die nachfolgende Anleitung.</td>
        </tr>
        <tr>
            <td rowspan="4" align="center"><strong>AI-G</strong></td>
            <td colspan="8">Arducam OV5647</td>
            <td>OV5647</td>
            <td>2592x1944 Pixel(5MP)</td>
            <td>1296x972</td>
            <td>30FPS</td>
            <td>/dev/video2</td>
            <td>Standardmäßig ausgewählte Kamera</td>
        </tr>
        <tr>
            <td colspan="8">Raspberry Pi Camera v1</td>
            <td>OV5647</td>
            <td>2592x1944 Pixel(5MP)</td>
            <td>1296x972</td>
            <td>30FPS</td>
            <td>/dev/video2</td>
            <td>Standardmäßig ausgewählte Kamera</td>
        </tr>
        <tr>
            <td colspan="8">Raspberry Pi Camera v2</td>
            <td>IMX219</td>
            <td>3280x2464 Pixel(8MP)</td>
            <td>1640x1232</td>
            <td>30FPS</td>
            <td>/dev/video2</td>
            <td>Standardmäßig deaktiviert. Zur Aktivierung siehe die nachfolgende Anleitung.</td>
        </tr>
        <tr>
            <td colspan="8">SEKONIX CXD5700</td>
            <td>CXD5700</td>
            <td>1920x1080 Pixel(2MP)</td>
            <td>1920x1080</td>
            <td>30FPS</td>
            <td>/dev/video0,1,2</td>
            <td>Standardmäßig deaktiviert. Zur Aktivierung siehe die nachfolgende Anleitung.</td>
        </tr>
    </table>
</div>

# 1. Einführung
Diese Anleitung soll Ingenieure dabei unterstützen, Kameraeingänge auf den Plattformen TOPST D3-G und AI-G schnell in Betrieb zu nehmen und eine rasche vorläufige Validierung für KI-Vision-Workloads durchzuführen. Sie zielt darauf ab, die Komplexität der Ersteinrichtung einschließlich Hardware-Verbindungen, Device-Tree-Konfiguration, Treibern und Pipeline-Vorbereitung zu verringern und einen klaren, reproduzierbaren Weg vom Einschalten bis zum ersten Videobild und schließlich bis zur ersten Inferenz aufzuzeigen.

## 1.1 Geltungsbereich
- **Unterstützte Schnittstellen:** MIPI CSI-2, GMSL (SerDes-basiert), USB UVC
- **Software-Komponenten:** Yocto-basierte BSP-Konfiguration, Device-Tree-Overlays, V4L2, GStreamer, OpenCV sowie die Integration mit den D3-G- und AI-G-SDKs
- **Anwendbare Anwendungsfälle:** Robotik, Drohnen und industrielle Automatisierungsanwendungen wie Inspektion, Sicherheitsüberwachung und Objektverfolgung
- **Nicht behandelte Themen:** ISP-Abstimmung der Kamera, fortgeschrittene Kalibrierungsabläufe (Stereo/IMU) und vollständige End-to-End-Anwendungs-Frameworks

## 1.2 Zielgruppe
- Embedded- und KI-Ingenieure, die Kameras für PoC- oder Pilotentwicklungen in die D3-G- oder AI-G-Plattformen integrieren
- Systemintegratoren, die Systeme bereitstellen oder validieren, die auf Multi-Kamera-Pipelines basieren
- Lehrende und Laborbenutzer, die eine reproduzierbare, praxisnahe Umgebung für Schulung und Experimente benötigen

## 1.3 Aufbau dieser Anleitung
- **Hardware-Verbindungen:** Anschlussbelegungen, Lane-Konfiguration, Anforderungen an Stromversorgung und Masse, Hinweise zum Umgang mit Kabeln sowie Referenz-Schaltpläne
- **Software-Konfiguration:** BSP-Einrichtung einschließlich Treibern und Device-Tree-Konfiguration sowie Methoden zur Überprüfung von Geräten über udev und V4L2
- **Pipelines und Beispiele:** GStreamer- und OpenCV-Befehle und -Skripte für Vorschau und Aufnahme mit einer oder mehreren Kameras
- **Fehlerbehebung:** Häufige Probleme, typische dmesg-Muster, Tipps zum I²C-Probing, timing-bedingte Probleme und Methoden zur Leistungsüberprüfung

## 1.4 Voraussetzungen
- **Hardware:** TOPST D3-G- oder AI-G-Board, unterstützte Kameramodule sowie die erforderlichen Kabel/Adapter (MIPI-FPC, Koaxialkabel für GMSL, USB 3.0 usw.)
- **Host-Werkzeuge:** Zugriff auf die serielle Konsole, SSH-Client und grundlegende Build-/Debug-Hilfsprogramme
- **Technische Vorkenntnisse:** Vertrautheit mit der Bedienung der Linux-Shell, den V4L2-Werkzeugen und grundlegenden Device-Tree-Konzepten
- **Images/SDK:** D3-G-, AI-G-BSP-Image(d3-g Version ≥ v1.3.0, ai-g Version ≥1.1.0)
  

# 2. Übersicht über die Kameraschnittstellen
In Kapitel 2 werden die Kameratypen beschrieben, die auf den D3-G- bzw. AI-G-Boards unterstützt werden.  
Tabelle 2.1 zeigt die Board-Support-Matrix für die Plattformen D3-G und AI-G.

<p align="center"><strong>Tabelle 2.1 Board-Support-Matrix</strong></p>
<div align="center">
    <table>
        <tr>
            <td colspan="3" align="center"><strong>Element</strong></td>
            <td align="center"><strong>D3-G</strong></td>
            <td align="center"><strong>AI-G</strong></td>
        </tr>
        <tr>
            <td colspan="3">OS-Unterstützung</td>
            <td>Yocto, Ubuntu(desktop)</td>
            <td>Yocto, Ubuntu(Headless)</td>
        </tr>
        <tr>
            <td colspan="3">MIPI CSI-2</td>
            <td>2-4 Lanes, 2.1 Gbps/Lane x2</td>
            <td>2-4 Lanes, 1.5 Gbps/Lane x1</td>
        </tr>
        <tr>
            <td colspan="3">GMSL (SerDes)</td>
            <td>TOPST 4ch SerDes Carrier</td>
            <td>TOPST 4ch SerDes Carrier</td>
        </tr>
        <tr>
            <td colspan="3">USB (UVC)</td>
            <td>USB2.0/USB3.0 </td>
            <td>Nicht unterstützt</td>
        </tr>
    </table>
</div>

## 2.1 Übersicht über MIPI-Kameras
Eine MIPI-Kamera ist ein bildsensorbasiertes Kameramodul, das über den Standard **MIPI CSI-2 (Mobile Industry Processor Interface – Camera Serial Interface 2)** direkt mit dem Prozessor verbunden wird. Sie ist die am weitesten verbreitete Kameraschnittstelle in Smartphones, Embedded-Boards und KI-basierten Kamerasystemen und bietet Vorteile wie geringen Stromverbrauch, hohe Bandbreite und niedrige Latenz.  
MIPI-CSI-2-Kameras liefern die RAW-Bayer-Sensorausgabe in der Regel direkt an das System, wobei die Bildsignalverarbeitung (ISP) entweder vom internen ISP im SoC oder von einem externen ISP übernommen wird. Anders als USB-Kameras erfordern MIPI-Sensoren eine Initialisierung über die I2C-Registerkonfiguration sowie die Einrichtung der ISP-Pipeline, ermöglichen dafür aber eine hochwertige Bildverarbeitung, die die Leistung des Sensors voll ausschöpft.  
MIPI-Kameras werden aus den folgenden Gründen häufig in Embedded-Plattformen eingesetzt:
- **Hohe Bandbreite:** Mit 2-Lane- oder 4-Lane-Konfigurationen können MIPI-Kameras hochauflösende Daten (4K und höher) mit hoher Bildrate zuverlässig übertragen.
- **Geringer Stromverbrauch:** Da sie für mobile und eingebettete Geräte ausgelegt sind, ist der Stromverbrauch deutlich geringer als bei Alternativen.
- **Direkte Sensorsteuerung:** Sensorparameter wie Belichtung, Verstärkung und Bildrate lassen sich über I2C steuern, was eine feine Abstimmung der Bildqualität ermöglicht.
- **niedrige Latenz:** Da RAW-Daten direkt geliefert werden, eignen sich MIPI-Kameras für Echtzeitanwendungen wie Robotik und Embedded-Vision-Systeme.
- **Große Sensorauswahl:** Zahlreiche Sensoren—darunter die Sony IMX-Serie (IMX219, IMX708 usw.) und die Omnivision OV-Serie—können unter demselben CSI-2-Standard verwendet werden.  

MIPI-Kameras verwenden Anschlüsse wie **15-pin (2-lane)** oder **20-pin (4-lane)** FFC-Kabel, wobei die korrekte Lane-Konfiguration und die Pinbelegung zum CSI-Anschluss des Boards passen müssen.  
Auf Linux-basierten Systemen muss der Sensortreiber (einschließlich der Device-Tree-Konfiguration) korrekt eingerichtet sein, damit die Kamera als /dev/video*-Gerät oder als Media-Controller-Knoten erkannt wird. Nach der Erkennung kann über das V4L2-Framework auf das Video-Streaming zugegriffen werden.  
Aufgrund dieser Eigenschaften haben sich MIPI-Kameras als De-facto-Standardschnittstelle für hochwertige Bildverarbeitung, Streaming mit niedriger Latenz und KI-gestützte Embedded-Vision-Anwendungen etabliert.

## 2.2 Übersicht über GMSL-Kameras
Eine GMSL-Kamera ist ein serialisiertes Kameramodul, das Bilddaten, Steuersignale und Stromversorgung über ein einziges Koaxial- oder geschirmtes Twisted-Pair-Kabel überträgt und dabei den Standard Gigabit Multimedia Serial Link (GMSL) verwendet. Anders als MIPI-Kameras, die kurze FFC-Verbindungen erfordern, nutzt GMSL ein Serializer–Deserializer-Paar (SerDes), um CSI-2-Bilddaten über mehrere Meter zu übertragen, was eine störungsresistente Kameraintegration über große Entfernungen ermöglicht.  

GMSL-Systeme bieten in Embedded- und Automotive-Umgebungen mehrere Vorteile:
- **Übertragung über große Entfernungen:** Unterstützt eine zuverlässige Videoübertragung über Kabel mit einer Länge von bis zu ~15 m und eignet sich für Robotik und die Sensorplatzierung im Fahrzeug.
- **Hohe Bandbreite:** GMSL1/2/3 können CSI-2-Streams im Multi-Gigabit-Bereich übertragen und ermöglichen so hochauflösende oder Mehrkamera-Konfigurationen.
- **Power over Coax (PoC):** Ermöglicht Stromversorgung und Datenübertragung über ein einziges Kabel, verringert die Anzahl der Anschlüsse und vereinfacht die Systemverkabelung.
- **Robustheit und EMI-Störfestigkeit:** Koaxialkabel und differenzielle Signalübertragung machen GMSL in elektrisch stark gestörten Umgebungen stabil.
- **Standardmäßige Sensorsteuerung:** Der Deserializer leitet die I2C-Kommunikation an den Sensor weiter und ermöglicht so die übliche Konfiguration von Belichtung, Verstärkung und Bildrate.

Ein typischer GMSL-Kamerapfad umfasst den Bildsensor mit einem Serializer, ein Koaxialkabel, einen Deserializer und schließlich einen CSI-2-Ausgang zum SoC. Sobald SerDes und Sensor unter Linux korrekt im Device Tree beschrieben sind, erscheint die Kamera als V4L2- oder Media-Controller-Gerät—ganz ähnlich wie eine standardmäßige MIPI-Kamera, jedoch mit weitaus größerer Flexibilität bei Platzierung und Systemdesign

## 2.3 Übersicht über USB-Kameras
Eine USB-Kamera ist ein digitales Bildaufnahmegerät, das über eine USB 2.0- oder USB 3.0-Schnittstelle mit einem System verbunden wird. Ihr wesentlicher Vorteil besteht darin, dass sie ohne speziellen Treiber arbeitet, da sie dem Standardprotokoll UVC (USB Video Class) folgt. Da die meisten Betriebssysteme—Linux, Windows und macOS—UVC nativ unterstützen, erhalten Benutzer unmittelbar nach dem Anschließen der Kamera einen Videostream, ohne zusätzliche Konfiguration.
  
USB-Kameras werden aus den folgenden Gründen häufig in Embedded-Plattformen eingesetzt:
- **Plug-and-Play-Fähigkeit:** Anders als MIPI-Sensoren erfordern USB-Kameras keine Sensorinitialisierung, keine I2C-Registerkonfiguration und keine Einrichtung der ISP-Pipeline; das Video kann unmittelbar nach dem Anschließen aufgenommen werden.
- **Hohe Kompatibilität:** Die meisten USB-Kameras halten sich an die UVC-Spezifikation, sodass sie unabhängig von Hersteller oder Modell auf einheitliche Weise arbeiten.
- **Umfangreiche Unterstützung von Auflösungen und Formaten:** Gängige Formate wie MJPEG, YUYV und NV12 sind weit verbreitet.
- **Einfacher Anschluss und einfache Verkabelung:** USB-Kabel ermöglichen eine vereinfachte Verkabelung und unterstützen größere Entfernungen, oft mehrere Meter.
- **Geeignet für die Embedded-Entwicklung:** Weniger treiberbezogene Probleme ermöglichen ein schnelleres Prototyping.

In Linux-basierten Systemen werden USB-Kameras automatisch erkannt und als /dev/video*-Knoten bereitgestellt. Videoaufnahme und -steuerung können mit Standardwerkzeugen wie v4l2-ctl, ffmpeg und GStreamer durchgeführt werden.  
Viele USB-Kameras verfügen über einen integrierten ISP, der die Bildverarbeitung intern übernimmt—etwa automatischen Weißabgleich, automatische Belichtung und Farbkorrektur. Dies ermöglicht eine stabile Bildqualität auch auf Boards ohne externen ISP. Aufgrund dieser Eigenschaften haben sich USB-Kameras zu einer der einfachsten und vielseitigsten Kameralösungen in Bereichen wie Test, Embedded-Linux-Entwicklung, Robotik und schnellem Prototyping entwickelt.

## 2.4 Verfügbare Kameratypen auf dem D3-G
Die TOPST D3-G-Plattform unterstützt in Yocto- und Ubuntu-Umgebungen denselben Satz an Kameratypen. Zu den verfügbaren Kameraschnittstellen gehören USB, MIPI, GMSL, mit geringfügigen Konfigurationsunterschieden je nach verwendeter Schnittstelle.  
1. **MIPI-Kamera**  
Der TOPST D3-G bietet zwei MIPI-CSI-Anschlüsse, sodass pro Anschluss eine MIPI-Kamera verwendet werden kann. Die MIPI-CSI-Schnittstelle unterstützt zwei Anschlussformate:
    - **15-pin(2-Lane):** Geeignet für Sensoren mit geringerer Bandbreite wie OV5647 oder IMX219.
    - **20-pin (4-Lane):** Vorgesehen für hochauflösende Sensoren oder Sensoren mit hoher Bildrate.
2. **GMSL-Kamera**  
GMSL-Kameras unterstützen die Übertragung über große Entfernungen und werden häufig in Automotive- und Industrieanwendungen eingesetzt. Um GMSL auf dem TOPST D3-G zu verwenden, sind die folgenden Komponenten erforderlich:
    1. Verbinden Sie den Anschluss **20-pin MIPI CSI (4-Lane)** mit dem **TOPST MIPI Gender Board**.
    2. Montieren Sie das **Deserializer (Des)**-Board auf dem Gender Board.
    3. Schließen Sie über Fakra-Kabel bis zu vier GMSL-Kameras an das Des-Board an.
3. **USB-Kamera**  
USB-Kameras bieten den einfachsten Einstieg. Wenn sie an einen beliebigen USB 2.0- oder USB 3.0-Anschluss des Boards angeschlossen werden, werden sie automatisch erkannt und können ohne zusätzliche Konfiguration verwendet werden.  
Wenn es sich bei dem Gerät um eine V4L2-kompatible UVC-Kamera handelt, können Sie deren Erkennung mit dem folgenden Befehl überprüfen:  
    ``` 
    v4l2-ctl --list-devices
    ```

## 2.4 Verfügbare Kameratypen auf dem D3-G
Die TOPST AI-G-Plattform unterstützt ebenfalls mehrere Kameraeingangsschnittstellen, die Gesamtkonfiguration ist jedoch einfacher als beim D3-G und für leistungsstarke KI-Workloads optimiert. Insbesondere werden USB-Kameras auf dieser Plattform nicht unterstützt. Es stehen nur MIPI- und GMSL-Eingänge zur Verfügung.  
1. **MIPI-Kamera**  
Der TOPST D3-G bietet zwei MIPI-CSI-Anschlüsse, sodass pro Anschluss eine MIPI-Kamera verwendet werden kann. Die MIPI-CSI-Schnittstelle unterstützt zwei Anschlussformate:
    - **15-pin(2-Lane):** Geeignet für Sensoren mit geringerer Bandbreite wie OV5647 oder IMX219.
    - **20-pin (4-Lane):** Vorgesehen für hochauflösende Sensoren oder Sensoren mit hoher Bildrate.
2. **GMSL-Kamera**  
GMSL-Kameras unterstützen die Übertragung über große Entfernungen und werden häufig in Automotive- und Industrieanwendungen eingesetzt. Um GMSL auf dem TOPST D3-G zu verwenden, sind die folgenden Komponenten erforderlich:
    1. Verbinden Sie den Anschluss **20-pin MIPI CSI (4-Lane)** mit dem **TOPST MIPI Gender Board**.
    2. Montieren Sie das **Deserializer (Des)**-Board auf dem Gender Board.
    3. Schließen Sie über Fakra-Kabel bis zu vier GMSL-Kameras an das Des-Board an.

# 3. Anleitung zum Anschließen der Kamera
In Kapitel 3 wird beschrieben, wie Kameras an die Boards D3-G und AI-G angeschlossen werden.  
Dieser Abschnitt stellt sicher, dass Board und Kamera korrekt verbunden sind, damit die Kamera zuverlässig arbeiten kann. Bitte folgen Sie der nachstehenden Anleitung, um die von Ihnen vorgesehene Kamera anzuschließen.

## 3.1 Anschließen einer Kamera an den D3-G
Hinweise dazu, wie MIPI-CSI-2-, GMSL- und USB-Kameras an den D3-G angeschlossen werden, finden Sie in der nachstehenden Anleitung.  

### 3.1.1 MIPI-CSI-2-Kamera
Abbildung 3.1 zeigt die MIPI-CSI-Anschlüsse auf dem D3-G. Der D3-G unterstützt 2 Kanäle MIPI CSI, die jeweils mit einer 2-Lane-Schnittstelle konfiguriert sind. Eine 4-Lane-Schnittstelle ist optional und erfordert einen 20-poligen anstelle eines 15-poligen Anschlusses. Informationen zu den Pins finden Sie im D3-G Hardware-User Guide.

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/accessories/Camera/3.1%20MIPI%20CSI%20Connector%20on%20D3-G.png"></p>
<p align="center"><strong>Abbildung 3.1 MIPI-CSI-Anschluss auf dem D3-G</strong></p>

Verwenden Sie beim Anschließen einer MIPI-Kamera ein FFC (Flat Flexible Cable). Den richtigen Kabeltyp und die richtige Ausrichtung finden Sie in den Abbildungen 3.2 und 3.3.

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/accessories/Camera/3.2%20FFC%20Type.png"></p>
<p align="center"><strong>Abbildung 3.2 FFC-Typ</strong></p>

Das FFC-Kabel ist vom Typ 1.0 mm, 15-polig, und eine Seite muss eine andersfarbige Markierung (blau oder grau) aufweisen. Das Kabel sollte in der Ausrichtung B-Forward Direction eingesteckt werden. Den FFC-Typ finden Sie in Abbildung 3.2.

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/accessories/Camera/3.3%20An%20example%20of%20an%20FFC%20connected%20to%20the%20D3-G%20MIPI0%2015-pin%20Connector.png"></p>
<p align="center"><strong>Abbildung 3.3 Beispiel für ein an den 15-poligen MIPI0-Anschluss des D3-G angeschlossenes FFC</strong></p>

Stellen Sie sicher, dass die 15 silbernen Kontakte am FFC mit den 15 silbernen Kontakten im MIPI-Anschluss des D3-G fluchten.  
Beim MIPI1-Anschluss gilt dieselbe Anschlussmethode; verbinden Sie ihn auf dieselbe Weise wie den MIPI0-Anschluss.

### 3.1.2 GMSL-Kamera
GMSL-Kameras verwenden Fakra-Kabel. Daher können sie nicht direkt an das D3-G-Board angeschlossen werden. Stattdessen müssen sie über das Deserializer-Board (Des) und das TOPST MIPI Gender Board angeschlossen werden, bevor eine Verbindung zum D3-G hergestellt wird.  
Der Anschlussaufbau ist wie folgt.  

<p align="center"><strong>< D3-G > ↔ < TOPST MIPI Gender Board > ↔ < Des Board > ↔ < GMSL Camera ></strong></p>

GMSL-Kameras erfordern die Verwendung des TOPST MIPI Gender Board, das über den 20-poligen MIPI-Anschluss angeschlossen werden muss. Wenn Sie beispielsweise vier GMSL-Kameras verwenden möchten, müssen Sie diese über die 20-polige MIPI-Schnittstelle anschließen, wie in Abbildung 3.4 dargestellt.

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/accessories/Camera/3.4%2020-pin%20MIPI0%20Connector.png"></p>
<p align="center"><strong>Abbildung 3.4 20-poliger MIPI0-Anschluss</strong></p>  

1. Anschließen des D3-G-Boards an das TOPST MIPI Gender Board.  
    Das FFC-Kabel ist vom Typ 1.0 mm, 20-polig, und eine Seite muss eine andersfarbige Markierung (blau oder grau) aufweisen. Das Kabel sollte in der Ausrichtung A-Forward Direction eingesteckt werden. Den FFC-Typ finden Sie in Abbildung 3.5.  
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/accessories/Camera/3.2%20FFC%20Type.png"></p>
    <p align="center"><strong>Abbildung 3.5 FFC-Typ</strong></p>
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/accessories/Camera/3.6%20Anexample%20of%20an%20FFC%20connected%20to%20the%20D3-G%20MIPI0%2020-pin%20Connector.png"></p>
    <p align="center"><strong>Abbildung 3.6 Beispiel für ein an den 20-poligen MIPI0-Anschluss des D3-G angeschlossenes FFC</strong></p> 
    Stellen Sie sicher, dass die 20 silbernen Kontakte am FFC mit den 20 silbernen Kontakten im MIPI-Anschluss des D3-G fluchten
    Beim MIPI1-Anschluss gilt dieselbe Anschlussmethode; verbinden Sie ihn auf dieselbe Weise wie den MIPI0-Anschluss.
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/accessories/Camera/3.7%20An%20example%20of%20an%20FFC%20connected%20th%20toe%20TOPST%20MIPI%20Gender%20Board%20MIPI%20Connector.png"></p>
    <p align="center"><strong>Abbildung 3.7 Beispiel für ein an den MIPI-Anschluss des TOPST MIPI Gender Board angeschlossenes FFC</strong></p>
2. Anschließen des Deserializer-Boards an das MIPI Gender Board.  
    Verbinden Sie den JH2-Anschluss auf dem MIPI Gender Board mit dem JH1-Anschluss auf der Unterseite des SerDes-Boards.
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/accessories/Camera/3.8%20JH2%20Connector.png"></p>
    <p align="center"><strong>Abbildung 3.8 JH2-Anschluss</strong></p>
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/accessories/Camera/3.9%20JH1%20Connector.png"></p>
    <p align="center"><strong>Abbildung 3.9 JH1-Anschluss</strong></p>
3. Anschluss der GMSL-Kamera
    Schließen Sie die Kameras wie in Abbildung 3.10 dargestellt an. Die Abbildung zeigt ein Beispiel mit zwei Kameras, Sie können jedoch je nach Bedarf eine bis vier Kameras anschließen.
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/accessories/Camera/3.10%20GMSL%20Camera%20Connection.png"></p>
    <p align="center"><strong>Abbildung 3.10 JH2-Anschluss</strong></p>

### 3.1.3 USB-Kamera
USB-Kameras können verwendet werden, indem sie an einen USB 2.0- oder USB 3.0-Anschluss des D3-G angeschlossen werden. Wenn Sie eine USB-Kamera verwenden, die die USB 3.0-Spezifikation erfordert, schließen Sie diese unbedingt an den USB 3.0-Anschluss an.

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/accessories/Camera/3.11%20USB%20Camera%20Connection.png"></p>
<p align="center"><strong>Abbildung 3.11 Anschluss der USB-Kamera</strong></p>

## 3.2 Anschließen einer Kamera an den AI-G
### 3.2.1 MIPI-CSI-2-Kamera
Abbildung 3.12 zeigt die MIPI-CSI-Anschlüsse auf dem AI-G. Der AI-G unterstützt 2 Kanäle MIPI CSI, die jeweils mit einer 2-Lane-Schnittstelle konfiguriert sind.

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/accessories/Camera/3.12%20MIPI%20CSI%20Connector%20on%20AI-G.png"></p>
<p align="center"><strong>Abbildung 3.12 MIPI-CSI-Anschluss auf dem AI-G</strong></p>

Verwenden Sie beim Anschließen einer MIPI-Kamera ein FFC (Flat Flexible Cable). Den richtigen Kabeltyp und die richtige Ausrichtung finden Sie in den Abbildungen 3.13 und 3.14.

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/accessories/Camera/3.2%20FFC%20Type.png"></p>
<p align="center"><strong>Abbildung 3.13 FFC-Typ</strong></p>

Das FFC-Kabel ist vom Typ 1.0 mm, 15-polig, und eine Seite muss eine andersfarbige Markierung (blau oder grau) aufweisen. Das Kabel sollte in der Ausrichtung B-Forward Direction eingesteckt werden. Den FFC-Typ finden Sie in Abbildung 3.13.

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/accessories/Camera/3.14%20An%20example%20of%20an%20FFC%20connected%20to%20the%20AI-G%20MIPI%2015-pin%20Connector.png"></p>
<p align="center"><strong>Abbildung 3.14 Beispiel für ein an den 15-poligen MIPI-Anschluss des AI-G angeschlossenes FFC</strong></p>

Stellen Sie sicher, dass die 15 silbernen Kontakte am FFC mit den 15 silbernen Kontakten im MIPI-Anschluss des AI-G fluchten.

### 3.2.2 GMSL-Kamera
GMSL-Kameras verwenden Fakra-Kabel. Daher können sie nicht direkt an das AI-G-Board angeschlossen werden. Stattdessen müssen sie über das Deserializer-Board (Des) und das TOPST MIPI Gender Board angeschlossen werden, bevor eine Verbindung zum AI-G hergestellt wird.  
Der Anschlussaufbau ist wie folgt.

<p align="center"><strong>< AI-G > ↔ < TOPST MIPI Gender Board > ↔ < Des Board > ↔ < GMSL Camera ></strong></p>

GMSL-Kameras erfordern die Verwendung des TOPST MIPI Gender Board, das über den 20-poligen MIPI-Anschluss angeschlossen werden muss. Wenn Sie beispielsweise vier GMSL-Kameras verwenden möchten, müssen Sie diese über die 20-polige MIPI-Schnittstelle anschließen, wie in Abbildung 3.15 dargestellt.

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/accessories/Camera/3.15%2020-pin%20MIPI%20Connector.png"></p>
<p align="center"><strong>Abbildung 3.15 20-poliger MIPI-Anschluss</strong></p>

1. Anschließen des AI-G-Boards an das TOPST MIPI Gender Board.  
    Das FFC-Kabel ist vom Typ 1.0 mm, 20-polig, und eine Seite muss eine andersfarbige Markierung (blau oder grau) aufweisen. Das Kabel sollte in der Ausrichtung A-Forward Direction eingesteckt werden. Den FFC-Typ finden Sie in Abbildung 3.16.
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/accessories/Camera/3.2%20FFC%20Type.png"></p>
    <p align="center"><strong>Abbildung 3.16 FFC-Typ</strong></p>
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/accessories/Camera/3.17%20An%20example%20of%20an%20FFC%20connected%20to%20the%20AI-G%20MIPI%2020-pin%20Connector.png"></p>
    <p align="center"><strong>Abbildung 3.17 Beispiel für ein an den 20-poligen MIPI-Anschluss des AI-G angeschlossenes FFC</strong></p>
    Stellen Sie sicher, dass die 20 silbernen Kontakte am FFC mit den 20 silbernen Kontakten im MIPI-Anschluss des AI-G fluchten
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/accessories/Camera/3.18%20An%20example%20of%20an%20FFC%20connected%20to%20the%20TOPST%20MIPI%20Gender%20Board%20MIPI%20Connector.png"></p>
    <p align="center"><strong>Abbildung 3.18 Beispiel für ein an den MIPI-Anschluss des TOPST MIPI Gender Board angeschlossenes FFC</strong></p>
2. Anschließen des Deserializer-Boards an das MIPI Gender Board.  
    Verbinden Sie den JH2-Anschluss auf dem MIPI Gender Board mit dem JH1-Anschluss auf der Unterseite des SerDes-Boards.
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/accessories/Camera/3.19%20JH2%20Connector.png"></p>
    <p align="center"><strong>Abbildung 3.19 JH2-Anschluss</strong></p>
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/accessories/Camera/3.20%20JH1%20Connector.png"></p>
    <p align="center"><strong>Abbildung 3.20 JH1-Anschluss</strong></p>
3. Anschluss der GMSL-Kamera
    Schließen Sie die Kameras wie in Abbildung 3.21 dargestellt an. Die Abbildung zeigt ein Beispiel mit zwei Kameras, Sie können jedoch je nach Bedarf eine bis vier Kameras anschließen.
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/accessories/Camera/3.21%20GMSL%20Camera%20Connection.png"></p>
    <p align="center"><strong>Abbildung 3.21 Anschluss der GMSL-Kamera</strong></p>

# 4. Software-Einrichtung
In Kapitel 4 wird die für den Kamerabetrieb erforderliche Software-Einrichtung beschrieben. Für die Konfiguration von MIPI-CSI-2-Kameras (OV5647, IMX219) und GMSL-Kameras auf den Plattformen D3-G und AI-G beachten Sie die nachstehenden Anweisungen zur Yocto-Einrichtung.

## 4.1 Einrichtungsanleitung für MIPI-CSI-2-Kameras
Die TX-Datenrate kann mit der folgenden Formel berechnet werden:

<p align="center"><strong>TX-Datenrate ={ H_active }×{V_active }×{FPS}×{BPP}×{ Number_of_Cameras} × 1.3 (Reserve)</strong></p>

Die Gesamtdatenrate darf die MIPI-CSI-2-Bandbreitengrenze des D3-G von 2.1 Gbps pro Lane nicht überschreiten.  
Und die Gesamtdatenrate darf die MIPI-CSI-2-Bandbreitengrenze des AI-G von 1.5 Gbps pro Lane nicht überschreiten

### 4.1.1 Einrichtungsanleitung für den OV5647 auf dem D3-G
#### 4.1.1.1 Übersicht über den Sensor OV5647
##### 4.1.1.1.1 Einführung
Der OV5647 ist ein CMOS-Bildsensor mit 5 Megapixeln, der aufgrund seiner kompakten Größe, seiner stabilen Leistung und seiner Kompatibilität mit standardmäßigen MIPI-CSI-2-Schnittstellen häufig in Embedded-Kameraanwendungen eingesetzt wird. Er ist zudem der Bildsensor des Raspberry Pi Camera Module v1 und über verschiedene Arducam OV5647-Kameramodule erhältlich, die alle mit der TOPST D3-G-Plattform kompatibel sind.  
Benutzer können für den Kamerabetrieb entweder eine Raspberry Pi Camera v1 oder ein Arducam OV5647-Modul an den MIPI-CSI-Anschluss anschließen.

Auf der TOPST D3-G-Plattform wird der OV5647 über den 15- oder 20-poligen MIPI-CSI-Anschluss verbunden und über das V4L2-Framework gesteuert, wodurch ein einheitlicher Betrieb in Yocto- und Ubuntu-Umgebungen gewährleistet wird.

##### 4.1.1.1.2 Unterstützte Auflösungen und FPS
Die technischen Daten des OV5647-Kameramoduls (Raspberry Pi v1 oder Arducam OV5647) lauten wie folgt:  

<p align="center"><strong>Tabelle 4.1 Technische Daten des OV5647-Kameramoduls</strong></p>
<div align="center">
    <table>
        <tr>
            <td colspan="2" align="center"><strong>Spezifikation</strong></td>
            <td align="center"><strong>Beschreibung</strong></td>
        </tr>
        <tr>
            <td colspan="2">Sensor</td>
            <td>OmniVision OV5647</td>
        </tr>
        <tr>
            <td colspan="2">Auflösung</td>
            <td>2592 x 1944 (5MP)</td>
        </tr>
        <tr>
            <td colspan="2">Ausgabeformate</td>
            <td>RAW, YUV, JPEG</td>
        </tr>
        <tr>
            <td colspan="2">Schnittstelle</td>
            <td>MIPI CSI-2</td>
        </tr>
        <tr>
            <td colspan="2">Bildrate</td>
            <td>1080p30, 720p60, 480p90</td>
        </tr>
        <tr>
            <td colspan="2">Objektiv</td>
            <td>Fixfokus</td>
        </tr>
        <tr>
            <td colspan="2">Sichtfeld (FOV)</td>
            <td>Up to 54°</td>
        </tr>
        <tr>
            <td colspan="2">Kabeltyp</td>
            <td>FFC (15-polig)</td>
        </tr>
        <tr>
            <td colspan="2">Board-Abmessungen</td>
            <td>25mm x 24mm</td>
        </tr>
        <tr>
            <td colspan="2">Kompatibilität</td>
            <td>D3-G und Rasbperry Pi (über den MIPI-CSI-2-Anschluss)</td>
        </tr>
    </table>
</div>

Die auf dem D3-G unterstützten Sensorauflösungen und FPS lauten wie folgt:  
<p align="center"><strong>Tabelle 4.2 OV5647-Sensorauflösung auf dem D3-G</strong></p>
<div align="center">
    <table>
        <tr>
            <td colspan="3" align="center"><strong>Auflösung</strong></td>
            <td align="center"><strong>FPS</strong></td>
            <td align="center"><strong>Beschreibung</strong></td>
        </tr>
        <tr>
            <td colspan="3">1920x1080</td>
            <td>30</td>
            <td>Gibt ein 1080p-Bild aus, indem der mittlere Bereich des Bildes in voller Auflösung zugeschnitten wird</td>
        </tr>
        <tr>
            <td colspan="3">1296x972</td>
            <td>30</td>
            <td>Nutzt 2×2-Pixel-Binning, um die Empfindlichkeit zu erhöhen und das Rauschen zu verringern</td>
        </tr>
        <tr>
            <td colspan="3">640x480</td>
            <td>60</td>
            <td>Kombiniert 2×2-Binning mit <strong>Subsampling</strong>, wobei beim Auslesen Pixel übersprungen werden, um den Datendurchsatz zu verringern und höhere Bildraten zu erreichen</td>
        </tr>
    </table>
</div>

**Hinweis:** Wie in Tabelle 4.2 gezeigt, kann die volle Auflösung von **2592×1944 nicht verwendet werden**, bedingt durch die ISP-Spezifikationen des D3-G.

<p align="center"><strong>Tabelle 4.3 Maximale Auflösung nach Betriebsmodus</strong></p>
<div align="center">
    <table>
        <tr>
            <td rowspan="2" align="center"><strong>ISP-Kern</strong></td>
            <td colspan="2"><strong>Auflösung nach Betriebsmodus</strong></td>
        </tr>
        <tr>
            <td align="center"><strong>Standardmodus</strong></td>
            <td align="center"><strong>Speicherfreigabe-Modus</strong></td>
        </tr>
        <tr>
            <td>ISP0</td>
            <td>2048x1536 @ 60fps</td>
            <td>2048x1536 @ 60fps</td>
        </tr>
        <tr>
            <td>ISP1</td>
            <td>2560x1440 @ 60fps</td>
            <td>2560x1440 @ 60fps</td>
        </tr>
        <tr>
            <td>ISP2</td>
            <td>1280x720 @ 60fps</td>
            <td>1560x1440 @ 60fps</td>
        </tr>
        <tr>
            <td>ISP3</td>
            <td>1280x720 @ 60fps</td>
            <td>N/A</td>
        </tr>
    </table>
</div>

#### 4.1.1.2 OV5647-Auflösungskonfiguration in Yocto: Treiber
Um die Auflösung des OV5647-Sensors während des Yocto-Build-Prozesses zu ändern, folgen Sie den nachstehenden Anweisungen.  

Stellen Sie zunächst sicher, dass zur Aktivierung des OV5647 TOPST_CAM_MODULE = "ov5647" gesetzt ist in  
{build_dir}/build/d3-g-topst-main/conf/local.conf.  
Obwohl dies beim Initialisieren des Repositorys für den ersten Build standardmäßig aktiviert ist, überprüfen Sie es bitte erneut.

Um außerdem zu verhindern, dass der Quellcode während des Build-Prozesses entfernt wird, aktivieren Sie die folgende Zeile in  
{build_dir}/build/d3-g-topst-main/conf/local.conf:
```
INHERIT:remove = “rm_work”
```

Nachdem Sie die obige Option aktiviert haben, erstellen Sie das Image mit dem folgenden Befehl neu.
```
$ bitbake telechips-topst-image
```

Öffnen Sie zweitens nach Abschluss des Builds die Treiberdatei ov5647.c und nehmen Sie die erforderlichen Änderungen vor.

Wechseln Sie in das folgende Verzeichnis:
```
${build_dir}/build/d3-g-topst-main/tmp/work/d3_g_topst_main-telechips-linux/linux-topst/5.10.205-r0/git/drivers/media/i2c/telechips/
```

Beachten Sie vor der Änderung des Codes, dass der aktuelle Treiber die folgenden drei Modi unterstützt:
- 1920x1080 @ 30fps
- 1296x972 @ 30fps
- 640x480 @ 60fps  

Jede Auflösung entspricht jeweils Modus 1, Modus 2 und Modus 3.  

Der Modus 1920×1080 @ 30fps verwendet einen zentrierten Bildausschnitt, was zu einem engeren Sichtfeld führt, und der Modus 640×480 bietet eine unzureichende Auflösung. Im Gegensatz dazu verwendet der Modus 1296×972 ein 2×2-Binning, das ein größeres Sichtfeld bietet; daher wird er derzeit als Standardmodus verwendet.  
Öffnen Sie die Treiberdatei ov5647.c und ändern Sie den Standardmodus des OV5647 wie unten gezeigt.
```
#define OV5647_DEFAULT_MODE (&supported_modes_10bit[2])
```
1920×1080 @ 30fps entspricht Modus 1; Sie können **“#define OV5647_DEFAULT_MODE (&supported_modes_10bit[1])”** unverändert verwenden.  
Der Modus 1296×972 @ 30fps entspricht Modus 2, daher ist **“#define OV5647_DEFAULT_MODE (&supported_modes_10bit[2])”** bereits korrekt eingestellt.  
Für 640×480 @ 60fps, was Modus 3 entspricht, ändern Sie die Definition in **“#define OV5647_DEFAULT_MODE (&supported_modes_10bit[3])”**.

Erstellen Sie drittens den Kernel neu und generieren Sie das FAI-Image.  
Kehren Sie in das Build-Verzeichnis zurück und erstellen Sie den Kernel mit dem folgenden Befehl neu.
```
$ cd ${build_dir}/build/d3-g-topst-main/
$ bitbake -C compile linux-topst
$ cd ${build_dir}
$ ./stitch-fai-d3.sh
```
Flashen Sie anschließend die erzeugte Datei output_d3g.fai mit FWDN auf das Board; danach können Sie den OV5647-Sensor mit der gewünschten Auflösung verwenden.

**Hinweis:** Wenn Sie den MIPI1-CSI-Anschluss verwenden möchten, öffnen Sie die Datei tcc805x-videoinput-camera-module.dtsi unter
“{build_dir}/build/d3-g-topst-main/tmp/work/d3_g_topst_main-telechips-linux/linux-topst/5.10.205-r0/git/arch/arm64/boot/dts/telechips/tcc805x/override/” and change the included dtsi file from “tcc805x-videoinput-mipi0-ov5647.dtsi” to “tcc805x-videoinput-mipi1-ov5647.dtsi”. + Open the tcc805x-videoinput.dtsi file located in "{build_dir}/build/d3-g-topst-main/tmp/work/d3_g_topst_main-telechips-linux/linux-topst/5.10.205-r0/git/arch/arm64/boot/dts/telechips/tcc805x/" and change the mipi chmux from "mipi-chmux-0 = <0>;" to "mipi-chmux-0 = <1>;".

### 4.1.2 Einrichtungsanleitung für D3-G IMX219
#### 4.1.2.1 Übersicht über den IMX219-Sensor
##### 4.1.2.1.1 Einführung
Der IMX219 ist ein leistungsstarker 8-Megapixel-CMOS-Bildsensor von Sony, der für seine ausgezeichnete Bildqualität, seinen geringen Stromverbrauch und seine stabile Aufnahmeleistung in kompakten Kameramodulen bekannt ist. Er ist zudem der Sensor, der im Raspberry Pi Camera Module v2 verwendet wird, und ist in eingebetteten Bildverarbeitungssystemen, in der Robotik und in KI-basierten Kameraanwendungen weit verbreitet.

Auf der TOPST D3-G-Plattform kann der IMX219-Sensor entweder über den 15-poligen oder den 20-poligen MIPI-CSI-Anschluss angeschlossen werden und wird über das V4L2-Framework gesteuert. Dies ermöglicht eine einheitliche Schnittstelle und einen stabilen Kamerabetrieb sowohl in Yocto- als auch in Ubuntu-Umgebungen.

Mit seiner hohen Auflösung (8MP) und seinen rauscharmen Bildeigenschaften eignet sich der IMX219 gut für die Umsetzung hochwertiger Videoaufnahme- und Bildverarbeitungsfunktionen auf der TOPST D3-G-Plattform.

##### 4.1.2.1.2 Unterstützte Auflösungen und FPS
Die technischen Daten des IMX219-Kameramoduls (Raspberry Pi v2) lauten wie folgt:

<p align="center"><strong>Tabelle 4.4 Spezifikation des IMX219-Kameramoduls</strong></p>
<div align="center">
    <table>
        <tr>
            <td colspan="2" align="center"><strong>Spezifikation</strong></td>
            <td align="center"><strong>Beschreibung</strong></td>
        </tr>
        <tr>
            <td colspan="2">Sensor</td>
            <td>Sony Imx219</td>
        </tr>
        <tr>
            <td colspan="2">Auflösung</td>
            <td>3280 x 2464 (8 MP)</td>
        </tr>
        <tr>
            <td colspan="2">Ausgabeformate</td>
            <td>RAW, YUV, JPEG</td>
        </tr>
        <tr>
            <td colspan="2">Schnittstelle</td>
            <td>MIPI CSI-2</td>
        </tr>
        <tr>
            <td colspan="2">Bildrate</td>
            <td>1080p60, 720p180, 480p206</td>
        </tr>
        <tr>
            <td colspan="2">Objektiv</td>
            <td>Einstellbarer Fokus</td>
        </tr>
        <tr>
            <td colspan="2">Sichtfeld (FOV)</td>
            <td>Up to 62°</td>
        </tr>
        <tr>
            <td colspan="2">Kabeltyp</td>
            <td>FFC (15-polig)</td>
        </tr>
        <tr>
            <td colspan="2">Board-Abmessungen</td>
            <td>25mm x 24mm</td>
        </tr>
        <tr>
            <td colspan="2">Kompatibilität</td>
            <td>D3-G und Rasbperry Pi (über den MIPI-CSI-2-Anschluss)</td>
        </tr>
    </table>
</div>

Die auf dem D3-G unterstützten Sensorauflösungen und FPS lauten wie folgt:
<p align="center"><strong>Tabelle 4.5 IMX219-Sensorauflösung auf dem D3-G</strong></p>
<div align="center">
    <table>
        <tr>
            <td colspan="3" align="center"><strong>Auflösung</strong></td>
            <td align="center"><strong>FPS</strong></td>
            <td align="center"><strong>Beschreibung</strong></td>
        </tr>
        <tr>
            <td colspan="3">1920x1080</td>
            <td>30</td>
            <td>Gibt ein 1080p-Bild aus, indem der mittlere Bereich des Bildes in voller Auflösung zugeschnitten wird</td>
        </tr>
        <tr>
            <td colspan="3">1640x1232</td>
            <td>30</td>
            <td>Nutzt 2×2-Pixel-Binning, um die Empfindlichkeit zu erhöhen und das Rauschen zu verringern</td>
        </tr>
        <tr>
            <td colspan="3">640x480</td>
            <td>30</td>
            <td>Kombiniert 2×2-Binning mit <strong>Subsampling</strong>, wobei beim Auslesen Pixel übersprungen werden, um den Datendurchsatz zu verringern</td>
        </tr>
    </table>
</div>  

**Hinweis:** Wie in Tabelle 4.5 gezeigt, kann die volle Auflösung von **3820×2464 nicht verwendet werden**, bedingt durch die ISP-Spezifikationen des D3-G.

<p align="center"><strong>Tabelle 4.6 Maximale Auflösung nach Betriebsmodus</strong></p>
<div align="center">
    <table>
        <tr>
            <td rowspan="2" align="center"><strong>ISP-Kern</strong></td>
            <td colspan="2"><strong>Auflösung nach Betriebsmodus</strong></td>
        </tr>
        <tr>
            <td align="center"><strong>Standardmodus</strong></td>
            <td align="center"><strong>Speicherfreigabe-Modus</strong></td>
        </tr>
        <tr>
            <td>ISP0</td>
            <td>2048x1536 @ 60fps</td>
            <td>2048x1536 @ 60fps</td>
        </tr>
        <tr>
            <td>ISP1</td>
            <td>2560x1440 @ 60fps</td>
            <td>2560x1440 @ 60fps</td>
        </tr>
        <tr>
            <td>ISP2</td>
            <td>1280x720 @ 60fps</td>
            <td>1560x1440 @ 60fps</td>
        </tr>
        <tr>
            <td>ISP3</td>
            <td>1280x720 @ 60fps</td>
            <td>N/A</td>
        </tr>
    </table>
</div>

#### 4.1.2.2 IMX219 in Yocto aktivieren
Da das D3-G SDK standardmäßig so konfiguriert ist, dass der OV5647 aktiviert ist, müssen Sie den IMX219 vor dem Build aktivieren.   
Dabei sind zwei Fälle zu unterscheiden: wenn das SDK bereits erstellt wurde und wenn es zum ersten Mal erstellt wird.

##### 4.1.2.2.1 IMX219 vor dem ersten Build aktivieren
Folgen Sie beim ersten Build den nachstehenden Schritten, um den IMX219 zu aktivieren, und fahren Sie mit dem Build fort.
1. Sourcen Sie das Umgebungs-Setup-Skript und wählen Sie Option 2
    ```
    $ source poky/meta-topst/topst-build.sh
    ```
2. Öffnen Sie die Datei local.conf unter dem folgenden Pfad
    ```
    ${build_dir}/build/d3-g-topst-main/conf/local.conf
    ```
3. Kommentieren Sie den TOPST_CAM_MODULE-Eintrag für ov5647 aus und aktivieren Sie den Eintrag für imx219
    ```
    #TOPST_CAM_MODULE = "ov5647"
    TOPST_CAM_MODULE = "imx219"
    ```
4. Führen Sie den Build-Prozess aus
    ```
    $ bitbake telechips-topst-image
    ```
##### 4.1.2.2.2 IMX219 aktivieren, nachdem der Build bereits abgeschlossen ist
Im vorhandenen Build ist standardmäßig der OV5647-Sensor aktiviert. Folgen Sie den nachstehenden Schritten, um den IMX219 zu aktivieren.
1. Öffnen Sie die Datei local.conf unter dem folgenden Pfad
    ```
    ${build_dir}/build/d3-g-topst-main/conf/local.conf
    ```
2. Kommentieren Sie den TOPST_CAM_MODULE-Eintrag für ov5647 aus und aktivieren Sie den Eintrag für imx219
    ```
    #TOPST_CAM_MODULE = "ov5647"
    TOPST_CAM_MODULE = "imx219"
    ```
3. Führen Sie eine cleansstate-Operation für isp-server und isp-firmware aus
    ```
    $ bitbake -c cleansstate isp-firmware
    $ bitbake -c cleansstate isp-server
    ```
4. Führen Sie den Build-Prozess aus
    ```
    $ bitbake telechips-topst-image


#### 4.1.2.3 IMX219-Auflösungskonfiguration in Yocto: Treiber
Um die Auflösung des IMX219-Sensors während des Yocto-Build-Prozesses zu ändern, folgen Sie den nachstehenden Anweisungen.

Stellen Sie zunächst sicher, dass zur Aktivierung des imx219 TOPST_CAM_MODULE = "imx219" gesetzt ist in
{build_dir}/build/d3-g-topst-main/conf/local.conf.

Um außerdem zu verhindern, dass der Quellcode während des Build-Prozesses entfernt wird, aktivieren Sie die folgende Zeile in
{build_dir}/build/d3-g-topst-main/conf/local.conf:
```
INHERIT:remove = “rm_work”
```

Nachdem Sie die obige Option aktiviert haben, erstellen Sie das Image mit dem folgenden Befehl neu.
```
$ bitbake telechips-topst-image
```

Öffnen Sie zweitens nach Abschluss des Builds die Treiberdatei imx219.c und nehmen Sie die erforderlichen Änderungen vor.

Wechseln Sie in das folgende Verzeichnis:
```
${build_dir}/build/d3-g-topst-main/tmp/work/d3_g_topst_main-telechips-linux/linux-topst/5.10.205-r0/git/drivers/media/i2c/telechips/
```

Beachten Sie vor der Änderung des Codes, dass der aktuelle Treiber die folgenden drei Modi unterstützt:
- 1920x1080 @ 30fps
- 1640x1232 @ 30fps
- 640x480 @ 30fps

Jede Auflösung entspricht jeweils Modus 1, Modus 2 und Modus 3.

Der Modus 1920×1080 @ 30fps verwendet einen zentrierten Bildausschnitt, was zu einem engeren Sichtfeld führt, und der Modus 640×480 bietet eine unzureichende Auflösung. Im Gegensatz dazu verwendet der Modus 1640×1232 ein 2×2-Binning, das ein größeres Sichtfeld bietet; daher wird er derzeit als Standardmodus verwendet.  
Öffnen Sie die Treiberdatei imx219.c und ändern Sie die unten beschriebenen Abschnitte innerhalb der Funktionen imx219_set_default_format, imx219_open und imx219_probe.
- imx219_set_default_format
    ```
    fmt->width = supported_modes[2].width;
    fmt->height = supported_modes[2].height;
    ```
- imx219_open
    ```
    try_fmt_img->width = supported_modes[2].width;
    try_fmt_img->height = supported_modes[2].height;
    ```
- imx219_probe
    ```
    imx219->mode = &supported_modes[2];
    ```

Da 1920×1080 @ 30fps Modus 1 entspricht, ändern Sie alle supported_modes-Verweise innerhalb der drei Funktionen in **“supported_modes[1]”**.  
Der Modus 1640×1232 @ 30fps entspricht Modus 2, ersetzen Sie sie daher entsprechend durch **“supported_modes[2]”**.  
Für 640×480 @ 30fps, was Modus 3 entspricht, ändern Sie alle Verweise in **“supported_modes [3]”**.

Erstellen Sie drittens den Kernel neu und generieren Sie das FAI-Image.  
Kehren Sie in das Build-Verzeichnis zurück und erstellen Sie den Kernel mit dem folgenden Befehl neu.
```
$ cd ${build_dir}/build/d3-g-topst-main/
$ bitbake -C compile linux-topst
$ cd ${build_dir}
$ ./stitch-fai-d3.sh
```

Flashen Sie anschließend die erzeugte Datei output_d3g.fai mit FWDN auf das Board; danach können Sie den IMX219-Sensor mit der gewünschten Auflösung verwenden.

**Hinweis:** Wenn Sie den MIPI1-CSI-Anschluss verwenden möchten, öffnen Sie die Datei tcc805x-videoinput-camera-module.dtsi unter
“{build_dir}/build/d3-g-topst-main/tmp/work/d3_g_topst_main-telechips-linux/linux-topst/5.10.205-r0/git/arch/arm64/boot/dts/telechips/tcc805x/override/”and change the included dtsi file from “tcc805x-videoinput-mipi0-imx219.dtsi” to “tcc805x-videoinput-mipi1-imx219.dtsi”. + Open the tcc805x-videoinput.dtsi file located in "{build_dir}/build/d3-g-topst-main/tmp/work/d3_g_topst_main-telechips-linux/linux-topst/5.10.205-r0/git/arch/arm64/boot/dts/telechips/tcc805x/" and change the mipi chmux from "mipi-chmux-0 = <0>;" to "mipi-chmux-0 = <1>;".

#### 4.1.2.4 So erhöhen Sie die FPS des IMX219 in Yocto: Treiber und Device Tree
Gemäß der Beschreibung des IMX219-Sensors unterstützt der Sensor Modi mit hoher Bildrate wie 1080p60, 720p180 und VGA206. Daher ist es möglich, die FPS für die vom Treiber imx219.c unterstützten Auflösungen—1920×1080, 1640×1232 und 640×480—zu erhöhen. Da der ISP-Kern auf der D3-G-Plattform bis zu 60 fps unterstützt, kann jede dieser Auflösungen auf maximal 60 fps angehoben werden. 

Die Formel zur Berechnung der FPS lautet:
<p align="center"><strong>{fps} = {pixel_rate}/{hts}x{vts}</strong></p>
Um die FPS zu erhöhen, müssen daher die Werte pixel_rate, hts und vts angepasst werden.  
In der aktuellen Treiberimplementierung sind sowohl pixel_rate als auch hts fest vorgegeben. Um die FPS zu erhöhen, besteht der einzig praktikable Ansatz darin, pixel_rate zu erhöhen, hts konstant zu halten und anschließend vts entsprechend anzupassen, um die gewünschte Bildrate zu erreichen.

Um die FPS auf 60 zu ändern, müssen sowohl der Treiber als auch der Device Tree aktualisiert werden.
Folgen Sie der nachstehenden Anleitung, um die FPS auf 60 zu ändern.

##### 4.1.2.4.1 1920x1080 @ 60fps
Um 60 fps zu erreichen, muss die folgende Beziehung gelten:  
fps = pixel_rate / (hts × vts)
- pixel_rate = 182,400,000
- hts = 3448
- Ziel-fps = 60

wäre der erforderliche VTS-Wert:
- vts = pixel_rate / (hts × fps) = 182,400,000 / (3448 × 60) ≈ 882

Der VTS-Wert muss jedoch größer als 1080 sein, daher ist diese Konfiguration nicht gültig.  
Um 60 fps zu erreichen, müssen daher hts fest bleiben und stattdessen pixel_rate, vts und das PLL_VT-Register angepasst werden.

Die erforderlichen Änderungen lauten wie folgt:
1. Treiberdatei imx219.c  
    A. Erhöhen Sie die Pixelrate und die Link-Frequenz
    ```
    #define IMX219_PIXEL_RATE            182400000    →   #define IMX219_PIXEL_RATE            278400000
    #define IMX219_DEFAULT_LINK_FREQ     456000000   →   #define IMX219_DEFAULT_LINK_FREQ     696000000
    ``` 
    B. Aktualisieren Sie den VTS-Wert für den 1080p-Modus:
    ```
    #define IMX219_VTS_30FPS_1080P       0x06e3       →   #define IMX219_VTS_30FPS_1080P       0x0542
    ```
    C. Ändern Sie das PLL_VT-Register in der Modustabelle für 1920x1080:
    ```
    // imx219_reg mode_1920_1080_regs[]
    {0x0307, 0x39}   →   {0x0307, 0x57}
    ```
2. Device-Tree-Datei tcc805x-videoinput-mipi0-imx219.dtsi  
    A. Aktualisieren Sie die Link-Frequenz passend zur neuen Pixelrate:
    ```
    // &i2c7
    /bits/ 64 <456000000> → /bits/ 64 <696000000>
    ```
    B. Aktualisieren Sie den hs-settle-Wert:
    ```
    hs-settle = <13> → hs-settle = <35>
    ```
3. Erstellen Sie den Kernel neu und generieren Sie das FAI-Image.  
    Kehren Sie in das Build-Verzeichnis zurück und erstellen Sie den Kernel mit dem folgenden Befehl neu.
    ```
    $ cd ${build_dir}/build/d3-g-topst-main/
    $ bitbake -C compile linux-topst
    $ cd ${build_dir}
    $ ./stitch-fai-d3.sh
    ```
Mit dem folgenden Befehl auf dem D3-G können Sie überprüfen, dass die FPS-Ausgabe 59.9 beträgt, was 60 fps entspricht.
```
$ v4l2-ctl --stream-mmap=3 --stream-count=300 --stream-to=/dev/null --verbose
```
Der GStreamer-Befehl auf dem D3-G für die Kamerawiedergabe ist nachfolgend dargestellt.
```
$ gst-launch-1.0 v4l2src device=/dev/video0 io-mode=2 ! video/x-raw,format=NV12,width=1920,height=1080,framerate=60/1 ! videoconvert ! waylandsink sync=false
```

##### 4.1.2.4.2 1640x1232 @ 60fps
Um 60 fps zu erreichen, muss die folgende Beziehung gelten:  
fps = pixel_rate / (hts × vts)
- pixel_rate = 182,400,000
- hts = 3448
- Ziel-fps = 60

wäre der erforderliche VTS-Wert:
- vts = pixel_rate / (hts × fps) = 182,400,000 / (3448 × 60) ≈ 882

Der VTS-Wert muss jedoch größer als 1080 sein, daher ist diese Konfiguration nicht gültig.  
Um 60 fps zu erreichen, müssen daher hts fest bleiben und stattdessen pixel_rate, vts und das PLL_VT-Register angepasst werden.

Die erforderlichen Änderungen lauten wie folgt:
1. Treiberdatei imx219.c  
    A. Erhöhen Sie die Pixelrate und die Link-Frequenz
    ```
    #define IMX219_PIXEL_RATE            182400000    →   #define IMX219_PIXEL_RATE            278400000
    #define IMX219_DEFAULT_LINK_FREQ     456000000   →   #define IMX219_DEFAULT_LINK_FREQ     696000000
    ``` 
    B. Aktualisieren Sie den VTS-Wert für den 1640_1232-Modus:
    ```
    #define IMX219_VTS_30FPS_BINNED       0x06e3       →   #define IMX219_VTS_30FPS_BINNED       0x0542
    ```
    C. Ändern Sie das PLL_VT-Register in der Modustabelle für 1920x1080:
    ```
    // imx219_reg mode_1640_1232_regs[]
    {0x0307, 0x39}   →   {0x0307, 0x57}
    ```
2. Device-Tree-Datei tcc805x-videoinput-mipi0-imx219.dtsi  
    A. Aktualisieren Sie die Link-Frequenz passend zur neuen Pixelrate:
    ```
    // &i2c7
    /bits/ 64 <456000000> → /bits/ 64 <696000000>
    ```
    B. Aktualisieren Sie den hs-settle-Wert:
    ```
    hs-settle = <13> → hs-settle = <34>
    ```
3. Erstellen Sie den Kernel neu und generieren Sie das FAI-Image.  
    Kehren Sie in das Build-Verzeichnis zurück und erstellen Sie den Kernel mit dem folgenden Befehl neu.
    ```
    $ cd ${build_dir}/build/d3-g-topst-main/
    $ bitbake -C compile linux-topst
    $ cd ${build_dir}
    $ ./stitch-fai-d3.sh
    ```
Mit dem folgenden Befehl auf dem D3-G können Sie überprüfen, dass die FPS-Ausgabe 59.9 beträgt, was 60 fps entspricht.
```
$ v4l2-ctl --stream-mmap=3 --stream-count=300 --stream-to=/dev/null --verbose
```
Der GStreamer-Befehl auf dem D3-G für die Kamerawiedergabe ist nachfolgend dargestellt.
```
$ gst-launch-1.0 v4l2src device=/dev/video0 io-mode=2 ! video/x-raw,format=NV12,width=1640,height=1232,framerate=60/1 ! videoconvert ! waylandsink sync=false
```

##### 4.1.2.4.3 640x480 @ 60fps
Um 60 fps zu erreichen, muss die folgende Beziehung gelten:  
fps = pixel_rate / (hts × vts)
- pixel_rate = 182,400,000
- hts = 3448
- Ziel-fps = 60

wäre der erforderliche VTS-Wert:
- vts = pixel_rate / (hts × fps) = 182,400,000 / (3448 × 60) ≈ 882

Da der VTS-Wert größer als 480 ist, ist die Bedingung erfüllt. Wie im vorherigen Beispiel passen wir die pixelrate und den VTS-Wert an, um die FPS zu ändern, während HTS fest bleibt.  
Sie können die FPS auch anpassen, indem Sie nur den VTS-Wert ändern, ohne die pixelrate zu verändern. Der Registerwert 0x0307 des IMX219 muss jedoch unverändert bleiben.

Die erforderlichen Änderungen lauten wie folgt:
1. Treiberdatei imx219.c  
    A. Erhöhen Sie die Pixelrate und die Link-Frequenz
    ```
    #define IMX219_PIXEL_RATE            182400000    →   #define IMX219_PIXEL_RATE            278400000
    #define IMX219_DEFAULT_LINK_FREQ     456000000   →   #define IMX219_DEFAULT_LINK_FREQ     696000000
    ``` 
    B. Aktualisieren Sie den VTS-Wert für den 640_480-Modus:
    ```
    #define IMX219_VTS_30FPS_640x480       0x06e3       →   #define IMX219_VTS_30FPS_640x480       0x0542
    ```
    C. Ändern Sie das PLL_VT-Register in der Modustabelle für 640x480:
    ```
    // imx219_reg mode_640_480_regs[]
    {0x0307, 0x39}   →   {0x0307, 0x57}
    ```
2. Device-Tree-Datei tcc805x-videoinput-mipi0-imx219.dtsi  
    A. Aktualisieren Sie die Link-Frequenz passend zur neuen Pixelrate:
    ```
    // &i2c7
    /bits/ 64 <456000000> → /bits/ 64 <696000000>
    ```
    B. Aktualisieren Sie den hs-settle-Wert:
    ```
    hs-settle = <13> → hs-settle = <26>
    ```
3. Erstellen Sie den Kernel neu und generieren Sie das FAI-Image.  
    Kehren Sie in das Build-Verzeichnis zurück und erstellen Sie den Kernel mit dem folgenden Befehl neu.
    ```
    $ cd ${build_dir}/build/d3-g-topst-main/
    $ bitbake -C compile linux-topst
    $ cd ${build_dir}
    $ ./stitch-fai-d3.sh
    ```
Mit dem folgenden Befehl auf dem D3-G können Sie überprüfen, dass die FPS-Ausgabe 59.9 beträgt, was 60 fps entspricht.
```
$ v4l2-ctl --stream-mmap=3 --stream-count=300 --stream-to=/dev/null --verbose
```
Der GStreamer-Befehl auf dem D3-G für die Kamerawiedergabe ist nachfolgend dargestellt.
```
$ gst-launch-1.0 v4l2src device=/dev/video0 io-mode=2 ! video/x-raw,format=NV12,width=640,height=480,framerate=60/1 ! videoconvert ! waylandsink sync=false
```

### 4.1.3 Benutzerhandbuch für den AI-G OV5647-Sensor
#### 4.1.3.1 Übersicht über den OV5647-Sensor
##### 4.1.3.1.1 Einführung
Der OV5647 ist ein 5-Megapixel-CMOS-Bildsensor, der aufgrund seiner kompakten Größe, seiner stabilen Leistung und seiner Kompatibilität mit standardmäßigen MIPI-CSI-2-Schnittstellen in eingebetteten Kameraanwendungen weit verbreitet ist. Er ist zudem der Bildsensor, der im Raspberry Pi Camera Module v1 verwendet wird, und ist über verschiedene Arducam OV5647-Kameramodule erhältlich, die alle mit der TOPST AI-G-Plattform kompatibel sind.  
Benutzer können für den Kamerabetrieb entweder eine Raspberry Pi Camera v1 oder ein Arducam OV5647-Modul an den MIPI-CSI-Anschluss anschließen.

Auf der TOPST AI-G-Plattform wird der OV5647 über den 15-poligen oder 20-poligen MIPI-CSI-Anschluss angeschlossen und über das V4L2-Framework gesteuert, was einen einheitlichen Betrieb sowohl in Yocto- als auch in Ubuntu-Umgebungen ermöglicht.

##### 4.1.3.1.2 Unterstützte Auflösungen und FPS
Die technischen Daten des OV5647-Kameramoduls (Raspberry Pi v1 oder Arducam OV5647) lauten wie folgt:
<p align="center"><strong>Tabelle 4.7 Spezifikation des OV5647-Kameramoduls</strong></p>
<div align="center">
    <table>
        <tr>
            <td colspan="2" align="center"><strong>Spezifikation</strong></td>
            <td align="center"><strong>Beschreibung</strong></td>
        </tr>
        <tr>
            <td colspan="2">Sensor</td>
            <td>OmniVision OV5647</td>
        </tr>
        <tr>
            <td colspan="2">Auflösung</td>
            <td>2592 x 1944 (5MP)</td>
        </tr>
        <tr>
            <td colspan="2">Ausgabeformate</td>
            <td>RAW, YUV, JPEG</td>
        </tr>
        <tr>
            <td colspan="2">Schnittstelle</td>
            <td>MIPI CSI-2</td>
        </tr>
        <tr>
            <td colspan="2">Bildrate</td>
            <td>1080p30, 720p60, 480p90</td>
        </tr>
        <tr>
            <td colspan="2">Objektiv</td>
            <td>Fixfokus</td>
        </tr>
        <tr>
            <td colspan="2">Sichtfeld (FOV)</td>
            <td>Up to 54°</td>
        </tr>
        <tr>
            <td colspan="2">Kabeltyp</td>
            <td>FFC (15-polig)</td>
        </tr>
        <tr>
            <td colspan="2">Board-Abmessungen</td>
            <td>25mm x 24mm</td>
        </tr>
        <tr>
            <td colspan="2">Kompatibilität</td>
            <td>D3-G und Rasbperry Pi (über den MIPI-CSI-2-Anschluss)</td>
        </tr>
    </table>
</div>

Die auf dem AI-G unterstützten Sensorauflösungen und FPS lauten wie folgt:  
<p align="center"><strong>Tabelle 4.8 OV5647-Sensorauflösung auf dem AI-G</strong></p>
<div align="center">
    <table>
        <tr>
            <td colspan="3" align="center"><strong>Auflösung</strong></td>
            <td align="center"><strong>FPS</strong></td>
            <td align="center"><strong>Beschreibung</strong></td>
        </tr>
        <tr>
            <td colspan="3">1920x1080</td>
            <td>30</td>
            <td>Gibt ein 1080p-Bild aus, indem der mittlere Bereich des Bildes in voller Auflösung zugeschnitten wird</td>
        </tr>
        <tr>
            <td colspan="3">1296x972</td>
            <td>30</td>
            <td>Nutzt 2×2-Pixel-Binning, um die Empfindlichkeit zu erhöhen und das Rauschen zu verringern</td>
        </tr>
        <tr>
            <td colspan="3">640x480</td>
            <td>60</td>
            <td>Kombiniert 2×2-Binning mit <strong>Subsampling</strong>, wobei beim Auslesen Pixel übersprungen werden, um den Datendurchsatz zu verringern und höhere Bildraten zu erreichen</td>
        </tr>
    </table>
</div>

**Hinweis:** Wie in Tabelle 4.8 gezeigt, wird die volle **Auflösung von 2592×1944 nicht verwendet**, da sie die Inferenzleistung erheblich verlangsamt.

<p align="center"><strong>Tabelle 4.9 Maximale Auflösung nach Betriebsmodus</strong></p>
<div align="center">
    <table>
        <tr>
            <td colspan="4" align="center"><strong>Verwendete CH.</strong></td>
            <td align="center"><strong>Betriebsmodus</strong></td>
            <td align="center"><strong>Max. Auflösung</strong></td>
            <td align="center"><strong>Eingabeformat</strong></td>
        </tr>
        <tr>
            <td colspan="4">4CH</td>
            <td>Standardmodus</td>
            <td>1280 x 720 @ 60fps</td>
            <td>RAW 24</td>
        </tr>
        <tr>
            <td colspan="4" rowspan="2">2CH</td>
            <td rowspan="2">Speicherfreigabe-Modus</td>
            <td>Option 1: 2048 x 1280 @ 60fps</td>
            <td>RAW 20</td>
        </tr>
        <tr>
            <td>Option 2: 2592 x 2048 @ 30fps + 2048 x 1280 @ 30fps</td>
            <td>RAW 24</td>
        </tr>
        <tr>
            <td colspan="4">1CH</td>
            <td>Speicherfreigabe-Modus</td>
            <td>2592 x 2048 @ 60fps</td>
            <td>RAW 20</td>
        </tr>
    </table>
</div>

#### 4.1.3.2 OV5647-Auflösungskonfiguration in Yocto: Treiber
Um die Auflösung des OV5647-Sensors während des Yocto-Build-Prozesses zu ändern, folgen Sie den nachstehenden Anweisungen.

Stellen Sie zunächst sicher, dass zur Aktivierung des OV5647 TOPST_CAM_MODULE = "ov5647" gesetzt ist in  
{build_dir}/build/ai-g-topst-main/conf/local.conf.  
Obwohl dies beim Initialisieren des Repositorys für den ersten Build standardmäßig aktiviert ist, überprüfen Sie es bitte erneut.

Um außerdem zu verhindern, dass der Quellcode während des Build-Prozesses entfernt wird, aktivieren Sie die folgende Zeile in  
{build_dir}/build/ai-g-topst-main/conf/local.conf:
```
INHERIT:remove = “rm_work”
```

Nachdem Sie die obige Option aktiviert haben, erstellen Sie das Image mit dem folgenden Befehl neu.
```
$ bitbake telechips-topst-image
```

Öffnen Sie zweitens nach Abschluss des Builds die Treiberdatei ov5647.c und nehmen Sie die erforderlichen Änderungen vor.

Wechseln Sie in das folgende Verzeichnis:
```
${build_dir}/build/ai-g-topst-main/tmp/work/ai_g_topst-telechips-linux/linux-topst/5.10.223-r0/git/drivers/media/i2c/telechips/
```

Beachten Sie vor der Änderung des Codes, dass der aktuelle Treiber die folgenden drei Modi unterstützt:
- 1920×1080 @ 30fps
- 1296×972 @ 30fps
- 640×480 @ 60fps

Jede Auflösung entspricht jeweils Modus 1, Modus 2 und Modus 3.

Der Modus 1920×1080 @ 30fps verwendet einen zentrierten Bildausschnitt, was zu einem engeren Sichtfeld führt, und der Modus 640×480 bietet eine unzureichende Auflösung. Im Gegensatz dazu verwendet der Modus 1296×972 ein 2×2-Binning, das ein größeres Sichtfeld bietet; daher wird er derzeit als Standardmodus verwendet.  
Öffnen Sie die Treiberdatei ov5647.c und ändern Sie den Standardmodus des OV5647 wie unten gezeigt.
```
#define OV5647_DEFAULT_MODE (&supported_modes_10bit[2])
```
1920×1080 @ 30fps entspricht Modus 1; Sie können **“#define OV5647_DEFAULT_MODE (&supported_modes_10bit[1])”** unverändert verwenden.  
Der Modus 1296×972 @ 30fps entspricht Modus 2, daher ist **“#define OV5647_DEFAULT_MODE (&supported_modes_10bit[2])”**bereits korrekt eingestellt.  
Für 640×480 @ 60fps, was Modus 3 entspricht, ändern Sie die Definition in **“#define OV5647_DEFAULT_MODE (&supported_modes_10bit[3])”**.

Erstellen Sie drittens den Kernel neu und generieren Sie das FAI-Image.  
Kehren Sie in das Build-Verzeichnis zurück und erstellen Sie den Kernel mit dem folgenden Befehl neu.
```
$ cd ${build_dir}/build/ai-g-topst-main/
$ bitbake -C compile linux-topst
$ cd ${build_dir}
$ ./stitch-fai-ai.sh
```

Flashen Sie anschließend die erzeugte Datei output_aig.fai mit FWDN auf das Board; danach können Sie den OV5647-Sensor mit der gewünschten Auflösung verwenden.

### 4.1.4 Einrichtungsanleitung für den AI-G IMX219-Sensor
#### 4.1.4.1 Übersicht über den IMX219-Sensor
##### 4.1.4.1.1 Einführung
Der IMX219 ist ein leistungsstarker 8-Megapixel-CMOS-Bildsensor von Sony, der für seine ausgezeichnete Bildqualität, seinen geringen Stromverbrauch und seine stabile Aufnahmeleistung in kompakten Kameramodulen bekannt ist. Er ist zudem der Sensor, der im Raspberry Pi Camera Module v2 verwendet wird, und ist in eingebetteten Bildverarbeitungssystemen, in der Robotik und in KI-basierten Kameraanwendungen weit verbreitet.

Auf der TOPST AI-G-Plattform kann der IMX219-Sensor entweder über den 15-poligen oder den 20-poligen MIPI-CSI-Anschluss angeschlossen werden und wird über das V4L2-Framework gesteuert. Dies ermöglicht eine einheitliche Schnittstelle und einen stabilen Kamerabetrieb sowohl in Yocto- als auch in Ubuntu-Umgebungen.

Mit seiner hohen Auflösung (8MP) und seinen rauscharmen Bildeigenschaften eignet sich der IMX219 gut für die Umsetzung hochwertiger Videoaufnahme- und Bildverarbeitungsfunktionen auf der TOPST AI-G-Plattform.

##### 4.1.4.1.2 Unterstützte Auflösungen und FPS
Die technischen Daten des IMX219-Kameramoduls (Raspberry Pi v2) lauten wie folgt:
<p align="center"><strong>Tabelle 4.10 Spezifikation des IMX219-Kameramoduls</strong></p>
<div align="center">
    <table>
        <tr>
            <td colspan="2" align="center"><strong>Spezifikation</strong></td>
            <td align="center"><strong>Beschreibung</strong></td>
        </tr>
        <tr>
            <td colspan="2">Sensor</td>
            <td>Sony Imx219</td>
        </tr>
        <tr>
            <td colspan="2">Auflösung</td>
            <td>3280 x 2464 (8 MP)</td>
        </tr>
        <tr>
            <td colspan="2">Ausgabeformate</td>
            <td>RAW, YUV, JPEG</td>
        </tr>
        <tr>
            <td colspan="2">Schnittstelle</td>
            <td>MIPI CSI-2</td>
        </tr>
        <tr>
            <td colspan="2">Bildrate</td>
            <td>1080p60, 720p180, 480p206</td>
        </tr>
        <tr>
            <td colspan="2">Objektiv</td>
            <td>Einstellbarer Fokus</td>
        </tr>
        <tr>
            <td colspan="2">Sichtfeld (FOV)</td>
            <td>Up to 62°</td>
        </tr>
        <tr>
            <td colspan="2">Kabeltyp</td>
            <td>FFC (15-polig)</td>
        </tr>
        <tr>
            <td colspan="2">Board-Abmessungen</td>
            <td>25mm x 24mm</td>
        </tr>
        <tr>
            <td colspan="2">Kompatibilität</td>
            <td>D3-G und Rasbperry Pi (über den MIPI-CSI-2-Anschluss)</td>
        </tr>
    </table>
</div>

Die auf dem AI-G unterstützten Sensorauflösungen und FPS lauten wie folgt:
<p align="center"><strong>Tabelle 4.11 IMX219-Sensorauflösung auf dem AI-G</strong></p>
<div align="center">
    <table>
        <tr>
            <td colspan="3" align="center"><strong>Auflösung</strong></td>
            <td align="center"><strong>FPS</strong></td>
            <td align="center"><strong>Beschreibung</strong></td>
        </tr>
        <tr>
            <td colspan="3">1920x1080</td>
            <td>30</td>
            <td>Gibt ein 1080p-Bild aus, indem der mittlere Bereich des Bildes in voller Auflösung zugeschnitten wird</td>
        </tr>
        <tr>
            <td colspan="3">1640x1232</td>
            <td>30</td>
            <td>Nutzt 2×2-Pixel-Binning, um die Empfindlichkeit zu erhöhen und das Rauschen zu verringern</td>
        </tr>
        <tr>
            <td colspan="3">640x480</td>
            <td>30</td>
            <td>Kombiniert 2×2-Binning mit <strong>Subsampling</strong>, wobei beim Auslesen Pixel übersprungen werden, um den Datendurchsatz zu verringern</td>
        </tr>
    </table>
</div>

**Hinweis:** Wie in Tabelle 4.11 gezeigt, wird die volle Auflösung von 3820×2464 nicht verwendet, da sie die Inferenzleistung erheblich verlangsamt.

<p align="center"><strong>Tabelle 4.12 Maximale Auflösung nach Betriebsmodus</strong></p>
<div align="center">
    <table>
        <tr>
            <td colspan="4" align="center"><strong>Verwendete CH.</strong></td>
            <td align="center"><strong>Betriebsmodus</strong></td>
            <td align="center"><strong>Max. Auflösung</strong></td>
            <td align="center"><strong>Eingabeformat</strong></td>
        </tr>
        <tr>
            <td colspan="4">4CH</td>
            <td>Standardmodus</td>
            <td>1280 x 720 @ 60fps</td>
            <td>RAW 24</td>
        </tr>
        <tr>
            <td colspan="4" rowspan="2">2CH</td>
            <td rowspan="2">Speicherfreigabe-Modus</td>
            <td>Option 1: 2048 x 1280 @ 60fps</td>
            <td>RAW 20</td>
        </tr>
        <tr>
            <td>Option 2: 2592 x 2048 @ 30fps + 2048 x 1280 @ 30fps</td>
            <td>RAW 24</td>
        </tr>
        <tr>
            <td colspan="4">1CH</td>
            <td>Speicherfreigabe-Modus</td>
            <td>2592 x 2048 @ 60fps</td>
            <td>RAW 20</td>
        </tr>
    </table>
</div>

#### 4.1.4.2 IMX219 in Yocto aktivieren
Da das AI-G SDK standardmäßig so konfiguriert ist, dass der OV5647 aktiviert ist, müssen Sie den IMX219 vor dem Build aktivieren.  
Dabei sind zwei Fälle zu unterscheiden: wenn das SDK bereits erstellt wurde und wenn es zum ersten Mal erstellt wird.

##### 4.1.4.2.1 IMX219 vor dem ersten Build aktivieren
Folgen Sie beim ersten Build den nachstehenden Schritten, um den IMX219 zu aktivieren, und fahren Sie mit dem Build fort.
1. Sourcen Sie das Umgebungs-Setup-Skript und wählen Sie Option 1
    ```
    $ source poky/meta-topst/topst-build.sh
    ```
2. Öffnen Sie die Datei local.conf unter dem folgenden Pfad
    ```
    ${build_dir}/build/ai-g-topst-main/conf/local.conf
    ```
3. Kommentieren Sie den TOPST_CAM_MODULE-Eintrag für ov5647 aus und aktivieren Sie den Eintrag für imx219
    ```
    #TOPST_CAM_MODULE = "ov5647"
    TOPST_CAM_MODULE = "imx219"
    ```
4. Führen Sie den Build-Prozess aus
    ```
    $ bitbake telechips-topst-ai-image
    ```

##### 4.1.4.2.2 IMX219 aktivieren, nachdem der Build bereits abgeschlossen ist
Im vorhandenen Build ist standardmäßig der OV5647-Sensor aktiviert. Folgen Sie den nachstehenden Schritten, um den IMX219 zu aktivieren.
1. Öffnen Sie die Datei local.conf unter dem folgenden Pfad
    ```
    ${build_dir}/build/ai-g-topst-main/conf/local.conf
    ```
2. Kommentieren Sie den TOPST_CAM_MODULE-Eintrag für ov5647 aus und aktivieren Sie den Eintrag für imx219
    ```
    #TOPST_CAM_MODULE = "ov5647"
    TOPST_CAM_MODULE = "imx219"
    ```
3. Führen Sie eine cleansstate-Operation für isp-server und isp-firmware aus
    ```
    $ bitbake -c cleansstate isp-firmware
    $ bitbake -c cleansstate isp-server
    ```
4. Führen Sie den Build-Prozess aus
    ```
    $ bitbake telechips-topst-ai-image
    ```

#### 4.1.4.3 IMX219-Auflösungskonfiguration in Yocto: Treiber
Um die Auflösung des IMX219-Sensors während des Yocto-Build-Prozesses zu ändern, folgen Sie den nachstehenden Anweisungen.

Stellen Sie zunächst sicher, dass zur Aktivierung des imx219 TOPST_CAM_MODULE = "imx219" gesetzt ist in
{build_dir}/build/ai-g-topst-main/conf/local.conf.

Um außerdem zu verhindern, dass der Quellcode während des Build-Prozesses entfernt wird, aktivieren Sie die folgende Zeile in
{build_dir}/build/ai-g-topst-main/conf/local.conf:
```
INHERIT:remove = “rm_work”
```

Nachdem Sie die obige Option aktiviert haben, erstellen Sie das Image mit dem folgenden Befehl neu.
```
$ bitbake telechips-topst-ai-image
```
Öffnen Sie zweitens nach Abschluss des Builds die Treiberdatei imx219.c und nehmen Sie die erforderlichen Änderungen vor.

Wechseln Sie in das folgende Verzeichnis:
```
${build_dir}/build/ai-g-topst-main /ai-g-topst/tmp/work/ai_g_topst-telechips-linux/linux-topst/5.10.223-r0/git/drivers/media/i2c/telechips/
```
Beachten Sie vor der Änderung des Codes, dass der aktuelle Treiber die folgenden drei Modi unterstützt:
- 1920×1080 @ 30fps
- 1640×1232 @ 30fps
- 640×480 @ 30fps
Jede Auflösung entspricht jeweils Modus 1, Modus 2 und Modus 3.

Der Modus 1920×1080 @ 30fps verwendet einen zentrierten Bildausschnitt, was zu einem engeren Sichtfeld führt, und der Modus 640×480 bietet eine unzureichende Auflösung. Im Gegensatz dazu verwendet der Modus 1640×1232 ein 2×2-Binning, das ein größeres Sichtfeld bietet; daher wird er derzeit als Standardmodus verwendet.  
Öffnen Sie die Treiberdatei imx219.c und ändern Sie die unten beschriebenen Abschnitte innerhalb der Funktionen imx219_set_default_format, imx219_open und imx219_probe.
- imx219_set_default_format
    ```
    fmt->width = supported_modes[2].width;
    fmt->height = supported_modes[2].height;
    ```
- imx219_open
    ```
    try_fmt_img->width = supported_modes[2].width;
    try_fmt_img->height = supported_modes[2].height;
    ```
- imx219_probe
    ```
    imx219->mode = &supported_modes[2];
    ```

Da 1920×1080 @ 30fps Modus 1 entspricht, ändern Sie alle supported_modes-Verweise innerhalb der drei Funktionen in **“supported_modes[1]”**.  
Der Modus 1640×1232 @ 30fps entspricht Modus 2, ersetzen Sie sie daher entsprechend durch **“supported_modes[2]”**.  
Für 640×480 @ 30fps, was Modus 3 entspricht, ändern Sie alle Verweise in **“supported_modes [3]”**.

Erstellen Sie drittens den Kernel neu und generieren Sie das FAI-Image.  
Kehren Sie in das Build-Verzeichnis zurück und erstellen Sie den Kernel mit dem folgenden Befehl neu.
```
$ cd ${build_dir}/build/ai-g-topst-main/
$ bitbake -C compile linux-topst
$ cd ${build_dir}
$ ./stitch-fai-ai.sh
```

Flashen Sie anschließend die erzeugte Datei output_aig.fai mit FWDN auf das Board; danach können Sie den IMX219-Sensor mit der gewünschten Auflösung verwenden.

#### 4.1.4.4 So erhöhen Sie die FPS des IMX219 in Yocto: Treiber und Device Tree
Gemäß der Beschreibung des IMX219-Sensors unterstützt der Sensor Modi mit hoher Bildrate wie 1080p60, 720p180 und VGA206. Daher ist es möglich, die FPS für die vom Treiber imx219.c unterstützten Auflösungen—1920×1080, 1640×1232 und 640×480—zu erhöhen. Da der ISP-Kern auf der AI-G-Plattform bis zu 60 fps unterstützt, kann jede dieser Auflösungen auf maximal 60 fps angehoben werden.  

Die Formel zur Berechnung der FPS lautet:
<p align="center"><strong>{fps} = {pixel_rate}/{hts}x{vts}</strong></p>
Um die FPS zu erhöhen, müssen daher die Werte pixel_rate, hts und vts angepasst werden.  
In der aktuellen Treiberimplementierung sind sowohl pixel_rate als auch hts fest vorgegeben. Um die FPS zu erhöhen, besteht der einzig praktikable Ansatz darin, pixel_rate zu erhöhen, hts konstant zu halten und anschließend vts entsprechend anzupassen, um die gewünschte Bildrate zu erreichen.

Um die FPS auf 60 zu ändern, müssen sowohl der Treiber als auch der Device Tree aktualisiert werden.
Folgen Sie der nachstehenden Anleitung, um die FPS auf 60 zu ändern.

##### 4.1.2.4.1 1920x1080 @ 60fps
Um 60 fps zu erreichen, muss die folgende Beziehung gelten:  
fps = pixel_rate / (hts × vts)
- pixel_rate = 182,400,000
- hts = 3448
- Ziel-fps = 60

wäre der erforderliche VTS-Wert:
- vts = pixel_rate / (hts × fps) = 182,400,000 / (3448 × 60) ≈ 882

Der VTS-Wert muss jedoch größer als 1080 sein, daher ist diese Konfiguration nicht gültig.  
Um 60 fps zu erreichen, müssen daher hts fest bleiben und stattdessen pixel_rate, vts und das PLL_VT-Register angepasst werden.

Die erforderlichen Änderungen lauten wie folgt:
1. Treiberdatei imx219.c  
    A. Erhöhen Sie die Pixelrate und die Link-Frequenz
    ```
    #define IMX219_PIXEL_RATE            182400000    →   #define IMX219_PIXEL_RATE            278400000
    #define IMX219_DEFAULT_LINK_FREQ     456000000   →   #define IMX219_DEFAULT_LINK_FREQ     696000000
    ``` 
    B. Aktualisieren Sie den VTS-Wert für den 1080p-Modus:
    ```
    #define IMX219_VTS_30FPS_1080P       0x06e3       →   #define IMX219_VTS_30FPS_1080P       0x0542
    ```
    C. Ändern Sie das PLL_VT-Register in der Modustabelle für 1920x1080:
    ```
    // imx219_reg mode_1920_1080_regs[]
    {0x0307, 0x39}   →   {0x0307, 0x57}
    ```
2. Device-Tree-Datei tcc805x-videoinput-mipi0-imx219.dtsi  
    A. Aktualisieren Sie die Link-Frequenz passend zur neuen Pixelrate:
    ```
    // &i2c7
    /bits/ 64 <456000000> → /bits/ 64 <696000000>
    ```
    B. Aktualisieren Sie den hs-settle-Wert:
    ```
    hs-settle = <13> → hs-settle = <35>
    ```
3. Erstellen Sie den Kernel neu und generieren Sie das FAI-Image.  
    Kehren Sie in das Build-Verzeichnis zurück und erstellen Sie den Kernel mit dem folgenden Befehl neu.
    ```
    $ cd ${build_dir}/build/d3-g-topst-main/
    $ bitbake -C compile linux-topst
    $ cd ${build_dir}
    $ ./stitch-fai-d3.sh
    ```
Mit dem folgenden Befehl auf dem AI-G können Sie überprüfen, dass die FPS-Ausgabe 59.9 beträgt, was 60 fps entspricht.
```
$ v4l2-ctl --stream-mmap=3 --stream-count=300 --stream-to=/dev/null --verbose
```

##### 4.1.2.4.2 1640x1232 @ 60fps
Um 60 fps zu erreichen, muss die folgende Beziehung gelten:  
fps = pixel_rate / (hts × vts)
- pixel_rate = 182,400,000
- hts = 3448
- Ziel-fps = 60

wäre der erforderliche VTS-Wert:
- vts = pixel_rate / (hts × fps) = 182,400,000 / (3448 × 60) ≈ 882

Der VTS-Wert muss jedoch größer als 1080 sein, daher ist diese Konfiguration nicht gültig.  
Um 60 fps zu erreichen, müssen daher hts fest bleiben und stattdessen pixel_rate, vts und das PLL_VT-Register angepasst werden.

Die erforderlichen Änderungen lauten wie folgt:
1. Treiberdatei imx219.c  
    A. Erhöhen Sie die Pixelrate und die Link-Frequenz
    ```
    #define IMX219_PIXEL_RATE            182400000    →   #define IMX219_PIXEL_RATE            278400000
    #define IMX219_DEFAULT_LINK_FREQ     456000000   →   #define IMX219_DEFAULT_LINK_FREQ     696000000
    ``` 
    B. Aktualisieren Sie den VTS-Wert für den 1640_1232-Modus:
    ```
    #define IMX219_VTS_30FPS_BINNED       0x06e3       →   #define IMX219_VTS_30FPS_BINNED       0x0542
    ```
    C. Ändern Sie das PLL_VT-Register in der Modustabelle für 1920x1080:
    ```
    // imx219_reg mode_1640_1232_regs[]
    {0x0307, 0x39}   →   {0x0307, 0x57}
    ```
2. Device-Tree-Datei tcc805x-videoinput-mipi0-imx219.dtsi  
    A. Aktualisieren Sie die Link-Frequenz passend zur neuen Pixelrate:
    ```
    // &i2c7
    /bits/ 64 <456000000> → /bits/ 64 <696000000>
    ```
    B. Aktualisieren Sie den hs-settle-Wert:
    ```
    hs-settle = <13> → hs-settle = <34>
    ```
3. Erstellen Sie den Kernel neu und generieren Sie das FAI-Image.  
    Kehren Sie in das Build-Verzeichnis zurück und erstellen Sie den Kernel mit dem folgenden Befehl neu.
    ```
    $ cd ${build_dir}/build/d3-g-topst-main/
    $ bitbake -C compile linux-topst
    $ cd ${build_dir}
    $ ./stitch-fai-d3.sh
    ```
Mit dem folgenden Befehl auf dem AI-G können Sie überprüfen, dass die FPS-Ausgabe 59.9 beträgt, was 60 fps entspricht.
```
$ v4l2-ctl --stream-mmap=3 --stream-count=300 --stream-to=/dev/null --verbose
```

##### 4.1.2.4.3 640x480 @ 60fps
Um 60 fps zu erreichen, muss die folgende Beziehung gelten:  
fps = pixel_rate / (hts × vts)
- pixel_rate = 182,400,000
- hts = 3448
- Ziel-fps = 60

wäre der erforderliche VTS-Wert:
- vts = pixel_rate / (hts × fps) = 182,400,000 / (3448 × 60) ≈ 882

Da der VTS-Wert größer als 480 ist, ist die Bedingung erfüllt. Wie im vorherigen Beispiel passen wir die pixelrate und den VTS-Wert an, um die FPS zu ändern, während HTS fest bleibt.  
Sie können die FPS auch anpassen, indem Sie nur den VTS-Wert ändern, ohne die pixelrate zu verändern. Der Registerwert 0x0307 des IMX219 muss jedoch unverändert bleiben.

Die erforderlichen Änderungen lauten wie folgt:
1. Treiberdatei imx219.c  
    A. Erhöhen Sie die Pixelrate und die Link-Frequenz
    ```
    #define IMX219_PIXEL_RATE            182400000    →   #define IMX219_PIXEL_RATE            278400000
    #define IMX219_DEFAULT_LINK_FREQ     456000000   →   #define IMX219_DEFAULT_LINK_FREQ     696000000
    ``` 
    B. Aktualisieren Sie den VTS-Wert für den 640_480-Modus:
    ```
    #define IMX219_VTS_30FPS_640x480       0x06e3       →   #define IMX219_VTS_30FPS_640x480       0x0542
    ```
    C. Ändern Sie das PLL_VT-Register in der Modustabelle für 640x480:
    ```
    // imx219_reg mode_640_480_regs[]
    {0x0307, 0x39}   →   {0x0307, 0x57}
    ```
2. Device-Tree-Datei tcc805x-videoinput-mipi0-imx219.dtsi  
    A. Aktualisieren Sie die Link-Frequenz passend zur neuen Pixelrate:
    ```
    // &i2c7
    /bits/ 64 <456000000> → /bits/ 64 <696000000>
    ```
    B. Aktualisieren Sie den hs-settle-Wert:
    ```
    hs-settle = <13> → hs-settle = <26>
    ```
3. Erstellen Sie den Kernel neu und generieren Sie das FAI-Image.  
    Kehren Sie in das Build-Verzeichnis zurück und erstellen Sie den Kernel mit dem folgenden Befehl neu.
    ```
    $ cd ${build_dir}/build/d3-g-topst-main/
    $ bitbake -C compile linux-topst
    $ cd ${build_dir}
    $ ./stitch-fai-d3.sh
    ```
Mit dem folgenden Befehl auf dem AI-G können Sie überprüfen, dass die FPS-Ausgabe 59.9 beträgt, was 60 fps entspricht.
```
$ v4l2-ctl --stream-mmap=3 --stream-count=300 --stream-to=/dev/null --verbose
```

## 4.2 Einrichtungsanleitung für GMSL-Kameras
### 4.2.1 Einrichtungsanleitung für die D3-G GMSL-Kamera
Mit einem Deserializer-Board können Sie bis zu vier Kameras an einen einzelnen MIPI-CSI-Anschluss anschließen. Da das D3-G zwei MIPI-CSI-Anschlüsse bietet, können Sie eine der folgenden Konfigurationen wählen:
- Vier Kameras am MIPI0-Anschluss verwenden
- Vier Kameras am MIPI1-Anschluss verwenden
- MIPI0 und MIPI1 gemeinsam verwenden, um insgesamt acht Kameras anzuschließen

Bei der Konfiguration aller acht Kameras kann die Display-Erweiterungsfunktion des D3-G—die bis zu vier Displays unterstützt—mit bis zu drei Displays verwendet werden.

**Hinweis:** In dieser Anleitung wird die FHD-GMSL-Kamera IMX290 (cxd5700) verwendet.  
Wenn Sie eine andere GMSL-Kamera verwenden möchten, ist eine zusätzliche Kameraportierung erforderlich.

#### 4.2.1.1 So verwenden Sie den MIPI0-Anschluss
Zunächst müssen Sie die Kernel-Konfiguration sowohl für die GMSL-Kameras als auch für das SerDes-Board aktivieren.  
Fügen Sie die folgenden Einträge hinzu in die  
**{build_dir}/poky/meta-topst-bsp/recipes-kernel/linux/linux-topst/tcc805x/camera.cfg** file.
```
CONFIG_VIDEO_TCC_CXD5700=y
CONFIG_VIDEO_TCC_MAX9275=y
CONFIG_VIDEO_TCC_MAX96712=y
```
To prevent the source code from being removed during the build process, enable the following line, and comment out all occurrences of `TOPST_CAM_MODULE in {build_dir}/build/d3-g-topst-main/conf/local.conf:
```
#TOPST_CAM_MODULE = "ov5647"
#TOPST_CAM_MODULE = "imx219"
```
Nachdem Sie die obige Option geändert haben, erstellen Sie das Image mit dem folgenden Befehl neu.
```
$ bitbake -c cleansstate isp-firmware
$ bitbake -c cleansstate isp-server
$ bitbake telechips-topst-image
```
Als Nächstes müssen Sie den Device Tree im Kernel ändern. Folgen Sie der nachstehenden Anleitung, um die Änderungen anzuwenden und das Image neu zu erstellen.
1. Modify file {build_dir}/build/d3-g-topst-main/tmp/work/d3_g_topst_main-telechips-linux/linux-topst/5.10.205-r0/git/arch/arm64/boot/dts/telechips/tcc805x/override/tcc8050_53-lpd4x322-sv1.0-videoinput.dtsi as shown below
    ```
    @@ -192,7 +192,7 @@ max9295_1: max9295_1@40 {
            max9286_1: max9286_1@48 {
                    status          = "disabled";
                    compatible      = "tcc-maxim,max9286";
    -               pwd-gpios       = <&gpmc 0 1>;
    +               pwd-gpios       = <&gpg 5 1>;
                    reg             = <0x48>;       // 0x90 >> 1
            };
    @@ -200,7 +200,7 @@ max9286_1: max9286_1@48 {
            max96712_1: max96712_1@2a {
                    status          = "disabled";
                    compatible      = "tcc-maxim,max96712";
    -               pwd-gpios       = <&gpmc 0 1>;
    +               pwd-gpios       = <&gpg 5 1>;
                    reg             = <0x2A>;
            };
    };
    @@ -325,7 +325,7 @@ max9295e: max9295e@42 {
            max9286: max9286@48 {
                    status          = "disabled";
                    compatible      = "tcc-maxim,max9286";
    -               pwd-gpios       = <&gpg 5 1>;
    +               pwd-gpios       = <&gpmc 0 1>;
                    reg             = <0x48>;       // 0x90 >> 1
            };
    @@ -333,7 +333,7 @@ max9286: max9286@48 {
            max96712: max96712@2a {
                    status          = "disabled";
                    compatible      = "tcc-maxim,max96712";
    -               pwd-gpios       = <&gpg 5 1>;
    +              pwd-gpios       = <&gpmc 0 1>;
                    reg             = <0x2A>;
            };
    ```
2. Modify file {build_dir}/build/d3-g-topst-main/tmp/work/d3_g_topst_main-telechips-linux/linux-topst/5.10.205-r0/git/arch/arm64/boot/dts/telechips/tcc805x/override/tcc805x-videoinput-camera-module.dtsi as shown below
    ```
    //#include "tcc805x-videoinput-mipi0-ov5647.dtsi"
    //#include "tcc805x-videoinput-mipi0-imx219.dtsi"
    +#include "tcc805x-videoinput-mipi0-fhd.dtsi"
    ```
3. Create file {build_dir}/build/d3-g-topst-main/tmp/work/d3_g_topst_main-telechips-linux/linux-topst/5.10.205-r0/git/arch/arm64/boot/dts/telechips/tcc805x/override/tcc805x-videoinput-mipi0-fhd.dtsi as shown below
    ```
    // SPDX-License-Identifier: (GPL-2.0-or-later OR MIT)
    /*
    * Copyright (C) Telechips Inc.
    */

    &i2c6 {
        status = "okay";
    };

    &cxd5700_1 {
        /* ISP of camera module */
        status          = "okay";
        port {
                cxd5700_1_out: endpoint {
                        remote-endpoint = <&max9275_1_in>;
                        io-direction    = "output";
                };
        };
    };

    &max9275_1 {
        /* serializer */
        status          = "okay";
        ports {
                #address-cells = <1>;
                #size-cells = <0>;
                port@0 {
                        reg = <0>;
                        max9275_1_in: endpoint {
                                remote-endpoint = <&cxd5700_1_out>;
                                io-direction    = "input";
                        };
                };
                port@1 {
                        reg = <1>;
                        max9275_1_out: endpoint {
                                remote-endpoint = <&max96712_1_in0>;
                                io-direction    = "output";
                        };
                };
        };
    };

    &max96712_1 {
        /* deserializer */
        status          = "okay";
        pvd-name        = "fhd";
        /*
            * broadcasting mode access each linked devices
            * by the same I2C slave address.
            *
            * Also,
            * using the serdes I2C address mapping table,
            * each liked devices can be accessed
            * by the unique I2C slave address.
            */
        broadcasting-mode;
        ports {
                #address-cells = <1>;
                #size-cells = <0>;
                /*
                    * 0 ~ 3
                    * input ports. The number is matched with VC
                    *
                    * 4
                    * output port.
                    */
                port@0 {
                        reg = <0>;
                        max96712_1_in0: endpoint {
                                remote-endpoint = <&max9275_1_out>;
                                io-direction    = "input";
                                channel         = <0>;
                        };
                };
                port@1 {
                        reg = <1>;
                        max96712_1_in1: endpoint {
                                remote-endpoint = <&max9275_1_out>;
                                io-direction    = "input";
                                channel         = <1>;
                        };
                };
                port@2 {
                        reg = <2>;
                        max96712_1_in2: endpoint {
                                remote-endpoint = <&max9275_1_out>;
                                io-direction    = "input";
                                channel         = <2>;
                        };
                };
                port@3 {
                        reg = <3>;
                        max96712_1_in3: endpoint {
                                remote-endpoint = <&max9275_1_out>;
                                io-direction    = "input";
                                channel         = <3>;
                        };
                };
                port@4 {
                        reg = <4>;
                        max96712_1_out: endpoint {
                                remote-endpoint = <&mipi_csi2_0_in>;
                                io-direction    = "output";
                                channel         = <0>;
                        };
                };
        };
    };

    &mipi_csi2_0 {
        status = "okay";
        ports {
                #address-cells = <1>;
                #size-cells = <0>;
                /*
                    * 0
                    * input port.
                    *
                    * 1 ~ 4
                    * output ports. (1: VC0 ~ 4: VC3)
                    */
                port@0 {
                        reg = <0>;
                        mipi_csi2_0_in: endpoint {
                                remote-endpoint = <&max96712_1_out>;
                                io-direction    = "input";
                                num-channel     = <4>;

                                   /*
                                    * 0: CH0 only, no data interleave
                                    * 1: DT only
                                    * 2: VC only
                                    * 3: VC and DT
                                    */
                                interleave-mode = <3>;
                                hs-settle = <37>;
                                data-lanes = <1 2 3 4>;
                        };
                };
                port@1 {
                        reg = <1>;
                        mipi_csi2_0_out0: endpoint {
                                remote-endpoint = <&videoinput4_in>;
                                io-direction    = "output";
                                channel         = <0>;
                                /*
                                    * 0: Single pixel mode
                                    * 1: Dual pixel mode (RAW8/10/12, YUV422)
                                    * 2: Quad pixel mode (RAW8/10/12)
                                    * 3: Invalid
                                    */
                                pixel-mode = <1>;
                        };
                };
                port@2 {
                        reg = <2>;
                        mipi_csi2_0_out1: endpoint {
                                remote-endpoint = <&videoinput5_in>;
                                io-direction    = "output";
                                channel         = <1>;
                                pixel-mode = <1>;
                        };
                };
                port@3 {
                        reg = <3>;
                        mipi_csi2_0_out2: endpoint {
                                remote-endpoint = <&videoinput6_in>;
                                io-direction    = "output";
                                channel         = <2>;
                                pixel-mode = <1>;
                        };
                };
                port@4 {
                        reg = <4>;
                        mipi_csi2_0_out3: endpoint {
                                remote-endpoint = <&videoinput7_in>;
                                io-direction    = "output";
                                channel         = <3>;
                                pixel-mode = <1>;
                        };
                };
        };
    };

    &videoinput4 {
        status          = "okay";
        cifport         = <&cifport             9>;
        /* memory-region
            *  - [0]: parking guideline
            *  - [1]: deinterlacing by viqe
            *  - [2]: preview
            *  - [3]: last frame
            */
        memory-region   = <0
                            0
                            &pmap_rearcamera4
                            0>;
        port {
                videoinput4_in: endpoint {
                        remote-endpoint = <&mipi_csi2_0_out0>;
                        io-direction    = "input";
                        stream-enable   = <1>;  // VIN_CTRL.SE
                        flush-vsync     = <1>;  // VIN_MISC.FVS
                };
        };
    };

    &videoinput5 {
        status          = "okay";
        cifport         = <&cifport             10>;
        /* memory-region
            *  - [0]: parking guideline
            *  - [1]: deinterlacing by viqe
            *  - [2]: preview
            *  - [3]: last frame
            */
        memory-region   = <0
                            0
                            &pmap_rearcamera5
                            0>;
        port {
                videoinput5_in: endpoint {
                        remote-endpoint = <&mipi_csi2_0_out1>;
                        io-direction    = "input";
                        stream-enable   = <1>;  // VIN_CTRL.SE
                        flush-vsync     = <1>;  // VIN_MISC.FVS
                };
        };
    };

    &videoinput6 {
        status          = "okay";
        cifport         = <&cifport             11>;
        /* memory-region
            *  - [0]: parking guideline
            *  - [1]: deinterlacing by viqe
            *  - [2]: preview
            *  - [3]: last frame
            */
        memory-region   = <0
                            0
                            &pmap_rearcamera6
                            0>;
        port {
                videoinput6_in: endpoint {
                        remote-endpoint = <&mipi_csi2_0_out2>;
                        io-direction    = "input";
                        stream-enable   = <1>;  // VIN_CTRL.SE
                        flush-vsync     = <1>;  // VIN_MISC.FVS
                };
           };
    };

    &videoinput7 {
        status          = "okay";
        cifport         = <&cifport             12>;
        /* memory-region
            *  - [0]: parking guideline
            *  - [1]: deinterlacing by viqe
            *  - [2]: preview
            *  - [3]: last frame
            */
        memory-region   = <0
                            0
                            &pmap_rearcamera7
                            0>;
        port {
                videoinput7_in: endpoint {
                        remote-endpoint = <&mipi_csi2_0_out3>;
                        io-direction    = "input";
                        stream-enable   = <1>;  // VIN_CTRL.SE
                        flush-vsync     = <1>;  // VIN_MISC.FVS
                };
        };
    };
    ```
4. Modify file {build_dir}/build/d3-g-topst-main/tmp/work/d3_g_topst_main-telechips-linux/linux-topst/5.10.205-r0/git/arch/arm64/boot/dts/telechips/tcc805x/override/topst-d3-g-i2c.dtsi as shown below
    ```
    @@ -62,10 +62,10 @@ MPQ7920_2_LDO4: ldo4 {

    &i2c6 {
            status = "disabled";
    -       port-mux = <35>;
    +       port-mux = <12>;
            pinctrl-names = "default", "sleep";
    -       pinctrl-0 = <&i2c35_bus_active>;
    -       pinctrl-1 = <&i2c35_bus_sleep>;
    +       pinctrl-0 = <&i2c12_bus_active>;
    +       pinctrl-1 = <&i2c12_bus_sleep>;

            #address-cells = <1>;
            #size-cells = <0>;
    @@ -84,10 +84,10 @@ &i2c3 {

    &i2c7 {
            status = "disabled";
    -       port-mux = <12>;
    +       port-mux = <35>;
            pinctrl-names = "default", "sleep";
    -       pinctrl-0 = <&i2c12_bus_active>;
    -       pinctrl-1 = <&i2c12_bus_sleep>;
    +       pinctrl-0 = <&i2c35_bus_active>;
    +       pinctrl-1 = <&i2c35_bus_sleep>;

            #address-cells = <1>;
            #size-cells = <0>;
    ```
5. Modify file {build_dir}/build/d3-g-topst-main/tmp/work/d3_g_topst_main-telechips-linux/linux-topst/5.10.205-r0/git/arch/arm64/boot/dts/telechips/tcc805x/tcc805x-videoinput.dtsi as shown below
    ```
    @@ -40,26 +40,26 @@ mipi_wrap: mipi_wrap {
                    * 0: select output of MIPI0
                    * 1: select output of MIPI1
                    */
    -               mipi-chmux-0 = <0>;
    +               mipi-chmux-0 = <1>;
                    mipi-chmux-1 = <1>;
    -               mipi-chmux-2 = <0>;
    -               mipi-chmux-3 = <0>;
    +               mipi-chmux-2 = <1>;
    +               mipi-chmux-3 = <1>;

                    /*
                    * 0: select output of MIPI1
                    * 1: select output of MIPI0
                    */
    -               mipi-chmux-4 = <0>;
    -               mipi-chmux-5 = <0>;
    -               mipi-chmux-6 = <0>;
    -               mipi-chmux-7 = <0>;
    +               mipi-chmux-4 = <1>;
    +               mipi-chmux-5 = <1>;
    +               mipi-chmux-6 = <1>;
    +               mipi-chmux-7 = <1>;

                    /*
                    * 1: bypass isp
                    * 0: use isp
                    */
                    isp0-bypass = <0>;
    -               isp1-bypass = <0>;
    +               isp1-bypass = <1>;
                    isp2-bypass = <1>;
                    isp3-bypass = <1>;
    ```
6. Modify file {build_dir}/build/d3-g-topst-main/tmp/work/d3_g_topst_main-telechips-linux/linux-topst/5.10.205-r0/git/include/dt-bindings/pmap/tcc805x/pmap-tcc805x-linux-videoinput.h as shown below
    ```
    @@ -21,13 +21,13 @@
     /* The number of buffers */
    #define FRAMES_CAMERA_VIQE             4
    #define FRAMES_CAMERA_PREVIEW0         4
    -#define FRAMES_CAMERA_PREVIEW1         4
    +#define FRAMES_CAMERA_PREVIEW1         0
    #define FRAMES_CAMERA_PREVIEW2         0
    #define FRAMES_CAMERA_PREVIEW3         0
    -#define FRAMES_CAMERA_PREVIEW4         0
    -#define FRAMES_CAMERA_PREVIEW5         0
    -#define FRAMES_CAMERA_PREVIEW6         0
    -#define FRAMES_CAMERA_PREVIEW7         0
    +#define FRAMES_CAMERA_PREVIEW4         4
    +#define FRAMES_CAMERA_PREVIEW5         4
    +#define FRAMES_CAMERA_PREVIEW6         4
    +#define FRAMES_CAMERA_PREVIEW7         4

    /* Reserved memory size */
    #define PMAP_SIZE_CAMERA_VIQE          \
    ```
7. Erstellen Sie den Kernel neu und generieren Sie das FAI-Image.  
    Kehren Sie in das Build-Verzeichnis zurück und erstellen Sie den Kernel mit dem folgenden Befehl neu
    ```
    $ cd ${build_dir}/build/ai-g-topst-main/
    $ bitbake -C compile linux-topst
    $ cd ${build_dir}
    $ ./stitch-fai-ai.sh
    ```

Nach Abschluss des Builds gemäß der obigen Anleitung stehen die GMSL-Kameras unter /dev/ als video4, video5, video6 und video7 zur Verfügung.

#### 4.2.1.2 So verwenden Sie den MIPI1-Anschluss
Zunächst müssen Sie die Kernel-Konfiguration sowohl für die GMSL-Kameras als auch für das SerDes-Board aktivieren.  
Fügen Sie die folgenden Einträge hinzu in die  
**{build_dir}/poky/meta-topst-bsp/recipes-kernel/linux/linux-topst/tcc805x/camera.cfg** file.
```
CONFIG_VIDEO_TCC_CXD5700=y
CONFIG_VIDEO_TCC_MAX9275=y
CONFIG_VIDEO_TCC_MAX96712=y
```
To prevent the source code from being removed during the build process, enable the following line, and comment out all occurrences of `TOPST_CAM_MODULE in {build_dir}/build/d3-g-topst-main/conf/local.conf:
```
#TOPST_CAM_MODULE = "ov5647"
#TOPST_CAM_MODULE = "imx219"
```
Nachdem Sie die obige Option geändert haben, erstellen Sie das Image mit dem folgenden Befehl neu.
```
$ bitbake -c cleansstate isp-firmware
$ bitbake -c cleansstate isp-server
$ bitbake telechips-topst-image
```

Als Nächstes müssen Sie den Device Tree im Kernel ändern. Folgen Sie der nachstehenden Anleitung, um die Änderungen anzuwenden und das Image neu zu erstellen.
1. Modify file {build_dir}/build/d3-g-topst-main/tmp/work/d3_g_topst_main-telechips-linux/linux-topst/5.10.205-r0/git/arch/arm64/boot/dts/telechips/tcc805x/override/tcc805x-videoinput-camera-module.dtsi as shown below
    ```
    //#include "tcc805x-videoinput-mipi0-ov5647.dtsi"
    //#include "tcc805x-videoinput-mipi0-imx219.dtsi"
    +#include "tcc805x-videoinput-mipi1-fhd.dtsi"
    ```
2. Modify file {build_dir}/build/d3-g-topst-main/tmp/work/d3_g_topst_main-telechips-linux/linux-topst/5.10.205-r0/git/arch/arm64/boot/dts/telechips/tcc805x/tcc805x-videoinput.dtsi as shown below
    ```
    @@ -40,26 +40,26 @@ mipi_wrap: mipi_wrap {
                     * 0: select output of MIPI0
                     * 1: select output of MIPI1
                    */
                    mipi-chmux-0 = <0>;
                    mipi-chmux-1 = <1>;
    +               mipi-chmux-1 = <0>;
                    mipi-chmux-2 = <0>;
                    mipi-chmux-3 = <0>;

                    /*
                    * 0: select output of MIPI1
                    * 1: select output of MIPI0
                    */
                    mipi-chmux-4 = <0>;
                    mipi-chmux-5 = <0>;
                    mipi-chmux-6 = <0>;
                    mipi-chmux-7 = <0>;

                    /*
                    * 1: bypass isp
                    * 0: use isp
                    */
                    isp0-bypass = <0>;
    -               isp1-bypass = <0>;
    +               isp1-bypass = <1>;
                    isp2-bypass = <1>;
                    isp3-bypass = <1>;
    ```
3. Modify file {build_dir}/build/d3-g-topst-main/tmp/work/d3_g_topst_main-telechips-linux/linux-topst/5.10.205-r0/git/include/dt-bindings/pmap/tcc805x/pmap-tcc805x-linux-videoinput.h as shown below
    ```
    @@ -21,13 +21,13 @@
    /* The number of buffers */
    #define FRAMES_CAMERA_VIQE             4
    #define FRAMES_CAMERA_PREVIEW0         4
    -#define FRAMES_CAMERA_PREVIEW1         4
    +#define FRAMES_CAMERA_PREVIEW1         0
    #define FRAMES_CAMERA_PREVIEW2         0
    #define FRAMES_CAMERA_PREVIEW3         0
    -#define FRAMES_CAMERA_PREVIEW4         0
    -#define FRAMES_CAMERA_PREVIEW5         0
    -#define FRAMES_CAMERA_PREVIEW6         0
    -#define FRAMES_CAMERA_PREVIEW7         0
    +#define FRAMES_CAMERA_PREVIEW4         4
    +#define FRAMES_CAMERA_PREVIEW5         4
    +#define FRAMES_CAMERA_PREVIEW6         4
    +#define FRAMES_CAMERA_PREVIEW7         4

    /* Reserved memory size */
    #define PMAP_SIZE_CAMERA_VIQE          \
    ```
4. Erstellen Sie den Kernel neu und generieren Sie das FAI-Image.  
    Kehren Sie in das Build-Verzeichnis zurück und erstellen Sie den Kernel mit dem folgenden Befehl neu.
    ```
    $ cd ${build_dir}/build/ai-g-topst-main/
    $ bitbake -C compile linux-topst
    $ cd ${build_dir}
    $ ./stitch-fai-ai.sh
    ```

Nach Abschluss des Builds gemäß der obigen Anleitung stehen die GMSL-Kameras unter /dev/ als video4, video5, video6 und video7 zur Verfügung.

#### 4.2.1.3 So verwenden Sie die MIPI0- und MIPI1-Anschlüsse
Zunächst müssen Sie die Kernel-Konfiguration sowohl für die GMSL-Kameras als auch für das SerDes-Board aktivieren.  
Fügen Sie die folgenden Einträge hinzu in die  
**{build_dir}/poky/meta-topst-bsp/recipes-kernel/linux/linux-topst/tcc805x/camera.cfg** file.
```
CONFIG_VIDEO_TCC_CXD5700=y
CONFIG_VIDEO_TCC_MAX9275=y
CONFIG_VIDEO_TCC_MAX96712=y
```

To prevent the source code from being removed during the build process, enable the following line, and comment out all occurrences of `TOPST_CAM_MODULE in {build_dir}/build/d3-g-topst-main/conf/local.conf:
```
#TOPST_CAM_MODULE = "ov5647"
#TOPST_CAM_MODULE = "imx219"
```

Nachdem Sie die obige Option geändert haben, erstellen Sie das Image mit dem folgenden Befehl neu.
```
$ bitbake -c cleansstate isp-firmware
$ bitbake -c cleansstate isp-server
$ bitbake telechips-topst-image
```

Da sich die Display- und videoinput-Pfade in VIOC überschneiden, kann die 4-Display-Erweiterung nicht verwendet werden. Daher müssen Sie zunächst einen der in Konflikt stehenden Pfade in der Display-Konfiguration deaktivieren.
1. Modify file {build_dir}/build/d3-g-topst-main/tmp/work/d3_g_topst_main-telechips-linux/linux-topst/5.10.205-r0/git/arch/arm64/boot/dts/telechips/tcc805x/override/topst-d3-g-disp.dtsi as shown below
    ```
    @@ -437,7 +437,7 @@ dpv14_tx: dpv14_tx@12400000 {
                    sink_vcp_id = <1 2 3 4>;

                    /* default displayport configuration */
    -               dp-video-codes = <0 16 0 16 0 16 0 16>; /* video standard video codes */
    +               dp-video-codes = <0 16 0 16 0 16>; /* video standard video codes */
                    dp-phy-lane-swap = <1>;
                    dp-max-lane = <4>;
                    dp-max-rate = <3>;
    ```
2. Modify file {build_dir}/build/d3-g-topst-main/tmp/work/d3_g_topst_main-telechips-linux/linux-topst/5.10.205-r0/git/arch/arm64/boot/dts/telechips/tcc805x/override/topst-d3-g-display.dtsi as shown below
    ```
    @@ -34,9 +32,6 @@ &tccdrm_vioc2 {
            status = "okay";
    };

    -&tccdrm_vioc3 {
    -       status = "okay";
    -};

    &vioc0_out {
            vioc0_output_dp0: endpoint@0 {
    @@ -59,13 +54,6 @@ vioc2_output_dp2: endpoint@0 {
            };
    };

    -&vioc3_out {
    -       vioc3_output_dp3: endpoint@0 {
    -               reg = <0>;
    -               remote-endpoint = <&dp3_in_vioc3>;
    -       };
    -};
    -

    /* tcdrm dp */
    &tccdrm_dp0 {
    @@ -80,9 +68,6 @@ &tccdrm_dp2 {
            status = "okay";
    };

    -&tccdrm_dp3 {
    -       status = "okay";
    -};

    /* vioc0_output_dp0 -> dp0_in_vioc0 */
    &dp0_in {
    @@ -108,14 +93,6 @@ dp2_in_vioc2: endpoint@0 {
            };
    };

    -/* vioc3_output_dp3 -> dp3_in_vioc3 */
    -&dp3_in {
    -       dp3_in_vioc3: endpoint@0 {
    -               reg = <0>;
    -               remote-endpoint = <&vioc3_output_dp3>;
    -       };
    -};
    -
    /* screen_share_display_out -> tcc_drm_dummy0  */
    /* screen share */
    &tccdrm_screen_share {
    --
    ```

Als Nächstes müssen Sie den Device Tree im Kernel ändern. Folgen Sie der nachstehenden Anleitung, um die Änderungen anzuwenden und das Image neu zu erstellen.
1. Modify file {build_dir}/build/d3-g-topst-main/tmp/work/d3_g_topst_main-telechips-linux/linux-topst/5.10.205-r0/git/arch/arm64/boot/dts/telechips/tcc805x/override/tcc805x-videoinput-camera-module.dtsi as shown below
    ```
    //#include "tcc805x-videoinput-mipi0-ov5647.dtsi"
    //#include "tcc805x-videoinput-mipi0-imx219.dtsi"
    +#include "tcc805x-videoinput-mipi0-fhd.dtsi"
    +#include "tcc805x-videoinput-mipi1-fhd.dtsi"
    ```
2. Create file {build_dir}/build/d3-g-topst-main/tmp/work/d3_g_topst_main-telechips-linux/linux-topst/5.10.205-r0/git/arch/arm64/boot/dts/telechips/tcc805x/override/tcc805x-videoinput-mipi0-fhd.dtsi as shown below
    ```
    // SPDX-License-Identifier: (GPL-2.0-or-later OR MIT)
    /*
    * Copyright (C) Telechips Inc.
    */

    &i2c7 {
    	status = "okay";
    };

    &cxd5700 {
    	/* ISP of camera module */
    	status		= "okay";
    	port {
		    cxd5700_out: endpoint {
    			remote-endpoint = <&max9275_in>;
			    io-direction	= "output";
		    };
	    };
    };

    &max9275 {
    	/* serializer */
    	status		= "okay";
    	ports {
		    #address-cells = <1>;
		    #size-cells = <0>;
		    port@0 {
    			reg = <0>;
			    max9275_in: endpoint {
    				remote-endpoint = <&cxd5700_out>;
				    io-direction	= "input";
			    };
		    };
		    port@1 {
    			reg = <1>;
			    max9275_out: endpoint {
    				remote-endpoint = <&max96712_in0>;
				    io-direction	= "output";
			    };
		    };
	    };
    };

    &max96712 {
    	/* deserializer */
    	status		= "okay";
    	pvd-name	= "fhd";
    	/*
	    * broadcasting mode access each linked devices
	    * by the same I2C slave address.
	    *
	    * Also,
	    * using the serdes I2C address mapping table,
	    * each liked devices can be accessed
	    * by the unique I2C slave address.
	    */
	    broadcasting-mode;
	    ports {
    		#address-cells = <1>;
		    #size-cells = <0>;
		    /*
		    * 0 ~ 3
		    * input ports. The number is matched with VC
		    *
		    * 4
		    * output port.
		    */
		    port@0 {
    			reg = <0>;
			    max96712_in0: endpoint {
    				remote-endpoint = <&max9275_out>;
				    io-direction	= "input";
				    channel		= <0>;
			    };
		    };
		    port@1 {
    			reg = <1>;
			    max96712_in1: endpoint {
    				remote-endpoint = <&max9275_out>;
				    io-direction	= "input";
				    channel		= <1>;
			    };
		    };
		    port@2 {
    			reg = <2>;
			    max96712_in2: endpoint {
    				remote-endpoint = <&max9275_out>;
				    io-direction	= "input";
				    channel		= <2>;
			    };  
		    };
		    port@3 {
    			reg = <3>;
			    max96712_in3: endpoint {
    				remote-endpoint = <&max9275_out>;
				    io-direction	= "input";
				    channel		= <3>;
			    };
		    };
		    port@4 {
    			reg = <4>;
			    max96712_out: endpoint {
    				remote-endpoint = <&mipi_csi2_0_in>;
				    io-direction	= "output";
				    channel		= <0>;
			    };
		    };
	    };
    };

    &mipi_csi2_0 {
    	status = "okay";
    	ports {
		    #address-cells = <1>;
		    #size-cells = <0>;
		    /*
		    * 0
		    * input port.
		    *
		    * 1 ~ 4
		    * output ports. (1: VC0 ~ 4: VC3)
		    */
		    port@0 {
    			reg = <0>;
			    mipi_csi2_0_in: endpoint {
    				remote-endpoint	= <&max96712_out>;
				    io-direction	= "input";
				    num-channel	= <4>;

				    /*
				    * 0: CH0 only, no data interleave
				    * 1: DT only
				    * 2: VC only
				    * 3: VC and DT
				    */
				    interleave-mode = <3>;
				    hs-settle = <37>;
				    data-lanes = <1 2 3 4>;
			    };
		    };
		    port@1 {
    			reg = <1>;
			    mipi_csi2_0_out0: endpoint {
    				remote-endpoint	= <&videoinput0_in>;
				    io-direction	= "output";
				    channel		= <0>;
				    /*
				    * 0: Single pixel mode
				    * 1: Dual pixel mode (RAW8/10/12, YUV422)
				    * 2: Quad pixel mode (RAW8/10/12)
				    * 3: Invalid
				    */
				    pixel-mode = <1>;
			    };
		    };
		    port@2 {
    			reg = <2>;
	    		mipi_csi2_0_out1: endpoint {
    				remote-endpoint	= <&videoinput1_in>;
				    io-direction	= "output";
				    channel		= <1>;
				    pixel-mode = <1>;
			    };
		    };
		    port@3 {
    			reg = <3>;
			    mipi_csi2_0_out2: endpoint {
    				remote-endpoint	= <&videoinput2_in>;
				    io-direction	= "output";
				    channel		= <2>;
				    pixel-mode = <1>;
			    };
		    };
		    port@4 {
    			reg = <4>;
			    mipi_csi2_0_out3: endpoint {
    				remote-endpoint	= <&videoinput3_in>;
				    io-direction	= "output";
				    channel		= <3>;
				    pixel-mode = <1>;
			    };
		    };
	    };
    };

    &videoinput0 {
    	status		= "okay";
    	cifport		= <&cifport		5>;
    	/* memory-region
	    *  - [0]: parking guideline
	    *  - [1]: deinterlacing by viqe
	    *  - [2]: preview
	    *  - [3]: last frame
	    */
	    memory-region	= <0
			    0
			    &pmap_rearcamera
			    0>;
	    port {
    		videoinput0_in: endpoint {
			    remote-endpoint	= <&mipi_csi2_0_out0>;
			    io-direction	= "input";
			    stream-enable	= <1>;	// VIN_CTRL.SE
			    flush-vsync	= <1>;	// VIN_MISC.FVS
		    };
	    };
    };

    &videoinput1 {
    	status		= "okay";
    	cifport		= <&cifport		6>;
    	/* memory-region
	    *  - [0]: parking guideline
	    *  - [1]: deinterlacing by viqe
	    *  - [2]: preview
	    *  - [3]: last frame
	    */
	    memory-region	= <0
			    0
			    &pmap_rearcamera1
			    0>;
	    port {
    		videoinput1_in: endpoint {
			    remote-endpoint	= <&mipi_csi2_0_out1>;
    			io-direction	= "input";
			    stream-enable	= <1>;	// VIN_CTRL.SE
    			flush-vsync	= <1>;	// VIN_MISC.FVS
		    };
	    };
    };

    &videoinput2 {
    	status		= "okay";
    	cifport		= <&cifport		7>;
    	/* memory-region
	    *  - [0]: parking guideline
	    *  - [1]: deinterlacing by viqe
	    *  - [2]: preview
	    *  - [3]: last frame
	    */
	    memory-region	= <0
			    0
			    &pmap_rearcamera2
			    0>;
	    port {
    		videoinput2_in: endpoint {
			    remote-endpoint	= <&mipi_csi2_0_out2>;
			    io-direction	= "input";
			    stream-enable	= <1>;	// VIN_CTRL.SE
			    flush-vsync	= <1>;	// VIN_MISC.FVS
		    };
	    };
    };

    &videoinput3 {
    	status		= "okay";
	    cifport		= <&cifport		8>;
	    /* memory-region
	    *  - [0]: parking guideline
	    *  - [1]: deinterlacing by viqe
	    *  - [2]: preview
	    *  - [3]: last frame
	    */
	    memory-region	= <0
			    0
			    &pmap_rearcamera3
			    0>;
	    port {
    		videoinput3_in: endpoint {
			    remote-endpoint	= <&mipi_csi2_0_out3>;
			    io-direction	= "input";
			    stream-enable	= <1>;	// VIN_CTRL.SE
			    flush-vsync	= <1>;	// VIN_MISC.FVS
		    };
	    };
    };
    ```
3. Modify file {build_dir}/build/d3-g-topst-main/tmp/work/d3_g_topst_main-telechips-linux/linux-topst/5.10.205-r0/git/arch/arm64/boot/dts/telechips/tcc805x/tcc805x-videoinput.dtsi as shown below
    ```
    @@ -40,26 +40,26 @@ mipi_wrap: mipi_wrap {
                     * 0: select output of MIPI0
                    * 1: select output of MIPI1
                    */
                    mipi-chmux-0 = <0>;
    -               mipi-chmux-1 = <1>;
    +               mipi-chmux-1 = <0>;
                    mipi-chmux-2 = <0>;
                    mipi-chmux-3 = <0>;

                    /*
                    * 0: select output of MIPI1
                    * 1: select output of MIPI0
                    */
                    mipi-chmux-4 = <0>;
                    mipi-chmux-5 = <0>;
                    mipi-chmux-6 = <0>;
                    mipi-chmux-7 = <0>;

                    /*
                    * 1: bypass isp
                    * 0: use isp
                    */
    -               isp0-bypass = <0>;
    -               isp1-bypass = <0>;
    +               isp0-bypass = <1>;
    +               isp1-bypass = <1>;
                    isp2-bypass = <1>;
                    isp3-bypass = <1>;
    ```
4. Modify file {build_dir}/build/d3-g-topst-main/tmp/work/d3_g_topst_main-telechips-linux/linux-topst/5.10.205-r0/git/ include/dt-bindings/pmap/tcc805x/pmap-tcc805x-linux-videoinput.h as shown below
    ```
    @@ -21,13 +21,13 @@
     /* The number of buffers */
    #define FRAMES_CAMERA_VIQE             4
    #define FRAMES_CAMERA_PREVIEW0         4
    #define FRAMES_CAMERA_PREVIEW1         4
    -#define FRAMES_CAMERA_PREVIEW2         0
    -#define FRAMES_CAMERA_PREVIEW3         0
    -#define FRAMES_CAMERA_PREVIEW4         0
    -#define FRAMES_CAMERA_PREVIEW5         0
    -#define FRAMES_CAMERA_PREVIEW6         0
    -#define FRAMES_CAMERA_PREVIEW7         0
    +#define FRAMES_CAMERA_PREVIEW2         0
    +#define FRAMES_CAMERA_PREVIEW3         0
    +#define FRAMES_CAMERA_PREVIEW4         4
    +#define FRAMES_CAMERA_PREVIEW5         4
    +#define FRAMES_CAMERA_PREVIEW6         4
    +#define FRAMES_CAMERA_PREVIEW7         4

    /* Reserved memory size */
    #define PMAP_SIZE_CAMERA_VIQE          \
    ```
5. Erstellen Sie den Kernel neu und generieren Sie das FAI-Image.  
    Kehren Sie in das Build-Verzeichnis zurück und erstellen Sie den Kernel mit dem folgenden Befehl neu
    ```
    $ cd ${build_dir}/build/ai-g-topst-main/
    $ bitbake -C compile linux-topst
    $ cd ${build_dir}
    $ ./stitch-fai-ai.sh
    ```
Nach Abschluss des Builds gemäß der obigen Anleitung stehen die GMSL-Kameras unter /dev/ als video0, video1, video2, video3, 4, video5, video6 und video7 zur Verfügung.

### 4.2.2 Einrichtungsanleitung für die AI-G GMSL-Kamera
Mit einem Deserializer-Board können Sie bis zu vier Kameras an einen einzelnen MIPI-CSI-Anschluss anschließen.  
Das AI-G-Board bietet eine MIPI-CSI-Datenbandbreite von 1.5 Gbps pro Lane, sodass bis zu drei FHD-Kameras gleichzeitig betrieben werden können. Dementsprechend behandelt diese Anleitung den Anschluss von drei FHD-GMSL-Kameras.  
Bei HD-Kameras werden bis zu vier Einheiten unterstützt.

**Hinweis:** In dieser Anleitung wird die FHD-GMSL-Kamera IMX290 (cxd5700) verwendet.  
Wenn Sie eine andere GMSL-Kamera verwenden möchten, ist eine zusätzliche Kameraportierung erforderlich.

#### 4.2.2.1 So verwenden Sie den MIPI-CSI-Anschluss
Zunächst müssen Sie die Kernel-Konfiguration sowohl für die GMSL-Kameras als auch für das SerDes-Board aktivieren.  
Fügen Sie die folgenden Einträge hinzu in die  
**{build_dir}/poky/meta-topst-bsp/recipes-kernel/linux/linux-topst/tcc750x/camera.cfg** file.
```
CONFIG_VIDEO_TCC_CXD5700=y
CONFIG_VIDEO_TCC_MAX9275=y
CONFIG_VIDEO_TCC_MAX96712=y
```
To prevent the source code from being removed during the build process, enable the following line, and comment out all occurrences of `TOPST_CAM_MODULE in {build_dir}/build/ai-g-topst-main/conf/local.conf:
```
#TOPST_CAM_MODULE = "ov5647"
#TOPST_CAM_MODULE = "imx219"
```
Nachdem Sie die obige Option geändert haben, erstellen Sie das Image mit dem folgenden Befehl neu.
```
$ bitbake -c cleansstate isp-firmware
$ bitbake -c cleansstate isp-server
$ bitbake telechips-topst-ai-image
```

Als Nächstes müssen Sie den Device Tree im Kernel ändern. Folgen Sie der nachstehenden Anleitung, um die Änderungen anzuwenden und das Image neu zu erstellen.
1. Modify file {build_dir}/build/d3-g-topst-main/tmp/work/d3_g_topst_main-telechips-linux/linux-topst/5.10.205-r0/git/arch/arm64/boot/dts/telechips/tcc805x/override/tcc805x-videoinput-camera-module.dtsi as shown below
    ```
    //#include "tcc805x-videoinput-mipi0-ov5647.dtsi"
    //#include "tcc805x-videoinput-mipi0-imx219.dtsi"
    +#include " tcc750x-videoinput-odw-mipi0-fhd.dtsi"
    ```
2. Modify file {build_dir}/build/d3-g-topst-main/tmp/work/d3_g_topst_main-telechips-linux/linux-topst/5.10.205-r0/git/drivers/media/platform/tcc-mipi-csi2/csi2_s/v2.0/ tcc-mipi-csi2-csis-reg.h. as shown below
    ```
    @@ -6,7 +6,7 @@
    #ifndef TCC_MIPI_CSI2_CSIS_REG_H
    #define TCC_MIPI_CSI2_CSIS_REG_H
    
    -#define MAX_VC                         ((uint32_t)1)
    +#define MAX_VC                         ((uint32_t)4U)
    ```
3. Erstellen Sie den Kernel neu und generieren Sie das FAI-Image.  
    Kehren Sie in das Build-Verzeichnis zurück und erstellen Sie den Kernel mit dem folgenden Befehl neu
    ```
    $ cd ${build_dir}/build/ai-g-topst-main/
    $ bitbake -C compile linux-topst
    $ cd ${build_dir}
    $ ./stitch-fai-ai.sh
    ```
Nach Abschluss des Builds gemäß der obigen Anleitung stehen die GMSL-Kameras unter /dev/ als video0, video1 und video2 zur Verfügung.

# 5. Beispielcodes und Befehle
In diesem Kapitel werden Beispielcodes und Befehle bereitgestellt, die zeigen, wie MIPI-CSI-Kameras, GMSL-Kameras und USB-Kameras auf den Plattformen D3-G und AI-G verwendet werden. Dieser Abschnitt gibt einen kurzen Überblick über die Methoden der Kamerawiedergabe:  
auf dem D3-G können Kamerastreams mit GStreamer oder OpenCV angezeigt werden,  
während die Kamerawiedergabe auf dem AI-G über das Anwendungs-Framework erfolgt.

## 5.1 Beispielcodes und Befehle für die Kamerawiedergabe
### 5.1.1 Benutzerhandbuch für die MIPI-CSI-Kamera
In diesem Abschnitt wird beschrieben, wie das Video der MIPI-CSI-Kamera sowohl unter Yocto als auch unter Ubuntu angezeigt wird.

#### 5.1.1.1 Benutzerhandbuch für die MIPI-CSI-Kamera auf dem D3-G (OV5647)
##### 5.1.1.1.1 Verwendung des OV5647 mit dem Yocto-Image
Bei Verwendung des offiziellen Yocto-Image von der [topst.ai DOCS-Seite](https://topst.ai/tech/docs?page=624bd237b3013e87c05c125b8031e2f370ccca2b) oder eines durch manuelles Bauen von Yocto erzeugten Image arbeitet die OV5647-Kamera standardmäßig mit einer Auflösung von 1296×972 bei 30 fps. Daher wird für die Kamerawiedergabe in dieser Umgebung 1296×972 bei 30 fps verwendet.  
Führen Sie die folgenden Schritte aus:
1. Beenden Sie den aktuell laufenden Dienst topst-welcome
    ```
    $ sudo systemctl stop topst-welcome
    ```
2. Geben Sie den folgenden Befehl in der UART-Konsole ein
    ```
    $ export XDG_RUNTIME_DIR=/run/user/root
    ```
3. Geben Sie den Kamerastream mit einem GStreamer-Befehl wie unten gezeigt wieder
    ```
    $ gst-launch-1.0 v4l2src device=/dev/video0 io-mode=2 ! video/x-raw,format=NV12,width=1296,height=972,framerate=30/1 ! videoconvert ! waylandsink sync=false
    ```
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/accessories/Camera/5.1%201296%C3%97972%20ov5647%20camera%20out%20display%20on%20yocto.png"></p>
<p align="center"><strong>Abbildung 5.1 1296×972 OV5647 Kameraausgabe-Anzeige unter Yocto</strong></p>

**Hinweis:** Obwohl die Auflösung 1296×972 beträgt, können Sie das Video im Vollbildmodus wiedergeben, indem Sie die Option fullscreen=true am Ende des Befehls hinzufügen.

##### 5.1.1.1.2 Verwendung des OV5647 mit dem Ubuntu-Image
Bei Verwendung des offiziellen Ubuntu-Image von der [topst.ai DOCS-Seite](https://topst.ai/tech/docs?page=624bd237b3013e87c05c125b8031e2f370ccca2b) arbeitet die OV5647-Kamera standardmäßig mit einer Auflösung von 1296×972 bei 30 fps. Daher wird für die Kamerawiedergabe in dieser Umgebung 1296×972 bei 30 fps verwendet.  
Führen Sie die folgenden Schritte aus:
1. - Bei Verbindung über UART: Geben Sie den folgenden Befehl in der UART-Konsole ein, nachdem Sie sich mit Ihrem topst-Konto angemeldet haben
    ```
    $ export XDG_RUNTIME_DIR=/run/user/1000
    ```
    - Bei direkter Bedienung am Display: Öffnen Sie ein Terminalfenster
2. Geben Sie den Kamerastream mit einem GStreamer-Befehl wie unten gezeigt wieder. Da unter Ubuntu kein hardwarebeschleunigtes Wayland-Rendering verfügbar ist, wird stattdessen H.265-Encoding/Decoding verwendet, um die VPU-Beschleunigung für die Wiedergabe zu nutzen
    ```
    $ gst-launch-1.0 v4l2src device=/dev/video0 io-mode=2 ! video/x-raw,format=NV12,width=1280,height=720,framerate=30/1 ! v4l2h265enc ! h265parse ! v4l2h265dec ! videoconvert ! waylandsink sync=false
    ```
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/accessories/Camera/5.2%201296%C3%97972%20ov5647%20camera%20out%20display%20on%20ubuntu.png"></p>
<p align="center"><strong>Abbildung 5.2 1296×972 OV5647 Kameraausgabe-Anzeige unter Ubuntu</strong></p>

**Hinweis:** Obwohl die Auflösung 1296×972 beträgt, können Sie das Video im Vollbildmodus wiedergeben, indem Sie die Option fullscreen=true am Ende des Befehls hinzufügen.

Zusätzlich zu GStreamer können Sie auch OpenCV verwenden, um den Kamerastream anzuzeigen. Führen Sie die folgenden Schritte aus, um das Kamerabild mit OpenCV auf einfache Weise in der Vorschau anzuzeigen.
1. Installieren Sie OpenCV
    ```
    $ sudo apt-get install python3-opencv
    ```
2. Schreiben Sie den folgenden Code in die Datei opencv_cam.py
    ```
    import cv2
    
    pipeline = (
        "v4l2src device=/dev/video0 io-mode=2 ! "
        "video/x-raw,format=NV12,width=1296,height=972,framerate=30/1 ! "
        "videoconvert ! video/x-raw,format=BGR ! appsink sync=false"
    )
    
    cap = cv2.VideoCapture(pipeline, cv2.CAP_GSTREAMER)
    
    if not cap.isOpened():
        print("ERROR: cannot open camera via GStreamer")
        exit()
    
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Frame read error")
            break
    
        cv2.imshow("Camera", frame)
        if cv2.waitKey(1) == 27:
            break
    
    cap.release()
    cv2.destroyAllWindows()
    ```
3. Führen Sie opencv_cam.py mit Python aus
    ```
    $ python3 opencv_cam.py
    ```
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/accessories/Camera/5.3%201296%C3%97972%20opencv%20ov5647%20camera%20out%20display%20on%20ubuntu.png"></p>
<p align="center"><strong>Abbildung 5.3 1296×972 OV5647 Kameraausgabe unter Ubuntu mit OpenCV</strong></p>

##### 5.1.1.1.3 Gstreawmer-Pipeline-Konfiguration für jede Auflösung auf dem D3-G
Geben Sie für jede Auflösung die passenden GStreamer-Pipeline-Optionen an und starten Sie anschließend den Kamerastream.
1. 1920x1080 @ 30fps
    ```
    $ gst-launch-1.0 v4l2src device=/dev/video0 io-mode=2 ! video/x-raw,format=NV12,width=1920,height=1080,framerate=30/1 ! videoconvert ! waylandsink sync=false
    ```
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/accessories/Camera/5.4%201920x1080%20ov5647%20camera%20out%20display%20on%20yocto.png"></p>
    <p align="center"><strong>Abbildung 5.4 1920x1080 OV5647 Kameraausgabe-Anzeige unter Yocto</strong></p>
2. 1296x972 @ 30fps
    ```
    $ gst-launch-1.0 v4l2src device=/dev/video0 io-mode=2 ! video/x-raw,format=NV12,width=1296,height=972,framerate=30/1 ! videoconvert ! waylandsink sync=false
    ```
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/accessories/Camera/5.1%201296%C3%97972%20ov5647%20camera%20out%20display%20on%20yocto.png"></p>
    <p align="center"><strong>Abbildung 5.5 1296x972 OV5647 Kameraausgabe-Anzeige unter Yocto</strong></p>
3. 640x480 @ 60fps
    ```
    $ gst-launch-1.0 v4l2src device=/dev/video0 io-mode=2 ! video/x-raw,format=NV12,width=640,height=480,framerate=60/1 ! videoconvert ! waylandsink sync=false
    ```
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/accessories/Camera/5.6%20640x480%20ov5647%20camera%20out%20display%20on%20yocto.png"></p>
    <p align="center"><strong>Abbildung 5.6 640x480 OV5647 Kameraausgabe-Anzeige unter Yocto</strong></p>

Zusätzlich können Sie eine Pipeline konfigurieren, die den H.265-Encoder und -Decoder verwendet, um eine hardwarebeschleunigte Wiedergabe zu ermöglichen.
1. 1920x1080 @ 30fps
    ```
    $ gst-launch-1.0 v4l2src device=/dev/video0 io-mode=2 ! video/x-raw,format=NV12,width=1920,height=1080,framerate=30/1 ! v4l2h265enc ! h265parse ! v4l2h265dec ! videoconvert ! waylandsink sync=false
    ```
2. 1296x972 @ 30fps
    ```
    $ gst-launch-1.0 v4l2src device=/dev/video0 io-mode=2 ! video/x-raw,format=NV12,width=1280,height=720,framerate=30/1 !  v4l2h265enc ! h265parse ! v4l2h265dec ! videoconvert ! waylandsink sync=false
    ```
3. 640x480 @ 60fps
    ```
    $ gst-launch-1.0 v4l2src device=/dev/video0 io-mode=2 ! video/x-raw,format=NV12,width=640,height=480,framerate=60/1 ! v4l2h265enc ! h265parse ! v4l2h265dec ! videoconvert ! waylandsink sync=false
    ```

    Informationen zum Ändern der Auflösung finden Sie in Abschnitt 4.1.2.2.

#### 5.1.1.2 Benutzerhandbuch für die MIPI-CSI-Kamera auf dem D3-G (IMX219)
##### 5.1.1.2.1 Verwendung des IMX219 mit dem Yocto-Image
Bei Verwendung des offiziellen Yocto-Image von der [topst.ai DOCS-Seite](https://topst.ai/tech/docs?page=624bd237b3013e87c05c125b8031e2f370ccca2b) oder eines durch manuelles Bauen von Yocto erzeugten Image arbeitet die IMX219-Kamera standardmäßig mit einer Auflösung von 1640×1232 bei 30 fps. Daher wird für die Kamerawiedergabe in dieser Umgebung 1640×1232 bei 30 fps verwendet.  
Führen Sie die folgenden Schritte aus:
1. Beenden Sie den aktuell laufenden Dienst topst-welcome
    ```
    $ sudo systemctl stop topst-welcome
    ```
2. Geben Sie den folgenden Befehl in der UART-Konsole ein
    ```
    $ export XDG_RUNTIME_DIR=/run/user/root
    ```
3. Geben Sie den Kamerastream mit einem GSTreamer-Befehl wie unten gezeigt wieder
    ```
    $ gst-launch-1.0 v4l2src device=/dev/video0 io-mode=2 ! video/x-raw,format=NV12,width=1640,height=1232,framerate=30/1 ! videoconvert ! waylandsink sync=false
    ```
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/accessories/Camera/5.7%201640x1232%20imx219%20camera%20out%20display%20on%20yocto.png"></p>
<p align="center"><strong>Abbildung 5.7 1640x972 IMX219 Kameraausgabe-Anzeige unter Yocto</strong></p>

**Hinweis:** Obwohl die Auflösung 1640×1232 beträgt, können Sie das Video im Vollbildmodus wiedergeben, indem Sie die Option fullscreen=true am Ende des Befehls hinzufügen.

##### 5.1.1.2.2 Verwendung des IMX219 mit dem Ubuntu-Image
Bei Verwendung des offiziellen Ubuntu-Image von der [topst.ai DOCS-Seite](https://topst.ai/tech/docs?page=624bd237b3013e87c05c125b8031e2f370ccca2b) arbeitet die IMX219-Kamera standardmäßig mit einer Auflösung von 1640×1232 bei 30 fps. Daher wird für die Kamerawiedergabe in dieser Umgebung 1640×1232 bei 30 fps verwendet.  
Führen Sie die folgenden Schritte aus:
1. - Bei Verbindung über UART: Geben Sie den folgenden Befehl in der UART-Konsole ein, nachdem Sie sich mit Ihrem topst-Konto angemeldet haben
    ```
    $ export XDG_RUNTIME_DIR=/run/user/1000
    ```
    - Bei direkter Bedienung am Display: Öffnen Sie ein Terminalfenster
2. Geben Sie den Kamerastream mit einem GStreamer-Befehl wie unten gezeigt wieder. Da unter Ubuntu kein hardwarebeschleunigtes Wayland-Rendering verfügbar ist, wird stattdessen H.265-Encoding/Decoding verwendet, um die VPU-Beschleunigung für die Wiedergabe zu nutzen
    ```
    $ gst-launch-1.0 v4l2src device=/dev/video0 io-mode=2 ! video/x-raw,format=NV12,width=1600,height=1200,framerate=30/1 ! v4l2h265enc ! h265parse ! v4l2h265dec ! videoconvert ! waylandsink sync=false
    ```
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/accessories/Camera/5.8%201640x1232%20imx219%20camera%20out%20display%20on%20ubuntu.png"></p>
<p align="center"><strong>Abbildung 5.8 1640x972 IMX219 Kameraausgabe-Anzeige unter Ubuntu</strong></p>

**Hinweis:** Obwohl die Auflösung 1640×1232 beträgt, können Sie das Video im Vollbildmodus wiedergeben, indem Sie die Option fullscreen=true am Ende des Befehls hinzufügen.

Zusätzlich zu GStreamer können Sie auch OpenCV verwenden, um den Kamerastream anzuzeigen. Führen Sie die folgenden Schritte aus, um das Kamerabild mit OpenCV auf einfache Weise in der Vorschau anzuzeigen.
1. Installieren Sie OpenCV
    ```
    $ sudo apt-get install python3-opencv
    ```
2. Schreiben Sie den folgenden Code in die Datei opencv_cam.py.
    ```
    import cv2
    
    pipeline = (
        "v4l2src device=/dev/video0 io-mode=2 ! "
        "video/x-raw,format=NV12,width=1640,height=1232,framerate=30/1 ! "
        "videoconvert ! video/x-raw,format=BGR ! appsink sync=false"
    )
    
    cap = cv2.VideoCapture(pipeline, cv2.CAP_GSTREAMER)
    
    if not cap.isOpened():
        print("ERROR: cannot open camera via GStreamer")
        exit()
    
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Frame read error")
            break
    
        cv2.imshow("Camera", frame)
        if cv2.waitKey(1) == 27:
            break
    
    cap.release()
    cv2.destroyAllWindows()
    ```
3. Führen Sie opencv_cam.py mit Python aus
```
$ python3 opencv_cam.py
```
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/accessories/Camera/5.9%201640x1232%20opencv%20imx219%20camera%20out%20display.png"></p>
<p align="center"><strong>Abbildung 5.9 1640×1232 IMX219 Kameraausgabe unter Ubuntu mit OpenCV</strong></p>

##### 5.1.1.2.3 GStreamer-Pipeline-Konfiguration für jede Auflösung auf dem D3-G
Geben Sie für jede Auflösung die passenden GStreamer-Pipeline-Optionen an und starten Sie anschließend den Kamerastream.
1. 1920x1080 @ 30fps
    ```
    $ gst-launch-1.0 v4l2src device=/dev/video0 io-mode=2 ! video/x-raw,format=NV12,width=1920,height=1080,framerate=30/1 ! videoconvert ! waylandsink sync=false
    ```
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/accessories/Camera/5.10%201920x1080%20imx219%20camera%20out%20display%20on%20yocto.png"></p>
    <p align="center"><strong>Abbildung 5.10 1920x1080 IMX219 Kameraausgabe-Anzeige unter Yocto</strong></p>
2. 1640x1232 @ 30fps
    ```
    $ gst-launch-1.0 v4l2src device=/dev/video0 io-mode=2 ! video/x-raw,format=NV12,width=1640,height=1232,framerate=30/1 ! videoconvert ! waylandsink sync=false
    ```
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/accessories/Camera/5.7%201640x1232%20imx219%20camera%20out%20display%20on%20yocto.png"></p>
    <p align="center"><strong>Abbildung 5.11 1620x1232 IMX219 Kameraausgabe-Anzeige unter Yocto</strong></p>
3. 640x480 @ 30fps
    ```
    $ gst-launch-1.0 v4l2src device=/dev/video0 io-mode=2 ! video/x-raw,format=NV12,width=640,height=480,framerate=30/1 ! videoconvert ! waylandsink sync=false
    ```
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/accessories/Camera/5.12%20640x480%20imx219%20camera%20out%20display%20on%20yocto.png"></p>
    <p align="center"><strong>Abbildung 5.12 640x480 IMX219 Kameraausgabe-Anzeige unter Yocto</strong></p>

Zusätzlich können Sie eine Pipeline konfigurieren, die den H.265-Encoder und -Decoder verwendet, um eine hardwarebeschleunigte Wiedergabe zu ermöglichen.
1. 1920x1080 @ 30fps
    ```
    $ gst-launch-1.0 v4l2src device=/dev/video0 io-mode=2 ! video/x-raw,format=NV12,width=1920,height=1080,framerate=30/1 ! v4l2h265enc ! h265parse ! v4l2h265dec ! videoconvert ! waylandsink sync=false
    ```
2. 1640x1232 @ 30fps
    ```
    $ gst-launch-1.0 v4l2src device=/dev/video0 io-mode=2 ! video/x-raw,format=NV12,width=1600,height=1200,framerate=30/1 !  v4l2h265enc ! h265parse ! v4l2h265dec ! videoconvert ! waylandsink sync=false
    ```
3. 640x480 @ 30fps
    ```
    $ gst-launch-1.0 v4l2src device=/dev/video0 io-mode=2 ! video/x-raw,format=NV12,width=640,height=480,framerate=30/1 ! v4l2h265enc ! h265parse ! v4l2h265dec ! videoconvert ! waylandsink sync=false
    ```

Informationen zum Ändern der Auflösung finden Sie in Abschnitt 4.1.3.3.

#### 5.1.1.3 Benutzerhandbuch für die MIPI-CSI-Kamera auf dem AI-G (OV5647)
##### 5.1.1.3.1 Verwendung des OV5647 mit dem Yocto-Image
Auf dem AI-G stehen zwei Anwendungen zur Verfügung: eine für die Kamerawiedergabe mit Inferenzergebnissen und eine weitere für die einfache Kameraansicht. Sie können je nach Anwendungsfall eine der beiden Anwendungen wählen.
- tcnnapp
    ```
    $ tcnnapp
    ```
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/accessories/Camera/5.13%20ov5647%20camera%20out%20display%20with%20running%20tcnnapp%20on%20yocto.png"></p>
    <p align="center"><strong>Abbildung 5.13 OV5647 Kameraausgabe-Anzeige bei laufender tcnnapp unter Yocto</strong></p>
- tcnncameraapp
    ```
    $ tcnncameraapp
    ```
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/accessories/Camera/5.14%20ov5647%20camera%20out%20display%20with%20running%20tcnncameraapp%20on%20yocto.png"></p>
    <p align="center"><strong>Abbildung 5.14 OV5647 Kameraausgabe-Anzeige bei laufender tcnncameraapp unter Yocto</strong></p>

##### 5.1.1.3.2 Verwendung mit dem Ubuntu-Image
Auf dem AI-G stehen zwei Anwendungen zur Verfügung: eine für die Kamerawiedergabe mit Inferenzergebnissen und eine weitere für die einfache Kameraansicht. Sie können je nach Anwendungsfall eine der beiden Anwendungen wählen.
- tcnnapp
    ```
    $ tcnnapp
    ```
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/accessories/Camera/5.13%20ov5647%20camera%20out%20display%20with%20running%20tcnnapp%20on%20yocto.png"></p>
    <p align="center"><strong>Abbildung 5.15 OV5647 Kameraausgabe-Anzeige bei laufender tcnnapp unter Ubuntu</strong></p>
- tcnncameraapp
    ```
    $ tcnncameraapp
    ```
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/accessories/Camera/5.14%20ov5647%20camera%20out%20display%20with%20running%20tcnncameraapp%20on%20yocto.png"></p>
    <p align="center"><strong>Abbildung 5.16 OV5647 Kameraausgabe-Anzeige bei laufender tcnncameraapp unter Ubuntu</strong></p>

#### 5.1.1.4 Benutzerhandbuch für die MIPI-CSI-Kamera auf dem AI-G (IMX219)
##### 5.1.1.4.1 Verwendung des IMX219 mit dem Yocto-Image
Auf dem AI-G stehen zwei Anwendungen zur Verfügung: eine für die Kamerawiedergabe mit Inferenzergebnissen und eine weitere für die einfache Kameraansicht. Sie können je nach Anwendungsfall eine der beiden Anwendungen wählen.
- tcnnapp
    ```
    $ tcnnapp
    ```
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/accessories/Camera/5.17%20imx219%20camera%20out%20display%20with%20running%20tcnnapp%20on%20yocto.png"></p>
    <p align="center"><strong>Abbildung 5.17 OV5647 Kameraausgabe-Anzeige bei laufender tcnnapp unter Yocto</strong></p>
- tcnncameraapp
    ```
    $ tcnncameraapp
    ```
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/accessories/Camera/5.18%20imx219%20camera%20out%20display%20with%20running%20tcnncameraapp%20on%20yocto.png"></p>
    <p align="center"><strong>Abbildung 5.18 OV5647 Kameraausgabe-Anzeige bei laufender tcnncameraapp unter Yocto</strong></p>

##### 5.1.1.4.2 Verwendung des IMX219 mit dem Ubuntu-Image
Auf dem AI-G stehen zwei Anwendungen zur Verfügung: eine für die Kamerawiedergabe mit Inferenzergebnissen und eine weitere für die einfache Kameraansicht. Sie können je nach Anwendungsfall eine der beiden Anwendungen wählen.
- tcnnapp
    ```
    $ tcnnapp
    ```
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/accessories/Camera/5.17%20imx219%20camera%20out%20display%20with%20running%20tcnnapp%20on%20yocto.png"></p>
    <p align="center"><strong>Abbildung 5.17 OV5647 Kameraausgabe-Anzeige bei laufender tcnnapp unter Yocto</strong></p>
- tcnncameraapp
    ```
    $ tcnncameraapp
    ```
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/accessories/Camera/5.18%20imx219%20camera%20out%20display%20with%20running%20tcnncameraapp%20on%20yocto.png"></p>
    <p align="center"><strong>Abbildung 5.18 OV5647 Kameraausgabe-Anzeige bei laufender tcnncameraapp unter Yocto</strong></p>

### 5.1.2 Benutzerhandbuch für die GMSL-Kamera
In diesem Abschnitt wird beschrieben, wie das Video der GMSL-Kamera sowohl unter Yocto als auch unter Ubuntu angezeigt wird.

#### 5.1.2.1 Benutzerhandbuch für die GMSL-Kamera auf dem D3-G
##### 5.1.2.1.1 Verwendung der GMSL-Kamera mit dem Yocto-Image
Bei Verwendung des offiziellen Yocto-Image von der [topst.ai DOCS-Seite](https://topst.ai/tech/docs?page=624bd237b3013e87c05c125b8031e2f370ccca2b) oder eines durch manuelles Bauen von Yocto erzeugten Image arbeitet die GMSL-Kamera standardmäßig mit einer Auflösung von 1920×1080 bei 30 fps. Daher wird für die Kamerawiedergabe in dieser Umgebung 1920×1080 bei 30 fps verwendet.  
Führen Sie die folgenden Schritte aus:
1. Beenden Sie den aktuell laufenden Dienst topst-welcome
    ```
    $ sudo systemctl stop topst-welcome
    ```
2. Geben Sie den folgenden Befehl in der UART-Konsole ein
    ```
    $ export XDG_RUNTIME_DIR=/run/user/root
    ```
3. Geben Sie den Kamerastream mit einem GStreamer-Befehl wie unten gezeigt wieder
    ```
    $ gst-launch-1.0 v4l2src device=/dev/video4 io-mode=2 ! video/x-raw,format=NV12,width=1920,height=1080,framerate=30/1 ! videoconvert ! waylandsink sync=false
    ```

Zusätzlich können Sie durch Ausführen des unten stehenden Skripts die Kamerabilder mithilfe der gpu in einer vierfach geteilten Ansicht anzeigen.
```
#/bin/bash
 
set -euo pipefail
 
export GST_GL_WINDOW=wayland
export GST_GL_API=gles2
# glimagesink force-aspect-ratio=false sync=false \
 
gst-launch-1.0 -v \
  glvideomixer name=m background=black \
    sink_0::xpos=0   sink_0::ypos=0 \
    sink_1::xpos=960 sink_1::ypos=0 \
    sink_2::xpos=0   sink_2::ypos=540 \
    sink_3::xpos=960 sink_3::ypos=540 ! \
    "video/x-raw,format=RGBA,width=1920,height=1080,framerate=30/1" ! \
  waylandsink sync=false \
  v4l2src device=/dev/video4 io-mode=4 ! \
    video/x-raw,format=NV12,width=1920,height=1080,framerate=30/1 ! \
    glupload ! \
    glcolorscale ! "video/x-raw(memory:GLMemory),width=960,height=540" ! \
    m.sink_0 \
  \
  v4l2src device=/dev/video5 io-mode=4 ! \
    video/x-raw,format=NV12,width=1920,height=1080,framerate=30/1 ! \
    glupload ! \
    glcolorscale ! "video/x-raw(memory:GLMemory),width=960,height=540" ! \
    m.sink_1 \
  \
  v4l2src device=/dev/video6 io-mode=4 ! \
    video/x-raw,format=NV12,width=1920,height=1080,framerate=30/1 ! \
    glupload ! \
    glcolorscale ! "video/x-raw(memory:GLMemory),width=960,height=540" ! \
    m.sink_2 \
  \
  v4l2src device=/dev/video7 io-mode=4 ! \
    video/x-raw,format=NV12,width=1920,height=1080,framerate=30/1 ! \
    glupload ! \
    glcolorscale ! "video/x-raw(memory:GLMemory),width=960,height=540" ! \
    m.sink_3
```

GMSL-Kameras erscheinen als video4, video5, video6 und video7, und Sie können bei Bedarf eines dieser Geräte auswählen.  
Wenn acht Kameras angeschlossen sind, zählt das System sie als video0 bis video8 auf, sodass Sie einen beliebigen dieser Geräteknoten auswählen können.

##### 5.1.2.1.2 Verwendung der GMSL-Kamera mit dem Ubuntu-Image
Bei Verwendung des offiziellen Ubuntu-Image von der [topst.ai DOCS-Seite](https://topst.ai/tech/docs?page=624bd237b3013e87c05c125b8031e2f370ccca2b) arbeitet die GMSL-Kamera standardmäßig mit einer Auflösung von 1920×1080 bei 30 fps. Daher wird für die Kamerawiedergabe in dieser Umgebung 1920×1080 bei 30 fps verwendet.  
Führen Sie die folgenden Schritte aus:
1. - Bei Verbindung über UART: Geben Sie den folgenden Befehl in der UART-Konsole ein, nachdem Sie sich mit Ihrem topst-Konto angemeldet haben
    ```
    $ export XDG_RUNTIME_DIR=/run/user/1000
    ```
    - Bei direkter Bedienung am Display: Öffnen Sie ein Terminalfenster
2. Geben Sie den Kamerastream mit einem GStreamer-Befehl wie unten gezeigt wieder. Da unter Ubuntu kein hardwarebeschleunigtes Wayland-Rendering verfügbar ist, wird stattdessen H.265-Encoding/Decoding verwendet, um die VPU-Beschleunigung für die Wiedergabe zu nutzen
    ```
    $ gst-launch-1.0 v4l2src device=/dev/video0 io-mode=2 ! video/x-raw,format=NV12,width=1920,height=1080,framerate=30/1 ! v4l2h265enc ! h265parse ! v4l2h265dec ! videoconvert ! waylandsink sync=false
    ```

Zusätzlich können Sie durch Ausführen des unten stehenden Skripts die Kamerabilder mithilfe der gpu in einer vierfach geteilten Ansicht anzeigen.
```
#/bin/bash

set -euo pipefail

export GST_GL_WINDOW=wayland
export GST_GL_API=gles2

gst-launch-1.0 -v \
  glvideomixer name=m background=black \
    sink_0::xpos=0   sink_0::ypos=0 \
    sink_1::xpos=960 sink_1::ypos=0 \
    sink_2::xpos=0   sink_2::ypos=540 \
    sink_3::xpos=960 sink_3::ypos=540 ! \
    glcolorconvert ! "video/x-raw(memory:GLMemory),format=RGBA,width=1920,height=1080,framerate=30/1,pixel-aspect-ratio=1/1" ! \
  glimagesink force-aspect-ratio=false sync=false \
  \
  v4l2src device=/dev/video4 io-mode=4 ! video/x-raw,format=NV12,framerate=30/1,pixel-aspect-ratio=1/1 ! \
    videoconvert ! glupload ! glcolorscale ! \
    "video/x-raw(memory:GLMemory),format=RGBA,width=960,height=540,pixel-aspect-ratio=1/1" ! m.sink_0 \
  \
  v4l2src device=/dev/video5 io-mode=4 ! video/x-raw,format=NV12,framerate=30/1,pixel-aspect-ratio=1/1 ! \
    videoconvert ! glupload ! glcolorscale ! \
    "video/x-raw(memory:GLMemory),format=RGBA,width=960,height=540,pixel-aspect-ratio=1/1" ! m.sink_1 \
  \
  v4l2src device=/dev/video6 io-mode=4 ! video/x-raw,format=NV12,framerate=30/1,pixel-aspect-ratio=1/1 ! \
    videoconvert ! glupload ! glcolorscale ! \
    "video/x-raw(memory:GLMemory),format=RGBA,width=960,height=540,pixel-aspect-ratio=1/1" ! m.sink_2 \
  \
  v4l2src device=/dev/video7 io-mode=4 ! video/x-raw,format=NV12,framerate=30/1,pixel-aspect-ratio=1/1 ! \
    videoconvert ! glupload ! glcolorscale ! \
    "video/x-raw(memory:GLMemory),format=RGBA,width=960,height=540,pixel-aspect-ratio=1/1" ! m.sink_3
```

Darüber hinaus können Sie auch OpenCV verwenden, um den Kamerastream anzuzeigen. Führen Sie die folgenden Schritte aus, um das Kamerabild mit OpenCV auf einfache Weise in der Vorschau anzuzeigen.
1. Installieren Sie OpenCV
    ```
    $ sudo apt-get install python3-opencv
    ```
2. Schreiben Sie den folgenden Code in die Datei opencv_cam.py
    ```
    import cv2
    
    pipeline = (
        "v4l2src device=/dev/video4 io-mode=2 ! "
        "video/x-raw,format=NV12,width=1920,height=1080,framerate=30/1 ! "
        "videoconvert ! video/x-raw,format=BGR ! appsink sync=false"
    )
    
    cap = cv2.VideoCapture(pipeline, cv2.CAP_GSTREAMER)
    
    if not cap.isOpened():
        print("ERROR: cannot open camera via GStreamer")
        exit()
    
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Frame read error")
            break
    
        cv2.imshow("Camera", frame)
        if cv2.waitKey(1) == 27:
            break
    
    cap.release()
    cv2.destroyAllWindows()
    ```
3. Führen Sie die Datei opencv_cam.py mit Python aus
    ```
    $ python3 opencv_cam.py
    ```

GMSL-Kameras erscheinen als video4, video5, video6 und video7, und Sie können bei Bedarf eines dieser Geräte auswählen.  
Wenn acht Kameras angeschlossen sind, zählt das System sie als video0 bis video8 auf, sodass Sie einen beliebigen dieser Geräteknoten auswählen können.

#### 5.1.2.2 Benutzerhandbuch für die GMSL-Kamera auf dem AI-G
##### 5.1.2.2.1 Verwendung der GMSL-Kamera mit dem Yocto-Image
Auf dem AI-G stehen zwei Anwendungen zur Verfügung: eine für die Kamerawiedergabe mit Inferenzergebnissen und eine weitere für die einfache Kameraansicht. Sie können je nach Anwendungsfall eine der beiden Anwendungen wählen.
- tcnnapp
- tcnncameraapp

GMSL-Kameras erscheinen als **video0**, **video1** und **video2**, und Sie können bei Bedarf eines dieser Geräte auswählen.
Jede Anwendung verwendet standardmäßig video2, Sie können das Videogerät jedoch mit der **-p-Option** ändern.
Das folgende Beispiel zeigt, wie **video0** ausgewählt wird.

- tcnnapp
    ```
    $ tcnnapp -p /dev/video0
    ```
- tcnncameraapp
    ```
    $ tcnncameraapp -p /dev/video0
    ```

##### 5.1.2.2.2 Verwendung der GMSL-Kamera mit dem Ubuntu-Image
Auf dem AI-G stehen zwei Anwendungen zur Verfügung: eine für die Kamerawiedergabe mit Inferenzergebnissen und eine weitere für die einfache Kameraansicht. Sie können je nach Anwendungsfall eine der beiden Anwendungen wählen.
- tcnnapp
- tcnncameraapp

GMSL-Kameras erscheinen als **video0**, **video1** und **video2**, und Sie können bei Bedarf eines dieser Geräte auswählen.
Jede Anwendung verwendet standardmäßig video2, Sie können das Videogerät jedoch mit der **-p-Option** ändern.
Das folgende Beispiel zeigt, wie **video0** ausgewählt wird.

- tcnnapp
    ```
    $ tcnnapp -p /dev/video0
    ```
- tcnncameraapp
    ```
    $ tcnncameraapp -p /dev/video0
    ```

### 5.1.3 Benutzerhandbuch für die USB-Kamera
In diesem Abschnitt wird beschrieben, wie das Video der USB-Kamera sowohl unter Yocto als auch unter Ubuntu angezeigt wird.
Das AI-G verfügt über keine USB-Schnittstelle; daher wird für diese Plattform keine Anleitung für USB-Kameras bereitgestellt.

#### 5.1.3.1 Benutzerhandbuch für die USB-Kamera auf dem D3-G
In diesem Dokument basieren die Erläuterungen auf einer USB-Kamera, die 1920×1080 bei 30 fps unterstützt

**Hinweis:** Da der MIPI-Kamera standardmäßig **/dev/video0** zugewiesen ist, wird die USB-Kamera als /dev/video1 erstellt.
Stellen Sie sicher, dass Sie beim Betrieb der USB-Kamera **/dev/video1** verwenden.

##### 5.1.3.1.1 Verwendung der USB-Kamera mit dem Yocto-Image
Bei Verwendung des offiziellen Yocto-Image von der [topst.ai DOCS-Seite](https://topst.ai/tech/docs?page=624bd237b3013e87c05c125b8031e2f370ccca2b) oder eines durch manuelles Bauen von Yocto erzeugten Image arbeitet die USB-Kamera mit der Auflösung und der Bildrate, die durch die eigenen Spezifikationen der Kamera festgelegt sind. Daher wird das Video mit der von der USB-Kamera bereitgestellten Standardauflösung und Standard-FPS wiedergegeben.  
Führen Sie die folgenden Schritte aus:
1. Beenden Sie den aktuell laufenden Dienst topst-welcome
    ```
    $ sudo systemctl stop topst-welcome
    ```
2. Geben Sie den folgenden Befehl in der UART-Konsole ein
    ```
    $ export XDG_RUNTIME_DIR=/run/user/root
    ```
3. Geben Sie den Kamerastream mit einem GStreamer-Befehl wie unten gezeigt wieder. Beim Prüfen der USB-Kamerainformationen mit v4l2-ctl -d /dev/video1 --list-formats-ext wird MJPEG als unterstütztes Format angezeigt. Daher wird jpegdec verwendet
    ```
    $ gst-launch-1.0 v4l2src device=/dev/video1 ! image/jpeg,width=1920,height=1080 ! jpegdec ! videoconvert ! waylandsink
    ```

##### 5.1.3.1.2 Verwendung der USB-Kamera mit dem Ubuntu-Image
Bei Verwendung des offiziellen Ubuntu-Image von der [topst.ai DOCS-Seite](https://topst.ai/tech/docs?page=624bd237b3013e87c05c125b8031e2f370ccca2b) oder eines manuell erzeugten Image arbeitet die USB-Kamera mit der Auflösung und der Bildrate, die durch die eigenen Spezifikationen der Kamera festgelegt sind. Daher wird das Video mit der von der USB-Kamera bereitgestellten Standardauflösung und Standard-FPS wiedergegeben.  
Führen Sie die folgenden Schritte aus:
1. - Bei Verbindung über UART: Geben Sie den folgenden Befehl in der UART-Konsole ein, nachdem Sie sich mit Ihrem topst-Konto angemeldet haben
    ```
    $ export XDG_RUNTIME_DIR=/run/user/1000
    ```
    - Bei direkter Bedienung am Display: Öffnen Sie ein Terminalfenster
2. Geben Sie den Kamerastream mit einem GStreamer-Befehl wie unten gezeigt wieder. Beim Prüfen der USB-Kamerainformationen mit v4l2-ctl -d /dev/video1 --list-formats-ext wird MJPEG als unterstütztes Format angezeigt. Daher wird jpegdec verwendet
    ```
    $ gst-launch-1.0 v4l2src device=/dev/video1 ! image/jpeg,width=1920,height=1080 ! jpegdec ! videoconvert ! waylandsink
    ```
3. Um H.265-Encoding und -Decoding zu verwenden, muss das Video in das NV12-Format konvertiert werden, das von v4l2src unterstützt wird. Daher sollte die Pipeline wie unten gezeigt konfiguriert werden
    ```
    $ gst-launch-1.0 v4l2src device=/dev/video1 io-mode=2 ! image/jpeg,width=640,height=480,framerate=30/1 ! jpegdec ! videoconvert ! video/x-raw,format=NV12 !  v4l2h265enc ! h265parse ! v4l2h265dec ! videoconvert ! waylandsink
    ```

**Hinweis:** Sie können das Video im Vollbildmodus wiedergeben, indem Sie die Option fullscreen=true am Ende des Befehls hinzufügen.

Zusätzlich zu GStreamer können Sie auch OpenCV verwenden, um den Kamerastream anzuzeigen. Führen Sie die folgenden Schritte aus, um das Kamerabild mit OpenCV auf einfache Weise in der Vorschau anzuzeigen.
1. Installieren Sie OpenCV
    ```
    $ sudo apt-get install python3-opencv
    ```
2. Schreiben Sie den folgenden Code in die Datei opencv_cam.py
    ```
    import cv2

    cap = cv2.VideoCapture(1)

    if not cap.isOpened():
        print("\\@@ Camera open failed!")
        exit()

    print("Press 'q' to exit the camera window.")

    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Failed to read frame")
            break

        cv2.imshow("Camera Feed", frame)

        # pressed 'q' key, escape
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
    ```
3. Führen Sie opencv_cam.py mit Python aus
    ```
    $ python3 opencv_cam.py
    ```

The USB camera used in this guide operates over USB 2.0, which imposes bandwidth limitations. As a result, higher-resolution video capture is not supported when using OpenCV. If higher resolutions are required, it is recommended to use a USB 3.0 camera, which provides sufficient bandwidth for high-definition video streams.  
Alternatively, OpenCV can be used with higher resolutions by constructing the capture pipeline through GStreamer, as shown below.
1. Write the following code inside the gstreamer_opencv_cam.py file
    ```
    import cv2

    pipeline = (
        "v4l2src device=/dev/video1 ! "
        "image/jpeg,width=1920,height=1080,framerate=30/1 ! "
        "jpegdec ! videoconvert ! video/x-raw,format=BGR ! "
        "appsink drop=1 max-buffers=2"
    )

    print("Opening pipeline...")
    cap = cv2.VideoCapture(pipeline, cv2.CAP_GSTREAMER)

    if not cap.isOpened():
        print("Failed to open pipeline")
        exit()

    print("Press 'q' to exit the camera window.")

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Failed to read frame")
            break

        cv2.imshow("USB Camera 1080p MJPG", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
    ```
2. Run gstreamer_opencv_cam.py with Python
    ```
    $ python3 gstreamer_opencv_cam.py
    ```

# 6. Fehlerbehebung
Kapitel 6 behandelt die Fehlerbehebung für MIPI-CSI-Kameras, GMSL-Kameras und USB-Kameras.

## 6.1 Fehlerbehebung für MIPI-CSI- und GMSL-Kameras
Wenn Probleme mit MIPI-CSI- oder GMSL-Kameras auftreten, finden Sie in der nachfolgenden Debugging-Anleitung Hinweise zur Behebung des Problems.

### 6.1.1 Probleme beim Booten (Probe-Phase)
#### 6.1.1.1 Sensor-Probe fehlgeschlagen
**Symptome**
- Der Sensor wird beim Booten nicht erkannt
- /dev/videoX-Knoten werden nicht erstellt
- Die Sensor-Entität erscheint nicht in der Ausgabe von ‘media-ctrl -p’  

**Beispielhafte dmesg-Logs**
```
[    3.421000] imx219 2-0010: probing sensor failed
[    3.421120] imx219 2-0010: i2c read failed: addr=0x3000, ret=-5
[    3.200400] imx219 0-0010: reset gpio request failed
[    2.912830] imx219 1-0010: failed to get vddio regulator
```
**Mögliche Ursachen**
- Falsche I2C-Adresse oder falsche Bus-Konfiguration
- Falsche Polarität für RESET/PWDN-GPIO
- Fehlende oder falsch konfigurierte Regler-Stromversorgungen

**Lösung**
- Überprüfen Sie die I2C-Adresse, die Busnummer und die GPIO-Einstellungen im Device Tree
- Prüfen Sie auf fehlende oder falsch definierte Regler-Knoten
- Überprüfen Sie erneut die Kabelausrichtung und die Pin-Ausrichtung des Sensormoduls

#### 6.1.1.2 I2C-Kommunikationsfehler
**Beispielhafte dmesg-Logs**
```
[    3.101001] imx219 2-0010: i2c read error: -121
[    4.112121] i2c i2c-2: transfer failed: -110
```
**Mögliche Ursachen**
- SDA/SCL-Leitungen sind kurzgeschlossen oder unterbrochen
- Die I2C-Busnummer im Device Tree stimmt nicht mit der tatsächlichen Hardware-Konfiguration überein

**Lösung**
- Verwenden Sie “i2cdetect -y <bus>”, um zu prüfen, ob der Sensor unter der erwarteten I2C-Adresse antwortet
- Untersuchen Sie Kabel und Anschluss auf Beschädigungen, falschen Sitz oder lose Kontakte

### 6.1.2 Probleme mit Media Controller und Graph-Konfiguration
(überprüft mit ‘media-ctl -p’)

#### 6.1.2.1 Fehlende Sensor-Entität oder nicht konfigurierte Links
**Beispielausgabe von 'media-ctl -p'**
```
0 entities, 0 interfaces, 0 pads, 0 links
```
**Mögliche Ursachen**
- Fehlender Endpoint-Knoten (Port) im Device Tree
- Falsche Lane-Anzahl oder falsche ‘bus-type’-Einstellungen
- Fehlender ‘link-frequencies’-Eintrag

**Lösung**
- Überprüfen Sie die Richtigkeit der ‘port@0/1’-Endpoint-Definitionen
- Prüfen Sie das ‘data-lanes’-Array auf die korrekte Reihenfolge und Anzahl der Lanes
- Stellen Sie sicher, dass ‘link-frequencies’ mit den Spezifikationen des Sensors übereinstimmt

#### 6.1.2.2 Format-/Modus-Abweichung
**Mögliche Ursachen**
- Der Eintrag ‘supported_mode[]’ im Sensortreiber stimmt nicht mit dem in der DTS definierten Wert ‘hs-settle’ überein
- Abweichung bei der Anzahl der CSI-2-Lanes zwischen Treiber und Device Tree

**Lösung**
- Überprüfen Sie die Auflösung, die Pixelrate und die HTS/VTS-Werte in ‘supported_modes[]’ und passen Sie anschließend den Wert ‘hs-settle’ in der DTS entsprechend an
- Stellen Sie die Konsistenz zwischen der DTS-Konfiguration und den Einstellungen des Sensortreibers sicher

### 6.1.3 Probleme beim V4L2-Streaming
#### 6.1.3.1 VIDIOC_STREAMON-Fehler (Streaming kann nicht gestartet werden)
**Mögliche Ursachen**
- Falsche Konfiguration der Sensorregister
- Pixelrate oder PLL-Einstellungen stimmen nicht mit den erwarteten Werten überein
- HTS/VTS-Konflikte, die ein ungültiges Frame-Timing verursachen

**Lösung**
- Überprüfen Sie die Werte für Pixelrate, VTS und HTS in der Modus-Tabelle des Sensors erneut
- Prüfen Sie die PLL-Teiler (0x030x-Register) auf Richtigkeit
- Stellen Sie sicher, dass der Device Tree den korrekten Wert ‘hs-settle’ für die gewählte Auflösung und FPS angibt.

#### 6.1.3.2 Anforderung eines nicht unterstützten Formats
**Lösung**
- Prüfen Sie mit dem unten stehenden Befehl die tatsächlich unterstützten Formate und starten Sie das Streaming anschließend erneut mit einem unterstützten Format:
    ```
    V4l2-ctl –list-formats-ext
    ```

### 6.1.4 CSI-2-Fehler: SoT, CRC und verwandte Probleme
#### 6.1.4.1 SoT-Fehler (Sync on Transmission)
**Mögliche Ursachen**
- Abweichung in der MIPI-Timing-Konfiguration
- Pixelrate zu hoch eingestellt
- Schlechte Kabelqualität oder zu große Kabellänge

**Lösung**
- Verringern Sie die Pixelrate oder die Link-Frequenz
- Tauschen Sie das Kabel aus oder verkürzen Sie seine Länge
- Überprüfen Sie die MIPI-Timing-Parameter

#### 6.1.4.2 CRC-Fehler
**Beispielhafte dmesg-Logs**
```
[   13.700910] tccvin videoinput0: CSI-2 ERROR: CRC error
```
**Mögliche Ursachen**
- Verschlechterte MIPI-Signalqualität
- Abweichung bei PLL oder Lane-Geschwindigkeit

**Lösung**
- Passen Sie den Wert hs-settle an
- Tauschen Sie das Kabel aus
- Überprüfen Sie die PLL-Konfiguration und die Einstellungen der Lane-Geschwindigkeit

### 6.1.5 Fehler bei Pixelrate / Link-Frequenz
**Mögliche Ursachen**
- Überschreitung der verfügbaren CSI-2-Lane-Bandbreite
- Falsche PLL-Konfiguration

**Lösung**
- Berechnen Sie die Pixelrate neu und stellen Sie sicher, dass sie innerhalb der zulässigen CSI-2-Bandbreite liegt
- Passen Sie die PLL-Teiler an, um ein gültiges Timing zu erreichen
- Verringern Sie bei Bedarf die Bildrate (z. B. 30 -> 15fps) oder reduzieren Sie die Auflösung

### 6.1.6 Konfigurationsfehler im Device Tree (DTS)
#### 6.1.6.1 Inkompatibler compatible-String
**Mögliche Ursachen**
- Der Wert ‘compatible’ in der DTS stimmt nicht mit der im Sensortreiber definierten ‘of_device_id’ überein
- Der Treiber erkennt den Geräteknoten nicht, wodurch die Ausführung des Probe verhindert wird

**Lösung**
- Aktualisieren Sie die DTS mit dem exakten ‘compatible’-String, der im Sensortreiber definiert ist (z. B. “sony,imx219”)
- Erstellen Sie den Device Tree neu und überprüfen Sie, ob der Sensor korrekt erkannt wird

#### 6.1.6.2 Probleme bei der Endpoint-Konfiguration
**Mögliche Ursachen**
- Die Portnummern oder die ‘remote-endpoint’-Verweise stimmen zwischen dem Sensor-Endpoint und dem CSI-Endpoint nicht überein
- ‘data-lanes’ oder die Bus-Konfiguration erfüllt nicht die Anforderungen des Media-Graphen

**Lösung**
- Stellen Sie sicher, dass die Portnummern sowie die Werte ‘data-lanes’ und ‘remote-endpoint’ auf beiden Seiten übereinstimmen
- Verwenden Sie ‘media-ctl -p’, um zu überprüfen, ob die Media-Links korrekt hergestellt sind

#### Fehlende Eigenschaft Link-Frequencies
**Mögliche Ursachen**
- Das Feld ‘link-frequencies’ fehlt im Endpoint, wodurch die MIPI-Link-Geschwindigkeit nicht berechnet werden kann
- Das Format des Wertes (z. B. /bits/ 64) entspricht nicht dem, was der Treiber erwartet

**Lösung**
- Fügen Sie den korrekten Wert ‘link-frequencies’ (z. B. 456000000) entsprechend der Sensorspezifikation hinzu
- Stellen Sie sicher, dass das Format des Wertes den Anforderungen des Treibers entspricht (etwa einschließlich /bits/ 64, falls erforderlich)

### 6.1.7 Probleme bei der Gstreamer-Wiedergabe
#### 6.1.7.1 Fehler 'not negotiated'
**Mögliche Ursachen**
- Fehlgeschlagene Caps-Aushandlung innerhalb der Pipeline
- Formatabweichung beim Wayland-Compositor
- Videoconvert kann bestimmte Raw-Formate nicht verarbeiten

**Lösung**
- Verwenden Sie Pipelines auf Basis von NV12 oder YUY2, die eine breite Kompatibilität bieten
- Nutzen Sie ‘v4l2src io-mode=dmabuf’, um eine Zero-Copy-Pufferverarbeitung und eine korrekte Formataushandlung sicherzustellen

#### 6.1.7.2 Fehler bei der Initialisierung des Wayland-Sinks
**Mögliche Ursachen**
- Der Wayland-Compositor läuft nicht, oder es ist keine zugängliche Display-Umgebung verfügbar
- Die Pipeline wird über SSH oder mit einer ungültigen DISPLAY-/Wayland-Umgebung gestartet, wodurch die Initialisierung des Sinks verhindert wird

**Lösung**
- Überprüfen Sie, ob der Weston-Compositor läuft
- Führen Sie die Pipeline innerhalb einer lokalen Sitzung oder einer korrekt konfigurierten Wayland-Umgebung aus

### 6.1.8 Hardware-Probleme
#### 6.1.8.1 Falsche Kabelausrichtung
**Mögliche Ursachen**
- Das FFC-Kabel ist in der falschen Ausrichtung angeschlossen oder seine Pins sind falsch ausgerichtet, wodurch eine ordnungsgemäße I2C-/MIPI-Signalübertragung verhindert wird
- Der Sensor reagiert überhaupt nicht, sodass keine Frames empfangen werden

**Lösung**
- Überprüfen Sie die Ausrichtung des Anschlusses und stellen Sie sicher, dass die Kontaktpins gemäß der Spezifikation ausgerichtet sind
- Prüfen Sie das Kabel auf Beschädigungen oder abgenutzte Kontakte

#### 6.1.8.2 Probleme mit der Stromversorgung
**Mögliche Ursachen**
- Die Versorgungsspannungen des Sensors (z. B. 1.2V / 2.8V) sind instabil oder nicht aktiviert
- Der Power-Enable-GPIO wird nicht angesteuert
- Die Einschaltsequenz des Sensors wird während der Initialisierung nicht eingehalten

**Lösung**
- Überprüfen Sie die Regler- und GPIO-Konfigurationen in der DTS und stellen Sie sicher, dass alle erforderlichen Spannungen korrekt bereitgestellt werden
- Stellen Sie sicher, dass die Anforderungen an die Einschaltsequenz des Sensors erfüllt sind (RESET _> PWDN -> clock enable)

## 6.2 Fehlerbehebung bei USB-Kameras
Wenn bei der USB-Kamera Probleme auftreten, finden Sie in der folgenden Debugging-Anleitung Hinweise zur Fehlerbehebung.

### 6.2.1 Kamera wird nicht erkannt (USB-Gerät nicht erkannt)
**Beispielhafte dmesg-Logs**
```
usb 1-1: device descriptor read/64, error -71
uvcvideo: Failed to initialize the device
```
**Mögliche Ursachen**
- Unzureichende USB-Stromversorgung oder instabile Spannungsversorgung, wodurch die Initialisierung des Geräts fehlschlägt
- Defektes USB-Kabel oder defekter USB-Anschluss oder Verwendung eines inkompatiblen USB-Hubs

**Lösung**
- Verwenden Sie einen anderen USB-Anschluss oder einen Anschluss mit stabiler Stromversorgung
- Tauschen Sie das USB-Kabel oder den USB-Hub aus und schließen Sie das Gerät erneut an, um eine korrekte Enumeration sicherzustellen

### 6.2.2 Eingeschränkte oder leere Formatliste in v4l2-ctl
**Beispielhafte dmesg-Logs**
```
uvcvideo: Failed to query (GET_DEF) UVC control 2 on unit 1: -32
```
**Mögliche Ursachen**
- Die Kamera unterstützt bestimmte UVC-Steuerelemente nicht oder meldet sie während der Initialisierung nicht
- Protokollfehler zwischen Gerät und Treiber verhindern die Erkennung der Fähigkeiten

**Lösung**
- Testen Sie mit Standardformaten wie MJPEG oder YUYV
- Testen Sie mit einer anderen Kamera desselben Modells, um festzustellen, ob das Problem mit der UVC-Kompatibilität zusammenhängt

### 6.2.3 GStreamer-Wiedergabe: "not negotiated" oder Caps-Konflikt
**Mögliche Ursachen**
- Die Pipeline fordert ein Format an, das die Kamera nicht unterstützt (z. B. NV12, YUY2), wodurch die Caps-Aushandlung fehlschlägt
- Bei der gewählten Auflösung/Bildrate liefert die Kamera möglicherweise nur MJPEG, die Pipeline fordert jedoch ein Rohformat an
- Die Kamera gibt MJPEG aus, es ist jedoch kein JPEG-Decoder-Element (jpegdec oder avdec_mjpeg) enthalten, sodass die Dekodierung nicht möglich ist

**Lösung**
- Prüfen Sie die unterstützten Formate
    ```
    v4l2-ctl –list-formats-ext
    ```
- Wenn die Kamera MJPEG ausgibt:
    ```
    v4l2src ! image/jpeg ! jpegdec ! videoconvert ! …
    ```
- Wenn die Kamera Rohformate (z. B. YUYV) unterstützt, konfigurieren Sie die Pipeline-Caps entsprechend:  
    Verwenden Sie das Rohformat genau so, wie es in ‘v4l2-ctl –list-formats-ext’ aufgeführt ist

### 6.2.4 Fehler beim Einstellen von Auflösung oder FPS
**Mögliche Ursachen**
- Die angeforderte Auflösung oder Bildrate wird von der Kamera nicht unterstützt, wodurch die Aushandlung fehlschlägt

**Lösung**
- Prüfen Sie die unterstützten Kombinationen aus Auflösung und FPS mit ‘v4l2-ctl –list-formats-ext’

### 6.2.5 Ruckelndes Video / Bildaussetzer
**Mögliche Ursachen**
- Unzureichende USB-Bandbreite (gemeinsam genutzter Hub oder Verwendung eines USB 2.0-Anschlusses)
- Hohe CPU-Last durch die MJPEG-Dekodierung, wodurch die Pipeline zurückfällt

**Lösung**
- Verwenden Sie einen USB 3.0-Anschluss oder schließen Sie die Kamera direkt ohne Hub an
- Verringern Sie die MJPEG-Auflösung oder die Bildrate oder wechseln Sie zu einem Rohformat, sofern dies unterstützt wird

### 6.2.6 Falsche Farben oder fehlerhafte Ausgabe
**Mögliche Ursachen**
- Fehler bei der Konvertierung von MJPEG -> NV12 oder bei der Farbraumkonvertierung
- Bestimmte Formatkombinationen können in v4l2convert oder videoconvert fehlschlagen

**Lösung**
- Fügen Sie jpegdec oder avdec_mjpeg explizit vor videoconvert ein
- Vereinfachen Sie die Pipeline zu Testzwecken, zum Beispiel:
    ```
    V4l2src ! jpegdec ! videoconvert ! waylandsink
    ```

### 6.2.7 Unerwartete Trennung des Geräts oder erneute Enumeration
**Beispielhafte dmesg-Logs**
```
usb 1-1: USB disconnect, device number 4
```
**Mögliche Ursachen**
- Instabile Stromversorgung oder schlechter Kabelkontakt
- Thermische Probleme, die bei längerem Betrieb zu einem Reset des Geräts führen

**Lösung**
- Tauschen Sie das USB-Kabel aus oder verwenden Sie einen Anschluss mit stabiler und ausreichender Stromversorgung
- Ziehen Sie bei Kameras mit starker Wärmeentwicklung zusätzliche Kühlmaßnahmen in Betracht
