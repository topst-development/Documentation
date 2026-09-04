# 1. บทนำ 
---
เอกสารนี้ให้ตัวอย่างการใช้งาน D3-G   
เอกสารนี้ประกอบด้วยข้อมูลต่อไปนี้:
- อุปกรณ์อินพุต
  - คีย์บอร์ด 
  - เมาส์
- การแสดงผลวิดีโอ
- การเชื่อมต่อกล้อง
  - MIPI CSI
  - เว็บแคม USB
- การเชื่อมต่ออุปกรณ์จัดเก็บข้อมูล
  - การ์ด SD
  - SATA HDD
  - NVMe M.2 SSD
  - อุปกรณ์จัดเก็บข้อมูล USB
- การเชื่อมต่ออีเทอร์เน็ต
- เฮดเดอร์ GPIO 40 พิน
  - เซ็นเซอร์และอุปกรณ์ที่ใช้งานได้

<br/><br/><br/><br/>


# 2. อุปกรณ์อินพุต
---
D3-G รองรับพอร์ต USB สองพอร์ตสำหรับเชื่อมต่ออุปกรณ์อินพุต
ประกอบด้วยพอร์ต USB 2.0 Type-A หนึ่งพอร์ตและพอร์ต USB 3.0 Type-A หนึ่งพอร์ต ทำให้สามารถเชื่อมต่อเมาส์หรือคีย์บอร์ดเพื่อควบคุม D3-G ได้โดยตรง 

**หมายเหตุ**: พอร์ต USB Type-C บน D3-G สงวนไว้สำหรับการดาวน์โหลดเฟิร์มแวร์ และไม่สามารถใช้เชื่อมต่ออุปกรณ์อินพุตได้

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20D3-G/Software/input%20device.png" width="500"></p>
<p align="center"><strong>รูปที่ 2.1 การเชื่อมต่ออุปกรณ์อินพุตกับบอร์ด D3-G </strong></p><br/><br/><br/><br/>


# 3. เอาต์พุตวิดีโอ
---
D3-G รองรับจอมอนิเตอร์ FHD ผ่านเอาต์พุต DisplayPort (DP) เท่านั้น
นอกจากนี้ยังรองรับเอาต์พุตแบบหลายจอภาพด้วยการต่อแบบเดซี่เชน ซึ่งสามารถเชื่อมต่อจอมอนิเตอร์ FHD ได้สูงสุดสองเครื่องและจอมอนิเตอร์ HD หนึ่งเครื่องพร้อมกัน

**หมายเหตุ**: หากต้องการใช้ HDMI จำเป็นต้องมีอะแดปเตอร์แปลงสัญญาณแบบแอ็กทีฟแยกต่างหาก
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20D3-G/Software/monitor.png" width="500"></p>
<p align="center"><strong>รูปที่ 3.1 การเชื่อมต่อจอมอนิเตอร์กับบอร์ด D3-G </strong></p>

<br/><br/><br/><br/>

# 4. การเชื่อมต่อกล้อง
---
D3-G รองรับการทำงานของกล้อง ซึ่งให้ความยืดหยุ่นสำหรับการใช้งานที่หลากหลาย
คุณสามารถเชื่อมต่อกล้อง MIPI CSI หรือเว็บแคม USB ได้ตามความต้องการของโครงการ

<br/><br/><br/>

## 4.1 เว็บแคม USB
---
D3-G รองรับเว็บแคม USB ที่ความละเอียดสูงสุด Full HD (FHD)
คุณสามารถทดสอบเว็บแคมได้ตามขั้นตอนต่อไปนี้:


#### ขั้นตอนที่ 1. เชื่อมต่อกล้อง USB เข้ากับพอร์ต USB บนบอร์ด
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20D3-G/Software/webcam.png" width="400"></p>
<p align="center"><strong>รูปที่ 4.1 การเชื่อมต่อเว็บแคมกับบอร์ด D3-G</strong></p><br/>

#### ขั้นตอนที่ 2. เชื่อมต่ออุปกรณ์อินพุต (เมาส์และคีย์บอร์ด) และจอมอนิเตอร์เข้ากับ D3-G
   
#### ขั้นตอนที่ 3. ทำการบูต D3-G

#### ขั้นตอนที่ 4. ตรวจสอบอุปกรณ์ /dev/video ที่ใช้งานได้
```
$ ls /dev/video*
```

#### ขั้นตอนที่ 5. ตรวจสอบเอาต์พุตวิดีโอโดยใช้ OpenCV (หรือ vutils)
```
$ touch webcam.py
$ chmod a+x webcam.py
```
```
# You can edit the script file using vim or nano editor
# This is a Python camera application using OpenCV
import cv2

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("\\@@ Camera open failed!")
    exit()

print("Press 'q' to exit the camera window.")

cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

while True:
    ret, frame = cap.read()
    if not ret:
        print("\\@@ Failed to read frame")
        break

    cv2.imshow("Camera Feed", frame)

    # pressed 'q' key, escape
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
```
```
# Run the script
$ python3 webcam.py
```

<br/><br/><br/>

## 4.2 MIPI CSI
---
CSI ย่อมาจาก Camera Serial Interface ซึ่งเป็นอินเทอร์เฟซมาตรฐานที่กำหนดโดย MIPI Alliance สำหรับเชื่อมต่อโมดูลกล้องเข้ากับโปรเซสเซอร์โฮสต์
อินเทอร์เฟซนี้ช่วยให้ส่งข้อมูลภาพจากกล้องไปยังโปรเซสเซอร์ได้ด้วยความเร็วสูงและใช้พลังงานต่ำ

D3-G มีช่อง MIPI CSI สองช่อง (ch0 และ ch1) ทำให้สามารถต่อโมดูลกล้องที่รองรับการเชื่อมต่อแบบ Flat Flexible Cable (FFC) ได้
ปัจจุบัน D3-G รองรับเฉพาะโมดูล ArduCam (5 MP) และ Raspberry Pi v1 Camera (5 MP) เท่านั้น 

**หมายเหตุ**: ปัจจุบัน D3-G ไม่รองรับการใช้งาน CSI ช่อง 0 และ CSI ช่อง 1 พร้อมกัน

<br/><br/>

### 4.2.1 ArduCam
ArduCam เป็นโมดูลกล้องอเนกประสงค์ที่ออกแบบมาสำหรับระบบฝังตัวและแอปพลิเคชัน IoT รองรับเซ็นเซอร์ภาพและอินเทอร์เฟซหลากหลายรูปแบบ รวมถึง MIPI CSI จึงเหมาะสำหรับการใช้งานร่วมกับบอร์ดพัฒนาอย่าง D3-G
โมดูล ArduCam ขนาด 5 MP ที่ D3-G รองรับให้คุณภาพของภาพที่ดี และนิยมใช้กับงานคอมพิวเตอร์วิทัศน์พื้นฐาน การสตรีม และแอปพลิเคชัน AI ที่ใช้กล้อง ด้วยความเข้ากันได้กับสาย FFC จึงเชื่อมต่อกับอินเทอร์เฟซ CSI ของบอร์ด D3-G ได้ง่าย 

ข้อมูลจำเพาะของโมดูล ArduCam มีดังนี้

| ข้อมูลจำเพาะ                     | รายละเอียด                                 |
| ------------------------ | ------------------------------------------- |
| เซ็นเซอร์                   | OV5647 (5 ล้านพิกเซล)                        |
| ความละเอียด               | 2592 × 1944 (Full 5 MP)                      |
| รูปแบบเอาต์พุตที่รองรับ | RAW, YUV, JPEG (ขึ้นอยู่กับเซ็นเซอร์)           |
| อินเทอร์เฟซ                | MIPI CSI-2                                  |
| อัตราเฟรม               | สูงสุด 30fps ที่ 1080p และ 60fps ที่ 720p         |
| เมาท์เลนส์               | เลนส์โฟกัสคงที่ (มาตรฐาน)                 |
| มุมมองภาพ (FOV)           | ประมาณ 54° – 70° (แตกต่างกันตามรุ่น)             |
| ประเภทการเชื่อมต่อ          | Flat Flexible Cable (FFC)                   |
| แรงดันไฟฟ้าใช้งาน        | 3.3V (ค่าทั่วไป)                              |
| ขนาดรูปทรง              | PCB ขนาดกะทัดรัด ประมาณ 25 mm x 24 mm                   |
| ความเข้ากันได้             | Raspberry Pi และ D3-G (ผ่านพอร์ต MIPI CSI-2)      |
| คุณสมบัติเพิ่มเติม      | ใช้พลังงานต่ำ เป็นโมดูลแบบ plug-and-play |


คุณสามารถทดสอบ ArduCam ได้ตามขั้นตอนต่อไปนี้:
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20D3-G/Software/arducam.png" width="400"></p>
<p align="center"><strong>รูปที่ 4.2 ArduCam </strong></p><br/>

#### ขั้นตอนที่ 1. เชื่อมต่อ ArduCam เข้ากับ MIPI CSI 0 ของบอร์ด D3-G ตามที่แสดงในรูปที่ 4.3
 
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20D3-G/Software/rasp%20v1%20cam%20to%20d3g.png" width="500"></p>
<p align="center"><strong>รูปที่ 4.3 การเชื่อมต่อ ArduCam กับบอร์ด D3-G</strong></p> <br/>

#### ขั้นตอนที่ 2. หลังจากเชื่อมต่อ ArduCam แล้ว คุณสามารถตรวจสอบสตรีมวิดีโอด้วยคำสั่ง GStreamer ต่อไปนี้บนบอร์ด D3-G:
```
$ gst-launch-1.0 v4l2src device=/dev/video0 io-mode=2 ! video/x-raw,format=NV12,width=1920,height=1280,framerate=30/1 ! videoconvert ! waylandsink fullscreen=true
```

คำสั่งนี้จะจับภาพวิดีโอจาก ArduCam ที่เชื่อมต่อผ่าน CSI แปลงให้เหมาะสำหรับการแสดงผล และแสดงผลในโหมดเต็มหน้าจอโดยใช้เซิร์ฟเวอร์แสดงผล Wayland  
โปรดตรวจสอบว่าโมดูลกล้องเชื่อมต่อแน่นหนาก่อนรันคำสั่ง หากไม่มีวิดีโอปรากฏ ให้ตรวจสอบการเชื่อมต่อสายและยืนยันว่าระบบรู้จัก /dev/video0 อย่างถูกต้อง

<br/><br/>

### 4.2.2 Raspberry Pi v1 Camera
Raspberry Pi v1 Camera Module เป็นกล้องขนาดกะทัดรัด 5 MP ที่พัฒนาโดย Raspberry Pi Foundation โดยใช้เซ็นเซอร์ภาพ OmniVision OV5647 และเชื่อมต่อกับบอร์ดโฮสต์ผ่านอินเทอร์เฟซ MIPI CSI-2 ด้วยสาย Flat Flexible Cable (FFC)

แม้ว่าเดิมทีโมดูลนี้ออกแบบมาสำหรับซีรีส์ Raspberry Pi แต่ก็ใช้งานร่วมกับ D3-G ได้ จึงเป็นตัวเลือกที่เชื่อถือได้สำหรับแอปพลิเคชันกล้องพื้นฐาน เช่น การถ่ายภาพ การบันทึกวิดีโอ และโครงการคอมพิวเตอร์วิทัศน์

ข้อมูลจำเพาะของโมดูล Raspberry Pi v1 Camera มีดังนี้

| ข้อมูลจำเพาะ                | รายละเอียด                              |
| ------------------- | ---------------------------------------- |
| เซ็นเซอร์              | OmniVision OV5647                        |
| ความละเอียด          | 2592 × 1944 (5 MP)                        |
| รูปแบบเอาต์พุต      | RAW, YUV, JPEG                           |
| อินเทอร์เฟซ           | MIPI CSI-2                               |
| อัตราเฟรม          | 1080p30, 720p60, VGA90                   |
| เลนส์                | โฟกัสคงที่                              |
| มุมมองภาพ (FOV) | สูงสุด 54°                                     |
| ชนิดสายเคเบิล          | FFC (15 พิน)                             |
| ขนาดบอร์ด    | 25 mm x 24 mm                              |
| ความเข้ากันได้        | Raspberry Pi และ D3-G (ผ่านพอร์ต MIPI CSI-2) |

คุณสามารถทดสอบกล้อง Raspberry Pi v1 ได้ตามขั้นตอนต่อไปนี้:

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20D3-G/Software/rasp%20v1%20cam.jpg" width="400"></p>
<p align="center"><strong>รูปที่ 4.4. Raspberry Pi v1 Camera </strong></p><br/>

#### ขั้นตอนที่ 1. เชื่อมต่อกล้อง Raspberry Pi v1 เข้ากับ MIPI CSI 1 ของบอร์ด D3-G ตามที่แสดงในรูปที่ 4.5
 
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20D3-G/Software/rasp%20v1%20cam%20to%20d3g.png" width="500"></p>
<p align="center"><strong>รูปที่ 4.5 การเชื่อมต่อ Raspberry Pi v1 Camera กับบอร์ด D3-G</strong></p> <br/>

#### ขั้นตอนที่ 2. หลังจากเชื่อมต่อกล้อง Raspberry Pi แล้ว คุณสามารถตรวจสอบสตรีมวิดีโอได้โดยใช้คำสั่ง GStreamer ต่อไปนี้บน D3-G:
```
$ gst-launch-1.0 v4l2src device=/dev/video0 io-mode=2 ! video/x-raw,format=NV12,width=1920,height=1280,framerate=30/1 ! videoconvert ! waylandsink fullscreen=true
```

คำสั่งนี้จะจับภาพวิดีโอจากกล้อง Raspberry Pi ที่เชื่อมต่อผ่าน CSI แปลงให้เหมาะสำหรับการแสดงผล และเรนเดอร์ในโหมดเต็มหน้าจอโดยใช้เซิร์ฟเวอร์แสดงผล Wayland  
โปรดตรวจสอบว่าโมดูลกล้องเชื่อมต่อแน่นหนาก่อนรันคำสั่ง หากไม่มีวิดีโอปรากฏ ให้ตรวจสอบการเชื่อมต่อสายและยืนยันว่าระบบรู้จัก /dev/video0 อย่างถูกต้อง

<br/><br/><br/><br/>

# 5. การเชื่อมต่อสตอเรจ
---
บทนี้อธิบายวิธีเชื่อมต่อ D3-G เข้ากับอุปกรณ์สตอเรจต่าง ๆ ตัวเลือกสตอเรจที่รองรับ ได้แก่ USB ไดรฟ์ การ์ด SD และสตอเรจภายนอกผ่าน PCIe

<br/><br/><br/>

## 5.1 USB ไดรฟ์
---
D3-G รองรับอุปกรณ์สตอเรจ USB ผ่านพอร์ต USB 2.0 และ USB 3.0 Type-A
วิธีเชื่อมต่อ USB ไดรฟ์:

### ขั้นตอนที่ 1. เสียบ USB ไดรฟ์เข้ากับพอร์ต USB Type-A ที่ว่างอยู่พอร์ตใดพอร์ตหนึ่งบน D3-G
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20D3-G/Software/usb%20storage%20connection%20with%20d3g.png" width="500"></p>
<p align="center"><strong>รูปที่ 5.1 การเชื่อมต่อสตอเรจ USB เข้ากับบอร์ด D3-G</strong></p> <br/>

### ขั้นตอนที่ 2. หลังจากเชื่อมต่อแล้ว โดยทั่วไประบบจะรู้จักอุปกรณ์เป็น /dev/sda1, /dev/sdb1 และอื่น ๆ ขึ้นอยู่กับสถานะของระบบ

