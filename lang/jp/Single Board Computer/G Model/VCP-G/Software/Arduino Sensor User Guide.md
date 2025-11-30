# 1. はじめに
---
このドキュメントでは、VCP-GボードでさまざまなArduinoセンサーを使用するためのガイドラインを提供します。VCP-Gを使用してプロジェクトを簡単に開発できるように、接続手順とサンプルコードが含まれています。
 
具体的には、このドキュメントでは、以下を含むVCP-GのArduino IDEの例に関するガイダンスを提供します。
- VCP-G Digital
- VCP-G Analog
- VCP-G SPI
- VCP-G I2C
- VCP-G UART
- 追加の例
 
VCP-Gを使用する前に、図 1.1を参照してください。
 
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/vcp-g%20pinout%20Diagram.png"></p>
<p align="center"><strong>図 1.1 VCP-G ピン配置図</strong></p>
 
</br></br></br></br>
 
# 2. VCP-G デジタルピン
---
この章では、VCP-Gボードのデジタルピンを使用してLEDを制御する例を示します。VCP-Gでは、デジタルピンはバイナリ信号（HIGHまたはLOW）の送受信に使用されるため、LED、スイッチ、センサーなどのコンポーネントの制御に不可欠です。
 
この章には、デジタル出力を使用して複数のLEDを制御する方法を示す2つのサンプルプロジェクトが含まれており、デジタルピン機能の基礎的な理解を提供します。
 
</br></br></br>
 
## 2.1 vcp4LED
---
このサンプルプログラムは、VCP-Gボードがブレッドボード上の4つのLEDを制御する方法を示しています。サンプルコードは「vcp4LED.ino」ファイルで提供されています。このファイルがVCP-Gにアップロードされると、LEDは500ミリ秒の遅延で順方向と逆方向の両方のパターンで順次点灯および消灯します。
 
</br></br>
 
### 2.1.1 ハードウェア要件
- VCP-Gボード (x1)
- ブレッドボード (x1)
- LED (x4)
- 220Ω抵抗 (x4)
- 12V 1A電源アダプター (x1)
- USB Type-C to Aケーブル (x1)
- オス-オス ジャンパーワイヤー (x9)
</br></br>
 
### 2.1.2 回路
- LED01
    - (+) ピンは、220Ωの抵抗を介してブレッドボード上の5V電源レールに接続され、VCP-Gボードから供給されます。
    - (-) ピンはVCP-Gボードのピン47に接続されています。
- LED02
    - (+) ピンは、220Ωの抵抗を介してブレッドボード上の5V電源レールに接続されています。
    - (-) ピンはVCP-Gボードのピン17に接続されています。
- LED03
    - (+) ピンは、220Ωの抵抗を介してブレッドボード上の5V電源レールに接続されています。
    - (-) ピンはVCP-Gボードのピン50に接続されています。
- LED04
    - (+) ピンは、220Ωの抵抗を介してブレッドボード上の5V電源レールに接続されています。
    - (-) ピンはVCP-Gボードのピン48に接続されています。
 
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/vcp4LED%20Circuit%20Schematic.png"></p>
<p align="center"><strong>図 2.1 vcp4LED 回路図</strong></p>
 
#### 2.1.2.1 ピンマッピング
次の表はピンマッピングを示しています。
 
<p align="center"><strong>表 2.1 vcp4LEDのピンマッピング</strong></p>
<div align="center">	
	<table>
		<tr>
			<th colspan="3">ピン名</th>
	        <th>VCP-Gボード</th>
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
1. 「vcp4LED.ino」ファイルを開きます。
    1. Arduino IDEを開きます。
    2. **File -> Examples -> 01.VCP-G Digital -> vcp4LED**をクリックします。
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
2. 「vcp4LED.ino」ファイルを検証し、VCP-Gにアップロードします。
3. アップロードプロセスが無限アップロード状態で止まる場合は、FWDNモードがアクティブになっていないためです。これを解決するには：
    1. VCP-Gボードから電源ケーブルを外します。
    2. FWDNスイッチを押し続けます。
    3. FWDNスイッチを押したまま、電源ケーブルを再接続します。
    4. FWDNスイッチを放します。
        問題が解決しない場合は、管理者権限でArduino IDEを実行してみてください。
4. ファイルが正常にアップロードされたら、Arduino IDEの出力コンソールで次のメッセージを確認します。
 
     **注:** メッセージには **vcp4LED.ino.rom** が含まれている必要があります。
    ```
    [FWDN_VCP::WriteFile:577] Complete to send file - C:\Users\topst\AppData\Local\arduino\sketches\C05357299384CE5734F0E696C5A4DA3B/vcp4LED.ino.rom
    
    [main:155] Complete FWDN
    ```
 
</br></br></br>
 
## 2.2 vcp4LED_Button
---
このサンプルプログラムは、VCP-Gボードがブレッドボード上の4つのLEDとボタンを制御する方法を示しています。ボタンが押されると、右側の2つのLEDが消灯し、左側の2つのLEDが点灯します。ボタンが放されると、点灯していたLEDが消灯し、消灯していたLEDが点灯します。プログラムはボタンの状態を継続的にチェックし、それに応じてLEDを調整します。
</br></br>
 
### 2.2.1 ハードウェア要件
- VCP-Gボード (x1)
- ブレッドボード (x1)
- LED (x4)
- ボタン（センサー） (x1)
- 220Ω抵抗 (x4)
- 12V 1A電源アダプター (x1)
- USB Type-C to Aケーブル (x1)
- オス-オス ジャンパーワイヤー (x12)
</br></br>
 
### 2.2.2 回路
1.	LED01
    - (+) ピンは、220Ωの抵抗を介してブレッドボード上の5V電源レールに接続され、VCP-Gボードから供給されます。
    - (-) ピンはVCP-Gボードのピン47に接続されています。
2.	LED02
    - (+) ピンは、220Ωの抵抗を介してブレッドボード上の5V電源レールに接続されています。
    - (-) ピンはVCP-Gボードのピン17に接続されています。
3.	LED03
    - (+) ピンは、220Ωの抵抗を介してブレッドボード上の5V電源レールに接続されています。
    - (-) ピンはVCP-Gボードのピン50に接続されています。
4.	LED04
    - (+) ピンは、220Ωの抵抗を介してブレッドボード上の5V電源レールに接続されています。
    - (-) ピンはVCP-Gボードのピン48に接続されています。
5.	ボタンスイッチ
    - ボタンスイッチの片方の足は、VCP-Gボードのピン45に接続されています。
    - ボタンの対角線上にある足は、GNDピンに接続されています。
 
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/vcp4LED_Button%20Circuit%20Schematic.png"></p>
<p align="center"><strong>図 2.2 vcp4LED_Button 回路図</strong></p>
 
#### 2.2.2.1 ピンマッピング
次の表はピンマッピングを示しています。
 
<p align="center"><strong>表 2.2 vcp4LED_Buttonのピンマッピング</strong></p>
<div align="center">
	<table>
	    <tr>
	        <th colspan="3">ピン名</th>
	        <th>VCP-Gボード</th>
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
	        <td colspan="3">ボタンの片方の足</td>
	        <td>45</td>
	        <td>45</td>
	    </tr>
	</table>
</div>
</br></br>
 
