# 1. 소개
---
이 문서는 VCP-G 보드에서 다양한 Arduino 센서를 사용하는 방법에 대한 가이드라인을 제공합니다. VCP-G를 사용하여 프로젝트를 쉽게 개발할 수 있도록 연결 지침과 예제 코드가 포함되어 있습니다.
 
구체적으로 이 문서는 다음을 포함하여 VCP-G용 Arduino IDE 예제에 대한 지침을 제공합니다:
- VCP-G Digital
- VCP-G Analog
- VCP-G SPI
- VCP-G I2C
- VCP-G UART
- 추가 예제
 
VCP-G를 사용하기 전에 그림 1.1을 참조하십시오.
 
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/vcp-g%20pinout%20Diagram.png"></p>
<p align="center"><strong>그림 1.1 VCP-G 핀 배치도</strong></p>
 
</br></br></br></br>
 
# 2. VCP-G 디지털 핀
---
이 장에서는 VCP-G 보드의 디지털 핀을 사용하여 LED를 제어하는 예제를 제공합니다. VCP-G에서 디지털 핀은 이진 신호(HIGH 또는 LOW)를 보내거나 받는 데 사용되므로 LED, 스위치 및 센서와 같은 구성 요소를 제어하는 데 필수적입니다.
 
이 장에는 디지털 출력을 사용하여 여러 LED를 제어하는 방법을 보여주는 두 가지 예제 프로젝트가 포함되어 있어 디지털 핀 기능에 대한 기본적인 이해를 제공합니다.
 
</br></br></br>
 
## 2.1 vcp4LED
---
이 예제 프로그램은 VCP-G 보드가 브레드보드의 4개 LED를 제어하는 방법을 보여줍니다. 예제 코드는 "vcp4LED.ino" 파일에 제공됩니다. 이 파일이 VCP-G에 업로드되면 LED는 각 전환 사이에 500ms 지연을 두고 순방향 및 역방향 패턴으로 순차적으로 켜지고 꺼집니다.
 
</br></br>
 
### 2.1.1 하드웨어 요구 사항
- VCP-G 보드 (x1)
- 브레드보드 (x1)
- LED (x4)
- 220Ω 저항 (x4)
- 12V 1A 전원 어댑터 (x1)
- USB Type-C to A 케이블 (x1)
- 수-수 점퍼 와이어 (x9)
</br></br>
 
### 2.1.2 회로
- LED01
    - (+) 핀은 220Ω 저항을 통해 브레드보드의 5V 전원 레일에 연결되며, 이는 VCP-G 보드에서 공급됩니다.
    - (-) 핀은 VCP-G 보드의 47번 핀에 연결됩니다.
- LED02
    - (+) 핀은 220Ω 저항을 통해 브레드보드의 5V 전원 레일에 연결됩니다.
    - (-) 핀은 VCP-G 보드의 17번 핀에 연결됩니다.
- LED03
    - (+) 핀은 220Ω 저항을 통해 브레드보드의 5V 전원 레일에 연결됩니다.
    - (-) 핀은 VCP-G 보드의 50번 핀에 연결됩니다.
- LED04
    - (+) 핀은 220Ω 저항을 통해 브레드보드의 5V 전원 레일에 연결됩니다.
    - (-) 핀은 VCP-G 보드의 48번 핀에 연결됩니다.
 
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/vcp4LED%20Circuit%20Schematic.png"></p>
<p align="center"><strong>그림 2.1 vcp4LED 회로도</strong></p>
 
#### 2.1.2.1 핀 매핑
다음 표는 핀 매핑을 보여줍니다.
 
<p align="center"><strong>표 2.1 vcp4LED의 핀 매핑</strong></p>
<div align="center">	
	<table>
		<tr>
			<th colspan="3">핀 이름</th>
	        <th>VCP-G 보드</th>
	        <th>Arduino IDE</th>
	    </tr>
	    <tr>
	        <td colspan="3">LED01 (-) 핀</td>
	        <td>47</td>
	        <td>47</td>
	    </tr>
	        <tr>
	        <td colspan="3">LED02 (-) 핀</td>
	        <td>17</td>
	        <td>17</td>
	    </tr>
	        <tr>
	        <td colspan="3">LED03 (-) 핀</td>
	        <td>50</td>
	        <td>50</td>
	    </tr>
	        <tr>
	        <td colspan="3">LED04 (-) 핀</td>
	        <td>48</td>
	        <td>48</td>
	    </tr>
	</table>
</div>
</br></br>
 
### 2.1.3 실행 방법
1. "vcp4LED.ino" 파일을 엽니다.
    1. Arduino IDE를 엽니다.
    2. **파일 -> 예제 -> 01.VCP-G Digital -> vcp4LED**를 클릭합니다.
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
2. "vcp4LED.ino" 파일을 확인하고 VCP-G에 업로드합니다.
3. 업로드 프로세스가 무한 업로드 상태에서 멈추면 FWDN 모드가 활성화되지 않았기 때문입니다. 이 문제를 해결하려면:
    1. VCP-G 보드에서 전원 케이블을 분리합니다.
    2. FWDN 스위치를 길게 누릅니다.
    3. FWDN 스위치를 계속 누른 상태에서 전원 케이블을 다시 연결합니다.
    4. FWDN 스위치를 놓습니다.
        문제가 지속되면 관리자 권한으로 Arduino IDE를 실행해 보십시오.
4. 파일을 성공적으로 업로드한 후 Arduino IDE 출력 콘솔에서 다음 메시지를 확인합니다:
 
     **참고:** 메시지에는 **vcp4LED.ino.rom**이 포함되어야 합니다.
    ```
    [FWDN_VCP::WriteFile:577] Complete to send file - C:\Users\topst\AppData\Local\arduino\sketches\C05357299384CE5734F0E696C5A4DA3B/vcp4LED.ino.rom
 
    [main:155] Complete FWDN
    ```
 
</br></br></br>
 
## 2.2 vcp4LED_Button
---
이 예제 프로그램은 VCP-G 보드가 브레드보드의 4개 LED와 버튼을 제어하는 방법을 보여줍니다. 버튼을 누르면 오른쪽 두 개의 LED가 꺼지고 왼쪽 두 개의 LED가 켜집니다. 버튼을 놓으면 켜져 있던 LED가 꺼지고 꺼져 있던 LED가 켜집니다. 프로그램은 버튼 상태를 지속적으로 확인하고 그에 따라 LED를 조정합니다.
</br></br>
 
### 2.2.1 하드웨어 요구 사항
- VCP-G 보드 (x1)
- 브레드보드 (x1)
- LED (x4)
- 버튼 스위치 (센서) (x1)
- 220Ω 저항 (x4)
- 12V 1A 전원 어댑터 (x1)
- USB Type-C to A 케이블 (x1)
- 수-수 점퍼 와이어 (x12)
</br></br>
 
### 2.2.2 회로
1.	LED01
    - (+) 핀은 220Ω 저항을 통해 브레드보드의 5V 전원 레일에 연결되며, 이는 VCP-G 보드에서 공급됩니다.
    - (-) 핀은 VCP-G 보드의 47번 핀에 연결됩니다.
2.	LED02
    - (+) 핀은 220Ω 저항을 통해 브레드보드의 5V 전원 레일에 연결됩니다.
    - (-) 핀은 VCP-G 보드의 17번 핀에 연결됩니다.
3.	LED03
    - (+) 핀은 220Ω 저항을 통해 브레드보드의 5V 전원 레일에 연결됩니다.
    - (-) 핀은 VCP-G 보드의 50번 핀에 연결됩니다.
4.	LED04
    - (+) 핀은 220Ω 저항을 통해 브레드보드의 5V 전원 레일에 연결됩니다.
    - (-) 핀은 VCP-G 보드의 48번 핀에 연결됩니다.
5.	버튼 스위치
    - 버튼 스위치의 한쪽 다리는 VCP-G 보드의 45번 핀에 연결됩니다.
    - 버튼의 대각선 반대쪽 다리는 GND 핀에 연결됩니다.
 
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/vcp4LED_Button%20Circuit%20Schematic.png"></p>
<p align="center"><strong>그림 2.2 vcp4LED_Button 회로도</strong></p>
 
#### 2.2.2.1 핀 매핑
다음 표는 핀 매핑을 보여줍니다.
 
