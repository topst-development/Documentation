# 1. 簡介
---
本文件提供在 VCP-G 開發板上使用各種 Arduino 感測器的指引，內容包含連接說明與範例程式碼，協助您輕鬆使用 VCP-G 開發專案。

具體而言，本文件說明 VCP-G 的 Arduino IDE 範例，包括：  
- VCP-G Digital
- VCP-G Analog
- VCP-G SPI
- VCP-G I2C
- VCP-G UART
- 其他範例

使用 VCP-G 前請參閱圖 1.1。

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/vcp-g%20pinout%20Diagram.png"></p>
<p align="center"><strong>圖 1.1 VCP-G 腳位圖</strong></p>

</br></br></br></br>

# 2. VCP-G 數位腳位
---
本章提供使用 VCP-G 開發板數位腳位控制 LED 的範例。在 VCP-G 中，數位腳位用於傳送或接收二元訊號（HIGH 或 LOW），是控制 LED、開關與感測器等元件的關鍵。 

本章包含兩個範例專案，示範如何使用數位輸出控制多顆 LED，讓您對數位腳位功能有基本的了解。

</br></br></br>

## 2.1 vcp4LED
---
此範例程式示範 VCP-G 開發板如何控制麵包板上的四顆 LED。範例程式碼提供於 “vcp4LED.ino” 檔案中。將此檔案上傳至 VCP-G 後，LED 會依正向與反向順序依序亮起與熄滅，每次切換之間延遲 500 ms。 

</br></br>

### 2.1.1 硬體需求  
- VCP-G 開發板 (x1)
- 麵包板 (x1)
- LED (x4)
- 220Ω 電阻 (x4)
- 12V 1A 電源變壓器 (x1)
- USB Type-C 轉 A 傳輸線 (x1) 
- 公對公杜邦線 (x9)
</br></br>

### 2.1.2 電路
- LED01
    - (+) 腳位透過 220Ω 電阻連接至麵包板上的 5V 電源軌，該電源由 VCP-G 開發板供應。
    - (-) 腳位連接至 VCP-G 開發板上的第 47 腳位。
- LED02
    - (+) 腳位透過 220Ω 電阻連接至麵包板上的 5V 電源軌。
    - (-) 腳位連接至 VCP-G 開發板上的第 17 腳位。
- LED03
    - (+) 腳位透過 220Ω 電阻連接至麵包板上的 5V 電源軌。
    - (-) 腳位連接至 VCP-G 開發板上的第 50 腳位。
- LED04
    - (+) 腳位透過 220Ω 電阻連接至麵包板上的 5V 電源軌。
    - (-) 腳位連接至 VCP-G 開發板上的第 48 腳位。  

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/vcp4LED%20Circuit%20Schematic.png"></p>
<p align="center"><strong>圖 2.1 vcp4LED 電路圖</strong></p>

#### 2.1.2.1 腳位對應
下表列出腳位對應。

<p align="center"><strong>表 2.1 vcp4LED 的腳位對應</strong></p>
<div align="center">	
	<table>
		<tr>
			<th colspan="3">腳位名稱</th>
	        <th>VCP-G 開發板</th>
	        <th>Arduino IDE</th>
	    </tr>
	    <tr>
	        <td colspan="3">LED01 (-) 腳位</td>
	        <td>47</td>
	        <td>47</td>
	    </tr>
	        <tr>
	        <td colspan="3">LED02 (-) 腳位</td>
	        <td>17</td>
	        <td>17</td>
	    </tr>
	        <tr>
	        <td colspan="3">LED03 (-) 腳位</td>
	        <td>50</td>
	        <td>50</td>
	    </tr>
	        <tr>
	        <td colspan="3">LED04 (-) 腳位</td>
	        <td>48</td>
	        <td>48</td>
	    </tr>
	</table>
</div>
</br></br>

### 2.1.3 執行方式
1. 開啟 "vcp4LED.ino" 檔案。  
    1. 開啟 Arduino IDE。
    2. 點選 **File -> Examples -> 01.VCP-G Digital -> vcp4LED**。
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
2. 驗證並將 "vcp4LED.ino" 檔案上傳至 VCP-G。
3. 若上傳程序卡在無限上傳狀態，是因為 FWDN 模式未啟動。請依下列步驟解決：  
    1. 從 VCP-G 開發板拔除電源線。
    2. 按住 FWDN 開關不放。
    3. 持續按住 FWDN 開關的同時，重新接上電源線。
    4. 放開 FWDN 開關。
        若問題仍未解決，請嘗試以系統管理員權限執行 Arduino IDE。
4. 檔案成功上傳後，請在 Arduino IDE 輸出主控台中確認以下訊息：  

     **註：** 訊息中應包含 **vcp4LED.ino.rom**。
    ```
    [FWDN_VCP::WriteFile:577] Complete to send file - C:\Users\topst\AppData\Local\arduino\sketches\C05357299384CE5734F0E696C5A4DA3B/vcp4LED.ino.rom

    [main:155] Complete FWDN
    ```

</br></br></br>

## 2.2 vcp4LED_Button
---
此範例程式示範 VCP-G 開發板如何控制麵包板上的四顆 LED 與一個按鈕。按下按鈕時，右側兩顆 LED 熄滅，左側兩顆 LED 亮起。放開按鈕時，原本亮起的 LED 熄滅，原本熄滅的 LED 亮起。程式會持續檢查按鈕狀態並據此調整 LED。
</br></br>

### 2.2.1 硬體需求
- VCP-G 開發板 (x1)
- 麵包板 (x1)
- LED (x4)
- 按鈕開關（感測器）(x1)
- 220Ω 電阻 (x4)
- 12V 1A 電源變壓器 (x1)
- USB Type-C 轉 A 傳輸線 (x1)
- 公對公杜邦線 (x12)
</br></br>

### 2.2.2 電路
1.	LED01
    - (+) 腳位透過 220Ω 電阻連接至麵包板上的 5V 電源軌，該電源由 VCP-G 開發板供應。
    - (-) 腳位連接至 VCP-G 開發板上的第 47 腳位。
2.	LED02
    - (+) 腳位透過 220Ω 電阻連接至麵包板上的 5V 電源軌。
    - (-) 腳位連接至 VCP-G 開發板上的第 17 腳位。
3.	LED03
    - (+) 腳位透過 220Ω 電阻連接至麵包板上的 5V 電源軌。
    - (-) 腳位連接至 VCP-G 開發板上的第 50 腳位。
4.	LED04
    - (+) 腳位透過 220Ω 電阻連接至麵包板上的 5V 電源軌。
    - (-) 腳位連接至 VCP-G 開發板上的第 48 腳位。
5.	按鈕開關
    - 按鈕開關的一隻接腳連接至 VCP-G 開發板上的第 45 腳位。
    - 按鈕對角的另一隻接腳連接至 GND 腳位。

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/vcp4LED_Button%20Circuit%20Schematic.png"></p>
<p align="center"><strong>圖 2.2 vcp4LED_Button 電路圖</strong></p>

#### 2.2.2.1 腳位對應
下表列出腳位對應。

