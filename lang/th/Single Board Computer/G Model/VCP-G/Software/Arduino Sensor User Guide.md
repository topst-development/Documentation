# 1. บทนำ
---
เอกสารนี้ให้แนวทางการใช้งานเซ็นเซอร์ Arduino ต่าง ๆ ร่วมกับบอร์ด VCP-G โดยมีคำแนะนำการเชื่อมต่อและโค้ดตัวอย่างเพื่อช่วยให้ท่านพัฒนาโปรเจกต์ด้วย VCP-G ได้อย่างง่ายดาย

โดยเฉพาะอย่างยิ่ง เอกสารนี้ให้คำแนะนำเกี่ยวกับตัวอย่าง Arduino IDE สำหรับ VCP-G ซึ่งประกอบด้วย:  
- VCP-G Digital
- VCP-G Analog
- VCP-G SPI
- VCP-G I2C
- VCP-G UART
- Additional Example

โปรดดูรูปที่ 1.1 ก่อนใช้งาน VCP-G

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/vcp-g%20pinout%20Diagram.png"></p>
<p align="center"><strong>รูปที่ 1.1 แผนผังพินของ VCP-G</strong></p>

</br></br></br></br>

# 2. พินดิจิทัลของ VCP-G
---
บทนี้ให้ตัวอย่างการควบคุม LED โดยใช้พินดิจิทัลของบอร์ด VCP-G ใน VCP-G พินดิจิทัลใช้สำหรับส่งหรือรับสัญญาณไบนารี (HIGH หรือ LOW) จึงมีความสำคัญอย่างยิ่งต่อการควบคุมชิ้นส่วนต่าง ๆ เช่น LED สวิตช์ และเซ็นเซอร์ 

บทนี้ประกอบด้วยโปรเจกต์ตัวอย่างสองโปรเจกต์ที่แสดงวิธีใช้เอาต์พุตดิจิทัลเพื่อควบคุม LED หลายดวง ซึ่งช่วยให้เข้าใจพื้นฐานการทำงานของพินดิจิทัล

</br></br></br>

## 2.1 vcp4LED
---
โปรแกรมตัวอย่างนี้แสดงวิธีที่บอร์ด VCP-G ควบคุม LED สี่ดวงบนเบรดบอร์ด โค้ดตัวอย่างมีให้ในไฟล์ “vcp4LED.ino” เมื่ออัปโหลดไฟล์นี้ไปยัง VCP-G ไฟ LED จะติดและดับตามลำดับทั้งรูปแบบไปข้างหน้าและย้อนกลับ โดยมีการหน่วงเวลา 500 ms ระหว่างการเปลี่ยนแต่ละครั้ง 

</br></br>

### 2.1.1 ข้อกำหนดฮาร์ดแวร์  
- บอร์ด VCP-G (x1)
- เบรดบอร์ด (x1)
- LED (x4)
- ตัวต้านทาน 220Ω (x4)
- อะแดปเตอร์จ่ายไฟ 12V 1A (x1)
- สาย USB Type-C to A (x1) 
- สายจัมเปอร์ตัวผู้-ตัวผู้ (x9)
</br></br>

### 2.1.2 วงจร
- LED01
    - พิน (+) เชื่อมต่อกับรางไฟ 5V บนเบรดบอร์ดผ่านตัวต้านทาน 220Ω ซึ่งจ่ายไฟโดยบอร์ด VCP-G
    - พิน (-) เชื่อมต่อกับพิน 47 บนบอร์ด VCP-G
- LED02
    - พิน (+) เชื่อมต่อกับรางไฟ 5V บนเบรดบอร์ดผ่านตัวต้านทาน 220Ω
    - พิน (-) เชื่อมต่อกับพิน 17 บนบอร์ด VCP-G
- LED03
    - พิน (+) เชื่อมต่อกับรางไฟ 5V บนเบรดบอร์ดผ่านตัวต้านทาน 220Ω
    - พิน (-) เชื่อมต่อกับพิน 50 บนบอร์ด VCP-G
- LED04
    - พิน (+) เชื่อมต่อกับรางไฟ 5V บนเบรดบอร์ดผ่านตัวต้านทาน 220Ω
    - พิน (-) เชื่อมต่อกับพิน 48 บนบอร์ด VCP-G  

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/vcp4LED%20Circuit%20Schematic.png"></p>
<p align="center"><strong>รูปที่ 2.1 ผังวงจรของ vcp4LED</strong></p>

#### 2.1.2.1 การแมปพิน
ตารางต่อไปนี้แสดงการแมปพิน

<p align="center"><strong>ตารางที่ 2.1 การแมปพินของ vcp4LED</strong></p>
<div align="center">	
	<table>
		<tr>
			<th colspan="3">ชื่อพิน</th>
	        <th>บอร์ด VCP-G</th>
	        <th>Arduino IDE</th>
	    </tr>
	    <tr>
	        <td colspan="3">พิน (-) ของ LED01</td>
	        <td>47</td>
	        <td>47</td>
	    </tr>
	        <tr>
	        <td colspan="3">พิน (-) ของ LED02</td>
	        <td>17</td>
	        <td>17</td>
	    </tr>
	        <tr>
	        <td colspan="3">พิน (-) ของ LED03</td>
	        <td>50</td>
	        <td>50</td>
	    </tr>
	        <tr>
	        <td colspan="3">พิน (-) ของ LED04</td>
	        <td>48</td>
	        <td>48</td>
	    </tr>
	</table>
</div>
</br></br>

### 2.1.3 วิธีการดำเนินการ
1. เปิดไฟล์ "vcp4LED.ino"  
    1. เปิด Arduino IDE
    2. คลิก **File -> Examples -> 01.VCP-G Digital -> vcp4LED**
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
2. ตรวจสอบและอัปโหลดไฟล์ "vcp4LED.ino" ไปยัง VCP-G
3. หากกระบวนการอัปโหลดค้างอยู่ในสถานะกำลังอัปโหลดไม่สิ้นสุด แสดงว่าโหมด FWDN ยังไม่ถูกเปิดใช้งาน วิธีแก้ไขมีดังนี้:  
    1. ถอดสายไฟออกจากบอร์ด VCP-G
    2. กดสวิตช์ FWDN ค้างไว้
    3. เชื่อมต่อสายไฟอีกครั้งขณะที่ยังกดสวิตช์ FWDN ค้างไว้
    4. ปล่อยสวิตช์ FWDN
        หากยังพบปัญหาอยู่ ให้ลองเรียกใช้ Arduino IDE ด้วยสิทธิ์ผู้ดูแลระบบ
4. หลังจากอัปโหลดไฟล์สำเร็จแล้ว ให้ตรวจสอบข้อความต่อไปนี้ในคอนโซลเอาต์พุตของ Arduino IDE:  

     **หมายเหตุ:** ข้อความควรมี **vcp4LED.ino.rom** รวมอยู่ด้วย
    ```
    [FWDN_VCP::WriteFile:577] Complete to send file - C:\Users\topst\AppData\Local\arduino\sketches\C05357299384CE5734F0E696C5A4DA3B/vcp4LED.ino.rom

    [main:155] Complete FWDN
    ```

</br></br></br>

## 2.2 vcp4LED_Button
---
โปรแกรมตัวอย่างนี้แสดงวิธีที่บอร์ด VCP-G ควบคุม LED สี่ดวงและปุ่มกดหนึ่งปุ่มบนเบรดบอร์ด เมื่อกดปุ่ม LED สองดวงทางขวาจะดับ และ LED สองดวงทางซ้ายจะติด เมื่อปล่อยปุ่ม LED ที่ติดอยู่จะดับ และ LED ที่ดับอยู่จะติด โปรแกรมจะตรวจสอบสถานะของปุ่มอย่างต่อเนื่องและปรับการทำงานของ LED ตามนั้น
</br></br>

### 2.2.1 ข้อกำหนดฮาร์ดแวร์
- บอร์ด VCP-G (x1)
- เบรดบอร์ด (x1)
- LED (x4)
- สวิตช์ปุ่มกด (เซ็นเซอร์) (x1)
- ตัวต้านทาน 220Ω (x4)
- อะแดปเตอร์จ่ายไฟ 12V 1A (x1)
- สาย USB Type-C to A (x1)
- สายจัมเปอร์ตัวผู้-ตัวผู้ (x12)
</br></br>

### 2.2.2 วงจร
1.	LED01
    - พิน (+) เชื่อมต่อกับรางไฟ 5V บนเบรดบอร์ดผ่านตัวต้านทาน 220Ω ซึ่งจ่ายไฟโดยบอร์ด VCP-G
    - พิน (-) เชื่อมต่อกับพิน 47 บนบอร์ด VCP-G
2.	LED02
    - พิน (+) เชื่อมต่อกับรางไฟ 5V บนเบรดบอร์ดผ่านตัวต้านทาน 220Ω
    - พิน (-) เชื่อมต่อกับพิน 17 บนบอร์ด VCP-G
3.	LED03
    - พิน (+) เชื่อมต่อกับรางไฟ 5V บนเบรดบอร์ดผ่านตัวต้านทาน 220Ω
    - พิน (-) เชื่อมต่อกับพิน 50 บนบอร์ด VCP-G
4.	LED04
    - พิน (+) เชื่อมต่อกับรางไฟ 5V บนเบรดบอร์ดผ่านตัวต้านทาน 220Ω
    - พิน (-) เชื่อมต่อกับพิน 48 บนบอร์ด VCP-G
5.	สวิตช์ปุ่มกด
    - ขาข้างหนึ่งของสวิตช์ปุ่มกดเชื่อมต่อกับพิน 45 บนบอร์ด VCP-G
    - ขาที่อยู่ตรงข้ามในแนวทแยงของปุ่มเชื่อมต่อกับพิน GND

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/vcp4LED_Button%20Circuit%20Schematic.png"></p>
<p align="center"><strong>รูปที่ 2.2 ผังวงจรของ vcp4LED_Button</strong></p>

#### 2.2.2.1 การแมปพิน
ตารางต่อไปนี้แสดงการแมปพิน

<p align="center"><strong>ตารางที่ 2.2 การแมปพินของ vcp4LED_Button</strong></p>
<div align="center">
	<table>
	    <tr>
	        <th colspan="3">ชื่อพิน</th>
	        <th>บอร์ด VCP-G</th>
	        <th>Arduino IDE</th>
	    </tr>
	    <tr>
	        <td colspan="3">พิน (-) ของ LED01</td>
	        <td>47</td>
	        <td>47</td>
	    </tr>
	        <tr>
	        <td colspan="3">พิน (-) ของ LED02</td>
	        <td>17</td>
	        <td>17</td>
	    </tr>
	        <tr>
	        <td colspan="3">พิน (-) ของ LED03</td>
	        <td>50</td>
	        <td>50</td>
	    </tr>
	        <tr>
	        <td colspan="3">พิน (-) ของ LED04</td>
	        <td>48</td>
	        <td>48</td>
	    </tr>
	    </tr>
	        <tr>
	        <td colspan="3">พินขาข้างหนึ่งของปุ่ม</td>
	        <td>45</td>
	        <td>45</td>
	    </tr>
	</table>