### 2.1.3 実行方法
1. 「vcp4LED_Button.ino」ファイルを開きます。
    1. Arduino IDEを開きます。
    2. **File -> Examples -> 01.VCP-G Digital -> vcp4LED_Button**をクリックします。
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
2. 「vcp4LED_Button.ino」ファイルを検証し、VCP-Gにアップロードします。
3. アップロードプロセスが無限アップロード状態で止まる場合は、FWDNモードがアクティブになっていないためです。これを解決するには：
    1. VCP-Gボードから電源ケーブルを外します。
    2. FWDNスイッチを押し続けます。
    3. FWDNスイッチを押したまま、電源ケーブルを再接続します。
    4. FWDNスイッチを放します。
        問題が解決しない場合は、管理者権限でArduino IDEを実行してみてください。
4. ファイルが正常にアップロードされたら、Arduino IDEの出力コンソールで次のメッセージを確認します。
 
     **注:** メッセージには **vcp4LED_Button.ino.rom** が含まれている必要があります。
    ```
    [FWDN_VCP::WriteFile:577] Complete to send file - C:\Users\topst\AppData\Local\arduino\sketches\5CC1DB4CA216E2BC009504FAA3D06456/vcp4LED_Button.ino.rom
    
    [main:155] Complete FWDN
    ```
 
</br></br></br></br>
 
# 3. VCP-G アナログピン
---
この章では、VCP-Gボードのアナログピンを使用する例を示します。VCP-Gでは、アナログピンはセンサーから連続的な電圧信号を受信し、変化する入力値を正確に測定できます。第3.1章、第3.2章、および第3.3章では、アナログピンを使用してセンサーデータを読み取り、出力を制御する方法について説明し、アナログ入力処理の基礎的な理解を提供します。
 
</br></br></br>
 
## 3.1 AnalogInOutSerial
---
このサンプルプログラムは、VCP-Gボードがブレッドボード上のポテンショメータとLEDを制御する方法を示しています。VCP-Gはアナログ入力ピンから値を読み取り、その結果を0〜1000の範囲にマッピングし、この値を使用して出力ピン（LEDに接続）のパルス幅変調（PWM）を設定します。結果はシリアルモニタにも出力されます。
</br></br>
 
### 3.1.1 ハードウェア要件
- VCP-Gボード (x1)
- ブレッドボード (x1)
- LED (x1)
- ポテンショメータ (x1)
- 220Ω抵抗 (x2)
- 12V 1A電源アダプター (x1)
- USB Type-C to Aケーブル (x1)
- オス-オス ジャンパーワイヤー (x4)
</br></br>
 
### 3.1.2 回路
- ポテンショメータ
    - ポテンショメータの中央ピンは、VCP-GボードのアナログピンA5に接続されています。
    - ポテンショメータのGNDピンは、VCP-Gボードのピン43に接続され、220Ωの抵抗を介してVCP-GボードのGNDピンに接続されています。
- LED
    - LEDの(+) ピンは、220Ωの抵抗を介してVCP-Gボードの3.3Vに接続されています。
    - LEDの(-) ピンは、ポテンショメータの中央ピンに接続されています。
 
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/AnalogInOutSerial%20Circuit%20Schematic.png"></p>
<p align="center"><strong>図 3.1 AnalogInOutSerial 回路図</strong></p>
 
#### 3.1.2.1 ピンマッピング
次の表はピンマッピングを示しています。
 
<p align="center"><strong>表 3.1 AnalogInOutSerialのピンマッピング</strong></p>
<div align="center">
	<table>
	    <tr>
	        <th colspan="3">ピン名</th>
	        <th>VCP-Gボード</th>
	        <th>Arduino IDE</th>
	    </tr>
	    <tr>
	        <td colspan="3">ポテンショメータ中央ピン</td>
	        <td>A5</td>
	        <td>-</td>
	    </tr>
	        <tr>
	        <td colspan="3">ポテンショメータGNDピン</td>
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
1. 「AnalogInOutSerial.ino」ファイルを開きます。
    1. Arduino IDEを開きます。
    2. **File -> Examples -> 02.VCP-G Analog -> AnalogInOutSerial**をクリックします。
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
 
    **注:** 「Serial」が宣言されていないというエラーが発生した場合は、次のライブラリとオブジェクト宣言が正しく含まれていることを確認してください。
    ```
    #include <HardwareSerial.h>
    HardwareSerial Serial;
    ```
2. 「AnalogInOutSerial.ino」ファイルを検証し、VCP-Gにアップロードします。
3. アップロードプロセスが無限アップロード状態で止まる場合は、FWDNモードがアクティブになっていないためです。これを解決するには：
    1. VCP-Gボードから電源ケーブルを外します。
    2. FWDNスイッチを押し続けます。
    3. FWDNスイッチを押したまま、電源ケーブルを再接続します。
    4. FWDNスイッチを放します。
        問題が解決しない場合は、管理者権限でArduino IDEを実行してみてください。
4. ファイルが正常にアップロードされたら、Arduino IDEの出力コンソールで次のメッセージを確認します。
 
    **注:** メッセージには **AnalogInOutSerial.ino.rom** が含まれている必要があります。
    ```
    [FWDN_VCP::WriteFile:577] Complete to send file - C:\Users\topst\AppData\Local\arduino\sketches\EB016432EF98DEF0B9102FD77148DD5D/AnalogInOutSerial.ino.rom
    
    [main:155] Complete FWDN
    ```
 
</br></br></br>
 
## 3.2 AnalogInput
---
このサンプルプログラムは、VCP-Gボードがブレッドボード上のポテンショメータとLEDを制御する方法を示しています。アナログ入力ピンから値を読み取り、この値を使用してLEDを制御します。センサー値が3000未満の場合、LEDが点灯します。センサー値が3000以上の場合、LEDは消灯します。
</br></br>
 
### 3.2.1 ハードウェア要件
- VCP-Gボード (x1)
- ブレッドボード (x1)
- LED (x1)
- ポテンショメータ (x1)
- 220Ω抵抗 (x1)
- 12V 1A電源アダプター (x1)
- USB Type-C to Aケーブル (x1)
- オス-オス ジャンパーワイヤー (x6)
</br></br>
 
### 3.2.2 回路
- ポテンショメータ
    - ポテンショメータのVCCピンは、220Ωの抵抗を介してVCP-Gボードの3.3Vに接続されています。
    - ポテンショメータの中央ピンは、VCP-GボードのアナログピンA5に接続されています。
    - ポテンショメータのGNDピンは、220Ωの抵抗を介してVCP-GボードのGNDピンに接続されています。
- LED
    - LEDの(+) ピンは、220Ωの抵抗を介してVCP-Gボードの3.3Vに接続されています。
    - LEDの(-) ピンは、VCP-Gボードのピン5に接続されています。
 
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/AnalogInput%20Circuit%20Schematic.png"></p>
<p align="center"><strong>図 3.2 AnalogInput 回路図</strong></p>
 
#### 3.2.2.1 ピンマッピング
次の表はピンマッピングを示しています。
 
