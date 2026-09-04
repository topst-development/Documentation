# 1. Einführung
---
Dieses Dokument enthält Richtlinien zur Verwendung verschiedener Arduino-Sensoren mit dem VCP-G-Board. Es enthält Anschlussanweisungen und Beispielcodes, die Ihnen helfen, mit dem VCP-G auf einfache Weise Projekte zu entwickeln.

Im Einzelnen bietet dieses Dokument eine Anleitung zu Arduino-IDE-Beispielen für das VCP-G, darunter:  
- VCP-G Digital
- VCP-G Analog
- VCP-G SPI
- VCP-G I2C
- VCP-G UART
- Zusätzliches Beispiel

Siehe Abbildung 1.1, bevor Sie das VCP-G verwenden.

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/vcp-g%20pinout%20Diagram.png"></p>
<p align="center"><strong>Abbildung 1.1 VCP-G Pinout-Diagramm</strong></p>

</br></br></br></br>

# 2. Digitale Pins des VCP-G
---
Dieses Kapitel enthält Beispiele für die Steuerung von LEDs über die digitalen Pins des VCP-G-Boards. Im VCP-G werden digitale Pins zum Senden oder Empfangen von Binärsignalen (HIGH oder LOW) verwendet und sind daher für die Steuerung von Komponenten wie LEDs, Schaltern und Sensoren unverzichtbar. 

Dieses Kapitel enthält zwei Beispielprojekte, die zeigen, wie mehrere LEDs über digitale Ausgänge gesteuert werden, und vermittelt so ein grundlegendes Verständnis der Funktionsweise digitaler Pins.

</br></br></br>

## 2.1 vcp4LED
---
Dieses Beispielprogramm zeigt, wie das VCP-G-Board vier LEDs auf dem Breadboard steuert. Der Beispielcode wird in der Datei „vcp4LED.ino“ bereitgestellt. Wenn diese Datei auf das VCP-G hochgeladen wird, werden die LEDs nacheinander in Vorwärts- und Rückwärtsrichtung mit einer Verzögerung von 500 ms zwischen den einzelnen Übergängen ein- und ausgeschaltet. 

</br></br>

### 2.1.1 Hardware-Anforderungen  
- VCP-G-Board (x1)
- Breadboard (x1)
- LED (x4)
- 220Ω Widerstand (x4)
- 12V 1A Netzteil (x1)
- USB-Type-C-auf-A-Kabel (x1) 
- Jumperkabel Stecker auf Stecker (x9)
</br></br>

### 2.1.2 Schaltung
- LED01
    - Der (+) Pin ist über einen 220Ω Widerstand mit der 5V-Stromschiene auf dem Breadboard verbunden, die vom VCP-G-Board versorgt wird.
    - Der (-) Pin ist mit Pin 47 auf dem VCP-G-Board verbunden.
- LED02
    - Der (+) Pin ist über einen 220Ω Widerstand mit der 5V-Stromschiene auf dem Breadboard verbunden.
    - Der (-) Pin ist mit Pin 17 auf dem VCP-G-Board verbunden.
- LED03
    - Der (+) Pin ist über einen 220Ω Widerstand mit der 5V-Stromschiene auf dem Breadboard verbunden.
    - Der (-) Pin ist mit Pin 50 auf dem VCP-G-Board verbunden.
- LED04
    - Der (+) Pin ist über einen 220Ω Widerstand mit der 5V-Stromschiene auf dem Breadboard verbunden.
    - Der (-) Pin ist mit Pin 48 auf dem VCP-G-Board verbunden.  

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/vcp4LED%20Circuit%20Schematic.png"></p>
<p align="center"><strong>Abbildung 2.1 Schaltplan vcp4LED</strong></p>

#### 2.1.2.1 Pinbelegung
Die folgende Tabelle zeigt die Pinbelegung.

<p align="center"><strong>Tabelle 2.1 Pinbelegung von vcp4LED</strong></p>
<div align="center">	
	<table>
		<tr>
			<th colspan="3">Pinname</th>
	        <th>VCP-G-Board</th>
	        <th>Arduino IDE</th>
	    </tr>
	    <tr>
	        <td colspan="3">LED01 (-) Pin</td>
	        <td>47</td>
	        <td>47</td>
	    </tr>
	        <tr>
	        <td colspan="3">LED02 (-) Pin</td>
	        <td>17</td>
	        <td>17</td>
	    </tr>
	        <tr>
	        <td colspan="3">LED03 (-) Pin</td>
	        <td>50</td>
	        <td>50</td>
	    </tr>
	        <tr>
	        <td colspan="3">LED04 (-) Pin</td>
	        <td>48</td>
	        <td>48</td>
	    </tr>
	</table>
</div>
</br></br>

### 2.1.3 Ausführung
1. Öffnen Sie die Datei "vcp4LED.ino".  
    1. Öffnen Sie die Arduino IDE.
    2. Klicken Sie auf **File -> Examples -> 01.VCP-G Digital -> vcp4LED**.
    ```
    /*
    *  TOPST VCP : 4 LED Control
    */
    
    int ledPin[] = {47, 17, 50, 48};
    
    // the setup function runs once when you press reset or power the board
    void setup() {
    // LED Mode and Init 
    for(int i=0; i<4; i++)
    {
        pinMode(ledPin[i], OUTPUT);
        digitalWrite(ledPin[i], HIGH);
    }
    
    }
    
    // the loop function runs over and over again forever
    void loop() {
        
    for(int i=0; i<4; i++)
    {
        digitalWrite(ledPin[i], LOW);
        delay(500);
    }
    
    for(int i=3; i>=0; i--)
    {
        digitalWrite(ledPin[i], HIGH);
        delay(500);
    }
    
    }
    ```
2. Überprüfen Sie die Datei "vcp4LED.ino" und laden Sie sie auf das VCP-G hoch.
3. Wenn der Upload-Vorgang in einem endlosen Upload-Zustand hängen bleibt, liegt dies daran, dass der FWDN-Modus nicht aktiviert ist. So beheben Sie dies:  
    1. Trennen Sie das Stromkabel vom VCP-G-Board.
    2. Halten Sie den FWDN-Schalter gedrückt.
    3. Schließen Sie das Stromkabel wieder an, während Sie den FWDN-Schalter weiterhin gedrückt halten.
    4. Lassen Sie den FWDN-Schalter los.
        Wenn das Problem weiterhin besteht, führen Sie die Arduino IDE mit Administratorrechten aus.
4. Prüfen Sie nach dem erfolgreichen Hochladen der Datei die Ausgabekonsole der Arduino IDE auf die folgende Meldung:  

     **Hinweis:** Die Meldung sollte **vcp4LED.ino.rom** enthalten.
    ```
    [FWDN_VCP::WriteFile:577] Complete to send file - C:\Users\topst\AppData\Local\arduino\sketches\C05357299384CE5734F0E696C5A4DA3B/vcp4LED.ino.rom

    [main:155] Complete FWDN
    ```

</br></br></br>

## 2.2 vcp4LED_Button
---
Dieses Beispielprogramm zeigt, wie das VCP-G-Board vier LEDs und eine Taste auf dem Breadboard steuert. Wenn die Taste gedrückt wird, werden die beiden rechten LEDs ausgeschaltet und die beiden linken LEDs eingeschaltet. Wenn die Taste losgelassen wird, werden die eingeschalteten LEDs ausgeschaltet und die ausgeschalteten LEDs eingeschaltet. Das Programm prüft kontinuierlich den Zustand der Taste und passt die LEDs entsprechend an.
</br></br>

### 2.2.1 Hardware-Anforderungen
- VCP-G-Board (x1)
- Breadboard (x1)
- LED (x4)
- Tastschalter (Sensor) (x1)
- 220Ω Widerstand (x4)
- 12V 1A Netzteil (x1)
- USB-Type-C-auf-A-Kabel (x1)
- Jumperkabel Stecker auf Stecker (x12)
</br></br>

### 2.2.2 Schaltung
1.	LED01
    - Der (+) Pin ist über einen 220Ω Widerstand mit der 5V-Stromschiene auf dem Breadboard verbunden, die vom VCP-G-Board versorgt wird.
    - Der (-) Pin ist mit Pin 47 auf dem VCP-G-Board verbunden.
2.	LED02
    - Der (+) Pin ist über einen 220Ω Widerstand mit der 5V-Stromschiene auf dem Breadboard verbunden.
    - Der (-) Pin ist mit Pin 17 auf dem VCP-G-Board verbunden.
3.	LED03
    - Der (+) Pin ist über einen 220Ω Widerstand mit der 5V-Stromschiene auf dem Breadboard verbunden.
    - Der (-) Pin ist mit Pin 50 auf dem VCP-G-Board verbunden.
4.	LED04
    - Der (+) Pin ist über einen 220Ω Widerstand mit der 5V-Stromschiene auf dem Breadboard verbunden.
    - Der (-) Pin ist mit Pin 48 auf dem VCP-G-Board verbunden.
5.	Tastschalter
    - Ein Anschlussbein des Tastschalters ist mit Pin 45 auf dem VCP-G-Board verbunden.
    - Das diagonal gegenüberliegende Anschlussbein der Taste ist mit dem GND-Pin verbunden.

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/vcp4LED_Button%20Circuit%20Schematic.png"></p>
<p align="center"><strong>Abbildung 2.2 Schaltplan vcp4LED_Button</strong></p>

#### 2.2.2.1 Pinbelegung
Die folgende Tabelle zeigt die Pinbelegung.

<p align="center"><strong>Tabelle 2.2 Pinbelegung von vcp4LED_Button</strong></p>
<div align="center">
	<table>
	    <tr>
	        <th colspan="3">Pinname</th>
	        <th>VCP-G-Board</th>
	        <th>Arduino IDE</th>
	    </tr>
	    <tr>
	        <td colspan="3">LED01 (-) Pin</td>
	        <td>47</td>
	        <td>47</td>
	    </tr>
	        <tr>
	        <td colspan="3">LED02 (-) Pin</td>
	        <td>17</td>
	        <td>17</td>
	    </tr>
	        <tr>
	        <td colspan="3">LED03 (-) Pin</td>
	        <td>50</td>
	        <td>50</td>
	    </tr>
	        <tr>
	        <td colspan="3">LED04 (-) Pin</td>
	        <td>48</td>
	        <td>48</td>
	    </tr>
	    </tr>
	        <tr>
	        <td colspan="3">Ein Anschlussbein-Pin der Taste</td>
	        <td>45</td>
	        <td>45</td>
	    </tr>
	</table>
</div>
</br></br>

### 2.1.3 Ausführung
1. Öffnen Sie die Datei "vcp4LED_Button.ino".
    1. Öffnen Sie die Arduino IDE.
    2. Klicken Sie auf **File -> Examples -> 01.VCP-G Digital -> vcp4LED_Button**.
    ```
    /*
    *  TOPST VCP : 4 LED and Button Control
    */
    
    int ledPin[] = {47, 17, 50, 48};
    int buttonPin[] = {45};

    // the setup function runs once when you press reset or power the board
    void setup() {
        // LED Mode and Init 
        for(int i=0; i<4; i++)
        {
            pinMode(ledPin[i], OUTPUT);
            digitalWrite(ledPin[i], HIGH);
        }
 
        pinMode(buttonPin[0], INPUT);
 
    }
  
    // the loop function runs over and over again forever
    void loop() {
        
        int button = digitalRead(buttonPin[0]);
            if(button==HIGH)
            {
                for(int i=0; i<2; i++)
                {
                    digitalWrite(ledPin[i], LOW);
                    digitalWrite(ledPin[i+2], HIGH);
                }
            }
            else
            {
                for(int i=3; i>=2; i--)
                {
                    digitalWrite(ledPin[i-2], HIGH);
                    digitalWrite(ledPin[i], LOW);
                }
            }
    }

    ```
