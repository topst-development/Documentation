## โมดูลกล้องที่รองรับ
<div align="center">
    <table>
        <tr>
            <td colspan="8" align="center"><strong>บอร์ด</strong></td>
            <td align="center"><strong>รุ่น</strong></td>
            <td align="center"><strong>เซ็นเซอร์</strong></td>
            <td align="center"><strong>ความละเอียดของเซ็นเซอร์</strong></td>
            <td align="center"><strong>ความละเอียดเริ่มต้น</strong></td>
            <td align="center"><strong>อัตราเฟรม</strong></td>
            <td align="center"><strong>พาธวิดีโอเริ่มต้น</strong></td>
            <td align="center"><strong>หมายเหตุ</strong></td>
        </tr>
        <tr>
            <td rowspan="4" align="center"><strong>D3-G</strong></td>
            <td colspan="8">Arducam OV5647</td>
            <td>OV5647</td>
            <td>2592x1944 พิกเซล(5MP)</td>
            <td>1296x972</td>
            <td>30FPS</td>
            <td>/dev/video0</td>
            <td>กล้องที่ถูกเลือกโดยค่าเริ่มต้น</td>
        </tr>
        <tr>
            <td colspan="8">Raspberry Pi Camera v1</td>
            <td>OV5647</td>
            <td>2592x1944 พิกเซล(5MP)</td>
            <td>1296x972</td>
            <td>30FPS</td>
            <td>/dev/video0</td>
            <td>กล้องที่ถูกเลือกโดยค่าเริ่มต้น</td>
        </tr>
        <tr>
            <td colspan="8">Raspberry Pi Camera v2</td>
            <td>IMX219</td>
            <td>3280x2464 พิกเซล(8MP)</td>
            <td>1640x1232</td>
            <td>30FPS</td>
            <td>/dev/video0</td>
            <td>ปิดใช้งานโดยค่าเริ่มต้น โปรดดูคู่มือด้านล่างเพื่อเปิดใช้งาน</td>
        </tr>
        <tr>
            <td colspan="8">SEKONIX CXD5700</td>
            <td>CXD5700</td>
            <td>1920x1080 พิกเซล(2MP)</td>
            <td>1920x1080</td>
            <td>30FPS</td>
            <td>/dev/video0,1,2,3</td>
            <td>ปิดใช้งานโดยค่าเริ่มต้น โปรดดูคู่มือด้านล่างเพื่อเปิดใช้งาน</td>
        </tr>
        <tr>
            <td rowspan="4" align="center"><strong>AI-G</strong></td>
            <td colspan="8">Arducam OV5647</td>
            <td>OV5647</td>
            <td>2592x1944 พิกเซล(5MP)</td>
            <td>1296x972</td>
            <td>30FPS</td>
            <td>/dev/video2</td>
            <td>กล้องที่ถูกเลือกโดยค่าเริ่มต้น</td>
        </tr>
        <tr>
            <td colspan="8">Raspberry Pi Camera v1</td>
            <td>OV5647</td>
            <td>2592x1944 พิกเซล(5MP)</td>
            <td>1296x972</td>
            <td>30FPS</td>
            <td>/dev/video2</td>
            <td>กล้องที่ถูกเลือกโดยค่าเริ่มต้น</td>
        </tr>
        <tr>
            <td colspan="8">Raspberry Pi Camera v2</td>
            <td>IMX219</td>
            <td>3280x2464 พิกเซล(8MP)</td>
            <td>1640x1232</td>
            <td>30FPS</td>
            <td>/dev/video2</td>
            <td>ปิดใช้งานโดยค่าเริ่มต้น โปรดดูคู่มือด้านล่างเพื่อเปิดใช้งาน</td>
        </tr>
        <tr>
            <td colspan="8">SEKONIX CXD5700</td>
            <td>CXD5700</td>
            <td>1920x1080 พิกเซล(2MP)</td>
            <td>1920x1080</td>
            <td>30FPS</td>
            <td>/dev/video0,1,2</td>
            <td>ปิดใช้งานโดยค่าเริ่มต้น โปรดดูคู่มือด้านล่างเพื่อเปิดใช้งาน</td>
        </tr>
    </table>
</div>

# 1. บทนำ
คู่มือนี้จัดทำขึ้นเพื่อช่วยให้วิศวกรสามารถเริ่มใช้งานอินพุตกล้องบนแพลตฟอร์ม TOPST D3-G และ AI-G ได้อย่างรวดเร็ว และดำเนินการตรวจสอบเบื้องต้นสำหรับภาระงานด้าน AI vision ได้อย่างรวดเร็ว โดยมีเป้าหมายเพื่อลดความซับซ้อนของการตั้งค่าเริ่มต้น ซึ่งรวมถึงการเชื่อมต่อฮาร์ดแวร์ การกำหนดค่า device tree ไดรเวอร์ และการเตรียมไปป์ไลน์ พร้อมทั้งให้แนวทางที่ชัดเจนและทำซ้ำได้ ตั้งแต่การเปิดเครื่องไปจนถึงเฟรมวิดีโอแรก และท้ายที่สุดคือการอนุมานครั้งแรก

## 1.1 ขอบเขต
- **อินเทอร์เฟซที่รองรับ:** MIPI CSI-2, GMSL (ใช้ SerDes), USB UVC
- **ส่วนประกอบซอฟต์แวร์:** การกำหนดค่า BSP บนพื้นฐาน Yocto, device tree overlay, V4L2, GStreamer, OpenCV และการผสานรวมกับ SDK ของ D3-G และ AI-G
- **กรณีการใช้งานที่เกี่ยวข้อง:** หุ่นยนต์ โดรน และงานระบบอัตโนมัติในภาคอุตสาหกรรม เช่น การตรวจสอบคุณภาพ การเฝ้าระวังความปลอดภัย และการติดตามวัตถุ
- **รายการที่อยู่นอกขอบเขต:** การปรับจูน ISP ของกล้อง ขั้นตอนการสอบเทียบขั้นสูง (สเตอริโอ/IMU) และเฟรมเวิร์กแอปพลิเคชันแบบครบวงจร

## 1.2 กลุ่มผู้อ่านเป้าหมาย
- วิศวกรระบบฝังตัวและวิศวกร AI ที่ผสานรวมกล้องเข้ากับแพลตฟอร์ม D3-G หรือ AI-G สำหรับการพัฒนา PoC หรือโครงการนำร่อง
- ผู้ผสานรวมระบบที่ติดตั้งหรือตรวจสอบระบบซึ่งพึ่งพาไปป์ไลน์แบบหลายกล้อง
- ผู้สอนและผู้ใช้ในห้องปฏิบัติการที่ต้องการสภาพแวดล้อมฝึกปฏิบัติที่ทำซ้ำได้สำหรับการอบรมและการทดลอง

## 1.3 โครงสร้างของคู่มือนี้
- **การเชื่อมต่อฮาร์ดแวร์:** การจัดเรียงพินของขั้วต่อ การกำหนดค่าเลน ข้อกำหนดด้านแหล่งจ่ายไฟและกราวด์ แนวทางการจัดการสายเคเบิล และแผนผังการเดินสายอ้างอิง
- **การกำหนดค่าซอฟต์แวร์:** การตั้งค่า BSP ซึ่งรวมถึงไดรเวอร์และการกำหนดค่า device tree พร้อมด้วยวิธีตรวจสอบอุปกรณ์ผ่าน udev และ V4L2
- **ไปป์ไลน์และตัวอย่าง:** คำสั่งและสคริปต์ GStreamer และ OpenCV สำหรับการแสดงตัวอย่างและการบันทึกภาพแบบกล้องเดี่ยวและหลายกล้อง
- **การแก้ไขปัญหา:** ปัญหาที่พบบ่อย รูปแบบข้อความ dmesg ทั่วไป เคล็ดลับการตรวจสอบ I²C ปัญหาที่เกี่ยวข้องกับไทมิ่ง และวิธีตรวจสอบประสิทธิภาพ

## 1.4 ข้อกำหนดเบื้องต้น
- **ฮาร์ดแวร์:** บอร์ด TOPST D3-G หรือ AI-G โมดูลกล้องที่รองรับ และสายเคเบิล/อะแดปเตอร์ที่จำเป็น (MIPI FPC, สายโคแอกเชียลสำหรับ GMSL, USB 3.0 เป็นต้น)
- **เครื่องมือบนโฮสต์:** การเข้าถึงคอนโซลอนุกรม ไคลเอนต์ SSH และยูทิลิตีพื้นฐานสำหรับการบิลด์/ดีบัก
- **พื้นฐานทางเทคนิค:** ความคุ้นเคยกับการใช้งาน Linux shell ยูทิลิตี V4L2 และแนวคิดพื้นฐานของ device tree
- **อิมเมจ/SDK:** อิมเมจ BSP ของ D3-G, AI-G (เวอร์ชัน d3-g ≥ v1.3.0, เวอร์ชัน ai-g ≥1.1.0)
  

# 2. ภาพรวมอินเทอร์เฟซกล้อง
บทที่ 2 อธิบายประเภทของกล้องที่รองรับบนบอร์ด D3-G และ AI-G ตามลำดับ  
ตารางที่ 2.1 แสดงเมทริกซ์การรองรับของบอร์ดสำหรับแพลตฟอร์ม D3-G และ AI-G

<p align="center"><strong>ตารางที่ 2.1 เมทริกซ์การรองรับของบอร์ด</strong></p>
<div align="center">
    <table>
        <tr>
            <td colspan="3" align="center"><strong>รายการ</strong></td>
            <td align="center"><strong>D3-G</strong></td>
            <td align="center"><strong>AI-G</strong></td>
        </tr>
        <tr>
            <td colspan="3">การรองรับ OS</td>
            <td>Yocto, Ubuntu(desktop)</td>
            <td>Yocto, Ubuntu(Headless)</td>
        </tr>
        <tr>
            <td colspan="3">MIPI CSI-2</td>
            <td>2-4 เลน, 2.1 Gbps/เลน x2</td>
            <td>2-4 เลน, 1.5 Gbps/เลน x1</td>
        </tr>
        <tr>
            <td colspan="3">GMSL (SerDes)</td>
            <td>บอร์ดพ่วง TOPST 4ch SerDes</td>
            <td>บอร์ดพ่วง TOPST 4ch SerDes</td>
        </tr>
        <tr>
            <td colspan="3">USB (UVC)</td>
            <td>USB2.0/USB3.0 </td>
            <td>ไม่รองรับ</td>
        </tr>
    </table>
</div>

## 2.1 ภาพรวมกล้อง MIPI
กล้อง MIPI คือโมดูลกล้องที่ใช้เซ็นเซอร์ภาพ ซึ่งเชื่อมต่อโดยตรงกับโปรเซสเซอร์ผ่านมาตรฐาน **MIPI CSI-2 (Mobile Industry Processor Interface – Camera Serial Interface 2)** เป็นอินเทอร์เฟซกล้องที่ใช้กันแพร่หลายที่สุดในสมาร์ตโฟน บอร์ดระบบฝังตัว และระบบกล้องที่ใช้ AI โดยมีข้อดีคือใช้พลังงานต่ำ แบนด์วิดท์สูง และความหน่วงต่ำ  
โดยทั่วไปกล้อง MIPI CSI-2 จะส่งเอาต์พุตเซ็นเซอร์แบบ RAW Bayer ให้กับระบบโดยตรง โดยการประมวลผลสัญญาณภาพ (ISP) จะดำเนินการโดย ISP ภายใน SoC หรือโดย ISP ภายนอก ต่างจากกล้อง USB เซ็นเซอร์ MIPI จำเป็นต้องเริ่มต้นการทำงานผ่านการตั้งค่ารีจิสเตอร์ด้วย I2C และการตั้งค่าไปป์ไลน์ ISP แต่ในทางกลับกันก็ทำให้สามารถประมวลผลภาพคุณภาพสูงที่ใช้ประสิทธิภาพของเซ็นเซอร์ได้อย่างเต็มที่  
กล้อง MIPI ถูกใช้อย่างแพร่หลายในแพลตฟอร์มระบบฝังตัวด้วยเหตุผลดังต่อไปนี้
- **แบนด์วิดท์สูง:** ด้วยการกำหนดค่าแบบ 2 เลนหรือ 4 เลน กล้อง MIPI สามารถส่งข้อมูลความละเอียดสูง (4K ขึ้นไป) และอัตราเฟรมสูงได้อย่างเสถียร
- **การใช้พลังงานต่ำ:** ออกแบบมาสำหรับอุปกรณ์เคลื่อนที่และระบบฝังตัว จึงใช้พลังงานน้อยกว่าทางเลือกอื่นอย่างมีนัยสำคัญ
- **การควบคุมเซ็นเซอร์โดยตรง:** พารามิเตอร์ของเซ็นเซอร์ เช่น การเปิดรับแสง เกน และอัตราเฟรม สามารถควบคุมได้ผ่าน I2C ทำให้ปรับคุณภาพของภาพได้อย่างละเอียด
- **ความหน่วงต่ำ:** เนื่องจากข้อมูล RAW ถูกส่งโดยตรง กล้อง MIPI จึงเหมาะกับงานแบบเรียลไทม์ เช่น หุ่นยนต์และระบบวิชันสำหรับระบบฝังตัว
- **มีเซ็นเซอร์ให้เลือกหลากหลาย:** เซ็นเซอร์จำนวนมาก รวมถึงตระกูล Sony IMX (IMX219, IMX708 เป็นต้น) และตระกูล Omnivision OV สามารถใช้งานได้ภายใต้มาตรฐาน CSI-2 เดียวกัน  

กล้อง MIPI ใช้ขั้วต่อ เช่น สาย FFC แบบ **15 พิน (2 เลน)** หรือ **20 พิน (4 เลน)** และการกำหนดค่าเลนกับผังพินต้องตรงกับพอร์ต CSI ของบอร์ด  
บนระบบที่ใช้ Linux ต้องตั้งค่าไดรเวอร์ของเซ็นเซอร์ (รวมถึงการกำหนดค่า device tree) อย่างถูกต้อง เพื่อให้กล้องถูกตรวจพบเป็นอุปกรณ์ /dev/video* หรือโหนด Media Controller เมื่อตรวจพบแล้ว จะสามารถเข้าถึงการสตรีมวิดีโอผ่านเฟรมเวิร์ก V4L2 ได้  
ด้วยคุณลักษณะเหล่านี้ กล้อง MIPI จึงกลายเป็นอินเทอร์เฟซมาตรฐานโดยพฤตินัยสำหรับการประมวลผลภาพคุณภาพสูง การสตรีมที่มีความหน่วงต่ำ และแอปพลิเคชันวิชันในระบบฝังตัวที่ขับเคลื่อนด้วย AI

## 2.2 ภาพรวมกล้อง GMSL
กล้อง GMSL คือโมดูลกล้องแบบอนุกรมที่ส่งข้อมูลภาพ สัญญาณควบคุม และไฟเลี้ยงผ่านสายโคแอกเชียลหรือสายคู่บิดเกลียวหุ้มฉนวนเพียงเส้นเดียว โดยใช้มาตรฐาน Gigabit Multimedia Serial Link (GMSL) ต่างจากกล้อง MIPI ที่ต้องใช้การเชื่อมต่อ FFC ระยะสั้น GMSL ใช้คู่ซีเรียลไลเซอร์–ดีซีเรียลไลเซอร์ (SerDes) เพื่อส่งข้อมูลภาพ CSI-2 ได้ไกลหลายเมตร ทำให้สามารถติดตั้งกล้องในระยะไกลและทนต่อสัญญาณรบกวน  

ระบบ GMSL มีข้อดีหลายประการในสภาพแวดล้อมของระบบฝังตัวและยานยนต์
- **การส่งสัญญาณระยะไกล:** รองรับการส่งวิดีโอได้อย่างเสถียรบนสายยาวถึงประมาณ 15 ม. จึงเหมาะกับหุ่นยนต์และการติดตั้งเซ็นเซอร์บนยานพาหนะ
- **แบนด์วิดท์สูง:** GMSL1/2/3 สามารถรองรับสตรีม CSI-2 ระดับหลายกิกะบิต ทำให้ใช้งานความละเอียดสูงหรือการกำหนดค่าแบบหลายกล้องได้
- **Power over Coax (PoC):** ให้ทั้งไฟเลี้ยงและข้อมูลผ่านสายเส้นเดียว ช่วยลดจำนวนขั้วต่อและทำให้การเดินสายของระบบง่ายขึ้น
- **ความทนทานและภูมิคุ้มกันต่อ EMI:** สายโคแอกเชียลและการส่งสัญญาณแบบดิฟเฟอเรนเชียลทำให้ GMSL ทำงานได้อย่างเสถียรในสภาพแวดล้อมที่มีสัญญาณรบกวนทางไฟฟ้าสูง
- **การควบคุมเซ็นเซอร์แบบมาตรฐาน:** ดีซีเรียลไลเซอร์จะส่งต่อการสื่อสาร I2C ไปยังเซ็นเซอร์ ทำให้สามารถกำหนดค่าการเปิดรับแสง เกน และอัตราเฟรมได้ตามปกติ

เส้นทางของกล้อง GMSL โดยทั่วไปประกอบด้วยเซ็นเซอร์ภาพที่มีซีเรียลไลเซอร์ สายโคแอกเชียล ดีซีเรียลไลเซอร์ และสุดท้ายคือเอาต์พุต CSI-2 ไปยัง SoC บน Linux เมื่อ SerDes และเซ็นเซอร์ถูกกำหนดไว้อย่างถูกต้องในดีไวซ์ทรี กล้องจะปรากฏเป็นอุปกรณ์ V4L2 หรือ Media Controller ซึ่งคล้ายคลึงกับกล้อง MIPI มาตรฐานอย่างมาก แต่มีความยืดหยุ่นในการวางตำแหน่งและการออกแบบระบบมากกว่ามาก

## 2.3 ภาพรวมของกล้อง USB
กล้อง USB คืออุปกรณ์ถ่ายภาพดิจิทัลที่เชื่อมต่อกับระบบผ่านอินเทอร์เฟซ USB 2.0 หรือ USB 3.0 ข้อได้เปรียบสำคัญคือสามารถทำงานได้โดยไม่ต้องใช้ไดรเวอร์เฉพาะ เนื่องจากเป็นไปตามโปรโตคอลมาตรฐาน UVC (USB Video Class) เนื่องจากระบบปฏิบัติการส่วนใหญ่ ได้แก่ Linux, Windows และ macOS รองรับ UVC มาโดยกำเนิด ผู้ใช้จึงสามารถรับสตรีมวิดีโอได้ทันทีหลังจากเสียบกล้อง โดยไม่ต้องตั้งค่าเพิ่มเติมใด ๆ
  
กล้อง USB ถูกใช้งานอย่างแพร่หลายในแพลตฟอร์มฝังตัวด้วยเหตุผลดังต่อไปนี้
- **ความสามารถแบบพลักแอนด์เพลย์:** ต่างจากเซ็นเซอร์ MIPI กล้อง USB ไม่จำเป็นต้องมีการเริ่มต้นเซ็นเซอร์ การกำหนดค่ารีจิสเตอร์ I2C หรือการตั้งค่าไปป์ไลน์ ISP สามารถจับภาพวิดีโอได้ทันทีเมื่อเชื่อมต่อ
- **ความเข้ากันได้สูง:** กล้อง USB ส่วนใหญ่เป็นไปตามข้อมูลจำเพาะ UVC จึงทำงานในลักษณะเดียวกันโดยไม่ขึ้นกับผู้ผลิตหรือรุ่น
- **รองรับความละเอียดและรูปแบบที่หลากหลาย:** รูปแบบทั่วไป เช่น MJPEG, YUYV และ NV12 มีให้ใช้งานอย่างแพร่หลาย
- **เชื่อมต่อและเดินสายได้ง่าย:** สาย USB ช่วยให้การเดินสายง่ายขึ้นและรองรับระยะทางที่ยาวขึ้น ซึ่งมักอยู่ที่หลายเมตร
- **เหมาะสำหรับการพัฒนาระบบฝังตัว:** ปัญหาที่เกี่ยวข้องกับไดรเวอร์มีน้อยกว่า ทำให้สร้างต้นแบบได้รวดเร็วยิ่งขึ้น

ในระบบที่ใช้ Linux กล้อง USB จะถูกตรวจพบโดยอัตโนมัติและแสดงเป็นโหนด /dev/video* การจับภาพและการควบคุมวิดีโอสามารถทำได้ด้วยเครื่องมือมาตรฐาน เช่น v4l2-ctl, ffmpeg และ GStreamer  
กล้อง USB จำนวนมากมี ISP ในตัวซึ่งจัดการการประมวลผลภาพภายใน เช่น การปรับสมดุลแสงขาวอัตโนมัติ การปรับค่าแสงอัตโนมัติ และการแก้ไขสี ทำให้ได้คุณภาพของภาพที่เสถียรแม้บนบอร์ดที่ไม่มี ISP ภายนอก ด้วยคุณลักษณะเหล่านี้ กล้อง USB จึงกลายเป็นหนึ่งในโซลูชันกล้องที่ง่ายและอเนกประสงค์ที่สุดในด้านต่าง ๆ เช่น การทดสอบ การพัฒนา Linux แบบฝังตัว วิทยาการหุ่นยนต์ และการสร้างต้นแบบอย่างรวดเร็ว

## 2.4 ประเภทกล้องที่ใช้งานได้บน D3-G
แพลตฟอร์ม TOPST D3-G รองรับกล้องประเภทเดียวกันทั้งในสภาพแวดล้อม Yocto และ Ubuntu อินเทอร์เฟซกล้องที่ใช้งานได้ ได้แก่ USB, MIPI, GMSL โดยมีความแตกต่างของการตั้งค่าเล็กน้อยขึ้นอยู่กับอินเทอร์เฟซที่ใช้  
1. **กล้อง MIPI**  
TOPST D3-G มีพอร์ต MIPI CSI สองพอร์ต ทำให้สามารถต่อกล้อง MIPI ได้หนึ่งตัวต่อหนึ่งพอร์ต อินเทอร์เฟซ MIPI CSI รองรับขั้วต่อสองรูปแบบ
    - **15-pin(2-Lane):** เหมาะสำหรับเซ็นเซอร์ที่ใช้แบนด์วิดท์ต่ำ เช่น OV5647 หรือ IMX219
    - **20-pin (4-Lane):** มีไว้สำหรับเซ็นเซอร์ความละเอียดสูงหรืออัตราเฟรมสูง
2. **กล้อง GMSL**  
กล้อง GMSL รองรับการส่งสัญญาณระยะไกลและมักใช้ในงานยานยนต์และงานอุตสาหกรรม หากต้องการใช้ GMSL บน TOPST D3-G จำเป็นต้องมีส่วนประกอบดังต่อไปนี้
    1. เชื่อมต่อพอร์ต **20-pin MIPI CSI (4-Lane)** เข้ากับ **TOPST MIPI Gender Board**
    2. ติดตั้งบอร์ด **Deserializer (Des)** เข้ากับ Gender Board
    3. เชื่อมต่อกล้อง GMSL ได้สูงสุดสี่ตัวเข้ากับบอร์ด Des โดยใช้สาย Fakra
3. **กล้อง USB**  
กล้อง USB เป็นวิธีเริ่มต้นใช้งานที่ง่ายที่สุด เมื่อเชื่อมต่อเข้ากับพอร์ต USB 2.0 หรือ USB 3.0 พอร์ตใดก็ได้บนบอร์ด กล้องจะถูกรับรู้โดยอัตโนมัติและสามารถใช้งานได้โดยไม่ต้องตั้งค่าเพิ่มเติม  
หากอุปกรณ์เป็นกล้อง UVC ที่รองรับ V4L2 คุณสามารถตรวจสอบการตรวจพบได้ด้วยคำสั่งต่อไปนี้  
    ``` 
    v4l2-ctl --list-devices
    ```

## 2.4 ประเภทกล้องที่ใช้งานได้บน D3-G
แพลตฟอร์ม TOPST AI-G ก็รองรับอินเทอร์เฟซอินพุตกล้องหลายแบบเช่นกัน แต่การกำหนดค่าโดยรวมง่ายกว่าบน D3-G และได้รับการปรับให้เหมาะกับภาระงาน AI ประสิทธิภาพสูง ที่สำคัญคือแพลตฟอร์มนี้ไม่รองรับกล้อง USB มีเพียงอินพุต MIPI, GMSL เท่านั้นที่ใช้งานได้  
1. **กล้อง MIPI**  
TOPST D3-G มีพอร์ต MIPI CSI สองพอร์ต ทำให้สามารถต่อกล้อง MIPI ได้หนึ่งตัวต่อหนึ่งพอร์ต อินเทอร์เฟซ MIPI CSI รองรับขั้วต่อสองรูปแบบ
    - **15-pin(2-Lane):** เหมาะสำหรับเซ็นเซอร์ที่ใช้แบนด์วิดท์ต่ำ เช่น OV5647 หรือ IMX219
    - **20-pin (4-Lane):** มีไว้สำหรับเซ็นเซอร์ความละเอียดสูงหรืออัตราเฟรมสูง
2. **กล้อง GMSL**  
กล้อง GMSL รองรับการส่งสัญญาณระยะไกลและมักใช้ในงานยานยนต์และงานอุตสาหกรรม หากต้องการใช้ GMSL บน TOPST D3-G จำเป็นต้องมีส่วนประกอบดังต่อไปนี้
    1. เชื่อมต่อพอร์ต **20-pin MIPI CSI (4-Lane)** เข้ากับ **TOPST MIPI Gender Board**
    2. ติดตั้งบอร์ด **Deserializer (Des)** เข้ากับ Gender Board
    3. เชื่อมต่อกล้อง GMSL ได้สูงสุดสี่ตัวเข้ากับบอร์ด Des โดยใช้สาย Fakra

# 3. คู่มือการเชื่อมต่อกล้อง
บทที่ 3 อธิบายวิธีเชื่อมต่อกล้องเข้ากับบอร์ด D3-G และ AI-G  
หัวข้อนี้ช่วยให้มั่นใจว่าบอร์ดและกล้องเชื่อมต่อกันอย่างถูกต้อง เพื่อให้กล้องทำงานได้อย่างเสถียร โปรดปฏิบัติตามคู่มือด้านล่างเพื่อเชื่อมต่อกล้องที่ท่านต้องการใช้งาน

## 3.1 การเชื่อมต่อกล้องเข้ากับ D3-G
โปรดปฏิบัติตามคู่มือด้านล่างสำหรับคำแนะนำในการเชื่อมต่อกล้อง MIPI CSI-2, GMSL และ USB เข้ากับ D3-G  

### 3.1.1 กล้อง MIPI CSI-2
รูปที่ 3.1 แสดงขั้วต่อ MIPI CSI บน D3-G โดย D3-G รองรับ MIPI CSI จำนวน 2 ช่องสัญญาณ ซึ่งแต่ละช่องกำหนดค่าเป็นอินเทอร์เฟซแบบ 2-lane อินเทอร์เฟซแบบ 4-lane เป็นตัวเลือกเสริมและต้องใช้ขั้วต่อแบบ 20-pin แทนขั้วต่อแบบ 15-pin สำหรับข้อมูลเกี่ยวกับพิน โปรดดู D3-G Hardware-User Guide

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/accessories/Camera/3.1%20MIPI%20CSI%20Connector%20on%20D3-G.png"></p>
<p align="center"><strong>รูปที่ 3.1 ขั้วต่อ MIPI CSI บน D3-G</strong></p>

เมื่อเชื่อมต่อกล้อง MIPI ให้ใช้ FFC (Flat Flexible Cable) โปรดดูรูปที่ 3.2 และ 3.3 สำหรับชนิดและทิศทางของสายที่ถูกต้อง

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/accessories/Camera/3.2%20FFC%20Type.png"></p>
<p align="center"><strong>รูปที่ 3.2 ชนิดของ FFC</strong></p>