<p align="center"><strong>表 3.2 AnalogInputのピンマッピング</strong></p>
<div align="center">
	<table>
	    <tr>
	        <th colspan="3">ピン名</th>
	        <th>VCP-Gボード</th>
	        <th>Arduino IDE</th>
	    </tr>
	    <tr>
	        <td colspan="3">ポテンショメータVCCピン</td>
	        <td>3.3V</td>
	        <td>-</td>
	    </tr>
	    <tr>
	        <td colspan="3">ポテンショメータ中央ピン</td>
	        <td>A5</td>
	        <td>A5</td>
	    </tr>
	        <tr>
	        <td colspan="3">ポテンショメータGNDピン</td>
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
    1. Arduino IDEを開きます。
    2. **File -> Examples -> 02.VCP-G Analog -> AnalogInput**をクリックします。
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
 
    **注 1:** シリアルモニタで **sensorValue** を確認するには、ソースコードに **Serial.println()** を追加してください。
    **注 2:** センサー値を調整するために、可変抵抗器（ポテンショメータ）とともに固定抵抗器が使用されます。センサー値はポテンショメータをどれだけ回すかによって変化し、ポテンショメータを回す必要がある量は固定抵抗器の値によって異なります。
 
2. 「AnalogInput.ino」ファイルを検証し、VCP-Gにアップロードします。
3. アップロードプロセスが無限アップロード状態で止まる場合は、FWDNモードがアクティブになっていないためです。これを解決するには：
    1. VCP-Gボードから電源ケーブルを外します。
    2. FWDNスイッチを押し続けます。
    3. FWDNスイッチを押したまま、電源ケーブルを再接続します。
    4. FWDNスイッチを放します。
        問題が解決しない場合は、管理者権限でArduino IDEを実行してみてください。
4. ファイルが正常にアップロードされたら、Arduino IDEの出力コンソールで次のメッセージを確認します。
 
   **注:** メッセージには **AnalogInput.ino.rom** が含まれている必要があります。
    ```
    [FWDN_VCP::WriteFile:577] Complete to send file - C:\Users\topst\AppData\Local\arduino\sketches\C3FDEE51354320EA689DFEB4EDCF2ECD/AnalogInput.ino.rom
    
    [main:155] Complete FWDN
    ```
 
</br></br></br>
 
## 3.3 pwmFade
---
このサンプルプログラムは、VCP-GボードがPWMを使用してループ内で明るさを徐々に増減させることにより、ブレッドボード上のLEDを制御する方法を示しています。LEDが最大輝度に達した後、LEDの輝度は低下し始めます。プログラムはLEDの輝度を継続的に調整し、フェード効果を作成します。
</br></br>
 
### 3.3.1 ハードウェア要件
- VCP-Gボード (x1)
- ブレッドボード (x1)
- LED (x1)
- 220Ω抵抗 (x1)
- 12V 1A電源アダプター (x1)
- USB Type-C to Aケーブル (x1)
- オス-オス ジャンパーワイヤー (x2)
</br></br>
 
### 3.3.2 回路
- LED
    - LEDの(+) ピンは、VCP-Gボードの5Vに接続されています。
    - LEDの(-) ピンは、220Ωの抵抗を介してVCP-Gボードのピン9に接続されています。
 
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/pwmFade%20Circuit%20Schematic.png"></p>
<p align="center"><strong>図 3.3 pwmFade 回路図</strong></p>
 
#### 3.3.2.1 ピンマッピング
次の表はピンマッピングを示しています。
 
<p align="center"><strong>表 3.3 pwmFadeのピンマッピング</strong></p>
<div align="center">
	<table>
	    <tr>
	        <th colspan="3">ピン名</th>
	        <th>VCP-Gボード</th>
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
    1. Arduino IDEを開きます。
    2. **File -> Examples -> 02.VCP-G Analog -> pwmFade**をクリックします。
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
2. 「pwmFade.ino」ファイルを検証し、VCP-Gボードにアップロードします。
3. アップロードプロセスが無限アップロード状態で止まる場合は、FWDNモードがアクティブになっていないためです。これを解決するには：
    1. VCP-Gボードから電源ケーブルを外します。
    2. FWDNスイッチを押し続けます。
    3. FWDNスイッチを押したまま、電源ケーブルを再接続します。
    4. FWDNスイッチを放します。
        問題が解決しない場合は、管理者権限でArduino IDEを実行してみてください。
4. ファイルが正常にアップロードされたら、Arduino IDEの出力コンソールで次のメッセージを確認します。
 
     **注:** メッセージには **pwmFade.ino.rom** が含まれている必要があります。
    ```
    [FWDN_VCP::WriteFile:577] Complete to send file - C:\Users\topst\AppData\Local\arduino\sketches\69446E8A7F6616A7D5466014BDF759FC/pwmFade.ino.rom 
    
    [main:155] Complete FWDN
    ```
 
</br></br></br></br>
 
# 4. VCP SPI
---
この章では、VCP-Gでのシリアル周辺インターフェイス (SPI) 通信の構成手順について説明します。
SPIは、マイクロコントローラーと周辺機器の間でデータを交換するために使用される高速同期通信プロトコルです。データ送信 (MOSIおよびMISO)、クロック同期 (SCK)、およびデバイス選択 (SS) 用の個別のラインで動作し、効率的で信頼性の高い通信を保証します。
次の章では、SPIを設定して外部デバイスとインターフェイスする方法について説明します。
 
</br></br></br>
 
## 4.1 vcpSPI_Dot8x8
---
このサンプルプログラムは、VCP-GボードがMAX7219ドライバを使用して8x8 LEDドットマトリックスを制御する方法を示しています。8x8 LEDドットマトリックスは、事前に定義されたバイナリ配列で行を設定することにより、ハート形や文字「R」などのパターンを表示します。LEDの強度はパルス効果を作成するように調整され、動的な視覚効果を追加します。機能性を高めるために、ディスプレイの反転やクリアなどの追加機能が含まれています。
</br></br>
 
### 4.1.1 ハードウェア要件
- VCP-Gボード (x1)
- 8x8ドットマトリックス (x1)
- 12V 1A電源アダプター (x1)
- USB Type-C to Aケーブル (x1)
- オス-メス ジャンパーワイヤー (x5)
</br></br>
 
### 4.1.2 回路
- 8x8ドットマトリックス
    - 8x8ドットマトリックスのVCCピンは、VCP-Gボードのアナログピン5Vに接続されています。
    - 8x8ドットマトリックスのGNDピンは、VCP-GボードのGNDに接続されています。
    - 8x8ドットマトリックスのDINピンは、VCP-Gボードのピン11に接続されています。
    - 8x8ドットマトリックスのCSピンは、VCP-Gボードのピン10に接続されています。
    - 8x8ドットマトリックスのCLKピンは、VCP-Gボードのピン13に接続されています。
 
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/vcpSPI_Dot8x8%20Circuit%20Schematic.png"></p>
<p align="center"><strong>図 4.1 vcpSPI_Dot8x8 回路図</strong></p>
 
#### 4.1.2.1 ピンマッピング
次の表はピンマッピングを示しています。
 
<p align="center"><strong>表 4.1 vcpSPI_Dot8x8のピンマッピング</strong></p>
<div align="center">
	<table>
	    <tr>
	        <th colspan="3">ピン名</th>
	        <th>VCP-Gボード</th>
	        <th>Arduino IDE</th>
	    </tr>
	    <tr>
	        <td colspan="3">8x8ドットマトリックス VCCピン</td>
	        <td>5V</td>
	        <td>-</td>
	    </tr>
	        <tr>
	        <td colspan="3">8x8ドットマトリックス GNDピン</td>
	        <td>GND</td>
	        <td>-</td>
	    </tr>
	    <tr>
	        <td colspan="3">8x8ドットマトリックス DINピン</td>
	        <td>11</td>
	        <td>11</td>
	    </tr>
	    <tr>
	        <td colspan="3">8x8ドットマトリックス CSピン</td>
	        <td>10</td>
	        <td>10</td>
	    </tr>
	    <tr>
	        <td colspan="3">8x8ドットマトリックス CLKピン</td>
	        <td>13</td>
	        <td>13</td>
	    </tr>
	</table>
