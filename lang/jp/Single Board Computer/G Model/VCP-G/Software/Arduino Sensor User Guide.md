# 1. はじめに
---
本書は、VCP-G ボードでさまざまな Arduino センサーを使用するためのガイドラインを提供します。VCP-G を使用してプロジェクトを簡単に開発できるよう、接続手順とサンプルコードを含んでいます。

具体的には、本書は次の内容を含む VCP-G 向け Arduino IDE サンプルについて説明します:  
- VCP-G Digital
- VCP-G Analog
- VCP-G SPI
- VCP-G I2C
- VCP-G UART
- Additional Example

VCP-G を使用する前に、図 1.1 を参照してください。

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/vcp-g%20pinout%20Diagram.png"></p>
<p align="center"><strong>図 1.1 VCP-G ピンアウト図</strong></p>

</br></br></br></br>

# 2. VCP-G デジタルピン
---
本章では、VCP-G ボードのデジタルピンを使用して LED を制御するサンプルを提供します。VCP-G では、デジタルピンはバイナリ信号 (HIGH または LOW) の送受信に使用され、LED、スイッチ、センサーなどの部品を制御するために不可欠です。 

本章には、デジタル出力を使用して複数の LED を制御する方法を示す 2 つのサンプルプロジェクトが含まれており、デジタルピン機能の基礎的な理解を提供します。

</br></br></br>

## 2.1 vcp4LED
---
本サンプルプログラムは、VCP-G ボードがブレッドボード上の 4 個の LED を制御する方法を示します。サンプルコードは “vcp4LED.ino” ファイルで提供されます。このファイルを VCP-G にアップロードすると、各遷移の間に 500 ms の遅延を挟みながら、LED が順方向と逆方向のパターンで順次点灯および消灯します。 

</br></br>

### 2.1.1 ハードウェア要件  
- VCP-G ボード (x1)
- ブレッドボード (x1)
- LED (x4)
- 220Ω 抵抗 (x4)
- 12V 1A 電源アダプター (x1)
- USB Type-C to A ケーブル (x1) 
- オス-オス ジャンパーワイヤー (x9)
</br></br>

### 2.1.2 回路
- LED01
    - (+) ピンは 220Ω 抵抗を介してブレッドボード上の 5V 電源レールに接続されます。この電源は VCP-G ボードから供給されます。
    - (-) ピンは VCP-G ボードの 47 番ピンに接続されます。
- LED02
    - (+) ピンは 220Ω 抵抗を介してブレッドボード上の 5V 電源レールに接続されます。
    - (-) ピンは VCP-G ボードの 17 番ピンに接続されます。
- LED03
    - (+) ピンは 220Ω 抵抗を介してブレッドボード上の 5V 電源レールに接続されます。
    - (-) ピンは VCP-G ボードの 50 番ピンに接続されます。
- LED04
    - (+) ピンは 220Ω 抵抗を介してブレッドボード上の 5V 電源レールに接続されます。
    - (-) ピンは VCP-G ボードの 48 番ピンに接続されます。  

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/vcp4LED%20Circuit%20Schematic.png"></p>
<p align="center"><strong>図 2.1 vcp4LED 回路図</strong></p>

#### 2.1.2.1 ピンマッピング
次の表はピンマッピングを示しています。

<p align="center"><strong>表 2.1 vcp4LED のピンマッピング</strong></p>
<div align="center">	
	<table>
		<tr>
			<th colspan="3">ピン名</th>
	        <th>VCP-G ボード</th>
	        <th>Arduino IDE</th>
	    </tr>
	    <tr>
	        <td colspan="3">LED01 (-) ピン</td>
	        <td>47</td>
	        <td>47</td>
	    </tr>
	        <tr>
	        <td colspan="3">LED02 (-) ピン</td>
	        <td>17</td>
	        <td>17</td>
	    </tr>
	        <tr>
	        <td colspan="3">LED03 (-) ピン</td>
	        <td>50</td>
	        <td>50</td>
	    </tr>
	        <tr>
	        <td colspan="3">LED04 (-) ピン</td>
	        <td>48</td>
	        <td>48</td>
	    </tr>
	</table>
</div>
</br></br>

### 2.1.3 実行方法
1. "vcp4LED.ino" ファイルを開きます。  
    1. Arduino IDE を開きます。
    2. **File -> Examples -> 01.VCP-G Digital -> vcp4LED** をクリックします。
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
2. "vcp4LED.ino" ファイルを検証し、VCP-G にアップロードします。
3. アップロード処理が無限アップロード状態で止まる場合は、FWDN モードが有効になっていないことが原因です。これを解決するには、次の手順を実行します:  
    1. VCP-G ボードから電源ケーブルを取り外します。
    2. FWDN スイッチを押し続けます。
    3. FWDN スイッチを押し続けたまま、電源ケーブルを再接続します。
    4. FWDN スイッチを離します。
        問題が解決しない場合は、管理者権限で Arduino IDE を実行してみてください。
4. ファイルのアップロードが成功したら、Arduino IDE の出力コンソールで次のメッセージを確認します:  

     **注:** メッセージには **vcp4LED.ino.rom** が含まれている必要があります。
    ```
    [FWDN_VCP::WriteFile:577] Complete to send file - C:\Users\topst\AppData\Local\arduino\sketches\C05357299384CE5734F0E696C5A4DA3B/vcp4LED.ino.rom

    [main:155] Complete FWDN
    ```

</br></br></br>

## 2.2 vcp4LED_Button
---
本サンプルプログラムは、VCP-G ボードがブレッドボード上の 4 個の LED とボタンを制御する方法を示します。ボタンを押すと、右側の 2 個の LED が消灯し、左側の 2 個の LED が点灯します。ボタンを離すと、点灯していた LED が消灯し、消灯していた LED が点灯します。本プログラムはボタンの状態を継続的に確認し、それに応じて LED を制御します。
</br></br>

### 2.2.1 ハードウェア要件
- VCP-G ボード (x1)
- ブレッドボード (x1)
- LED (x4)
- ボタンスイッチ (センサー) (x1)
- 220Ω 抵抗 (x4)
- 12V 1A 電源アダプター (x1)
- USB Type-C to A ケーブル (x1)
- オス-オス ジャンパーワイヤー (x12)
</br></br>

### 2.2.2 回路
1.	LED01
    - (+) ピンは 220Ω 抵抗を介してブレッドボード上の 5V 電源レールに接続されます。この電源は VCP-G ボードから供給されます。
    - (-) ピンは VCP-G ボードの 47 番ピンに接続されます。
2.	LED02
    - (+) ピンは 220Ω 抵抗を介してブレッドボード上の 5V 電源レールに接続されます。
    - (-) ピンは VCP-G ボードの 17 番ピンに接続されます。
3.	LED03
    - (+) ピンは 220Ω 抵抗を介してブレッドボード上の 5V 電源レールに接続されます。
    - (-) ピンは VCP-G ボードの 50 番ピンに接続されます。
4.	LED04
    - (+) ピンは 220Ω 抵抗を介してブレッドボード上の 5V 電源レールに接続されます。
    - (-) ピンは VCP-G ボードの 48 番ピンに接続されます。
5.	ボタンスイッチ
    - ボタンスイッチの一方の脚は VCP-G ボードの 45 番ピンに接続されます。
    - ボタンの対角線上の反対側の脚は GND ピンに接続されます。

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/vcp4LED_Button%20Circuit%20Schematic.png"></p>
<p align="center"><strong>図 2.2 vcp4LED_Button 回路図</strong></p>

#### 2.2.2.1 ピンマッピング
次の表はピンマッピングを示しています。