สาย FFC เป็นชนิด 1.0 mm แบบ 15-pin และด้านหนึ่งต้องมีเครื่องหมายสีที่แตกต่าง (สีน้ำเงินหรือสีเทา) สายควรเสียบโดยใช้ทิศทางแบบ B-Forward Direction โปรดดูรูปที่ 3.2 สำหรับชนิดของ FFC

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/accessories/Camera/3.3%20An%20example%20of%20an%20FFC%20connected%20to%20the%20D3-G%20MIPI0%2015-pin%20Connector.png"></p>
<p align="center"><strong>รูปที่ 3.3 ตัวอย่างการเชื่อมต่อ FFC เข้ากับขั้วต่อ D3-G MIPI0 แบบ 15-pin</strong></p>

ตรวจสอบให้แน่ใจว่าหน้าสัมผัสสีเงินทั้ง 15 จุดบน FFC ตรงกับหน้าสัมผัสสีเงินทั้ง 15 จุดภายในขั้วต่อ MIPI ของ D3-G  
วิธีการเชื่อมต่อแบบเดียวกันนี้ใช้ได้เมื่อใช้ขั้วต่อ MIPI1 โปรดเชื่อมต่อในลักษณะเดียวกับขั้วต่อ MIPI0

### 3.1.2 กล้อง GMSL
กล้อง GMSL ใช้สาย Fakra จึงไม่สามารถเชื่อมต่อเข้ากับบอร์ด D3-G ได้โดยตรง แต่ต้องเชื่อมต่อผ่านบอร์ด Deserializer (Des) และ TOPST MIPI Gender Board ก่อนที่จะเชื่อมต่อกับ D3-G  
โครงสร้างการเชื่อมต่อมีดังนี้  

<p align="center"><strong>< D3-G > ↔ < TOPST MIPI Gender Board > ↔ < Des Board > ↔ < GMSL Camera ></strong></p>

กล้อง GMSL จำเป็นต้องใช้ TOPST MIPI Gender Board ซึ่งต้องเชื่อมต่อผ่านขั้วต่อ MIPI แบบ 20-pin ตัวอย่างเช่น หากท่านวางแผนจะใช้กล้อง GMSL สี่ตัว ท่านต้องเชื่อมต่อโดยใช้อินเทอร์เฟซ MIPI แบบ 20-pin ดังแสดงในรูปที่ 3.4

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/accessories/Camera/3.4%2020-pin%20MIPI0%20Connector.png"></p>
<p align="center"><strong>รูปที่ 3.4 ขั้วต่อ MIPI0 แบบ 20-pin</strong></p>  

1. การเชื่อมต่อบอร์ด D3-G เข้ากับ TOPST MIPI Gender Board  
    สาย FFC เป็นชนิด 1.0 mm แบบ 20-pin และด้านหนึ่งต้องมีเครื่องหมายสีที่แตกต่าง (สีน้ำเงินหรือสีเทา) สายควรเสียบโดยใช้ทิศทางแบบ A-Forward Direction โปรดดูรูปที่ 3.5 สำหรับชนิดของ FFC  
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/accessories/Camera/3.2%20FFC%20Type.png"></p>
    <p align="center"><strong>รูปที่ 3.5 ชนิดของ FFC</strong></p>
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/accessories/Camera/3.6%20Anexample%20of%20an%20FFC%20connected%20to%20the%20D3-G%20MIPI0%2020-pin%20Connector.png"></p>
    <p align="center"><strong>รูปที่ 3.6 ตัวอย่างการเชื่อมต่อ FFC เข้ากับขั้วต่อ D3-G MIPI0 แบบ 20-pin</strong></p> 
    ตรวจสอบให้แน่ใจว่าหน้าสัมผัสสีเงินทั้ง 20 จุดบน FFC ตรงกับหน้าสัมผัสสีเงินทั้ง 20 จุดภายในขั้วต่อ MIPI ของ D3-G
    วิธีการเชื่อมต่อแบบเดียวกันนี้ใช้ได้เมื่อใช้ขั้วต่อ MIPI1 โปรดเชื่อมต่อในลักษณะเดียวกับขั้วต่อ MIPI0
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/accessories/Camera/3.7%20An%20example%20of%20an%20FFC%20connected%20th%20toe%20TOPST%20MIPI%20Gender%20Board%20MIPI%20Connector.png"></p>
    <p align="center"><strong>รูปที่ 3.7 ตัวอย่างการเชื่อมต่อ FFC เข้ากับขั้วต่อ MIPI ของ TOPST MIPI Gender Board</strong></p>
2. การเชื่อมต่อบอร์ด Deserializer เข้ากับ MIPI Gender Board  
    ประกอบขั้วต่อ JH2 บน MIPI Gender Board เข้ากับขั้วต่อ JH1 ที่อยู่ด้านล่างของบอร์ด SerDes
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/accessories/Camera/3.8%20JH2%20Connector.png"></p>
    <p align="center"><strong>รูปที่ 3.8 ขั้วต่อ JH2</strong></p>
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/accessories/Camera/3.9%20JH1%20Connector.png"></p>
    <p align="center"><strong>รูปที่ 3.9 ขั้วต่อ JH1</strong></p>
3. การเชื่อมต่อกล้อง GMSL
    เชื่อมต่อกล้องดังแสดงในรูปที่ 3.10 รูปนี้แสดงตัวอย่างที่ใช้กล้องสองตัว แต่ท่านสามารถเชื่อมต่อกล้องได้ตั้งแต่หนึ่งถึงสี่ตัวตามความต้องการ
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/accessories/Camera/3.10%20GMSL%20Camera%20Connection.png"></p>
    <p align="center"><strong>รูปที่ 3.10 ขั้วต่อ JH2</strong></p>

### 3.1.3 กล้อง USB
กล้อง USB สามารถใช้งานได้โดยเชื่อมต่อเข้ากับพอร์ต USB 2.0 หรือ USB 3.0 บน D3-G เมื่อใช้กล้อง USB ที่ต้องการข้อมูลจำเพาะ USB 3.0 โปรดตรวจสอบว่าได้เชื่อมต่อเข้ากับพอร์ต USB 3.0

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/accessories/Camera/3.11%20USB%20Camera%20Connection.png"></p>
<p align="center"><strong>รูปที่ 3.11 การเชื่อมต่อกล้อง USB</strong></p>

## 3.2 การเชื่อมต่อกล้องเข้ากับ AI-G
### 3.2.1 กล้อง MIPI CSI-2
รูปที่ 3.12 แสดงขั้วต่อ MIPI CSI บน AI-G โดย AI-G รองรับ MIPI CSI จำนวน 2 ช่องสัญญาณ ซึ่งแต่ละช่องกำหนดค่าเป็นอินเทอร์เฟซแบบ 2-lane

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/accessories/Camera/3.12%20MIPI%20CSI%20Connector%20on%20AI-G.png"></p>
<p align="center"><strong>รูปที่ 3.12 ขั้วต่อ MIPI CSI บน AI-G</strong></p>

เมื่อเชื่อมต่อกล้อง MIPI ให้ใช้ FFC (Flat Flexible Cable) ดูรูปที่ 3.13 และ 3.14 สำหรับชนิดและทิศทางของสายที่ถูกต้อง

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/accessories/Camera/3.2%20FFC%20Type.png"></p>
<p align="center"><strong>รูปที่ 3.13 ชนิดของ FFC</strong></p>

สาย FFC เป็นชนิด 1.0 mm แบบ 15 พิน และด้านหนึ่งต้องมีเครื่องหมายสีที่แตกต่าง (สีน้ำเงินหรือสีเทา) ควรเสียบสายในทิศทางแบบ B-Forward Direction ดูรูปที่ 3.13 สำหรับชนิดของ FFC

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/accessories/Camera/3.14%20An%20example%20of%20an%20FFC%20connected%20to%20the%20AI-G%20MIPI%2015-pin%20Connector.png"></p>
<p align="center"><strong>รูปที่ 3.14 ตัวอย่างการเชื่อมต่อ FFC เข้ากับขั้วต่อ MIPI แบบ 15 พินของ AI-G</strong></p>

ตรวจสอบให้แน่ใจว่าหน้าสัมผัสสีเงิน 15 จุดบน FFC ตรงกับหน้าสัมผัสสีเงิน 15 จุดภายในขั้วต่อ MIPI ของ AI-G

### 3.2.2 กล้อง GMSL
กล้อง GMSL ใช้สาย Fakra จึงไม่สามารถเชื่อมต่อกับบอร์ด AI-G ได้โดยตรง แต่ต้องเชื่อมต่อผ่านบอร์ด Deserializer (Des) และ TOPST MIPI Gender Board ก่อนที่จะเชื่อมต่อกับ AI-G  
โครงสร้างการเชื่อมต่อมีดังนี้

<p align="center"><strong>< AI-G > ↔ < TOPST MIPI Gender Board > ↔ < Des Board > ↔ < GMSL Camera ></strong></p>

กล้อง GMSL จำเป็นต้องใช้ TOPST MIPI Gender Board ซึ่งต้องเชื่อมต่อผ่านขั้วต่อ MIPI แบบ 20 พิน ตัวอย่างเช่น หากคุณต้องการใช้กล้อง GMSL สี่ตัว คุณต้องเชื่อมต่อโดยใช้อินเทอร์เฟซ MIPI แบบ 20 พิน ดังแสดงในรูปที่ 3.15

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/accessories/Camera/3.15%2020-pin%20MIPI%20Connector.png"></p>
<p align="center"><strong>รูปที่ 3.15 ขั้วต่อ MIPI แบบ 20 พิน</strong></p>

1. การเชื่อมต่อบอร์ด AI-G เข้ากับ TOPST MIPI Gender Board  
    สาย FFC เป็นชนิด 1.0 mm แบบ 20 พิน และด้านหนึ่งต้องมีเครื่องหมายสีที่แตกต่าง (สีน้ำเงินหรือสีเทา) ควรเสียบสายในทิศทางแบบ A-Forward Direction ดูรูปที่ 3.16 สำหรับชนิดของ FFC
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/accessories/Camera/3.2%20FFC%20Type.png"></p>
    <p align="center"><strong>รูปที่ 3.16 ชนิดของ FFC</strong></p>
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/accessories/Camera/3.17%20An%20example%20of%20an%20FFC%20connected%20to%20the%20AI-G%20MIPI%2020-pin%20Connector.png"></p>
    <p align="center"><strong>รูปที่ 3.17 ตัวอย่างการเชื่อมต่อ FFC เข้ากับขั้วต่อ MIPI แบบ 20 พินของ AI-G</strong></p>
    ตรวจสอบให้แน่ใจว่าหน้าสัมผัสสีเงิน 20 จุดบน FFC ตรงกับหน้าสัมผัสสีเงิน 20 จุดภายในขั้วต่อ MIPI ของ AI-G
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/accessories/Camera/3.18%20An%20example%20of%20an%20FFC%20connected%20to%20the%20TOPST%20MIPI%20Gender%20Board%20MIPI%20Connector.png"></p>
    <p align="center"><strong>รูปที่ 3.18 ตัวอย่างการเชื่อมต่อ FFC เข้ากับขั้วต่อ MIPI ของ TOPST MIPI Gender Board</strong></p>
2. การเชื่อมต่อบอร์ด Deserializer เข้ากับ MIPI Gender Board  
    ต่อขั้วต่อ JH2 บน MIPI Gender Board เข้ากับขั้วต่อ JH1 ที่อยู่ด้านล่างของบอร์ด SerDes
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/accessories/Camera/3.19%20JH2%20Connector.png"></p>
    <p align="center"><strong>รูปที่ 3.19 ขั้วต่อ JH2</strong></p>
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/accessories/Camera/3.20%20JH1%20Connector.png"></p>
    <p align="center"><strong>รูปที่ 3.20 ขั้วต่อ JH1</strong></p>
3. การเชื่อมต่อกล้อง GMSL
    เชื่อมต่อกล้องตามที่แสดงในรูปที่ 3.21 รูปนี้แสดงตัวอย่างการใช้กล้องสองตัว แต่คุณสามารถเชื่อมต่อกล้องได้ตั้งแต่หนึ่งถึงสี่ตัวตามต้องการ
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/accessories/Camera/3.21%20GMSL%20Camera%20Connection.png"></p>
    <p align="center"><strong>รูปที่ 3.21 การเชื่อมต่อกล้อง GMSL</strong></p>

# 4. การตั้งค่าซอฟต์แวร์
บทที่ 4 อธิบายการตั้งค่าซอฟต์แวร์ที่จำเป็นสำหรับการทำงานของกล้อง สำหรับการกำหนดค่ากล้อง MIPI CSI-2 (OV5647, IMX219) และกล้อง GMSL บนแพลตฟอร์ม D3-G และ AI-G โปรดดูคำแนะนำการตั้งค่า Yocto ที่ให้ไว้ด้านล่าง

## 4.1 คู่มือการตั้งค่ากล้อง MIPI CSI-2
อัตราข้อมูล TX สามารถคำนวณได้โดยใช้สูตรต่อไปนี้

<p align="center"><strong>อัตราข้อมูล TX ={ H_active }×{V_active }×{FPS}×{BPP}×{ Number_of_Cameras} × 1.3 (มาร์จิน)</strong></p>

อัตราข้อมูลรวมต้องไม่เกินขีดจำกัดแบนด์วิดท์ MIPI CSI-2 ของ D3-G ที่ 2.1 Gbps ต่อเลน  
และอัตราข้อมูลรวมต้องไม่เกินขีดจำกัดแบนด์วิดท์ MIPI CSI-2 ของ AI-G ที่ 1.5 Gbps ต่อเลน

### 4.1.1 คู่มือการตั้งค่า OV5647 สำหรับ D3-G
#### 4.1.1.1 ภาพรวมเซ็นเซอร์ OV5647
##### 4.1.1.1.1 บทนำ
OV5647 เป็นเซ็นเซอร์ภาพ CMOS ความละเอียด 5 ล้านพิกเซล ซึ่งใช้กันอย่างแพร่หลายในแอปพลิเคชันกล้องแบบฝังตัว เนื่องจากมีขนาดกะทัดรัด ประสิทธิภาพเสถียร และเข้ากันได้กับอินเทอร์เฟซ MIPI CSI-2 มาตรฐาน อีกทั้งยังเป็นเซ็นเซอร์ภาพที่ใช้ใน Raspberry Pi Camera Module v1 และมีจำหน่ายผ่านโมดูลกล้อง Arducam OV5647 หลายรุ่น ซึ่งทั้งหมดเข้ากันได้กับแพลตฟอร์ม TOPST D3-G  
ผู้ใช้สามารถเชื่อมต่อ Raspberry Pi Camera v1 หรือโมดูล Arducam OV5647 เข้ากับพอร์ต MIPI CSI เพื่อใช้งานกล้องได้

บนแพลตฟอร์ม TOPST D3-G เซ็นเซอร์ OV5647 เชื่อมต่อผ่านขั้วต่อ MIPI CSI แบบ 15 พินหรือ 20 พิน และควบคุมผ่านเฟรมเวิร์ก V4L2 ทำให้ทำงานได้สอดคล้องกันทั้งในสภาพแวดล้อม Yocto และ Ubuntu

##### 4.1.1.1.2 ความละเอียดและ FPS ที่รองรับ
ข้อมูลจำเพาะของโมดูลกล้อง OV5647 (Raspberry Pi v1 หรือ Arducam OV5647) มีดังนี้  

<p align="center"><strong>ตารางที่ 4.1 ข้อมูลจำเพาะของโมดูลกล้อง OV5647</strong></p>
<div align="center">
    <table>
        <tr>
            <td colspan="2" align="center"><strong>ข้อมูลจำเพาะ</strong></td>
            <td align="center"><strong>คำอธิบาย</strong></td>
        </tr>
        <tr>
            <td colspan="2">เซ็นเซอร์</td>
            <td>OmniVision OV5647</td>
        </tr>
        <tr>
            <td colspan="2">ความละเอียด</td>
            <td>2592 x 1944 (5MP)</td>
        </tr>
        <tr>
            <td colspan="2">รูปแบบเอาต์พุต</td>
            <td>RAW, YUV, JPEG</td>
        </tr>
        <tr>
            <td colspan="2">อินเทอร์เฟซ</td>
            <td>MIPI CSI-2</td>
        </tr>
        <tr>
            <td colspan="2">อัตราเฟรม</td>
            <td>1080p30, 720p60, 480p90</td>
        </tr>
        <tr>
            <td colspan="2">เลนส์</td>
            <td>โฟกัสคงที่</td>
        </tr>
        <tr>
            <td colspan="2">มุมมองภาพ (FOV)</td>
            <td>Up to 54°</td>
        </tr>
        <tr>
            <td colspan="2">ชนิดของสาย</td>
            <td>FFC (15 พิน)</td>
        </tr>
        <tr>
            <td colspan="2">ขนาดบอร์ด</td>
            <td>25mm x 24mm</td>
        </tr>
        <tr>
            <td colspan="2">ความเข้ากันได้</td>
            <td>D3-G และ Rasbperry Pi (ผ่านพอร์ต MIPI CSI-2)</td>
        </tr>
    </table>
</div>

ความละเอียดของเซ็นเซอร์และ FPS ที่รองรับบน D3-G มีดังนี้  
<p align="center"><strong>ตารางที่ 4.2 ความละเอียดเซ็นเซอร์ OV5647 บน D3-G</strong></p>
<div align="center">
    <table>
        <tr>
            <td colspan="3" align="center"><strong>ความละเอียด</strong></td>
            <td align="center"><strong>FPS</strong></td>
            <td align="center"><strong>คำอธิบาย</strong></td>
        </tr>
        <tr>
            <td colspan="3">1920x1080</td>
            <td>30</td>
            <td>ส่งออกภาพ 1080p โดยการครอปพื้นที่ตรงกลางของเฟรมความละเอียดเต็ม</td>
        </tr>
        <tr>
            <td colspan="3">1296x972</td>
            <td>30</td>
            <td>ใช้การรวมพิกเซลแบบ 2×2 เพื่อเพิ่มความไวแสงและลดสัญญาณรบกวน</td>
        </tr>
        <tr>
            <td colspan="3">640x480</td>
            <td>60</td>
            <td>รวมการทำ binning แบบ 2×2 เข้ากับ <strong>การสุ่มตัวอย่างย่อย</strong> ซึ่งข้ามพิกเซลระหว่างการอ่านข้อมูลเพื่อลดปริมาณข้อมูลและให้อัตราเฟรมที่สูงขึ้น</td>
        </tr>
    </table>
</div>

**หมายเหตุ:** ดังแสดงในตารางที่ 4.2 ความละเอียดเต็มที่ **2592×1944 ไม่สามารถใช้งานได้** เนื่องจากข้อมูลจำเพาะของ ISP บน D3-G

<p align="center"><strong>ตารางที่ 4.3 ความละเอียดสูงสุดตามโหมดการทำงาน</strong></p>
<div align="center">
    <table>
        <tr>
            <td rowspan="2" align="center"><strong>แกนประมวลผล ISP</strong></td>
            <td colspan="2"><strong>ความละเอียดตามโหมดการทำงาน</strong></td>
        </tr>
        <tr>
            <td align="center"><strong>โหมดเริ่มต้น</strong></td>
            <td align="center"><strong>โหมดแชร์หน่วยความจำ</strong></td>
        </tr>
        <tr>
            <td>ISP0</td>
            <td>2048x1536 @ 60fps</td>
            <td>2048x1536 @ 60fps</td>
        </tr>
        <tr>
            <td>ISP1</td>
            <td>2560x1440 @ 60fps</td>
            <td>2560x1440 @ 60fps</td>
        </tr>
        <tr>
            <td>ISP2</td>
            <td>1280x720 @ 60fps</td>
            <td>1560x1440 @ 60fps</td>
        </tr>
        <tr>
            <td>ISP3</td>
            <td>1280x720 @ 60fps</td>
            <td>N/A</td>
        </tr>
    </table>
</div>

#### 4.1.1.2 การกำหนดค่าความละเอียด OV5647 ใน Yocto: ไดรเวอร์
หากต้องการแก้ไขความละเอียดของเซ็นเซอร์ OV5647 ระหว่างกระบวนการบิลด์ Yocto ให้ทำตามคำแนะนำด้านล่าง  

ขั้นแรก หากต้องการเปิดใช้งาน OV5647 ให้ตรวจสอบว่ามีการตั้งค่า TOPST_CAM_MODULE = "ov5647" ในไฟล์ต่อไปนี้  
{build_dir}/build/d3-g-topst-main/conf/local.conf.  
แม้ว่ารายการนี้จะเปิดใช้งานตามค่าเริ่มต้นเมื่อเริ่มต้นรีโพซิทอรีสำหรับการบิลด์ครั้งแรก แต่โปรดตรวจสอบอีกครั้ง

นอกจากนี้ เพื่อป้องกันไม่ให้ซอร์สโค้ดถูกลบระหว่างกระบวนการบิลด์ ให้เปิดใช้งานบรรทัดต่อไปนี้ในไฟล์  
{build_dir}/build/d3-g-topst-main/conf/local.conf:
```
INHERIT:remove = “rm_work”
```

หลังจากเปิดใช้งานตัวเลือกข้างต้นแล้ว ให้บิลด์อิมเมจใหม่โดยใช้คำสั่งต่อไปนี้
```
$ bitbake telechips-topst-image
```

ขั้นที่สอง หลังจากการบิลด์เสร็จสิ้น ให้เปิดไฟล์ไดรเวอร์ ov5647.c และทำการแก้ไขที่จำเป็น

ไปยังไดเรกทอรีต่อไปนี้
```
${build_dir}/build/d3-g-topst-main/tmp/work/d3_g_topst_main-telechips-linux/linux-topst/5.10.205-r0/git/drivers/media/i2c/telechips/
```

ก่อนแก้ไขโค้ด โปรดทราบว่าไดรเวอร์ปัจจุบันรองรับสามโหมดต่อไปนี้
- 1920x1080 @ 30fps
- 1296x972 @ 30fps
- 640x480 @ 60fps  

ความละเอียดแต่ละแบบสอดคล้องกับ Mode 1, Mode 2 และ Mode 3 ตามลำดับ  

โหมด 1920×1080 @ 30fps ใช้การครอปตรงกลาง ทำให้มุมมองภาพแคบลง และโหมด 640×480 ให้ความละเอียดไม่เพียงพอ ในทางตรงกันข้าม โหมด 1296×972 ใช้ binning แบบ 2×2 ซึ่งให้มุมมองภาพที่กว้างกว่า จึงถูกใช้เป็นโหมดเริ่มต้นในปัจจุบัน  
เปิดไฟล์ไดรเวอร์ ov5647.c และแก้ไขโหมดเริ่มต้นของ OV5647 ตามที่แสดงด้านล่าง
```
#define OV5647_DEFAULT_MODE (&supported_modes_10bit[2])
```
1920×1080 @ 30fps สอดคล้องกับ Mode 1 คุณสามารถใช้ **“#define OV5647_DEFAULT_MODE (&supported_modes_10bit[1])”** ได้ตามเดิม  
โหมด 1296×972 @ 30fps สอดคล้องกับ Mode 2 ดังนั้น **“#define OV5647_DEFAULT_MODE (&supported_modes_10bit[2])”** จึงถูกตั้งค่าไว้อย่างถูกต้องแล้ว  
สำหรับ 640×480 @ 60fps ซึ่งตรงกับ Mode 3 ให้เปลี่ยนคำนิยามเป็น **“#define OV5647_DEFAULT_MODE (&supported_modes_10bit[3])”**

ประการที่สาม ให้บิลด์เคอร์เนลใหม่และสร้างอิมเมจ FAI  
กลับไปยังไดเรกทอรีบิลด์ และบิลด์เคอร์เนลใหม่โดยใช้คำสั่งด้านล่าง
```
$ cd ${build_dir}/build/d3-g-topst-main/
$ bitbake -C compile linux-topst
$ cd ${build_dir}
$ ./stitch-fai-d3.sh
```
หลังจากนั้น ให้แฟลชไฟล์ output_d3g.fai ที่สร้างขึ้นไปยังบอร์ดด้วย FWDN แล้วท่านจะสามารถใช้งานเซ็นเซอร์ OV5647 ที่ความละเอียดที่ต้องการได้

**หมายเหตุ:** หากท่านต้องการใช้พอร์ต MIPI1-CSI ให้เปิดไฟล์ tcc805x-videoinput-camera-module.dtsi ที่อยู่ใน
“{build_dir}/build/d3-g-topst-main/tmp/work/d3_g_topst_main-telechips-linux/linux-topst/5.10.205-r0/git/arch/arm64/boot/dts/telechips/tcc805x/override/” and change the included dtsi file from “tcc805x-videoinput-mipi0-ov5647.dtsi” to “tcc805x-videoinput-mipi1-ov5647.dtsi”. + Open the tcc805x-videoinput.dtsi file located in "{build_dir}/build/d3-g-topst-main/tmp/work/d3_g_topst_main-telechips-linux/linux-topst/5.10.205-r0/git/arch/arm64/boot/dts/telechips/tcc805x/" and change the mipi chmux from "mipi-chmux-0 = <0>;" to "mipi-chmux-0 = <1>;".

### 4.1.2 คู่มือการตั้งค่า D3-G IMX219
#### 4.1.2.1 ภาพรวมเซ็นเซอร์ IMX219
##### 4.1.2.1.1 บทนำ
IMX219 เป็นเซ็นเซอร์ภาพ CMOS ความละเอียด 8 ล้านพิกเซล ประสิทธิภาพสูงจาก Sony ซึ่งเป็นที่รู้จักอย่างกว้างขวางในด้านคุณภาพของภาพที่ยอดเยี่ยม การใช้พลังงานต่ำ และประสิทธิภาพการถ่ายภาพที่เสถียรในโมดูลกล้องขนาดกะทัดรัด นอกจากนี้ยังเป็นเซ็นเซอร์ที่ใช้ใน Raspberry Pi Camera Module v2 และถูกนำไปใช้อย่างแพร่หลายในระบบวิชันแบบฝังตัว หุ่นยนต์ และแอปพลิเคชันกล้องที่ใช้ AI

บนแพลตฟอร์ม TOPST D3-G เซ็นเซอร์ IMX219 สามารถเชื่อมต่อผ่านขั้วต่อ MIPI CSI แบบ 15 พินหรือ 20 พิน และควบคุมผ่านเฟรมเวิร์ก V4L2 ซึ่งทำให้ได้อินเทอร์เฟซที่สอดคล้องกันและการทำงานของกล้องที่เสถียรทั้งในสภาพแวดล้อม Yocto และ Ubuntu

ด้วยความละเอียดสูง (8MP) และคุณลักษณะการสร้างภาพที่มีสัญญาณรบกวนต่ำ IMX219 จึงเหมาะอย่างยิ่งสำหรับการพัฒนาความสามารถในการบันทึกวิดีโอคุณภาพสูงและการประมวลผลภาพบนแพลตฟอร์ม TOPST D3-G

##### 4.1.2.1.2 ความละเอียดและ FPS ที่รองรับ
ข้อมูลจำเพาะของโมดูลกล้อง IMX219 (Raspberry Pi v2) มีดังนี้

<p align="center"><strong>ตารางที่ 4.4 ข้อมูลจำเพาะของโมดูลกล้อง IMX219</strong></p>
<div align="center">
    <table>
        <tr>
            <td colspan="2" align="center"><strong>ข้อมูลจำเพาะ</strong></td>
            <td align="center"><strong>คำอธิบาย</strong></td>
        </tr>
        <tr>
            <td colspan="2">เซ็นเซอร์</td>
            <td>Sony Imx219</td>
        </tr>
        <tr>
            <td colspan="2">ความละเอียด</td>
            <td>3280 x 2464 (8 MP)</td>
        </tr>
        <tr>
            <td colspan="2">รูปแบบเอาต์พุต</td>
            <td>RAW, YUV, JPEG</td>
        </tr>
        <tr>
            <td colspan="2">อินเทอร์เฟซ</td>
            <td>MIPI CSI-2</td>
        </tr>
        <tr>
            <td colspan="2">อัตราเฟรม</td>
            <td>1080p60, 720p180, 480p206</td>
        </tr>
        <tr>
            <td colspan="2">เลนส์</td>
            <td>ปรับโฟกัสได้</td>
        </tr>
        <tr>
            <td colspan="2">มุมมองภาพ (FOV)</td>
            <td>Up to 62°</td>
        </tr>
        <tr>
            <td colspan="2">ชนิดของสาย</td>
            <td>FFC (15 พิน)</td>
        </tr>
        <tr>
            <td colspan="2">ขนาดบอร์ด</td>
            <td>25mm x 24mm</td>
        </tr>
        <tr>
            <td colspan="2">ความเข้ากันได้</td>
            <td>D3-G และ Rasbperry Pi (ผ่านพอร์ต MIPI CSI-2)</td>
        </tr>
    </table>