</div>
</br></br>

### 2.1.3 วิธีการดำเนินการ
1. เปิดไฟล์ "vcp4LED_Button.ino"
    1. เปิด Arduino IDE
    2. คลิก **File -> Examples -> 01.VCP-G Digital -> vcp4LED_Button**
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
2. ตรวจสอบและอัปโหลดไฟล์ "vcp4LED_Button.ino" ไปยัง VCP-G
3. หากกระบวนการอัปโหลดค้างอยู่ในสถานะกำลังอัปโหลดไม่สิ้นสุด แสดงว่าโหมด FWDN ยังไม่ถูกเปิดใช้งาน วิธีแก้ไขมีดังนี้:  
    1. ถอดสายไฟออกจากบอร์ด VCP-G
    2. กดสวิตช์ FWDN ค้างไว้
    3. เชื่อมต่อสายไฟอีกครั้งขณะที่ยังกดสวิตช์ FWDN ค้างไว้
    4. ปล่อยสวิตช์ FWDN 
        หากยังพบปัญหาอยู่ ให้ลองเรียกใช้ Arduino IDE ด้วยสิทธิ์ผู้ดูแลระบบ
4. หลังจากอัปโหลดไฟล์สำเร็จแล้ว ให้ตรวจสอบข้อความต่อไปนี้ในคอนโซลเอาต์พุตของ Arduino IDE:  

    **หมายเหตุ:** ข้อความควรมี **vcp4LED_Button.ino.rom** รวมอยู่ด้วย
    ```
    [FWDN_VCP::WriteFile:577] Complete to send file - C:\Users\topst\AppData\Local\arduino\sketches\5CC1DB4CA216E2BC009504FAA3D06456/vcp4LED_Button.ino.rom

    [main:155] Complete FWDN
    ```

</br></br></br></br>

# 3. พินแอนะล็อกของ VCP-G
---
บทนี้ให้ตัวอย่างการใช้งานพินแอนะล็อกบนบอร์ด VCP-G ใน VCP-G พินแอนะล็อกจะรับสัญญาณแรงดันไฟฟ้าแบบต่อเนื่องจากเซ็นเซอร์ ทำให้สามารถวัดค่าอินพุตที่เปลี่ยนแปลงได้อย่างแม่นยำ บทที่ 3.1 บทที่ 3.2 และบทที่ 3.3 อธิบายวิธีใช้พินแอนะล็อกเพื่ออ่านข้อมูลเซ็นเซอร์และควบคุมเอาต์พุต ซึ่งช่วยให้เข้าใจพื้นฐานของการจัดการอินพุตแบบแอนะล็อก

</br></br></br>

## 3.1 AnalogInOutSerial
---
โปรแกรมตัวอย่างนี้แสดงวิธีที่บอร์ด VCP-G ควบคุมโพเทนชิโอมิเตอร์และ LED บนเบรดบอร์ด VCP-G จะอ่านค่าจากพินอินพุตแอนะล็อก แมปผลลัพธ์ไปยังช่วง 0 ถึง 1000 และใช้ค่านี้กำหนดการมอดูเลตความกว้างพัลส์ (PWM) ของพินเอาต์พุต (ที่เชื่อมต่อกับ LED) ผลลัพธ์จะถูกแสดงบน Serial Monitor ด้วย
</br></br>

### 3.1.1 ข้อกำหนดฮาร์ดแวร์
- บอร์ด VCP-G (x1)
- เบรดบอร์ด (x1)
- LED (x1)
- โพเทนชิโอมิเตอร์ (x1)
- ตัวต้านทาน 220Ω (x2)
- อะแดปเตอร์จ่ายไฟ 12V 1A (x1)
- สาย USB Type-C to A (x1)
- สายจัมเปอร์ตัวผู้-ตัวผู้ (x4)
</br></br>

### 3.1.2 วงจร
- โพเทนชิโอมิเตอร์
    - พินกลางของโพเทนชิโอมิเตอร์เชื่อมต่อกับพินแอนะล็อก A5 บนบอร์ด VCP-G
    - พิน GND ของโพเทนชิโอมิเตอร์เชื่อมต่อกับพิน 43 บนบอร์ด VCP-G และเชื่อมต่อกับพิน GND บนบอร์ด VCP-G ผ่านตัวต้านทาน 220Ω
- LED
    - พิน (+) ของ LED เชื่อมต่อกับ 3.3V บนบอร์ด VCP-G ผ่านตัวต้านทาน 220Ω
    - พิน (-) ของ LED เชื่อมต่อกับพินกลางของโพเทนชิโอมิเตอร์

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/AnalogInOutSerial%20Circuit%20Schematic.png"></p>
<p align="center"><strong>รูปที่ 3.1 ผังวงจรของ AnalogInOutSerial</strong></p>

#### 3.1.2.1 การแมปพิน
ตารางต่อไปนี้แสดงการแมปพิน

<p align="center"><strong>ตารางที่ 3.1 การแมปพินของ AnalogInOutSerial</strong></p>
<div align="center">
	<table>
	    <tr>
	        <th colspan="3">ชื่อพิน</th>
	        <th>บอร์ด VCP-G</th>
	        <th>Arduino IDE</th>
	    </tr>
	    <tr>
	        <td colspan="3">พินกลางของโพเทนชิโอมิเตอร์</td>
	        <td>A5</td>
	        <td>-</td>
	    </tr>
	        <tr>
	        <td colspan="3">พิน GND ของโพเทนชิโอมิเตอร์</td>
	        <td>43</td>
	        <td>43</td>
	    </tr>
	        <tr>
	        <td colspan="3">พิน (+) ของ LED</td>
	        <td>3.3V</td>
	        <td>-</td>
	    </tr>
	        <tr>
	        <td colspan="3">พิน (-) ของ LED</td>
	        <td>A5</td>
	        <td>A5</td>
	    </tr>
	</table>
</div>
</br></br>

### 3.1.3 วิธีการดำเนินการ
1. เปิดไฟล์ "AnalogInOutSerial.ino"  
    1. เปิด Arduino IDE
    2. คลิก **File -> Examples -> 02.VCP-G Analog -> AnalogInOutSerial**
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
 
    **หมายเหตุ:** หากเกิดข้อผิดพลาดที่ระบุว่าไม่ได้ประกาศ "Serial" ให้ตรวจสอบว่ามีการรวมไลบรารีและการประกาศออบเจ็กต์ต่อไปนี้อย่างถูกต้อง
    ```
    #include <HardwareSerial.h>
    HardwareSerial Serial;
    ```
2. ตรวจสอบและอัปโหลดไฟล์ "AnalogInOutSerial.ino" ไปยัง VCP-G
3. หากกระบวนการอัปโหลดค้างอยู่ในสถานะกำลังอัปโหลดไม่สิ้นสุด แสดงว่าโหมด FWDN ยังไม่ถูกเปิดใช้งาน วิธีแก้ไขมีดังนี้:  
    1. ถอดสายไฟออกจากบอร์ด VCP-G
    2. กดสวิตช์ FWDN ค้างไว้
    3. เชื่อมต่อสายไฟอีกครั้งขณะที่ยังกดสวิตช์ FWDN ค้างไว้
    4. ปล่อยสวิตช์ FWDN
        หากยังพบปัญหาอยู่ ให้ลองเรียกใช้ Arduino IDE ด้วยสิทธิ์ผู้ดูแลระบบ
4. หลังจากอัปโหลดไฟล์สำเร็จแล้ว ให้ตรวจสอบข้อความต่อไปนี้ในคอนโซลเอาต์พุตของ Arduino IDE:  
 
    **หมายเหตุ:** ข้อความควรมี **AnalogInOutSerial.ino.rom**
    ```
    [FWDN_VCP::WriteFile:577] Complete to send file - C:\Users\topst\AppData\Local\arduino\sketches\EB016432EF98DEF0B9102FD77148DD5D/AnalogInOutSerial.ino.rom

    [main:155] Complete FWDN
    ```

</br></br></br>

## 3.2 AnalogInput
---
โปรแกรมตัวอย่างนี้แสดงวิธีที่บอร์ด VCP-G ควบคุมโพเทนชิโอมิเตอร์และ LED บนเบรดบอร์ด โดยจะอ่านค่าจากขาอินพุตแบบแอนะล็อกและใช้ค่านี้ในการควบคุม LED หากค่าเซ็นเซอร์ต่ำกว่า 3000 LED จะติด หากค่าเซ็นเซอร์เท่ากับหรือสูงกว่า 3000 LED จะดับ
</br></br>

### 3.2.1 ข้อกำหนดฮาร์ดแวร์
- บอร์ด VCP-G (x1)
- เบรดบอร์ด (x1)
- LED (x1)
- โพเทนชิโอมิเตอร์ (x1)
- ตัวต้านทาน 220Ω (x1)
- อะแดปเตอร์จ่ายไฟ 12V 1A (x1)
- สาย USB Type-C to A (x1)
- สายจัมเปอร์แบบผู้-ผู้ (x6)
</br></br>

### 3.2.2 วงจร
- โพเทนชิโอมิเตอร์
    - ขา VCC ของโพเทนชิโอมิเตอร์เชื่อมต่อกับ 3.3V บนบอร์ด VCP-G ผ่านตัวต้านทาน 220Ω
    - พินกลางของโพเทนชิโอมิเตอร์เชื่อมต่อกับพินแอนะล็อก A5 บนบอร์ด VCP-G
    - ขา GND ของโพเทนชิโอมิเตอร์เชื่อมต่อกับขา GND บนบอร์ด VCP-G ผ่านตัวต้านทาน 220Ω
- LED
    - พิน (+) ของ LED เชื่อมต่อกับ 3.3V บนบอร์ด VCP-G ผ่านตัวต้านทาน 220Ω
    - ขา (-) ของ LED เชื่อมต่อกับขา 5 บนบอร์ด VCP-G

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/AnalogInput%20Circuit%20Schematic.png"></p>
<p align="center"><strong>รูปที่ 3.2 แผนผังวงจรของ AnalogInput</strong></p>

#### 3.2.2.1 ผังพิน
ตารางต่อไปนี้แสดงการแมปพิน

