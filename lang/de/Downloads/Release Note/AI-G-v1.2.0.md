# AI-G Versionshinweise - v1.2.0

## Aktualisierte Repositories

- [tc-nn-app](https://github.com/topst-development/tc-nn-app)
- [libtc-ndnpu](https://github.com/topst-development/libtc-ndnpu)
- [tc-compiled-nn](https://github.com/topst-development/tc-compiled-nn)
- [meta-topst](https://github.com/topst-development/meta-topst)

## Neue Funktionen

- Das Standardmodell zur Objekterkennung in `tcnnapp` und das Standardtestmodell in `tcnputestapp` wurden von YOLOv5s auf YOLOv8s umgestellt.

## Verbesserungen

- Die Freigabe des Anwendungsspeichers, die Prüfung der Ein- und Ausgabebereiche sowie die Fehlermeldungen bei der Initialisierung wurden verbessert.
- Die Modelldateien und Metadaten von MobileNetV2 wurden aktualisiert.
- Das Windows-Skript zum Übertragen der Firmware verwendet nun PowerShell zur Erkennung der COM-Ports.

## Hinweise zur Verwendung

- Das Standardmodell befindet sich unter `/usr/share/yolov8s_quantized/`. Das zweite Standardmodell von `tcnnapp` befindet sich unter `/usr/share/mobilenetv2_10_quantized/`.
- Das mitgelieferte YOLOv8s-Modell enthält keine Datei `sample/input.ia.bin`. Fehlt diese Datei, verwendet `tcnputestapp` mit Nullen gefüllte Eingabedaten und gibt `Input file not found. Using zero padding.` aus. Damit werden die NPU-Ausführung und ihre Leistung geprüft, jedoch nicht die Modellgenauigkeit.
- Das fertige Firmwarepaket enthält `fwdn_ai.bat` für Windows und `fwdn_ai.sh` für Linux.

## Firmware

- [AIG-TOPST-Yocto-image-v1.2.0-r01](https://topst-downloads.s3.ap-northeast-2.amazonaws.com/Yocto/v1.2.0/aig-yp4-v1.2.0-r01.zip)
