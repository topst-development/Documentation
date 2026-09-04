# AI-G クイックガイド
---

## 1.1 USB 起動モード (FWDN モード) 
---
ビルドしたイメージは ***FWDN*** を使用して AI-G に転送できます。AI-G は Ethernet および UART を使用して ***FWDN*** を提供します。 

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20AI-G/Software/Linux%20SDK/3.%20connect%20host%20pc%20to%20topst%20ai-g.png" ></p>
<p align="center"><strong>図 1.1 FWDN のためのホスト PC と AI-G の接続</strong></p><br/>

***FWDN V8*** を使用するには、次のように AI-G ボードをホスト PC に接続してください。 

1. ホスト PC に VTC ドライバがインストールされていることを確認してください。VTC ドライバがインストールされていない場合は、第 4.2.1 章に示すとおりにインストールしてください。  

2. USB Type-C ケーブル 1 本と Ethernet ケーブル 1 本を用意してください。 

3. USB 起動モードに入るには、USB Type-C ケーブルを AI-G ボードの USB Type-C FWDN ポートとホスト PC に接続してください。 

4. Ethernet ケーブル (RJ45) を AI-G ボードの Ethernet ポートとホスト PC に接続してください。 

5. FWDN スイッチを押しながら、電源ケーブルを AI-G ボードに接続してください。 

<br/><br/><br/>

## 1.2 VCP ドライバのインストール方法

