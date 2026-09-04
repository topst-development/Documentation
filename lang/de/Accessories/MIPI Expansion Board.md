# MIPI-Erweiterungsboard
----

Das MIPI-Erweiterungsboard nutzt die serielle Hochgeschwindigkeitskommunikation GMSL2, um die Schnittstellen MIPI CSI und MIPI DSI zu unterstützen(Abbildung 1). Jedes Board enthält Serializer- und Deserializer-Chipsätze für Kameraeingang und Displayausgabe und gewährleistet so eine zuverlässige Datenübertragung mit hoher Auflösung. 
**Hinweis:** Verfügbarkeit und Konfiguration der Komponenten erfolgen auftragsbezogen je nach den spezifischen Projektanforderungen.

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/accessories/mipi_expansion_board_crop.png" width="350"></p>
<p align="center"><strong>Abbildung 1. MIPI-Erweiterungsboard</strong></p><br/>

## MIPI CSI (Camera Serial Interface)

### Board-Informationen
- **Größe**: 71.5 mm × 73.5 mm × 1.6 t / 4 Lagen
- **Deserializer**: MAX96712 (ADI)
- **GMSL-Version**: GMSL2
- **Link-Anzahl**: Bis zu 4-Kanal MIPI CSI2 Eingang
- **Auflösung / Bandbreite**: Bis zu 1.5 Gbps × 4-lanes × 4 Kanäle
- **Stromversorgung**: 1.8V / 3.3V
- **Gehäuse**: 64 QFN / 9 mm × 9 mm
- **Steuerschnittstelle**: I²C
- **B2B-Steckverbinder**: 61083-043402LF (Amphenol)


## MIPI DSI (Display Serial Interface)

### Board-Informationen
- **Größe**: 60 mm × 30 mm × 1.6 t / 4 Lagen
- **Serializer**: MAX96789 (ADI)
- **GMSL-Version**: GMSL2
- **Link-Anzahl**: Bis zu 4-Kanal MIPI DSI2 Ausgang
- **Auflösung / Bandbreite**: Bis zu 6 Gbps
- **Stromversorgung**: 1.8V / 3.3V
- **Gehäuse**: 56 QFN / 8 mm × 8 mm
- **Steuerschnittstelle**: I²C
- **B2B-Steckverbinder**: 10132797-067110LF (Amphenol)