2. Überprüfen Sie die Datei "vcp4LED_Button.ino" und laden Sie sie auf das VCP-G hoch.
3. Wenn der Upload-Vorgang in einem endlosen Upload-Zustand hängen bleibt, liegt dies daran, dass der FWDN-Modus nicht aktiviert ist. So beheben Sie dies:  
    1. Trennen Sie das Stromkabel vom VCP-G-Board.
    2. Halten Sie den FWDN-Schalter gedrückt.
    3. Schließen Sie das Stromkabel wieder an, während Sie den FWDN-Schalter weiterhin gedrückt halten.
    4. Lassen Sie den FWDN-Schalter los. 
        Wenn das Problem weiterhin besteht, führen Sie die Arduino IDE mit Administratorrechten aus.
4. Prüfen Sie nach dem erfolgreichen Hochladen der Datei die Ausgabekonsole der Arduino IDE auf die folgende Meldung:  

    **Hinweis:** Die Meldung sollte **vcp4LED_Button.ino.rom** enthalten.
    ```
    [FWDN_VCP::WriteFile:577] Complete to send file - C:\Users\topst\AppData\Local\arduino\sketches\5CC1DB4CA216E2BC009504FAA3D06456/vcp4LED_Button.ino.rom

    [main:155] Complete FWDN
    ```

</br></br></br></br>

# 3. Analoge Pins des VCP-G
---
Dieses Kapitel enthält Beispiele für die Verwendung der analogen Pins auf dem VCP-G-Board. Im VCP-G empfangen analoge Pins kontinuierliche Spannungssignale von Sensoren und ermöglichen so die präzise Messung veränderlicher Eingangswerte. Kapitel 3.1, Kapitel 3.2 und Kapitel 3.3 beschreiben, wie analoge Pins zum Auslesen von Sensordaten und zur Steuerung von Ausgängen verwendet werden, und vermitteln so ein grundlegendes Verständnis der Verarbeitung analoger Eingänge.

</br></br></br>

## 3.1 AnalogInOutSerial
---
Dieses Beispielprogramm zeigt, wie das VCP-G-Board ein Potentiometer und eine LED auf dem Breadboard steuert. Das VCP-G liest einen Wert von einem analogen Eingangspin, bildet das Ergebnis auf einen Bereich von 0 bis 1000 ab und verwendet diesen Wert, um die Pulsweitenmodulation (PWM) eines Ausgangspins (mit einer LED verbunden) einzustellen. Die Ergebnisse werden außerdem im Serial Monitor ausgegeben.
</br></br>

### 3.1.1 Hardware-Anforderungen
- VCP-G-Board (x1)
- Breadboard (x1)
- LED (x1)
- Potentiometer (x1)
- 220Ω Widerstand (x2)
- 12V 1A Netzteil (x1)
- USB-Type-C-auf-A-Kabel (x1)
- Jumperkabel Stecker auf Stecker (x4)
</br></br>

### 3.1.2 Schaltung
- Potentiometer
    - Der mittlere Pin des Potentiometers ist mit dem analogen Pin A5 auf dem VCP-G-Board verbunden.
    - Der GND-Pin des Potentiometers ist mit Pin 43 auf dem VCP-G-Board und über einen 220Ω Widerstand mit dem GND-Pin auf dem VCP-G-Board verbunden.
- LED
    - Der (+) Pin der LED ist über einen 220Ω Widerstand mit 3.3V auf dem VCP-G-Board verbunden.
    - Der (-) Pin der LED ist mit dem mittleren Pin des Potentiometers verbunden.

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/AnalogInOutSerial%20Circuit%20Schematic.png"></p>
<p align="center"><strong>Abbildung 3.1 Schaltplan AnalogInOutSerial</strong></p>

#### 3.1.2.1 Pinbelegung
Die folgende Tabelle zeigt die Pinbelegung.

<p align="center"><strong>Tabelle 3.1 Pinbelegung von AnalogInOutSerial</strong></p>
<div align="center">
	<table>
	    <tr>
	        <th colspan="3">Pinname</th>
	        <th>VCP-G-Board</th>
	        <th>Arduino IDE</th>
	    </tr>
	    <tr>
	        <td colspan="3">Mittlerer Pin des Potentiometers</td>
	        <td>A5</td>
	        <td>-</td>
	    </tr>
	        <tr>
	        <td colspan="3">GND-Pin des Potentiometers</td>
	        <td>43</td>
	        <td>43</td>
	    </tr>
	        <tr>
	        <td colspan="3">LED (+) Pin</td>
	        <td>3.3V</td>
	        <td>-</td>
	    </tr>
	        <tr>
	        <td colspan="3">LED (-) Pin</td>
	        <td>A5</td>
	        <td>A5</td>
	    </tr>
	</table>
</div>
</br></br>

### 3.1.3 Ausführung
1. Öffnen Sie die Datei "AnalogInOutSerial.ino".  
    1. Öffnen Sie die Arduino IDE.
    2. Klicken Sie auf **File -> Examples -> 02.VCP-G Analog -> AnalogInOutSerial**.
    ```
    #include <HardwareSerial.h>
    HardwareSerial Serial;
 
    // These constants won't change. They're used to give names to the pins used:
    const int analogInPin = 43;  // Analog input pin that the potentiometer is attached to
    const int analogOutPin = A5;  // Analog output pin that the LED is attached to
 
    int sensorValue = 0;  // value read from the pot
    int outputValue = 0;  // value output to the PWM (analog out)
 
    void setup() {
        // initialize serial communications at 115200 bps:
        Serial.begin(115200);
    }
 
    void loop() {
        // read the analog in value:
        sensorValue = analogRead(analogInPin);
        // map it to the range of the analog out:
        outputValue = map(sensorValue, 0, 4095, 0, 1000);
        // change the analog out value:
        analogWrite(analogOutPin, outputValue / 4);
    
        // print the results to the Serial Monitor:
        Serial.print("sensor = ");
        Serial.print(sensorValue);
        Serial.print("\t output = ");
        Serial.println(outputValue);

        // wait 2 milliseconds before the next loop for the analog-to-digital
        // converter to settle after the last reading:
        delay(2);
    }
    ```
 
    **Hinweis:** Wenn der Fehler auftritt, dass "Serial" nicht deklariert ist, stellen Sie sicher, dass die folgende Bibliothek und Objektdeklaration korrekt eingebunden sind.
    ```
    #include <HardwareSerial.h>
    HardwareSerial Serial;
    ```
2. Überprüfen Sie die Datei "AnalogInOutSerial.ino" und laden Sie sie auf das VCP-G hoch.
3. Wenn der Upload-Vorgang in einem endlosen Upload-Zustand hängen bleibt, liegt dies daran, dass der FWDN-Modus nicht aktiviert ist. So beheben Sie dies:  
    1. Trennen Sie das Stromkabel vom VCP-G-Board.
    2. Halten Sie den FWDN-Schalter gedrückt.
    3. Schließen Sie das Stromkabel wieder an, während Sie den FWDN-Schalter weiterhin gedrückt halten.
    4. Lassen Sie den FWDN-Schalter los.
        Wenn das Problem weiterhin besteht, führen Sie die Arduino IDE mit Administratorrechten aus.
4. Prüfen Sie nach dem erfolgreichen Hochladen der Datei die Ausgabekonsole der Arduino IDE auf die folgende Meldung:  
 
    **Hinweis:** Die Meldung sollte **AnalogInOutSerial.ino.rom** enthalten.
    ```
    [FWDN_VCP::WriteFile:577] Complete to send file - C:\Users\topst\AppData\Local\arduino\sketches\EB016432EF98DEF0B9102FD77148DD5D/AnalogInOutSerial.ino.rom

    [main:155] Complete FWDN
    ```

</br></br></br>

## 3.2 AnalogInput
---
Dieses Beispielprogramm zeigt, wie das VCP-G-Board ein Potentiometer und eine LED auf dem Breadboard steuert. Es liest einen Wert von einem analogen Eingangspin und verwendet diesen Wert zur Steuerung einer LED. Wenn der Sensorwert kleiner als 3000 ist, leuchtet die LED. Wenn der Sensorwert 3000 oder höher ist, erlischt die LED.
</br></br>

### 3.2.1 Hardware-Anforderungen
- VCP-G-Board (x1)
- Breadboard (x1)
- LED (x1)
- Potentiometer (x1)
- 220Ω-Widerstand (x1)
- 12V 1A Netzteil (x1)
- USB-Type-C-auf-A-Kabel (x1)
- Jumperkabel Stecker auf Stecker (x6)
</br></br>

### 3.2.2 Schaltung
- Potentiometer
    - Der VCC-Pin des Potentiometers ist über einen 220Ω Widerstand mit 3.3V auf dem VCP-G-Board verbunden.
    - Der mittlere Pin des Potentiometers ist mit dem analogen Pin A5 auf dem VCP-G-Board verbunden.
    - Der GND-Pin des Potentiometers ist über einen 220Ω Widerstand mit dem GND-Pin auf dem VCP-G-Board verbunden.
- LED
    - Der (+) Pin der LED ist über einen 220Ω Widerstand mit 3.3V auf dem VCP-G-Board verbunden.
    - Der (-) Pin der LED ist mit Pin 5 auf dem VCP-G-Board verbunden.

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/AnalogInput%20Circuit%20Schematic.png"></p>
<p align="center"><strong>Abbildung 3.2 Schaltplan AnalogInput</strong></p>

#### 3.2.2.1 Pinbelegung
Die folgende Tabelle zeigt die Pinbelegung.

<p align="center"><strong>Tabelle 3.2 Pinbelegung von AnalogInput</strong></p>
<div align="center">
	<table>
	    <tr>
	        <th colspan="3">Pinname</th>
	        <th>VCP-G-Board</th>
	        <th>Arduino IDE</th>
	    </tr>
	    <tr>
	        <td colspan="3">VCC-Pin des Potentiometers</td>
	        <td>3.3V</td>
	        <td>-</td>
	    </tr>
	    <tr>
	        <td colspan="3">Mittlerer Pin des Potentiometers</td>
	        <td>A5</td>
	        <td>A5</td>
	    </tr>
	        <tr>
	        <td colspan="3">GND-Pin des Potentiometers</td>
	        <td>GND</td>
	        <td>-</td>
	    </tr>
	        <tr>
	        <td colspan="3">LED (+) Pin</td>
	        <td>3.3V</td>
	        <td>-</td>
	    </tr>
	        <tr>
	        <td colspan="3">LED (-) Pin</td>
	        <td>5</td>
	        <td>5</td>
	    </tr>
	</table>
</div>
</br></br>

