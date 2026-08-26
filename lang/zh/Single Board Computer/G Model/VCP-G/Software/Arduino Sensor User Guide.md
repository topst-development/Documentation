# 1. 简介
---
本文档提供了在 VCP-G 开发板上使用各种 Arduino 传感器的指南，其中包含连接说明和示例代码，帮助您轻松使用 VCP-G 开发项目。

具体而言，本文档提供针对 VCP-G 的 Arduino IDE 示例指导，包括：  
- VCP-G Digital
- VCP-G Analog
- VCP-G SPI
- VCP-G I2C
- VCP-G UART
- Additional Example

使用 VCP-G 之前，请参阅图 1.1。

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/vcp-g%20pinout%20Diagram.png"></p>
<p align="center"><strong>图 1.1 VCP-G 引脚分布图</strong></p>

</br></br></br></br>

# 2. VCP-G 数字引脚
---
本章提供使用 VCP-G 开发板的数字引脚控制 LED 的示例。在 VCP-G 中，数字引脚用于发送或接收二进制信号（HIGH 或 LOW），因此对于控制 LED、开关和传感器等元件至关重要。 

本章包含两个示例项目，演示如何使用数字输出控制多个 LED，帮助建立对数字引脚功能的基本理解。

</br></br></br>

## 2.1 vcp4LED
---
本示例程序演示 VCP-G 开发板如何控制面包板上的四个 LED。示例代码位于 “vcp4LED.ino” 文件中。将该文件上传到 VCP-G 后，LED 会按正向和反向的顺序依次点亮和熄灭，每次切换之间延时 500 ms。 

</br></br>

### 2.1.1 硬件要求  
- VCP-G 开发板 (x1)
- 面包板 (x1)
- LED (x4)
- 220Ω 电阻 (x4)
- 12V 1A 电源适配器 (x1)
- USB Type-C 转 A 线缆 (x1) 
- 公对公跳线 (x9)
</br></br>

### 2.1.2 电路
- LED01
    - (+) 引脚通过一个 220Ω 电阻连接到面包板上的 5V 电源轨，该电源由 VCP-G 开发板提供。
    - (-) 引脚连接到 VCP-G 开发板上的 47 号引脚。
- LED02
    - (+) 引脚通过一个 220Ω 电阻连接到面包板上的 5V 电源轨。
    - (-) 引脚连接到 VCP-G 开发板上的 17 号引脚。
- LED03
    - (+) 引脚通过一个 220Ω 电阻连接到面包板上的 5V 电源轨。
    - (-) 引脚连接到 VCP-G 开发板上的 50 号引脚。
- LED04
    - (+) 引脚通过一个 220Ω 电阻连接到面包板上的 5V 电源轨。
    - (-) 引脚连接到 VCP-G 开发板上的 48 号引脚。  

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/vcp4LED%20Circuit%20Schematic.png"></p>
<p align="center"><strong>图 2.1 vcp4LED 电路原理图</strong></p>

#### 2.1.2.1 引脚映射
下表显示了引脚映射。

<p align="center"><strong>表 2.1 vcp4LED 的引脚映射</strong></p>
<div align="center">	
	<table>
		<tr>
			<th colspan="3">引脚名称</th>
	        <th>VCP-G 开发板</th>
	        <th>Arduino IDE</th>
	    </tr>
	    <tr>
	        <td colspan="3">LED01 (-) 引脚</td>
	        <td>47</td>
	        <td>47</td>
	    </tr>
	        <tr>
	        <td colspan="3">LED02 (-) 引脚</td>
	        <td>17</td>
	        <td>17</td>
	    </tr>
	        <tr>
	        <td colspan="3">LED03 (-) 引脚</td>
	        <td>50</td>
	        <td>50</td>
	    </tr>
	        <tr>
	        <td colspan="3">LED04 (-) 引脚</td>
	        <td>48</td>
	        <td>48</td>
	    </tr>
	</table>
</div>
</br></br>

### 2.1.3 执行方法
1. 打开 "vcp4LED.ino" 文件。  
    1. 打开 Arduino IDE。
    2. 单击 **File -> Examples -> 01.VCP-G Digital -> vcp4LED**。
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
2. 验证并将 "vcp4LED.ino" 文件上传到 VCP-G。
3. 如果上传过程卡在无限上传状态，则是因为未激活 FWDN 模式。解决方法如下：  
    1. 从 VCP-G 开发板上拔下电源线。
    2. 按住 FWDN 开关。
    3. 在持续按住 FWDN 开关的同时重新连接电源线。
    4. 松开 FWDN 开关。
        如果问题仍然存在，请尝试以管理员权限运行 Arduino IDE。
4. 成功上传文件后，请在 Arduino IDE 输出控制台中查看以下消息：  

     **注意：** 该消息应包含 **vcp4LED.ino.rom**。
    ```
    [FWDN_VCP::WriteFile:577] Complete to send file - C:\Users\topst\AppData\Local\arduino\sketches\C05357299384CE5734F0E696C5A4DA3B/vcp4LED.ino.rom

    [main:155] Complete FWDN
    ```

</br></br></br>

## 2.2 vcp4LED_Button
---
本示例程序演示 VCP-G 开发板如何控制面包板上的四个 LED 和一个按钮。按下按钮时，右侧两个 LED 熄灭，左侧两个 LED 点亮。松开按钮时，原本点亮的 LED 熄灭，原本熄灭的 LED 点亮。该程序会持续检查按钮状态，并相应地调整 LED。
</br></br>

### 2.2.1 硬件要求
- VCP-G 开发板 (x1)
- 面包板 (x1)
- LED (x4)
- 按钮开关（传感器）(x1)
- 220Ω 电阻 (x4)
- 12V 1A 电源适配器 (x1)
- USB Type-C 转 A 线缆 (x1)
- 公对公跳线 (x12)
</br></br>

### 2.2.2 电路
1.	LED01
    - (+) 引脚通过一个 220Ω 电阻连接到面包板上的 5V 电源轨，该电源由 VCP-G 开发板提供。
    - (-) 引脚连接到 VCP-G 开发板上的 47 号引脚。
2.	LED02
    - (+) 引脚通过一个 220Ω 电阻连接到面包板上的 5V 电源轨。
    - (-) 引脚连接到 VCP-G 开发板上的 17 号引脚。
3.	LED03
    - (+) 引脚通过一个 220Ω 电阻连接到面包板上的 5V 电源轨。
    - (-) 引脚连接到 VCP-G 开发板上的 50 号引脚。
4.	LED04
    - (+) 引脚通过一个 220Ω 电阻连接到面包板上的 5V 电源轨。
    - (-) 引脚连接到 VCP-G 开发板上的 48 号引脚。
5.	按钮开关
    - 按钮开关的一个引脚连接到 VCP-G 开发板上的 45 号引脚。
    - 按钮对角线另一侧的引脚连接到 GND 引脚。

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/vcp4LED_Button%20Circuit%20Schematic.png"></p>
<p align="center"><strong>图 2.2 vcp4LED_Button 电路原理图</strong></p>

#### 2.2.2.1 引脚映射
下表显示了引脚映射。