<p align="center"><strong>表 2.2 vcp4LED_Button 的腳位對應</strong></p>
<div align="center">
	<table>
	    <tr>
	        <th colspan="3">腳位名稱</th>
	        <th>VCP-G 開發板</th>
	        <th>Arduino IDE</th>
	    </tr>
	    <tr>
	        <td colspan="3">LED01 (-) 腳位</td>
	        <td>47</td>
	        <td>47</td>
	    </tr>
	        <tr>
	        <td colspan="3">LED02 (-) 腳位</td>
	        <td>17</td>
	        <td>17</td>
	    </tr>
	        <tr>
	        <td colspan="3">LED03 (-) 腳位</td>
	        <td>50</td>
	        <td>50</td>
	    </tr>
	        <tr>
	        <td colspan="3">LED04 (-) 腳位</td>
	        <td>48</td>
	        <td>48</td>
	    </tr>
	    </tr>
	        <tr>
	        <td colspan="3">按鈕的一隻接腳</td>
	        <td>45</td>
	        <td>45</td>
	    </tr>
	</table>
</div>
</br></br>

### 2.1.3 執行方式
1. 開啟 "vcp4LED_Button.ino" 檔案。
    1. 開啟 Arduino IDE。
    2. 點選 **File -> Examples -> 01.VCP-G Digital -> vcp4LED_Button**。
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
2. 驗證並將 "vcp4LED_Button.ino" 檔案上傳至 VCP-G。
3. 若上傳程序卡在無限上傳狀態，是因為 FWDN 模式未啟動。請依下列步驟解決：  
    1. 從 VCP-G 開發板拔除電源線。
    2. 按住 FWDN 開關不放。
    3. 持續按住 FWDN 開關的同時，重新接上電源線。
    4. 放開 FWDN 開關。 
        若問題仍未解決，請嘗試以系統管理員權限執行 Arduino IDE。
4. 檔案成功上傳後，請在 Arduino IDE 輸出主控台中確認以下訊息：  

    **註：** 訊息中應包含 **vcp4LED_Button.ino.rom**。
    ```
    [FWDN_VCP::WriteFile:577] Complete to send file - C:\Users\topst\AppData\Local\arduino\sketches\5CC1DB4CA216E2BC009504FAA3D06456/vcp4LED_Button.ino.rom

    [main:155] Complete FWDN
    ```

</br></br></br></br>

# 3. VCP-G 類比腳位
---
本章提供在 VCP-G 開發板上使用類比腳位的範例。在 VCP-G 中，類比腳位接收來自感測器的連續電壓訊號，可精確量測變動的輸入值。第 3.1 章、第 3.2 章與第 3.3 章說明如何使用類比腳位讀取感測器資料並控制輸出，讓您對類比輸入處理有基本的了解。

</br></br></br>

## 3.1 AnalogInOutSerial
---
此範例程式示範 VCP-G 開發板如何控制麵包板上的可變電阻與 LED。VCP-G 從類比輸入腳位讀取數值，將結果對應至 0 到 1000 的範圍，並使用此數值設定輸出腳位（連接至 LED）的脈寬調變 (PWM)。結果也會列印至序列埠監控視窗。
</br></br>

### 3.1.1 硬體需求
- VCP-G 開發板 (x1)
- 麵包板 (x1)
- LED (x1)
- 可變電阻 (x1)
- 220Ω 電阻 (x2)
- 12V 1A 電源變壓器 (x1)
- USB Type-C 轉 A 傳輸線 (x1)
- 公對公杜邦線 (x4)
</br></br>

### 3.1.2 電路
- 可變電阻
    - 可變電阻的中間腳位連接至 VCP-G 開發板上的類比腳位 A5。
    - 可變電阻的 GND 腳位連接至 VCP-G 開發板上的第 43 腳位，並透過 220Ω 電阻連接至 VCP-G 開發板上的 GND 腳位。
- LED
    - LED 的 (+) 腳位透過 220Ω 電阻連接至 VCP-G 開發板上的 3.3V。
    - LED 的 (-) 腳位連接至可變電阻的中間腳位。

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/AnalogInOutSerial%20Circuit%20Schematic.png"></p>
<p align="center"><strong>圖 3.1 AnalogInOutSerial 電路圖</strong></p>

#### 3.1.2.1 腳位對應
下表列出腳位對應。

<p align="center"><strong>表 3.1 AnalogInOutSerial 的腳位對應</strong></p>
<div align="center">
	<table>
	    <tr>
	        <th colspan="3">腳位名稱</th>
	        <th>VCP-G 開發板</th>
	        <th>Arduino IDE</th>
	    </tr>
	    <tr>
	        <td colspan="3">可變電阻中間腳位</td>
	        <td>A5</td>
	        <td>-</td>
	    </tr>
	        <tr>
	        <td colspan="3">可變電阻 GND 腳位</td>
	        <td>43</td>
	        <td>43</td>
	    </tr>
	        <tr>
	        <td colspan="3">LED (+) 腳位</td>
	        <td>3.3V</td>
	        <td>-</td>
	    </tr>
	        <tr>
	        <td colspan="3">LED (-) 腳位</td>
	        <td>A5</td>
	        <td>A5</td>
	    </tr>
	</table>
</div>
</br></br>

### 3.1.3 執行方式
1. 開啟 "AnalogInOutSerial.ino" 檔案。  
    1. 開啟 Arduino IDE。
    2. 點選 **File -> Examples -> 02.VCP-G Analog -> AnalogInOutSerial**。
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
 
    **註：** 若發生 "Serial" 未宣告的錯誤，請確認已正確納入下列程式庫與物件宣告。
    ```
    #include <HardwareSerial.h>
    HardwareSerial Serial;
    ```
2. 驗證並將 "AnalogInOutSerial.ino" 檔案上傳至 VCP-G。
3. 若上傳程序卡在無限上傳狀態，是因為 FWDN 模式未啟動。請依下列步驟解決：  
    1. 從 VCP-G 開發板拔除電源線。
    2. 按住 FWDN 開關不放。
    3. 持續按住 FWDN 開關的同時，重新接上電源線。
    4. 放開 FWDN 開關。
        若問題仍未解決，請嘗試以系統管理員權限執行 Arduino IDE。
4. 檔案成功上傳後，請在 Arduino IDE 輸出主控台中確認以下訊息：  
 
    **註：** 訊息中應包含 **AnalogInOutSerial.ino.rom**。
    ```
    [FWDN_VCP::WriteFile:577] Complete to send file - C:\Users\topst\AppData\Local\arduino\sketches\EB016432EF98DEF0B9102FD77148DD5D/AnalogInOutSerial.ino.rom

    [main:155] Complete FWDN
    ```

</br></br></br>

## 3.2 AnalogInput
---
此範例程式示範 VCP-G 開發板如何控制麵包板上的可變電阻與 LED。它會從類比輸入腳位讀取數值，並使用此數值控制 LED。若感測器數值低於 3000，LED 亮起；若感測器數值達到 3000 或更高，LED 熄滅。
</br></br>

### 3.2.1 硬體需求
- VCP-G 開發板 (x1)
- 麵包板 (x1)
- LED (x1)
- 可變電阻 (x1)
- 220Ω 電阻（x1）
- 12V 1A 電源變壓器 (x1)
- USB Type-C 轉 A 傳輸線 (x1)
- 公對公杜邦線 (x6)
</br></br>

### 3.2.2 電路
- 可變電阻
    - 可變電阻的 VCC 腳位透過 220Ω 電阻連接至 VCP-G 開發板上的 3.3V。
    - 可變電阻的中間腳位連接至 VCP-G 開發板上的類比腳位 A5。
    - 可變電阻的 GND 腳位透過 220Ω 電阻連接至 VCP-G 開發板上的 GND 腳位。
