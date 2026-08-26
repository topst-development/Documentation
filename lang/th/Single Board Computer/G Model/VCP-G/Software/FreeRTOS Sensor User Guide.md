# 1. บทนำ
---
เอกสารนี้ให้แนวทางการใช้งาน VCP-G ร่วมกับ FreeRTOS โดยมีคำแนะนำในการกำหนดค่าและโค้ดตัวอย่าง เพื่อช่วยให้คุณพัฒนาแอปพลิเคชันแบบฝังตัวด้วย VCP-G ภายใต้สภาพแวดล้อม FreeRTOS ได้อย่างง่ายดาย

โดยเฉพาะอย่างยิ่ง เอกสารนี้ให้แนวทางเกี่ยวกับแอปพลิเคชันตัวอย่างที่ใช้ FreeRTOS สำหรับ VCP-G ซึ่งประกอบด้วย 
- เอาต์พุต/อินพุตแบบดิจิทัล
- SPI
- I2C
- UART
- PWM
- Additional Example

โปรดดูรูปที่ 1.1 ก่อนใช้งาน VCP-G
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/vcp-g%20pinout%20Diagram.png"></p>
<p align="center"><strong>รูปที่ 1.1 แผนผังพินของ VCP-G</strong></p>
</br>

ในการรันแต่ละตัวอย่าง คุณต้องแก้ไขไฟล์ `main.c` ซึ่งอยู่ที่:
```
$ ~/vcp/sources/app.sample/app.base/main.c
```
หลังจากทำการแก้ไขที่จำเป็นแล้ว ให้คอมไพล์โปรเจกต์โดยใช้ Makefile ที่ให้มาเพื่อสร้างไบนารีของเฟิร์มแวร์
</br></br></br></br>

# 2. อินพุต/เอาต์พุตแบบดิจิทัล
---
บทนี้ให้ตัวอย่างการควบคุม LED โดยใช้พินดิจิทัลของบอร์ด VCP-G ใน VCP-G พินดิจิทัลใช้สำหรับส่งหรือรับสัญญาณไบนารี (HIGH หรือ LOW) จึงมีความสำคัญอย่างยิ่งต่อการควบคุมชิ้นส่วนต่าง ๆ เช่น LED สวิตช์ และเซ็นเซอร์ 

บทนี้ประกอบด้วยโปรเจกต์ตัวอย่างสองรายการที่แสดงวิธีควบคุม LED และปุ่มกดโดยใช้เอาต์พุตและอินพุตแบบดิจิทัล ซึ่งช่วยให้คุณเข้าใจการทำงานพื้นฐานของพินดิจิทัล
</br></br></br>

## 2.1 เอาต์พุตแบบดิจิทัล
---
ตัวอย่างนี้แสดงวิธีควบคุม LED บนเบรดบอร์ดโดยใช้บอร์ด VCP-G ภายใต้ FreeRTOS  
คุณสามารถดูไฟล์ซอร์สที่เกี่ยวข้องได้ที่:  

```
$ ~/vcp/sources/app.sample/app.base/main.c
```
ก่อนดำเนินการต่อ โปรดตรวจสอบว่าได้ติดตั้ง VCP-G FreeRTOS SDK อย่างถูกต้องแล้ว สำหรับคำแนะนำในการติดตั้งและตั้งค่า โปรดดูคู่มือ VCP-G FreeRTOS SDK Getting Started

ในการใช้งานตัวอย่างนี้ ให้แก้ไขไฟล์ main.c เพื่อกำหนดค่าพิน GPIO ที่ต่อกับ LED ให้เป็นเอาต์พุตแบบดิจิทัล ควรสร้างงาน (task) ของ FreeRTOS เพื่อเปิด LED ทั้งสี่ดวงทีละดวงตามลำดับ จากนั้นปิดในลำดับย้อนกลับ การเปลี่ยนสถานะของ LED แต่ละครั้งควรมีการหน่วงเวลา 500 ms เพื่อให้สังเกตลำดับการทำงานได้อย่างชัดเจน
</br></br>

### 2.1.1 ข้อกำหนดฮาร์ดแวร์  
- บอร์ด VCP-G (x1)
- เบรดบอร์ด (x1)
- LED (x4)
- อะแดปเตอร์จ่ายไฟ 12V 1A (x1)
- สาย USB Type-C to A (x1) 
- สายจัมเปอร์ตัวผู้-ตัวผู้ (x9)
</br></br>

### 2.1.2 วงจร
- LED01
    - พิน (+) ต่อกับพินที่ 7 บนบอร์ด VCP-G
    - พิน (–) ต่อกับราง GND บนเบรดบอร์ด
- LED02
    - พิน (+) ต่อกับพินที่ 6 บนบอร์ด VCP-G
    - พิน (–) ต่อกับราง GND บนเบรดบอร์ด
- LED03
    - พิน (+) ต่อกับพินที่ 5 บนบอร์ด VCP-G
    - พิน (–) ต่อกับราง GND บนเบรดบอร์ด
- LED04
    - พิน (+) ต่อกับพินที่ 4 บนบอร์ด VCP-G
    - พิน (–) ต่อกับราง GND บนเบรดบอร์ด 

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/F_digital_out.png" width="600"></p>
<p align="center"><strong>รูปที่ 2.1 ผังวงจรของ vcp4LED</strong></p>

#### 2.1.2.1 การแมปพิน
ตารางต่อไปนี้แสดงการแมปพิน

<p align="center"><strong>ตารางที่ 2.1 การแมปพินของ vcp4LED</strong></p>
<div align="center">	
	<table>
		<tr>
			<th colspan="3">ชื่อพิน</th>
	        <th>บอร์ด VCP-G</th>
	        <th>GPIO</th>
	    </tr>
	    <tr>
	        <td colspan="3">พิน (+) ของ LED01</td>
	        <td>7</td>
	        <td>B[01]</td>
	    </tr>
	        <tr>
	        <td colspan="3">พิน (+) ของ LED02</td>
	        <td>6</td>
	        <td>A[13]</td>
	    </tr>
	        <tr>
	        <td colspan="3">พิน (+) ของ LED03</td>
	        <td>5</td>
	        <td>B[10]</td>
	    </tr>
	        <tr>
	        <td colspan="3">พิน (+) ของ LED04</td>
	        <td>4</td>
	        <td>B[27]</td>
	    </tr>
	</table>
</div>
</br></br>