</div>
</br></br>
 
### 4.1.3 実行方法
1. 「vcpSPI_Dot8x8.ino」ファイルを開きます。
    1. Arduino IDEを開きます。
    2. **File -> Examples -> 03.VCP-G SPI -> vcpSPI_Dot8x8**をクリックします。
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
2. 「vcpSPI_Dot8x8.ino」ファイルを検証し、VCP-Gにアップロードします。
3. アップロードプロセスが無限アップロード状態で止まる場合は、FWDNモードがアクティブになっていないためです。これを解決するには：
    1. VCP-Gボードから電源ケーブルを外します。
    2. FWDNスイッチを押し続けます。
    3. FWDNスイッチを押したまま、電源ケーブルを再接続します。
    4. FWDNスイッチを放します。
        問題が解決しない場合は、管理者権限でArduino IDEを実行してみてください。
4. ファイルが正常にアップロードされたら、Arduino IDEの出力コンソールで次のメッセージを確認します。
 
    **注:** メッセージには **vcpSPI_Dot8x8.ino.rom** が含まれている必要があります。
    ```
    [FWDN_VCP::WriteFile:577] Complete to send file - C:\Users\topst\AppData\Local\arduino\sketches\567805554B5B9F915DCC80B38483AE07/vcpSPI_Dot8x8.ino.rom
    
    [main:155] Complete FWDN
    ```
 
**注:** VCP-Gボードの中央にあるSPIピンを使用したい場合は、次のピン番号を参照して使用できます。
<p align="center"><strong>表 4.2 VCP-Gの中央SPIピンのマッピング</strong></p>
<div align="center">
	<table>
	    <tr>
	        <th colspan="3">ピン番号</th>
	        <th>SPI機能</th>
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
この章では、VCP-GでのInter-integrated Circuit (I2C) 通信の構成手順について説明します。
I2Cは、複数のデバイス間で効率的にデータを交換するために設計された2線式の同期通信プロトコルです。シリアルデータライン (SDA) とシリアルクロックライン (SCL) で動作し、複数の周辺機器が固有のアドレスを使用してマイクロコントローラーと通信できるようにします。I2Cはマスター/スレーブ通信とマルチマスター構成の両方をサポートしているため、必要な接続数を最小限に抑えながら、センサー、ディスプレイ、その他の低速デバイスを接続するのに最適です。
 
</br></br></br>
 
## 5.1 vcpI2C_LCD1602
---
このサンプルプログラムは、VCP-GボードがI2C通信プロトコルを使用してLCD1602ディスプレイを制御する方法を示しています。LCD1602は、組み込みシステムプロジェクトで一般的に使用される16文字×2行の液晶ディスプレイです。LiquidCrystal_I2Cライブラリを利用することで、ボードはI2Cバスを介してコマンドとデータを送信し、ディスプレイを効率的に制御します。
 
この例では、LCDが初期化され、バックライトが有効になって視認性が確保されます。次に、プログラムはカーソルを配置して、最初の行に「VCP-G」、2番目の行に「I2C Test!」というテキストを表示します。I2C通信を使用すると、最小限の配線で複数のデバイスを制御できるため、コンパクトなプロジェクトに効果的なソリューションとなります。
</br></br>
 
### 5.1.1 ハードウェア要件
- VCP-Gボード (x1)
- LCD1602 (x1)
- 12V 1A電源アダプター (x1)
- USB Type-C to Aケーブル (x1)
- オス-メス ジャンパーワイヤー (x4)
</br></br>
 
### 5.1.2 回路
- LCD1602
    - LCD1602のVCCピンは、VCP-Gボードのアナログピン5Vに接続されています。
    - LCD1602のGNDピンは、VCP-GボードのGNDに接続されています。
    - LCD1602のSDAピンは、VCP-Gボードのピン48に接続されています。
    - LCD1602のSCLピンは、VCP-Gボードのピン49に接続されています。
 
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/vcpI2C_LCD1602%20Circuit%20Schematic.png"></p>
<p align="center"><strong>図 5.1 vcpI2C_LCD1602 回路図</strong></p>
 
#### 5.1.2.1 ピンマッピング
次の表はピンマッピングを示しています。
 
<p align="center"><strong>表 5.1 vcpI2C_LCD1602のピンマッピング</strong></p>
<div align="center">
	<table>
	    <tr>
	        <th colspan="3">ピン名</th>
	        <th>VCP-Gボード</th>
	        <th>Arduino IDE</th>
	    </tr>
	    <tr>
	        <td colspan="3">LCD1602 VCCピン</td>
	        <td>5V</td>
	        <td>-</td>
	    </tr>
	        <tr>
	        <td colspan="3">LCD1602 GNDピン</td>
	        <td>GND</td>
	        <td>-</td>
	    </tr>
	    <tr>
	        <td colspan="3">LCD1602 SDAピン</td>
	        <td>48</td>
	        <td>-</td>
	    </tr>
	    <tr>
	        <td colspan="3">LCD1602 SCLピン</td>
	        <td>49</td>
		    <td>-</td>
	    </tr>
	</table>
</div>
 
</br></br>
 
### 5.1.3 実行方法
1. 「vcpI2C_LCD1602.ino」ファイルを開きます。
    1. Arduino IDEを開きます。
    2. **File -> Examples -> 04.VCP-G I2C -> vcpI2C_LCD1602**をクリックします。
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
2. 「vcpI2C_LCD1602.ino」ファイルを検証し、VCP-Gにアップロードします。
3. アップロードプロセスが無限アップロード状態で止まる場合は、FWDNモードがアクティブになっていないためです。これを解決するには：
    1. VCP-Gボードから電源ケーブルを外します。
    2. FWDNスイッチを押し続けます。
    3. FWDNスイッチを押したまま、電源ケーブルを再接続します。
    4. FWDNスイッチを放します。
        問題が解決しない場合は、管理者権限でArduino IDEを実行してみてください。
4. ファイルが正常にアップロードされたら、Arduino IDEの出力コンソールで次のメッセージを確認します。
   
    **注:** メッセージには **vcpI2C_LCD1602.ino.rom** が含まれている必要があります。
    ```
    [FWDN_VCP::WriteFile:577] Complete to send file -         C:\Users\topst\AppData\Local\arduino\sketches\C8D91A6857B651D6C665B0EF18B7EE53/vcpI2C_LCD1602.ino.rom
    
    [main:155] Complete FWDN
    ```
 
</br></br></br></br>
 
# 6. VCP-G UART
---
この章では、VCP-GでのUniversal Asynchronous Receiver-Transmitter (UART) 通信の構成手順について説明します。
UARTは、送信 (TX) と受信 (RX) の2本の線のみを使用して非同期でデータを送信する、広く使用されているシリアル通信プロトコルです。共有クロック信号を必要とせずに、マイクロコントローラー、センサー、およびコンピューター間でデータを交換するために不可欠です。
次の章では、UARTを介してデータを送受信する方法について説明します。
 
</br></br></br>
 
## 6.1 vcpASCIITable
---
このサンプルプログラムは、VCP-Gが文字のASCII値を10進数、16進数、8進数、および2進数のさまざまな形式で出力する方法を示しています。文字「!」（ASCII値33）から始まり、すべての表示可能なASCII文字をインクリメントして、それぞれを異なる形式で出力します。プログラムは、文字「~」（ASCII値126）に達するまで続きます。
</br></br>
 