<p align="center"><strong>表 2.2 vcp4LED_Button 的引脚映射</strong></p>
<div align="center">
	<table>
	    <tr>
	        <th colspan="3">引脚名称</th>
	        <th>VCP-G 开发板</th>
	        <th>Arduino IDE</th>
	    </tr>
	    <tr>
	        <td colspan="3">LED01 (-) 引脚</td>
	        <td>47</td>
	        <td>47</td>
	    </tr>
	        <tr>
	        <td colspan="3">LED02 (-) 引脚</td>
	        <td>17</td>
	        <td>17</td>
	    </tr>
	        <tr>
	        <td colspan="3">LED03 (-) 引脚</td>
	        <td>50</td>
	        <td>50</td>
	    </tr>
	        <tr>
	        <td colspan="3">LED04 (-) 引脚</td>
	        <td>48</td>
	        <td>48</td>
	    </tr>
	    </tr>
	        <tr>
	        <td colspan="3">按钮的一个引脚</td>
	        <td>45</td>
	        <td>45</td>
	    </tr>
	</table>
</div>
</br></br>

### 2.1.3 执行方法
1. 打开 "vcp4LED_Button.ino" 文件。
    1. 打开 Arduino IDE。
    2. 单击 **File -> Examples -> 01.VCP-G Digital -> vcp4LED_Button**。
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
2. 验证并将 "vcp4LED_Button.ino" 文件上传到 VCP-G。
3. 如果上传过程卡在无限上传状态，则是因为未激活 FWDN 模式。解决方法如下：  
    1. 从 VCP-G 开发板上拔下电源线。
    2. 按住 FWDN 开关。
    3. 在持续按住 FWDN 开关的同时重新连接电源线。
    4. 松开 FWDN 开关。 
        如果问题仍然存在，请尝试以管理员权限运行 Arduino IDE。
4. 成功上传文件后，请在 Arduino IDE 输出控制台中查看以下消息：  

    **注意：** 该消息应包含 **vcp4LED_Button.ino.rom**。
    ```
    [FWDN_VCP::WriteFile:577] Complete to send file - C:\Users\topst\AppData\Local\arduino\sketches\5CC1DB4CA216E2BC009504FAA3D06456/vcp4LED_Button.ino.rom

    [main:155] Complete FWDN
    ```

</br></br></br></br>

# 3. VCP-G 模拟引脚
---
本章提供在 VCP-G 开发板上使用模拟引脚的示例。在 VCP-G 中，模拟引脚接收来自传感器的连续电压信号，从而可以精确测量变化的输入值。第 3.1 章、第 3.2 章和第 3.3 章介绍了如何使用模拟引脚读取传感器数据并控制输出，帮助建立对模拟输入处理的基本理解。

</br></br></br>

## 3.1 AnalogInOutSerial
---
本示例程序演示 VCP-G 开发板如何控制面包板上的电位器和 LED。VCP-G 从模拟输入引脚读取数值，将结果映射到 0 至 1000 的范围，并使用该值设置输出引脚（连接到 LED）的脉冲宽度调制 (PWM)。结果同时会输出到 Serial Monitor。
</br></br>

### 3.1.1 硬件要求
- VCP-G 开发板 (x1)
- 面包板 (x1)
- LED (x1)
- 电位器 (x1)
- 220Ω 电阻 (x2)
- 12V 1A 电源适配器 (x1)
- USB Type-C 转 A 线缆 (x1)
- 公对公跳线 (x4)
</br></br>

### 3.1.2 电路
- 电位器
    - 电位器的中间引脚连接到 VCP-G 开发板上的模拟引脚 A5。
    - 电位器的 GND 引脚连接到 VCP-G 开发板上的 43 号引脚，并通过一个 220Ω 电阻连接到 VCP-G 开发板上的 GND 引脚。
- LED
    - LED 的 (+) 引脚通过一个 220Ω 电阻连接到 VCP-G 开发板上的 3.3V。
    - LED 的 (-) 引脚连接到电位器的中间引脚。

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/AnalogInOutSerial%20Circuit%20Schematic.png"></p>
<p align="center"><strong>图 3.1 AnalogInOutSerial 电路原理图</strong></p>

#### 3.1.2.1 引脚映射
下表显示了引脚映射。

<p align="center"><strong>表 3.1 AnalogInOutSerial 的引脚映射</strong></p>
<div align="center">
	<table>
	    <tr>
	        <th colspan="3">引脚名称</th>
	        <th>VCP-G 开发板</th>
	        <th>Arduino IDE</th>
	    </tr>
	    <tr>
	        <td colspan="3">电位器中间引脚</td>
	        <td>A5</td>
	        <td>-</td>
	    </tr>
	        <tr>
	        <td colspan="3">电位器 GND 引脚</td>
	        <td>43</td>
	        <td>43</td>
	    </tr>
	        <tr>
	        <td colspan="3">LED (+) 引脚</td>
	        <td>3.3V</td>
	        <td>-</td>
	    </tr>
	        <tr>
	        <td colspan="3">LED (-) 引脚</td>
	        <td>A5</td>
	        <td>A5</td>
	    </tr>
	</table>
</div>
</br></br>

### 3.1.3 执行方法
1. 打开 "AnalogInOutSerial.ino" 文件。  
    1. 打开 Arduino IDE。
    2. 单击 **File -> Examples -> 02.VCP-G Analog -> AnalogInOutSerial**。
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
 
    **注意：** 如果出现 "Serial" 未声明的错误，请确保正确包含以下库和对象声明。
    ```
    #include <HardwareSerial.h>
    HardwareSerial Serial;
    ```
2. 验证并将 "AnalogInOutSerial.ino" 文件上传到 VCP-G。
3. 如果上传过程卡在无限上传状态，则是因为未激活 FWDN 模式。解决方法如下：  
    1. 从 VCP-G 开发板上拔下电源线。
    2. 按住 FWDN 开关。
    3. 在持续按住 FWDN 开关的同时重新连接电源线。
    4. 松开 FWDN 开关。
        如果问题仍然存在，请尝试以管理员权限运行 Arduino IDE。
4. 成功上传文件后，请在 Arduino IDE 输出控制台中查看以下消息：  
 
    **注意：** 该消息应包含 **AnalogInOutSerial.ino.rom**。
    ```
    [FWDN_VCP::WriteFile:577] Complete to send file - C:\Users\topst\AppData\Local\arduino\sketches\EB016432EF98DEF0B9102FD77148DD5D/AnalogInOutSerial.ino.rom

    [main:155] Complete FWDN
    ```

</br></br></br>

## 3.2 AnalogInput
---
本示例程序演示 VCP-G 开发板如何控制面包板上的电位器和 LED。它从模拟输入引脚读取数值，并使用该数值控制 LED。当传感器数值低于 3000 时，LED 点亮。当传感器数值达到或高于 3000 时，LED 熄灭。
</br></br>

### 3.2.1 硬件要求
- VCP-G 开发板 (x1)
- 面包板 (x1)
- LED (x1)
- 电位器 (x1)
- 220Ω 电阻 (x1)
- 12V 1A 电源适配器 (x1)
- USB Type-C 转 A 线缆 (x1)
- 公对公跳线（x6）
</br></br>

### 3.2.2 电路
- 电位器
    - 电位器的 VCC 引脚通过 220Ω 电阻连接到 VCP-G 开发板上的 3.3V。
    - 电位器的中间引脚连接到 VCP-G 开发板上的模拟引脚 A5。
    - 电位器的 GND 引脚通过 220Ω 电阻连接到 VCP-G 开发板上的 GND 引脚。
