# 1. บทนำ
---
เอกสารนี้เป็นคู่มือผู้ใช้ด้านฮาร์ดแวร์สำหรับ VCP-G ซึ่งใช้แอปพลิเคชันโปรเซสเซอร์ TCC7045 เอกสารนี้อธิบายการติดตั้งระบบ การดีบัก และข้อมูลโดยละเอียดเกี่ยวกับการออกแบบและการใช้งานโดยรวมของ VCP-G


ตารางที่ 1.1 อธิบายคุณสมบัติของ VCP-G

<p align="center"><strong>ตารางที่ 1.1 คุณสมบัติของ VCP-G</strong></p>
<div align="center">
	<table>
	  <tr>
	    <td colspan="3">ชื่อชิ้นส่วน</td>
	    <td>TCC7045</td>
	  </tr>
	  <tr>
	    <td colspan="3">แพ็กเกจ</td>
	    <td>แพ็กเกจ	เข้ากันได้แบบพินต่อพิน FBGA 196-pin (12BD)</td>
	  </tr>
	    <tr>
	    <td colspan="3">ความถี่ CPU</td>
	    <td>200 MHz (สูงสุด 300 MHz)</td>
	  </tr>
	  <tr>
	    <td rowspan="4">หน่วยความจำบนชิป</td>
	    <td colspan="2">แฟลชโปรแกรม</td>
	    <td colspan="3">4 MB</td>
	  </tr>
	  <tr>
	    <td colspan="2">SRAM</td>
	    <td colspan="3">512 KB (รวม Retention RAM 16 KB)</td>
	  </tr>
	  <tr>
	    <td colspan="2">DataFlash</td>
	    <td colspan="3">256 KB</td>
	  </tr>
	  <tr>
	    <td colspan="2">ช่องสัญญาณ DMA</td>
	    <td colspan="3">16 ช่องสัญญาณ</td>
	  </tr>
	  <tr>
	    <td rowspan="13">อุปกรณ์ต่อพ่วง</td>
	    <td colspan="2">Ethernet</td>
	    <td>1 Gbps พร้อม AVB</td>
	  </tr>
	  <tr>
		<td colspan="2">CAN / CANFD</td>
	    <td>3 ช่องสัญญาณ</td>
	  </tr>
	  <tr>
	    <td colspan="2">LIN / UART เฉพาะ</td>
	    <td>3 ช่องสัญญาณ (สูงสุด 6 ช่องสัญญาณ)</td>
	  </tr>
	  <tr>
	    <td colspan="2">I2C เฉพาะ</td>
	    <td>3 ช่องสัญญาณ (สูงสุด 6 ช่องสัญญาณ)</td>
	  </tr>
	  <tr>
	  <tr>
	    <td colspan="2">GPSB (SPI) เฉพาะ</td>
	    <td>2 ช่องสัญญาณ (สูงสุด 5 ช่องสัญญาณ)</td>
	  </tr>
	    <tr>
	    <td colspan="2">MFIO (กำหนดให้ UART, I2C, GPSB)</td>
	    <td>3 ช่องสัญญาณ</td>
	  </tr>
	  <tr>
	    <td rowspan="4">ADC</td> 
	    <td>ความละเอียด</td>
	    <td>แบบ SAR ขนาด 12 บิต</td>
	  </tr>
	  <tr>
	    <td>ช่องสัญญาณ</td>
	    <td>12 ช่องสัญญาณ x 2 กลุ่ม</td>
	  </tr>
	  <tr>
	    <td>ช่วงอินพุต</td>
	    <td>3.3V</td>
	  </tr>
	  <tr>
	    <td>อัตราการสุ่มตัวอย่าง</td>
	    <td>มากกว่า 1.0 MSPs</td>
	  </tr>
	  <tr>
	    <td colspan="2">I2S</td>
	    <td>1 ช่องสัญญาณ</td>
	  </tr>
	  <tr>
	    <td colspan="2">อินเทอร์เฟซซีเรียลแฟลช</td>
	    <td>Quad SPI</td>
	  </tr>  
	  <tr>
	    <td colspan="3">ระบบไฟเลี้ยง</td>
	    <td>3.3V แหล่งเดียว</td>
	  </tr>
	  <tr>
	    <td colspan="3">อุณหภูมิ</td>
	    <td>-40 ℃ to 105 ℃</td>
	  </tr>
	</table>
</div>

</br></br></br>

## 1.1 คำศัพท์
---
<p align="center"><strong>ตารางที่ 1.2 คำศัพท์ </strong></p>
<div align="center">
	<table>
	  <tr>
	    <td clospan="2"><strong>คำศัพท์</strong></td>
	    <td><strong>คำจำกัดความ</strong></td>
	  </tr>
	  <tr>
	    <td clospan="2">ADC</td>
	    <td>ตัวแปลงสัญญาณแอนะล็อกเป็นดิจิทัล</td>
	  </tr>
	  <tr>
	    <td clospan="2">FWDN</td>
	    <td>การดาวน์โหลดเฟิร์มแวร์</td>
	  </tr>
	  <tr>
	    <td clospan="2">GPIO</td>
	    <td>อินพุตเอาต์พุตอเนกประสงค์</td>
	  </tr>
	  <tr>
	    <td clospan="2">MCU</td>
	    <td>หน่วยไมโครคอนโทรลเลอร์</td>
	  </tr>
	  <tr>
	    <td clospan="2">TOPST</td>
	    <td>แพลตฟอร์มเปิดแบบครบวงจรสำหรับการพัฒนาระบบและการฝึกอบรม</td>
	  </tr>
	  <tr>
	    <td clospan="2">VCP</td>
	    <td>โปรเซสเซอร์ควบคุมยานยนต์</td>
	  </tr>
	</table>
</div>

</br></br></br></br>

# 2. แผนภาพบล็อก
---
## 2.1 แผนภาพบล็อกของระบบ
---
รูปที่ 2.1 แสดงแผนภาพบล็อกของระบบของ VCP-G
<p align="center"><img src= "https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Hardware/2.1%20VCP-G%20System%20Block%20Diagram.png"></p>
<p align="center"><strong>รูปที่ 2.1 แผนภาพบล็อกของระบบ</strong></p>

</br></br></br></br>

# 3. ภาพรวมของ VCP-G
---
VCP-G สามารถใช้งานได้ตามวัตถุประสงค์ต่อไปนี้:
  - การพัฒนาระบบ
  - การฝึกอบรม

ตารางที่ 3.1 อธิบายการกำหนดค่าเริ่มต้นของ VCP-G

<p align="center"><strong>ตารางที่ 3.1 การกำหนดค่าเริ่มต้นของ VCP-G </strong></p>
<div align="center">
	<table>
	  <tr>
	    <td colspan="2"><strong>ชื่อบอร์ด</strong></td>
	    <td><strong>คำอธิบาย</strong></p>
	  </tr>
	  <tr>
	    <td colspan="2">TOPST_VCP_V2.1.1</td>
	    <td>บอร์ด MCU สำหรับ TOPST</td>
	  </tr>
	</table>
