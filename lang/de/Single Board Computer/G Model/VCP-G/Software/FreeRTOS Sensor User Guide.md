# 1. Einführung
---
Dieses Dokument enthält Richtlinien für die Verwendung des VCP-G mit FreeRTOS. Es umfasst Konfigurationsanweisungen und Beispielcodes, mit denen Sie in der FreeRTOS-Umgebung auf einfache Weise Embedded-Anwendungen mit dem VCP-G entwickeln können.

Insbesondere enthält dieses Dokument Hinweise zu FreeRTOS-basierten Beispielanwendungen für den VCP-G, darunter: 
- Digital Out/In
- SPI
- I2C
- UART
- PWM
- Zusätzliches Beispiel

Siehe Abbildung 1.1, bevor Sie das VCP-G verwenden.
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/vcp-g%20pinout%20Diagram.png"></p>
<p align="center"><strong>Abbildung 1.1 VCP-G Pinout-Diagramm</strong></p>
</br>

Um die einzelnen Beispiele auszuführen, müssen Sie die Datei `main.c` an folgendem Speicherort ändern:
```
$ ~/vcp/sources/app.sample/app.base/main.c
```
Nachdem Sie die erforderlichen Änderungen vorgenommen haben, kompilieren Sie das Projekt mit dem bereitgestellten Makefile, um die Firmware-Binärdatei zu erzeugen.
</br></br></br></br>

# 2. Digital In/Out
---
Dieses Kapitel enthält Beispiele für die Steuerung von LEDs über die digitalen Pins des VCP-G-Boards. Im VCP-G werden digitale Pins zum Senden oder Empfangen von Binärsignalen (HIGH oder LOW) verwendet und sind daher für die Steuerung von Komponenten wie LEDs, Schaltern und Sensoren unverzichtbar. 

Dieses Kapitel enthält zwei Beispielprojekte, die zeigen, wie LEDs und eine Taste über digitale Ausgänge und Eingänge gesteuert werden, und die Ihnen ein grundlegendes Verständnis der Funktionen digitaler Pins vermitteln.
</br></br></br>

## 2.1 Digital Out
---
Dieses Beispiel zeigt, wie LEDs auf einem Breadboard mit dem VCP-G-Board unter FreeRTOS gesteuert werden.  
Die zugehörige Quelldatei finden Sie unter:  

```
$ ~/vcp/sources/app.sample/app.base/main.c
```
Stellen Sie zunächst sicher, dass das VCP-G FreeRTOS SDK korrekt installiert ist. Weitere Informationen zur Installation und Einrichtung finden Sie in der Anleitung VCP-G FreeRTOS SDK Getting Started.

Um dieses Beispiel umzusetzen, ändern Sie die Datei main.c, um die mit den LEDs verbundenen GPIO-Pins als digitale Ausgänge zu konfigurieren. Es sollte ein FreeRTOS-Task erstellt werden, der vier LEDs nacheinander einschaltet und sie anschließend in umgekehrter Reihenfolge wieder ausschaltet. Jeder LED-Übergang sollte eine Verzögerung von 500 ms enthalten, damit die Abfolge deutlich zu erkennen ist.
</br></br>

### 2.1.1 Hardware-Anforderungen  
- VCP-G-Board (x1)
- Breadboard (x1)
- LED (x4)
- 12V 1A Netzteil (x1)
- USB-Type-C-auf-A-Kabel (x1) 
- Jumperkabel Stecker auf Stecker (x9)
</br></br>

### 2.1.2 Schaltung
- LED01
    - Der Pin (+) ist mit Pin 7 des VCP-G-Boards verbunden.
    - Der Pin (–) ist mit der GND-Schiene auf dem Breadboard verbunden.
- LED02
    - Der Pin (+) ist mit Pin 6 des VCP-G-Boards verbunden.
    - Der Pin (–) ist mit der GND-Schiene auf dem Breadboard verbunden.
- LED03
    - Der Pin (+) ist mit Pin 5 des VCP-G-Boards verbunden.
    - Der Pin (–) ist mit der GND-Schiene auf dem Breadboard verbunden.
- LED04
    - Der Pin (+) ist mit Pin 4 des VCP-G-Boards verbunden.
    - Der Pin (–) ist mit der GND-Schiene auf dem Breadboard verbunden. 

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/F_digital_out.png" width="600"></p>
<p align="center"><strong>Abbildung 2.1 Schaltplan vcp4LED</strong></p>

#### 2.1.2.1 Pinbelegung
Die folgende Tabelle zeigt die Pinbelegung.

<p align="center"><strong>Tabelle 2.1 Pinbelegung von vcp4LED</strong></p>
<div align="center">	
	<table>
		<tr>
			<th colspan="3">Pinname</th>
	        <th>VCP-G-Board</th>
	        <th>GPIO</th>
	    </tr>
	    <tr>
	        <td colspan="3">LED01 (+)-Pin</td>
	        <td>7</td>
	        <td>B[01]</td>
	    </tr>
	        <tr>
	        <td colspan="3">LED02 (+)-Pin</td>
	        <td>6</td>
	        <td>A[13]</td>
	    </tr>
	        <tr>
	        <td colspan="3">LED03 (+)-Pin</td>
	        <td>5</td>
	        <td>B[10]</td>
	    </tr>
	        <tr>
	        <td colspan="3">LED04 (+)-Pin</td>
	        <td>4</td>
	        <td>B[27]</td>
	    </tr>
	</table>
</div>
</br></br>

### 2.1.3 Ausführung
Um dieses Beispiel auszuführen, ändern Sie **Main_StartTask()** in der Datei main.c wie dargestellt.
```
#include <gpio.h>
static void Main_StartTask(void * pArg)
{
    (void)pArg;
    (void)SAL_OsInitFuncs();

    uint32 led_pins[4] = {
        GPIO_GPB(1),
        GPIO_GPA(13),
        GPIO_GPB(10),
        GPIO_GPB(27)
    };

    for (int i = 0; i < 4; i++) {
        GPIO_Config(led_pins[i], (GPIO_FUNC(0) | GPIO_OUTPUT));
        GPIO_Set(led_pins[i], 1); 
    }

    while (1) {
        for (int i = 0; i < 4; i++) {
            GPIO_Set(led_pins[i], 0); 
            SAL_TaskSleep(500);
        }
        for (int i = 3; i >= 0; i--) {
            GPIO_Set(led_pins[i], 1); 
            SAL_TaskSleep(500);
        }
    }
}
```
Wechseln Sie nach dem Bearbeiten des Codes in das folgende Verzeichnis und führen Sie den Build-Befehl aus:  
```
$ cd ~/vcp/build/tcc70xx/gcc
$ make
```
Dadurch wird ein Firmware-Image erzeugt und mit dem Tool ***FWDN*** auf den VCP-G geflasht.  
Nachdem der Code erfolgreich geflasht und ausgeführt wurde, leuchten die vier angeschlossenen LEDs nacheinander von LED01 bis LED04 auf und erlöschen anschließend in umgekehrter Reihenfolge. Jeder Übergang erfolgt mit einer Verzögerung von 500 ms, wodurch ein gleichmäßiges Blinkmuster entsteht.
</br></br></br>