### 6.1.1 ハードウェア要件
- VCP-Gボード (x1)
- 12V 1A電源アダプター (x1)
- USB Type-C to Aケーブル (x1)
</br></br>
 
### 6.1.3 実行方法
1. 「vcpASCIITable.ino」ファイルを開きます。
    1. Arduino IDEを開きます。
    2. **File -> Examples -> 05.VCP-G UART -> vcpASCIITable**をクリックします。
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
2. 「vcpASCIITable.ino」ファイルを検証し、VCP-Gにアップロードします。
3. アップロードプロセスが無限アップロード状態で止まる場合は、FWDNモードがアクティブになっていないためです。これを解決するには：
    1. VCP-Gボードから電源ケーブルを外します。
    2. FWDNスイッチを押し続けます。
    3. FWDNスイッチを押したまま、電源ケーブルを再接続します。
    4. FWDNスイッチを放します。
        問題が解決しない場合は、管理者権限でArduino IDEを実行してみてください。
4. ファイルが正常にアップロードされたら、Arduino IDEの出力コンソールで次のメッセージを確認します。
 
    **注:** メッセージには **vcpASCIITable.ino.rom** が含まれている必要があります。
    ```
    [FWDN_VCP::WriteFile:577] Complete to send file - C:\Users\topstAppData\Local\arduino\sketches\487F45098412336AA9D73C50C17E07D8/vcpASCIITable.ino.rom
    
    [main:155] Complete FWDN
    ```
 
</br></br></br>
 
## 6.2 vcpGraph
---
このサンプルプログラムは、VCP-Gがブレッドボード上のポテンショメータのアナログ値を読み取り、UARTを介してホストPCにデータを送信する方法を示しています。Arduinoコードは、ピンA5に接続されたアナログセンサー（ポテンショメータ）の値を継続的に読み取り、シリアルポートを介して送信します。付属のProcessingコードは、これらの値をリアルタイムで動的なグラフに視覚化し、時間の経過に伴うセンサー入力の変化を示します。
</br></br>
 
### 6.2.1 ハードウェア要件
- VCP-Gボード (x1)
- ブレッドボード (x1)
- ポテンショメータ (x1)
- 10 kΩ抵抗 (x1)
- 12V 1A電源アダプター (x1)
- USB Type-C to Aケーブル (x1)
- オス-オス ジャンパーワイヤー (x4)
</br></br>
 
### 6.2.2 回路
- ポテンショメータ
    - ポテンショメータの中央ピンは、VCP-GボードのアナログピンA5に接続されています。
    - ポテンショメータのGNDピンは、10 kΩの抵抗を介してVCP-GボードのGNDに接続されています。
    - ポテンショメータのVCCピンは、VCP-Gボードの3.3Vに接続されています。
 
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/vcpGraph%20Circuit%20Schematic.png"></p>
<p align="center"><strong>図 6.1 vcpGraph 回路図</strong></p>
 
#### 6.2.2.1 ピンマッピング
次の表はピンマッピングを示しています。
 
<p align="center"><strong>表 6.1 vcpGraphのピンマッピング</strong></p>
<div align="center">
	<table>
	    <tr>
	        <th colspan="3">ピン名</th>
	        <th>VCP-Gボード</th>
	        <th>Arduino IDE</th>
	    </tr>
	    <tr>
	        <td colspan="3">ポテンショメータ中央ピン</td>
	        <td>A5</td>
	        <td>A5</td>
	    </tr>
	        <tr>
	        <td colspan="3">ポテンショメータGNDピン</td>
	        <td>GND</td>
	        <td>-</td>
	    </tr>
	    <tr>
	        <td colspan="3">ポテンショメータVCCピン</td>
	        <td>3.3V</td>
	        <td>-</td>
	    </tr>
	</table>
</div>
</br></br>
 
### 6.2.3 実行方法
1. 「vcpGraph.ino」ファイルを開きます。
    1. Arduino IDEを開きます。
    2. **File -> Examples -> 05.VCP-G UART -> vcpGraph**をクリックします。
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
2. 「vcpGraph.ino」ファイルを検証し、VCP-Gにアップロードします。
3. アップロードプロセスが無限アップロード状態で止まる場合は、FWDNモードがアクティブになっていないためです。これを解決するには：
    1. VCP-Gボードから電源ケーブルを外します。
    2. FWDNスイッチを押し続けます。
    3. FWDNスイッチを押したまま、電源ケーブルを再接続します。
    4. FWDNスイッチを放します。
        問題が解決しない場合は、管理者権限でArduino IDEを実行してみてください。
4. ファイルが正常にアップロードされたら、Arduino IDEの出力コンソールで次のメッセージを確認します。
 
    **注:** メッセージには **vcpGraph.ino.rom** が含まれている必要があります。
    ```
    [FWDN_VCP::WriteFile:577] Complete to send file - C:\Users\topst\AppData\Local\arduino\sketches\F59E4532EC3A529F5910F376F809A5E5/vcpGraph.ino.rom
    
    [main:155] Complete FWDN
    ```
 
</br></br></br></br>
 
# 7. 追加の例
---
この章では、Arduino IDEの「Examples for TOPST VCP Rev G」に含まれていない追加のセンサーの例を提供します。
VCP-Gボードで一般的に使用されるArduinoセンサーを使用するためのガイド例を提供し、さまざまなセンサーをプロジェクトに効果的に統合できるようにします。
 
</br></br></br>
 
## 7.1 赤外線 (IR) センサー (トランシーバー)
---
### 7.1.1 赤外線 (IR) センサー 1
---
この例は、VCP-Gボードがブレッドボード上のIRセンサーと2つのLEDを制御する方法を示しています。IRセンサーの値を読み取った後、IRセンサーの値がHIGHの場合、障害物がないと見なされ、緑色のLEDが点灯し、赤色のLEDが消灯します。逆に、IRセンサーの値がLOWの場合、障害物があると見なされ、赤色のLEDが点灯し、緑色のLEDが消灯します。さらに、障害物の有無がシリアルモニタに表示されます。
 
#### 7.1.1.1 ハードウェア要件
- VCP-Gボード (x1)
- ブレッドボード (x1)
- IRトランシーバーセンサー (x1)
- LED (x2: 異なる色を推奨)
- 220Ω抵抗 (x2)
- 12V 1A電源アダプター (x1)
- USB Type-C to Aケーブル (x1)
- オス-オス ジャンパーワイヤー (x4)
- オス-メス ジャンパーワイヤー (x3)
 
#### 7.1.1.2 回路
- IRトランシーバーセンサー
    - IRセンサーのOUTピンは、VCP-Gボードのピン50に接続されています。
    - IRセンサーのVCCピンは、VCP-Gボードの5Vに接続されています。
    - IRセンサーのGNDピンは、VCP-GボードのGNDに接続されています。
- 赤色LED
    - LEDの(-) は抵抗に接続され、抵抗はVCP-GボードのGNDに接続されています。
    - LEDの(+) はVCP-Gボードのピン48に接続されています。
- 緑色LED
    - LEDの(-) は抵抗に接続され、抵抗はVCP-GボードのGNDに接続されています。
    - LEDの(+) はVCP-Gボードのピン17に接続されています。
 
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/Infrared%20(IR)%20Sensor%20Circuit%20Schematic.png"></p>
<p align="center"><strong>図 7.1 赤外線 (IR) センサー回路図</strong></p>
 