<p align="center"><strong>ตารางที่ 3.2 ผังพินของ AnalogInput</strong></p>
<div align="center">
	<table>
	    <tr>
	        <th colspan="3">ชื่อพิน</th>
	        <th>บอร์ด VCP-G</th>
	        <th>Arduino IDE</th>
	    </tr>
	    <tr>
	        <td colspan="3">ขา VCC ของโพเทนชิโอมิเตอร์</td>
	        <td>3.3V</td>
	        <td>-</td>
	    </tr>
	    <tr>
	        <td colspan="3">พินกลางของโพเทนชิโอมิเตอร์</td>
	        <td>A5</td>
	        <td>A5</td>
	    </tr>
	        <tr>
	        <td colspan="3">พิน GND ของโพเทนชิโอมิเตอร์</td>
	        <td>GND</td>
	        <td>-</td>
	    </tr>
	        <tr>
	        <td colspan="3">พิน (+) ของ LED</td>
	        <td>3.3V</td>
	        <td>-</td>
	    </tr>
	        <tr>
	        <td colspan="3">พิน (-) ของ LED</td>
	        <td>5</td>
	        <td>5</td>
	    </tr>
	</table>
</div>
</br></br>

### 3.2.3 วิธีการดำเนินการ
1. เปิดไฟล์ "AnalogInput.ino"  
    1. เปิด Arduino IDE
    2. คลิก **File -> Examples -> 02.VCP-G Analog -> AnalogInput**
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
 
    **หมายเหตุ 1:** หากต้องการตรวจสอบ **sensorValue** ใน Serial Monitor ให้เพิ่ม **Serial.println()** ลงในซอร์สโค้ด  
    **หมายเหตุ 2:** มีการใช้ตัวต้านทานค่าคงที่ร่วมกับตัวต้านทานปรับค่าได้ (โพเทนชิโอมิเตอร์) เพื่อปรับค่าเซ็นเซอร์ ค่าเซ็นเซอร์จะเปลี่ยนแปลงตามระดับการหมุนโพเทนชิโอมิเตอร์ และระดับการหมุนที่ต้องใช้จะแตกต่างกันไปตามค่าของตัวต้านทานค่าคงที่

2. ตรวจสอบและอัปโหลดไฟล์ "AnalogInput.ino" ไปยัง VCP-G
3. หากกระบวนการอัปโหลดค้างอยู่ในสถานะกำลังอัปโหลดไม่สิ้นสุด แสดงว่าโหมด FWDN ยังไม่ถูกเปิดใช้งาน วิธีแก้ไขมีดังนี้:  
    1. ถอดสายไฟออกจากบอร์ด VCP-G
    2. กดสวิตช์ FWDN ค้างไว้
    3. เชื่อมต่อสายไฟอีกครั้งขณะที่ยังกดสวิตช์ FWDN ค้างไว้
    4. ปล่อยสวิตช์ FWDN  
        หากยังพบปัญหาอยู่ ให้ลองเรียกใช้ Arduino IDE ด้วยสิทธิ์ผู้ดูแลระบบ
4. หลังจากอัปโหลดไฟล์สำเร็จแล้ว ให้ตรวจสอบข้อความต่อไปนี้ในคอนโซลเอาต์พุตของ Arduino IDE:  

   **หมายเหตุ:** ข้อความควรมี **AnalogInput.ino.rom**
    ```
    [FWDN_VCP::WriteFile:577] Complete to send file - C:\Users\topst\AppData\Local\arduino\sketches\C3FDEE51354320EA689DFEB4EDCF2ECD/AnalogInput.ino.rom

    [main:155] Complete FWDN
    ```

</br></br></br>

## 3.3 pwmFade
---
โปรแกรมตัวอย่างนี้แสดงวิธีที่บอร์ด VCP-G ควบคุม LED บนเบรดบอร์ดโดยค่อย ๆ เพิ่มและลดความสว่างเป็นวงรอบด้วยการใช้ PWM หลังจาก LED สว่างสูงสุดแล้ว ความสว่างของ LED จะเริ่มลดลง โปรแกรมจะปรับความสว่างของ LED อย่างต่อเนื่อง ทำให้เกิดเอฟเฟกต์การหรี่ไฟ
</br></br>

### 3.3.1 ข้อกำหนดฮาร์ดแวร์
- บอร์ด VCP-G (x1)
- เบรดบอร์ด (x1)
- LED (x1)
- ตัวต้านทาน 220Ω (x1)
- อะแดปเตอร์จ่ายไฟ 12V 1A (x1)
- สาย USB Type-C to A (x1)
- สายจัมเปอร์แบบผู้-ผู้ (x2)
</br></br>

### 3.3.2 วงจร
- LED
    - ขา (+) ของ LED เชื่อมต่อกับ 5V บนบอร์ด VCP-G
    - ขา (-) ของ LED เชื่อมต่อกับขา 9 บนบอร์ด VCP-G ผ่านตัวต้านทาน 220Ω

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/pwmFade%20Circuit%20Schematic.png"></p>
<p align="center"><strong>รูปที่ 3.3 แผนผังวงจรของ pwmFade</strong></p>

#### 3.3.2.1 ผังพิน
ตารางต่อไปนี้แสดงการแมปพิน

<p align="center"><strong>ตารางที่ 3.3 ผังพินของ pwmFade</strong></p>
<div align="center">
	<table>
	    <tr>
	        <th colspan="3">ชื่อพิน</th>
	        <th>บอร์ด VCP-G</th>
	        <th>Arduino IDE</th>
	    </tr>
	    <tr>
	        <td colspan="3">พิน (+) ของ LED</td>
	        <td>5V</td>
	        <td>-</td>
	    </tr>
	        <tr>
	        <td colspan="3">พิน (-) ของ LED</td>
	        <td>9</td>
	        <td>9</td>
	    </tr>
	</table>
</div>
</br></br>

### 3.3.3 วิธีการดำเนินการ
1. เปิดไฟล์ "pwmFade.ino"
    1. เปิด Arduino IDE
    2. คลิก **File -> Examples -> 02.VCP-G Analog -> pwmFade**
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
2. ตรวจสอบและอัปโหลดไฟล์ "pwmFade.ino" ไปยังบอร์ด VCP-G
3. หากกระบวนการอัปโหลดค้างอยู่ในสถานะกำลังอัปโหลดไม่สิ้นสุด แสดงว่าโหมด FWDN ยังไม่ถูกเปิดใช้งาน วิธีแก้ไขมีดังนี้:  
    1. ถอดสายไฟออกจากบอร์ด VCP-G
    2. กดสวิตช์ FWDN ค้างไว้
    3. เชื่อมต่อสายไฟอีกครั้งขณะที่ยังกดสวิตช์ FWDN ค้างไว้
    4. ปล่อยสวิตช์ FWDN
        หากยังพบปัญหาอยู่ ให้ลองเรียกใช้ Arduino IDE ด้วยสิทธิ์ผู้ดูแลระบบ
4. หลังจากอัปโหลดไฟล์สำเร็จแล้ว ให้ตรวจสอบข้อความต่อไปนี้ในคอนโซลเอาต์พุตของ Arduino IDE:  

     **หมายเหตุ:** ข้อความควรมี **pwmFade.ino.rom**
    ```
    [FWDN_VCP::WriteFile:577] Complete to send file - C:\Users\topst\AppData\Local\arduino\sketches\69446E8A7F6616A7D5466014BDF759FC/pwmFade.ino.rom 

    [main:155] Complete FWDN
    ```

</br></br></br></br>

# 4. VCP SPI
---
บทนี้ให้คำแนะนำสำหรับการกำหนดค่าการสื่อสารแบบ Serial Peripheral Interface (SPI) บน VCP-G  
SPI เป็นโปรโตคอลการสื่อสารแบบซิงโครนัสความเร็วสูงที่ใช้แลกเปลี่ยนข้อมูลระหว่างไมโครคอนโทรลเลอร์กับอุปกรณ์ต่อพ่วง โดยทำงานด้วยสายสัญญาณแยกกันสำหรับการส่งข้อมูล (MOSI และ MISO) การซิงโครไนซ์สัญญาณนาฬิกา (SCK) และการเลือกอุปกรณ์ (SS) ซึ่งช่วยให้การสื่อสารมีประสิทธิภาพและเชื่อถือได้  
บทต่อไปนี้อธิบายวิธีตั้งค่าและใช้งาน SPI เพื่อเชื่อมต่อกับอุปกรณ์ภายนอก

</br></br></br>

## 4.1 vcpSPI_Dot8x8
---
โปรแกรมตัวอย่างนี้แสดงวิธีที่บอร์ด VCP-G ควบคุม LED ดอตเมทริกซ์ขนาด 8x8 โดยใช้ไดรเวอร์ MAX7219 LED ดอตเมทริกซ์ขนาด 8x8 จะแสดงรูปแบบต่าง ๆ เช่น รูปหัวใจและตัวอักษร "R" โดยการกำหนดค่าแต่ละแถวด้วยอาร์เรย์ไบนารีที่กำหนดไว้ล่วงหน้า ความเข้มของ LED จะถูกปรับเพื่อสร้างเอฟเฟกต์การเต้นเป็นจังหวะ ซึ่งเพิ่มความน่าสนใจทางภาพแบบไดนามิก คุณสมบัติเพิ่มเติมได้แก่ การกลับสีและการล้างหน้าจอเพื่อเพิ่มความสามารถในการใช้งาน
</br></br>

### 4.1.1 ข้อกำหนดฮาร์ดแวร์
- บอร์ด VCP-G (x1)
- ดอตเมทริกซ์ขนาด 8x8 (x1)
- อะแดปเตอร์จ่ายไฟ 12V 1A (x1)
- สาย USB Type-C to A (x1)
- สายจัมเปอร์ผู้-เมีย (x5)
</br></br>

### 4.1.2 วงจร
- ดอตเมทริกซ์ 8x8
    - ขา VCC ของดอตเมทริกซ์ขนาด 8x8 เชื่อมต่อกับขาแอนะล็อก 5V บนบอร์ด VCP-G
    - ขา GND ของดอตเมทริกซ์ขนาด 8x8 เชื่อมต่อกับ GND บนบอร์ด VCP-G
    - ขา DIN ของดอตเมทริกซ์ขนาด 8x8 เชื่อมต่อกับขา 11 บนบอร์ด VCP-G
    - ขา CS ของดอตเมทริกซ์ขนาด 8x8 เชื่อมต่อกับขา 10 บนบอร์ด VCP-G
    - ขา CLS ของดอตเมทริกซ์ขนาด 8x8 เชื่อมต่อกับขา 13 บนบอร์ด VCP-G

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/vcpSPI_Dot8x8%20Circuit%20Schematic.png"></p>
<p align="center"><strong>รูปที่ 4.1 แผนผังวงจรของ vcpSPI_Dot8x8</strong></p>

#### 4.1.2.1 ผังพิน
ตารางต่อไปนี้แสดงการแมปพิน