- LED
    - LED 的 (+) 引脚通过一个 220Ω 电阻连接到 VCP-G 开发板上的 3.3V。
    - LED 的 (-) 引脚连接到 VCP-G 开发板上的 5 号引脚。

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/AnalogInput%20Circuit%20Schematic.png"></p>
<p align="center"><strong>图 3.2 AnalogInput 电路原理图</strong></p>

#### 3.2.2.1 引脚图
下表显示了引脚映射。

<p align="center"><strong>表 3.2 AnalogInput 的引脚图</strong></p>
<div align="center">
	<table>
	    <tr>
	        <th colspan="3">引脚名称</th>
	        <th>VCP-G 开发板</th>
	        <th>Arduino IDE</th>
	    </tr>
	    <tr>
	        <td colspan="3">电位器 VCC 引脚</td>
	        <td>3.3V</td>
	        <td>-</td>
	    </tr>
	    <tr>
	        <td colspan="3">电位器中间引脚</td>
	        <td>A5</td>
	        <td>A5</td>
	    </tr>
	        <tr>
	        <td colspan="3">电位器 GND 引脚</td>
	        <td>GND</td>
	        <td>-</td>
	    </tr>
	        <tr>
	        <td colspan="3">LED (+) 引脚</td>
	        <td>3.3V</td>
	        <td>-</td>
	    </tr>
	        <tr>
	        <td colspan="3">LED (-) 引脚</td>
	        <td>5</td>
	        <td>5</td>
	    </tr>
	</table>
</div>
</br></br>

### 3.2.3 执行方法
1. 打开 "AnalogInput.ino" 文件。  
    1. 打开 Arduino IDE。
    2. 单击 **File -> Examples -> 02.VCP-G Analog -> AnalogInput**。
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
 
    **注意 1：** 要在 Serial Monitor 中查看 **sensorValue**，请在源代码中添加 **Serial.println()**。  
    **注意 2：** 固定电阻与可变电阻（电位器）配合使用，用于调节传感器数值。传感器数值随电位器旋转的幅度而变化，而所需旋转的幅度取决于固定电阻的阻值。

2. 验证 "AnalogInput.ino" 文件并将其上传到 VCP-G。
3. 如果上传过程卡在无限上传状态，则是因为未激活 FWDN 模式。解决方法如下：  
    1. 从 VCP-G 开发板上拔下电源线。
    2. 按住 FWDN 开关。
    3. 在持续按住 FWDN 开关的同时重新连接电源线。
    4. 松开 FWDN 开关。  
        如果问题仍然存在，请尝试以管理员权限运行 Arduino IDE。
4. 成功上传文件后，请在 Arduino IDE 输出控制台中查看以下消息：  

   **注意：** 该消息应包含 **AnalogInput.ino.rom**。
    ```
    [FWDN_VCP::WriteFile:577] Complete to send file - C:\Users\topst\AppData\Local\arduino\sketches\C3FDEE51354320EA689DFEB4EDCF2ECD/AnalogInput.ino.rom

    [main:155] Complete FWDN
    ```

</br></br></br>

## 3.3 pwmFade
---
本示例程序演示 VCP-G 开发板如何使用 PWM 通过循环逐渐增加和降低亮度来控制面包板上的 LED。LED 达到最大亮度后，其亮度开始降低。程序持续调节 LED 的亮度，从而形成渐隐渐显的效果。
</br></br>

### 3.3.1 硬件要求
- VCP-G 开发板 (x1)
- 面包板 (x1)
- LED (x1)
- 220Ω 电阻 (x1)
- 12V 1A 电源适配器 (x1)
- USB Type-C 转 A 线缆 (x1)
- 公对公跳线（x2）
</br></br>

### 3.3.2 电路
- LED
    - LED 的 (+) 引脚连接到 VCP-G 开发板上的 5V。
    - LED 的 (-) 引脚通过 220Ω 电阻连接到 VCP-G 开发板上的 9 号引脚。

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/pwmFade%20Circuit%20Schematic.png"></p>
<p align="center"><strong>图 3.3 pwmFade 电路原理图</strong></p>

#### 3.3.2.1 引脚图
下表显示了引脚映射。

<p align="center"><strong>表 3.3 pwmFade 的引脚图</strong></p>
<div align="center">
	<table>
	    <tr>
	        <th colspan="3">引脚名称</th>
	        <th>VCP-G 开发板</th>
	        <th>Arduino IDE</th>
	    </tr>
	    <tr>
	        <td colspan="3">LED (+) 引脚</td>
	        <td>5V</td>
	        <td>-</td>
	    </tr>
	        <tr>
	        <td colspan="3">LED (-) 引脚</td>
	        <td>9</td>
	        <td>9</td>
	    </tr>
	</table>
</div>
</br></br>

### 3.3.3 执行方法
1. 打开 "pwmFade.ino" 文件。
    1. 打开 Arduino IDE。
    2. 单击 **File -> Examples -> 02.VCP-G Analog -> pwmFade**。
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
2. 验证 "pwmFade.ino" 文件并将其上传到 VCP-G 开发板。
3. 如果上传过程卡在无限上传状态，则是因为未激活 FWDN 模式。解决方法如下：  
    1. 从 VCP-G 开发板上拔下电源线。
    2. 按住 FWDN 开关。
    3. 在持续按住 FWDN 开关的同时重新连接电源线。
    4. 松开 FWDN 开关。
        如果问题仍然存在，请尝试以管理员权限运行 Arduino IDE。
4. 成功上传文件后，请在 Arduino IDE 输出控制台中查看以下消息：  

     **注意：** 该消息应包含 **pwmFade.ino.rom**。
    ```
    [FWDN_VCP::WriteFile:577] Complete to send file - C:\Users\topst\AppData\Local\arduino\sketches\69446E8A7F6616A7D5466014BDF759FC/pwmFade.ino.rom 

    [main:155] Complete FWDN
    ```

</br></br></br></br>

# 4. VCP SPI
---
本章介绍如何在 VCP-G 上配置 Serial Peripheral Interface (SPI) 通信。  
SPI 是一种高速同步通信协议，用于在微控制器与外围设备之间交换数据。它使用独立的信号线分别进行数据传输（MOSI 和 MISO）、时钟同步（SCK）和设备选择（SS），从而确保通信高效可靠。  
以下各章介绍如何设置和使用 SPI 与外部设备进行接口连接。

</br></br></br>

## 4.1 vcpSPI_Dot8x8
---
本示例程序演示 VCP-G 开发板如何使用 MAX7219 驱动程序控制 8x8 LED 点阵。8x8 LED 点阵通过使用预定义的二进制数组设置各行，显示心形和字母 "R" 等图案。通过调节 LED 的亮度产生脉动效果，增加动态视觉效果。其他功能包括反转和清除显示，以进一步增强功能性。
</br></br>

### 4.1.1 硬件要求
- VCP-G 开发板 (x1)
- 8x8 点阵（x1）
- 12V 1A 电源适配器 (x1)
- USB Type-C 转 A 线缆 (x1)
- 公对母跳线 (x5)
</br></br>