ホスト PC 上で管理者として実行し、Vendor Telechips Certification (VTC) ドライバ ([VCP ドライバ](https://drive.google.com/file/d/1muQnY8kuKxDsy3p3FUiQqcG34Zjk-mnR/view?usp=sharing) にあります) をインストールしてください。上記のように FWDN モードで USB を接続すると、図 1.2 のように Telechips VTC USB ドライバが設定されます。

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20AI-G/Software/Linux%20SDK/4.%20VTC.png" width="550"></p>
<p align="center"><strong>図 1.2 COM ポートの確認</strong></p><br/>

<br/><br/>

## 1.3 Ethernet の設定

ホスト PC のネットワーク構成 

- コントロール パネル → ネットワークとインターネット → ネットワーク接続 → FWDN 用の Ethernet デバイスのプロパティを設定 
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20AI-G/Software/Linux%20SDK/5.%20network_setting.png"></p>
<p align="center"><strong>図 1.3 FWDN 用の Ethernet デバイスのプロパティ設定</strong></p><br/>
<br/><br/><br/>

## 1.4 WMIC の追加
FWDN の前に、AI-G ボードの FWDN ポートに接続されているポートを確認するために WMIC をインストールする必要があります。

1. 設定を開く: スタート メニューから設定を開きます。
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20AI-G/Software/Linux%20SDK/8.%20Open%20Settings%20from%20Start%20menu.png"></p>
<p align="center"><strong>図 1.4 スタート メニューから設定を開く</strong></p>  <br/>

2. システムの選択: システム メニューに移動します。
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20AI-G/Software/Linux%20SDK/9.%20Go%20to%20the%20System%20menu.png"></p>
<p align="center"><strong>図 1.5 システム メニューに移動</strong></p>  <br/>

3. オプション機能: オプション機能メニューをクリックします。
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20AI-G/Software/Linux%20SDK/10.%20Click%20the%20Selective%20Features%20menu.png"></p>
<p align="center"><strong>図 1.6 オプション機能メニューをクリック</strong></p>  <br/>

4. 機能の表示: **オプション機能の追加** の横にある **機能の表示** ボタンをクリックします。
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20AI-G/Software/Linux%20SDK/11.%20Click%20the%20View%20Features%20button%20next%20to%20Add%20optional%20Features.png"></p>
<p align="center"><strong>図 1.7 オプション機能の追加の横にある機能の表示ボタンをクリック</strong></p>  <br/>

5. WMIC の検索: 検索ボックスに **"WMIC"** と入力します。
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20AI-G/Software/Linux%20SDK/12.%20Type%20WMIC%20in%20the%20search%20box.png"></p>
<p align="center"><strong>図 1.8 検索ボックスに WMIC と入力</strong></p>  <br/>

6. インストール: WMIC の項目を選択し、**"次へ"** ボタンをクリックしてインストールを完了します。
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20AI-G/Software/Linux%20SDK/13.%20Select%20the%20WMIC%20item%20and%20click%20the%20Next%20button%20to%20complete%20the%20installation.png"></p>
<p align="center"><strong>図 1.9 WMIC の項目を選択し、次へボタンをクリックしてインストールを完了</strong></p>  <br/>

## 1.5 Windows 環境での FWDN の実行
1. ダウンロード ページに移動します。

2. AI-G Yocto イメージのダウンロード
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/Quick%20Guide/Download%20AI-G%20Image.png" width="550"></p>
<p align="center"><strong>図 1.10 AI-G Yocto イメージのダウンロード</strong></p> <br/>

3. fwdn_aig.bat をクリックします。「fwdn_aig.bat」は ***FWDN V8*** を使用してファームウェアを自動的にダウンロードする実行ファイルです。 
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/Quick%20Guide/Click%20fwdn_aig.bat.png" width="550"></p>
<p align="center"><strong>図 1.11 fwdn_aig.bat をクリック</strong></p> <br/>

```
TOPST AI-G FWDN Batch File

Find Port.
Silicon Labs CP210x USB to UART Bridge(COM44)

Input USB Port Number : 44


Step 1. Connect between Host PC and TOPST AI-G
[FWDNLogger::PrintCurTime:100] 25/06/12-16:11:36
[main:24] FWDN N-Dolphin v1.0.1 - 2024.9.24 16:18:11
[main:92] Start FWDN
[FWDN_ND::ImageSend:442] Complete to send MCERT image
[FWDN_ND::ImageSend:442] Complete to send HSM image
[FWDN_ND::ImageSend:442] Complete to send FWDN_BL1 image
[FWDN_ND::ImageSend:442] Complete to send FWDN_DRAM_PARAMETER image
[FWDN_ND::ImageSend:442] Complete to send FWDN_BL2 image
[FWDN_ND::ImageSend:442] Complete to send FWDN_BL3 image
[FWDN_ND::InfoDevice:123] ############## Device Info ##############
[PrintIP:527] ip      : 192.168.0.100
[PrintIP:527] mask    : 255.255.255.0
[PrintIP:527] gateway : 0.0.0.0
[FWDN_ND::InfoDevice:132] port : 8080
[FWDN_ND::InfoDevice:135]
mmc0_user: 7818182656 byte block_size: 512 byte
mmc0_boot0: 4194304 byte block_size: 512 byte
mmc0_boot1: 4194304 byte block_size: 512 byte
snor1: 0 byte
snor2: 0 byte
fw_version: tcc750x_v0.0.111
fw_build_id: g90e2b777
fw_build_date: 2024-09-24-17:11:42+0900

----- Firmware Information -----
VERSION    : tcc750x_v0.0.111
BUILD ID   : g90e2b777
BUILD DATE : 2024-09-24-17:11:42+0900

----- Detail of Storages -----
#### eMMC Info ####
Manufacture ID: 0x15
OEM: 0x100
Name: 0x8GTF4
User Capacity: 7.3 GiB (7818182656 Byte)
Boot Capacity: 4 MiB (4194304 Byte)
RPMB Capacity: 512 KiB (524288 Byte)
Speed Mode: HS200
#### SNOR Info ####

----- Summary of Storages -----
eMMC : O
SNOR : X
- O : Init success
- X : Init failed or not exist

----- Summary of DRAM Init -----
DRAM Init : Success
DRAM Size : TBD MB

----- PMU Status -----
PMU_USER   : 0x0
PMU_SIC_USER   : 0x80
PMU_CONFIG : 0x0
* BM : PMU_CONFIG[1:0]
-  0 : USB BOOT
-  1 : SNOR BOOT
-  2 : eMMC BOOT
-  3 : eMMC with SIC BOOT

--------------------------------

[FWDN_ND::LoadFwdnFW:676] TCP Ready OK
[main:156] Complete FWDN, Total Time = 18424 ms
[main:162] **Notification : For more detailed FWDN Log, use the -g or --debug option.

Step 2. Low-format
[FWDNLogger::PrintCurTime:100] 25/06/12-16:11:55
[main:24] FWDN N-Dolphin v1.0.1 - 2024.9.24 16:18:11
[main:92] Start FWDN
[FWDN_ND::InfoDevice:123] ############## Device Info ##############
[PrintIP:527] ip      : 192.168.0.100
[PrintIP:527] mask    : 255.255.255.0
[PrintIP:527] gateway : 0.0.0.0
[FWDN_ND::InfoDevice:132] port : 8080
[FWDN_ND::InfoDevice:135]
mmc0_user: 7818182656 byte block_size: 512 byte
mmc0_boot0: 4194304 byte block_size: 512 byte
mmc0_boot1: 4194304 byte block_size: 512 byte
snor1: 0 byte
snor2: 0 byte
fw_version: tcc750x_v0.0.111
fw_build_id: g90e2b777
fw_build_date: 2024-09-24-17:11:42+0900

----- Firmware Information -----
VERSION    : tcc750x_v0.0.111
BUILD ID   : g90e2b777
BUILD DATE : 2024-09-24-17:11:42+0900

----- Detail of Storages -----
#### eMMC Info ####
Manufacture ID: 0x15
OEM: 0x100
Name: 0x8GTF4
User Capacity: 7.3 GiB (7818182656 Byte)
Boot Capacity: 4 MiB (4194304 Byte)
RPMB Capacity: 512 KiB (524288 Byte)
Speed Mode: HS200
#### SNOR Info ####

----- Summary of Storages -----
eMMC : O
SNOR : X
- O : Init success
- X : Init failed or not exist

----- Summary of DRAM Init -----
DRAM Init : Success
DRAM Size : TBD MB

----- PMU Status -----
PMU_USER   : 0x0
PMU_SIC_USER   : 0x80
PMU_CONFIG : 0x0
* BM : PMU_CONFIG[1:0]
-  0 : USB BOOT
-  1 : SNOR BOOT
-  2 : eMMC BOOT
-  3 : eMMC with SIC BOOT

--------------------------------

[ParseStorageSize:558] 1
[ParseStorageSize:583] 7818182656,7818182656
[FWDN_ND::LoadFwdnFW:676] TCP Ready OK
[FWDN_ND::LowformatCommand:1495] Lowformat Start(eMMC)
[main:156] Complete FWDN, Total Time = 1755 ms
[main:162] **Notification : For more detailed FWDN Log, use the -g or --debug option.

Step 3. Download boot-firmware
[FWDNLogger::PrintCurTime:100] 25/06/12-16:11:57
[main:24] FWDN N-Dolphin v1.0.1 - 2024.9.24 16:18:11
[main:92] Start FWDN
[FWDN_ND::InfoDevice:123] ############## Device Info ##############
[PrintIP:527] ip      : 192.168.0.100
[PrintIP:527] mask    : 255.255.255.0
[PrintIP:527] gateway : 0.0.0.0
[FWDN_ND::InfoDevice:132] port : 8080
[FWDN_ND::InfoDevice:135]
mmc0_user: 7818182656 byte block_size: 512 byte
mmc0_boot0: 4194304 byte block_size: 512 byte
mmc0_boot1: 4194304 byte block_size: 512 byte
snor1: 0 byte
snor2: 0 byte
fw_version: tcc750x_v0.0.111
fw_build_id: g90e2b777
fw_build_date: 2024-09-24-17:11:42+0900

----- Firmware Information -----
VERSION    : tcc750x_v0.0.111
BUILD ID   : g90e2b777
BUILD DATE : 2024-09-24-17:11:42+0900

----- Detail of Storages -----
#### eMMC Info ####
Manufacture ID: 0x15
OEM: 0x100
Name: 0x8GTF4
User Capacity: 7.3 GiB (7818182656 Byte)
Boot Capacity: 4 MiB (4194304 Byte)
RPMB Capacity: 512 KiB (524288 Byte)
Speed Mode: HS200
#### SNOR Info ####

----- Summary of Storages -----
eMMC : O
SNOR : X
- O : Init success
- X : Init failed or not exist

----- Summary of DRAM Init -----
DRAM Init : Success
DRAM Size : TBD MB

----- PMU Status -----
PMU_USER   : 0x0
PMU_SIC_USER   : 0x80
PMU_CONFIG : 0x0
* BM : PMU_CONFIG[1:0]
-  0 : USB BOOT
-  1 : SNOR BOOT
-  2 : eMMC BOOT
-  3 : eMMC with SIC BOOT

--------------------------------

[FWDN_ND::LoadFwdnFW:676] TCP Ready OK
[main:121] Start Write
[FWDN_ND::GetFileAndWriteCommand:1388] C:\output_aig.fwdn\boot-firmware\.\prebuilt\bconf.bin
[FWDN_ND::GetFileAndWriteCommand:1388] C:\output_aig.fwdn\boot-firmware\.\prebuilt\bconf.bin
[FWDN_ND::GetFileAndWriteCommand:1388] C:\output_aig.fwdn\boot-firmware\.\prebuilt\mcert.bin
[FWDN_ND::GetFileAndWriteCommand:1388] C:\output_aig.fwdn\boot-firmware\.\prebuilt\mcert.bin
[FWDN_ND::GetFileAndWriteCommand:1388] C:\output_aig.fwdn\boot-firmware\.\prebuilt\dram_params.bin
[FWDN_ND::GetFileAndWriteCommand:1388] C:\output_aig.fwdn\boot-firmware\.\prebuilt\dram_params.bin
[FWDN_ND::GetFileAndWriteCommand:1388] C:\output_aig.fwdn\boot-firmware\.\prebuilt\hsm.bin
[FWDN_ND::GetFileAndWriteCommand:1388] C:\output_aig.fwdn\boot-firmware\.\prebuilt\hsm.bin
[FWDN_ND::GetFileAndWriteCommand:1388] C:\output_aig.fwdn\boot-firmware\.\prebuilt\ca53_bl1.rom
[FWDN_ND::GetFileAndWriteCommand:1388] C:\output_aig.fwdn\boot-firmware\.\prebuilt\ca53_bl1.rom
[FWDN_ND::GetFileAndWriteCommand:1388] C:\output_aig.fwdn\boot-firmware\.\prebuilt\ca53_bl2.rom
[FWDN_ND::GetFileAndWriteCommand:1388] C:\output_aig.fwdn\boot-firmware\.\prebuilt\ca53_bl2.rom
[FWDN_ND::GetFileAndWriteCommand:1388] C:\output_aig.fwdn\boot-firmware\.\prebuilt\optee.rom
[FWDN_ND::GetFileAndWriteCommand:1388] C:\output_aig.fwdn\boot-firmware\.\prebuilt\optee.rom
[main:156] Complete FWDN, Total Time = 3307 ms
[main:162] **Notification : For more detailed FWDN Log, use the -g or --debug option.
100%[||||||||||||||||||||||||||||||] 328064/328064
Step 4. Download FAI file (system image)
[FWDNLogger::PrintCurTime:100] 25/06/12-16:12:00
[main:24] FWDN N-Dolphin v1.0.1 - 2024.9.24 16:18:11
[main:92] Start FWDN
[FWDN_ND::InfoDevice:123] ############## Device Info ##############
[PrintIP:527] ip      : 192.168.0.100
[PrintIP:527] mask    : 255.255.255.0
[PrintIP:527] gateway : 0.0.0.0
[FWDN_ND::InfoDevice:132] port : 8080
[FWDN_ND::InfoDevice:135]
mmc0_user: 7818182656 byte block_size: 512 byte
mmc0_boot0: 4194304 byte block_size: 512 byte
mmc0_boot1: 4194304 byte block_size: 512 byte
snor1: 0 byte
snor2: 0 byte
fw_version: tcc750x_v0.0.111
fw_build_id: g90e2b777
fw_build_date: 2024-09-24-17:11:42+0900

----- Firmware Information -----
VERSION    : tcc750x_v0.0.111
BUILD ID   : g90e2b777
BUILD DATE : 2024-09-24-17:11:42+0900

----- Detail of Storages -----
#### eMMC Info ####
Manufacture ID: 0x15
OEM: 0x100
Name: 0x8GTF4
User Capacity: 7.3 GiB (7818182656 Byte)
Boot Capacity: 4 MiB (4194304 Byte)
RPMB Capacity: 512 KiB (524288 Byte)
Speed Mode: HS200
#### SNOR Info ####

----- Summary of Storages -----
eMMC : O
SNOR : X
- O : Init success
- X : Init failed or not exist

----- Summary of DRAM Init -----
DRAM Init : Success
DRAM Size : TBD MB

----- PMU Status -----
PMU_USER   : 0x0
PMU_SIC_USER   : 0x80
PMU_CONFIG : 0x0
* BM : PMU_CONFIG[1:0]
-  0 : USB BOOT
-  1 : SNOR BOOT
-  2 : eMMC BOOT
-  3 : eMMC with SIC BOOT

--------------------------------

[ParseStorageSize:558] 1
[ParseStorageSize:583] 7818182656,7818182656
[FWDN_ND::LoadFwdnFW:676] TCP Ready OK
[main:121] Start Write
[FWDN_ND::GetFileAndWriteCommand:1388] output_aig.fai
[main:156] Complete FWDN, Total Time = 71367 ms
[main:162] **Notification : For more detailed FWDN Log, use the -g or --debug option.
100%[||||||||||||||||||||||||||||||] 356166304/356166304
TOPST AI-G FWDN is complete!
```
<br/><br/>

## 1.6 Linux 環境での FWDN の実行

### 1.6.1 AI-G イメージの展開
---
1.5 節でダウンロードした AI-G イメージを Linux システム上で展開してください。
<br/><br/><br/>

### 1.6.2 Telechips USB デバイス用の Udev ルール
---
次のコマンドを実行すると、Linux で FWDN をダウンロードする際に 'sudo' コマンドを使用する必要がなくなります。
```
$ echo "SUBSYSTEM==\"usb\", ATTR{idVendor}==\"140e\", MODE=\"0666\", OWNER=\"${USER}\"" | sudo tee /etc/udev/rules.d/99-topst.rules
$ sudo udevadm control --reload-rules && sudo udevadm trigger
```
<br/><br/><br/>

### 1.6.3 fwdn.sh による AI-G イメージの書き込み

Linux 環境では、次のコマンドを入力して AI-G イメージをダウンロードできます。 

```
./fwdn.sh 
```
***FWDN*** が完了したら、FWDN ポートから USB Type-C ケーブルを取り外し、電源ケーブルを取り外してください。 

<br/><br/><br/>



## 1.7 UART による AI-G ボードの接続
--- 
次の手順を実行し、UART 接続を使用してファームウェアのダウンロードが正常に完了したことを確認してください。  

1. Windows 環境でシリアル ポート ドライバ (例: CP210x Windows Driver) と PL2303_prolific ドライバをインストールしてください。
2. Tera Term や PuTTY などのターミナル エミュレータをインストールしてください。 
3. ホスト PC と AI-G ボードの UART ピンを接続してください。USB to TTL ケーブルを使用してください。 
4. 黒色のケーブルを GND ピンに接続してください。 
5. 白色のケーブル (RXD) を UART ピンの TX ピンに、緑色のケーブル (TXD) を UART ピンの RX ピンに接続してください。
6. ターミナル エミュレータ アプリケーションを実行してください。
7. PC でデバイス マネージャーを開き、UART に使用されているポート番号を確認してください。
8. デバイス マネージャーで確認したポート番号を、ターミナル エミュレータの **Serial line** フィールドに入力してください。**Speed** (bps) を 115200 に、**Flow control を None に設定してください。**
9. 電源ケーブルを接続してください。すると、AI-G はデフォルトの eMMC 起動モードで起動します。

 
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20AI-G/Software/Linux%20SDK/6.%20connetc%20host%20pc%20to%20ai-g%20with%20uart%20cable.png"></p>
<p align="center"><strong>図 1.12 ホスト PC との UART 接続</strong></p>  <br/>


以下の図 1.13 は、ログインに成功した状態を示しています。  

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20AI-G/Software/Linux%20SDK/7.%20connenct%20screen.png" width="550"></p>
<p align="center"><strong>図 1.13 接続された画面 (ID とパスワードは topst です)</strong></p> <br/>

<br/><br/>