## 2.2 Digital In
---
Dieses Beispiel zeigt, wie mit dem VCP-G-Board unter FreeRTOS die Eingabe eines Tasters gelesen und damit eine LED gesteuert wird.
Die zugehörige Quelldatei finden Sie unter:
``` 
$ ~/vcp/sources/app.sample/app.base/main.c
```
Um dieses Beispiel umzusetzen, ändern Sie main.c, um einen GPIO-Pin als digitalen Eingang (mit einer Taste verbunden) und vier GPIO-Pins als digitale Ausgänge (mit LEDs verbunden) zu konfigurieren.  
Ein FreeRTOS-Task überwacht kontinuierlich den Zustand der Taste; wenn die Taste gedrückt wird, leuchten LED1 und LED3 auf.
Wenn die Taste nicht gedrückt wird, leuchten stattdessen LED2 und LED4 auf.
</br></br>

### 2.2.1 Hardware-Anforderungen
- VCP-G-Board (x1)
- Breadboard (x1)
- LED (x4)
- Tastschalter (Sensor) (x1)
- 12V 1A Netzteil (x1)
- USB-Type-C-auf-A-Kabel (x1)
- Jumper-Kabel Stecker auf Stecker (x11)
</br></br>

### 2.2.2 Schaltung
- LED01
    - Der Pin (+) ist mit Pin 7 des VCP-G-Boards verbunden.
    - Der Pin (–) ist mit der GND-Schiene auf dem Breadboard verbunden.
- LED02
    - Der Pin (+) ist mit Pin 6 des VCP-G-Boards verbunden.
    - Der Pin (–) ist mit der GND-Schiene auf dem Breadboard verbunden.
- LED03
    - Der Pin (+) ist mit Pin 5 des VCP-G-Boards verbunden.
    - Der Pin (–) ist mit der GND-Schiene auf dem Breadboard verbunden.
- LED04
    - Der Pin (+) ist mit Pin 4 des VCP-G-Boards verbunden.
    - Der Pin (–) ist mit der GND-Schiene auf dem Breadboard verbunden. 
- Tasterschalter
    - Ein Anschlussbein des Tasters ist mit Pin 2 des VCP-G-Boards verbunden.
    - Das diagonal gegenüberliegende Anschlussbein der Taste ist mit der Stromschiene auf dem Breadboard verbunden.

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/F_digital_in.png" width="600"></p>
<p align="center"><strong>Abbildung 2.2 Schaltplan vcp4LED_Button</strong></p>

#### 2.2.2.1 Pinbelegung
Die folgende Tabelle zeigt die Pinbelegung.

<p align="center"><strong>Tabelle 2.2 Pinbelegung von vcp4LED_Button</strong></p>
<div align="center">
	<table>
	    <tr>
	        <th colspan="3">Pinname</th>
	        <th>VCP-G-Board</th>
	        <th>GPIO</th>
	    </tr>
	    <tr>
	        <td colspan="3">LED01 (+)-Pin</td>
	        <td>7</td>
	        <td>B[01]</td>
	    </tr>
	        <tr>
	        <td colspan="3">LED02 (+)-Pin</td>
	        <td>6</td>
	        <td>A[13]</td>
	    </tr>
	        <tr>
	        <td colspan="3">LED03 (+)-Pin</td>
	        <td>5</td>
	        <td>B[10]</td>
	    </tr>
	        <tr>
	        <td colspan="3">LED04 (+)-Pin</td>
	        <td>4</td>
	        <td>B[27]</td>
	    </tr>
	    </tr>
	        <tr>
	        <td colspan="3">Ein Anschlussbein-Pin der Taste</td>
	        <td>2</td>
	        <td>B[28]</td>
	    </tr>
	</table>
</div>
</br></br>

### 2.2.3 Ausführung
Um dieses Beispiel auszuführen, ändern Sie **Main_StartTask()** in der Datei main.c wie dargestellt.
```
#include <gpio.h>
static void Main_StartTask(void *pArg)
{
    (void)pArg;
    SAL_OsInitFuncs();

    uint32 led_pins[4] = {
        GPIO_GPB(1),   
        GPIO_GPA(13),  
        GPIO_GPB(10),  
        GPIO_GPB(27)   
    };

    uint32 btn_pin = GPIO_GPB(28);   
    for (int i = 0; i < 4; i++) {
        GPIO_Config(led_pins[i], GPIO_FUNC(0) | GPIO_OUTPUT);
        GPIO_Set(led_pins[i], 0); 
    }

    GPIO_Config(btn_pin, GPIO_FUNC(0) | GPIO_INPUT | GPIO_INPUTBUF_EN | GPIO_PULLDN);

    while (1) {
        int btn = GPIO_Get(btn_pin);
        if (btn == 1) {
            GPIO_Set(led_pins[0], 1);  
            GPIO_Set(led_pins[1], 0);  
            GPIO_Set(led_pins[2], 1);  
            GPIO_Set(led_pins[3], 0);  
        } else {
            GPIO_Set(led_pins[0], 0);  
            GPIO_Set(led_pins[1], 1); 
            GPIO_Set(led_pins[2], 0);  
            GPIO_Set(led_pins[3], 1); 
        }
        SAL_TaskSleep(50);  
    }
}
```
Wechseln Sie nach dem Bearbeiten des Codes in das folgende Verzeichnis und führen Sie den Build-Befehl aus:  
```
$ cd ~/vcp/build/tcc70xx/gcc
$ make
```
Dadurch wird ein Firmware-Image erzeugt und mit dem Tool ***FWDN*** auf den VCP-G geflasht.  
Nachdem der Code erfolgreich geflasht und ausgeführt wurde, leuchten beim Drücken der Taste LED01 und LED03 auf, während beim Loslassen der Taste LED02 und LED04 aufleuchten.
Das System überwacht den Zustand der Taste kontinuierlich und aktualisiert den LED-Status in Echtzeit mit einem Abfrageintervall von 50 ms.
</br></br></br></br>

# 3. VCP-G I2C
---
Dieses Kapitel enthält Anweisungen zur Konfiguration der Inter-integrated Circuit (I2C)-Kommunikation auf dem VCP-G unter FreeRTOS.  
I2C ist ein synchrones Zweidraht-Kommunikationsprotokoll für den effizienten Datenaustausch zwischen mehreren Geräten. Es arbeitet mit einer seriellen Datenleitung (SDA) und einer seriellen Taktleitung (SCL), sodass mehrere Peripheriegeräte über eindeutige Adressen mit einem Mikrocontroller kommunizieren können. I2C unterstützt sowohl die Master-Slave-Kommunikation als auch Multi-Master-Konfigurationen und eignet sich damit ideal für den Anschluss von Sensoren, Displays und anderen langsamen Geräten bei minimaler Anzahl erforderlicher Verbindungen.
</br></br></br>

## 3.1 vcpI2C_LCD1602
---
Dieses Beispielprogramm zeigt, wie das VCP-G-Board über das I2C-Kommunikationsprotokoll ein LCD1602-Display steuert. Das LCD1602 ist ein Flüssigkristalldisplay mit 16 Zeichen und 2 Zeilen, das häufig in Embedded-System-Projekten eingesetzt wird. Durch die Verwendung der Bibliothek LiquidCrystal_I2C sendet das Board Befehle und Daten über den I2C-Bus, um das Display effizient zu steuern.  
In diesem Beispiel wird das LCD initialisiert und die Hintergrundbeleuchtung für eine gute Lesbarkeit aktiviert. Anschließend positioniert das Programm den Cursor, um den Text "Hello TOPST" auf dem Bildschirm anzuzeigen.
</br></br>

