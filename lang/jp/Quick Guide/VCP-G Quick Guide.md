# VCP-G クイックガイド
---

### 1.1 Windows環境でのFWDNの実行
1. ボードをダウンロードモードに設定します
   FWDNスイッチを押しながら、電源ケーブルをVCP-Gボードに接続します。
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/Set%20Board%20to%20Download%20Mode.png"></p>
    <p align="center"><strong>図 1.1 ボードをダウンロードモードに設定</strong></p>
2. ダウンロードページに移動します

3. Yocto VCP-Gイメージをダウンロードします
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/Quick%20Guide/Download%20VCP-G%20Image.png" width="550"></p>
    <p align="center"><strong>図 1.2 VCP-Gイメージのダウンロード</strong></p> <br/>

4. fwdn_vcp.batをクリックします。「fwdn_vcp.bat」は、***FWDN V8***を使用してファームウェアを自動的にダウンロードする実行ファイルです。
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/Quick%20Guide/Click%20fwdn_vcp.bat.png" width="550"></p>
    <p align="center"><strong>図 1.3 fwdn_vcp.batをクリック</strong></p> <br/>
```
[main:27] FWDN VCP v0.1.1 - 2022.8.12 11:38:19
Com port num : 10
[FWDNWindowsUART::OpenPort:34] Complete open port(\\.\COM10)
[ProtocolFW::CheckResPacket:260] Complete to receive ack for cmd(0xAAAA0013(FW_PING))
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

4. ボードのリセット
   ダウンロードプロセスが完了したら、電源ケーブルを取り外して再接続します。
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/Reset%20the%20Board.png"></p>
    <p align="center"><strong>図 1.4 ボードのリセット</strong></p>

</br></br></br>

### 1.2 Linux環境でのFWDNの実行
Linux環境では、以下のコマンドを入力してVCP-Gイメージをダウンロードできます。

```
./fwdn.sh 
```

</br></br></br>