### 2.1.3 วิธีการดำเนินการ
ในการรันตัวอย่างนี้ ให้แก้ไข **Main_StartTask()** ในไฟล์ main.c ตามที่แสดง
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
หลังจากแก้ไขโค้ดแล้ว ให้ไปยังไดเรกทอรีต่อไปนี้และรันคำสั่งบิลด์:  
```
$ cd ~/vcp/build/tcc70xx/gcc
$ make
```
ขั้นตอนนี้จะสร้างอิมเมจของเฟิร์มแวร์ และใช้เครื่องมือ ***FWDN*** เพื่อแฟลชอิมเมจที่สร้างขึ้นไปยัง VCP-G  
หลังจากแฟลชและรันโค้ดสำเร็จแล้ว LED ทั้งสี่ดวงที่ต่ออยู่จะติดตามลำดับตั้งแต่ LED01 ถึง LED04 จากนั้นจะดับในลำดับย้อนกลับ การเปลี่ยนสถานะแต่ละครั้งจะมีการหน่วงเวลา 500 ms ทำให้เกิดรูปแบบการกะพริบที่ต่อเนื่องราบรื่น
</br></br></br>

## 2.2 อินพุตแบบดิจิทัล
---
ตัวอย่างนี้แสดงวิธีอ่านค่าอินพุตจากปุ่มกดและนำไปใช้ควบคุม LED โดยใช้บอร์ด VCP-G ภายใต้ FreeRTOS
ไฟล์ซอร์สที่เกี่ยวข้องอยู่ที่:
``` 
$ ~/vcp/sources/app.sample/app.base/main.c
```
ในการใช้งานตัวอย่างนี้ ให้แก้ไข main.c เพื่อกำหนดค่าพิน GPIO หนึ่งพินเป็นอินพุตแบบดิจิทัล (ต่อกับปุ่มกด) และพิน GPIO สี่พินเป็นเอาต์พุตแบบดิจิทัล (ต่อกับ LED)  
งาน (task) ของ FreeRTOS จะตรวจสอบสถานะของปุ่มอย่างต่อเนื่อง และเมื่อกดปุ่ม LED1 และ LED3 จะติด
เมื่อไม่ได้กดปุ่ม LED2 และ LED4 จะติดแทน
</br></br>

### 2.2.1 ข้อกำหนดฮาร์ดแวร์
- บอร์ด VCP-G (x1)
- เบรดบอร์ด (x1)
- LED (x4)
- สวิตช์ปุ่มกด (เซ็นเซอร์) (x1)
- อะแดปเตอร์จ่ายไฟ 12V 1A (x1)
- สาย USB Type-C to A (x1)
- สายจัมเปอร์ผู้-ผู้ (x11)
</br></br>

### 2.2.2 วงจร
- LED01
    - พิน (+) ต่อกับพินที่ 7 บนบอร์ด VCP-G
    - พิน (–) ต่อกับราง GND บนเบรดบอร์ด
- LED02
    - พิน (+) ต่อกับพินที่ 6 บนบอร์ด VCP-G
    - พิน (–) ต่อกับราง GND บนเบรดบอร์ด
- LED03
    - พิน (+) ต่อกับพินที่ 5 บนบอร์ด VCP-G
    - พิน (–) ต่อกับราง GND บนเบรดบอร์ด
- LED04
    - พิน (+) ต่อกับพินที่ 4 บนบอร์ด VCP-G
    - พิน (–) ต่อกับราง GND บนเบรดบอร์ด 
- สวิตช์ปุ่มกด
    - ขาข้างหนึ่งของสวิตช์ปุ่มกดต่อกับพินที่ 2 บนบอร์ด VCP-G
    - ขาที่อยู่ตรงข้ามในแนวทแยงของปุ่มต่อกับรางจ่ายไฟบนเบรดบอร์ด

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/F_digital_in.png" width="600"></p>
<p align="center"><strong>รูปที่ 2.2 ผังวงจรของ vcp4LED_Button</strong></p>

#### 2.2.2.1 การแมปพิน
ตารางต่อไปนี้แสดงการแมปพิน

<p align="center"><strong>ตารางที่ 2.2 การแมปพินของ vcp4LED_Button</strong></p>
<div align="center">
	<table>
	    <tr>
	        <th colspan="3">ชื่อพิน</th>
	        <th>บอร์ด VCP-G</th>
	        <th>GPIO</th>
	    </tr>
	    <tr>
	        <td colspan="3">พิน (+) ของ LED01</td>
	        <td>7</td>
	        <td>B[01]</td>
	    </tr>
	        <tr>
	        <td colspan="3">พิน (+) ของ LED02</td>
	        <td>6</td>
	        <td>A[13]</td>
	    </tr>
	        <tr>
	        <td colspan="3">พิน (+) ของ LED03</td>
	        <td>5</td>
	        <td>B[10]</td>
	    </tr>
	        <tr>
	        <td colspan="3">พิน (+) ของ LED04</td>
	        <td>4</td>
	        <td>B[27]</td>
	    </tr>
	    </tr>
	        <tr>
	        <td colspan="3">พินขาข้างหนึ่งของปุ่ม</td>
	        <td>2</td>
	        <td>B[28]</td>
	    </tr>
	</table>
</div>
</br></br>

### 2.2.3 วิธีการดำเนินการ
ในการรันตัวอย่างนี้ ให้แก้ไข **Main_StartTask()** ในไฟล์ main.c ตามที่แสดง
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
หลังจากแก้ไขโค้ดแล้ว ให้ไปยังไดเรกทอรีต่อไปนี้และรันคำสั่งบิลด์:  
```
$ cd ~/vcp/build/tcc70xx/gcc
$ make
```
ขั้นตอนนี้จะสร้างอิมเมจของเฟิร์มแวร์ และใช้เครื่องมือ ***FWDN*** เพื่อแฟลชอิมเมจที่สร้างขึ้นไปยัง VCP-G  
หลังจากแฟลชและรันโค้ดสำเร็จแล้ว การกดปุ่มจะทำให้ LED01 และ LED03 ติด ส่วนการปล่อยปุ่มจะทำให้ LED02 และ LED04 ติด
ระบบจะตรวจสอบสถานะของปุ่มอย่างต่อเนื่องและอัปเดตสถานะของ LED แบบเรียลไทม์ด้วยช่วงเวลาการโพลทุก 50 ms
</br></br></br></br>

# 3. VCP-G I2C
---
บทนี้ให้คำแนะนำในการกำหนดค่าการสื่อสารแบบ Inter-integrated Circuit (I2C) บน VCP-G ที่รัน FreeRTOS  
I2C เป็นโปรโตคอลการสื่อสารแบบซิงโครนัสสองสายที่ออกแบบมาเพื่อการแลกเปลี่ยนข้อมูลอย่างมีประสิทธิภาพระหว่างอุปกรณ์หลายตัว โดยทำงานด้วยสายข้อมูลอนุกรม (SDA) และสายสัญญาณนาฬิกาอนุกรม (SCL) ซึ่งช่วยให้อุปกรณ์ต่อพ่วงหลายตัวสื่อสารกับไมโครคอนโทรลเลอร์ได้โดยใช้แอดเดรสเฉพาะของแต่ละตัว I2C รองรับทั้งการสื่อสารแบบมาสเตอร์-สเลฟและการกำหนดค่าแบบหลายมาสเตอร์ จึงเหมาะอย่างยิ่งสำหรับการเชื่อมต่อเซ็นเซอร์ จอแสดงผล และอุปกรณ์ความเร็วต่ำอื่น ๆ ในขณะที่ลดจำนวนการเชื่อมต่อที่ต้องใช้ให้น้อยที่สุด
</br></br></br>