- LED
    - LED 的 (+) 腳位透過 220Ω 電阻連接至 VCP-G 開發板上的 3.3V。
    - LED 的 (-) 腳位連接至 VCP-G 開發板上的第 5 腳位。

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/AnalogInput%20Circuit%20Schematic.png"></p>
<p align="center"><strong>圖 3.2 AnalogInput 電路圖</strong></p>

#### 3.2.2.1 腳位對應
下表列出腳位對應。

<p align="center"><strong>表 3.2 AnalogInput 的腳位對應</strong></p>
<div align="center">
	<table>
	    <tr>
	        <th colspan="3">腳位名稱</th>
	        <th>VCP-G 開發板</th>
	        <th>Arduino IDE</th>
	    </tr>
	    <tr>
	        <td colspan="3">可變電阻 VCC 腳位</td>
	        <td>3.3V</td>
	        <td>-</td>
	    </tr>
	    <tr>
	        <td colspan="3">可變電阻中間腳位</td>
	        <td>A5</td>
	        <td>A5</td>
	    </tr>
	        <tr>
	        <td colspan="3">可變電阻 GND 腳位</td>
	        <td>GND</td>
	        <td>-</td>
	    </tr>
	        <tr>
	        <td colspan="3">LED (+) 腳位</td>
	        <td>3.3V</td>
	        <td>-</td>
	    </tr>
	        <tr>
	        <td colspan="3">LED (-) 腳位</td>
	        <td>5</td>
	        <td>5</td>
	    </tr>
	</table>
</div>
</br></br>

### 3.2.3 執行方式
1. 開啟 "AnalogInput.ino" 檔案。  
    1. 開啟 Arduino IDE。
    2. 點選 **File -> Examples -> 02.VCP-G Analog -> AnalogInput**。
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
 
    **註 1：** 若要在序列埠監控視窗中檢視 **sensorValue**，請在原始程式碼中加入 **Serial.println()**。  
    **註 2：** 固定電阻會與可變電阻（電位器）搭配使用，以調整感測器數值。感測器數值會依電位器轉動的幅度而改變，而所需轉動電位器的幅度則取決於固定電阻的阻值。

2. 請驗證並將「AnalogInput.ino」檔案上傳至 VCP-G。
3. 若上傳程序卡在無限上傳狀態，是因為 FWDN 模式未啟動。請依下列步驟解決：  
    1. 從 VCP-G 開發板拔除電源線。
    2. 按住 FWDN 開關不放。
    3. 持續按住 FWDN 開關的同時，重新接上電源線。
    4. 請放開 FWDN 開關。  
        若問題仍未解決，請嘗試以系統管理員權限執行 Arduino IDE。
4. 檔案成功上傳後，請在 Arduino IDE 輸出主控台中確認以下訊息：  

   **註：** 訊息中應包含 **AnalogInput.ino.rom**。
    ```
    [FWDN_VCP::WriteFile:577] Complete to send file - C:\Users\topst\AppData\Local\arduino\sketches\C3FDEE51354320EA689DFEB4EDCF2ECD/AnalogInput.ino.rom

    [main:155] Complete FWDN
    ```

</br></br></br>

## 3.3 pwmFade
---
此範例程式示範 VCP-G 開發板如何使用 PWM，以迴圈方式逐漸增加與降低麵包板上 LED 的亮度。當 LED 達到最大亮度後，LED 的亮度便開始下降。此程式會持續調整 LED 的亮度，形成淡入淡出的效果。
</br></br>

### 3.3.1 硬體需求
- VCP-G 開發板 (x1)
- 麵包板 (x1)
- LED (x1)
- 220Ω 電阻（x1）
- 12V 1A 電源變壓器 (x1)
- USB Type-C 轉 A 傳輸線 (x1)
- 公對公跳線（x2）
</br></br>

### 3.3.2 電路
- LED
    - LED 的 (+) 腳位連接至 VCP-G 開發板上的 5V。
    - LED 的 (-) 腳位透過 220Ω 電阻連接至 VCP-G 開發板上的 9 號腳位。

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/pwmFade%20Circuit%20Schematic.png"></p>
<p align="center"><strong>圖 3.3 pwmFade 電路圖</strong></p>

#### 3.3.2.1 腳位對應
下表列出腳位對應。

<p align="center"><strong>表 3.3 pwmFade 的腳位對應</strong></p>
<div align="center">
	<table>
	    <tr>
	        <th colspan="3">腳位名稱</th>
	        <th>VCP-G 開發板</th>
	        <th>Arduino IDE</th>
	    </tr>
	    <tr>
	        <td colspan="3">LED (+) 腳位</td>
	        <td>5V</td>
	        <td>-</td>
	    </tr>
	        <tr>
	        <td colspan="3">LED (-) 腳位</td>
	        <td>9</td>
	        <td>9</td>
	    </tr>
	</table>
</div>
</br></br>

### 3.3.3 執行方式
1. 請開啟「pwmFade.ino」檔案。
    1. 開啟 Arduino IDE。
    2. 請點選 **File -> Examples -> 02.VCP-G Analog -> pwmFade**。
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
2. 請驗證並將「pwmFade.ino」檔案上傳至 VCP-G 開發板。
3. 若上傳程序卡在無限上傳狀態，是因為 FWDN 模式未啟動。請依下列步驟解決：  
    1. 從 VCP-G 開發板拔除電源線。
    2. 按住 FWDN 開關不放。
    3. 持續按住 FWDN 開關的同時，重新接上電源線。
    4. 放開 FWDN 開關。
        若問題仍未解決，請嘗試以系統管理員權限執行 Arduino IDE。
4. 檔案成功上傳後，請在 Arduino IDE 輸出主控台中確認以下訊息：  

     **註：** 訊息中應包含 **pwmFade.ino.rom**。
    ```
    [FWDN_VCP::WriteFile:577] Complete to send file - C:\Users\topst\AppData\Local\arduino\sketches\69446E8A7F6616A7D5466014BDF759FC/pwmFade.ino.rom 

    [main:155] Complete FWDN
    ```

</br></br></br></br>

# 4. VCP SPI
---
本章說明如何在 VCP-G 上設定序列周邊介面（SPI）通訊。  
SPI 是一種高速的同步通訊協定，用於微控制器與周邊裝置之間的資料交換。它以獨立線路分別進行資料傳輸（MOSI 與 MISO）、時脈同步（SCK）與裝置選擇（SS），確保通訊高效且可靠。  
以下章節說明如何設定並使用 SPI 與外部裝置介接。

</br></br></br>

## 4.1 vcpSPI_Dot8x8
---
此範例程式示範 VCP-G 開發板如何使用 MAX7219 驅動 IC 控制 8x8 LED 點矩陣。8x8 LED 點矩陣會透過以預先定義的二進位陣列設定各列，顯示愛心圖形與字母「R」等圖案。LED 的亮度會經過調整以產生脈動效果，增添動態視覺變化。其他功能還包括反轉與清除顯示內容，以強化功能性。
</br></br>

### 4.1.1 硬體需求
- VCP-G 開發板 (x1)
- 8x8 點矩陣（x1）
- 12V 1A 電源變壓器 (x1)
- USB Type-C 轉 A 傳輸線 (x1)
- 公對母杜邦線（x5）
</br></br>