</div>

</br></br></br>

## 3.1 VCP-G
---
รูปที่ 3.1 แสดงมุมมองด้านบนของ VCP-G
<p align="center"><img src= "https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Hardware/3.1%20TOPST%20VCP-G%20Board%20(Top%20View)%20.png"></p>
<p align="center"><strong>รูปที่ 3.1 VCP-G (มุมมองด้านบน)</strong></p>

ตารางที่ 3.2 อธิบายขั้วต่อของ VCP-G (มุมมองด้านบน)
<p align="center"><strong>ตารางที่ 3.2 ขั้วต่อของ VCP-G (มุมมองด้านบน)</strong></p>
<div align="center">
	<table>
	  <tr>
	    <td colspan="4"><strong>หมายเลข</strong></td>
	    <td><strong>หมายเลขอ้างอิง</strong></td>
	    <td><strong>ชื่อ</strong></td>
	    <td><strong>คำอธิบาย</strong></td>
	  </tr>
	  <tr>
	    <td colspan="4">1</td>
	    <td>J18D100</td>
	    <td>เฮดเดอร์ตัวเมีย 36 พิน</td>
	    <td>เฮดเดอร์สำหรับ GPIO และ ADC</td>
	  </tr>
	  <tr>
	    <td colspan="4">2</td>
	    <td>J5D100</td>
	    <td>เฮดเดอร์ตัวผู้ 10 พิน</td>
	    <td>เฮดเดอร์สำหรับ CAN</td>
	  </tr>
	  <tr>
	    <td colspan="4">3</td>
	    <td>J3D100</td>
	    <td>เฮดเดอร์ตัวผู้ 6 พิน</td>
	    <td>เฮดเดอร์สำหรับ SPI</td>
	  </tr>
	  <tr>
	    <td colspan="4">4</td>
	    <td>J8D104</td>
	    <td>เฮดเดอร์ตัวเมีย 8 พิน</td>
	    <td>เฮดเดอร์สำหรับ GPIO และ ADC</td>
	  </tr>
	  <tr>
	    <td colspan="4">5</td>
	    <td>J8D102</td>
	    <td>เฮดเดอร์ตัวเมีย 8 พิน</td>
	    <td>เฮดเดอร์สำหรับ GPIO</td>
	  </tr>
	  <tr>
	    <td colspan="4">6</td>
	    <td>J10D100</td>
	    <td>เฮดเดอร์ตัวเมีย 10 พิน</td>
	    <td>เฮดเดอร์สำหรับ GPIO และ ADC</td>
	  </tr>
	  <tr>
	    <td colspan="4">7</td>
	    <td>J100</td>
	    <td>เฮดเดอร์ตัวผู้ 10 พิน</td>
	    <td>เฮดเดอร์สำหรับ JTAG</td>
	  </tr>
	  <tr>
	    <td colspan="4">8</td>
	    <td>SW100</td>
	    <td>สวิตช์แท็กต์ RESET</td>
	    <td>GRESETn: เริ่มต้นระบบและการจัดการพลังงานของ VCP-G ใหม่</td>
	  </tr>
	  <tr>
	    <td colspan="4">9</td>
	    <td>JC100</td>
	    <td>ขั้วต่อ USB Type-C</td>
	    <td>UART สำหรับการดีบักหรือพอร์ต FWDN</td>
	  </tr>
	  <tr>
	    <td colspan="4">10</td>
	    <td>SW101</td>
	    <td>สวิตช์แท็กต์</td>
	    <td>FWDN: เข้าสู่โหมดดาวน์โหลดเฟิร์มแวร์ของ VCP-G</td>
	  </tr>  
	  <tr>
	    <td colspan="4">11</td>
		<td>J101</td>
	    <td>แจ็ค DC</td>
	    <td>แจ็คอินพุตไฟเลี้ยง DC</td>
	  </tr>  
	  <tr>
	    <td colspan="4">12</td>
	    <td>J8D100</td>
	    <td>เฮดเดอร์ตัวเมีย 8 พิน</td>
	    <td>เฮดเดอร์สำหรับไฟเลี้ยงและรีเซ็ต</td>
	  </tr>  
	  <tr>
	    <td colspan="4">13</td>
	    <td>J8D101</td>
	    <td>เฮดเดอร์ตัวเมีย 8 พิน</td>
	    <td>เฮดเดอร์สำหรับ GPIO และ ADC</td>
	  </tr>  
	  <tr>
	    <td colspan="4">14</td>
	    <td>J8D103</td>
	    <td>เฮดเดอร์ตัวเมีย 8 พิน</td>
	    <td>เฮดเดอร์สำหรับ GPIO และ ADC</td>
	  </tr>    
	</table>
</div>

รูปที่ 3.2 แสดงมุมมองด้านล่างของ VCP-G  

**หมายเหตุ:** รูปที่ 3.2 ในปัจจุบันแสดงบอร์ด TOPST_VCP-G_V1.1.1 ภาพนี้จะได้รับการอัปเดตเป็นบอร์ด TOPST_VCP-G_V2.1.1
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Hardware/3.2%20TOPST%20VCP-G%20Board%20(Bottom%20View).png"></p>
<p align="center"><strong>รูปที่ 3.2 VCP-G (มุมมองด้านล่าง)</strong></p>

</br></br></br></br>

# 4. ข้อมูลจำเพาะ
---
## 4.1 หน่วยความจำแฟลช Quad SPI (U101)
---
ข้อมูลเกี่ยวกับหน่วยความจำแฟลช Quad SPI มีดังนี้:
  - ความจุ : 64 Mb  
  
**หมายเหตุ:** โดยค่าเริ่มต้น SNOR ไม่ได้ติดตั้งอยู่บน VCP-G

</br></br></br>

## 4.2 ขั้วต่อไฟเลี้ยงเข้า (J101)
---
ไฟ DC 12V จ่ายให้กับ VCP-G ผ่านแจ็ค DC ของ J101 จากอะแดปเตอร์ 12V  
รูปที่ 4.1 แสดงตำแหน่งของ J101
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Hardware/4.1%20Power%20In%20Connector%20(J101).png"></p>
<p align="center"><strong>รูปที่ 4.1 ขั้วต่อไฟเลี้ยงเข้า (J101)</strong><p>

</br></br></br>

## 4.3 ขั้วต่อสำหรับ JTAG (J100)
---
สามารถเชื่อมต่ออีมูเลเตอร์ JTAG เข้ากับ VCP-G ผ่าน J100 เพื่อการดีบักได้ รูปที่ 4.2 แสดงตำแหน่งของ J100
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Hardware/4.2%20Connector%20for%20JTAG%20(J100).png"></p>
<p align="center"><strong>รูปที่ 4.2 ขั้วต่อสำหรับ JTAG (J100)</strong><p>
JTAG ถูกปิดใช้งานโดยค่าเริ่มต้น หากต้องการเปิดใช้งาน JTAG ท่านต้องเปลี่ยนการเชื่อมต่อของ R178 และ R179 หาก TRSRn ถูกตั้งค่าเป็น high โดย R178 ตัว MCU จะเข้าสู่โหมด JTAG