</div>

ความละเอียดเซ็นเซอร์และ FPS ที่รองรับบน D3-G มีดังนี้
<p align="center"><strong>ตารางที่ 4.5 ความละเอียดเซ็นเซอร์ IMX219 บน D3-G</strong></p>
<div align="center">
    <table>
        <tr>
            <td colspan="3" align="center"><strong>ความละเอียด</strong></td>
            <td align="center"><strong>FPS</strong></td>
            <td align="center"><strong>คำอธิบาย</strong></td>
        </tr>
        <tr>
            <td colspan="3">1920x1080</td>
            <td>30</td>
            <td>ส่งออกภาพ 1080p โดยการครอปพื้นที่ตรงกลางของเฟรมความละเอียดเต็ม</td>
        </tr>
        <tr>
            <td colspan="3">1640x1232</td>
            <td>30</td>
            <td>ใช้การรวมพิกเซลแบบ 2×2 เพื่อเพิ่มความไวแสงและลดสัญญาณรบกวน</td>
        </tr>
        <tr>
            <td colspan="3">640x480</td>
            <td>30</td>
            <td>ผสาน 2×2 binning เข้ากับ<strong>การสุ่มตัวอย่างย่อย</strong> ซึ่งข้ามพิกเซลระหว่างการอ่านค่าเพื่อลดปริมาณข้อมูลที่ต้องส่ง</td>
        </tr>
    </table>
</div>  

**หมายเหตุ:** ดังที่แสดงในตารางที่ 4.5 ความละเอียดเต็ม **3820×2464 ไม่สามารถใช้งานได้** เนื่องจากข้อมูลจำเพาะของ ISP บน D3-G

<p align="center"><strong>ตารางที่ 4.6 ความละเอียดสูงสุดตามโหมดการทำงาน</strong></p>
<div align="center">
    <table>
        <tr>
            <td rowspan="2" align="center"><strong>แกนประมวลผล ISP</strong></td>
            <td colspan="2"><strong>ความละเอียดตามโหมดการทำงาน</strong></td>
        </tr>
        <tr>
            <td align="center"><strong>โหมดเริ่มต้น</strong></td>
            <td align="center"><strong>โหมดแชร์หน่วยความจำ</strong></td>
        </tr>
        <tr>
            <td>ISP0</td>
            <td>2048x1536 @ 60fps</td>
            <td>2048x1536 @ 60fps</td>
        </tr>
        <tr>
            <td>ISP1</td>
            <td>2560x1440 @ 60fps</td>
            <td>2560x1440 @ 60fps</td>
        </tr>
        <tr>
            <td>ISP2</td>
            <td>1280x720 @ 60fps</td>
            <td>1560x1440 @ 60fps</td>
        </tr>
        <tr>
            <td>ISP3</td>
            <td>1280x720 @ 60fps</td>
            <td>N/A</td>
        </tr>
    </table>
</div>

#### 4.1.2.2 การเปิดใช้งาน IMX219 ใน Yocto
เนื่องจาก D3-G SDK ถูกกำหนดค่าให้เปิดใช้งาน OV5647 โดยค่าเริ่มต้น ท่านจึงต้องเปิดใช้งาน IMX219 ก่อนทำการบิลด์   
มีสองกรณีที่ต้องพิจารณา ได้แก่ กรณีที่บิลด์ SDK ไปแล้ว และกรณีที่ทำการบิลด์เป็นครั้งแรก

##### 4.1.2.2.1 การเปิดใช้งาน IMX219 ก่อนการบิลด์ครั้งแรก
สำหรับการบิลด์ครั้งแรก ให้ปฏิบัติตามขั้นตอนด้านล่างเพื่อเปิดใช้งาน IMX219 แล้วจึงดำเนินการบิลด์
1. รัน source สคริปต์ตั้งค่าสภาพแวดล้อม แล้วเลือกตัวเลือก 2
    ```
    $ source poky/meta-topst/topst-build.sh
    ```
2. เปิดไฟล์ local.conf ที่อยู่ในพาธด้านล่าง
    ```
    ${build_dir}/build/d3-g-topst-main/conf/local.conf
    ```
3. คอมเมนต์รายการ TOPST_CAM_MODULE สำหรับ ov5647 และเปิดใช้งานรายการสำหรับ imx219
    ```
    #TOPST_CAM_MODULE = "ov5647"
    TOPST_CAM_MODULE = "imx219"
    ```
4. ดำเนินการกระบวนการบิลด์
    ```
    $ bitbake telechips-topst-image
    ```
##### 4.1.2.2.2 การเปิดใช้งาน IMX219 หลังจากทำการบิลด์เสร็จสิ้นแล้ว
บิลด์ที่มีอยู่ถูกกำหนดค่าให้เปิดใช้งานเซ็นเซอร์ OV5647 โดยค่าเริ่มต้น ให้ปฏิบัติตามขั้นตอนด้านล่างเพื่อเปิดใช้งาน IMX219
1. เปิดไฟล์ local.conf ที่อยู่ในพาธด้านล่าง
    ```
    ${build_dir}/build/d3-g-topst-main/conf/local.conf
    ```
2. คอมเมนต์รายการ TOPST_CAM_MODULE สำหรับ ov5647 และเปิดใช้งานรายการสำหรับ imx219
    ```
    #TOPST_CAM_MODULE = "ov5647"
    TOPST_CAM_MODULE = "imx219"
    ```
3. ดำเนินการ cleansstate สำหรับ isp-server และ isp-firmware
    ```
    $ bitbake -c cleansstate isp-firmware
    $ bitbake -c cleansstate isp-server
    ```
