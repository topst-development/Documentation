# 1. Einführung
---
Dieses Dokument ist ein Hardware-Benutzerhandbuch für das VCP-G auf Basis des TCC7045 Application Processors. Dieses Dokument beschreibt die Systeminstallation, das Debugging sowie detaillierte Informationen zum Gesamtdesign und zur Verwendung des VCP-G.


Tabelle 1.1 beschreibt die Merkmale des VCP-G.

<p align="center"><strong>Tabelle 1.1 Merkmale des VCP-G</strong></p>
<div align="center">
	<table>
	  <tr>
	    <td colspan="3">Teilebezeichnung</td>
	    <td>TCC7045</td>
	  </tr>
	  <tr>
	    <td colspan="3">Gehäuse</td>
	    <td>Gehäuse	Pin-zu-Pin-kompatibel FBGA 196-pin (12BD)</td>
	  </tr>
	    <tr>
	    <td colspan="3">CPU-Frequenz</td>
	    <td>200 MHz (bis zu 300 MHz)</td>
	  </tr>
	  <tr>
	    <td rowspan="4">On-Chip-Speicher</td>
	    <td colspan="2">Programm-Flash</td>
	    <td colspan="3">4 MB</td>
	  </tr>
	  <tr>
	    <td colspan="2">SRAM</td>
	    <td colspan="3">512 KB (einschließlich Retention RAM 16 KB)</td>
	  </tr>
	  <tr>
	    <td colspan="2">DataFlash</td>
	    <td colspan="3">256 KB</td>
	  </tr>
	  <tr>
	    <td colspan="2">DMA-Kanal</td>
	    <td colspan="3">16 Kanäle</td>
	  </tr>
	  <tr>
	    <td rowspan="13">Peripherie</td>
	    <td colspan="2">Ethernet</td>
	    <td>1 Gbps mit AVB</td>
	  </tr>
	  <tr>
		<td colspan="2">CAN / CANFD</td>
	    <td>3-Kanal</td>
	  </tr>
	  <tr>
	    <td colspan="2">Dedizierte LIN / UART</td>
	    <td>3 Kanäle (maximal 6 Kanäle)</td>
	  </tr>
	  <tr>
	    <td colspan="2">Dediziertes I2C</td>
	    <td>3 Kanäle (maximal 6 Kanäle)</td>
	  </tr>
	  <tr>
	  <tr>
	    <td colspan="2">Dediziertes GPSB (SPI)</td>
	    <td>2 Kanäle (maximal 5 Kanäle)</td>
	  </tr>
	    <tr>
	    <td colspan="2">MFIO (zugewiesen UART, I2C, GPSB)</td>
	    <td>3 Kanäle</td>
	  </tr>
	  <tr>
	    <td rowspan="4">ADC</td> 
	    <td>Auflösung</td>
	    <td>12-bit SAR-Typ</td>
	  </tr>
	  <tr>
	    <td>Kanäle</td>
	    <td>12-Kanal x 2 Gruppen</td>
	  </tr>
	  <tr>
	    <td>Eingangsbereich</td>
	    <td>3.3V</td>
	  </tr>
	  <tr>
	    <td>Abtastrate</td>
	    <td>Über 1.0 MSPs</td>
	  </tr>
	  <tr>
	    <td colspan="2">I2S</td>
	    <td>1-Kanal</td>
	  </tr>
	  <tr>
	    <td colspan="2">Serielle Flash-Schnittstelle</td>
	    <td>Quad SPI</td>
	  </tr>  
	  <tr>
	    <td colspan="3">Stromversorgungssystem</td>
	    <td>3.3V Einzelversorgung</td>
	  </tr>
	  <tr>
	    <td colspan="3">Temperatur</td>
	    <td>-40 ℃ to 105 ℃</td>
	  </tr>
	</table>
</div>

</br></br></br>

## 1.1 Terminologie
---
<p align="center"><strong>Tabelle 1.2 Terminologie </strong></p>
<div align="center">
	<table>
	  <tr>
	    <td clospan="2"><strong>Terminologie</strong></td>
	    <td><strong>Definition</strong></td>
	  </tr>
	  <tr>
	    <td clospan="2">ADC</td>
	    <td>Analog-Digital-Wandler</td>
	  </tr>
	  <tr>
	    <td clospan="2">FWDN</td>
	    <td>Firmware-Download</td>
	  </tr>
	  <tr>
	    <td clospan="2">GPIO</td>
	    <td>Universeller Ein-/Ausgang</td>
	  </tr>
	  <tr>
	    <td clospan="2">MCU</td>
	    <td>Mikrocontroller-Einheit</td>
	  </tr>
	  <tr>
	    <td clospan="2">TOPST</td>
	    <td>Total Open-Platform for System development and Training</td>
	  </tr>
	  <tr>
	    <td clospan="2">VCP</td>
	    <td>Fahrzeugsteuerungsprozessor</td>
	  </tr>
	</table>
</div>

</br></br></br></br>

# 2. Blockdiagramm
---
## 2.1 System-Blockdiagramm
---
Abbildung 2.1 zeigt das Systemblockdiagramm des VCP-G.
<p align="center"><img src= "https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Hardware/2.1%20VCP-G%20System%20Block%20Diagram.png"></p>
<p align="center"><strong>Abbildung 2.1 Systemblockdiagramm</strong></p>

</br></br></br></br>

# 3. VCP-G Übersicht
---
Das VCP-G kann für die folgenden Zwecke verwendet werden:
  - Systementwicklung
  - Schulung

Tabelle 3.1 beschreibt die Standardkonfiguration des VCP-G.

<p align="center"><strong>Tabelle 3.1 Standardkonfiguration des VCP-G </strong></p>
<div align="center">
	<table>
	  <tr>
	    <td colspan="2"><strong>Board-Name</strong></td>
	    <td><strong>Beschreibung</strong></p>
	  </tr>
	  <tr>
	    <td colspan="2">TOPST_VCP_V2.1.1</td>
	    <td>MCU-Board für TOPST</td>
	  </tr>
	</table>
</div>

</br></br></br>

## 3.1 VCP-G
---
Abbildung 3.1 zeigt die Draufsicht des VCP-G.
<p align="center"><img src= "https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Hardware/3.1%20TOPST%20VCP-G%20Board%20(Top%20View)%20.png"></p>
<p align="center"><strong>Abbildung 3.1 VCP-G (Draufsicht)</strong></p>