<p align="center"><strong>表 2.2 vcp4LED_Button のピンマッピング</strong></p>
<div align="center">
	<table>
	    <tr>
	        <th colspan="3">ピン名</th>
	        <th>VCP-G ボード</th>
	        <th>Arduino IDE</th>
	    </tr>
	    <tr>
	        <td colspan="3">LED01 (-) ピン</td>
	        <td>47</td>
	        <td>47</td>
	    </tr>
	        <tr>
	        <td colspan="3">LED02 (-) ピン</td>
	        <td>17</td>
	        <td>17</td>
	    </tr>
	        <tr>
	        <td colspan="3">LED03 (-) ピン</td>
	        <td>50</td>
	        <td>50</td>
	    </tr>
	        <tr>
	        <td colspan="3">LED04 (-) ピン</td>
	        <td>48</td>
	        <td>48</td>
	    </tr>
	    </tr>
	        <tr>
	        <td colspan="3">ボタンの一方の脚のピン</td>
	        <td>45</td>
	        <td>45</td>
	    </tr>
	</table>
</div>
</br></br>

### 2.1.3 実行方法
1. "vcp4LED_Button.ino" ファイルを開きます。
    1. Arduino IDE を開きます。
    2. **File -> Examples -> 01.VCP-G Digital -> vcp4LED_Button** をクリックします。
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
2. "vcp4LED_Button.ino" ファイルを検証し、VCP-G にアップロードします。
3. アップロード処理が無限アップロード状態で止まる場合は、FWDN モードが有効になっていないことが原因です。これを解決するには、次の手順を実行します:  
    1. VCP-G ボードから電源ケーブルを取り外します。
    2. FWDN スイッチを押し続けます。
    3. FWDN スイッチを押し続けたまま、電源ケーブルを再接続します。
    4. FWDN スイッチを離します。 
        問題が解決しない場合は、管理者権限で Arduino IDE を実行してみてください。
4. ファイルのアップロードが成功したら、Arduino IDE の出力コンソールで次のメッセージを確認します:  

    **注:** メッセージには **vcp4LED_Button.ino.rom** が含まれている必要があります。
    ```
    [FWDN_VCP::WriteFile:577] Complete to send file - C:\Users\topst\AppData\Local\arduino\sketches\5CC1DB4CA216E2BC009504FAA3D06456/vcp4LED_Button.ino.rom

    [main:155] Complete FWDN
    ```

</br></br></br></br>

# 3. VCP-G アナログピン
---
本章では、VCP-G ボードのアナログピンを使用するサンプルを提供します。VCP-G では、アナログピンはセンサーから連続的な電圧信号を受信し、変化する入力値を高精度に測定できます。第 3.1 章、第 3.2 章、第 3.3 章では、アナログピンを使用してセンサーデータを読み取り、出力を制御する方法を説明し、アナログ入力処理の基礎的な理解を提供します。

</br></br></br>

## 3.1 AnalogInOutSerial
---
本サンプルプログラムは、VCP-G ボードがブレッドボード上のポテンショメータと LED を制御する方法を示します。VCP-G はアナログ入力ピンから値を読み取り、その結果を 0 から 1000 の範囲にマッピングし、この値を使用して出力ピン (LED に接続) のパルス幅変調 (PWM) を設定します。結果は Serial Monitor にも出力されます。
</br></br>

### 3.1.1 ハードウェア要件
- VCP-G ボード (x1)
- ブレッドボード (x1)
- LED (x1)
- ポテンショメータ (x1)
- 220Ω 抵抗 (x2)
- 12V 1A 電源アダプター (x1)
- USB Type-C to A ケーブル (x1)
- オス-オス ジャンパーワイヤー (x4)
</br></br>

### 3.1.2 回路
- ポテンショメータ
    - ポテンショメータの中央ピンは VCP-G ボードのアナログピン A5 に接続されます。
    - ポテンショメータの GND ピンは VCP-G ボードの 43 番ピンに接続され、220Ω 抵抗を介して VCP-G ボードの GND ピンに接続されます。
- LED
    - LED の (+) ピンは 220Ω 抵抗を介して VCP-G ボードの 3.3V に接続されます。
    - LED の (-) ピンはポテンショメータの中央ピンに接続されます。

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/AnalogInOutSerial%20Circuit%20Schematic.png"></p>
<p align="center"><strong>図 3.1 AnalogInOutSerial 回路図</strong></p>

#### 3.1.2.1 ピンマッピング
次の表はピンマッピングを示しています。

<p align="center"><strong>表 3.1 AnalogInOutSerial のピンマッピング</strong></p>
<div align="center">
	<table>
	    <tr>
	        <th colspan="3">ピン名</th>
	        <th>VCP-G ボード</th>
	        <th>Arduino IDE</th>
	    </tr>
	    <tr>
	        <td colspan="3">ポテンショメータの中央ピン</td>
	        <td>A5</td>
	        <td>-</td>
	    </tr>
	        <tr>
	        <td colspan="3">ポテンショメータの GND ピン</td>
	        <td>43</td>
	        <td>43</td>
	    </tr>
	        <tr>
	        <td colspan="3">LED (+) ピン</td>
	        <td>3.3V</td>
	        <td>-</td>
	    </tr>
	        <tr>
	        <td colspan="3">LED (-) ピン</td>
	        <td>A5</td>
	        <td>A5</td>
	    </tr>
	</table>
</div>
</br></br>

### 3.1.3 実行方法
1. "AnalogInOutSerial.ino" ファイルを開きます。  
    1. Arduino IDE を開きます。
    2. **File -> Examples -> 02.VCP-G Analog -> AnalogInOutSerial** をクリックします。
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
 
    **注:** "Serial" が宣言されていないというエラーが発生する場合は、次のライブラリとオブジェクト宣言が正しく含まれていることを確認してください。
    ```
    #include <HardwareSerial.h>
    HardwareSerial Serial;
    ```
2. "AnalogInOutSerial.ino" ファイルを検証し、VCP-G にアップロードします。
3. アップロード処理が無限アップロード状態で止まる場合は、FWDN モードが有効になっていないことが原因です。これを解決するには、次の手順を実行します:  
    1. VCP-G ボードから電源ケーブルを取り外します。
    2. FWDN スイッチを押し続けます。
    3. FWDN スイッチを押し続けたまま、電源ケーブルを再接続します。
    4. FWDN スイッチを離します。
        問題が解決しない場合は、管理者権限で Arduino IDE を実行してみてください。
4. ファイルのアップロードが成功したら、Arduino IDE の出力コンソールで次のメッセージを確認します:  
 
    **注記:** メッセージには **AnalogInOutSerial.ino.rom** が含まれている必要があります。
    ```
    [FWDN_VCP::WriteFile:577] Complete to send file - C:\Users\topst\AppData\Local\arduino\sketches\EB016432EF98DEF0B9102FD77148DD5D/AnalogInOutSerial.ino.rom

    [main:155] Complete FWDN
    ```

</br></br></br>

## 3.2 AnalogInput
---
このサンプルプログラムは、VCP-G ボードがブレッドボード上のポテンショメータと LED を制御する方法を示します。アナログ入力ピンから値を読み取り、この値を使用して LED を制御します。センサー値が 3000 より小さい場合、LED が点灯します。センサー値が 3000 以上の場合、LED は消灯します。
</br></br>

### 3.2.1 ハードウェア要件
- VCP-G ボード (x1)
- ブレッドボード (x1)
- LED (x1)
- ポテンショメータ (x1)
- 220Ω 抵抗 (x1)
- 12V 1A 電源アダプター (x1)
- USB Type-C to A ケーブル (x1)
- オス-オス ジャンパーワイヤ (x6)
</br></br>

### 3.2.2 回路
- ポテンショメータ
    - ポテンショメータの VCC ピンは、220Ω 抵抗を介して VCP-G ボードの 3.3V に接続されます。
    - ポテンショメータの中央ピンは VCP-G ボードのアナログピン A5 に接続されます。
    - ポテンショメータの GND ピンは、220Ω 抵抗を介して VCP-G ボードの GND ピンに接続されます。