<p align="center"><strong>표 2.2 vcp4LED_Button의 핀 매핑</strong></p>
<div align="center">
	<table>
	    <tr>
	        <th colspan="3">핀 이름</th>
	        <th>VCP-G 보드</th>
	        <th>Arduino IDE</th>
	    </tr>
	    <tr>
	        <td colspan="3">LED01 (-) 핀</td>
	        <td>47</td>
	        <td>47</td>
	    </tr>
	        <tr>
	        <td colspan="3">LED02 (-) 핀</td>
	        <td>17</td>
	        <td>17</td>
	    </tr>
	        <tr>
	        <td colspan="3">LED03 (-) 핀</td>
	        <td>50</td>
	        <td>50</td>
	    </tr>
	        <tr>
	        <td colspan="3">LED04 (-) 핀</td>
	        <td>48</td>
	        <td>48</td>
	    </tr>
	    </tr>
	        <tr>
	        <td colspan="3">버튼의 한쪽 다리 핀</td>
	        <td>45</td>
	        <td>45</td>
	    </tr>
	</table>
</div>
</br></br>
 
### 2.1.3 실행 방법
1. "vcp4LED_Button.ino" 파일을 엽니다.
    1. Arduino IDE를 엽니다.
    2. **파일 -> 예제 -> 01.VCP-G Digital -> vcp4LED_Button**을 클릭합니다.
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
2. "vcp4LED_Button.ino" 파일을 확인하고 VCP-G에 업로드합니다.
3. 업로드 프로세스가 무한 업로드 상태에서 멈추면 FWDN 모드가 활성화되지 않았기 때문입니다. 이 문제를 해결하려면:
    1. VCP-G 보드에서 전원 케이블을 분리합니다.
    2. FWDN 스위치를 길게 누릅니다.
    3. FWDN 스위치를 계속 누른 상태에서 전원 케이블을 다시 연결합니다.
    4. FWDN 스위치를 놓습니다.
        문제가 지속되면 관리자 권한으로 Arduino IDE를 실행해 보십시오.
4. 파일을 성공적으로 업로드한 후 Arduino IDE 출력 콘솔에서 다음 메시지를 확인합니다:
 
    **참고:** 메시지에는 **vcp4LED_Button.ino.rom**이 포함되어야 합니다.
    ```
    [FWDN_VCP::WriteFile:577] Complete to send file - C:\Users\topst\AppData\Local\arduino\sketches\5CC1DB4CA216E2BC009504FAA3D06456/vcp4LED_Button.ino.rom
 
    [main:155] Complete FWDN
    ```
 
</br></br></br></br>
 
# 3. VCP-G 아날로그 핀
---
이 장에서는 VCP-G 보드의 아날로그 핀을 사용하는 예제를 제공합니다. VCP-G에서 아날로그 핀은 센서로부터 연속적인 전압 신호를 수신하여 다양한 입력 값을 정밀하게 측정할 수 있습니다. 3.1장, 3.2장, 3.3장에서는 아날로그 핀을 사용하여 센서 데이터를 읽고 출력을 제어하는 방법을 설명하여 아날로그 입력 처리에 대한 기본적인 이해를 제공합니다.
 
</br></br></br>
 
## 3.1 AnalogInOutSerial
---
이 예제 프로그램은 VCP-G 보드가 브레드보드의 가변 저항과 LED를 제어하는 방법을 보여줍니다. VCP-G는 아날로그 입력 핀에서 값을 읽고 결과를 0에서 1000 사이의 범위로 매핑한 다음 이 값을 사용하여 출력 핀(LED에 연결됨)의 펄스 폭 변조(PWM)를 설정합니다. 결과는 시리얼 모니터에도 출력됩니다.
</br></br>
 
### 3.1.1 하드웨어 요구 사항
- VCP-G 보드 (x1)
- 브레드보드 (x1)
- LED (x1)
- 가변 저항 (x1)
- 220Ω 저항 (x2)
- 12V 1A 전원 어댑터 (x1)
- USB Type-C to A 케이블 (x1)
- 수-수 점퍼 와이어 (x4)
</br></br>
 
### 3.1.2 회로
- 가변 저항
    - 가변 저항의 중앙 핀은 VCP-G 보드의 아날로그 핀 A5에 연결됩니다.
    - 가변 저항의 GND 핀은 VCP-G 보드의 43번 핀에 연결되고 220Ω 저항을 통해 VCP-G 보드의 GND 핀에 연결됩니다.
- LED
    - LED의 (+) 핀은 220Ω 저항을 통해 VCP-G 보드의 3.3V에 연결됩니다.
    - LED의 (-) 핀은 가변 저항의 중앙 핀에 연결됩니다.
 
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/AnalogInOutSerial%20Circuit%20Schematic.png"></p>
<p align="center"><strong>그림 3.1 AnalogInOutSerial 회로도</strong></p>
 
#### 3.1.2.1 핀 매핑
다음 표는 핀 매핑을 보여줍니다.
 
<p align="center"><strong>표 3.1 AnalogInOutSerial의 핀 매핑</strong></p>
<div align="center">
	<table>
	    <tr>
	        <th colspan="3">핀 이름</th>
	        <th>VCP-G 보드</th>
	        <th>Arduino IDE</th>
	    </tr>
	    <tr>
	        <td colspan="3">가변 저항 중앙 핀</td>
	        <td>A5</td>
	        <td>-</td>
	    </tr>
	        <tr>
	        <td colspan="3">가변 저항 GND 핀</td>
	        <td>43</td>
	        <td>43</td>
	    </tr>
	        <tr>
	        <td colspan="3">LED (+) 핀</td>
	        <td>3.3V</td>
	        <td>-</td>
	    </tr>
	        <tr>
	        <td colspan="3">LED (-) 핀</td>
	        <td>A5</td>
	        <td>A5</td>
	    </tr>
	</table>
</div>
</br></br>
 
### 3.1.3 실행 방법
1. "AnalogInOutSerial.ino" 파일을 엽니다.
    1. Arduino IDE를 엽니다.
    2. **파일 -> 예제 -> 02.VCP-G Analog -> AnalogInOutSerial**을 클릭합니다.
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
 
    **참고:** "Serial"이 선언되지 않았다는 오류가 발생하면 다음 라이브러리 및 객체 선언이 올바르게 포함되었는지 확인하십시오.
    ```
    #include <HardwareSerial.h>
    HardwareSerial Serial;
    ```
2. "AnalogInOutSerial.ino" 파일을 확인하고 VCP-G에 업로드합니다.
3. 업로드 프로세스가 무한 업로드 상태에서 멈추면 FWDN 모드가 활성화되지 않았기 때문입니다. 이 문제를 해결하려면:
    1. VCP-G 보드에서 전원 케이블을 분리합니다.
    2. FWDN 스위치를 길게 누릅니다.
    3. FWDN 스위치를 계속 누른 상태에서 전원 케이블을 다시 연결합니다.
    4. FWDN 스위치를 놓습니다.
        문제가 지속되면 관리자 권한으로 Arduino IDE를 실행해 보십시오.
4. 파일을 성공적으로 업로드한 후 Arduino IDE 출력 콘솔에서 다음 메시지를 확인합니다:
 
    **참고:** 메시지에는 **AnalogInOutSerial.ino.rom**이 포함되어야 합니다.
    ```
    [FWDN_VCP::WriteFile:577] Complete to send file - C:\Users\topst\AppData\Local\arduino\sketches\EB016432EF98DEF0B9102FD77148DD5D/AnalogInOutSerial.ino.rom
 
    [main:155] Complete FWDN
    ```
 
</br></br></br>
 
## 3.2 AnalogInput
---
이 예제 프로그램은 VCP-G 보드가 브레드보드의 가변 저항과 LED를 제어하는 방법을 보여줍니다. 아날로그 입력 핀에서 값을 읽고 이 값을 사용하여 LED를 제어합니다. 센서 값이 3000보다 낮으면 LED가 켜집니다. 센서 값이 3000 이상이면 LED가 꺼집니다.
</br></br>
 
### 3.2.1 하드웨어 요구 사항
- VCP-G 보드 (x1)
- 브레드보드 (x1)
- LED (x1)
- 가변 저항 (x1)
- 220Ω 저항 (x1)
- 12V 1A 전원 어댑터 (x1)
- USB Type-C to A 케이블 (x1)
- 수-수 점퍼 와이어 (x6)
</br></br>
 
### 3.2.2 회로
- 가변 저항
    - 가변 저항의 VCC 핀은 220Ω 저항을 통해 VCP-G 보드의 3.3V에 연결됩니다.
    - 가변 저항의 중앙 핀은 VCP-G 보드의 아날로그 핀 A5에 연결됩니다.
    - 가변 저항의 GND 핀은 220Ω 저항을 통해 VCP-G 보드의 GND 핀에 연결됩니다.