<p align="center"><strong>ตารางที่ 4.1 ผังพินของ vcpSPI_Dot8x8</strong></p>
<div align="center">
	<table>
	    <tr>
	        <th colspan="3">ชื่อพิน</th>
	        <th>บอร์ด VCP-G</th>
	        <th>Arduino IDE</th>
	    </tr>
	    <tr>
	        <td colspan="3">ขา VCC ของดอตเมทริกซ์ 8x8</td>
	        <td>5V</td>
	        <td>-</td>
	    </tr>
	        <tr>
	        <td colspan="3">ขา GND ของดอตเมทริกซ์ 8x8</td>
	        <td>GND</td>
	        <td>-</td>
	    </tr>
	    <tr>
	        <td colspan="3">ขา DIN ของดอตเมทริกซ์ 8x8</td>
	        <td>11</td>
	        <td>11</td>
	    </tr>
	    <tr>
	        <td colspan="3">ขา CS ของดอตเมทริกซ์ 8x8</td>
	        <td>10</td>
	        <td>10</td>
	    </tr>
	    <tr>
	        <td colspan="3">ขา CLK ของดอตเมทริกซ์ 8x8</td>
	        <td>13</td>
	        <td>13</td>
	    </tr>
	</table>
</div>
</br></br>

### 4.1.3 วิธีการดำเนินการ
1. เปิดไฟล์ "vcpSPI_Dot8x8.ino"  
    1. เปิด Arduino IDE
    2. คลิก **File -> Examples -> 03.VCP-G SPI -> vcpSPI_Dot8x8**
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
2. ตรวจสอบและอัปโหลดไฟล์ "vcpSPI_Dot8x8.ino" ไปยัง VCP-G
3. หากกระบวนการอัปโหลดค้างอยู่ในสถานะกำลังอัปโหลดไม่สิ้นสุด แสดงว่าโหมด FWDN ยังไม่ถูกเปิดใช้งาน วิธีแก้ไขมีดังนี้:  
    1. ถอดสายไฟออกจากบอร์ด VCP-G
    2. กดสวิตช์ FWDN ค้างไว้
    3. เชื่อมต่อสายไฟอีกครั้งขณะที่ยังกดสวิตช์ FWDN ค้างไว้
    4. ปล่อยสวิตช์ FWDN
        หากยังพบปัญหาอยู่ ให้ลองเรียกใช้ Arduino IDE ด้วยสิทธิ์ผู้ดูแลระบบ
4. หลังจากอัปโหลดไฟล์สำเร็จแล้ว ให้ตรวจสอบข้อความต่อไปนี้ในคอนโซลเอาต์พุตของ Arduino IDE:  

    **หมายเหตุ:** ข้อความควรมี **vcpSPI_Dot8x8.ino.rom**
    ```
    [FWDN_VCP::WriteFile:577] Complete to send file - C:\Users\topst\AppData\Local\arduino\sketches\567805554B5B9F915DCC80B38483AE07/vcpSPI_Dot8x8.ino.rom

    [main:155] Complete FWDN
    ```

**หมายเหตุ:** หากต้องการใช้ขา SPI ที่อยู่ตรงกลางบอร์ด VCP-G สามารถใช้งานได้โดยอ้างอิงหมายเลขขาต่อไปนี้
<p align="center"><strong>ตารางที่ 4.2 การแมปขา SPI ตรงกลางบน VCP-G</strong></p>
<div align="center">
	<table>
	    <tr>
	        <th colspan="3">หมายเลขขา</th>
	        <th>ฟังก์ชัน SPI</th>
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
บทนี้ให้คำแนะนำสำหรับการกำหนดค่าการสื่อสารแบบ Inter-integrated Circuit (I2C) บน VCP-G  
I2C เป็นโปรโตคอลการสื่อสารแบบซิงโครนัสสองสายที่ออกแบบมาเพื่อการแลกเปลี่ยนข้อมูลอย่างมีประสิทธิภาพระหว่างอุปกรณ์หลายตัว โดยทำงานด้วยสายข้อมูลอนุกรม (SDA) และสายสัญญาณนาฬิกาอนุกรม (SCL) ซึ่งช่วยให้อุปกรณ์ต่อพ่วงหลายตัวสื่อสารกับไมโครคอนโทรลเลอร์ได้โดยใช้แอดเดรสเฉพาะของแต่ละตัว I2C รองรับทั้งการสื่อสารแบบมาสเตอร์-สเลฟและการกำหนดค่าแบบมัลติมาสเตอร์ จึงเหมาะอย่างยิ่งสำหรับการเชื่อมต่อเซ็นเซอร์ จอแสดงผล และอุปกรณ์ความเร็วต่ำอื่น ๆ ในขณะที่ลดจำนวนการเชื่อมต่อที่ต้องใช้ให้น้อยที่สุด

</br></br></br>

## 5.1 vcpI2C_LCD1602
---
โปรแกรมตัวอย่างนี้แสดงวิธีที่บอร์ด VCP-G ควบคุมจอแสดงผล LCD1602 โดยใช้โปรโตคอลการสื่อสาร I2C LCD1602 เป็นจอแสดงผลผลึกเหลวขนาด 16 ตัวอักษร 2 บรรทัด ซึ่งใช้กันทั่วไปในโครงงานระบบสมองกลฝังตัว บอร์ดจะใช้ไลบรารี LiquidCrystal_I2C ในการส่งคำสั่งและข้อมูลผ่านบัส I2C เพื่อควบคุมจอแสดงผลอย่างมีประสิทธิภาพ

ในตัวอย่างนี้ LCD จะถูกเริ่มต้นการทำงานและเปิดไฟพื้นหลังเพื่อให้มองเห็นได้ชัดเจน จากนั้นโปรแกรมจะกำหนดตำแหน่งเคอร์เซอร์เพื่อแสดงข้อความ "VCP-G" ในบรรทัดแรก และ "I2C Test!" ในบรรทัดที่สอง ด้วยการสื่อสารแบบ I2C จึงสามารถควบคุมอุปกรณ์หลายตัวได้โดยใช้สายไฟน้อยที่สุด ทำให้เป็นโซลูชันที่มีประสิทธิภาพสำหรับโครงงานขนาดกะทัดรัด
</br></br>

### 5.1.1 ข้อกำหนดฮาร์ดแวร์
- บอร์ด VCP-G (x1)
- LCD1602 (x1)
- อะแดปเตอร์จ่ายไฟ 12V 1A (x1)
- สาย USB Type-C to A (x1)
- สายจัมเปอร์แบบผู้-เมีย (x4)
</br></br>

### 5.1.2 วงจร
- LCD1602
    - ขา VCC ของ LCD1602 เชื่อมต่อกับขาแอนะล็อก 5V บนบอร์ด VCP-G
    - ขา GND ของ LCD1602 เชื่อมต่อกับ GND บนบอร์ด VCP-G
    - ขา SDA ของ LCD1602 เชื่อมต่อกับขา 48 บนบอร์ด VCP-G
    - ขา SCL ของ LCD1602 เชื่อมต่อกับขา 49 บนบอร์ด VCP-G

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/vcpI2C_LCD1602%20Circuit%20Schematic.png"></p>
<p align="center"><strong>รูปที่ 5.1 แผนผังวงจรของ vcpI2C_LCD1602</strong></p>

#### 5.1.2.1 ผังพิน
ตารางต่อไปนี้แสดงการแมปพิน

<p align="center"><strong>ตารางที่ 5.1 ผังพินของ vcpI2C_LCD1602</strong></p>
<div align="center">
	<table>
	    <tr>
	        <th colspan="3">ชื่อพิน</th>
	        <th>บอร์ด VCP-G</th>
	        <th>Arduino IDE</th>
	    </tr>
	    <tr>
	        <td colspan="3">ขา VCC ของ LCD1602</td>
	        <td>5V</td>
	        <td>-</td>
	    </tr>
	        <tr>
	        <td colspan="3">ขา GND ของ LCD1602</td>
	        <td>GND</td>
	        <td>-</td>
	    </tr>
	    <tr>
	        <td colspan="3">ขา SDA ของ LCD1602</td>
	        <td>48</td>
	        <td>-</td>
	    </tr>
	    <tr>
	        <td colspan="3">ขา SCL ของ LCD1602</td>
	        <td>49</td>
		    <td>-</td>
	    </tr>
	</table>
</div>

</br></br>

### 5.1.3 วิธีการดำเนินการ
1. เปิดไฟล์ "vcpI2C_LCD1602.ino"  
    1. เปิด Arduino IDE  
    2. คลิก **File -> Examples -> 04.VCP-G I2C -> vcpI2C_LCD1602**
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
2. ตรวจสอบและอัปโหลดไฟล์ "vcpI2C_LCD1602.ino" ไปยัง VCP-G
3. หากกระบวนการอัปโหลดค้างอยู่ในสถานะกำลังอัปโหลดไม่สิ้นสุด แสดงว่าโหมด FWDN ยังไม่ถูกเปิดใช้งาน วิธีแก้ไขมีดังนี้:  
    1. ถอดสายไฟออกจากบอร์ด VCP-G
    2. กดสวิตช์ FWDN ค้างไว้
    3. เชื่อมต่อสายไฟอีกครั้งขณะที่ยังกดสวิตช์ FWDN ค้างไว้
    4. ปล่อยสวิตช์ FWDN
        หากยังพบปัญหาอยู่ ให้ลองเรียกใช้ Arduino IDE ด้วยสิทธิ์ผู้ดูแลระบบ
4. หลังจากอัปโหลดไฟล์สำเร็จแล้ว ให้ตรวจสอบข้อความต่อไปนี้ในคอนโซลเอาต์พุตของ Arduino IDE:
   
    **หมายเหตุ:** ข้อความควรมี **vcpI2C_LCD1602.ino.rom**
    ```
    [FWDN_VCP::WriteFile:577] Complete to send file -         C:\Users\topst\AppData\Local\arduino\sketches\C8D91A6857B651D6C665B0EF18B7EE53/vcpI2C_LCD1602.ino.rom

    [main:155] Complete FWDN
    ```

</br></br></br></br>

# 6. VCP-G UART
---
บทนี้ให้คำแนะนำสำหรับการกำหนดค่าการสื่อสารแบบ Universal Asynchronous Receiver-Transmitter (UART) บน VCP-G  
UART เป็นโปรโตคอลการสื่อสารแบบอนุกรมที่ใช้กันอย่างแพร่หลาย ซึ่งส่งข้อมูลแบบอะซิงโครนัสโดยใช้สายสัญญาณเพียงสองเส้น ได้แก่ สายส่ง (TX) และสายรับ (RX) โปรโตคอลนี้มีความสำคัญอย่างยิ่งต่อการแลกเปลี่ยนข้อมูลระหว่างไมโครคอนโทรลเลอร์ เซ็นเซอร์ และคอมพิวเตอร์ โดยไม่จำเป็นต้องใช้สัญญาณนาฬิการ่วมกัน  
บทต่อไปนี้อธิบายวิธีส่งและรับข้อมูลผ่าน UART