ตารางที่ 4.1 อธิบายพินของ J100
<p align="center"><strong>ตารางที่ 4.1 คำอธิบายพินของ J100</strong></p>
<div align="center">
	<table>
	  <tr>
	    <th rowspan="2"><strong>หมายเลขพิน</strong></th>
	    <th rowspan="2"><strong>ชื่อเน็ตในผังวงจร</strong></th>
	    <th><strong>DIR</strong></th>
	    <th rowspan="2"><strong>คำอธิบาย</strong></th>
	  </tr>
	  <tr>
	    <th><strong>MCU ◄► J100</strong></th>
	  </tr>
	  <tr>
	    <td>1</td>
	    <td>SW_VDD_3P3</td>
	    <td>-</td>
	    <td>ไฟเลี้ยง 3.3V</td>
	  </tr>
	  <tr>
	    <td>2</td>
	    <td>TMS</td>
	    <td>◄</td>
	    <td>สถานะโหมดทดสอบ</td>
	  </tr>
	  <tr>
	    <td>3</td>
	    <td>DGND</td>
	    <td>-</td>
	    <td>กราวด์</td>
	  </tr>
	  <tr>
	    <td>4</td>
	    <td>TCK</td>
	    <td>◄</td>
	    <td>สัญญาณนาฬิกาทดสอบ</td>
	  </tr>
	  <tr>
	    <td>5</td>
		<td>DGND</td>
	    <td>-</td>
	    <td>กราวด์</td>
	  </tr>
	  <tr>
	    <td>6</td>
	    <td>TDO</td>
	    <td>►</td>
	    <td>เอาต์พุตข้อมูลทดสอบ</td>
	  </tr>
	  <tr>
	    <td>7</td>
	    <td>NC</td>
	    <td>-</td>
	    <td>ไม่ได้เชื่อมต่อ</td>
	  </tr>
	  <tr>
	    <td>8</td>
	    <td>TDI</td>
	    <td>◄</td>
	    <td>อินพุตข้อมูลทดสอบ</td>
	  </tr>
	  <tr>
	    <td>9</td>
	    <td>DGND</td>
	    <td>-</td>
	    <td>กราวด์</td>
	  </tr>
	  <tr>
	    <td>10</td>
	    <td>JTAG_RESETn</td>
	    <td>◄</td>
	    <td>การรีเซ็ตระบบ</td>
	  </tr>   
	</table>
</div>

ตารางที่ 4.2 อธิบายการตั้งค่าการปิด/เปิดใช้งาน JTAG
<p align="center"><strong>ตารางที่ 4.2 การตั้งค่าการปิด/เปิดใช้งาน JTAG</strong></p>
<div align="center">
	<table>
	  <tr>
	    <th colspan="4"><strong>โหมด</strong></th>
	    <th><strong>ค่า TRSTn</strong></th>
	    <th><strong>R178</strong></th>
	    <th><strong>R179</strong></th>
	  </tr>
	  <tr>
	    <td colspan="4">ปิดใช้งาน JTAG (ค่าเริ่มต้น)</td>
	    <td>Low (1)</td>
	    <td>N.C</td>
	    <td>1K</td>
	  </tr>
	  <tr>
	    <td colspan="4">เปิดใช้งาน JTAG (ตัวเลือก)</td>
	    <td>High (1)</td>
	    <td>1K</td>
	    <td>N.C</td>
	  </tr>
	</table>
</div>

</br></br></br>

## 4.4 สวิตช์ FWDN (SW101)
---
VCP-G มีพินหนึ่งพินสำหรับการกำหนดค่าการบูตโดยใช้ Boot Mode (BM) และรองรับ 2 โหมด ได้แก่ โหมด UART FWDN และโหมดปกติ   
รูปที่ 4.3 แสดงตำแหน่งของสวิตช์แท็กต์ FWDN (SW101) ซึ่งใช้สำหรับเลือกโหมดการบูตของ VCP-G
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Hardware/4.3%20FWDN%20Tact%20Switch%20(SW101).png"></p>
<p align="center"><strong>รูปที่ 4.3 สวิตช์แท็กต์ FWDN (SW101)</strong><p>

ตารางที่ 4.3 อธิบายวิธีใช้สวิตช์แท็กต์ FWDN (SW101) เพื่อเลือกโหมดการบูต
<p align="center"><strong>ตารางที่ 4.3 คำอธิบายสวิตช์แท็กต์ (SW101) สำหรับโหมดการบูต</strong></p>
<div align="center">
	<table>
	  <tr>
	    <th colspan="3"><strong>โหมด</strong></th>
	    <th><strong>ค่า BM00</strong></th>
	    <th><strong>สถานะ SW101</strong></th>
	  </tr>
	  <tr>
	    <td colspan="3">ปกติ (ค่าเริ่มต้น)</td>
	    <td>Low (1)</td>
	    <td>ค่าเริ่มต้น</td>
	  </tr>
	  <tr>
	    <td colspan="3">FWDN (ตัวเลือก)</td>
	    <td>High (1)</td>
	    <td>กดค้างแล้วจ่ายไฟ</td>
	  </tr>
	</table>
</div>
</br></br>

### 4.4.1 วิธีเข้าสู่โหมด FWDN
มีสองวิธีในการเข้าสู่โหมด FWDN ดังต่อไปนี้

#### 4.4.1.1 วิธีที่ 1
ขณะกดสวิตช์ FWDN (SW101) ค้างไว้ ให้เชื่อมต่อแหล่งจ่ายไฟ 12V เพื่อเปิดบอร์ด VCP-G  
ไฟแสดงสถานะสีแดงของ FWDN จะติดขึ้นเมื่อจ่ายไฟขณะที่กดสวิตช์ FWDN ค้างไว้ หลังจากปล่อยสวิตช์ FWDN (SW101) ตัว MCU จะเข้าสู่โหมด FWDN  
รูปที่ 4.4 แสดงวิธีเข้าสู่โหมด FWDN โดยใช้วิธีที่ 1
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Hardware/4.4%20Entering%20FWDN%20Mode%20by%20Using%20Method%201.png"></p>
<p align="center"><strong>รูปที่ 4.4 การเข้าสู่โหมด FWDN โดยใช้วิธีที่ 1</strong><p>

#### 4.4.1.2 วิธีที่ 2
ขณะที่บอร์ด VCP-G เชื่อมต่อกับแหล่งจ่ายไฟ 12V อยู่ ให้กดสวิตช์ FWDN (SW101) จากนั้นกดสวิตช์แท็กต์ RESET (SW100)  
ไฟแสดงสถานะสีแดงของ FWDN จะติดขึ้นเมื่อจ่ายไฟขณะที่กดสวิตช์ FWDN ค้างไว้ ไฟแสดงสถานะสีเขียว 3.3V จะดับลงขณะที่กดสวิตช์แท็กต์ RESET ค้างไว้ หลังจากปล่อยสวิตช์ FWDN (SW101) ตัว MCU จะเข้าสู่โหมด FWDN  
รูปที่ 4.5 แสดงโหมด FWDN โดยใช้วิธีที่ 2

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Hardware/4.5%20Entering%20FWDN%20Mode%20by%20Using%20Method%202.png"></p>
<p align="center"><strong>รูปที่ 4.5 การเข้าสู่โหมด FWDN โดยใช้วิธีที่ 2</strong><p>