### 3.2.3 Ausführung
1. Öffnen Sie die Datei "AnalogInput.ino".  
    1. Öffnen Sie die Arduino IDE.
    2. Klicken Sie auf **File -> Examples -> 02.VCP-G Analog -> AnalogInput**.
    ```
    #include <HardwareSerial.h>
    HardwareSerial Serial;

    int sensorPin = A5;
    int ledPin = 5;
    int sensorValue = 0;  

    void setup()
    {
        Serial.begin(115200);
        pinMode(ledPin, OUTPUT);
    }

    void loop()
    {
        for(;;)
        {
            sensorValue = analogRead(sensorPin);
            Serial.println(sensorValue);
            if(sensorValue<3000)
            {
                digitalWrite(ledPin, HIGH);
            }
            else
            {
                digitalWrite(ledPin, LOW);
            }
            delay(10);
        }
    }
    ```
 
    **Hinweis 1:** Um **sensorValue** im Serial Monitor zu prüfen, fügen Sie **Serial.println()** zum Quellcode hinzu.  
    **Hinweis 2:** Ein Festwiderstand wird zusammen mit einem variablen Widerstand (Potentiometer) verwendet, um den Sensorwert einzustellen. Der Sensorwert ändert sich abhängig davon, wie weit das Potentiometer gedreht wird, und das erforderliche Maß der Drehung des Potentiometers hängt vom Wert des Festwiderstands ab.

2. Überprüfen Sie die Datei "AnalogInput.ino" und laden Sie sie auf das VCP-G hoch.
3. Wenn der Upload-Vorgang in einem endlosen Upload-Zustand hängen bleibt, liegt dies daran, dass der FWDN-Modus nicht aktiviert ist. So beheben Sie dies:  
    1. Trennen Sie das Stromkabel vom VCP-G-Board.
    2. Halten Sie den FWDN-Schalter gedrückt.
    3. Schließen Sie das Stromkabel wieder an, während Sie den FWDN-Schalter weiterhin gedrückt halten.
    4. Lassen Sie den FWDN-Schalter los.  
        Wenn das Problem weiterhin besteht, führen Sie die Arduino IDE mit Administratorrechten aus.
4. Prüfen Sie nach dem erfolgreichen Hochladen der Datei die Ausgabekonsole der Arduino IDE auf die folgende Meldung:  

   **Hinweis:** Die Meldung sollte **AnalogInput.ino.rom** enthalten.
    ```
    [FWDN_VCP::WriteFile:577] Complete to send file - C:\Users\topst\AppData\Local\arduino\sketches\C3FDEE51354320EA689DFEB4EDCF2ECD/AnalogInput.ino.rom

    [main:155] Complete FWDN
    ```

</br></br></br>

## 3.3 pwmFade
---
Dieses Beispielprogramm zeigt, wie das VCP-G-Board eine LED auf dem Steckbrett steuert, indem es deren Helligkeit mithilfe von PWM in einer Schleife schrittweise erhöht und verringert. Nachdem die LED ihre maximale Helligkeit erreicht hat, beginnt die Helligkeit der LED abzunehmen. Das Programm passt die Helligkeit der LED kontinuierlich an und erzeugt so einen Überblendeffekt.
</br></br>

### 3.3.1 Hardware-Anforderungen
- VCP-G-Board (x1)
- Breadboard (x1)
- LED (x1)
- 220Ω-Widerstand (x1)
- 12V 1A Netzteil (x1)
- USB-Type-C-auf-A-Kabel (x1)
- Jumperkabel Stecker auf Stecker (x2)
</br></br>

### 3.3.2 Schaltung
- LED
    - Der (+)-Pin der LED ist mit 5V auf dem VCP-G-Board verbunden.
    - Der (-)-Pin der LED ist über einen 220Ω-Widerstand mit Pin 9 auf dem VCP-G-Board verbunden.

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/pwmFade%20Circuit%20Schematic.png"></p>
<p align="center"><strong>Abbildung 3.3 Schaltplan von pwmFade</strong></p>

#### 3.3.2.1 Pinbelegung
Die folgende Tabelle zeigt die Pinbelegung.

<p align="center"><strong>Tabelle 3.3 Pinbelegung von pwmFade</strong></p>
<div align="center">
	<table>
	    <tr>
	        <th colspan="3">Pinname</th>
	        <th>VCP-G-Board</th>
	        <th>Arduino IDE</th>
	    </tr>
	    <tr>
	        <td colspan="3">LED (+) Pin</td>
	        <td>5V</td>
	        <td>-</td>
	    </tr>
	        <tr>
	        <td colspan="3">LED (-) Pin</td>
	        <td>9</td>
	        <td>9</td>
	    </tr>
	</table>
</div>
</br></br>

### 3.3.3 Ausführung
1. Öffnen Sie die Datei "pwmFade.ino".
    1. Öffnen Sie die Arduino IDE.
    2. Klicken Sie auf **File -> Examples -> 02.VCP-G Analog -> pwmFade**.
    ```
    /*
    Fade

    This example shows how to fade an LED on pin 11 using the analogWrite()
    function.

    The analogWrite() function uses PWM, so if you want to change the pin you're
    using, be sure to use another PWM capable pin.
    */

    int led = 9;         // the PWM pin the LED is attached to
    int brightness = 0;  // how bright the LED is
    int fadeAmount = 5;  // how many points to fade the LED by

    // the setup routine runs once when you press reset:
    void setup() {
    }

    // the loop routine runs over and over again forever:
    void loop() {
        // set the brightness of pin 9:
        analogWrite(led, brightness);

        // change the brightness for next time through the loop:
        brightness = brightness + fadeAmount;

        // reverse the direction of the fading at the ends of the fade:
        if (brightness <= 0 || brightness >= 255) {
            fadeAmount = -fadeAmount;
        }
        // wait for 30 milliseconds to see the dimming effect
        delay(30);
    }
    ```
2. Überprüfen Sie die Datei "pwmFade.ino" und laden Sie sie auf das VCP-G-Board hoch.
3. Wenn der Upload-Vorgang in einem endlosen Upload-Zustand hängen bleibt, liegt dies daran, dass der FWDN-Modus nicht aktiviert ist. So beheben Sie dies:  
    1. Trennen Sie das Stromkabel vom VCP-G-Board.
    2. Halten Sie den FWDN-Schalter gedrückt.
    3. Schließen Sie das Stromkabel wieder an, während Sie den FWDN-Schalter weiterhin gedrückt halten.
    4. Lassen Sie den FWDN-Schalter los.
        Wenn das Problem weiterhin besteht, führen Sie die Arduino IDE mit Administratorrechten aus.
4. Prüfen Sie nach dem erfolgreichen Hochladen der Datei die Ausgabekonsole der Arduino IDE auf die folgende Meldung:  

     **Hinweis:** Die Meldung sollte **pwmFade.ino.rom** enthalten.
    ```
    [FWDN_VCP::WriteFile:577] Complete to send file - C:\Users\topst\AppData\Local\arduino\sketches\69446E8A7F6616A7D5466014BDF759FC/pwmFade.ino.rom 

    [main:155] Complete FWDN
    ```

</br></br></br></br>

# 4. VCP SPI
---
In diesem Kapitel wird beschrieben, wie die Kommunikation über das Serial Peripheral Interface (SPI) auf dem VCP-G konfiguriert wird.  
SPI ist ein schnelles, synchrones Kommunikationsprotokoll, das zum Datenaustausch zwischen Mikrocontrollern und Peripheriegeräten verwendet wird. Es arbeitet mit separaten Leitungen für die Datenübertragung (MOSI und MISO), die Taktsynchronisation (SCK) und die Geräteauswahl (SS) und gewährleistet so eine effiziente und zuverlässige Kommunikation.  
In den folgenden Kapiteln wird beschrieben, wie SPI eingerichtet und für die Anbindung externer Geräte verwendet wird.

</br></br></br>

## 4.1 vcpSPI_Dot8x8
---
Dieses Beispielprogramm zeigt, wie das VCP-G-Board eine 8x8-LED-Dotmatrix mithilfe des MAX7219-Treibers steuert. Die 8x8-LED-Dotmatrix zeigt Muster wie eine Herzform und den Buchstaben „R“ an, indem Zeilen mit vordefinierten Binärarrays gesetzt werden. Die Intensität der LEDs wird angepasst, um einen pulsierenden Effekt und damit eine dynamische Darstellung zu erzeugen. Zu den weiteren Funktionen gehören das Invertieren und das Löschen der Anzeige, um den Funktionsumfang zu erweitern.
</br></br>

### 4.1.1 Hardware-Anforderungen
- VCP-G-Board (x1)
- 8x8-Dotmatrix (x1)
- 12V 1A Netzteil (x1)
- USB-Type-C-auf-A-Kabel (x1)
- Stecker-auf-Buchse-Jumperkabel (x5)
</br></br>

### 4.1.2 Schaltung
- 8x8-Dot-Matrix
    - Der VCC-Pin der 8x8-Dotmatrix ist mit dem analogen Pin 5V auf dem VCP-G-Board verbunden.
    - Der GND-Pin der 8x8-Dotmatrix ist mit GND auf dem VCP-G-Board verbunden.
    - Der DIN-Pin der 8x8-Dotmatrix ist mit Pin 11 auf dem VCP-G-Board verbunden.
    - Der CS-Pin der 8x8-Dotmatrix ist mit Pin 10 auf dem VCP-G-Board verbunden.
    - Der CLS-Pin der 8x8-Dotmatrix ist mit Pin 13 auf dem VCP-G-Board verbunden.

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/vcpSPI_Dot8x8%20Circuit%20Schematic.png"></p>
<p align="center"><strong>Abbildung 4.1 Schaltplan von vcpSPI_Dot8x8</strong></p>

#### 4.1.2.1 Pinbelegung
Die folgende Tabelle zeigt die Pinbelegung.

<p align="center"><strong>Tabelle 4.1 Pinbelegung von vcpSPI_Dot8x8</strong></p>
<div align="center">
	<table>
	    <tr>
	        <th colspan="3">Pinname</th>
	        <th>VCP-G-Board</th>
	        <th>Arduino IDE</th>
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
	        <td>11</td>
	        <td>11</td>
	    </tr>
	    <tr>
	        <td colspan="3">CS-Pin der 8x8-Dotmatrix</td>
	        <td>10</td>
	        <td>10</td>
	    </tr>
	    <tr>
	        <td colspan="3">CLK-Pin der 8x8-Dotmatrix</td>
	        <td>13</td>
	        <td>13</td>
	    </tr>
	</table>
</div>
</br></br>