</br></br></br>

## 6.1 vcpASCIITable
---
โปรแกรมตัวอย่างนี้แสดงวิธีที่ VCP-G พิมพ์ค่า ASCII ของตัวอักษรในรูปแบบต่าง ๆ ได้แก่ ฐานสิบ ฐานสิบหก ฐานแปด และฐานสอง โดยเริ่มจากตัวอักษร '!' (ค่า ASCII 33) และไล่เพิ่มขึ้นไปจนครบตัวอักษร ASCII ที่มองเห็นได้ทั้งหมด พร้อมพิมพ์แต่ละตัวในรูปแบบที่แตกต่างกัน โปรแกรมจะทำงานต่อเนื่องจนกระทั่งถึงตัวอักษร '~' (ค่า ASCII 126)
</br></br>

### 6.1.1 ข้อกำหนดฮาร์ดแวร์
- บอร์ด VCP-G (x1)
- อะแดปเตอร์จ่ายไฟ 12V 1A (x1)
- สาย USB Type-C to A (x1)
</br></br>

### 6.1.3 วิธีการดำเนินการ
1. เปิดไฟล์ "vcpASCIITable.ino"
    1. เปิด Arduino IDE
    2. คลิก **File -> Examples -> 05.VCP-G UART -> vcpASCIITable**
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
2. ตรวจสอบและอัปโหลดไฟล์ "vcpASCIITable.ino" ไปยัง VCP-G
3. หากกระบวนการอัปโหลดค้างอยู่ในสถานะกำลังอัปโหลดไม่สิ้นสุด แสดงว่าโหมด FWDN ยังไม่ถูกเปิดใช้งาน วิธีแก้ไขมีดังนี้:  
    1. ถอดสายไฟออกจากบอร์ด VCP-G
    2. กดสวิตช์ FWDN ค้างไว้
    3. เชื่อมต่อสายไฟอีกครั้งขณะที่ยังกดสวิตช์ FWDN ค้างไว้
    4. ปล่อยสวิตช์ FWDN
        หากยังพบปัญหาอยู่ ให้ลองเรียกใช้ Arduino IDE ด้วยสิทธิ์ผู้ดูแลระบบ
4. หลังจากอัปโหลดไฟล์สำเร็จแล้ว ให้ตรวจสอบข้อความต่อไปนี้ในคอนโซลเอาต์พุตของ Arduino IDE:  

    **หมายเหตุ:** ข้อความควรมี **vcpASCIITable.ino.rom**
    ```
    [FWDN_VCP::WriteFile:577] Complete to send file - C:\Users\topstAppData\Local\arduino\sketches\487F45098412336AA9D73C50C17E07D8/vcpASCIITable.ino.rom

    [main:155] Complete FWDN
    ```

</br></br></br>

## 6.2 vcpGraph
---
โปรแกรมตัวอย่างนี้แสดงวิธีที่ VCP-G อ่านค่าแอนะล็อกของโพเทนชิออมิเตอร์บนเบรดบอร์ดและส่งข้อมูลไปยังเครื่อง PC โฮสต์ผ่าน UART โค้ด Arduino จะอ่านค่าของเซ็นเซอร์แอนะล็อก (โพเทนชิออมิเตอร์) ที่ต่ออยู่กับขา A5 อย่างต่อเนื่องและส่งผ่านพอร์ตอนุกรม โค้ด Processing ที่ให้มาด้วยจะแสดงค่าเหล่านี้เป็นกราฟแบบไดนามิกตามเวลาจริง เพื่อแสดงการเปลี่ยนแปลงของสัญญาณอินพุตจากเซ็นเซอร์ตามช่วงเวลา
</br></br>

### 6.2.1 ข้อกำหนดฮาร์ดแวร์
- บอร์ด VCP-G (x1)
- เบรดบอร์ด (x1)
- โพเทนชิโอมิเตอร์ (x1)
- ตัวต้านทาน 10 kΩ (x1)
- อะแดปเตอร์จ่ายไฟ 12V 1A (x1)
- สาย USB Type-C to A (x1)
- สายจัมเปอร์ตัวผู้-ตัวผู้ (x4)
</br></br>

### 6.2.2 วงจร
- โพเทนชิโอมิเตอร์
    - พินกลางของโพเทนชิโอมิเตอร์เชื่อมต่อกับพินแอนะล็อก A5 บนบอร์ด VCP-G
    - ขา GND ของโพเทนชิออมิเตอร์เชื่อมต่อกับ GND บนบอร์ด VCP-G ผ่านตัวต้านทาน 10 kΩ
    - ขา VCC ของโพเทนชิออมิเตอร์เชื่อมต่อกับ 3.3V บนบอร์ด VCP-G

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/vcpGraph%20Circuit%20Schematic.png"></p>
<p align="center"><strong>รูปที่ 6.1 แผนผังวงจรของ vcpGraph</strong></p>

#### 6.2.2.1 ผังพิน
ตารางต่อไปนี้แสดงการแมปพิน

<p align="center"><strong>ตารางที่ 6.1 ผังพินของ vcpGraph</strong></p>
<div align="center">
	<table>
	    <tr>
	        <th colspan="3">ชื่อพิน</th>
	        <th>บอร์ด VCP-G</th>
	        <th>Arduino IDE</th>
	    </tr>
	    <tr>
	        <td colspan="3">พินกลางของโพเทนชิโอมิเตอร์</td>
	        <td>A5</td>
	        <td>A5</td>
	    </tr>
	        <tr>
	        <td colspan="3">พิน GND ของโพเทนชิโอมิเตอร์</td>
	        <td>GND</td>
	        <td>-</td>
	    </tr>
	    <tr>
	        <td colspan="3">ขา VCC ของโพเทนชิโอมิเตอร์</td>
	        <td>3.3V</td>
	        <td>-</td>
	    </tr>
	</table>
</div>
</br></br>

### 6.2.3 วิธีการดำเนินการ
1. เปิดไฟล์ "vcpGraph.ino"
    1. เปิด Arduino IDE
    2. คลิก **File -> Examples -> 05.VCP-G UART -> vcpGraph**
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
2. ตรวจสอบและอัปโหลดไฟล์ "vcpGraph.ino" ไปยัง VCP-G
3. หากกระบวนการอัปโหลดค้างอยู่ในสถานะกำลังอัปโหลดไม่สิ้นสุด แสดงว่าโหมด FWDN ยังไม่ถูกเปิดใช้งาน วิธีแก้ไขมีดังนี้:  
    1. ถอดสายไฟออกจากบอร์ด VCP-G
    2. กดสวิตช์ FWDN ค้างไว้
    3. เชื่อมต่อสายไฟอีกครั้งขณะที่ยังกดสวิตช์ FWDN ค้างไว้
    4. ปล่อยสวิตช์ FWDN
        หากยังพบปัญหาอยู่ ให้ลองเรียกใช้ Arduino IDE ด้วยสิทธิ์ผู้ดูแลระบบ
4. หลังจากอัปโหลดไฟล์สำเร็จแล้ว ให้ตรวจสอบข้อความต่อไปนี้ในคอนโซลเอาต์พุตของ Arduino IDE:

    **หมายเหตุ:** ข้อความควรมี **vcpGraph.ino.rom** รวมอยู่ด้วย
    ```
    [FWDN_VCP::WriteFile:577] Complete to send file - C:\Users\topst\AppData\Local\arduino\sketches\F59E4532EC3A529F5910F376F809A5E5/vcpGraph.ino.rom

    [main:155] Complete FWDN
    ```

</br></br></br></br>

# 7. ตัวอย่างเพิ่มเติม
---
บทนี้ให้ตัวอย่างเซ็นเซอร์เพิ่มเติมที่ไม่ได้รวมอยู่ใน "Examples for TOPST VCP Rev G" ใน Arduino IDE  
บทนี้ให้คำแนะนำตัวอย่างสำหรับการใช้งานเซ็นเซอร์ Arduino ที่ใช้กันทั่วไปกับบอร์ด VCP-G ซึ่งช่วยให้คุณผสานเซ็นเซอร์ต่าง ๆ เข้ากับโครงการของคุณได้อย่างมีประสิทธิภาพ

</br></br></br>

## 7.1 เซ็นเซอร์อินฟราเรด (IR) (ตัวรับส่งสัญญาณ)
---
### 7.1.1 เซ็นเซอร์อินฟราเรด (IR) 1
---
ตัวอย่างนี้แสดงวิธีที่บอร์ด VCP-G ควบคุมเซ็นเซอร์ IR และ LED สองดวงบนเบรดบอร์ด หลังจากอ่านค่าเซ็นเซอร์ IR แล้ว หากค่าเซ็นเซอร์ IR เป็น HIGH จะถือว่าไม่มีสิ่งกีดขวาง LED สีเขียวจะติดและ LED สีแดงจะดับ ในทางกลับกัน หากค่าเซ็นเซอร์ IR เป็น LOW จะถือว่ามีสิ่งกีดขวาง LED สีแดงจะติดและ LED สีเขียวจะดับ นอกจากนี้ การมีหรือไม่มีสิ่งกีดขวางจะแสดงบนซีเรียลมอนิเตอร์

#### 7.1.1.1 ข้อกำหนดฮาร์ดแวร์
- บอร์ด VCP-G (x1)
- เบรดบอร์ด (x1)
- เซ็นเซอร์รับส่งสัญญาณ IR (x1)
- LED (x2: แนะนำให้ใช้คนละสี)
- ตัวต้านทาน 220Ω (x2)
- อะแดปเตอร์จ่ายไฟ 12V 1A (x1)
- สาย USB Type-C to A (x1)
- สายจัมเปอร์ตัวผู้-ตัวผู้ (x4)
- สายจัมเปอร์ตัวผู้-ตัวเมีย (x3)

#### 7.1.1.2 วงจร
- เซ็นเซอร์รับส่งสัญญาณ IR
    - ขา OUT ของเซ็นเซอร์ IR เชื่อมต่อกับขา 50 บนบอร์ด VCP-G
    - ขา VCC ของเซ็นเซอร์ IR เชื่อมต่อกับ 5V บนบอร์ด VCP-G
    - ขา GND ของเซ็นเซอร์ IR เชื่อมต่อกับ GND บนบอร์ด VCP-G
- LED สีแดง
    - ขา (-) ของ LED เชื่อมต่อกับตัวต้านทาน และตัวต้านทานเชื่อมต่อกับ GND บนบอร์ด VCP-G
    - ขา (+) ของ LED เชื่อมต่อกับขา 48 บนบอร์ด VCP-G