</br></br></br>

## 4.5 สวิตช์แท็กต์ RESET (SW100)
---
VCP-G มีสวิตช์ RESET หนึ่งตัวสำหรับไฟเลี้ยงของ RESET โดยใช้พิน GRESETn  
รูปที่ 4.6 แสดงสวิตช์แท็กต์ RESET (SW100)
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Hardware/4.6%20RESET%20Tact%20Switch%20(SW100).png"></p>
<p align="center"><strong>รูปที่ 4.6 สวิตช์แท็กต์ RESET (SW100)</strong><p>
</br></br>

### 4.5.1 ฟังก์ชันของสวิตช์แท็กต์ RESET (SW100)
SW100 เป็นสวิตช์แท็กต์สำหรับรีเซ็ตบล็อกไฟเลี้ยงและบล็อกระบบใน VCP-G  
ฟังก์ชันของปุ่มนี้มีดังนี้:
  - การกดสวิตช์แท็กต์ RESET (SW100) ขณะที่เปิดไฟอยู่ จะบังคับให้บล็อกไฟเลี้ยงและระบบของ VCP-G รีเซ็ต

**สำคัญ:** โปรดใช้ความระมัดระวังเมื่อกดสวิตช์แท็กต์ เนื่องจากไฟจะดับลงอย่างกะทันหันและข้อมูลอาจเสียหายได้

</br></br></br>

## 4.6 ขั้วต่อสำหรับการดีบักและ FWDN (JC100)
---
JC100 เป็นขั้วต่อ USB Type-C มาตรฐาน บน VCP-G นั้น JC100 ใช้สำหรับการดีบักหรือ FWDN ผ่าน UART  
รูปที่ 4.7 แสดงตำแหน่งของ JC100
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Hardware/4.7%20USB%20Type-C%20Connector%20(JC100).png"></p>
<p align="center"><strong>รูปที่ 4.7 ขั้วต่อ USB Type-C (JC100)</strong><p>

ท่านสามารถดำเนินการ FWDN หรือตรวจสอบข้อความดีบักของ VCP-G ผ่าน JC100 ได้
JC100 บน VCP-G มีตัวควบคุมบริดจ์ USB-to-UART ในตัว ดังนั้นท่านจึงสามารถเชื่อมต่อ JC100 เข้ากับ PC ได้โดยตรงด้วยสาย USB Type-C

</br></br></br>

## 4.7 พินเฮดเดอร์สำหรับ GPIO, ADC, ไฟเลี้ยง, CAN และ SPI
---
VCP-G มีพินเฮดเดอร์ขนาด 2.54 mm จำนวนเก้าตัวสำหรับไฟเลี้ยง, GPIO, ADC, CAN และ SPI เพื่อเชื่อมต่อกับอุปกรณ์ต่อพ่วงอื่น เช่น เซ็นเซอร์หรือบอร์ดย่อย  

ตารางที่ 4.4 อธิบายวัตถุประสงค์ของพินเฮดเดอร์ทั้งเก้าตัวบน VCP-G
<p align="center"><strong>ตารางที่ 4.4 พินเฮดเดอร์บน VCP-G </strong></p>
<div align="center">
	<table>
	  <tr>
	    <td colspan="4"><strong>หมายเลข</strong></td>
	    <td><strong>หมายเลขอ้างอิง</strong></td>
	    <td><strong>ชื่อ</strong></td>
	    <td><strong>คำอธิบาย</strong></td>
	  </tr>
	  <tr>
	    <td colspan="4">1</td>
	    <td>J18D100</td>
	    <td>เฮดเดอร์ตัวเมีย 36 พิน</td>
	    <td>เฮดเดอร์สำหรับ GPIO และ ADC</td>
	  </tr>
	  <tr>
	    <td colspan="4">2</td>
	    <td>J5D100</td>
	    <td>เฮดเดอร์ตัวผู้ 10 พิน</td>
	    <td>เฮดเดอร์สำหรับ CAN</td>
	  </tr>
	  <tr>
	    <td colspan="4">3</td>
	    <td>J3D100</td>
	    <td>เฮดเดอร์ตัวผู้ 6 พิน</td>
	    <td>เฮดเดอร์สำหรับ SPI</td>
	  </tr>
	  <tr>
	    <td colspan="4">4</td>
	    <td>J8D104</td>
	    <td>เฮดเดอร์ตัวเมีย 8 พิน</td>
	    <td>เฮดเดอร์สำหรับ GPIO และ ADC</td>
	  </tr>
	  <tr>
	    <td colspan="4">5</td>
	    <td>J8D102</td>
	    <td>เฮดเดอร์ตัวเมีย 8 พิน</td>
	    <td>เฮดเดอร์สำหรับ GPIO</td>
	  </tr>
	  <tr>
	    <td colspan="4">6</td>
	    <td>J10D100</td>
	    <td>เฮดเดอร์ตัวเมีย 10 พิน</td>
	    <td>เฮดเดอร์สำหรับ GPIO และ ADC</td>
	  </tr>
	  <tr>
	    <td colspan="4">7</td>
	    <td>J8D100</td>
	    <td>เฮดเดอร์ตัวเมีย 8 พิน</td>
	    <td>เฮดเดอร์สำหรับไฟเลี้ยงและรีเซ็ต</td>
	  </tr>
	  <tr>
	    <td colspan="4">8</td>
	    <td>J8D101</td>
	    <td>เฮดเดอร์ตัวเมีย 8 พิน</td>
	    <td>เฮดเดอร์สำหรับ GPIO และ ADC</td>
	  </tr>
	  <tr>
	    <td colspan="4">9</td>
	    <td>J8D103</td>
	    <td>เฮดเดอร์ตัวเมีย 8 พิน</td>
	    <td>เฮดเดอร์สำหรับ GPIO และ ADC</td>
	  </tr>
	</table>
</div>

รูปที่ 4.8 แสดงตำแหน่งของพินเฮดเดอร์บน VCP-G
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Hardware/4.8%20Pin%20Headers%20on%20TOPST%20VCP-G%20Board.png"></p>
<p align="center"><strong>รูปที่ 4.8 พินเฮดเดอร์บน VCP-G </strong><p>