Tabelle 3.2 beschreibt die Anschlüsse des VCP-G (Draufsicht).
<p align="center"><strong>Tabelle 3.2 Anschlüsse des VCP-G (Draufsicht)</strong></p>
<div align="center">
	<table>
	  <tr>
	    <td colspan="4"><strong>Nummer</strong></td>
	    <td><strong>Referenznummer</strong></td>
	    <td><strong>Name</strong></td>
	    <td><strong>Beschreibung</strong></td>
	  </tr>
	  <tr>
	    <td colspan="4">1</td>
	    <td>J18D100</td>
	    <td>36-poliger Header (Buchse)</td>
	    <td>Header für GPIO und ADC</td>
	  </tr>
	  <tr>
	    <td colspan="4">2</td>
	    <td>J5D100</td>
	    <td>10-poliger Header (Stift)</td>
	    <td>Header für CAN</td>
	  </tr>
	  <tr>
	    <td colspan="4">3</td>
	    <td>J3D100</td>
	    <td>6-poliger Header (Stift)</td>
	    <td>Header für SPI</td>
	  </tr>
	  <tr>
	    <td colspan="4">4</td>
	    <td>J8D104</td>
	    <td>8-poliger Header (Buchse)</td>
	    <td>Header für GPIO und ADC</td>
	  </tr>
	  <tr>
	    <td colspan="4">5</td>
	    <td>J8D102</td>
	    <td>8-poliger Header (Buchse)</td>
	    <td>Header für GPIO</td>
	  </tr>
	  <tr>
	    <td colspan="4">6</td>
	    <td>J10D100</td>
	    <td>10-poliger Header (Buchse)</td>
	    <td>Header für GPIO und ADC</td>
	  </tr>
	  <tr>
	    <td colspan="4">7</td>
	    <td>J100</td>
	    <td>10-poliger Header (Stift)</td>
	    <td>Header für JTAG</td>
	  </tr>
	  <tr>
	    <td colspan="4">8</td>
	    <td>SW100</td>
	    <td>RESET-Taster</td>
	    <td>GRESETn: Initialisiert das System und das Power-Management des VCP-G</td>
	  </tr>
	  <tr>
	    <td colspan="4">9</td>
	    <td>JC100</td>
	    <td>USB-Type-C-Anschluss</td>
	    <td>UART zum Debuggen oder FWDN-Port</td>
	  </tr>
	  <tr>
	    <td colspan="4">10</td>
	    <td>SW101</td>
	    <td>Taster</td>
	    <td>FWDN: Aufrufen des Firmware-Download-Modus des VCP-G</td>
	  </tr>  
	  <tr>
	    <td colspan="4">11</td>
		<td>J101</td>
	    <td>DC-Buchse</td>
	    <td>DC-Stromeingangsbuchse</td>
	  </tr>  
	  <tr>
	    <td colspan="4">12</td>
	    <td>J8D100</td>
	    <td>8-poliger Header (Buchse)</td>
	    <td>Header für Stromversorgung und Reset</td>
	  </tr>  
	  <tr>
	    <td colspan="4">13</td>
	    <td>J8D101</td>
	    <td>8-poliger Header (Buchse)</td>
	    <td>Header für GPIO und ADC</td>
	  </tr>  
	  <tr>
	    <td colspan="4">14</td>
	    <td>J8D103</td>
	    <td>8-poliger Header (Buchse)</td>
	    <td>Header für GPIO und ADC</td>
	  </tr>    
	</table>
</div>

Abbildung 3.2 zeigt die Unteransicht des VCP-G.  

**Hinweis:** Abbildung 3.2 zeigt derzeit das Board TOPST_VCP-G_V1.1.1. Dieses Bild wird auf das Board TOPST_VCP-G_V2.1.1 aktualisiert.
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Hardware/3.2%20TOPST%20VCP-G%20Board%20(Bottom%20View).png"></p>
<p align="center"><strong>Abbildung 3.2 VCP-G (Unteransicht)</strong></p>

</br></br></br></br>

# 4. Technische Daten
---
## 4.1 Quad-SPI-Flash-Speicher (U101)
---
Die Informationen zum Quad-SPI-Flash-Speicher lauten wie folgt:
  - Dichte : 64 Mb  
  
**Hinweis:** SNOR ist auf dem VCP-G standardmäßig nicht bestückt.

</br></br></br>

## 4.2 Stromeingangsanschluss (J101)
---
DC 12V wird dem VCP-G über die DC-Buchse von J101 aus einem 12V-Adapter zugeführt.  
Abbildung 4.1 zeigt die Position von J101.
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Hardware/4.1%20Power%20In%20Connector%20(J101).png"></p>
<p align="center"><strong>Abbildung 4.1 Stromeingangsanschluss (J101)</strong><p>

</br></br></br>

## 4.3 Anschluss für JTAG (J100)
---
Zum Debuggen kann über J100 ein JTAG-Emulator an das VCP-G angeschlossen werden. Abbildung 4.2 zeigt die Position von J100.
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Hardware/4.2%20Connector%20for%20JTAG%20(J100).png"></p>
<p align="center"><strong>Abbildung 4.2 Anschluss für JTAG (J100)</strong><p>
JTAG ist standardmäßig deaktiviert. Um JTAG zu aktivieren, müssen Sie die Verbindungen von R178 und R179 ändern. Wenn TRSRn durch R178 auf High gesetzt wird, wechselt der MCU in den JTAG-Modus.