- LED
    - LED의 (+) 핀은 220Ω 저항을 통해 VCP-G 보드의 3.3V에 연결됩니다.
    - LED의 (-) 핀은 VCP-G 보드의 5번 핀에 연결됩니다.
 
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/AnalogInput%20Circuit%20Schematic.png"></p>
<p align="center"><strong>그림 3.2 AnalogInput 회로도</strong></p>
 
#### 3.2.2.1 핀 매핑
다음 표는 핀 매핑을 보여줍니다.
 
<p align="center"><strong>표 3.2 AnalogInput의 핀 매핑</strong></p>
<div align="center">
	<table>
	    <tr>
	        <th colspan="3">핀 이름</th>
	        <th>VCP-G 보드</th>
	        <th>Arduino IDE</th>
	    </tr>
	    <tr>
	        <td colspan="3">가변 저항 VCC 핀</td>
	        <td>3.3V</td>
	        <td>-</td>
	    </tr>
	    <tr>
	        <td colspan="3">가변 저항 중앙 핀</td>
	        <td>A5</td>
	        <td>A5</td>
	    </tr>
	        <tr>
	        <td colspan="3">가변 저항 GND 핀</td>
	        <td>GND</td>
	        <td>-</td>
	    </tr>
	        <tr>
	        <td colspan="3">LED (+) 핀</td>
	        <td>3.3V</td>
	        <td>-</td>
	    </tr>
	        <tr>
	        <td colspan="3">LED (-) 핀</td>
	        <td>5</td>
	        <td>5</td>
	    </tr>
	</table>
</div>
</br></br>
 
### 3.2.3 실행 방법
1. "AnalogInput.ino" 파일을 엽니다.
    1. Arduino IDE를 엽니다.
    2. **파일 -> 예제 -> 02.VCP-G Analog -> AnalogInput**을 클릭합니다.
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
 
    **참고 1:** 시리얼 모니터에서 **sensorValue**를 확인하려면 소스 코드에 **Serial.println()**을 추가하십시오.
    **참고 2:** 고정 저항은 가변 저항(포텐쇼미터)과 함께 사용하여 센서 값을 조정합니다. 센서 값은 가변 저항을 얼마나 돌리느냐에 따라 달라지며, 가변 저항을 돌려야 하는 양은 고정 저항의 값에 따라 다릅니다.

2. "AnalogInput.ino" 파일을 확인하고 VCP-G에 업로드합니다.
3. 업로드 프로세스가 무한 업로드 상태에서 멈추면 FWDN 모드가 활성화되지 않았기 때문입니다. 이 문제를 해결하려면:
    1. VCP-G 보드에서 전원 케이블을 분리합니다.
    2. FWDN 스위치를 길게 누릅니다.
    3. FWDN 스위치를 계속 누른 상태에서 전원 케이블을 다시 연결합니다.
    4. FWDN 스위치를 놓습니다.
        문제가 지속되면 관리자 권한으로 Arduino IDE를 실행해 보십시오.
4. 파일을 성공적으로 업로드한 후 Arduino IDE 출력 콘솔에서 다음 메시지를 확인합니다:
 
    **참고:** 메시지에는 **AnalogInput.ino.rom**이 포함되어야 합니다.
    ```
    [FWDN_VCP::WriteFile:577] Complete to send file - C:\Users\topst\AppData\Local\arduino\sketches\C3FDEE51354320EA689DFEB4EDCF2ECD/AnalogInput.ino.rom
 
    [main:155] Complete FWDN
    ```
 
</br></br></br>
 
## 3.3 pwmFade
---
이 예제 프로그램은 VCP-G 보드가 PWM을 사용하여 루프에서 밝기를 점차 높이거나 낮추어 브레드보드의 LED를 제어하는 방법을 보여줍니다. LED가 최대 밝기에 도달하면 LED의 밝기가 감소하기 시작합니다. 프로그램은 LED의 밝기를 지속적으로 조정하여 페이딩 효과를 만듭니다.
</br></br>
 
### 3.3.1 하드웨어 요구 사항
- VCP-G 보드 (x1)
- 브레드보드 (x1)
- LED (x1)
- 220Ω 저항 (x1)
- 12V 1A 전원 어댑터 (x1)
- USB Type-C to A 케이블 (x1)
- 수-수 점퍼 와이어 (x2)
</br></br>
 
### 3.3.2 회로
- LED
    - LED의 (+) 핀은 VCP-G 보드의 5V에 연결됩니다.
    - LED의 (-) 핀은 220Ω 저항을 통해 VCP-G 보드의 9번 핀에 연결됩니다.
 
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/pwmFade%20Circuit%20Schematic.png"></p>
<p align="center"><strong>그림 3.3 pwmFade 회로도</strong></p>
 
#### 3.3.2.1 핀 매핑
다음 표는 핀 매핑을 보여줍니다.
 
<p align="center"><strong>표 3.3 pwmFade의 핀 매핑</strong></p>
<div align="center">
	<table>
	    <tr>
	        <th colspan="3">핀 이름</th>
	        <th>VCP-G 보드</th>
	        <th>Arduino IDE</th>
	    </tr>
	    <tr>
	        <td colspan="3">LED (+) 핀</td>
	        <td>5V</td>
	        <td>-</td>
	    </tr>
	        <tr>
	        <td colspan="3">LED (-) 핀</td>
	        <td>9</td>
	        <td>9</td>
	    </tr>
	</table>
</div>
</br></br>
 
### 3.3.3 실행 방법
1. "pwmFade.ino" 파일을 엽니다.
    1. Arduino IDE를 엽니다.
    2. **파일 -> 예제 -> 02.VCP-G Analog -> pwmFade**를 클릭합니다.
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
2. "pwmFade.ino" 파일을 확인하고 VCP-G 보드에 업로드합니다.
3. 업로드 프로세스가 무한 업로드 상태에서 멈추면 FWDN 모드가 활성화되지 않았기 때문입니다. 이 문제를 해결하려면:
    1. VCP-G 보드에서 전원 케이블을 분리합니다.
    2. FWDN 스위치를 길게 누릅니다.
    3. FWDN 스위치를 계속 누른 상태에서 전원 케이블을 다시 연결합니다.
    4. FWDN 스위치를 놓습니다.
        문제가 지속되면 관리자 권한으로 Arduino IDE를 실행해 보십시오.
4. 파일을 성공적으로 업로드한 후 Arduino IDE 출력 콘솔에서 다음 메시지를 확인합니다:
 
     **참고:** 메시지에는 **pwmFade.ino.rom**이 포함되어야 합니다.
    ```
    [FWDN_VCP::WriteFile:577] Complete to send file - C:\Users\topst\AppData\Local\arduino\sketches\69446E8A7F6616A7D5466014BDF759FC/pwmFade.ino.rom 
 
    [main:155] Complete FWDN
    ```
 
</br></br></br></br>
 
# 4. VCP SPI
---
이 장에서는 VCP-G에서 SPI(Serial Peripheral Interface) 통신을 구성하는 지침을 제공합니다.
SPI는 마이크로컨트롤러와 주변 장치 간에 데이터를 교환하는 데 사용되는 고속 동기식 통신 프로토콜입니다. 데이터 전송(MOSI 및 MISO), 클록 동기화(SCK) 및 장치 선택(SS)을 위한 별도의 라인으로 작동하여 효율적이고 안정적인 통신을 보장합니다.
다음 장에서는 SPI를 설정하고 사용하여 외부 장치와 인터페이스하는 방법을 설명합니다.
 
</br></br></br>
 
## 4.1 vcpSPI_Dot8x8
---
이 예제 프로그램은 VCP-G 보드가 MAX7219 드라이버를 사용하여 8x8 LED 도트 매트릭스를 제어하는 방법을 보여줍니다. 8x8 LED 도트 매트릭스는 미리 정의된 이진 배열로 행을 설정하여 하트 모양 및 문자 "R"과 같은 패턴을 표시합니다. LED의 강도는 펄싱 효과를 생성하도록 조정되어 동적 시각 효과를 추가합니다. 추가 기능으로 디스플레이 반전 및 지우기가 포함되어 기능을 향상시킵니다.
</br></br>
 
### 4.1.1 하드웨어 요구 사항
- VCP-G 보드 (x1)
- 8x8 도트 매트릭스 (x1)
- 12V 1A 전원 어댑터 (x1)
- USB Type-C to A 케이블 (x1)
- 수-암 점퍼 와이어 (x5)
</br></br>
 