### 4.1.2 電路
- 8x8 點矩陣
    - 8x8 點矩陣的 VCC 腳位連接至 VCP-G 開發板上的類比腳位 5V。
    - 8x8 點矩陣的 GND 腳位連接至 VCP-G 開發板上的 GND。
    - 8x8 點矩陣的 DIN 腳位連接至 VCP-G 開發板上的 11 號腳位。
    - 8x8 點矩陣的 CS 腳位連接至 VCP-G 開發板上的 10 號腳位。
    - 8x8 點矩陣的 CLS 腳位連接至 VCP-G 開發板上的 13 號腳位。

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/vcpSPI_Dot8x8%20Circuit%20Schematic.png"></p>
<p align="center"><strong>圖 4.1 vcpSPI_Dot8x8 電路圖</strong></p>

#### 4.1.2.1 腳位對應
下表列出腳位對應。

<p align="center"><strong>表 4.1 vcpSPI_Dot8x8 的腳位對應</strong></p>
<div align="center">
	<table>
	    <tr>
	        <th colspan="3">腳位名稱</th>
	        <th>VCP-G 開發板</th>
	        <th>Arduino IDE</th>
	    </tr>
	    <tr>
	        <td colspan="3">8x8 點矩陣 VCC 腳位</td>
	        <td>5V</td>
	        <td>-</td>
	    </tr>
	        <tr>
	        <td colspan="3">8x8 點矩陣 GND 腳位</td>
	        <td>GND</td>
	        <td>-</td>
	    </tr>
	    <tr>
	        <td colspan="3">8x8 點矩陣 DIN 腳位</td>
	        <td>11</td>
	        <td>11</td>
	    </tr>
	    <tr>
	        <td colspan="3">8x8 點矩陣 CS 腳位</td>
	        <td>10</td>
	        <td>10</td>
	    </tr>
	    <tr>
	        <td colspan="3">8x8 點矩陣 CLK 腳位</td>
	        <td>13</td>
	        <td>13</td>
	    </tr>
	</table>
</div>
</br></br>

### 4.1.3 執行方式
1. 請開啟「vcpSPI_Dot8x8.ino」檔案。  
    1. 開啟 Arduino IDE。
    2. 請點選 **File -> Examples -> 03.VCP-G SPI -> vcpSPI_Dot8x8**。
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
2. 請驗證並將「vcpSPI_Dot8x8.ino」檔案上傳至 VCP-G。
3. 若上傳程序卡在無限上傳狀態，是因為 FWDN 模式未啟動。請依下列步驟解決：  
    1. 從 VCP-G 開發板拔除電源線。
    2. 按住 FWDN 開關不放。
    3. 持續按住 FWDN 開關的同時，重新接上電源線。
    4. 放開 FWDN 開關。
        若問題仍未解決，請嘗試以系統管理員權限執行 Arduino IDE。
4. 檔案成功上傳後，請在 Arduino IDE 輸出主控台中確認以下訊息：  

    **註：** 訊息中應包含 **vcpSPI_Dot8x8.ino.rom**。
    ```
    [FWDN_VCP::WriteFile:577] Complete to send file - C:\Users\topst\AppData\Local\arduino\sketches\567805554B5B9F915DCC80B38483AE07/vcpSPI_Dot8x8.ino.rom

    [main:155] Complete FWDN
    ```

**註：** 若要使用 VCP-G 開發板中央的 SPI 腳位，可參考以下腳位編號使用。
<p align="center"><strong>表 4.2 VCP-G 上中央 SPI 腳位的對應</strong></p>
<div align="center">
	<table>
	    <tr>
	        <th colspan="3">腳位編號</th>
	        <th>SPI 功能</th>
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
本章說明如何在 VCP-G 上設定積體電路匯流排（I2C）通訊。  
I2C 是一種雙線式同步通訊協定，專為多個裝置之間的高效資料交換而設計。它使用一條序列資料線（SDA）與一條序列時脈線（SCL），讓多個周邊裝置能以各自專屬的位址與微控制器通訊。I2C 同時支援主從式通訊與多主控組態，因此非常適合連接感測器、顯示器及其他低速裝置，同時將所需的接線數量降至最低。

</br></br></br>

## 5.1 vcpI2C_LCD1602
---
此範例程式示範 VCP-G 開發板如何使用 I2C 通訊協定控制 LCD1602 顯示器。LCD1602 是一款 16 字元、2 行的液晶顯示器，常用於嵌入式系統專案。開發板透過 LiquidCrystal_I2C 函式庫，經由 I2C 匯流排傳送命令與資料，以有效率地控制顯示器。

在此範例中，LCD 會先完成初始化並啟用背光以確保清晰可見。程式接著會移動游標，在第一行顯示文字「VCP-G」，並在第二行顯示「I2C Test!」。透過 I2C 通訊，只需極少的接線即可控制多個裝置，是小型專案的有效解決方案。
</br></br>

### 5.1.1 硬體需求
- VCP-G 開發板 (x1)
- LCD1602（x1）
- 12V 1A 電源變壓器 (x1)
- USB Type-C 轉 A 傳輸線 (x1)
- 公對母跳線（x4）
</br></br>

### 5.1.2 電路
- LCD1602
    - LCD1602 的 VCC 腳位連接至 VCP-G 開發板上的類比腳位 5V。
    - LCD1602 的 GND 腳位連接至 VCP-G 開發板上的 GND。
    - LCD1602 的 SDA 腳位連接至 VCP-G 開發板上的 48 號腳位。
    - LCD1602 的 SCL 腳位連接至 VCP-G 開發板上的 49 號腳位。

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/vcpI2C_LCD1602%20Circuit%20Schematic.png"></p>
<p align="center"><strong>圖 5.1 vcpI2C_LCD1602 電路圖</strong></p>

#### 5.1.2.1 腳位對應
下表列出腳位對應。

<p align="center"><strong>表 5.1 vcpI2C_LCD1602 的腳位對應</strong></p>
<div align="center">
	<table>
	    <tr>
	        <th colspan="3">腳位名稱</th>
	        <th>VCP-G 開發板</th>
	        <th>Arduino IDE</th>
	    </tr>
	    <tr>
	        <td colspan="3">LCD1602 VCC 腳位</td>
	        <td>5V</td>
	        <td>-</td>
	    </tr>
	        <tr>
	        <td colspan="3">LCD1602 GND 腳位</td>
	        <td>GND</td>
	        <td>-</td>
	    </tr>
	    <tr>
	        <td colspan="3">LCD1602 SDA 腳位</td>
	        <td>48</td>
	        <td>-</td>
	    </tr>
	    <tr>
	        <td colspan="3">LCD1602 SCL 腳位</td>
	        <td>49</td>
		    <td>-</td>
	    </tr>
	</table>
</div>

</br></br>

### 5.1.3 執行方式
1. 請開啟「vcpI2C_LCD1602.ino」檔案。  
    1. 請開啟 Arduino IDE  
    2. 請點選 **File -> Examples -> 04.VCP-G I2C -> vcpI2C_LCD1602**。
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
2. 請驗證並將「vcpI2C_LCD1602.ino」檔案上傳至 VCP-G。
3. 若上傳程序卡在無限上傳狀態，是因為 FWDN 模式未啟動。請依下列步驟解決：  
    1. 從 VCP-G 開發板拔除電源線。
    2. 按住 FWDN 開關不放。
    3. 持續按住 FWDN 開關的同時，重新接上電源線。
    4. 放開 FWDN 開關。
        若問題仍未解決，請嘗試以系統管理員權限執行 Arduino IDE。
4. 檔案成功上傳後，請於 Arduino IDE 輸出主控台中確認以下訊息：
   
    **註：** 訊息中應包含 **vcpI2C_LCD1602.ino.rom**。
    ```
    [FWDN_VCP::WriteFile:577] Complete to send file -         C:\Users\topst\AppData\Local\arduino\sketches\C8D91A6857B651D6C665B0EF18B7EE53/vcpI2C_LCD1602.ino.rom

    [main:155] Complete FWDN
    ```

