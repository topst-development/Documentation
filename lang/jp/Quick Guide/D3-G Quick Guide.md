# D3-G クイックガイド
---

## 1.1 USBブートモードでのD3-GボードとホストPCの接続
---
ファームウェアダウンローダー (FWDN) は、ホストPCとのUSB通信を通じてD3-GにROMイメージを書き込みます。

D3-Gには1つのブートモードボタンがあり、2種類のブートモードをサポートしています。このガイドでは、FWDNモードに焦点を当てています。

- USBブートモード (FWDNモード) : ホストPC上のFWDNツールを使用してROMイメージを書き込むために使用されます

- eMMCブートモード : eMMCデバイスに保存されているROMイメージを使用してD3-Gを起動するために使用されます

**注**: USB Type-C FWDNポートは、ファームウェアダウンローダー (FWDN) に使用されます。



FWDNを使用するには、次のようにD3-GボードをホストPCに接続します。

1. ホストPCにVTCドライバがインストールされていることを確認します。VTCドライバがインストールされていない場合は、第1.2章に示すようにインストールしてください。

2. USB Type-Cケーブル1本を用意します。

3. USBブートモードに入るには、FWDNスイッチを押しながら電源ケーブルをD3-Gボードに接続します。

4. USB Type-CケーブルをD3-GボードのUSB Type-C FWDNポートとホストPCに接続します。

<p align="center">
    <img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20D3-G/Hardware/connect%20to%20d3g%20to%20host%20pc%20using%20c%20type.png">
</p>
<p align="center"><strong>図 1.1 USB C-Typeケーブルを使用したD3-GボードとホストPCの接続</strong></p>

<br/><br/>

