# 1. บทนำ
---
เอกสารนี้ให้แนวทางสำหรับการบิลด์ D3-G SDK ซึ่งรวมถึงการตั้งค่าสภาพแวดล้อมของโฮสต์ การบิลด์ SDK การใช้ตัวดาวน์โหลดเฟิร์มแวร์ และการดาวน์โหลด Ubuntu  

เอกสารนี้ประกอบด้วยข้อมูลต่อไปนี้: 
- การตั้งค่าสภาพแวดล้อมของโฮสต์  
- คู่มือการบิลด์อิมเมจ  
- คู่มือการดาวน์โหลดเฟิร์มแวร์ 
- การเชื่อมต่อบอร์ด D3-G กับ PC

<br/><br/><br/><br/>

# 2. การตั้งค่าสภาพแวดล้อมของโฮสต์
---
บทนี้ให้คำแนะนำเกี่ยวกับวิธีตั้งค่าสภาพแวดล้อมของเครื่อง PC โฮสต์ โดยแยกคำแนะนำสำหรับ Windows และ Ubuntu
</br><br/><br/>

## 2.1 สภาพแวดล้อม Windows 
---
เอกสารนี้อธิบายวิธีตั้งค่า Windows Subsystem for Linux (WSL) เพื่อใช้งาน Linux บนเครื่อง PC ที่ใช้ Windows
D3-G Linux SDK พัฒนาขึ้นบนพื้นฐานของ Yocto Project ดังนั้น Linux เวอร์ชันของ D3-G SDK จึงเป็นไปตาม Yocto Project
คุณสามารถติดตั้ง Linux เวอร์ชันอื่นได้ แต่เอกสารนี้อธิบาย D3-G Linux SDK ที่อ้างอิงกับ Ubuntu 22.04
หากระบบปฏิบัติการโฮสต์ของคุณคือ Ubuntu ให้ไปที่บทที่ 2.2

</br><br/>

### 2.1.1 การติดตั้ง WSL2 Ubuntu
1. เรียกใช้ Windows PowerShell ด้วย "**เรียกใช้ด้วยสิทธิ์ผู้ดูแลระบบ**"
2. เปิดใช้งานระบบ WSL2
    ```
    dism.exe /online /enable-feature /featurename:Microsoft-Windows-Subsystem-Linux /all /norestart
    ```
3. เปิดใช้งานคุณสมบัติเครื่องเสมือน
    ```
    dism.exe /online /enable-feature /featurename:VirtualMachinePlatform /all /norestart
    ```
4. ตั้งค่า WSL 2 ให้เป็นเวอร์ชันเริ่มต้น
    ```
    wsl --set-default-version 2
    ```