## 3.1 vcpI2C_LCD1602
---
โปรแกรมตัวอย่างนี้แสดงวิธีที่บอร์ด VCP-G ควบคุมจอแสดงผล LCD1602 โดยใช้โปรโตคอลการสื่อสาร I2C โดย LCD1602 เป็นจอผลึกเหลวขนาด 16 ตัวอักษร 2 บรรทัด ซึ่งนิยมใช้ในโปรเจกต์ระบบฝังตัว บอร์ดจะส่งคำสั่งและข้อมูลผ่านบัส I2C โดยใช้ไลบรารี LiquidCrystal_I2C เพื่อควบคุมจอแสดงผลอย่างมีประสิทธิภาพ  
ในตัวอย่างนี้ จอ LCD จะถูกเริ่มต้นการทำงานและเปิดไฟแบ็คไลท์เพื่อให้มองเห็นได้ชัดเจน จากนั้นโปรแกรมจะกำหนดตำแหน่งเคอร์เซอร์เพื่อแสดงข้อความ "Hello TOPST" บนหน้าจอ
</br></br>

### 3.1.1 ข้อกำหนดฮาร์ดแวร์
- บอร์ด VCP-G (x1)
- LCD1602 (x1)
- อะแดปเตอร์จ่ายไฟ 12V 1A (x1)
- สาย USB Type-C to A (x1)
- สายจัมเปอร์แบบผู้-เมีย (x4)
</br></br>

### 3.1.2 วงจร
- LCD1602
    - ขา VCC ของ LCD1602 เชื่อมต่อกับขาแอนะล็อก 5V บนบอร์ด VCP-G
    - ขา GND ของ LCD1602 เชื่อมต่อกับ GND บนบอร์ด VCP-G
    - พิน SDA ของ LCD1602 ต่อกับพินที่ 7 บนบอร์ด VCP-G
    - พิน SCL ของ LCD1602 ต่อกับพินที่ 8 บนบอร์ด VCP-G

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/F_i2c.png" width="600"></p>
<p align="center"><strong>รูปที่ 3.1 ผังวงจรของ vcpI2C_LCD1602</strong></p>

#### 3.1.2.1 การแมปพิน
ตารางต่อไปนี้แสดงการแมปพิน

<p align="center"><strong>ตารางที่ 3.1 การแมปพินของ vcpI2C_LCD1602</strong></p>
<div align="center">
	<table>
	    <tr>
	        <th colspan="3">ชื่อพิน</th>
	        <th>บอร์ด VCP-G</th>
	        <th>GPIO</th>
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
	        <td>7</td>
	        <td>B[01]</td>
	    </tr>
	        <tr>
	        <td colspan="3">พิน (-) ของ LED</td>
	        <td>8</td>
	        <td>B[00]</td>
	    </tr>
	</table>
</div>

</br></br>

### 3.1.3 วิธีการดำเนินการ
ในการรันตัวอย่างนี้ ให้แก้ไข **Main_StartTask()** ในไฟล์ main.c ตามที่แสดง
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
#### หมายเหตุเพิ่มเติมเกี่ยวกับการกำหนดค่า
ในการเปิดใช้งานการทดสอบ LCD ผ่าน I2C ให้ทำตามขั้นตอนต่อไปนี้:  

**1. เปิดใช้งาน lcd.c ในระบบบิลด์**  
- ไปยังพาธต่อไปนี้:
```
$ vi ~/vcp/sources/dev.drivers/i2c/rules.mk
```
- ค้นหาบรรทัดต่อไปนี้:
```
#SRCS += lcd.c
```
- ยกเลิกการคอมเมนต์บรรทัดดังกล่าวเพื่อเปิดใช้งานไฟล์:
```
SRCS += lcd.c
```

**2. ตรวจสอบหรือแก้ไขตรรกะของฟังก์ชัน LCD**  
หากคุณต้องการตรวจสอบหรือแก้ไขตรรกะสำหรับการเริ่มต้นการทำงานของ LCD คำสั่ง หรือฟังก์ชันการพิมพ์ โปรดดูที่:
```
$ vi ~/vcp/sources/dev.drivers/i2c/lcd.c
```

**3. กำหนดค่าช่องสัญญาณและพอร์ตของ I2C**  
หมายเลขช่องสัญญาณ I2C และพอร์ตที่เกี่ยวข้องซึ่ง LCD ใช้งานอยู่สามารถเปลี่ยนแปลงได้ที่:
```
$ vi ~/vcp/sources/dev.drivers/i2c/lcd.h
```

หลังจากแก้ไขโค้ดแล้ว ให้ไปยังไดเรกทอรีต่อไปนี้และรันคำสั่งบิลด์ต่อไปนี้:  
```
$ cd ~/vcp/build/tcc70xx/gcc
$ make
```
ขั้นตอนนี้จะสร้างอิมเมจของเฟิร์มแวร์ และใช้เครื่องมือ ***FWDN*** เพื่อแฟลชอิมเมจที่สร้างขึ้นไปยัง VCP-G  
หลังจากแฟลชและรันโค้ดสำเร็จแล้ว จอ LCD จะแสดงข้อความ "Hello TOPST" บนหน้าจอ ซึ่งยืนยันว่าการสื่อสาร I2C ทำงานได้อย่างถูกต้อง  
</br></br></br></br>

# 4. VCP SPI
---
บทนี้ให้คำแนะนำสำหรับการกำหนดค่าการสื่อสารแบบ Serial Peripheral Interface (SPI) บน VCP-G  
SPI เป็นโปรโตคอลการสื่อสารแบบซิงโครนัสความเร็วสูงที่ใช้แลกเปลี่ยนข้อมูลระหว่างไมโครคอนโทรลเลอร์กับอุปกรณ์ต่อพ่วง โดยทำงานด้วยสายสัญญาณแยกกันสำหรับการส่งข้อมูล (MOSI และ MISO) การซิงโครไนซ์สัญญาณนาฬิกา (SCK) และการเลือกอุปกรณ์ (SS) ซึ่งช่วยให้การสื่อสารมีประสิทธิภาพและเชื่อถือได้  
</br></br></br>

## 4.1 vcpSPI_Dot8x8
---
โปรแกรมตัวอย่างนี้แสดงวิธีที่บอร์ด VCP-G ควบคุม LED ดอตเมทริกซ์ขนาด 8x8 โดยใช้ไดรเวอร์ MAX7219 ผ่าน SPI
ในตัวอย่างนี้ มีการใช้อาร์เรย์ไบนารีที่กำหนดไว้ล่วงหน้าเพื่อแสดงตัวอักษร "X" บนดอตเมทริกซ์ การแสดงผลจะได้รับการอัปเดตผ่านการสื่อสาร SPI และ MAX7219 จะจัดการการควบคุมแถวและคอลัมน์ภายในตัวเอง
ตัวอย่างนี้ช่วยอธิบายวิธีการส่งรูปแบบข้อมูลผ่าน SPI เพื่อควบคุมอุปกรณ์แสดงผลภายนอก เช่น LED เมทริกซ์
</br></br>