<br/>

### ขั้นตอนที่ 3. คุณสามารถเมานต์ USB ไดรฟ์ด้วยตนเองโดยใช้คำสั่งต่อไปนี้:
   ```
   $ sudo mount /dev/sda1 /mnt
   ```

<br/><br/><br/>

## 5.2 การ์ด SD
---
D3-G มีช่องเสียบการ์ด microSD ที่รองรับการ์ด SDHC/SDXC มาตรฐาน
วิธีใช้การ์ด SD กับ D3-G:

<br/>

### ขั้นตอนที่ 1. เสียบการ์ด microSD เข้ากับช่องเสียบการ์ด SD บนบอร์ด D3-G
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20D3-G/Software/sd%20card%20connect%20with%20d3g.png" width="500"></p>
<p align="center"><strong>รูปที่ 5.2 การเชื่อมต่อการ์ด SD เข้ากับบอร์ด D3-G</strong></p> <br/>

### ขั้นตอนที่ 2. หลังจากเสียบแล้ว โดยทั่วไประบบจะรู้จักการ์ด SD เป็น /dev/mmcblk1p1 หรือโหนดอุปกรณ์ที่คล้ายกัน
  ```
  $ ls /dev/mmcblk*
  ```
<br/>

### ขั้นตอนที่ 3. หากต้องการเมานต์การ์ด SD ด้วยตนเอง ให้ใช้คำสั่งต่อไปนี้:
```
$ sudo mount /dev/mmcblk1p1 /mnt 
```
### ขั้นตอนที่ 4. หลังจากเมานต์แล้ว คุณสามารถเข้าถึงเนื้อหาของการ์ด SD ได้ภายใต้ไดเรกทอรี /mnt

<br/><br/><br/>

## 5.3 SATA HDD
---

D3-G รองรับการใช้งานอุปกรณ์สตอเรจ SATA เช่น HDD หรือ SSD ผ่านสล็อต PCIe โดยใช้คอนโทรลเลอร์ SATA ที่เข้ากันได้

<br/>

#### ขั้นตอนที่ 1. เชื่อมต่อโมดูล PCIe to SATA

หากต้องการใช้ SATA HDD กับ D3-G ผ่าน PCIe คุณต้องเชื่อมต่อโมดูลอะแดปเตอร์ PCIe-to-SATA เข้ากับสล็อต PCIe ของ D3-G ก่อน

จากนั้นเชื่อมต่อ HDD เข้ากับโมดูล SATA และตรวจสอบให้แน่ใจว่า HDD ได้รับไฟจากแหล่งจ่ายไฟภายนอก 12V

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20D3-G/Software/sata.png" width="500"></p>
<p align="center"><strong>รูปที่ 5.3 การเชื่อมต่อโมดูล SATA เข้ากับ PCIe ของบอร์ด D3-G </strong></p><br/>

#### ขั้นตอนที่ 2. บูต D3-G 
หลังจากบูต D3-G แล้ว ให้ตรวจสอบบันทึกการบูตเพื่อยืนยันว่าระบบรู้จักอุปกรณ์ PCIe
มองหาข้อความ เช่น **telechips-pcie: Link up** ซึ่งบ่งชี้ว่าลิงก์ PCIe ถูกสร้างขึ้นสำเร็จแล้ว

```
Starting kernel ...

[    1.191696] telechips-pcie 11000000.pcie: invalid resource
[    1.230423] telechips-pcie 11000000.pcie: Link up
[    1.693516] debugfs: Directory '16680000.udma' with parent 'dmaengine' already present!
[    1.702282] debugfs: Directory '16681000.udma' with parent 'dmaengine' already present!
[    1.711022] debugfs: Directory '16682000.udma' with parent 'dmaengine' already present!
[    1.719799] debugfs: Directory '16683000.udma' with parent 'dmaengine' already present!
[    1.728562] debugfs: Directory '16684000.udma' with parent 'dmaengine' already present!
[    1.737308] debugfs: Directory '16685000.udma' with parent 'dmaengine' already present!
[    1.746084] debugfs: Directory '16686000.udma' with parent 'dmaengine' already present!
[    1.754824] debugfs: Directory '16687000.udma' with parent 'dmaengine' already present!
 
...
Ubuntu 22.04.5 LTS TOPST ttyAMA0

TOPST login: 
```

<br/>

#### ขั้นตอนที่ 3. ตรวจสอบการรู้จัก SATA HDD
```
root@TOPST:~# lspci
00:00.0 PCI bridge: Synopsys, Inc. Device 8040 (rev 01)
01:00.0 SATA controller: ASMedia Technology Inc. Device 1064 (rev 02)
```
หากไม่มีคำสั่ง **lspci** ให้ติดตั้ง pciutils โดยใช้คำสั่งต่อไปนี้

```
$ sudo apt-get install pciutils
```

<br/>

#### ขั้นตอนที่ 4. เมานต์ SATA HDD
```
$ fdisk /dev/sda
Welcome to fdisk (util-linux 2.37.4).
Changes will remain in memory only, until you decide to write them.
Be careful before using the write command.

Command (m for help): 
```

พิมพ์คีย์ต่อไปนี้ตามลำดับในพรอมต์ของ fdisk:

- o — สร้างตารางพาร์ติชัน DOS ว่างขึ้นใหม่ (ไม่บังคับ ล้างตารางเดิมทิ้ง)

- n — เพิ่มพาร์ติชันใหม่

- p — เลือกพาร์ติชันหลัก

- 1 — กำหนดหมายเลขพาร์ติชันเป็น 1

- กด Enter — ยอมรับเซกเตอร์เริ่มต้นตามค่าเริ่มต้น

- กด Enter — ยอมรับเซกเตอร์สุดท้ายตามค่าเริ่มต้น (ใช้พื้นที่ดิสก์ทั้งหมด)

- w — เขียนตารางพาร์ทิชันและออกจากโปรแกรม

```
$ mkfs.ext4 /dev/sda1

$ mkdir -p /mnt/sata

$ mount /dev/sda1 /mnt/sata
```

<br/>

#### ขั้นตอนที่ 5. ผลลัพธ์การทำงาน
ผลลัพธ์นี้ยืนยันว่าพาร์ทิชันของ SATA SSD (/dev/sdb1) ได้รับการฟอร์แมตด้วยระบบไฟล์ ext4 และเมานต์ที่ /mnt/sata เรียบร้อยแล้ว
คำสั่ง **df -h** แสดงให้เห็นว่าระบบรู้จักอุปกรณ์นี้แล้วและพร้อมใช้งาน

```
$ df -h

Filesystem      Size  Used Avail Use% Mounted on
/dev/mmcblk0p4   29G  4.0G   25G  14% /
tmpfs           100M     0  100M   0% /dev/shm
tmpfs           592M  976K  591M   1% /run
tmpfs           5.0M  4.0K  5.0M   1% /run/lock
tmpfs           1.5G  4.0K  1.5G   1% /tmp
tmpfs           1.5G     0  1.5G   0% /var/volatile
tmpfs           296M  4.0K  296M   1% /run/user/0
/dev/sdb1       234G   28K  222G   1% /mnt/sata
```

<br/><br/><br/>

## 5.4 NVMe M.2 SSD
---
D3-G รองรับการเชื่อมต่อ NVMe M.2 SSD โดยตรงผ่านสล็อต PCIe
<br/>

#### ขั้นตอนที่ 1. เชื่อมต่อ SSD
- NVMe SSD (M.2 PCIe): เสียบ NVMe M.2 SSD เข้ากับสล็อต PCIe ของ D3-G 

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20D3-G/Software/M.2%20SSD%20connection.png" width="600"></p>
<p align="center"><strong>รูปที่ 5.4 การเชื่อมต่อ NVMe M.2 SSD เข้ากับบอร์ด D3-G</strong></p><br/>

#### ขั้นตอนที่ 2. บูต D3-G
หลังจากรันคำสั่ง **reboot** ให้ตรวจดูบันทึกการบูตเพื่อยืนยันว่าระบบตรวจพบอุปกรณ์ PCIe แล้ว
มองหาข้อความ เช่น **telechips-pcie: Link up** ซึ่งบ่งชี้ว่าลิงก์ PCIe ถูกสร้างขึ้นสำเร็จแล้ว

```
$ reboot
...
Starting kernel ...

[    1.191696] telechips-pcie 11000000.pcie: invalid resource
[    1.230423] telechips-pcie 11000000.pcie: Link up
[    1.693516] debugfs: Directory '16680000.udma' with parent 'dmaengine' already present!
[    1.702282] debugfs: Directory '16681000.udma' with parent 'dmaengine' already present!
[    1.711022] debugfs: Directory '16682000.udma' with parent 'dmaengine' already present!
[    1.719799] debugfs: Directory '16683000.udma' with parent 'dmaengine' already present!
[    1.728562] debugfs: Directory '16684000.udma' with parent 'dmaengine' already present!
[    1.737308] debugfs: Directory '16685000.udma' with parent 'dmaengine' already present!
[    1.746084] debugfs: Directory '16686000.udma' with parent 'dmaengine' already present!
[    1.754824] debugfs: Directory '16687000.udma' with parent 'dmaengine' already present!
 
...
Ubuntu 22.04.5 LTS TOPST ttyAMA0

TOPST login: 
```

<br/>

#### ขั้นตอนที่ 3. ตรวจสอบการตรวจพบ SSD
```
root@TOPST:~# lspci
00:00.0 PCI bridge: Synopsys, Inc. Device 8040 (rev 01)
01:00.0 Non-Volatile memory controller: Solid State Storage Technology Corporation Device 1007 (rev 03)
```
หากไม่มีคำสั่ง **lspci** ให้ติดตั้ง pciutils โดยใช้คำสั่งต่อไปนี้

```
$ sudo apt-get install pciutils
```

<br/>

#### ขั้นตอนที่ 4. เมานต์ SSD
```
$ fdisk /dev/nvme0n1
Welcome to fdisk (util-linux 2.37.4).
Changes will remain in memory only, until you decide to write them.
Be careful before using the write command.

Command (m for help): 
```

พิมพ์คีย์ต่อไปนี้ตามลำดับในพรอมต์ของ fdisk:

- o — สร้างตารางพาร์ติชัน DOS ว่างขึ้นใหม่ (ไม่บังคับ ล้างตารางเดิมทิ้ง)

- n — เพิ่มพาร์ติชันใหม่

- p — เลือกพาร์ติชันหลัก

- 1 — กำหนดหมายเลขพาร์ติชันเป็น 1

- กด Enter — ยอมรับเซกเตอร์เริ่มต้นตามค่าเริ่มต้น

- กด Enter — ยอมรับเซกเตอร์สุดท้ายตามค่าเริ่มต้น (ใช้พื้นที่ดิสก์ทั้งหมด)

- w — เขียนตารางพาร์ทิชันและออกจากโปรแกรม

```
$ mkfs.ext4 /dev/nvme0n1p1

$ mkdir -p /mnt/nvme

$ mount /dev/nvme0n1p1 /mnt/nvme
```

<br/>

#### ขั้นตอนที่ 5. ผลลัพธ์การทำงาน
ผลลัพธ์นี้ยืนยันว่าอุปกรณ์ NVMe SSD (/dev/nvme0n1p1) ได้รับการตรวจพบและเมาต์โดยระบบที่ /mnt/nvme เรียบร้อยแล้ว
```
$ df -h

Filesystem      Size  Used Avail Use% Mounted on
/dev/mmcblk0p4   29G  4.0G   25G  14% /
tmpfs           100M     0  100M   0% /dev/shm
tmpfs           592M  976K  591M   1% /run
tmpfs           5.0M  4.0K  5.0M   1% /run/lock
tmpfs           1.5G  4.0K  1.5G   1% /tmp
tmpfs           1.5G     0  1.5G   0% /var/volatile
tmpfs           296M  4.0K  296M   1% /run/user/0
/dev/nvme0n1p1  234G   28K  222G   1% /mnt/nvme
```
<br/><br/><br/><br/>


# 6. การเชื่อมต่ออีเทอร์เน็ต
---
D3-G รองรับการเชื่อมต่ออีเทอร์เน็ตผ่านพอร์ตอีเทอร์เน็ต J2C บนบอร์ด ซึ่งช่วยให้ D3-G สื่อสารกับเครือข่ายภายในหรืออินเทอร์เน็ตได้โดยใช้โปรโตคอล TCP/IP มาตรฐาน อีเทอร์เน็ตมักถูกใช้สำหรับการติดตั้งใช้งานแอปพลิเคชันที่ต้องการการเข้าถึงระยะไกล การสตรีมข้อมูล หรือการอัปเดตซอฟต์แวร์

<br/><br/><br/>

## 6.1 การเชื่อมต่อเครือข่ายผ่านเราเตอร์
---
วิธีนี้เชื่อมต่อ D3-G เข้ากับเครือข่ายภายในโดยใช้เราเตอร์มาตรฐาน D3-G สามารถรับที่อยู่ IP โดยอัตโนมัติผ่าน DHCP หรือกำหนดค่าให้ใช้ที่อยู่ IP แบบคงที่ได้

<br/><br/>

### 6.1.1 สร้างไฟล์กำหนดค่าเครือข่าย

1. IP แบบไดนามิกผ่าน DHCP
หากเครือข่ายของคุณมีเซิร์ฟเวอร์ DHCP (เช่น เราเตอร์ หรือเครื่อง PC ที่ใช้ Windows ซึ่งเปิดใช้งาน ICS) ก็ไม่จำเป็นต้องแก้ไขไฟล์ ระบบจะรับที่อยู่ IP โดยอัตโนมัติทันทีที่เชื่อมต่อสายอีเทอร์เน็ต

คุณเพียงเสียบสายแล้วเริ่มใช้งานเครือข่ายได้ทันที ให้ดำเนินการต่อที่บทที่ 6.1.3 การตรวจสอบการเชื่อมต่อเครือข่าย

2. การกำหนดค่า IP แบบคงที่
หากต้องการกำหนดที่อยู่ IP แบบคงที่ (ตัวอย่างเช่น เมื่อเชื่อมต่อกับ PC โดยตรง หรือไม่มีเซิร์ฟเวอร์ DHCP ให้ใช้งาน) ให้แก้ไขไฟล์เดิมด้วยเนื้อหาต่อไปนี้:
```
$ vi /etc/systemd/network/20-wired.network

[Match]
Name=eth0

[Network]
Address=192.168.137.2/24
Gateway=192.168.137.1
DNS=8.8.8.8
```

การตั้งค่านี้กำหนดที่อยู่ IP เป็น 192.168.137.2 ใช้ 192.168.137.1 เป็นเกตเวย์ (ซึ่งพบได้ทั่วไปใน Windows ICS) และกำหนดค่า Google DNS

<br/><br/>

### 6.1.2 รีสตาร์ตบริการเครือข่าย
ใช้การกำหนดค่าเครือข่ายใหม่โดยการรีสตาร์ตบริการ systemd-networkd:

```
sudo systemctl restart systemd-networkd
```

<br/><br/>

### 6.1.3 ตรวจสอบการเชื่อมต่อเครือข่าย
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20D3-G/Software/router%20connection.png"width="500"></p>
<p align="center"><strong>รูปที่ 6.1 การเชื่อมต่อเครือข่ายผ่านเราเตอร์</strong></p>

ทดสอบการเชื่อมต่ออินเทอร์เน็ตโดยการ ping ไปยังเซิร์ฟเวอร์ DNS สาธารณะของ Google:

```
$ ping 8.8.8.8
PING 8.8.8.8 (8.8.8.8): 56 data bytes
64 bytes from 8.8.8.8: seq=0 ttl=113 time=30.208 ms
64 bytes from 8.8.8.8: seq=1 ttl=113 time=38.143 ms
64 bytes from 8.8.8.8: seq=2 ttl=113 time=30.969 ms
64 bytes from 8.8.8.8: seq=3 ttl=113 time=33.586 ms
 
```

<br/><br/><br/>

## 6.2 การแชร์เครือข่ายกับเครื่อง PC โฮสต์
---
คุณสามารถแชร์การเชื่อมต่ออินเทอร์เน็ตของ PC กับ D3-G ได้โดยไม่ต้องใช้เราเตอร์ ด้วยการใช้คุณสมบัติ Internet Connection Sharing (ICS) ที่มีอยู่ในระบบปฏิบัติการ Windows

<br/><br/>

### 6.2.1 การกำหนดค่าเครือข่ายของเครื่อง PC โฮสต์
- แผงควบคุม → เครือข่ายและอินเทอร์เน็ต → การเชื่อมต่อเครือข่าย → ตั้งค่าอีเทอร์เน็ต
 
1. ค้นหาอะแดปเตอร์เครือข่ายที่เชื่อมต่อกับอินเทอร์เน็ต (ตัวอย่างเช่น Wi-Fi) คลิกขวาที่อะแดปเตอร์นั้น แล้วเลือก **คุณสมบัติ**

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20AI-G/Available%20Applications/ethernet1.png" width="600"></p>
<p align="center"><strong>รูปที่ 6.2 เลือก Properties</strong></p><br/>
 
2. เลือกแท็บการแชร์

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20AI-G/Available%20Applications/ethernet2.png" width="400"></p>
<p align="center"><strong>รูปที่ 6.3 เลือกแท็บ Sharing</strong></p><br/>

3. ทำเครื่องหมายในช่อง "อนุญาตให้ผู้ใช้เครือข่ายอื่นเชื่อมต่อผ่านการเชื่อมต่ออินเทอร์เน็ตของคอมพิวเตอร์เครื่องนี้"
 
4. ในเมนูแบบเลื่อนลง Home networking connection ให้เลือกอะแดปเตอร์อีเทอร์เน็ตที่ D3-G จะเชื่อมต่อด้วย (เช่น "Ethernet")

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20AI-G/Available%20Applications/ethernet3.png" width="400"></p>
<p align="center"><strong>รูปที่ 6.4 เลือกอะแดปเตอร์อีเทอร์เน็ต</strong></p><br/>
 
5. คลิก **ตกลง** เพื่อบันทึกการตั้งค่า

<br/><br/>

### 6.2.2 สร้างไฟล์กำหนดค่าเครือข่าย 
1. IP แบบไดนามิกผ่าน DHCP
หากเครือข่ายของคุณมีเซิร์ฟเวอร์ DHCP (เช่น เราเตอร์ หรือเครื่อง PC ที่ใช้ Windows ซึ่งเปิดใช้งาน ICS) ก็ไม่จำเป็นต้องแก้ไขไฟล์ ระบบจะรับที่อยู่ IP โดยอัตโนมัติทันทีที่เชื่อมต่อสายอีเทอร์เน็ต

คุณเพียงเสียบสายแล้วเริ่มใช้งานเครือข่ายได้ทันที ให้ดำเนินการต่อที่บทที่ 6.2.4 การตรวจสอบการเชื่อมต่อเครือข่าย

2. การกำหนดค่า IP แบบคงที่
หากต้องการกำหนดที่อยู่ IP แบบคงที่ (ตัวอย่างเช่น เมื่อเชื่อมต่อกับ PC โดยตรง หรือไม่มีเซิร์ฟเวอร์ DHCP ให้ใช้งาน) ให้แก้ไขไฟล์เดิมด้วยเนื้อหาต่อไปนี้:
```
$ vi /etc/systemd/network/20-wired.network

[Match]
Name=eth0

[Network]
Address=192.168.137.2/24
Gateway=192.168.137.1
DNS=8.8.8.8
```
การตั้งค่านี้กำหนดที่อยู่ IP เป็น 192.168.137.2 ใช้ 192.168.137.1 เป็นเกตเวย์ (ซึ่งพบได้ทั่วไปใน Windows ICS) และกำหนดค่า Google DNS

<br/><br/>

### 6.2.3 รีสตาร์ตบริการเครือข่าย
ใช้การกำหนดค่าเครือข่ายใหม่โดยการรีสตาร์ตบริการ systemd-networkd:

```
sudo systemctl restart systemd-networkd
```

<br/><br/>

### 6.2.4 ตรวจสอบการเชื่อมต่อเครือข่าย
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20D3-G/Software/host%20pc%20ethernet%20connection.png"width="500"></p>
<p align="center"><strong>รูปที่ 6.5 การแชร์เครือข่ายกับเครื่อง PC โฮสต์</strong></p>
<br/>

ทดสอบการเชื่อมต่ออินเทอร์เน็ตโดยการ ping ไปยังเซิร์ฟเวอร์ DNS สาธารณะของ Google:

```
$ ping 8.8.8.8
PING 8.8.8.8 (8.8.8.8): 56 data bytes
64 bytes from 8.8.8.8: seq=0 ttl=113 time=30.208 ms
64 bytes from 8.8.8.8: seq=1 ttl=113 time=38.143 ms
64 bytes from 8.8.8.8: seq=2 ttl=113 time=30.969 ms
64 bytes from 8.8.8.8: seq=3 ttl=113 time=33.586 ms
```

<br/><br/><br/><br/>

# 7. เฮดเดอร์ GPIO 40 พิน
---
D3-G มีเฮดเดอร์ GPIO 40 พิน ซึ่งให้ความสามารถด้าน I/O ที่ยืดหยุ่นสำหรับโปรเจกต์ฮาร์ดแวร์ต่าง ๆ
เฮดเดอร์นี้รองรับการทำงานแบบอินพุต/เอาต์พุตอเนกประสงค์ (GPIO) และสามารถใช้เชื่อมต่อเซ็นเซอร์ LED ปุ่มกด และอุปกรณ์ต่อพ่วงอื่น ๆ ได้

แต่ละพินรองรับหลายฟังก์ชัน เช่น I/O ดิจิทัล, PWM, I2C, SPI และ UART ขึ้นอยู่กับการกำหนดค่า

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/d3g/Assets/TOPST%20D3-G/Software/d3-g%20gpio%2040pinmap.png" width="800"></p>
<p align="center"><strong>รูปที่ 7.1 ผังพินของเฮดเดอร์ GPIO 40 พินของ D3-G </strong></p> <br/>

**หมายเหตุ**: ก่อนเชื่อมต่อฮาร์ดแวร์ภายนอก โปรดดูแผนผังพินอย่างเป็นทางการเพื่อทราบฟังก์ชันของพินและระดับแรงดันไฟฟ้าโดยละเอียด

<br/><br/><br/>

## 7.1 อินพุต/เอาต์พุตดิจิทัลของ GPIO
---
D3-G รองรับอินพุตและเอาต์พุตดิจิทัล (GPIO) ผ่านเฮดเดอร์ 40 พิน ซึ่งช่วยให้คุณโต้ตอบกับอุปกรณ์ภายนอก เช่น ปุ่มกด LED และเซ็นเซอร์ได้ 

### 7.1.1 LED
---
หนึ่งในตัวอย่างเอาต์พุต GPIO ที่ง่ายและพบบ่อยที่สุดคือการควบคุม LED  
หัวข้อนี้สาธิตวิธีเชื่อมต่อและใช้งานเซ็นเซอร์ LED โดยใช้ D3-G

#### ขั้นตอนที่ 1. ข้อกำหนดด้านฮาร์ดแวร์
- บอร์ด D3-G (x1)
- เบรดบอร์ด (x1)
- LED (x1)
- สายจัมเปอร์ผู้-เมีย (x2)
- อะแดปเตอร์จ่ายไฟ DC 5V (x1)
- สายซีเรียล USB to TTL (x1)

#### ขั้นตอนที่ 2. ตัวอย่างวงจร
- LED
    - พิน (+) เชื่อมต่อกับพินที่ 12 บนบอร์ด D3-G
    - พิน (-) เชื่อมต่อกับพินที่ 14 ซึ่งทำหน้าที่เป็น GND บนบอร์ด D3-G  
    
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20D3-G/Software/led.png"></p>

<p align="center"><strong>รูปที่ 7.2 แผนผังวงจร LED GPIO ของ D3-G </strong></p> <br/>

##### ขั้นตอนที่ 2.1 การแมปพิน
ตารางต่อไปนี้แสดงการแมปพิน

<div align="center">
  <p><strong>ตารางที่ 7.1 ผังพินของ LED บน D3-G</strong></p>
  <table>
      <tr>
          <th colspan="3">ชื่อพิน</th>
          <th>D3-G</th>
          <th>GPIO</th>
      </tr>
      <tr>
          <td colspan="3">พิน (+) ของ LED</td>
          <td>12</td>
          <td>89</td>
      </tr>
      <tr>
          <td colspan="3">พิน (-) ของ LED</td>
          <td>14</td>
          <td>GND</td>
      </tr>
  </table>
</div>

#### ขั้นตอนที่ 3. วิธีการดำเนินการ
หากต้องการสั่งงาน LED ที่เชื่อมต่อกับ GPIO89 บนบอร์ด D3-G ให้รันโค้ดต่อไปนี้:

```
import time
import os
  
def export_gpio(pin, direction: str):
    # If the pin is already active, unexport it.
    if os.path.exists(f"/sys/class/gpio/gpio{pin}"):
        with open("/sys/class/gpio/unexport", "w") as f:
            f.write(str(pin))
  
    # Export the pin to activate it.
    with open("/sys/class/gpio/export", "w") as f:
        f.write(str(pin))
  
    # Set the pin direction.
    with open(f"/sys/class/gpio/gpio{pin}/direction", "w") as f:
        f.write(direction)

def read_gpio_value(pin: int):
    gpio_value_path = f"/sys/class/gpio/gpio{pin}/value"
    with open(gpio_value_path, "r") as f:
        return f.read().strip()

def write_gpio_value(pin: int, value: int):
    gpio_value_path = f"/sys/class/gpio/gpio{pin}/value"
    with open(gpio_value_path, "w") as f:
        f.write(str(value))

def unexport_gpio(pin: int):
    with open("/sys/class/gpio/unexport", "w") as f:
        f.write(str(pin))

  
def main():
    print("""\
                        +--------+
                    3P3-|-1    2-|-5P0
       I2C_SDA / GPIO82-|-3    4-|-5P0
       I2C_SCL / GPIO81-|-5    6-|-GND
                 GPIO83-|-7    8-|-GPIO87 / UT_TXD
                    GND-|-9   10-|-GPIO88 / UT_RXD
                 GPIO84-|-11  12-|-GPIO89 / PWM 0
                 GPIO85-|-13  14-|-GND
                 GPIO86-|-15  16-|-GPIO90
                    3P3-|-17  18-|-GPIO65
     SPIO_MOSI / GPIO63-|-19  20-|-GND
     SPIO_MISO / GPIO64-|-21  22-|-GPIO66
     SPIO_SCLK / GPIO61-|-23  24-|-GPIO62 / SPIO_CS0
                    GND-|-25  26-|-GPIO67 / SPIO_CS1
              RESERVED0-|-27  28-|-RESERVED1
                GPIO112-|-29  30-|-GND
                GPIO113-|-31  32-|-GPIO115 / PWM 2
         PWM1 / GPIO114-|-33  34-|-GND
    SPI1_MISO / GPIO121-|-35  36-|-GPIO119 / SPI1_CS0
                GPIO117-|-37  38-|-GPIO120 / SPI1_MOSI
                    GND-|-39  40-|-GPIO118 / SPI1_SCLK
                        +--------+""")
  
    LED_PIN = 89  # LED connected to GPIO 89
  
    try:
        # Setup the GPIO pins
        export_gpio(LED_PIN, direction="out")
        print("GPIO pins initialized.")
        
        count = 0
        while (count < 10):
            write_gpio_value(LED_PIN, 1)  # Turn on the LED
            print("LED ON.")
            count += 1
            time.sleep(1.0)  # Polling delay
            write_gpio_value(LED_PIN, 0)  # Turn off the LED
            print("LED OFF.")
            time.sleep(1.0)  # Polling delay
 
        write_gpio_value(LED_PIN, 0)  # Turn off the LED
 
    except KeyboardInterrupt:
        print("Program interrupted by user.")
  
    finally:
        unexport_gpio(LED_PIN) # unexport LED pin
        print("GPIO pins unexported.")
        print("Program terminated.")

if __name__ == "__main__":
    main()
```

#### ขั้นตอนที่ 4. ผลลัพธ์การทำงาน
รันโค้ดด้วยคำสั่งต่อไปนี้

```
$ python3 led_test.py
```

สคริปต์นี้กำหนดค่า GPIO89 เป็นเอาต์พุตดิจิทัล และสลับสถานะของพินทุก ๆ 1 วินาที
เมื่อรันแล้ว LED ที่เชื่อมต่อกับ GPIO89 จะกะพริบ 10 ครั้ง โดยติด 1 วินาทีแล้วดับ 1 วินาทีสลับกันไป หลังจากครบ 10 รอบ สคริปต์จะสิ้นสุดการทำงานและ unexport GPIO โดยอัตโนมัติ

หากต้องการหยุดสคริปต์ก่อนกำหนด ให้กด **[Ctrl+C]**
ไม่ว่ากรณีใด พินจะถูกปลดและล้างค่าอย่างถูกต้อง

**หมายเหตุ**: การตั้งค่านี้ถือว่าเป็นการเชื่อมต่อ LED โดยตรง เพื่อการใช้งานที่ปลอดภัยและยาวนาน ขอแนะนำอย่างยิ่งให้ใช้ตัวต้านทานจำกัดกระแส (เช่น 220Ω) ต่ออนุกรมกับ LED เพื่อป้องกันการดึงกระแสมากเกินไปและปกป้องพิน GPIO จากความเสียหายที่อาจเกิดขึ้น

<br/><br/><br/><br/>

### 7.1.2 ปุ่มกด
---
ปุ่มกดเป็นอุปกรณ์อินพุตพื้นฐานที่มักใช้สาธิตการจัดการอินพุตดิจิทัลผ่าน GPIO
หัวข้อนี้สาธิตวิธีเชื่อมต่อและใช้งานโมดูลปุ่มกดพื้นฐานกับ D3-G

#### ขั้นตอนที่ 1. ข้อกำหนดด้านฮาร์ดแวร์
- บอร์ด D3-G (x1)
- เบรดบอร์ด (x1)
- ปุ่มกด (x1)
- สายจัมเปอร์ผู้-เมีย (x2)
- อะแดปเตอร์จ่ายไฟ DC 5V (x1)
- สายซีเรียล USB to TTL (x1)

#### ขั้นตอนที่ 2. ตัวอย่างวงจร
- สวิตช์ปุ่มกด
    - ขาหนึ่งของสวิตช์ปุ่มกดเชื่อมต่อกับพินที่ 10 บนบอร์ด D3-G
    - ขาด้านตรงข้ามเหนือปุ่มกดเชื่อมต่อกับพิน 3.3V

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20D3-G/Software/button_circuit.png"></p> 
<p align="center"><strong>รูปที่ 7.3 แผนผังวงจรปุ่มกด GPIO ของ D3-G</strong></p>

##### ขั้นตอนที่ 2.1 การแมปพิน
ตารางต่อไปนี้แสดงการแมปพิน