- LED
    - LED の (+) ピンは 220Ω 抵抗を介して VCP-G ボードの 3.3V に接続されます。
    - LED の (-) ピンは、VCP-G ボードの 5 番ピンに接続されます。

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/AnalogInput%20Circuit%20Schematic.png"></p>
<p align="center"><strong>図 3.2 AnalogInput 回路図</strong></p>

#### 3.2.2.1 ピンマップ
次の表はピンマッピングを示しています。

<p align="center"><strong>表 3.2 AnalogInput のピンマップ</strong></p>
<div align="center">
	<table>
	    <tr>
	        <th colspan="3">ピン名</th>
	        <th>VCP-G ボード</th>
	        <th>Arduino IDE</th>
	    </tr>
	    <tr>
	        <td colspan="3">ポテンショメータ VCC ピン</td>
	        <td>3.3V</td>
	        <td>-</td>
	    </tr>
	    <tr>
	        <td colspan="3">ポテンショメータの中央ピン</td>
	        <td>A5</td>
	        <td>A5</td>
	    </tr>
	        <tr>
	        <td colspan="3">ポテンショメータの GND ピン</td>
	        <td>GND</td>
	        <td>-</td>
	    </tr>
	        <tr>
	        <td colspan="3">LED (+) ピン</td>
	        <td>3.3V</td>
	        <td>-</td>
	    </tr>
	        <tr>
	        <td colspan="3">LED (-) ピン</td>
	        <td>5</td>
	        <td>5</td>
	    </tr>
	</table>
</div>
</br></br>

### 3.2.3 実行方法
1. 「AnalogInput.ino」ファイルを開きます。  
    1. Arduino IDE を開きます。
    2. **File -> Examples -> 02.VCP-G Analog -> AnalogInput** をクリックします。
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
 
    **注記 1:** Serial Monitor で **sensorValue** を確認するには、ソースコードに **Serial.println()** を追加してください。  
    **注記 2:** センサー値を調整するために、可変抵抗（ポテンショメータ）とともに固定抵抗が使用されます。センサー値はポテンショメータをどれだけ回すかによって変化し、回す必要のある量は固定抵抗の値によって異なります。

2. 「AnalogInput.ino」ファイルを検証し、VCP-G にアップロードします。
3. アップロード処理が無限アップロード状態で止まる場合は、FWDN モードが有効になっていないことが原因です。これを解決するには、次の手順を実行します:  
    1. VCP-G ボードから電源ケーブルを取り外します。
    2. FWDN スイッチを押し続けます。
    3. FWDN スイッチを押し続けたまま、電源ケーブルを再接続します。
    4. FWDN スイッチを離します。  
        問題が解決しない場合は、管理者権限で Arduino IDE を実行してみてください。
4. ファイルのアップロードが成功したら、Arduino IDE の出力コンソールで次のメッセージを確認します:  

   **注記:** メッセージには **AnalogInput.ino.rom** が含まれている必要があります。
    ```
    [FWDN_VCP::WriteFile:577] Complete to send file - C:\Users\topst\AppData\Local\arduino\sketches\C3FDEE51354320EA689DFEB4EDCF2ECD/AnalogInput.ino.rom

    [main:155] Complete FWDN
    ```

</br></br></br>

## 3.3 pwmFade
---
このサンプルプログラムは、VCP-G ボードが PWM を使用してブレッドボード上の LED の明るさをループ内で徐々に上げ下げしながら制御する方法を示します。LED が最大の明るさに達すると、LED の明るさは減少し始めます。プログラムは LED の明るさを継続的に調整し、フェード効果を作り出します。
</br></br>

### 3.3.1 ハードウェア要件
- VCP-G ボード (x1)
- ブレッドボード (x1)
- LED (x1)
- 220Ω 抵抗 (x1)
- 12V 1A 電源アダプター (x1)
- USB Type-C to A ケーブル (x1)
- オス-オス ジャンパーワイヤ (x2)
</br></br>

### 3.3.2 回路
- LED
    - LED の (+) ピンは、VCP-G ボードの 5V に接続されます。
    - LED の (-) ピンは、220Ω 抵抗を介して VCP-G ボードの 9 番ピンに接続されます。

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/pwmFade%20Circuit%20Schematic.png"></p>
<p align="center"><strong>図 3.3 pwmFade 回路図</strong></p>

#### 3.3.2.1 ピンマップ
次の表はピンマッピングを示しています。

<p align="center"><strong>表 3.3 pwmFade のピンマップ</strong></p>
<div align="center">
	<table>
	    <tr>
	        <th colspan="3">ピン名</th>
	        <th>VCP-G ボード</th>
	        <th>Arduino IDE</th>
	    </tr>
	    <tr>
	        <td colspan="3">LED (+) ピン</td>
	        <td>5V</td>
	        <td>-</td>
	    </tr>
	        <tr>
	        <td colspan="3">LED (-) ピン</td>
	        <td>9</td>
	        <td>9</td>
	    </tr>
	</table>
</div>
</br></br>

### 3.3.3 実行方法
1. 「pwmFade.ino」ファイルを開きます。
    1. Arduino IDE を開きます。
    2. **File -> Examples -> 02.VCP-G Analog -> pwmFade** をクリックします。
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
2. 「pwmFade.ino」ファイルを検証し、VCP-G ボードにアップロードします。
3. アップロード処理が無限アップロード状態で止まる場合は、FWDN モードが有効になっていないことが原因です。これを解決するには、次の手順を実行します:  
    1. VCP-G ボードから電源ケーブルを取り外します。
    2. FWDN スイッチを押し続けます。
    3. FWDN スイッチを押し続けたまま、電源ケーブルを再接続します。
    4. FWDN スイッチを離します。
        問題が解決しない場合は、管理者権限で Arduino IDE を実行してみてください。
4. ファイルのアップロードが成功したら、Arduino IDE の出力コンソールで次のメッセージを確認します:  

     **注記:** メッセージには **pwmFade.ino.rom** が含まれている必要があります。
    ```
    [FWDN_VCP::WriteFile:577] Complete to send file - C:\Users\topst\AppData\Local\arduino\sketches\69446E8A7F6616A7D5466014BDF759FC/pwmFade.ino.rom 

    [main:155] Complete FWDN
    ```

</br></br></br></br>

# 4. VCP SPI
---
この章では、VCP-G で Serial Peripheral Interface (SPI) 通信を設定する手順について説明します。  
SPI は、マイクロコントローラと周辺機器の間でデータを交換するために使用される高速の同期通信プロトコルです。データ送信 (MOSI および MISO)、クロック同期 (SCK)、デバイス選択 (SS) 用の独立した信号線で動作し、効率的で信頼性の高い通信を実現します。  
以降の章では、外部デバイスとインターフェースするために SPI を設定して使用する方法について説明します。

</br></br></br>

## 4.1 vcpSPI_Dot8x8
---
このサンプルプログラムは、VCP-G ボードが MAX7219 ドライバを使用して 8x8 LED ドットマトリクスを制御する方法を示します。8x8 LED ドットマトリクスは、あらかじめ定義されたバイナリ配列で行を設定することにより、ハート形や文字「R」などのパターンを表示します。LED の輝度を調整して脈動する効果を作り出し、動的な視覚効果を加えます。さらに、表示の反転やクリアといった機能により機能性を高めています。
</br></br>

### 4.1.1 ハードウェア要件
- VCP-G ボード (x1)
- 8x8 ドットマトリクス (x1)
- 12V 1A 電源アダプター (x1)
- USB Type-C to A ケーブル (x1)
- オス-メス ジャンパーワイヤ (x5)
</br></br>