Tabelle 4.1 beschreibt die Pins von J100.
<p align="center"><strong>Tabelle 4.1 J100 Pinbeschreibung</strong></p>
<div align="center">
	<table>
	  <tr>
	    <th rowspan="2"><strong>Pin-Nummer</strong></th>
	    <th rowspan="2"><strong>Schaltplan-Netzname</strong></th>
	    <th><strong>DIR</strong></th>
	    <th rowspan="2"><strong>Beschreibung</strong></th>
	  </tr>
	  <tr>
	    <th><strong>MCU ◄► J100</strong></th>
	  </tr>
	  <tr>
	    <td>1</td>
	    <td>SW_VDD_3P3</td>
	    <td>-</td>
	    <td>Stromversorgung 3.3V</td>
	  </tr>
	  <tr>
	    <td>2</td>
	    <td>TMS</td>
	    <td>◄</td>
	    <td>Testmodus-Zustand</td>
	  </tr>
	  <tr>
	    <td>3</td>
	    <td>DGND</td>
	    <td>-</td>
	    <td>Masse</td>
	  </tr>
	  <tr>
	    <td>4</td>
	    <td>TCK</td>
	    <td>◄</td>
	    <td>Testtakt</td>
	  </tr>
	  <tr>
	    <td>5</td>
		<td>DGND</td>
	    <td>-</td>
	    <td>Masse</td>
	  </tr>
	  <tr>
	    <td>6</td>
	    <td>TDO</td>
	    <td>►</td>
	    <td>Testdatenausgang</td>
	  </tr>
	  <tr>
	    <td>7</td>
	    <td>NC</td>
	    <td>-</td>
	    <td>Nicht angeschlossen</td>
	  </tr>
	  <tr>
	    <td>8</td>
	    <td>TDI</td>
	    <td>◄</td>
	    <td>Testdateneingang</td>
	  </tr>
	  <tr>
	    <td>9</td>
	    <td>DGND</td>
	    <td>-</td>
	    <td>Masse</td>
	  </tr>
	  <tr>
	    <td>10</td>
	    <td>JTAG_RESETn</td>
	    <td>◄</td>
	    <td>System-Reset</td>
	  </tr>   
	</table>
</div>

Tabelle 4.2 beschreibt die Einstellung zum Deaktivieren/Aktivieren von JTAG.
<p align="center"><strong>Tabelle 4.2 Einstellung zum Deaktivieren/Aktivieren von JTAG</strong></p>
<div align="center">
	<table>
	  <tr>
	    <th colspan="4"><strong>Modus</strong></th>
	    <th><strong>TRSTn-Wert</strong></th>
	    <th><strong>R178</strong></th>
	    <th><strong>R179</strong></th>
	  </tr>
	  <tr>
	    <td colspan="4">JTAG deaktiviert (Standard)</td>
	    <td>Low (1)</td>
	    <td>N.C</td>
	    <td>1K</td>
	  </tr>
	  <tr>
	    <td colspan="4">JTAG aktiviert (Option)</td>
	    <td>High (1)</td>
	    <td>1K</td>
	    <td>N.C</td>
	  </tr>
	</table>
</div>

</br></br></br>

## 4.4 FWDN-Schalter (SW101)
---
Das VCP-G verfügt über einen Pin für die Boot-Konfiguration über Boot Mode (BM) und unterstützt 2 Modi: den UART-FWDN-Modus und den normalen Modus.   
Abbildung 4.3 zeigt die Position des FWDN-Tasters (SW101), mit dem der Boot-Modus des VCP-G ausgewählt wird.
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Hardware/4.3%20FWDN%20Tact%20Switch%20(SW101).png"></p>
<p align="center"><strong>Abbildung 4.3 FWDN-Taster (SW101)</strong><p>

Tabelle 4.3 beschreibt, wie Sie mit dem FWDN-Taster (SW101) den Boot-Modus auswählen.
<p align="center"><strong>Tabelle 4.3 Beschreibung des Tasters (SW101) für den Boot-Modus</strong></p>
<div align="center">
	<table>
	  <tr>
	    <th colspan="3"><strong>Modus</strong></th>
	    <th><strong>BM00-Wert</strong></th>
	    <th><strong>SW101-Status</strong></th>
	  </tr>
	  <tr>
	    <td colspan="3">Normal (Standard)</td>
	    <td>Low (1)</td>
	    <td>Standard</td>
	  </tr>
	  <tr>
	    <td colspan="3">FWDN (Option)</td>
	    <td>High (1)</td>
	    <td>Gedrückt und Stromversorgung</td>
	  </tr>
	</table>
</div>
</br></br>

### 4.4.1 Methode für den FWDN-Modus
Es gibt die folgenden zwei Methoden, um in den FWDN-Modus zu wechseln.

#### 4.4.1.1 Methode 1
Halten Sie den FWDN-Schalter (SW101) gedrückt und schließen Sie die 12V-Stromversorgung an, um das VCP-G-Board einzuschalten.  
Die rote FWDN-Anzeige leuchtet auf, wenn die Stromversorgung bei gedrücktem FWDN-Schalter angelegt wird. Nach dem Loslassen des FWDN-Schalters (SW101) wechselt der MCU in den FWDN-Modus.  
Abbildung 4.4 zeigt, wie Sie mit Methode 1 in den FWDN-Modus wechseln.
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Hardware/4.4%20Entering%20FWDN%20Mode%20by%20Using%20Method%201.png"></p>
<p align="center"><strong>Abbildung 4.4 Wechsel in den FWDN-Modus mit Methode 1</strong><p>

#### 4.4.1.2 Methode 2
Drücken Sie bei an die 12V-Stromversorgung angeschlossenem VCP-G-Board den FWDN-Schalter (SW101) und anschließend den RESET-Taster (SW100).  
Die rote FWDN-Anzeige leuchtet auf, wenn die Stromversorgung bei gedrücktem FWDN-Schalter angelegt wird. Die grüne 3.3V-Anzeige erlischt, während der RESET-Taster gedrückt wird. Nach dem Loslassen des FWDN-Schalters (SW101) wechselt der MCU in den FWDN-Modus.  
Abbildung 4.5 zeigt den FWDN-Modus mit Methode 2.

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Hardware/4.5%20Entering%20FWDN%20Mode%20by%20Using%20Method%202.png"></p>
<p align="center"><strong>Abbildung 4.5 Wechsel in den FWDN-Modus mit Methode 2</strong><p>

</br></br></br>

## 4.5 RESET-Taster (SW100)
---
Das VCP-G verfügt über einen RESET-Schalter für den RESET der Stromversorgung über den GRESETn-Pin.  
Abbildung 4.6 zeigt den RESET-Taster (SW100).
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Hardware/4.6%20RESET%20Tact%20Switch%20(SW100).png"></p>
<p align="center"><strong>Abbildung 4.6 RESET-Taster (SW100)</strong><p>
</br></br>

### 4.5.1 Funktion des RESET-Tasters (SW100)
SW100 ist ein Taster, mit dem der Power-Block und der System-Block im VCP-G zurückgesetzt werden.  
Die Funktion dieser Taste lautet wie folgt:
  - Durch Drücken des RESET-Tasters (SW100) bei eingeschalteter Stromversorgung werden der Power-Block und das System des VCP-G zurückgesetzt.