### 4.1.3 Ausführung
1. Öffnen Sie die Datei "vcpSPI_Dot8x8.ino".  
    1. Öffnen Sie die Arduino IDE.
    2. Klicken Sie auf **File -> Examples -> 03.VCP-G SPI -> vcpSPI_Dot8x8**.
    ```
    #include <MAX7219.h>

    // 8x8 Dot-Matrix
    #define DATAPIN     11 // SPI1_DO
    #define CLOCKPIN    13 // SPI1_CLK
    #define LOADPIN     10 // SPI1_CS

    // binary represention of a heart shape
    const static byte HEART[8] = {
        0b01100110,
        0b10011001,
        0b10000001,
        0b10000001,
        0b01000010,
        0b00100100,
        0b00011000,
        0b00000000
    };

    // The Letter "R"
    // human-readable binary representation from left-to-right and top-to-bottom    
    const static byte R[8] = {
        0b00000000,
        0b01111100,
        0b01000110,
        0b01111100,
        0b01001000,
        0b01000100,
        0b01000010,
        0b00000000
    };

    void setup() {

    }

    void loop() {
        MAX7219 Matrix(1, DATAPIN, CLOCKPIN, LOADPIN);
        // First LED in upper left Corner
        Matrix.setLed(1, 0, 0, true);
        delay(500);
        Matrix.setLed(1, 0, 0, false);
        delay(500);

        // Make Heartshape from array
        for(int row = 0; row <= 7; row++)
        {
            Matrix.setRow(1, row, HEART[row]);
            delay(100);
        }
        delay(500);

        // Change Intensity to make it pulse
        for(int repeats = 0; repeats < 3; repeats++)
        {
            // increase intensity
            for(int i = 1; i <= 15; i++)
            {
            Matrix.setIntensity(1, i);
            delay(20);
            }

            // decrease intensity
            for(int j = 15; j >= 1; j--)
            {
            Matrix.setIntensity(1, j);
            delay(20);
            }
        }
        delay(500);
  
        // Make Letter "R" from array
        for(int row = 0; row <= 7; row++)
        {
            Matrix.setRow(1, row, R[row]);
            delay(100);
        }
        delay(1000);

        // invert display
        Matrix.invertDisplay(1);
        delay(1000);
  
        // clear display
        Matrix.clearDisplay(1);
        delay(1000);
    }
    ```
2. Überprüfen Sie die Datei "vcpSPI_Dot8x8.ino" und laden Sie sie auf das VCP-G hoch.
3. Wenn der Upload-Vorgang in einem endlosen Upload-Zustand hängen bleibt, liegt dies daran, dass der FWDN-Modus nicht aktiviert ist. So beheben Sie dies:  
    1. Trennen Sie das Stromkabel vom VCP-G-Board.
    2. Halten Sie den FWDN-Schalter gedrückt.
    3. Schließen Sie das Stromkabel wieder an, während Sie den FWDN-Schalter weiterhin gedrückt halten.
    4. Lassen Sie den FWDN-Schalter los.
        Wenn das Problem weiterhin besteht, führen Sie die Arduino IDE mit Administratorrechten aus.
4. Prüfen Sie nach dem erfolgreichen Hochladen der Datei die Ausgabekonsole der Arduino IDE auf die folgende Meldung:  

    **Hinweis:** Die Meldung sollte **vcpSPI_Dot8x8.ino.rom** enthalten.
    ```
    [FWDN_VCP::WriteFile:577] Complete to send file - C:\Users\topst\AppData\Local\arduino\sketches\567805554B5B9F915DCC80B38483AE07/vcpSPI_Dot8x8.ino.rom

    [main:155] Complete FWDN
    ```

**Hinweis:** Wenn Sie den SPI-Pin in der Mitte des VCP-G-Boards verwenden möchten, können Sie ihn anhand der folgenden Pinnummer verwenden.
<p align="center"><strong>Tabelle 4.2 Belegung des mittleren SPI-Pins auf dem VCP-G</strong></p>
<div align="center">
	<table>
	    <tr>
	        <th colspan="3">Pinnummer</th>
	        <th>SPI-Funktion</th>
	        <th>Arduino IDE</th>
	    </tr>
	    <tr>
	        <td colspan="3">1</td>
	        <td>MISO</td>
	        <td>58</td>
	    </tr>
	    <tr>
	        <td colspan="3">2</td>
	        <td>5V</td>
	        <td>-</td>
	    </tr>
	        <tr>
	        <td colspan="3">3</td>
	        <td>SCK</td>
	        <td>59</td>
	    </tr>
	    <tr>
	        <td colspan="3">4</td>
	        <td>MOSI</td>
	        <td>60</td>
	    </tr>
	    <tr>
	        <td colspan="3">5</td>
	        <td>CMD</td>
	        <td>61</td>
	    </tr>
	    <tr>
	        <td colspan="3">6</td>
	        <td>GND</td>
	        <td>-</td>
	    </tr>
	</table>
</div> 

</br></br></br></br>

# 5. VCP-G I2C
---
In diesem Kapitel wird beschrieben, wie die Kommunikation über Inter-integrated Circuit (I2C) auf dem VCP-G konfiguriert wird.  
I2C ist ein synchrones Zweidraht-Kommunikationsprotokoll, das für den effizienten Datenaustausch zwischen mehreren Geräten entwickelt wurde. Es arbeitet mit einer seriellen Datenleitung (SDA) und einer seriellen Taktleitung (SCL), sodass mehrere Peripheriegeräte über eindeutige Adressen mit einem Mikrocontroller kommunizieren können. I2C unterstützt sowohl die Master-Slave-Kommunikation als auch Multi-Master-Konfigurationen und eignet sich damit ideal für den Anschluss von Sensoren, Displays und anderen langsamen Geräten bei minimaler Anzahl erforderlicher Verbindungen.

</br></br></br>

## 5.1 vcpI2C_LCD1602
---
Dieses Beispielprogramm zeigt, wie das VCP-G-Board ein LCD1602-Display über das I2C-Kommunikationsprotokoll steuert. Das LCD1602 ist ein Flüssigkristalldisplay mit 16 Zeichen und 2 Zeilen, das häufig in Projekten mit eingebetteten Systemen eingesetzt wird. Mithilfe der Bibliothek LiquidCrystal_I2C sendet das Board Befehle und Daten über den I2C-Bus, um das Display effizient zu steuern.

In diesem Beispiel wird das LCD initialisiert und die Hintergrundbeleuchtung für eine gute Lesbarkeit aktiviert. Anschließend positioniert das Programm den Cursor, um den Text "VCP-G" in der ersten Zeile und "I2C Test!" in der zweiten Zeile anzuzeigen. Mit der I2C-Kommunikation lassen sich mehrere Geräte mit minimaler Verkabelung steuern, was eine effektive Lösung für kompakte Projekte darstellt.
</br></br>

### 5.1.1 Hardware-Anforderungen
- VCP-G-Board (x1)
- LCD1602 (x1)
- 12V 1A Netzteil (x1)
- USB-Type-C-auf-A-Kabel (x1)
- Jumperkabel Stecker auf Buchse (x4)
</br></br>

### 5.1.2 Schaltung
- LCD1602
    - Der VCC-Pin des LCD1602 ist mit dem analogen Pin 5V auf dem VCP-G-Board verbunden.
    - Der GND-Pin des LCD1602 ist mit GND auf dem VCP-G-Board verbunden.
    - Der SDA-Pin des LCD1602 ist mit Pin 48 auf dem VCP-G-Board verbunden.
    - Der SCL-Pin des LCD1602 ist mit Pin 49 auf dem VCP-G-Board verbunden.

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/vcpI2C_LCD1602%20Circuit%20Schematic.png"></p>
<p align="center"><strong>Abbildung 5.1 Schaltplan von vcpI2C_LCD1602</strong></p>

#### 5.1.2.1 Pinbelegung
Die folgende Tabelle zeigt die Pinbelegung.

<p align="center"><strong>Tabelle 5.1 Pinbelegung von vcpI2C_LCD1602</strong></p>
<div align="center">
	<table>
	    <tr>
	        <th colspan="3">Pinname</th>
	        <th>VCP-G-Board</th>
	        <th>Arduino IDE</th>
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
	        <td>48</td>
	        <td>-</td>
	    </tr>
	    <tr>
	        <td colspan="3">SCL-Pin des LCD1602</td>
	        <td>49</td>
		    <td>-</td>
	    </tr>
	</table>
</div>

</br></br>

### 5.1.3 Ausführung
1. Öffnen Sie die Datei "vcpI2C_LCD1602.ino".  
    1. Öffnen Sie die Arduino IDE  
    2. Klicken Sie auf **File -> Examples -> 04.VCP-G I2C -> vcpI2C_LCD1602**.
    ```
    #include <LiquidCrystal_I2C.h>
  
    LiquidCrystal_I2C lcd(0x27,16,2);  // set the LCD address to 0x27 for a 16 chars and 2 line display

    void setup()
    {
        LiquidCrystal_I2C lcd(0x27,16,2);

        lcd.init(); 
        lcd.backlight(); // initialize the lcd 

        lcd.setCursor(2, 0);
        delay(10);
        lcd.print("* TOPST VCP-G *");
  
        lcd.setCursor(4, 1);
        delay(10);
        lcd.print("I2C Test!");
    }

    void loop()
    {  

    }
    ```
2. Überprüfen Sie die Datei "vcpI2C_LCD1602.ino" und laden Sie sie auf das VCP-G hoch.
3. Wenn der Upload-Vorgang in einem endlosen Upload-Zustand hängen bleibt, liegt dies daran, dass der FWDN-Modus nicht aktiviert ist. So beheben Sie dies:  
    1. Trennen Sie das Stromkabel vom VCP-G-Board.
    2. Halten Sie den FWDN-Schalter gedrückt.
    3. Schließen Sie das Stromkabel wieder an, während Sie den FWDN-Schalter weiterhin gedrückt halten.
    4. Lassen Sie den FWDN-Schalter los.
        Wenn das Problem weiterhin besteht, führen Sie die Arduino IDE mit Administratorrechten aus.
4. Prüfen Sie nach dem erfolgreichen Hochladen der Datei die Ausgabekonsole der Arduino IDE auf die folgende Meldung:
   
    **Hinweis:** Die Meldung sollte **vcpI2C_LCD1602.ino.rom** enthalten.
    ```
    [FWDN_VCP::WriteFile:577] Complete to send file -         C:\Users\topst\AppData\Local\arduino\sketches\C8D91A6857B651D6C665B0EF18B7EE53/vcpI2C_LCD1602.ino.rom

    [main:155] Complete FWDN
    ```

</br></br></br></br>

# 6. VCP-G UART
---
In diesem Kapitel wird beschrieben, wie die Kommunikation über den Universal Asynchronous Receiver-Transmitter (UART) auf dem VCP-G konfiguriert wird.  
UART ist ein weit verbreitetes serielles Kommunikationsprotokoll, das Daten asynchron über nur zwei Leitungen überträgt: Transmit (TX) und Receive (RX). Es ist unverzichtbar für den Datenaustausch zwischen Mikrocontrollern, Sensoren und Computern, ohne dass ein gemeinsames Taktsignal erforderlich ist.  
In den folgenden Kapiteln wird beschrieben, wie Daten über UART gesendet und empfangen werden.

</br></br></br>

## 6.1 vcpASCIITable
---
Dieses Beispielprogramm zeigt, wie das VCP-G die ASCII-Werte von Zeichen in verschiedenen Formaten ausgibt: dezimal, hexadezimal, oktal und binär. Es beginnt beim Zeichen '!' (ASCII-Wert 33) und durchläuft alle sichtbaren ASCII-Zeichen, wobei jedes in den verschiedenen Formaten ausgegeben wird. Das Programm läuft weiter, bis es das Zeichen '~' (ASCII-Wert 126) erreicht.
</br></br>

### 6.1.1 Hardware-Anforderungen
- VCP-G-Board (x1)
- 12V 1A Netzteil (x1)
- USB-Type-C-auf-A-Kabel (x1)
</br></br>