##### 7.1.1.2.1 ピンマッピング
次の表はピンマッピングを示しています。
 
<p align="center"><strong>表 7.1 irSensor_LEDのピンマッピング</strong></p>
<div align="center">
	<table>
	    <tr>
	        <th colspan="3">ピン名</th>
	        <th>VCP-Gボード</th>
	        <th>Arduino IDE</th>
	    </tr>
	    <tr>
	        <td colspan="3">IRセンサー OUTピン </td>
	        <td>50</td>
	        <td>50</td>
	    </tr>
	        <tr>
	        <td colspan="3">IRセンサー VCCピン </td>
	        <td>5V</td>
	        <td>-</td>
	    </tr>
	    <tr>
	        <td colspan="3">IRセンサー GNDピン</td>
	        <td>GND</td>
	        <td>-</td>
	    </tr>
	    <tr>
	        <td colspan="3">赤色LED (+) ピン</td>
	        <td>48</td>
	        <td>48</td>
	    </tr>
	    <tr>
	        <td colspan="3">赤色LED (-) ピン</td>
	        <td>GND</td>
	        <td>-</td>
	    </tr>
	    <tr>
	        <td colspan="3">緑色LED (+) ピン</td>
	        <td>17</td>
	        <td>17</td>
	    </tr>
	    <tr>
	        <td colspan="3">緑色LED (-) ピン </td>
	        <td>GND</td>
	        <td>-</td>
	    </tr>
	</table>
</div>
 
#### 7.1.1.3 実行方法
1. 次のソースコードをArduino IDEにコピーし、ファイルを「irSensor_LED.ino」として保存します。
    
   **注:** 次のソースコードはこのドキュメントでのみ提供されています。
 
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
2. 「irSensor_LED.ino」ファイルを検証し、VCP-Gにアップロードします。
3. アップロードプロセスが無限アップロード状態で止まる場合は、FWDNモードがアクティブになっていないためです。これを解決するには：
    1. VCP-Gボードから電源ケーブルを外します。
    2. FWDNスイッチを押し続けます。
    3. FWDNスイッチを押したまま、電源ケーブルを再接続します。
    4. FWDNスイッチを放します。
        問題が解決しない場合は、管理者権限でArduino IDEを実行してみてください。
4. ファイルが正常にアップロードされたら、Arduino IDEの出力コンソールで次のメッセージを確認します。
 
    **注:** メッセージには **irSensor_LED.ino.rom** が含まれている必要があります。
    ```
    [FWDN_VCP::WriteFile:577] Complete to send file - C:\Users\topst\AppData\Local\arduino\sketches\1D003A72AB3391D6D60FD7993380F8CD/irSensor_LED.ino.rom 
    
    [main:155] Complete FWDN
    ```
</br></br>
 
### 7.1.2 赤外線 (IR) センサー 2
---
この例は、VCP-GボードがIRセンサーを制御して物体を検出し、検出ステータスをシリアルモニタに出力する方法を示しています。IRトランシーバーは障害物の有無を読み取ります。IRトランシーバーの値がHIGHの場合、障害物がないことを示し、緑色のLEDが点灯し、赤色のLEDが消灯します。逆に、IRトランシーバーの値がLOWの場合、障害物があることを示し、赤色のLEDが点灯し、緑色のLEDが消灯します。さらに、障害物の有無がシリアルモニタに表示されます。
 
#### 7.1.2.1 ハードウェア要件
- VCP-Gボード (x1)
- IRトランシーバーセンサー (x1)
- 12V 1A電源アダプター (x1)
- USB Type-C to Aケーブル (x1)
- オス-メス ジャンパーワイヤー (x3)
 
#### 7.1.2.2 回路
- IRトランシーバーセンサー
    - IRトランシーバーセンサーのOutピンは、VCP-Gボードのピン8に接続されています。
    - IRトランシーバーセンサーのVCCピンは、VCP-Gボードの5Vに接続されています。
    - IRトランシーバーセンサーのGNDピンは、VCP-GボードのGNDに接続されています。
 
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/Infrared%20(IR)%20Sensor%20(Transceiver)%20Circuit%20Schematic.png"></p>
<p align="center"><strong>図 7.2 赤外線 (IR) センサー (トランシーバー) 回路図</strong></p>
 
##### 7.1.2.2.1 ピンマッピング
次の表はピンマッピングを示しています。
 
<p align="center"><strong>表 7.2 irTransceiverのピンマッピング</strong></p>
<div align="center">
	<table>
	    <tr>
	        <th colspan="3">ピン名</th>
	        <th>VCP-Gボード</th>
	        <th>Arduino IDE</th>
	    </tr>
	    <tr>
	        <td colspan="3">IRトランシーバーセンサー OUTピン</td>
	        <td>8</td>
	        <td>8</td>
	    </tr>
	    <tr>
	        <td colspan="3">IRトランシーバーセンサー VCCピン</td>
	        <td>5V</td>
	        <td>-</td>
	    </tr>
	    <tr>
	        <td colspan="3">IRトランシーバーセンサー GNDピン</td>
	        <td>GND</td>
	        <td>-</td>
	    </tr>
	</table>
</div>
 
#### 7.1.2.3 実行方法
1. 次のソースコードをArduino IDEにコピーし、ファイルを「irTransceiver.ino」として保存します。
   
   **注:** 次のソースコードはこのドキュメントでのみ提供されています。
 
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
2. 「irTransceiver.ino」ファイルを検証し、VCP-Gにアップロードします。
3. アップロードプロセスが無限アップロード状態で止まる場合は、FWDNモードがアクティブになっていないためです。これを解決するには：
    1. VCP-Gボードから電源ケーブルを外します。
    2. FWDNスイッチを押し続けます。
    3. FWDNスイッチを押したまま、電源ケーブルを再接続します。
    4. FWDNスイッチを放します。
        問題が解決しない場合は、管理者権限でArduino IDEを実行してみてください。
4. ファイルが正常にアップロードされたら、Arduino IDEの出力コンソールで次のメッセージを確認します。
   
    **注:** メッセージには **irTransceiver.ino.rom** が含まれている必要があります。
    ```
    [FWDN_VCP::WriteFile:577] Complete to send file - C:\Users\topst\AppData\Local\arduino\sketches\1D003A72AB3391D6D60FD7993380F8CD/irTransceiver.ino.rom 
    
    [main:155] Complete FWDN
    ```
 
</br></br></br>
 
## 7.2 ジョイスティック
---
この例は、VCP-Gがジョイスティック入力を読み取り、その値をシリアルモニタに表示する方法を示しています。X軸、Y軸、およびボタンの3つの入力を受信できます。シリアルモニタは受信した信号を確認します。X軸とY軸で行われた動きはポートの値を変更し、これはアナログ出力の数値に対応します。微調整が必要なアプリケーションの正確な制御が可能になります。
 
**注:** デュアルアクシスジョイスティックモジュール (KY-023) はJoy-ITの製品です。そのデザイン、商標、および関連する知的財産に対するすべての権利はJoy-ITが所有しています。
</br></br>
 
### 7.2.1 ハードウェア要件
- VCP-Gボード (x1)
- デュアルアクシスジョイスティックモジュール (KY-023) (x1)
- 12V 1A電源アダプター (x1)
- USB Type-C to Aケーブル (x1)
- オス-メス ジャンパーワイヤー (x5)
</br></br>
 