<div align="center">
  <p><strong>ตารางที่ 7.2 ผังพินของปุ่มกดบน D3-G</strong></p>
  <table>
      <tr>
          <th colspan="3">ชื่อพิน</th>
          <th>D3-G</th>
          <th>GPIO</th>
      </tr>
      <tr>
          <td colspan="3">พินขาหนึ่งของปุ่มกด</td>
          <td>10</td>
          <td>88</td>
      </tr>
  </table>
</div>

#### ขั้นตอนที่ 3. วิธีการดำเนินการ
หากต้องการตรวจสอบอินพุตของปุ่มกดที่เชื่อมต่อกับ GPIO88 บนบอร์ด D3-G ให้รันโค้ดต่อไปนี้:

```
import os
import time
BUTTON_PIN = 88  # button sensor GPIO pin
 
def export_gpio(pin: int, direction: str):
    # If the pin is already active, unexport it.
    if os.path.exists(f"/sys/class/gpio/gpio{pin}"):
        with open("/sys/class/gpio/unexport", "w") as f:
            f.write(str(pin))
  
    # Export the pin to activate it.
    with open("/sys/class/gpio/export", "w") as f:
        f.write(str(pin))
  
    # Set the pin direction.
    with open(f"/sys/class/gpio/gpio{pin}/direction", "w") as f:
        f.write(direction)

def read_gpio_value(pin: int):
    gpio_value_path = f"/sys/class/gpio/gpio{pin}/value"
    with open(gpio_value_path, "r") as f:
        return f.read().strip()

def write_gpio_value(pin: int, value: int):
    gpio_value_path = f"/sys/class/gpio/gpio{pin}/value"
    with open(gpio_value_path, "w") as f:
        f.write(str(value))

def unexport_gpio(pin: int):
    with open("/sys/class/gpio/unexport", "w") as f:
        f.write(str(pin))
def main():
    # initialize GPIO pins
    export_gpio(BUTTON_PIN, "in")  
    print("gpio pins initialized.")
 
    try:
        while True:
            sensor_value = read_gpio_value(BUTTON_PIN)
 
            if sensor_value == "0":  
                print("button pressed.")
            else:    
                print("button released.")
 
            time.sleep(0.5)  # 500ms delay

    except KeyboardInterrupt:
        print("Program interrupted by user.")
 
    finally:
        unexport_gpio(BUTTON_PIN)  # unexport the GPIO pin
        print("GPIO pins unexported.")
        print("Program terminated.")
         
if __name__ == "__main__":
    main()
```

#### ขั้นตอนที่ 4. ผลลัพธ์การทำงาน
รันโค้ดด้วยคำสั่งต่อไปนี้
```
$ python3 test_button.py
```
สคริปต์นี้กำหนดค่า GPIO88 เป็นอินพุตดิจิทัล และตรวจสอบค่าของพินอย่างต่อเนื่องแบบเรียลไทม์
เมื่อรันแล้ว การกดปุ่มที่เชื่อมต่อกับ GPIO88 จะแสดงข้อความที่ระบุว่ามีการกดปุ่ม

หากต้องการหยุดสคริปต์ ให้กด **[Ctrl+C]**
เมื่อสคริปต์สิ้นสุดการทำงาน GPIO88 จะถูก unexport และล้างค่าโดยอัตโนมัติ

**หมายเหตุ**: ที่นี่ใช้ GPIO88 เป็นตัวอย่าง คุณสามารถใช้พิน GPIO ใดก็ได้ที่ว่างอยู่บน D3-G ตามผังพินของเฮดเดอร์ 40 พิน
โปรดดูแผนผังพินอย่างเป็นทางการ และเลือกหมายเลข GPIO ที่ตรงกับการกำหนดค่าฮาร์ดแวร์ของคุณ

<br/><br/><br/><br/>

### 7.1.3 เซ็นเซอร์สัมผัส
---
เซ็นเซอร์สัมผัสสามารถใช้ตรวจจับการสัมผัสของมนุษย์เป็นสัญญาณอินพุตดิจิทัลผ่าน GPIO ได้
หัวข้อนี้สาธิตวิธีเชื่อมต่อและอ่านค่าอินพุตจากโมดูลเซ็นเซอร์สัมผัสพื้นฐานโดยใช้ D3-G

#### ขั้นตอนที่ 1. ข้อกำหนดด้านฮาร์ดแวร์
- บอร์ด D3-G (x1)
- เซ็นเซอร์สัมผัส (x1)
- สายจัมเปอร์ตัวเมีย-ตัวเมีย (x3)
- อะแดปเตอร์จ่ายไฟ DC 5V (x1)
- สายซีเรียล USB to TTL (x1)

#### ขั้นตอนที่ 2. ตัวอย่างวงจร
- เซ็นเซอร์สัมผัส
    - พิน SIG ของเซ็นเซอร์สัมผัสเชื่อมต่อกับพินที่ 88 บนบอร์ด D3-G
    - พิน VCC ของเซ็นเซอร์สัมผัสเชื่อมต่อกับ 3.3V บนบอร์ด D3-G
    - พิน GND ของเซ็นเซอร์สัมผัสเชื่อมต่อกับ GND บนบอร์ด D3-G


<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20D3-G/Software/touch%20circuit.png"></p>
<p align="center"><strong>รูปที่ 7.4 แผนผังวงจรเซ็นเซอร์สัมผัส GPIO ของ D3-G</strong></p>

##### ขั้นตอนที่ 2.1 การแมปพิน
ตารางต่อไปนี้แสดงการแมปพิน

<div align="center">
  <p><strong>ตารางที่ 7.3 ผังพินของเซ็นเซอร์สัมผัสบน D3-G</strong></p>
  <table>
      <tr>
          <th colspan="3">ชื่อพิน</th>
          <th>D3-G</th>
          <th>GPIO</th>
      </tr>
      <tr>
          <td colspan="3">SIG</td>
          <td>10</td>
          <td>88</td>
      </tr>
      <tr>
          <td colspan="3">VCC</td>
          <td>1</td>
          <td>3.3</td>
      </tr>
      <tr>
          <td colspan="3">GND</td>
          <td>20</td>
          <td>GND</td>
      </tr>
  </table>
</div>

#### ขั้นตอนที่ 3. วิธีการดำเนินการ
หากต้องการตรวจสอบเซ็นเซอร์สัมผัสที่เชื่อมต่อกับ GPIO88 บนบอร์ด D3-G เพียงรันโค้ดต่อไปนี้:
```
import os
import time
 
# GPIO pin numbers setting
TOUCH_SENSOR_PIN = 88  # sensor GPIO pin
 
def export_gpio(pin: int, direction: str):
    # If the pin is already active, unexport it.
    if os.path.exists(f"/sys/class/gpio/gpio{pin}"):
        with open("/sys/class/gpio/unexport", "w") as f:
            f.write(str(pin))
  
    # Export the pin to activate it.
    with open("/sys/class/gpio/export", "w") as f:
        f.write(str(pin))
  
    # Set the pin direction.
    with open(f"/sys/class/gpio/gpio{pin}/direction", "w") as f:
        f.write(direction)

def read_gpio_value(pin: int):
    gpio_value_path = f"/sys/class/gpio/gpio{pin}/value"
    with open(gpio_value_path, "r") as f:
        return f.read().strip()

def write_gpio_value(pin: int, value: int):
    gpio_value_path = f"/sys/class/gpio/gpio{pin}/value"
    with open(gpio_value_path, "w") as f:
        f.write(str(value))

def unexport_gpio(pin: int):
    with open("/sys/class/gpio/unexport", "w") as f:
        f.write(str(pin))
def main():
    # initialize GPIO pins
    export_gpio(TOUCH_SENSOR_PIN, "in")  # touch sensor pin direction "in"
    print("gpio pins initialized.")
 
    try:
        while True:
            # button sensor value read
            # If the sensor value is 0, it means an touch detected.
            # If the sensor value is 1, it means no touch released.
            sensor_value = read_gpio_value(TOUCH_SENSOR_PIN)
 
            if sensor_value == "1":  
                print("touch detected.")
            else:    
                print("touch released.")
 
            time.sleep(0.5)  # 500ms delay

    except KeyboardInterrupt:
        print("program interrupted by user.")
 
    finally:
        unexport_gpio(TOUCH_SENSOR_PIN)  # unexport the GPIO pin
        print("GPIO pins unexported.")
        print("program terminated.")
         
if __name__ == "__main__":
    main()
```

#### ขั้นตอนที่ 4. ผลลัพธ์การทำงาน
รันโค้ดด้วยคำสั่งต่อไปนี้

```
$ python3 touch_test.py
```

สคริปต์นี้กำหนดค่า GPIO88 เป็นอินพุตดิจิทัล และตรวจสอบค่าของพินอย่างต่อเนื่องแบบเรียลไทม์

เมื่อรันแล้ว การสัมผัสเซ็นเซอร์จะทำให้เทอร์มินัลแสดงข้อความ เช่น:
```
touch detected.
```
เมื่อไม่มีการสัมผัสเซ็นเซอร์ ผลลัพธ์จะเป็น:
```
touch released.
```
หากต้องการหยุดสคริปต์ ให้กด **[Ctrl+C]**
เมื่อสคริปต์สิ้นสุดการทำงาน GPIO88 จะถูก unexport และล้างค่าโดยอัตโนมัติ

**หมายเหตุ**: ที่นี่ใช้ GPIO88 เป็นตัวอย่าง คุณสามารถใช้พิน GPIO ใดก็ได้ที่ว่างอยู่บน D3-G ตามผังพินของเฮดเดอร์ 40 พิน
โปรดดูแผนผังพินอย่างเป็นทางการ และเลือกหมายเลข GPIO ที่ตรงกับการกำหนดค่าฮาร์ดแวร์ของคุณ

<br/><br/><br/><br/>

### 7.1.4 เซ็นเซอร์ตรวจจับการสั่นสะเทือน
---
เซ็นเซอร์ตรวจจับการสั่นสะเทือนสามารถใช้ตรวจจับแรงกระแทกหรือการสั่นสะเทือนทางกายภาพ และส่งสัญญาณอินพุตดิจิทัลผ่าน GPIO ได้
หัวข้อนี้แสดงวิธีเชื่อมต่อและตรวจจับอินพุตจากโมดูลเซ็นเซอร์ตรวจจับการสั่นสะเทือนพื้นฐานโดยใช้ D3-G

#### ขั้นตอนที่ 1. ข้อกำหนดด้านฮาร์ดแวร์
- บอร์ด D3-G (x1)
- เซ็นเซอร์ตรวจจับการสั่นสะเทือน (x1)
- สายจัมเปอร์แบบหัวเมีย-เมีย (x4)
- อะแดปเตอร์จ่ายไฟ DC 5V (x1)
- สายซีเรียล USB to TTL (x1)

#### ขั้นตอนที่ 2. ตัวอย่างวงจร
- เซ็นเซอร์ตรวจจับการสั่นสะเทือน
    - พิน VCC ของเซ็นเซอร์ตรวจจับการสั่นสะเทือนเชื่อมต่อกับพิน 3.3V บนบอร์ด D3-G
    - พิน GND ของเซ็นเซอร์ตรวจจับการสั่นสะเทือนเชื่อมต่อกับ GND บนบอร์ด D3-G
    - พิน DO ของเซ็นเซอร์ตรวจจับการสั่นสะเทือนเชื่อมต่อกับพิน 88 บนบอร์ด D3-G

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20D3-G/Software/vibr%20circuit.png"></p>
<p align="center"><strong>รูปที่ 7.5 ผังวงจรเซ็นเซอร์ตรวจจับการสั่นสะเทือนแบบ GPIO ของ D3-G</strong></p>

##### ขั้นตอนที่ 2.1 การแมปพิน
ตารางต่อไปนี้แสดงการแมปพิน

<div align="center">
  <p><strong>ตารางที่ 7.4 การแมปพินของเซ็นเซอร์ตรวจจับการสั่นสะเทือนของ D3-G</strong></p>
  <table>
      <tr>
          <th colspan="3">ชื่อพิน</th>
          <th>D3-G</th>
          <th>GPIO</th>
      </tr>
      <tr>
          <td colspan="3">VCC</td>
          <td>1</td>
          <td>3.3V</td>
      </tr>
      <tr>
          <td colspan="3">GND</td>
          <td>20</td>
          <td>GND</td>
      </tr>
      <tr>
          <td colspan="3">DO</td>
          <td>10</td>
          <td>88</td>
      </tr>
  </table>
</div>

#### ขั้นตอนที่ 3. วิธีการดำเนินการ
หากต้องการตรวจสอบเซ็นเซอร์ตรวจจับการสั่นสะเทือนที่เชื่อมต่อกับ GPIO88 บนบอร์ด D3-G ให้รันโค้ดต่อไปนี้:
```
import os
import time
VIBRATION_SENSOR_PIN = 88  # VIBRATION_SENSOR sensor GPIO pin
 
def export_gpio(pin: int, direction: str):
    # If the pin is already active, unexport it.
    if os.path.exists(f"/sys/class/gpio/gpio{pin}"):
        with open("/sys/class/gpio/unexport", "w") as f:
            f.write(str(pin))
  
    # Export the pin to activate it.
    with open("/sys/class/gpio/export", "w") as f:
        f.write(str(pin))
  
    # Set the pin direction.
    with open(f"/sys/class/gpio/gpio{pin}/direction", "w") as f:
        f.write(direction)

def read_gpio_value(pin: int):
    gpio_value_path = f"/sys/class/gpio/gpio{pin}/value"
    with open(gpio_value_path, "r") as f:
        return f.read().strip()

def write_gpio_value(pin: int, value: int):
    gpio_value_path = f"/sys/class/gpio/gpio{pin}/value"
    with open(gpio_value_path, "w") as f:
        f.write(str(value))

def unexport_gpio(pin: int):
    with open("/sys/class/gpio/unexport", "w") as f:
        f.write(str(pin))
def main():
    # initialize GPIO pins
    export_gpio(VIBRATION_SENSOR_PIN, "in")  # vibration sensor pin direction "in"
    print("gpio pins initialized.")
 
    try:
        while True:
            sensor_value = read_gpio_value(VIBRATION_SENSOR_PIN)
 
            if sensor_value == "0":  # vibration detected
                print("vibration detected.")
            else:    # no vibration detected
                print("no vibration detected.")
 
            time.sleep(0.5)  # 500ms delay

    except KeyboardInterrupt:
        print("Program interrupted by user.")
 
    finally:
        unexport_gpio(VIBRATION_SENSOR_PIN)  # unexport the GPIO pin
        print("GPIO pins unexported.")
        print("Program terminated.")
         
if __name__ == "__main__":
    main()
```

#### ขั้นตอนที่ 4. ผลลัพธ์การทำงาน
รันโค้ดด้วยคำสั่งต่อไปนี้

```
$ python3 vibration_test.py
```

สคริปต์นี้กำหนดค่า GPIO88 เป็นอินพุตดิจิทัล และตรวจสอบค่าของพินอย่างต่อเนื่องแบบเรียลไทม์
เมื่อรัน การสั่นสะเทือนหรือแรงกระแทกที่เซ็นเซอร์ตรวจจับได้จะทำให้เทอร์มินัลแสดงข้อความ เช่น:
```
vibration detected.
```
เมื่อไม่มีการสั่นสะเทือน ผลลัพธ์จะเป็นดังนี้:
```
no vibration detected.
```
หากต้องการหยุดสคริปต์ ให้กด **[Ctrl+C]**
เมื่อสิ้นสุดการทำงาน GPIO88 จะถูก unexport และล้างค่าโดยอัตโนมัติ