### 6.1.3 Ausführung
1. Öffnen Sie die Datei "vcpASCIITable.ino".
    1. Öffnen Sie die Arduino IDE.
    2. Klicken Sie auf **File -> Examples -> 05.VCP-G UART -> vcpASCIITable**.
    ```
    /*
    ASCII table

    Prints out byte values in all possible formats:
    - as raw binary values
    - as ASCII-encoded decimal, hex, octal, and binary values

    For more on ASCII, see http://www.asciitable.com and http://en.wikipedia.org/wiki/ASCII

    The circuit: No external hardware needed.

    created 2006
    by Nicholas Zambetti <http://www.zambetti.com>
    modified 9 Apr 2012
    by Tom Igoe

    This example code is in the public domain.

    https://www.arduino.cc/en/Tutorial/BuiltInExamples/ASCIITable
    */

    #include "HardwareSerial.h"
    HardwareSerial Serial;

    void setup() {
        //Initialize serial and wait for port to open:
        Serial.begin(115200);
        while (!Serial) {
            ;  // wait for serial port to connect. Needed for native USB port only
        }

        // prints title with ending line break
        Serial.println("ASCII Table ~ Character Map");
    }

    // first visible ASCIIcharacter '!' is number 33:
    int thisByte = 33;
    // you can also write ASCII characters in single quotes.
    // for example, '!' is the same as 33, so you could also use this:
    // int thisByte = '!';

    void loop() {
        // prints value unaltered, i.e. the raw binary version of the byte.
        // The Serial Monitor interprets all bytes as ASCII, so 33, the first number,
        // will show up as '!'

        Serial.print(", dec: ");
        // prints value as string as an ASCII-encoded decimal (base 10).
        // Decimal is the default format for Serial.print() and Serial.println(),
        // so no modifier is needed:
        Serial.print(thisByte);
        // But you can declare the modifier for decimal if you want to.
        // this also works if you uncomment it:

        // Serial.print(thisByte, DEC);

        Serial.print(", hex: ");
        // prints value as string in hexadecimal (base 16):
        Serial.print(thisByte, HEX);

        Serial.print(", oct: ");
        // prints value as string in octal (base 8);
        Serial.print(thisByte, OCT);

        Serial.print(", bin: ");
        // prints value as string in binary (base 2) also prints ending line break:
        Serial.println(thisByte, BIN);

        // if printed last visible character '~' or 126, stop:
        if (thisByte == 126) {  // you could also use if (thisByte == '~') {
            // This loop loops forever and does nothing
            while (true) {
                continue;
            }
        }
        // go on to the next character
        thisByte++;
        }
    }
    ```
2. Überprüfen Sie die Datei "vcpASCIITable.ino" und laden Sie sie auf das VCP-G hoch.
3. Wenn der Upload-Vorgang in einem endlosen Upload-Zustand hängen bleibt, liegt dies daran, dass der FWDN-Modus nicht aktiviert ist. So beheben Sie dies:  
    1. Trennen Sie das Stromkabel vom VCP-G-Board.
    2. Halten Sie den FWDN-Schalter gedrückt.
    3. Schließen Sie das Stromkabel wieder an, während Sie den FWDN-Schalter weiterhin gedrückt halten.
    4. Lassen Sie den FWDN-Schalter los.
        Wenn das Problem weiterhin besteht, führen Sie die Arduino IDE mit Administratorrechten aus.
4. Prüfen Sie nach dem erfolgreichen Hochladen der Datei die Ausgabekonsole der Arduino IDE auf die folgende Meldung:  

    **Hinweis:** Die Meldung sollte **vcpASCIITable.ino.rom** enthalten.
    ```
    [FWDN_VCP::WriteFile:577] Complete to send file - C:\Users\topstAppData\Local\arduino\sketches\487F45098412336AA9D73C50C17E07D8/vcpASCIITable.ino.rom

    [main:155] Complete FWDN
    ```

</br></br></br>

## 6.2 vcpGraph
---
Dieses Beispielprogramm zeigt, wie das VCP-G den Analogwert des Potentiometers auf dem Steckbrett liest und die Daten über UART an den Host-PC überträgt. Der Arduino-Code liest kontinuierlich den Wert des an Pin A5 angeschlossenen analogen Sensors (Potentiometer) und sendet ihn über den seriellen Port. Der zugehörige Processing-Code visualisiert diese Werte in Echtzeit in einem dynamischen Diagramm und zeigt so die Änderung des Sensoreingangs im zeitlichen Verlauf.
</br></br>

### 6.2.1 Hardware-Anforderungen
- VCP-G-Board (x1)
- Breadboard (x1)
- Potentiometer (x1)
- 10 kΩ-Widerstand (x1)
- 12V 1A Netzteil (x1)
- USB-Type-C-auf-A-Kabel (x1)
- Jumperkabel Stecker auf Stecker (x4)
</br></br>

### 6.2.2 Schaltung
- Potentiometer
    - Der mittlere Pin des Potentiometers ist mit dem analogen Pin A5 auf dem VCP-G-Board verbunden.
    - Der GND-Pin des Potentiometers ist über einen 10 kΩ-Widerstand mit GND auf dem VCP-G-Board verbunden.
    - Der VCC-Pin des Potentiometers ist mit 3.3V auf dem VCP-G-Board verbunden.

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/vcpGraph%20Circuit%20Schematic.png"></p>
<p align="center"><strong>Abbildung 6.1 Schaltplan von vcpGraph</strong></p>

#### 6.2.2.1 Pinbelegung
Die folgende Tabelle zeigt die Pinbelegung.

<p align="center"><strong>Tabelle 6.1 Pinbelegung von vcpGraph</strong></p>
<div align="center">
	<table>
	    <tr>
	        <th colspan="3">Pinname</th>
	        <th>VCP-G-Board</th>
	        <th>Arduino IDE</th>
	    </tr>
	    <tr>
	        <td colspan="3">Mittlerer Pin des Potentiometers</td>
	        <td>A5</td>
	        <td>A5</td>
	    </tr>
	        <tr>
	        <td colspan="3">GND-Pin des Potentiometers</td>
	        <td>GND</td>
	        <td>-</td>
	    </tr>
	    <tr>
	        <td colspan="3">VCC-Pin des Potentiometers</td>
	        <td>3.3V</td>
	        <td>-</td>
	    </tr>
	</table>
</div>
</br></br>

### 6.2.3 Ausführung
1. Öffnen Sie die Datei "vcpGraph.ino".
    1. Öffnen Sie die Arduino IDE.
    2. Klicken Sie auf **File -> Examples -> 05.VCP-G UART -> vcpGraph**.
    ```
    /*
    Graph

    A simple example of communication from the Arduino board to the computer: The
    value of analog input 0 is sent out the serial port. We call this "serial"
    communication because the connection appears to both the Arduino and the
    computer as a serial port, even though it may actually use a USB cable. Bytes
    are sent one after another (serially) from the Arduino to the computer.

    You can use the Arduino Serial Monitor to view the sent data, or it can be
    read by Processing, PD, Max/MSP, or any other program capable of reading data
    from a serial port. The Processing code below graphs the data received so you
    can see the value of the analog input changing over time.

    The circuit:
    - any analog input sensor attached to analog in pin 0

    created 2006
    by David A. Mellis
    modified 9 Apr 2012
    by Tom Igoe and Scott Fitzgerald

    This example code is in the public domain.

    https://www.arduino.cc/en/Tutorial/BuiltInExamples/Graph
    */

    #include "HardwareSerial.h"
    HardwareSerial Serial;

    void setup() {
        // initialize the serial communication:
        Serial.begin(115200);
        for(;;)
        {
            Serial.println(analogRead(A5));
            // wait a bit for the analog-to-digital converter to stabilize after the last
            // reading:
            delay(2);
        }
    }

    void loop() {
        // send the value of analog input 0:
        // Serial.println(analogRead(A0));
        // // wait a bit for the analog-to-digital converter to stabilize after the last
        // // reading:
        // delay(2);
    }

    /* Processing code for this example

    // Graphing sketch

    // This program takes ASCII-encoded strings from the serial port at 9600 baud
    // and graphs them. It expects values in the range 0 to 1023, followed by a
    // newline, or newline and carriage return

    // created 20 Apr 2005
    // updated 24 Nov 2015
    // by Tom Igoe
    // This example code is in the public domain.

    import processing.serial.*;

    Serial myPort;        // The serial port
    int xPos = 1;         // horizontal position of the graph
    float inByte = 0;

    void setup () {
        // set the window size:
        size(400, 300);

        // List all the available serial ports
        // if using Processing 2.1 or later, use Serial.printArray()
        println(Serial.list());

        // I know that the first port in the serial list on my Mac is always my
        // Arduino, so I open Serial.list()[0].
        // Open whatever port is the one you're using.
        myPort = new Serial(this, Serial.list()[0], 9600);

        // don't generate a serialEvent() unless you get a newline character:
        myPort.bufferUntil('\n');

        // set initial background:
        background(0);
    }

    void draw () {
        // draw the line:
        stroke(127, 34, 255);
        line(xPos, height, xPos, height - inByte);

        // at the edge of the screen, go back to the beginning:
        if (xPos >= width) {
            xPos = 0;
            background(0);
        } else {
            // increment the horizontal position:
        xPos++;
        }
    }

    void serialEvent (Serial myPort) {
        // get the ASCII string:
        String inString = myPort.readStringUntil('\n');

        if (inString != null) {
            // trim off any whitespace:
            inString = trim(inString);
            // convert to an int and map to the screen height:
            inByte = float(inString);
            println(inByte);
            inByte = map(inByte, 0, 1023, 0, height);
        }
    }

    */
    ```
2. Überprüfen Sie die Datei "vcpGraph.ino" und laden Sie sie auf das VCP-G hoch.
3. Wenn der Upload-Vorgang in einem endlosen Upload-Zustand hängen bleibt, liegt dies daran, dass der FWDN-Modus nicht aktiviert ist. So beheben Sie dies:  
    1. Trennen Sie das Stromkabel vom VCP-G-Board.
    2. Halten Sie den FWDN-Schalter gedrückt.
    3. Schließen Sie das Stromkabel wieder an, während Sie den FWDN-Schalter weiterhin gedrückt halten.
    4. Lassen Sie den FWDN-Schalter los.
        Wenn das Problem weiterhin besteht, führen Sie die Arduino IDE mit Administratorrechten aus.
4. Prüfen Sie nach dem erfolgreichen Hochladen der Datei die Ausgabekonsole der Arduino IDE auf die folgende Meldung:

    **Hinweis:** Die Meldung sollte **vcpGraph.ino.rom** enthalten.
    ```
    [FWDN_VCP::WriteFile:577] Complete to send file - C:\Users\topst\AppData\Local\arduino\sketches\F59E4532EC3A529F5910F376F809A5E5/vcpGraph.ino.rom

    [main:155] Complete FWDN
    ```

</br></br></br></br>

# 7. Weitere Beispiele
---
In diesem Kapitel werden zusätzliche Sensorbeispiele bereitgestellt, die nicht in den "Examples for TOPST VCP Rev G" in der Arduino IDE enthalten sind.  
Es enthält Beispielanleitungen für die Verwendung gängiger Arduino-Sensoren mit dem VCP-G-Board, damit Sie verschiedene Sensoren effektiv in Ihre Projekte integrieren können.