4. ดำเนินการกระบวนการบิลด์
    ```
    $ bitbake telechips-topst-image


#### 4.1.2.3 การกำหนดค่าความละเอียด IMX219 ใน Yocto: ไดรเวอร์
หากต้องการแก้ไขความละเอียดของเซ็นเซอร์ IMX219 ระหว่างกระบวนการบิลด์ Yocto ให้ปฏิบัติตามคำแนะนำด้านล่าง

ขั้นแรก หากต้องการเปิดใช้งาน imx219 ให้ตรวจสอบว่ามีการตั้งค่า TOPST_CAM_MODULE = "imx219" ใน
{build_dir}/build/d3-g-topst-main/conf/local.conf.

นอกจากนี้ เพื่อป้องกันไม่ให้ซอร์สโค้ดถูกลบระหว่างกระบวนการบิลด์ ให้เปิดใช้งานบรรทัดต่อไปนี้ใน
{build_dir}/build/d3-g-topst-main/conf/local.conf:
```
INHERIT:remove = “rm_work”
```

หลังจากเปิดใช้งานตัวเลือกข้างต้นแล้ว ให้บิลด์อิมเมจใหม่โดยใช้คำสั่งต่อไปนี้
```
$ bitbake telechips-topst-image
```

ประการที่สอง หลังจากการบิลด์เสร็จสมบูรณ์ ให้เปิดไฟล์ไดรเวอร์ imx219.c และดำเนินการแก้ไขตามที่กำหนด

ไปยังไดเรกทอรีต่อไปนี้
```
${build_dir}/build/d3-g-topst-main/tmp/work/d3_g_topst_main-telechips-linux/linux-topst/5.10.205-r0/git/drivers/media/i2c/telechips/
```

ก่อนแก้ไขโค้ด โปรดทราบว่าไดรเวอร์ปัจจุบันรองรับสามโหมดต่อไปนี้
- 1920x1080 @ 30fps
- 1640x1232 @ 30fps
- 640x480 @ 30fps

ความละเอียดแต่ละค่าสอดคล้องกับ Mode 1, Mode 2 และ Mode 3 ตามลำดับ

โหมด 1920×1080 @ 30fps ใช้การครอบตัดจากศูนย์กลาง ทำให้มุมมองภาพแคบลง และโหมด 640×480 ให้ความละเอียดไม่เพียงพอ ในทางกลับกัน โหมด 1640×1232 ใช้การทำ binning แบบ 2×2 ซึ่งให้มุมมองภาพที่กว้างกว่า จึงถูกใช้เป็นโหมดเริ่มต้นในปัจจุบัน  
เปิดไฟล์ไดรเวอร์ imx219.c และแก้ไขส่วนที่อธิบายด้านล่างภายในฟังก์ชัน imx219_set_default_format, imx219_open และ imx219_probe
- imx219_set_default_format
    ```
    fmt->width = supported_modes[2].width;
    fmt->height = supported_modes[2].height;
    ```
- imx219_open
    ```
    try_fmt_img->width = supported_modes[2].width;
    try_fmt_img->height = supported_modes[2].height;
    ```
- imx219_probe
    ```
    imx219->mode = &supported_modes[2];
    ```

เนื่องจาก 1920×1080 @ 30fps ตรงกับ Mode 1 จึงต้องเปลี่ยนการอ้างอิง supported_modes ทั้งหมดภายในฟังก์ชันทั้งสามเป็น **“supported_modes[1]”**  
โหมด 1640×1232 @ 30fps ตรงกับ Mode 2 จึงต้องเปลี่ยนเป็น **“supported_modes[2]”** ให้สอดคล้องกัน  
สำหรับ 640×480 @ 30fps ซึ่งสอดคล้องกับ Mode 3 ให้เปลี่ยนการอ้างอิงทั้งหมดเป็น **“supported_modes [3]”**

ประการที่สาม ให้บิลด์เคอร์เนลใหม่และสร้างอิมเมจ FAI  
กลับไปยังไดเรกทอรีบิลด์ และบิลด์เคอร์เนลใหม่โดยใช้คำสั่งด้านล่าง
```
$ cd ${build_dir}/build/d3-g-topst-main/
$ bitbake -C compile linux-topst
$ cd ${build_dir}
$ ./stitch-fai-d3.sh
```

จากนั้นแฟลช output_d3g.fai ที่สร้างขึ้นไปยังบอร์ดด้วย FWDN แล้วคุณจะสามารถใช้เซ็นเซอร์ IMX219 ที่ความละเอียดที่ต้องการได้

**หมายเหตุ:** หากท่านต้องการใช้พอร์ต MIPI1-CSI ให้เปิดไฟล์ tcc805x-videoinput-camera-module.dtsi ที่อยู่ใน
“{build_dir}/build/d3-g-topst-main/tmp/work/d3_g_topst_main-telechips-linux/linux-topst/5.10.205-r0/git/arch/arm64/boot/dts/telechips/tcc805x/override/”and change the included dtsi file from “tcc805x-videoinput-mipi0-imx219.dtsi” to “tcc805x-videoinput-mipi1-imx219.dtsi”. + Open the tcc805x-videoinput.dtsi file located in "{build_dir}/build/d3-g-topst-main/tmp/work/d3_g_topst_main-telechips-linux/linux-topst/5.10.205-r0/git/arch/arm64/boot/dts/telechips/tcc805x/" and change the mipi chmux from "mipi-chmux-0 = <0>;" to "mipi-chmux-0 = <1>;".

#### 4.1.2.4 วิธีเพิ่ม FPS ของ IMX219 ใน Yocto: ไดรเวอร์และ Device Tree
ตามคำอธิบายของเซ็นเซอร์ IMX219 เซ็นเซอร์นี้รองรับโหมดอัตราเฟรมสูง เช่น 1080p60, 720p180 และ VGA206 ดังนั้นจึงสามารถเพิ่ม FPS สำหรับความละเอียดที่ไดรเวอร์ imx219.c รองรับ ได้แก่ 1920×1080, 1640×1232 และ 640×480 เนื่องจาก ISP core บนแพลตฟอร์ม D3-G รองรับสูงสุด 60 fps ความละเอียดเหล่านี้จึงสามารถเพิ่มได้สูงสุดถึง 60 fps 

สูตรสำหรับการคำนวณ FPS มีดังนี้
<p align="center"><strong>{fps} = {pixel_rate}/{hts}x{vts}</strong></p>
ดังนั้น เพื่อเพิ่ม FPS จึงต้องปรับค่า pixel_rate, hts และ vts  
ในการใช้งานไดรเวอร์ปัจจุบัน ทั้ง pixel_rate และ hts ถูกกำหนดตายตัว หากต้องการเพิ่ม FPS วิธีเดียวที่ทำได้คือเพิ่ม pixel_rate โดยคง hts ไว้เท่าเดิม แล้วปรับ vts ให้เหมาะสมเพื่อให้ได้อัตราเฟรมที่ต้องการ

หากต้องการแก้ไข FPS เป็น 60 จะต้องอัปเดตทั้งไดรเวอร์และดีไวซ์ทรี
ทำตามคู่มือด้านล่างเพื่อเปลี่ยน FPS เป็น 60

##### 4.1.2.4.1 1920x1080 @ 60fps
เพื่อให้ได้ 60 fps จะต้องเป็นไปตามความสัมพันธ์ต่อไปนี้  
fps = pixel_rate / (hts × vts)
- pixel_rate = 182,400,000
- hts = 3448
- target fps = 60

ค่า VTS ที่ต้องใช้จะเป็นดังนี้
- vts = pixel_rate / (hts × fps) = 182,400,000 / (3448 × 60) ≈ 882

อย่างไรก็ตาม ค่า VTS ต้องมากกว่า 1080 ดังนั้นการกำหนดค่านี้จึงไม่ถูกต้อง  
ดังนั้น เพื่อให้ได้ 60 fps จึงต้องคงค่า hts ไว้คงที่ และปรับค่า pixel_rate, vts รวมถึงรีจิสเตอร์ PLL_VT แทน

รายการที่ต้องเปลี่ยนแปลงมีดังนี้
1. ไฟล์ไดรเวอร์ imx219.c  
    A. เพิ่มอัตราพิกเซลและความถี่ลิงก์
    ```
    #define IMX219_PIXEL_RATE            182400000    →   #define IMX219_PIXEL_RATE            278400000
    #define IMX219_DEFAULT_LINK_FREQ     456000000   →   #define IMX219_DEFAULT_LINK_FREQ     696000000
    ``` 
    B. อัปเดตค่า VTS สำหรับโหมด 1080p:
    ```
    #define IMX219_VTS_30FPS_1080P       0x06e3       →   #define IMX219_VTS_30FPS_1080P       0x0542
    ```
    C. แก้ไขรีจิสเตอร์ PLL_VT ในตารางโหมด 1920x1080:
    ```
    // imx219_reg mode_1920_1080_regs[]
    {0x0307, 0x39}   →   {0x0307, 0x57}
    ```
2. ไฟล์ดีไวซ์ทรี tcc805x-videoinput-mipi0-imx219.dtsi  
    A. อัปเดตความถี่ลิงก์ให้ตรงกับอัตราพิกเซลใหม่:
    ```
    // &i2c7
    /bits/ 64 <456000000> → /bits/ 64 <696000000>
    ```
    B. อัปเดตค่า hs-settle:
    ```
    hs-settle = <13> → hs-settle = <35>
    ```
3. บิลด์เคอร์เนลใหม่และสร้างอิมเมจ FAI  
    กลับไปยังไดเรกทอรีบิลด์ แล้วบิลด์เคอร์เนลใหม่โดยใช้คำสั่งด้านล่าง
    ```
    $ cd ${build_dir}/build/d3-g-topst-main/
    $ bitbake -C compile linux-topst
    $ cd ${build_dir}
    $ ./stitch-fai-d3.sh
    ```
เมื่อใช้คำสั่งด้านล่างบน D3-G จะเห็นได้ว่าค่า FPS ที่แสดงคือ 59.9 ซึ่งตรงกับ 60 fps
```
$ v4l2-ctl --stream-mmap=3 --stream-count=300 --stream-to=/dev/null --verbose
```
คำสั่ง GStreamer สำหรับการเล่นภาพจากกล้องบน D3-G แสดงไว้ด้านล่าง
```
$ gst-launch-1.0 v4l2src device=/dev/video0 io-mode=2 ! video/x-raw,format=NV12,width=1920,height=1080,framerate=60/1 ! videoconvert ! waylandsink sync=false
```

##### 4.1.2.4.2 1640x1232 @ 60fps
เพื่อให้ได้ 60 fps จะต้องเป็นไปตามความสัมพันธ์ต่อไปนี้  
fps = pixel_rate / (hts × vts)
- pixel_rate = 182,400,000
- hts = 3448
- target fps = 60

ค่า VTS ที่ต้องใช้จะเป็นดังนี้
- vts = pixel_rate / (hts × fps) = 182,400,000 / (3448 × 60) ≈ 882

อย่างไรก็ตาม ค่า VTS ต้องมากกว่า 1080 ดังนั้นการกำหนดค่านี้จึงไม่ถูกต้อง  
ดังนั้น เพื่อให้ได้ 60 fps จึงต้องคงค่า hts ไว้คงที่ และปรับค่า pixel_rate, vts รวมถึงรีจิสเตอร์ PLL_VT แทน

รายการที่ต้องเปลี่ยนแปลงมีดังนี้
1. ไฟล์ไดรเวอร์ imx219.c  
    A. เพิ่มอัตราพิกเซลและความถี่ลิงก์
    ```
    #define IMX219_PIXEL_RATE            182400000    →   #define IMX219_PIXEL_RATE            278400000
    #define IMX219_DEFAULT_LINK_FREQ     456000000   →   #define IMX219_DEFAULT_LINK_FREQ     696000000
    ``` 
    B. อัปเดตค่า VTS สำหรับโหมด 1640_1232:
    ```
    #define IMX219_VTS_30FPS_BINNED       0x06e3       →   #define IMX219_VTS_30FPS_BINNED       0x0542
    ```
    C. แก้ไขรีจิสเตอร์ PLL_VT ในตารางโหมด 1920x1080:
    ```
    // imx219_reg mode_1640_1232_regs[]
    {0x0307, 0x39}   →   {0x0307, 0x57}
    ```
2. ไฟล์ดีไวซ์ทรี tcc805x-videoinput-mipi0-imx219.dtsi  
    A. อัปเดตความถี่ลิงก์ให้ตรงกับอัตราพิกเซลใหม่:
    ```
    // &i2c7
    /bits/ 64 <456000000> → /bits/ 64 <696000000>
    ```
    B. อัปเดตค่า hs-settle:
    ```
    hs-settle = <13> → hs-settle = <34>
    ```
3. บิลด์เคอร์เนลใหม่และสร้างอิมเมจ FAI  
    กลับไปยังไดเรกทอรีบิลด์ แล้วบิลด์เคอร์เนลใหม่โดยใช้คำสั่งด้านล่าง
    ```
    $ cd ${build_dir}/build/d3-g-topst-main/
    $ bitbake -C compile linux-topst
    $ cd ${build_dir}
    $ ./stitch-fai-d3.sh
    ```
เมื่อใช้คำสั่งด้านล่างบน D3-G จะเห็นได้ว่าค่า FPS ที่แสดงคือ 59.9 ซึ่งตรงกับ 60 fps
```
$ v4l2-ctl --stream-mmap=3 --stream-count=300 --stream-to=/dev/null --verbose
```
คำสั่ง GStreamer สำหรับการเล่นภาพจากกล้องบน D3-G แสดงไว้ด้านล่าง
```
$ gst-launch-1.0 v4l2src device=/dev/video0 io-mode=2 ! video/x-raw,format=NV12,width=1640,height=1232,framerate=60/1 ! videoconvert ! waylandsink sync=false
```

##### 4.1.2.4.3 640x480 @ 60fps
เพื่อให้ได้ 60 fps จะต้องเป็นไปตามความสัมพันธ์ต่อไปนี้  
fps = pixel_rate / (hts × vts)
- pixel_rate = 182,400,000
- hts = 3448
- target fps = 60

ค่า VTS ที่ต้องใช้จะเป็นดังนี้
- vts = pixel_rate / (hts × fps) = 182,400,000 / (3448 × 60) ≈ 882

เนื่องจากค่า VTS มากกว่า 480 จึงเป็นไปตามเงื่อนไข เช่นเดียวกับตัวอย่างก่อนหน้านี้ เราจะปรับ pixelrate และ VTS เพื่อเปลี่ยน FPS โดยคงค่า HTS ไว้คงที่  
นอกจากนี้ยังสามารถปรับ FPS โดยการแก้ไขเฉพาะค่า VTS โดยไม่เปลี่ยนค่า pixelrate ได้ อย่างไรก็ตาม ค่ารีจิสเตอร์ 0x0307 ของ IMX219 จะต้องคงไว้โดยไม่เปลี่ยนแปลง

รายการที่ต้องเปลี่ยนแปลงมีดังนี้
1. ไฟล์ไดรเวอร์ imx219.c  
    A. เพิ่มอัตราพิกเซลและความถี่ลิงก์
    ```
    #define IMX219_PIXEL_RATE            182400000    →   #define IMX219_PIXEL_RATE            278400000
    #define IMX219_DEFAULT_LINK_FREQ     456000000   →   #define IMX219_DEFAULT_LINK_FREQ     696000000
    ``` 
    B. อัปเดตค่า VTS สำหรับโหมด 640_480:
    ```
    #define IMX219_VTS_30FPS_640x480       0x06e3       →   #define IMX219_VTS_30FPS_640x480       0x0542
    ```
    C. แก้ไขรีจิสเตอร์ PLL_VT ในตารางโหมด 640x480:
    ```
    // imx219_reg mode_640_480_regs[]
    {0x0307, 0x39}   →   {0x0307, 0x57}
    ```
2. ไฟล์ดีไวซ์ทรี tcc805x-videoinput-mipi0-imx219.dtsi  
    A. อัปเดตความถี่ลิงก์ให้ตรงกับอัตราพิกเซลใหม่:
    ```
    // &i2c7
    /bits/ 64 <456000000> → /bits/ 64 <696000000>
    ```
    B. อัปเดตค่า hs-settle:
    ```
    hs-settle = <13> → hs-settle = <26>
    ```
3. บิลด์เคอร์เนลใหม่และสร้างอิมเมจ FAI  
    กลับไปยังไดเรกทอรีบิลด์ แล้วบิลด์เคอร์เนลใหม่โดยใช้คำสั่งด้านล่าง
    ```
    $ cd ${build_dir}/build/d3-g-topst-main/
    $ bitbake -C compile linux-topst
    $ cd ${build_dir}
    $ ./stitch-fai-d3.sh
    ```
เมื่อใช้คำสั่งด้านล่างบน D3-G จะเห็นได้ว่าค่า FPS ที่แสดงคือ 59.9 ซึ่งตรงกับ 60 fps
```
$ v4l2-ctl --stream-mmap=3 --stream-count=300 --stream-to=/dev/null --verbose
```
คำสั่ง GStreamer สำหรับการเล่นภาพจากกล้องบน D3-G แสดงไว้ด้านล่าง
```
$ gst-launch-1.0 v4l2src device=/dev/video0 io-mode=2 ! video/x-raw,format=NV12,width=640,height=480,framerate=60/1 ! videoconvert ! waylandsink sync=false
```

### 4.1.3 คู่มือผู้ใช้เซ็นเซอร์ AI-G OV5647
#### 4.1.3.1 ภาพรวมเซ็นเซอร์ OV5647
##### 4.1.3.1.1 บทนำ
OV5647 เป็นเซ็นเซอร์ภาพ CMOS ความละเอียด 5 ล้านพิกเซล ซึ่งถูกใช้อย่างแพร่หลายในแอปพลิเคชันกล้องแบบฝังตัว เนื่องจากมีขนาดกะทัดรัด ประสิทธิภาพที่เสถียร และความเข้ากันได้กับอินเทอร์เฟซ MIPI CSI-2 มาตรฐาน อีกทั้งยังเป็นเซ็นเซอร์ภาพที่ใช้ใน Raspberry Pi Camera Module v1 และมีจำหน่ายในรูปแบบโมดูลกล้อง Arducam OV5647 หลากหลายรุ่น ซึ่งทั้งหมดเข้ากันได้กับแพลตฟอร์ม TOPST AI-G  
ผู้ใช้สามารถเชื่อมต่อ Raspberry Pi Camera v1 หรือโมดูล Arducam OV5647 เข้ากับพอร์ต MIPI CSI เพื่อใช้งานกล้องได้

บนแพลตฟอร์ม TOPST AI-G เซ็นเซอร์ OV5647 เชื่อมต่อผ่านขั้วต่อ MIPI CSI แบบ 15 พินหรือ 20 พิน และควบคุมผ่านเฟรมเวิร์ก V4L2 จึงให้การทำงานที่สอดคล้องกันทั้งในสภาพแวดล้อม Yocto และ Ubuntu

##### 4.1.3.1.2 ความละเอียดและ FPS ที่รองรับ
ข้อมูลจำเพาะของโมดูลกล้อง OV5647 (Raspberry Pi v1 หรือ Arducam OV5647) มีดังนี้
<p align="center"><strong>ตารางที่ 4.7 ข้อมูลจำเพาะของโมดูลกล้อง OV5647</strong></p>
<div align="center">
    <table>
        <tr>
            <td colspan="2" align="center"><strong>ข้อมูลจำเพาะ</strong></td>
            <td align="center"><strong>คำอธิบาย</strong></td>
        </tr>
        <tr>
            <td colspan="2">เซ็นเซอร์</td>
            <td>OmniVision OV5647</td>
        </tr>
        <tr>
            <td colspan="2">ความละเอียด</td>
            <td>2592 x 1944 (5MP)</td>
        </tr>
        <tr>
            <td colspan="2">รูปแบบเอาต์พุต</td>
            <td>RAW, YUV, JPEG</td>
        </tr>
        <tr>
            <td colspan="2">อินเทอร์เฟซ</td>
            <td>MIPI CSI-2</td>
        </tr>
        <tr>
            <td colspan="2">อัตราเฟรม</td>
            <td>1080p30, 720p60, 480p90</td>
        </tr>
        <tr>
            <td colspan="2">เลนส์</td>
            <td>โฟกัสคงที่</td>
        </tr>
        <tr>
            <td colspan="2">มุมมองภาพ (FOV)</td>
            <td>Up to 54°</td>
        </tr>
        <tr>
            <td colspan="2">ชนิดของสาย</td>
            <td>FFC (15 พิน)</td>
        </tr>
        <tr>
            <td colspan="2">ขนาดบอร์ด</td>
            <td>25mm x 24mm</td>
        </tr>
        <tr>
            <td colspan="2">ความเข้ากันได้</td>
            <td>D3-G และ Rasbperry Pi (ผ่านพอร์ต MIPI CSI-2)</td>
        </tr>
    </table>
</div>

ความละเอียดของเซ็นเซอร์และ FPS ที่รองรับบน AI-G มีดังนี้  
<p align="center"><strong>ตารางที่ 4.8 ความละเอียดของเซ็นเซอร์ OV5647 บน AI-G</strong></p>
<div align="center">
    <table>
        <tr>
            <td colspan="3" align="center"><strong>ความละเอียด</strong></td>
            <td align="center"><strong>FPS</strong></td>
            <td align="center"><strong>คำอธิบาย</strong></td>
        </tr>
        <tr>
            <td colspan="3">1920x1080</td>
            <td>30</td>
            <td>ส่งออกภาพ 1080p โดยการครอปพื้นที่ตรงกลางของเฟรมความละเอียดเต็ม</td>
        </tr>
        <tr>
            <td colspan="3">1296x972</td>
            <td>30</td>
            <td>ใช้การรวมพิกเซลแบบ 2×2 เพื่อเพิ่มความไวแสงและลดสัญญาณรบกวน</td>
        </tr>
        <tr>
            <td colspan="3">640x480</td>
            <td>60</td>
            <td>รวมการทำ binning แบบ 2×2 เข้ากับ <strong>การสุ่มตัวอย่างย่อย</strong> ซึ่งข้ามพิกเซลระหว่างการอ่านข้อมูลเพื่อลดปริมาณข้อมูลและให้อัตราเฟรมที่สูงขึ้น</td>
        </tr>
    </table>
</div>

**หมายเหตุ:** ตามที่แสดงในตารางที่ 4.8 **จะไม่ใช้ความละเอียดเต็ม 2592×1944** เนื่องจากทำให้ประสิทธิภาพการอนุมานช้าลงอย่างมาก

<p align="center"><strong>ตารางที่ 4.9 ความละเอียดสูงสุดตามโหมดการทำงาน</strong></p>
<div align="center">
    <table>
        <tr>
            <td colspan="4" align="center"><strong>CH. ที่ใช้</strong></td>
            <td align="center"><strong>โหมดการทำงาน</strong></td>
            <td align="center"><strong>ความละเอียดสูงสุด</strong></td>
            <td align="center"><strong>รูปแบบอินพุต</strong></td>
        </tr>
        <tr>
            <td colspan="4">4CH</td>
            <td>โหมดเริ่มต้น</td>
            <td>1280 x 720 @ 60fps</td>
            <td>RAW 24</td>
        </tr>
        <tr>
            <td colspan="4" rowspan="2">2CH</td>
            <td rowspan="2">โหมดแชร์หน่วยความจำ</td>
            <td>ตัวเลือกที่ 1: 2048 x 1280 @ 60fps</td>
            <td>RAW 20</td>
        </tr>
        <tr>
            <td>ตัวเลือกที่ 2: 2592 x 2048 @ 30fps + 2048 x 1280 @ 30fps</td>
            <td>RAW 24</td>
        </tr>
        <tr>
            <td colspan="4">1CH</td>
            <td>โหมดแชร์หน่วยความจำ</td>
            <td>2592 x 2048 @ 60fps</td>
            <td>RAW 20</td>
        </tr>
    </table>
</div>

#### 4.1.3.2 การกำหนดค่าความละเอียด OV5647 ใน Yocto: ไดรเวอร์
หากต้องการแก้ไขความละเอียดของเซ็นเซอร์ OV5647 ระหว่างกระบวนการบิลด์ Yocto ให้ปฏิบัติตามคำแนะนำด้านล่าง

ขั้นแรก หากต้องการเปิดใช้งาน OV5647 ให้ตรวจสอบว่ามีการตั้งค่า TOPST_CAM_MODULE = "ov5647" ในไฟล์ต่อไปนี้  
{build_dir}/build/ai-g-topst-main/conf/local.conf.  
แม้ว่ารายการนี้จะเปิดใช้งานตามค่าเริ่มต้นเมื่อเริ่มต้นรีโพซิทอรีสำหรับการบิลด์ครั้งแรก แต่โปรดตรวจสอบอีกครั้ง

นอกจากนี้ เพื่อป้องกันไม่ให้ซอร์สโค้ดถูกลบระหว่างกระบวนการบิลด์ ให้เปิดใช้งานบรรทัดต่อไปนี้ในไฟล์  
{build_dir}/build/ai-g-topst-main/conf/local.conf:
```
INHERIT:remove = “rm_work”
```

หลังจากเปิดใช้งานตัวเลือกข้างต้นแล้ว ให้บิลด์อิมเมจใหม่โดยใช้คำสั่งต่อไปนี้
```
$ bitbake telechips-topst-image
```

ขั้นที่สอง หลังจากการบิลด์เสร็จสิ้น ให้เปิดไฟล์ไดรเวอร์ ov5647.c และทำการแก้ไขที่จำเป็น

ไปยังไดเรกทอรีต่อไปนี้
```
${build_dir}/build/ai-g-topst-main/tmp/work/ai_g_topst-telechips-linux/linux-topst/5.10.223-r0/git/drivers/media/i2c/telechips/
```

ก่อนแก้ไขโค้ด โปรดทราบว่าไดรเวอร์ปัจจุบันรองรับสามโหมดต่อไปนี้
- 1920×1080 @ 30fps
- 1296×972 @ 30fps
- 640×480 @ 60fps

ความละเอียดแต่ละค่าสอดคล้องกับ Mode 1, Mode 2 และ Mode 3 ตามลำดับ

โหมด 1920×1080 @ 30fps ใช้การครอปตรงกลาง ทำให้มุมมองภาพแคบลง และโหมด 640×480 ให้ความละเอียดไม่เพียงพอ ในทางตรงกันข้าม โหมด 1296×972 ใช้ binning แบบ 2×2 ซึ่งให้มุมมองภาพที่กว้างกว่า จึงถูกใช้เป็นโหมดเริ่มต้นในปัจจุบัน  
เปิดไฟล์ไดรเวอร์ ov5647.c และแก้ไขโหมดเริ่มต้นของ OV5647 ตามที่แสดงด้านล่าง
```
#define OV5647_DEFAULT_MODE (&supported_modes_10bit[2])
```
1920×1080 @ 30fps สอดคล้องกับ Mode 1 คุณสามารถใช้ **“#define OV5647_DEFAULT_MODE (&supported_modes_10bit[1])”** ได้ตามเดิม  
โหมด 1296×972 @ 30fps ตรงกับ Mode 2 ดังนั้น **“#define OV5647_DEFAULT_MODE (&supported_modes_10bit[2])”** จึงถูกตั้งค่าไว้อย่างถูกต้องแล้ว  
สำหรับ 640×480 @ 60fps ซึ่งตรงกับ Mode 3 ให้เปลี่ยนคำนิยามเป็น **“#define OV5647_DEFAULT_MODE (&supported_modes_10bit[3])”**

ประการที่สาม ให้บิลด์เคอร์เนลใหม่และสร้างอิมเมจ FAI  
กลับไปยังไดเรกทอรีบิลด์ และบิลด์เคอร์เนลใหม่โดยใช้คำสั่งด้านล่าง
```
$ cd ${build_dir}/build/ai-g-topst-main/
$ bitbake -C compile linux-topst
$ cd ${build_dir}
$ ./stitch-fai-ai.sh
```

จากนั้นแฟลช output_aig.fai ที่สร้างขึ้นไปยังบอร์ดด้วย FWDN แล้วคุณจะสามารถใช้เซ็นเซอร์ OV5647 ที่ความละเอียดที่ต้องการได้

### 4.1.4 คู่มือการตั้งค่าเซ็นเซอร์ AI-G IMX219
#### 4.1.4.1 ภาพรวมเซ็นเซอร์ IMX219
##### 4.1.4.1.1 บทนำ
IMX219 เป็นเซ็นเซอร์ภาพ CMOS ความละเอียด 8 ล้านพิกเซล ประสิทธิภาพสูงจาก Sony ซึ่งเป็นที่รู้จักอย่างกว้างขวางในด้านคุณภาพของภาพที่ยอดเยี่ยม การใช้พลังงานต่ำ และประสิทธิภาพการถ่ายภาพที่เสถียรในโมดูลกล้องขนาดกะทัดรัด นอกจากนี้ยังเป็นเซ็นเซอร์ที่ใช้ใน Raspberry Pi Camera Module v2 และถูกนำไปใช้อย่างแพร่หลายในระบบวิชันแบบฝังตัว หุ่นยนต์ และแอปพลิเคชันกล้องที่ใช้ AI

บนแพลตฟอร์ม TOPST AI-G เซ็นเซอร์ IMX219 สามารถเชื่อมต่อผ่านขั้วต่อ MIPI CSI แบบ 15 พินหรือ 20 พิน และควบคุมผ่านเฟรมเวิร์ก V4L2 ซึ่งทำให้ได้อินเทอร์เฟซที่สอดคล้องกันและการทำงานของกล้องที่เสถียรทั้งในสภาพแวดล้อม Yocto และ Ubuntu

ด้วยความละเอียดสูง (8MP) และคุณลักษณะการถ่ายภาพที่มีสัญญาณรบกวนต่ำ IMX219 จึงเหมาะอย่างยิ่งสำหรับการใช้งานด้านการบันทึกวิดีโอคุณภาพสูงและการประมวลผลภาพบนแพลตฟอร์ม TOPST AI-G

##### 4.1.4.1.2 ความละเอียดและ FPS ที่รองรับ
ข้อมูลจำเพาะของโมดูลกล้อง IMX219 (Raspberry Pi v2) มีดังนี้
<p align="center"><strong>ตารางที่ 4.10 ข้อมูลจำเพาะของโมดูลกล้อง IMX219</strong></p>
<div align="center">
    <table>
        <tr>
            <td colspan="2" align="center"><strong>ข้อมูลจำเพาะ</strong></td>
            <td align="center"><strong>คำอธิบาย</strong></td>
        </tr>
        <tr>
            <td colspan="2">เซ็นเซอร์</td>
            <td>Sony Imx219</td>
        </tr>
        <tr>
            <td colspan="2">ความละเอียด</td>
            <td>3280 x 2464 (8 MP)</td>
        </tr>
        <tr>
            <td colspan="2">รูปแบบเอาต์พุต</td>
            <td>RAW, YUV, JPEG</td>
        </tr>
        <tr>
            <td colspan="2">อินเทอร์เฟซ</td>
            <td>MIPI CSI-2</td>
        </tr>
        <tr>
            <td colspan="2">อัตราเฟรม</td>
            <td>1080p60, 720p180, 480p206</td>
        </tr>
        <tr>
            <td colspan="2">เลนส์</td>
            <td>ปรับโฟกัสได้</td>
        </tr>
        <tr>
            <td colspan="2">มุมมองภาพ (FOV)</td>
            <td>Up to 62°</td>
        </tr>
        <tr>
            <td colspan="2">ชนิดของสาย</td>
            <td>FFC (15 พิน)</td>
        </tr>
        <tr>
            <td colspan="2">ขนาดบอร์ด</td>
            <td>25mm x 24mm</td>
        </tr>
        <tr>
            <td colspan="2">ความเข้ากันได้</td>
            <td>D3-G และ Rasbperry Pi (ผ่านพอร์ต MIPI CSI-2)</td>
        </tr>
    </table>
</div>

ความละเอียดของเซ็นเซอร์และ FPS ที่รองรับบน AI-G มีดังนี้
<p align="center"><strong>ตารางที่ 4.11 ความละเอียดของเซ็นเซอร์ IMX219 บน AI-G</strong></p>
<div align="center">
    <table>
        <tr>
            <td colspan="3" align="center"><strong>ความละเอียด</strong></td>
            <td align="center"><strong>FPS</strong></td>
            <td align="center"><strong>คำอธิบาย</strong></td>
        </tr>
        <tr>
            <td colspan="3">1920x1080</td>
            <td>30</td>
            <td>ส่งออกภาพ 1080p โดยการครอปพื้นที่ตรงกลางของเฟรมความละเอียดเต็ม</td>
        </tr>
        <tr>
            <td colspan="3">1640x1232</td>
            <td>30</td>
            <td>ใช้การรวมพิกเซลแบบ 2×2 เพื่อเพิ่มความไวแสงและลดสัญญาณรบกวน</td>
        </tr>
        <tr>
            <td colspan="3">640x480</td>
            <td>30</td>
            <td>ผสาน 2×2 binning เข้ากับ<strong>การสุ่มตัวอย่างย่อย</strong> ซึ่งข้ามพิกเซลระหว่างการอ่านค่าเพื่อลดปริมาณข้อมูลที่ต้องส่ง</td>
        </tr>
    </table>
</div>

**หมายเหตุ:** ตามที่แสดงในตารางที่ 4.11 จะไม่ใช้ความละเอียดเต็ม 3820×2464 เนื่องจากทำให้ประสิทธิภาพการอนุมานช้าลงอย่างมาก

<p align="center"><strong>ตารางที่ 4.12 ความละเอียดสูงสุดตามโหมดการทำงาน</strong></p>
<div align="center">
    <table>
        <tr>
            <td colspan="4" align="center"><strong>CH. ที่ใช้</strong></td>
            <td align="center"><strong>โหมดการทำงาน</strong></td>
            <td align="center"><strong>ความละเอียดสูงสุด</strong></td>
            <td align="center"><strong>รูปแบบอินพุต</strong></td>
        </tr>
        <tr>
            <td colspan="4">4CH</td>
            <td>โหมดเริ่มต้น</td>
            <td>1280 x 720 @ 60fps</td>
            <td>RAW 24</td>
        </tr>
        <tr>
            <td colspan="4" rowspan="2">2CH</td>
            <td rowspan="2">โหมดแชร์หน่วยความจำ</td>
            <td>ตัวเลือกที่ 1: 2048 x 1280 @ 60fps</td>
            <td>RAW 20</td>
        </tr>
        <tr>
            <td>ตัวเลือกที่ 2: 2592 x 2048 @ 30fps + 2048 x 1280 @ 30fps</td>
            <td>RAW 24</td>
        </tr>
        <tr>
            <td colspan="4">1CH</td>
            <td>โหมดแชร์หน่วยความจำ</td>
            <td>2592 x 2048 @ 60fps</td>
            <td>RAW 20</td>
        </tr>
    </table>
</div>

#### 4.1.4.2 การเปิดใช้งาน IMX219 ใน Yocto
เนื่องจาก AI-G SDK ถูกกำหนดค่าให้เปิดใช้งาน OV5647 เป็นค่าเริ่มต้น จึงต้องเปิดใช้งาน IMX219 ก่อนทำการบิลด์  
มีสองกรณีที่ต้องพิจารณา ได้แก่ กรณีที่บิลด์ SDK ไปแล้ว และกรณีที่ทำการบิลด์เป็นครั้งแรก

##### 4.1.4.2.1 เปิดใช้งาน IMX219 ก่อนการบิลด์ครั้งแรก
สำหรับการบิลด์ครั้งแรก ให้ปฏิบัติตามขั้นตอนด้านล่างเพื่อเปิดใช้งาน IMX219 แล้วจึงดำเนินการบิลด์
1. เรียก source สคริปต์ตั้งค่าสภาพแวดล้อมและเลือกตัวเลือก 1
    ```
    $ source poky/meta-topst/topst-build.sh
    ```
2. เปิดไฟล์ local.conf ที่อยู่ในพาธด้านล่าง
    ```
    ${build_dir}/build/ai-g-topst-main/conf/local.conf
    ```
3. คอมเมนต์รายการ TOPST_CAM_MODULE สำหรับ ov5647 และเปิดใช้งานรายการสำหรับ imx219
    ```
    #TOPST_CAM_MODULE = "ov5647"
    TOPST_CAM_MODULE = "imx219"
    ```
4. ดำเนินการกระบวนการบิลด์
    ```
    $ bitbake telechips-topst-ai-image
    ```

##### 4.1.4.2.2 เปิดใช้งาน IMX219 หลังจากบิลด์เสร็จสิ้นแล้ว
บิลด์ที่มีอยู่ถูกกำหนดค่าให้เปิดใช้งานเซ็นเซอร์ OV5647 โดยค่าเริ่มต้น ให้ปฏิบัติตามขั้นตอนด้านล่างเพื่อเปิดใช้งาน IMX219
1. เปิดไฟล์ local.conf ที่อยู่ในพาธด้านล่าง
    ```
    ${build_dir}/build/ai-g-topst-main/conf/local.conf
    ```
2. คอมเมนต์รายการ TOPST_CAM_MODULE สำหรับ ov5647 และเปิดใช้งานรายการสำหรับ imx219
    ```
    #TOPST_CAM_MODULE = "ov5647"
    TOPST_CAM_MODULE = "imx219"
    ```
3. ดำเนินการ cleansstate สำหรับ isp-server และ isp-firmware
    ```
    $ bitbake -c cleansstate isp-firmware
    $ bitbake -c cleansstate isp-server
    ```
4. ดำเนินการกระบวนการบิลด์
    ```
    $ bitbake telechips-topst-ai-image
    ```

#### 4.1.4.3 การกำหนดค่าความละเอียด IMX219 ใน Yocto: ไดรเวอร์
หากต้องการแก้ไขความละเอียดของเซ็นเซอร์ IMX219 ระหว่างกระบวนการบิลด์ Yocto ให้ปฏิบัติตามคำแนะนำด้านล่าง

ขั้นแรก หากต้องการเปิดใช้งาน imx219 ให้ตรวจสอบว่ามีการตั้งค่า TOPST_CAM_MODULE = "imx219" ใน
{build_dir}/build/ai-g-topst-main/conf/local.conf.

นอกจากนี้ เพื่อป้องกันไม่ให้ซอร์สโค้ดถูกลบระหว่างกระบวนการบิลด์ ให้เปิดใช้งานบรรทัดต่อไปนี้ใน
{build_dir}/build/ai-g-topst-main/conf/local.conf:
```
INHERIT:remove = “rm_work”
```

หลังจากเปิดใช้งานตัวเลือกข้างต้นแล้ว ให้บิลด์อิมเมจใหม่โดยใช้คำสั่งต่อไปนี้
```
$ bitbake telechips-topst-ai-image
```
ประการที่สอง หลังจากการบิลด์เสร็จสมบูรณ์ ให้เปิดไฟล์ไดรเวอร์ imx219.c และดำเนินการแก้ไขตามที่กำหนด

ไปยังไดเรกทอรีต่อไปนี้
```
${build_dir}/build/ai-g-topst-main /ai-g-topst/tmp/work/ai_g_topst-telechips-linux/linux-topst/5.10.223-r0/git/drivers/media/i2c/telechips/
```
ก่อนแก้ไขโค้ด โปรดทราบว่าไดรเวอร์ปัจจุบันรองรับสามโหมดต่อไปนี้
- 1920×1080 @ 30fps
- 1640×1232 @ 30fps
- 640×480 @ 30fps
ความละเอียดแต่ละค่าสอดคล้องกับ Mode 1, Mode 2 และ Mode 3 ตามลำดับ

โหมด 1920×1080 @ 30fps ใช้การครอบตัดจากศูนย์กลาง ทำให้มุมมองภาพแคบลง และโหมด 640×480 ให้ความละเอียดไม่เพียงพอ ในทางกลับกัน โหมด 1640×1232 ใช้การทำ binning แบบ 2×2 ซึ่งให้มุมมองภาพที่กว้างกว่า จึงถูกใช้เป็นโหมดเริ่มต้นในปัจจุบัน  
เปิดไฟล์ไดรเวอร์ imx219.c และแก้ไขส่วนที่อธิบายด้านล่างภายในฟังก์ชัน imx219_set_default_format, imx219_open และ imx219_probe
- imx219_set_default_format
    ```
    fmt->width = supported_modes[2].width;
    fmt->height = supported_modes[2].height;
    ```
- imx219_open
    ```
    try_fmt_img->width = supported_modes[2].width;
    try_fmt_img->height = supported_modes[2].height;
    ```
- imx219_probe
    ```
    imx219->mode = &supported_modes[2];
    ```

เนื่องจาก 1920×1080 @ 30fps ตรงกับ Mode 1 จึงต้องเปลี่ยนการอ้างอิง supported_modes ทั้งหมดภายในฟังก์ชันทั้งสามเป็น **“supported_modes[1]”**  
โหมด 1640×1232 @ 30fps ตรงกับ Mode 2 จึงต้องเปลี่ยนเป็น **“supported_modes[2]”** ให้สอดคล้องกัน  
สำหรับ 640×480 @ 30fps ซึ่งสอดคล้องกับ Mode 3 ให้เปลี่ยนการอ้างอิงทั้งหมดเป็น **“supported_modes [3]”**

ประการที่สาม ให้บิลด์เคอร์เนลใหม่และสร้างอิมเมจ FAI  
กลับไปยังไดเรกทอรีบิลด์ และบิลด์เคอร์เนลใหม่โดยใช้คำสั่งด้านล่าง
```
$ cd ${build_dir}/build/ai-g-topst-main/
$ bitbake -C compile linux-topst
$ cd ${build_dir}
$ ./stitch-fai-ai.sh
```

จากนั้นแฟลช output_aig.fai ที่สร้างขึ้นไปยังบอร์ดด้วย FWDN แล้วคุณจะสามารถใช้เซ็นเซอร์ IMX219 ที่ความละเอียดที่ต้องการได้

#### 4.1.4.4 วิธีเพิ่ม FPS ของ IMX219 ใน Yocto: ไดรเวอร์และ Device Tree
ตามคำอธิบายของเซ็นเซอร์ IMX219 เซ็นเซอร์นี้รองรับโหมดอัตราเฟรมสูง เช่น 1080p60, 720p180 และ VGA206 ดังนั้นจึงสามารถเพิ่ม FPS สำหรับความละเอียดที่ไดรเวอร์ imx219.c รองรับ ได้แก่ 1920×1080, 1640×1232 และ 640×480 เนื่องจาก ISP core บนแพลตฟอร์ม AI-G รองรับสูงสุด 60 fps ความละเอียดเหล่านี้จึงสามารถเพิ่มได้สูงสุดถึง 60 fps  

สูตรสำหรับการคำนวณ FPS มีดังนี้
<p align="center"><strong>{fps} = {pixel_rate}/{hts}x{vts}</strong></p>
ดังนั้น เพื่อเพิ่ม FPS จึงต้องปรับค่า pixel_rate, hts และ vts  
ในการใช้งานไดรเวอร์ปัจจุบัน ทั้ง pixel_rate และ hts ถูกกำหนดตายตัว หากต้องการเพิ่ม FPS วิธีเดียวที่ทำได้คือเพิ่ม pixel_rate โดยคง hts ไว้เท่าเดิม แล้วปรับ vts ให้เหมาะสมเพื่อให้ได้อัตราเฟรมที่ต้องการ

หากต้องการแก้ไข FPS เป็น 60 จะต้องอัปเดตทั้งไดรเวอร์และดีไวซ์ทรี
ทำตามคู่มือด้านล่างเพื่อเปลี่ยน FPS เป็น 60

##### 4.1.2.4.1 1920x1080 @ 60fps
เพื่อให้ได้ 60 fps จะต้องเป็นไปตามความสัมพันธ์ต่อไปนี้  
fps = pixel_rate / (hts × vts)
- pixel_rate = 182,400,000
- hts = 3448
- target fps = 60

ค่า VTS ที่ต้องใช้จะเป็นดังนี้
- vts = pixel_rate / (hts × fps) = 182,400,000 / (3448 × 60) ≈ 882

อย่างไรก็ตาม ค่า VTS ต้องมากกว่า 1080 ดังนั้นการกำหนดค่านี้จึงไม่ถูกต้อง  
ดังนั้น เพื่อให้ได้ 60 fps จึงต้องคงค่า hts ไว้คงที่ และปรับค่า pixel_rate, vts รวมถึงรีจิสเตอร์ PLL_VT แทน

รายการที่ต้องเปลี่ยนแปลงมีดังนี้
1. ไฟล์ไดรเวอร์ imx219.c  
    A. เพิ่มอัตราพิกเซลและความถี่ลิงก์
    ```
    #define IMX219_PIXEL_RATE            182400000    →   #define IMX219_PIXEL_RATE            278400000
    #define IMX219_DEFAULT_LINK_FREQ     456000000   →   #define IMX219_DEFAULT_LINK_FREQ     696000000
    ``` 
    B. อัปเดตค่า VTS สำหรับโหมด 1080p:
    ```
    #define IMX219_VTS_30FPS_1080P       0x06e3       →   #define IMX219_VTS_30FPS_1080P       0x0542
    ```
    C. แก้ไขรีจิสเตอร์ PLL_VT ในตารางโหมด 1920x1080:
    ```
    // imx219_reg mode_1920_1080_regs[]
    {0x0307, 0x39}   →   {0x0307, 0x57}
    ```
2. ไฟล์ดีไวซ์ทรี tcc805x-videoinput-mipi0-imx219.dtsi  
    A. อัปเดตความถี่ลิงก์ให้ตรงกับอัตราพิกเซลใหม่:
    ```
    // &i2c7
    /bits/ 64 <456000000> → /bits/ 64 <696000000>
    ```
    B. อัปเดตค่า hs-settle:
    ```
    hs-settle = <13> → hs-settle = <35>
    ```
3. บิลด์เคอร์เนลใหม่และสร้างอิมเมจ FAI  
    กลับไปยังไดเรกทอรีบิลด์ แล้วบิลด์เคอร์เนลใหม่โดยใช้คำสั่งด้านล่าง
    ```
    $ cd ${build_dir}/build/d3-g-topst-main/
    $ bitbake -C compile linux-topst
    $ cd ${build_dir}
    $ ./stitch-fai-d3.sh
    ```
เมื่อใช้คำสั่งด้านล่างบน AI-G จะเห็นได้ว่าค่า FPS ที่แสดงคือ 59.9 ซึ่งตรงกับ 60 fps
```
$ v4l2-ctl --stream-mmap=3 --stream-count=300 --stream-to=/dev/null --verbose
```

##### 4.1.2.4.2 1640x1232 @ 60fps
เพื่อให้ได้ 60 fps จะต้องเป็นไปตามความสัมพันธ์ต่อไปนี้  
fps = pixel_rate / (hts × vts)
- pixel_rate = 182,400,000
- hts = 3448
- target fps = 60

ค่า VTS ที่ต้องใช้จะเป็นดังนี้
- vts = pixel_rate / (hts × fps) = 182,400,000 / (3448 × 60) ≈ 882

อย่างไรก็ตาม ค่า VTS ต้องมากกว่า 1080 ดังนั้นการกำหนดค่านี้จึงไม่ถูกต้อง  
ดังนั้น เพื่อให้ได้ 60 fps จึงต้องคงค่า hts ไว้คงที่ และปรับค่า pixel_rate, vts รวมถึงรีจิสเตอร์ PLL_VT แทน

รายการที่ต้องเปลี่ยนแปลงมีดังนี้
1. ไฟล์ไดรเวอร์ imx219.c  
    A. เพิ่มอัตราพิกเซลและความถี่ลิงก์
    ```
    #define IMX219_PIXEL_RATE            182400000    →   #define IMX219_PIXEL_RATE            278400000
    #define IMX219_DEFAULT_LINK_FREQ     456000000   →   #define IMX219_DEFAULT_LINK_FREQ     696000000
    ``` 
    B. อัปเดตค่า VTS สำหรับโหมด 1640_1232:
    ```
    #define IMX219_VTS_30FPS_BINNED       0x06e3       →   #define IMX219_VTS_30FPS_BINNED       0x0542
    ```
    C. แก้ไขรีจิสเตอร์ PLL_VT ในตารางโหมด 1920x1080:
    ```
    // imx219_reg mode_1640_1232_regs[]
    {0x0307, 0x39}   →   {0x0307, 0x57}
    ```
2. ไฟล์ดีไวซ์ทรี tcc805x-videoinput-mipi0-imx219.dtsi  
    A. อัปเดตความถี่ลิงก์ให้ตรงกับอัตราพิกเซลใหม่:
    ```
    // &i2c7
    /bits/ 64 <456000000> → /bits/ 64 <696000000>
    ```
    B. อัปเดตค่า hs-settle:
    ```
    hs-settle = <13> → hs-settle = <34>
    ```
3. บิลด์เคอร์เนลใหม่และสร้างอิมเมจ FAI  
    กลับไปยังไดเรกทอรีบิลด์ แล้วบิลด์เคอร์เนลใหม่โดยใช้คำสั่งด้านล่าง
    ```
    $ cd ${build_dir}/build/d3-g-topst-main/
    $ bitbake -C compile linux-topst
    $ cd ${build_dir}
    $ ./stitch-fai-d3.sh
    ```
เมื่อใช้คำสั่งด้านล่างบน AI-G จะเห็นได้ว่าค่า FPS ที่แสดงคือ 59.9 ซึ่งตรงกับ 60 fps
```
$ v4l2-ctl --stream-mmap=3 --stream-count=300 --stream-to=/dev/null --verbose
```

##### 4.1.2.4.3 640x480 @ 60fps
เพื่อให้ได้ 60 fps จะต้องเป็นไปตามความสัมพันธ์ต่อไปนี้  
fps = pixel_rate / (hts × vts)
- pixel_rate = 182,400,000
- hts = 3448
- target fps = 60

ค่า VTS ที่ต้องใช้จะเป็นดังนี้
- vts = pixel_rate / (hts × fps) = 182,400,000 / (3448 × 60) ≈ 882

เนื่องจากค่า VTS มากกว่า 480 จึงเป็นไปตามเงื่อนไข เช่นเดียวกับตัวอย่างก่อนหน้านี้ เราจะปรับ pixelrate และ VTS เพื่อเปลี่ยน FPS โดยคงค่า HTS ไว้คงที่  
นอกจากนี้ยังสามารถปรับ FPS โดยการแก้ไขเฉพาะค่า VTS โดยไม่เปลี่ยนค่า pixelrate ได้ อย่างไรก็ตาม ค่ารีจิสเตอร์ 0x0307 ของ IMX219 จะต้องคงไว้โดยไม่เปลี่ยนแปลง

รายการที่ต้องเปลี่ยนแปลงมีดังนี้
1. ไฟล์ไดรเวอร์ imx219.c  
    A. เพิ่มอัตราพิกเซลและความถี่ลิงก์
    ```
    #define IMX219_PIXEL_RATE            182400000    →   #define IMX219_PIXEL_RATE            278400000
    #define IMX219_DEFAULT_LINK_FREQ     456000000   →   #define IMX219_DEFAULT_LINK_FREQ     696000000
    ``` 
    B. อัปเดตค่า VTS สำหรับโหมด 640_480:
    ```
    #define IMX219_VTS_30FPS_640x480       0x06e3       →   #define IMX219_VTS_30FPS_640x480       0x0542
    ```
    C. แก้ไขรีจิสเตอร์ PLL_VT ในตารางโหมด 640x480:
    ```
    // imx219_reg mode_640_480_regs[]
    {0x0307, 0x39}   →   {0x0307, 0x57}
    ```
2. ไฟล์ดีไวซ์ทรี tcc805x-videoinput-mipi0-imx219.dtsi  
    A. อัปเดตความถี่ลิงก์ให้ตรงกับอัตราพิกเซลใหม่:
    ```
    // &i2c7
    /bits/ 64 <456000000> → /bits/ 64 <696000000>
    ```
    B. อัปเดตค่า hs-settle:
    ```
    hs-settle = <13> → hs-settle = <26>
    ```
3. บิลด์เคอร์เนลใหม่และสร้างอิมเมจ FAI  
    กลับไปยังไดเรกทอรีบิลด์ แล้วบิลด์เคอร์เนลใหม่โดยใช้คำสั่งด้านล่าง
    ```
    $ cd ${build_dir}/build/d3-g-topst-main/
    $ bitbake -C compile linux-topst
    $ cd ${build_dir}
    $ ./stitch-fai-d3.sh
    ```
เมื่อใช้คำสั่งด้านล่างบน AI-G จะเห็นได้ว่าค่า FPS ที่แสดงคือ 59.9 ซึ่งตรงกับ 60 fps
```
$ v4l2-ctl --stream-mmap=3 --stream-count=300 --stream-to=/dev/null --verbose
```

## 4.2 คู่มือการตั้งค่ากล้อง GMSL
### 4.2.1 คู่มือการตั้งค่ากล้อง D3-G GMSL
การใช้บอร์ด Deserializer ช่วยให้คุณเชื่อมต่อกล้องได้สูงสุดสี่ตัวเข้ากับพอร์ต MIPI CSI เพียงพอร์ตเดียว เนื่องจาก D3-G มีพอร์ต MIPI CSI สองพอร์ต คุณจึงสามารถเลือกการกำหนดค่าอย่างใดอย่างหนึ่งต่อไปนี้:
- ใช้กล้องสี่ตัวบนพอร์ต MIPI0
- ใช้กล้องสี่ตัวบนพอร์ต MIPI1
- ใช้ทั้ง MIPI0 และ MIPI1 เพื่อเชื่อมต่อกล้องรวมทั้งหมดแปดตัว

เมื่อกำหนดค่ากล้องทั้งแปดตัว ฟังก์ชันขยายการแสดงผลของ D3-G ซึ่งรองรับจอแสดงผลได้สูงสุดสี่จอ จะสามารถใช้งานได้สูงสุดสามจอ

**หมายเหตุ:** คู่มือนี้ใช้กล้อง IMX290 (cxd5700) FHD GMSL  
หากคุณต้องการใช้กล้อง GMSL รุ่นอื่น จะต้องมีการพอร์ตกล้องเพิ่มเติม

#### 4.2.1.1 วิธีใช้พอร์ต MIPI0
ขั้นแรก คุณต้องเปิดใช้งานการกำหนดค่าเคอร์เนลสำหรับทั้งกล้อง GMSL และบอร์ด SerDes  
เพิ่มรายการต่อไปนี้ลงใน  
**{build_dir}/poky/meta-topst-bsp/recipes-kernel/linux/linux-topst/tcc805x/camera.cfg** file.
```
CONFIG_VIDEO_TCC_CXD5700=y
CONFIG_VIDEO_TCC_MAX9275=y
CONFIG_VIDEO_TCC_MAX96712=y
```
To prevent the source code from being removed during the build process, enable the following line, and comment out all occurrences of `TOPST_CAM_MODULE in {build_dir}/build/d3-g-topst-main/conf/local.conf:
```
#TOPST_CAM_MODULE = "ov5647"
#TOPST_CAM_MODULE = "imx219"
```
หลังจากแก้ไขตัวเลือกข้างต้นแล้ว ให้บิลด์อิมเมจใหม่ด้วยคำสั่งต่อไปนี้
```
$ bitbake -c cleansstate isp-firmware
$ bitbake -c cleansstate isp-server
$ bitbake telechips-topst-image
```
ขั้นต่อไป คุณต้องแก้ไขดีไวซ์ทรีในเคอร์เนล ทำตามคู่มือด้านล่างเพื่อใช้การเปลี่ยนแปลงและบิลด์อิมเมจใหม่
1. Modify file {build_dir}/build/d3-g-topst-main/tmp/work/d3_g_topst_main-telechips-linux/linux-topst/5.10.205-r0/git/arch/arm64/boot/dts/telechips/tcc805x/override/tcc8050_53-lpd4x322-sv1.0-videoinput.dtsi as shown below
    ```
    @@ -192,7 +192,7 @@ max9295_1: max9295_1@40 {
            max9286_1: max9286_1@48 {
                    status          = "disabled";
                    compatible      = "tcc-maxim,max9286";
    -               pwd-gpios       = <&gpmc 0 1>;
    +               pwd-gpios       = <&gpg 5 1>;
                    reg             = <0x48>;       // 0x90 >> 1
            };
    @@ -200,7 +200,7 @@ max9286_1: max9286_1@48 {
            max96712_1: max96712_1@2a {
                    status          = "disabled";
                    compatible      = "tcc-maxim,max96712";
    -               pwd-gpios       = <&gpmc 0 1>;
    +               pwd-gpios       = <&gpg 5 1>;
                    reg             = <0x2A>;
            };
    };
    @@ -325,7 +325,7 @@ max9295e: max9295e@42 {
            max9286: max9286@48 {
                    status          = "disabled";
                    compatible      = "tcc-maxim,max9286";
    -               pwd-gpios       = <&gpg 5 1>;
    +               pwd-gpios       = <&gpmc 0 1>;
                    reg             = <0x48>;       // 0x90 >> 1
            };
    @@ -333,7 +333,7 @@ max9286: max9286@48 {
            max96712: max96712@2a {
                    status          = "disabled";
                    compatible      = "tcc-maxim,max96712";
    -               pwd-gpios       = <&gpg 5 1>;
    +              pwd-gpios       = <&gpmc 0 1>;
                    reg             = <0x2A>;
            };
    ```