### 4.1.2 回路
- 8x8 ドットマトリクス
    - 8x8 ドットマトリクスの VCC ピンは、VCP-G ボードのアナログピン 5V に接続されます。
    - 8x8 ドットマトリクスの GND ピンは、VCP-G ボードの GND に接続されます。
    - 8x8 ドットマトリクスの DIN ピンは、VCP-G ボードの 11 番ピンに接続されます。
    - 8x8 ドットマトリクスの CS ピンは、VCP-G ボードの 10 番ピンに接続されます。
    - 8x8 ドットマトリクスの CLS ピンは、VCP-G ボードの 13 番ピンに接続されます。

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/vcpSPI_Dot8x8%20Circuit%20Schematic.png"></p>
<p align="center"><strong>図 4.1 vcpSPI_Dot8x8 回路図</strong></p>

#### 4.1.2.1 ピンマップ
次の表はピンマッピングを示しています。

<p align="center"><strong>表 4.1 vcpSPI_Dot8x8 のピンマップ</strong></p>
<div align="center">
	<table>
	    <tr>
	        <th colspan="3">ピン名</th>
	        <th>VCP-G ボード</th>
	        <th>Arduino IDE</th>
	    </tr>
	    <tr>
	        <td colspan="3">8x8 ドットマトリクス VCC ピン</td>
	        <td>5V</td>
	        <td>-</td>
	    </tr>
	        <tr>
	        <td colspan="3">8x8 ドットマトリクス GND ピン</td>
	        <td>GND</td>
	        <td>-</td>
	    </tr>
	    <tr>
	        <td colspan="3">8x8 ドットマトリクス DIN ピン</td>
	        <td>11</td>
	        <td>11</td>
	    </tr>
	    <tr>
	        <td colspan="3">8x8 ドットマトリクス CS ピン</td>
	        <td>10</td>
	        <td>10</td>
	    </tr>
	    <tr>
	        <td colspan="3">8x8 ドットマトリクス CLK ピン</td>
	        <td>13</td>
	        <td>13</td>
	    </tr>
	</table>
</div>
</br></br>

### 4.1.3 実行方法
1. 「vcpSPI_Dot8x8.ino」ファイルを開きます。  
    1. Arduino IDE を開きます。
    2. **File -> Examples -> 03.VCP-G SPI -> vcpSPI_Dot8x8** をクリックします。
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
2. 「vcpSPI_Dot8x8.ino」ファイルを検証し、VCP-G にアップロードします。
3. アップロード処理が無限アップロード状態で止まる場合は、FWDN モードが有効になっていないことが原因です。これを解決するには、次の手順を実行します:  
    1. VCP-G ボードから電源ケーブルを取り外します。
    2. FWDN スイッチを押し続けます。
    3. FWDN スイッチを押し続けたまま、電源ケーブルを再接続します。
    4. FWDN スイッチを離します。
        問題が解決しない場合は、管理者権限で Arduino IDE を実行してみてください。
4. ファイルのアップロードが成功したら、Arduino IDE の出力コンソールで次のメッセージを確認します:  

    **注記:** メッセージには **vcpSPI_Dot8x8.ino.rom** が含まれている必要があります。
    ```
    [FWDN_VCP::WriteFile:577] Complete to send file - C:\Users\topst\AppData\Local\arduino\sketches\567805554B5B9F915DCC80B38483AE07/vcpSPI_Dot8x8.ino.rom

    [main:155] Complete FWDN
    ```

**注記:** VCP-G ボード中央の SPI ピンを使用する場合は、次のピン番号を参照して使用できます。
<p align="center"><strong>表 4.2 VCP-G の中央 SPI ピンのマッピング</strong></p>
<div align="center">
	<table>
	    <tr>
	        <th colspan="3">ピン番号</th>
	        <th>SPI 機能</th>
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
この章では、VCP-G で Inter-integrated Circuit (I2C) 通信を設定する手順について説明します。  
I2C は、複数のデバイス間で効率的にデータを交換するために設計された 2 線式の同期通信プロトコルです。シリアルデータライン (SDA) とシリアルクロックライン (SCL) で動作し、固有のアドレスを使用して複数の周辺機器がマイクロコントローラと通信できるようにします。I2C はマスタ・スレーブ通信とマルチマスタ構成の両方をサポートしており、必要な接続数を最小限に抑えながら、センサーやディスプレイなどの低速デバイスを接続するのに最適です。

</br></br></br>

## 5.1 vcpI2C_LCD1602
---
このサンプルプログラムは、VCP-G ボードが I2C 通信プロトコルを使用して LCD1602 ディスプレイを制御する方法を示します。LCD1602 は、組み込みシステムのプロジェクトでよく使用される 16 文字 2 行の液晶ディスプレイです。LiquidCrystal_I2C ライブラリを利用して、ボードは I2C バス経由でコマンドとデータを送信し、ディスプレイを効率的に制御します。

この例では、LCD が初期化され、見やすくするためにバックライトが有効になります。次にプログラムはカーソルを配置し、1 行目に「VCP-G」、2 行目に「I2C Test!」というテキストを表示します。I2C 通信により、最小限の配線で複数のデバイスを制御できるため、小型のプロジェクトに効果的なソリューションとなります。
</br></br>

### 5.1.1 ハードウェア要件
- VCP-G ボード (x1)
- LCD1602 (x1)
- 12V 1A 電源アダプター (x1)
- USB Type-C to A ケーブル (x1)
- オス-メス ジャンパーワイヤ (x4)
</br></br>

### 5.1.2 回路
- LCD1602
    - LCD1602 の VCC ピンは、VCP-G ボードのアナログピン 5V に接続されます。
    - LCD1602 の GND ピンは、VCP-G ボードの GND に接続されます。
    - LCD1602 の SDA ピンは、VCP-G ボードの 48 番ピンに接続されます。
    - LCD1602 の SCL ピンは、VCP-G ボードの 49 番ピンに接続されます。

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/vcpI2C_LCD1602%20Circuit%20Schematic.png"></p>
<p align="center"><strong>図 5.1 vcpI2C_LCD1602 回路図</strong></p>

#### 5.1.2.1 ピンマップ
次の表はピンマッピングを示しています。

<p align="center"><strong>表 5.1 vcpI2C_LCD1602 のピンマップ</strong></p>
<div align="center">
	<table>
	    <tr>
	        <th colspan="3">ピン名</th>
	        <th>VCP-G ボード</th>
	        <th>Arduino IDE</th>
	    </tr>
	    <tr>
	        <td colspan="3">LCD1602 VCC ピン</td>
	        <td>5V</td>
	        <td>-</td>
	    </tr>
	        <tr>
	        <td colspan="3">LCD1602 GND ピン</td>
	        <td>GND</td>
	        <td>-</td>
	    </tr>
	    <tr>
	        <td colspan="3">LCD1602 SDA ピン</td>
	        <td>48</td>
	        <td>-</td>
	    </tr>
	    <tr>
	        <td colspan="3">LCD1602 SCL ピン</td>
	        <td>49</td>
		    <td>-</td>
	    </tr>
	</table>
</div>

</br></br>

### 5.1.3 実行方法
1. 「vcpI2C_LCD1602.ino」ファイルを開きます。  
    1. Arduino IDE を開きます  
    2. **File -> Examples -> 04.VCP-G I2C -> vcpI2C_LCD1602** をクリックします。
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
2. 「vcpI2C_LCD1602.ino」ファイルを検証し、VCP-G にアップロードします。
3. アップロード処理が無限アップロード状態で止まる場合は、FWDN モードが有効になっていないことが原因です。これを解決するには、次の手順を実行します:  
    1. VCP-G ボードから電源ケーブルを取り外します。
    2. FWDN スイッチを押し続けます。
    3. FWDN スイッチを押し続けたまま、電源ケーブルを再接続します。
    4. FWDN スイッチを離します。
        問題が解決しない場合は、管理者権限で Arduino IDE を実行してみてください。