- LED สีเขียว
    - ขา (-) ของ LED เชื่อมต่อกับตัวต้านทาน และตัวต้านทานเชื่อมต่อกับ GND บนบอร์ด VCP-G
    - ขา (+) ของ LED เชื่อมต่อกับขา 17 บนบอร์ด VCP-G

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/Infrared%20(IR)%20Sensor%20Circuit%20Schematic.png"></p>
<p align="center"><strong>รูปที่ 7.1 แผนผังวงจรของเซ็นเซอร์อินฟราเรด (IR)</strong></p>

##### 7.1.1.2.1 ผังพิน
ตารางต่อไปนี้แสดงการแมปพิน

<p align="center"><strong>ตารางที่ 7.1 ผังพินของ irSensor_LED</strong></p>
<div align="center">
	<table>
	    <tr>
	        <th colspan="3">ชื่อพิน</th>
	        <th>บอร์ด VCP-G</th>
	        <th>Arduino IDE</th>
	    </tr>
	    <tr>
	        <td colspan="3">ขา OUT ของเซ็นเซอร์ IR </td>
	        <td>50</td>
	        <td>50</td>
	    </tr>
	        <tr>
	        <td colspan="3">ขา VCC ของเซ็นเซอร์ IR </td>
	        <td>5V</td>
	        <td>-</td>
	    </tr>
	    <tr>
	        <td colspan="3">ขา GND ของเซ็นเซอร์ IR</td>
	        <td>GND</td>
	        <td>-</td>
	    </tr>
	    <tr>
	        <td colspan="3">ขา (+) ของ LED สีแดง</td>
	        <td>48</td>
	        <td>48</td>
	    </tr>
	    <tr>
	        <td colspan="3">ขา (-) ของ LED สีแดง</td>
	        <td>GND</td>
	        <td>-</td>
	    </tr>
	    <tr>
	        <td colspan="3">ขา (+) ของ LED สีเขียว</td>
	        <td>17</td>
	        <td>17</td>
	    </tr>
	    <tr>
	        <td colspan="3">ขา (-) ของ LED สีเขียว </td>
	        <td>GND</td>
	        <td>-</td>
	    </tr>
	</table>
</div>

#### 7.1.1.3 วิธีการดำเนินการ
1. คัดลอกซอร์สโค้ดต่อไปนี้ลงใน Arduino IDE และบันทึกไฟล์เป็น "irSensor_LED.ino"
    
   **หมายเหตุ:** ซอร์สโค้ดต่อไปนี้มีให้เฉพาะในเอกสารฉบับนี้เท่านั้น 

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
2. ตรวจสอบและอัปโหลดไฟล์ "irSensor_LED.ino" ไปยัง VCP-G
3. หากกระบวนการอัปโหลดค้างอยู่ในสถานะกำลังอัปโหลดไม่สิ้นสุด แสดงว่าโหมด FWDN ยังไม่ถูกเปิดใช้งาน วิธีแก้ไขมีดังนี้:  
    1. ถอดสายไฟออกจากบอร์ด VCP-G
    2. กดสวิตช์ FWDN ค้างไว้
    3. เชื่อมต่อสายไฟอีกครั้งขณะที่ยังกดสวิตช์ FWDN ค้างไว้
    4. ปล่อยสวิตช์ FWDN
        หากยังพบปัญหาอยู่ ให้ลองเรียกใช้ Arduino IDE ด้วยสิทธิ์ผู้ดูแลระบบ
4. หลังจากอัปโหลดไฟล์สำเร็จแล้ว ให้ตรวจสอบข้อความต่อไปนี้ในคอนโซลเอาต์พุตของ Arduino IDE:
 
    **หมายเหตุ:** ข้อความควรมี **irSensor_LED.ino.rom** รวมอยู่ด้วย
    ```
    [FWDN_VCP::WriteFile:577] Complete to send file - C:\Users\topst\AppData\Local\arduino\sketches\1D003A72AB3391D6D60FD7993380F8CD/irSensor_LED.ino.rom 

    [main:155] Complete FWDN
    ```
</br></br>

### 7.1.2 เซ็นเซอร์อินฟราเรด (IR) 2
---
ตัวอย่างนี้แสดงวิธีที่บอร์ด VCP-G ควบคุมเซ็นเซอร์ IR เพื่อตรวจจับวัตถุและพิมพ์สถานะการตรวจจับไปยังซีเรียลมอนิเตอร์ ตัวรับส่งสัญญาณ IR จะอ่านการมีอยู่ของสิ่งกีดขวาง หากค่าของตัวรับส่งสัญญาณ IR เป็น HIGH แสดงว่าไม่มีสิ่งกีดขวาง LED สีเขียวจะติดและ LED สีแดงจะดับ ในทางกลับกัน หากค่าของตัวรับส่งสัญญาณ IR เป็น LOW แสดงว่ามีสิ่งกีดขวาง LED สีแดงจะติดและ LED สีเขียวจะดับ นอกจากนี้ การมีหรือไม่มีสิ่งกีดขวางจะแสดงบนซีเรียลมอนิเตอร์

#### 7.1.2.1 ข้อกำหนดฮาร์ดแวร์
- บอร์ด VCP-G (x1)
- เซ็นเซอร์รับส่งสัญญาณ IR (x1)
- อะแดปเตอร์จ่ายไฟ 12V 1A (x1)
- สาย USB Type-C to A (x1)
- สายจัมเปอร์ตัวผู้-ตัวเมีย (x3)

#### 7.1.2.2 วงจร
- เซ็นเซอร์รับส่งสัญญาณ IR
    - ขา Out ของเซ็นเซอร์รับส่งสัญญาณ IR เชื่อมต่อกับขา 8 บนบอร์ด VCP-G 
    - ขา VCC ของเซ็นเซอร์รับส่งสัญญาณ IR เชื่อมต่อกับ 5V บนบอร์ด VCP-G
    - ขา GND ของเซ็นเซอร์รับส่งสัญญาณ IR เชื่อมต่อกับ GND บนบอร์ด VCP-G

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/Infrared%20(IR)%20Sensor%20(Transceiver)%20Circuit%20Schematic.png"></p>
<p align="center"><strong>รูปที่ 7.2 แผนผังวงจรของเซ็นเซอร์อินฟราเรด (IR) (ตัวรับส่งสัญญาณ)</strong></p>

##### 7.1.2.2.1 ผังพิน
ตารางต่อไปนี้แสดงการแมปพิน

<p align="center"><strong>ตารางที่ 7.2 ผังพินของ irTransceiver</strong></p>
<div align="center">
	<table>
	    <tr>
	        <th colspan="3">ชื่อพิน</th>
	        <th>บอร์ด VCP-G</th>
	        <th>Arduino IDE</th>
	    </tr>
	    <tr>
	        <td colspan="3">ขา OUT ของเซ็นเซอร์รับส่งสัญญาณ IR</td>
	        <td>8</td>
	        <td>8</td>
	    </tr>
	    <tr>
	        <td colspan="3">ขา VCC ของเซ็นเซอร์รับส่งสัญญาณ IR</td>
	        <td>5V</td>
	        <td>-</td>
	    </tr>
	    <tr>
	        <td colspan="3">ขา GND ของเซ็นเซอร์รับส่งสัญญาณ IR</td>
	        <td>GND</td>
	        <td>-</td>
	    </tr>
	</table>
</div>

#### 7.1.2.3 วิธีการดำเนินการ
1. คัดลอกซอร์สโค้ดต่อไปนี้ลงใน Arduino IDE และบันทึกไฟล์เป็น "irTransceiver.ino"
   
   **หมายเหตุ:** ซอร์สโค้ดต่อไปนี้มีให้เฉพาะในเอกสารฉบับนี้เท่านั้น 

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
2. ตรวจสอบและอัปโหลดไฟล์ "irTransceiver.ino" ไปยัง VCP-G
3. หากกระบวนการอัปโหลดค้างอยู่ในสถานะกำลังอัปโหลดไม่สิ้นสุด แสดงว่าโหมด FWDN ยังไม่ถูกเปิดใช้งาน วิธีแก้ไขมีดังนี้:  
    1. ถอดสายไฟออกจากบอร์ด VCP-G
    2. กดสวิตช์ FWDN ค้างไว้
    3. เชื่อมต่อสายไฟอีกครั้งขณะที่ยังกดสวิตช์ FWDN ค้างไว้
    4. ปล่อยสวิตช์ FWDN
        หากยังพบปัญหาอยู่ ให้ลองเรียกใช้ Arduino IDE ด้วยสิทธิ์ผู้ดูแลระบบ
4. หลังจากอัปโหลดไฟล์สำเร็จแล้ว ให้ตรวจสอบข้อความต่อไปนี้ในคอนโซลเอาต์พุตของ Arduino IDE:
   
    **หมายเหตุ:** ข้อความควรมี **irTransceiver.ino.rom** รวมอยู่ด้วย
    ```
    [FWDN_VCP::WriteFile:577] Complete to send file - C:\Users\topst\AppData\Local\arduino\sketches\1D003A72AB3391D6D60FD7993380F8CD/irTransceiver.ino.rom 

    [main:155] Complete FWDN
    ```

</br></br></br>

## 7.2 จอยสติ๊ก
---
ตัวอย่างนี้แสดงวิธีที่ VCP-G อ่านอินพุตจากจอยสติ๊กและแสดงค่าบนซีเรียลมอนิเตอร์ คุณสามารถรับอินพุตได้สามแบบ ได้แก่ แกน X แกน Y และปุ่มกด ซีเรียลมอนิเตอร์ใช้ตรวจสอบสัญญาณที่ได้รับ การเคลื่อนไหวบนแกน X และแกน Y จะเปลี่ยนค่าของพอร์ต ซึ่งสอดคล้องกับค่าตัวเลขของเอาต์พุตแอนะล็อก ทำให้สามารถควบคุมได้อย่างแม่นยำสำหรับแอปพลิเคชันที่ต้องการการปรับละเอียด

**หมายเหตุ:** Dual Axis Joystick Module (KY-023) เป็นผลิตภัณฑ์ของ Joy-IT สิทธิ์ทั้งหมดในการออกแบบ เครื่องหมายการค้า และทรัพย์สินทางปัญญาที่เกี่ยวข้องเป็นของ Joy-IT
</br></br>

### 7.2.1 ข้อกำหนดฮาร์ดแวร์
- บอร์ด VCP-G (x1)
- Dual Axis Joystick Module (KY-023) (x1)
- อะแดปเตอร์จ่ายไฟ 12V 1A (x1)
- สาย USB Type-C to A (x1)
- สายจัมเปอร์ผู้-เมีย (x5)
</br></br>