</br></br></br></br>

# 6. VCP-G UART
---
本章說明如何在 VCP-G 上設定通用非同步收發傳輸器（UART）通訊。  
UART 是一種廣泛使用的序列通訊協定，僅使用傳送（TX）與接收（RX）兩條線路即可非同步傳輸資料。它是微控制器、感測器與電腦之間交換資料的重要方式，且不需要共用的時脈訊號。  
以下章節說明如何透過 UART 傳送與接收資料。

</br></br></br>

## 6.1 vcpASCIITable
---
此範例程式示範 VCP-G 如何以十進位、十六進位、八進位與二進位等多種格式列印字元的 ASCII 值。程式從字元 '!'（ASCII 值 33）開始，逐一遞增至所有可見的 ASCII 字元，並以不同格式列印每個字元。程式會持續執行，直到字元 '~'（ASCII 值 126）為止。
</br></br>

### 6.1.1 硬體需求
- VCP-G 開發板 (x1)
- 12V 1A 電源變壓器 (x1)
- USB Type-C 轉 A 傳輸線 (x1)
</br></br>

### 6.1.3 執行方式
1. 請開啟「vcpASCIITable.ino」檔案。
    1. 開啟 Arduino IDE。
    2. 請點選 **File -> Examples -> 05.VCP-G UART -> vcpASCIITable**。
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
2. 請驗證並將「vcpASCIITable.ino」檔案上傳至 VCP-G。
3. 若上傳程序卡在無限上傳狀態，是因為 FWDN 模式未啟動。請依下列步驟解決：  
    1. 從 VCP-G 開發板拔除電源線。
    2. 按住 FWDN 開關不放。
    3. 持續按住 FWDN 開關的同時，重新接上電源線。
    4. 放開 FWDN 開關。
        若問題仍未解決，請嘗試以系統管理員權限執行 Arduino IDE。
4. 檔案成功上傳後，請在 Arduino IDE 輸出主控台中確認以下訊息：  

    **註：** 訊息中應包含 **vcpASCIITable.ino.rom**。
    ```
    [FWDN_VCP::WriteFile:577] Complete to send file - C:\Users\topstAppData\Local\arduino\sketches\487F45098412336AA9D73C50C17E07D8/vcpASCIITable.ino.rom

    [main:155] Complete FWDN
    ```

</br></br></br>

## 6.2 vcpGraph
---
此範例程式示範 VCP-G 如何讀取麵包板上電位器的類比數值，並透過 UART 將資料傳輸至主機 PC。Arduino 程式碼會持續讀取連接至 A5 腳位的類比感測器（電位器）數值，並透過序列埠傳送。搭配的 processing 程式碼會即時將這些數值以動態圖表呈現，顯示感測器輸入隨時間的變化。
</br></br>

### 6.2.1 硬體需求
- VCP-G 開發板 (x1)
- 麵包板 (x1)
- 可變電阻 (x1)
- 10 kΩ 電阻（x1）
- 12V 1A 電源變壓器 (x1)
- USB Type-C 轉 A 傳輸線 (x1)
- 公對公杜邦線 (x4)
</br></br>

### 6.2.2 電路
- 可變電阻
    - 可變電阻的中間腳位連接至 VCP-G 開發板上的類比腳位 A5。
    - 電位器的 GND 腳位透過 10 kΩ 電阻連接至 VCP-G 開發板上的 GND。
    - 電位器的 VCC 腳位連接至 VCP-G 開發板上的 3.3V。

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/vcpGraph%20Circuit%20Schematic.png"></p>
<p align="center"><strong>圖 6.1 vcpGraph 電路圖</strong></p>

#### 6.2.2.1 腳位對應
下表列出腳位對應。

<p align="center"><strong>表 6.1 vcpGraph 的腳位對應</strong></p>
<div align="center">
	<table>
	    <tr>
	        <th colspan="3">腳位名稱</th>
	        <th>VCP-G 開發板</th>
	        <th>Arduino IDE</th>
	    </tr>
	    <tr>
	        <td colspan="3">可變電阻中間腳位</td>
	        <td>A5</td>
	        <td>A5</td>
	    </tr>
	        <tr>
	        <td colspan="3">可變電阻 GND 腳位</td>
	        <td>GND</td>
	        <td>-</td>
	    </tr>
	    <tr>
	        <td colspan="3">可變電阻 VCC 腳位</td>
	        <td>3.3V</td>
	        <td>-</td>
	    </tr>
	</table>
</div>
</br></br>

### 6.2.3 執行方式
1. 請開啟「vcpGraph.ino」檔案。
    1. 開啟 Arduino IDE。
    2. 請點選 **File -> Examples -> 05.VCP-G UART -> vcpGraph**。
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
2. 請驗證並將「vcpGraph.ino」檔案上傳至 VCP-G。
3. 若上傳程序卡在無限上傳狀態，是因為 FWDN 模式未啟動。請依下列步驟解決：  
    1. 請將電源線從 VCP-G 開發板上拔除。
    2. 按住 FWDN 開關不放。
    3. 持續按住 FWDN 開關的同時，重新接上電源線。
    4. 放開 FWDN 開關。
        若問題仍未解決，請嘗試以系統管理員權限執行 Arduino IDE。
4. 檔案成功上傳後，請於 Arduino IDE 輸出主控台中確認以下訊息：

    **註：** 訊息中應包含 **vcpGraph.ino.rom**。
    ```
    [FWDN_VCP::WriteFile:577] Complete to send file - C:\Users\topst\AppData\Local\arduino\sketches\F59E4532EC3A529F5910F376F809A5E5/vcpGraph.ino.rom

    [main:155] Complete FWDN
    ```

</br></br></br></br>

# 7. 其他範例
---
本章提供 Arduino IDE 中「Examples for TOPST VCP Rev G」未包含的其他感測器範例。  
本章提供在 VCP-G 開發板上使用常見 Arduino 感測器的範例指南，協助您有效地將各種感測器整合至專案中。

</br></br></br>

## 7.1 紅外線（IR）感測器（收發器）
---
### 7.1.1 紅外線（IR）感測器 1
---
此範例示範 VCP-G 開發板如何控制麵包板上的 IR 感測器與兩顆 LED。讀取 IR 感測器數值後，若 IR 感測器數值為 HIGH，即視為沒有障礙物，此時綠色 LED 亮起，紅色 LED 熄滅。反之，若 IR 感測器數值為 LOW，即視為有障礙物，此時紅色 LED 亮起，綠色 LED 熄滅。此外，是否偵測到障礙物也會顯示於序列監控視窗中。

#### 7.1.1.1 硬體需求
- VCP-G 開發板 (x1)
- 麵包板 (x1)
- IR 收發器感測器（x1）
- LED（x2：建議使用不同顏色）
- 220Ω 電阻（x2）
- 12V 1A 電源變壓器 (x1)
- USB Type-C 轉 A 傳輸線 (x1)
- 公對公杜邦線 (x4)
- 公對母跳線（x3）

#### 7.1.1.2 電路
- IR 收發器感測器
    - IR 感測器的 OUT 腳位連接至 VCP-G 開發板上的 50 號腳位。
    - IR 感測器的 VCC 腳位連接至 VCP-G 開發板上的 5V。
    - IR 感測器的 GND 腳位連接至 VCP-G 開發板上的 GND。
