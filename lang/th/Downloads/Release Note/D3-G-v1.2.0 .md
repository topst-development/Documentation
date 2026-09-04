# บันทึกการเผยแพร่ D3-G - v1.2.0

## รีโพซิทอรีที่อัปเดต
- [vpu-kernel-library](https://github.com/topst-development/vpu-kernel-library/tree/release/1.2.0-r01)
- [kernel-5.10](https://github.com/topst-development/kernel-5.10/tree/release/d3/1.2.0)
- [meta-topst](https://github.com/topst-development/meta-topst/tree/release/1.2.0)
- [meta-topst-bsp](https://github.com/topst-development/meta-topst-bsp/tree/release/1.2.0)
- [manifests](https://github.com/topst-development/manifests/tree/release/1.2.0)

## คุณสมบัติใหม่
- สามารถใช้งานตัวเข้ารหัส/ตัวถอดรหัส VPU-AVC ผ่าน gstreamer ได้
- สามารถใช้งานตัวถอดรหัส VPU-VP9 ผ่าน gstreamer ได้

## การปรับปรุง
- ตัวเข้ารหัส VPU รองรับการเข้ารหัสเนื้อหาเป็น 4K


## ปัญหาที่ทราบ
- การรีบูตแบบวอร์มใช้เวลานาน (ประมาณ 40 วินาที) เป็นบางครั้งเมื่อใส่ sdcard
- กล้องภายนอกที่เชื่อมต่อกับ MIPI รองรับได้สูงสุด 30fps ในขณะนี้ (จะรองรับสูงสุด 60fps ในรุ่นถัดไป)

## คู่มือ
- VLC Player
    - ควรตั้งค่า video output เป็น **'X11 video output(XCB)'** ในการตั้งค่าคุณสมบัติก่อนเล่นเนื้อหา
- firefox
	- ติดตั้ง Firefox ใหม่ด้วย 'sudo apt install --reinstall firefox' หากจำเป็น

## ภาคผนวก.
<p align="center"><strong>ตารางที่ 1.1 USB Bluetooth ดองเกิล</strong></p>
<div align="center">
	<table>
	  <tr>
	    <td><strong>ชื่อผู้ผลิต</strong></td>
	    <td><strong>ชื่อชิปเซ็ต</strong></td>
	  </tr>
	  <tr>
	    <td rowspan="16">RealTek</td>
        <td>rtl8192</td>
	  </tr>
	  <tr>
	    <td>rtl8723</td>
	  </tr>
      <tr>
	    <td>rtl8761a</td>
	  </tr>
      <tr>
	    <td>rtl8761b</td>
	  </tr>
      <tr>
	    <td>rtl8761bu</td>
	  </tr>
      <tr>
	    <td>rtl8812ae</td>
	  </tr>
      <tr>
	    <td>rtl8821a</td>
	  </tr>
      <tr>
	    <td>rtl8821c</td>
	  </tr>
      <tr>
	    <td>rtl8821cs</td>
	  </tr>
      <tr>
	    <td>rtl8822b</td>
	  </tr>
      <tr>
	    <td>rtl8822cs</td>
	  </tr>
      <tr>
	    <td>rtl8822cu</td>
	  </tr>
      <tr>
	    <td>rtl8851bu</td>
	  </tr>
      <tr>
	    <td>rtl8852au</td>
	  </tr>
      <tr>
	    <td>rtl8852bu</td>
	  </tr>
      <tr>
	    <td>rtl8852cu</td>
	  </tr>
      <tr>
        <td>MediaTek</td>
        <td>MT763F</td>
      </tr>
      <tr>
        <td rowspan="3">Broadcom</td>
        <td>bcm2070x</td>
      </tr>
      <tr>
	    <td>bcm4365</td>
	  </tr>
      <tr>
	    <td>bcm4345</td>
	  </tr>
      <tr>
        <td rowspan="3">Intel</td>
        <td>Wireless-AC 7260</td>
      </tr>
      <tr>
	    <td>Wireless-AC 3160</td>
	  </tr>
      <tr>
	    <td>Wireless-AC 8260</td>
	  </tr>
    </table>
</div>  


<p align="center"><strong>ตารางที่ 1.2 USB Wifi ดองเกิล</strong></p>
<div align="center">
	<table>
	  <tr>
	    <td><strong>ชื่อผู้ผลิต</strong></td>
	    <td><strong>ชื่อชิปเซ็ต</strong></td>
	  </tr>
	  <tr>
	    <td>RealTek</td>
        <td>rtl88x2bu (8812bu, 8822bu)</td>
	  </tr>
	  <tr>
	    <td>MediaTek</td>
        <td>MT7601U</td>
	  </tr>
    </table>
</div>