### 3.1.1 Hardware-Anforderungen
- VCP-G-Board (x1)
- LCD1602 (x1)
- 12V 1A Netzteil (x1)
- USB-Type-C-auf-A-Kabel (x1)
- Jumperkabel Stecker auf Buchse (x4)
</br></br>

### 3.1.2 Schaltung
- LCD1602
    - Der VCC-Pin des LCD1602 ist mit dem analogen Pin 5V auf dem VCP-G-Board verbunden.
    - Der GND-Pin des LCD1602 ist mit GND auf dem VCP-G-Board verbunden.
    - Der SDA-Pin des LCD1602 ist mit Pin 7 des VCP-G-Boards verbunden.
    - Der SCL-Pin des LCD1602 ist mit Pin 8 des VCP-G-Boards verbunden.

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/F_i2c.png" width="600"></p>
<p align="center"><strong>Abbildung 3.1 Schaltplan vcpI2C_LCD1602</strong></p>

#### 3.1.2.1 Pinbelegung
Die folgende Tabelle zeigt die Pinbelegung.

<p align="center"><strong>Tabelle 3.1 Pinbelegung von vcpI2C_LCD1602</strong></p>
<div align="center">
	<table>
	    <tr>
	        <th colspan="3">Pinname</th>
	        <th>VCP-G-Board</th>
	        <th>GPIO</th>
	    </tr>
	    <tr>
	        <td colspan="3">VCC-Pin des LCD1602</td>
	        <td>5V</td>
	        <td>-</td>
	    </tr>
	        <tr>
	        <td colspan="3">GND-Pin des LCD1602</td>
	        <td>GND</td>
	        <td>-</td>
	    </tr>
	        <tr>
	        <td colspan="3">SDA-Pin des LCD1602</td>
	        <td>7</td>
	        <td>B[01]</td>
	    </tr>
	        <tr>
	        <td colspan="3">LED (-) Pin</td>
	        <td>8</td>
	        <td>B[00]</td>
	    </tr>
	</table>
</div>

</br></br>

### 3.1.3 Ausführung
Um dieses Beispiel auszuführen, ändern Sie **Main_StartTask()** in der Datei main.c wie dargestellt.
```
#include <i2c.h>
#include <lcd.h>
static void Main_StartTask(void * pArg)
{
    {
        (void)pArg;
        SAL_OsInitFuncs();

        I2C_Init();
        if (I2C_Open(I2C_CH, I2C_PORT, I2C_SPEED, NULL, NULL) != SAL_RET_SUCCESS) {
            mcu_printf("I2C open failed\n");
            return;
        }
        uint32 detected_addr = I2C_ScanSlave(I2C_CH);
        mcu_printf("Detected I2C Slave Address: 0x%02X\n", detected_addr);

        lcd_init();
        lcd_cmd(0x80);
        lcd_print("Hello TOPST");
        while (1) {
            SAL_TaskSleep(1000);
        }
    }
}
```
#### Zusätzliche Konfigurationshinweise
Um den LCD-Test über I2C zu aktivieren, führen Sie die folgenden Schritte aus:  

**1. lcd.c im Build-System aktivieren**  
- Navigieren Sie zu folgendem Pfad:
```
$ vi ~/vcp/sources/dev.drivers/i2c/rules.mk
```
- Suchen Sie die folgende Zeile:
```
#SRCS += lcd.c
```
- Heben Sie die Auskommentierung der Zeile auf, um die Datei zu aktivieren:
```
SRCS += lcd.c
```

**2. LCD-Funktionslogik prüfen oder ändern**  
Wenn Sie die Logik für die LCD-Initialisierung, Befehle oder Ausgabefunktionen prüfen oder bearbeiten möchten, siehe:
```
$ vi ~/vcp/sources/dev.drivers/i2c/lcd.c
```

**3. I2C-Kanal und Port konfigurieren**  
Die I2C-Kanalnummer und der zugehörige Port, die vom LCD verwendet werden, können hier geändert werden:
```
$ vi ~/vcp/sources/dev.drivers/i2c/lcd.h
```

Wechseln Sie nach dem Bearbeiten des Codes in das folgende Verzeichnis und führen Sie den folgenden Build-Befehl aus:  
```
$ cd ~/vcp/build/tcc70xx/gcc
$ make
```
Dadurch wird ein Firmware-Image erzeugt und mit dem Tool ***FWDN*** auf den VCP-G geflasht.  
Nachdem der Code erfolgreich geflasht und ausgeführt wurde, zeigt das LCD die Meldung "Hello TOPST" auf dem Bildschirm an. Damit ist bestätigt, dass die I2C-Kommunikation ordnungsgemäß funktioniert.  
</br></br></br></br>

# 4. VCP SPI
---
In diesem Kapitel wird beschrieben, wie die Kommunikation über das Serial Peripheral Interface (SPI) auf dem VCP-G konfiguriert wird.  
SPI ist ein schnelles, synchrones Kommunikationsprotokoll, das zum Datenaustausch zwischen Mikrocontrollern und Peripheriegeräten verwendet wird. Es arbeitet mit separaten Leitungen für die Datenübertragung (MOSI und MISO), die Taktsynchronisation (SCK) und die Geräteauswahl (SS) und gewährleistet so eine effiziente und zuverlässige Kommunikation.  
</br></br></br>

## 4.1 vcpSPI_Dot8x8
---
Dieses Beispielprogramm zeigt, wie das VCP-G-Board über SPI mit dem MAX7219-Treiber eine 8x8-LED-Dot-Matrix steuert.
In diesem Beispiel wird ein vordefiniertes Binär-Array verwendet, um den Buchstaben "X" auf der Dot-Matrix anzuzeigen. Die Anzeige wird über die SPI-Kommunikation aktualisiert, und der MAX7219 übernimmt intern die Zeilen- und Spaltensteuerung.
Dieses Beispiel veranschaulicht, wie Datenmuster über SPI gesendet werden, um externe Anzeigegeräte wie LED-Matrizen zu steuern.
</br></br>

### 4.1.1 Hardware-Anforderungen
- VCP-G-Board (x1)
- 8x8-Dotmatrix (x1)
- 12V 1A Netzteil (x1)
- USB-Type-C-auf-A-Kabel (x1)
- Jumperkabel Stecker auf Buchse (x2)
- Buchse-auf-Buchse-Jumperkabel (x3)
</br></br>

### 4.1.2 Schaltung
- 8x8-Dot-Matrix
    - Der VCC-Pin der 8x8-Dotmatrix ist mit dem analogen Pin 5V auf dem VCP-G-Board verbunden.
    - Der GND-Pin der 8x8-Dotmatrix ist mit GND auf dem VCP-G-Board verbunden.
    - Der DIN-Pin der 8x8-Dot-Matrix ist mit SPI-Pin 4 des VCP-G-Boards verbunden.
    - Der CS-Pin der 8x8-Dot-Matrix ist mit SPI-Pin 5 des VCP-G-Boards verbunden.
    - Der CLS-Pin der 8x8-Dot-Matrix ist mit SPI-Pin 3 des VCP-G-Boards verbunden.

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/F_spi.png" width="600"></p>
<p align="center"><strong>Abbildung 4.1 Schaltplan von vcpSPI_Dot8x8</strong></p>

#### 4.1.2.1 Pinbelegung
Die folgende Tabelle zeigt die Pinbelegung.