### 7.2.2 วงจร
- KY-023 (Dual Axis Joystick Module)
    - ขา 5V ของ KY-023 เชื่อมต่อกับ 5V บนบอร์ด VCP-G
    - ขา GND ของ KY-023 เชื่อมต่อกับ GND บนบอร์ด VCP-G 
    - ขา VRx ของ KY-023 เชื่อมต่อกับขาแอนะล็อก A5 บนบอร์ด VCP-G 
    - ขา VRy ของ KY-023 เชื่อมต่อกับขาแอนะล็อก A4 บนบอร์ด VCP-G 
    - ขา SW ของ KY-023 เชื่อมต่อกับขา 2 บนบอร์ด VCP-G

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/Joystick%20Circuit%20Schematic.png"></p>
<p align="center"><strong>รูปที่ 7.3 แผนผังวงจรของจอยสติ๊ก</strong></p>

#### 7.2.2.1 ผังพิน
ตารางต่อไปนี้แสดงการแมปพิน

<p align="center"><strong>ตารางที่ 7.3 ผังพินของจอยสติ๊ก</strong></p>
<div align="center">
	<table>
	    <tr>
	        <th colspan="3">ชื่อพิน</th>
	        <th>บอร์ด VCP-G</th>
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

### 7.2.3 วิธีการดำเนินการ
1. คัดลอกซอร์สโค้ดต่อไปนี้ลงใน Arduino IDE และบันทึกไฟล์เป็น "joystick.ino"
   
   **หมายเหตุ:** ซอร์สโค้ดต่อไปนี้มีให้เฉพาะในเอกสารฉบับนี้เท่านั้น 

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
2. ตรวจสอบและอัปโหลดไฟล์ "joystick.ino" ไปยัง VCP-G
3. หากกระบวนการอัปโหลดค้างอยู่ในสถานะกำลังอัปโหลดไม่สิ้นสุด แสดงว่าโหมด FWDN ยังไม่ถูกเปิดใช้งาน วิธีแก้ไขมีดังนี้:  
    1. ถอดสายไฟออกจากบอร์ด VCP-G
    2. กดสวิตช์ FWDN ค้างไว้
    3. เชื่อมต่อสายไฟอีกครั้งขณะที่ยังกดสวิตช์ FWDN ค้างไว้
    4. ปล่อยสวิตช์ FWDN  
        หากยังพบปัญหาอยู่ ให้ลองเรียกใช้ Arduino IDE ด้วยสิทธิ์ผู้ดูแลระบบ
4. หลังจากอัปโหลดไฟล์สำเร็จแล้ว ให้ตรวจสอบข้อความต่อไปนี้ในคอนโซลเอาต์พุตของ Arduino IDE:
   
    **หมายเหตุ:** ข้อความควรมี **joystick.ino.rom** รวมอยู่ด้วย
    ```
    [FWDN_VCP::WriteFile:577] Complete to send file - C:\Users\topst\AppData\Local\arduino\sketches\1D003A72AB3391D6D60FD7993380F8CD/joystick.ino.rom 

    [main:155] Complete FWDN
    ```

</br></br></br>

## 7.3 เซ็นเซอร์แก๊ส
---
ตัวอย่างนี้แสดงวิธีที่บอร์ด VCP-G ใช้เซ็นเซอร์แก๊ส (MQ 135) เพื่อตรวจจับแก๊สอันตรายชนิดต่าง ๆ ในอากาศ โดยจะอ่านค่าแอนะล็อกจากเซ็นเซอร์ที่ต่ออยู่กับขาแอนะล็อกบนบอร์ด VCP-G แปลงเป็นค่าแรงดันไฟฟ้า แล้วพิมพ์ค่าดังกล่าวไปยังซีเรียลมอนิเตอร์โดยมีทศนิยมหนึ่งตำแหน่ง

**หมายเหตุ:** Gas Sensor (MQ-135) เป็นผลิตภัณฑ์ของ Winsen® สิทธิ์ทั้งหมดในการออกแบบ เครื่องหมายการค้า และทรัพย์สินทางปัญญาที่เกี่ยวข้องเป็นของ Winsen
</br></br>

### 7.3.1 ข้อกำหนดฮาร์ดแวร์
- บอร์ด VCP-G (x1)
- เซ็นเซอร์แก๊ส (MQ135) (x1)
- อะแดปเตอร์จ่ายไฟ 12V 1A (x1)
- สาย USB Type-C to A (x1)
- สายจัมเปอร์ตัวผู้-ตัวเมีย (x3)
</br></br>

### 7.3.2 วงจร
- เซ็นเซอร์แก๊ส
    - ขา A0 ของเซ็นเซอร์แก๊สเชื่อมต่อกับขาแอนะล็อก A5 บนบอร์ด VCP-G 
    - ขา VCC ของเซ็นเซอร์แก๊สเชื่อมต่อกับ 5V บนบอร์ด VCP-G
    - ขา GND ของเซ็นเซอร์แก๊สเชื่อมต่อกับ GND บนบอร์ด VCP-G


<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/Gas%20Sensor%20Circuit%20Schematic.png"></p>
<p align="center"><strong>รูปที่ 7.4 แผนผังวงจรของเซ็นเซอร์แก๊ส</strong></p>

#### 7.3.2.1 ผังพิน
ตารางต่อไปนี้แสดงการแมปพิน

<p align="center"><strong>ตารางที่ 7.4 ผังพินของเซ็นเซอร์แก๊ส</strong></p>
<div align="center">
	<table>
	    <tr>
	        <th colspan="3">ชื่อพิน</th>
	        <th>บอร์ด VCP-G</th>
	        <th>Arduino IDE</th>
	    </tr>
	    <tr>
	        <td colspan="3">ขา A0 ของเซ็นเซอร์แก๊ส</td>
	        <td>A5</td>
	        <td>A5</td>
	    </tr>
	        <tr>
	        <td colspan="3">ขา VCC ของเซ็นเซอร์แก๊ส</td>
	        <td>5V</td>
	        <td>-</td>
	    </tr>
	    <tr>
	        <td colspan="3">ขา GND ของเซ็นเซอร์แก๊ส</td>
	        <td>GND</td>
	        <td>-</td>
	    </tr>
	</table>
</div>
</br></br>

### 7.3.3 วิธีการดำเนินการ
1. คัดลอกซอร์สโค้ดต่อไปนี้ลงใน Arduino IDE และบันทึกไฟล์เป็น "GasSensor.ino"
  
   **หมายเหตุ:** ซอร์สโค้ดต่อไปนี้มีให้เฉพาะในเอกสารฉบับนี้เท่านั้น 

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
2. ตรวจสอบและอัปโหลดไฟล์ "GasSensor.ino" ไปยัง VCP-G
3. หากกระบวนการอัปโหลดค้างอยู่ในสถานะกำลังอัปโหลดไม่สิ้นสุด แสดงว่าโหมด FWDN ยังไม่ถูกเปิดใช้งาน วิธีแก้ไขมีดังนี้:  
    1. ถอดสายไฟออกจากบอร์ด VCP-G
    2. กดสวิตช์ FWDN ค้างไว้
    3. เชื่อมต่อสายไฟอีกครั้งขณะที่ยังกดสวิตช์ FWDN ค้างไว้
    4. ปล่อยสวิตช์ FWDN  
        หากยังพบปัญหาอยู่ ให้ลองเรียกใช้ Arduino IDE ด้วยสิทธิ์ผู้ดูแลระบบ
4. หลังจากอัปโหลดไฟล์สำเร็จแล้ว ให้ตรวจสอบข้อความต่อไปนี้ในคอนโซลเอาต์พุตของ Arduino IDE:
   
    **หมายเหตุ:** ข้อความควรมี **GasSensor.ino.rom** รวมอยู่ด้วย
    ```
    [FWDN_VCP::WriteFile:577] Complete to send file - C:\Users\topst\AppData\Local\arduino\sketches\1D003A72AB3391D6D60FD7993380F8CD/joystick.ino.rom 

    [main:155] Complete FWDN
    ```
</br></br></br>

## 7.4 โมดูลเซ็นเซอร์สัมผัสโลหะ
---
โปรแกรมตัวอย่างนี้แสดงวิธีที่บอร์ด VCP-G ควบคุมเซ็นเซอร์สัมผัสและ LED บนเบรดบอร์ด โมดูลเซ็นเซอร์สัมผัสโลหะ (KY-036) เป็นเซ็นเซอร์แอนะล็อก/ดิจิทัลอเนกประสงค์ที่ออกแบบมาเพื่อตรวจจับการสัมผัสบนพื้นผิวโลหะหรือผิวหนังของมนุษย์ โมดูลนี้ใช้ทรานซิสเตอร์เพื่อตรวจจับการเปลี่ยนแปลงของสภาพนำไฟฟ้าเมื่อมีการสัมผัส และให้สัญญาณเอาต์พุตทั้งแบบดิจิทัลและแอนะล็อกเพื่อทำงานร่วมกับ VCP-G  
เมื่อตรวจพบการสัมผัส โมดูลเซ็นเซอร์สัมผัสโลหะจะส่งค่าดิจิทัล/แอนะล็อกที่เกี่ยวข้องไปยังซีเรียลมอนิเตอร์ คุณยังสามารถควบคุม LED ตามสถานะการสัมผัสได้อีกด้วย 

**หมายเหตุ:** โมดูลเซ็นเซอร์สัมผัสโลหะ (KY-036) มีโพเทนชิออมิเตอร์ในตัวสำหรับปรับความไว คุณสามารถหมุนโพเทนชิออมิเตอร์นี้เพื่อเพิ่มหรือลดความไวได้
</br></br>

### 7.4.1 ข้อกำหนดฮาร์ดแวร์
- บอร์ด VCP-G (x1)
- เบรดบอร์ด (x1)
- โมดูลเซ็นเซอร์สัมผัสโลหะ (KY-036) (x1)
- LED (x1)
- ตัวต้านทาน 220Ω (x1)
- อะแดปเตอร์จ่ายไฟ 12V 1A (x1)
- สาย USB Type-C to A (x1)
- สายจัมเปอร์ตัวผู้-ตัวผู้ (x4)
- สายจัมเปอร์แบบผู้-เมีย (x4)
</br></br>

### 7.4.2 วงจร
- โมดูลเซ็นเซอร์สัมผัสโลหะ
    - ขา A0 ของโมดูลเซ็นเซอร์สัมผัสโลหะเชื่อมต่อกับขาแอนะล็อก A5 บนบอร์ด VCP-G
    - ขา G ของโมดูลเซ็นเซอร์สัมผัสโลหะเชื่อมต่อกับ GND บนบอร์ด VCP-G
    - พิน (+) ของโมดูลเซ็นเซอร์ Metal Touch ต่อกับ 5V บนบอร์ด VCP-G
    - พิน D0 ของโมดูลเซ็นเซอร์ Metal Touch ต่อกับพินที่ 30 บนบอร์ด VCP-G