### 4.1.2 회로
- 8x8 도트 매트릭스
    - 8x8 도트 매트릭스의 VCC 핀은 VCP-G 보드의 아날로그 핀 5V에 연결됩니다.
    - 8x8 도트 매트릭스의 GND 핀은 VCP-G 보드의 GND에 연결됩니다.
    - 8x8 도트 매트릭스의 DIN 핀은 VCP-G 보드의 11번 핀에 연결됩니다.
    - 8x8 도트 매트릭스의 CS 핀은 VCP-G 보드의 10번 핀에 연결됩니다.
    - 8x8 도트 매트릭스의 CLS 핀은 VCP-G 보드의 13번 핀에 연결됩니다.
 
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/vcpSPI_Dot8x8%20Circuit%20Schematic.png"></p>
<p align="center"><strong>그림 4.1 vcpSPI_Dot8x8 회로도</strong></p>
 
#### 4.1.2.1 핀 매핑
다음 표는 핀 매핑을 보여줍니다.
 
<p align="center"><strong>표 4.1 vcpSPI_Dot8x8의 핀 매핑</strong></p>
<div align="center">
	<table>
	    <tr>
	        <th colspan="3">핀 이름</th>
	        <th>VCP-G 보드</th>
	        <th>Arduino IDE</th>
	    </tr>
	    <tr>
	        <td colspan="3">8x8 도트 매트릭스 VCC 핀</td>
	        <td>5V</td>
	        <td>-</td>
	    </tr>
	        <tr>
	        <td colspan="3">8x8 도트 매트릭스 GND 핀</td>
	        <td>GND</td>
	        <td>-</td>
	    </tr>
	    <tr>
	        <td colspan="3">8x8 도트 매트릭스 DIN 핀</td>
	        <td>11</td>
	        <td>11</td>
	    </tr>
	    <tr>
	        <td colspan="3">8x8 도트 매트릭스 CS 핀</td>
	        <td>10</td>
	        <td>10</td>
	    </tr>
	    <tr>
	        <td colspan="3">8x8 도트 매트릭스 CLK 핀</td>
	        <td>13</td>
	        <td>13</td>
	    </tr>
	</table>
</div>
</br></br>
 
### 4.1.3 실행 방법
1. "vcpSPI_Dot8x8.ino" 파일을 엽니다.
    1. Arduino IDE를 엽니다.
    2. **파일 -> 예제 -> 03.VCP-G SPI -> vcpSPI_Dot8x8**을 클릭합니다.
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
2. "vcpSPI_Dot8x8.ino" 파일을 확인하고 VCP-G에 업로드합니다.
3. 업로드 프로세스가 무한 업로드 상태에서 멈추면 FWDN 모드가 활성화되지 않았기 때문입니다. 이 문제를 해결하려면:
    1. VCP-G 보드에서 전원 케이블을 분리합니다.
    2. FWDN 스위치를 길게 누릅니다.
    3. FWDN 스위치를 계속 누른 상태에서 전원 케이블을 다시 연결합니다.
    4. FWDN 스위치를 놓습니다.
        문제가 지속되면 관리자 권한으로 Arduino IDE를 실행해 보십시오.
4. 파일을 성공적으로 업로드한 후 Arduino IDE 출력 콘솔에서 다음 메시지를 확인합니다:
 
    **참고:** 메시지에는 **vcpSPI_Dot8x8.ino.rom**이 포함되어야 합니다.
    ```
    [FWDN_VCP::WriteFile:577] Complete to send file - C:\Users\topst\AppData\Local\arduino\sketches\567805554B5B9F915DCC80B38483AE07/vcpSPI_Dot8x8.ino.rom
 
    [main:155] Complete FWDN
    ```
 
**참고:** VCP-G 보드 중앙의 SPI 핀을 사용하려면 다음 핀 번호를 참조하여 사용할 수 있습니다.
<p align="center"><strong>표 4.2 VCP-G 중앙 SPI 핀 매핑</strong></p>
<div align="center">
	<table>
	    <tr>
	        <th colspan="3">핀 번호</th>
	        <th>SPI 기능</th>
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
이 장에서는 VCP-G에서 I2C(Inter-integrated Circuit) 통신을 구성하는 지침을 제공합니다.
I2C는 여러 장치 간의 효율적인 데이터 교환을 위해 설계된 2선식 동기 통신 프로토콜입니다. 직렬 데이터 라인(SDA)과 직렬 클록 라인(SCL)으로 작동하여 여러 주변 장치가 고유 주소를 사용하여 마이크로컨트롤러와 통신할 수 있습니다. I2C는 마스터-슬레이브 통신과 멀티 마스터 구성을 모두 지원하므로 필요한 연결 수를 최소화하면서 센서, 디스플레이 및 기타 저속 장치를 연결하는 데 이상적입니다.
 
</br></br></br>
 
## 5.1 vcpI2C_LCD1602
---
이 예제 프로그램은 VCP-G 보드가 I2C 통신 프로토콜을 사용하여 LCD1602 디스플레이를 제어하는 방법을 보여줍니다. LCD1602는 임베디드 시스템 프로젝트에서 일반적으로 사용되는 16자 2줄 액정 디스플레이입니다. LiquidCrystal_I2C 라이브러리를 활용하여 보드는 I2C 버스를 통해 명령과 데이터를 전송하여 디스플레이를 효율적으로 제어합니다.
 
이 예제에서는 LCD가 초기화되고 명확한 가시성을 위해 백라이트가 활성화됩니다. 그런 다음 프로그램은 커서를 첫 번째 행에 "VCP-G" 텍스트를 표시하고 두 번째 행에 "I2C Test!"를 표시하도록 위치시킵니다. I2C 통신을 사용하면 최소한의 배선으로 여러 장치를 제어할 수 있어 소형 프로젝트에 효과적인 솔루션입니다.
</br></br>
 
### 5.1.1 하드웨어 요구 사항
- VCP-G 보드 (x1)
- LCD1602 (x1)
- 12V 1A 전원 어댑터 (x1)
- USB Type-C to A 케이블 (x1)
- 수-암 점퍼 와이어 (x4)
</br></br>
 
### 5.1.2 회로
- LCD1602
    - LCD1602의 VCC 핀은 VCP-G 보드의 아날로그 핀 5V에 연결됩니다.
    - LCD1602의 GND 핀은 VCP-G 보드의 GND에 연결됩니다.
    - LCD1602의 SDA 핀은 VCP-G 보드의 48번 핀에 연결됩니다.
    - LCD1602의 SCL 핀은 VCP-G 보드의 49번 핀에 연결됩니다.
 
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/vcpI2C_LCD1602%20Circuit%20Schematic.png"></p>
<p align="center"><strong>그림 5.1 vcpI2C_LCD1602 회로도</strong></p>
 
#### 5.1.2.1 핀 매핑
다음 표는 핀 매핑을 보여줍니다.
 
<p align="center"><strong>표 5.1 vcpI2C_LCD1602의 핀 매핑</strong></p>
<div align="center">
	<table>
	    <tr>
	        <th colspan="3">핀 이름</th>
	        <th>VCP-G 보드</th>
	        <th>Arduino IDE</th>
	    </tr>
	    <tr>
	        <td colspan="3">LCD1602 VCC 핀</td>
	        <td>5V</td>
	        <td>-</td>
	    </tr>
	        <tr>
	        <td colspan="3">LCD1602 GND 핀</td>
	        <td>GND</td>
	        <td>-</td>
	    </tr>
	    <tr>
	        <td colspan="3">LCD1602 SDA 핀</td>
	        <td>48</td>
	        <td>-</td>
	    </tr>
	    <tr>
	        <td colspan="3">LCD1602 SCL 핀</td>
	        <td>49</td>
		    <td>-</td>
	    </tr>
	</table>
</div>
 
</br></br>
 
### 5.1.3 실행 방법
1. "vcpI2C_LCD1602.ino" 파일을 엽니다.
    1. Arduino IDE를 엽니다.
    2. **파일 -> 예제 -> 04.VCP-G I2C -> vcpI2C_LCD1602**를 클릭합니다.
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
2. "vcpI2C_LCD1602.ino" 파일을 확인하고 VCP-G에 업로드합니다.
3. 업로드 프로세스가 무한 업로드 상태에서 멈추면 FWDN 모드가 활성화되지 않았기 때문입니다. 이 문제를 해결하려면:
    1. VCP-G 보드에서 전원 케이블을 분리합니다.
    2. FWDN 스위치를 길게 누릅니다.
    3. FWDN 스위치를 계속 누른 상태에서 전원 케이블을 다시 연결합니다.
    4. FWDN 스위치를 놓습니다.
        문제가 지속되면 관리자 권한으로 Arduino IDE를 실행해 보십시오.