<p align="center"><strong>Tabelle 4.1 Pinbelegung von vcpSPI_Dot8x8</strong></p>
<div align="center">
	<table>
	    <tr>
	        <th colspan="3">Pinname</th>
	        <th>VCP-G-Board</th>
	        <th>GPIO</th>
	    </tr>
	    <tr>
	        <td colspan="3">VCC-Pin der 8x8-Dotmatrix</td>
	        <td>5V</td>
	        <td>-</td>
	    </tr>
	        <tr>
	        <td colspan="3">GND-Pin der 8x8-Dotmatrix</td>
	        <td>GND</td>
	        <td>-</td>
	    </tr>
	    <tr>
	        <td colspan="3">DIN-Pin der 8x8-Dotmatrix</td>
	        <td>SPI 4</td>
	        <td>B[06]</td>
	    </tr>
	    <tr>
	        <td colspan="3">CS-Pin der 8x8-Dotmatrix</td>
	        <td>SPI 5</td>
	        <td>B[05]</td>
	    </tr>
	    <tr>
	        <td colspan="3">CLK-Pin der 8x8-Dotmatrix</td>
	        <td>SPI 3</td>
	        <td>B[04]</td>
	    </tr>
	</table>
</div>
</br></br>

### 4.1.3 Ausführung
Um dieses Beispiel auszuführen, ändern Sie **Main_StartTask()** in der Datei main.c wie dargestellt.
```
#include <dot_matrix.h>
static void Main_StartTask(void * pArg)
{
    {
        (void)pArg;
        SAL_OsInitFuncs();
   
        mcu_printf("[MAX7219] Init Start\n");
        MAX7219_Init();
        SAL_TaskSleep(200);
        MAX7219_XPattern();
   
        while (1) {
            SAL_TaskSleep(1000);
        }
    }
}
```
#### Zusätzliche Konfigurationshinweise
Um den Dot-Matrix-Test über SPI zu aktivieren, führen Sie die folgenden Schritte aus:  
**1. dot_matrix.c im Build-System aktivieren**  
- Navigieren Sie zu folgendem Pfad:
```
$ vi ~/vcp/sources/dev.drivers/gpsb/rules.mk
```
- Suchen Sie die Zeile:
```
#SRCS += dot_matrix.c
```
- Heben Sie die Auskommentierung auf, um die Datei zu aktivieren:
```
SRCS += dot_matrix.c
```
**2. Dot-Matrix-Funktionslogik prüfen oder ändern**  
Um die Logik für die Dot-Matrix-Initialisierung, Steuerbefehle oder Anzeigemuster zu prüfen oder zu bearbeiten, siehe die folgende Quelldatei:
```
$ vi ~/vcp/sources/dev.drivers/gpsb/dot_matrix.c
```
**3. SPI-Kanal und GPIOs konfigurieren**  
Der SPI-Kanal und die zugehörigen GPIO-Pins, die von der Dot-Matrix verwendet werden, können in der folgenden Header-Datei konfiguriert werden:
```
$ vi ~/vcp/sources/dev.drivers/gpsb/dot_matrix.h
```
Wechseln Sie nach dem Bearbeiten des Codes in das folgende Verzeichnis und führen Sie den Build-Befehl aus:  
```
$ cd ~/vcp/build/tcc70xx/gcc
$ make
```
Dadurch wird ein Firmware-Image erzeugt und mit dem Tool ***FWDN*** auf den VCP-G geflasht.  
Nachdem der Code erfolgreich geflasht und ausgeführt wurde, zeigt die 8x8-LED-Dot-Matrix den Buchstaben "X" an. Damit ist bestätigt, dass die SPI-Kommunikation mit dem MAX7219-Treiber korrekt funktioniert. 
</br></br></br></br>

# 5. VCP-G UART
---
In diesem Kapitel wird beschrieben, wie die Kommunikation über den Universal Asynchronous Receiver-Transmitter (UART) auf dem VCP-G konfiguriert wird.  
UART ist ein weit verbreitetes serielles Kommunikationsprotokoll, das Daten asynchron über nur zwei Leitungen überträgt: Transmit (TX) und Receive (RX). Es ist unverzichtbar für den Datenaustausch zwischen Mikrocontrollern, Sensoren und Computern, ohne dass ein gemeinsames Taktsignal erforderlich ist.  
In den folgenden Kapiteln wird beschrieben, wie Daten über UART gesendet und empfangen werden.
</br></br></br>

## 5.1 UART-Kommunikationstest (FT232BL)
---
Dieses Beispiel zeigt, wie die UART-Kommunikation auf dem VCP-G-Board mit dem seriellen FT232BL-USB-zu-TTL-Modul überprüft wird.
Die UART-TX- und -RX-Pins des VCP-G-Boards sind mit dem FT232BL-Modul verbunden, das wiederum über USB an einen PC angeschlossen ist.
Auf dem PC wird ein Terminalprogramm wie MobaXterm verwendet, um die übertragenen Meldungen anzuzeigen.
</br></br>

### 5.1.1 Hardware-Anforderungen
- VCP-G-Board (x1)
- Serielles FT232BL-USB-zu-TTL-Modul (x1)
- Mini-USB-Kabel (x1)
- 12V 1A Netzteil (x1)
- USB-Type-C-auf-A-Kabel (x1)
- Jumperkabel Stecker auf Buchse (x2)
</br></br>

### 5.1.2 Schaltung
- FT232BL
    - Der RXD-Pin des FT232BL-Moduls ist mit Pin 18 (TXD) des VCP-G-Boards verbunden.
    - Der TXD-Pin des FT232BL-Moduls ist mit Pin 19 (RXD) des VCP-G-Boards verbunden.

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/F_uart.png" width="600"></p>
<p align="center"><strong>Abbildung 5.1 Schaltplan vcpUART</strong></p>

#### 5.1.2.1 Pinbelegung
Die folgende Tabelle zeigt die Pinbelegung.

<p align="center"><strong>Tabelle 4.1 Pinbelegung von vcpUART</strong></p>
<div align="center">
	<table>
	    <tr>
	        <th colspan="3">Pinname</th>
	        <th>VCP-G-Board</th>
	        <th>GPIO</th>
	    </tr>
	    <tr>
	        <td colspan="3">FT232BL RXD</td>
	        <td>18</td>
	        <td>A[28]</td>
	    </tr>
	        <tr>
	        <td colspan="3">FT232BL TXD</td>
	        <td>19</td>
	        <td>A[29]</td>
	    </tr>
	</table>
</div>
</br></br>