- 紅色 LED
    - LED 的 (-) 連接至電阻，電阻再連接至 VCP-G 開發板上的 GND。
    - LED 的 (+) 連接至 VCP-G 開發板上的 48 號腳位。
- 綠色 LED
    - LED 的 (-) 連接至電阻，電阻再連接至 VCP-G 開發板上的 GND。
    - LED 的 (+) 連接至 VCP-G 開發板上的 17 號腳位。

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/Infrared%20(IR)%20Sensor%20Circuit%20Schematic.png"></p>
<p align="center"><strong>圖 7.1 紅外線（IR）感測器電路圖</strong></p>

##### 7.1.1.2.1 腳位對應
下表列出腳位對應。

<p align="center"><strong>表 7.1 irSensor_LED 的腳位對應</strong></p>
<div align="center">
	<table>
	    <tr>
	        <th colspan="3">腳位名稱</th>
	        <th>VCP-G 開發板</th>
	        <th>Arduino IDE</th>
	    </tr>
	    <tr>
	        <td colspan="3">IR 感測器 OUT 腳位 </td>
	        <td>50</td>
	        <td>50</td>
	    </tr>
	        <tr>
	        <td colspan="3">IR 感測器 VCC 腳位 </td>
	        <td>5V</td>
	        <td>-</td>
	    </tr>
	    <tr>
	        <td colspan="3">IR 感測器 GND 腳位</td>
	        <td>GND</td>
	        <td>-</td>
	    </tr>
	    <tr>
	        <td colspan="3">紅色 LED (+) 腳位</td>
	        <td>48</td>
	        <td>48</td>
	    </tr>
	    <tr>
	        <td colspan="3">紅色 LED (-) 腳位</td>
	        <td>GND</td>
	        <td>-</td>
	    </tr>
	    <tr>
	        <td colspan="3">綠色 LED (+) 腳位</td>
	        <td>17</td>
	        <td>17</td>
	    </tr>
	    <tr>
	        <td colspan="3">綠色 LED (-) 腳位 </td>
	        <td>GND</td>
	        <td>-</td>
	    </tr>
	</table>
</div>

#### 7.1.1.3 執行方式
1. 請將以下原始程式碼複製到 Arduino IDE，並將檔案儲存為「irSensor_LED.ino」。
    
   **註：** 以下原始程式碼僅於本文件中提供。 

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
2. 請驗證並將「irSensor_LED.ino」檔案上傳至 VCP-G。
3. 若上傳程序卡在無限上傳狀態，是因為 FWDN 模式未啟動。請依下列步驟解決：  
    1. 從 VCP-G 開發板拔除電源線。
    2. 按住 FWDN 開關不放。
    3. 持續按住 FWDN 開關的同時，重新接上電源線。
    4. 放開 FWDN 開關。
        若問題仍未解決，請嘗試以系統管理員權限執行 Arduino IDE。
4. 檔案成功上傳後，請於 Arduino IDE 輸出主控台中確認以下訊息：
 
    **註：** 訊息中應包含 **irSensor_LED.ino.rom**。
    ```
    [FWDN_VCP::WriteFile:577] Complete to send file - C:\Users\topst\AppData\Local\arduino\sketches\1D003A72AB3391D6D60FD7993380F8CD/irSensor_LED.ino.rom 

    [main:155] Complete FWDN
    ```
</br></br>

### 7.1.2 紅外線（IR）感測器 2
---
此範例示範 VCP-G 開發板如何控制 IR 感測器以偵測物體，並將偵測狀態列印至序列監控視窗。IR 收發器會讀取是否有障礙物存在。若 IR 收發器數值為 HIGH，表示沒有障礙物，此時綠色 LED 亮起，紅色 LED 熄滅。反之，若 IR 收發器數值為 LOW，表示有障礙物，此時紅色 LED 亮起，綠色 LED 熄滅。此外，是否偵測到障礙物也會顯示於序列監控視窗中。

#### 7.1.2.1 硬體需求
- VCP-G 開發板 (x1)
- IR 收發器感測器（x1）
- 12V 1A 電源變壓器 (x1)
- USB Type-C 轉 A 傳輸線 (x1)
- 公對母跳線（x3）

#### 7.1.2.2 電路
- IR 收發器感測器
    - IR 收發器感測器的 Out 腳位連接至 VCP-G 開發板上的 8 號腳位。 
    - IR 收發器感測器的 VCC 腳位連接至 VCP-G 開發板上的 5V。
    - IR 收發器感測器的 GND 腳位連接至 VCP-G 開發板上的 GND。

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/Infrared%20(IR)%20Sensor%20(Transceiver)%20Circuit%20Schematic.png"></p>
<p align="center"><strong>圖 7.2 紅外線（IR）感測器（收發器）電路圖</strong></p>

##### 7.1.2.2.1 腳位對應
下表列出腳位對應。

<p align="center"><strong>表 7.2 irTransceiver 的腳位對應</strong></p>
<div align="center">
	<table>
	    <tr>
	        <th colspan="3">腳位名稱</th>
	        <th>VCP-G 開發板</th>
	        <th>Arduino IDE</th>
	    </tr>
	    <tr>
	        <td colspan="3">IR 收發器感測器 OUT 腳位</td>
	        <td>8</td>
	        <td>8</td>
	    </tr>
	    <tr>
	        <td colspan="3">IR 收發器感測器 VCC 腳位</td>
	        <td>5V</td>
	        <td>-</td>
	    </tr>
	    <tr>
	        <td colspan="3">IR 收發器感測器 GND 腳位</td>
	        <td>GND</td>
	        <td>-</td>
	    </tr>
	</table>
</div>

#### 7.1.2.3 執行方式
1. 請將以下原始程式碼複製到 Arduino IDE，並將檔案儲存為「irTransceiver.ino」。
   
   **註：** 以下原始程式碼僅於本文件中提供。 

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
2. 請驗證並將「irTransceiver.ino」檔案上傳至 VCP-G。
3. 若上傳程序卡在無限上傳狀態，是因為 FWDN 模式未啟動。請依下列步驟解決：  
    1. 從 VCP-G 開發板拔除電源線。
    2. 按住 FWDN 開關不放。
    3. 持續按住 FWDN 開關的同時，重新接上電源線。
    4. 放開 FWDN 開關。
        若問題仍未解決，請嘗試以系統管理員權限執行 Arduino IDE。
4. 檔案成功上傳後，請於 Arduino IDE 輸出主控台中確認以下訊息：
   
    **註：** 訊息中應包含 **irTransceiver.ino.rom**。
    ```
    [FWDN_VCP::WriteFile:577] Complete to send file - C:\Users\topst\AppData\Local\arduino\sketches\1D003A72AB3391D6D60FD7993380F8CD/irTransceiver.ino.rom 

    [main:155] Complete FWDN
    ```

</br></br></br>

## 7.2 搖桿
---
此範例示範 VCP-G 如何讀取搖桿輸入並將其數值顯示於序列監控視窗。您可以接收三種輸入：X 軸、Y 軸與按鈕。序列監控視窗可用來驗證接收到的訊號。在 X 軸與 Y 軸上的移動會改變連接埠的數值，此數值即對應類比輸出的數值。這使得需要精細調整的應用能夠達到精準控制。

**註：** 雙軸搖桿模組（KY-023）為 Joy-IT 的產品。其設計、商標及相關智慧財產權皆歸 Joy-IT 所有。
</br></br>