4. 파일을 성공적으로 업로드한 후 Arduino IDE 출력 콘솔에서 다음 메시지를 확인합니다:
   
    **참고:** 메시지에는 **vcpI2C_LCD1602.ino.rom**이 포함되어야 합니다.
    ```
    [FWDN_VCP::WriteFile:577] Complete to send file -         C:\Users\topst\AppData\Local\arduino\sketches\C8D91A6857B651D6C665B0EF18B7EE53/vcpI2C_LCD1602.ino.rom
 
    [main:155] Complete FWDN
    ```
 
</br></br></br></br>
 
# 6. VCP-G UART
---
이 장에서는 VCP-G에서 UART(Universal Asynchronous Receiver-Transmitter) 통신을 구성하는 지침을 제공합니다.
UART는 송신(TX)과 수신(RX)의 두 라인만 사용하여 데이터를 비동기적으로 전송하는 널리 사용되는 직렬 통신 프로토콜입니다. 공유 클록 신호 없이 마이크로컨트롤러, 센서 및 컴퓨터 간에 데이터를 교환하는 데 필수적입니다.
다음 장에서는 UART를 통해 데이터를 송수신하는 방법을 설명합니다.
 
</br></br></br>
 
## 6.1 vcpASCIITable
---
이 예제 프로그램은 VCP-G가 10진수, 16진수, 8진수 및 2진수와 같은 다양한 형식으로 문자의 ASCII 값을 인쇄하는 방법을 보여줍니다. 문자 '!'(ASCII 값 33)부터 시작하여 모든 표시 가능한 ASCII 문자를 증가시키며 각 문자를 다른 형식으로 인쇄합니다. 프로그램은 문자 '~'(ASCII 값 126)에 도달할 때까지 계속됩니다.
</br></br>
 
### 6.1.1 하드웨어 요구 사항
- VCP-G 보드 (x1)
- 12V 1A 전원 어댑터 (x1)
- USB Type-C to A 케이블 (x1)
</br></br>
 
### 6.1.3 실행 방법
1. "vcpASCIITable.ino" 파일을 엽니다.
    1. Arduino IDE를 엽니다.
    2. **파일 -> 예제 -> 05.VCP-G UART -> vcpASCIITable**을 클릭합니다.
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
2. "vcpASCIITable.ino" 파일을 확인하고 VCP-G에 업로드합니다.
3. 업로드 프로세스가 무한 업로드 상태에서 멈추면 FWDN 모드가 활성화되지 않았기 때문입니다. 이 문제를 해결하려면:
    1. VCP-G 보드에서 전원 케이블을 분리합니다.
    2. FWDN 스위치를 길게 누릅니다.
    3. FWDN 스위치를 계속 누른 상태에서 전원 케이블을 다시 연결합니다.
    4. FWDN 스위치를 놓습니다.
        문제가 지속되면 관리자 권한으로 Arduino IDE를 실행해 보십시오.
4. 파일을 성공적으로 업로드한 후 Arduino IDE 출력 콘솔에서 다음 메시지를 확인합니다:
 
    **참고:** 메시지에는 **vcpASCIITable.ino.rom**이 포함되어야 합니다.
    ```
    [FWDN_VCP::WriteFile:577] Complete to send file - C:\Users\topstAppData\Local\arduino\sketches\487F45098412336AA9D73C50C17E07D8/vcpASCIITable.ino.rom
 
    [main:155] Complete FWDN
    ```
 
</br></br></br>
 
## 6.2 vcpGraph
---
이 예제 프로그램은 VCP-G가 브레드보드의 가변 저항 아날로그 값을 읽고 데이터를 UART를 통해 호스트 PC로 전송하는 방법을 보여줍니다. Arduino 코드는 핀 A5에 연결된 아날로그 센서(가변 저항)의 값을 지속적으로 읽고 시리얼 포트를 통해 전송합니다. 함께 제공되는 프로세싱 코드는 이러한 값을 실시간으로 동적 그래프로 시각화하여 시간 경과에 따른 센서 입력의 변화를 보여줍니다.
</br></br>
 
### 6.2.1 하드웨어 요구 사항
- VCP-G 보드 (x1)
- 브레드보드 (x1)
- 가변 저항 (x1)
- 10 kΩ 저항 (x1)
- 12V 1A 전원 어댑터 (x1)
- USB Type-C to A 케이블 (x1)
- 수-수 점퍼 와이어 (x4)
</br></br>
 
### 6.2.2 회로
- 가변 저항
    - 가변 저항의 중앙 핀은 VCP-G 보드의 아날로그 핀 A5에 연결됩니다.
    - 가변 저항의 GND 핀은 10 kΩ 저항을 통해 VCP-G 보드의 GND에 연결됩니다.
    - 가변 저항의 VCC 핀은 VCP-G 보드의 3.3V에 연결됩니다.
 
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/vcpGraph%20Circuit%20Schematic.png"></p>
<p align="center"><strong>그림 6.1 vcpGraph 회로도</strong></p>
 
#### 6.2.2.1 핀 매핑
다음 표는 핀 매핑을 보여줍니다.
 
<p align="center"><strong>표 6.1 vcpGraph의 핀 매핑</strong></p>
<div align="center">
	<table>
	    <tr>
	        <th colspan="3">핀 이름</th>
	        <th>VCP-G 보드</th>
	        <th>Arduino IDE</th>
	    </tr>
	    <tr>
	        <td colspan="3">가변 저항 중앙 핀</td>
	        <td>A5</td>
	        <td>A5</td>
	    </tr>
	        <tr>
	        <td colspan="3">가변 저항 GND 핀</td>
	        <td>GND</td>
	        <td>-</td>
	    </tr>
	    <tr>
	        <td colspan="3">가변 저항 VCC 핀</td>
	        <td>3.3V</td>
	        <td>-</td>
	    </tr>
	</table>
</div>
</br></br>
 
### 6.2.3 실행 방법
1. "vcpGraph.ino" 파일을 엽니다.
    1. Arduino IDE를 엽니다.
    2. **파일 -> 예제 -> 05.VCP-G UART -> vcpGraph**를 클릭합니다.
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
        If the issue persists, try running the Arduino IDE with administrator privileges.
4. After successfully uploading the file, check the Arduino IDE output console for the following message:

    **Note:** The message should include **vcpGraph.ino.rom**.
    ```
    [FWDN_VCP::WriteFile:577] Complete to send file - C:\Users\topst\AppData\Local\arduino\sketches\F59E4532EC3A529F5910F376F809A5E5/vcpGraph.ino.rom

    [main:155] Complete FWDN
    ```

</br></br></br></br>

# 7. 추가 예제
---
이 장에서는 Arduino IDE의 "Examples for TOPST VCP Rev G"에 포함되지 않은 추가 센서 예제를 제공합니다.
VCP-G 보드와 함께 일반적으로 사용되는 Arduino 센서를 사용하는 예제 가이드를 제공하여 다양한 센서를 프로젝트에 효과적으로 통합할 수 있도록 합니다.

</br></br></br>

## 7.1 적외선(IR) 센서 (트랜시버)
---
### 7.1.1 적외선(IR) 센서 1
---
이 예제는 VCP-G 보드가 브레드보드의 IR 센서와 두 개의 LED를 제어하는 방법을 보여줍니다. IR 센서 값을 읽은 후 IR 센서 값이 HIGH이면 장애물이 없는 것으로 간주하여 녹색 LED가 켜지고 빨간색 LED가 꺼집니다. 반대로 IR 센서 값이 LOW이면 장애물이 있는 것으로 간주하여 빨간색 LED가 켜지고 녹색 LED가 꺼집니다. 또한 장애물의 유무가 시리얼 모니터에 표시됩니다.

#### 7.1.1.1 하드웨어 요구 사항
- VCP-G 보드 (x1)
- 브레드보드 (x1)
- IR 트랜시버 센서 (x1)
- LED (x2: 다른 색상 권장)
- 220Ω 저항 (x2)
- 12V 1A 전원 어댑터 (x1)
- USB Type-C to A 케이블 (x1)
- 수-수 점퍼 와이어 (x4)
- 수-암 점퍼 와이어 (x3)

#### 7.1.1.2 회로
- IR 트랜시버 센서
    - IR 센서의 OUT 핀은 VCP-G 보드의 50번 핀에 연결됩니다.
    - IR 센서의 VCC 핀은 VCP-G 보드의 5V에 연결됩니다.
    - IR 센서의 GND 핀은 VCP-G 보드의 GND에 연결됩니다.