4. ファイルのアップロードが成功したら、Arduino IDE の出力コンソールで次のメッセージを確認します。
   
    **注記:** メッセージには **vcpI2C_LCD1602.ino.rom** が含まれている必要があります。
    ```
    [FWDN_VCP::WriteFile:577] Complete to send file -         C:\Users\topst\AppData\Local\arduino\sketches\C8D91A6857B651D6C665B0EF18B7EE53/vcpI2C_LCD1602.ino.rom

    [main:155] Complete FWDN
    ```

</br></br></br></br>

# 6. VCP-G UART
---
この章では、VCP-G で Universal Asynchronous Receiver-Transmitter (UART) 通信を設定する手順について説明します。  
UART は、送信 (TX) と受信 (RX) の 2 本の信号線のみを使用してデータを非同期に伝送する、広く使用されているシリアル通信プロトコルです。共有クロック信号を必要とせずに、マイクロコントローラ、センサー、コンピュータ間でデータを交換するために不可欠です。  
以降の章では、UART を介してデータを送受信する方法について説明します。

</br></br></br>

## 6.1 vcpASCIITable
---
このサンプルプログラムは、VCP-G が文字の ASCII 値を 10 進数、16 進数、8 進数、2 進数などのさまざまな形式で出力する方法を示します。文字 '!' (ASCII 値 33) から始まり、表示可能なすべての ASCII 文字を順に進めながら、それぞれを異なる形式で出力します。プログラムは文字 '~' (ASCII 値 126) に達するまで続きます。
</br></br>

### 6.1.1 ハードウェア要件
- VCP-G ボード (x1)
- 12V 1A 電源アダプター (x1)
- USB Type-C to A ケーブル (x1)
</br></br>

### 6.1.3 実行方法
1. 「vcpASCIITable.ino」ファイルを開きます。
    1. Arduino IDE を開きます。
    2. **File -> Examples -> 05.VCP-G UART -> vcpASCIITable** をクリックします。
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
2. 「vcpASCIITable.ino」ファイルを検証し、VCP-G にアップロードします。
3. アップロード処理が無限アップロード状態で止まる場合は、FWDN モードが有効になっていないことが原因です。これを解決するには、次の手順を実行します:  
    1. VCP-G ボードから電源ケーブルを取り外します。
    2. FWDN スイッチを押し続けます。
    3. FWDN スイッチを押し続けたまま、電源ケーブルを再接続します。
    4. FWDN スイッチを離します。
        問題が解決しない場合は、管理者権限で Arduino IDE を実行してみてください。
4. ファイルのアップロードが成功したら、Arduino IDE の出力コンソールで次のメッセージを確認します:  

    **注記:** メッセージには **vcpASCIITable.ino.rom** が含まれている必要があります。
    ```
    [FWDN_VCP::WriteFile:577] Complete to send file - C:\Users\topstAppData\Local\arduino\sketches\487F45098412336AA9D73C50C17E07D8/vcpASCIITable.ino.rom

    [main:155] Complete FWDN
    ```

</br></br></br>

## 6.2 vcpGraph
---
このサンプルプログラムは、VCP-G がブレッドボード上のポテンショメータのアナログ値を読み取り、UART を介してホスト PC にデータを送信する方法を示します。Arduino コードは、A5 ピンに接続されたアナログセンサー（ポテンショメータ）の値を継続的に読み取り、シリアルポートを介して送信します。付属の Processing コードは、これらの値をリアルタイムで動的なグラフに可視化し、時間の経過に伴うセンサー入力の変化を表示します。
</br></br>

### 6.2.1 ハードウェア要件
- VCP-G ボード (x1)
- ブレッドボード (x1)
- ポテンショメータ (x1)
- 10 kΩ 抵抗 (x1)
- 12V 1A 電源アダプター (x1)
- USB Type-C to A ケーブル (x1)
- オス-オス ジャンパーワイヤー (x4)
</br></br>

### 6.2.2 回路
- ポテンショメータ
    - ポテンショメータの中央ピンは VCP-G ボードのアナログピン A5 に接続されます。
    - ポテンショメータの GND ピンは、10 kΩ 抵抗を介して VCP-G ボードの GND に接続します。
    - ポテンショメータの VCC ピンは、VCP-G ボードの 3.3V に接続します。

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/vcpGraph%20Circuit%20Schematic.png"></p>
<p align="center"><strong>図 6.1 vcpGraph 回路図</strong></p>

#### 6.2.2.1 ピンマップ
次の表はピンマッピングを示しています。

<p align="center"><strong>表 6.1 vcpGraph のピンマップ</strong></p>
<div align="center">
	<table>
	    <tr>
	        <th colspan="3">ピン名</th>
	        <th>VCP-G ボード</th>
	        <th>Arduino IDE</th>
	    </tr>
	    <tr>
	        <td colspan="3">ポテンショメータの中央ピン</td>
	        <td>A5</td>
	        <td>A5</td>
	    </tr>
	        <tr>
	        <td colspan="3">ポテンショメータの GND ピン</td>
	        <td>GND</td>
	        <td>-</td>
	    </tr>
	    <tr>
	        <td colspan="3">ポテンショメータ VCC ピン</td>
	        <td>3.3V</td>
	        <td>-</td>
	    </tr>
	</table>
</div>
</br></br>

### 6.2.3 実行方法
1. "vcpGraph.ino" ファイルを開きます。
    1. Arduino IDE を開きます。
    2. **File -> Examples -> 05.VCP-G UART -> vcpGraph** をクリックします。
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
2. "vcpGraph.ino" ファイルを検証し、VCP-G にアップロードします。
3. アップロード処理が無限アップロード状態で止まる場合は、FWDN モードが有効になっていないことが原因です。これを解決するには、次の手順を実行します:  
    1. VCP-G ボードから電源ケーブルを取り外します。
    2. FWDN スイッチを押し続けます。
    3. FWDN スイッチを押し続けたまま、電源ケーブルを再接続します。
    4. FWDN スイッチを離します。
        問題が解決しない場合は、管理者権限で Arduino IDE を実行してみてください。
4. ファイルのアップロードが成功したら、Arduino IDE の出力コンソールで次のメッセージを確認します。

    **注:** メッセージに **vcpGraph.ino.rom** が含まれている必要があります。
    ```
    [FWDN_VCP::WriteFile:577] Complete to send file - C:\Users\topst\AppData\Local\arduino\sketches\F59E4532EC3A529F5910F376F809A5E5/vcpGraph.ino.rom

    [main:155] Complete FWDN
    ```

</br></br></br></br>

# 7. 追加のサンプル
---
この章では、Arduino IDE の "Examples for TOPST VCP Rev G" に含まれていない追加のセンサーサンプルを説明します。  
一般的に使用される Arduino センサーを VCP-G ボードで使用するためのサンプルガイドを提供しており、さまざまなセンサーをプロジェクトに効果的に統合できます。

</br></br></br>

## 7.1 赤外線 (IR) センサー（トランシーバー）
---
### 7.1.1 赤外線 (IR) センサー 1
---
このサンプルは、VCP-G ボードがブレッドボード上の IR センサーと 2 個の LED を制御する方法を示します。IR センサーの値を読み取った後、IR センサーの値が HIGH の場合は障害物がないと判断され、緑色の LED が点灯し、赤色の LED が消灯します。逆に、IR センサーの値が LOW の場合は障害物があると判断され、赤色の LED が点灯し、緑色の LED が消灯します。また、障害物の有無がシリアルモニタに表示されます。

#### 7.1.1.1 ハードウェア要件
- VCP-G ボード (x1)
- ブレッドボード (x1)
- IR トランシーバーセンサー (x1)
- LED (x2: 異なる色を推奨します)
- 220Ω 抵抗 (x2)
- 12V 1A 電源アダプター (x1)
- USB Type-C to A ケーブル (x1)
- オス-オス ジャンパーワイヤー (x4)
- オス-メス ジャンパーワイヤ (x3)