### 7.2.1 硬體需求
- VCP-G 開發板 (x1)
- 雙軸搖桿模組（KY-023）（x1）
- 12V 1A 電源變壓器 (x1)
- USB Type-C 轉 A 傳輸線 (x1)
- 公對母杜邦線（x5）
</br></br>

### 7.2.2 電路
- KY-023（雙軸搖桿模組）
    - KY-023 的 5V 腳位連接至 VCP-G 開發板上的 5V。
    - KY-023 的 GND 腳位連接至 VCP-G 開發板上的 GND。 
    - KY-023 的 VRx 腳位連接至 VCP-G 開發板上的類比腳位 A5。 
    - KY-023 的 VRy 腳位連接至 VCP-G 開發板上的類比腳位 A4。 
    - KY-023 的 SW 腳位連接至 VCP-G 開發板上的 2 號腳位。

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/Joystick%20Circuit%20Schematic.png"></p>
<p align="center"><strong>圖 7.3 搖桿電路圖</strong></p>

#### 7.2.2.1 腳位對應
下表列出腳位對應。

<p align="center"><strong>表 7.3 搖桿的腳位對應</strong></p>
<div align="center">
	<table>
	    <tr>
	        <th colspan="3">腳位名稱</th>
	        <th>VCP-G 開發板</th>
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

### 7.2.3 執行方式
1. 請將以下原始程式碼複製到 Arduino IDE，並將檔案儲存為「joystick.ino」。
   
   **註：** 以下原始程式碼僅於本文件中提供。 

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
2. 請驗證並將「joystick.ino」檔案上傳至 VCP-G。
3. 若上傳程序卡在無限上傳狀態，是因為 FWDN 模式未啟動。請依下列步驟解決：  
    1. 從 VCP-G 開發板拔除電源線。
    2. 按住 FWDN 開關不放。
    3. 持續按住 FWDN 開關的同時，重新接上電源線。
    4. 請放開 FWDN 開關。  
        若問題仍未解決，請嘗試以系統管理員權限執行 Arduino IDE。
4. 檔案成功上傳後，請於 Arduino IDE 輸出主控台中確認以下訊息：
   
    **註：** 訊息中應包含 **joystick.ino.rom**。
    ```
    [FWDN_VCP::WriteFile:577] Complete to send file - C:\Users\topst\AppData\Local\arduino\sketches\1D003A72AB3391D6D60FD7993380F8CD/joystick.ino.rom 

    [main:155] Complete FWDN
    ```

</br></br></br>

## 7.3 氣體感測器
---
此範例示範 VCP-G 開發板如何使用氣體感測器（MQ 135）偵測空氣中的各種有害氣體。程式會讀取連接至 VCP-G 開發板類比腳位之感測器的類比數值，將其換算為電壓，然後以小數點後一位列印至序列監控視窗。

**註：** 氣體感測器（MQ-135）為 Winsen® 的產品。其設計、商標及相關智慧財產權皆歸 Winsen 所有。
</br></br>

### 7.3.1 硬體需求
- VCP-G 開發板 (x1)
- 氣體感測器（MQ135）（x1）
- 12V 1A 電源變壓器 (x1)
- USB Type-C 轉 A 傳輸線 (x1)
- 公對母跳線（x3）
</br></br>

### 7.3.2 電路
- 氣體感測器
    - 氣體感測器的 A0 腳位連接至 VCP-G 開發板上的類比腳位 A5。 
    - 氣體感測器的 VCC 腳位連接至 VCP-G 開發板上的 5V。
    - 氣體感測器的 GND 腳位連接至 VCP-G 開發板上的 GND。


<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/Gas%20Sensor%20Circuit%20Schematic.png"></p>
<p align="center"><strong>圖 7.4 氣體感測器電路圖</strong></p>

#### 7.3.2.1 腳位對應
下表列出腳位對應。

<p align="center"><strong>表 7.4 氣體感測器的腳位對應</strong></p>
<div align="center">
	<table>
	    <tr>
	        <th colspan="3">腳位名稱</th>
	        <th>VCP-G 開發板</th>
	        <th>Arduino IDE</th>
	    </tr>
	    <tr>
	        <td colspan="3">氣體感測器 A0 腳位</td>
	        <td>A5</td>
	        <td>A5</td>
	    </tr>
	        <tr>
	        <td colspan="3">氣體感測器 VCC 腳位</td>
	        <td>5V</td>
	        <td>-</td>
	    </tr>
	    <tr>
	        <td colspan="3">氣體感測器 GND 腳位</td>
	        <td>GND</td>
	        <td>-</td>
	    </tr>
	</table>
</div>
</br></br>

### 7.3.3 執行方式
1. 請將以下原始程式碼複製到 Arduino IDE，並將檔案儲存為「GasSensor.ino」。
  
   **註：** 以下原始程式碼僅於本文件中提供。 

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
2. 請驗證並將「GasSensor.ino」檔案上傳至 VCP-G。
3. 若上傳程序卡在無限上傳狀態，是因為 FWDN 模式未啟動。請依下列步驟解決：  
    1. 請將電源線從 VCP-G 開發板上拔除。
    2. 按住 FWDN 開關不放。
    3. 持續按住 FWDN 開關的同時，重新接上電源線。
    4. 請放開 FWDN 開關。  
        若問題仍未解決，請嘗試以系統管理員權限執行 Arduino IDE。
4. 檔案成功上傳後，請於 Arduino IDE 輸出主控台中確認以下訊息：
   
    **註：** 訊息中應包含 **GasSensor.ino.rom**。
    ```
    [FWDN_VCP::WriteFile:577] Complete to send file - C:\Users\topst\AppData\Local\arduino\sketches\1D003A72AB3391D6D60FD7993380F8CD/joystick.ino.rom 

    [main:155] Complete FWDN
    ```
</br></br></br>

## 7.4 金屬觸控感測器模組
---
此範例程式示範 VCP-G 開發板如何控制麵包板上的觸控感測器與一顆 LED。金屬觸控感測器模組（KY-036）是一款用途廣泛的類比／數位感測器，用於偵測對金屬表面或人體皮膚的觸碰。此模組利用電晶體感測觸碰時導電性的變化，並同時輸出數位與類比訊號，以便與 VCP-G 互動。  
偵測到觸碰時，金屬觸控感測器模組會將相關的數位／類比數值輸出至序列監控視窗。您也可以依觸碰狀態控制 LED。 

**註：** 金屬觸控感測器模組（KY-036）內建可調整靈敏度的電位器。您可以轉動此電位器以提高或降低靈敏度。
</br></br>

### 7.4.1 硬體需求
- VCP-G 開發板 (x1)
- 麵包板 (x1)
- 金屬觸控感測器模組（KY-036）（x1）
- LED (x1)
- 220Ω 電阻（x1）
- 12V 1A 電源變壓器 (x1)
- USB Type-C 轉 A 傳輸線 (x1)
- 公對公杜邦線 (x4)
- 公對母跳線（x4）
</br></br>

### 7.4.2 電路
- 金屬觸控感測器模組
    - 金屬觸控感測器模組的 A0 腳位連接至 VCP-G 開發板上的類比腳位 A5。
    - 金屬觸控感測器模組的 G 腳位連接至 VCP-G 開發板上的 GND。
    - 金屬觸控感測器模組的 (+) 腳位連接至 VCP-G 開發板上的 5V。
    - 金屬觸控感測器模組的 D0 腳位連接至 VCP-G 開發板上的 30 號腳位。