- 빨간색 LED
    - LED의 (-)는 저항에 연결되고 저항은 VCP-G 보드의 GND에 연결됩니다.
    - LED의 (+)는 VCP-G 보드의 48번 핀에 연결됩니다.
- 녹색 LED
    - LED의 (-)는 저항에 연결되고 저항은 VCP-G 보드의 GND에 연결됩니다.
    - LED의 (+)는 VCP-G 보드의 17번 핀에 연결됩니다.

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/Infrared%20(IR)%20Sensor%20Circuit%20Schematic.png"></p>
<p align="center"><strong>그림 7.1 적외선(IR) 센서 회로도</strong></p>

##### 7.1.1.2.1 핀 매핑
다음 표는 핀 매핑을 보여줍니다.

<p align="center"><strong>표 7.1 irSensor_LED의 핀 매핑</strong></p>
<div align="center">
	<table>
	    <tr>
	        <th colspan="3">핀 이름</th>
	        <th>VCP-G 보드</th>
	        <th>Arduino IDE</th>
	    </tr>
	    <tr>
	        <td colspan="3">IR 센서 OUT 핀 </td>
	        <td>50</td>
	        <td>50</td>
	    </tr>
	        <tr>
	        <td colspan="3">IR 센서 VCC 핀 </td>
	        <td>5V</td>
	        <td>-</td>
	    </tr>
	    <tr>
	        <td colspan="3">IR 센서 GND 핀</td>
	        <td>GND</td>
	        <td>-</td>
	    </tr>
	    <tr>
	        <td colspan="3">빨간색 LED (+) 핀</td>
	        <td>48</td>
	        <td>48</td>
	    </tr>
	    <tr>
	        <td colspan="3">빨간색 LED (-) 핀</td>
	        <td>GND</td>
	        <td>-</td>
	    </tr>
	    <tr>
	        <td colspan="3">녹색 LED (+) 핀</td>
	        <td>17</td>
	        <td>17</td>
	    </tr>
	    <tr>
	        <td colspan="3">녹색 LED (-) 핀 </td>
	        <td>GND</td>
	        <td>-</td>
	    </tr>
	</table>
</div>

#### 7.1.1.3 실행 방법
1. 다음 소스 코드를 Arduino IDE에 복사하고 파일을 "irSensor_LED.ino"로 저장합니다.
    
   **참고:** 다음 소스 코드는 이 문서에서만 제공됩니다.
 
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
2. "irSensor_LED.ino" 파일을 확인하고 VCP-G에 업로드합니다.
3. 업로드 프로세스가 무한 업로드 상태에서 멈추면 FWDN 모드가 활성화되지 않았기 때문입니다. 이 문제를 해결하려면:
    1. VCP-G 보드에서 전원 케이블을 분리합니다.
    2. FWDN 스위치를 길게 누릅니다.
    3. FWDN 스위치를 계속 누른 상태에서 전원 케이블을 다시 연결합니다.
    4. FWDN 스위치를 놓습니다.
        문제가 지속되면 관리자 권한으로 Arduino IDE를 실행해 보십시오.
4. 파일을 성공적으로 업로드한 후 Arduino IDE 출력 콘솔에서 다음 메시지를 확인합니다:
 
    **참고:** 메시지에는 **irSensor_LED.ino.rom**이 포함되어야 합니다.
    ```
    [FWDN_VCP::WriteFile:577] Complete to send file - C:\Users\topst\AppData\Local\arduino\sketches\1D003A72AB3391D6D60FD7993380F8CD/irSensor_LED.ino.rom 
 
    [main:155] Complete FWDN
    ```
</br></br>
 
### 7.1.2 적외선(IR) 센서 2
---
이 예제는 VCP-G 보드가 IR 센서를 제어하여 물체를 감지하고 감지 상태를 시리얼 모니터에 인쇄하는 방법을 보여줍니다. IR 트랜시버는 장애물의 존재를 읽습니다. IR 트랜시버 값이 HIGH이면 장애물이 없음을 나타내며 녹색 LED가 켜지고 빨간색 LED가 꺼집니다. 반대로 IR 트랜시버 값이 LOW이면 장애물이 있음을 나타내며 빨간색 LED가 켜지고 녹색 LED가 꺼집니다. 또한 장애물의 유무가 시리얼 모니터에 표시됩니다.
 
#### 7.1.2.1 하드웨어 요구 사항
- VCP-G 보드 (x1)
- IR 트랜시버 센서 (x1)
- 12V 1A 전원 어댑터 (x1)
- USB Type-C to A 케이블 (x1)
- 수-암 점퍼 와이어 (x3)
 
#### 7.1.2.2 회로
- IR 트랜시버 센서
    - IR 트랜시버 센서의 Out 핀은 VCP-G 보드의 8번 핀에 연결됩니다.
    - IR 트랜시버 센서의 VCC 핀은 VCP-G 보드의 5V에 연결됩니다.
    - IR 트랜시버 센서의 GND 핀은 VCP-G 보드의 GND에 연결됩니다.
 
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/Infrared%20(IR)%20Sensor%20(Transceiver)%20Circuit%20Schematic.png"></p>
<p align="center"><strong>그림 7.2 적외선(IR) 센서 (트랜시버) 회로도</strong></p>
 
##### 7.1.2.2.1 핀 매핑
다음 표는 핀 매핑을 보여줍니다.
 
<p align="center"><strong>표 7.2 irTransceiver의 핀 매핑</strong></p>
<div align="center">
	<table>
	    <tr>
	        <th colspan="3">핀 이름</th>
	        <th>VCP-G 보드</th>
	        <th>Arduino IDE</th>
	    </tr>
	    <tr>
	        <td colspan="3">IR 트랜시버 센서 OUT 핀</td>
	        <td>8</td>
	        <td>8</td>
	    </tr>
	    <tr>
	        <td colspan="3">IR 트랜시버 센서 VCC 핀</td>
	        <td>5V</td>
	        <td>-</td>
	    </tr>
	    <tr>
	        <td colspan="3">IR 트랜시버 센서 GND 핀</td>
	        <td>GND</td>
	        <td>-</td>
	    </tr>
	</table>
</div>
 
#### 7.1.2.3 실행 방법
1. 다음 소스 코드를 Arduino IDE에 복사하고 파일을 "irTransceiver.ino"로 저장합니다.
   
   **참고:** 다음 소스 코드는 이 문서에서만 제공됩니다.
 
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
2. "irTransceiver.ino" 파일을 확인하고 VCP-G에 업로드합니다.
3. 업로드 프로세스가 무한 업로드 상태에서 멈추면 FWDN 모드가 활성화되지 않았기 때문입니다. 이 문제를 해결하려면:
    1. VCP-G 보드에서 전원 케이블을 분리합니다.
    2. FWDN 스위치를 길게 누릅니다.
    3. FWDN 스위치를 계속 누른 상태에서 전원 케이블을 다시 연결합니다.
    4. FWDN 스위치를 놓습니다.
        문제가 지속되면 관리자 권한으로 Arduino IDE를 실행해 보십시오.
4. 파일을 성공적으로 업로드한 후 Arduino IDE 출력 콘솔에서 다음 메시지를 확인합니다:
   
    **참고:** 메시지에는 **irTransceiver.ino.rom**이 포함되어야 합니다.
    ```
    [FWDN_VCP::WriteFile:577] Complete to send file - C:\Users\topst\AppData\Local\arduino\sketches\1D003A72AB3391D6D60FD7993380F8CD/irTransceiver.ino.rom 
 
    [main:155] Complete FWDN
    ```
 
</br></br></br>
 
## 7.2 조이스틱
---
이 예제는 VCP-G가 조이스틱 입력을 읽고 그 값을 시리얼 모니터에 표시하는 방법을 보여줍니다. X축, Y축 및 버튼의 세 가지 입력을 받을 수 있습니다. 시리얼 모니터는 수신된 신호를 확인합니다. X축과 Y축에서 이루어진 움직임은 포트 값을 변경하며, 이는 아날로그 출력의 숫자 값에 해당합니다. 이를 통해 미세 조정이 필요한 애플리케이션을 정밀하게 제어할 수 있습니다.
 
**참고:** 듀얼 축 조이스틱 모듈(KY-023)은 Joy-IT의 제품입니다. 디자인, 상표 및 관련 지적 재산권에 대한 모든 권리는 Joy-IT에 있습니다.
</br></br>
 