### 4.1.1 ข้อกำหนดฮาร์ดแวร์
- บอร์ด VCP-G (x1)
- ดอตเมทริกซ์ขนาด 8x8 (x1)
- อะแดปเตอร์จ่ายไฟ 12V 1A (x1)
- สาย USB Type-C to A (x1)
- สายจัมเปอร์ผู้-เมีย (x2)
- สายจัมเปอร์ตัวเมีย-ตัวเมีย (x3)
</br></br>

### 4.1.2 วงจร
- ดอตเมทริกซ์ 8x8
    - ขา VCC ของดอตเมทริกซ์ขนาด 8x8 เชื่อมต่อกับขาแอนะล็อก 5V บนบอร์ด VCP-G
    - ขา GND ของดอตเมทริกซ์ขนาด 8x8 เชื่อมต่อกับ GND บนบอร์ด VCP-G
    - พิน DIN ของดอตเมทริกซ์ 8x8 เชื่อมต่อกับพิน SPI 4 บนบอร์ด VCP-G
    - พิน CS ของดอตเมทริกซ์ 8x8 เชื่อมต่อกับพิน SPI 5 บนบอร์ด VCP-G
    - พิน CLS ของดอตเมทริกซ์ 8x8 เชื่อมต่อกับพิน SPI 3 บนบอร์ด VCP-G

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/F_spi.png" width="600"></p>
<p align="center"><strong>รูปที่ 4.1 แผนผังวงจรของ vcpSPI_Dot8x8</strong></p>

#### 4.1.2.1 ผังพิน
ตารางต่อไปนี้แสดงการแมปพิน

<p align="center"><strong>ตารางที่ 4.1 ผังพินของ vcpSPI_Dot8x8</strong></p>
<div align="center">
	<table>
	    <tr>
	        <th colspan="3">ชื่อพิน</th>
	        <th>บอร์ด VCP-G</th>
	        <th>GPIO</th>
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
	        <td>SPI 4</td>
	        <td>B[06]</td>
	    </tr>
	    <tr>
	        <td colspan="3">ขา CS ของดอตเมทริกซ์ 8x8</td>
	        <td>SPI 5</td>
	        <td>B[05]</td>
	    </tr>
	    <tr>
	        <td colspan="3">ขา CLK ของดอตเมทริกซ์ 8x8</td>
	        <td>SPI 3</td>
	        <td>B[04]</td>
	    </tr>
	</table>
</div>
</br></br>

### 4.1.3 วิธีการดำเนินการ
ในการรันตัวอย่างนี้ ให้แก้ไข **Main_StartTask()** ในไฟล์ main.c ตามที่แสดง
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
#### หมายเหตุเพิ่มเติมเกี่ยวกับการกำหนดค่า
หากต้องการเปิดใช้งานการทดสอบดอตเมทริกซ์ผ่าน SPI ให้ทำตามขั้นตอนต่อไปนี้:  
**1. เปิดใช้งาน dot_matrix.c ในระบบบิลด์**  
- ไปยังพาธต่อไปนี้:
```
$ vi ~/vcp/sources/dev.drivers/gpsb/rules.mk
```
- ค้นหาบรรทัดต่อไปนี้:
```
#SRCS += dot_matrix.c
```
- ยกเลิกการคอมเมนต์เพื่อเปิดใช้งานไฟล์:
```
SRCS += dot_matrix.c
```
**2. ตรวจสอบหรือแก้ไขลอจิกการทำงานของดอตเมทริกซ์**  
หากต้องการตรวจสอบหรือแก้ไขลอจิกสำหรับการเริ่มต้นดอตเมทริกซ์ คำสั่งควบคุม หรือรูปแบบการแสดงผล ให้ดูไฟล์ซอร์สต่อไปนี้:
```
$ vi ~/vcp/sources/dev.drivers/gpsb/dot_matrix.c
```
**3. กำหนดค่าช่อง SPI และ GPIO**  
ช่อง SPI และพิน GPIO ที่เกี่ยวข้องซึ่งดอตเมทริกซ์ใช้งานสามารถกำหนดค่าได้ในไฟล์เฮดเดอร์ต่อไปนี้:
```
$ vi ~/vcp/sources/dev.drivers/gpsb/dot_matrix.h
```
หลังจากแก้ไขโค้ดแล้ว ให้ไปยังไดเรกทอรีต่อไปนี้และรันคำสั่งบิลด์:  
```
$ cd ~/vcp/build/tcc70xx/gcc
$ make
```
ขั้นตอนนี้จะสร้างอิมเมจของเฟิร์มแวร์ และใช้เครื่องมือ ***FWDN*** เพื่อแฟลชอิมเมจที่สร้างขึ้นไปยัง VCP-G  
หลังจากแฟลชและรันโค้ดสำเร็จ ดอตเมทริกซ์ LED 8x8 จะแสดงตัวอักษร "X" ซึ่งยืนยันว่าการสื่อสาร SPI กับไดรเวอร์ MAX7219 ทำงานได้อย่างถูกต้อง 
</br></br></br></br>

# 5. VCP-G UART
---
บทนี้ให้คำแนะนำสำหรับการกำหนดค่าการสื่อสารแบบ Universal Asynchronous Receiver-Transmitter (UART) บน VCP-G  
UART เป็นโปรโตคอลการสื่อสารแบบอนุกรมที่ใช้กันอย่างแพร่หลาย ซึ่งส่งข้อมูลแบบอะซิงโครนัสโดยใช้เพียงสองสาย คือ สายส่ง (TX) และสายรับ (RX) โปรโตคอลนี้มีความสำคัญอย่างยิ่งต่อการแลกเปลี่ยนข้อมูลระหว่างไมโครคอนโทรลเลอร์ เซ็นเซอร์ และคอมพิวเตอร์ โดยไม่ต้องใช้สัญญาณนาฬิการ่วมกัน  
บทต่อไปนี้อธิบายวิธีส่งและรับข้อมูลผ่าน UART
</br></br></br>

## 5.1 การทดสอบการสื่อสาร UART (FT232BL)
---
ตัวอย่างนี้แสดงวิธีการตรวจสอบการสื่อสาร UART บนบอร์ด VCP-G โดยใช้โมดูล FT232BL USB to TTL serial
พิน UART TX และ RX ของบอร์ด VCP-G เชื่อมต่อกับโมดูล FT232BL ซึ่งเชื่อมต่อกับ PC ผ่าน USB อีกทอดหนึ่ง
โปรแกรมเทอร์มินัล เช่น MobaXterm จะถูกใช้บน PC เพื่อดูข้อความที่ส่งออกมา
</br></br>