**หมายเหตุ**: ที่นี่ใช้ GPIO88 เป็นตัวอย่าง คุณสามารถใช้พิน GPIO อื่นที่ว่างอยู่ได้ตามการเดินสายเซ็นเซอร์และผังของเฮดเดอร์ โปรดดูผังพินของ D3-G ก่อนเลือกหมายเลข GPIO

<br/><br/><br/><br/>

### 7.1.5 เซ็นเซอร์อินฟราเรด (SZH-SSBH-002)
---
เซ็นเซอร์อินฟราเรดสามารถใช้ตรวจจับสิ่งกีดขวางที่อยู่ใกล้เคียงโดยการตรวจจับแสงอินฟราเรดที่สะท้อนกลับ และส่งสัญญาณดิจิทัลผ่าน GPIO
หัวข้อนี้แสดงวิธีเชื่อมต่อและอ่านอินพุตจากเซ็นเซอร์อินฟราเรด SZH-SSBH-002 โดยใช้ D3-G

#### ขั้นตอนที่ 1. ข้อกำหนดด้านฮาร์ดแวร์
- บอร์ด D3-G (x1)
- เบรดบอร์ด (x1)
- เซ็นเซอร์อินฟราเรด (x1)
- สายจัมเปอร์ผู้-เมีย (x5)
- อะแดปเตอร์จ่ายไฟ DC 5V (x1)
- สายซีเรียล USB to TTL (x1)

#### ขั้นตอนที่ 2. ตัวอย่างวงจร
- เซ็นเซอร์อินฟราเรด
    - พิน VCC ของเซ็นเซอร์อินฟราเรดเชื่อมต่อกับพิน 3.3V บนบอร์ด D3-G
    - พิน GND ของเซ็นเซอร์อินฟราเรดเชื่อมต่อกับ GND บนบอร์ด D3-G
    - พิน OUT ของเซ็นเซอร์อินฟราเรดเชื่อมต่อกับพิน 89 บนบอร์ด D3-G


<p align="center">
  <img src="https://raw.githubusercontent.com/topst-development/Documentation/d3g/Assets/TOPST%20D3-G/Software/szh-ssbh-002_circuit.png">
</p> 
<p align="center"><strong>รูปที่ 7.6 วงจรทดลองเซ็นเซอร์ IR</strong></p>

##### ขั้นตอนที่ 2.1 การแมปพิน
ตารางต่อไปนี้แสดงการแมปพิน

<div align="center">
  <p><strong>ตารางที่ 7.5 การแมปพินของเซ็นเซอร์ IR ของ D3-G</strong></p>
  <table>
      <tr>
          <th colspan="3">ชื่อพิน</th>
          <th>D3-G</th>
          <th>GPIO</th>
      </tr>
      <tr>
          <td colspan="3">VCC</td>
          <td>1</td>
          <td>3.3V</td>
      </tr>
      <tr>
          <td colspan="3">GND</td>
          <td>6</td>
          <td>GND</td>
      </tr>
      <tr>
          <td colspan="3">OUT</td>
          <td>12</td>
          <td>89</td>
      </tr>
  </table>
</div>

#### ขั้นตอนที่ 3. วิธีการดำเนินการ
หากต้องการตรวจสอบเซ็นเซอร์ IR ที่เชื่อมต่อกับ GPIO89 บนบอร์ด D3-G ให้รันโค้ดต่อไปนี้:

```
import os
import time
 
# GPIO pin numbers setting
IR_SENSOR_PIN = 89  # IR sensor GPIO pin
 
def export_gpio(pin: int, direction: str):
    # If the pin is already active, unexport it.
    if os.path.exists(f"/sys/class/gpio/gpio{pin}"):
        with open("/sys/class/gpio/unexport", "w") as f:
            f.write(str(pin))
  
    # Export the pin to activate it.
    with open("/sys/class/gpio/export", "w") as f:
        f.write(str(pin))
  
    # Set the pin direction.
    with open(f"/sys/class/gpio/gpio{pin}/direction", "w") as f:
        f.write(direction)

def read_gpio_value(pin: int):
    gpio_value_path = f"/sys/class/gpio/gpio{pin}/value"
    with open(gpio_value_path, "r") as f:
        return f.read().strip()

def write_gpio_value(pin: int, value: int):
    gpio_value_path = f"/sys/class/gpio/gpio{pin}/value"
    with open(gpio_value_path, "w") as f:
        f.write(str(value))

def unexport_gpio(pin: int):
    with open("/sys/class/gpio/unexport", "w") as f:
        f.write(str(pin))
def main():
    # initialize GPIO pins
    export_gpio(IR_SENSOR_PIN, "in")  # IR sensor pin direction "in"
    print("gpio pins initialized.")
 
    try:
        while True:
            sensor_value = read_gpio_value(IR_SENSOR_PIN)
 
            if sensor_value == "0":  # obstacle detected
                print("obstacle detected.")
            else: 
                print("No obstacle detected.")
 
            time.sleep(0.5)  # 500ms delay

    except KeyboardInterrupt:
        print("program interrupted by user.")
 
    finally:
        unexport_gpio(IR_SENSOR_PIN)  # unexport the GPIO pin
        print("GPIO pins unexported.")
        print("program terminated.")
         
if __name__ == "__main__":
    main()
```

#### ขั้นตอนที่ 4. ผลลัพธ์การทำงาน
รันโค้ดด้วยคำสั่งต่อไปนี้
```
$ python3 ir_test.py
```
สคริปต์นี้กำหนดให้ GPIO89 เป็นอินพุตดิจิทัล และตรวจสอบสถานะอย่างต่อเนื่องเพื่อตรวจจับสิ่งกีดขวาง
เมื่อตรวจพบวัตถุอยู่ด้านหน้าเซ็นเซอร์ IR เทอร์มินัลจะแสดง:
```
obstacle detected.
```
เมื่อไม่พบวัตถุ จะแสดง:
```
no obstacle detected.
```
หากต้องการหยุดสคริปต์ ให้กด **[Ctrl+C]**
เมื่อสคริปต์สิ้นสุดการทำงาน GPIO89 จะถูก unexport และล้างค่าโดยอัตโนมัติ

**หมายเหตุ**: สคริปต์นี้ใช้ GPIO89 เป็นตัวอย่าง
คุณสามารถใช้พิน GPIO ใดก็ได้ที่ว่างอยู่ตามเฮดเดอร์ 40 พินของ D3-G โปรดดูผังพินอย่างเป็นทางการเพื่อเลือกพินได้อย่างถูกต้อง

<br/><br/><br/><br/>

### 7.1.6 ตัวต้านทานไวแสง (SZH-SSBH-011)
---
ตัวต้านทานไวแสงสามารถใช้ตรวจจับระดับแสงโดยรอบ และส่งสัญญาณดิจิทัลผ่าน GPIO เมื่อความเข้มแสงเกินค่าเกณฑ์ที่กำหนด
หัวข้อนี้แสดงวิธีเชื่อมต่อและอ่านอินพุตจากเซ็นเซอร์ตัวต้านทานไวแสง SZH-SSBH-011 โดยใช้ D3-G

#### ขั้นตอนที่ 1. ข้อกำหนดด้านฮาร์ดแวร์
- บอร์ด D3-G (x1)
- โมดูลตัวต้านทานไวแสง (SZH-SSBH-011) (x1)
- LED (x1)
- ตัวต้านทาน 220Ω (x1)
- เบรดบอร์ด (x1)
- สายจัมเปอร์ผู้-เมีย (x7)
- อะแดปเตอร์จ่ายไฟ DC 5V (x1)
- สายซีเรียล USB to TTL (x1)

#### ขั้นตอนที่ 2. ตัวอย่างวงจร
- ตัวต้านทานไวแสง (SZH-SSBH-011)
    - พิน VCC ของตัวต้านทานไวแสงเชื่อมต่อกับพิน 3.3V บนบอร์ด D3-G
    - พิน GND ของตัวต้านทานไวแสงเชื่อมต่อกับ GND บนบอร์ด D3-G
    - พิน DO ของตัวต้านทานไวแสงเชื่อมต่อกับพิน 89 บนบอร์ด D3-G
- LED
    - พิน (+) ของ LED เชื่อมต่อกับ GND บนบอร์ด D3-G
    - พิน (-) ของ LED เชื่อมต่อกับพิน 83 บนบอร์ด D3-G

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20D3-G/Software/circuit.png"></p>
<p align="center"><strong>รูปที่ 7.7 วงจรทดลองตัวต้านทานไวแสง</strong></p>

##### ขั้นตอนที่ 2.1 การแมปพิน
ตารางต่อไปนี้แสดงการแมปพิน

<div align="center">
  <p><strong>ตารางที่ 7.6 การแมปพินของตัวต้านทานไวแสงของ D3-G</strong></p>
  <table>
      <tr>
          <th colspan="3">ชื่อพิน</th>
          <th>D3-G</th>
          <th>GPIO</th>
      </tr>
      <tr>
          <td colspan="3">VCC</td>
          <td>1</td>
          <td>3.3V</td>
      </tr>
      <tr>
          <td colspan="3">GND</td>
          <td>6</td>
          <td>GND</td>
      </tr>
      <tr>
          <td colspan="3">DO</td>
          <td>12</td>
          <td>89</td>
      </tr>
  </table>
</div>


<div align="center">
  <p><strong>ตารางที่ 7.7 การแมปพินของ LED ของ D3-G</strong></p>
  <table>
      <tr>
          <th colspan="3">ชื่อพิน</th>
          <th>D3-G</th>
          <th>GPIO</th>
      </tr>
      <tr>
          <td colspan="3">(+)</td>
          <td>7</td>
          <td>83</td>
      </tr>
      <tr>
          <td colspan="3">(-)</td>
          <td>14</td>
          <td>GND</td>
      </tr>
  </table>
</div>

### ขั้นตอนที่ 3. วิธีการรัน
รันสคริปต์ Python ต่อไปนี้เพื่อตรวจสอบความสว่างด้วยเซ็นเซอร์ CDS และควบคุม LED ตามนั้น:

```
import os
import time
LED_PIN = 83           # LED GPIO pin
CDS_SENSOR_PIN = 89    # szh-ssbh-011 CDS sensor GPIO pin

def export_gpio(pin, direction: str):
    # If the pin is already active, unexport it.
    if os.path.exists(f"/sys/class/gpio/gpio{pin}"):
        with open("/sys/class/gpio/unexport", "w") as f:
            f.write(str(pin))
  
    # Export the pin to activate it.
    with open("/sys/class/gpio/export", "w") as f:
        f.write(str(pin))
  
    # Set the pin direction.
    with open(f"/sys/class/gpio/gpio{pin}/direction", "w") as f:
        f.write(direction)

def read_gpio_value(pin: int):
    gpio_value_path = f"/sys/class/gpio/gpio{pin}/value"
    with open(gpio_value_path, "r") as f:
        return f.read().strip()

def write_gpio_value(pin: int, value: int):
    gpio_value_path = f"/sys/class/gpio/gpio{pin}/value"
    with open(gpio_value_path, "w") as f:
        f.write(str(value))

def unexport_gpio(pin: int):
    with open("/sys/class/gpio/unexport", "w") as f:
        f.write(str(pin))

def main():
    # initialize GPIO pins
    export_gpio(LED_PIN, "out")          # LED pin direction "out"
    export_gpio(CDS_SENSOR_PIN, "in")     # CDS sensor pin direction "in"
    print("gpio pins initialized.")

    try:
        while True:
            sensor_value = read_gpio_value(CDS_SENSOR_PIN)
            print("sensor value: {}".format(sensor_value))
            if sensor_value == "0": # light detected
                print("brightness detected. Turning on the LED.")
                write_gpio_value(LED_PIN, 1)  # turn on the LED
            else:
                print("no brightness detected. Turning off the LED.")
                write_gpio_value(LED_PIN, 0)  # turn off the LED

            time.sleep(0.5)  #  500ms delay

    except KeyboardInterrupt:
        print("program interrupted by user.")

    finally:
        unexport_gpio(LED_PIN)          # unexport LED pin
        unexport_gpio(CDS_SENSOR_PIN)   # unexport CDS sensor pin
        print("GPIO pins unexported.")
        print("program terminated.")

if __name__ == "__main__":
    main()
```

### ขั้นตอนที่ 4. ผลการรัน
รันโค้ดด้วยคำสั่งต่อไปนี้
```
$ python3 CDS_test.py
```
สคริปต์นี้กำหนดให้ GPIO89 เป็นอินพุตสำหรับเซ็นเซอร์ตัวต้านทานไวแสง และ GPIO83 เป็นเอาต์พุตสำหรับ LED
เมื่อตรวจพบแสงโดยรอบ เทอร์มินัลจะแสดง:
```
sensor value: 0
brightness detected. Turning on the LED.
```
และ LED จะติดสว่าง
เมื่อไม่พบแสง จะแสดง:
```
sensor value: 1
no brightness detected. Turning off the LED.
```
และ LED จะดับ
หากต้องการหยุดสคริปต์ ให้กด **[Ctrl+C]**
เมื่อสคริปต์สิ้นสุดการทำงาน พิน GPIO ทั้งสองจะถูก unexport และล้างค่าโดยอัตโนมัติ

**หมายเหตุ**: ตัวอย่างนี้ใช้ GPIO83 และ GPIO89 คุณสามารถใช้พิน GPIO ใดก็ได้ที่ว่างอยู่ตามผังเฮดเดอร์ 40 พินของ D3-G โปรดดูผังพินอย่างเป็นทางการเพื่อเลือกพินได้อย่างถูกต้อง

<br/><br/><br/><br/>

### 7.1.7 เซ็นเซอร์ตรวจจับมลพิษทางอากาศ
---
เซ็นเซอร์ตรวจจับมลพิษทางอากาศสามารถใช้ตรวจสอบการมีอยู่ของก๊าซอันตรายหรือฝุ่นละอองในสภาพแวดล้อม และส่งสัญญาณดิจิทัลผ่าน GPIO
หัวข้อนี้แสดงวิธีเชื่อมต่อและอ่านอินพุตจากเซ็นเซอร์ตรวจจับมลพิษทางอากาศโดยใช้ D3-G

#### ขั้นตอนที่ 1. ข้อกำหนดด้านฮาร์ดแวร์
- บอร์ด D3-G (x1)
- โมดูลเซ็นเซอร์ตรวจจับมลพิษทางอากาศ (ก๊าซ) (x1)
- เบรดบอร์ด (x1)
- สายจัมเปอร์ผู้-เมีย (x3)
- อะแดปเตอร์จ่ายไฟ DC 5V (x1)
- สายซีเรียล USB to TTL (x1)

#### ขั้นตอนที่ 2. ตัวอย่างวงจร
- เซ็นเซอร์ตรวจจับมลพิษทางอากาศ
    - พิน VCC ของเซ็นเซอร์ตรวจจับมลพิษทางอากาศเชื่อมต่อกับพิน 3.3V บนบอร์ด D3-G
    - พิน GND ของเซ็นเซอร์ตรวจจับมลพิษทางอากาศเชื่อมต่อกับ GND บนบอร์ด D3-G
    - พิน DO ของเซ็นเซอร์ตรวจจับมลพิษทางอากาศเชื่อมต่อกับพิน 88 บนบอร์ด D3-G

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20D3-G/Software/gas%20circuit.png"></p>
<p align="center"><strong>รูปที่ 7.8 วงจรทดลองเซ็นเซอร์ตรวจจับมลพิษทางอากาศ</strong></p>

