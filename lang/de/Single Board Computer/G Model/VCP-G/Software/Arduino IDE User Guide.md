# 1. Einführung
---
In diesem Dokument wird beschrieben, wie Sie die Arduino IDE für den TOPST Vehicle Control Processor (VCP) verwenden, einen leistungsstarken und effizienten Prozessor, der für Automotive-Anwendungen entwickelt wurde und auf dem TCC7045 basiert. Ziel ist es, den VCP-G in die Arduino-Umgebung zu integrieren, um eine Entwicklungsumgebung bereitzustellen, die der Einfachheit und Flexibilität von Arduino entspricht und speziell auf Automotive-Halbleiter zugeschnitten ist, und den Entwicklungsprozess zu vereinfachen und zu beschleunigen.  

Dieses Dokument enthält Informationen zu den folgenden Themen:  
- Installationsanleitung

</br></br></br></br>

# 2. Installationsanleitung
---
In diesem Kapitel wird beschrieben, wie Sie das VCP-G Arduino-Paket herunterladen und installieren, um es mit der integrierten Arduino-Entwicklungsumgebung (IDE) zu verwenden.

</br></br></br>

## 2.1 Installationsanleitung
---
**Schritt 1: Arduino IDE herunterladen**

Zunächst benötigen Sie die Arduino IDE, die als Plattform zum Programmieren Ihrer Arduino-Boards dient.  
1. Besuchen Sie die offizielle Arduino-Website : [Arduino Software](https://www.arduino.cc/en/software)
2. Wählen Sie die für Ihr Betriebssystem geeignete Version aus (Windoiws, macOS oder Linux).
3. Laden Sie das Installationsprogramm herunter und führen Sie es aus.

**Schritt 2: Arduino IDE installieren**  
Führen Sie je nach Betriebssystem die folgenden Schritte aus, um die Arduino IDE zu installieren:  

- Windows:
    1. Führen Sie die heruntergeladene .exe-Datei aus.
    2. Folgen Sie den Installationsanweisungen. Stellen Sie sicher, dass Sie alle erforderlichen Treiber installieren.
- macOS:
    1. Öffnen Sie die .dmg-Datei
    2. Ziehen Sie die Arduino-Anwendung in Ihren Ordner Applications.
- Linux:
    1. Entpacken Sie die .tar.xz-Datei.
    2. Öffnen Sie ein Terminal im entpackten Verzeichnis.
    3. Führen Sie ./install.sh aus, um die Installation durchzuführen.

**Schritt 3: Die VCP-G .json-Datei zur Arduino IDE hinzufügen**  
Um den VCP-G zu programmieren, müssen Sie die VCP-G .json-Datei über den Board Manager zur Arduino IDE hinzufügen.
1. Öffnen Sie die Arduino IDE.
2. Navigieren Sie zu **File > Preferences**.
3. Fügen Sie im Feld **„Additional Board Manager URLs“** die folgende URL hinzu:
    ```
    https://raw.githubusercontent.com/topst-development/VCP-Arduino_Board_Manager/develop/package_topst_vcp_index.json
    ```
4. Klicken Sie auf **OK**, um Ihre Änderungen zu speichern.
5. Gehen Sie zu **Tools > Board > Boards Manager.**
6. Suchen Sie im Boards Manager nach „TOPST VCP-G“.
7. Wenn der Eintrag TOPST VCP-G erscheint, wählen Sie v1.0.0 aus dem Dropdown-Menü aus und klicken Sie auf **Install**.

**Schritt 4: Den VCP-G auswählen**  
Nach der Installation müssen Sie das TOPST VCP-G Board auswählen:  
1. Gehen Sie in der Arduino IDE zu **Tools > Board**.
2. Scrollen Sie nach unten, um „TOPST VCP-G“ zu finden, und wählen Sie es aus.

**Schritt 5: Installation überprüfen**  
Testen Sie, ob Ihre Einrichtung funktioniert, indem Sie einen einfachen Sketch hochladen:
1. Verbinden Sie das VCP-G Board über USB mit Ihrem PC.
2. Wählen Sie unter **Tools > Port** den passenden Anschluss aus.
3.	Öffnen Sie **File > Examples > 01.Basics > Blink**.
4.	Klicken Sie auf **Upload**, um den Sketch auf das Board zu übertragen.  
    **Hinweis:** Wenn der Upload-Vorgang in einem endlosen Upload-Zustand hängen bleibt, liegt das daran, dass der FWDN-Modus nicht aktiviert ist. Ziehen Sie das Netzkabel ab, halten Sie den FWDN-Schalter gedrückt, schließen Sie das Netzkabel wieder an und lassen Sie dann die Taste los. Falls das Problem weiterhin besteht, führen Sie die Arduino IDE mit Administratorrechten aus.
5.	Wenn die Onboard-LED zu blinken beginnt, ist das Board korrekt eingerichtet.

</br></br></br>

## 2.2 Fehlerbehebung
---
Wenn während der Einrichtung Probleme auftreten, siehe [Arduino Troubleshooting Guide](https://www.arduino.cc/en/Guide/Troubleshooting).  
Weitere Informationen und erweiterte Funktionen finden Sie in der VCP-G Dokumentation oder unter [Arduino Help Center](https://support.arduino.cc/hc/en-us).

</br></br></br></br>

# 3. Referenzen
---
- Weitere Details erhalten Sie von TOPST: topst@topst.ai

**Hinweis:** Referenzdokumente können bereitgestellt werden, sofern verfügbar und je nach den Bedingungen eines Vertrags. Wenn die
Referenzdokumente nicht verfügbar sind, kann zu den Inhalten beraten werden, die direkt mit Ihrer Entwicklung zusammenhängen.