### 5.1.3 Ausführung
Um dieses Beispiel auszuführen, ändern Sie **Main_StartTask()** in der Datei main.c wie dargestellt.
```
#include <uart_example.h>
void Main_StartTask(void *pArg)
{
    (void)pArg;
    (void)SAL_OsInitFuncs();

    UART_Test();

    while (1) {
        SAL_TaskSleep(1000);
    }
}
```
#### Zusätzliche Konfigurationshinweise
Um den UART-Test zu aktivieren, führen Sie die folgenden Schritte aus:  
**1. uart_example.c im Build-System aktivieren**  
- Navigieren Sie zu folgendem Pfad:
```
$ vi ~/vcp/sources/dev.drivers/uart/rules.mk
```
- Suchen Sie die Zeile:
```
#SRCS += uart_example.c
```
- Heben Sie die Auskommentierung auf, um die Datei zu aktivieren:
```
SRCS += uart_example.c
```
**2. UART-Funktionslogik prüfen oder ändern**  
Um die Logik für die UART-Initialisierung, das Senden/Empfangen von Daten oder die Interrupt-Behandlung zu prüfen oder zu bearbeiten, siehe die folgende Quelldatei:
```
$ vi ~/vcp/sources/dev.drivers/uart/tcc70xx/uart_example.c
```
**3. UART-Kanal und GPIOs konfigurieren**  
Der UART-Kanal, die Baudrate und die zugehörigen TX/RX-GPIO-Pins, die für den UART-Test verwendet werden, können in der folgenden Header-Datei konfiguriert werden:
```
$ vi ~/vcp/sources/dev.drivers/uart/uart_example.h
```
Wechseln Sie nach dem Bearbeiten des Codes in das folgende Verzeichnis und führen Sie den Build-Befehl aus:  
```
$ cd ~/vcp/build/tcc70xx/gcc
$ make
```
Dadurch wird ein Firmware-Image erzeugt und mit dem Tool ***FWDN*** auf den VCP-G geflasht.  
Nachdem der Code erfolgreich geflasht und ausgeführt wurde, erscheint die Meldung "[UART] Hello from UART!" einmal im seriellen Terminal. Damit ist bestätigt, dass die UART-Übertragung vom VCP-G-Board über das FT232BL-USB-zu-TTL-Modul ordnungsgemäß funktioniert.
</br></br></br></br>

# 6. VCP-G PWM
---
Dieses Kapitel enthält Anweisungen zur Konfiguration der Pulsweitenmodulation (PWM) auf dem VCP-G. PWM ist ein Verfahren, mit dem die an Geräte wie Motoren, LEDs und Summer abgegebene Leistung durch Variation des Tastverhältnisses eines digitalen Signals gesteuert wird. Dabei wird der Ausgangspin mit hoher Frequenz ein- und ausgeschaltet, wobei das Verhältnis von Einschaltzeit zur Gesamtperiode den effektiven Ausgangspegel bestimmt. In den folgenden Kapiteln wird beschrieben, wie PWM-Signale mit FreeRTOS auf dem VCP-G erzeugt und zur Steuerung externer Komponenten eingesetzt werden.
</br></br></br>

## 6.1 pwmFade
---
Dieses Beispielprogramm zeigt, wie das VCP-Board mithilfe von PWM eine LED auf dem Breadboard steuert, indem es deren Helligkeit in einer Schleife schrittweise erhöht und verringert. Nachdem die LED ihre maximale Helligkeit erreicht hat, beginnt die Helligkeit der LED abzunehmen. Das Programm passt die Helligkeit der LED kontinuierlich an und erzeugt so einen Fading-Effekt.
</br></br>

### 6.1.1 Hardware-Anforderungen
- VCP-G-Board (x1)
- Breadboard (x1)
- LED (x1)
- 12V 1A Netzteil (x1)
- USB-Type-C-auf-A-Kabel (x1)
- Jumperkabel Stecker auf Stecker (x2)
</br></br>

### 6.1.2 Schaltung
- LED
    - Der Pin (+) ist mit Pin 45 des VCP-G-Boards verbunden.
    - Der Pin (–) ist mit der GND-Schiene auf dem Breadboard verbunden.

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/F_pwm.png" width="600"></p>
<p align="center"><strong>Abbildung 5.1 Schaltplan pwmFade</strong></p>

#### 6.1.2.1 Pinbelegung
Die folgende Tabelle zeigt die Pinbelegung.

<p align="center"><strong>Tabelle 4.1 Pinbelegung von pwmFade</strong></p>
<div align="center">
	<table>
	    <tr>
	        <th colspan="3">Pinname</th>
	        <th>VCP-G-Board</th>
	        <th>GPIO</th>
	    </tr>
	    <tr>
	        <td colspan="3">LED</td>
	        <td>45</td>
	        <td>A[10]</td>
	    </tr>
	</table>
</div>
</br></br>

### 6.1.3 Ausführung
Um dieses Beispiel auszuführen, ändern Sie **Main_StartTask()** in der Datei main.c wie dargestellt.
```
#include <gpio.h>
#include <pdm.h>
void Main_StartTask(void * pArg)
{
    PDMModeConfig_t pwm_cfg;
    uint32 duty_ns;
    uint32 wait_cnt;

    PDM_Init();

    pwm_cfg.mcPortNumber      = GPIO_PERICH_CH0;  // GPIO A10
    pwm_cfg.mcOperationMode   = PDM_OUTPUT_MODE_PHASE_1;
    pwm_cfg.mcInversedSignal  = 0;
    pwm_cfg.mcOutSignalInIdle = 0;
    pwm_cfg.mcLoopCount       = 0;
    pwm_cfg.mcOutputCtrl      = 0;

    pwm_cfg.mcPeriodNanoSec1  = 1000000; 
    pwm_cfg.mcDutyNanoSec2    = 0;
    pwm_cfg.mcPeriodNanoSec2  = 0;

    while (1)
    {
        // Fade-in
        for (duty_ns = 0; duty_ns <= pwm_cfg.mcPeriodNanoSec1; duty_ns += 10000)
        {
            pwm_cfg.mcDutyNanoSec1 = duty_ns;
            PDM_Disable(0, PMM_ON);
            wait_cnt = 0;
            while (PDM_GetChannelStatus(0))
            {
                SAL_TaskSleep(1); 
                wait_cnt++;
                if (wait_cnt > 100)
                {
                    mcu_printf("Timeout waiting for PDM to disable\n");
                    break;
                }
            }
            if (PDM_SetConfig(0, &pwm_cfg) != SAL_RET_SUCCESS)
            {
                mcu_printf("PDM_SetConfig failed\n");
                return;
            }
            if (PDM_Enable(0, PMM_ON) != SAL_RET_SUCCESS)
            {
                mcu_printf("PDM_Enable failed\n");
                return;
            }
            SAL_TaskSleep(10);
        }
        // Fade-out
        for (duty_ns = pwm_cfg.mcPeriodNanoSec1; duty_ns > 0; duty_ns -= 10000)
        {
            pwm_cfg.mcDutyNanoSec1 = duty_ns;

            PDM_Disable(0, PMM_ON);

            wait_cnt = 0;
            while (PDM_GetChannelStatus(0))
            {
                SAL_TaskSleep(1);
                wait_cnt++;
                if (wait_cnt > 100)
                {
                    mcu_printf("Timeout waiting for PDM to disable\n");
                    break;
                }
            }

            if (PDM_SetConfig(0, &pwm_cfg) != SAL_RET_SUCCESS)
            {
                mcu_printf("PDM_SetConfig failed\n");
                return;
            }
            if (PDM_Enable(0, PMM_ON) != SAL_RET_SUCCESS)
            {
                mcu_printf("PDM_Enable failed\n");
                return;
            }
            SAL_TaskSleep(10);
        }
    }
}
```
Wechseln Sie nach dem Bearbeiten des Codes in das folgende Verzeichnis und führen Sie den Build-Befehl aus:  
```
$ cd ~/vcp/build/tcc70xx/gcc
$ make
```
Dadurch wird ein Firmware-Image erzeugt und mit dem Tool ***FWDN*** auf den VCP-G geflasht.  
Nachdem der Code erfolgreich geflasht und ausgeführt wurde, können Sie einen allmählichen Ein- und Ausblendeffekt der LED beobachten, der über PWM an GPIO A10 gesteuert wird. Damit ist bestätigt, dass die PDM-basierte PWM-Ausgabe des VCP-G korrekt funktioniert.

