# TOPST Imager Benutzerhandbuch

TOPST Imager installiert ein Betriebssystem oder eine Firmware auf einem TOPST-Board. Programmier- oder Elektronikkenntnisse sind nicht erforderlich. Lassen Sie diese Anleitung geöffnet und folgen Sie einem Bildschirm nach dem anderen.

> **Wichtig:** Beim Flashen können alle Daten im eMMC des Boards gelöscht werden. Sichern Sie vor dem Start alle benötigten Dateien.

> **Zu den Bildschirmaufnahmen:** Rote Rahmen und nummerierte Kreise wurden nur für diese Anleitung ergänzt. In TOPST Imager erscheinen sie nicht. Die Bilder zeigen das helle Windows-Design; Linux und das dunkle Design funktionieren genauso.

## 1. Begriffe auf dem Bildschirm

| Begriff | Einfache Erklärung |
| --- | --- |
| Board / Device | Das TOPST-Produkt, auf dem das Image installiert wird. |
| Image | Eine Datei mit einem Betriebssystem oder einer Firmware. |
| Flashing | Das Schreiben des ausgewählten Images auf das Board. |
| Firmware Download Mode / Boot Mode | Ein besonderer Board-Zustand zum Flashen. |
| FWDN | Das Werkzeug, das TOPST Imager im Hintergrund ausführt. Sie starten es nicht selbst. |
| COM port | Die USB-Seriellverbindung für AI-G und VCP-G. Linux zeigt sie als `/dev/ttyUSB...` oder `/dev/ttyACM...` an. |
| eMMC | Der eingebaute Speicher des Boards. |

## 2. Unterstützte Boards

| Board | Eigenes Image | Verbindungen beim Flashen |
| --- | --- | --- |
| TOPST D3-G | `.fai` | Board-Stromversorgung und FWDN-USB-Type-C-Datenkabel |
| TOPST AI-G | `.fai` | Board-Stromversorgung, FWDN-USB-Type-C-Datenkabel und Ethernet-Kabel |
| TOPST VCP-G | `.rom` | Board-Stromversorgung und FWDN-USB-Type-C-Datenkabel |

Verwenden Sie ein USB-Type-C-Kabel mit **Datenübertragung**. Ein reines Ladekabel funktioniert nicht.

## 3. Vorbereitung

- Das richtige TOPST-Board und sein Netzteil
- Ein USB-Type-C-Datenkabel
- Für AI-G ein Ethernet-Kabel
- Für offizielle Images einen Computer mit Internetverbindung
- Genügend Speicher für den komprimierten Download und das entpackte Paket
- Eine Sicherung wichtiger Board-Daten

Während des Flashens:

- Schalten Sie Board und Computer nicht aus.
- Trennen Sie weder USB noch Ethernet.
- Schließen Sie TOPST Imager nicht.
- Lassen Sie den Computer nicht in den Energiesparmodus wechseln.

## 4. Anwendungsoptionen

Wählen Sie unten links im Hauptfenster **App-Optionen**.

![Anwendungsoptionen von TOPST Imager](https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/Quick%20Guide/TOPST%20Imager/de/TOPST%20Imager%20App%20Options.png)