</br></br></br>

## 7.1 Infrarotsensor (IR) (Transceiver)
---
### 7.1.1 Infrarotsensor (IR) 1
---
Dieses Beispiel zeigt, wie das VCP-G-Board einen IR-Sensor und zwei LEDs auf dem Steckbrett steuert. Ist der IR-Sensorwert nach dem Auslesen HIGH, wird davon ausgegangen, dass kein Hindernis vorhanden ist, und die grüne LED leuchtet auf, während die rote LED erlischt. Ist der IR-Sensorwert dagegen LOW, wird davon ausgegangen, dass ein Hindernis vorhanden ist, und die rote LED leuchtet auf, während die grüne LED erlischt. Zusätzlich wird das Vorhandensein oder Fehlen eines Hindernisses auf dem seriellen Monitor angezeigt.

#### 7.1.1.1 Hardware-Anforderungen
- VCP-G-Board (x1)
- Breadboard (x1)
- IR-Transceiver-Sensor (x1)
- LED (x2: Unterschiedliche Farben werden empfohlen)
- 220Ω-Widerstände (x2)
- 12V 1A Netzteil (x1)
- USB-Type-C-auf-A-Kabel (x1)
- Jumperkabel Stecker auf Stecker (x4)
- Jumperkabel Stecker auf Buchse (x3)

#### 7.1.1.2 Schaltung
- IR-Transceiver-Sensor
    - Der OUT-Pin des IR-Sensors ist mit Pin 50 auf dem VCP-G-Board verbunden.
    - Der VCC-Pin des IR-Sensors ist mit 5V auf dem VCP-G-Board verbunden.
    - Der GND-Pin des IR-Sensors ist mit GND auf dem VCP-G-Board verbunden.
- Rote LED
    - Der (-)-Anschluss der LED ist mit dem Widerstand verbunden, und der Widerstand ist mit GND auf dem VCP-G-Board verbunden.
    - Der (+)-Anschluss der LED ist mit Pin 48 auf dem VCP-G-Board verbunden.
- Grüne LED
    - Der (-)-Anschluss der LED ist mit dem Widerstand verbunden, und der Widerstand ist mit GND auf dem VCP-G-Board verbunden.
    - Der (+)-Anschluss der LED ist mit Pin 17 auf dem VCP-G-Board verbunden.

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/Infrared%20(IR)%20Sensor%20Circuit%20Schematic.png"></p>
<p align="center"><strong>Abbildung 7.1 Schaltplan des Infrarotsensors (IR)</strong></p>

##### 7.1.1.2.1 Pinbelegung
Die folgende Tabelle zeigt die Pinbelegung.

<p align="center"><strong>Tabelle 7.1 Pinbelegung von irSensor_LED</strong></p>
<div align="center">
	<table>
	    <tr>
	        <th colspan="3">Pinname</th>
	        <th>VCP-G-Board</th>
	        <th>Arduino IDE</th>
	    </tr>
	    <tr>
	        <td colspan="3">OUT-Pin des IR-Sensors </td>
	        <td>50</td>
	        <td>50</td>
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
	        <td colspan="3">(+)-Pin der roten LED</td>
	        <td>48</td>
	        <td>48</td>
	    </tr>
	    <tr>
	        <td colspan="3">(-)-Pin der roten LED</td>
	        <td>GND</td>
	        <td>-</td>
	    </tr>
	    <tr>
	        <td colspan="3">(+)-Pin der grünen LED</td>
	        <td>17</td>
	        <td>17</td>
	    </tr>
	    <tr>
	        <td colspan="3">(-)-Pin der grünen LED </td>
	        <td>GND</td>
	        <td>-</td>
	    </tr>
	</table>
</div>

#### 7.1.1.3 Ausführung
1. Kopieren Sie den folgenden Quellcode in die Arduino IDE und speichern Sie die Datei als "irSensor_LED.ino".
    
   **Hinweis:** Der folgende Quellcode wird nur in diesem Dokument bereitgestellt. 

    ```
    #include "HardwareSerial.h" 
    HardwareSerial Serial; 
 
    // Control LEDs based on obstacle detection using an IR sensor
    int outputPin = 50, red = 48, green = 17; 
 
    void setup() { 
        pinMode(outputPin, INPUT); 
        pinMode(red, OUTPUT); 
        pinMode(green, OUTPUT); 
        Serial.begin(115200); 
    } 
 
    void loop() { 
        // Read the value from the IR sensor
        int value = digitalRead(outputPin); 
 
        // Control LEDs based on the presence of an obstacle
        if (value == HIGH) { 
            // No obstacle detected
            digitalWrite(red, LOW); 
            digitalWrite(green, HIGH); 
            Serial.println("No object detected.");  
        } 
        else { 
            // Obstacle detected
            digitalWrite(red, HIGH); 
            digitalWrite(green, LOW); 
            Serial.println("Object detected!");  
        } 
    }
    ```
2. Überprüfen Sie die Datei "irSensor_LED.ino" und laden Sie sie auf das VCP-G hoch.
3. Wenn der Upload-Vorgang in einem endlosen Upload-Zustand hängen bleibt, liegt dies daran, dass der FWDN-Modus nicht aktiviert ist. So beheben Sie dies:  
    1. Trennen Sie das Stromkabel vom VCP-G-Board.
    2. Halten Sie den FWDN-Schalter gedrückt.
    3. Schließen Sie das Stromkabel wieder an, während Sie den FWDN-Schalter weiterhin gedrückt halten.
    4. Lassen Sie den FWDN-Schalter los.
        Wenn das Problem weiterhin besteht, führen Sie die Arduino IDE mit Administratorrechten aus.
4. Prüfen Sie nach dem erfolgreichen Hochladen der Datei die Ausgabekonsole der Arduino IDE auf die folgende Meldung:
 
    **Hinweis:** Die Meldung sollte **irSensor_LED.ino.rom** enthalten.
    ```
    [FWDN_VCP::WriteFile:577] Complete to send file - C:\Users\topst\AppData\Local\arduino\sketches\1D003A72AB3391D6D60FD7993380F8CD/irSensor_LED.ino.rom 

    [main:155] Complete FWDN
    ```
</br></br>

### 7.1.2 Infrarotsensor (IR) 2
---
Dieses Beispiel zeigt, wie das VCP-G-Board einen IR-Sensor zur Objekterkennung steuert und den Erkennungsstatus auf dem seriellen Monitor ausgibt. Der IR-Transceiver erfasst das Vorhandensein eines Hindernisses. Ist der Wert des IR-Transceivers HIGH, bedeutet dies, dass kein Hindernis vorhanden ist, und die grüne LED leuchtet auf und die rote LED erlischt. Ist der Wert des IR-Transceivers dagegen LOW, bedeutet dies, dass ein Hindernis vorhanden ist, und die rote LED leuchtet auf und die grüne LED erlischt. Zusätzlich wird das Vorhandensein oder Fehlen eines Hindernisses auf dem seriellen Monitor angezeigt.

#### 7.1.2.1 Hardware-Anforderungen
- VCP-G-Board (x1)
- IR-Transceiver-Sensor (x1)
- 12V 1A Netzteil (x1)
- USB-Type-C-auf-A-Kabel (x1)
- Jumperkabel Stecker auf Buchse (x3)

#### 7.1.2.2 Schaltung
- IR-Transceiver-Sensor
    - Der Out-Pin des IR-Transceiver-Sensors ist mit Pin 8 auf dem VCP-G-Board verbunden. 
    - Der VCC-Pin des IR-Transceiver-Sensors ist mit 5V auf dem VCP-G-Board verbunden.
    - Der GND-Pin des IR-Transceiver-Sensors ist mit GND auf dem VCP-G-Board verbunden.

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/Infrared%20(IR)%20Sensor%20(Transceiver)%20Circuit%20Schematic.png"></p>
<p align="center"><strong>Abbildung 7.2 Schaltplan des Infrarotsensors (IR) (Transceiver)</strong></p>

##### 7.1.2.2.1 Pinbelegung
Die folgende Tabelle zeigt die Pinbelegung.

<p align="center"><strong>Tabelle 7.2 Pinbelegung von irTransceiver</strong></p>
<div align="center">
	<table>
	    <tr>
	        <th colspan="3">Pinname</th>
	        <th>VCP-G-Board</th>
	        <th>Arduino IDE</th>
	    </tr>
	    <tr>
	        <td colspan="3">OUT-Pin des IR-Transceiver-Sensors</td>
	        <td>8</td>
	        <td>8</td>
	    </tr>
	    <tr>
	        <td colspan="3">VCC-Pin des IR-Transceiver-Sensors</td>
	        <td>5V</td>
	        <td>-</td>
	    </tr>
	    <tr>
	        <td colspan="3">GND-Pin des IR-Transceiver-Sensors</td>
	        <td>GND</td>
	        <td>-</td>
	    </tr>
	</table>
</div>

#### 7.1.2.3 Ausführung
1. Kopieren Sie den folgenden Quellcode in die Arduino IDE und speichern Sie die Datei als "irTransceiver.ino".
   
   **Hinweis:** Der folgende Quellcode wird nur in diesem Dokument bereitgestellt. 

    ```
    /*  
    This code prints "Detected" to the Serial Monitor when an object is detected,   
    and "Not Detected" when no object is detected.  
    */  
  
    #include "HardwareSerial.h"  
    HardwareSerial Serial;  
  
    int sensorValue = 8;  
    int val = 0;  
  
    void setup() {  
        Serial.begin(9600);  
        pinMode(sensorValue, INPUT);  
    }  
  
    void loop() {  
        val = digitalRead(sensorValue);  
        if (val == HIGH) {  
            Serial.println("Not Detected");  
        }  
        else {  
            Serial.println("Detected");  
        }  
    }  
    ```
2. Überprüfen Sie die Datei "irTransceiver.ino" und laden Sie sie auf das VCP-G hoch.
3. Wenn der Upload-Vorgang in einem endlosen Upload-Zustand hängen bleibt, liegt dies daran, dass der FWDN-Modus nicht aktiviert ist. So beheben Sie dies:  
    1. Trennen Sie das Stromkabel vom VCP-G-Board.
    2. Halten Sie den FWDN-Schalter gedrückt.
    3. Schließen Sie das Stromkabel wieder an, während Sie den FWDN-Schalter weiterhin gedrückt halten.
    4. Lassen Sie den FWDN-Schalter los.
        Wenn das Problem weiterhin besteht, führen Sie die Arduino IDE mit Administratorrechten aus.
4. Prüfen Sie nach dem erfolgreichen Hochladen der Datei die Ausgabekonsole der Arduino IDE auf die folgende Meldung:
   
    **Hinweis:** Die Meldung sollte **irTransceiver.ino.rom** enthalten.
    ```
    [FWDN_VCP::WriteFile:577] Complete to send file - C:\Users\topst\AppData\Local\arduino\sketches\1D003A72AB3391D6D60FD7993380F8CD/irTransceiver.ino.rom 

    [main:155] Complete FWDN
    ```

</br></br></br>