ตารางที่ 4.5 แสดงคำอธิบายพินของ J10D100
<p align="center"><strong>ตารางที่ 4.5 คำอธิบายพินของ J10D100</strong></p>
<div align="center">
	<table>
	  <tr>
	    <th rowspan="3"><strong>หมายเลขพิน</strong></th>
	    <th colspan="4"><strong>J10D100</strong></th>
	  </tr>
	  <tr>
	    <th rowspan="2"><strong>ชื่อพอร์ต</strong></th>
	    <th rowspan="2"><strong>ชื่อสัญญาณ</strong></th>
	    <th><strong>DIR</strong></th>
	    <th rowspan="2"><strong>คำอธิบาย</strong></th>
	  </tr>
	  <tr>
	    <th><strong>MCU ◄► J10D100</strong></th>
	  </tr>
	  <tr>
	    <td>1</td>
	    <td>SCL</td>
	    <td>GPIO_AC07</td>
	    <td>◄►</td>
	    <td>สัญญาณ GPIO หรือ ADC</td>
	  </tr>
	  <tr>
	    <td>2</td>
	    <td>SDA</td>
	    <td>GPIO_AC06</td>
	    <td>◄►</td>
	    <td>สัญญาณ GPIO หรือ ADC</td>
	  </tr>
	  <tr>
	    <td>3</td>
	    <td>AREF</td>
	    <td>ADC06</td>
	    <td>◄</td>
	    <td>สัญญาณ ADC</td>
	  </tr>
	  <tr>
	    <td>4</td>
	    <td>GND</td>
	    <td>DGND</td>
	    <td>-</td>
	    <td>กราวด์</td>
	  </tr>
	  <tr>
	    <td>5</td>
	    <td>13</td>
	    <td>GPIO_C12</td>
	    <td>◄►</td>
	    <td>สัญญาณ GPIO</td>
	  </tr>
	  <tr>
	    <td>6</td>
	    <td>12</td>
	    <td>GPIO_C15</td>
	    <td>◄►</td>
	    <td>สัญญาณ GPIO</td>
	  </tr>
	  <tr>
	    <td>7</td>
	    <td>11</td>
	    <td>GPIO_C14</td>
	    <td>◄►</td>
	    <td>สัญญาณ GPIO</td>
	  </tr>
	  <tr>
	    <td>8</td>
	    <td>10</td>
	    <td>GPIO_C13</td>
	    <td>◄►</td>
	    <td>สัญญาณ GPIO</td>
	  </tr>
	  <tr>
	    <td>9</td>
	    <td>9</td>
	    <td>GPIO_A12</td>
	    <td>◄►</td>
	    <td>สัญญาณ GPIO</td>
	  </tr>
	  <tr>
	    <td>10</td>
	    <td>8</td>
	    <td>GPIO_B00</td>
	    <td>◄►</td>
	    <td>สัญญาณ GPIO</td>
	  </tr>
	</table>
</div>

ตารางที่ 4.6 แสดงคำอธิบายพินของ J8D100
<p align="center"><strong>ตารางที่ 4.6 คำอธิบายพินของ J8D100</strong></p>
<div align="center">
	<table>
	  <tr>
	    <th rowspan="3"><strong>หมายเลขพิน</strong></th>
	    <th colspan="4"><strong>J8D100</strong></th>
	  </tr>
	  <tr>
	    <th rowspan="2"><strong>ชื่อพอร์ต</strong></th>
	    <th rowspan="2"><strong>ชื่อสัญญาณ</strong></th>
	    <th><strong>DIR</strong></th>
	    <th rowspan="2"><strong>คำอธิบาย</strong></th>
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
	    <td>ไฟเลี้ยง 3.3V</td>
	  </tr>
	  <tr>
	    <td>3</td>
	    <td>RST</td>
	    <td>RESET</td>
	    <td>◄</td>
	    <td>สัญญาณรีเซ็ต</td>
	  </tr>
	  <tr>
	    <td>4</td>
	    <td>3.3V</td>
	    <td>VCP_3P3</td>
	    <td>-</td>
	    <td>ไฟเลี้ยง 3.3V</td>
	  </tr>
	  <tr>
	    <td>5</td>
	    <td>5V</td>
	    <td>VCP_5P0</td>
	    <td>-</td>
	    <td>ไฟเลี้ยง 5.0V</td>
	  </tr>
	  <tr>
	    <td>6</td>
	    <td>GND</td>
	    <td>DGND</td>
	    <td>-</td>
	    <td>กราวด์</td>
	  </tr>
	  <tr>
	    <td>7</td>
	    <td>GND</td>
	    <td>DGND</td>
	    <td>-</td>
	    <td>กราวด์</td>
	  </tr>
	  <tr>
	    <td>8</td>
	    <td>VIN</td>
	    <td>VIN</td>
	    <td>-</td>
	    <td>อินพุตแรงดันไฟฟ้าสำหรับ VCP-G</td>
	  </tr>
	</table>
</div>

ตารางที่ 4.7 แสดงคำอธิบายพินของ J8D101
<p align="center"><strong>ตารางที่ 4.7 คำอธิบายพินของ J8D101</strong></p>
<div align="center">
	<table>
	  <tr>
	    <th rowspan="3"><strong>หมายเลขพิน</strong></th>
	    <th colspan="4"><strong>J8D101</strong></th>
	  </tr>
	  <tr>
	    <th rowspan="2"><strong>ชื่อพอร์ต</strong></th>
	    <th rowspan="2"><strong>ชื่อสัญญาณ</strong></th>
	    <th><strong>DIR</strong></th>
	    <th rowspan="2"><strong>คำอธิบาย</strong></th>
	  </tr>
	  <tr>
	    <th><strong>MCU ◄► J8D101</strong></th>
	  </tr>
	  <tr>
	    <td>1</td>
	    <td>A0</td>
	    <td>ADC03</td>
	    <td>◄</td>
	    <td>สัญญาณ ADC</td>
	  </tr>
	  <tr>
	    <td>2</td>
	    <td>A1</td>
	    <td>ADC04</td>
	    <td>◄</td>
	    <td>สัญญาณ ADC</td>
	  </tr>
	  <tr>
	    <td>3</td>
	    <td>A2</td>
	    <td>GPIO_AC02</td>
	    <td>◄►</td>
	    <td>สัญญาณ GPIO</td>
	  </tr>
	  <tr>
	    <td>4</td>
	    <td>A3</td>
	    <td>GPIO_AC03</td>
	    <td>◄►</td>
	    <td>สัญญาณ GPIO</td>
	  </tr>
	  <tr>
	    <td>5</td>
	    <td>A4</td>
	    <td>GPIO_AC05</td>
	    <td>◄►</td>
	    <td>สัญญาณ GPIO</td>
	  </tr>
	  <tr>
	    <td>6</td>
	    <td>A5</td>
	    <td>GPIO_AC04</td>
	    <td>◄►</td>
	    <td>สัญญาณ GPIO</td>
	  </tr>
	  <tr>
	    <td>7</td>
	    <td>A6</td>
	    <td>ADC05</td>
	    <td>◄</td>
	    <td>สัญญาณ ADC</td>
	  </tr>
	  <tr>
	    <td>8</td>
	    <td>A7</td>
	    <td>ADC01</td>
	    <td>◄</td>
	    <td>สัญญาณ ADC</td>
	  </tr>
	</table>
</div>

