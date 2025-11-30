# AI-G クイックガイド
---

## 1.1 USBブートモード (FWDNモード) 
---
***FWDN***を使用して、ビルドされたイメージをAI-Gに転送できます。AI-Gは、イーサネットとUARTを使用した***FWDN***を提供します。

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20AI-G/Software/Linux%20SDK/3.%20connect%20host%20pc%20to%20topst%20ai-g.png" ></p>
<p align="center"><strong>図 1.1 FWDNのためのホストPCとAI-G間の接続</strong></p><br/>

***FWDN V8***を使用するには、次のようにAI-GボードをホストPCに接続します。

1. ホストPCにVTCドライバがインストールされていることを確認します。VTCドライバがインストールされていない場合は、第4.2.1章に示すようにインストールしてください。

2. USB Type-Cケーブル1本とイーサネットケーブル1本を用意します。

3. USBブートモードに入るには、USB Type-CケーブルをAI-GボードのUSB Type-C FWDNポートとホストPCに接続します。

4. イーサネットケーブル(RJ45)をAI-GボードのイーサネットポートとホストPCに接続します。

5. FWDNスイッチを押しながら、電源ケーブルをAI-Gボードに接続します。

<br/><br/><br/>

## 1.2 VCPドライバのインストール方法

管理者として実行して、Vendor Telechips Certification (VTC) ドライバ（[VCPドライバ](https://drive.google.com/file/d/1muQnY8kuKxDsy3p3FUiQqcG34Zjk-mnR/view?usp=sharing)にあります）をホストPCにインストールします。上記のようにFWDNモードでUSBを接続すると、Telechips VTC USBドライバが図1.2のように設定されます。

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20AI-G/Software/Linux%20SDK/4.%20VTC.png" width="550"></p>
<p align="center"><strong>図 1.2 COMポートの確認</strong></p><br/>

<br/><br/>

## 1.3 イーサネットの設定

ホストPCのネットワーク構成

- コントロールパネル → ネットワークとインターネット → ネットワーク接続 → FWDN用のイーサネットデバイスのプロパティを設定
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20AI-G/Software/Linux%20SDK/5.%20network_setting.png"></p>
<p align="center"><strong>図 1.3 FWDN用のイーサネットデバイスのプロパティ設定</strong></p><br/>
<br/><br/><br/>

## 1.4 WMICの追加
FWDNの前に、AI-GボードのFWDNポートに接続されているポートを知るために、WMICをインストールする必要があります。

1. 設定を開く: スタートメニューから設定を開きます。
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20AI-G/Software/Linux%20SDK/8.%20Open%20Settings%20from%20Start%20menu.png"></p>
<p align="center"><strong>図 1.4 スタートメニューから設定を開く</strong></p>  <br/>

2. システムを選択: システムメニューに移動します。
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20AI-G/Software/Linux%20SDK/9.%20Go%20to%20the%20System%20menu.png"></p>
<p align="center"><strong>図 1.5 システムメニューに移動</strong></p>  <br/>

3. オプション機能: オプション機能メニューをクリックします。
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20AI-G/Software/Linux%20SDK/10.%20Click%20the%20Selective%20Features%20menu.png"></p>
<p align="center"><strong>図 1.6 オプション機能メニューをクリック</strong></p>  <br/>

4. 機能の表示: **オプション機能の追加**の横にある**機能の表示**ボタンをクリックします。
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20AI-G/Software/Linux%20SDK/11.%20Click%20the%20View%20Features%20button%20next%20to%20Add%20optional%20Features.png"></p>
<p align="center"><strong>図 1.7 オプション機能の追加の横にある機能の表示ボタンをクリック</strong></p>  <br/>

5. WMIC検索: 検索ボックスに**「WMIC」**と入力します。
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20AI-G/Software/Linux%20SDK/12.%20Type%20WMIC%20in%20the%20search%20box.png"></p>
<p align="center"><strong>図 1.8 検索ボックスにWMICと入力</strong></p>  <br/>

6. インストール: WMIC項目を選択し、**「次へ」**ボタンをクリックしてインストールを完了します。
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20AI-G/Software/Linux%20SDK/13.%20Select%20the%20WMIC%20item%20and%20click%20the%20Next%20button%20to%20complete%20the%20installation.png"></p>
<p align="center"><strong>図 1.9 WMIC項目を選択し、次へボタンをクリックしてインストールを完了</strong></p>  <br/>

## 1.5 Windows環境でのFWDNの実行
1. ダウンロードページに移動します

2. AI-G Yoctoイメージをダウンロードします
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/Quick%20Guide/Download%20AI-G%20Image.png" width="550"></p>
<p align="center"><strong>図 1.10 AI-G Yoctoイメージのダウンロード</strong></p> <br/>

3. fwdn_aig.batをクリックします。「fwdn_aig.bat」は、***FWDN V8***を使用してファームウェアを自動的にダウンロードする実行ファイルです。
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/Quick%20Guide/Click%20fwdn_aig.bat.png" width="550"></p>
<p align="center"><strong>図 1.11 fwdn_aig.batをクリック</strong></p> <br/>

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

## 1.6 Linux環境でのFWDNの実行

### 1.6.1 AI-Gイメージの抽出
---
セクション1.5でダウンロードしたAI-GイメージをLinuxシステム上で抽出します。
<br/><br/><br/>

### 1.6.2 Telechips USBデバイスのUdevルール
---
以下のコマンドを実行すると、LinuxでFWDNをダウンロードする際に「sudo」コマンドを使用する必要がなくなります。
```
$ echo "SUBSYSTEM==\"usb\", ATTR{idVendor}==\"140e\", MODE=\"0666\", OWNER=\"${USER}\"" | sudo tee /etc/udev/rules.d/99-topst.rules
$ sudo udevadm control --reload-rules && sudo udevadm trigger
```
<br/><br/><br/>

### 1.6.3 fwdn.shを使用したAI-Gイメージのフラッシュ

Linux環境では、以下のコマンドを入力してAI-Gイメージをダウンロードできます。

```
./fwdn.sh 
```
***FWDN***が完了したら、FWDNポートからUSB Type-Cケーブルを取り外し、電源ケーブルを取り外します。

<br/><br/><br/>



## 1.7 UARTを使用したAI-Gボードの接続
--- 
以下の手順を実行し、UART接続を使用してファームウェアのダウンロードが正常に完了したことを確認します。

1. Windows環境にシリアルポートドライバ（例：CP210x Windowsドライバ）とPL2303_prolificドライバをインストールします。
2. Tera TermやPuTTYなどのターミナルエミュレータをインストールします。
3. ホストPCとAI-GボードのUARTピンを接続します。USB-TTLケーブルを使用してください。
4. 黒いケーブルをGNDピンに接続します。
5. 白いケーブル(RXD)をUARTピンのTXピンに接続し、緑色のケーブル(TXD)をUARTピンのRXピンに接続します。
6. ターミナルエミュレータアプリケーションを実行します。
7. PCでデバイスマネージャーを開き、UARTに使用されているポート番号を確認します。
8. デバイスマネージャーで確認したポート番号をターミナルエミュレータの**Serial line**フィールドに入力します。**Speed** (bps)を115200に設定し、**Flow control**を**None**に設定します。
9. 電源ケーブルを接続します。すると、AI-GはデフォルトのeMMCブートモードで起動します。

 
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20AI-G/Software/Linux%20SDK/6.%20connetc%20host%20pc%20to%20ai-g%20with%20uart%20cable.png"></p>
<p align="center"><strong>図 1.12 ホストPCとのUART接続</strong></p>  <br/>


以下の図1.13は、正常なログインを示しています。

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20AI-G/Software/Linux%20SDK/7.%20connenct%20screen.png" width="550"></p>
<p align="center"><strong>図 1.13 接続画面 (IDとパスワードはtopstです)</strong></p> <br/>

<br/><br/>