### 4.1.2 电路
- 8x8 点阵屏
    - 8x8 点阵的 VCC 引脚连接到 VCP-G 开发板上的模拟引脚 5V。
    - 8x8 点阵的 GND 引脚连接到 VCP-G 开发板上的 GND。
    - 8x8 点阵的 DIN 引脚连接到 VCP-G 开发板上的 11 号引脚。
    - 8x8 点阵的 CS 引脚连接到 VCP-G 开发板上的 10 号引脚。
    - 8x8 点阵的 CLS 引脚连接到 VCP-G 开发板上的 13 号引脚。

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/vcpSPI_Dot8x8%20Circuit%20Schematic.png"></p>
<p align="center"><strong>图 4.1 vcpSPI_Dot8x8 电路原理图</strong></p>

#### 4.1.2.1 引脚图
下表显示了引脚映射。

<p align="center"><strong>表 4.1 vcpSPI_Dot8x8 的引脚图</strong></p>
<div align="center">
	<table>
	    <tr>
	        <th colspan="3">引脚名称</th>
	        <th>VCP-G 开发板</th>
	        <th>Arduino IDE</th>
	    </tr>
	    <tr>
	        <td colspan="3">8x8 点阵 VCC 引脚</td>
	        <td>5V</td>
	        <td>-</td>
	    </tr>
	        <tr>
	        <td colspan="3">8x8 点阵 GND 引脚</td>
	        <td>GND</td>
	        <td>-</td>
	    </tr>
	    <tr>
	        <td colspan="3">8x8 点阵 DIN 引脚</td>
	        <td>11</td>
	        <td>11</td>
	    </tr>
	    <tr>
	        <td colspan="3">8x8 点阵 CS 引脚</td>
	        <td>10</td>
	        <td>10</td>
	    </tr>
	    <tr>
	        <td colspan="3">8x8 点阵 CLK 引脚</td>
	        <td>13</td>
	        <td>13</td>
	    </tr>
	</table>
</div>
</br></br>

### 4.1.3 执行方法
1. 打开 "vcpSPI_Dot8x8.ino" 文件。  
    1. 打开 Arduino IDE。
    2. 单击 **File -> Examples -> 03.VCP-G SPI -> vcpSPI_Dot8x8**。
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
2. 验证 "vcpSPI_Dot8x8.ino" 文件并将其上传到 VCP-G。
3. 如果上传过程卡在无限上传状态，则是因为未激活 FWDN 模式。解决方法如下：  
    1. 从 VCP-G 开发板上拔下电源线。
    2. 按住 FWDN 开关。
    3. 在持续按住 FWDN 开关的同时重新连接电源线。
    4. 松开 FWDN 开关。
        如果问题仍然存在，请尝试以管理员权限运行 Arduino IDE。
4. 成功上传文件后，请在 Arduino IDE 输出控制台中查看以下消息：  

    **注意：** 该消息应包含 **vcpSPI_Dot8x8.ino.rom**。
    ```
    [FWDN_VCP::WriteFile:577] Complete to send file - C:\Users\topst\AppData\Local\arduino\sketches\567805554B5B9F915DCC80B38483AE07/vcpSPI_Dot8x8.ino.rom

    [main:155] Complete FWDN
    ```

**注意：** 如果要使用 VCP-G 开发板中央的 SPI 引脚，可参考以下引脚编号使用。
<p align="center"><strong>表 4.2 VCP-G 上中央 SPI 引脚的映射</strong></p>
<div align="center">
	<table>
	    <tr>
	        <th colspan="3">引脚编号</th>
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
本章介绍如何在 VCP-G 上配置 Inter-integrated Circuit (I2C) 通信。  
I2C 是一种双线同步通信协议，专为多个设备之间高效交换数据而设计。它通过串行数据线（SDA）和串行时钟线（SCL）工作，允许多个外围设备使用唯一地址与微控制器通信。I2C 同时支持主从通信和多主机配置，非常适合在尽量减少所需连接数量的情况下连接传感器、显示器和其他低速设备。

</br></br></br>

## 5.1 vcpI2C_LCD1602
---
本示例程序演示 VCP-G 开发板如何使用 I2C 通信协议控制 LCD1602 显示屏。LCD1602 是一种 16 字符 2 行的液晶显示屏，常用于嵌入式系统项目。开发板利用 LiquidCrystal_I2C 库通过 I2C 总线发送命令和数据，从而高效地控制显示屏。

在本示例中，LCD 被初始化并启用背光以确保清晰可见。随后程序定位光标，在第一行显示文本 "VCP-G"，在第二行显示 "I2C Test!"。借助 I2C 通信，只需极少的接线即可控制多个设备，是紧凑型项目的有效解决方案。
</br></br>

### 5.1.1 硬件要求
- VCP-G 开发板 (x1)
- LCD1602（x1）
- 12V 1A 电源适配器 (x1)
- USB Type-C 转 A 线缆 (x1)
- 公对母跳线（x4）
</br></br>

### 5.1.2 电路
- LCD1602
    - LCD1602 的 VCC 引脚连接到 VCP-G 开发板上的模拟引脚 5V。
    - LCD1602 的 GND 引脚连接到 VCP-G 开发板上的 GND。
    - LCD1602 的 SDA 引脚连接到 VCP-G 开发板上的 48 号引脚。
    - LCD1602 的 SCL 引脚连接到 VCP-G 开发板上的 49 号引脚。

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/vcpI2C_LCD1602%20Circuit%20Schematic.png"></p>
<p align="center"><strong>图 5.1 vcpI2C_LCD1602 电路原理图</strong></p>

#### 5.1.2.1 引脚图
下表显示了引脚映射。

<p align="center"><strong>表 5.1 vcpI2C_LCD1602 的引脚图</strong></p>
<div align="center">
	<table>
	    <tr>
	        <th colspan="3">引脚名称</th>
	        <th>VCP-G 开发板</th>
	        <th>Arduino IDE</th>
	    </tr>
	    <tr>
	        <td colspan="3">LCD1602 VCC 引脚</td>
	        <td>5V</td>
	        <td>-</td>
	    </tr>
	        <tr>
	        <td colspan="3">LCD1602 GND 引脚</td>
	        <td>GND</td>
	        <td>-</td>
	    </tr>
	    <tr>
	        <td colspan="3">LCD1602 SDA 引脚</td>
	        <td>48</td>
	        <td>-</td>
	    </tr>
	    <tr>
	        <td colspan="3">LCD1602 SCL 引脚</td>
	        <td>49</td>
		    <td>-</td>
	    </tr>
	</table>
</div>

</br></br>

### 5.1.3 执行方法
1. 打开 "vcpI2C_LCD1602.ino" 文件。  
    1. 打开 Arduino IDE  
    2. 单击 **File -> Examples -> 04.VCP-G I2C -> vcpI2C_LCD1602**。
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
2. 验证 "vcpI2C_LCD1602.ino" 文件并将其上传到 VCP-G。
3. 如果上传过程卡在无限上传状态，则是因为未激活 FWDN 模式。解决方法如下：  
    1. 从 VCP-G 开发板上拔下电源线。
    2. 按住 FWDN 开关。
    3. 在持续按住 FWDN 开关的同时重新连接电源线。
    4. 松开 FWDN 开关。
        如果问题仍然存在，请尝试以管理员权限运行 Arduino IDE。