#### 7.1.1.2 回路
- IR トランシーバーセンサー
    - IR センサーの OUT ピンは、VCP-G ボードの 50 番ピンに接続します。
    - IR センサーの VCC ピンは、VCP-G ボードの 5V に接続します。
    - IR センサーの GND ピンは、VCP-G ボードの GND に接続します。
- 赤色 LED
    - LED の (-) は抵抗に接続し、抵抗は VCP-G ボードの GND に接続します。
    - LED の (+) は、VCP-G ボードの 48 番ピンに接続します。
- 緑色 LED
    - LED の (-) は抵抗に接続し、抵抗は VCP-G ボードの GND に接続します。
    - LED の (+) は、VCP-G ボードの 17 番ピンに接続します。

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/Infrared%20(IR)%20Sensor%20Circuit%20Schematic.png"></p>
<p align="center"><strong>図 7.1 赤外線 (IR) センサー回路図</strong></p>

##### 7.1.1.2.1 ピンマップ
次の表はピンマッピングを示しています。

<p align="center"><strong>表 7.1 irSensor_LED のピンマップ</strong></p>
<div align="center">
	<table>
	    <tr>
	        <th colspan="3">ピン名</th>
	        <th>VCP-G ボード</th>
	        <th>Arduino IDE</th>
	    </tr>
	    <tr>
	        <td colspan="3">IR センサー OUT ピン </td>
	        <td>50</td>
	        <td>50</td>
	    </tr>
	        <tr>
	        <td colspan="3">IR センサー VCC ピン </td>
	        <td>5V</td>
	        <td>-</td>
	    </tr>
	    <tr>
	        <td colspan="3">IR センサー GND ピン</td>
	        <td>GND</td>
	        <td>-</td>
	    </tr>
	    <tr>
	        <td colspan="3">赤色 LED (+) ピン</td>
	        <td>48</td>
	        <td>48</td>
	    </tr>
	    <tr>
	        <td colspan="3">赤色 LED (-) ピン</td>
	        <td>GND</td>
	        <td>-</td>
	    </tr>
	    <tr>
	        <td colspan="3">緑色 LED (+) ピン</td>
	        <td>17</td>
	        <td>17</td>
	    </tr>
	    <tr>
	        <td colspan="3">緑色 LED (-) ピン </td>
	        <td>GND</td>
	        <td>-</td>
	    </tr>
	</table>
</div>

#### 7.1.1.3 実行方法
1. 次のソースコードを Arduino IDE にコピーし、ファイルを "irSensor_LED.ino" として保存します。
    
   **注:** 次のソースコードは本書でのみ提供されます。 

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
2. "irSensor_LED.ino" ファイルを検証し、VCP-G にアップロードします。
3. アップロード処理が無限アップロード状態で止まる場合は、FWDN モードが有効になっていないことが原因です。これを解決するには、次の手順を実行します:  
    1. VCP-G ボードから電源ケーブルを取り外します。
    2. FWDN スイッチを押し続けます。
    3. FWDN スイッチを押し続けたまま、電源ケーブルを再接続します。
    4. FWDN スイッチを離します。
        問題が解決しない場合は、管理者権限で Arduino IDE を実行してみてください。
4. ファイルのアップロードが成功したら、Arduino IDE の出力コンソールで次のメッセージを確認します。
 
    **注:** メッセージに **irSensor_LED.ino.rom** が含まれている必要があります。
    ```
    [FWDN_VCP::WriteFile:577] Complete to send file - C:\Users\topst\AppData\Local\arduino\sketches\1D003A72AB3391D6D60FD7993380F8CD/irSensor_LED.ino.rom 

    [main:155] Complete FWDN
    ```
</br></br>

### 7.1.2 赤外線 (IR) センサー 2
---
このサンプルは、VCP-G ボードが IR センサーを制御して物体を検知し、検知状態をシリアルモニタに出力する方法を示します。IR トランシーバーは障害物の有無を読み取ります。IR トランシーバーの値が HIGH の場合は障害物がないことを示し、緑色の LED が点灯し、赤色の LED が消灯します。逆に、IR トランシーバーの値が LOW の場合は障害物があることを示し、赤色の LED が点灯し、緑色の LED が消灯します。また、障害物の有無がシリアルモニタに表示されます。

#### 7.1.2.1 ハードウェア要件
- VCP-G ボード (x1)
- IR トランシーバーセンサー (x1)
- 12V 1A 電源アダプター (x1)
- USB Type-C to A ケーブル (x1)
- オス-メス ジャンパーワイヤ (x3)

#### 7.1.2.2 回路
- IR トランシーバーセンサー
    - IR トランシーバーセンサーの Out ピンは、VCP-G ボードの 8 番ピンに接続します。 
    - IR トランシーバーセンサーの VCC ピンは、VCP-G ボードの 5V に接続します。
    - IR トランシーバーセンサーの GND ピンは、VCP-G ボードの GND に接続します。

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/Infrared%20(IR)%20Sensor%20(Transceiver)%20Circuit%20Schematic.png"></p>
<p align="center"><strong>図 7.2 赤外線 (IR) センサー（トランシーバー）回路図</strong></p>

##### 7.1.2.2.1 ピンマップ
次の表はピンマッピングを示しています。

<p align="center"><strong>表 7.2 irTransceiver のピンマップ</strong></p>
<div align="center">
	<table>
	    <tr>
	        <th colspan="3">ピン名</th>
	        <th>VCP-G ボード</th>
	        <th>Arduino IDE</th>
	    </tr>
	    <tr>
	        <td colspan="3">IR トランシーバーセンサー OUT ピン</td>
	        <td>8</td>
	        <td>8</td>
	    </tr>
	    <tr>
	        <td colspan="3">IR トランシーバーセンサー VCC ピン</td>
	        <td>5V</td>
	        <td>-</td>
	    </tr>
	    <tr>
	        <td colspan="3">IR トランシーバーセンサー GND ピン</td>
	        <td>GND</td>
	        <td>-</td>
	    </tr>
	</table>
</div>

#### 7.1.2.3 実行方法
1. 次のソースコードを Arduino IDE にコピーし、ファイルを "irTransceiver.ino" として保存します。
   
   **注:** 次のソースコードは本書でのみ提供されます。 

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
2. "irTransceiver.ino" ファイルを検証し、VCP-G にアップロードします。
3. アップロード処理が無限アップロード状態で止まる場合は、FWDN モードが有効になっていないことが原因です。これを解決するには、次の手順を実行します:  
    1. VCP-G ボードから電源ケーブルを取り外します。
    2. FWDN スイッチを押し続けます。
    3. FWDN スイッチを押し続けたまま、電源ケーブルを再接続します。
    4. FWDN スイッチを離します。
        問題が解決しない場合は、管理者権限で Arduino IDE を実行してみてください。
4. ファイルのアップロードが成功したら、Arduino IDE の出力コンソールで次のメッセージを確認します。
   
    **注:** メッセージに **irTransceiver.ino.rom** が含まれている必要があります。
    ```
    [FWDN_VCP::WriteFile:577] Complete to send file - C:\Users\topst\AppData\Local\arduino\sketches\1D003A72AB3391D6D60FD7993380F8CD/irTransceiver.ino.rom 

    [main:155] Complete FWDN
    ```

</br></br></br>

## 7.2 ジョイスティック
---
このサンプルは、VCP-G がジョイスティックの入力を読み取り、その値をシリアルモニタに表示する方法を示します。X 軸、Y 軸、ボタンの 3 つの入力を受け取ることができます。シリアルモニタで受信した信号を確認します。X 軸および Y 軸で行われた動きはポートの値を変化させ、これはアナログ出力の数値に対応します。これにより、微調整が必要なアプリケーションで精密な制御が可能になります。

**注:** Dual Axis Joystick Module (KY-023) は Joy-IT の製品です。そのデザイン、商標および関連する知的財産に関するすべての権利は Joy-IT が所有しています。
</br></br>