**Wichtig:** Seien Sie beim Drücken des Tasters vorsichtig, da die Stromversorgung plötzlich abgeschaltet wird und Daten beschädigt werden können.

</br></br></br>

## 4.6 Anschluss für Debugging und FWDN (JC100)
---
JC100 ist ein standardmäßiger USB-Type-C-Anschluss. Auf dem VCP-G wird JC100 zum Debuggen oder für FWDN über UART verwendet.  
Abbildung 4.7 zeigt die Position von JC100.
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Hardware/4.7%20USB%20Type-C%20Connector%20(JC100).png"></p>
<p align="center"><strong>Abbildung 4.7 USB-Type-C-Anschluss (JC100)</strong><p>

Über JC100 können Sie FWDN durchführen oder die Debugging-Meldungen des VCP-G prüfen.
JC100 auf dem VCP-G enthält einen integrierten USB-zu-UART-Bridge-Controller, sodass Sie JC100 mit dem USB-Type-C-Kabel direkt an einen PC anschließen können.

</br></br></br>

## 4.7 Pin-Header für GPIO, ADC, Stromversorgung, CAN und SPI
---
Das VCP-G verfügt über neun 2.54 mm Pin-Header für Stromversorgung, GPIO, ADC, CAN und SPI, um weitere Peripheriegeräte wie Sensoren oder Sub-Boards anzuschließen.  

Tabelle 4.4 beschreibt den Zweck der neun Pin-Header auf dem VCP-G.
<p align="center"><strong>Tabelle 4.4 Pin-Header auf dem VCP-G </strong></p>
<div align="center">
	<table>
	  <tr>
	    <td colspan="4"><strong>Nummer</strong></td>
	    <td><strong>Referenznummer</strong></td>
	    <td><strong>Name</strong></td>
	    <td><strong>Beschreibung</strong></td>
	  </tr>
	  <tr>
	    <td colspan="4">1</td>
	    <td>J18D100</td>
	    <td>36-poliger Header (Buchse)</td>
	    <td>Header für GPIO und ADC</td>
	  </tr>
	  <tr>
	    <td colspan="4">2</td>
	    <td>J5D100</td>
	    <td>10-poliger Header (Stift)</td>
	    <td>Header für CAN</td>
	  </tr>
	  <tr>
	    <td colspan="4">3</td>
	    <td>J3D100</td>
	    <td>6-poliger Header (Stift)</td>
	    <td>Header für SPI</td>
	  </tr>
	  <tr>
	    <td colspan="4">4</td>
	    <td>J8D104</td>
	    <td>8-poliger Header (Buchse)</td>
	    <td>Header für GPIO und ADC</td>
	  </tr>
	  <tr>
	    <td colspan="4">5</td>
	    <td>J8D102</td>
	    <td>8-poliger Header (Buchse)</td>
	    <td>Header für GPIO</td>
	  </tr>
	  <tr>
	    <td colspan="4">6</td>
	    <td>J10D100</td>
	    <td>10-poliger Header (Buchse)</td>
	    <td>Header für GPIO und ADC</td>
	  </tr>
	  <tr>
	    <td colspan="4">7</td>
	    <td>J8D100</td>
	    <td>8-poliger Header (Buchse)</td>
	    <td>Header für Stromversorgung und Reset</td>
	  </tr>
	  <tr>
	    <td colspan="4">8</td>
	    <td>J8D101</td>
	    <td>8-poliger Header (Buchse)</td>
	    <td>Header für GPIO und ADC</td>
	  </tr>
	  <tr>
	    <td colspan="4">9</td>
	    <td>J8D103</td>
	    <td>8-poliger Header (Buchse)</td>
	    <td>Header für GPIO und ADC</td>
	  </tr>
	</table>
</div>

Abbildung 4.8 zeigt die Position der Pin-Header auf dem VCP-G.
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Hardware/4.8%20Pin%20Headers%20on%20TOPST%20VCP-G%20Board.png"></p>
<p align="center"><strong>Abbildung 4.8 Pin-Header auf dem VCP-G </strong><p>

Tabelle 4.5 zeigt die Pinbeschreibung von J10D100.
<p align="center"><strong>Tabelle 4.5 J10D100 Pinbeschreibung</strong></p>
<div align="center">
	<table>
	  <tr>
	    <th rowspan="3"><strong>Pin-Nummer</strong></th>
	    <th colspan="4"><strong>J10D100</strong></th>
	  </tr>
	  <tr>
	    <th rowspan="2"><strong>Port-Name</strong></th>
	    <th rowspan="2"><strong>Signalname</strong></th>
	    <th><strong>DIR</strong></th>
	    <th rowspan="2"><strong>Beschreibung</strong></th>
	  </tr>
	  <tr>
	    <th><strong>MCU ◄► J10D100</strong></th>
	  </tr>
	  <tr>
	    <td>1</td>
	    <td>SCL</td>
	    <td>GPIO_AC07</td>
	    <td>◄►</td>
	    <td>GPIO- oder ADC-Signal</td>
	  </tr>
	  <tr>
	    <td>2</td>
	    <td>SDA</td>
	    <td>GPIO_AC06</td>
	    <td>◄►</td>
	    <td>GPIO- oder ADC-Signal</td>
	  </tr>
	  <tr>
	    <td>3</td>
	    <td>AREF</td>
	    <td>ADC06</td>
	    <td>◄</td>
	    <td>ADC-Signal</td>
	  </tr>
	  <tr>
	    <td>4</td>
	    <td>GND</td>
	    <td>DGND</td>
	    <td>-</td>
	    <td>Masse</td>
	  </tr>
	  <tr>
	    <td>5</td>
	    <td>13</td>
	    <td>GPIO_C12</td>
	    <td>◄►</td>
	    <td>GPIO-Signal</td>
	  </tr>
	  <tr>
	    <td>6</td>
	    <td>12</td>
	    <td>GPIO_C15</td>
	    <td>◄►</td>
	    <td>GPIO-Signal</td>
	  </tr>
	  <tr>
	    <td>7</td>
	    <td>11</td>
	    <td>GPIO_C14</td>
	    <td>◄►</td>
	    <td>GPIO-Signal</td>
	  </tr>
	  <tr>
	    <td>8</td>
	    <td>10</td>
	    <td>GPIO_C13</td>
	    <td>◄►</td>
	    <td>GPIO-Signal</td>
	  </tr>
	  <tr>
	    <td>9</td>
	    <td>9</td>
	    <td>GPIO_A12</td>
	    <td>◄►</td>
	    <td>GPIO-Signal</td>
	  </tr>
	  <tr>
	    <td>10</td>
	    <td>8</td>
	    <td>GPIO_B00</td>
	    <td>◄►</td>
	    <td>GPIO-Signal</td>
	  </tr>
	</table>
