# 1. บทนำ
---
เอกสารนี้ให้แนวทางในการตั้งค่าสภาพแวดล้อมการพัฒนาซอฟต์แวร์สำหรับ VCP-G SDK โดยอธิบายเครื่องมือ การกำหนดค่า และทูลเชนที่จำเป็น

</br></br></br></br>

# 2. การตั้งค่าสภาพแวดล้อมของโฮสต์
---
## 2.1 การติดตั้ง Ubuntu
---
ขอแนะนำให้ตั้งค่าสภาพแวดล้อมการพัฒนาบน Ubuntu 22.04 เวอร์ชันนี้ให้แพลตฟอร์มที่เสถียรพร้อมการสนับสนุนจากชุมชนอย่างกว้างขวาง ซึ่งช่วยรับประกันความเข้ากันได้และความสะดวกในการใช้งานร่วมกับ VCP-G และทูลเชนที่เกี่ยวข้อง

เวอร์ชันของ Linux ดิสทริบิวชัน:  
- Ubuntu 22.04 (LTS)

</br></br></br>

## 2.2 การติดตั้ง WSL2 Ubuntu (เฉพาะสภาพแวดล้อม Windows)
---
**หมายเหตุ:** หากใช้โฮสต์ Ubuntu สามารถข้ามการติดตั้ง WSL2 ได้  

1.	ตั้งค่าคุณลักษณะของ Windows โดยคลิก **Control Panel -> Programs -> Windows Features On/Off -> Enable Virtual Machine Platform & Hyper-V**
2.	เรียกใช้ Windows Powershell ด้วย **“Run with administrator privileges”.**
3.	เปิดใช้งานระบบ WSL2
    ```
    dism.exe /online /enable-feature /featurename:Microsoft-Windows-Subsystem-Linux /all /norestart
    ```
4.	เปิดใช้งานคุณลักษณะเครื่องเสมือน
    ```
    dism.exe /online /enable-feature /featurename:VirtualMachinePlatform /all /norestart
    ```
5.	ตั้งค่า WSL ให้ใช้เวอร์ชันเริ่มต้นเป็น 2 (WSL2)
    ```
    wsl --set-default-version 2
    ```