ตารางที่ 4.8 แสดงคำอธิบายพินของ J8D102
<p align="center"><strong>ตารางที่ 4.8 คำอธิบายพินของ J8D102</strong></p>
<div align="center">
	<table>
	  <tr>
	    <th rowspan="3"><strong>หมายเลขพิน</strong></th>
	    <th colspan="4"><strong>J8D102</strong></th>
	  </tr>
	  <tr>
	    <th rowspan="2"><strong>ชื่อพอร์ต</strong></th>
	    <th rowspan="2"><strong>ชื่อสัญญาณ</strong></th>
	    <th><strong>DIR</strong></th>
	    <th rowspan="2"><strong>คำอธิบาย</strong></th>
	  </tr>
	  <tr>
	    <th><strong>MCU ◄► J8D102</strong></th>
	  </tr>
	  <tr>
	    <td>1</td>
	    <td>7</td>
	    <td>GPIO_B01</td>
	    <td>◄►</td>
	    <td>สัญญาณ GPIO</td>
	  </tr>
	  <tr>
	    <td>2</td>
	    <td>6</td>
	    <td>GPIO_A13</td>
	    <td>◄►</td>
	    <td>สัญญาณ GPIO</td>
	  </tr>
	  <tr>
	    <td>3</td>
	    <td>5</td>
	    <td>GPIO_B10</td>
	    <td>◄►</td>
	    <td>สัญญาณ GPIO</td>
	  </tr>
	  <tr>
	    <td>4</td>
	    <td>4</td>
	    <td>GPIO_B27</td>
	    <td>◄►</td>
	    <td>สัญญาณ GPIO</td>
	  </tr>
	  <tr>
	    <td>5</td>
	    <td>3</td>
	    <td>GPIO_B11</td>
	    <td>◄►</td>
	    <td>สัญญาณ GPIO</td>
	  </tr>
	  <tr>
	    <td>6</td>
	    <td>2</td>
	    <td>GPIO_B28</td>
	    <td>◄►</td>
	    <td>สัญญาณ GPIO</td>
	  </tr>
	  <tr>
	    <td>7</td>
	    <td>1</td>
	    <td>GPIO_B25</td>
	    <td>◄►</td>
	    <td>สัญญาณ GPIO</td>
	  </tr>
	  <tr>
	    <td>8</td>
	    <td>0</td>
	    <td>GPIO_B26</td>
	    <td>◄►</td>
	    <td>สัญญาณ GPIO</td>
	  </tr>
	</table>
</div>

ตารางที่ 4.9 แสดงคำอธิบายพินของ J8D103
<p align="center"><strong>ตารางที่ 4.9 คำอธิบายพินของ J8D103</strong></p>
<div align="center">
	<table>
	  <tr>
	    <th rowspan="3"><strong>หมายเลขพิน</strong></th>
	    <th colspan="4"><strong>J8D103</strong></th>
	  </tr>
	  <tr>
	    <th rowspan="2"><strong>ชื่อพอร์ต</strong></th>
	    <th rowspan="2"><strong>ชื่อสัญญาณ</strong></th>
	    <th><strong>DIR</strong></th>
	    <th rowspan="2"><strong>คำอธิบาย</strong></th>
	  </tr>
	  <tr>
	    <th><strong>MCU ◄► J8D103</strong></th>
	  </tr>
	  <tr>
	    <td>1</td>
	    <td>A8</td>
	    <td>GPIO_AC08</td>
	    <td>◄►</td>
	    <td>สัญญาณ GPIO หรือ ADC</td>
	  </tr>
	  <tr>
	    <td>2</td>
	    <td>A9</td>
	    <td>GPIO_AC09</td>
	    <td>◄►</td>
	    <td>สัญญาณ GPIO หรือ ADC</td>
	  </tr>
	  <tr>
	    <td>3</td>
	    <td>A10</td>
	    <td>GPIO_AC10</td>
	    <td>◄►</td>
	    <td>สัญญาณ GPIO หรือ ADC</td>
	  </tr>
	  <tr>
	    <td>4</td>
	    <td>A11</td>
	    <td>GPIO_ADC-2</td>
	    <td>◄</td>
	    <td>สัญญาณ ADC</td>
	  </tr>
	  <tr>
	    <td>5</td>
	    <td>54</td>
	    <td>GPIO_K14</td>
	    <td>◄►</td>
	    <td>สัญญาณ GPIO</td>
	  </tr>
	  <tr>
	    <td>6</td>
	    <td>55</td>
	    <td>GPIO_K15</td>
	    <td>◄►</td>
	    <td>สัญญาณ GPIO</td>
	  </tr>
	  <tr>
	    <td>7</td>
	    <td>56</td>
	    <td>GPIO_K01</td>
	    <td>◄</td>
	    <td>สัญญาณ GPIO</td>
	  </tr>
	  <tr>
	    <td>8</td>
	    <td>57</td>
	    <td>GPIO_K08</td>
	    <td>◄►</td>
	    <td>สัญญาณ GPIO</td>
	  </tr>
	</table>
</div>

ตารางที่ 4.10 แสดงคำอธิบายพินของ J8D104
<p align="center"><strong>ตารางที่ 4.10 คำอธิบายพินของ J8D104</strong></p>
<div align="center">
	<table>
	  <tr>
	    <th rowspan="3"><strong>หมายเลขพิน</strong></th>
	    <th colspan="4"><strong>J8D104</strong></th>
	  </tr>
	  <tr>
	    <th rowspan="2"><strong>ชื่อพอร์ต</strong></th>
	    <th rowspan="2"><strong>ชื่อสัญญาณ</strong></th>
	    <th><strong>DIR</strong></th>
	    <th rowspan="2"><strong>คำอธิบาย</strong></th>
	  </tr>
	  <tr>
	    <th><strong>MCU ◄► J8D104</strong></th>
	  </tr>
	  <tr>
	    <td>1</td>
	    <td>14</td>
	    <td>GPIO_AC00</td>
	    <td>◄►</td>
	    <td>สัญญาณ GPIO หรือ ADC</td>
	  </tr>
	  <tr>
	    <td>2</td>
	    <td>15</td>
	    <td>GPIO_AC01</td>
	    <td>◄►</td>
	    <td>สัญญาณ GPIO หรือ ADC</td>
	  </tr>
	  <tr>
	    <td>3</td>
	    <td>16</td>
	    <td>GPIO_A06</td>
	    <td>◄►</td>
	    <td>สัญญาณ GPIO</td>
	  </tr>
	  <tr>
	    <td>4</td>
	    <td>17</td>
	    <td>GPIO_A07</td>
		<td>◄►</td>
	    <td>สัญญาณ GPIO</td>
	  </tr>
	  <tr>
	    <td>5</td>
	    <td>18</td>
	    <td>GPIO_A28</td>
	    <td>◄►</td>
	    <td>สัญญาณ GPIO</td>
	  </tr>
	  <tr>
	    <td>6</td>
	    <td>19</td>
	    <td>GPIO_A29</td>
	    <td>◄►</td>
	    <td>สัญญาณ GPIO</td>
	  </tr>
	  <tr>
	    <td>7</td>
	    <td>20</td>
	    <td>GPIO_B03</td>
	    <td>◄►</td>
	    <td>สัญญาณ GPIO</td>
	  </tr>
	  <tr>
	    <td>8</td>
	    <td>21</td>
	    <td>GPIO_B02</td>
	    <td>◄►</td>
	    <td>สัญญาณ GPIO</td>
	  </tr>
	</table>