##### ขั้นตอนที่ 2.1 การแมปพิน
ตารางต่อไปนี้แสดงการแมปพิน

<div align="center">
  <p><strong>ตารางที่ 7.8 การแมปพินของเซ็นเซอร์ตรวจจับมลพิษทางอากาศของ D3-G</strong></p>
  <table>
      <tr>
          <th colspan="3">ชื่อพิน</th>
          <th>D3-G</th>
          <th>GPIO</th>
      </tr>
      <tr>
          <td colspan="3">VCC</td>
          <td>1</td>
          <td>3.3V</td>
      </tr>
      <tr>
          <td colspan="3">GND</td>
          <td>20</td>
          <td>GND</td>
      </tr>
      <tr>
          <td colspan="3">DO</td>
          <td>10</td>
          <td>88</td>
      </tr>
  </table>
</div>

#### ขั้นตอนที่ 3. วิธีการรัน
รันสคริปต์ Python ต่อไปนี้เพื่อตรวจสอบการตรวจจับก๊าซโดยใช้พิน GPIO88:

```
import os
import time
GAS_SENSOR_PIN = 88  # gas sensor GPIO pin
 
def export_gpio(pin: int, direction: str):
    # If the pin is already active, unexport it.
    if os.path.exists(f"/sys/class/gpio/gpio{pin}"):
        with open("/sys/class/gpio/unexport", "w") as f:
            f.write(str(pin))
  
    # Export the pin to activate it.
    with open("/sys/class/gpio/export", "w") as f:
        f.write(str(pin))
  
    # Set the pin direction.
    with open(f"/sys/class/gpio/gpio{pin}/direction", "w") as f:
        f.write(direction)

def read_gpio_value(pin: int):
    gpio_value_path = f"/sys/class/gpio/gpio{pin}/value"
    with open(gpio_value_path, "r") as f:
        return f.read().strip()

def write_gpio_value(pin: int, value: int):
    gpio_value_path = f"/sys/class/gpio/gpio{pin}/value"
    with open(gpio_value_path, "w") as f:
        f.write(str(value))

def unexport_gpio(pin: int):
    with open("/sys/class/gpio/unexport", "w") as f:
        f.write(str(pin))
def main():
    # initialize GPIO pins
    export_gpio(GAS_SENSOR_PIN, "in")  # gas sensor pin direction "in"
    print("gpio pins initialized.")
 
    try:
        while True:
            # gas sensor value read
            sensor_value = read_gpio_value(GAS_SENSOR_PIN)
 
            if sensor_value == "0":  # gas detected
                print("gas detected.")
            else:
                print("no gas detected.")
 
            time.sleep(0.5)  # 500ms delay

    except KeyboardInterrupt:
        print("program interrupted by user.")
 
    finally:
        unexport_gpio(GAS_SENSOR_PIN)  # unexport the GPIO pin
        print("GPIO pins unexported.")
        print("program terminated.")
         
if __name__ == "__main__":
    main()
```

#### ขั้นตอนที่ 4. ผลลัพธ์การทำงาน
รันโค้ดด้วยคำสั่งต่อไปนี้
```
$ python3 gas_sensor_test.py
```
สคริปต์นี้กำหนดให้ GPIO88 เป็นอินพุตดิจิทัล และตรวจสอบสถานะการตรวจจับก๊าซอย่างต่อเนื่อง
เมื่อความเข้มข้นของก๊าซถึงค่าเกณฑ์ของเซ็นเซอร์ เทอร์มินัลจะแสดง:
```
gas detected.
```
เมื่อไม่พบก๊าซ เทอร์มินัลจะแสดง:
```
no gas detected.
```
หากต้องการหยุดสคริปต์ ให้กด **[Ctrl+C]**
เมื่อสคริปต์สิ้นสุดการทำงาน GPIO88 จะถูก unexport และล้างค่าโดยอัตโนมัติ

**หมายเหตุ**: ที่นี่ใช้ GPIO88 เป็นตัวอย่าง คุณสามารถใช้พิน GPIO ใดก็ได้ที่ว่างอยู่ตามผังเฮดเดอร์ 40 พินของ D3-G โปรดดูผังพินอย่างเป็นทางการเพื่อเลือกพินได้อย่างถูกต้อง

<br/><br/><br/><br/>

### 7.1.8 เซ็นเซอร์อัลตราโซนิก
---
เซ็นเซอร์อัลตราโซนิกสามารถใช้วัดระยะห่างจากวัตถุใกล้เคียงโดยการปล่อยคลื่นอัลตราโซนิกและรับสัญญาณที่สะท้อนกลับ จากนั้นส่งสัญญาณดิจิทัล (หรือแบบพัลส์) ผ่าน GPIO
หัวข้อนี้แสดงวิธีเชื่อมต่อและอ่านอินพุตจากเซ็นเซอร์อัลตราโซนิกโดยใช้ D3-G

#### ขั้นตอนที่ 1. ข้อกำหนดด้านฮาร์ดแวร์
- บอร์ด D3-G (x1)
- เซ็นเซอร์อัลตราโซนิก (x1)
- สายจัมเปอร์เมีย-เมีย (x4)
- อะแดปเตอร์จ่ายไฟ DC 5V (x1)
- สายซีเรียล USB to TTL (x1)

#### ขั้นตอนที่ 2. ตัวอย่างวงจร
- เซ็นเซอร์อัลตราโซนิก
    - พิน VCC ของเซ็นเซอร์อัลตราโซนิกเชื่อมต่อกับพิน 5V บนบอร์ด D3-G
    - พิน GND ของเซ็นเซอร์อัลตราโซนิกเชื่อมต่อกับ GND บนบอร์ด D3-G
    - พิน TRIG ของเซ็นเซอร์อัลตราโซนิกเชื่อมต่อกับพิน 82 บนบอร์ด D3-G
    - พิน ECHO ของเซ็นเซอร์อัลตราโซนิกเชื่อมต่อกับพิน 88 บนบอร์ด D3-G

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20D3-G/Software/ultra%20circuit.png"></p>
<p align="center"><strong>รูปที่ 7.9 วงจรทดลองเซ็นเซอร์อัลตราโซนิก</strong></p>

##### ขั้นตอนที่ 2.1 การแมปพิน
ตารางต่อไปนี้แสดงการแมปพิน

<div align="center">
  <p><strong>ตารางที่ 7.9 การแมปพินของเซ็นเซอร์อัลตราโซนิกของ D3-G</strong></p>
  <table>
      <tr>
          <th colspan="3">ชื่อพิน</th>
          <th>D3-G</th>
          <th>GPIO</th>
      </tr>
      <tr>
          <td colspan="3">VCC</td>
          <td>2</td>
          <td>5V</td>
      </tr>
      <tr>
          <td colspan="3">GND</td>
          <td>6</td>
          <td>GND</td>
      </tr>
      <tr>
          <td colspan="3">TRIG</td>
          <td>3</td>
          <td>82</td>
      </tr>
      <tr>
          <td colspan="3">ECHO</td>
          <td>10</td>
          <td>88</td>
      </tr>
  </table>
</div>

#### ขั้นตอนที่ 3. วิธีการรัน
รันสคริปต์ Python ต่อไปนี้เพื่อวัดระยะทางด้วยเซ็นเซอร์อัลตราโซนิก:
```
import os
import time

TRIG_PIN = 82  
ECHO_PIN = 88  

def export_gpio(pin: int, direction: str):
    if os.path.exists(f"/sys/class/gpio/gpio{pin}"):
        with open("/sys/class/gpio/unexport", "w") as f:
            f.write(str(pin))
    with open("/sys/class/gpio/export", "w") as f:
        f.write(str(pin))
    with open(f"/sys/class/gpio/gpio{pin}/direction", "w") as f:
        f.write(direction)

def write_gpio_value(pin: int, value: int):
    with open(f"/sys/class/gpio/gpio{pin}/value", "w") as f:
        f.write(str(value))

def read_gpio_value(pin: int) -> str:
    with open(f"/sys/class/gpio/gpio{pin}/value", "r") as f:
        return f.read().strip()

def unexport_gpio(pin: int):
    with open("/sys/class/gpio/unexport", "w") as f:
        f.write(str(pin))

def get_distance_cm():
    write_gpio_value(TRIG_PIN, 0)
    time.sleep(0.00002)  
    write_gpio_value(TRIG_PIN, 1)
    time.sleep(0.00001)  
    write_gpio_value(TRIG_PIN, 0)

    start = time.time()
    while read_gpio_value(ECHO_PIN) == "0":
        start = time.time()
    end = start
    while read_gpio_value(ECHO_PIN) == "1":
        end = time.time()
    duration = end - start
    distance = (duration * 34300) / 2  # cm
    return round(distance, 2)

def main():
    export_gpio(TRIG_PIN, "out")
    export_gpio(ECHO_PIN, "in")
    print("GPIO pins initialized.")

    try:
        while True:
            distance = get_distance_cm()
            print(f"Distance: {distance} cm")
            time.sleep(1)

    except KeyboardInterrupt:
        print("Program interrupted by user.")

    finally:
        unexport_gpio(TRIG_PIN)
        unexport_gpio(ECHO_PIN)
        print("GPIO pins unexported.")
        print("Program terminated.")

if __name__ == "__main__":
    main()
```

#### ขั้นตอนที่ 4. ผลลัพธ์การทำงาน
รันโค้ดด้วยคำสั่งต่อไปนี้
```
$ python3 ultrasonic_sensor_test.py
```
สคริปต์นี้กำหนดให้ GPIO82 เป็นเอาต์พุตดิจิทัลสำหรับกระตุ้นพัลส์อัลตราโซนิก และ GPIO88 เป็นอินพุตดิจิทัลสำหรับรับสัญญาณสะท้อน
เมื่อสคริปต์ทำงาน ระยะห่างถึงวัตถุที่ใกล้ที่สุดด้านหน้าเซ็นเซอร์จะถูกแสดงทุกวินาที ตัวอย่างเช่น:
```
Distance: 23.45 cm
Distance: 24.12 cm
...
```
หากต้องการหยุดสคริปต์ ให้กด **[Ctrl+C]**
เมื่อสคริปต์สิ้นสุดการทำงาน GPIO82 และ GPIO88 จะถูก unexport และล้างค่าโดยอัตโนมัติ

**หมายเหตุ**: ที่นี่ใช้ GPIO82 และ GPIO88 เป็นตัวอย่าง คุณสามารถใช้พิน GPIO ใดก็ได้ที่ว่างอยู่ตามผังเฮดเดอร์ 40 พินของ D3-G โปรดดูผังพินอย่างเป็นทางการเพื่อเลือกพินได้อย่างถูกต้อง นอกจากนี้ โปรดตรวจสอบว่าระดับแรงดันของพิน ECHO ปลอดภัยสำหรับ D3-G (บางโมดูลส่งออก 5V และอาจต้องใช้วงจรแบ่งแรงดันหรือเลเวลชิฟเตอร์)

<br/><br/><br/><br/>

## 7.2 I2C
---
D3-G รองรับการสื่อสาร I2C ผ่านเฮดเดอร์ GPIO 40 พิน ทำให้สามารถเชื่อมต่อกับอุปกรณ์ต่อพ่วงต่าง ๆ เช่น เซ็นเซอร์ จอแสดงผล และโมดูลส่วนขยาย
Inter-integrated Circuit (I2C) เป็นโปรโตคอลการสื่อสารแบบสองสายที่ประกอบด้วยสายข้อมูล (SDA) และสายสัญญาณนาฬิกา (SCL) ซึ่งช่วยให้อุปกรณ์หลายตัวสื่อสารกันบนบัสร่วมกันได้

การสื่อสาร I2C ใช้สถาปัตยกรรมแบบมาสเตอร์-สเลฟ โดยอุปกรณ์มาสเตอร์หนึ่งตัวควบคุมการสื่อสาร และสามารถเชื่อมต่ออุปกรณ์สเลฟได้สูงสุด 127 ตัวบนบัสเดียวกัน
สาย SDA ใช้สำหรับทั้งการส่งและรับข้อมูล ส่วนสาย SCL ทำหน้าที่ซิงโครไนซ์จังหวะเวลาของการถ่ายโอนข้อมูล รูปแบบการสื่อสารแบบซิงโครนัสนี้ทำให้อุปกรณ์แลกเปลี่ยนข้อมูลกันได้อย่างประสานสอดคล้องตามสัญญาณนาฬิกา

<br/><br/><br/><br/>

### 7.2.1 จอแสดงผล LCD 1602A
---
1602A LCD เป็นโมดูลแสดงผลตัวอักษรที่ใช้กันทั่วไปในระบบสมองกลฝังตัว
บน D3-G สาย SDA และ SCL ของ LCD สามารถเชื่อมต่อกับพิน GPIO ที่กำหนดค่าไว้สำหรับ I2C ได้ เมื่อเชื่อมต่อแล้ว สามารถควบคุม LCD ได้ด้วยเครื่องมือ I2C ของ Linux หรือซอฟต์แวร์ที่พัฒนาขึ้นเอง

#### ขั้นตอนที่ 1. ข้อกำหนดด้านฮาร์ดแวร์
- บอร์ด D3-G (x1)
- โมดูล 1602A I2C LCD (x1)
- สายจัมเปอร์เมีย-เมีย (x4)
- อะแดปเตอร์จ่ายไฟ DC 5V (x1)
- สายซีเรียล USB to TTL (x1)  

โปรดตรวจสอบว่าโมดูล LCD มีบอร์ดแปลง I2C ติดตั้งอยู่

#### ขั้นตอนที่ 2. ตัวอย่างวงจร
- โมดูล I2C LCD
    - พิน GND ของโมดูล I2C LCD เชื่อมต่อกับพิน GND บนบอร์ด D3-G
    - พิน VCC ของโมดูล I2C LCD เชื่อมต่อกับ 5V บนบอร์ด D3-G
    - พิน SDA ของโมดูล I2C LCD เชื่อมต่อกับพิน 82 บนบอร์ด D3-G
    - พิน SCL ของโมดูล I2C LCD เชื่อมต่อกับพิน 81 บนบอร์ด D3-G

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20D3-G/Software/lcd_circuit.png"></p>
<p align="center"><strong>รูปที่ 7.10 ผังวงจรโมดูล I2C LCD ของ D3-G  </strong></p>

##### ขั้นตอนที่ 2.1 การแมปพิน
ตารางต่อไปนี้แสดงการแมปพิน

<div align="center">
  <p><strong>ตารางที่ 7.10 การแมปพินของโมดูล I2C LCD ของ D3-G</strong></p>
  <table>
      <tr>
          <th colspan="3">ชื่อพิน</th>
          <th>D3-G</th>
          <th>GPIO</th>
      </tr>
      <tr>
          <td colspan="3">GND</td>
          <td>20</td>
          <td>GND</td>
      </tr>
      <tr>
          <td colspan="3">VCC</td>
          <td>2</td>
          <td>5V</td>
      </tr>
      <tr>
          <td colspan="3">SDA</td>
          <td>3</td>
          <td>82</td>
      </tr>
      <tr>
          <td colspan="3">SCL</td>
          <td>5</td>
          <td>81</td>
      </tr>
  </table>
</div>