</div>

Tabelle 4.6 zeigt die Pinbeschreibung von J8D100.
<p align="center"><strong>Tabelle 4.6 J8D100 Pinbeschreibung</strong></p>
<div align="center">
	<table>
	  <tr>
	    <th rowspan="3"><strong>Pin-Nummer</strong></th>
	    <th colspan="4"><strong>J8D100</strong></th>
	  </tr>
	  <tr>
	    <th rowspan="2"><strong>Port-Name</strong></th>
	    <th rowspan="2"><strong>Signalname</strong></th>
	    <th><strong>DIR</strong></th>
	    <th rowspan="2"><strong>Beschreibung</strong></th>
	  </tr>
	  <tr>
	    <th><strong>MCU ◄► J8D100</strong></th>
	  </tr>
	  <tr>
	    <td>1</td>
	    <td>-</td>
	    <td>-</td>
	    <td>-</td>
	    <td>-</td>
	  </tr>
	  <tr>
	    <td>2</td>
	    <td>IOREF</td>
	    <td>VCP_3P3</td>
	    <td>-</td>
	    <td>Stromversorgung 3.3V</td>
	  </tr>
	  <tr>
	    <td>3</td>
	    <td>RST</td>
	    <td>RESET</td>
	    <td>◄</td>
	    <td>Reset-Signal</td>
	  </tr>
	  <tr>
	    <td>4</td>
	    <td>3.3V</td>
	    <td>VCP_3P3</td>
	    <td>-</td>
	    <td>Stromversorgung 3.3V</td>
	  </tr>
	  <tr>
	    <td>5</td>
	    <td>5V</td>
	    <td>VCP_5P0</td>
	    <td>-</td>
	    <td>Stromversorgung 5.0V</td>
	  </tr>
	  <tr>
	    <td>6</td>
	    <td>GND</td>
	    <td>DGND</td>
	    <td>-</td>
	    <td>Masse</td>
	  </tr>
	  <tr>
	    <td>7</td>
	    <td>GND</td>
	    <td>DGND</td>
	    <td>-</td>
	    <td>Masse</td>
	  </tr>
	  <tr>
	    <td>8</td>
	    <td>VIN</td>
	    <td>VIN</td>
	    <td>-</td>
	    <td>Spannungseingang für VCP-G</td>
	  </tr>
	</table>
</div>

Tabelle 4.7 zeigt die Pinbeschreibung von J8D101.
<p align="center"><strong>Tabelle 4.7 J8D101 Pinbeschreibung</strong></p>
<div align="center">
	<table>
	  <tr>
	    <th rowspan="3"><strong>Pin-Nummer</strong></th>
	    <th colspan="4"><strong>J8D101</strong></th>
	  </tr>
	  <tr>
	    <th rowspan="2"><strong>Port-Name</strong></th>
	    <th rowspan="2"><strong>Signalname</strong></th>
	    <th><strong>DIR</strong></th>
	    <th rowspan="2"><strong>Beschreibung</strong></th>
	  </tr>
	  <tr>
	    <th><strong>MCU ◄► J8D101</strong></th>
	  </tr>
	  <tr>
	    <td>1</td>
	    <td>A0</td>
	    <td>ADC03</td>
	    <td>◄</td>
	    <td>ADC-Signal</td>
	  </tr>
	  <tr>
	    <td>2</td>
	    <td>A1</td>
	    <td>ADC04</td>
	    <td>◄</td>
	    <td>ADC-Signal</td>
	  </tr>
	  <tr>
	    <td>3</td>
	    <td>A2</td>
	    <td>GPIO_AC02</td>
	    <td>◄►</td>
	    <td>GPIO-Signal</td>
	  </tr>
	  <tr>
	    <td>4</td>
	    <td>A3</td>
	    <td>GPIO_AC03</td>
	    <td>◄►</td>
	    <td>GPIO-Signal</td>
	  </tr>
	  <tr>
	    <td>5</td>
	    <td>A4</td>
	    <td>GPIO_AC05</td>
	    <td>◄►</td>
	    <td>GPIO-Signal</td>
	  </tr>
	  <tr>
	    <td>6</td>
	    <td>A5</td>
	    <td>GPIO_AC04</td>
	    <td>◄►</td>
	    <td>GPIO-Signal</td>
	  </tr>
	  <tr>
	    <td>7</td>
	    <td>A6</td>
	    <td>ADC05</td>
	    <td>◄</td>
	    <td>ADC-Signal</td>
	  </tr>
	  <tr>
	    <td>8</td>
	    <td>A7</td>
	    <td>ADC01</td>
	    <td>◄</td>
	    <td>ADC-Signal</td>
	  </tr>
	</table>
</div>

Tabelle 4.8 zeigt die Pinbeschreibung von J8D102.
<p align="center"><strong>Tabelle 4.8 J8D102 Pinbeschreibung</strong></p>
<div align="center">
	<table>
	  <tr>
	    <th rowspan="3"><strong>Pin-Nummer</strong></th>
	    <th colspan="4"><strong>J8D102</strong></th>
	  </tr>
	  <tr>
	    <th rowspan="2"><strong>Port-Name</strong></th>
	    <th rowspan="2"><strong>Signalname</strong></th>
	    <th><strong>DIR</strong></th>
	    <th rowspan="2"><strong>Beschreibung</strong></th>
	  </tr>
	  <tr>
	    <th><strong>MCU ◄► J8D102</strong></th>
	  </tr>
	  <tr>
	    <td>1</td>
	    <td>7</td>
	    <td>GPIO_B01</td>
	    <td>◄►</td>
	    <td>GPIO-Signal</td>
	  </tr>
	  <tr>
	    <td>2</td>
	    <td>6</td>
	    <td>GPIO_A13</td>
	    <td>◄►</td>
	    <td>GPIO-Signal</td>
	  </tr>
	  <tr>
	    <td>3</td>
	    <td>5</td>
	    <td>GPIO_B10</td>
	    <td>◄►</td>
	    <td>GPIO-Signal</td>
	  </tr>
	  <tr>
	    <td>4</td>
	    <td>4</td>
	    <td>GPIO_B27</td>
	    <td>◄►</td>
	    <td>GPIO-Signal</td>
	  </tr>
	  <tr>
	    <td>5</td>
	    <td>3</td>
	    <td>GPIO_B11</td>
	    <td>◄►</td>
	    <td>GPIO-Signal</td>
	  </tr>
	  <tr>
	    <td>6</td>
	    <td>2</td>
	    <td>GPIO_B28</td>
	    <td>◄►</td>
	    <td>GPIO-Signal</td>
	  </tr>
	  <tr>
	    <td>7</td>
	    <td>1</td>
	    <td>GPIO_B25</td>
	    <td>◄►</td>
	    <td>GPIO-Signal</td>
	  </tr>
	  <tr>
	    <td>8</td>
	    <td>0</td>
	    <td>GPIO_B26</td>
	    <td>◄►</td>
	    <td>GPIO-Signal</td>
	  </tr>
	</table>