### 7.2.1 하드웨어 요구 사항
- VCP-G 보드 (x1)
- 듀얼 축 조이스틱 모듈 (KY-023) (x1)
- 12V 1A 전원 어댑터 (x1)
- USB Type-C to A 케이블 (x1)
- 수-암 점퍼 와이어 (x5)
</br></br>
 
### 7.2.2 회로
- KY-023 (듀얼 축 조이스틱 모듈)
    - KY-023의 5V 핀은 VCP-G 보드의 5V에 연결됩니다.
    - KY-023의 GND 핀은 VCP-G 보드의 GND에 연결됩니다.
    - KY-023의 VRx 핀은 VCP-G 보드의 아날로그 핀 A5에 연결됩니다.
    - KY-023의 VRy 핀은 VCP-G 보드의 아날로그 핀 A4에 연결됩니다.
    - KY-023의 SW 핀은 VCP-G 보드의 2번 핀에 연결됩니다.
 
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/Joystick%20Circuit%20Schematic.png"></p>
<p align="center"><strong>그림 7.3 조이스틱 회로도</strong></p>
 
#### 7.2.2.1 핀 매핑
다음 표는 핀 매핑을 보여줍니다.
 
<p align="center"><strong>표 7.3 조이스틱의 핀 매핑</strong></p>
<div align="center">
	<table>
	    <tr>
	        <th colspan="3">핀 이름</th>
	        <th>VCP-G 보드</th>
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

### 7.2.3 실행 방법
1. 다음 소스 코드를 Arduino IDE에 복사하고 파일을 "joystick.ino"로 저장합니다.
   
   **참고:** 다음 소스 코드는 이 문서에서만 제공됩니다. 

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
2. "joystick.ino" 파일을 확인하고 VCP-G에 업로드합니다.
3. 업로드 프로세스가 무한 업로드 상태에서 멈추면 FWDN 모드가 활성화되지 않았기 때문입니다. 이 문제를 해결하려면:  
    1. VCP-G 보드에서 전원 케이블을 분리합니다.
    2. FWDN 스위치를 길게 누릅니다.
    3. FWDN 스위치를 계속 누른 상태에서 전원 케이블을 다시 연결합니다.
    4. FWDN 스위치를 놓습니다.  
        문제가 지속되면 관리자 권한으로 Arduino IDE를 실행해 보십시오.
4. 파일을 성공적으로 업로드한 후 Arduino IDE 출력 콘솔에서 다음 메시지를 확인합니다:
   
    **참고:** 메시지에는 **joystick.ino.rom**이 포함되어야 합니다.
    ```
    [FWDN_VCP::WriteFile:577] Complete to send file - C:\Users\topst\AppData\Local\arduino\sketches\1D003A72AB3391D6D60FD7993380F8CD/joystick.ino.rom 

    [main:155] Complete FWDN
    ```

</br></br></br>

## 7.3 가스 센서
---
이 예제는 VCP-G 보드가 가스 센서(MQ 135)를 사용하여 공기 중의 다양한 유해 가스를 감지하는 방법을 보여줍니다. VCP-G 보드의 아날로그 핀에 연결된 센서에서 아날로그 값을 읽어 전압으로 변환한 다음 소수점 첫째 자리까지 시리얼 모니터에 출력합니다.

**참고:** 가스 센서(MQ-135)는 Winsen®의 제품입니다. 디자인, 상표 및 관련 지적 재산권에 대한 모든 권리는 Winsen에 있습니다.
</br></br>

### 7.3.1 하드웨어 요구 사항
- VCP-G 보드 (x1)
- 가스 센서 (MQ135) (x1)
- 12V 1A 전원 어댑터 (x1)
- USB Type-C to A 케이블 (x1)
- 수-암 점퍼 와이어 (x3)
</br></br>

### 7.3.2 회로
- 가스 센서
    - 가스 센서의 A0 핀은 VCP-G 보드의 아날로그 핀 A5에 연결됩니다. 
    - 가스 센서의 VCC 핀은 VCP-G 보드의 5V에 연결됩니다.
    - 가스 센서의 GND 핀은 VCP-G 보드의 GND에 연결됩니다.


<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/Gas%20Sensor%20Circuit%20Schematic.png"></p>
<p align="center"><strong>그림 7.4 가스 센서 회로도</strong></p>

#### 7.3.2.1 핀 매핑
다음 표는 핀 매핑을 보여줍니다.

<p align="center"><strong>표 7.4 가스 센서의 핀 매핑</strong></p>
<div align="center">
	<table>
	    <tr>
	        <th colspan="3">핀 이름</th>
	        <th>VCP-G 보드</th>
	        <th>Arduino IDE</th>
	    </tr>
	    <tr>
	        <td colspan="3">가스 센서 A0 핀</td>
	        <td>A5</td>
	        <td>A5</td>
	    </tr>
	        <tr>
	        <td colspan="3">가스 센서 VCC 핀</td>
	        <td>5V</td>
	        <td>-</td>
	    </tr>
	    <tr>
	        <td colspan="3">가스 센서 GND 핀</td>
	        <td>GND</td>
	        <td>-</td>
	    </tr>
	</table>
</div>
</br></br>

### 7.3.3 실행 방법
1. 다음 소스 코드를 Arduino IDE에 복사하고 파일을 "GasSensor.ino"로 저장합니다.
  
   **참고:** 다음 소스 코드는 이 문서에서만 제공됩니다. 

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
2. "GasSensor.ino" 파일을 확인하고 VCP-G에 업로드합니다.
3. 업로드 프로세스가 무한 업로드 상태에서 멈추면 FWDN 모드가 활성화되지 않았기 때문입니다. 이 문제를 해결하려면:  
    1. VCP-G 보드에서 전원 케이블을 분리합니다.
    2. FWDN 스위치를 길게 누릅니다.
    3. FWDN 스위치를 계속 누른 상태에서 전원 케이블을 다시 연결합니다.
    4. FWDN 스위치를 놓습니다.  
        문제가 지속되면 관리자 권한으로 Arduino IDE를 실행해 보십시오.
4. 파일을 성공적으로 업로드한 후 Arduino IDE 출력 콘솔에서 다음 메시지를 확인합니다:
   
    **참고:** 메시지에는 **GasSensor.ino.rom**이 포함되어야 합니다.
    ```
    [FWDN_VCP::WriteFile:577] Complete to send file - C:\Users\topst\AppData\Local\arduino\sketches\1D003A72AB3391D6D60FD7993380F8CD/joystick.ino.rom 

    [main:155] Complete FWDN
    ```
</br></br></br>

## 7.4 금속 터치 센서 모듈
---
이 예제 프로그램은 VCP-G 보드가 터치 센서와 브레드보드의 LED를 제어하는 방법을 보여줍니다. 금속 터치 센서 모듈(KY-036)은 금속 표면이나 사람의 피부에 닿는 것을 감지하도록 설계된 다목적 아날로그/디지털 센서입니다. 이 모듈은 트랜지스터를 사용하여 터치 시 전기 전도도의 변화를 감지하며, VCP-G와의 상호 작용을 위해 디지털 및 아날로그 신호를 모두 출력합니다.  
터치가 감지되면 금속 터치 센서 모듈은 관련 디지털/아날로그 값을 시리얼 모니터에 출력합니다. 터치 상태에 따라 LED를 제어할 수도 있습니다. 

**참고:** 금속 터치 센서 모듈(KY-036)에는 감도 조절을 위한 내장 가변 저항이 있습니다. 이 가변 저항을 돌려 감도를 높이거나 낮출 수 있습니다.
</br></br>

### 7.4.1 하드웨어 요구 사항
- VCP-G 보드 (x1)
- 브레드보드 (x1)
- 금속 터치 센서 모듈 (KY-036) (x1)
- LED (x1)
- 220Ω 저항 (x1)
- 12V 1A 전원 어댑터 (x1)
- USB Type-C to A 케이블 (x1)
- 수-수 점퍼 와이어 (x4)
- 수-암 점퍼 와이어 (x4)
</br></br>

### 7.4.2 회로
- 금속 터치 센서 모듈
    - 금속 터치 센서 모듈의 A0 핀은 VCP-G 보드의 아날로그 핀 A5에 연결됩니다.
    - 금속 터치 센서 모듈의 G 핀은 VCP-G 보드의 GND에 연결됩니다.
    - 금속 터치 센서 모듈의 (+) 핀은 VCP-G 보드의 5V에 연결됩니다.
    - 금속 터치 센서 모듈의 D0 핀은 VCP-G 보드의 30번 핀에 연결됩니다.