#### ขั้นตอนที่ 3. วิธีการดำเนินการ
ติดตั้งไลบรารี Python ที่จำเป็นก่อน:
```
$ pip install RPLCD smbus2
```
จากนั้นใช้โค้ด Python ต่อไปนี้เพื่อเขียนข้อความไปยัง LCD:
```
import smbus2
import time
from RPLCD.i2c import CharLCD
 
# I2C bus num
I2C_BUS = 3
LCD_ADDRESS = 0x27

lcd = CharLCD(i2c_expander='PCF8574', address=LCD_ADDRESS, port=I2C_BUS,
              cols=16, rows=2, dotsize=8,
              charmap='A00', auto_linebreaks=True,
              backlight_enabled=True)
 
def display_text(text):
    lcd.clear()
    lcd.write_string(text)

def main():
    while True:
        user_input = input("Enter text to display on LCD: ")
        display_text(user_input)
        time.sleep(4)
        lcd.clear()
if __name__ == "__main__":
    main()
```

#### ขั้นตอนที่ 4. ผลลัพธ์การทำงาน
รันโค้ดด้วยคำสั่งต่อไปนี้
```
$ python3 lcd_test.py
```
สคริปต์นี้เริ่มต้นการทำงานของ LCD 1602A แบบ I2C โดยใช้ไลบรารี RPLCD และแสดงข้อความที่ผู้ใช้ป้อนบนหน้าจอ
เมื่อเรียกใช้สคริปต์ ระบบจะแจ้งให้ป้อนข้อความ ข้อความดังกล่าวจะแสดงบน LCD เป็นเวลา 4 วินาที จากนั้นจะถูกล้าง ตัวอย่างเช่น:
```
Enter text to display on LCD: Hello D3-G!
```
LCD จะแสดงผลดังนี้:
```
Hello D3-G!
```
จากนั้นจะถูกล้างหลังจาก 4 วินาที

หากต้องการหยุดสคริปต์ ให้กด **[Ctrl+C]**

**หมายเหตุ** : บน D3-G จะใช้ GPIO82 และ GPIO81 สำหรับ I2C โดยค่าเริ่มต้น
โปรดตรวจสอบว่าที่อยู่ I2C (0x27) ตรงกับโมดูล LCD ที่ใช้งานอยู่ หากจำเป็น ให้ใช้ **i2cdetect -y 3** เพื่อสแกนหาอุปกรณ์ I2C

<br/><br/><br/><br/>

## 7.3 SPI
---
D3-G รองรับการสื่อสารแบบ Serial Peripheral Interface (SPI) ผ่านเฮดเดอร์ GPIO 40 พิน ทำให้สามารถแลกเปลี่ยนข้อมูลระหว่างอุปกรณ์ภายนอกกับ D3-G ได้

SPI เป็นโปรโตคอลการสื่อสารแบบอนุกรมชนิดซิงโครนัสที่รองรับการสื่อสารแบบฟูลดูเพล็กซ์ กล่าวคือสามารถส่งและรับข้อมูลได้พร้อมกัน โดยใช้สายสัญญาณหลักสี่เส้น ได้แก่ Master Out Slave In (MOSI), Master In Slave Out (MISO), Serial Clock (SCLK) และ Chip Select (CS)

ต่างจาก I2C ที่ใช้สายสัญญาณร่วมกันสำหรับอุปกรณ์หลายตัว SPI ต้องใช้สาย CS เฉพาะสำหรับอุปกรณ์สเลฟแต่ละตัว โครงสร้างแบบหนึ่งต่อหลายนี้ทำให้ SPI มีความเร็วสูงและนำไปใช้งานได้ง่าย แต่อาจต้องใช้การเดินสายทางกายภาพมากขึ้นเมื่อมีอุปกรณ์หลายตัว

<br/><br/><br/><br/>

### 7.3.1 ดอตเมทริกซ์
---
จอแสดงผลดอตเมทริกซ์ขนาด 8x8 มักใช้สำหรับแสดงข้อความหรือรูปแบบอย่างง่ายในระบบสมองกลฝังตัว บน D3-G สามารถควบคุมโมดูลดอตเมทริกซ์ผ่าน SPI โดยใช้ชิปไดรเวอร์ เช่น MAX7219

MAX7219 จัดการการสแกนแถวและคอลัมน์ภายในตัวเอง ทำให้ไมโครคอนโทรลเลอร์สามารถควบคุมจอแสดงผลทั้งหมดได้โดยใช้สัญญาณ SPI เพียงไม่กี่เส้น ได้แก่ MOSI (DIN), SCLK และ CS (LOAD) เมื่อเชื่อมต่อแล้ว สามารถควบคุมจอแสดงผลผ่านการสื่อสาร SPI ด้วยสคริปต์หรือไลบรารีที่ผู้ใช้กำหนดเองได้

#### ขั้นตอนที่ 1. ข้อกำหนดด้านฮาร์ดแวร์
- บอร์ด D3-G (x1)
- ดอตเมทริกซ์ (x1)
- สายจัมเปอร์ผู้-เมีย (x4)
- อะแดปเตอร์จ่ายไฟ DC 5V (x1)
- สายซีเรียล USB to TTL (x1)

#### ขั้นตอนที่ 2. ตัวอย่างวงจร
- ดอตเมทริกซ์
    - พิน VCC ของดอตเมทริกซ์เชื่อมต่อกับพิน 5V บนบอร์ด D3-G
    - พิน GND ของดอตเมทริกซ์เชื่อมต่อกับพิน GND บนบอร์ด D3-G
    - พิน DIN ของดอตเมทริกซ์เชื่อมต่อกับพินหมายเลข 120 บนบอร์ด D3-G
    - พิน CS ของดอตเมทริกซ์เชื่อมต่อกับพินหมายเลข 119 บนบอร์ด D3-G
    - พิน CLK ของดอตเมทริกซ์เชื่อมต่อกับพินหมายเลข 118 บนบอร์ด D3-G

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20D3-G/Software/dot%20circuit.png"></p>
<p align="center"><strong>รูปที่ 7.11 แผนผังวงจรโมดูลดอตเมทริกซ์ของ D3-G  </strong></p>

##### ขั้นตอนที่ 2.1 การแมปพิน
ตารางต่อไปนี้แสดงการแมปพิน
<div align="center">
  <p><strong>ตารางที่ 7.11 การแมปพินของดอตเมทริกซ์ D3-G</strong></p>
  <table>
      <tr>
          <th colspan="3">ชื่อพิน</th>
          <th>D3-G</th>
          <th>GPIO</th>
      </tr>
      <tr>
          <td colspan="3">VCC</td>
          <td>2</td>
          <td>5V</td>
      </tr>
      <tr>
          <td colspan="3">GND</td>
          <td>6</td>
          <td>GND</td>
      </tr>
      <tr>
          <td colspan="3">DIN</td>
          <td>19</td>
          <td>63</td>
      </tr>
      <tr>
          <td colspan="3">CS</td>
          <td>24</td>
          <td>62</td>
      </tr>
      <tr>
          <td colspan="3">CLK</td>
          <td>23</td>
          <td>61</td>
      </tr>
  </table>
</div>

#### ขั้นตอนที่ 3. วิธีการดำเนินการ
สคริปต์ Python ต่อไปนี้แสดงวิธีควบคุม MAX7219 โดยตรงผ่าน /dev/spidev3.0 ด้วยการเรียกใช้ fcntl ระดับล่าง วิธีนี้เหมาะสำหรับอุปกรณ์ที่ไม่มีไลบรารี SPI ภายนอก:
```
#!/usr/bin/env python3
 
import os
import fcntl
import time
from ctypes import Structure, addressof, create_string_buffer, c_uint64, c_uint32, c_uint16, c_uint8
 
SPI_MODE = 0
SPI_SPEED_HZ = 5000000
SPI_BITS_PER_WORD = 8
 
SPI_IOC_RD_MODE = 0x80016b01
SPI_IOC_WR_MODE = 0x40016b01
SPI_IOC_RD_BITS_PER_WORD = 0x80016b03
SPI_IOC_WR_BITS_PER_WORD = 0x40016b03
SPI_IOC_WR_MAX_SPEED_HZ = 0x40046b04
SPI_IOC_MESSAGE_1 = 0x40206b00
 
class spi_ioc_transfer(Structure):
    _fields_ = [
        ("tx_buf", c_uint64),
        ("rx_buf", c_uint64),
        ("len", c_uint32),
        ("speed_hz", c_uint32),
        ("delay_usecs", c_uint16),
        ("bits_per_word", c_uint8),
        ("cs_change", c_uint8),
        ("pad", c_uint32)
    ]
 
def spi_transfer(fd, tx_data):
    tx_buffer = create_string_buffer(bytes(tx_data))
    rx_buffer = create_string_buffer(len(tx_data))
 
    xfer = spi_ioc_transfer(
        tx_buf=addressof(tx_buffer),
        rx_buf=addressof(rx_buffer),
        len=len(tx_data),
        delay_usecs=0,
        speed_hz=SPI_SPEED_HZ,
        bits_per_word=SPI_BITS_PER_WORD,
        cs_change=0
    )
 
    fcntl.ioctl(fd, SPI_IOC_MESSAGE_1, xfer)
 
    return list(rx_buffer)
 
def MAX7219_write(fd, address, data):
    spi_transfer(fd, [address, data])
 
def MAX7219_init(fd):
    MAX7219_write(fd, 0x09, 0x00)  # Decoding mode: none
    MAX7219_write(fd, 0x0A, 0x03)  # Intensity: 3 (range 0-15)
    MAX7219_write(fd, 0x0B, 0x07)  # Scan limit: 8 LEDs
    MAX7219_write(fd, 0x0C, 0x01)  # Power on
    MAX7219_write(fd, 0x0F, 0x00)  # Display test: off
 
NUMBER_CODE = [
    [0x3C, 0x42, 0x42, 0x42, 0x42, 0x42, 0x42, 0x3C],  # 0
    [0x10, 0x30, 0x50, 0x10, 0x10, 0x10, 0x10, 0x7C],  # 1
    [0x3E, 0x02, 0x02, 0x3E, 0x20, 0x20, 0x3E, 0x00],  # 2
    [0x00, 0x7C, 0x04, 0x04, 0x7C, 0x04, 0x04, 0x7C],  # 3
    [0x08, 0x18, 0x28, 0x48, 0xFE, 0x08, 0x08, 0x08],  # 4
    [0x3C, 0x20, 0x20, 0x3C, 0x04, 0x04, 0x3C, 0x00],  # 5
    [0x3C, 0x20, 0x20, 0x3C, 0x24, 0x24, 0x3C, 0x00],  # 6
    [0x3E, 0x22, 0x04, 0x08, 0x08, 0x08, 0x08, 0x08],  # 7
    [0x00, 0x3E, 0x22, 0x22, 0x3E, 0x22, 0x22, 0x3E],  # 8
    [0x3E, 0x22, 0x22, 0x3E, 0x02, 0x02, 0x02, 0x3E]   # 9
]
 
ALPHABET_CODE = {
    'A': [0x08, 0x14, 0x22, 0x3E, 0x22, 0x22, 0x22, 0x22],
    'B': [0x3C, 0x22, 0x22, 0x3E, 0x22, 0x22, 0x3C, 0x00],
    'C': [0x3C, 0x40, 0x40, 0x40, 0x40, 0x40, 0x3C, 0x00],
    'D': [0x7C, 0x42, 0x42, 0x42, 0x42, 0x42, 0x7C, 0x00],
    'E': [0x7C, 0x40, 0x40, 0x7C, 0x40, 0x40, 0x40, 0x7C],
    'F': [0x7C, 0x40, 0x40, 0x7C, 0x40, 0x40, 0x40, 0x40],
    'G': [0x3C, 0x40, 0x40, 0x40, 0x40, 0x44, 0x44, 0x3C],
    'H': [0x44, 0x44, 0x44, 0x7C, 0x44, 0x44, 0x44, 0x44],
    'I': [0x7C, 0x10, 0x10, 0x10, 0x10, 0x10, 0x10, 0x7C],
    'J': [0x3C, 0x08, 0x08, 0x08, 0x08, 0x08, 0x48, 0x30],
    'K': [0x40, 0x40, 0x40, 0x40, 0x40, 0x40, 0x40, 0x7C],
    'L': [0x40, 0x40, 0x40, 0x40, 0x40, 0x40, 0x40, 0x7C],
    'M': [0x00, 0x42, 0x62, 0x52, 0x4A, 0x46, 0x42, 0x00],
    'N': [0x00, 0x42, 0x62, 0x52, 0x4A, 0x46, 0x42, 0x00],
    'O': [0x3C, 0x42, 0x42, 0x42, 0x42, 0x42, 0x42, 0x3C],
    'P': [0x3C, 0x42, 0x42, 0x3E, 0x02, 0x02, 0x02, 0x3E],
    'Q': [0x3C, 0x42, 0x42, 0x42, 0x42, 0x42, 0x42, 0x3C],
    'R': [0x08, 0x14, 0x22, 0x3E, 0x22, 0x22, 0x22, 0x22],
    'S': [0x7C, 0x40, 0x40, 0x7C, 0x40, 0x40, 0x40, 0x7C],
    'T': [0x7C, 0x10, 0x10, 0x10, 0x10, 0x10, 0x10, 0x7C],
    'U': [0x3C, 0x08, 0x08, 0x08, 0x08, 0x08, 0x48, 0x30],
    'V': [0x40, 0x40, 0x40, 0x40, 0x40, 0x40, 0x40, 0x7C],
    'W': [0x00, 0x41, 0x41, 0x41, 0x49, 0x2a, 0x2a, 0x14],
    'X': [0x40, 0x40, 0x40, 0x40, 0x40, 0x40, 0x40, 0x7C],
    'Y': [0x7C, 0x40, 0x40, 0x7C, 0x40, 0x40, 0x40, 0x7C],
    'Z': [0x7C, 0x40, 0x40, 0x7C, 0x40, 0x40, 0x40, 0x7C],
    'Smile': [0x3c, 0x42, 0xa5, 0x81, 0xa5, 0x99, 0x42, 0x3c],
    'dance0': [0x10, 0x28, 0x10, 0x10, 0xfe, 0x10, 0x28, 0x28],
    'dance1': [0x10, 0x28, 0x92, 0x54, 0x38, 0x10, 0x28, 0x44],
    'angry': [0x00, 0x00, 0xe7, 0x00, 0x00, 0x00, 0x3c, 0x00],
    'Good': [0x30, 0x30, 0x30, 0x3c, 0x32, 0x3c, 0x32, 0x3c]
}
 
 
def main():
    print('*' * 50)
    fd = os.open('/dev/spidev3.0', os.O_RDWR)
 
    fcntl.ioctl(fd, SPI_IOC_RD_BITS_PER_WORD, bytes([SPI_BITS_PER_WORD]))
    fcntl.ioctl(fd, SPI_IOC_WR_BITS_PER_WORD, bytes([SPI_BITS_PER_WORD]))
    fcntl.ioctl(fd, SPI_IOC_WR_MODE, bytes([SPI_MODE]))
    fcntl.ioctl(fd, SPI_IOC_WR_MAX_SPEED_HZ, SPI_SPEED_HZ.to_bytes(4, byteorder='little'))
 
    MAX7219_init(fd)
 
    try:
        while True:
            input_str = input("Enter a number, an uppercase letter (0-9, A-Z), 'Smile', 'Dance', 'Angry', 'Good', 'Nice', 'Emotion': ")
            if input_str.isdigit() and 0 <= int(input_str) <= 9:
                num = int(input_str)
                for col in range(8):
                    MAX7219_write(fd, col + 1, NUMBER_CODE[num][col])
                    time.sleep(0.1)
            elif input_str.isalpha() and input_str.isupper() and len(input_str) == 1:
                char = input_str
                for col in range(8):
                    MAX7219_write(fd, col + 1, ALPHABET_CODE[char][col])
                    time.sleep(0.1)
            elif input_str == 'Smile':
                smile_pattern = ALPHABET_CODE['Smile']
                for col in range(8):
                    MAX7219_write(fd, col + 1, smile_pattern[col])
                    time.sleep(0.1)
            elif input_str == 'Dance': 
                for _ in range(10):
                    for col in range(8):
                        MAX7219_write(fd, col + 1, ALPHABET_CODE['dance0'][col])
                    time.sleep(0.5)
                    for col in range(8):
                        MAX7219_write(fd, col + 1, ALPHABET_CODE['dance1'][col])
                    time.sleep(0.5)
            elif input_str == 'Angry': 
                angry_pattern = ALPHABET_CODE['angry']
                for col in range(8):
                    MAX7219_write(fd, col + 1, angry_pattern[col])
                    time.sleep(0.1)
            elif input_str == 'Good':
                good_pattern = ALPHABET_CODE['Good']
                for col in range(8):
                    MAX7219_write(fd, col + 1, good_pattern[col])
                    time.sleep(0.1)
            elif input_str == 'Nice':
                for _ in range(3):
                    for col in range(8):
                        MAX7219_write(fd, col + 1, ALPHABET_CODE['N'][col])
                    time.sleep(0.5)
                    for col in range(8):
                        MAX7219_write(fd, col + 1, ALPHABET_CODE['I'][col])
                    time.sleep(0.5)
                    for col in range(8):
                        MAX7219_write(fd, col + 1, ALPHABET_CODE['C'][col])
                    time.sleep(0.5)
                    for col in range(8):
                        MAX7219_write(fd, col + 1, ALPHABET_CODE['E'][col])
                    time.sleep(0.5)
            elif input_str == 'Emotion':
                for _ in range (6):
                    for col in range(8):
                        MAX7219_write(fd, col + 1, ALPHABET_CODE['Smile'][col])
                    time.sleep(0.5)
                    for col in range(8):
                        MAX7219_write(fd, col + 1, ALPHABET_CODE['angry'][col])
                    time.sleep(0.5)
            else:
                   print("Invalid input. Please enter a number (0-9), an uppercase letter (A-Z), 'Smile', 'Dance', 'Angry', 'Good', 'Nice', 'Emotion'.")
 
    except KeyboardInterrupt:
        os.close(fd)
    finally:
        os.close(fd)
 
if __name__ == "__main__":
    main()
```