4. 成功上传文件后，在 Arduino IDE 输出控制台中查看以下消息：
   
    **注意：** 该消息应包含 **vcpI2C_LCD1602.ino.rom**。
    ```
    [FWDN_VCP::WriteFile:577] Complete to send file -         C:\Users\topst\AppData\Local\arduino\sketches\C8D91A6857B651D6C665B0EF18B7EE53/vcpI2C_LCD1602.ino.rom

    [main:155] Complete FWDN
    ```

</br></br></br></br>

# 6. VCP-G UART
---
本章介绍如何在 VCP-G 上配置 Universal Asynchronous Receiver-Transmitter (UART) 通信。  
UART 是一种广泛使用的串行通信协议，仅使用发送（TX）和接收（RX）两条信号线异步传输数据。它对于在微控制器、传感器和计算机之间交换数据而无需共享时钟信号至关重要。  
以下各章介绍如何通过 UART 发送和接收数据。

</br></br></br>

## 6.1 vcpASCIITable
---
本示例程序演示 VCP-G 如何以十进制、十六进制、八进制和二进制等多种格式打印字符的 ASCII 值。它从字符 '!'（ASCII 值 33）开始，逐个递增遍历所有可见的 ASCII 字符，并以不同格式打印每个字符。程序持续运行，直到到达字符 '~'（ASCII 值 126）。
</br></br>

### 6.1.1 硬件要求
- VCP-G 开发板 (x1)
- 12V 1A 电源适配器 (x1)
- USB Type-C 转 A 线缆 (x1)
</br></br>

### 6.1.3 执行方法
1. 打开 "vcpASCIITable.ino" 文件。
    1. 打开 Arduino IDE。
    2. 单击 **File -> Examples -> 05.VCP-G UART -> vcpASCIITable**。
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
2. 验证 "vcpASCIITable.ino" 文件并将其上传到 VCP-G。
3. 如果上传过程卡在无限上传状态，则是因为未激活 FWDN 模式。解决方法如下：  
    1. 从 VCP-G 开发板上拔下电源线。
    2. 按住 FWDN 开关。
    3. 在持续按住 FWDN 开关的同时重新连接电源线。
    4. 松开 FWDN 开关。
        如果问题仍然存在，请尝试以管理员权限运行 Arduino IDE。
4. 成功上传文件后，请在 Arduino IDE 输出控制台中查看以下消息：  

    **注意：** 该消息应包含 **vcpASCIITable.ino.rom**。
    ```
    [FWDN_VCP::WriteFile:577] Complete to send file - C:\Users\topstAppData\Local\arduino\sketches\487F45098412336AA9D73C50C17E07D8/vcpASCIITable.ino.rom

    [main:155] Complete FWDN
    ```

</br></br></br>

## 6.2 vcpGraph
---
本示例程序演示 VCP-G 如何读取面包板上电位器的模拟值，并通过 UART 将数据传输到主机 PC。Arduino 代码持续读取连接到 A5 引脚的模拟传感器（电位器）的值，并通过串口发送。配套的 Processing 代码将这些值实时可视化为动态图形，显示传感器输入随时间的变化。
</br></br>

### 6.2.1 硬件要求
- VCP-G 开发板 (x1)
- 面包板 (x1)
- 电位器 (x1)
- 10 kΩ 电阻 (x1)
- 12V 1A 电源适配器 (x1)
- USB Type-C 转 A 线缆 (x1)
- 公对公跳线 (x4)
</br></br>

### 6.2.2 电路
- 电位器
    - 电位器的中间引脚连接到 VCP-G 开发板上的模拟引脚 A5。
    - 电位器的 GND 引脚通过 10 kΩ 电阻连接到 VCP-G 开发板上的 GND。
    - 电位器的 VCC 引脚连接到 VCP-G 开发板上的 3.3V。

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/vcpGraph%20Circuit%20Schematic.png"></p>
<p align="center"><strong>图 6.1 vcpGraph 电路原理图</strong></p>

#### 6.2.2.1 引脚图
下表显示了引脚映射。

<p align="center"><strong>表 6.1 vcpGraph 的引脚图</strong></p>
<div align="center">
	<table>
	    <tr>
	        <th colspan="3">引脚名称</th>
	        <th>VCP-G 开发板</th>
	        <th>Arduino IDE</th>
	    </tr>
	    <tr>
	        <td colspan="3">电位器中间引脚</td>
	        <td>A5</td>
	        <td>A5</td>
	    </tr>
	        <tr>
	        <td colspan="3">电位器 GND 引脚</td>
	        <td>GND</td>
	        <td>-</td>
	    </tr>
	    <tr>
	        <td colspan="3">电位器 VCC 引脚</td>
	        <td>3.3V</td>
	        <td>-</td>
	    </tr>
	</table>
</div>
</br></br>

### 6.2.3 执行方法
1. 打开 "vcpGraph.ino" 文件。
    1. 打开 Arduino IDE。
    2. 单击 **File -> Examples -> 05.VCP-G UART -> vcpGraph**。
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
2. 验证 "vcpGraph.ino" 文件并将其上传到 VCP-G。
3. 如果上传过程卡在无限上传状态，则是因为未激活 FWDN 模式。解决方法如下：  
    1. 从 VCP-G 开发板上拔下电源线。
    2. 按住 FWDN 开关。
    3. 在持续按住 FWDN 开关的同时重新连接电源线。
    4. 松开 FWDN 开关。
        如果问题仍然存在，请尝试以管理员权限运行 Arduino IDE。
4. 成功上传文件后，在 Arduino IDE 输出控制台中查看以下消息：

    **注意：** 消息中应包含 **vcpGraph.ino.rom**。
    ```
    [FWDN_VCP::WriteFile:577] Complete to send file - C:\Users\topst\AppData\Local\arduino\sketches\F59E4532EC3A529F5910F376F809A5E5/vcpGraph.ino.rom

    [main:155] Complete FWDN
    ```

</br></br></br></br>

# 7. 附加示例
---
本章提供 Arduino IDE 中 "Examples for TOPST VCP Rev G" 未包含的附加传感器示例。  
本章提供在 VCP-G 开发板上使用常用 Arduino 传感器的示例指南，使您能够将各种传感器有效地集成到项目中。

</br></br></br>

## 7.1 红外 (IR) 传感器（收发器）
---
### 7.1.1 红外 (IR) 传感器 1
---
本示例演示 VCP-G 开发板如何控制面包板上的 IR 传感器和两个 LED。读取 IR 传感器的值后，如果 IR 传感器的值为 HIGH，则视为没有障碍物，绿色 LED 点亮而红色 LED 熄灭。相反，如果 IR 传感器的值为 LOW，则视为存在障碍物，红色 LED 点亮而绿色 LED 熄灭。此外，障碍物的有无会显示在串口监视器上。

#### 7.1.1.1 硬件要求
- VCP-G 开发板 (x1)
- 面包板 (x1)
- IR 收发传感器 (x1)
- LED (x2：建议使用不同颜色)
- 220Ω 电阻 (x2)
- 12V 1A 电源适配器 (x1)
- USB Type-C 转 A 线缆 (x1)
- 公对公跳线 (x4)
- 公对母跳线 (x3)

#### 7.1.1.2 电路
- IR 收发传感器
    - IR 传感器的 OUT 引脚连接到 VCP-G 开发板上的 50 号引脚。
    - IR 传感器的 VCC 引脚连接到 VCP-G 开发板上的 5V。
    - IR 传感器的 GND 引脚连接到 VCP-G 开发板上的 GND。
