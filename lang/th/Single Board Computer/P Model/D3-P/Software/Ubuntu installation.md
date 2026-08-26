# 1. บทนำ
เอกสารนี้อธิบายวิธีการพัฒนาสภาพแวดล้อม Ubuntu ในคอร์หลัก (CA72) ของ TOPST D3 (บอร์ดแพลตฟอร์มแบบเปิด) นอกเหนือจากอิมเมจ Ubuntu ดั้งเดิมที่มีให้บนบอร์ดแล้ว เอกสารนี้ยังอธิบายวิธีการพัฒนาสภาพแวดล้อม Ubuntu เฉพาะทางของคุณเองด้วย ระบบไฟล์ ubuntu ที่ผู้ใช้สร้างขึ้นสามารถดาวน์โหลดไปยังพื้นที่ระบบไฟล์ของคอร์หลัก (CA72) ได้โดยใช้เครื่องมือ **_FWDN_**

เอกสารนี้อธิบายตามลำดับต่อไปนี้:
* คู่มือการสร้างระบบไฟล์ Ubuntu
* คู่มือ FWDN
* หน้าจอ GUI ของ Ubuntu ที่บูตแล้ว 
  
<br><br>

# 2. คู่มือการสร้างระบบไฟล์ Ubuntu

บทนี้อธิบายวิธีการติดตั้งระบบไฟล์ Ubuntu สำหรับคอร์หลัก (CA72) บนเครื่อง Host PC

โปรดดู “Documentation/TOPST-D3/Software/SDK/LINUX” สำหรับสภาพแวดล้อมการพัฒนาของผู้ใช้

<br><br>

## 2.1. รับ Ubuntu ด้วย Git
เวอร์ชัน Ubuntu ที่ Git ให้มาคือ Ubuntu 22.04.2 LTS (Jammy Jellyfish) ดังแสดงด้านล่าง

```
$ git clone https://gitlab.com/topst.ai/topst-d3-ubuntu.git
```

<br><br>

# 3. เรียกใช้สคริปต์


เรียกใช้ 'populate_ubuntu.sh'
```
$ sudo ./populate_ubuntu.sh 
[!] Prepare workspace
[!] Initial debian bootstraping
I: Retrieving InRelease 
I: Checking Release signature
I: Valid Release signature (key id F6ECB3762474EDA9D21B7022871920D1991BC93C)
I: Retrieving Packages 
I: Validating Packages 
I: Resolving dependencies of required packages...
I: Resolving dependencies of base packages...
I: Checking component main on http://ports.ubuntu.com/ubuntu-ports...
I: Retrieving adduser 3.118ubuntu5
I: Validating adduser 3.118ubuntu5
I: Retrieving apt 2.4.5
I: Validating apt 2.4.5
I: Retrieving apt-utils 2.4.5
I: Validating apt-utils 2.4.5
I: Retrieving base-files 12ubuntu4
I: Validating base-files 12ubuntu4
I: Retrieving base-passwd 3.5.52build1
I: Validating base-passwd 3.5.52build1
I: Retrieving bash 5.1-6ubuntu1
I: Validating bash 5.1-6ubuntu1
I: Retrieving bsdutils 1:2.37.2-4ubuntu3
I: Validating bsdutils 1:2.37.2-4ubuntu3
I: Retrieving ca-certificates 20211016
I: Validating ca-certificates 20211016
I: Retrieving console-setup 1.205ubuntu3
I: Validating console-setup 1.205ubuntu3
I: Retrieving console-setup-linux 1.205ubuntu3
I: Validating console-setup-linux 1.205ubuntu3
I: Retrieving coreutils 8.32-4.1ubuntu1
I: Validating coreutils 8.32-4.1ubuntu1
I: Retrieving cron 3.0pl1-137ubuntu3
I: Validating cron 3.0pl1-137ubuntu3
I: Retrieving dash 0.5.11+git20210903+057cd650a4ed-3build1
I: Validating dash 0.5.11+git20210903+057cd650a4ed-3build1
I: Retrieving dbus 1.12.20-2ubuntu4

                   ㆍ
                   ㆍ
                   ㆍ
```
คุณสามารถตรวจสอบไฟล์ etx4 ได้ด้านล่าง
```
$ ls
populate_ubuntu.sh  src  ubuntu.ext4
```