#### ขั้นตอนที่ 4. ผลลัพธ์การทำงาน
รันโค้ดด้วยคำสั่งต่อไปนี้
```
$ python3 dot_matrix_test.py
```
สคริปต์นี้เริ่มต้นการทำงานของจอแสดงผลดอตเมทริกซ์ MAX7219 ที่เชื่อมต่อผ่าน SPI และแจ้งให้ป้อนค่า รูปแบบที่แสดงบนเมทริกซ์ LED ขนาด 8x8 จะขึ้นอยู่กับค่าที่ป้อน

เมื่อเรียกใช้สคริปต์ คุณจะเห็น:
```
Enter a number, an uppercase letter (0-9, A-Z), 'Smile', 'Dance', 'Angry', 'Good', 'Nice', 'Emotion':
```
ตัวอย่าง:
- การป้อน A จะแสดงตัวอักษร A
- การป้อน Smile จะแสดงรูปแบบหน้ายิ้ม
- การป้อน Dance จะเรียกใช้แอนิเมชันการเต้นแบบสลับกัน
- การป้อน Nice จะแสดงแอนิเมชันตัวอักษร N-I-C-E ตามลำดับ

หากต้องการหยุดสคริปต์ ให้กด **[Ctrl+C]**
เมื่อสิ้นสุดการทำงาน อุปกรณ์ SPI จะถูกปิดอย่างปลอดภัย และเมทริกซ์ LED จะหยุดอัปเดต

**หมายเหตุ**: โปรดตรวจสอบว่ามี /dev/spidev3.0 อยู่ และการเดินสายตรงกับตารางการแมปพิน นอกจากนี้ ให้จ่ายไฟให้โมดูล MAX7219 ด้วยแหล่งจ่ายไฟ 5V ที่เสถียร

<br/><br/><br/><br/>

## 7.4 PWM
---
Pulse Width Modulation (PWM) ใช้ควบคุมอุปกรณ์ เช่น LED มอเตอร์ และบัซเซอร์ โดยการปรับความกว้างของสัญญาณพัลส์ D3-G รองรับ PWM ผ่านอินเทอร์เฟซ sysfs ใน Linux

### 7.4.1 การควบคุมความสว่างของ LED
---
ตัวอย่างนี้สาธิตการควบคุมความสว่างของ LED โดยใช้ PWM บน D3-G

#### ขั้นตอนที่ 1. ข้อกำหนดด้านฮาร์ดแวร์
- บอร์ด D3-G (x1)
- LED (x1)
- สายจัมเปอร์ผู้-เมีย (x2)
- เบรดบอร์ด
- อะแดปเตอร์จ่ายไฟ DC 5V (x1)
- สายซีเรียล USB to TTL (x1)

#### ขั้นตอนที่ 2. ตัวอย่างวงจร
- LED
    - พิน (+) ของ LED เชื่อมต่อกับพินหมายเลข 89 บนบอร์ด D3-G
    - พิน (-) ของ LED เชื่อมต่อกับพิน GND บนบอร์ด D3-G

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20D3-G/Software/led.png"></p>
<p align="center"><strong>รูปที่ 7.12 แผนผังวงจร LED ของ D3-G  </strong></p>

##### ขั้นตอนที่ 2.1 การแมปพิน
ตารางต่อไปนี้แสดงการแมปพิน

<div align="center">
  <p><strong>ตารางที่ 7.12 การแมปพินของ LED D3-G</strong></p>
  <table>
      <tr>
          <th colspan="3">ชื่อพิน</th>
          <th>D3-G</th>
          <th>GPIO</th>
      </tr>
      <tr>
          <td colspan="3">( + )</td>
          <td>12</td>
          <td>89</td>
      </tr>
      <tr>
          <td colspan="3">( – )</td>
          <td>14</td>
          <td>GND</td>
      </tr>
  </table>
</div>

#### ขั้นตอนที่ 3. วิธีการดำเนินการ
หากต้องการใช้งาน LED (PWM) ที่เชื่อมต่อกับ GPIO89 บนบอร์ด D3-G ให้เรียกใช้โค้ดต่อไปนี้:
```
import time

PWM_CHIP = "pwmchip0"
PWM_CHANNEL = "pwm0"
PWM_PATH = f"/sys/class/pwm/{PWM_CHIP}/{PWM_CHANNEL}"
EXPORT_PATH = f"/sys/class/pwm/{PWM_CHIP}/export"
UNEXPORT_PATH = f"/sys/class/pwm/{PWM_CHIP}/unexport"

PERIOD = 1000000  # 1ms = 1kHz
STEP = 10000
SLEEP = 0.01

def pwm_setup():
    try:
        with open(EXPORT_PATH, "w") as f:
            f.write("0")
    except Exception:
        pass  # Already exported
    time.sleep(0.1)

    with open(f"{PWM_PATH}/period", "w") as f:
        f.write(str(PERIOD))
        f.flush()

    with open(f"{PWM_PATH}/enable", "w") as f:
        f.write("1")
        f.flush()

def pwm_cleanup():
    try:
        with open(f"{PWM_PATH}/enable", "w") as f:
            f.write("0")
            f.flush()
        with open(UNEXPORT_PATH, "w") as f:
            f.write("0")
    except Exception as e:
        print("PWM cleanup failed:", e)

try:
    pwm_setup()
    print("Starting LED PWM control (press Ctrl+C to stop)")

    while True:
        for duty in range(0, PERIOD, STEP):
            with open(f"{PWM_PATH}/duty_cycle", "w") as f:
                f.write(str(min(duty, PERIOD - 1)))
                f.flush()
            time.sleep(SLEEP)

        for duty in range(PERIOD, 0, -STEP):
            with open(f"{PWM_PATH}/duty_cycle", "w") as f:
                f.write(str(min(duty, PERIOD - 1)))
                f.flush()
            time.sleep(SLEEP)

except KeyboardInterrupt:
    print("\nStopped by user.")

finally:
    pwm_cleanup()
    print("PWM disabled and cleaned up.")
```

#### ขั้นตอนที่ 4. ผลลัพธ์การทำงาน
รันโค้ดด้วยคำสั่งต่อไปนี้
```
$ python3 led_pwm.py
```
สคริปต์นี้เริ่มต้นการทำงานของ PWM บนพินของ LED และปรับความสว่างของ LED ให้เพิ่มขึ้นและลดลงอย่างต่อเนื่อง

เมื่อเรียกใช้สคริปต์แล้ว คุณจะเห็นผลลัพธ์ดังนี้:
```
Starting LED PWM control (press Ctrl+C to stop)
```
LED จะค่อย ๆ สว่างขึ้นแล้วหรี่ลงซ้ำ ๆ เพื่อจำลองเอฟเฟกต์ "การหายใจ"

หากต้องการหยุดสคริปต์ ให้กด **[Ctrl+C]**

**หมายเหตุ**: โปรดตรวจสอบว่าช่องสัญญาณ PWM ยังไม่ถูกใช้งานอยู่ และ D3-G รองรับฮาร์ดแวร์ PWM บน GPIO ที่เลือก หาก PWM ไม่ทำงาน ให้ตรวจสอบการตั้งค่า export, period และ duty_cycle ใน /sys/class/pwm/

<br/><br/><br/><br/>

### 7.4.2 มอเตอร์เซอร์โวขนาดเล็ก
---
มอเตอร์เซอร์โวขนาดเล็กสามารถใช้ควบคุมการเคลื่อนที่เชิงมุมอย่างแม่นยำ โดยอาศัยสัญญาณ Pulse Width Modulation (PWM) ผ่าน GPIO
หัวข้อนี้สาธิตวิธีเชื่อมต่อและควบคุมมอเตอร์เซอร์โวขนาดเล็กโดยใช้ D3-G

#### ขั้นตอนที่ 1. ข้อกำหนดด้านฮาร์ดแวร์
- บอร์ด D3-G (x1)
- มอเตอร์เซอร์โว (x1)
- สายจัมเปอร์ผู้-เมีย (x3)
- อะแดปเตอร์จ่ายไฟ DC 5V (x1)
- สายซีเรียล USB to TTL (x1)

#### ขั้นตอนที่ 2. ตัวอย่างวงจร
- มอเตอร์เซอร์โว
    - พิน VCC ของมอเตอร์เซอร์โวเชื่อมต่อกับ 5V บนบอร์ด D3-G
    - พิน GND ของมอเตอร์เซอร์โวเชื่อมต่อกับ GND บนบอร์ด D3-G
    - พิน SIG ของมอเตอร์เซอร์โวเชื่อมต่อกับพินหมายเลข 89 บนบอร์ด D3-G

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20D3-G/Software/motor_circuit.png"p>
<p align="center"><strong>รูปที่ 7.13 แผนผังวงจรมอเตอร์เซอร์โวของ D3-G  </strong></p>

##### ขั้นตอนที่ 2.1 การแมปพิน
ตารางต่อไปนี้แสดงการแมปพิน

<div align="center">
  <p><strong>ตารางที่ 7.13 การแมปพินของมอเตอร์เซอร์โว D3-G</strong></p>
  <table>
      <tr>
          <th colspan="3">ชื่อพิน</th>
          <th>D3-G</th>
          <th>GPIO</th>
      </tr>
      <tr>
          <td colspan="3">VCC</td>
          <td>2</td>
          <td>5V</td>
      </tr>
      <tr>
          <td colspan="3">GND</td>
          <td>20</td>
          <td>GND</td>
      </tr>
      <tr>
          <td colspan="3">SIG</td>
          <td>12</td>
          <td>89</td>
      </tr>
  </table>
</div>

#### ขั้นตอนที่ 3. วิธีการดำเนินการ
สคริปต์ Python ต่อไปนี้แสดงวิธีควบคุมมอเตอร์เซอร์โวขนาดเล็กโดยตรงด้วย PWM ผ่านอินเทอร์เฟซ sysfs บน D3-G วิธีนี้ไม่จำเป็นต้องใช้ไลบรารีภายนอก และให้การควบคุมตำแหน่งตามมุมได้อย่างละเอียด
```
import time
import os

PWM_CHIP = "pwmchip0"
PWM_CHANNEL = "pwm0"
PWM_PATH = f"/sys/class/pwm/{PWM_CHIP}/{PWM_CHANNEL}"
EXPORT_PATH = f"/sys/class/pwm/{PWM_CHIP}/export"
UNEXPORT_PATH = f"/sys/class/pwm/{PWM_CHIP}/unexport"

PERIOD = 20_000_000  # 20ms (50Hz)

def angle_to_duty(angle):
    pulse_width = 1_000_000 + (angle / 180) * 1_000_000
    return int(pulse_width)

def pwm_setup():
    if not os.path.exists(PWM_PATH):
        with open(EXPORT_PATH, "w") as f:
            f.write("0")
        time.sleep(0.1)
    with open(f"{PWM_PATH}/period", "w") as f:
        f.write(str(PERIOD))
    with open(f"{PWM_PATH}/enable", "w") as f:
        f.write("1")

def pwm_set_angle(angle):
    duty = angle_to_duty(angle)
    with open(f"{PWM_PATH}/duty_cycle", "w") as f:
        f.write(str(duty))

def pwm_cleanup():
    try:
        with open(f"{PWM_PATH}/enable", "w") as f:
            f.write("0")
        with open(UNEXPORT_PATH, "w") as f:
            f.write("0")
    except Exception as e:
        print("PWM cleanup failed:", e)

if __name__ == "__main__":
    pwm_setup()

    try:
        while True:
            user_input = input("Enter 1 (CW) or 0 (CCW), q to quit: ").strip()
            if user_input == 'q':
                break
            elif user_input == '1':
                pwm_set_angle(180)  
                time.sleep(0.5)
            elif user_input == '0':
                pwm_set_angle(0)   
                time.sleep(0.5)
            else:
                print("Invalid input. Use 0, 1, or q.")
    except KeyboardInterrupt:
        print("\nInterrupted by user.")
    finally:
        pwm_cleanup()
        print("PWM cleaned up.")
```

#### ขั้นตอนที่ 4. ผลลัพธ์การทำงาน
รันโค้ดด้วยคำสั่งต่อไปนี้
```
$ python3 motor_test.py
```
สคริปต์นี้ใช้ PWM ควบคุมมอเตอร์เซอร์โวขนาดเล็ก โดยปรับดิวตี้ไซเคิลตามมุมเป้าหมาย
เมื่อเรียกใช้แล้ว ระบบจะแจ้งข้อความดังนี้:
```
Enter 1 (CW) or 0 (CCW), q to quit:
```
การป้อน 1 จะหมุนเซอร์โวตามเข็มนาฬิกาไปที่ 180° และการป้อน 0 จะหมุนเซอร์โวทวนเข็มนาฬิกาไปที่ 0° คุณสามารถทำซ้ำได้ตามต้องการ

หากต้องการหยุดสคริปต์ ให้ป้อน **[q]** หรือกด **[Ctrl+C]** จากนั้นสคริปต์จะปิดใช้งานและ unexport ช่องสัญญาณ PWM

**หมายเหตุ**: โปรดตรวจสอบว่ามอเตอร์เซอร์โวของคุณรองรับสัญญาณ PWM ที่ 50 Hz และทำงานในช่วงพัลส์ดิวตี้ 1 ms ถึง 2 ms เพื่อการใช้งานที่ปลอดภัย