2. Modify file {build_dir}/build/d3-g-topst-main/tmp/work/d3_g_topst_main-telechips-linux/linux-topst/5.10.205-r0/git/arch/arm64/boot/dts/telechips/tcc805x/override/tcc805x-videoinput-camera-module.dtsi as shown below
    ```
    //#include "tcc805x-videoinput-mipi0-ov5647.dtsi"
    //#include "tcc805x-videoinput-mipi0-imx219.dtsi"
    +#include "tcc805x-videoinput-mipi0-fhd.dtsi"
    ```
3. Create file {build_dir}/build/d3-g-topst-main/tmp/work/d3_g_topst_main-telechips-linux/linux-topst/5.10.205-r0/git/arch/arm64/boot/dts/telechips/tcc805x/override/tcc805x-videoinput-mipi0-fhd.dtsi as shown below
    ```
    // SPDX-License-Identifier: (GPL-2.0-or-later OR MIT)
    /*
    * Copyright (C) Telechips Inc.
    */

    &i2c6 {
        status = "okay";
    };

    &cxd5700_1 {
        /* ISP of camera module */
        status          = "okay";
        port {
                cxd5700_1_out: endpoint {
                        remote-endpoint = <&max9275_1_in>;
                        io-direction    = "output";
                };
        };
    };

    &max9275_1 {
        /* serializer */
        status          = "okay";
        ports {
                #address-cells = <1>;
                #size-cells = <0>;
                port@0 {
                        reg = <0>;
                        max9275_1_in: endpoint {
                                remote-endpoint = <&cxd5700_1_out>;
                                io-direction    = "input";
                        };
                };
                port@1 {
                        reg = <1>;
                        max9275_1_out: endpoint {
                                remote-endpoint = <&max96712_1_in0>;
                                io-direction    = "output";
                        };
                };
        };
    };

    &max96712_1 {
        /* deserializer */
        status          = "okay";
        pvd-name        = "fhd";
        /*
            * broadcasting mode access each linked devices
            * by the same I2C slave address.
            *
            * Also,
            * using the serdes I2C address mapping table,
            * each liked devices can be accessed
            * by the unique I2C slave address.
            */
        broadcasting-mode;
        ports {
                #address-cells = <1>;
                #size-cells = <0>;
                /*
                    * 0 ~ 3
                    * input ports. The number is matched with VC
                    *
                    * 4
                    * output port.
                    */
                port@0 {
                        reg = <0>;
                        max96712_1_in0: endpoint {
                                remote-endpoint = <&max9275_1_out>;
                                io-direction    = "input";
                                channel         = <0>;
                        };
                };
                port@1 {
                        reg = <1>;
                        max96712_1_in1: endpoint {
                                remote-endpoint = <&max9275_1_out>;
                                io-direction    = "input";
                                channel         = <1>;
                        };
                };
                port@2 {
                        reg = <2>;
                        max96712_1_in2: endpoint {
                                remote-endpoint = <&max9275_1_out>;
                                io-direction    = "input";
                                channel         = <2>;
                        };
                };
                port@3 {
                        reg = <3>;
                        max96712_1_in3: endpoint {
                                remote-endpoint = <&max9275_1_out>;
                                io-direction    = "input";
                                channel         = <3>;
                        };
                };
                port@4 {
                        reg = <4>;
                        max96712_1_out: endpoint {
                                remote-endpoint = <&mipi_csi2_0_in>;
                                io-direction    = "output";
                                channel         = <0>;
                        };
                };
        };
    };

    &mipi_csi2_0 {
        status = "okay";
        ports {
                #address-cells = <1>;
                #size-cells = <0>;
                /*
                    * 0
                    * input port.
                    *
                    * 1 ~ 4
                    * output ports. (1: VC0 ~ 4: VC3)
                    */
                port@0 {
                        reg = <0>;
                        mipi_csi2_0_in: endpoint {
                                remote-endpoint = <&max96712_1_out>;
                                io-direction    = "input";
                                num-channel     = <4>;

                                   /*
                                    * 0: CH0 only, no data interleave
                                    * 1: DT only
                                    * 2: VC only
                                    * 3: VC and DT
                                    */
                                interleave-mode = <3>;
                                hs-settle = <37>;
                                data-lanes = <1 2 3 4>;
                        };
                };
                port@1 {
                        reg = <1>;
                        mipi_csi2_0_out0: endpoint {
                                remote-endpoint = <&videoinput4_in>;
                                io-direction    = "output";
                                channel         = <0>;
                                /*
                                    * 0: Single pixel mode
                                    * 1: Dual pixel mode (RAW8/10/12, YUV422)
                                    * 2: Quad pixel mode (RAW8/10/12)
                                    * 3: Invalid
                                    */
                                pixel-mode = <1>;
                        };
                };
                port@2 {
                        reg = <2>;
                        mipi_csi2_0_out1: endpoint {
                                remote-endpoint = <&videoinput5_in>;
                                io-direction    = "output";
                                channel         = <1>;
                                pixel-mode = <1>;
                        };
                };
                port@3 {
                        reg = <3>;
                        mipi_csi2_0_out2: endpoint {
                                remote-endpoint = <&videoinput6_in>;
                                io-direction    = "output";
                                channel         = <2>;
                                pixel-mode = <1>;
                        };
                };
                port@4 {
                        reg = <4>;
                        mipi_csi2_0_out3: endpoint {
                                remote-endpoint = <&videoinput7_in>;
                                io-direction    = "output";
                                channel         = <3>;
                                pixel-mode = <1>;
                        };
                };
        };
    };

    &videoinput4 {
        status          = "okay";
        cifport         = <&cifport             9>;
        /* memory-region
            *  - [0]: parking guideline
            *  - [1]: deinterlacing by viqe
            *  - [2]: preview
            *  - [3]: last frame
            */
        memory-region   = <0
                            0
                            &pmap_rearcamera4
                            0>;
        port {
                videoinput4_in: endpoint {
                        remote-endpoint = <&mipi_csi2_0_out0>;
                        io-direction    = "input";
                        stream-enable   = <1>;  // VIN_CTRL.SE
                        flush-vsync     = <1>;  // VIN_MISC.FVS
                };
        };
    };

    &videoinput5 {
        status          = "okay";
        cifport         = <&cifport             10>;
        /* memory-region
            *  - [0]: parking guideline
            *  - [1]: deinterlacing by viqe
            *  - [2]: preview
            *  - [3]: last frame
            */
        memory-region   = <0
                            0
                            &pmap_rearcamera5
                            0>;
        port {
                videoinput5_in: endpoint {
                        remote-endpoint = <&mipi_csi2_0_out1>;
                        io-direction    = "input";
                        stream-enable   = <1>;  // VIN_CTRL.SE
                        flush-vsync     = <1>;  // VIN_MISC.FVS
                };
        };
    };

    &videoinput6 {
        status          = "okay";
        cifport         = <&cifport             11>;
        /* memory-region
            *  - [0]: parking guideline
            *  - [1]: deinterlacing by viqe
            *  - [2]: preview
            *  - [3]: last frame
            */
        memory-region   = <0
                            0
                            &pmap_rearcamera6
                            0>;
        port {
                videoinput6_in: endpoint {
                        remote-endpoint = <&mipi_csi2_0_out2>;
                        io-direction    = "input";
                        stream-enable   = <1>;  // VIN_CTRL.SE
                        flush-vsync     = <1>;  // VIN_MISC.FVS
                };
           };
    };

    &videoinput7 {
        status          = "okay";
        cifport         = <&cifport             12>;
        /* memory-region
            *  - [0]: parking guideline
            *  - [1]: deinterlacing by viqe
            *  - [2]: preview
            *  - [3]: last frame
            */
        memory-region   = <0
                            0
                            &pmap_rearcamera7
                            0>;
        port {
                videoinput7_in: endpoint {
                        remote-endpoint = <&mipi_csi2_0_out3>;
                        io-direction    = "input";
                        stream-enable   = <1>;  // VIN_CTRL.SE
                        flush-vsync     = <1>;  // VIN_MISC.FVS
                };
        };
    };
    ```
4. Modify file {build_dir}/build/d3-g-topst-main/tmp/work/d3_g_topst_main-telechips-linux/linux-topst/5.10.205-r0/git/arch/arm64/boot/dts/telechips/tcc805x/override/topst-d3-g-i2c.dtsi as shown below
    ```
    @@ -62,10 +62,10 @@ MPQ7920_2_LDO4: ldo4 {

    &i2c6 {
            status = "disabled";
    -       port-mux = <35>;
    +       port-mux = <12>;
            pinctrl-names = "default", "sleep";
    -       pinctrl-0 = <&i2c35_bus_active>;
    -       pinctrl-1 = <&i2c35_bus_sleep>;
    +       pinctrl-0 = <&i2c12_bus_active>;
    +       pinctrl-1 = <&i2c12_bus_sleep>;

            #address-cells = <1>;
            #size-cells = <0>;
    @@ -84,10 +84,10 @@ &i2c3 {

    &i2c7 {
            status = "disabled";
    -       port-mux = <12>;
    +       port-mux = <35>;
            pinctrl-names = "default", "sleep";
    -       pinctrl-0 = <&i2c12_bus_active>;
    -       pinctrl-1 = <&i2c12_bus_sleep>;
    +       pinctrl-0 = <&i2c35_bus_active>;
    +       pinctrl-1 = <&i2c35_bus_sleep>;

            #address-cells = <1>;
            #size-cells = <0>;
    ```
5. Modify file {build_dir}/build/d3-g-topst-main/tmp/work/d3_g_topst_main-telechips-linux/linux-topst/5.10.205-r0/git/arch/arm64/boot/dts/telechips/tcc805x/tcc805x-videoinput.dtsi as shown below
    ```
    @@ -40,26 +40,26 @@ mipi_wrap: mipi_wrap {
                    * 0: select output of MIPI0
                    * 1: select output of MIPI1
                    */
    -               mipi-chmux-0 = <0>;
    +               mipi-chmux-0 = <1>;
                    mipi-chmux-1 = <1>;
    -               mipi-chmux-2 = <0>;
    -               mipi-chmux-3 = <0>;
    +               mipi-chmux-2 = <1>;
    +               mipi-chmux-3 = <1>;

                    /*
                    * 0: select output of MIPI1
                    * 1: select output of MIPI0
                    */
    -               mipi-chmux-4 = <0>;
    -               mipi-chmux-5 = <0>;
    -               mipi-chmux-6 = <0>;
    -               mipi-chmux-7 = <0>;
    +               mipi-chmux-4 = <1>;
    +               mipi-chmux-5 = <1>;
    +               mipi-chmux-6 = <1>;
    +               mipi-chmux-7 = <1>;

                    /*
                    * 1: bypass isp
                    * 0: use isp
                    */
                    isp0-bypass = <0>;
    -               isp1-bypass = <0>;
    +               isp1-bypass = <1>;
                    isp2-bypass = <1>;
                    isp3-bypass = <1>;
    ```
6. Modify file {build_dir}/build/d3-g-topst-main/tmp/work/d3_g_topst_main-telechips-linux/linux-topst/5.10.205-r0/git/include/dt-bindings/pmap/tcc805x/pmap-tcc805x-linux-videoinput.h as shown below
    ```
    @@ -21,13 +21,13 @@
     /* The number of buffers */
    #define FRAMES_CAMERA_VIQE             4
    #define FRAMES_CAMERA_PREVIEW0         4
    -#define FRAMES_CAMERA_PREVIEW1         4
    +#define FRAMES_CAMERA_PREVIEW1         0
    #define FRAMES_CAMERA_PREVIEW2         0
    #define FRAMES_CAMERA_PREVIEW3         0
    -#define FRAMES_CAMERA_PREVIEW4         0
    -#define FRAMES_CAMERA_PREVIEW5         0
    -#define FRAMES_CAMERA_PREVIEW6         0
    -#define FRAMES_CAMERA_PREVIEW7         0
    +#define FRAMES_CAMERA_PREVIEW4         4
    +#define FRAMES_CAMERA_PREVIEW5         4
    +#define FRAMES_CAMERA_PREVIEW6         4
    +#define FRAMES_CAMERA_PREVIEW7         4

    /* Reserved memory size */
    #define PMAP_SIZE_CAMERA_VIQE          \
    ```
7. บิลด์เคอร์เนลใหม่และสร้างอิมเมจ FAI  
    กลับไปยังไดเรกทอรีบิลด์ แล้วบิลด์เคอร์เนลใหม่โดยใช้คำสั่งด้านล่าง
    ```
    $ cd ${build_dir}/build/ai-g-topst-main/
    $ bitbake -C compile linux-topst
    $ cd ${build_dir}
    $ ./stitch-fai-ai.sh
    ```

หลังจากบิลด์เสร็จสมบูรณ์ตามคู่มือด้านบน กล้อง GMSL จะพร้อมใช้งานภายใต้ /dev/ ในชื่อ video4, video5, video6 และ video7