</div>

Tabelle 4.9 zeigt die Pinbeschreibung von J8D103.
<p align="center"><strong>Tabelle 4.9 J8D103 Pinbeschreibung</strong></p>
<div align="center">
	<table>
	  <tr>
	    <th rowspan="3"><strong>Pin-Nummer</strong></th>
	    <th colspan="4"><strong>J8D103</strong></th>
	  </tr>
	  <tr>
	    <th rowspan="2"><strong>Port-Name</strong></th>
	    <th rowspan="2"><strong>Signalname</strong></th>
	    <th><strong>DIR</strong></th>
	    <th rowspan="2"><strong>Beschreibung</strong></th>
	  </tr>
	  <tr>
	    <th><strong>MCU ◄► J8D103</strong></th>
	  </tr>
	  <tr>
	    <td>1</td>
	    <td>A8</td>
	    <td>GPIO_AC08</td>
	    <td>◄►</td>
	    <td>GPIO- oder ADC-Signal</td>
	  </tr>
	  <tr>
	    <td>2</td>
	    <td>A9</td>
	    <td>GPIO_AC09</td>
	    <td>◄►</td>
	    <td>GPIO- oder ADC-Signal</td>
	  </tr>
	  <tr>
	    <td>3</td>
	    <td>A10</td>
	    <td>GPIO_AC10</td>
	    <td>◄►</td>
	    <td>GPIO- oder ADC-Signal</td>
	  </tr>
	  <tr>
	    <td>4</td>
	    <td>A11</td>
	    <td>GPIO_ADC-2</td>
	    <td>◄</td>
	    <td>ADC-Signal</td>
	  </tr>
	  <tr>
	    <td>5</td>
	    <td>54</td>
	    <td>GPIO_K14</td>
	    <td>◄►</td>
	    <td>GPIO-Signal</td>
	  </tr>
	  <tr>
	    <td>6</td>
	    <td>55</td>
	    <td>GPIO_K15</td>
	    <td>◄►</td>
	    <td>GPIO-Signal</td>
	  </tr>
	  <tr>
	    <td>7</td>
	    <td>56</td>
	    <td>GPIO_K01</td>
	    <td>◄</td>
	    <td>GPIO-Signal</td>
	  </tr>
	  <tr>
	    <td>8</td>
	    <td>57</td>
	    <td>GPIO_K08</td>
	    <td>◄►</td>
	    <td>GPIO-Signal</td>
	  </tr>
	</table>
</div>

Tabelle 4.10 zeigt die Pinbeschreibung von J8D104.
<p align="center"><strong>Tabelle 4.10 J8D104 Pinbeschreibung</strong></p>
<div align="center">
	<table>
	  <tr>
	    <th rowspan="3"><strong>Pin-Nummer</strong></th>
	    <th colspan="4"><strong>J8D104</strong></th>
	  </tr>
	  <tr>
	    <th rowspan="2"><strong>Port-Name</strong></th>
	    <th rowspan="2"><strong>Signalname</strong></th>
	    <th><strong>DIR</strong></th>
	    <th rowspan="2"><strong>Beschreibung</strong></th>
	  </tr>
	  <tr>
	    <th><strong>MCU ◄► J8D104</strong></th>
	  </tr>
	  <tr>
	    <td>1</td>
	    <td>14</td>
	    <td>GPIO_AC00</td>
	    <td>◄►</td>
	    <td>GPIO- oder ADC-Signal</td>
	  </tr>
	  <tr>
	    <td>2</td>
	    <td>15</td>
	    <td>GPIO_AC01</td>
	    <td>◄►</td>
	    <td>GPIO- oder ADC-Signal</td>
	  </tr>
	  <tr>
	    <td>3</td>
	    <td>16</td>
	    <td>GPIO_A06</td>
	    <td>◄►</td>
	    <td>GPIO-Signal</td>
	  </tr>
	  <tr>
	    <td>4</td>
	    <td>17</td>
	    <td>GPIO_A07</td>
		<td>◄►</td>
	    <td>GPIO-Signal</td>
	  </tr>
	  <tr>
	    <td>5</td>
	    <td>18</td>
	    <td>GPIO_A28</td>
	    <td>◄►</td>
	    <td>GPIO-Signal</td>
	  </tr>
	  <tr>
	    <td>6</td>
	    <td>19</td>
	    <td>GPIO_A29</td>
	    <td>◄►</td>
	    <td>GPIO-Signal</td>
	  </tr>
	  <tr>
	    <td>7</td>
	    <td>20</td>
	    <td>GPIO_B03</td>
	    <td>◄►</td>
	    <td>GPIO-Signal</td>
	  </tr>
	  <tr>
	    <td>8</td>
	    <td>21</td>
	    <td>GPIO_B02</td>
	    <td>◄►</td>
	    <td>GPIO-Signal</td>
	  </tr>
	</table>
</div>