### 5.1.1 ข้อกำหนดฮาร์ดแวร์
- บอร์ด VCP-G (x1)
- โมดูล FT232BL USB to TTL serial (x1)
- สาย Mini USB (x1)
- อะแดปเตอร์จ่ายไฟ 12V 1A (x1)
- สาย USB Type-C to A (x1)
- สายจัมเปอร์ผู้-เมีย (x2)
</br></br>

### 5.1.2 วงจร
- FT232BL
    - พิน RXD ของโมดูล FT232BL เชื่อมต่อกับพิน 18 (TXD) บนบอร์ด VCP-G
    - พิน TXD ของโมดูล FT232BL เชื่อมต่อกับพิน 19 (RXD) บนบอร์ด VCP-G

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/F_uart.png" width="600"></p>
<p align="center"><strong>รูปที่ 5.1 แผนผังวงจร vcpUART</strong></p>

#### 5.1.2.1 ผังพิน
ตารางต่อไปนี้แสดงการแมปพิน

<p align="center"><strong>ตารางที่ 4.1 ผังพินของ vcpUART</strong></p>
<div align="center">
	<table>
	    <tr>
	        <th colspan="3">ชื่อพิน</th>
	        <th>บอร์ด VCP-G</th>
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

### 5.1.3 วิธีการดำเนินการ
ในการรันตัวอย่างนี้ ให้แก้ไข **Main_StartTask()** ในไฟล์ main.c ตามที่แสดง
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
#### หมายเหตุเพิ่มเติมเกี่ยวกับการกำหนดค่า
หากต้องการเปิดใช้งานการทดสอบ UART ให้ทำตามขั้นตอนต่อไปนี้:  
**1. เปิดใช้งาน uart_example.c ในระบบบิลด์**  
- ไปยังพาธต่อไปนี้:
```
$ vi ~/vcp/sources/dev.drivers/uart/rules.mk
```
- ค้นหาบรรทัดต่อไปนี้:
```
#SRCS += uart_example.c
```
- ยกเลิกการคอมเมนต์เพื่อเปิดใช้งานไฟล์:
```
SRCS += uart_example.c
```
**2. ตรวจสอบหรือแก้ไขลอจิกการทำงานของ UART**  
หากต้องการตรวจสอบหรือแก้ไขลอจิกสำหรับการเริ่มต้น UART การส่ง/รับข้อมูล หรือการจัดการอินเทอร์รัปต์ ให้ดูไฟล์ซอร์สต่อไปนี้:
```
$ vi ~/vcp/sources/dev.drivers/uart/tcc70xx/uart_example.c
```
**3. กำหนดค่าช่อง UART และ GPIO**  
ช่อง UART อัตราบอด และพิน GPIO TX/RX ที่เกี่ยวข้องซึ่งใช้สำหรับการทดสอบ UART สามารถกำหนดค่าได้ในไฟล์เฮดเดอร์ต่อไปนี้:
```
$ vi ~/vcp/sources/dev.drivers/uart/uart_example.h
```
หลังจากแก้ไขโค้ดแล้ว ให้ไปยังไดเรกทอรีต่อไปนี้และรันคำสั่งบิลด์:  
```
$ cd ~/vcp/build/tcc70xx/gcc
$ make
```
ขั้นตอนนี้จะสร้างอิมเมจของเฟิร์มแวร์ และใช้เครื่องมือ ***FWDN*** เพื่อแฟลชอิมเมจที่สร้างขึ้นไปยัง VCP-G  
หลังจากแฟลชและรันโค้ดสำเร็จ ข้อความ "[UART] Hello from UART!" จะปรากฏขึ้นหนึ่งครั้งบนเทอร์มินัลอนุกรม ซึ่งยืนยันว่าการส่งข้อมูล UART จากบอร์ด VCP-G ผ่านโมดูล FT232BL USB to TTL ทำงานได้อย่างถูกต้อง
</br></br></br></br>

# 6. VCP-G PWM
---
บทนี้ให้คำแนะนำสำหรับการกำหนดค่า Pulse Width Modulation (PWM) บน VCP-G โดย PWM เป็นเทคนิคที่ใช้ควบคุมปริมาณพลังงานที่ส่งไปยังอุปกรณ์ เช่น มอเตอร์ LED และบัซเซอร์ ด้วยการเปลี่ยนดิวตี้ไซเคิลของสัญญาณดิจิทัล เทคนิคนี้ทำงานโดยการสลับเปิดและปิดพินเอาต์พุตที่ความถี่สูง โดยอัตราส่วนของเวลาที่เปิดต่อคาบเวลาทั้งหมดจะกำหนดระดับเอาต์พุตที่มีผล บทต่อไปนี้อธิบายวิธีการสร้างสัญญาณ PWM โดยใช้ FreeRTOS บน VCP-G และวิธีการนำไปใช้ควบคุมชิ้นส่วนภายนอก
</br></br></br>

## 6.1 pwmFade
---
โปรแกรมตัวอย่างนี้แสดงวิธีที่บอร์ด VCP ควบคุม LED บนเบรดบอร์ดโดยค่อย ๆ เพิ่มและลดความสว่างเป็นวงรอบด้วยการใช้ PWM หลังจาก LED มีความสว่างสูงสุดแล้ว ความสว่างของ LED จะเริ่มลดลง โปรแกรมจะปรับความสว่างของ LED อย่างต่อเนื่อง ทำให้เกิดเอฟเฟกต์การหรี่แสง
</br></br>

### 6.1.1 ข้อกำหนดฮาร์ดแวร์
- บอร์ด VCP-G (x1)
- เบรดบอร์ด (x1)
- LED (x1)
- อะแดปเตอร์จ่ายไฟ 12V 1A (x1)
- สาย USB Type-C to A (x1)
- สายจัมเปอร์แบบผู้-ผู้ (x2)
</br></br>

### 6.1.2 วงจร
- LED
    - พิน (+) เชื่อมต่อกับพิน 45 บนบอร์ด VCP-G
    - พิน (–) ต่อกับราง GND บนเบรดบอร์ด

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/F_pwm.png" width="600"></p>
<p align="center"><strong>รูปที่ 5.1 แผนผังวงจร pwmFade</strong></p>

#### 6.1.2.1 ผังพิน
ตารางต่อไปนี้แสดงการแมปพิน

<p align="center"><strong>ตารางที่ 4.1 ผังพินของ pwmFade</strong></p>
<div align="center">
	<table>
	    <tr>
	        <th colspan="3">ชื่อพิน</th>
	        <th>บอร์ด VCP-G</th>
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