- 红色 LED
    - LED 的 (-) 连接到电阻，电阻连接到 VCP-G 开发板上的 GND。
    - LED 的 (+) 连接到 VCP-G 开发板上的 48 号引脚。
- 绿色 LED
    - LED 的 (-) 连接到电阻，电阻连接到 VCP-G 开发板上的 GND。
    - LED 的 (+) 连接到 VCP-G 开发板上的 17 号引脚。

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/Infrared%20(IR)%20Sensor%20Circuit%20Schematic.png"></p>
<p align="center"><strong>图 7.1 红外 (IR) 传感器电路原理图</strong></p>

##### 7.1.1.2.1 引脚图
下表显示了引脚映射。

<p align="center"><strong>表 7.1 irSensor_LED 的引脚图</strong></p>
<div align="center">
	<table>
	    <tr>
	        <th colspan="3">引脚名称</th>
	        <th>VCP-G 开发板</th>
	        <th>Arduino IDE</th>
	    </tr>
	    <tr>
	        <td colspan="3">IR 传感器 OUT 引脚 </td>
	        <td>50</td>
	        <td>50</td>
	    </tr>
	        <tr>
	        <td colspan="3">IR 传感器 VCC 引脚 </td>
	        <td>5V</td>
	        <td>-</td>
	    </tr>
	    <tr>
	        <td colspan="3">IR 传感器 GND 引脚</td>
	        <td>GND</td>
	        <td>-</td>
	    </tr>
	    <tr>
	        <td colspan="3">红色 LED (+) 引脚</td>
	        <td>48</td>
	        <td>48</td>
	    </tr>
	    <tr>
	        <td colspan="3">红色 LED (-) 引脚</td>
	        <td>GND</td>
	        <td>-</td>
	    </tr>
	    <tr>
	        <td colspan="3">绿色 LED (+) 引脚</td>
	        <td>17</td>
	        <td>17</td>
	    </tr>
	    <tr>
	        <td colspan="3">绿色 LED (-) 引脚 </td>
	        <td>GND</td>
	        <td>-</td>
	    </tr>
	</table>
</div>

#### 7.1.1.3 执行方法
1. 将以下源代码复制到 Arduino IDE 中，并将文件保存为 "irSensor_LED.ino"。
    
   **注意：** 以下源代码仅在本文档中提供。 

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
2. 验证 "irSensor_LED.ino" 文件并将其上传到 VCP-G。
3. 如果上传过程卡在无限上传状态，则是因为未激活 FWDN 模式。解决方法如下：  
    1. 从 VCP-G 开发板上拔下电源线。
    2. 按住 FWDN 开关。
    3. 在持续按住 FWDN 开关的同时重新连接电源线。
    4. 松开 FWDN 开关。
        如果问题仍然存在，请尝试以管理员权限运行 Arduino IDE。
4. 成功上传文件后，在 Arduino IDE 输出控制台中查看以下消息：
 
    **注意：** 消息中应包含 **irSensor_LED.ino.rom**。
    ```
    [FWDN_VCP::WriteFile:577] Complete to send file - C:\Users\topst\AppData\Local\arduino\sketches\1D003A72AB3391D6D60FD7993380F8CD/irSensor_LED.ino.rom 

    [main:155] Complete FWDN
    ```
</br></br>

### 7.1.2 红外 (IR) 传感器 2
---
本示例演示 VCP-G 开发板如何控制 IR 传感器以检测物体，并将检测状态打印到串口监视器。IR 收发器读取障碍物的有无。如果 IR 收发器的值为 HIGH，表示没有障碍物，绿色 LED 点亮，红色 LED 熄灭。相反，如果 IR 收发器的值为 LOW，表示存在障碍物，红色 LED 点亮，绿色 LED 熄灭。此外，障碍物的有无会显示在串口监视器上。

#### 7.1.2.1 硬件要求
- VCP-G 开发板 (x1)
- IR 收发传感器 (x1)
- 12V 1A 电源适配器 (x1)
- USB Type-C 转 A 线缆 (x1)
- 公对母跳线 (x3)

#### 7.1.2.2 电路
- IR 收发传感器
    - IR 收发传感器的 Out 引脚连接到 VCP-G 开发板上的 8 号引脚。 
    - IR 收发传感器的 VCC 引脚连接到 VCP-G 开发板上的 5V。
    - IR 收发传感器的 GND 引脚连接到 VCP-G 开发板上的 GND。

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/Infrared%20(IR)%20Sensor%20(Transceiver)%20Circuit%20Schematic.png"></p>
<p align="center"><strong>图 7.2 红外 (IR) 传感器（收发器）电路原理图</strong></p>

##### 7.1.2.2.1 引脚图
下表显示了引脚映射。

<p align="center"><strong>表 7.2 irTransceiver 的引脚图</strong></p>
<div align="center">
	<table>
	    <tr>
	        <th colspan="3">引脚名称</th>
	        <th>VCP-G 开发板</th>
	        <th>Arduino IDE</th>
	    </tr>
	    <tr>
	        <td colspan="3">IR 收发传感器 OUT 引脚</td>
	        <td>8</td>
	        <td>8</td>
	    </tr>
	    <tr>
	        <td colspan="3">IR 收发传感器 VCC 引脚</td>
	        <td>5V</td>
	        <td>-</td>
	    </tr>
	    <tr>
	        <td colspan="3">IR 收发传感器 GND 引脚</td>
	        <td>GND</td>
	        <td>-</td>
	    </tr>
	</table>
</div>

#### 7.1.2.3 执行方法
1. 将以下源代码复制到 Arduino IDE 中，并将文件保存为 "irTransceiver.ino"。
   
   **注意：** 以下源代码仅在本文档中提供。 

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
2. 验证 "irTransceiver.ino" 文件并将其上传到 VCP-G。
3. 如果上传过程卡在无限上传状态，则是因为未激活 FWDN 模式。解决方法如下：  
    1. 从 VCP-G 开发板上拔下电源线。
    2. 按住 FWDN 开关。
    3. 在持续按住 FWDN 开关的同时重新连接电源线。
    4. 松开 FWDN 开关。
        如果问题仍然存在，请尝试以管理员权限运行 Arduino IDE。
4. 成功上传文件后，在 Arduino IDE 输出控制台中查看以下消息：
   
    **注意：** 消息中应包含 **irTransceiver.ino.rom**。
    ```
    [FWDN_VCP::WriteFile:577] Complete to send file - C:\Users\topst\AppData\Local\arduino\sketches\1D003A72AB3391D6D60FD7993380F8CD/irTransceiver.ino.rom 

    [main:155] Complete FWDN
    ```

</br></br></br>

## 7.2 摇杆
---
本示例说明 VCP-G 如何读取摇杆输入并将其值显示在串口监视器上。您可以接收三种输入：X 轴、Y 轴和按钮。串口监视器用于验证接收到的信号。在 X 轴和 Y 轴上的移动会改变端口的值，该值对应于模拟输出的数值。这使得需要精细调节的应用能够实现精确控制。

**注意：** Dual Axis Joystick Module (KY-023) 是 Joy-IT 的产品。其设计、商标及相关知识产权的所有权利均归 Joy-IT 所有。
</br></br>