**Hinweis**: Um den für die PWM-Ausgabe verwendeten GPIO-Port zu ändern, siehe die Konfiguration in der Datei pdm.c.
</br></br></br></br>

# 7. Weitere Beispiele
---
Dieses Kapitel stellt weitere Sensorbeispiele mit FreeRTOS auf dem VCP-G-Board vor. Es enthält Beispielanleitungen zur Verwendung gängiger Arduino-Sensoren mit FreeRTOS auf dem VCP-G-Board, damit Sie verschiedene Sensoren effektiv in Ihre Projekte integrieren können.
</br></br></br>

## 7.1 Infrarotsensor (IR) (Transceiver)
---
Dieses Beispiel zeigt, wie das VCP-G-Board einen IR-Sensor und zwei LEDs auf einem Breadboard steuert. Wenn der IR-Sensor ein Objekt erkennt (Sensorwert ist LOW), leuchtet die erste LED auf und die zweite LED erlischt. Umgekehrt leuchtet die zweite LED auf und die erste LED erlischt, wenn kein Objekt erkannt wird (Sensorwert ist HIGH). Das Vorhandensein oder Fehlen eines Objekts wird außerdem auf dem seriellen Monitor ausgegeben.
</br></br>

### 7.1.1 Hardware-Anforderungen
- VCP-G-Board (x1)
- Breadboard (x1)
- IR-Transceiver-Sensor (x1)
- LED (x2: Unterschiedliche Farben werden empfohlen)
- 12V 1A Netzteil (x1)
- USB-Type-C-auf-A-Kabel (x1)
- Jumper-Kabel Stecker auf Stecker (x5)
- Jumperkabel Stecker auf Buchse (x3)
</br></br>

### 7.1.2 Schaltung
- IR-Transceiver-Sensor
    - Der OUT-Pin des IR-Sensors ist mit Pin 38 des VCP-G-Boards verbunden.
    - Der VCC-Pin des IR-Sensors ist mit 5V auf dem VCP-G-Board verbunden.
    - Der GND-Pin des IR-Sensors ist mit GND auf dem VCP-G-Board verbunden.
- LED01
    - Der Pin (+) ist mit Pin 16 des VCP-G-Boards verbunden.
    - Der Pin (–) ist mit der GND-Schiene auf dem Breadboard verbunden.
- LED02
    - Der Pin (+) ist mit Pin 17 des VCP-G-Boards verbunden.
    - Der Pin (–) ist mit der GND-Schiene auf dem Breadboard verbunden.

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/F_irsensor1.png" width="600"></p>
<p align="center"><strong>Abbildung 7.1 Schaltplan des Infrarotsensors (IR)</strong></p>

##### 7.1.2.1 Pinbelegung
Die folgende Tabelle zeigt die Pinbelegung.

<p align="center"><strong>Tabelle 7.1 Pinbelegung von irSensor_LED</strong></p>
<div align="center">
	<table>
	    <tr>
	        <th colspan="3">Pinname</th>
	        <th>VCP-G-Board</th>
	        <th>GPIO</th>
	    </tr>
	    <tr>
	        <td colspan="3">OUT-Pin des IR-Sensors </td>
	        <td>38</td>
	        <td>K[13]</td>
	    </tr>
	        <tr>
	        <td colspan="3">VCC-Pin des IR-Sensors </td>
	        <td>5V</td>
	        <td>-</td>
	    </tr>
	    <tr>
	        <td colspan="3">GND-Pin des IR-Sensors</td>
	        <td>GND</td>
	        <td>-</td>
	    </tr>
	    <tr>
	        <td colspan="3">LED01 (+)-Pin</td>
	        <td>16</td>
	        <td>A[06]</td>
	    </tr>
	    <tr>
	        <td colspan="3">LED01 (-) Pin</td>
	        <td>GND</td>
	        <td>-</td>
	    </tr>
	    <tr>
	        <td colspan="3">LED02 (+)-Pin</td>
	        <td>17</td>
	        <td>A[07]</td>
	    </tr>
	    <tr>
	        <td colspan="3">LED02 (-)-Pin </td>
	        <td>GND</td>
	        <td>-</td>
	    </tr>
	</table>
</div>
</br></br>

### 7.1.3 Ausführung
Um dieses Beispiel auszuführen, ändern Sie **Main_StartTask()** in der Datei main.c wie dargestellt.
```
#include <gpio.h>
#define PIR_SENSOR_PIN   GPIO_GPK(13)
static void Main_StartTask(void * pArg)
{
    (void)pArg;
    (void)SAL_OsInitFuncs();

    GPIO_Config(PIR_SENSOR_PIN, GPIO_FUNC(0) | GPIO_INPUT | GPIO_INPUTBUF_EN | GPIO_PULLDN);
    GPIO_Config(GPIO_GPA(6), GPIO_FUNC(0) | GPIO_OUTPUT);  
    GPIO_Config(GPIO_GPA(7), GPIO_FUNC(0) | GPIO_OUTPUT);  

    while (1)
    {
        if (GPIO_Get(GPIO_GPK(13))) {
            mcu_printf("No\n");

            GPIO_Set(GPIO_GPA(6), 0); // LED1 OFF
            GPIO_Set(GPIO_GPA(7), 1); // LED2 ON
        } else {
            mcu_printf("Detected!\n");

            GPIO_Set(GPIO_GPA(6), 1); // LED1 ON
            GPIO_Set(GPIO_GPA(7), 0); // LED2 OFF
        }
        SAL_TaskSleep(500); 
    }
}
```
Wechseln Sie nach dem Bearbeiten des Codes in das folgende Verzeichnis und führen Sie den Build-Befehl aus:  
```
$ cd ~/vcp/build/tcc70xx/gcc
$ make
```
Dadurch wird ein Firmware-Image erzeugt und mit dem Tool ***FWDN*** auf den VCP-G geflasht.  
Nachdem der Code erfolgreich geflasht und ausgeführt wurde, erkennt der IR-Sensor das Vorhandensein oder Fehlen eines Objekts und steuert entsprechend zwei LEDs. Wenn ein Objekt erkannt wird, leuchtet die erste LED auf; wenn kein Objekt erkannt wird, leuchtet die zweite LED auf. Dieses Verhalten bestätigt, dass der IR-Sensoreingang und der GPIO-Ausgang auf dem VCP-G-Board ordnungsgemäß funktionieren.

**Hinweis**: Wenn Sie die für den IR-Sensor oder die LEDs verwendeten GPIO-Pins ändern möchten, siehe den Konfigurationsabschnitt im Quellcode.
</br></br></br>

## 7.2 Infrarot-Sensor (IR) (Empfänger)
---
Dieses Beispiel zeigt, wie das VCP-G-Board mit einem IR-Empfängersensor Signale einer Fernbedienung erkennt. Wenn ein IR-Signal empfangen wird, schaltet die Onboard-Logik eine mit dem Breadboard verbundene LED ein. Damit ist bestätigt, dass das IR-Empfängermodul eingehende Signale korrekt decodiert und der VCP-G wie erwartet reagiert. Der Empfangsstatus wird außerdem auf dem seriellen Monitor angezeigt.
</br></br>