### 6.1.3 วิธีการดำเนินการ
ในการรันตัวอย่างนี้ ให้แก้ไข **Main_StartTask()** ในไฟล์ main.c ตามที่แสดง
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
หลังจากแก้ไขโค้ดแล้ว ให้ไปยังไดเรกทอรีต่อไปนี้และรันคำสั่งบิลด์:  
```
$ cd ~/vcp/build/tcc70xx/gcc
$ make
```
ขั้นตอนนี้จะสร้างอิมเมจของเฟิร์มแวร์ และใช้เครื่องมือ ***FWDN*** เพื่อแฟลชอิมเมจที่สร้างขึ้นไปยัง VCP-G  
หลังจากแฟลชและรันโค้ดสำเร็จ คุณจะสังเกตเห็นเอฟเฟกต์การค่อย ๆ สว่างขึ้นและหรี่ลงของ LED ที่ขับด้วย PWM บน GPIO A10 ซึ่งยืนยันว่าเอาต์พุต PWM ที่ใช้ PDM ของ VCP-G ทำงานได้อย่างถูกต้อง

**หมายเหตุ**: หากต้องการเปลี่ยนพอร์ต GPIO ที่ใช้สำหรับเอาต์พุต PWM ให้ดูการกำหนดค่าในไฟล์ pdm.c
</br></br></br></br>

# 7. ตัวอย่างเพิ่มเติม
---
บทนี้แนะนำตัวอย่างเซ็นเซอร์เพิ่มเติมที่ใช้ FreeRTOS บนบอร์ด VCP-G โดยให้คู่มือตัวอย่างเกี่ยวกับวิธีการใช้เซ็นเซอร์ Arduino ที่ใช้กันทั่วไปร่วมกับ FreeRTOS บนบอร์ด VCP-G ซึ่งช่วยให้คุณผสานเซ็นเซอร์ต่าง ๆ เข้ากับโปรเจกต์ของคุณได้อย่างมีประสิทธิภาพ
</br></br></br>

## 7.1 เซ็นเซอร์อินฟราเรด (IR) (ตัวรับส่งสัญญาณ)
---
ตัวอย่างนี้แสดงวิธีที่บอร์ด VCP-G ควบคุมเซ็นเซอร์ IR และ LED สองดวงบนเบรดบอร์ด เมื่อเซ็นเซอร์ IR ตรวจพบวัตถุ (ค่าเซ็นเซอร์เป็น LOW) LED ดวงแรกจะติดและ LED ดวงที่สองจะดับ ในทางกลับกัน เมื่อไม่พบวัตถุ (ค่าเซ็นเซอร์เป็น HIGH) LED ดวงที่สองจะติดในขณะที่ LED ดวงแรกจะดับ การมีอยู่หรือไม่มีอยู่ของวัตถุจะถูกแสดงบนซีเรียลมอนิเตอร์ด้วย
</br></br>

### 7.1.1 ข้อกำหนดด้านฮาร์ดแวร์
- บอร์ด VCP-G (x1)
- เบรดบอร์ด (x1)
- เซ็นเซอร์รับส่งสัญญาณ IR (x1)
- LED (x2: แนะนำให้ใช้คนละสี)
- อะแดปเตอร์จ่ายไฟ 12V 1A (x1)
- สาย USB Type-C to A (x1)
- สายจัมเปอร์ผู้-ผู้ (x5)
- สายจัมเปอร์ตัวผู้-ตัวเมีย (x3)
</br></br>

### 7.1.2 วงจร
- เซ็นเซอร์รับส่งสัญญาณ IR
    - พิน OUT ของเซ็นเซอร์ IR เชื่อมต่อกับพิน 38 บนบอร์ด VCP-G
    - ขา VCC ของเซ็นเซอร์ IR เชื่อมต่อกับ 5V บนบอร์ด VCP-G
    - ขา GND ของเซ็นเซอร์ IR เชื่อมต่อกับ GND บนบอร์ด VCP-G
- LED01
    - พิน (+) เชื่อมต่อกับพิน 16 บนบอร์ด VCP-G
    - พิน (–) ต่อกับราง GND บนเบรดบอร์ด
- LED02
    - พิน (+) เชื่อมต่อกับพิน 17 บนบอร์ด VCP-G
    - พิน (–) ต่อกับราง GND บนเบรดบอร์ด

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/F_irsensor1.png" width="600"></p>
<p align="center"><strong>รูปที่ 7.1 แผนผังวงจรของเซ็นเซอร์อินฟราเรด (IR)</strong></p>

##### 7.1.2.1 ผังพิน
ตารางต่อไปนี้แสดงการแมปพิน

<p align="center"><strong>ตารางที่ 7.1 ผังพินของ irSensor_LED</strong></p>
<div align="center">
	<table>
	    <tr>
	        <th colspan="3">ชื่อพิน</th>
	        <th>บอร์ด VCP-G</th>
	        <th>GPIO</th>
	    </tr>
	    <tr>
	        <td colspan="3">ขา OUT ของเซ็นเซอร์ IR </td>
	        <td>38</td>
	        <td>K[13]</td>
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
	        <td colspan="3">พิน (+) ของ LED01</td>
	        <td>16</td>
	        <td>A[06]</td>
	    </tr>
	    <tr>
	        <td colspan="3">พิน (-) ของ LED01</td>
	        <td>GND</td>
	        <td>-</td>
	    </tr>
	    <tr>
	        <td colspan="3">พิน (+) ของ LED02</td>
	        <td>17</td>
	        <td>A[07]</td>
	    </tr>
	    <tr>
	        <td colspan="3">พิน LED02 (-) </td>
	        <td>GND</td>
	        <td>-</td>
	    </tr>
	</table>
</div>
</br></br>

### 7.1.3 วิธีการดำเนินการ
ในการรันตัวอย่างนี้ ให้แก้ไข **Main_StartTask()** ในไฟล์ main.c ตามที่แสดง
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
หลังจากแก้ไขโค้ดแล้ว ให้ไปยังไดเรกทอรีต่อไปนี้และรันคำสั่งบิลด์:  
```
$ cd ~/vcp/build/tcc70xx/gcc
$ make
```
ขั้นตอนนี้จะสร้างอิมเมจของเฟิร์มแวร์ และใช้เครื่องมือ ***FWDN*** เพื่อแฟลชอิมเมจที่สร้างขึ้นไปยัง VCP-G  
หลังจากแฟลชและรันโค้ดสำเร็จ เซ็นเซอร์ IR จะตรวจจับการมีอยู่หรือไม่มีอยู่ของวัตถุและควบคุม LED สองดวงตามนั้น เมื่อตรวจพบวัตถุ LED ดวงแรกจะติด เมื่อไม่พบวัตถุ LED ดวงที่สองจะติด พฤติกรรมนี้ยืนยันว่าอินพุตของเซ็นเซอร์ IR และเอาต์พุต GPIO บนบอร์ด VCP-G ทำงานได้อย่างถูกต้อง

**หมายเหตุ**: หากคุณต้องการเปลี่ยนพิน GPIO ที่ใช้สำหรับเซ็นเซอร์ IR หรือ LED ให้ดูส่วนการกำหนดค่าภายในซอร์สโค้ด
</br></br></br>