## 7.2 Joystick
---
Dieses Beispiel zeigt, wie das VCP-G Joystick-Eingaben liest und deren Wert auf dem seriellen Monitor anzeigt. Sie können drei Eingaben empfangen: X-Achse, Y-Achse und Tasten. Der serielle Monitor überprüft die empfangenen Signale. Die Bewegungen auf der X- und der Y-Achse ändern den Wert des Ports, der dem numerischen Wert des analogen Ausgangs entspricht. Dies ermöglicht eine präzise Steuerung für Anwendungen, die eine Feinjustierung erfordern.

**Hinweis:** Das Dual Axis Joystick Module (KY-023) ist ein Produkt von Joy-IT. Alle Rechte an Design, Marke und zugehörigem geistigem Eigentum liegen bei Joy-IT.
</br></br>

### 7.2.1 Hardware-Anforderungen
- VCP-G-Board (x1)
- Dual Axis Joystick Module (KY-023) (x1)
- 12V 1A Netzteil (x1)
- USB-Type-C-auf-A-Kabel (x1)
- Stecker-auf-Buchse-Jumperkabel (x5)
</br></br>

### 7.2.2 Schaltung
- KY-023 (Dual Axis Joystick Module)
    - Der 5V-Pin des KY-023 ist mit 5V auf dem VCP-G-Board verbunden.
    - Der GND-Pin des KY-023 ist mit GND auf dem VCP-G-Board verbunden. 
    - Der VRx-Pin des KY-023 ist mit dem analogen Pin A5 auf dem VCP-G-Board verbunden. 
    - Der VRy-Pin des KY-023 ist mit dem analogen Pin A4 auf dem VCP-G-Board verbunden. 
    - Der SW-Pin des KY-023 ist mit Pin 2 auf dem VCP-G-Board verbunden.

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/Joystick%20Circuit%20Schematic.png"></p>
<p align="center"><strong>Abbildung 7.3 Schaltplan des Joysticks</strong></p>

#### 7.2.2.1 Pinbelegung
Die folgende Tabelle zeigt die Pinbelegung.

<p align="center"><strong>Tabelle 7.3 Pinbelegung des Joysticks</strong></p>
<div align="center">
	<table>
	    <tr>
	        <th colspan="3">Pinname</th>
	        <th>VCP-G-Board</th>
	        <th>Arduino IDE</th>
	    </tr>
	    <tr>
	        <td colspan="3">VRx</td>
	        <td>A5</td>
	        <td>A5</td>
	    </tr>
	        <tr>
	        <td colspan="3">VRy</td>
	        <td>A4</td>
	        <td>A4</td>
	    </tr>
	    <tr>
	        <td colspan="3">SW</td>
	        <td>2</td>
	        <td>2</td>
	    </tr>
	    <tr>
	        <td colspan="3">5V</td>
	        <td>5V</td>
	        <td>-</td>
	    </tr>
	    <tr>
	        <td colspan="3">GND</td>
	        <td>GND</td>
	        <td>-</td>
	    </tr>
	</table>
</div>
</br></br>

### 7.2.3 Ausführung
1. Kopieren Sie den folgenden Quellcode in die Arduino IDE und speichern Sie die Datei als "joystick.ino".
   
   **Hinweis:** Der folgende Quellcode wird nur in diesem Dokument bereitgestellt. 

    ```
    #include "HardwareSerial.h"  
    HardwareSerial Serial;  
  
    int X = A5; //VCP A5 pin  
    int Y = A4; //VCP A4 pin  
    int SW = 2; //VCP 2 pin  
  
    void setup()  
    {  
        pinMode(SW, INPUT_PULLUP);    
        pinMode(X, INPUT);             
        pinMode(Y, INPUT);             
        Serial.begin(9600);        
    }  
  
    void loop()  
    {  
        Serial.print(" Switch: ");  
        Serial.print(digitalRead(SW));    
        Serial.print(" X: ");  
        Serial.print(analogRead(X));      
        Serial.print(" Y: ");  
        Serial.println(analogRead(Y));    
        delay(100);  
    } 
    ```
2. Überprüfen Sie die Datei "joystick.ino" und laden Sie sie auf das VCP-G hoch.
3. Wenn der Upload-Vorgang in einem endlosen Upload-Zustand hängen bleibt, liegt dies daran, dass der FWDN-Modus nicht aktiviert ist. So beheben Sie dies:  
    1. Trennen Sie das Stromkabel vom VCP-G-Board.
    2. Halten Sie den FWDN-Schalter gedrückt.
    3. Schließen Sie das Stromkabel wieder an, während Sie den FWDN-Schalter weiterhin gedrückt halten.
    4. Lassen Sie den FWDN-Schalter los.  
        Wenn das Problem weiterhin besteht, führen Sie die Arduino IDE mit Administratorrechten aus.
4. Prüfen Sie nach dem erfolgreichen Hochladen der Datei die Ausgabekonsole der Arduino IDE auf die folgende Meldung:
   
    **Hinweis:** Die Meldung sollte **joystick.ino.rom** enthalten.
    ```
    [FWDN_VCP::WriteFile:577] Complete to send file - C:\Users\topst\AppData\Local\arduino\sketches\1D003A72AB3391D6D60FD7993380F8CD/joystick.ino.rom 

    [main:155] Complete FWDN
    ```

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
    - Der A0-Pin des Gassensors ist mit dem analogen Pin A5 auf dem VCP-G-Board verbunden. 
    - Der VCC-Pin des Gassensors ist mit 5V auf dem VCP-G-Board verbunden.
    - Der GND-Pin des Gassensors ist mit GND auf dem VCP-G-Board verbunden.


<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/Gas%20Sensor%20Circuit%20Schematic.png"></p>
<p align="center"><strong>Abbildung 7.4 Schaltplan des Gassensors</strong></p>

#### 7.3.2.1 Pinbelegung
Die folgende Tabelle zeigt die Pinbelegung.

<p align="center"><strong>Tabelle 7.4 Pinbelegung des Gassensors</strong></p>
<div align="center">
	<table>
	    <tr>
	        <th colspan="3">Pinname</th>
	        <th>VCP-G-Board</th>
	        <th>Arduino IDE</th>
	    </tr>
	    <tr>
	        <td colspan="3">A0-Pin des Gassensors</td>
	        <td>A5</td>
	        <td>A5</td>
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
1. Kopieren Sie den folgenden Quellcode in die Arduino IDE und speichern Sie die Datei als "GasSensor.ino".
  
   **Hinweis:** Der folgende Quellcode wird nur in diesem Dokument bereitgestellt. 

    ```
    #include "HardwareSerial.h"  
    HardwareSerial Serial;  
  
    void setup()  
    {  
        Serial.begin(9600);        
    }  
  
    void loop()  
    {  
        float vol;  
        int sensorValue = analogRead(A5);    
        vol=(float)sensorValue/1024*5.0;  
        Serial.print(vol, 1);      
    }
     ```
2. Überprüfen Sie die Datei "GasSensor.ino" und laden Sie sie auf das VCP-G hoch.
3. Wenn der Upload-Vorgang in einem endlosen Upload-Zustand hängen bleibt, liegt dies daran, dass der FWDN-Modus nicht aktiviert ist. So beheben Sie dies:  
    1. Trennen Sie das Stromkabel vom VCP-G-Board.
    2. Halten Sie den FWDN-Schalter gedrückt.
    3. Schließen Sie das Stromkabel wieder an, während Sie den FWDN-Schalter weiterhin gedrückt halten.
    4. Lassen Sie den FWDN-Schalter los.  
        Wenn das Problem weiterhin besteht, führen Sie die Arduino IDE mit Administratorrechten aus.
4. Prüfen Sie nach dem erfolgreichen Hochladen der Datei die Ausgabekonsole der Arduino IDE auf die folgende Meldung:
   
    **Hinweis:** Die Meldung sollte **GasSensor.ino.rom** enthalten.
    ```
    [FWDN_VCP::WriteFile:577] Complete to send file - C:\Users\topst\AppData\Local\arduino\sketches\1D003A72AB3391D6D60FD7993380F8CD/joystick.ino.rom 

    [main:155] Complete FWDN
    ```
</br></br></br>

## 7.4 Metall-Touch-Sensormodul
---
Dieses Beispielprogramm zeigt, wie das VCP-G-Board einen Touch-Sensor und eine LED auf dem Steckbrett steuert. Das Metall-Touch-Sensormodul (KY-036) ist ein vielseitiger analoger/digitaler Sensor, der Berührungen auf Metalloberflächen oder menschlicher Haut erkennt. Dieses Modul verwendet einen Transistor, um bei Berührung Änderungen der elektrischen Leitfähigkeit zu erfassen, und gibt sowohl digitale als auch analoge Signale für die Interaktion mit dem VCP-G aus.  
Wenn eine Berührung erkannt wird, gibt das Metall-Touch-Sensormodul die entsprechenden digitalen/analogen Werte auf dem seriellen Monitor aus. Sie können außerdem eine LED abhängig vom Berührungsstatus steuern. 

**Hinweis:** Das Metall-Touch-Sensormodul (KY-036) verfügt über ein integriertes Potentiometer zum Einstellen der Empfindlichkeit. Sie können dieses Potentiometer drehen, um die Empfindlichkeit zu erhöhen oder zu verringern.
</br></br>

### 7.4.1 Hardware-Anforderungen
- VCP-G-Board (x1)
- Breadboard (x1)
- Metall-Touch-Sensormodul (KY-036) (x1)
- LED (x1)
- 220Ω-Widerstand (x1)
- 12V 1A Netzteil (x1)
- USB-Type-C-auf-A-Kabel (x1)
- Jumperkabel Stecker auf Stecker (x4)
- Jumperkabel Stecker auf Buchse (x4)
</br></br>

### 7.4.2 Schaltung
- Metall-Touch-Sensormodul
    - Der A0-Pin des Metall-Touch-Sensormoduls ist mit dem analogen Pin A5 auf dem VCP-G-Board verbunden.
    - Der G-Pin des Metall-Touch-Sensormoduls ist mit GND auf dem VCP-G-Board verbunden.
    - Der (+)-Pin des Metall-Touch-Sensormoduls ist mit 5V auf dem VCP-G-Board verbunden.
    - Der D0-Pin des Metall-Touch-Sensormoduls ist mit Pin 30 auf dem VCP-G-Board verbunden.

- LED
    - Der (+)-Pin der LED ist mit Pin 13 auf dem VCP-G-Board verbunden.
    - Der (-)-Pin der LED ist über einen 220Ω-Widerstand mit GND auf dem VCP-G-Board verbunden.


<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/Metal%20Touch%20Sensor%20Circuit%20Schematic.png"></p>
<p align="center"><strong>Abbildung 7.5 Schaltplan des Metall-Touch-Sensors</strong></p>

#### 7.4.2.1 Pinbelegung
Die folgende Tabelle zeigt die Pinbelegung.