5. ค้นหา Ubuntu 22.04.3 LTS ใน Microsoft Store แล้วดาวน์โหลด

    * หากคุณจำเป็นต้องดาวน์โหลดแพ็กเกจอัปเดตเคอร์เนลของ Linux ให้ดาวน์โหลดแพ็กเกจล่าสุด[ที่นี่](https://learn.microsoft.com/ko-kr/windows/wsl/install-manual)

6. เลือกชื่อผู้ใช้ใดก็ได้ระหว่างการติดตั้ง Ubuntu
</br><br/>

### 2.1.2 การเข้าถึง Ubuntu ผ่าน WSL2
เปิด Command Prompt ของ Windows และป้อนคำสั่งต่อไปนี้เพื่อเข้าถึง Ubuntu
เมื่อเข้าถึง Ubuntu ระบบจะเริ่มต้นที่ไดเรกทอรี /mnt/c/Users/[username] โดยค่าเริ่มต้น
```
wsl  // access ubuntu 
ls   // check contents in your directory
```
โปรดดูรูปที่ 2.1 เพื่อตรวจสอบผลลัพธ์ (ผลลัพธ์อาจแตกต่างกันไปตามระบบของคุณ)
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20D3-G/Software/1.1%20wsl%20linux.png" width="500"></p>
<p align="center"><strong>รูปที่ 2.1 ภาพหน้าจอ WSL2 </strong></p>

<br/><br/>

### 2.1.3 การตั้งค่าโลแคล

หลังจากรัน Ubuntu บน WSL แล้ว คุณควรตั้งค่าโลแคลเพื่อให้การตั้งค่าภาษาและภูมิภาคถูกต้อง แนะนำให้ใช้ en_US.UTF-8 ให้รันคำสั่งต่อไปนี้เพื่อใช้ en_US.UTF-8 

```
sudo locale-gen en_US.UTF-8 && sudo update-locale LANG=en_US.UTF-8 
```

หลังจากตั้งค่าโลแคลแล้ว คุณสามารถตรวจสอบชนิดของโลแคลได้ด้วยคำสั่งต่อไปนี้ 

```
echo 'LANG=en_US.UTF-8' | sudo tee -a /etc/default/locale && \  

echo 'LC_ALL=en_US.UTF-8' | sudo tee -a /etc/default/locale 
```
<br/><br/>

### 2.1.4 การติดตั้ง SSH และ Samba

หลังจากเข้าสู่ Ubuntu แล้ว คุณสามารถใช้ยูทิลิตีเพิ่มเติม เช่น SSH และ Samba เพื่อให้สภาพแวดล้อมการพัฒนาสะดวกยิ่งขึ้น SSH และ Samba ช่วยให้คุณเรียกใช้คำสั่งบนคอมพิวเตอร์ระยะไกลและคัดลอกไฟล์ไปยังคอมพิวเตอร์เครื่องอื่นได้
 - ขั้นตอนต่อไปนี้กำหนดให้เครื่อง PC โฮสต์เชื่อมต่อกับเครือข่าย โปรดตรวจสอบสถานะเครือข่ายของคุณด้วยคำสั่งต่อไปนี้
  ```
  $ sudo apt-get update
  $ sudo apt-get install -y net-tools
  $ ifconfig 
  ```

หากติดตั้ง SSH และ Samba ไว้แล้ว หรือคุณจะไม่ใช้งาน คุณสามารถข้ามบทนี้ได้

ใช้คำสั่งต่อไปนี้เพื่อติดตั้ง net-tools, SSH และ Samba

```
$ sudo apt-get update 
$ sudo apt install -y net-tools openssh-server samba
```
หลังจากติดตั้ง SSH และ Samba แล้ว ให้กำหนดค่าแต่ละโปรแกรมตามความเหมาะสมกับสภาพแวดล้อมของคุณ
</br><br/>

### 2.1.5 การติดตั้งยูทิลิตี

ใช้คำสั่งต่อไปนี้เพื่อติดตั้งยูทิลิตีที่จำเป็นทั้งหมดในคราวเดียว หากต้องการใช้ Yocto Project จะต้องติดตั้งยูทิลิตีต่อไปนี้บนเครื่อง PC โฮสต์ (คอมพิวเตอร์ส่วนบุคคลหรือเซิร์ฟเวอร์สำหรับการพัฒนา)


```
$ sudo apt-get install -y gawk wget git diffstat unzip texinfo gcc-multilib build-essential chrpath

$ sudo apt-get install -y socat cpio python3 python3-pip python3-pexpect xz-utils debianutils

$ sudo apt-get install -y iputils-ping python3-git python3-jinja2 libegl1-mesa-dev libsdl1.2-dev pylint

$ sudo apt-get install -y xterm zstd ncftp curl git-lfs vim zip lz4
```

<br/><br/>

### 2.1.6 การติดตั้ง Repo

หากติดตั้ง Repo ไว้แล้ว คุณสามารถใช้งานได้โดยไม่ต้องติดตั้งใหม่  
ก่อนติดตั้ง Repo โปรดตรวจสอบว่าได้ติดตั้ง Python เวอร์ชัน 3.6 ขึ้นไปแล้ว

ใช้คำสั่งต่อไปนี้เพื่อติดตั้ง Repo
```
$ sudo apt-get install repo
```

หากพบข้อความแสดงข้อผิดพลาด '/usr/bin/env 'python' no such file or directory' ให้ใช้คำสั่งต่อไปนี้เพื่อลิงก์ 'python' ไปยัง 'python3'

```
$ sudo ln -sf /usr/bin/python3 /usr/bin/python
```
หากเกิดข้อผิดพลาดของ Repo ให้ใช้คำสั่งต่อไปนี้เพื่อดาวน์โหลดเวอร์ชันล่าสุดและวางไว้ในโฟลเดอร์ /usr/bin/

```
$ mkdir -p ~/bin

$ curl http://commondatastorage.googleapis.com/git-repo-downloads/repo > ~/bin/repo

$ chmod a+x ~/bin/repo

$ sudo mv ~/bin/repo /usr/bin/repo
```
ดำเนินการต่อที่ **บทที่ 3: คู่มือการบิลด์อิมเมจ**

<br/><br/><br/>

## 2.2 สภาพแวดล้อม Linux
---
บทนี้อธิบายขั้นตอนการตั้งค่าสำหรับการใช้ Ubuntu เป็นระบบปฏิบัติการโฮสต์
</br><br/>

### 2.2.1 การตั้งค่าสภาพแวดล้อม
บทต่อไปนี้ (2.2.2 ถึง 2.2.5) จะต้องดำเนินการในเทอร์มินัลของ Ubuntu หากต้องการเปิดเทอร์มินัล ให้ใช้ปุ่มลัด [Ctrl + Alt + T]
<br/><br/>

### 2.2.2 การตั้งค่าโลแคล

หลังจากรัน Ubuntu บน WSL แล้ว คุณควรตั้งค่าโลแคลเพื่อให้การตั้งค่าภาษาและภูมิภาคถูกต้อง แนะนำให้ใช้ en_US.UTF-8 ให้รันคำสั่งต่อไปนี้เพื่อใช้ en_US.UTF-8 

```
sudo locale-gen en_US.UTF-8 && sudo update-locale LANG=en_US.UTF-8 
```

หลังจากตั้งค่าโลแคลแล้ว คุณสามารถตรวจสอบชนิดของโลแคลได้ด้วยคำสั่งต่อไปนี้ 

```
echo 'LANG=en_US.UTF-8' | sudo tee -a /etc/default/locale && \  

echo 'LC_ALL=en_US.UTF-8' | sudo tee -a /etc/default/locale 
```
<br/><br/>

### 2.2.3 การติดตั้ง SSH และ Samba

หลังจากเข้าสู่ Ubuntu แล้ว คุณสามารถใช้ยูทิลิตีเพิ่มเติม เช่น SSH และ Samba เพื่อให้สภาพแวดล้อมการพัฒนาสะดวกยิ่งขึ้น SSH และ Samba ช่วยให้คุณเรียกใช้คำสั่งบนคอมพิวเตอร์ระยะไกลและคัดลอกไฟล์ไปยังคอมพิวเตอร์เครื่องอื่นได้
 - ขั้นตอนต่อไปนี้กำหนดให้เครื่อง PC โฮสต์เชื่อมต่อกับเครือข่าย โปรดตรวจสอบสถานะเครือข่ายของคุณด้วยคำสั่งต่อไปนี้
  ```
  $ sudo apt-get update
  $ sudo apt-get install -y net-tools
  $ ifconfig 
  ```

หากติดตั้ง SSH และ Samba ไว้แล้ว หรือคุณจะไม่ใช้งาน คุณสามารถข้ามบทนี้ได้

ใช้คำสั่งต่อไปนี้เพื่อติดตั้ง SSH และ Samba

```
$ sudo apt-get update 
$ sudo apt install -y openssh-server samba
```
หลังจากติดตั้ง SSH และ Samba แล้ว ให้กำหนดค่าแต่ละโปรแกรมตามความเหมาะสมกับสภาพแวดล้อมของคุณ

<br/><br/>

### 2.2.4 การติดตั้งยูทิลิตี

ใช้คำสั่งต่อไปนี้เพื่อติดตั้งยูทิลิตีที่จำเป็นทั้งหมดในคราวเดียว หากต้องการใช้ Yocto Project **จะต้อง**ติดตั้งยูทิลิตีต่อไปนี้บนเครื่อง PC โฮสต์ (คอมพิวเตอร์ส่วนบุคคลหรือเซิร์ฟเวอร์สำหรับการพัฒนา)
****


```
$ sudo apt-get install -y gawk wget git diffstat unzip texinfo gcc-multilib build-essential chrpath

$ sudo apt-get install -y socat cpio python3 python3-pip python3-pexpect xz-utils debianutils

$ sudo apt-get install -y iputils-ping python3-git python3-jinja2 libegl1-mesa-dev libsdl1.2-dev pylint

$ sudo apt-get install -y xterm zstd ncftp curl git-lfs vim zip lz4
```

<br/><br/>

### 2.2.5 การติดตั้ง Repo

คุณสามารถดาวน์โหลด D3-G SDK ผ่าน Android Repo ได้  
หากต้องการติดตั้ง Repo โปรดดูเว็บไซต์ต่อไปนี้: https://source.android.com/source/downloading.html.  
หากติดตั้ง Repo ไว้แล้ว คุณสามารถใช้งานได้โดยไม่ต้องติดตั้งใหม่  
ก่อนติดตั้ง Repo โปรดตรวจสอบว่าได้ติดตั้ง Python เวอร์ชัน 3.6 ขึ้นไปแล้ว

ใช้คำสั่งต่อไปนี้เพื่อติดตั้ง Repo
```
$ sudo apt-get install repo
```

หากพบข้อความแสดงข้อผิดพลาด '/usr/bin/env 'python' no such file or directory' ให้ใช้คำสั่งต่อไปนี้เพื่อลิงก์ 'python' ไปยัง 'python3'

```
$ sudo ln -sf /usr/bin/python3 /usr/bin/python
```
หากเกิดข้อผิดพลาดของ Repo ให้ใช้คำสั่งต่อไปนี้เพื่อดาวน์โหลดเวอร์ชันล่าสุดและวางไว้ในโฟลเดอร์ /usr/bin/

```
$ mkdir -p ~/bin

$ curl http://commondatastorage.googleapis.com/git-repo-downloads/repo > ~/bin/repo

$ chmod a+x ~/bin/repo

$ sudo mv ~/bin/repo /usr/bin/repo
```

<br/><br/>

### 2.2.6 Udev Rules สำหรับอุปกรณ์ USB ของ Telechips
หลังจากที่คุณดำเนินการคำสั่งต่อไปนี้แล้ว คุณไม่จำเป็นต้องใช้คำสั่ง 'sudo' อีกต่อไปเมื่อดาวน์โหลด FWDN ใน Linux
```
$ echo "SUBSYSTEM==\"usb\", ATTR{idVendor}==\"140e\", MODE=\"0666\", OWNER=\"${USER}\"" | sudo tee /etc/udev/rules.d/99-topst.rules
$ sudo udevadm control --reload-rules && sudo udevadm trigger
```
ดำเนินการต่อที่ **บทที่ 3: คู่มือการบิลด์อิมเมจ**

<br/><br/><br/><br/>

# 3. คู่มือการบิลด์อิมเมจ
---
บทนี้ให้คำแนะนำโดยอ้างอิงจากระบบปฏิบัติการ Ubuntu ที่ติดตั้งบนเครื่อง PC โฮสต์ (ไม่ว่าจะเป็น WSL หรือการติดตั้ง Ubuntu ในเครื่องก็ตาม) อิมเมจที่จะอัปโหลดไปยัง D3-G ถูกบิลด์ด้วย Yocto Project ดังนั้นกระบวนการบิลด์จึงต้องดำเนินการในสภาพแวดล้อม Ubuntu
</br></br>

## 3.1 การเตรียมการบิลด์ SDK
---
D3-G Linux SDK อ้างอิงจาก Yocto Project 4.0 Kirkstone ดังนั้นคุณต้องกำหนดค่าสภาพแวดล้อม Yocto Project บนเครื่อง PC โฮสต์เพื่อใช้งาน D3-G Linux SDK หากต้องการดาวน์โหลด SDK, source-mirror และทูลต่าง ๆ คุณต้องติดตั้งยูทิลิตีที่จำเป็น เพื่อให้การบิลด์อิมเมจเป็นไปอย่างราบรื่น เครื่อง PC ของคุณต้องมี**พื้นที่จัดเก็บว่างอย่างน้อย 60 GB** และ**RAM อย่างน้อย 16 GB**

</br><br/>  

## 3.2 Yocto Project  
---
Yocto Project เป็นโครงการโอเพนซอร์สที่มุ่งเน้นการพัฒนา Linux แบบฝังตัว  
โดยใช้การผสมผสานระหว่างโครงการ Open Embedded ซึ่งก็คือ Poky และ ***bitbake*** เป็นระบบบิลด์เพื่อสร้างอิมเมจ Linux  
เมื่อใช้ Yocto Project คุณสามารถบิลด์ bootloader, kernel และ rootfs ได้พร้อมกัน  

<br/><br/>

## 3.3 กระบวนการทำงานของ Yocto Project
---
รูปที่ 3.1 แสดงกระบวนการทำงานของ Yocto Project คุณสามารถดาวน์โหลดซอร์สจาก upstream ตามข้อมูลเมตาและทำการบิลด์ได้ หลังจากการบิลด์เสร็จสิ้น จะได้แพ็กเกจ อิมเมจ และ SDK เป็นผลลัพธ์

<p align="center">
    <img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20D3-G/Software/2.1%20yocto%20project%20task%20process.png", width="700">
</p>
<p align="center"><strong>รูปที่ 3.1 กระบวนการทำงานของ Yocto Project</strong></p>

<br/><br/>

## 3.4 องค์ประกอบของ D3-G SDK
---
ต่อไปนี้คือส่วนประกอบของ Yocto Project ที่เราได้กำหนดค่าไว้
ตารางที่ 3.1 แสดงองค์ประกอบของ D3-G SDK



**ตารางที่ 3.1 องค์ประกอบของ D3-G SDK**
<table border="1" cellspacing="0" cellpadding="5">
  <colgroup>
    <col style="width: 10%">
    <col style="width: 10%">
    <col style="width: 10%">
    <col style="width: 56%">
  </colgroup>
  <thead>
    <tr>
      <th colspan="3"style="text-align: center; vertical-align: middle;"><strong>รายการ</strong></th>
      <th style="text-align: center; vertical-align: middle;" ><strong>คำอธิบาย</strong></th>
    </tr>
  </thead>
  <tbody>
  <tr>
      <td colspan="3"style="text-align: center; vertical-align: middle;">easy-setup.sh</td>
      <td>สคริปต์ Python สำหรับดาวน์โหลดและบิลด์ SDK โดยอัตโนมัติ</td>
    </tr>
    <tr>
      <td colspan="3"style="text-align: center; vertical-align: middle;">stitch-fai-ai.sh</td>
      <td>สคริปต์สำหรับสร้างอิมเมจ fai ของ AI-G (minimal + แอปพลิเคชันตัวอย่าง)</td>
    </tr>
    <tr>
      <td colspan="3"style="text-align: center; vertical-align: middle;">stitch-fai-d3.sh</td>
      <td>สคริปต์สำหรับสร้างอิมเมจ fai ของ D3-G (minimal + แอปพลิเคชันตัวอย่าง)</td>
    </tr>
    <tr>
      <td colspan="3"style="text-align: center; vertical-align: middle;">mktcimg</td>
      <td rowspan="2">เครื่องมือที่เกี่ยวข้องกับกระบวนการบิลด์และ <strong>FWDN</strong></td>
    </tr>
    <tr>
      <td colspan="3"style="text-align: center; vertical-align: middle;">tools</td>
    </tr>
    <tr>
      <td rowspan="8"style="text-align: center; vertical-align: middle;">poky</td>
      <td colspan="2"style="text-align: center; vertical-align: middle;">poky</td>
      <td>ระบบบิลด์ Yocto Project 4.0 Kirkstone</td>
    </tr>
    <tr>
      <td colspan="2"style="text-align: center; vertical-align: middle;">meta-openembedded</td>
      <td>เลเยอร์ที่รองรับ OE-Core</td>
    </tr>
    <tr>
      <td colspan="2"style="text-align: center; vertical-align: middle;">meta-arm</td>
      <td>เลเยอร์ที่รองรับทูลเชน ARM</td>
    </tr>
    <tr>
      <td colspan="2"style="text-align: center; vertical-align: middle;">meta-topst-bsp</td>
      <td>เลเยอร์ที่รองรับ TOPST BSP</td>
    </tr>
    <tr>
      <td colspan="2"style="text-align: center; vertical-align: middle;">meta-gplv2</td>
      <td>เลเยอร์ที่มีแพ็กเกจซึ่งหลีกเลี่ยงไลเซนส์ GPLv3</td>
    </tr>
    <tr>
      <td colspan="2"style="text-align: center; vertical-align: middle;">meta-topst</td>
      <td>เรซิพีของ TOPST</td>
    </tr>
  </tbody>
</table>
<br/><br/><br/>


## 3.5 การเตรียมพร้อมสำหรับการบิลด์
---
บทต่อไปนี้อธิบายวิธีกำหนดค่า Yocto Project เพื่อบิลด์อิมเมจ D3-G

<br/><br/>

### 3.5.1 ตั้งค่าอีเมลผู้ใช้และชื่อผู้ใช้ใน .gitconfig
หากต้องการดาวน์โหลด D3-G SDK จาก git อย่างเป็นทางการของ TOPST ให้กำหนดค่าอีเมลและชื่อของคุณ
1. ป้อนคำสั่งต่อไปนี้
```
vi ~/.gitconfig
```
2. ป้อนข้อมูลต่อไปนี้
```
[user]
    email = User email
    name = User name
```

<br/><br/>

### 3.5.2 รับ D3-G จาก Git

1. สร้างไดเรกทอรีใหม่ชื่อ **topst-sdk** และเปลี่ยนไดเรกทอรีปัจจุบันเป็น **topst-sdk**

```
$ mkdir topst-sdk
$ cd topst-sdk
```

2. รันคำสั่งต่อไปนี้เพื่อเริ่มต้นรีพอสิทอรี

```
$ repo init -u https://github.com/topst-development/manifests.git -b release/1.3.0 -m linux_yp4.0_topst.xml
```

หลังจากรันคำสั่งแล้ว จะแสดงผลลัพธ์ดังต่อไปนี้

```
Downloading Repo source from https://gerrit.googlesource.com/git-repo

... A new version of repo (2.54) is available.
... New version is available at: /home/topst/topst-sdk/.repo/repo/repo
... The launcher is run from: /usr/bin/repo
!!! The launcher is not writable.  Please talk to your sysadmin or distro
!!! to get an update installed.


Your identity is: TopstDeveloper <topstdeveloper@gmail.com>
If you want to change this, please re-run 'repo init' with --config-name

repo has been initialized in /home/topst/topst-sdk
```

3. รันคำสั่งต่อไปนี้เพื่อซิงโครไนซ์รีพอสิทอรี

```
$ repo sync
```

หลังจากรันคำสั่งแล้ว จะแสดงผลลัพธ์ดังต่อไปนี้

```
... A new version of repo (2.54) is available.
... New version is available at: /home/topst/topst-sdk/.repo/repo/repo
... The launcher is run from: /usr/bin/repo
!!! The launcher is not writable.  Please talk to your sysadmin or distro
!!! to get an update installed.

Fetching: 100% (12/12), done in 33.103s
Checking out:  25% (3/12), done in 0.863s
Checking out:  75% (9/12), done in 0.415s
repo sync has finished successfully.
```

<br/><br/><br/>

## 3.6 การดำเนินการ topst-build.sh 
---
หากคุณรันสคริปต์ ./easy-setup.sh คุณจะเห็นหน้าจอต่อไปนี้ 

**ข้อควรระวัง: หากคุณรัน ./easy-setup.sh ใหม่อีกครั้ง โปรดระวังเนื่องจากซอร์สที่บิลด์ไว้จะถูกลบหากคุณเลือก yes**
```
./easy-setup.sh
```
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20AI-G/Software/Linux%20SDK/license1.png"></p>
<p align="center"><strong>รูปที่ 3.2 ข้อตกลงอนุญาตให้ใช้สิทธิสำหรับผู้ใช้ปลายทาง</strong></p>

เลื่อนลงไปที่ด้านล่างสุดของหน้าจอและอ่านประกาศนี้ หลังจากอ่านประกาศนี้แล้ว ให้กดปุ่มลูกศรขวาและ [Enter]
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20AI-G/Software/Linux%20SDK/license2.png"></p>
<p align="center"><strong>รูปที่ 3.3 ไปที่ 'Proceed to confirm'</strong></p>


จากนั้นท่านจะเห็นหน้าจอดังต่อไปนี้ 
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20AI-G/Software/Linux%20SDK/license3.png" ></p>
<p align="center"><strong>รูปที่ 3.4 หน้าจอยอมรับ </strong></p>


อิมเมจที่บิลด์จะถูกสร้างขึ้นในพาธต่อไปนี้:

- {TOPST_PATH}/build/d3-g-topst-main/tmp/deploy/images/d3-g-topst-main

topst-build.sh เป็นเชลล์สคริปต์ที่ตั้งค่าสภาพแวดล้อมหลักที่จำเป็นสำหรับการบิลด์อิมเมจสำหรับ D3-G และ AI-G ให้ดำเนินการคำสั่งต่อไปนี้ และเลือกตัวเลือกที่ 2 เพื่อเตรียมสภาพแวดล้อมการบิลด์สำหรับการติดตั้ง OS หลักบน D3-G



```
$ source poky/meta-topst/topst-build.sh 
Choose MACHINE
  1. ai-g-topst
  2. d3-g-topst-main
  3. d3-g-topst-sub
  4. d5-g-topst-main
  5. d5-g-topst-sub
select number(1-5) => 2
machine(d3-g-topst-main) selected.
You had no conf/local.conf file. This configuration file has therefore been
created for you from /home/topst/topst-sdk/poky/meta-topst/template/d3-g-topst-main/local.conf.sample
You may wish to edit it to, for example, select a different MACHINE (target
hardware). See conf/local.conf for more information as common configuration
options are commented.

You had no conf/bblayers.conf file. This configuration file has therefore been
created for you from /home/topst/topst-sdk/poky/meta-topst/template/d3-g-topst-main/bblayers.conf.sample
To add additional metadata layers into your configuration please add entries
to conf/bblayers.conf.

The Yocto Project has extensive documentation about OE including a reference
manual which can be found at:
    https://docs.yoctoproject.org

For more information about OpenEmbedded see the website:
    https://www.openembedded.org/

Yocto Project common targets are:
    core-image-minimal
    core-image-sato
    meta-toolchain
    adt-installer
    meta-ide-support


Telechips common targets are:
    telechips-topst-image-minimal
    telechips-topst-image-multimedia
    telechips-topst-image

    meta-toolchain-topst(Application Development Toolkit)


You can also run generated TOPST images on D3-G board

Other commonly useful commands are:
 - 'devtool' and 'recipetool' handle common recipe tasks
 - 'bitbake-layers' handles common layer tasks
 - 'oe-pkgdata-util' handles common target package tasks

```

รันคำสั่งต่อไปนี้เพื่อเริ่มการบิลด์ OS หลัก
```
$ bitbake telechips-topst-image
```

<br/><br/><br/>

## 3.7 การสร้างอิมเมจ Firmware Downloader (FWDN) 
---
ตัวเลือกนี้จะรวมไบนารีต่าง ๆ เข้าเป็นอิมเมจเดียวสำหรับอิมเมจแพลตฟอร์ม D3-G

ไฟล์ **output_d3g.fwdn.zip** ซึ่งประกอบด้วย **อิมเมจบิลด์ 'output_d3g.fai'** และ **ทูล FWDN** จะถูกสร้างขึ้นในพาธต่อไปนี้:

-  ~/topst-sdk

```
$ cd ~/topst-sdk

$ ./stitch-fai-d3.sh -f
Filesystem too small for a journal
[mktcimg] v1.2.1 - Nov 15 2021 19:33:18
location : bl3_ca72_a
location : 4096 sector(2097152 byte)
location : build/d3-g-topst-main/tmp/deploy/images/d3-g-topst-main/ca72_bl3.rom
location : boot
location : 122880 sector(62914560 byte)
location : build/d3-g-topst-main/tmp/deploy/images/d3-g-topst-main/tc-boot-d3-g-topst-main.img
location : system
location : 33554432 sector(17179869184 byte)
location : build/d3-g-topst-main/tmp/deploy/images/d3-g-topst-main/telechips-topst-image-d3-g-topst-main.ext4
location : dtb
location : 400 sector(204800 byte)
location : build/d3-g-topst-main/tmp/deploy/images/d3-g-topst-main/tcc8050-topst-d3-g.dtb
path : build/d3-g-topst-main/tmp/deploy/images/d3-g-topst-main/ca72_bl3.rom
uuid : 7eb23c82-ccc0-44ce-8237-3315fc34e3f5 , part-name : bl3_ca72_a
uuid : 1c76ef36-314d-4548-8207-5ab1d1376ca2 , part-name : boot
uuid : b32eb80f-e014-4f17-b140-77bf3e137ba0 , part-name : system
uuid : 429d8444-87b0-4c1d-8b3f-278dec2616f3 , part-name : dtb
crc32 of header : 2a7c0194
crc32 of partition array : b181e432
idx : 0  bl3_ca72_a
idx : 1  boot
idx : 2  system
idx : 3  dtb
crc32 of header : 2a7c0194
crc32 of partition array : 990446d3
Complete to make fai file
 
===== arguments info =====
 
--storage_size : 17818182656
--parttype : gpt
--area_name : "SD Data"
--outfile : /home/topst/topst-sdk/.stitch_tOPE26E/output_d3g.fai
--gptfile : /home/topst/topst-sdk/.stitch_tOPE26E/output_d3g.gpt
--fplist : /home/topst/topst-sdk/.stitch_tOPE26E/partition.single.list
--sector_size : 512
--sparse_fill : 0
 
===========================
 
[+] Packaging FWDN binaries
  adding: boot-firmware/ (stored 0%)
  adding: boot-firmware/boot.dual.json (deflated 87%)
  adding: boot-firmware/prebuilt/ (stored 0%)
  adding: boot-firmware/prebuilt/subcore_optee.rom (deflated 93%)
  adding: boot-firmware/prebuilt/mcert.bin (deflated 96%)
  adding: boot-firmware/prebuilt/fwdn.rom (deflated 49%)
  adding: boot-firmware/prebuilt/bconf.dual.bin (deflated 95%)
  adding: boot-firmware/prebuilt/ca72_bl1.rom (deflated 53%)
  adding: boot-firmware/prebuilt/dram_params.bin (deflated 81%)
  adding: boot-firmware/prebuilt/hsm.cs.bin (deflated 13%)
  adding: boot-firmware/prebuilt/ca72_bl2.rom (deflated 54%)
  adding: boot-firmware/prebuilt/ca53_bl1.rom (deflated 53%)
  adding: boot-firmware/prebuilt/optee.rom (deflated 93%)
  adding: boot-firmware/prebuilt/ca53_bl2.rom (deflated 52%)
  adding: boot-firmware/prebuilt/hsm.bin (deflated 49%)
  adding: boot-firmware/prebuilt/bconf.single.bin (deflated 93%)
  adding: boot-firmware/prebuilt/scfw.rom (deflated 57%)
  adding: boot-firmware/prebuilt/tcc8050_snor.cs.rom (deflated 93%)
  adding: boot-firmware/boot.single.json (deflated 87%)
  adding: boot-firmware/fwdn.json (deflated 50%)
  adding: fwdn (deflated 69%)
  adding: fwdn.bat (deflated 40%)
  adding: fwdn.exe (deflated 62%)
  adding: fwdn.sh (deflated 40%)
  adding: output_d3g.fai (deflated 73%)
  adding: output_d3g.gpt (deflated 99%)
  adding: output_d3g.gpt.back (deflated 98%)
  adding: output_d3g.gpt.prim (deflated 98%)
  adding: VtcUsbPort.dll (deflated 68%)

```

หากคุณเห็นบันทึกต่อไปนี้ หมายความว่าไฟล์ "output_d3g.fwdn.zip" ถูกสร้างขึ้นแล้ว 
```
$ ls
build  easy-setup.sh  mktcimg  output_d3g.fwdn.zip  poky  stitch-fai-ai.sh  stitch-fai-d3.sh  tools
```

</br></br><br/><br/>

# 4. การดาวน์โหลดเฟิร์มแวร์
---
บทนี้อธิบายวิธีใช้ ***FWDN*** เพื่อดาวน์โหลดเฟิร์มแวร์ไปยัง D3-G และเข้าสู่ระบบคอนโซล Linux  
***FWDN V8*** เป็นทูลบน PC สำหรับดาวน์โหลดเฟิร์มแวร์ทั้งในสภาพแวดล้อม Windows 10(11) 64 บิต และ Linux บทนี้อธิบายกรณีการดาวน์โหลดในสภาพแวดล้อม Windows และ Linux

<br/><br/><br/>

## 4.1 ลำดับการดาวน์โหลดเฟิร์มแวร์
---
ลำดับการดาวน์โหลดของ ***FWDN*** มีดังนี้:

1. ตั้งค่าสวิตช์โหมดการบูตเป็นโหมดการบูต USB
2. เปิดพรอมต์ของ Windows หรือคอนโซลของ Linux
3. เชื่อมต่อ ***FWDN V8*** เข้ากับบอร์ด
4. ดาวน์โหลดไฟล์ fai

<br/><br/><br/>

## 4.2 เชื่อมต่อบอร์ด D3-G กับเครื่อง PC โฮสต์ด้วยโหมดการบูต USB
---
Firmware Downloader (FWDN) เขียนอิมเมจ ROM ลงใน D3-G ผ่านการสื่อสาร USB กับเครื่อง PC โฮสต์ 

D3-G มีปุ่ม Boot Mode หนึ่งปุ่มและรองรับโหมดการบูตสองประเภท คู่มือนี้มุ่งเน้นไปที่โหมด FWDN

- USB Boot Mode (FWDN Mode) : ใช้สำหรับเขียนอิมเมจ ROM โดยใช้ทูล FWDN บนเครื่อง PC โฮสต์ของคุณ 

- eMMC Boot Mode : ใช้สำหรับบูต D3-G โดยใช้อิมเมจ ROM ที่จัดเก็บอยู่ในอุปกรณ์ eMMC 

**หมายเหตุ**: พอร์ต USB Type-C FWDN ใช้สำหรับ firmware downloader (FWDN) 



หากต้องการใช้ FWDN ให้เชื่อมต่อบอร์ด D3-G เข้ากับเครื่อง PC โฮสต์ดังนี้: 

1. ตรวจสอบว่าได้ติดตั้งไดรเวอร์ VTC บนเครื่อง PC โฮสต์แล้ว หากยังไม่ได้ติดตั้งไดรเวอร์ VTC ให้ติดตั้งตามที่แสดงในบทที่ 4.2.1  

2. เตรียมสาย USB Type-C หนึ่งเส้น 

3. หากต้องการเข้าสู่โหมดการบูต USB ให้เชื่อมต่อสายไฟเข้ากับบอร์ด D3-G ขณะที่กดสวิตช์ FWDN ค้างไว้
   - สำหรับรายละเอียดเพิ่มเติม โปรดดู **"2. Boot Mode"** ในส่วน Hardware ของแถบด้านข้าง

4. เชื่อมต่อสาย USB Type-C เข้ากับพอร์ต USB Type-C FWDN บนบอร์ด D3-G และเครื่อง PC โฮสต์ 

<p align="center">
    <img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20D3-G/Hardware/connect%20to%20d3g%20to%20host%20pc%20using%20c%20type.png">
</p>
<p align="center"><strong>รูปที่ 4.1 การเชื่อมต่อบอร์ด D3-G กับเครื่อง PC โฮสต์โดยใช้สาย USB C-Type </strong></p>

<br/><br/>

### 4.2.1 วิธีติดตั้งไดรเวอร์ VTC (Windows/Ubuntu)
ติดตั้งไดรเวอร์ Vendor Telechips Certification (VTC) (อยู่ที่ [telechips driver](https://drive.google.com/file/d/1muQnY8kuKxDsy3p3FUiQqcG34Zjk-mnR/view?usp=sharing)) บนเครื่อง PC โฮสต์โดยเรียกใช้ในฐานะผู้ดูแลระบบ เมื่อคุณเชื่อมต่อ USB ในโหมด FWDN ดังที่แสดงไว้ข้างต้น ไดรเวอร์ Telechips VTC USB จะถูกตั้งค่าดังแสดงในรูปที่ 4.2 และรูปที่ 4.3

<p align="center">
    <img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20D3-G/Software/USB%20Connection%20in%20Windows%20Environment.png", width="700">
</p>
<p align="center"><strong>รูปที่ 4.2 การเชื่อมต่อ USB ในสภาพแวดล้อม Windows</strong></p>

<p align="center">
    <img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20D3-G/Software/USB%20Connection%20in%20Linux%20System.png", width="700">
</p>
<p align="center"><strong>รูปที่ 4.3 การเชื่อมต่อ USB ในสภาพแวดล้อม Linux</strong></p>  

**หมายเหตุ**: ใช้ไดรเวอร์ VTC เวอร์ชัน V5.0.0.14 ขึ้นไป หากต้องการตรวจสอบเวอร์ชัน ให้ยืนยันที่ตัวจัดการอุปกรณ์ในสภาพแวดล้อม Windows  

<br/><br/><br/>

## 4.3 การเตรียมพร้อมสำหรับการดาวน์โหลด FWDN
---
ก่อนดำเนินการ FWDN ให้ถ่ายโอนอิมเมจและทูลที่สร้างขึ้นในสภาพแวดล้อม Ubuntu (WSL2) ไปยังสภาพแวดล้อม Windows


1. แตกไฟล์ "output_d3g.fwdn.zip"   
    ```
    $ cd ~/topst-sdk
    $ mkdir images
    $ mv ./output_d3g.fwdn.zip ./images
    $ cd images
    $ unzip output_d3g.fwdn.zip
    ```
2. คัดลอกโฟลเดอร์ "images" ไปยังไดรฟ์ C ของ Windows  
    ```
    $ cd ..
    $ cp -r ./images /mnt/c/
    ```

<br/><br/><br/>

## 4.4 FWDN ในสภาพแวดล้อม Windows
---
1. ดำเนินการ Powershell และไปที่ "C:\images\"
```
$ cd C:\images 
```

2. ป้อนคำสั่ง **.\fwdn.bat** เพื่อเริ่มการดาวน์โหลดเฟิร์มแวร์ “fwdn.bat” เป็นไฟล์ปฏิบัติการที่ดาวน์โหลดเฟิร์มแวร์โดยอัตโนมัติด้วย FWDN V8 

```
.\fwdn.bat

C:\images>fwdn.exe --fwdn boot-firmware\fwdn.json
[main:30] FWDN V8 v1.4.6 - 2021.12.13 13:42:37
[FWDN_V8::LoadFWDNRom:403] Start to load FWDN rom
[FWDN_V8::LoadMCERT:592] C:\images\boot-firmware\mcert.bin
[FWDN_V8::LoadHSM:609] C:\images\boot-firmware\hsm.cs.bin
[FWDN_V8::SendFWDNHeader:634] C:\images\boot-firmware\fwdn.rom - Header
[FWDN_V8::SendFWDNBody_V8:537] C:\images\boot-firmware\fwdn.rom - Body
[FWDN_V8::LoadFWDNRom:414] Complete to load FWDN rom
[FWDN_V8::GetFWDNRomVersion:1526] fwdn.rom version : 21.9.29
[FWDN_V8::GetFileAndWriteCommand:748] C:\images\boot-firmware\dram_params.bin
[FWDN_V8::PrintDeviceInfo:1183] --------------Device info-------------
[FWDN_V8::PrintDeviceInfo:1184]

----- Detail of Storages -----
#### eMMC Info ####
Manufacture ID: 0x15
OEM: 0x100
Name: 8GTF4
User Capacity: 7.3 GiB (7818182656 Byte)
Boot Capacity: 4 MiB (4194304 Byte)
RPMB Capacity: 512 KiB (524288 Byte)
Speed Mode: HS200
#### SNOR Info ####
Manufacture ID: 0xc2
Device ID: 0x2016
Name: MXIC-MX25L3233F
Sector Size: 4 KiB (4096 Byte)
Total Capacity: 4 MiB (4194304 Byte)
4Byte Address Mode: Unsupported

----- Summary of Storages -----
eMMC : O
SNOR : O
UFS : X
- O : Init success
- X : Init failed or not exist

----- Summary of DRAM Init -----
DRAM Init : Success (Result 0x0 )
DRAM Size : 4096MB

[FWDN_V8::PrintDeviceInfo:1185] --------------------------------------
[main:142] Complete FWDN
[FWDNLogger::PrintCurTime:111] 24/04/25-09:57:47

C:\images>fwdn.exe --storage emmc --low-format
[main:30] FWDN V8 v1.4.6 - 2021.12.13 13:42:37
[FWDN_V8::GetFWDNRomVersion:1526] fwdn.rom version : 21.9.29
[FWDN_V8::LowformatCommand:1352] Start low-format
[FWDN_V8::LowformatCommand:1353] low-format can take a long time
[FWDN_V8::LowformatCommand:1382] Complete low-format
[main:142] Complete FWDN
[FWDNLogger::PrintCurTime:111] 24/04/25-09:57:50

C:\images>fwdn.exe -w boot-firmware\boot.single.json
[main:30] FWDN V8 v1.4.6 - 2021.12.13 13:42:37
[FWDN_V8::GetFWDNRomVersion:1526] fwdn.rom version : 21.9.29
[main:117] Start write command
[FWDN_V8::GetFileAndWriteCommand:748] C:\images\boot-firmware\bconf.single.bin
[FWDN_V8::GetFileAndWriteCommand:748] C:\images\boot-firmware\bconf.single.bin
[FWDN_V8::GetFileAndWriteCommand:748] C:\images\boot-firmware\mcert.bin
[FWDN_V8::GetFileAndWriteCommand:748] C:\images\boot-firmware\mcert.bin
[FWDN_V8::GetFileAndWriteCommand:748] C:\images\boot-firmware\dram_params.bin
[FWDN_V8::GetFileAndWriteCommand:748] C:\images\boot-firmware\dram_params.bin
[FWDN_V8::GetFileAndWriteCommand:748] C:\images\boot-firmware\hsm.cs.bin
[FWDN_V8::GetFileAndWriteCommand:748] C:\images\boot-firmware\hsm.cs.bin
[FWDN_V8::GetFileAndWriteCommand:748] C:\images\boot-firmware\scfw.rom
[FWDN_V8::GetFileAndWriteCommand:748] C:\images\boot-firmware\scfw.rom
[FWDN_V8::GetFileAndWriteCommand:748] C:\images\boot-firmware\optee.rom
[FWDN_V8::GetFileAndWriteCommand:748] C:\images\boot-firmware\optee.rom
[FWDN_V8::GetFileAndWriteCommand:748] C:\images\boot-firmware\ca72_bl1.rom
[FWDN_V8::GetFileAndWriteCommand:748] C:\images\boot-firmware\ca72_bl1.rom
[FWDN_V8::GetFileAndWriteCommand:748] C:\images\boot-firmware\ca53_bl1.rom
[FWDN_V8::GetFileAndWriteCommand:748] C:\images\boot-firmware\ca53_bl1.rom
[FWDN_V8::GetFileAndWriteCommand:748] C:\images\boot-firmware\ca72_bl2.rom
[FWDN_V8::GetFileAndWriteCommand:748] C:\images\boot-firmware\ca72_bl2.rom
[FWDN_V8::GetFileAndWriteCommand:748] C:\images\boot-firmware\ca53_bl2.rom
[FWDN_V8::GetFileAndWriteCommand:748] C:\images\boot-firmware\ca53_bl2.rom
[main:125] Complete write command
[main:142] Complete FWDN
[FWDNLogger::PrintCurTime:111] 24/04/25-09:57:53
100% [||||||||||||||||||||||||||||||] 859264/859264
C:\images>fwdn.exe -w "output_d3g.fai" --storage emmc --area user
[main:30] FWDN V8 v1.4.6 - 2021.12.13 13:42:37
[FWDN_V8::GetFWDNRomVersion:1526] fwdn.rom version : 21.9.29
[main:117] Start write command
[FWDN_V8::GetFileAndWriteCommand:748] output_d3g.fai
[main:125] Complete write command
[main:142] Complete FWDN
[FWDNLogger::PrintCurTime:111] 24/04/25-10:05:21
100% [||||||||||||||||||||||||||||||] 7238688960/7238688960
** When writing FAI files without low-format, there may be garbage values in partition where data is not written.
```

<br/><br/><br/>

## 4.5  FWDN ในสภาพแวดล้อม Linux
---
หากต้องการดาวน์โหลดอิมเมจ D3-G ใน Linux ให้ดำเนินการคำสั่งต่อไปนี้: "./fwdn.sh"

```
$ ./fwdn.sh
```

คุณพร้อมที่จะบูต D3-G แล้ว โปรดดูบทที่ 5 เพื่อเริ่มการสื่อสารกับอุปกรณ์


<br/><br/><br/><br/>

# 5. การเชื่อมต่อบอร์ด D3-G กับเครื่อง PC โฮสต์
---
บทนี้อธิบายวิธีเชื่อมต่อเครื่อง PC โฮสต์เข้ากับบอร์ด D3-G ผ่าน UART สำหรับการดาวน์โหลดเฟิร์มแวร์และการสื่อสารแบบอนุกรม

<br/><br/><br/>

## 5.1 การเชื่อมต่อบอร์ด D3-G ด้วย UART 
---
ทำตามขั้นตอนเหล่านี้และตรวจสอบว่าการดาวน์โหลดเฟิร์มแวร์เสร็จสมบูรณ์แล้วโดยใช้การเชื่อมต่อ UART 

1. ติดตั้งไดรเวอร์พอร์ตอนุกรม (เช่น CP210x Windows Driver) และไดรเวอร์ PL2303_prolific ในสภาพแวดล้อม Windows 
2. ติดตั้งโปรแกรมจำลองเทอร์มินัล เช่น Tera Term หรือ PuTTY 
3. เชื่อมต่อเครื่อง PC โฮสต์กับพิน UART บนบอร์ด D3-G ใช้สาย USB-to-TTL 
4. เชื่อมต่อสายสีดำเข้ากับพิน GND 
5. เชื่อมต่อสายสีขาว (RXD) เข้ากับพิน TX ของพิน UART และเชื่อมต่อสายสีเขียว (TXD) เข้ากับพิน RX ของพิน UART
6. รันแอปพลิเคชันจำลองเทอร์มินัล
7. เปิดตัวจัดการอุปกรณ์บน PC ของคุณและตรวจสอบหมายเลขพอร์ตที่กำหนดให้กับอุปกรณ์ UART
8. ในโปรแกรมจำลองเทอร์มินัล ให้ป้อนหมายเลขพอร์ตที่ตรวจสอบแล้วลงในช่อง Serial line ตั้งค่า **Speed** (bps) เป็น 115200 และ **Flow control** เป็น **None**
9. เชื่อมต่อสายไฟ จากนั้นบอร์ด D3-G จะบูตในโหมดการบูต eMMC ตามค่าเริ่มต้น


 
<p align="center">
    <img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20D3-G/Software/USB%20to%20TTL%20Connection.png", width="700">
</p>
<p align="center"><strong>รูปที่ 5.1 การเชื่อมต่อ UART กับเครื่อง PC โฮสต์</strong></p><br/>  


รูปที่ 5.2 แสดงการเข้าสู่ระบบที่สำเร็จ  
ทั้งชื่อผู้ใช้และรหัสผ่านสำหรับการเข้าสู่ระบบถูกตั้งค่าเป็น **root**

<p align="center">
    <img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20D3-G/Software/d3-g%20login%20as%20root.png", width="700">
</p>
<p align="center"><strong>รูปที่ 5.2 หน้าจอที่เชื่อมต่อแล้ว (ID และรหัสผ่านคือ topst)</strong></p><br/>

<br/><br/><br/>

# 6. การปรับขนาดพาร์ทิชันของ Ubuntu OS
---
เรายังมี Ubuntu OS ให้บริการด้วย
เมื่อทำตามบทนี้ คุณสามารถดาวน์โหลดอิมเมจ Ubuntu อัปโหลดไปยังบอร์ด และขยายความจุพื้นที่จัดเก็บ eMMC ที่จัดสรรไว้ได้

<br/><br/><br/>

## 6.1 ดาวน์โหลดอิมเมจ Ubuntu
---
ระบบอย่างเป็นทางการของ D3-G อ้างอิงจาก Ubuntu 22.04  
คุณสามารถดาวน์โหลดไฟล์อิมเมจได้ที่นี่  

<img src="https://github.com/topst-development/Documentation/assets/161264431/83d93c78-6437-4f96-a0bf-23f22da1aba1">  

**ดาวน์โหลด :**  
-	[ลิงก์ดาวน์โหลดที่นี่](https://drive.google.com/file/d/1oc2qwaXUt6-QDME3s5WXKVHzAg4xqVyc/view?usp=drive_link)
<br>
-	สำหรับข้อมูลเพิ่มเติม โปรดไปที่ [หน้า github](https://github.com/topst-development) ของเรา

**บันทึกการเผยแพร่ :**  

|Ver|   วันที่   |
|:-:|:--------:|
|1.0|2024.04.25|  

ทีม TOPST กำลังเตรียม OS เวอร์ชันอย่างเป็นทางการอื่น ๆ ด้วยเช่นกัน  
สำหรับข้อมูลเกี่ยวกับการเผยแพร่ OS อื่น ๆ โปรดดูที่ชุมชน TOPST  

<br/><br/><br/>

## 6.2 การอัปโหลดเฟิร์มแวร์ไปยัง D3-G
---
รันไฟล์ “fwdn_ubuntu.batch” 
โปรดดูบทที่ 5 สำหรับวิธีอัปโหลดอิมเมจ Ubuntu ไปยัง D3-G
หลังจาก FWDN เสร็จสิ้น ให้ถอดสาย USB Type-C ออกจากพอร์ต FWDN และถอดสายไฟออก 

<br/><br/><br/>

## 6.3 ปรับขนาดพื้นที่จัดเก็บ eMMC (เฉพาะ D3-G)
---
หลังจากเข้าสู่ระบบและบูตบอร์ดแล้ว ขอแนะนำให้ปรับขนาดพื้นที่จัดเก็บ eMMC ก่อน
ทำตามขั้นตอนด้านล่างเพื่อปรับขนาดพื้นที่จัดเก็บ eMMC

1. หากต้องการแก้ไขขนาดและเลย์เอาต์ของพาร์ทิชัน ให้ใช้คำสั่งต่อไปนี้
     ```
     $ parted
     ```

2. ขยาย GUID Partition Table(GPT) 
    ```
    $ rescue
    $ Fix 
    $ 0 
    $ 100%
    ```
3. ใช้คำสั่ง p (print) เพื่อตรวจสอบว่าประเภทพาร์ทิชันเป็น ext4 
   ```
   $ p
   ```
4. ปรับขนาดพาร์ทิชัน 4
    ```
    $ resizepart 4
    $ Yes
    $ 100%
    ```
5. รีบูตบอร์ด
6. ปรับขนาดระบบไฟล์ ext4 บนพาร์ทิชัน 4
    ```
    $ resize2fs /dev/mmcblk0p4
    ```
7. ตรวจสอบขนาดพาร์ทิชันที่เปลี่ยนแปลงโดยใช้คำสั่งต่อไปนี้
   ```
   $ df -h
   ```

คุณสามารถยืนยันได้ว่าพื้นที่ว่างคือ 27GB หลังจากการปรับขนาด

<br/><br/><br/><br/>

# 7. เอกสารอ้างอิง
---
- ติดต่อ TOPST สำหรับรายละเอียดเพิ่มเติม: topst@topst.ai

**หมายเหตุ:** เอกสารอ้างอิงสามารถจัดหาให้ได้เมื่อมีอยู่ ทั้งนี้ขึ้นอยู่กับเงื่อนไขของสัญญา หากไม่มีเอกสาร
อ้างอิงดังกล่าว จะมีการแนะนำเนื้อหาที่เกี่ยวข้องโดยตรงกับการพัฒนาของท่านแทน