### 7.2.1 硬件要求
- VCP-G 开发板 (x1)
- Dual Axis Joystick Module (KY-023) (x1)
- 12V 1A 电源适配器 (x1)
- USB Type-C 转 A 线缆 (x1)
- 公对母跳线 (x5)
</br></br>

### 7.2.2 电路
- KY-023 (Dual Axis Joystick Module)
    - KY-023 的 5V 引脚连接到 VCP-G 开发板上的 5V。
    - KY-023 的 GND 引脚连接到 VCP-G 开发板上的 GND。 
    - KY-023 的 VRx 引脚连接到 VCP-G 开发板上的模拟引脚 A5。 
    - KY-023 的 VRy 引脚连接到 VCP-G 开发板上的模拟引脚 A4。 
    - KY-023 的 SW 引脚连接到 VCP-G 开发板上的 2 号引脚。

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/Joystick%20Circuit%20Schematic.png"></p>
<p align="center"><strong>图 7.3 摇杆电路原理图</strong></p>

#### 7.2.2.1 引脚图
下表显示了引脚映射。

<p align="center"><strong>表 7.3 摇杆的引脚图</strong></p>
<div align="center">
	<table>
	    <tr>
	        <th colspan="3">引脚名称</th>
	        <th>VCP-G 开发板</th>
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

### 7.2.3 执行方法
1. 将以下源代码复制到 Arduino IDE 中，并将文件保存为 "joystick.ino"。
   
   **注意：** 以下源代码仅在本文档中提供。 

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
2. 验证 "joystick.ino" 文件并将其上传到 VCP-G。
3. 如果上传过程卡在无限上传状态，则是因为未激活 FWDN 模式。解决方法如下：  
    1. 从 VCP-G 开发板上拔下电源线。
    2. 按住 FWDN 开关。
    3. 在持续按住 FWDN 开关的同时重新连接电源线。
    4. 松开 FWDN 开关。  
        如果问题仍然存在，请尝试以管理员权限运行 Arduino IDE。
4. 成功上传文件后，在 Arduino IDE 输出控制台中查看以下消息：
   
    **注意：** 消息中应包含 **joystick.ino.rom**。
    ```
    [FWDN_VCP::WriteFile:577] Complete to send file - C:\Users\topst\AppData\Local\arduino\sketches\1D003A72AB3391D6D60FD7993380F8CD/joystick.ino.rom 

    [main:155] Complete FWDN
    ```

</br></br></br>

## 7.3 气体传感器
---
本示例演示 VCP-G 开发板如何使用气体传感器 (MQ 135) 检测空气中的各种有害气体。它从连接到 VCP-G 开发板模拟引脚的传感器读取模拟值，将其转换为电压，然后以一位小数打印到串口监视器。

**注意：** Gas Sensor (MQ-135) 是 Winsen® 的产品。其设计、商标及相关知识产权的所有权利均归 Winsen 所有。
</br></br>

### 7.3.1 硬件要求
- VCP-G 开发板 (x1)
- 气体传感器 (MQ135) (x1)
- 12V 1A 电源适配器 (x1)
- USB Type-C 转 A 线缆 (x1)
- 公对母跳线 (x3)
</br></br>

### 7.3.2 电路
- 气体传感器
    - 气体传感器的 A0 引脚连接到 VCP-G 开发板上的模拟引脚 A5。 
    - 气体传感器的 VCC 引脚连接到 VCP-G 开发板上的 5V。
    - 气体传感器的 GND 引脚连接到 VCP-G 开发板上的 GND。


<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/Gas%20Sensor%20Circuit%20Schematic.png"></p>
<p align="center"><strong>图 7.4 气体传感器电路原理图</strong></p>

#### 7.3.2.1 引脚图
下表显示了引脚映射。

<p align="center"><strong>表 7.4 气体传感器的引脚图</strong></p>
<div align="center">
	<table>
	    <tr>
	        <th colspan="3">引脚名称</th>
	        <th>VCP-G 开发板</th>
	        <th>Arduino IDE</th>
	    </tr>
	    <tr>
	        <td colspan="3">气体传感器 A0 引脚</td>
	        <td>A5</td>
	        <td>A5</td>
	    </tr>
	        <tr>
	        <td colspan="3">气体传感器 VCC 引脚</td>
	        <td>5V</td>
	        <td>-</td>
	    </tr>
	    <tr>
	        <td colspan="3">气体传感器 GND 引脚</td>
	        <td>GND</td>
	        <td>-</td>
	    </tr>
	</table>
</div>
</br></br>

### 7.3.3 执行方法
1. 将以下源代码复制到 Arduino IDE 中，并将文件保存为 "GasSensor.ino"。
  
   **注意：** 以下源代码仅在本文档中提供。 

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
2. 验证 "GasSensor.ino" 文件并将其上传到 VCP-G。
3. 如果上传过程卡在无限上传状态，则是因为未激活 FWDN 模式。解决方法如下：  
    1. 从 VCP-G 开发板上拔下电源线。
    2. 按住 FWDN 开关。
    3. 在持续按住 FWDN 开关的同时重新连接电源线。
    4. 松开 FWDN 开关。  
        如果问题仍然存在，请尝试以管理员权限运行 Arduino IDE。
4. 成功上传文件后，在 Arduino IDE 输出控制台中查看以下消息：
   
    **注意：** 消息中应包含 **GasSensor.ino.rom**。
    ```
    [FWDN_VCP::WriteFile:577] Complete to send file - C:\Users\topst\AppData\Local\arduino\sketches\1D003A72AB3391D6D60FD7993380F8CD/joystick.ino.rom 

    [main:155] Complete FWDN
    ```
</br></br></br>

## 7.4 金属触摸传感器模块
---
本示例程序演示 VCP-G 开发板如何控制面包板上的触摸传感器和一个 LED。金属触摸传感器模块 (KY-036) 是一款多用途模拟/数字传感器，设计用于检测对金属表面或人体皮肤的触摸。该模块使用晶体管感知触摸时电导率的变化，并同时输出数字和模拟信号以便与 VCP-G 交互。  
检测到触摸时，金属触摸传感器模块会将相应的数字/模拟值输出到串口监视器。您还可以根据触摸状态控制 LED。 

**注意：** 金属触摸传感器模块 (KY-036) 内置用于调节灵敏度的电位器。您可以旋转该电位器来提高或降低灵敏度。
</br></br>

### 7.4.1 硬件要求
- VCP-G 开发板 (x1)
- 面包板 (x1)
- 金属触摸传感器模块 (KY-036) (x1)
- LED (x1)
- 220Ω 电阻 (x1)
- 12V 1A 电源适配器 (x1)
- USB Type-C 转 A 线缆 (x1)
- 公对公跳线 (x4)
- 公对母跳线（x4）
</br></br>

### 7.4.2 电路
- 金属触摸传感器模块
    - 金属触摸传感器模块的 A0 引脚连接到 VCP-G 开发板上的模拟引脚 A5。
    - 金属触摸传感器模块的 G 引脚连接到 VCP-G 开发板上的 GND。
    - Metal Touch 传感器模块的 (+) 引脚连接到 VCP-G 开发板的 5V。
    - Metal Touch 传感器模块的 D0 引脚连接到 VCP-G 开发板的 30 号引脚。

- LED
    - LED 的 (+) 引脚连接到 VCP-G 开发板的 13 号引脚。
    - LED 的 (-) 引脚通过一个 220Ω 电阻连接到 VCP-G 开发板的 GND。