</div>

ตารางที่ 4.11 แสดงคำอธิบายพินของ J3D100
<p align="center"><strong>ตารางที่ 4.11 คำอธิบายพินของ J3D100</strong></p>
<div align="center">
	<table>
	  <tr>
	    <th rowspan="3"><strong>หมายเลขพิน</strong></th>
	    <th colspan="4"><strong>J3D100</strong></th>
	  </tr>
	  <tr>
	    <th rowspan="2"><strong>ชื่อพอร์ต</strong></th>
	    <th rowspan="2"><strong>ชื่อสัญญาณ</strong></th>
	    <th><strong>DIR</strong></th>
	    <th rowspan="2"><strong>คำอธิบาย</strong></th>
	  </tr>
	  <tr>
	    <th><strong>MCU ◄► J3D100</strong></th>
	  </tr>
	  <tr>
	    <td>1</td>
	    <td>MISO</td>
	    <td>GPIO_B07</td>
	    <td>◄►</td>
	    <td>สัญญาณ GPIO</td>
	  </tr>
	  <tr>
	    <td>2</td>
	    <td>5V</td>
	    <td>VCP_5P0</td>
	    <td>-</td>
	    <td>ไฟเลี้ยง 5.0V</td>
	  </tr>
	  <tr>
	    <td>3</td>
	    <td>SCK</td>
	    <td>GPIO_B04</td>
	    <td>◄►</td>
	    <td>สัญญาณ GPIO</td>
	  </tr>
	  <tr>
	    <td>4</td>
	    <td>MOSI</td>
	    <td>GPIO_B06</td>
	    <td>◄►</td>
	    <td>สัญญาณ GPIO</td>
	  </tr>
	  <tr>
	    <td>5</td>
	    <td>CMD</td>
	    <td>GPIO_B05</td>
	    <td>◄►</td>
	    <td>สัญญาณ GPIO</td>
	  </tr>
	  <tr>
	    <td>6</td>
	    <td>GND</td>
	    <td>DGND</td>
	    <td>-</td>
	    <td>กราวด์</td>
	  </tr>
	</table>
</div>

ตารางที่ 4.12 แสดงคำอธิบายพินของ J18D100
<p align="center"><strong>ตารางที่ 4.12 คำอธิบายพินของ J18D100</strong></p>
<div align="center">
	<table>
	  <tr>
	    <th rowspan="3"><strong>หมายเลขพิน</strong></th>
	    <th colspan="4"><strong>J18D100</strong></th>
	  </tr>
	  <tr>
	    <th rowspan="2"><strong>ชื่อพอร์ต</strong></th>
	    <th rowspan="2"><strong>ชื่อสัญญาณ</strong></th>
	    <th><strong>DIR</strong></th>
	    <th rowspan="2"><strong>คำอธิบาย</strong></th>
	  </tr>
	  <tr>
	    <th><strong>MCU ◄► J18D100</strong></th>
	  </tr>
	  <tr>
	    <td>1</td>
	    <td>5V</td>
	    <td>VCP_5P0</td>
	    <td>-</td>
	    <td>ไฟเลี้ยง 5.0V</td>
	  </tr>
	  <tr>
	    <td>2</td>
	   <td>5V</td>
	    <td>VCP_5P0</td>
	    <td>-</td>
	    <td>ไฟเลี้ยง 5.0V</td>
	  </tr>
	  <tr>
	    <td>3</td>
	    <td>22</td>
	    <td>GPIO_B24</td>
	    <td>◄►</td>
	    <td>สัญญาณ GPIO</td>
	  </tr>
	  <tr>
	    <td>4</td>
	    <td>23</td>
	    <td>GPIO_B23</td>
	    <td>◄►</td>
	    <td>สัญญาณ GPIO</td>
	  </tr>
	  <tr>
	    <td>5</td>
	    <td>24</td>
	    <td>GPIO_B22</td>
	    <td>◄►</td>
	    <td>สัญญาณ GPIO</td>
	  </tr>
	  <tr>
	    <td>6</td>
	    <td>25</td>
	    <td>GPIO_B21</td>
	    <td>◄►</td>
	    <td>สัญญาณ GPIO</td>
	  </tr>
	  <tr>
	    <td>7</td>
	    <td>26</td>
	    <td>GPIO_B20</td>
	    <td>◄►</td>
	    <td>สัญญาณ GPIO</td>
	  </tr>
	  <tr>
	    <td>8</td>
	    <td>27</td>
	    <td>GPIO_B19</td>
	    <td>◄►</td>
	    <td>สัญญาณ GPIO</td>
	  </tr>
	  <tr>
	    <td>9</td>
	    <td>28</td>
	    <td>GPIO_A30</td>
	    <td>◄►</td>
	    <td>สัญญาณ GPIO</td>
	  </tr>
	  <tr>
	    <td>10</td>
	    <td>29</td>
	    <td>GPIO_A27</td>
	    <td>◄►</td>
	    <td>สัญญาณ GPIO</td>
	  </tr>
	  <tr>
	    <td>11</td>
	    <td>230</td>
	    <td>GPIO_A26</td>
	    <td>◄►</td>
	    <td>สัญญาณ GPIO</td>
	  </tr>
	  <tr>
	    <td>12</td>
	    <td>31</td>
	    <td>GPIO_A24</td>
	    <td>◄►</td>
	    <td>สัญญาณ GPIO</td>
	  </tr>
	  <tr>
	    <td>13</td>
	    <td>32</td>
	    <td>GPIO_A25</td>
	    <td>◄►</td>
	    <td>สัญญาณ GPIO</td>
	  </tr>
	  <tr>
	    <td>14</td>
	    <td>33</td>
	    <td>GPIO_A23</td>
	    <td>◄►</td>
	    <td>สัญญาณ GPIO</td>
	  </tr>
	  <tr>
	    <td>15</td>
	    <td>34</td>
	    <td>GPIO_A22</td>
	    <td>◄►</td>
	    <td>สัญญาณ GPIO</td>
	  </tr>
	  <tr>
	    <td>16</td>
	    <td>35</td>
	    <td>GPIO_A21</td>
	    <td>◄►</td>
		<td>สัญญาณ GPIO</td>
	  </tr>
	  <tr>
	    <td>17</td>
	    <td>36</td>
	    <td>GPIO_A20</td>
	    <td>◄►</td>
	    <td>สัญญาณ GPIO</td>
	  </tr>
	  <tr>
	    <td>18</td>
	    <td>37</td>
	    <td>GPIO_A19</td>
	    <td>◄►</td>
	    <td>สัญญาณ GPIO</td>
	  </tr>
	  <tr>
	    <td>19</td>
	    <td>38</td>
	    <td>GPIO_K13</td>
	    <td>◄►</td>
		<td>สัญญาณ GPIO</td>
	  </tr>
	  <tr>
	    <td>20</td>
	    <td>39</td>
	    <td>GPIO_K12</td>
	    <td>◄►</td>
	    <td>สัญญาณ GPIO</td>
	  </tr>
	  <tr>
	    <td>21</td>
	    <td>40</td>
	    <td>GPIO_K11</td>
	    <td>◄►</td>
	    <td>สัญญาณ GPIO</td>
	  </tr>
	  <tr>
	    <td>22</td>
	    <td>41</td>
	    <td>GPIO_A18</td>
	    <td>◄►</td>
	    <td>สัญญาณ GPIO</td>
	  </tr>
	  <tr>
	    <td>23</td>
	    <td>42</td>
	    <td>GPIO_A17</td>
	    <td>◄►</td>
	    <td>สัญญาณ GPIO</td>
	  </tr>
	  <tr>
	    <td>24</td>
	    <td>43</td>
	    <td>GPIO_A16</td>
	    <td>◄►</td>
	    <td>สัญญาณ GPIO</td>
	  </tr>
	  <tr>
	    <td>25</td>
	    <td>44</td>
	    <td>GPIO_A11</td>
	    <td>◄►</td>
	    <td>สัญญาณ GPIO</td>
	  </tr>
	  <tr>
	    <td>26</td>
	    <td>45</td>
	    <td>GPIO_A10</td>
	    <td>◄►</td>
	    <td>สัญญาณ GPIO</td>
	  </tr>
	  <tr>
	    <td>27</td>
	    <td>46</td>
	    <td>GPIO_A09</td>
	    <td>◄►</td>
	    <td>สัญญาณ GPIO</td>
	  </tr>
	  <tr>
	    <td>28</td>
	    <td>47</td>
	    <td>GPIO_A08</td>
	    <td>◄►</td>
	    <td>สัญญาณ GPIO</td>
	  </tr>
	  <tr>
	    <td>29</td>
	    <td>48</td>
	    <td>GPIO_A05</td>
	    <td>◄►</td>
	    <td>สัญญาณ GPIO</td>
	  </tr>
	  <tr>
	    <td>30</td>
	    <td>49</td>
	    <td>GPIO_A04</td>
	    <td>◄►</td>
	    <td>สัญญาณ GPIO</td>
	  </tr>
	  <tr>
	    <td>31</td>
	    <td>50</td>
	    <td>GPIO_A03</td>
	    <td>◄►</td>
	    <td>สัญญาณ GPIO</td>
	  </tr>
	  <tr>
	    <td>32</td>
	    <td>51</td>
	    <td>GPIO_A02</td>
	    <td>◄►</td>
	    <td>สัญญาณ GPIO</td>
	  </tr>
	  <tr>
	    <td>33</td>
	    <td>52</td>
	    <td>GPIO_A01</td>
	    <td>◄►</td>
	    <td>สัญญาณ GPIO</td>
	  </tr>
	  <tr>
	    <td>34</td>
	    <td>53</td>
	    <td>GPIO_A00</td>
	    <td>◄►</td>
	    <td>สัญญาณ GPIO</td>
	  </tr>
	  <tr>
	    <td>35</td>
	    <td>GND</td>
	    <td>DGND</td>
	    <td>-</td>
	    <td>กราวด์</td>
	  </tr>
	  <tr>
	    <td>36</td>
	    <td>GND</td>
	    <td>DGND</td>
	    <td>-</td>
	    <td>กราวด์</td>
	  </tr>
	</table>