1. **Sprache:** Die Anzeige wechselt sofort zur Vorschau in die gewählte Sprache.
2. **TOPST Imager Benutzerhandbuch:** Öffnet dieses Handbuch im Webbrowser.
3. **Community fragen:** Öffnet die [TOPST-Community](https://community.topst.ai/).
4. **Speichern:** Speichert die Sprache. **Abbrechen**, die Taste `Esc` oder ein Klick außerhalb des Fensters stellt die zuvor aktive Sprache wieder her.

Unterstützt werden Koreanisch, Englisch, Japanisch, vereinfachtes und traditionelles Chinesisch, Thai und Deutsch. Die helle oder dunkle Darstellung folgt automatisch dem Betriebssystemdesign.

---

# Windows

## 1. TOPST Imager installieren

### 1.1 Voraussetzungen

- Windows 10, 64 Bit, oder neuer
- Windows 11, 64 Bit

### 1.2 Installation

Der Installer unterstützt Koreanisch und Englisch. **Install** und **Launch TOPST Imager now** unten entsprechen dem englischen Installer.

1. Laden Sie den offiziellen Windows-Installer für TOPST Imager herunter.
2. Doppelklicken Sie darauf.
3. Lesen und akzeptieren Sie die Lizenzvereinbarung.
4. Wählen Sie **Install**.
5. Wählen Sie nach Abschluss **Launch TOPST Imager now**.

Beim Start von TOPST Imager oder des VTC-Installers kann Windows Administratorrechte anfordern. Prüfen Sie vor **Ja**, ob die Datei aus der offiziellen TOPST-Distribution stammt.

## 2. Board, Betriebssystem und Version auswählen

### 2.1 Board auswählen

![Ein TOPST-Board auswählen](https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/Quick%20Guide/TOPST%20Imager/de/TOPST%20Imager%20Board%20Selection.png)

1. Wählen Sie das Board, das Ihrem tatsächlichen Produkt entspricht.
2. Prüfen Sie die hervorgehobene Zeile mit **Ausgewählt** und wählen Sie **Weiter**.

Auch ein Doppelklick führt weiter. Bei falscher Auswahl gehen Sie mit **Zurück** zurück.

### 2.2 Betriebssystem auswählen

![Offizielles Betriebssystem oder eigenes Image auswählen](https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/Quick%20Guide/TOPST%20Imager/de/TOPST%20Imager%20OS%20Selection.png)

1. Wählen Sie ein von TOPST bereitgestelltes Betriebssystem.
2. Für eine lokale Datei wählen Sie **Benutzerdefiniertes Image verwenden**.
3. Wählen Sie **Weiter** oder doppelklicken Sie auf die gewählte Zeile.

### 2.3 Version auswählen

![Eine Image-Version auswählen](https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/Quick%20Guide/TOPST%20Imager/de/TOPST%20Imager%20Version%20Selection.png)

1. Wählen Sie die benötigte Version. Prüfen Sie Beschreibung, Veröffentlichungsdatum, Downloadgröße und entpackte Größe.
2. Wählen Sie **Flashen**.

- **Online-Download** ist die komprimierte Dateigröße aus dem Internet.
- **Erforderlicher Mindestspeicher** ist der ungefähre Speicherbedarf nach dem Entpacken.

Nutzen Sie ohne projektspezifische Vorgaben die neueste stabile oder empfohlene Version.

### 2.4 Datenlöschung bestätigen

![Die eMMC-Löschwarnung bestätigen](https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/Quick%20Guide/TOPST%20Imager/de/TOPST%20Imager%20eMMC%20Erase%20Warning.png)

1. Wählen Sie **Abbrechen**, wenn Sie Board, Image oder Sicherung erneut prüfen müssen.
2. Wählen Sie **Bestätigen** nur, wenn Sie die mögliche Löschung der eMMC-Daten verstanden haben.

**Abbrechen** löscht das Board an dieser Stelle nicht.

## 3. D3-G unter Windows flashen

Die Flash-Einrichtung besteht aus drei Schritten.

### Schritt 1: VTC-Treiber installieren

![Den D3-G-VTC-Treiber installieren](https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/Quick%20Guide/TOPST%20Imager/de/TOPST%20Imager%20D3-G%20Driver%20Installation.png)

1. Wählen Sie **Treiber installieren**.
2. Bestätigen Sie die Windows-Administratoranfrage.
3. Schließen Sie den VTC Driver Installer ab.
4. Kehren Sie zu TOPST Imager zurück.
5. Wählen Sie **Treiberinstallation abgeschlossen**.

Normalerweise ist die Installation pro Windows-Computer nur einmal nötig. Brechen Sie die Administratoranfrage ab, wird kein Treiber installiert. Wählen Sie später erneut **Treiber installieren**.

### Schritt 2: Bootmodus und Board-Erkennung

![D3-G in den Bootmodus versetzen und erkennen](https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/Quick%20Guide/TOPST%20Imager/de/TOPST%20Imager%20D3-G%20Boot%20Mode.png)

1. Folgen Sie den blinkenden Markierungen der Animation.
2. Halten Sie die **BOOT**-Taste gedrückt.
3. Drücken Sie dabei die **RESET**-Taste und lassen Sie die **RESET**-Taste los.
4. Lassen Sie die **BOOT**-Taste los.
5. Verbinden Sie das FWDN-USB-Type-C-Datenkabel fest.
6. Wählen Sie **Erneut prüfen**, wenn sich der Status nicht automatisch aktualisiert.
7. Wählen Sie bei verbundenem Status **Flashen starten**.

Im Windows-Geräte-Manager kann D3-G unter USB-Controllern etwa als `Telechips TCCxxxx VTC USB Driver` erscheinen.

### Schritt 3: Flashen

Offizielle Images zeigen separate Fortschrittswerte für:

1. Download
2. Entpacken
3. Flashen

Jeder Wert steigt von 0 % auf 100 %. Trennen Sie erst nach dem Bildschirm **Abgeschlossen** eine Verbindung.

## 4. AI-G unter Windows flashen

Die Einrichtung besteht aus drei Schritten.

### Schritt 1: Ethernet einrichten

![Ethernet-Adapter und Netzwerkeinrichtung für AI-G](https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/Quick%20Guide/TOPST%20Imager/de/TOPST%20Imager%20AI-G%20Ethernet%20Setup.png)

1. Verbinden Sie Computer und AI-G direkt per Ethernet-Kabel.
2. Wählen Sie den angeschlossenen kabelgebundenen Adapter, nicht WLAN.
3. Erlauben Sie auf Aufforderung die temporäre Adresse `192.168.0.8/24`.
4. Fahren Sie fort, wenn das Netzwerk bereit ist.

Nach Abschluss oder Abbruch stellt TOPST Imager die vorübergehend geänderten Windows-Netzwerkeinstellungen wieder her.

### Schritt 2: Bootmodus und COM-Port

1. Folgen Sie der Bootmodus-Animation.
2. Halten Sie die **BOOT**-Taste gedrückt.
3. Drücken Sie die **RESET**-Taste und lassen Sie die **RESET**-Taste los.
4. Lassen Sie die **BOOT**-Taste los.
5. Wählen Sie den AI-G-COM-Port.
6. Prüfen Sie Stromversorgung, USB Type-C und Ethernet.
7. Fahren Sie mit dem Flashen fort.

Bei mehreren Ports ziehen Sie AI-G-USB kurz ab. Der verschwundene Port gehört normalerweise zu AI-G. Verbinden Sie das Kabel erneut, wiederholen Sie den Bootmodus und wählen Sie diesen Port.

### Schritt 3: Flashen

Warten Sie auf 100 % und den Bildschirm **Abgeschlossen**.

## 5. VCP-G unter Windows flashen

Die Einrichtung besteht aus zwei Schritten.

### Schritt 1: Bootmodus und COM-Port

![Bootmodus und COM-Port-Auswahl für VCP-G](https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/Quick%20Guide/TOPST%20Imager/de/TOPST%20Imager%20VCP-G%20Boot%20Mode%20and%20COM%20Port.png)

Bootmodus-Anleitung und Portauswahl stehen auf derselben Seite.

1. Versetzen Sie VCP-G anhand der Animation in den Firmware Download Mode.
2. Drücken Sie die **RESET**-Taste und lassen Sie die **RESET**-Taste los, wenn die Anleitung dies vorgibt.
3. Wählen Sie den VCP-G-COM-Port.
4. Prüfen Sie Stromversorgung und FWDN-USB-Type-C-Datenkabel erneut.
5. Fahren Sie mit dem Flashen fort.

### Schritt 2: Flashen

Warten Sie auf 100 % und den Bildschirm **Abgeschlossen**.

## 6. Eigenes Image unter Windows verwenden

**D3-G / AI-G (.fai)**

![Eigenes FAI-Image für D3-G und AI-G auswählen](https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/Quick%20Guide/TOPST%20Imager/de/TOPST%20Imager%20Custom%20FAI%20Image.png)

**VCP-G (.rom)**

![Eigenes ROM-Image für VCP-G auswählen](https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/Quick%20Guide/TOPST%20Imager/de/TOPST%20Imager%20Custom%20ROM%20Image.png)

1. Wählen Sie zuerst das richtige Board.
2. Klicken Sie auf der Betriebssystemseite einmal auf **Benutzerdefiniertes Image verwenden**.
3. Wählen Sie **Weiter** oder doppelklicken Sie auf **Benutzerdefiniertes Image verwenden**.
4. Ziehen Sie die Datei in den Ablagebereich oder verwenden Sie die Durchsuchen-Schaltfläche.
5. Prüfen Sie den Dateinamen und fahren Sie fort.

Verwenden Sie das richtige Format:

- D3-G: `.fai`
- AI-G: `.fai`
- VCP-G: `.rom`

Da die Datei lokal vorliegt, sind **Download** und **Entpacken** ausgeblendet. Die boardspezifischen Treiber-, Netzwerk-, Bootmodus-, COM-Port- und Flash-Schritte gelten weiterhin.

---

# Linux

## 1. Linux-Voraussetzungen

Die aktuelle Distribution unterstützt **x86_64 Linux**. Windows-FWDN-`.exe`-Dateien lassen sich nicht verwenden.

Diese ausführbaren Linux-Werkzeuge müssen enthalten sein:

```text
tools/fwdn_d3/fwdn_d3
tools/fwdn_ai/fwdn_ai
tools/fwdn_vcp/fwdn_vcp
```

Der Computer benötigt außerdem:

- `unzip` für offizielle ZIP-Pakete
- `policykit-1` für die Administratorbestätigung
- `acl` für temporären seriellen Zugriff auf AI-G und VCP-G

Unter Ubuntu kann ein Administrator sie so installieren:

```bash
sudo apt update
sudo apt install unzip policykit-1 acl
```

Starten Sie TOPST Imager oder FWDN **nicht** mit `sudo`. Die Anwendung fordert Administratorrechte nur für temporären Zugriff auf das ausgewählte serielle Gerät an.

## 2. Linux-Paket installieren und starten

Der Archivname hängt von der Version ab. Für ein `.tar.gz`-Paket:

```bash
cd ~/Downloads
tar -xzf TOPST-Imager-<version>-Linux-x86_64.tar.gz
cd TOPST-Imager-<version>-Linux-x86_64
chmod +x topst-imager
./topst-imager
```

Verwenden Sie die tatsächlichen Datei- und Ordnernamen. Ein Benutzerpaket sollte Qt enthalten. Fehlen Qt-Bibliotheken, laden Sie das vollständige offizielle Linux-Paket herunter, statt die Anwendung als root auszuführen.

## 3. Image unter Linux auswählen

Board-, Betriebssystem-, Versions-, Custom-Image- und eMMC-Warnseiten funktionieren wie die Windows-Seiten in Abschnitt 2 und 6.

## 4. D3-G unter Linux flashen

Ohne den Windows-VTC-Installer besteht die Einrichtung aus zwei Schritten.

### Schritt 1: Bootmodus und Board-Erkennung

1. Halten Sie die **BOOT**-Taste gedrückt.
2. Drücken Sie die **RESET**-Taste und lassen Sie die **RESET**-Taste los.
3. Lassen Sie die **BOOT**-Taste los.
4. Verbinden Sie das FWDN-USB-Type-C-Datenkabel.
5. Wählen Sie bei Bedarf **Erneut prüfen**.
6. Fahren Sie nach Erkennung von D3-G fort.

Linux erkennt das D3-G-FWDN-USB-Gerät direkt. Prüfen Sie sonst Datenkabel, Stromversorgung, Bootmodus und die mitgelieferte installierte udev-Regel.

### Schritt 2: Flashen

Warten Sie auf Download, Entpacken und Flashen. Eigene `.fai`-Images zeigen nur den Flash-Fortschritt.

## 5. AI-G unter Linux flashen

Die Einrichtung besteht aus drei Schritten.

### Schritt 1: Ethernet einrichten

Die Linux-Ethernet-Adresse wird nicht automatisch geändert. Richten Sie sie in den Netzwerkeinstellungen ein:

1. Öffnen Sie **Einstellungen → Netzwerk**.
2. Öffnen Sie die kabelgebundene AI-G-Verbindung.
3. Setzen Sie IPv4 auf **Manuell**.
4. Adresse: `192.168.0.8`
5. Netzmaske: `255.255.255.0` oder Präfixlänge `24`
6. Lassen Sie Gateway und DNS ohne andere Administratorvorgaben leer.
7. Übernehmen Sie die Änderung, verbinden Sie das Kabelnetz erneut und kehren Sie zur Anwendung zurück.

### Schritt 2: Bootmodus, COM-Port und temporärer Zugriff

1. Folgen Sie der Animation.
2. Wählen Sie den AI-G-Port, etwa `/dev/ttyUSB0`.
3. Wählen Sie bei fehlendem Schreibzugriff **Temporären Zugriff gewähren**.
4. Bestätigen Sie das Linux-Administratorfenster.
5. Sobald der Zugriff bereit ist, wird die Flash-Schaltfläche verfügbar.

Der Zugriff gilt nur für das ausgewählte serielle Gerät. Er endet nach Flashen, Abbruch oder Verlassen der Flash-Seite. Eine dauerhafte Mitgliedschaft in `dialout` ist nicht nötig.

### Schritt 3: Flashen

Warten Sie auf **Abgeschlossen**.

## 6. VCP-G unter Linux flashen

Wie unter Windows gibt es zwei Einrichtungsschritte.

### Schritt 1: Bootmodus, COM-Port und temporärer Zugriff

1. Folgen Sie der Bootmodus-Anleitung.
2. Wählen Sie den VCP-G-Port, etwa `/dev/ttyUSB0`.
3. Wählen Sie gegebenenfalls **Temporären Zugriff gewähren** und bestätigen Sie das Administratorfenster.
4. Fahren Sie fort, sobald der Port zugänglich ist.

### Schritt 2: Flashen

Warten Sie auf 100 % und **Abgeschlossen**. Eigene `.rom`-Images zeigen nur den Flash-Fortschritt.

## 7. Downloads, Wiederholungen und temporäre Dateien

Bei offiziellen Images führt TOPST Imager diese Schritte aus:

1. Temporären Arbeitsordner erstellen.
2. ZIP-Paket herunterladen.
3. In den temporären Ordner entpacken.
4. Boardspezifisches FWDN-Programm ausführen.
5. Nach Erfolg oder Abbruch temporäre Download- und Entpackdaten löschen.

Bei einer Internetunterbrechung lassen Sie die Anwendung geöffnet und verbinden Sie das Netzwerk erneut. Sie wiederholt automatisch den Versuch und setzt Teildownloads fort, wenn der Server dies unterstützt. Der Status erscheint in der gewählten Sprache.

Manche behebbaren Flash-Fehler behalten das vorbereitete Paket vorübergehend, damit Sie ohne erneuten Download zum angegebenen Schritt zurückkehren können.

## 8. Wenn ein Fehlerfenster erscheint

Bekannte FWDN-Fehler werden sofort angezeigt. Lesen Sie bei einem Drei-Sekunden-Countdown die Meldung; danach kehrt die Anwendung zum erforderlichen Wiederherstellungsschritt zurück. Prüfen Sie die Punkte und wählen Sie **Bestätigen**.

### D3-G-Verbindungsfehler

Prüfen Sie:

1. Stromversorgung
2. FWDN-USB-Type-C-Verbindung
3. Firmware Download Mode

Die Anwendung kehrt zum D3-G-Bootmodus zurück.

### AI-G-Verbindungs- oder Synchronisationsfehler

Prüfen Sie:

1. Stromversorgung
2. Firmware Download Mode
3. Richtigen COM-Port

Bei `Failed open port` prüfen Sie FWDN-USB-Type-C und den gewählten Port. Bei `TCP Socket Open Fail` prüfen Sie Ethernet-Kabel, Adapter und `192.168.0.8/24`.

### VCP-G-Verbindungsfehler

Prüfen Sie:

1. Stromversorgung
2. Firmware Download Mode
3. Richtigen COM-Port

Bei `GetLastError : 22` prüfen Sie die FWDN-USB-Type-C-Verbindung.

### Kein COM-Port erscheint

1. Prüfen Sie die Stromversorgung.
2. Verbinden Sie das USB-Datenkabel erneut.
3. Wiederholen Sie den Firmware Download Mode.
4. Aktualisieren Sie die Liste.
5. Wählen Sie unter Linux nach der Portauswahl **Temporären Zugriff gewähren**.

### Flashen schlägt vollständig fehl

Bei `Failed to write in eFlash` oder `Failed FWDN` beginnen Sie nach Meldung wieder mit dem ersten Einrichtungsschritt. Trennen Sie das Board nicht während eines laufenden Schreibvorgangs.

## 9. Protokolldateien

Geben Sie bei Hilfsanfragen vollständige Fehlermeldung, Boardname, Image-Version, Betriebssystem und Protokolldatei an.

Windows-Protokollpfad:

```text
%LOCALAPPDATA%\Telechips\TOPST Imager\logs\topst-imager.log
```

Üblicher Linux-Protokollpfad:

```text
~/.local/share/Telechips/TOPST Imager/logs/topst-imager.log
```

Verwenden Sie **App-Optionen → Community fragen** oder besuchen Sie die [TOPST-Community](https://community.topst.ai/).

## 10. Nach dem Flashen

1. Prüfen Sie, ob **Abgeschlossen** angezeigt wird.
2. Warten Sie auf die Abschlussmeldung der Anwendung.
3. Schalten Sie das Board sicher aus.
4. Entfernen Sie FWDN oder stellen Sie die normale Verkabelung her.
5. Schalten Sie das Board ein und prüfen Sie den Start des neuen Systems.

Beachten Sie drei Regeln:

1. Wählen Sie Board und Image sorgfältig.
2. Trennen Sie während des Flashens niemals Strom oder Kabel.
3. Prüfen Sie bei Fehlern alle angezeigten Punkte von oben nach unten.