<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/Metal%20Touch%20Sensor%20Circuit%20Schematic.png"></p>
<p align="center"><strong>图 7.5 Metal Touch 传感器电路原理图</strong></p>

#### 7.4.2.1 引脚映射
下表显示了引脚映射。

<p align="center"><strong>表 7.5 Metal Touch 传感器的引脚映射</strong></p>
<div align="center">
	<table>
	    <tr>
	        <th colspan="3">引脚名称</th>
	        <th>VCP-G 开发板</th>
	        <th>Arduino IDE</th>
	    </tr>
	    <tr>
	        <td colspan="3">Metal Touch 传感器模块 A0 引脚</td>
	        <td>A5</td>
	        <td>A5</td>
	    </tr>
	        <tr>
	        <td colspan="3">Metal Touch 传感器模块 G 引脚</td>
	        <td>GND</td>
	        <td>-</td>
	    </tr>
	    <tr>
	        <td colspan="3">Metal Touch 传感器模块 (+) 引脚</td>
	        <td>5V</td>
		    <td>-</td>
		</tr>
	    <tr>
	        <td colspan="3">Metal Touch 传感器模块 D0 引脚</td>
	        <td>30</td>
	        <td>30</td>
	    </tr>
	    <tr>
	        <td colspan="3">LED (+) 引脚</td>
	        <td>13</td>
	        <td>13</td>
	    </tr>
	    <tr>
	        <td colspan="3">LED (+) 引脚</td>
	        <td>GND</td>
	        <td>-</td>
	    </tr>
	</table>
</div>
</br></br>

### 7.4.3 执行方法
1. 将以下源代码复制到 Arduino IDE 中，并将文件保存为 "vcp_touch.ino"。  

   **注意：** 以下源代码仅在本文档中提供。 

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
2. 验证 "vcp_touch.ino" 文件并将其上传到 VCP-G。
3. 如果上传过程卡在无限上传状态，则是因为未激活 FWDN 模式。解决方法如下：  
    1. 从 VCP-G 开发板上拔下电源线。
    2. 按住 FWDN 开关。
    3. 在持续按住 FWDN 开关的同时重新连接电源线。
    4. 松开 FWDN 开关。  
        如果问题仍然存在，请尝试以管理员权限运行 Arduino IDE。
4. 成功上传文件后，在 Arduino IDE 输出控制台中查看以下消息：
   
    **注意：** 该消息应包含 **vcp_touch.ino.rom**。
    ```
    [FWDN_VCP::WriteFile:577] Complete to send file - C:\Users\topst\AppData\Local\arduino\sketches\567805554B5B9F915DCC80B38483AE07/vcp_touch.ino.rom

    [main:155] Complete FWDN
    ```

**注意：** 请为串行通信设置合适的波特率。

</br></br></br>

## 7.5 使用电机驱动器的步进电机
---
本示例演示 VCP-G 开发板如何控制四线步进电机 (28BYJ-48 (5VDC)) 和电机驱动器 (ULN2003 (5V–12V))。第 7.5.3 章中的代码定义了连接到电机驱动器的引脚，并设置了每转的步数。电机先正向旋转一整圈，暂停，然后反向旋转一整圈，再次暂停。电机速度由步进之间的延时控制，旋转方向由线圈的通电顺序控制。

**注意：** 28BYJ-48 电机在 Half step 模式下旋转一整圈需要 4096 个信号，在 Full step 模式下旋转一整圈需要 2048 个信号。为实现精确的电机控制，应考虑不同模式下所需的信号数量。 
</br></br>

### 7.5.1 硬件要求
- VCP-G 开发板 (x1)
- 步进电机 (28BYJ-48) (x1)
- 电机驱动器 (ULN2003) (x1)
- 12V 1A 电源适配器 (x1)
- USB Type-C 转 A 线缆 (x1)
- 公对公跳线（x6）
</br></br>

### 7.5.2 电路
- 电机驱动器
    - IN1 引脚连接到 VCP-G 开发板的 8 号引脚。
    - IN2 引脚连接到 VCP-G 开发板的 9 号引脚。
    - IN3 引脚连接到 VCP-G 开发板的 10 号引脚。
    - IN4 引脚连接到 VCP-G 开发板的 11 号引脚。
    - (+) 引脚连接到 VCP-G 开发板的 5V。
    - (-) 引脚连接到 VCP-G 开发板的 GND。

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/Step%20Motor%20with%20Motor%20Driver%20Circuit%20Schematic.png"></p>
<p align="center"><strong>图 7.6 使用电机驱动器的步进电机电路原理图</strong></p>

#### 7.5.2.1 引脚映射
下表显示了引脚映射。

<p align="center"><strong>表 7.6 电机驱动器的引脚映射</strong></p>
<div align="center">
	<table>
	    <tr>
	        <th colspan="3">引脚名称</th>
	        <th>VCP-G 开发板</th>
	        <th>Arduino IDE</th>
	    </tr>
	    <tr>
	        <td colspan="3">电机驱动器 IN1 引脚</td>
	        <td>8</td>
	        <td>8</td>
	    </tr>
	        <tr>
	        <td colspan="3">电机驱动器 IN2 引脚</td>
	        <td>9</td>
	        <td>9</td>
	    </tr>
	    <tr>
	        <td colspan="3">电机驱动器 IN3 引脚</td>
	        <td>10</td>
	        <td>10</td>
		</tr>
	    <tr>
	        <td colspan="3">电机驱动器 IN4 引脚</td>
		    <td>11</td>
			<td>11</td>
	    </tr>
		<tr>
			<td colspan="3">电机驱动器 (+) 引脚</td>
	        <td>5V</td>
	        <td>-</td>
		</tr>
	    <tr>
	        <td colspan="3">电机驱动器 (-) 引脚</td>
	        <td>GND</td>
	        <td>-</td>
	    </tr>
	</table>
</div>
</br></br>

### 7.5.3 执行方法
1. 将以下源代码复制到 Arduino IDE 中，并将文件保存为 "motordriver.ino"。

    **注意：** 以下源代码仅在本文档中提供。 

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
2. 验证 "motordriver.ino" 文件并将其上传到 VCP-G。
3. 如果上传过程卡在无限上传状态，则是因为未激活 FWDN 模式。解决方法如下：  
    1. 从 VCP-G 开发板上拔下电源线。
    2. 按住 FWDN 开关。
    3. 在持续按住 FWDN 开关的同时重新连接电源线。
    4. 松开 FWDN 开关。  
        如果问题仍然存在，请尝试以管理员权限运行 Arduino IDE。
4. 成功上传文件后，请在 Arduino IDE 输出控制台中查看以下消息：  

    **注意：** 该消息应包含 **motordriver.ino.rom**。
    ```
    [FWDN_VCP::WriteFile:577] Complete to send file - C:\Users\topst\AppData\Local\arduino\sketches\567805554B5B9F915DCC80B38483AE07/motordriver.rom

    [main:155] Complete FWDN
    ```
</br></br></br></br>

# 8. 参考资料
---
- 有关更多详细信息，请联系 TOPST：topst@topst.ai

**注意：** 参考文档可根据合同条款在可提供时提供。如果参考
文档无法提供，则可就与您的开发直接相关的内容提供指导。