## 7.2 เซ็นเซอร์อินฟราเรด (IR) (ตัวรับ)
---
ตัวอย่างนี้แสดงวิธีที่บอร์ด VCP-G ใช้เซ็นเซอร์ตัวรับ IR เพื่อตรวจจับสัญญาณจากรีโมตคอนโทรล เมื่อได้รับสัญญาณ IR ลอจิกบนบอร์ดจะเปิด LED ที่เชื่อมต่อกับเบรดบอร์ด สิ่งนี้ยืนยันว่าโมดูลตัวรับ IR ถอดรหัสสัญญาณที่เข้ามาได้อย่างถูกต้อง และ VCP-G ตอบสนองตามที่คาดไว้ สถานะการรับสัญญาณจะแสดงบนซีเรียลมอนิเตอร์ด้วย
</br></br>

### 7.2.1 ข้อกำหนดฮาร์ดแวร์
- บอร์ด VCP-G (x1)
- เบรดบอร์ด (x1)
- เซ็นเซอร์ตัวรับ IR (x1)
- รีโมต Arduino (x1)
- LED (x1)
- อะแดปเตอร์จ่ายไฟ 12V 1A (x1)
- สาย USB Type-C to A (x1)
- สายจัมเปอร์ผู้-ผู้ (x5)
</br></br>

### 7.2.2 วงจร
- เซ็นเซอร์ตัวรับ IR
    - พิน SIG ของเซ็นเซอร์ IR เชื่อมต่อกับพิน 40 บนบอร์ด VCP-G
    - ขา GND ของเซ็นเซอร์ IR เชื่อมต่อกับ GND บนบอร์ด VCP-G
    - ขา VCC ของเซ็นเซอร์ IR เชื่อมต่อกับ 5V บนบอร์ด VCP-G
- LED
    - พิน (+) ต่อกับพินที่ 7 บนบอร์ด VCP-G
    - พิน (–) ต่อกับราง GND บนเบรดบอร์ด

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/F_irsensor2.png" width="600"></p>
<p align="center"><strong>รูปที่ 7.2 แผนผังวงจรเซ็นเซอร์ตัวรับ IR</strong></p>

##### 7.2.2.1 ผังพิน
ตารางต่อไปนี้แสดงการแมปพิน

<p align="center"><strong>ตารางที่ 7.1 ผังพินของ irSensor_LED</strong></p>
<div align="center">
	<table>
	    <tr>
	        <th colspan="3">ชื่อพิน</th>
	        <th>บอร์ด VCP-G</th>
	        <th>GPIO</th>
	    </tr>
	    <tr>
	        <td colspan="3">พิน SIG ของเซ็นเซอร์ IR </td>
	        <td>40</td>
	        <td>K[11]</td>
	    </tr>
	        <tr>
	        <td colspan="3">พิน GND ของเซ็นเซอร์ IR </td>
	        <td>GND</td>
	        <td>-</td>
	    </tr>
	    <tr>
	        <td colspan="3">พิน VCC ของเซ็นเซอร์ IR</td>
	        <td>VCC</td>
	        <td>-</td>
	    </tr>
	    <tr>
	        <td colspan="3">พิน (+) ของ LED</td>
	        <td>7</td>
	        <td>B[01]</td>
	    </tr>
	    <tr>
	        <td colspan="3">พิน (-) ของ LED</td>
	        <td>GND</td>
	        <td>-</td>
	    </tr>
	</table>
</div>

</br></br>

### 7.2.3 วิธีการดำเนินการ
ในการรันตัวอย่างนี้ ให้แก้ไข **Main_StartTask()** ในไฟล์ main.c ตามที่แสดง
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
หลังจากแก้ไขโค้ดแล้ว ให้ไปยังไดเรกทอรีต่อไปนี้และรันคำสั่งบิลด์:  
```
$ cd ~/vcp/build/tcc70xx/gcc
$ make
```
ขั้นตอนนี้จะสร้างอิมเมจของเฟิร์มแวร์ และใช้เครื่องมือ ***FWDN*** เพื่อแฟลชอิมเมจที่สร้างขึ้นไปยัง VCP-G  
หลังจากแฟลชและรันโค้ดสำเร็จ ตัวรับ IR จะตรวจจับสัญญาณจากรีโมตคอนโทรลและเปิด LED เป็นเวลาสั้น ๆ สิ่งนี้ยืนยันว่า VCP-G อ่านอินพุต IR ได้อย่างถูกต้องและควบคุมเอาต์พุต GPIO ตามสัญญาณที่ได้รับ

**หมายเหตุ**: หากต้องการเปลี่ยนพิน GPIO ที่ใช้สำหรับเซ็นเซอร์ IR หรือ LED ให้ดูส่วนการกำหนดค่าภายในซอร์สโค้ด
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
    - พิน A0 ของเซ็นเซอร์แก๊สเชื่อมต่อกับพินแอนะล็อก 55 บนบอร์ด VCP-G 
    - ขา VCC ของเซ็นเซอร์แก๊สเชื่อมต่อกับ 5V บนบอร์ด VCP-G
    - ขา GND ของเซ็นเซอร์แก๊สเชื่อมต่อกับ GND บนบอร์ด VCP-G

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/F_gassensor.png" width="600"></p>
<p align="center"><strong>รูปที่ 7.3 แผนผังวงจรเซ็นเซอร์แก๊ส</strong></p>

#### 7.3.2.1 ผังพิน
ตารางต่อไปนี้แสดงการแมปพิน

<p align="center"><strong>ตารางที่ 7.3 ผังพินของเซ็นเซอร์แก๊ส</strong></p>
<div align="center">
	<table>
	    <tr>
	        <th colspan="3">ชื่อพิน</th>
	        <th>บอร์ด VCP-G</th>
	        <th>GPIO</th>
	    </tr>
	    <tr>
	        <td colspan="3">ขา A0 ของเซ็นเซอร์แก๊ส</td>
	        <td>55</td>
	        <td>K[15]</td>
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
ในการรันตัวอย่างนี้ ให้แก้ไข **Main_StartTask()** ในไฟล์ main.c ตามที่แสดง
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
หลังจากแก้ไขโค้ดแล้ว ให้ไปยังไดเรกทอรีต่อไปนี้และรันคำสั่งบิลด์:  
```
$ cd ~/vcp/build/tcc70xx/gcc
$ make
```
ขั้นตอนนี้จะสร้างอิมเมจเฟิร์มแวร์และใช้เครื่องมือ **FWDN** เพื่อแฟลชอิมเมจที่สร้างขึ้นไปยัง VCP-G  
หลังจากแฟลชและรันโค้ดสำเร็จ เซ็นเซอร์แก๊สจะตรวจสอบคุณภาพอากาศโดยรอบอย่างต่อเนื่อง เมื่อตรวจพบแก๊ส (เอาต์พุตของเซ็นเซอร์เป็น LOW) ข้อความที่ระบุการตรวจพบแก๊สจะแสดงบนซีเรียลมอนิเตอร์ มิฉะนั้นจะรายงานว่าอากาศสะอาด สิ่งนี้ยืนยันว่า VCP-G อ่านอินพุตดิจิทัลจากเซ็นเซอร์แก๊สได้อย่างถูกต้อง

