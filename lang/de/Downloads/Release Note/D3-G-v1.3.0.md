# D3-G Versionshinweise - v1.3.0

## Aktualisierte Repositories
- [isp-server](https://github.com/topst-development/isp-server/tree/feature/d3g-ov5647)
- [isp-frontend](https://github.com/topst-development/isp-frontend/tree/feature/d3g)
- [kernel-5.10](https://github.com/topst-development/kernel-5.10/tree/release/d3/1.3.0)
- [meta-topst](https://github.com/topst-development/meta-topst/tree/release/1.3.0)
- [meta-topst-bsp](https://github.com/topst-development/meta-topst-bsp/tree/release/1.3.0)
- [manifests](https://github.com/topst-development/manifests/tree/release/1.3.0)

## Neue Funktionen
- unterstützt den Vulkan-Treiber
- unterstützt ein grundlegendes Kamera-ISP-Tuning-Tool
- unterstützt die PIv2-Kamera über die Build-Konfiguration
- unterstützt firefox-esr (extended support release) im Ubuntu-Desktop-Release

## Verbesserungen
- verbessert die Geschwindigkeit der PCIe-Datenübertragung
- stabilisiert die Erkennung von PCIe-Blockgeräten beim Booten

## Bekannte Probleme
- Ein Warmstart dauert gelegentlich lange (etwa 40 Sekunden), wenn eine SD-Karte eingesteckt ist.
- Eine über MIPI angeschlossene externe Kamera unterstützt derzeit bis zu 30fps (im nächsten Release werden bis zu 60fps unterstützt)

## Anleitungen
 - VLC Player
   - Vor dem Abspielen von Inhalten muss die Videoausgabe in den Einstellungen auf 'X11 video output(XCB)' gesetzt werden.
 - Vulkan-Treiber
   - Führen Sie den Befehl 'vkcube' aus, um das Vulkan-Beispiel zu starten.
   - Unter [https://github.com/krh/vkcube.git](https://github.com/krh/vkcube.git) erfahren Sie, wie Sie Ihre eigene Vulkan-Anwendung programmieren.