Tabelle 4.11 zeigt die Pinbeschreibung von J3D100.
<p align="center"><strong>Tabelle 4.11 J3D100 Pinbeschreibung</strong></p>
<div align="center">
	<table>
	  <tr>
	    <th rowspan="3"><strong>Pin-Nummer</strong></th>
	    <th colspan="4"><strong>J3D100</strong></th>
	  </tr>
	  <tr>
	    <th rowspan="2"><strong>Port-Name</strong></th>
	    <th rowspan="2"><strong>Signalname</strong></th>
	    <th><strong>DIR</strong></th>
	    <th rowspan="2"><strong>Beschreibung</strong></th>
	  </tr>
	  <tr>
	    <th><strong>MCU ◄► J3D100</strong></th>
	  </tr>
	  <tr>
	    <td>1</td>
	    <td>MISO</td>
	    <td>GPIO_B07</td>
	    <td>◄►</td>
	    <td>GPIO-Signal</td>
	  </tr>
	  <tr>
	    <td>2</td>
	    <td>5V</td>
	    <td>VCP_5P0</td>
	    <td>-</td>
	    <td>Stromversorgung 5.0V</td>
	  </tr>
	  <tr>
	    <td>3</td>
	    <td>SCK</td>
	    <td>GPIO_B04</td>
	    <td>◄►</td>
	    <td>GPIO-Signal</td>
	  </tr>
	  <tr>
	    <td>4</td>
	    <td>MOSI</td>
	    <td>GPIO_B06</td>
	    <td>◄►</td>
	    <td>GPIO-Signal</td>
	  </tr>
	  <tr>
	    <td>5</td>
	    <td>CMD</td>
	    <td>GPIO_B05</td>
	    <td>◄►</td>
	    <td>GPIO-Signal</td>
	  </tr>
	  <tr>
	    <td>6</td>
	    <td>GND</td>
	    <td>DGND</td>
	    <td>-</td>
	    <td>Masse</td>
	  </tr>
	</table>
</div>

Tabelle 4.12 zeigt die Pinbeschreibung von J18D100.
<p align="center"><strong>Tabelle 4.12 J18D100 Pinbeschreibung</strong></p>
<div align="center">
	<table>
	  <tr>
	    <th rowspan="3"><strong>Pin-Nummer</strong></th>
	    <th colspan="4"><strong>J18D100</strong></th>
	  </tr>
	  <tr>
	    <th rowspan="2"><strong>Port-Name</strong></th>
	    <th rowspan="2"><strong>Signalname</strong></th>
	    <th><strong>DIR</strong></th>
	    <th rowspan="2"><strong>Beschreibung</strong></th>
	  </tr>
	  <tr>
	    <th><strong>MCU ◄► J18D100</strong></th>
	  </tr>
	  <tr>
	    <td>1</td>
	    <td>5V</td>
	    <td>VCP_5P0</td>
	    <td>-</td>
	    <td>Stromversorgung 5.0V</td>
	  </tr>
	  <tr>
	    <td>2</td>
	   <td>5V</td>
	    <td>VCP_5P0</td>
	    <td>-</td>
	    <td>Stromversorgung 5.0V</td>
	  </tr>
	  <tr>
	    <td>3</td>
	    <td>22</td>
	    <td>GPIO_B24</td>
	    <td>◄►</td>
	    <td>GPIO-Signal</td>
	  </tr>
	  <tr>
	    <td>4</td>
	    <td>23</td>
	    <td>GPIO_B23</td>
	    <td>◄►</td>
	    <td>GPIO-Signal</td>
	  </tr>
	  <tr>
	    <td>5</td>
	    <td>24</td>
	    <td>GPIO_B22</td>
	    <td>◄►</td>
	    <td>GPIO-Signal</td>
	  </tr>
	  <tr>
	    <td>6</td>
	    <td>25</td>
	    <td>GPIO_B21</td>
	    <td>◄►</td>
	    <td>GPIO-Signal</td>
	  </tr>
	  <tr>
	    <td>7</td>
	    <td>26</td>
	    <td>GPIO_B20</td>
	    <td>◄►</td>
	    <td>GPIO-Signal</td>
	  </tr>
	  <tr>
	    <td>8</td>
	    <td>27</td>
	    <td>GPIO_B19</td>
	    <td>◄►</td>
	    <td>GPIO-Signal</td>
	  </tr>
	  <tr>
	    <td>9</td>
	    <td>28</td>
	    <td>GPIO_A30</td>
	    <td>◄►</td>
	    <td>GPIO-Signal</td>
	  </tr>
	  <tr>
	    <td>10</td>
	    <td>29</td>
	    <td>GPIO_A27</td>
	    <td>◄►</td>
	    <td>GPIO-Signal</td>
	  </tr>
	  <tr>
	    <td>11</td>
	    <td>230</td>
	    <td>GPIO_A26</td>
	    <td>◄►</td>
	    <td>GPIO-Signal</td>
	  </tr>
	  <tr>
	    <td>12</td>
	    <td>31</td>
	    <td>GPIO_A24</td>
	    <td>◄►</td>
	    <td>GPIO-Signal</td>
	  </tr>
	  <tr>
	    <td>13</td>
	    <td>32</td>
	    <td>GPIO_A25</td>
	    <td>◄►</td>
	    <td>GPIO-Signal</td>
	  </tr>
	  <tr>
	    <td>14</td>
	    <td>33</td>
	    <td>GPIO_A23</td>
	    <td>◄►</td>
	    <td>GPIO-Signal</td>
	  </tr>
	  <tr>
	    <td>15</td>
	    <td>34</td>
	    <td>GPIO_A22</td>
	    <td>◄►</td>
	    <td>GPIO-Signal</td>
	  </tr>
	  <tr>
	    <td>16</td>
	    <td>35</td>
	    <td>GPIO_A21</td>
	    <td>◄►</td>
		<td>GPIO-Signal</td>
	  </tr>
	  <tr>
	    <td>17</td>
	    <td>36</td>
	    <td>GPIO_A20</td>
	    <td>◄►</td>
	    <td>GPIO-Signal</td>
	  </tr>
	  <tr>
	    <td>18</td>
	    <td>37</td>
	    <td>GPIO_A19</td>
	    <td>◄►</td>
	    <td>GPIO-Signal</td>
	  </tr>
	  <tr>
	    <td>19</td>
	    <td>38</td>
	    <td>GPIO_K13</td>
	    <td>◄►</td>
		<td>GPIO-Signal</td>
	  </tr>
	  <tr>
	    <td>20</td>
	    <td>39</td>
	    <td>GPIO_K12</td>
	    <td>◄►</td>
	    <td>GPIO-Signal</td>
	  </tr>
	  <tr>
	    <td>21</td>
	    <td>40</td>
	    <td>GPIO_K11</td>
	    <td>◄►</td>
	    <td>GPIO-Signal</td>
	  </tr>
	  <tr>
	    <td>22</td>
	    <td>41</td>
	    <td>GPIO_A18</td>
	    <td>◄►</td>
	    <td>GPIO-Signal</td>
	  </tr>
	  <tr>
	    <td>23</td>
	    <td>42</td>
	    <td>GPIO_A17</td>
	    <td>◄►</td>
	    <td>GPIO-Signal</td>
	  </tr>
	  <tr>
	    <td>24</td>
	    <td>43</td>
	    <td>GPIO_A16</td>
	    <td>◄►</td>
	    <td>GPIO-Signal</td>
	  </tr>
	  <tr>
	    <td>25</td>
	    <td>44</td>
	    <td>GPIO_A11</td>
	    <td>◄►</td>
	    <td>GPIO-Signal</td>
	  </tr>
	  <tr>
	    <td>26</td>
	    <td>45</td>
	    <td>GPIO_A10</td>
	    <td>◄►</td>
	    <td>GPIO-Signal</td>
	  </tr>
	  <tr>
	    <td>27</td>
	    <td>46</td>
	    <td>GPIO_A09</td>
	    <td>◄►</td>
	    <td>GPIO-Signal</td>
	  </tr>
	  <tr>
	    <td>28</td>
	    <td>47</td>
	    <td>GPIO_A08</td>
	    <td>◄►</td>
	    <td>GPIO-Signal</td>
	  </tr>
	  <tr>
	    <td>29</td>
	    <td>48</td>
	    <td>GPIO_A05</td>
	    <td>◄►</td>
	    <td>GPIO-Signal</td>
	  </tr>
	  <tr>
	    <td>30</td>
	    <td>49</td>
	    <td>GPIO_A04</td>
	    <td>◄►</td>
	    <td>GPIO-Signal</td>
	  </tr>
	  <tr>
	    <td>31</td>
	    <td>50</td>
	    <td>GPIO_A03</td>
	    <td>◄►</td>
	    <td>GPIO-Signal</td>
	  </tr>
	  <tr>
	    <td>32</td>
	    <td>51</td>
	    <td>GPIO_A02</td>
	    <td>◄►</td>
	    <td>GPIO-Signal</td>
	  </tr>
	  <tr>
	    <td>33</td>
	    <td>52</td>
	    <td>GPIO_A01</td>
	    <td>◄►</td>
	    <td>GPIO-Signal</td>
	  </tr>
	  <tr>
	    <td>34</td>
	    <td>53</td>
	    <td>GPIO_A00</td>
	    <td>◄►</td>
	    <td>GPIO-Signal</td>
	  </tr>
	  <tr>
	    <td>35</td>
	    <td>GND</td>
	    <td>DGND</td>
	    <td>-</td>
	    <td>Masse</td>
	  </tr>
	  <tr>
	    <td>36</td>
	    <td>GND</td>
	    <td>DGND</td>
	    <td>-</td>
	    <td>Masse</td>
	  </tr>
	</table>