### 7.2.1 Hardware-Anforderungen
- VCP-G-Board (x1)
- Breadboard (x1)
- IR-Empfängersensor (x1)
- Arduino-Fernbedienung (x1)
- LED (x1)
- 12V 1A Netzteil (x1)
- USB-Type-C-auf-A-Kabel (x1)
- Jumper-Kabel Stecker auf Stecker (x5)
</br></br>

### 7.2.2 Schaltung
- IR-Empfängersensor
    - Der SIG-Pin des IR-Sensors ist mit Pin 40 des VCP-G-Boards verbunden.
    - Der GND-Pin des IR-Sensors ist mit GND auf dem VCP-G-Board verbunden.
    - Der VCC-Pin des IR-Sensors ist mit 5V auf dem VCP-G-Board verbunden.
- LED
    - Der Pin (+) ist mit Pin 7 des VCP-G-Boards verbunden.
    - Der Pin (–) ist mit der GND-Schiene auf dem Breadboard verbunden.

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/F_irsensor2.png" width="600"></p>
<p align="center"><strong>Abbildung 7.2 Schaltplan IR-Empfängersensor</strong></p>

##### 7.2.2.1 Pinbelegung
Die folgende Tabelle zeigt die Pinbelegung.

<p align="center"><strong>Tabelle 7.1 Pinbelegung von irSensor_LED</strong></p>
<div align="center">
	<table>
	    <tr>
	        <th colspan="3">Pinname</th>
	        <th>VCP-G-Board</th>
	        <th>GPIO</th>
	    </tr>
	    <tr>
	        <td colspan="3">IR-Sensor SIG-Pin </td>
	        <td>40</td>
	        <td>K[11]</td>
	    </tr>
	        <tr>
	        <td colspan="3">IR-Sensor GND-Pin </td>
	        <td>GND</td>
	        <td>-</td>
	    </tr>
	    <tr>
	        <td colspan="3">IR-Sensor VCC-Pin</td>
	        <td>VCC</td>
	        <td>-</td>
	    </tr>
	    <tr>
	        <td colspan="3">LED (+) Pin</td>
	        <td>7</td>
	        <td>B[01]</td>
	    </tr>
	    <tr>
	        <td colspan="3">LED (-) Pin</td>
	        <td>GND</td>
	        <td>-</td>
	    </tr>
	</table>
</div>

</br></br>

### 7.2.3 Ausführung
Um dieses Beispiel auszuführen, ändern Sie **Main_StartTask()** in der Datei main.c wie dargestellt.
```
#include <gpio.h>
#define PIR_SENSOR_PIN   GPIO_GPK(11)
static void Main_StartTask(void * pArg)
{
    (void)pArg;
    (void)SAL_OsInitFuncs();

    GPIO_Config(PIR_SENSOR_PIN, GPIO_FUNC(0) | GPIO_INPUT | GPIO_INPUTBUF_EN);
    GPIO_Config(GPIO_GPB(1), GPIO_FUNC(0) | GPIO_OUTPUT);

    uint32 prev_state = 0xFFFFFFFF;
    uint32 curr_state;

    while (1)
    {
        curr_state = GPIO_Get(PIR_SENSOR_PIN);
        if (curr_state != prev_state)
        {
            if (curr_state == 0)
            {
                mcu_printf("IR Signal Detected!\n");
                GPIO_Set(GPIO_GPB(1), 1);  // LED ON
            }
            else
            {
                GPIO_Set(GPIO_GPB(1), 0);  // LED OFF
            }
            prev_state = curr_state;
        }
        SAL_TaskSleep(50);
    }
}
```
Wechseln Sie nach dem Bearbeiten des Codes in das folgende Verzeichnis und führen Sie den Build-Befehl aus:  
```
$ cd ~/vcp/build/tcc70xx/gcc
$ make
```
Dadurch wird ein Firmware-Image erzeugt und mit dem Tool ***FWDN*** auf den VCP-G geflasht.  
Nachdem der Code erfolgreich geflasht und ausgeführt wurde, erkennt der IR-Empfänger Signale einer Fernbedienung und schaltet eine LED für kurze Zeit ein. Damit ist bestätigt, dass der VCP-G die IR-Eingaben korrekt liest und den GPIO-Ausgang entsprechend den empfangenen Signalen steuert.

**Hinweis**: Um die für den IR-Sensor oder die LED verwendeten GPIO-Pins zu ändern, siehe den Konfigurationsabschnitt im Quellcode.
</br></br></br>

## 7.3 Gassensor
---
Dieses Beispiel zeigt, wie das VCP-G-Board einen Gassensor (MQ 135) verwendet, um verschiedene schädliche Gase in der Luft zu erkennen. Es liest den Analogwert eines an den analogen Pin des VCP-G-Boards angeschlossenen Sensors, wandelt ihn in eine Spannung um und gibt ihn anschließend mit einer Nachkommastelle auf dem seriellen Monitor aus.

**Hinweis:** Der Gassensor (MQ-135) ist ein Produkt von Winsen®. Alle Rechte an Design, Marke und zugehörigem geistigem Eigentum liegen bei Winsen.
</br></br>

### 7.3.1 Hardware-Anforderungen
- VCP-G-Board (x1)
- Gassensor (MQ135) (x1)
- 12V 1A Netzteil (x1)
- USB-Type-C-auf-A-Kabel (x1)
- Jumperkabel Stecker auf Buchse (x3)
</br></br>

### 7.3.2 Schaltung
- Gassensor
    - Der A0-Pin des Gassensors ist mit dem analogen Pin 55 des VCP-G-Boards verbunden. 
    - Der VCC-Pin des Gassensors ist mit 5V auf dem VCP-G-Board verbunden.
    - Der GND-Pin des Gassensors ist mit GND auf dem VCP-G-Board verbunden.

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/F_gassensor.png" width="600"></p>
<p align="center"><strong>Abbildung 7.3 Schaltplan Gassensor</strong></p>

#### 7.3.2.1 Pinbelegung
Die folgende Tabelle zeigt die Pinbelegung.

<p align="center"><strong>Tabelle 7.3 Pinbelegung des Gassensors</strong></p>
<div align="center">
	<table>
	    <tr>
	        <th colspan="3">Pinname</th>
	        <th>VCP-G-Board</th>
	        <th>GPIO</th>
	    </tr>
	    <tr>
	        <td colspan="3">A0-Pin des Gassensors</td>
	        <td>55</td>
	        <td>K[15]</td>
	    </tr>
	        <tr>
	        <td colspan="3">VCC-Pin des Gassensors</td>
	        <td>5V</td>
	        <td>-</td>
	    </tr>
	    <tr>
	        <td colspan="3">GND-Pin des Gassensors</td>
	        <td>GND</td>
	        <td>-</td>
	    </tr>
	</table>
</div>
</br></br>