6.	ค้นหา Ubuntu 22.04 LTS ใน Microsoft Store แล้วดาวน์โหลด

    * หากคุณจำเป็นต้องดาวน์โหลดแพ็กเกจอัปเดตเคอร์เนลของ Linux ให้ดาวน์โหลดแพ็กเกจล่าสุด[ที่นี่](https://learn.microsoft.com/ko-kr/windows/wsl/install-manual)
7.	ตรวจสอบ Ubuntu 22.04 ในรายการของ WSL
    ```
    wsl --list -online
    ```
8.	ติดตั้ง Ubuntu 22.04
    ```
    wsl --install Ubuntu-22.04
    ```
9.	ค้นหา WSL2 ในช่องค้นหาของ Windows แล้วเรียกใช้งาน 

</br></br></br>

## 2.3 การตั้งค่าสภาพแวดล้อม Linux
---
หากต้องการตั้งค่าสภาพแวดล้อม Linux บนเครื่อง PC โฮสต์ ให้ทำตามขั้นตอนต่อไปนี้:  

1. เรียกใช้ WSL2 (เฉพาะสภาพแวดล้อม Windows)  
    หากใช้ Windows ให้เริ่ม WSL2 โดยเรียกใช้คำสั่งใดคำสั่งหนึ่งต่อไปนี้ใน Windows PowerShell  
    ```
    wsl
    ```
    ```
    ubuntu
    ```

2.	อัปเดตรายการแพ็กเกจ  
ก่อนติดตั้งซอฟต์แวร์ใหม่ ให้อัปเดตรายการแพ็กเกจที่มีอยู่เพื่อให้แน่ใจว่าได้รับเวอร์ชันและส่วนที่ต้องพึ่งพาล่าสุด คำสั่งต่อไปนี้จะดึงรายการแพ็กเกจล่าสุดที่มีอยู่จากรีโพซิทอรี
    ```
    sudo apt update && /
    sudo apt upgrade
    ```

3.	ติดตั้งเครื่องมือพัฒนาทั่วไป  
    ติดตั้งเครื่องมือพัฒนาทั่วไปโดยป้อนคำสั่งต่อไปนี้:
    ```
    sudo apt install build-essential git
    ```

**หมายเหตุ:** คำสั่งนี้จะติดตั้งทั้งแพ็กเกจ build-essential และ git

</br></br></br></br>

# 3. ทูลเชน
---
VCP-G ใช้ทูลเชน **gcc-linaro-7.2.1-2017.11-x86_64_arm-eabi**  
ทูลเชนนี้ได้รับการปรับให้เหมาะกับสถาปัตยกรรม ARM และรับประกันความเข้ากันได้กับชิป TCC7045 บน VCP-G

</br></br></br>

## 3.1 การติดตั้งและตั้งค่าทูลเชน
---
ทำตามขั้นตอนต่อไปนี้เพื่อดาวน์โหลด แตกไฟล์ และตั้งค่าทูลเชน:  
1. ดาวน์โหลดทูลเชน  
   ป้อนคำสั่ง **wget** เพื่อดาวน์โหลดทูลเชนจากเว็บไซต์ Linaro:
    ```
    wget https://releases.linaro.org/components/toolchain/binaries/7.2-2017.11/arm-eabi/gcc-linaro-7.2.1-2017.11-x86_64_arm-eabi.tar.xz
    ```
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/Download%20Toolchain.png"></p>
    <p align="center"><strong>รูปที่ 3.1 ดาวน์โหลดทูลเชน</strong></p>
    
2. แตกไฟล์ทูลเชน  
    เมื่อดาวน์โหลดเสร็จสิ้น ให้แตกไฟล์เนื้อหาของไฟล์ .tar.xz
    ```
    tar -xvf gcc-linaro-7.2.1-2017.11-x86_64_arm-eabi.tar.xz
    ```
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/Extract%20Toolchain.png"></p>
    <p align="center"><strong>รูปที่ 3.2 แตกไฟล์ทูลเชน</strong></p>
    
3. ย้ายทูลเชนไปยัง /opt  
    ไดเรกทอรี /opt เป็นตำแหน่งมาตรฐานสำหรับซอฟต์แวร์เสริมบน Linux ให้ย้ายทูลเชนที่แตกไฟล์แล้วไปยังไดเรกทอรีนี้
    ```
    sudo mv gcc-linaro-7.2.1-2017.11-x86_64_arm-eabi /opt/
    ```
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/Move%20Toolchain.png"></p>
    <p align="center"><strong>รูปที่ 3.3 ย้ายทูลเชน</strong></p>

</br></br></br>

## 3.2 การตรวจสอบทูลเชน
---
เพื่อให้แน่ใจว่าติดตั้งทูลเชนอย่างถูกต้อง  
1. ไปยังไดเรกทอรีของทูลเชน
    ```
    cd /opt/gcc-linaro-7.2.1-2017.11-x86_64_arm-eabi
    ```
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/Navigate%20to%20Toolchain%20Directory.png"></p>
    <p align="center"><strong>รูปที่ 3.4 ไปยังไดเรกทอรีของทูลเชน</strong></p>
    
2. ตรวจสอบเวอร์ชันของคอมไพเลอร์ GCC ที่ติดตั้ง
    ```
    ./bin/arm-eabi-gcc --version
    ```
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/Check%20Version%20of%20Installed%20GCC%20Compiler.png"></p>
    <p align="center"><strong>รูปที่ 3.5 ตรวจสอบเวอร์ชันของคอมไพเลอร์ GCC ที่ติดตั้ง</strong></p>

หลังจากติดตั้งคอมไพเลอร์ GCC สำเร็จแล้ว ให้ตรวจสอบเวอร์ชันของคอมไพเลอร์ GCC ที่ติดตั้งว่าตรงกับ **gcc-linaro-7.2.1-2017.11.**

</br></br></br></br>

# 4. การโคลนซอร์สโค้ด
---
บทนี้อธิบายวิธีการโคลนซอร์สโค้ดโดยใช้ Git

</br></br></br>

## 4.1 การโคลนซอร์สโค้ดของ VCP-G
---
หากต้องการรับซอร์สโค้ดของ VCP-G ให้ป้อนคำสั่ง **git clone** คำสั่งนี้จะสร้างสำเนาของรีโพซิทอรีระยะไกลไว้บนเครื่องของคุณ ทำให้สามารถทำงานกับโค้ดได้โดยตรง

ทำตามขั้นตอนต่อไปนี้เพื่อโคลนซอร์สโค้ดของ VCP-G:
1. เปิดเทอร์มินัล  
    เปิดแอปพลิเคชันเทอร์มินัลบนระบบ Ubuntu 22.04

2. ไปยังไดเรกทอรีที่ต้องการ  
    เลือกตำแหน่งที่เหมาะสมสำหรับจัดเก็บซอร์สโค้ด ตัวอย่างเช่น หากต้องการบันทึกรีโพซิทอรีไว้ในโฮมไดเรกทอรี ให้ใช้คำสั่งต่อไปนี้
    ```
    cd ~
    ```
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/Navigate%20to%20Desired%20Directory.png"></p>
    <p align="center"><strong>รูปที่ 4.1 ไปยังไดเรกทอรีที่ต้องการ</strong></p>

3. โคลนรีโพซิทอรี  
    ใช้คำสั่งต่อไปนี้เพื่อโคลนซอร์สโค้ดของ VCP-G จากที่อยู่ git ที่ให้ไว้
    ```
    git clone https://github.com/topst-development/FreeRTOS-VCP.git topst-vcp
    ```
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/Figure%204.2%20Clone%20Repository.png"></p>
    <p align="center"><strong>รูปที่ 4.2 โคลนรีโพซิทอรี</strong></p>

4. ไปยังไดเรกทอรีที่โคลนมา  
    เมื่อกระบวนการโคลนเสร็จสิ้น ให้ใช้คำสั่งต่อไปนี้เพื่อไปยังไดเรกทอรีที่มีซอร์สโค้ด
    ```
    cd topst-vcp
    ```
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/Navigate%20to%20Cloned%20Directory.png"></p>
    <p align="center"><strong>รูปที่ 4.3 ไปยังไดเรกทอรีที่โคลนมา</strong></p>

ขณะนี้ซอร์สโค้ดของ VCP-G พร้อมใช้งานบนเครื่องสำหรับการบิลด์และการพัฒนาแล้ว

</br></br></br>

## 4.2 โครงสร้างของซอร์สโค้ด
---
หลังจากโคลนแล้ว ให้ป้อนคำสั่ง **ls** เพื่อแสดงรายการเนื้อหาในไดเรกทอรี และตรวจดูไฟล์สำคัญเพื่อทำความเข้าใจโครงสร้างของซอร์สโค้ด
```
ls

build  documents  easy-setup_vcp.sh  LICENSE  scripts  sources  tools
```

</br></br></br></br>

# 5. คู่มือการบิลด์
---
## 5.1 การเรียกใช้ easy-setup_vcp-g.sh
---
หากเรียกใช้สคริปต์ ./easy-setup_vcp-g.sh จะปรากฏหน้าจอต่อไปนี้

**ข้อควรระวัง**: หากเรียกใช้ ./easy-setup_vcp-g.sh ซ้ำ โปรดระวังว่าซอร์สที่บิลด์ไว้จะถูกลบหากเลือก yes
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20AI-G/Software/Linux%20SDK/license1.png"></p>
<p align="center"><strong>รูปที่ 5.1 ข้อตกลงอนุญาตให้ใช้สิทธิสำหรับผู้ใช้ปลายทาง</strong></p>

เลื่อนลงไปที่ด้านล่างสุดของหน้าจอและอ่านประกาศนี้ หลังจากอ่านประกาศนี้แล้ว ให้กดปุ่มลูกศรขวาและ [Enter]
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20AI-G/Software/Linux%20SDK/license2.png"></p>
<p align="center"><strong>รูปที่ 5.2 ไปที่ 'Proceed to confirm'</strong></p>


จากนั้นท่านจะเห็นหน้าจอดังต่อไปนี้ 
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20AI-G/Software/Linux%20SDK/license3.png" ></p>
<p align="center"><strong>รูปที่ 5.3 หน้าจอ Accept </strong></p>
เมื่อกด [Enter] เพื่อเลือก Accept แล้ว คุณสามารถบิลด์ได้โดยใช้คำสั่งต่อไปนี้

</br></br></br>

## 5.2 Makefile และระบบบิลด์
---
Makefile เป็นองค์ประกอบสำคัญของระบบบิลด์จำนวนมาก โดยประกอบด้วยกฎและคำสั่งสำหรับยูทิลิตี **make** เพื่อคอมไพล์และลิงก์โปรแกรม การใช้ Makefile ช่วยให้กระบวนการบิลด์เป็นแบบอัตโนมัติ พร้อมทั้งรับประกันความสอดคล้องและประสิทธิภาพ

</br></br></br>

## 5.3 การเริ่มกระบวนการบิลด์
---
หากต้องการบิลด์ซอร์สโค้ด ให้ทำตามขั้นตอนต่อไปนี้:  
1. ไปยังไดเรกทอรีสำหรับการบิลด์
    ```
    cd build/tcc70xx/gcc/
    ```
2. เรียกใช้คำสั่ง **make**  
    ```
    make
    ```
    คำสั่ง **make** จะอ่าน Makefile ในไดเรกทอรีปัจจุบันและดำเนินกระบวนการบิลด์
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/Run%20make%20Command.png"></p>
    <p align="center"><strong>รูปที่ 5.4 เรียกใช้คำสั่ง make </strong></p>
    
3. ตรวจสอบผลลัพธ์ของการบิลด์  
    เมื่อกระบวนการบิลด์เสร็จสิ้น ควรมีไฟล์ผลลัพธ์ต่อไปนี้แสดงอยู่ในเทอร์มินัล
    - output/tcc70xx_pflash_boot.rom
    - output/tcc70xx_pflash_boot_2M_ECC.rom
    - output/tcc70xx_pflash_boot_3M_ECC.rom
    - output/tcc70xx_pflash_boot_4M_ECC.rom
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/Verify%20Build%20Output.png"></p>
    <p align="center"><strong>รูปที่ 5.5 ตรวจสอบผลลัพธ์ของการบิลด์</strong></p>
   
    หากต้องการตรวจสอบรายการไฟล์ผลลัพธ์ ให้ใช้คำสั่งต่อไปนี้:
    ```
    ls output/ -al
    ```
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/Build%20Output%20File.png"></p>
    <p align="center"><strong>รูปที่ 5.6 ไฟล์ผลลัพธ์ของการบิลด์</strong></p>

</br></br></br></br>

# 6. การดาวน์โหลดเฟิร์มแวร์
---
บทนี้อธิบายวิธีการดาวน์โหลด ***FWDN*** ไปยัง VCP-G ในสภาพแวดล้อมการพัฒนาที่ใช้ Linux

</br></br></br>

## 6.1 การเตรียม VCP-G
---
ก่อนเริ่มกระบวนการดาวน์โหลด ให้ตรวจสอบว่า VCP-G วางอยู่ในตำแหน่งที่มั่นคงและปราศจากสิ่งรบกวน ตรวจสอบให้แน่ใจว่าสวิตช์และขั้วต่อทั้งหมดเข้าถึงได้ง่าย และสายไฟ 3.3V เชื่อมต่ออย่างถูกต้อง

</br></br></br>

## 6.2 การเชื่อมต่อฮาร์ดแวร์เข้ากับเครื่อง PC โฮสต์
---
หากใช้โฮสต์ Ubuntu ให้ข้ามไปยังขั้นตอนที่ 3 โดยตรง  
1. ดาวน์โหลด usbipd-win  
    จำเป็นต้องใช้โปรเจกต์ usbipd-win เพื่อใช้งาน USB ใน WSL2   
    ดาวน์โหลด usbipd-win จาก https://learn.microsoft.com/ko-kr/windows/wsl/connect-usb#attach-a-usb-device
2. เรียกใช้ PowerShell แล้วเชื่อมต่อ VCP-G (ซึ่ง Windows จะรู้จักเป็นพอร์ต COM) เข้ากับ WSL2  
    เรียกใช้คำสั่งต่อไปนี้ใน Windows PowerShell (ไม่ใช่ Linux)
    ```
    usbipd list
    ```
    ```
    usbipd bind --busid <busid>
    ```
    ```
    usbipd attach --wsl --busid <busid>
    ```
3. เชื่อมต่อสาย USB Type-C  
    ใช้สาย USB Type-C เพื่อเชื่อมต่อบอร์ด VCP-G เข้ากับเครื่อง PC โฮสต์สำหรับการพัฒนา
4. ตรวจสอบการเชื่อมต่อ USB  
    เรียกใช้คำสั่งต่อไปนี้ใน WSL2
    ```
    sudo apt-get install usbutils && lsusb
    ```
    ```
    sudo dmesg | grep tty
    ```
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/Verify%20USB%20Connection.png"></p>
    <p align="center"><strong>รูปที่ 6.1 ตรวจสอบการเชื่อมต่อ USB</strong></p>

หากปรากฏผลลัพธ์ดังที่แสดงในรูปที่ 6.1 แสดงว่าการเชื่อมต่อสำเร็จเรียบร้อยแล้ว

</br></br></br>

## 6.3 การดาวน์โหลดซอฟต์แวร์ลงบน VCP-G
---

### 6.3.1 การเรียกใช้ FWDN ในสภาพแวดล้อม Windows
1. ตั้งค่าบอร์ดให้อยู่ในโหมดดาวน์โหลด  
   เชื่อมต่อสายไฟเข้ากับบอร์ด VCP-G ขณะกดสวิตช์ FWDN
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/Set%20Board%20to%20Download%20Mode.png"></p>
    <p align="center"><strong>รูปที่ 6.2 ตั้งค่าบอร์ดให้อยู่ในโหมดดาวน์โหลด</strong></p>

2. คัดลอก tcc70xx_pflash_boot_2M_ECC.rom ไปยังโฟลเดอร์ fwdn_vcp
```
cp ~/topst-vcp/build/tcc70xx/gcc/output/tcc70xx_pflash_boot_2M_ECC.rom ~/topst-vcp/tools/fwdn_vcp/
```

3. คัดลอกโฟลเดอร์ fwdn_vcp ไปยังไดรฟ์ C
```
cp -r ~/topst-vcp/tools/fwdn_vcp /mnt/c/
```

4. คลิก fwdn_vcp.bat  
    ใช้ ***FWDN*** เพื่อดาวน์โหลดซอฟต์แวร์ที่บิลด์แล้วลงในแฟลช 4 MB บน VCP-G

    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/Click%20fwdn_vcp.bat.png"></p>
    <p align="center"><strong>รูปที่ 6.3 คลิก fwdn_vcp.bat</strong></p>
```
[main:27] FWDN VCP v0.1.1 - 2022.8.12 11:38:19
Com port num : 10
[FWDNWindowsUART::OpenPort:34] Complete open port(\\.\COM10)
[ProtocolCB::StartVCPFWDN:45] Complete to receive start res
[FWDN_VCP::LoadFwdnFW:144] Complete to send start msg
[ProtocolCB::CheckResPacket:172] Complete to receive ack for cmd(0xFFFF0000(RECEIVE_HSM_CMD))
[FWDN_VCP::WriteFile:284] Complete to send command(0xFFFF0000(RECEIVE_HSM_CMD))
[ProtocolCB::SendFile:151] Complete to send file
[ProtocolCB::CheckResPacket:172] Complete to receive ack for cmd(0xFFFF0000(RECEIVE_HSM_CMD))
[FWDN_VCP::WriteFile:295] Complete to send file - .\tcc70xx_pflash_boot_2M_ECC.rom
[FWDN_VCP::LoadFwdnFW:163] Complete to send hsm
[ProtocolCB::CheckResPacket:172] Complete to receive ack for cmd(0xFFFF0001(RECEIVE_FWDN_CMD))
[FWDN_VCP::WriteFile:284] Complete to send command(0xFFFF0001(RECEIVE_FWDN_CMD))
[ProtocolCB::SendFile:126] uiRemainSize = 43136
[ProtocolCB::SendFile:151] Complete to send file
[ProtocolCB::CheckResPacket:172] Complete to receive ack for cmd(0xFFFF0001(RECEIVE_FWDN_CMD))
[FWDN_VCP::WriteFile:295] Complete to send file - .\vcp_fwdn.rom
[FWDN_VCP::LoadFwdnFW:173] Complete to send fwdn
[FWDN_VCP::LoadFwdnFW:179] Complete to load FWDN F/W
RM=00000000
MT
MR0=0000a042
MR1=00020018
MR2=00000000
[ProtocolFW::CheckResPacket:260] Complete to receive ack for cmd(0xAAAA0016(VERSION_CMD))
[FWDN_VCP::GetDeviceVersion:77]  FWDN Firmware Version(20230728)
[ProtocolFW::CheckResPacket:260] Complete to receive ack for cmd(0xAAAA0014(STORAGE_INFO_CMD))
[FWDN_VCP::InfoStorage:56]
#### SNOR Info ####
Manufacture ID: 0x9d
Device ID: 0x6015
Name: ISSI-IS25LP016D
Sector Size: 4 KiB (4096 Byte)
Total Capacity: 2 MiB (2097152 Byte)
4Byte Address Mode: Unsupported
#### EFLASH Info ####
DCYCRDCON 0x1e0002
DCYCWRCON 0x20100
Sector Size: 8 KiB
Page Size: 2 KiB

-----Storage init info-----
O : Init success
X : Init failed or not exist
SNOR : O
eFlash : O

[ProtocolFW::CheckResPacket:260] Complete to receive ack for cmd(0xAAAA0017(CHIP_INFO_CMD))
[FWDN_VCP::GetChipInfo:121] ---chip info---
Chip Number : 0x57045
Dual Bank : false
Expand Flash : true
ECC : true
[FWDN_VCP::PrintBankInfo:468] ---bank info---
bank - 0
eFlash offset : 0x0
eFlash size : 2097152 byte
SNOR offset : 0x0
SNOR size : 2097152 byte
[FWDN_VCP::PrintStorageOption:451] ---storage info---
eflash
offset : 0x0
size : 2097152 byte
[ProtocolFW::CheckResPacket:260] Complete to receive ack for cmd(0xAAAA0011(WRITE_CMD))
[FWDN_VCP::WriteFile:284] Complete to send command(0xAAAA0011(WRITE_CMD))
 100% [||||||||||||||||||||||||||||||] 2097152/2097152
```

5. รีเซ็ตบอร์ด  
    เมื่อกระบวนการดาวน์โหลดเสร็จสิ้น ให้ถอดสายไฟออกแล้วเสียบกลับเข้าไปใหม่
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/Reset%20the%20Board.png"></p>
    <p align="center"><strong>รูปที่ 6.4 การรีเซ็ตบอร์ด</strong></p>

### 6.3.2 การเรียกใช้ FWDN ในสภาพแวดล้อม Linux
1. ตั้งค่าบอร์ดให้อยู่ในโหมดดาวน์โหลด  
   เชื่อมต่อสายไฟเข้ากับบอร์ด VCP-G ขณะกดสวิตช์ FWDN
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/Set%20Board%20to%20Download%20Mode.png"></p>
    <p align="center"><strong>รูปที่ 6.5 การตั้งค่าบอร์ดให้อยู่ในโหมดดาวน์โหลด</strong></p>
    
2. เรียกใช้คำสั่งดาวน์โหลด  
   ใช้ ***FWDN*** เพื่อดาวน์โหลดซอฟต์แวร์ที่บิลด์แล้วลงในหน่วยความจำแฟลชขนาด 4 MB บน VCP-G
    ```
    sudo ~/topst-vcp/tools/fwdn_vcp/fwdn --fwdn ~/topst-vcp/tools/fwdn_vcp/vcp_fwdn.rom -w output/tcc70xx_pflash_boot_2M_ECC.rom
    ```
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/Execute%20Download%20Command.png"></p>
    <p align="center"><strong>รูปที่ 6.6 การเรียกใช้คำสั่งดาวน์โหลด</strong></p>
    
3. รีเซ็ตบอร์ด  
    เมื่อกระบวนการดาวน์โหลดเสร็จสิ้น ให้ถอดสายไฟออกแล้วเสียบกลับเข้าไปใหม่
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/Reset%20the%20Board.png"></p>
    <p align="center"><strong>รูปที่ 6.7 การรีเซ็ตบอร์ด</strong></p>

</br></br></br>

## 6.4 การตรวจสอบซอฟต์แวร์บนบอร์ด
---
หลังจากดาวน์โหลดซอฟต์แวร์ลงบอร์ดแล้ว ให้ทำตามขั้นตอนต่อไปนี้เพื่อตรวจสอบว่าซอฟต์แวร์ทำงานอย่างถูกต้อง
1. ติดตั้ง minicom  
    ```
    sudo apt install minicom
    ```
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/Install%20Minicom.png"></p>
    <p align="center"><strong>รูปที่ 6.8 การติดตั้ง minicom</strong></p>
2. เปิดการเชื่อมต่อแบบอนุกรม  
    ใช้คำสั่งต่อไปนี้เพื่อเริ่มการเชื่อมต่อแบบอนุกรม
    ```
    minicom -D /dev/ttyUSB0 -b 115200 -8
    ```
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/Open%20Serial%20Connection.png"></p>
    <p align="center"><strong>รูปที่ 6.9 การเปิดการเชื่อมต่อแบบอนุกรม</strong></p>

เมื่อดำเนินการขั้นตอนที่ 1 และ 2 เสร็จสิ้น จะปรากฏผลลัพธ์ต่อไปนี้บนเทอร์มินัล หากการเชื่อมต่อสำเร็จ บอร์ดจะตอบสนองต่อการโต้ตอบ ซึ่งยืนยันได้ว่าซอฟต์แวร์ถูกดาวน์โหลดและทำงานอย่างถูกต้องบน VCP-G
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/Figure%206.7%20Open%20Serial%20Connection.png"></p>
<p align="center"><strong>รูปที่ 6.10 การเปิดการเชื่อมต่อแบบอนุกรม</strong></p>

</br></br></br>

## 6.5 การแก้ไขปัญหาที่พบบ่อย
---
บทนี้อธิบายวิธีแก้ไขปัญหาที่พบบ่อยระหว่างการใช้งาน VCP-G

**ปัญหา:** ***FWDN*** รายงานว่าไม่มีสิทธิ์ในการเข้าถึงอุปกรณ์ ttyUSB0  
**วิธีแก้ไข:** ปัญหานี้เกิดขึ้นเมื่อบัญชีผู้ใช้ของท่าน (**$USER**) ไม่มีสิทธิ์ที่จำเป็นในการเข้าถึงอุปกรณ์แบบอนุกรม เพื่อแก้ไขปัญหานี้ ให้เพิ่มบัญชีผู้ใช้เข้าไปในกลุ่ม dialout

1. แก้ไขสิทธิ์ของกลุ่มผู้ใช้  
    เรียกใช้คำสั่งต่อไปนี้
    ```
    sudo usermod -aG dialout $USER
    ```
2. ออกจากระบบแล้วเข้าสู่ระบบใหม่  
    ออกจากระบบของเซสชันปัจจุบันแล้วเข้าสู่ระบบใหม่เพื่อให้การเปลี่ยนแปลงมีผล จากนั้นให้ลองเข้าถึงอุปกรณ์ ttyUSB0 อีกครั้ง
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/Modify%20User%20Group%20Permissions.png"></p>
    <p align="center"><strong>รูปที่ 6.11 การแก้ไขสิทธิ์ของกลุ่มผู้ใช้ </strong></p>

**ปัญหา:** เมื่อใช้ minicom การสื่อสารกับ VCP-G ไม่ถูกต้องหรือมีการทำงานที่ผิดปกติ  
**วิธีแก้ไข:** ปัญหานี้อาจเกิดขึ้นหากการตั้งค่าการควบคุมการไหลของข้อมูลเริ่มต้นของ minicom ถูกกำหนดเป็น **hardware** ต้องตั้งค่าการควบคุมการไหลของข้อมูลแบบฮาร์ดแวร์เป็น No เพื่อให้ทำงานได้อย่างถูกต้อง 
1. เริ่มใช้งาน minicom  
    ใช้คำสั่งต่อไปนี้
    ```
    minicom -D /dev/ttyUSB0 -b 115200 -8
    ```
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/Launch%20Minicom.png"></p>
    <p align="center"><strong>รูปที่ 6.12 การเปิดใช้งาน minicom</strong></p>
2. เข้าสู่หน้าจอการตั้งค่า  
    ขณะอยู่ใน minicom ให้กด **[Ctrl+A]** จากนั้นกด **[o]** เพื่อเปิดเมนูการตั้งค่า
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/Access%20Set%20up%20Screen.png"></p>
    <p align="center"><strong>รูปที่ 6.13 การเข้าสู่หน้าจอการตั้งค่า</strong></p>
3. ไปที่ Serial port setup  
    เลือก **Serial port setup** จากตัวเลือกที่มี
4. แก้ไขการควบคุมการไหลของข้อมูล  
    ภายในหน้าการตั้งค่าพอร์ตอนุกรม ให้กด **[F]** เพื่อตั้งค่าการควบคุมการไหลของข้อมูลแบบฮาร์ดแวร์เป็น **No**
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/Modify%20Flow%20Control.png"></p>
    <p align="center"><strong>รูปที่ 6.14 การแก้ไขการควบคุมการไหลของข้อมูล</strong></p>
5. ออกและบันทึก  
    ออกจากหน้าการตั้งค่าและบันทึกการกำหนดค่า จากนั้น minicom จะสื่อสารกับ VCP-G ได้อย่างถูกต้อง
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/Save%20and%20Exit.png"></p>
    <p align="center"><strong>รูปที่ 6.15 การบันทึกและออก</strong></p>

**หมายเหตุ:** หากท่านใช้เครื่องมือสื่อสารแบบอนุกรมอื่นที่ไม่ใช่ minicom โปรดตรวจสอบให้แน่ใจว่าการตั้งค่าการควบคุมการไหลของข้อมูลของเครื่องมือนั้นถูกกำหนดเป็น **No** ด้วยเช่นกัน เพื่อให้ทำงานได้อย่างถูกต้อง
</br></br></br></br>

# 7. เอกสารอ้างอิง
---
- ติดต่อ TOPST สำหรับรายละเอียดเพิ่มเติม: topst@topst.ai

**หมายเหตุ:** เอกสารอ้างอิงสามารถจัดหาให้ได้เมื่อมีอยู่ ทั้งนี้ขึ้นอยู่กับเงื่อนไขของสัญญา หากไม่มีเอกสาร
อ้างอิงดังกล่าว จะมีการแนะนำเนื้อหาที่เกี่ยวข้องโดยตรงกับการพัฒนาของท่านแทน