</div>

Tabelle 4.13 zeigt die Pinbeschreibung von J5D100.
<p align="center"><strong>Tabelle 4.13 J5D100 Pinbeschreibung</strong></p>
<div align="center">
	<table>
	  <tr>
	    <th rowspan="3"><strong>Pin-Nummer</strong></th>
	    <th colspan="4"><strong>J5D100</strong></th>
	  </tr>
	  <tr>
	    <th rowspan="2"><strong>Port-Name</strong></th>
	    <th rowspan="2"><strong>Signalname</strong></th>
	    <th><strong>DIR</strong></th>
	    <th rowspan="2"><strong>Beschreibung</strong></th>
	  </tr>
	  <tr>
	    <th><strong>MCU ◄► J5D100</strong></th>
	  </tr>
	  <tr>
	    <td>1</td>
	    <td>3.3V</td>
	    <td>VCP_3P3</td>
	    <td>-</td>
	    <td>Stromversorgung 3.3V</td>
	  </tr>
	  <tr>
	    <td>2</td>
	    <td>3.3V</td>
	    <td>VCP_3P3</td>
	    <td>-</td>
    <td>Stromversorgung 3.3V</td>
	  </tr>
	  <tr>
	    <td>3</td>
	    <td>TX0</td>
	    <td>GPIO_K08</td>
	    <td>◄►</td>
	    <td>GPIO-Signal</td>
	  </tr>
	  <tr>
	    <td>4</td>
	    <td>RX0</td>
	    <td>GPIO_K01</td>
	    <td>◄</td>
	    <td>GPIO-Signal</td>
	  </tr>
	  <tr>
	    <td>5</td>
	    <td>TX1</td>
	    <td>GPIO_K09</td>
	    <td>◄►</td>
	    <td>GPIO-Signal</td>
	  </tr>
	  <tr>
	    <td>6</td>
	    <td>RX1</td>
	    <td>GPIO_K02</td>
	    <td>◄</td>
	    <td>GPIO-Signal</td>
	  </tr>
	  <tr>
	    <td>7</td>
	    <td>TX2</td>
	    <td>GPIO_K10</td>
	    <td>◄►</td>
	    <td>GPIO-Signal</td>
	  </tr>
	  <tr>
	    <td>8</td>
	    <td>RX2</td>
	    <td>GPIO_K03</td>
	    <td>◄</td>
	    <td>GPIO-Signal</td>
	  </tr>
	  <tr>
	    <td>9</td>
	    <td>GND</td>
	    <td>DGND</td>
	    <td>-</td>
	    <td>DGND</td>
	  </tr>
	  <tr>
	    <td>10</td>
	    <td>GND</td>
	    <td>DGND</td>
	    <td>-</td>
	    <td>DGND</td>
	  </tr>
	</table>
</div>

Abbildung 4.9 zeigt die gesamte Pinbelegung der zehn Pin-Header auf dem VCP-G.
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Hardware/4.9%20Total%20Pin%20Assignment%20of%20Pin%20Headers%20on%20TOPST%20VCP-G%20Board.png"></p>
<p align="center"><strong>Abbildung 4.9 Gesamte Pinbelegung der Pin-Header auf dem VCP-G </strong><p>

# Referenzen
  - Kontaktieren Sie TOPST für weitere Einzelheiten: topst@topst.ai

**Hinweis:** Referenzdokumente können je nach Vertragsbedingungen bereitgestellt werden, sofern sie verfügbar sind. Wenn die Referenzdokumente nicht verfügbar sind, kann eine Anleitung zu den Inhalten gegeben werden, die direkt mit Ihrer Entwicklung zusammenhängen.