#### 4.2.1.2 วิธีใช้พอร์ต MIPI1
ขั้นแรก คุณต้องเปิดใช้งานการกำหนดค่าเคอร์เนลสำหรับทั้งกล้อง GMSL และบอร์ด SerDes  
เพิ่มรายการต่อไปนี้ลงใน  
**{build_dir}/poky/meta-topst-bsp/recipes-kernel/linux/linux-topst/tcc805x/camera.cfg** file.
```
CONFIG_VIDEO_TCC_CXD5700=y
CONFIG_VIDEO_TCC_MAX9275=y
CONFIG_VIDEO_TCC_MAX96712=y
```
To prevent the source code from being removed during the build process, enable the following line, and comment out all occurrences of `TOPST_CAM_MODULE in {build_dir}/build/d3-g-topst-main/conf/local.conf:
```
#TOPST_CAM_MODULE = "ov5647"
#TOPST_CAM_MODULE = "imx219"
```
หลังจากแก้ไขตัวเลือกข้างต้นแล้ว ให้บิลด์อิมเมจใหม่ด้วยคำสั่งต่อไปนี้
```
$ bitbake -c cleansstate isp-firmware
$ bitbake -c cleansstate isp-server
$ bitbake telechips-topst-image
```

ขั้นต่อไป คุณต้องแก้ไขดีไวซ์ทรีในเคอร์เนล ทำตามคู่มือด้านล่างเพื่อใช้การเปลี่ยนแปลงและบิลด์อิมเมจใหม่
1. Modify file {build_dir}/build/d3-g-topst-main/tmp/work/d3_g_topst_main-telechips-linux/linux-topst/5.10.205-r0/git/arch/arm64/boot/dts/telechips/tcc805x/override/tcc805x-videoinput-camera-module.dtsi as shown below
    ```
    //#include "tcc805x-videoinput-mipi0-ov5647.dtsi"
    //#include "tcc805x-videoinput-mipi0-imx219.dtsi"
    +#include "tcc805x-videoinput-mipi1-fhd.dtsi"
    ```
2. Modify file {build_dir}/build/d3-g-topst-main/tmp/work/d3_g_topst_main-telechips-linux/linux-topst/5.10.205-r0/git/arch/arm64/boot/dts/telechips/tcc805x/tcc805x-videoinput.dtsi as shown below
    ```
    @@ -40,26 +40,26 @@ mipi_wrap: mipi_wrap {
                     * 0: select output of MIPI0
                     * 1: select output of MIPI1
                    */
                    mipi-chmux-0 = <0>;
                    mipi-chmux-1 = <1>;
    +               mipi-chmux-1 = <0>;
                    mipi-chmux-2 = <0>;
                    mipi-chmux-3 = <0>;

                    /*
                    * 0: select output of MIPI1
                    * 1: select output of MIPI0
                    */
                    mipi-chmux-4 = <0>;
                    mipi-chmux-5 = <0>;
                    mipi-chmux-6 = <0>;
                    mipi-chmux-7 = <0>;

                    /*
                    * 1: bypass isp
                    * 0: use isp
                    */
                    isp0-bypass = <0>;
    -               isp1-bypass = <0>;
    +               isp1-bypass = <1>;
                    isp2-bypass = <1>;
                    isp3-bypass = <1>;
    ```
3. Modify file {build_dir}/build/d3-g-topst-main/tmp/work/d3_g_topst_main-telechips-linux/linux-topst/5.10.205-r0/git/include/dt-bindings/pmap/tcc805x/pmap-tcc805x-linux-videoinput.h as shown below
    ```
    @@ -21,13 +21,13 @@
    /* The number of buffers */
    #define FRAMES_CAMERA_VIQE             4
    #define FRAMES_CAMERA_PREVIEW0         4
    -#define FRAMES_CAMERA_PREVIEW1         4
    +#define FRAMES_CAMERA_PREVIEW1         0
    #define FRAMES_CAMERA_PREVIEW2         0
    #define FRAMES_CAMERA_PREVIEW3         0
    -#define FRAMES_CAMERA_PREVIEW4         0
    -#define FRAMES_CAMERA_PREVIEW5         0
    -#define FRAMES_CAMERA_PREVIEW6         0
    -#define FRAMES_CAMERA_PREVIEW7         0
    +#define FRAMES_CAMERA_PREVIEW4         4
    +#define FRAMES_CAMERA_PREVIEW5         4
    +#define FRAMES_CAMERA_PREVIEW6         4
    +#define FRAMES_CAMERA_PREVIEW7         4

    /* Reserved memory size */
    #define PMAP_SIZE_CAMERA_VIQE          \
    ```
4. บิลด์เคอร์เนลใหม่และสร้างอิมเมจ FAI  
    กลับไปยังไดเรกทอรีบิลด์ แล้วบิลด์เคอร์เนลใหม่โดยใช้คำสั่งด้านล่าง
    ```
    $ cd ${build_dir}/build/ai-g-topst-main/
    $ bitbake -C compile linux-topst
    $ cd ${build_dir}
    $ ./stitch-fai-ai.sh
    ```

หลังจากบิลด์เสร็จสมบูรณ์ตามคู่มือด้านบน กล้อง GMSL จะพร้อมใช้งานภายใต้ /dev/ ในชื่อ video4, video5, video6 และ video7

#### 4.2.1.3 วิธีใช้พอร์ต MIPI0, 1
ขั้นแรก คุณต้องเปิดใช้งานการกำหนดค่าเคอร์เนลสำหรับทั้งกล้อง GMSL และบอร์ด SerDes  
เพิ่มรายการต่อไปนี้ลงใน  
**{build_dir}/poky/meta-topst-bsp/recipes-kernel/linux/linux-topst/tcc805x/camera.cfg** file.
```
CONFIG_VIDEO_TCC_CXD5700=y
CONFIG_VIDEO_TCC_MAX9275=y
CONFIG_VIDEO_TCC_MAX96712=y
```

To prevent the source code from being removed during the build process, enable the following line, and comment out all occurrences of `TOPST_CAM_MODULE in {build_dir}/build/d3-g-topst-main/conf/local.conf:
```
#TOPST_CAM_MODULE = "ov5647"
#TOPST_CAM_MODULE = "imx219"
```

หลังจากแก้ไขตัวเลือกข้างต้นแล้ว ให้บิลด์อิมเมจใหม่ด้วยคำสั่งต่อไปนี้
```
$ bitbake -c cleansstate isp-firmware
$ bitbake -c cleansstate isp-server
$ bitbake telechips-topst-image
```

เนื่องจากเส้นทาง display และ videoinput ทับซ้อนกันใน VIOC จึงไม่สามารถใช้การขยายแบบ 4-display ได้ ดังนั้นคุณต้องปิดใช้งานเส้นทางที่ขัดแย้งกันหนึ่งเส้นทางในการตั้งค่า display ก่อน
1. Modify file {build_dir}/build/d3-g-topst-main/tmp/work/d3_g_topst_main-telechips-linux/linux-topst/5.10.205-r0/git/arch/arm64/boot/dts/telechips/tcc805x/override/topst-d3-g-disp.dtsi as shown below
    ```
    @@ -437,7 +437,7 @@ dpv14_tx: dpv14_tx@12400000 {
                    sink_vcp_id = <1 2 3 4>;

                    /* default displayport configuration */
    -               dp-video-codes = <0 16 0 16 0 16 0 16>; /* video standard video codes */
    +               dp-video-codes = <0 16 0 16 0 16>; /* video standard video codes */
                    dp-phy-lane-swap = <1>;
                    dp-max-lane = <4>;
                    dp-max-rate = <3>;
    ```
2. Modify file {build_dir}/build/d3-g-topst-main/tmp/work/d3_g_topst_main-telechips-linux/linux-topst/5.10.205-r0/git/arch/arm64/boot/dts/telechips/tcc805x/override/topst-d3-g-display.dtsi as shown below
    ```
    @@ -34,9 +32,6 @@ &tccdrm_vioc2 {
            status = "okay";
    };

    -&tccdrm_vioc3 {
    -       status = "okay";
    -};

    &vioc0_out {
            vioc0_output_dp0: endpoint@0 {
    @@ -59,13 +54,6 @@ vioc2_output_dp2: endpoint@0 {
            };
    };

    -&vioc3_out {
    -       vioc3_output_dp3: endpoint@0 {
    -               reg = <0>;
    -               remote-endpoint = <&dp3_in_vioc3>;
    -       };
    -};
    -

    /* tcdrm dp */
    &tccdrm_dp0 {
    @@ -80,9 +68,6 @@ &tccdrm_dp2 {
            status = "okay";
    };

    -&tccdrm_dp3 {
    -       status = "okay";
    -};

    /* vioc0_output_dp0 -> dp0_in_vioc0 */
    &dp0_in {
    @@ -108,14 +93,6 @@ dp2_in_vioc2: endpoint@0 {
            };
    };

    -/* vioc3_output_dp3 -> dp3_in_vioc3 */
    -&dp3_in {
    -       dp3_in_vioc3: endpoint@0 {
    -               reg = <0>;
    -               remote-endpoint = <&vioc3_output_dp3>;
    -       };
    -};
    -
    /* screen_share_display_out -> tcc_drm_dummy0  */
    /* screen share */
    &tccdrm_screen_share {
    --
    ```

ขั้นต่อไป คุณต้องแก้ไขดีไวซ์ทรีในเคอร์เนล ทำตามคู่มือด้านล่างเพื่อใช้การเปลี่ยนแปลงและบิลด์อิมเมจใหม่
1. Modify file {build_dir}/build/d3-g-topst-main/tmp/work/d3_g_topst_main-telechips-linux/linux-topst/5.10.205-r0/git/arch/arm64/boot/dts/telechips/tcc805x/override/tcc805x-videoinput-camera-module.dtsi as shown below
    ```
    //#include "tcc805x-videoinput-mipi0-ov5647.dtsi"
    //#include "tcc805x-videoinput-mipi0-imx219.dtsi"
    +#include "tcc805x-videoinput-mipi0-fhd.dtsi"
    +#include "tcc805x-videoinput-mipi1-fhd.dtsi"
    ```
2. Create file {build_dir}/build/d3-g-topst-main/tmp/work/d3_g_topst_main-telechips-linux/linux-topst/5.10.205-r0/git/arch/arm64/boot/dts/telechips/tcc805x/override/tcc805x-videoinput-mipi0-fhd.dtsi as shown below
    ```
    // SPDX-License-Identifier: (GPL-2.0-or-later OR MIT)
    /*
    * Copyright (C) Telechips Inc.
    */

    &i2c7 {
    	status = "okay";
    };

    &cxd5700 {
    	/* ISP of camera module */
    	status		= "okay";
    	port {
		    cxd5700_out: endpoint {
    			remote-endpoint = <&max9275_in>;
			    io-direction	= "output";
		    };
	    };
    };

    &max9275 {
    	/* serializer */
    	status		= "okay";
    	ports {
		    #address-cells = <1>;
		    #size-cells = <0>;
		    port@0 {
    			reg = <0>;
			    max9275_in: endpoint {
    				remote-endpoint = <&cxd5700_out>;
				    io-direction	= "input";
			    };
		    };
		    port@1 {
    			reg = <1>;
			    max9275_out: endpoint {
    				remote-endpoint = <&max96712_in0>;
				    io-direction	= "output";
			    };
		    };
	    };
    };

    &max96712 {
    	/* deserializer */
    	status		= "okay";
    	pvd-name	= "fhd";
    	/*
	    * broadcasting mode access each linked devices
	    * by the same I2C slave address.
	    *
	    * Also,
	    * using the serdes I2C address mapping table,
	    * each liked devices can be accessed
	    * by the unique I2C slave address.
	    */
	    broadcasting-mode;
	    ports {
    		#address-cells = <1>;
		    #size-cells = <0>;
		    /*
		    * 0 ~ 3
		    * input ports. The number is matched with VC
		    *
		    * 4
		    * output port.
		    */
		    port@0 {
    			reg = <0>;
			    max96712_in0: endpoint {
    				remote-endpoint = <&max9275_out>;
				    io-direction	= "input";
				    channel		= <0>;
			    };
		    };
		    port@1 {
    			reg = <1>;
			    max96712_in1: endpoint {
    				remote-endpoint = <&max9275_out>;
				    io-direction	= "input";
				    channel		= <1>;
			    };
		    };
		    port@2 {
    			reg = <2>;
			    max96712_in2: endpoint {
    				remote-endpoint = <&max9275_out>;
				    io-direction	= "input";
				    channel		= <2>;
			    };  
		    };
		    port@3 {
    			reg = <3>;
			    max96712_in3: endpoint {
    				remote-endpoint = <&max9275_out>;
				    io-direction	= "input";
				    channel		= <3>;
			    };
		    };
		    port@4 {
    			reg = <4>;
			    max96712_out: endpoint {
    				remote-endpoint = <&mipi_csi2_0_in>;
				    io-direction	= "output";
				    channel		= <0>;
			    };
		    };
	    };
    };

    &mipi_csi2_0 {
    	status = "okay";
    	ports {
		    #address-cells = <1>;
		    #size-cells = <0>;
		    /*
		    * 0
		    * input port.
		    *
		    * 1 ~ 4
		    * output ports. (1: VC0 ~ 4: VC3)
		    */
		    port@0 {
    			reg = <0>;
			    mipi_csi2_0_in: endpoint {
    				remote-endpoint	= <&max96712_out>;
				    io-direction	= "input";
				    num-channel	= <4>;

				    /*
				    * 0: CH0 only, no data interleave
				    * 1: DT only
				    * 2: VC only
				    * 3: VC and DT
				    */
				    interleave-mode = <3>;
				    hs-settle = <37>;
				    data-lanes = <1 2 3 4>;
			    };
		    };
		    port@1 {
    			reg = <1>;
			    mipi_csi2_0_out0: endpoint {
    				remote-endpoint	= <&videoinput0_in>;
				    io-direction	= "output";
				    channel		= <0>;
				    /*
				    * 0: Single pixel mode
				    * 1: Dual pixel mode (RAW8/10/12, YUV422)
				    * 2: Quad pixel mode (RAW8/10/12)
				    * 3: Invalid
				    */
				    pixel-mode = <1>;
			    };
		    };
		    port@2 {
    			reg = <2>;
	    		mipi_csi2_0_out1: endpoint {
    				remote-endpoint	= <&videoinput1_in>;
				    io-direction	= "output";
				    channel		= <1>;
				    pixel-mode = <1>;
			    };
		    };
		    port@3 {
    			reg = <3>;
			    mipi_csi2_0_out2: endpoint {
    				remote-endpoint	= <&videoinput2_in>;
				    io-direction	= "output";
				    channel		= <2>;
				    pixel-mode = <1>;
			    };
		    };
		    port@4 {
    			reg = <4>;
			    mipi_csi2_0_out3: endpoint {
    				remote-endpoint	= <&videoinput3_in>;
				    io-direction	= "output";
				    channel		= <3>;
				    pixel-mode = <1>;
			    };
		    };
	    };
    };

    &videoinput0 {
    	status		= "okay";
    	cifport		= <&cifport		5>;
    	/* memory-region
	    *  - [0]: parking guideline
	    *  - [1]: deinterlacing by viqe
	    *  - [2]: preview
	    *  - [3]: last frame
	    */
	    memory-region	= <0
			    0
			    &pmap_rearcamera
			    0>;
	    port {
    		videoinput0_in: endpoint {
			    remote-endpoint	= <&mipi_csi2_0_out0>;
			    io-direction	= "input";
			    stream-enable	= <1>;	// VIN_CTRL.SE
			    flush-vsync	= <1>;	// VIN_MISC.FVS
		    };
	    };
    };

    &videoinput1 {
    	status		= "okay";
    	cifport		= <&cifport		6>;
    	/* memory-region
	    *  - [0]: parking guideline
	    *  - [1]: deinterlacing by viqe
	    *  - [2]: preview
	    *  - [3]: last frame
	    */
	    memory-region	= <0
			    0
			    &pmap_rearcamera1
			    0>;
	    port {
    		videoinput1_in: endpoint {
			    remote-endpoint	= <&mipi_csi2_0_out1>;
    			io-direction	= "input";
			    stream-enable	= <1>;	// VIN_CTRL.SE
    			flush-vsync	= <1>;	// VIN_MISC.FVS
		    };
	    };
    };

    &videoinput2 {
    	status		= "okay";
    	cifport		= <&cifport		7>;
    	/* memory-region
	    *  - [0]: parking guideline
	    *  - [1]: deinterlacing by viqe
	    *  - [2]: preview
	    *  - [3]: last frame
	    */
	    memory-region	= <0
			    0
			    &pmap_rearcamera2
			    0>;
	    port {
    		videoinput2_in: endpoint {
			    remote-endpoint	= <&mipi_csi2_0_out2>;
			    io-direction	= "input";
			    stream-enable	= <1>;	// VIN_CTRL.SE
			    flush-vsync	= <1>;	// VIN_MISC.FVS
		    };
	    };
    };

    &videoinput3 {
    	status		= "okay";
	    cifport		= <&cifport		8>;
	    /* memory-region
	    *  - [0]: parking guideline
	    *  - [1]: deinterlacing by viqe
	    *  - [2]: preview
	    *  - [3]: last frame
	    */
	    memory-region	= <0
			    0
			    &pmap_rearcamera3
			    0>;
	    port {
    		videoinput3_in: endpoint {
			    remote-endpoint	= <&mipi_csi2_0_out3>;
			    io-direction	= "input";
			    stream-enable	= <1>;	// VIN_CTRL.SE
			    flush-vsync	= <1>;	// VIN_MISC.FVS
		    };
	    };
    };
    ```
3. Modify file {build_dir}/build/d3-g-topst-main/tmp/work/d3_g_topst_main-telechips-linux/linux-topst/5.10.205-r0/git/arch/arm64/boot/dts/telechips/tcc805x/tcc805x-videoinput.dtsi as shown below
    ```
    @@ -40,26 +40,26 @@ mipi_wrap: mipi_wrap {
                     * 0: select output of MIPI0
                    * 1: select output of MIPI1
                    */
                    mipi-chmux-0 = <0>;
    -               mipi-chmux-1 = <1>;
    +               mipi-chmux-1 = <0>;
                    mipi-chmux-2 = <0>;
                    mipi-chmux-3 = <0>;

                    /*
                    * 0: select output of MIPI1
                    * 1: select output of MIPI0
                    */
                    mipi-chmux-4 = <0>;
                    mipi-chmux-5 = <0>;
                    mipi-chmux-6 = <0>;
                    mipi-chmux-7 = <0>;

                    /*
                    * 1: bypass isp
                    * 0: use isp
                    */
    -               isp0-bypass = <0>;
    -               isp1-bypass = <0>;
    +               isp0-bypass = <1>;
    +               isp1-bypass = <1>;
                    isp2-bypass = <1>;
                    isp3-bypass = <1>;
    ```
4. Modify file {build_dir}/build/d3-g-topst-main/tmp/work/d3_g_topst_main-telechips-linux/linux-topst/5.10.205-r0/git/ include/dt-bindings/pmap/tcc805x/pmap-tcc805x-linux-videoinput.h as shown below
    ```
    @@ -21,13 +21,13 @@
     /* The number of buffers */
    #define FRAMES_CAMERA_VIQE             4
    #define FRAMES_CAMERA_PREVIEW0         4
    #define FRAMES_CAMERA_PREVIEW1         4
    -#define FRAMES_CAMERA_PREVIEW2         0
    -#define FRAMES_CAMERA_PREVIEW3         0
    -#define FRAMES_CAMERA_PREVIEW4         0
    -#define FRAMES_CAMERA_PREVIEW5         0
    -#define FRAMES_CAMERA_PREVIEW6         0
    -#define FRAMES_CAMERA_PREVIEW7         0
    +#define FRAMES_CAMERA_PREVIEW2         0
    +#define FRAMES_CAMERA_PREVIEW3         0
    +#define FRAMES_CAMERA_PREVIEW4         4
    +#define FRAMES_CAMERA_PREVIEW5         4
    +#define FRAMES_CAMERA_PREVIEW6         4
    +#define FRAMES_CAMERA_PREVIEW7         4

    /* Reserved memory size */
    #define PMAP_SIZE_CAMERA_VIQE          \
    ```
5. บิลด์เคอร์เนลใหม่และสร้างอิมเมจ FAI  
    กลับไปยังไดเรกทอรีบิลด์ แล้วบิลด์เคอร์เนลใหม่โดยใช้คำสั่งด้านล่าง
    ```
    $ cd ${build_dir}/build/ai-g-topst-main/
    $ bitbake -C compile linux-topst
    $ cd ${build_dir}
    $ ./stitch-fai-ai.sh
    ```
หลังจากบิลด์เสร็จสมบูรณ์ตามคู่มือด้านบน กล้อง GMSL จะพร้อมใช้งานภายใต้ /dev/ ในชื่อ video0, video1, video2, video3, 4, video5, video6 และ video7

### 4.2.2 คู่มือการตั้งค่ากล้อง AI-G GMSL
การใช้บอร์ด Deserializer ช่วยให้คุณเชื่อมต่อกล้องได้สูงสุดสี่ตัวเข้ากับพอร์ต MIPI CSI เพียงพอร์ตเดียว  
บอร์ด AI-G รองรับแบนด์วิดท์ข้อมูล MIPI CSI ที่ 1.5 Gbps ต่อเลน จึงสามารถใช้งานกล้อง FHD ได้พร้อมกันสูงสุดสามตัว ด้วยเหตุนี้ คู่มือนี้จึงกล่าวถึงการเชื่อมต่อกล้อง FHD GMSL จำนวนสามตัว  
สำหรับกล้อง HD สามารถรองรับได้สูงสุดสี่ตัว

**หมายเหตุ:** คู่มือนี้ใช้กล้อง IMX290 (cxd5700) FHD GMSL  
หากคุณต้องการใช้กล้อง GMSL รุ่นอื่น จะต้องมีการพอร์ตกล้องเพิ่มเติม

#### 4.2.2.1 วิธีใช้พอร์ต MIPI CSI
ขั้นแรก คุณต้องเปิดใช้งานการกำหนดค่าเคอร์เนลสำหรับทั้งกล้อง GMSL และบอร์ด SerDes  
เพิ่มรายการต่อไปนี้ลงใน  
**{build_dir}/poky/meta-topst-bsp/recipes-kernel/linux/linux-topst/tcc750x/camera.cfg** file.
```
CONFIG_VIDEO_TCC_CXD5700=y
CONFIG_VIDEO_TCC_MAX9275=y
CONFIG_VIDEO_TCC_MAX96712=y
```
To prevent the source code from being removed during the build process, enable the following line, and comment out all occurrences of `TOPST_CAM_MODULE in {build_dir}/build/ai-g-topst-main/conf/local.conf:
```
#TOPST_CAM_MODULE = "ov5647"
#TOPST_CAM_MODULE = "imx219"
```
หลังจากแก้ไขตัวเลือกข้างต้นแล้ว ให้บิลด์อิมเมจใหม่ด้วยคำสั่งต่อไปนี้
```
$ bitbake -c cleansstate isp-firmware
$ bitbake -c cleansstate isp-server
$ bitbake telechips-topst-ai-image
```

ขั้นต่อไป คุณต้องแก้ไขดีไวซ์ทรีในเคอร์เนล ทำตามคู่มือด้านล่างเพื่อใช้การเปลี่ยนแปลงและบิลด์อิมเมจใหม่
1. Modify file {build_dir}/build/d3-g-topst-main/tmp/work/d3_g_topst_main-telechips-linux/linux-topst/5.10.205-r0/git/arch/arm64/boot/dts/telechips/tcc805x/override/tcc805x-videoinput-camera-module.dtsi as shown below
    ```
    //#include "tcc805x-videoinput-mipi0-ov5647.dtsi"
    //#include "tcc805x-videoinput-mipi0-imx219.dtsi"
    +#include " tcc750x-videoinput-odw-mipi0-fhd.dtsi"
    ```
2. Modify file {build_dir}/build/d3-g-topst-main/tmp/work/d3_g_topst_main-telechips-linux/linux-topst/5.10.205-r0/git/drivers/media/platform/tcc-mipi-csi2/csi2_s/v2.0/ tcc-mipi-csi2-csis-reg.h. as shown below
    ```
    @@ -6,7 +6,7 @@
    #ifndef TCC_MIPI_CSI2_CSIS_REG_H
    #define TCC_MIPI_CSI2_CSIS_REG_H
    
    -#define MAX_VC                         ((uint32_t)1)
    +#define MAX_VC                         ((uint32_t)4U)
    ```
3. บิลด์เคอร์เนลใหม่และสร้างอิมเมจ FAI  
    กลับไปยังไดเรกทอรีบิลด์ แล้วบิลด์เคอร์เนลใหม่โดยใช้คำสั่งด้านล่าง
    ```
    $ cd ${build_dir}/build/ai-g-topst-main/
    $ bitbake -C compile linux-topst
    $ cd ${build_dir}
    $ ./stitch-fai-ai.sh
    ```
หลังจากบิลด์เสร็จสมบูรณ์ตามคู่มือด้านบน กล้อง GMSL จะพร้อมใช้งานภายใต้ /dev/ ในชื่อ video0, video1 และ video2

# 5. โค้ดตัวอย่างและคำสั่ง
บทนี้ให้ตัวอย่างโค้ดและคำสั่งที่แสดงวิธีการใช้งานกล้อง MIPI CSI กล้อง GMSL และกล้อง USB บนแพลตฟอร์ม D3-G และ AI-G หัวข้อนี้ให้ภาพรวมโดยย่อของวิธีการเล่นภาพจากกล้อง  
บน D3-G สามารถดูสตรีมของกล้องได้โดยใช้ GStreamer หรือ OpenCV  
ในขณะที่บน AI-G การเล่นภาพจากกล้องจะถูกจัดการผ่านเฟรมเวิร์กของแอปพลิเคชัน

## 5.1 โค้ดตัวอย่างและคำสั่งสำหรับการเล่นภาพจากกล้อง
### 5.1.1 คู่มือผู้ใช้กล้อง MIPI CSI
หัวข้อนี้อธิบายวิธีการแสดงภาพวิดีโอจากกล้อง MIPI CSI ทั้งในสภาพแวดล้อม Yocto และ Ubuntu

#### 5.1.1.1 คู่มือผู้ใช้กล้อง MIPI CSI บน D3-G (OV5647)
##### 5.1.1.1.1 การใช้ OV5647 บนอิมเมจ Yocto
เมื่อใช้อิมเมจ Yocto อย่างเป็นทางการที่ให้ไว้ใน [หน้า topst.ai DOCS](https://topst.ai/tech/docs?page=624bd237b3013e87c05c125b8031e2f370ccca2b) หรืออิมเมจที่สร้างขึ้นจากการบิลด์ Yocto ด้วยตนเอง กล้อง OV5647 จะทำงานด้วยความละเอียดเริ่มต้น 1296×972 ที่ 30 fps ดังนั้นการเล่นภาพจากกล้องในสภาพแวดล้อมนี้จะใช้ 1296×972 ที่ 30 fps  
ทำตามขั้นตอนด้านล่างนี้:
1. หยุดบริการ topst-welcome ที่กำลังทำงานอยู่
    ```
    $ sudo systemctl stop topst-welcome
    ```
2. ป้อนคำสั่งต่อไปนี้ในคอนโซล UART
    ```
    $ export XDG_RUNTIME_DIR=/run/user/root
    ```
3. เล่นสตรีมกล้องโดยใช้คำสั่ง GStreamer ดังต่อไปนี้
    ```
    $ gst-launch-1.0 v4l2src device=/dev/video0 io-mode=2 ! video/x-raw,format=NV12,width=1296,height=972,framerate=30/1 ! videoconvert ! waylandsink sync=false
    ```
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/accessories/Camera/5.1%201296%C3%97972%20ov5647%20camera%20out%20display%20on%20yocto.png"></p>
<p align="center"><strong>รูปที่ 5.1 การแสดงผลเอาต์พุตกล้อง OV5647 ขนาด 1296×972 บน Yocto</strong></p>

**หมายเหตุ:** แม้ว่าความละเอียดจะเป็น 1296×972 แต่คุณสามารถเล่นวิดีโอแบบเต็มหน้าจอได้โดยเพิ่มตัวเลือก fullscreen=true ที่ท้ายคำสั่ง

##### 5.1.1.1.2 การใช้ OV5647 บนอิมเมจ Ubuntu
เมื่อใช้อิมเมจ Ubuntu อย่างเป็นทางการที่ให้ไว้ใน [หน้า topst.ai DOCS](https://topst.ai/tech/docs?page=624bd237b3013e87c05c125b8031e2f370ccca2b) กล้อง OV5647 จะทำงานด้วยความละเอียดเริ่มต้น 1296×972 ที่ 30 fps ดังนั้นการเล่นภาพจากกล้องในสภาพแวดล้อมนี้จะใช้ 1296×972 ที่ 30 fps  
ทำตามขั้นตอนด้านล่างนี้:
1. - หากเชื่อมต่อผ่าน UART: ป้อนคำสั่งต่อไปนี้ในคอนโซล UART เมื่อเข้าสู่ระบบด้วยบัญชี topst ของคุณ
    ```
    $ export XDG_RUNTIME_DIR=/run/user/1000
    ```
    - หากควบคุมบนจอแสดงผลโดยตรง: เปิดหน้าต่างเทอร์มินัล
2. เล่นสตรีมจากกล้องโดยใช้คำสั่ง GStreamer ดังที่แสดงด้านล่าง เนื่องจากบน Ubuntu ไม่มีการเรนเดอร์ Wayland แบบเร่งความเร็วด้วยฮาร์ดแวร์ จึงใช้การเข้ารหัส/ถอดรหัส H.265 แทน เพื่อใช้ประโยชน์จากการเร่งความเร็วด้วย VPU ในการเล่น
    ```
    $ gst-launch-1.0 v4l2src device=/dev/video0 io-mode=2 ! video/x-raw,format=NV12,width=1280,height=720,framerate=30/1 ! v4l2h265enc ! h265parse ! v4l2h265dec ! videoconvert ! waylandsink sync=false
    ```
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/accessories/Camera/5.2%201296%C3%97972%20ov5647%20camera%20out%20display%20on%20ubuntu.png"></p>
<p align="center"><strong>รูปที่ 5.2 การแสดงผลเอาต์พุตกล้อง OV5647 ขนาด 1296×972 บน Ubuntu</strong></p>

**หมายเหตุ:** แม้ว่าความละเอียดจะเป็น 1296×972 แต่คุณสามารถเล่นวิดีโอแบบเต็มหน้าจอได้โดยเพิ่มตัวเลือก fullscreen=true ที่ท้ายคำสั่ง

นอกจาก GStreamer แล้ว คุณยังสามารถใช้ OpenCV เพื่อแสดงสตรีมกล้องได้ ทำตามขั้นตอนด้านล่างเพื่อดูตัวอย่างวิดีโอจากกล้องด้วย OpenCV ได้อย่างง่ายดาย
1. ติดตั้ง OpenCV
    ```
    $ sudo apt-get install python3-opencv
    ```
2. เขียนโค้ดต่อไปนี้ในไฟล์ opencv_cam.py
    ```
    import cv2
    
    pipeline = (
        "v4l2src device=/dev/video0 io-mode=2 ! "
        "video/x-raw,format=NV12,width=1296,height=972,framerate=30/1 ! "
        "videoconvert ! video/x-raw,format=BGR ! appsink sync=false"
    )
    
    cap = cv2.VideoCapture(pipeline, cv2.CAP_GSTREAMER)
    
    if not cap.isOpened():
        print("ERROR: cannot open camera via GStreamer")
        exit()
    
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Frame read error")
            break
    
        cv2.imshow("Camera", frame)
        if cv2.waitKey(1) == 27:
            break
    
    cap.release()
    cv2.destroyAllWindows()
    ```
3. รัน opencv_cam.py ด้วย Python
    ```
    $ python3 opencv_cam.py
    ```
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/accessories/Camera/5.3%201296%C3%97972%20opencv%20ov5647%20camera%20out%20display%20on%20ubuntu.png"></p>
<p align="center"><strong>รูปที่ 5.3 เอาต์พุตกล้อง OV5647 ขนาด 1296×972 ที่ทำงานบน Ubuntu ด้วย OpenCV</strong></p>

##### 5.1.1.1.3 การกำหนดค่าไปป์ไลน์ Gstreawmer สำหรับแต่ละความละเอียดบน D3-G
ระบุตัวเลือกไปป์ไลน์ของ GStreamer ที่เหมาะสมสำหรับแต่ละความละเอียด จากนั้นจึงเรียกใช้สตรีมของกล้อง
1. 1920x1080 @ 30fps
    ```
    $ gst-launch-1.0 v4l2src device=/dev/video0 io-mode=2 ! video/x-raw,format=NV12,width=1920,height=1080,framerate=30/1 ! videoconvert ! waylandsink sync=false
    ```
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/accessories/Camera/5.4%201920x1080%20ov5647%20camera%20out%20display%20on%20yocto.png"></p>
    <p align="center"><strong>รูปที่ 5.4 การแสดงผลเอาต์พุตกล้อง OV5647 ที่ 1920x1080 บน Yocto</strong></p>
2. 1296x972 @ 30fps
    ```
    $ gst-launch-1.0 v4l2src device=/dev/video0 io-mode=2 ! video/x-raw,format=NV12,width=1296,height=972,framerate=30/1 ! videoconvert ! waylandsink sync=false
    ```
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/accessories/Camera/5.1%201296%C3%97972%20ov5647%20camera%20out%20display%20on%20yocto.png"></p>
    <p align="center"><strong>รูปที่ 5.5 การแสดงผลเอาต์พุตกล้อง OV5647 ที่ 1296x972 บน Yocto</strong></p>
3. 640x480 @ 60fps
    ```
    $ gst-launch-1.0 v4l2src device=/dev/video0 io-mode=2 ! video/x-raw,format=NV12,width=640,height=480,framerate=60/1 ! videoconvert ! waylandsink sync=false
    ```
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/accessories/Camera/5.6%20640x480%20ov5647%20camera%20out%20display%20on%20yocto.png"></p>
    <p align="center"><strong>รูปที่ 5.6 การแสดงผลเอาต์พุตกล้อง OV5647 ที่ 640x480 บน Yocto</strong></p>

นอกจากนี้ คุณสามารถกำหนดค่าไปป์ไลน์ที่ใช้ตัวเข้ารหัสและตัวถอดรหัส H.265 เพื่อเปิดใช้งานการเล่นแบบเร่งความเร็วด้วยฮาร์ดแวร์ได้
1. 1920x1080 @ 30fps
    ```
    $ gst-launch-1.0 v4l2src device=/dev/video0 io-mode=2 ! video/x-raw,format=NV12,width=1920,height=1080,framerate=30/1 ! v4l2h265enc ! h265parse ! v4l2h265dec ! videoconvert ! waylandsink sync=false
    ```
2. 1296x972 @ 30fps
    ```
    $ gst-launch-1.0 v4l2src device=/dev/video0 io-mode=2 ! video/x-raw,format=NV12,width=1280,height=720,framerate=30/1 !  v4l2h265enc ! h265parse ! v4l2h265dec ! videoconvert ! waylandsink sync=false
    ```
3. 640x480 @ 60fps
    ```
    $ gst-launch-1.0 v4l2src device=/dev/video0 io-mode=2 ! video/x-raw,format=NV12,width=640,height=480,framerate=60/1 ! v4l2h265enc ! h265parse ! v4l2h265dec ! videoconvert ! waylandsink sync=false
    ```

    สำหรับการเปลี่ยนความละเอียด โปรดดูหัวข้อ 4.1.2.2

#### 5.1.1.2 คู่มือผู้ใช้กล้อง MIPI CSI บน D3-G (IMX219)
##### 5.1.1.2.1 การใช้ IMX219 บนอิมเมจ Yocto
เมื่อใช้อิมเมจ Yocto อย่างเป็นทางการที่ให้ไว้ใน [หน้า topst.ai DOCS](https://topst.ai/tech/docs?page=624bd237b3013e87c05c125b8031e2f370ccca2b) หรืออิมเมจที่สร้างขึ้นจากการบิลด์ Yocto ด้วยตนเอง กล้อง IMX219 จะทำงานด้วยความละเอียดเริ่มต้น 1640×1232 ที่ 30 fps ดังนั้นการเล่นภาพจากกล้องในสภาพแวดล้อมนี้จะใช้ 1640×1232 ที่ 30 fps  
ทำตามขั้นตอนด้านล่างนี้:
1. หยุดบริการ topst-welcome ที่กำลังทำงานอยู่
    ```
    $ sudo systemctl stop topst-welcome
    ```
2. ป้อนคำสั่งต่อไปนี้ในคอนโซล UART
    ```
    $ export XDG_RUNTIME_DIR=/run/user/root
    ```
3. เล่นสตรีมกล้องโดยใช้คำสั่ง GSTreamer ดังต่อไปนี้
    ```
    $ gst-launch-1.0 v4l2src device=/dev/video0 io-mode=2 ! video/x-raw,format=NV12,width=1640,height=1232,framerate=30/1 ! videoconvert ! waylandsink sync=false
    ```
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/accessories/Camera/5.7%201640x1232%20imx219%20camera%20out%20display%20on%20yocto.png"></p>
<p align="center"><strong>รูปที่ 5.7 การแสดงผลเอาต์พุตกล้อง IMX219 ขนาด 1640x972 บน Yocto</strong></p>

**หมายเหตุ:** แม้ว่าความละเอียดจะเป็น 1640×1232 แต่คุณสามารถเล่นวิดีโอแบบเต็มหน้าจอได้โดยเพิ่มตัวเลือก fullscreen=true ที่ท้ายคำสั่ง

##### 5.1.1.2.2 การใช้ IMX219 บนอิมเมจ Ubuntu
เมื่อใช้อิมเมจ Ubuntu อย่างเป็นทางการที่ให้ไว้ใน [หน้า topst.ai DOCS](https://topst.ai/tech/docs?page=624bd237b3013e87c05c125b8031e2f370ccca2b) กล้อง IMX219 จะทำงานด้วยความละเอียดเริ่มต้น 1640×1232 ที่ 30 fps ดังนั้นการเล่นภาพจากกล้องในสภาพแวดล้อมนี้จะใช้ 1640×1232 ที่ 30 fps  
ทำตามขั้นตอนด้านล่างนี้:
1. - หากเชื่อมต่อผ่าน UART: ป้อนคำสั่งต่อไปนี้ในคอนโซล UART เมื่อเข้าสู่ระบบด้วยบัญชี topst ของคุณ
    ```
    $ export XDG_RUNTIME_DIR=/run/user/1000
    ```
    - หากควบคุมบนจอแสดงผลโดยตรง: เปิดหน้าต่างเทอร์มินัล
2. เล่นสตรีมจากกล้องโดยใช้คำสั่ง GStreamer ดังที่แสดงด้านล่าง เนื่องจากบน Ubuntu ไม่มีการเรนเดอร์ Wayland แบบเร่งความเร็วด้วยฮาร์ดแวร์ จึงใช้การเข้ารหัส/ถอดรหัส H.265 แทน เพื่อใช้ประโยชน์จากการเร่งความเร็วด้วย VPU ในการเล่น
    ```
    $ gst-launch-1.0 v4l2src device=/dev/video0 io-mode=2 ! video/x-raw,format=NV12,width=1600,height=1200,framerate=30/1 ! v4l2h265enc ! h265parse ! v4l2h265dec ! videoconvert ! waylandsink sync=false
    ```
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/accessories/Camera/5.8%201640x1232%20imx219%20camera%20out%20display%20on%20ubuntu.png"></p>
<p align="center"><strong>รูปที่ 5.8 การแสดงผลเอาต์พุตกล้อง IMX219 ขนาด 1640x972 บน Ubuntu</strong></p>

**หมายเหตุ:** แม้ว่าความละเอียดจะเป็น 1640×1232 แต่คุณสามารถเล่นวิดีโอแบบเต็มหน้าจอได้โดยเพิ่มตัวเลือก fullscreen=true ที่ท้ายคำสั่ง

นอกจาก GStreamer แล้ว คุณยังสามารถใช้ OpenCV เพื่อแสดงสตรีมกล้องได้ ทำตามขั้นตอนด้านล่างเพื่อดูตัวอย่างวิดีโอจากกล้องด้วย OpenCV ได้อย่างง่ายดาย
1. ติดตั้ง OpenCV
    ```
    $ sudo apt-get install python3-opencv
    ```
2. เขียนโค้ดต่อไปนี้ในไฟล์ opencv_cam.py
    ```
    import cv2
    
    pipeline = (
        "v4l2src device=/dev/video0 io-mode=2 ! "
        "video/x-raw,format=NV12,width=1640,height=1232,framerate=30/1 ! "
        "videoconvert ! video/x-raw,format=BGR ! appsink sync=false"
    )
    
    cap = cv2.VideoCapture(pipeline, cv2.CAP_GSTREAMER)
    
    if not cap.isOpened():
        print("ERROR: cannot open camera via GStreamer")
        exit()
    
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Frame read error")
            break
    
        cv2.imshow("Camera", frame)
        if cv2.waitKey(1) == 27:
            break
    
    cap.release()
    cv2.destroyAllWindows()
    ```
3. รัน opencv_cam.py ด้วย Python
```
$ python3 opencv_cam.py
```
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/accessories/Camera/5.9%201640x1232%20opencv%20imx219%20camera%20out%20display.png"></p>
<p align="center"><strong>รูปที่ 5.9 เอาต์พุตกล้อง IMX219 ขนาด 1640×1232 ที่ทำงานบน Ubuntu ด้วย OpenCV</strong></p>

##### 5.1.1.2.3 การกำหนดค่าไปป์ไลน์ GStreamer สำหรับแต่ละความละเอียดบน D3-G
ระบุตัวเลือกไปป์ไลน์ของ GStreamer ที่เหมาะสมสำหรับแต่ละความละเอียด จากนั้นจึงเรียกใช้สตรีมของกล้อง
1. 1920x1080 @ 30fps
    ```
    $ gst-launch-1.0 v4l2src device=/dev/video0 io-mode=2 ! video/x-raw,format=NV12,width=1920,height=1080,framerate=30/1 ! videoconvert ! waylandsink sync=false
    ```
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/accessories/Camera/5.10%201920x1080%20imx219%20camera%20out%20display%20on%20yocto.png"></p>
    <p align="center"><strong>รูปที่ 5.10 การแสดงผลเอาต์พุตกล้อง IMX219 ที่ 1920x1080 บน Yocto</strong></p>
2. 1640x1232 @ 30fps
    ```
    $ gst-launch-1.0 v4l2src device=/dev/video0 io-mode=2 ! video/x-raw,format=NV12,width=1640,height=1232,framerate=30/1 ! videoconvert ! waylandsink sync=false
    ```
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/accessories/Camera/5.7%201640x1232%20imx219%20camera%20out%20display%20on%20yocto.png"></p>
    <p align="center"><strong>รูปที่ 5.11 การแสดงผลเอาต์พุตกล้อง IMX219 ที่ 1620x1232 บน Yocto</strong></p>
3. 640x480 @ 30fps
    ```
    $ gst-launch-1.0 v4l2src device=/dev/video0 io-mode=2 ! video/x-raw,format=NV12,width=640,height=480,framerate=30/1 ! videoconvert ! waylandsink sync=false
    ```
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/accessories/Camera/5.12%20640x480%20imx219%20camera%20out%20display%20on%20yocto.png"></p>
    <p align="center"><strong>รูปที่ 5.12 การแสดงผลเอาต์พุตกล้อง IMX219 ที่ 640x480 บน Yocto</strong></p>

นอกจากนี้ คุณสามารถกำหนดค่าไปป์ไลน์ที่ใช้ตัวเข้ารหัสและตัวถอดรหัส H.265 เพื่อเปิดใช้งานการเล่นแบบเร่งความเร็วด้วยฮาร์ดแวร์ได้
1. 1920x1080 @ 30fps
    ```
    $ gst-launch-1.0 v4l2src device=/dev/video0 io-mode=2 ! video/x-raw,format=NV12,width=1920,height=1080,framerate=30/1 ! v4l2h265enc ! h265parse ! v4l2h265dec ! videoconvert ! waylandsink sync=false
    ```
2. 1640x1232 @ 30fps
    ```
    $ gst-launch-1.0 v4l2src device=/dev/video0 io-mode=2 ! video/x-raw,format=NV12,width=1600,height=1200,framerate=30/1 !  v4l2h265enc ! h265parse ! v4l2h265dec ! videoconvert ! waylandsink sync=false
    ```
3. 640x480 @ 30fps
    ```
    $ gst-launch-1.0 v4l2src device=/dev/video0 io-mode=2 ! video/x-raw,format=NV12,width=640,height=480,framerate=30/1 ! v4l2h265enc ! h265parse ! v4l2h265dec ! videoconvert ! waylandsink sync=false
    ```

สำหรับการเปลี่ยนความละเอียด โปรดดูหัวข้อ 4.1.3.3

#### 5.1.1.3 คู่มือผู้ใช้กล้อง MIPI CSI บน AI-G (OV5647)
##### 5.1.1.3.1 การใช้ OV5647 บนอิมเมจ Yocto
บน AI-G มีแอปพลิเคชันให้ใช้งานสองตัว ได้แก่ ตัวหนึ่งสำหรับการเล่นภาพจากกล้องพร้อมผลการอนุมาน และอีกตัวสำหรับการดูภาพจากกล้องแบบง่าย คุณสามารถเลือกใช้แอปพลิเคชันใดก็ได้ตามกรณีการใช้งาน
- tcnnapp
    ```
    $ tcnnapp
    ```
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/accessories/Camera/5.13%20ov5647%20camera%20out%20display%20with%20running%20tcnnapp%20on%20yocto.png"></p>
    <p align="center"><strong>รูปที่ 5.13 การแสดงผลเอาต์พุตกล้อง OV5647 ขณะรัน tcnnapp บน Yocto</strong></p>
- tcnncameraapp
    ```
    $ tcnncameraapp
    ```
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/accessories/Camera/5.14%20ov5647%20camera%20out%20display%20with%20running%20tcnncameraapp%20on%20yocto.png"></p>
    <p align="center"><strong>รูปที่ 5.14 การแสดงผลเอาต์พุตกล้อง OV5647 ขณะรัน tcnncameraapp บน Yocto</strong></p>

##### 5.1.1.3.2 การใช้งานบนอิมเมจ Ubuntu
บน AI-G มีแอปพลิเคชันให้ใช้งานสองตัว ได้แก่ ตัวหนึ่งสำหรับการเล่นภาพจากกล้องพร้อมผลการอนุมาน และอีกตัวสำหรับการดูภาพจากกล้องแบบง่าย คุณสามารถเลือกใช้แอปพลิเคชันใดก็ได้ตามกรณีการใช้งาน
- tcnnapp
    ```
    $ tcnnapp
    ```
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/accessories/Camera/5.13%20ov5647%20camera%20out%20display%20with%20running%20tcnnapp%20on%20yocto.png"></p>
    <p align="center"><strong>รูปที่ 5.15 การแสดงผลเอาต์พุตกล้อง OV5647 ขณะรัน tcnnapp บน Ubuntu</strong></p>
- tcnncameraapp
    ```
    $ tcnncameraapp
    ```
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/accessories/Camera/5.14%20ov5647%20camera%20out%20display%20with%20running%20tcnncameraapp%20on%20yocto.png"></p>
    <p align="center"><strong>รูปที่ 5.16 การแสดงผลเอาต์พุตกล้อง OV5647 ขณะรัน tcnncameraapp บน Ubuntu</strong></p>

#### 5.1.1.4 คู่มือผู้ใช้กล้อง MIPI CSI บน AI-G (IMX219)
##### 5.1.1.4.1 การใช้ IMX219 บนอิมเมจ Yocto
บน AI-G มีแอปพลิเคชันให้ใช้งานสองตัว ได้แก่ ตัวหนึ่งสำหรับการเล่นภาพจากกล้องพร้อมผลการอนุมาน และอีกตัวสำหรับการดูภาพจากกล้องแบบง่าย คุณสามารถเลือกใช้แอปพลิเคชันใดก็ได้ตามกรณีการใช้งาน
- tcnnapp
    ```
    $ tcnnapp
    ```
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/accessories/Camera/5.17%20imx219%20camera%20out%20display%20with%20running%20tcnnapp%20on%20yocto.png"></p>
    <p align="center"><strong>รูปที่ 5.17 การแสดงผลเอาต์พุตกล้อง OV5647 ขณะรัน tcnnapp บน Yocto</strong></p>
- tcnncameraapp
    ```
    $ tcnncameraapp
    ```
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/accessories/Camera/5.18%20imx219%20camera%20out%20display%20with%20running%20tcnncameraapp%20on%20yocto.png"></p>
    <p align="center"><strong>รูปที่ 5.18 การแสดงผลเอาต์พุตกล้อง OV5647 ขณะรัน tcnncameraapp บน Yocto</strong></p>

##### 5.1.1.4.2 การใช้ IMX219 บนอิมเมจ Ubuntu
บน AI-G มีแอปพลิเคชันให้ใช้งานสองตัว ได้แก่ ตัวหนึ่งสำหรับการเล่นภาพจากกล้องพร้อมผลการอนุมาน และอีกตัวสำหรับการดูภาพจากกล้องแบบง่าย คุณสามารถเลือกใช้แอปพลิเคชันใดก็ได้ตามกรณีการใช้งาน
- tcnnapp
    ```
    $ tcnnapp
    ```
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/accessories/Camera/5.17%20imx219%20camera%20out%20display%20with%20running%20tcnnapp%20on%20yocto.png"></p>
    <p align="center"><strong>รูปที่ 5.17 การแสดงผลเอาต์พุตกล้อง OV5647 ขณะรัน tcnnapp บน Yocto</strong></p>
- tcnncameraapp
    ```
    $ tcnncameraapp
    ```
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/accessories/Camera/5.18%20imx219%20camera%20out%20display%20with%20running%20tcnncameraapp%20on%20yocto.png"></p>
    <p align="center"><strong>รูปที่ 5.18 การแสดงผลเอาต์พุตกล้อง OV5647 ขณะรัน tcnncameraapp บน Yocto</strong></p>

### 5.1.2 คู่มือผู้ใช้กล้อง GMSL
หัวข้อนี้อธิบายวิธีการแสดงภาพวิดีโอจากกล้อง GMSL ทั้งในสภาพแวดล้อม Yocto และ Ubuntu

#### 5.1.2.1 คู่มือผู้ใช้กล้อง GMSL บน D3-G
##### 5.1.2.1.1 การใช้กล้อง GMSL บนอิมเมจ Yocto
เมื่อใช้อิมเมจ Yocto อย่างเป็นทางการที่ให้ไว้ใน [หน้า topst.ai DOCS](https://topst.ai/tech/docs?page=624bd237b3013e87c05c125b8031e2f370ccca2b) หรืออิมเมจที่สร้างขึ้นจากการบิลด์ Yocto ด้วยตนเอง กล้อง GMSL จะทำงานด้วยความละเอียดเริ่มต้น 1920×1080 ที่ 30 fps ดังนั้นการเล่นภาพจากกล้องในสภาพแวดล้อมนี้จะใช้ 1920×1080 ที่ 30 fps  
ทำตามขั้นตอนด้านล่างนี้:
1. หยุดบริการ topst-welcome ที่กำลังทำงานอยู่
    ```
    $ sudo systemctl stop topst-welcome
    ```
2. ป้อนคำสั่งต่อไปนี้ในคอนโซล UART
    ```
    $ export XDG_RUNTIME_DIR=/run/user/root
    ```
3. เล่นสตรีมกล้องโดยใช้คำสั่ง GStreamer ดังต่อไปนี้
    ```
    $ gst-launch-1.0 v4l2src device=/dev/video4 io-mode=2 ! video/x-raw,format=NV12,width=1920,height=1080,framerate=30/1 ! videoconvert ! waylandsink sync=false
    ```

นอกจากนี้ การรันสคริปต์ด้านล่างจะช่วยให้แสดงภาพจากกล้องแบบแบ่งสี่ส่วนโดยใช้ gpu ได้
```
#/bin/bash
 
set -euo pipefail
 
export GST_GL_WINDOW=wayland
export GST_GL_API=gles2
# glimagesink force-aspect-ratio=false sync=false \
 
gst-launch-1.0 -v \
  glvideomixer name=m background=black \
    sink_0::xpos=0   sink_0::ypos=0 \
    sink_1::xpos=960 sink_1::ypos=0 \
    sink_2::xpos=0   sink_2::ypos=540 \
    sink_3::xpos=960 sink_3::ypos=540 ! \
    "video/x-raw,format=RGBA,width=1920,height=1080,framerate=30/1" ! \
  waylandsink sync=false \
  v4l2src device=/dev/video4 io-mode=4 ! \
    video/x-raw,format=NV12,width=1920,height=1080,framerate=30/1 ! \
    glupload ! \
    glcolorscale ! "video/x-raw(memory:GLMemory),width=960,height=540" ! \
    m.sink_0 \
  \
  v4l2src device=/dev/video5 io-mode=4 ! \
    video/x-raw,format=NV12,width=1920,height=1080,framerate=30/1 ! \
    glupload ! \
    glcolorscale ! "video/x-raw(memory:GLMemory),width=960,height=540" ! \
    m.sink_1 \
  \
  v4l2src device=/dev/video6 io-mode=4 ! \
    video/x-raw,format=NV12,width=1920,height=1080,framerate=30/1 ! \
    glupload ! \
    glcolorscale ! "video/x-raw(memory:GLMemory),width=960,height=540" ! \
    m.sink_2 \
  \
  v4l2src device=/dev/video7 io-mode=4 ! \
    video/x-raw,format=NV12,width=1920,height=1080,framerate=30/1 ! \
    glupload ! \
    glcolorscale ! "video/x-raw(memory:GLMemory),width=960,height=540" ! \
    m.sink_3
```

กล้อง GMSL จะปรากฏเป็น video4, video5, video6 และ video7 และคุณสามารถเลือกอุปกรณ์ใดก็ได้ตามต้องการ  
หากเชื่อมต่อกล้องแปดตัว ระบบจะแจกแจงกล้องเหล่านั้นเป็น video0 ถึง video8 ซึ่งคุณสามารถเลือกใช้โหนดอุปกรณ์ใดก็ได้

##### 5.1.2.1.2 การใช้กล้อง GMSL บนอิมเมจ Ubuntu
เมื่อใช้อิมเมจ Ubuntu อย่างเป็นทางการที่ให้ไว้ใน [หน้า topst.ai DOCS](https://topst.ai/tech/docs?page=624bd237b3013e87c05c125b8031e2f370ccca2b) กล้อง GMSL จะทำงานด้วยความละเอียดเริ่มต้น 1920×1080 ที่ 30 fps ดังนั้นการเล่นภาพจากกล้องในสภาพแวดล้อมนี้จะใช้ 1920×1080 ที่ 30 fps  
ทำตามขั้นตอนด้านล่างนี้:
1. - หากเชื่อมต่อผ่าน UART: ป้อนคำสั่งต่อไปนี้ในคอนโซล UART เมื่อเข้าสู่ระบบด้วยบัญชี topst ของคุณ
    ```
    $ export XDG_RUNTIME_DIR=/run/user/1000
    ```
    - หากควบคุมบนจอแสดงผลโดยตรง: เปิดหน้าต่างเทอร์มินัล
2. เล่นสตรีมจากกล้องโดยใช้คำสั่ง GStreamer ดังที่แสดงด้านล่าง เนื่องจากบน Ubuntu ไม่มีการเรนเดอร์ Wayland แบบเร่งความเร็วด้วยฮาร์ดแวร์ จึงใช้การเข้ารหัส/ถอดรหัส H.265 แทน เพื่อใช้ประโยชน์จากการเร่งความเร็วด้วย VPU ในการเล่น
    ```
    $ gst-launch-1.0 v4l2src device=/dev/video0 io-mode=2 ! video/x-raw,format=NV12,width=1920,height=1080,framerate=30/1 ! v4l2h265enc ! h265parse ! v4l2h265dec ! videoconvert ! waylandsink sync=false
    ```

นอกจากนี้ การรันสคริปต์ด้านล่างจะช่วยให้แสดงภาพจากกล้องแบบแบ่งสี่ส่วนโดยใช้ gpu ได้
```
#/bin/bash

set -euo pipefail

export GST_GL_WINDOW=wayland
export GST_GL_API=gles2

gst-launch-1.0 -v \
  glvideomixer name=m background=black \
    sink_0::xpos=0   sink_0::ypos=0 \
    sink_1::xpos=960 sink_1::ypos=0 \
    sink_2::xpos=0   sink_2::ypos=540 \
    sink_3::xpos=960 sink_3::ypos=540 ! \
    glcolorconvert ! "video/x-raw(memory:GLMemory),format=RGBA,width=1920,height=1080,framerate=30/1,pixel-aspect-ratio=1/1" ! \
  glimagesink force-aspect-ratio=false sync=false \
  \
  v4l2src device=/dev/video4 io-mode=4 ! video/x-raw,format=NV12,framerate=30/1,pixel-aspect-ratio=1/1 ! \
    videoconvert ! glupload ! glcolorscale ! \
    "video/x-raw(memory:GLMemory),format=RGBA,width=960,height=540,pixel-aspect-ratio=1/1" ! m.sink_0 \
  \
  v4l2src device=/dev/video5 io-mode=4 ! video/x-raw,format=NV12,framerate=30/1,pixel-aspect-ratio=1/1 ! \
    videoconvert ! glupload ! glcolorscale ! \
    "video/x-raw(memory:GLMemory),format=RGBA,width=960,height=540,pixel-aspect-ratio=1/1" ! m.sink_1 \
  \
  v4l2src device=/dev/video6 io-mode=4 ! video/x-raw,format=NV12,framerate=30/1,pixel-aspect-ratio=1/1 ! \
    videoconvert ! glupload ! glcolorscale ! \
    "video/x-raw(memory:GLMemory),format=RGBA,width=960,height=540,pixel-aspect-ratio=1/1" ! m.sink_2 \
  \
  v4l2src device=/dev/video7 io-mode=4 ! video/x-raw,format=NV12,framerate=30/1,pixel-aspect-ratio=1/1 ! \
    videoconvert ! glupload ! glcolorscale ! \
    "video/x-raw(memory:GLMemory),format=RGBA,width=960,height=540,pixel-aspect-ratio=1/1" ! m.sink_3
```

นอกจากนี้ คุณยังสามารถใช้ OpenCV เพื่อแสดงสตรีมกล้องได้ ทำตามขั้นตอนด้านล่างเพื่อดูตัวอย่างวิดีโอจากกล้องด้วย OpenCV ได้อย่างง่ายดาย
1. ติดตั้ง OpenCV
    ```
    $ sudo apt-get install python3-opencv
    ```
2. เขียนโค้ดต่อไปนี้ในไฟล์ opencv_cam.py
    ```
    import cv2
    
    pipeline = (
        "v4l2src device=/dev/video4 io-mode=2 ! "
        "video/x-raw,format=NV12,width=1920,height=1080,framerate=30/1 ! "
        "videoconvert ! video/x-raw,format=BGR ! appsink sync=false"
    )
    
    cap = cv2.VideoCapture(pipeline, cv2.CAP_GSTREAMER)
    
    if not cap.isOpened():
        print("ERROR: cannot open camera via GStreamer")
        exit()
    
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Frame read error")
            break
    
        cv2.imshow("Camera", frame)
        if cv2.waitKey(1) == 27:
            break
    
    cap.release()
    cv2.destroyAllWindows()
    ```
3. รันไฟล์ opencv_cam.py ด้วย Python
    ```
    $ python3 opencv_cam.py
    ```

กล้อง GMSL จะปรากฏเป็น video4, video5, video6 และ video7 และคุณสามารถเลือกอุปกรณ์ใดก็ได้ตามต้องการ  
หากเชื่อมต่อกล้องแปดตัว ระบบจะแจกแจงกล้องเหล่านั้นเป็น video0 ถึง video8 ซึ่งคุณสามารถเลือกใช้โหนดอุปกรณ์ใดก็ได้

#### 5.1.2.2 คู่มือผู้ใช้กล้อง GMSL บน AI-G
##### 5.1.2.2.1 การใช้กล้อง GMSL บนอิมเมจ Yocto
บน AI-G มีแอปพลิเคชันให้ใช้งานสองตัว ได้แก่ ตัวหนึ่งสำหรับการเล่นภาพจากกล้องพร้อมผลการอนุมาน และอีกตัวสำหรับการดูภาพจากกล้องแบบง่าย คุณสามารถเลือกใช้แอปพลิเคชันใดก็ได้ตามกรณีการใช้งาน
- tcnnapp
- tcnncameraapp

กล้อง GMSL จะปรากฏเป็น **video0**, **video1** และ **video2** และคุณสามารถเลือกอุปกรณ์ใดก็ได้ตามต้องการ
แต่ละแอปพลิเคชันจะใช้ video2 เป็นค่าเริ่มต้น แต่คุณสามารถเปลี่ยนอุปกรณ์วิดีโอได้โดยใช้ **ตัวเลือก -p**
ตัวอย่างด้านล่างแสดงวิธีการเลือก **video0**

- tcnnapp
    ```
    $ tcnnapp -p /dev/video0
    ```
- tcnncameraapp
    ```
    $ tcnncameraapp -p /dev/video0
    ```

##### 5.1.2.2.2 การใช้กล้อง GMSL บนอิมเมจ Ubuntu
บน AI-G มีแอปพลิเคชันให้ใช้งานสองตัว ได้แก่ ตัวหนึ่งสำหรับการเล่นภาพจากกล้องพร้อมผลการอนุมาน และอีกตัวสำหรับการดูภาพจากกล้องแบบง่าย คุณสามารถเลือกใช้แอปพลิเคชันใดก็ได้ตามกรณีการใช้งาน
- tcnnapp
- tcnncameraapp

กล้อง GMSL จะปรากฏเป็น **video0**, **video1** และ **video2** และคุณสามารถเลือกอุปกรณ์ใดก็ได้ตามต้องการ
แต่ละแอปพลิเคชันจะใช้ video2 เป็นค่าเริ่มต้น แต่คุณสามารถเปลี่ยนอุปกรณ์วิดีโอได้โดยใช้ **ตัวเลือก -p**
ตัวอย่างด้านล่างแสดงวิธีการเลือก **video0**

- tcnnapp
    ```
    $ tcnnapp -p /dev/video0
    ```
- tcnncameraapp
    ```
    $ tcnncameraapp -p /dev/video0
    ```

### 5.1.3 คู่มือผู้ใช้กล้อง USB
หัวข้อนี้อธิบายวิธีการแสดงภาพวิดีโอจากกล้อง USB ทั้งในสภาพแวดล้อม Yocto และ Ubuntu
AI-G ไม่มีอินเทอร์เฟซ USB ดังนั้นจึงไม่มีคู่มือกล้อง USB สำหรับแพลตฟอร์มนี้

#### 5.1.3.1 คู่มือผู้ใช้กล้อง USB บน D3-G
ในเอกสารนี้ คำอธิบายจะอ้างอิงจากกล้อง USB ที่รองรับ 1920×1080 ที่ 30 fps

**หมายเหตุ:** เนื่องจากกล้อง MIPI ถูกกำหนดให้เป็น **/dev/video0** ตามค่าเริ่มต้น กล้อง USB จึงถูกสร้างเป็น /dev/video1
โปรดตรวจสอบให้แน่ใจว่าใช้ **/dev/video1** เมื่อใช้งานกล้อง USB

##### 5.1.3.1.1 การใช้กล้อง USB บนอิมเมจ Yocto
เมื่อใช้อิมเมจ Yocto อย่างเป็นทางการที่ให้ไว้ใน [หน้า topst.ai DOCS](https://topst.ai/tech/docs?page=624bd237b3013e87c05c125b8031e2f370ccca2b) หรืออิมเมจที่สร้างขึ้นจากการบิลด์ Yocto ด้วยตนเอง กล้อง USB จะทำงานด้วยความละเอียดและอัตราเฟรมที่กำหนดไว้ตามข้อมูลจำเพาะของกล้องเอง ดังนั้นวิดีโอจะถูกเล่นด้วยความละเอียดและ FPS เริ่มต้นที่กล้อง USB กำหนดไว้  
ทำตามขั้นตอนด้านล่างนี้:
1. หยุดบริการ topst-welcome ที่กำลังทำงานอยู่
    ```
    $ sudo systemctl stop topst-welcome
    ```
2. ป้อนคำสั่งต่อไปนี้ในคอนโซล UART
    ```
    $ export XDG_RUNTIME_DIR=/run/user/root
    ```
3. เล่นสตรีมกล้องโดยใช้คำสั่ง GStreamer ดังต่อไปนี้ เมื่อตรวจสอบข้อมูลกล้อง USB ด้วย v4l2-ctl -d /dev/video1 --list-formats-ext รูปแบบที่รองรับจะแสดงเป็น MJPEG ดังนั้นจึงใช้ jpegdec
    ```
    $ gst-launch-1.0 v4l2src device=/dev/video1 ! image/jpeg,width=1920,height=1080 ! jpegdec ! videoconvert ! waylandsink
    ```

##### 5.1.3.1.2 การใช้กล้อง USB บนอิมเมจ Ubuntu
เมื่อใช้อิมเมจ Ubuntu อย่างเป็นทางการที่ให้ไว้ใน [หน้า topst.ai DOCS](https://topst.ai/tech/docs?page=624bd237b3013e87c05c125b8031e2f370ccca2b) หรืออิมเมจที่สร้างขึ้นเอง กล้อง USB จะทำงานด้วยความละเอียดและอัตราเฟรมที่กำหนดไว้ตามข้อมูลจำเพาะของกล้องเอง ดังนั้นวิดีโอจะถูกเล่นด้วยความละเอียดและ FPS เริ่มต้นที่กล้อง USB กำหนดไว้  
ทำตามขั้นตอนด้านล่างนี้:
1. - หากเชื่อมต่อผ่าน UART: ป้อนคำสั่งต่อไปนี้ในคอนโซล UART เมื่อเข้าสู่ระบบด้วยบัญชี topst ของคุณ
    ```
    $ export XDG_RUNTIME_DIR=/run/user/1000
    ```
    - หากควบคุมบนจอแสดงผลโดยตรง: เปิดหน้าต่างเทอร์มินัล
2. เล่นสตรีมกล้องโดยใช้คำสั่ง GStreamer ดังต่อไปนี้ เมื่อตรวจสอบข้อมูลกล้อง USB ด้วย v4l2-ctl -d /dev/video1 --list-formats-ext รูปแบบที่รองรับจะแสดงเป็น MJPEG ดังนั้นจึงใช้ jpegdec
    ```
    $ gst-launch-1.0 v4l2src device=/dev/video1 ! image/jpeg,width=1920,height=1080 ! jpegdec ! videoconvert ! waylandsink
    ```
3. หากต้องการใช้การเข้ารหัสและถอดรหัส H.265 ต้องแปลงวิดีโอเป็นรูปแบบ NV12 ซึ่ง v4l2src รองรับ ดังนั้นควรกำหนดค่าไปป์ไลน์ดังต่อไปนี้
    ```
    $ gst-launch-1.0 v4l2src device=/dev/video1 io-mode=2 ! image/jpeg,width=640,height=480,framerate=30/1 ! jpegdec ! videoconvert ! video/x-raw,format=NV12 !  v4l2h265enc ! h265parse ! v4l2h265dec ! videoconvert ! waylandsink
    ```

**หมายเหตุ:** คุณสามารถเล่นวิดีโอแบบเต็มหน้าจอได้โดยเพิ่มตัวเลือก fullscreen=true ที่ท้ายคำสั่ง

นอกจาก GStreamer แล้ว คุณยังสามารถใช้ OpenCV เพื่อแสดงสตรีมกล้องได้ ทำตามขั้นตอนด้านล่างเพื่อดูตัวอย่างวิดีโอจากกล้องด้วย OpenCV ได้อย่างง่ายดาย
1. ติดตั้ง OpenCV
    ```
    $ sudo apt-get install python3-opencv
    ```
2. เขียนโค้ดต่อไปนี้ในไฟล์ opencv_cam.py
    ```
    import cv2

    cap = cv2.VideoCapture(1)

    if not cap.isOpened():
        print("\\@@ Camera open failed!")
        exit()

    print("กด 'q' เพื่อออกจากหน้าต่างกล้อง")

    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

    while True:
        ret, frame = cap.read()
        if not ret:
            print("อ่านเฟรมไม่สำเร็จ")
            break

        cv2.imshow("Camera Feed", frame)

        # เมื่อกดปุ่ม 'q' จะออกจากโปรแกรม
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
    ```
3. รัน opencv_cam.py ด้วย Python
    ```
    $ python3 opencv_cam.py
    ```

The USB camera used in this guide operates over USB 2.0, which imposes bandwidth limitations. As a result, higher-resolution video capture is not supported when using OpenCV. If higher resolutions are required, it is recommended to use a USB 3.0 camera, which provides sufficient bandwidth for high-definition video streams.  
Alternatively, OpenCV can be used with higher resolutions by constructing the capture pipeline through GStreamer, as shown below.
1. Write the following code inside the gstreamer_opencv_cam.py file
    ```
    import cv2

    pipeline = (
        "v4l2src device=/dev/video1 ! "
        "image/jpeg,width=1920,height=1080,framerate=30/1 ! "
        "jpegdec ! videoconvert ! video/x-raw,format=BGR ! "
        "appsink drop=1 max-buffers=2"
    )

    print("กำลังเปิดไปป์ไลน์...")
    cap = cv2.VideoCapture(pipeline, cv2.CAP_GSTREAMER)

    if not cap.isOpened():
        print("เปิดไปป์ไลน์ไม่สำเร็จ")
        exit()

    print("กด 'q' เพื่อออกจากหน้าต่างกล้อง")

    while True:
        ret, frame = cap.read()
        if not ret:
            print("อ่านเฟรมไม่สำเร็จ")
            break

        cv2.imshow("USB Camera 1080p MJPG", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
    ```
2. Run gstreamer_opencv_cam.py with Python
    ```
    $ python3 gstreamer_opencv_cam.py
    ```

# 6. การแก้ไขปัญหา
บทที่ 6 ครอบคลุมการแก้ไขปัญหาสำหรับกล้อง MIPI CSI, กล้อง GMSL และกล้อง USB

## 6.1 การแก้ไขปัญหากล้อง MIPI CSI และ GMSL
หากคุณพบปัญหากับกล้อง MIPI CSI หรือ GMSL โปรดดูคู่มือการดีบักด้านล่างเพื่อแก้ไขปัญหา

### 6.1.1 ปัญหาระหว่างการบูต (ขั้นตอนโพรบ)
#### 6.1.1.1 การโพรบเซ็นเซอร์ล้มเหลว
**อาการ**
- ไม่พบเซ็นเซอร์ระหว่างการบูต
- ไม่มีการสร้างโหนด /dev/videoX
- ไม่พบเอนทิตีของเซ็นเซอร์ในผลลัพธ์ของ ‘media-ctrl -p’  

**ตัวอย่างล็อก dmesg**
```
[    3.421000] imx219 2-0010: probing sensor failed
[    3.421120] imx219 2-0010: i2c read failed: addr=0x3000, ret=-5
[    3.200400] imx219 0-0010: reset gpio request failed
[    2.912830] imx219 1-0010: failed to get vddio regulator
```
**สาเหตุที่เป็นไปได้**
- ที่อยู่ I2C หรือการกำหนดค่าบัสไม่ถูกต้อง
- ขั้วของ RESET/PWDN GPIO ไม่ถูกต้อง
- แหล่งจ่ายไฟ regulator ขาดหายไปหรือกำหนดค่าไม่ถูกต้อง

**วิธีแก้ไข**
- ตรวจสอบที่อยู่ I2C หมายเลขบัส และการตั้งค่า GPIO ใน device tree
- ตรวจสอบว่ามีโหนด regulator ที่ขาดหายไปหรือกำหนดไว้ไม่ถูกต้องหรือไม่
- ตรวจสอบทิศทางของสายเคเบิลโมดูลเซ็นเซอร์และการจัดเรียงพินอีกครั้ง

#### 6.1.1.2 การสื่อสาร I2C ล้มเหลว
**ตัวอย่างล็อก dmesg**
```
[    3.101001] imx219 2-0010: i2c read error: -121
[    4.112121] i2c i2c-2: transfer failed: -110
```
**สาเหตุที่เป็นไปได้**
- สาย SDA/SCL ลัดวงจรหรือขาดการเชื่อมต่อ
- หมายเลขบัส I2C ใน device tree ไม่ตรงกับการกำหนดค่าฮาร์ดแวร์จริง

**วิธีแก้ไข**
- ใช้ “i2cdetect -y <bus>” เพื่อตรวจสอบว่าเซ็นเซอร์ตอบสนองที่ที่อยู่ I2C ที่คาดไว้หรือไม่
- ตรวจสอบสายเคเบิลและขั้วต่อว่าชำรุด เสียบไม่แน่น หรือหน้าสัมผัสหลวมหรือไม่

### 6.1.2 ปัญหาการกำหนดค่า Media Controller และกราฟ
(ตรวจสอบโดยใช้ ‘media-ctl -p’)

#### 6.1.2.1 ไม่พบเอนทิตีเซ็นเซอร์หรือลิงก์ยังไม่ได้กำหนดค่า
**ตัวอย่างเอาต์พุตของ 'media-ctl -p'**
```
0 entities, 0 interfaces, 0 pads, 0 links
```
**สาเหตุที่เป็นไปได้**
- ไม่มีโหนด endpoint (port) ใน device tree
- จำนวนเลนหรือการตั้งค่า ‘bus-type’ ไม่ถูกต้อง
- ไม่มีรายการ ‘link-frequencies’

**วิธีแก้ไข**
- ตรวจสอบความถูกต้องของนิยาม endpoint ‘port@0/1’
- ตรวจสอบอาร์เรย์ ‘data-lanes’ ว่ามีลำดับและจำนวนเลนถูกต้อง
- ตรวจสอบให้แน่ใจว่า ‘link-frequencies’ ตรงกับข้อมูลจำเพาะของเซ็นเซอร์

#### 6.1.2.2 รูปแบบ / โหมดไม่ตรงกัน
**สาเหตุที่เป็นไปได้**
- ‘supported_mode[]’ ในไดรเวอร์เซ็นเซอร์ไม่ตรงกับค่า ‘hs-settle’ ที่กำหนดไว้ใน DTS
- จำนวนเลน CSI-2 ระหว่างไดรเวอร์กับ device tree ไม่ตรงกัน

**วิธีแก้ไข**
- ตรวจสอบความละเอียด pixel rate และค่า HTS/VTS ใน ‘supported_modes[]’ จากนั้นปรับค่า ‘hs-settle’ ใน DTS ให้สอดคล้องกัน
- ตรวจสอบให้แน่ใจว่าการตั้งค่า DTS สอดคล้องกับการตั้งค่าไดรเวอร์เซ็นเซอร์

### 6.1.3 ปัญหาการสตรีม V4L2
#### 6.1.3.1 VIDIOC_STREAMON ล้มเหลว (ไม่สามารถเริ่มการสตรีมได้)
**สาเหตุที่เป็นไปได้**
- การกำหนดค่ารีจิสเตอร์ของเซ็นเซอร์ไม่ถูกต้อง
- ค่า pixel rate หรือการตั้งค่า PLL ไม่ตรงกับค่าที่คาดไว้
- ความขัดแย้งของ HTS/VTS ทำให้ไทม์มิงของเฟรมไม่ถูกต้อง

**วิธีแก้ไข**
- ตรวจสอบค่า pixel rate, VTS และ HTS ในตารางโหมดของเซ็นเซอร์อีกครั้ง
- ตรวจสอบค่าตัวหาร PLL (รีจิสเตอร์ 0x030x) ว่าถูกต้องหรือไม่
- ตรวจสอบว่า device tree ระบุค่า ‘hs-settle’ ที่ถูกต้องสำหรับความละเอียดและ FPS ที่เลือก.

#### 6.1.3.2 การร้องขอรูปแบบที่ไม่รองรับ
**วิธีแก้ไข**
- ตรวจสอบฟอร์แมตที่รองรับจริงโดยใช้คำสั่งด้านล่าง จากนั้นลองสตรีมใหม่ด้วยฟอร์แมตที่รองรับ:
    ```
    V4l2-ctl –list-formats-ext
    ```

### 6.1.4 ข้อผิดพลาด CSI-2: SoT, CRC และปัญหาที่เกี่ยวข้อง
#### 6.1.4.1 ข้อผิดพลาด SoT (Sync on Transmission)
**สาเหตุที่เป็นไปได้**
- การกำหนดค่าไทม์มิง MIPI ไม่ตรงกัน
- ตั้งค่า pixel rate สูงเกินไป
- คุณภาพสายเคเบิลต่ำหรือสายยาวเกินไป

**วิธีแก้ไข**
- ลดค่า pixel rate หรือความถี่ลิงก์
- เปลี่ยนสายเคเบิลหรือลดความยาวของสาย
- ตรวจสอบพารามิเตอร์ไทม์มิงของ MIPI

#### 6.1.4.2 ข้อผิดพลาด CRC
**ตัวอย่างล็อก dmesg**
```
[   13.700910] tccvin videoinput0: CSI-2 ERROR: CRC error
```
**สาเหตุที่เป็นไปได้**
- คุณภาพสัญญาณ MIPI ลดลง
- PLL หรือความเร็วเลนไม่ตรงกัน

**วิธีแก้ไข**
- ปรับค่า hs-settle
- เปลี่ยนสายเคเบิล
- ตรวจสอบการกำหนดค่า PLL และการตั้งค่าความเร็วเลน

### 6.1.5 ข้อผิดพลาดอัตราพิกเซล / ความถี่ลิงก์
**สาเหตุที่เป็นไปได้**
- ใช้แบนด์วิดท์เลน CSI-2 เกินกว่าที่มีอยู่
- การกำหนดค่า PLL ไม่ถูกต้อง

**วิธีแก้ไข**
- คำนวณ pixel rate ใหม่และตรวจสอบว่าอยู่ในแบนด์วิดท์ CSI-2 ที่อนุญาต
- ปรับตัวหารความถี่ของ PLL เพื่อให้ได้ไทม์มิงที่ถูกต้อง
- หากจำเป็น ให้ลดอัตราเฟรม (เช่น 30 -> 15fps) หรือลดความละเอียด

### 6.1.6 ข้อผิดพลาดการกำหนดค่า Device Tree (DTS)
#### 6.1.6.1 สตริง compatible ที่ไม่เข้ากัน
**สาเหตุที่เป็นไปได้**
- ค่า ‘compatible’ ใน DTS ไม่ตรงกับ ‘of_device_id’ ที่กำหนดไว้ในไดรเวอร์เซ็นเซอร์
- ไดรเวอร์ไม่รู้จักโหนดอุปกรณ์ ทำให้ไม่มีการเรียกใช้ probe

**วิธีแก้ไข**
- อัปเดต DTS ด้วยสตริง ‘compatible’ ที่ถูกต้องตามที่กำหนดไว้ในไดรเวอร์เซ็นเซอร์ (เช่น “sony,imx219”)
- สร้าง device tree ใหม่และตรวจสอบว่าเซ็นเซอร์ทำ probe ได้อย่างถูกต้อง

#### 6.1.6.2 ปัญหาการกำหนดค่าเอนด์พอยต์
**สาเหตุที่เป็นไปได้**
- หมายเลขพอร์ตหรือการอ้างอิง ‘remote-endpoint’ ระหว่าง endpoint ของเซ็นเซอร์กับ endpoint ของ CSI ไม่ตรงกัน
- ‘data-lanes’ หรือการกำหนดค่าบัสไม่เป็นไปตามข้อกำหนดของ media graph

**วิธีแก้ไข**
- ตรวจสอบให้แน่ใจว่าหมายเลขพอร์ต ‘data-lanes’ และ ‘remote-endpoint’ ตรงกันทั้งสองฝั่ง
- ใช้ ‘media-ctl -p’ เพื่อตรวจสอบว่าลิงก์สื่อถูกสร้างขึ้นอย่างถูกต้อง

#### ไม่มีพร็อพเพอร์ตี้ Link-Frequencies
**สาเหตุที่เป็นไปได้**
- ไม่มีฟิลด์ ‘link-frequencies’ ใน endpoint ทำให้ไม่สามารถคำนวณความเร็วลิงก์ MIPI ได้
- รูปแบบของค่า (เช่น /bits/ 64) ไม่ตรงกับที่ไดรเวอร์คาดหวัง

**วิธีแก้ไข**
- เพิ่มค่า ‘link-frequencies’ ที่ถูกต้อง (เช่น 456000000) ตามข้อมูลจำเพาะของเซ็นเซอร์
- ตรวจสอบให้แน่ใจว่ารูปแบบของค่าตรงตามข้อกำหนดของไดรเวอร์ (เช่น การใส่ /bits/ 64 หากจำเป็น)

### 6.1.7 ปัญหาการเล่นภาพด้วย Gstreamer
#### 6.1.7.1 ข้อผิดพลาด 'not negotiated'
**สาเหตุที่เป็นไปได้**
- การเจรจา Caps ภายในไปป์ไลน์ล้มเหลว
- ฟอร์แมตของ Wayland compositor ไม่ตรงกัน
- videoconvert ไม่สามารถจัดการฟอร์แมต raw บางรูปแบบได้

**วิธีแก้ไข**
- ใช้ไปป์ไลน์ที่อิงกับ NV12 หรือ YUY2 ซึ่งมีความเข้ากันได้กว้างขวาง
- ใช้ ‘v4l2src io-mode=dmabuf’ เพื่อให้มีการจัดการบัฟเฟอร์แบบ zero-copy และการเจรจาฟอร์แมตที่ถูกต้อง

#### 6.1.7.2 การเริ่มต้น Wayland Sink ล้มเหลว
**สาเหตุที่เป็นไปได้**
- Wayland compositor ไม่ทำงาน หรือไม่มีสภาพแวดล้อมการแสดงผลที่เข้าถึงได้
- ไปป์ไลน์ถูกเรียกใช้ผ่าน SSH หรือด้วยสภาพแวดล้อม DISPLAY/Wayland ที่ไม่ถูกต้อง ทำให้ไม่สามารถเริ่มต้น sink ได้

**วิธีแก้ไข**
- ตรวจสอบว่า Weston compositor กำลังทำงานอยู่
- รันไปป์ไลน์ภายในเซสชันในเครื่อง หรือในสภาพแวดล้อม Wayland ที่ตั้งค่าไว้อย่างถูกต้อง

### 6.1.8 ปัญหาฮาร์ดแวร์
#### 6.1.8.1 ทิศทางของสายเคเบิลไม่ถูกต้อง
**สาเหตุที่เป็นไปได้**
- สาย FFC เชื่อมต่อผิดทิศทางหรือพินไม่ตรงแนว ทำให้ส่งสัญญาณ I2C/MIPI ได้ไม่ถูกต้อง
- เซ็นเซอร์ไม่ตอบสนองเลย ส่งผลให้ไม่ได้รับเฟรมใด ๆ

**วิธีแก้ไข**
- ตรวจสอบทิศทางของขั้วต่อ และตรวจสอบให้แน่ใจว่าพินหน้าสัมผัสจัดเรียงตามข้อมูลจำเพาะ
- ตรวจสอบความเสียหายของสายเคเบิลหรือหน้าสัมผัสที่สึกหรอ

#### 6.1.8.2 ปัญหาแหล่งจ่ายไฟ
**สาเหตุที่เป็นไปได้**
- แรงดันไฟเลี้ยงของเซ็นเซอร์ (เช่น 1.2V / 2.8V) ไม่เสถียรหรือไม่ได้เปิดใช้งาน
- ไม่ได้ยืนยันสัญญาณ GPIO สำหรับเปิดใช้งานแหล่งจ่ายไฟ
- ลำดับการจ่ายไฟของเซ็นเซอร์ไม่เป็นไปตามข้อกำหนดระหว่างการเริ่มต้นระบบ

**วิธีแก้ไข**
- ตรวจสอบการกำหนดค่า regulator และ GPIO ใน DTS และยืนยันว่ามีการจ่ายแรงดันไฟฟ้าที่จำเป็นทั้งหมดอย่างถูกต้อง
- ตรวจสอบให้แน่ใจว่าเป็นไปตามข้อกำหนดลำดับการจ่ายไฟของเซ็นเซอร์ (RESET _> PWDN -> clock enable)

## 6.2 การแก้ไขปัญหากล้อง USB
หากคุณพบปัญหากับ USB Camera โปรดดูคู่มือการดีบักด้านล่างเพื่อแก้ไขปัญหา

### 6.2.1 ตรวจไม่พบกล้อง (ไม่รู้จักอุปกรณ์ USB)
**ตัวอย่างล็อก dmesg**
```
usb 1-1: device descriptor read/64, error -71
uvcvideo: Failed to initialize the device
```
**สาเหตุที่เป็นไปได้**
- กำลังไฟ USB ไม่เพียงพอหรือจ่ายไฟไม่เสถียร ทำให้การเริ่มต้นอุปกรณ์ล้มเหลว
- สายหรือพอร์ต USB ชำรุด หรือใช้ USB hub ที่ไม่รองรับ

**วิธีแก้ไข**
- ลองใช้พอร์ต USB อื่น หรือใช้พอร์ตที่มีแหล่งจ่ายไฟเสถียร
- เปลี่ยนสายหรือ hub USB แล้วเชื่อมต่ออุปกรณ์ใหม่เพื่อให้มีการ enumerate อย่างถูกต้อง

### 6.2.2 รายการรูปแบบใน v4l2-ctl จำกัดหรือว่างเปล่า
**ตัวอย่างล็อก dmesg**
```
uvcvideo: Failed to query (GET_DEF) UVC control 2 on unit 1: -32
```
**สาเหตุที่เป็นไปได้**
- กล้องไม่รองรับการควบคุม UVC บางรายการ หรือไม่รายงานรายการเหล่านั้นระหว่างการเริ่มต้นระบบ
- ข้อผิดพลาดของโปรโตคอลระหว่างอุปกรณ์กับไดรเวอร์ทำให้ตรวจไม่พบความสามารถของอุปกรณ์

**วิธีแก้ไข**
- ทดสอบโดยใช้ฟอร์แมตมาตรฐาน เช่น MJPEG หรือ YUYV
- ทดสอบด้วยกล้องรุ่นเดียวกันอีกตัวเพื่อพิจารณาว่าปัญหาเกี่ยวข้องกับความเข้ากันได้ของ UVC หรือไม่

### 6.2.3 การเล่นภาพด้วย GStreamer: "not negotiated" หรือ Caps ไม่ตรงกัน
**สาเหตุที่เป็นไปได้**
- ไปป์ไลน์ร้องขอฟอร์แมตที่กล้องไม่รองรับ (เช่น NV12, YUY2) ส่งผลให้การเจรจา caps ล้มเหลว
- ที่ความละเอียด/อัตราเฟรมที่เลือก กล้องอาจให้ได้เฉพาะ MJPEG แต่ไปป์ไลน์ร้องขอรูปแบบ raw
- กล้องส่งออกเป็น MJPEG แต่ไม่ได้รวมเอลิเมนต์ตัวถอดรหัส JPEG (jpegdec หรือ avdec_mjpeg) จึงไม่สามารถถอดรหัสได้

**วิธีแก้ไข**
- ตรวจสอบฟอร์แมตที่รองรับ
    ```
    v4l2-ctl –list-formats-ext
    ```
- หากกล้องส่งออกเป็น MJPEG:
    ```
    v4l2src ! image/jpeg ! jpegdec ! videoconvert ! …
    ```
- หากกล้องรองรับฟอร์แมต raw (เช่น YUYV) ให้ตั้งค่า caps ของไปป์ไลน์ให้สอดคล้องกัน:  
    ใช้รูปแบบ raw ตามที่แสดงใน ‘v4l2-ctl –list-formats-ext’ ทุกประการ

### 6.2.4 การตั้งค่าความละเอียดหรือ FPS ล้มเหลว
**สาเหตุที่เป็นไปได้**
- กล้องไม่รองรับความละเอียดหรืออัตราเฟรมที่ร้องขอ ส่งผลให้การเจรจาล้มเหลว

**วิธีแก้ไข**
- ตรวจสอบชุดความละเอียด/FPS ที่รองรับโดยใช้ ‘v4l2-ctl –list-formats-ext’

### 6.2.5 วิดีโอกระตุก / เฟรมตกหล่น
**สาเหตุที่เป็นไปได้**
- แบนด์วิดท์ USB ไม่เพียงพอ (ใช้ hub ร่วมกันหรือใช้พอร์ต USB 2.0)
- โหลด CPU สูงจากการถอดรหัส MJPEG ทำให้ไปป์ไลน์ทำงานตามไม่ทัน

**วิธีแก้ไข**
- ใช้พอร์ต USB 3.0 หรือเชื่อมต่อกล้องโดยตรงโดยไม่ผ่าน hub
- ลดความละเอียดหรืออัตราเฟรมของ MJPEG หรือเปลี่ยนไปใช้ฟอร์แมต raw หากรองรับ

### 6.2.6 สีไม่ถูกต้องหรือเอาต์พุตเสียหาย
**สาเหตุที่เป็นไปได้**
- เกิดข้อผิดพลาดระหว่างการแปลง MJPEG -> NV12 หรือการแปลงปริภูมิสี
- ชุดฟอร์แมตบางชุดอาจทำงานล้มเหลวใน v4l2convert หรือ videoconvert

**วิธีแก้ไข**
- แทรก jpegdec หรือ avdec_mjpeg ไว้ก่อน videoconvert อย่างชัดเจน
- ลดความซับซ้อนของไปป์ไลน์เพื่อการทดสอบ ตัวอย่างเช่น:
    ```
    V4l2src ! jpegdec ! videoconvert ! waylandsink
    ```

### 6.2.7 อุปกรณ์ตัดการเชื่อมต่อหรือถูกแจงนับใหม่โดยไม่คาดคิด
**ตัวอย่างล็อก dmesg**
```
usb 1-1: USB disconnect, device number 4
```
**สาเหตุที่เป็นไปได้**
- การจ่ายไฟไม่เสถียรหรือหน้าสัมผัสของสายไม่ดี
- ปัญหาความร้อนทำให้อุปกรณ์รีเซ็ตระหว่างการใช้งานเป็นเวลานาน

**วิธีแก้ไข**
- เปลี่ยนสาย USB หรือใช้พอร์ตที่จ่ายไฟได้เสถียรและเพียงพอ
- สำหรับกล้องที่เกิดความร้อนสูง ควรพิจารณาเพิ่มวิธีการระบายความร้อน
