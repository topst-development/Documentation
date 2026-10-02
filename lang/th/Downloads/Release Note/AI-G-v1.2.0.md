# บันทึกการเผยแพร่ AI-G - v1.2.0

## ที่เก็บโค้ดที่อัปเดต

- [tc-nn-app](https://github.com/topst-development/tc-nn-app)
- [libtc-ndnpu](https://github.com/topst-development/libtc-ndnpu)
- [tc-compiled-nn](https://github.com/topst-development/tc-compiled-nn)
- [meta-topst](https://github.com/topst-development/meta-topst)

## คุณสมบัติใหม่

- เปลี่ยนโมเดลตรวจจับวัตถุเริ่มต้นของ `tcnnapp` และโมเดลทดสอบเริ่มต้นของ `tcnputestapp` จาก YOLOv5s เป็น YOLOv8s

## การปรับปรุง

- ปรับปรุงการคืนหน่วยความจำของแอปพลิเคชัน การตรวจสอบช่วงของอินพุตและเอาต์พุต และการรายงานข้อผิดพลาดระหว่างการเริ่มต้นทำงาน
- อัปเดตไฟล์ไบนารีและเมทาดาทาของโมเดล MobileNetV2
- เปลี่ยนการค้นหาพอร์ต COM ในสคริปต์ดาวน์โหลดเฟิร์มแวร์บน Windows จาก WMIC เป็น PowerShell
- แก้ไขเส้นทางอินพุตกล้องเริ่มต้นที่แสดงในข้อความช่วยเหลือของ `tc-nn-camera-app` ให้ตรงกับค่าเริ่มต้นที่ใช้งานจริงคือ `/dev/video2`

## ข้อควรทราบในการใช้งาน

- ไดเรกทอรีโมเดลเริ่มต้นคือ `/usr/share/yolov8s_quantized/` ส่วนโมเดลเริ่มต้นตัวที่สองของ `tcnnapp` อยู่ที่ `/usr/share/mobilenetv2_10_quantized/`
- โมเดล YOLOv8s ที่รวมอยู่ในแพ็กเกจไม่มีไฟล์ `sample/input.ia.bin` หากไม่พบไฟล์นี้ `tcnputestapp` จะใช้ข้อมูลอินพุตที่เติมด้วยศูนย์และแสดงข้อความ `Input file not found. Using zero padding.` การทดสอบนี้ใช้ตรวจสอบการทำงานและประสิทธิภาพของ NPU ไม่ใช่การประเมินความแม่นยำของโมเดล
- แพ็กเกจเฟิร์มแวร์ที่บิลด์ไว้แล้วมี `fwdn_ai.bat` สำหรับ Windows และ `fwdn_ai.sh` สำหรับ Linux

## เฟิร์มแวร์

- [AIG-TOPST-Yocto-image-v1.2.0-r01](https://topst-downloads.s3.ap-northeast-2.amazonaws.com/Yocto/v1.2.0/aig-yp4-v1.2.0-r01.zip)