- LED
    - พิน (+) ของ LED ต่อกับพินที่ 13 บนบอร์ด VCP-G
    - พิน (-) ของ LED ต่อกับ GND บนบอร์ด VCP-G ผ่านตัวต้านทาน 220Ω


<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/Metal%20Touch%20Sensor%20Circuit%20Schematic.png"></p>
<p align="center"><strong>รูปที่ 7.5 ผังวงจรของเซ็นเซอร์ Metal Touch</strong></p>

#### 7.4.2.1 การแมปพิน
ตารางต่อไปนี้แสดงการแมปพิน

<p align="center"><strong>ตารางที่ 7.5 การแมปพินของเซ็นเซอร์ Metal Touch</strong></p>
<div align="center">
	<table>
	    <tr>
	        <th colspan="3">ชื่อพิน</th>
	        <th>บอร์ด VCP-G</th>
	        <th>Arduino IDE</th>
	    </tr>
	    <tr>
	        <td colspan="3">พิน A0 ของโมดูลเซ็นเซอร์ Metal Touch</td>
	        <td>A5</td>
	        <td>A5</td>
	    </tr>
	        <tr>
	        <td colspan="3">พิน G ของโมดูลเซ็นเซอร์ Metal Touch</td>
	        <td>GND</td>
	        <td>-</td>
	    </tr>
	    <tr>
	        <td colspan="3">พิน (+) ของโมดูลเซ็นเซอร์ Metal Touch</td>
	        <td>5V</td>
		    <td>-</td>
		</tr>
	    <tr>
	        <td colspan="3">พิน D0 ของโมดูลเซ็นเซอร์ Metal Touch</td>
	        <td>30</td>
	        <td>30</td>
	    </tr>
	    <tr>
	        <td colspan="3">พิน (+) ของ LED</td>
	        <td>13</td>
	        <td>13</td>
	    </tr>
	    <tr>
	        <td colspan="3">พิน (+) ของ LED</td>
	        <td>GND</td>
	        <td>-</td>
	    </tr>
	</table>
</div>
</br></br>

### 7.4.3 วิธีการดำเนินการ
1. คัดลอกซอร์สโค้ดต่อไปนี้ลงใน Arduino IDE และบันทึกไฟล์ในชื่อ "vcp_touch.ino"  

   **หมายเหตุ:** ซอร์สโค้ดต่อไปนี้มีให้เฉพาะในเอกสารฉบับนี้เท่านั้น 

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
2. ตรวจสอบและอัปโหลดไฟล์ "vcp_touch.ino" ไปยัง VCP-G
3. หากกระบวนการอัปโหลดค้างอยู่ในสถานะกำลังอัปโหลดไม่สิ้นสุด แสดงว่าโหมด FWDN ยังไม่ถูกเปิดใช้งาน วิธีแก้ไขมีดังนี้:  
    1. ถอดสายไฟออกจากบอร์ด VCP-G
    2. กดสวิตช์ FWDN ค้างไว้
    3. เชื่อมต่อสายไฟอีกครั้งขณะที่ยังกดสวิตช์ FWDN ค้างไว้
    4. ปล่อยสวิตช์ FWDN  
        หากยังพบปัญหาอยู่ ให้ลองเรียกใช้ Arduino IDE ด้วยสิทธิ์ผู้ดูแลระบบ
4. หลังจากอัปโหลดไฟล์สำเร็จแล้ว ให้ตรวจสอบข้อความต่อไปนี้ในคอนโซลเอาต์พุตของ Arduino IDE:
   
    **หมายเหตุ:** ข้อความดังกล่าวควรมี **vcp_touch.ino.rom** รวมอยู่ด้วย
    ```
    [FWDN_VCP::WriteFile:577] Complete to send file - C:\Users\topst\AppData\Local\arduino\sketches\567805554B5B9F915DCC80B38483AE07/vcp_touch.ino.rom

    [main:155] Complete FWDN
    ```

**หมายเหตุ:** โปรดกำหนดอัตราบอดที่เหมาะสมสำหรับการสื่อสารแบบอนุกรม

</br></br></br>

## 7.5 สเต็ปมอเตอร์พร้อมไดรเวอร์มอเตอร์
---
ตัวอย่างนี้แสดงวิธีที่บอร์ด VCP-G ควบคุมสเต็ปมอเตอร์แบบ 4 สาย (28BYJ-48 (5VDC)) และไดรเวอร์มอเตอร์ (ULN2003 (5V–12V)) โค้ดในบทที่ 7.5.3 กำหนดพินที่ต่อกับไดรเวอร์มอเตอร์และตั้งค่าจำนวนสเต็ปต่อหนึ่งรอบ มอเตอร์จะหมุนไปข้างหน้าครบหนึ่งรอบ หยุดชั่วครู่ จากนั้นหมุนย้อนกลับครบหนึ่งรอบ แล้วหยุดอีกครั้ง ความเร็วของมอเตอร์ควบคุมด้วยการหน่วงเวลาระหว่างสเต็ป และทิศทางควบคุมด้วยลำดับการจ่ายไฟให้ขดลวด

**หมายเหตุ:** มอเตอร์ 28BYJ-48 ต้องใช้สัญญาณ 4096 ครั้งต่อการหมุนครบหนึ่งรอบในโหมด Half step และ 2048 ครั้งต่อการหมุนครบหนึ่งรอบในโหมด Full step เพื่อการควบคุมมอเตอร์อย่างแม่นยำ ควรคำนึงถึงจำนวนสัญญาณที่ต้องใช้ในแต่ละโหมด 
</br></br>

### 7.5.1 ข้อกำหนดด้านฮาร์ดแวร์
- บอร์ด VCP-G (x1)
- สเต็ปมอเตอร์ (28BYJ-48) (x1)
- ไดรเวอร์มอเตอร์ (ULN2003) (x1)
- อะแดปเตอร์จ่ายไฟ 12V 1A (x1)
- สาย USB Type-C to A (x1)
- สายจัมเปอร์แบบผู้-ผู้ (x6)
</br></br>

### 7.5.2 วงจร
- ไดรเวอร์มอเตอร์
    - พิน IN1 ต่อกับพินที่ 8 บนบอร์ด VCP-G
    - พิน IN2 ต่อกับพินที่ 9 บนบอร์ด VCP-G
    - พิน IN3 ต่อกับพินที่ 10 บนบอร์ด VCP-G
    - พิน IN4 ต่อกับพินที่ 11 บนบอร์ด VCP-G
    - พิน (+) ต่อกับ 5V บนบอร์ด VCP-G
    - พิน (-) ต่อกับ GND บนบอร์ด VCP-G

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/Step%20Motor%20with%20Motor%20Driver%20Circuit%20Schematic.png"></p>
<p align="center"><strong>รูปที่ 7.6 ผังวงจรของสเต็ปมอเตอร์พร้อมไดรเวอร์มอเตอร์</strong></p>

#### 7.5.2.1 การแมปพิน
ตารางต่อไปนี้แสดงการแมปพิน

<p align="center"><strong>ตารางที่ 7.6 การแมปพินของไดรเวอร์มอเตอร์</strong></p>
<div align="center">
	<table>
	    <tr>
	        <th colspan="3">ชื่อพิน</th>
	        <th>บอร์ด VCP-G</th>
	        <th>Arduino IDE</th>
	    </tr>
	    <tr>
	        <td colspan="3">พิน IN1 ของไดรเวอร์มอเตอร์</td>
	        <td>8</td>
	        <td>8</td>
	    </tr>
	        <tr>
	        <td colspan="3">พิน IN2 ของไดรเวอร์มอเตอร์</td>
	        <td>9</td>
	        <td>9</td>
	    </tr>
	    <tr>
	        <td colspan="3">พิน IN3 ของไดรเวอร์มอเตอร์</td>
	        <td>10</td>
	        <td>10</td>
		</tr>
	    <tr>
	        <td colspan="3">พิน IN4 ของไดรเวอร์มอเตอร์</td>
		    <td>11</td>
			<td>11</td>
	    </tr>
		<tr>
			<td colspan="3">พิน (+) ของไดรเวอร์มอเตอร์</td>
	        <td>5V</td>
	        <td>-</td>
		</tr>
	    <tr>
	        <td colspan="3">พิน (-) ของไดรเวอร์มอเตอร์</td>
	        <td>GND</td>
	        <td>-</td>
	    </tr>
	</table>
</div>
</br></br>

### 7.5.3 วิธีการดำเนินการ
1. คัดลอกซอร์สโค้ดต่อไปนี้ลงใน Arduino IDE และบันทึกไฟล์ในชื่อ "motordriver.ino"

    **หมายเหตุ:** ซอร์สโค้ดต่อไปนี้มีให้เฉพาะในเอกสารฉบับนี้เท่านั้น 

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
2. ตรวจสอบและอัปโหลดไฟล์ "motordriver.ino" ไปยัง VCP-G
3. หากกระบวนการอัปโหลดค้างอยู่ในสถานะกำลังอัปโหลดไม่สิ้นสุด แสดงว่าโหมด FWDN ยังไม่ถูกเปิดใช้งาน วิธีแก้ไขมีดังนี้:  
    1. ถอดสายไฟออกจากบอร์ด VCP-G
    2. กดสวิตช์ FWDN ค้างไว้
    3. เชื่อมต่อสายไฟอีกครั้งขณะที่ยังกดสวิตช์ FWDN ค้างไว้
    4. ปล่อยสวิตช์ FWDN  
        หากยังพบปัญหาอยู่ ให้ลองเรียกใช้ Arduino IDE ด้วยสิทธิ์ผู้ดูแลระบบ
4. หลังจากอัปโหลดไฟล์สำเร็จแล้ว ให้ตรวจสอบข้อความต่อไปนี้ในคอนโซลเอาต์พุตของ Arduino IDE:  

    **หมายเหตุ:** ข้อความดังกล่าวควรมี **motordriver.ino.rom** รวมอยู่ด้วย
    ```
    [FWDN_VCP::WriteFile:577] Complete to send file - C:\Users\topst\AppData\Local\arduino\sketches\567805554B5B9F915DCC80B38483AE07/motordriver.rom

    [main:155] Complete FWDN
    ```
</br></br></br></br>

# 8. เอกสารอ้างอิง
---
- ติดต่อ TOPST สำหรับรายละเอียดเพิ่มเติม: topst@topst.ai

**หมายเหตุ:** เอกสารอ้างอิงสามารถจัดหาให้ได้เมื่อมีอยู่ ทั้งนี้ขึ้นอยู่กับเงื่อนไขของสัญญา หากไม่มีเอกสาร
อ้างอิงดังกล่าว จะมีการแนะนำเนื้อหาที่เกี่ยวข้องโดยตรงกับการพัฒนาของท่านแทน