### 7.2.1 ハードウェア要件
- VCP-G ボード (x1)
- Dual Axis Joystick Module (KY-023) (x1)
- 12V 1A 電源アダプター (x1)
- USB Type-C to A ケーブル (x1)
- オス-メス ジャンパーワイヤ (x5)
</br></br>

### 7.2.2 回路
- KY-023 (Dual Axis Joystick Module)
    - KY-023 の 5V ピンは、VCP-G ボードの 5V に接続します。
    - KY-023 の GND ピンは、VCP-G ボードの GND に接続します。 
    - KY-023 の VRx ピンは、VCP-G ボードのアナログピン A5 に接続します。 
    - KY-023 の VRy ピンは、VCP-G ボードのアナログピン A4 に接続します。 
    - KY-023 の SW ピンは、VCP-G ボードの 2 番ピンに接続します。

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/Joystick%20Circuit%20Schematic.png"></p>
<p align="center"><strong>図 7.3 ジョイスティック回路図</strong></p>

#### 7.2.2.1 ピンマップ
次の表はピンマッピングを示しています。

<p align="center"><strong>表 7.3 ジョイスティックのピンマップ</strong></p>
<div align="center">
	<table>
	    <tr>
	        <th colspan="3">ピン名</th>
	        <th>VCP-G ボード</th>
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

### 7.2.3 実行方法
1. 次のソースコードを Arduino IDE にコピーし、ファイルを "joystick.ino" として保存します。
   
   **注:** 次のソースコードは本書でのみ提供されます。 

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
2. "joystick.ino" ファイルを検証し、VCP-G にアップロードします。
3. アップロード処理が無限アップロード状態で止まる場合は、FWDN モードが有効になっていないことが原因です。これを解決するには、次の手順を実行します:  
    1. VCP-G ボードから電源ケーブルを取り外します。
    2. FWDN スイッチを押し続けます。
    3. FWDN スイッチを押し続けたまま、電源ケーブルを再接続します。
    4. FWDN スイッチを離します。  
        問題が解決しない場合は、管理者権限で Arduino IDE を実行してみてください。
4. ファイルのアップロードが成功したら、Arduino IDE の出力コンソールで次のメッセージを確認します。
   
    **注:** メッセージに **joystick.ino.rom** が含まれている必要があります。
    ```
    [FWDN_VCP::WriteFile:577] Complete to send file - C:\Users\topst\AppData\Local\arduino\sketches\1D003A72AB3391D6D60FD7993380F8CD/joystick.ino.rom 

    [main:155] Complete FWDN
    ```

</br></br></br>

## 7.3 ガスセンサー
---
このサンプルは、VCP-G ボードがガスセンサー (MQ 135) を使用して空気中のさまざまな有害ガスを検知する方法を示します。VCP-G ボードのアナログピンに接続されたセンサーからアナログ値を読み取り、電圧に変換した後、小数点以下 1 桁でシリアルモニタに出力します。

**注:** Gas Sensor (MQ-135) は Winsen® の製品です。そのデザイン、商標および関連する知的財産に関するすべての権利は Winsen が所有しています。
</br></br>

### 7.3.1 ハードウェア要件
- VCP-G ボード (x1)
- ガスセンサー (MQ135) (x1)
- 12V 1A 電源アダプター (x1)
- USB Type-C to A ケーブル (x1)
- オス-メス ジャンパーワイヤ (x3)
</br></br>

### 7.3.2 回路
- ガスセンサー
    - ガスセンサーの A0 ピンは、VCP-G ボードのアナログピン A5 に接続します。 
    - ガスセンサーの VCC ピンは、VCP-G ボードの 5V に接続します。
    - ガスセンサーの GND ピンは、VCP-G ボードの GND に接続します。


<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/Gas%20Sensor%20Circuit%20Schematic.png"></p>
<p align="center"><strong>図 7.4 ガスセンサー回路図</strong></p>

#### 7.3.2.1 ピンマップ
次の表はピンマッピングを示しています。

<p align="center"><strong>表 7.4 ガスセンサーのピンマップ</strong></p>
<div align="center">
	<table>
	    <tr>
	        <th colspan="3">ピン名</th>
	        <th>VCP-G ボード</th>
	        <th>Arduino IDE</th>
	    </tr>
	    <tr>
	        <td colspan="3">ガスセンサー A0 ピン</td>
	        <td>A5</td>
	        <td>A5</td>
	    </tr>
	        <tr>
	        <td colspan="3">ガスセンサー VCC ピン</td>
	        <td>5V</td>
	        <td>-</td>
	    </tr>
	    <tr>
	        <td colspan="3">ガスセンサー GND ピン</td>
	        <td>GND</td>
	        <td>-</td>
	    </tr>
	</table>
</div>
</br></br>

### 7.3.3 実行方法
1. 次のソースコードを Arduino IDE にコピーし、ファイルを "GasSensor.ino" として保存します。
  
   **注:** 次のソースコードは本書でのみ提供されます。 

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
2. "GasSensor.ino" ファイルを検証し、VCP-G にアップロードします。
3. アップロード処理が無限アップロード状態で止まる場合は、FWDN モードが有効になっていないことが原因です。これを解決するには、次の手順を実行します:  
    1. VCP-G ボードから電源ケーブルを取り外します。
    2. FWDN スイッチを押し続けます。
    3. FWDN スイッチを押し続けたまま、電源ケーブルを再接続します。
    4. FWDN スイッチを離します。  
        問題が解決しない場合は、管理者権限で Arduino IDE を実行してみてください。
4. ファイルのアップロードが成功したら、Arduino IDE の出力コンソールで次のメッセージを確認します。
   
    **注:** メッセージに **GasSensor.ino.rom** が含まれている必要があります。
    ```
    [FWDN_VCP::WriteFile:577] Complete to send file - C:\Users\topst\AppData\Local\arduino\sketches\1D003A72AB3391D6D60FD7993380F8CD/joystick.ino.rom 

    [main:155] Complete FWDN
    ```
</br></br></br>

## 7.4 メタルタッチセンサーモジュール
---
このサンプルプログラムは、VCP-G ボードがブレッドボード上のタッチセンサーと LED を制御する方法を示します。メタルタッチセンサーモジュール (KY-036) は、金属表面や人の皮膚へのタッチを検知するように設計された多用途のアナログ/デジタルセンサーです。このモジュールはトランジスタを使用してタッチ時の電気伝導率の変化を検知し、VCP-G との連携のためにデジタル信号とアナログ信号の両方を出力します。  
タッチが検知されると、メタルタッチセンサーモジュールは該当するデジタル/アナログ値をシリアルモニタに出力します。また、タッチの状態に応じて LED を制御することもできます。 

**注:** メタルタッチセンサーモジュール (KY-036) には、感度を調整するためのポテンショメータが内蔵されています。このポテンショメータを回すことで感度を上げ下げできます。
</br></br>

### 7.4.1 ハードウェア要件
- VCP-G ボード (x1)
- ブレッドボード (x1)
- メタルタッチセンサーモジュール (KY-036) (x1)
- LED (x1)
- 220Ω 抵抗 (x1)
- 12V 1A 電源アダプター (x1)
- USB Type-C to A ケーブル (x1)
- オス-オス ジャンパーワイヤー (x4)
- オス-メス ジャンパーワイヤ (x4)
</br></br>

### 7.4.2 回路
- メタルタッチセンサーモジュール
    - メタルタッチセンサーモジュールの A0 ピンは、VCP-G ボードのアナログピン A5 に接続します。
    - メタルタッチセンサーモジュールの G ピンは、VCP-G ボードの GND に接続します。
    - Metal Touch センサーモジュールの (+) ピンは、VCP-G ボードの 5V に接続します。
    - Metal Touch センサーモジュールの D0 ピンは、VCP-G ボードの 30 番ピンに接続します。