</div>

ตารางที่ 4.13 แสดงคำอธิบายพินของ J5D100
<p align="center"><strong>ตารางที่ 4.13 คำอธิบายพินของ J5D100</strong></p>
<div align="center">
	<table>
	  <tr>
	    <th rowspan="3"><strong>หมายเลขพิน</strong></th>
	    <th colspan="4"><strong>J5D100</strong></th>
	  </tr>
	  <tr>
	    <th rowspan="2"><strong>ชื่อพอร์ต</strong></th>
	    <th rowspan="2"><strong>ชื่อสัญญาณ</strong></th>
	    <th><strong>DIR</strong></th>
	    <th rowspan="2"><strong>คำอธิบาย</strong></th>
	  </tr>
	  <tr>
	    <th><strong>MCU ◄► J5D100</strong></th>
	  </tr>
	  <tr>
	    <td>1</td>
	    <td>3.3V</td>
	    <td>VCP_3P3</td>
	    <td>-</td>
	    <td>ไฟเลี้ยง 3.3V</td>
	  </tr>
	  <tr>
	    <td>2</td>
	    <td>3.3V</td>
	    <td>VCP_3P3</td>
	    <td>-</td>
    <td>ไฟเลี้ยง 3.3V</td>
	  </tr>
	  <tr>
	    <td>3</td>
	    <td>TX0</td>
	    <td>GPIO_K08</td>
	    <td>◄►</td>
	    <td>สัญญาณ GPIO</td>
	  </tr>
	  <tr>
	    <td>4</td>
	    <td>RX0</td>
	    <td>GPIO_K01</td>
	    <td>◄</td>
	    <td>สัญญาณ GPIO</td>
	  </tr>
	  <tr>
	    <td>5</td>
	    <td>TX1</td>
	    <td>GPIO_K09</td>
	    <td>◄►</td>
	    <td>สัญญาณ GPIO</td>
	  </tr>
	  <tr>
	    <td>6</td>
	    <td>RX1</td>
	    <td>GPIO_K02</td>
	    <td>◄</td>
	    <td>สัญญาณ GPIO</td>
	  </tr>
	  <tr>
	    <td>7</td>
	    <td>TX2</td>
	    <td>GPIO_K10</td>
	    <td>◄►</td>
	    <td>สัญญาณ GPIO</td>
	  </tr>
	  <tr>
	    <td>8</td>
	    <td>RX2</td>
	    <td>GPIO_K03</td>
	    <td>◄</td>
	    <td>สัญญาณ GPIO</td>
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

รูปที่ 4.9 แสดงการกำหนดพินทั้งหมดของพินเฮดเดอร์สิบชุดบน VCP-G
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Hardware/4.9%20Total%20Pin%20Assignment%20of%20Pin%20Headers%20on%20TOPST%20VCP-G%20Board.png"></p>
<p align="center"><strong>รูปที่ 4.9 การกำหนดพินทั้งหมดของพินเฮดเดอร์บน VCP-G </strong><p>

# เอกสารอ้างอิง
  - ติดต่อ TOPST เพื่อขอรายละเอียดเพิ่มเติม: topst@topst.ai

**หมายเหตุ:** เอกสารอ้างอิงสามารถจัดหาให้ได้เมื่อมีพร้อม ทั้งนี้ขึ้นอยู่กับเงื่อนไขของสัญญา หากไม่มีเอกสารอ้างอิง จะมีการแนะนำเนื้อหาที่เกี่ยวข้องโดยตรงกับการพัฒนาของท่าน