### 7.3.3 Ausführung
Um dieses Beispiel auszuführen, ändern Sie **Main_StartTask()** in der Datei main.c wie dargestellt.
```
#include <gpio.h>
#define GAS_SENSOR_PIN  GPIO_GPK(15)
static void Main_StartTask(void * pArg)
{
    (void)pArg;
    (void)SAL_OsInitFuncs();

    GPIO_Config(GAS_SENSOR_PIN, GPIO_FUNC(0) | GPIO_INPUT | GPIO_INPUTBUF_EN | GPIO_PULLUP);
    while (1)
    {
        if (GPIO_Get(GAS_SENSOR_PIN) == 0) 
            mcu_printf("Gas Detected!\n");
        else
            mcu_printf("Clean Air\n");
        SAL_TaskSleep(500); 
    }
}
```
Wechseln Sie nach dem Bearbeiten des Codes in das folgende Verzeichnis und führen Sie den Build-Befehl aus:  
```
$ cd ~/vcp/build/tcc70xx/gcc
$ make
```
Dadurch wird ein Firmware-Image erzeugt und mit dem Tool **FWDN** auf den VCP-G geflasht.  
Nachdem der Code erfolgreich geflasht und ausgeführt wurde, überwacht der Gassensor kontinuierlich die Qualität der Umgebungsluft. Wenn Gas erkannt wird (Sensorausgang ist LOW), wird eine Meldung über die Gaserkennung auf dem seriellen Monitor angezeigt; andernfalls wird saubere Luft gemeldet. Damit ist bestätigt, dass der VCP-G den digitalen Eingang des Gassensors korrekt liest.

**Hinweis**: Um den für den Gassensor verwendeten GPIO-Pin zu ändern, siehe den Konfigurationsabschnitt im Quellcode. Die meisten Gassensormodule verfügen über eine kleine Einstellschraube (Potentiometer) zur Regelung der Empfindlichkeit. Wenn der Sensor nicht zuverlässig reagiert, stellen Sie den Schwellenwert für die Gaserkennung mit dieser Schraube genauer ein.
</br></br></br>

## 7.4 Kapazitiver Touch-Sensor
---
Dieses Beispiel zeigt, wie das VCP-G-Board mit einem kapazitiven Touch-Sensor zusammenarbeitet und eine LED auf einem Breadboard steuert. Der kapazitive Touch-Sensor erkennt die physische Berührung durch einen Finger, indem er Änderungen der Kapazität misst.  
Wenn eine Berührung erkannt wird, gibt der Sensor ein digitales HIGH-Signal an den VCP-G aus, der wiederum eine LED einschaltet. Dieses Beispiel bestätigt, dass die Berührungseingabe korrekt erkannt wird und dass der GPIO-Ausgang entsprechend reagiert. Der Status der Berührungserkennung wird außerdem auf dem seriellen Monitor angezeigt.
</br></br>

### 7.4.1 Hardware-Anforderungen
- VCP-G-Board (x1)
- Breadboard (x1)
- Kapazitiver Touch-Sensor (x1)
- LED (x1)
- 12V 1A Netzteil (x1)
- USB-Type-C-auf-A-Kabel (x1)
- Jumperkabel Stecker auf Stecker (x6)
</br></br>

### 7.4.2 Schaltung
- Touch-Sensor 
    - Der SIG-Pin des Touch-Sensor-Moduls ist mit Pin 39 auf dem VCP-G-Board verbunden.
    - Der VCC-Pin des Touch-Sensor-Moduls ist mit 5V auf dem VCP-G-Board verbunden.
    - Der GND-Pin des Touch-Sensor-Moduls ist mit GND auf dem VCP-G-Board verbunden.
- LED
    - Der (+)-Pin der LED ist mit Pin 7 auf dem VCP-G-Board verbunden.
    - Der (–)-Pin der LED ist mit der GND-Schiene auf dem Steckbrett verbunden.

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/F_touchsensor.png" width="600"></p>
<p align="center"><strong>Abbildung 7.4 Schaltplan des Touch-Sensors</strong></p>

#### 7.4.2.1 Pinbelegung
Die folgende Tabelle zeigt die Pinbelegung.

<p align="center"><strong>Tabelle 7.5 Pinbelegung des Touch-Sensors</strong></p>
<div align="center">
	<table>
	    <tr>
	        <th colspan="3">Pinname</th>
	        <th>VCP-G-Board</th>
	        <th>GPIO</th>
	    </tr>
	    <tr>
	        <td colspan="3">SIG-Pin des Touch-Sensors</td>
	        <td>39</td>
	        <td>K[12]</td>
	    </tr>
	        <tr>
	        <td colspan="3">VCC-Pin des Touch-Sensors</td>
	        <td>5V</td>
	        <td>-</td>
	    </tr>
	    <tr>
	        <td colspan="3">GND-Pin des Touch-Sensors</td>
	        <td>GND</td>
		    <td>-</td>
		</tr>
	    <tr>
	        <td colspan="3">LED (+) Pin</td>
	        <td>7</td>
	        <td>B[01]</td>
	    </tr>
	    <tr>
	        <td colspan="3">LED (-) Pin</td>
	        <td>GND</td>
	        <td>-</td>
	    </tr>
	</table>
</div>

</br></br>

### 7.4.3 Ausführung
Um dieses Beispiel auszuführen, ändern Sie **Main_StartTask()** in der Datei main.c wie dargestellt.
```
#include <gpio.h>
#define TOUCH_SENSOR_PIN GPIO_GPK(12) 
void Main_StartTask(void * pArg)
{
    (void)pArg;
    (void)SAL_OsInitFuncs();

    GPIO_Config(TOUCH_SENSOR_PIN, GPIO_FUNC(0) | GPIO_INPUT | GPIO_INPUTBUF_EN | GPIO_PULLDN);
    GPIO_Config(GPIO_GPB(1), GPIO_FUNC(0) | GPIO_OUTPUT);

    while (1)
    {
        if (GPIO_Get(TOUCH_SENSOR_PIN)) {
            mcu_printf("Touch Detected!\n");
            GPIO_Set(GPIO_GPB(1), 1); // LED ON
        }
        else {
            mcu_printf("Not touched\n");
            GPIO_Set(GPIO_GPB(1), 0); // LED OFF
        }

        SAL_TaskSleep(300);
    }
}
```
Wechseln Sie nach dem Bearbeiten des Codes in das folgende Verzeichnis und führen Sie den Build-Befehl aus:  
```
$ cd ~/vcp/build/tcc70xx/gcc
$ make
```
Dadurch wird ein Firmware-Image erzeugt; verwenden Sie das FWDN-Tool, um das erzeugte Image auf den VCP-G zu flashen.  
Sobald der Code erfolgreich geflasht und ausgeführt wurde, überwacht der kapazitive Touch-Sensor die Berührungseingabe durch einen menschlichen Finger. Wenn eine Berührung erkannt wird (Sensorausgang ist HIGH), wird eine Meldung auf dem seriellen Monitor ausgegeben und eine LED eingeschaltet. Wenn keine Berührung erkannt wird, wird die LED ausgeschaltet. Dies bestätigt, dass der VCP-G die Eingabe des Touch-Sensors korrekt liest und den GPIO-Ausgang entsprechend steuert.

**Hinweis**: Um den für den Touch-Sensor oder die LED verwendeten GPIO-Pin zu ändern, siehe den Konfigurationsabschnitt im Quellcode.
</br></br></br></br>

# 8. Referenzen
---
- Kontaktieren Sie TOPST für weitere Einzelheiten: topst@topst.ai

**Hinweis:** Referenzdokumente können, sofern verfügbar, je nach Vertragsbedingungen bereitgestellt werden. Wenn die Referenzdokumente
nicht verfügbar sind, können die Inhalte, die sich direkt auf Ihre Entwicklung beziehen, erläutert werden.