**หมายเหตุ**: หากต้องการเปลี่ยนพิน GPIO ที่ใช้สำหรับเซ็นเซอร์แก๊ส ให้ดูส่วนการกำหนดค่าภายในซอร์สโค้ด โมดูลเซ็นเซอร์แก๊สส่วนใหญ่มีสกรูปรับขนาดเล็ก (โพเทนชิโอมิเตอร์) สำหรับควบคุมความไว หากเซ็นเซอร์ตอบสนองไม่สม่ำเสมอ ให้ลองปรับสกรูนี้เพื่อปรับค่าเกณฑ์การตรวจจับแก๊สอย่างละเอียด
</br></br></br>

## 7.4 เซ็นเซอร์สัมผัสแบบคาปาซิทีฟ
---
ตัวอย่างนี้แสดงวิธีที่บอร์ด VCP-G เชื่อมต่อกับเซ็นเซอร์สัมผัสแบบคาปาซิทีฟและควบคุม LED บนเบรดบอร์ด เซ็นเซอร์สัมผัสแบบคาปาซิทีฟตรวจจับการสัมผัสทางกายภาพจากนิ้วมือโดยการตรวจจับการเปลี่ยนแปลงของค่าความจุไฟฟ้า  
เมื่อตรวจพบการสัมผัส เซ็นเซอร์จะส่งสัญญาณดิจิทัล HIGH ไปยัง VCP-G ซึ่งจะเปิด LED ตามลำดับ ตัวอย่างนี้ยืนยันว่าอินพุตการสัมผัสได้รับการรับรู้อย่างถูกต้องและเอาต์พุต GPIO ตอบสนองตามนั้น สถานะการตรวจจับการสัมผัสจะแสดงบนซีเรียลมอนิเตอร์ด้วย
</br></br>

### 7.4.1 ข้อกำหนดฮาร์ดแวร์
- บอร์ด VCP-G (x1)
- เบรดบอร์ด (x1)
- เซ็นเซอร์สัมผัสแบบคาปาซิทีฟ (x1)
- LED (x1)
- อะแดปเตอร์จ่ายไฟ 12V 1A (x1)
- สาย USB Type-C to A (x1)
- สายจัมเปอร์แบบผู้-ผู้ (x6)
</br></br>

### 7.4.2 วงจร
- เซ็นเซอร์สัมผัส 
    - พิน SIG ของโมดูลเซ็นเซอร์สัมผัสเชื่อมต่อกับพิน 39 บนบอร์ด VCP-G
    - พิน VCC ของโมดูลเซ็นเซอร์สัมผัสเชื่อมต่อกับ 5V บนบอร์ด VCP-G
    - ขา GND ของโมดูลเซ็นเซอร์สัมผัสเชื่อมต่อกับ GND บนบอร์ด VCP-G
- LED
    - ขา (+) ของ LED เชื่อมต่อกับพิน 7 บนบอร์ด VCP-G
    - ขา (–) ของ LED เชื่อมต่อกับราง GND บนเบรดบอร์ด

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/F_touchsensor.png" width="600"></p>
<p align="center"><strong>รูปที่ 7.4 ผังวงจรของเซ็นเซอร์สัมผัส</strong></p>

#### 7.4.2.1 การแมปพิน
ตารางต่อไปนี้แสดงการแมปพิน

<p align="center"><strong>ตารางที่ 7.5 การแมปพินของเซ็นเซอร์สัมผัส</strong></p>
<div align="center">
	<table>
	    <tr>
	        <th colspan="3">ชื่อพิน</th>
	        <th>บอร์ด VCP-G</th>
	        <th>GPIO</th>
	    </tr>
	    <tr>
	        <td colspan="3">ขา SIG ของเซ็นเซอร์สัมผัส</td>
	        <td>39</td>
	        <td>K[12]</td>
	    </tr>
	        <tr>
	        <td colspan="3">ขา VCC ของเซ็นเซอร์สัมผัส</td>
	        <td>5V</td>
	        <td>-</td>
	    </tr>
	    <tr>
	        <td colspan="3">ขา GND ของเซ็นเซอร์สัมผัส</td>
	        <td>GND</td>
		    <td>-</td>
		</tr>
	    <tr>
	        <td colspan="3">พิน (+) ของ LED</td>
	        <td>7</td>
	        <td>B[01]</td>
	    </tr>
	    <tr>
	        <td colspan="3">พิน (-) ของ LED</td>
	        <td>GND</td>
	        <td>-</td>
	    </tr>
	</table>
</div>

</br></br>

### 7.4.3 วิธีการดำเนินการ
ในการรันตัวอย่างนี้ ให้แก้ไข **Main_StartTask()** ในไฟล์ main.c ตามที่แสดง
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
หลังจากแก้ไขโค้ดแล้ว ให้ไปยังไดเรกทอรีต่อไปนี้และรันคำสั่งบิลด์:  
```
$ cd ~/vcp/build/tcc70xx/gcc
$ make
```
ขั้นตอนนี้จะสร้างอิมเมจเฟิร์มแวร์ และใช้เครื่องมือ FWDN เพื่อแฟลชอิมเมจที่สร้างขึ้นลงใน VCP-G  
เมื่อแฟลชและรันโค้ดสำเร็จ เซ็นเซอร์สัมผัสแบบคาปาซิทีฟจะตรวจจับการสัมผัสจากนิ้วมือของมนุษย์ เมื่อตรวจพบการสัมผัส (เอาต์พุตของเซ็นเซอร์เป็น HIGH) ข้อความจะถูกแสดงบนซีเรียลมอนิเตอร์และ LED จะติดสว่าง เมื่อไม่พบการสัมผัส LED จะดับลง สิ่งนี้ยืนยันว่า VCP-G อ่านอินพุตจากเซ็นเซอร์สัมผัสได้อย่างถูกต้องและควบคุมเอาต์พุต GPIO ได้อย่างเหมาะสม

**หมายเหตุ**: หากต้องการเปลี่ยนพิน GPIO ที่ใช้กับเซ็นเซอร์สัมผัสหรือ LED โปรดดูส่วนการกำหนดค่าภายในซอร์สโค้ด
</br></br></br></br>

# 8. เอกสารอ้างอิง
---
- ติดต่อ TOPST สำหรับรายละเอียดเพิ่มเติม: topst@topst.ai

**หมายเหตุ:** เอกสารอ้างอิงสามารถจัดหาให้ได้เมื่อมีอยู่ ทั้งนี้ขึ้นอยู่กับเงื่อนไขของสัญญา หากไม่มีเอกสาร
อ้างอิงดังกล่าว จะมีการแนะนำเนื้อหาที่เกี่ยวข้องโดยตรงกับการพัฒนาของท่านแทน