## 1.2 VTCドライバのインストール方法 (Windows/Ubuntu)
管理者として実行して、Vendor Telechips Certification (VTC) ドライバ（[telechipsドライバ](https://drive.google.com/file/d/1muQnY8kuKxDsy3p3FUiQqcG34Zjk-mnR/view?usp=sharing)にあります）をホストPCにインストールします。上記のようにFWDNモードでUSBを接続すると、Telechips VTC USBドライバが図1.2および図1.3のように設定されます。

<p align="center">
    <img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20D3-G/Software/USB%20Connection%20in%20Windows%20Environment.png", width="700">
</p>
<p align="center"><strong>図 1.2 Windows環境でのUSB接続</strong></p>

<p align="center">
    <img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20D3-G/Software/USB%20Connection%20in%20Linux%20System.png", width="700">
</p>
<p align="center"><strong>図 1.3 Linux環境でのUSB接続</strong></p>  

**注**: VTCドライバ V5.0.0.14以降を使用してください。バージョンを確認するには、Windows環境のデバイスマネージャーを確認してください。

<br/><br/><br/>

## 1.3 Windows環境でのFWDN

### 1.3.1 D3-G Yocto
---
1. ダウンロードページに移動します

2. D3-G Yoctoイメージをダウンロードします
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/Quick%20Guide/Download%20D3-G%20v1.2.0%20Yocto%20Image.png" width="550"></p>
<p align="center"><strong>図 1.4 D3-G Yoctoイメージのダウンロード</strong></p> <br/>

3. fwdn.batをクリックします。「fwdn.bat」は、***FWDN V8***を使用してファームウェアを自動的にダウンロードする実行ファイルです。
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/Quick%20Guide/Click%20fwdn.bat.png" width="550"></p>
<p align="center"><strong>図 1.5 fwdn.batをクリック</strong></p> <br/>

```
C:\output_d3g.fwdn>fwdn.exe --fwdn boot-firmware\fwdn.json
[main:30] FWDN V8 v1.4.6 - 2021.12.13 13:42:37
[FWDN_V8::LoadFWDNRom:403] Start to load FWDN rom
[FWDN_V8::LoadMCERT:592] C:\output_d3g.fwdn\boot-firmware\mcert.bin
[FWDN_V8::LoadHSM:609] C:\output_d3g.fwdn\boot-firmware\hsm.cs.bin
[FWDN_V8::SendFWDNHeader:634] C:\output_d3g.fwdn\boot-firmware\fwdn.rom - Header
[FWDN_V8::SendFWDNBody_V8:537] C:\output_d3g.fwdn\boot-firmware\fwdn.rom - Body
[FWDN_V8::LoadFWDNRom:414] Complete to load FWDN rom
[FWDN_V8::GetFWDNRomVersion:1526] fwdn.rom version : 21.9.29
[FWDN_V8::GetFileAndWriteCommand:748] C:\output_d3g.fwdn\boot-firmware\dram_params.bin
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

C:\output_d3g.fwdn>fwdn.exe --storage emmc --low-format
[main:30] FWDN V8 v1.4.6 - 2021.12.13 13:42:37
[FWDN_V8::GetFWDNRomVersion:1526] fwdn.rom version : 21.9.29
[FWDN_V8::LowformatCommand:1352] Start low-format
[FWDN_V8::LowformatCommand:1353] low-format can take a long time
[FWDN_V8::LowformatCommand:1382] Complete low-format
[main:142] Complete FWDN
[FWDNLogger::PrintCurTime:111] 24/04/25-09:57:50

C:\output_d3g.fwdn>fwdn.exe -w boot-firmware\boot.single.json
[main:30] FWDN V8 v1.4.6 - 2021.12.13 13:42:37
[FWDN_V8::GetFWDNRomVersion:1526] fwdn.rom version : 21.9.29
[main:117] Start write command
[FWDN_V8::GetFileAndWriteCommand:748] C:\output_d3g.fwdn\boot-firmware\bconf.single.bin
[FWDN_V8::GetFileAndWriteCommand:748] C:\output_d3g.fwdn\boot-firmware\bconf.single.bin
[FWDN_V8::GetFileAndWriteCommand:748] C:\output_d3g.fwdn\boot-firmware\mcert.bin
[FWDN_V8::GetFileAndWriteCommand:748] C:\output_d3g.fwdn\boot-firmware\mcert.bin
[FWDN_V8::GetFileAndWriteCommand:748] C:\output_d3g.fwdn\boot-firmware\dram_params.bin
[FWDN_V8::GetFileAndWriteCommand:748] C:\output_d3g.fwdn\boot-firmware\dram_params.bin
[FWDN_V8::GetFileAndWriteCommand:748] C:\output_d3g.fwdn\boot-firmware\hsm.cs.bin
[FWDN_V8::GetFileAndWriteCommand:748] C:\output_d3g.fwdn\boot-firmware\hsm.cs.bin
[FWDN_V8::GetFileAndWriteCommand:748] C:\output_d3g.fwdn\boot-firmware\scfw.rom
[FWDN_V8::GetFileAndWriteCommand:748] C:\output_d3g.fwdn\boot-firmware\scfw.rom
[FWDN_V8::GetFileAndWriteCommand:748] C:\output_d3g.fwdn\boot-firmware\optee.rom
[FWDN_V8::GetFileAndWriteCommand:748] C:\output_d3g.fwdn\boot-firmware\optee.rom
[FWDN_V8::GetFileAndWriteCommand:748] C:\output_d3g.fwdn\boot-firmware\ca72_bl1.rom
[FWDN_V8::GetFileAndWriteCommand:748] C:\output_d3g.fwdn\boot-firmware\ca72_bl1.rom
[FWDN_V8::GetFileAndWriteCommand:748] C:\output_d3g.fwdn\boot-firmware\ca53_bl1.rom
[FWDN_V8::GetFileAndWriteCommand:748] C:\output_d3g.fwdn\boot-firmware\ca53_bl1.rom
[FWDN_V8::GetFileAndWriteCommand:748] C:\output_d3g.fwdn\boot-firmware\ca72_bl2.rom
[FWDN_V8::GetFileAndWriteCommand:748] C:\output_d3g.fwdn\boot-firmware\ca72_bl2.rom
[FWDN_V8::GetFileAndWriteCommand:748] C:\output_d3g.fwdn\boot-firmware\ca53_bl2.rom
[FWDN_V8::GetFileAndWriteCommand:748] C:\output_d3g.fwdn\boot-firmware\ca53_bl2.rom
[main:125] Complete write command
[main:142] Complete FWDN
[FWDNLogger::PrintCurTime:111] 24/04/25-09:57:53
100% [||||||||||||||||||||||||||||||] 859264/859264
C:\output_d3g.fwdn>fwdn.exe -w "output_d3g.fai" --storage emmc --area user
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

### 1.3.2 D3-G Ubuntuデスクトップ
---
1. ダウンロードページに移動します

2. D3-G Ubuntuデスクトップイメージをダウンロードします
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/Quick%20Guide/Download%20D3-G%20v1.2.0%20Ubuntu%20Desktop%20Image.png" width="550"></p>
<p align="center"><strong>図 1.6 D3-G Ubuntuデスクトップイメージのダウンロード</strong></p> <br/>

3. fwdn.batをクリックします。「fwdn.bat」は、***FWDN V8***を使用してファームウェアを自動的にダウンロードする実行ファイルです。
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/Quick%20Guide/Click%20fwdn_ubuntu.bat.png" width="550"></p>
<p align="center"><strong>図 1.7 fwdn.batをクリック</strong></p> <br/>

```
C:\d3g-ubuntu.fwdn>fwdn.exe --fwdn boot-firmware\fwdn.json
[main:30] FWDN V8 v1.4.11 - 2022.11.14 13:47:30
[FWDN_V8::GetFWDNRomVersion:1588] fwdn.rom version : 23.5.22
[main:156] Complete FWDN
[FWDNLogger::PrintCurTime:112] 25/06/25-10:32:29

C:\d3g-ubuntu.fwdn>fwdn.exe --storage emmc --low-format
[main:30] FWDN V8 v1.4.11 - 2022.11.14 13:47:30
[FWDN_V8::GetFWDNRomVersion:1588] fwdn.rom version : 23.5.22
[FWDN_V8::LowformatCommand:1370] Start low-format
[FWDN_V8::LowformatCommand:1371] low-format can take a long time
[FWDN_V8::LowformatCommand:1400] Complete low-format
[main:156] Complete FWDN
[FWDNLogger::PrintCurTime:112] 25/06/25-10:32:29

C:\d3g-ubuntu.fwdn>fwdn.exe -w boot-firmware\boot.single.json
[main:30] FWDN V8 v1.4.11 - 2022.11.14 13:47:30
[FWDN_V8::GetFWDNRomVersion:1588] fwdn.rom version : 23.5.22
[main:131] Start write command
[FWDN_V8::GetFileAndWriteCommand:762] C:\d3g-ubuntu.fwdn\boot-firmware\.\prebuilt\bconf.single.bin
[FWDN_V8::GetFileAndWriteCommand:762] C:\d3g-ubuntu.fwdn\boot-firmware\.\prebuilt\bconf.single.bin
[FWDN_V8::GetFileAndWriteCommand:762] C:\d3g-ubuntu.fwdn\boot-firmware\.\prebuilt\mcert.bin
[FWDN_V8::GetFileAndWriteCommand:762] C:\d3g-ubuntu.fwdn\boot-firmware\.\prebuilt\mcert.bin
[FWDN_V8::GetFileAndWriteCommand:762] C:\d3g-ubuntu.fwdn\boot-firmware\.\prebuilt\dram_params.bin
[FWDN_V8::GetFileAndWriteCommand:762] C:\d3g-ubuntu.fwdn\boot-firmware\.\prebuilt\dram_params.bin
[FWDN_V8::GetFileAndWriteCommand:762] C:\d3g-ubuntu.fwdn\boot-firmware\.\prebuilt\hsm.cs.bin
[FWDN_V8::GetFileAndWriteCommand:762] C:\d3g-ubuntu.fwdn\boot-firmware\.\prebuilt\scfw.rom
[FWDN_V8::GetFileAndWriteCommand:762] C:\d3g-ubuntu.fwdn\boot-firmware\.\prebuilt\scfw.rom
[FWDN_V8::GetFileAndWriteCommand:762] C:\d3g-ubuntu.fwdn\boot-firmware\.\prebuilt\optee.rom
[FWDN_V8::GetFileAndWriteCommand:762] C:\d3g-ubuntu.fwdn\boot-firmware\.\prebuilt\optee.rom
[FWDN_V8::GetFileAndWriteCommand:762] C:\d3g-ubuntu.fwdn\boot-firmware\.\prebuilt\subcore_optee.rom
[FWDN_V8::GetFileAndWriteCommand:762] C:\d3g-ubuntu.fwdn\boot-firmware\.\prebuilt\subcore_optee.rom
[FWDN_V8::GetFileAndWriteCommand:762] C:\d3g-ubuntu.fwdn\boot-firmware\.\prebuilt\ca72_bl1.rom
[FWDN_V8::GetFileAndWriteCommand:762] C:\d3g-ubuntu.fwdn\boot-firmware\.\prebuilt\ca72_bl1.rom
[FWDN_V8::GetFileAndWriteCommand:762] C:\d3g-ubuntu.fwdn\boot-firmware\.\prebuilt\ca53_bl1.rom
[FWDN_V8::GetFileAndWriteCommand:762] C:\d3g-ubuntu.fwdn\boot-firmware\.\prebuilt\ca53_bl1.rom
[FWDN_V8::GetFileAndWriteCommand:762] C:\d3g-ubuntu.fwdn\boot-firmware\.\prebuilt\ca72_bl2.rom
[FWDN_V8::GetFileAndWriteCommand:762] C:\d3g-ubuntu.fwdn\boot-firmware\.\prebuilt\ca72_bl2.rom
[FWDN_V8::GetFileAndWriteCommand:762] C:\d3g-ubuntu.fwdn\boot-firmware\.\prebuilt\ca53_bl2.rom
[FWDN_V8::GetFileAndWriteCommand:762] C:\d3g-ubuntu.fwdn\boot-firmware\.\prebuilt\ca53_bl2.rom
[main:139] Complete write command
[main:156] Complete FWDN
[FWDNLogger::PrintCurTime:112] 25/06/25-10:32:29
100[||||||||||||||||||||||||||||||] 864768/864768
C:\d3g-ubuntu.fwdn>fwdn.exe -w "d3g.fai" --storage emmc --area user
[main:30] FWDN V8 v1.4.11 - 2022.11.14 13:47:30
[FWDN_V8::GetFWDNRomVersion:1588] fwdn.rom version : 23.5.22
[main:131] Start write command
[FWDN_V8::GetFileAndWriteCommand:762] d3g.fai
100% [||||||||||||||||||||||||||||||] 4291763824/4291763824
** When writing FAI files without low-format, there may be garbage values in partition where data is not written.
```

### 1.3.3 D3-G Ubuntuヘッドレス
---
1. ダウンロードページに移動します

2. D3-G Ubuntuヘッドレスイメージをダウンロードします
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/Quick%20Guide/Download%20D3-G%20Ubuntu%20Headless%20Image.png" width="550"></p>
<p align="center"><strong>図 1.8 D3-G Ubuntuヘッドレスイメージのダウンロード</strong></p> <br/>

3. fwdn.batをクリックします。「fwdn.bat」は、***FWDN V8***を使用してファームウェアを自動的にダウンロードする実行ファイルです。
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/Quick%20Guide/Click%20fwdn_ubuntu_headless.bat.png" width="550"></p>
<p align="center"><strong>図 1.9 fwdn.batをクリック</strong></p> <br/>

```
C:\d3g-ubuntu-headless>fwdn.exe --fwdn boot-firmware\fwdn.json
[main:30] FWDN V8 v1.4.11 - 2022.11.14 13:47:30
[FWDN_V8::GetFWDNRomVersion:1588] fwdn.rom version : 23.5.22
[main:156] Complete FWDN
[FWDNLogger::PrintCurTime:112] 25/06/25-10:28:35

C:\d3g-ubuntu-headless>fwdn.exe --storage emmc --low-format
[main:30] FWDN V8 v1.4.11 - 2022.11.14 13:47:30
[FWDN_V8::GetFWDNRomVersion:1588] fwdn.rom version : 23.5.22
[FWDN_V8::LowformatCommand:1370] Start low-format
[FWDN_V8::LowformatCommand:1371] low-format can take a long time
[FWDN_V8::LowformatCommand:1400] Complete low-format
[main:156] Complete FWDN
[FWDNLogger::PrintCurTime:112] 25/06/25-10:28:36

C:\d3g-ubuntu-headless>fwdn.exe -w boot-firmware\boot.single.json
[main:30] FWDN V8 v1.4.11 - 2022.11.14 13:47:30
[FWDN_V8::GetFWDNRomVersion:1588] fwdn.rom version : 23.5.22
[main:131] Start write command
[FWDN_V8::GetFileAndWriteCommand:762] C:\d3g-ubuntu-headless\boot-firmware\.\prebuilt\bconf.single.bin
[FWDN_V8::GetFileAndWriteCommand:762] C:\d3g-ubuntu-headless\boot-firmware\.\prebuilt\bconf.single.bin
[FWDN_V8::GetFileAndWriteCommand:762] C:\d3g-ubuntu-headless\boot-firmware\.\prebuilt\mcert.bin
[FWDN_V8::GetFileAndWriteCommand:762] C:\d3g-ubuntu-headless\boot-firmware\.\prebuilt\mcert.bin
[FWDN_V8::GetFileAndWriteCommand:762] C:\d3g-ubuntu-headless\boot-firmware\.\prebuilt\dram_params.bin
[FWDN_V8::GetFileAndWriteCommand:762] C:\d3g-ubuntu-headless\boot-firmware\.\prebuilt\dram_params.bin
[FWDN_V8::GetFileAndWriteCommand:762] C:\d3g-ubuntu-headless\boot-firmware\.\prebuilt\hsm.cs.bin
[FWDN_V8::GetFileAndWriteCommand:762] C:\d3g-ubuntu-headless\boot-firmware\.\prebuilt\hsm.cs.bin
[FWDN_V8::GetFileAndWriteCommand:762] C:\d3g-ubuntu-headless\boot-firmware\.\prebuilt\scfw.rom
[FWDN_V8::GetFileAndWriteCommand:762] C:\d3g-ubuntu-headless\boot-firmware\.\prebuilt\scfw.rom
[FWDN_V8::GetFileAndWriteCommand:762] C:\d3g-ubuntu-headless\boot-firmware\.\prebuilt\optee.rom
[FWDN_V8::GetFileAndWriteCommand:762] C:\d3g-ubuntu-headless\boot-firmware\.\prebuilt\optee.rom
[FWDN_V8::GetFileAndWriteCommand:762] C:\d3g-ubuntu-headless\boot-firmware\.\prebuilt\subcore_optee.rom
[FWDN_V8::GetFileAndWriteCommand:762] C:\d3g-ubuntu-headless\boot-firmware\.\prebuilt\subcore_optee.rom
[FWDN_V8::GetFileAndWriteCommand:762] C:\d3g-ubuntu-headless\boot-firmware\.\prebuilt\ca72_bl1.rom
[FWDN_V8::GetFileAndWriteCommand:762] C:\d3g-ubuntu-headless\boot-firmware\.\prebuilt\ca72_bl1.rom
[FWDN_V8::GetFileAndWriteCommand:762] C:\d3g-ubuntu-headless\boot-firmware\.\prebuilt\ca53_bl1.rom
[FWDN_V8::GetFileAndWriteCommand:762] C:\d3g-ubuntu-headless\boot-firmware\.\prebuilt\ca53_bl1.rom
[FWDN_V8::GetFileAndWriteCommand:762] C:\d3g-ubuntu-headless\boot-firmware\.\prebuilt\ca72_bl2.rom
[FWDN_V8::GetFileAndWriteCommand:762] C:\d3g-ubuntu-headless\boot-firmware\.\prebuilt\ca72_bl2.rom
[FWDN_V8::GetFileAndWriteCommand:762] C:\d3g-ubuntu-headless\boot-firmware\.\prebuilt\ca53_bl2.rom
[FWDN_V8::GetFileAndWriteCommand:762] C:\d3g-ubuntu-headless\boot-firmware\.\prebuilt\ca53_bl2.rom
[main:139] Complete write command
[main:156] Complete FWDN
[FWDNLogger::PrintCurTime:112] 25/06/25-10:28:36
100[||||||||||||||||||||||||||||||] 864768/864768
C:\d3g-ubuntu-headless>fwdn.exe -w "d3g.fai" --storage emmc --area user
[main:30] FWDN V8 v1.4.11 - 2022.11.14 13:47:30
[FWDN_V8::GetFWDNRomVersion:1588] fwdn.rom version : 23.5.22
[main:131] Start write command
[FWDN_V8::GetFileAndWriteCommand:762] d3g.fai
100% [||||||||||||||||||||||||||||||] 2594119280/2594119280
** When writing FAI files without low-format, there may be garbage values in partition where data is not written.
```

<br/><br/><br/>

## 1.4 Linux環境でのFWDN

### 1.4.1 D3-Gイメージの抽出
---
セクション1.3でダウンロードしたD3-GイメージをLinuxシステム上で抽出します。

<br/><br/><br/>

### 1.4.2 Telechips USBデバイスのUdevルール
---
以下のコマンドを実行すると、LinuxでFWDNをダウンロードする際に「sudo」コマンドを使用する必要がなくなります。
```
$ echo "SUBSYSTEM==\"usb\", ATTR{idVendor}==\"140e\", MODE=\"0666\", OWNER=\"${USER}\"" | sudo tee /etc/udev/rules.d/99-topst.rules
$ sudo udevadm control --reload-rules && sudo udevadm trigger
```
<br/><br/><br/>

### 1.4.3 fwdn.shを使用したD3-Gイメージのフラッシュ
---
LinuxでD3-Gイメージをダウンロードするには、次のコマンドを実行します: "./fwdn.sh"。

```
$ ./fwdn.sh
```

これでD3-Gを起動する準備が整いました。デバイスとの通信を開始するには、第1.5章を参照してください。


<br/><br/><br/><br/>

## 1.5 D3-GボードとホストPCの接続
---
この章では、ファームウェアのダウンロードとシリアル通信のために、UARTを介してホストPCをD3-Gボードに接続する方法について説明します。

<br/><br/><br/>

## 1.6 UARTを使用したD3-Gボードの接続 
---
以下の手順に従い、UART接続を使用してファームウェアのダウンロードが正常に完了したことを確認します。

1. Windows環境にシリアルポートドライバ（例：CP210x Windowsドライバ）とPL2303_prolificドライバをインストールします。
2. Tera TermやPuTTYなどのターミナルエミュレータをインストールします。
3. ホストPCとD3-GボードのUARTピンを接続します。USB-TTLケーブルを使用してください。
4. 黒いケーブルをGNDピンに接続します。
5. 白いケーブル(RXD)をUARTピンのTXピンに接続し、緑色のケーブル(TXD)をUARTピンのRXピンに接続します。
6. ターミナルエミュレータアプリケーションを実行します。
7. PCでデバイスマネージャーを開き、UARTに使用されているポート番号を確認します。
8. デバイスマネージャーで確認したポート番号をターミナルエミュレータのSerial lineフィールドに入力します。**Speed** (bps)を115200に設定し、**Flow control**を**None**に設定します。
9. 電源ケーブルを接続します。すると、D3-GはデフォルトのeMMCブートモードで起動します。


 
<p align="center">
    <img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20D3-G/Software/USB%20to%20TTL%20Connection.png", width="700">
</p>
<p align="center"><strong>図 1.6 ホストPCとのUART接続</strong></p><br/>  