<p align="center"><strong>Tabelle 7.5 Pinbelegung des Metall-Touch-Sensors</strong></p>
<div align="center">
	<table>
	    <tr>
	        <th colspan="3">Pinname</th>
	        <th>VCP-G-Board</th>
	        <th>Arduino IDE</th>
	    </tr>
	    <tr>
	        <td colspan="3">Metal-Touch-Sensormodul A0-Pin</td>
	        <td>A5</td>
	        <td>A5</td>
	    </tr>
	        <tr>
	        <td colspan="3">Metal-Touch-Sensormodul G-Pin</td>
	        <td>GND</td>
	        <td>-</td>
	    </tr>
	    <tr>
	        <td colspan="3">Metal-Touch-Sensormodul (+)-Pin</td>
	        <td>5V</td>
		    <td>-</td>
		</tr>
	    <tr>
	        <td colspan="3">Metal-Touch-Sensormodul D0-Pin</td>
	        <td>30</td>
	        <td>30</td>
	    </tr>
	    <tr>
	        <td colspan="3">LED (+) Pin</td>
	        <td>13</td>
	        <td>13</td>
	    </tr>
	    <tr>
	        <td colspan="3">LED (+) Pin</td>
	        <td>GND</td>
	        <td>-</td>
	    </tr>
	</table>
</div>
</br></br>

### 7.4.3 Ausführung
1. Kopieren Sie den folgenden Quellcode in die Arduino IDE und speichern Sie die Datei als "vcp_touch.ino"  

   **Hinweis:** Der folgende Quellcode wird nur in diesem Dokument bereitgestellt. 

    ```
    #include <Arduino.h>
    #include "HardwareSerial.h"
    HardwareSerial Serial;

    const int touchPin = 30;   // touch sensor D0 pin - VCP 30 pin
    const int ledPin = 13;     // LED - VCP 13 pin
    const int analogPin = A5; // touch sensor A0 pin - VCP A5 pin

    int touchState = 0;    // Variable to store the touch sensor state
    int touchIntensity = 0; // Variable to store the touch intensity

    void setup() {
        Serial.begin(9600);         
        pinMode(touchPin, INPUT);   
        pinMode(ledPin, OUTPUT);    
    }

    void loop() {
        touchState = digitalRead(touchPin); 
        touchIntensity = analogRead(analogPin); // Read the analog value from the sensor

        if (touchState == HIGH) {
            Serial.print("Touch detected, ");  // Print message when touch is detected
            digitalWrite(ledPin, HIGH);        // LED turns on when touch is detected
        } 
        else {
            Serial.print("No touch detected, ");  // Print message when touch is not detected
            digitalWrite(ledPin, LOW);           // LED turns off when touch is not detected
            touchIntensity = 0;                  // Set touch intensity to 0 when no touch is detected
        }

        Serial.print("Touch intensity: ");
        Serial.println(touchIntensity);  // Print the touch intensity value

        delay(500);
    }
     ```
2. Überprüfen Sie die Datei "vcp_touch.ino" und laden Sie sie auf den VCP-G hoch.
3. Wenn der Upload-Vorgang in einem endlosen Upload-Zustand hängen bleibt, liegt dies daran, dass der FWDN-Modus nicht aktiviert ist. So beheben Sie dies:  
    1. Trennen Sie das Stromkabel vom VCP-G-Board.
    2. Halten Sie den FWDN-Schalter gedrückt.
    3. Schließen Sie das Stromkabel wieder an, während Sie den FWDN-Schalter weiterhin gedrückt halten.
    4. Lassen Sie den FWDN-Schalter los.  
        Wenn das Problem weiterhin besteht, führen Sie die Arduino IDE mit Administratorrechten aus.
4. Prüfen Sie nach dem erfolgreichen Hochladen der Datei die Ausgabekonsole der Arduino IDE auf die folgende Meldung:
   
    **Hinweis:** Die Meldung sollte **vcp_touch.ino.rom** enthalten.
    ```
    [FWDN_VCP::WriteFile:577] Complete to send file - C:\Users\topst\AppData\Local\arduino\sketches\567805554B5B9F915DCC80B38483AE07/vcp_touch.ino.rom

    [main:155] Complete FWDN
    ```

**Hinweis:** Stellen Sie eine geeignete Baudrate für die serielle Kommunikation ein.

</br></br></br>

## 7.5 Schrittmotor mit Motortreiber
---
Dieses Beispiel zeigt, wie das VCP-G-Board einen 4-Draht-Schrittmotor (28BYJ-48 (5VDC)) und einen Motortreiber (ULN2003 (5V–12V)) steuert. Der Code in Kapitel 7.5.3 definiert die mit dem Motortreiber verbundenen Pins und legt die Anzahl der Schritte pro Umdrehung fest. Der Motor dreht sich eine volle Umdrehung vorwärts, pausiert, dreht sich eine volle Umdrehung rückwärts und pausiert erneut. Die Motorgeschwindigkeit wird über die Verzögerung zwischen den Schritten gesteuert, die Drehrichtung über die Reihenfolge, in der die Spulen aktiviert werden.

**Hinweis:** Der Motor 28BYJ-48 benötigt 4096 Signale für eine volle Umdrehung im Half-Step-Modus und 2048 Signale für eine volle Umdrehung im Full-Step-Modus. Für eine präzise Motorsteuerung sollte die je nach Modus erforderliche Anzahl der Signale berücksichtigt werden. 
</br></br>

### 7.5.1 Hardware-Anforderungen
- VCP-G-Board (x1)
- Schrittmotor (28BYJ-48) (x1)
- Motortreiber (ULN2003) (x1)
- 12V 1A Netzteil (x1)
- USB-Type-C-auf-A-Kabel (x1)
- Jumperkabel Stecker auf Stecker (x6)
</br></br>

### 7.5.2 Schaltung
- Motortreiber
    - Der Pin IN1 ist mit Pin 8 des VCP-G-Boards verbunden.
    - Der Pin IN2 ist mit Pin 9 des VCP-G-Boards verbunden.
    - Der Pin IN3 ist mit Pin 10 des VCP-G-Boards verbunden.
    - Der Pin IN4 ist mit Pin 11 des VCP-G-Boards verbunden.
    - Der Pin (+) ist mit 5V des VCP-G-Boards verbunden.
    - Der Pin (-) ist mit GND des VCP-G-Boards verbunden.

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/Step%20Motor%20with%20Motor%20Driver%20Circuit%20Schematic.png"></p>
<p align="center"><strong>Abbildung 7.6 Schaltplan Schrittmotor mit Motortreiber</strong></p>

#### 7.5.2.1 Pinbelegung
Die folgende Tabelle zeigt die Pinbelegung.

<p align="center"><strong>Tabelle 7.6 Pinbelegung des Motortreibers</strong></p>
<div align="center">
	<table>
	    <tr>
	        <th colspan="3">Pinname</th>
	        <th>VCP-G-Board</th>
	        <th>Arduino IDE</th>
	    </tr>
	    <tr>
	        <td colspan="3">Motortreiber IN1-Pin</td>
	        <td>8</td>
	        <td>8</td>
	    </tr>
	        <tr>
	        <td colspan="3">Motortreiber IN2-Pin</td>
	        <td>9</td>
	        <td>9</td>
	    </tr>
	    <tr>
	        <td colspan="3">Motortreiber IN3-Pin</td>
	        <td>10</td>
	        <td>10</td>
		</tr>
	    <tr>
	        <td colspan="3">Motortreiber IN4-Pin</td>
		    <td>11</td>
			<td>11</td>
	    </tr>
		<tr>
			<td colspan="3">Motortreiber (+)-Pin</td>
	        <td>5V</td>
	        <td>-</td>
		</tr>
	    <tr>
	        <td colspan="3">Motortreiber (-)-Pin</td>
	        <td>GND</td>
	        <td>-</td>
	    </tr>
	</table>
</div>
</br></br>

### 7.5.3 Ausführung
1. Kopieren Sie den folgenden Quellcode in die Arduino IDE und speichern Sie die Datei als "motordriver.ino".

    **Hinweis:** Der folgende Quellcode wird nur in diesem Dokument bereitgestellt. 

    ```
    /*
    This code controls a 4-wire stepper motor using an Arduino.
    It defines the pins connected to the motor driver and sets the number of steps per revolution.
    The motor rotates forward for one full revolution, pauses, then rotates backward for one full revolution, and pauses again.
    The motor's speed is controlled by the delay between steps, and the direction is controlled by the order in which the coils are activated.
    */

    #define IN1 8
    #define IN2 9
    #define IN3 10
    #define IN4 11

    const int stepsPerRevolution = 2037; // Number of steps per revolution

    void setup() {
        pinMode(IN1, OUTPUT);
        pinMode(IN2, OUTPUT);
        pinMode(IN3, OUTPUT);
        pinMode(IN4, OUTPUT);
    }

    void loop() {
        // Rotate forward
        for (int i = 0; i < stepsPerRevolution; i++) {
            stepMotor(i % 4); // Call stepMotor with the current step (0 to 3)
            delay(2); // Adjust speed
        }
        delay(1000);

        // Rotate backward
        for (int i = 0; i < stepsPerRevolution; i++) {
            stepMotor(3 - (i % 4)); // Call stepMotor with the current step in reverse order (3 to 0)
            delay(2);
        }
        delay(1000);
    }

    void stepMotor(int step) {
        switch (step) {
          case 0:
            digitalWrite(IN1, HIGH);
            digitalWrite(IN2, LOW);
            digitalWrite(IN3, HIGH);
            digitalWrite(IN4, LOW);
            break;
        case 1:
            digitalWrite(IN1, LOW);
            digitalWrite(IN2, HIGH);
            digitalWrite(IN3, HIGH);
            digitalWrite(IN4, LOW);
            break;
        case 2:
            digitalWrite(IN1, LOW);
            digitalWrite(IN2, HIGH);
            digitalWrite(IN3, LOW);
            digitalWrite(IN4, HIGH);
            break;
        case 3:
            digitalWrite(IN1, HIGH);
            digitalWrite(IN2, LOW);
            digitalWrite(IN3, LOW);
            digitalWrite(IN4, HIGH);
            break;
        }
    }
     ```
2. Überprüfen Sie die Datei "motordriver.ino" und laden Sie sie auf den VCP-G hoch.
3. Wenn der Upload-Vorgang in einem endlosen Upload-Zustand hängen bleibt, liegt dies daran, dass der FWDN-Modus nicht aktiviert ist. So beheben Sie dies:  
    1. Trennen Sie das Stromkabel vom VCP-G-Board.
    2. Halten Sie den FWDN-Schalter gedrückt.
    3. Schließen Sie das Stromkabel wieder an, während Sie den FWDN-Schalter weiterhin gedrückt halten.
    4. Lassen Sie den FWDN-Schalter los.  
        Wenn das Problem weiterhin besteht, führen Sie die Arduino IDE mit Administratorrechten aus.
4. Prüfen Sie nach dem erfolgreichen Hochladen der Datei die Ausgabekonsole der Arduino IDE auf die folgende Meldung:  

    **Hinweis:** Die Meldung sollte **motordriver.ino.rom** enthalten.
    ```
    [FWDN_VCP::WriteFile:577] Complete to send file - C:\Users\topst\AppData\Local\arduino\sketches\567805554B5B9F915DCC80B38483AE07/motordriver.rom

    [main:155] Complete FWDN
    ```
</br></br></br></br>

# 8. Referenzen
---
- Kontaktieren Sie TOPST für weitere Einzelheiten: topst@topst.ai

**Hinweis:** Referenzdokumente können, sofern verfügbar, je nach Vertragsbedingungen bereitgestellt werden. Wenn die Referenzdokumente
nicht verfügbar sind, können die Inhalte, die sich direkt auf Ihre Entwicklung beziehen, erläutert werden.