### 7.2.2 回路
- KY-023 (デュアルアクシスジョイスティックモジュール)
    - KY-023の5Vピンは、VCP-Gボードの5Vに接続されています。
    - KY-023のGNDピンは、VCP-GボードのGNDに接続されています。
    - KY-023のVRxピンは、VCP-GボードのアナログピンA5に接続されています。
    - KY-023のVRyピンは、VCP-GボードのアナログピンA4に接続されています。
    - KY-023のSWピンは、VCP-Gボードのピン2に接続されています。
 
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/Joystick%20Circuit%20Schematic.png"></p>
<p align="center"><strong>図 7.3 ジョイスティック回路図</strong></p>
 
#### 7.2.2.1 ピンマッピング
次の表はピンマッピングを示しています。
 
<p align="center"><strong>表 7.3 ジョイスティックのピンマッピング</strong></p>
<div align="center">
	<table>
	    <tr>
	        <th colspan="3">ピン名</th>
	        <th>VCP-Gボード</th>
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
1. 次のソースコードをArduino IDEにコピーし、ファイルを「joystick.ino」として保存します。
   
   **注:** 次のソースコードはこのドキュメントでのみ提供されています。
 
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
2. 「joystick.ino」ファイルを検証し、VCP-Gにアップロードします。
3. アップロードプロセスが無限アップロード状態で止まる場合は、FWDNモードがアクティブになっていないためです。これを解決するには：
    1. VCP-Gボードから電源ケーブルを外します。
    2. FWDNスイッチを押し続けます。
    3. FWDNスイッチを押したまま、電源ケーブルを再接続します。
    4. FWDNスイッチを放します。
        問題が解決しない場合は、管理者権限でArduino IDEを実行してみてください。
4. ファイルが正常にアップロードされたら、Arduino IDEの出力コンソールで次のメッセージを確認します。
   
    **注:** メッセージには **joystick.ino.rom** が含まれている必要があります。
    ```
    [FWDN_VCP::WriteFile:577] Complete to send file - C:\Users\topst\AppData\Local\arduino\sketches\1D003A72AB3391D6D60FD7993380F8CD/joystick.ino.rom 
    
    [main:155] Complete FWDN
    ```
 
</br></br></br>
 
## 7.3 ガスセンサー
---
この例は、VCP-Gボードがガスセンサー (MQ 135) を使用して空気中のさまざまな有害ガスを検出する方法を示しています。VCP-Gボードのアナログピンに接続されたセンサーからアナログ値を読み取り、電圧に変換してから、小数点以下1桁でシリアルモニタに出力します。
 
**注:** ガスセンサー (MQ-135) はWinsen®の製品です。そのデザイン、商標、および関連する知的財産に対するすべての権利はWinsenが所有しています。
</br></br>
 
### 7.3.1 ハードウェア要件
- VCP-Gボード (x1)
- ガスセンサー (MQ135) (x1)
- 12V 1A電源アダプター (x1)
- USB Type-C to Aケーブル (x1)
- オス-メス ジャンパーワイヤー (x3)
</br></br>
 
### 7.3.2 回路
- ガスセンサー
    - ガスセンサーのA0ピンは、VCP-GボードのアナログピンA5に接続されています。
    - ガスセンサーのVCCピンは、VCP-Gボードの5Vに接続されています。
    - ガスセンサーのGNDピンは、VCP-GボードのGNDに接続されています。
 
 
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/Gas%20Sensor%20Circuit%20Schematic.png"></p>
<p align="center"><strong>図 7.4 ガスセンサー回路図</strong></p>
 
#### 7.3.2.1 ピンマッピング
次の表はピンマッピングを示しています。
 
<p align="center"><strong>表 7.4 ガスセンサーのピンマッピング</strong></p>
<div align="center">
	<table>
	    <tr>
	        <th colspan="3">ピン名</th>
	        <th>VCP-Gボード</th>
	        <th>Arduino IDE</th>
	    </tr>
	    <tr>
	        <td colspan="3">ガスセンサー A0ピン</td>
	        <td>A5</td>
	        <td>A5</td>
	    </tr>
	        <tr>
	        <td colspan="3">ガスセンサー VCCピン</td>
	        <td>5V</td>
	        <td>-</td>
	    </tr>
	    <tr>
	        <td colspan="3">ガスセンサー GNDピン</td>
	        <td>GND</td>
	        <td>-</td>
	    </tr>
	</table>
</div>
</br></br>
 
### 7.3.3 実行方法
1. 次のソースコードをArduino IDEにコピーし、ファイルを「GasSensor.ino」として保存します。
  
   **注:** 次のソースコードはこのドキュメントでのみ提供されています。
 
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
2. 「GasSensor.ino」ファイルを検証し、VCP-Gにアップロードします。
3. アップロードプロセスが無限アップロード状態で止まる場合は、FWDNモードがアクティブになっていないためです。これを解決するには：
    1. VCP-Gボードから電源ケーブルを外します。
    2. FWDNスイッチを押し続けます。
    3. FWDNスイッチを押したまま、電源ケーブルを再接続します。
    4. FWDNスイッチを放します。
        問題が解決しない場合は、管理者権限でArduino IDEを実行してみてください。
4. ファイルが正常にアップロードされたら、Arduino IDEの出力コンソールで次のメッセージを確認します。
   
    **注:** メッセージには **GasSensor.ino.rom** が含まれている必要があります。
    ```
    [FWDN_VCP::WriteFile:577] Complete to send file - C:\Users\topst\AppData\Local\arduino\sketches\1D003A72AB3391D6D60FD7993380F8CD/joystick.ino.rom 
    
    [main:155] Complete FWDN
    ```
</br></br></br>
 
## 7.4 メタルタッチセンサーモジュール
---
このサンプルプログラムは、VCP-Gボードがタッチセンサーとブレッドボード上のLEDを制御する方法を示しています。メタルタッチセンサーモジュール (KY-036) は、金属表面や人間の皮膚への接触を検出するように設計された多用途のアナログ/デジタルセンサーです。このモジュールは、トランジスタを使用して接触時の電気伝導率の変化を感知し、VCP-Gとの相互作用のためにデジタル信号とアナログ信号の両方を出力します。
タッチが検出されると、メタルタッチセンサーモジュールは関連するデジタル/アナログ値をシリアルモニタに出力します。タッチステータスに基づいてLEDを制御することもできます。
 
**注:** メタルタッチセンサーモジュール (KY-036) には、感度を調整するためのポテンショメータが内蔵されています。このポテンショメータを回して、感度を上げたり下げたりできます。
</br></br>
 
### 7.4.1 ハードウェア要件
- VCP-Gボード (x1)
- ブレッドボード (x1)
- メタルタッチセンサーモジュール (KY-036) (x1)
- LED (x1)
- 220Ω抵抗 (x1)
- 12V 1A電源アダプター (x1)
- USB Type-C to Aケーブル (x1)
- オス-オス ジャンパーワイヤー (x4)
- オス-メス ジャンパーワイヤー (x4)
</br></br>
 
### 7.4.2 回路
- メタルタッチセンサーモジュール
    - メタルタッチセンサーモジュールのA0ピンは、VCP-GボードのアナログピンA5に接続されています。
    - メタルタッチセンサーモジュールのGピンは、VCP-GボードのGNDに接続されています。
    - メタルタッチセンサーモジュールの(+) ピンは、VCP-Gボードの5Vに接続されています。
    - メタルタッチセンサーモジュールのD0ピンは、VCP-Gボードのピン30に接続されています。
 
