# บันทึกการเผยแพร่ D3-G - v1.3.0

## ที่เก็บข้อมูลที่อัปเดต
- [isp-server](https://github.com/topst-development/isp-server/tree/feature/d3g-ov5647)
- [isp-frontend](https://github.com/topst-development/isp-frontend/tree/feature/d3g)
- [kernel-5.10](https://github.com/topst-development/kernel-5.10/tree/release/d3/1.3.0)
- [meta-topst](https://github.com/topst-development/meta-topst/tree/release/1.3.0)
- [meta-topst-bsp](https://github.com/topst-development/meta-topst-bsp/tree/release/1.3.0)
- [manifests](https://github.com/topst-development/manifests/tree/release/1.3.0)

## คุณสมบัติใหม่
- รองรับไดรเวอร์ vulkan
- รองรับเครื่องมือปรับจูน isp ของกล้องแบบพื้นฐาน
- รองรับกล้อง PIv2 ผ่านการกำหนดค่าการบิลด์
- รองรับ firefox-esr (extended support release) ในรุ่นเผยแพร่ของ Ubuntu เดสก์ท็อป

## การปรับปรุง
- ปรับปรุงความเร็วในการรับส่งข้อมูลของ pcie
- ทำให้การตรวจพบบล็อกดีไวซ์ของ pcie ระหว่างการบูตมีเสถียรภาพมากขึ้น

## ปัญหาที่ทราบ
- การรีบูตแบบวอร์มรีบูตใช้เวลานาน (ประมาณ 40 วินาที) เป็นบางครั้งเมื่อเสียบ sdcard อยู่
- กล้องภายนอกที่เชื่อมต่อกับ MIPI รองรับได้สูงสุด 30fps ในขณะนี้ (จะรองรับสูงสุด 60fps ในรุ่นเผยแพร่ถัดไป)

## คู่มือ
 - VLC Player
   - ก่อนเล่นเนื้อหา ควรตั้งค่าเอาต์พุตวิดีโอเป็น 'X11 video output(XCB)' ในหน้าการตั้งค่า
 - ไดรเวอร์ Vulkan
   - รันคำสั่ง 'vkcube' เพื่อเรียกใช้ตัวอย่าง vulkan
   - ดู [https://github.com/krh/vkcube.git](https://github.com/krh/vkcube.git) เพื่อเรียนรู้วิธีเขียนแอปพลิเคชัน vulkan ของคุณเอง