- LED
    - LED 的 (+) 腳位連接至 VCP-G 開發板上的 13 號腳位。
    - LED 的 (-) 腳位透過 220Ω 電阻連接至 VCP-G 開發板上的 GND。


<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/Metal%20Touch%20Sensor%20Circuit%20Schematic.png"></p>
<p align="center"><strong>圖 7.5 金屬觸控感測器電路圖</strong></p>

#### 7.4.2.1 腳位對應
下表列出腳位對應。

<p align="center"><strong>表 7.5 金屬觸控感測器的腳位對應</strong></p>
<div align="center">
	<table>
	    <tr>
	        <th colspan="3">腳位名稱</th>
	        <th>VCP-G 開發板</th>
	        <th>Arduino IDE</th>
	    </tr>
	    <tr>
	        <td colspan="3">Metal Touch 感測器模組 A0 腳位</td>
	        <td>A5</td>
	        <td>A5</td>
	    </tr>
	        <tr>
	        <td colspan="3">Metal Touch 感測器模組 G 腳位</td>
	        <td>GND</td>
	        <td>-</td>
	    </tr>
	    <tr>
	        <td colspan="3">Metal Touch 感測器模組 (+) 腳位</td>
	        <td>5V</td>
		    <td>-</td>
		</tr>
	    <tr>
	        <td colspan="3">Metal Touch 感測器模組 D0 腳位</td>
	        <td>30</td>
	        <td>30</td>
	    </tr>
	    <tr>
	        <td colspan="3">LED (+) 腳位</td>
	        <td>13</td>
	        <td>13</td>
	    </tr>
	    <tr>
	        <td colspan="3">LED (+) 腳位</td>
	        <td>GND</td>
	        <td>-</td>
	    </tr>
	</table>
</div>
</br></br>

### 7.4.3 執行方式
1. 請將下列原始程式碼複製到 Arduino IDE，並將檔案儲存為「vcp_touch.ino」  

   **註：** 以下原始程式碼僅於本文件中提供。 

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
2. 請驗證並將「vcp_touch.ino」檔案上傳至 VCP-G。
3. 若上傳程序卡在無限上傳狀態，是因為 FWDN 模式未啟動。請依下列步驟解決：  
    1. 從 VCP-G 開發板拔除電源線。
    2. 按住 FWDN 開關不放。
    3. 持續按住 FWDN 開關的同時，重新接上電源線。
    4. 請放開 FWDN 開關。  
        若問題仍未解決，請嘗試以系統管理員權限執行 Arduino IDE。
4. 檔案成功上傳後，請於 Arduino IDE 輸出主控台中確認以下訊息：
   
    **註：** 訊息中應包含 **vcp_touch.ino.rom**。
    ```
    [FWDN_VCP::WriteFile:577] Complete to send file - C:\Users\topst\AppData\Local\arduino\sketches\567805554B5B9F915DCC80B38483AE07/vcp_touch.ino.rom

    [main:155] Complete FWDN
    ```

**註：** 請為序列通訊設定適當的鮑率。

</br></br></br>

## 7.5 步進馬達與馬達驅動器
---
本範例示範 VCP-G 開發板如何控制四線式步進馬達 (28BYJ-48 (5VDC)) 與馬達驅動器 (ULN2003 (5V–12V))。第 7.5.3 章的程式碼定義了連接至馬達驅動器的腳位，並設定每轉一圈所需的步數。馬達會正轉一整圈後暫停，接著反轉一整圈後再次暫停。馬達轉速由每一步之間的延遲時間控制，轉向則由線圈啟動的順序決定。

**註：** 28BYJ-48 馬達在 Half step 模式下需要 4096 個訊號才能轉一整圈，在 Full step 模式下則需要 2048 個訊號。為了精確控制馬達，應依照模式考量所需的訊號數量。 
</br></br>

### 7.5.1 硬體需求
- VCP-G 開發板 (x1)
- 步進馬達 (28BYJ-48) (x1)
- 馬達驅動器 (ULN2003) (x1)
- 12V 1A 電源變壓器 (x1)
- USB Type-C 轉 A 傳輸線 (x1)
- 公對公杜邦線 (x6)
</br></br>

### 7.5.2 電路
- 馬達驅動器
    - IN1 腳位連接至 VCP-G 開發板上的 8 號腳位。
    - IN2 腳位連接至 VCP-G 開發板上的 9 號腳位。
    - IN3 腳位連接至 VCP-G 開發板上的 10 號腳位。
    - IN4 腳位連接至 VCP-G 開發板上的 11 號腳位。
    - (+) 腳位連接至 VCP-G 開發板上的 5V。
    - (-) 腳位連接至 VCP-G 開發板上的 GND。

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/Step%20Motor%20with%20Motor%20Driver%20Circuit%20Schematic.png"></p>
<p align="center"><strong>圖 7.6 步進馬達與馬達驅動器電路圖</strong></p>

#### 7.5.2.1 腳位對應
下表列出腳位對應。

<p align="center"><strong>表 7.6 馬達驅動器腳位對應</strong></p>
<div align="center">
	<table>
	    <tr>
	        <th colspan="3">腳位名稱</th>
	        <th>VCP-G 開發板</th>
	        <th>Arduino IDE</th>
	    </tr>
	    <tr>
	        <td colspan="3">馬達驅動器 IN1 腳位</td>
	        <td>8</td>
	        <td>8</td>
	    </tr>
	        <tr>
	        <td colspan="3">馬達驅動器 IN2 腳位</td>
	        <td>9</td>
	        <td>9</td>
	    </tr>
	    <tr>
	        <td colspan="3">馬達驅動器 IN3 腳位</td>
	        <td>10</td>
	        <td>10</td>
		</tr>
	    <tr>
	        <td colspan="3">馬達驅動器 IN4 腳位</td>
		    <td>11</td>
			<td>11</td>
	    </tr>
		<tr>
			<td colspan="3">馬達驅動器 (+) 腳位</td>
	        <td>5V</td>
	        <td>-</td>
		</tr>
	    <tr>
	        <td colspan="3">馬達驅動器 (-) 腳位</td>
	        <td>GND</td>
	        <td>-</td>
	    </tr>
	</table>
</div>
</br></br>

### 7.5.3 執行方式
1. 請將下列原始程式碼複製到 Arduino IDE，並將檔案儲存為「motordriver.ino」。

    **註：** 下列原始程式碼僅在本文件中提供。 

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
2. 請驗證並將「motordriver.ino」檔案上傳至 VCP-G。
3. 若上傳程序卡在無限上傳狀態，是因為 FWDN 模式未啟動。請依下列步驟解決：  
    1. 從 VCP-G 開發板拔除電源線。
    2. 按住 FWDN 開關不放。
    3. 持續按住 FWDN 開關的同時，重新接上電源線。
    4. 請放開 FWDN 開關。  
        若問題仍未解決，請嘗試以系統管理員權限執行 Arduino IDE。
4. 檔案成功上傳後，請在 Arduino IDE 輸出主控台中確認以下訊息：  

    **註：** 訊息中應包含 **motordriver.ino.rom**。
    ```
    [FWDN_VCP::WriteFile:577] Complete to send file - C:\Users\topst\AppData\Local\arduino\sketches\567805554B5B9F915DCC80B38483AE07/motordriver.rom

    [main:155] Complete FWDN
    ```
</br></br></br></br>

# 8. 參考資料
---
- 如需更多詳細資訊，請聯絡 TOPST：topst@topst.ai

**註：**參考文件可依合約條款於可提供時提供。若參考
文件無法提供，則可就與您的開發直接相關的內容提供指引。