- LED
    - LEDの(+) ピンは、VCP-Gボードのピン13に接続されています。
    - LEDの(-) ピンは、220Ωの抵抗を介してVCP-GボードのGNDに接続されています。
 
 
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/Metal%20Touch%20Sensor%20Circuit%20Schematic.png"></p>
<p align="center"><strong>図 7.5 メタルタッチセンサー回路図</strong></p>
 
#### 7.4.2.1 ピンマッピング
次の表はピンマッピングを示しています。
 
<p align="center"><strong>表 7.5 メタルタッチセンサーのピンマッピング</strong></p>
<div align="center">
	<table>
	    <tr>
	        <th colspan="3">ピン名</th>
	        <th>VCP-Gボード</th>
	        <th>Arduino IDE</th>
	    </tr>
	    <tr>
	        <td colspan="3">メタルタッチセンサーモジュール A0ピン</td>
	        <td>A5</td>
	        <td>A5</td>
	    </tr>
	        <tr>
	        <td colspan="3">メタルタッチセンサーモジュール Gピン</td>
	        <td>GND</td>
	        <td>-</td>
	    </tr>
	    <tr>
	        <td colspan="3">メタルタッチセンサーモジュール (+) ピン</td>
	        <td>5V</td>
		    <td>-</td>
		</tr>
	    <tr>
	        <td colspan="3">メタルタッチセンサーモジュール D0ピン</td>
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
1. 次のソースコードをArduino IDEにコピーし、ファイルを「vcp_touch.ino」として保存します。
 
   **注:** 次のソースコードはこのドキュメントでのみ提供されています。
 
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
2. 「vcp_touch.ino」ファイルを検証し、VCP-Gにアップロードします。
3. アップロードプロセスが無限アップロード状態で止まる場合は、FWDNモードがアクティブになっていないためです。これを解決するには：
    1. VCP-Gボードから電源ケーブルを外します。
    2. FWDNスイッチを押し続けます。
    3. FWDNスイッチを押したまま、電源ケーブルを再接続します。
    4. FWDNスイッチを放します。
        問題が解決しない場合は、管理者権限でArduino IDEを実行してみてください。
4. ファイルが正常にアップロードされたら、Arduino IDEの出力コンソールで次のメッセージを確認します。
   
    **注:** メッセージには **vcp_touch.ino.rom** が含まれている必要があります。
    ```
    [FWDN_VCP::WriteFile:577] Complete to send file - C:\Users\topst\AppData\Local\arduino\sketches\567805554B5B9F915DCC80B38483AE07/vcp_touch.ino.rom
    
    [main:155] Complete FWDN
    ```
 
**注:** シリアル通信には適切なボーレートを設定してください。
 
</br></br></br>
 
## 7.5 モータードライバー付きステップモーター
---
この例は、VCP-Gボードが4線式ステッピングモーター (28BYJ-48 (5VDC)) とモータードライバー (ULN2003 (5V–12V)) を制御する方法を示しています。第7.5.3章のコードは、モータードライバーに接続されたピンを定義し、1回転あたりのステップ数を設定します。モーターは1回転正転して一時停止し、1回転逆転して再び一時停止します。モーターの速度はステップ間の遅延によって制御され、方向はコイルがアクティブになる順序によって制御されます。
 
**注:** 28BYJ-48モーターは、ハーフステップモードで1回転するのに4096信号、フルステップモードで1回転するのに2048信号を必要とします。正確なモーター制御のためには、モードに応じた必要な信号数を考慮する必要があります。
</br></br>
 
### 7.5.1 ハードウェア要件
- VCP-Gボード (x1)
- ステップモーター (28BYJ-48) (x1)
- モータードライバー (ULN2003) (x1)
- 12V 1A電源アダプター (x1)
- USB Type-C to Aケーブル (x1)
- オス-オス ジャンパーワイヤー (x6)
</br></br>
 
### 7.5.2 回路
- モータードライバー
    - IN1ピンはVCP-Gボードのピン8に接続されています。
    - IN2ピンはVCP-Gボードのピン9に接続されています。
    - IN3ピンはVCP-Gボードのピン10に接続されています。
    - IN4ピンはVCP-Gボードのピン11に接続されています。
    - (+) ピンはVCP-Gボードの5Vに接続されています。
    - (-) ピンはVCP-GボードのGNDに接続されています。
 
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/Step%20Motor%20with%20Motor%20Driver%20Circuit%20Schematic.png"></p>
<p align="center"><strong>図 7.6 モータードライバー付きステップモーター回路図</strong></p>
 
#### 7.5.2.1 ピンマッピング
次の表はピンマッピングを示しています。
 
<p align="center"><strong>表 7.6 モータードライバーのピンマッピング</strong></p>
<div align="center">
	<table>
	    <tr>
	        <th colspan="3">ピン名</th>
	        <th>VCP-Gボード</th>
	        <th>Arduino IDE</th>
	    </tr>
	    <tr>
	        <td colspan="3">モータードライバー IN1ピン</td>
	        <td>8</td>
	        <td>8</td>
	    </tr>
	        <tr>
	        <td colspan="3">モータードライバー IN2ピン</td>
	        <td>9</td>
	        <td>9</td>
	    </tr>
	    <tr>
	        <td colspan="3">モータードライバー IN3ピン</td>
	        <td>10</td>
	        <td>10</td>
	    </tr>
		</tr>
	    <tr>
	        <td colspan="3">モータードライバー IN4ピン</td>
		    <td>11</td>
			<td>11</td>
	    </tr>
		<tr>
			<td colspan="3">モータードライバー (+) ピン</td>
	        <td>5V</td>
	        <td>-</td>
		</tr>
	    <tr>
	        <td colspan="3">モータードライバー (-) ピン</td>
	        <td>GND</td>
	        <td>-</td>
	    </tr>
	</table>
</div>
</br></br>
 
### 7.5.3 実行方法
1. 次のソースコードをArduino IDEにコピーし、ファイルを「motordriver.ino」として保存します。
 
    **注:** 次のソースコードはこのドキュメントでのみ提供されています。
 
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
2. 「motordriver.ino」ファイルを検証し、VCP-Gにアップロードします。
3. アップロードプロセスが無限アップロード状態で止まる場合は、FWDNモードがアクティブになっていないためです。これを解決するには：
    1. VCP-Gボードから電源ケーブルを外します。
    2. FWDNスイッチを押し続けます。
    3. FWDNスイッチを押したまま、電源ケーブルを再接続します。
    4. FWDNスイッチを放します。
        問題が解決しない場合は、管理者権限でArduino IDEを実行してみてください。
4. ファイルが正常にアップロードされたら、Arduino IDEの出力コンソールで次のメッセージを確認します。
 
    **注:** メッセージには **motordriver.ino.rom** が含まれている必要があります。
    ```
    [FWDN_VCP::WriteFile:577] Complete to send file - C:\Users\topst\AppData\Local\arduino\sketches\567805554B5B9F915DCC80B38483AE07/motordriver.rom
    
    [main:155] Complete FWDN
    ```
</br></br></br></br>
 
# 8. 参考文献
---
- 詳細については、TOPSTにお問い合わせください: topst@topst.ai
 
**注:** 参考文献は、契約条件に応じて、利用可能な場合にいつでも提供できます。参考文献が利用できない場合は、開発に直接関連する内容をご案内できます。