- LED
    - LED의 (+) 핀은 VCP-G 보드의 13번 핀에 연결됩니다.
    - LED의 (-) 핀은 220Ω 저항을 통해 VCP-G 보드의 GND에 연결됩니다.


<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/Metal%20Touch%20Sensor%20Circuit%20Schematic.png"></p>
<p align="center"><strong>그림 7.5 금속 터치 센서 회로도</strong></p>

#### 7.4.2.1 핀 매핑
다음 표는 핀 매핑을 보여줍니다.

<p align="center"><strong>표 7.5 금속 터치 센서의 핀 매핑</strong></p>
<div align="center">
	<table>
	    <tr>
	        <th colspan="3">핀 이름</th>
	        <th>VCP-G 보드</th>
	        <th>Arduino IDE</th>
	    </tr>
	    <tr>
	        <td colspan="3">금속 터치 센서 모듈 A0 핀</td>
	        <td>A5</td>
	        <td>A5</td>
	    </tr>
	        <tr>
	        <td colspan="3">금속 터치 센서 모듈 G 핀</td>
	        <td>GND</td>
	        <td>-</td>
	    </tr>
	    <tr>
	        <td colspan="3">금속 터치 센서 모듈 (+) 핀</td>
	        <td>5V</td>
		    <td>-</td>
		</tr>
	    <tr>
	        <td colspan="3">금속 터치 센서 모듈 D0 핀</td>
	        <td>30</td>
	        <td>30</td>
	    </tr>
	    <tr>
	        <td colspan="3">LED (+) 핀</td>
	        <td>13</td>
	        <td>13</td>
	    </tr>
	    <tr>
	        <td colspan="3">LED (+) 핀</td>
	        <td>GND</td>
	        <td>-</td>
	    </tr>
	</table>
</div>
</br></br>

### 7.4.3 실행 방법
1. 다음 소스 코드를 Arduino IDE에 복사하고 파일을 "vcp_touch.ino"로 저장합니다.  

   **참고:** 다음 소스 코드는 이 문서에서만 제공됩니다. 

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
2. "vcp_touch.ino" 파일을 확인하고 VCP-G에 업로드합니다.
3. 업로드 프로세스가 무한 업로드 상태에서 멈추면 FWDN 모드가 활성화되지 않았기 때문입니다. 이 문제를 해결하려면:  
    1. VCP-G 보드에서 전원 케이블을 분리합니다.
    2. FWDN 스위치를 길게 누릅니다.
    3. FWDN 스위치를 계속 누른 상태에서 전원 케이블을 다시 연결합니다.
    4. FWDN 스위치를 놓습니다.  
        문제가 지속되면 관리자 권한으로 Arduino IDE를 실행해 보십시오.
4. 파일을 성공적으로 업로드한 후 Arduino IDE 출력 콘솔에서 다음 메시지를 확인합니다:
   
    **참고:** 메시지에는 **vcp_touch.ino.rom**이 포함되어야 합니다.
    ```
    [FWDN_VCP::WriteFile:577] Complete to send file - C:\Users\topst\AppData\Local\arduino\sketches\567805554B5B9F915DCC80B38483AE07/vcp_touch.ino.rom

    [main:155] Complete FWDN
    ```

**참고:** 시리얼 통신에 적절한 전송 속도를 설정하십시오.

</br></br></br>

## 7.5 모터 드라이버가 있는 스텝 모터
---
이 예제는 VCP-G 보드가 4선식 스텝 모터(28BYJ-48 (5VDC))와 모터 드라이버(ULN2003 (5V–12V))를 제어하는 방법을 보여줍니다. 7.5.3장의 코드는 모터 드라이버에 연결된 핀을 정의하고 회전당 스텝 수를 설정합니다. 모터는 정방향으로 한 바퀴 회전하고 잠시 멈춘 다음, 역방향으로 한 바퀴 회전하고 다시 멈춥니다. 모터 속도는 스텝 간의 지연 시간으로 제어되며, 방향은 코일이 활성화되는 순서로 제어됩니다.

**참고:** 28BYJ-48 모터는 Half step 모드에서 한 바퀴 회전하는 데 4096개의 신호가 필요하고 Full step 모드에서는 2048개의 신호가 필요합니다. 정밀한 모터 제어를 위해서는 모드에 따라 필요한 신호 수를 고려해야 합니다. 
</br></br>

### 7.5.1 하드웨어 요구 사항
- VCP-G 보드 (x1)
- 스텝 모터 (28BYJ-48) (x1)
- 모터 드라이버 (ULN2003) (x1)
- 12V 1A 전원 어댑터 (x1)
- USB Type-C to A 케이블 (x1)
- 수-수 점퍼 와이어 (x6)
</br></br>

### 7.5.2 회로
- 모터 드라이버
    - IN1 핀은 VCP-G 보드의 8번 핀에 연결됩니다.
    - IN2 핀은 VCP-G 보드의 9번 핀에 연결됩니다.
    - IN3 핀은 VCP-G 보드의 10번 핀에 연결됩니다.
    - IN4 핀은 VCP-G 보드의 11번 핀에 연결됩니다.
    - (+) 핀은 VCP-G 보드의 5V에 연결됩니다.
    - (-) 핀은 VCP-G 보드의 GND에 연결됩니다.

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/Step%20Motor%20with%20Motor%20Driver%20Circuit%20Schematic.png"></p>
<p align="center"><strong>그림 7.6 모터 드라이버가 있는 스텝 모터 회로도</strong></p>

#### 7.5.2.1 핀 매핑
다음 표는 핀 매핑을 보여줍니다.

<p align="center"><strong>표 7.6 모터 드라이버의 핀 매핑</strong></p>
<div align="center">
	<table>
	    <tr>
	        <th colspan="3">핀 이름</th>
	        <th>VCP-G 보드</th>
	        <th>Arduino IDE</th>
	    </tr>
	    <tr>
	        <td colspan="3">모터 드라이버 IN1 핀</td>
	        <td>8</td>
	        <td>8</td>
	    </tr>
	        <tr>
	        <td colspan="3">모터 드라이버 IN2 핀</td>
	        <td>9</td>
	        <td>9</td>
	    </tr>
	    <tr>
	        <td colspan="3">모터 드라이버 IN3 핀</td>
	        <td>10</td>
	        <td>10</td>
		</tr>
	    <tr>
	        <td colspan="3">모터 드라이버 IN4 핀</td>
		    <td>11</td>
			<td>11</td>
	    </tr>
		<tr>
			<td colspan="3">모터 드라이버 (+) 핀</td>
	        <td>5V</td>
	        <td>-</td>
		</tr>
	    <tr>
	        <td colspan="3">모터 드라이버 (-) 핀</td>
	        <td>GND</td>
	        <td>-</td>
	    </tr>
	</table>
</div>
</br></br>

### 7.5.3 실행 방법
1. 다음 소스 코드를 Arduino IDE에 복사하고 파일을 "motordriver.ino"로 저장합니다.

    **참고:** 다음 소스 코드는 이 문서에서만 제공됩니다. 

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
2. "motordriver.ino" 파일을 확인하고 VCP-G에 업로드합니다.
3. 업로드 프로세스가 무한 업로드 상태에서 멈추면 FWDN 모드가 활성화되지 않았기 때문입니다. 이 문제를 해결하려면:  
    1. VCP-G 보드에서 전원 케이블을 분리합니다.
    2. FWDN 스위치를 길게 누릅니다.
    3. FWDN 스위치를 계속 누른 상태에서 전원 케이블을 다시 연결합니다.
    4. FWDN 스위치를 놓습니다.  
        문제가 지속되면 관리자 권한으로 Arduino IDE를 실행해 보십시오.
4. 파일을 성공적으로 업로드한 후 Arduino IDE 출력 콘솔에서 다음 메시지를 확인합니다:  

    **참고:** 메시지에는 **motordriver.ino.rom**이 포함되어야 합니다.
    ```
    [FWDN_VCP::WriteFile:577] Complete to send file - C:\Users\topst\AppData\Local\arduino\sketches\567805554B5B9F915DCC80B38483AE07/motordriver.rom

    [main:155] Complete FWDN
    ```
</br></br></br></br>

# 8. 참고 문헌
---
- 자세한 내용은 TOPST에 문의하십시오: topst@topst.ai

**참고:** 참조 문서는 계약 조건에 따라 가능한 경우 제공될 수 있습니다. 참조 문서를 사용할 수 없는 경우 개발과 직접 관련된 내용을 안내받을 수 있습니다.