- LED
    - LED の (+) ピンは、VCP-G ボードの 13 番ピンに接続します。
    - LED の (-) ピンは、220Ω の抵抗を介して VCP-G ボードの GND に接続します。


<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/Metal%20Touch%20Sensor%20Circuit%20Schematic.png"></p>
<p align="center"><strong>図 7.5 Metal Touch センサーの回路図</strong></p>

#### 7.4.2.1 ピンマッピング
次の表はピンマッピングを示しています。

<p align="center"><strong>表 7.5 Metal Touch センサーのピンマッピング</strong></p>
<div align="center">
	<table>
	    <tr>
	        <th colspan="3">ピン名</th>
	        <th>VCP-G ボード</th>
	        <th>Arduino IDE</th>
	    </tr>
	    <tr>
	        <td colspan="3">Metal Touch センサーモジュール A0 ピン</td>
	        <td>A5</td>
	        <td>A5</td>
	    </tr>
	        <tr>
	        <td colspan="3">Metal Touch センサーモジュール G ピン</td>
	        <td>GND</td>
	        <td>-</td>
	    </tr>
	    <tr>
	        <td colspan="3">Metal Touch センサーモジュール (+) ピン</td>
	        <td>5V</td>
		    <td>-</td>
		</tr>
	    <tr>
	        <td colspan="3">Metal Touch センサーモジュール D0 ピン</td>
	        <td>30</td>
	        <td>30</td>
	    </tr>
	    <tr>
	        <td colspan="3">LED (+) ピン</td>
	        <td>13</td>
	        <td>13</td>
	    </tr>
	    <tr>
	        <td colspan="3">LED (+) ピン</td>
	        <td>GND</td>
	        <td>-</td>
	    </tr>
	</table>
</div>
</br></br>

### 7.4.3 実行方法
1. 以下のソースコードを Arduino IDE にコピーし、ファイルを "vcp_touch.ino" という名前で保存します。  

   **注:** 次のソースコードは本書でのみ提供されます。 

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
2. "vcp_touch.ino" ファイルを検証し、VCP-G にアップロードします。
3. アップロード処理が無限アップロード状態で止まる場合は、FWDN モードが有効になっていないことが原因です。これを解決するには、次の手順を実行します:  
    1. VCP-G ボードから電源ケーブルを取り外します。
    2. FWDN スイッチを押し続けます。
    3. FWDN スイッチを押し続けたまま、電源ケーブルを再接続します。
    4. FWDN スイッチを離します。  
        問題が解決しない場合は、管理者権限で Arduino IDE を実行してみてください。
4. ファイルのアップロードが成功したら、Arduino IDE の出力コンソールで次のメッセージを確認します。
   
    **注:** メッセージには **vcp_touch.ino.rom** が含まれている必要があります。
    ```
    [FWDN_VCP::WriteFile:577] Complete to send file - C:\Users\topst\AppData\Local\arduino\sketches\567805554B5B9F915DCC80B38483AE07/vcp_touch.ino.rom

    [main:155] Complete FWDN
    ```

**注:** シリアル通信には適切なボーレートを設定してください。

</br></br></br>

## 7.5 モータードライバを使用したステッピングモーター
---
この例では、VCP-G ボードで 4 線式ステッピングモーター (28BYJ-48 (5VDC)) とモータードライバ (ULN2003 (5V–12V)) を制御する方法を説明します。7.5.3 章のコードでは、モータードライバに接続するピンを定義し、1 回転あたりのステップ数を設定します。モーターは正方向に 1 回転して停止し、その後逆方向に 1 回転して再び停止します。モーターの速度はステップ間の遅延時間によって制御され、回転方向はコイルを励磁する順序によって制御されます。

**注:** 28BYJ-48 モーターは、Half step モードでは 1 回転に 4096 個の信号、Full step モードでは 1 回転に 2048 個の信号を必要とします。正確なモーター制御を行うには、モードに応じて必要な信号数を考慮する必要があります。 
</br></br>

### 7.5.1 ハードウェア要件
- VCP-G ボード (x1)
- ステッピングモーター (28BYJ-48) (x1)
- モータードライバ (ULN2003) (x1)
- 12V 1A 電源アダプター (x1)
- USB Type-C to A ケーブル (x1)
- オス-オス ジャンパーワイヤ (x6)
</br></br>

### 7.5.2 回路
- モータードライバ
    - IN1 ピンは、VCP-G ボードの 8 番ピンに接続します。
    - IN2 ピンは、VCP-G ボードの 9 番ピンに接続します。
    - IN3 ピンは、VCP-G ボードの 10 番ピンに接続します。
    - IN4 ピンは、VCP-G ボードの 11 番ピンに接続します。
    - (+) ピンは、VCP-G ボードの 5V に接続します。
    - (-) ピンは、VCP-G ボードの GND に接続します。

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/Step%20Motor%20with%20Motor%20Driver%20Circuit%20Schematic.png"></p>
<p align="center"><strong>図 7.6 モータードライバを使用したステッピングモーターの回路図</strong></p>

#### 7.5.2.1 ピンマッピング
次の表はピンマッピングを示しています。

<p align="center"><strong>表 7.6 モータードライバのピンマッピング</strong></p>
<div align="center">
	<table>
	    <tr>
	        <th colspan="3">ピン名</th>
	        <th>VCP-G ボード</th>
	        <th>Arduino IDE</th>
	    </tr>
	    <tr>
	        <td colspan="3">モータードライバ IN1 ピン</td>
	        <td>8</td>
	        <td>8</td>
	    </tr>
	        <tr>
	        <td colspan="3">モータードライバ IN2 ピン</td>
	        <td>9</td>
	        <td>9</td>
	    </tr>
	    <tr>
	        <td colspan="3">モータードライバ IN3 ピン</td>
	        <td>10</td>
	        <td>10</td>
		</tr>
	    <tr>
	        <td colspan="3">モータードライバ IN4 ピン</td>
		    <td>11</td>
			<td>11</td>
	    </tr>
		<tr>
			<td colspan="3">モータードライバ (+) ピン</td>
	        <td>5V</td>
	        <td>-</td>
		</tr>
	    <tr>
	        <td colspan="3">モータードライバ (-) ピン</td>
	        <td>GND</td>
	        <td>-</td>
	    </tr>
	</table>
</div>
</br></br>

### 7.5.3 実行方法
1. 以下のソースコードを Arduino IDE にコピーし、ファイルを "motordriver.ino" という名前で保存します。

    **注:** 以下のソースコードは本ドキュメントでのみ提供されます。 

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
2. "motordriver.ino" ファイルを検証し、VCP-G にアップロードします。
3. アップロード処理が無限アップロード状態で止まる場合は、FWDN モードが有効になっていないことが原因です。これを解決するには、次の手順を実行します:  
    1. VCP-G ボードから電源ケーブルを取り外します。
    2. FWDN スイッチを押し続けます。
    3. FWDN スイッチを押し続けたまま、電源ケーブルを再接続します。
    4. FWDN スイッチを離します。  
        問題が解決しない場合は、管理者権限で Arduino IDE を実行してみてください。
4. ファイルのアップロードが成功したら、Arduino IDE の出力コンソールで次のメッセージを確認します:  

    **注:** メッセージには **motordriver.ino.rom** が含まれている必要があります。
    ```
    [FWDN_VCP::WriteFile:577] Complete to send file - C:\Users\topst\AppData\Local\arduino\sketches\567805554B5B9F915DCC80B38483AE07/motordriver.rom

    [main:155] Complete FWDN
    ```
</br></br></br></br>

# 8. 参考資料
---
- 詳細については TOPST にお問い合わせください: topst@topst.ai

**注意:** 参考文書は、契約条件に応じて提供可能な場合に提供されます。参考
文書が入手できない場合は、お客様の開発に直接関連する内容をご案内できます。
