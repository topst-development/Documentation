# 1. はじめに
---
本書では、D3-Gの使用例を紹介します。
本書には以下の情報が含まれています。
- 入力デバイス
  - キーボード
  - マウス
- ビデオ出力
- カメラ接続
  - MIPI CSI
  - USBウェブカメラ
- ストレージ接続
  - SDカード
  - SATA HDD
  - NVMe M.2 SSD
  - USBストレージ
- イーサネット接続
- 40ピンGPIOヘッダー
  - 利用可能なセンサーとデバイス
 
<br/><br/><br/><br/>
 
 
# 2. 入力デバイス
---
D3-Gは、入力デバイスを接続するための2つのUSBポートをサポートしています。
USB 2.0 Type-Aポート1つとUSB 3.0 Type-Aポート1つが含まれており、マウスやキーボードを接続してD3-Gを直接制御できます。
 
**注**: D3-GのUSB Type-Cポートはファームウェアのダウンロード用に予約されており、入力デバイスの接続には使用できません。
 
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20D3-G/Software/input%20device.png" width="500"></p>
<p align="center"><strong>図 2.1 入力デバイスのD3-Gボードへの接続 </strong></p><br/><br/><br/><br/>
 
 
# 3. ビデオ出力
---
D3-Gは、DisplayPort (DP) 出力を介してのみFHDモニターをサポートします。
また、デイジーチェーン設定を使用したマルチディスプレイ出力もサポートしており、最大2台のFHDモニターと1台のHDモニターを同時に接続できます。
 
**注**: HDMIを使用するには、別途アクティブコンバーターアダプターが必要です。
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20D3-G/Software/monitor.png" width="500"></p>
<p align="center"><strong>図 3.1 モニターのD3-Gボードへの接続 </strong></p>
 
<br/><br/><br/><br/>
 
# 4. カメラ接続
---
D3-Gはカメラ機能をサポートしており、さまざまなアプリケーションに柔軟に対応します。
プロジェクトの要件に応じて、MIPI CSIカメラまたはUSBウェブカメラのいずれかを接続できます。
 
<br/><br/><br/>
 
## 4.1 USBウェブカメラ
---
D3-GはUSBウェブカメラをサポートしており、最大フルHD (FHD) の解像度に対応しています。
次の手順に従ってウェブカメラをテストできます。
 
 
#### ステップ 1. USBカメラをボードのUSBポートに接続します。
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20D3-G/Software/webcam.png" width="400"></p>
<p align="center"><strong>図 4.1 ウェブカメラのD3-Gボードへの接続</strong></p><br/>
 
#### ステップ 2. 入力デバイス (マウスとキーボード) とモニターをD3-Gに接続します。
   
#### ステップ 3. D3-Gを起動します。
 
#### ステップ 4. 利用可能な /dev/video デバイスを確認します。
```
$ ls /dev/video*
```
 
#### ステップ 5. OpenCV (または vutils) を使用してビデオ出力を確認します。
```
$ touch webcam.py
$ chmod a+x webcam.py
```
```
# vimまたはnanoエディタを使用してスクリプトファイルを編集できます
# これはOpenCVを使用したPythonカメラアプリケーションです
import cv2
 
cap = cv2.VideoCapture(0)
 
if not cap.isOpened():
    print("\\@@ Camera open failed!")
    exit()
 
print("Press 'q' to exit the camera window.")
 
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
 
while True:
    ret, frame = cap.read()
    if not ret:
        print("\\@@ Failed to read frame")
        break
 
    cv2.imshow("Camera Feed", frame)
 
    # 'q' キーが押されたら終了
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
 
cap.release()
cv2.destroyAllWindows()
```
```
# スクリプトを実行します
$ python3 webcam.py
```
 
<br/><br/><br/>
 
## 4.2 MIPI CSI
---
CSIはCamera Serial Interfaceの略で、カメラモジュールをホストプロセッサに接続するためにMIPI Allianceによって定義された標準インターフェースです。
これにより、カメラからプロセッサへの画像データの高速かつ低電力な転送が可能になります。
 
D3-Gは2つのMIPI CSIチャネル (ch0およびch1) を備えており、フラットフレキシブルケーブル (FFC) 接続をサポートするカメラモジュールを取り付けることができます。
現在、D3-GはArduCam (5 MP) およびRaspberry Pi v1 Camera (5 MP) モジュールのみをサポートしています。
 
**注**: 現在、D3-GはCSIチャネル0とCSIチャネル1の同時使用をサポートしていません。
 
<br/><br/>
 
### 4.2.1 ArduCam
ArduCamは、組み込みシステムおよびIoTアプリケーション向けに設計された汎用性の高いカメラモジュールです。MIPI CSIを含むさまざまなイメージセンサーとインターフェースをサポートしており、D3-Gのような開発ボードとの統合に適しています。
D3-Gでサポートされている5 MP ArduCamモジュールは、十分な画質を提供し、基本的なコンピュータビジョンタスク、ストリーミング、およびカメラベースのAIアプリケーションによく使用されます。FFCケーブルとの互換性があるため、D3-GボードのCSIインターフェースに簡単に接続できます。
 
ArduCamモジュールの仕様は次のとおりです。
 
| 仕様                     | 説明                                 |
| ------------------------ | ------------------------------------------- |
| センサー                   | OV5647 (5メガピクセル)                        |
| 解像度               | 2592 × 1944 (フル5 MP)                      |
| サポートされている出力形式 | RAW, YUV, JPEG (センサー依存)           |
| インターフェース                | MIPI CSI-2                                  |
| フレームレート               | 1080pで最大30fps、720pで60fps         |
| レンズマウント               | 固定焦点レンズ (標準)                 |
| 視野角 (FOV)      | 約54° – 70° (モデルにより異なる)         |
| 接続タイプ          | フラットフレキシブルケーブル (FFC)                   |
| 動作電圧        | 3.3V (標準)                              |
| フォームファクタ              | コンパクトPCB、約25 mm x 24 mm                   |
| 互換性            | Raspberry PiおよびD3-G (MIPI CSI-2ポート経由)    |
| 追加機能      | 低消費電力、プラグアンドプレイモジュール |
 
 
次の手順に従ってArduCamをテストできます。
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20D3-G/Software/arducam.png" width="400"></p>
<p align="center"><strong>図 4.2 ArduCam </strong></p><br/>
 
#### ステップ 1. 図4.3に示すように、ArduCamをD3-GボードのMIPI CSI 0に接続します。
 
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20D3-G/Software/rasp%20v1%20cam%20to%20d3g.png" width="500"></p>
<p align="center"><strong>図 4.3 ArduCamのD3-Gボードへの接続</strong></p> <br/>
 
#### ステップ 2. ArduCamを接続した後、D3-Gボードで次のGStreamerコマンドを使用してビデオストリームを確認できます。
```
$ gst-launch-1.0 v4l2src device=/dev/video0 io-mode=2 ! video/x-raw,format=NV12,width=1920,height=1280,framerate=30/1 ! videoconvert ! waylandsink fullscreen=true
```
 
このコマンドは、CSI接続されたArduCamからビデオをキャプチャし、表示用に変換して、Waylandディスプレイサーバーを使用して全画面モードでレンダリングします。
コマンドを実行する前に、カメラモジュールがしっかりと接続されていることを確認してください。ビデオが表示されない場合は、ケーブル接続を確認し、/dev/video0がシステムによって正しく認識されていることを確認してください。
 
<br/><br/>
 
### 4.2.2 Raspberry Pi v1 Camera
Raspberry Pi v1 Camera Moduleは、Raspberry Pi Foundationによって開発されたコンパクトな5 MPカメラです。OmniVision OV5647イメージセンサーに基づいており、フラットフレキシブルケーブル (FFC) を使用してMIPI CSI-2インターフェースを介してホストボードに接続します。
 
もともとRaspberry Piシリーズ向けに設計されたこのモジュールは、D3-Gとも互換性があり、画像キャプチャ、ビデオ録画、コンピュータビジョンプロジェクトなどの基本的なカメラアプリケーションにとって信頼できる選択肢となります。
 
Raspberry Pi v1カメラモジュールの仕様は次のとおりです。
 
| 仕様                | 説明                              |
| ------------------- | ---------------------------------------- |
| センサー              | OmniVision OV5647                        |
| 解像度          | 2592 × 1944 (5 MP)                        |
| 出力形式      | RAW, YUV, JPEG                           |
| インターフェース           | MIPI CSI-2                               |
| フレームレート          | 1080p30, 720p60, VGA90                   |
| レンズ                | 固定焦点                              |
| 視野角 (FOV) | 最大54°                                     |
| ケーブルタイプ          | FFC (15ピン)                             |
| ボード寸法    | 25 mm x 24 mm                              |
| 互換性       | Raspberry PiおよびD3-G (MIPI CSI-2ポート経由) |
 
次の手順に従ってRaspberry Pi v1カメラをテストできます。
 
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20D3-G/Software/rasp%20v1%20cam.jpg" width="400"></p>
<p align="center"><strong>図 4.4. Raspberry Pi v1 Camera </strong></p><br/>
 
#### ステップ 1. 図4.5に示すように、Raspberry Pi v1カメラをD3-GボードのMIPI CSI 1に接続します。
 
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20D3-G/Software/rasp%20v1%20cam%20to%20d3g.png" width="500"></p>
<p align="center"><strong>図 4.5 Raspberry Pi v1 CameraのD3-Gボードへの接続</strong></p> <br/>
 
#### ステップ 2. Raspberry Piカメラを接続した後、D3-Gで次のGStreamerコマンドを使用してビデオストリームを確認できます。
```
$ gst-launch-1.0 v4l2src device=/dev/video0 io-mode=2 ! video/x-raw,format=NV12,width=1920,height=1280,framerate=30/1 ! videoconvert ! waylandsink fullscreen=true
```
 
このコマンドは、CSI接続されたRaspberry Piカメラからビデオをキャプチャし、表示用に変換して、Waylandディスプレイサーバーを使用して全画面モードでレンダリングします。
コマンドを実行する前に、カメラモジュールがしっかりと接続されていることを確認してください。ビデオが表示されない場合は、ケーブル接続を確認し、/dev/video0がシステムによって正しく認識されていることを確認してください。
 
<br/><br/><br/><br/>
 
# 5. ストレージ接続
---
この章では、D3-Gをさまざまなストレージデバイスに接続する方法について説明します。サポートされているストレージオプションには、USBドライブ、SDカード、PCIe経由の外部ストレージが含まれます。
 
<br/><br/><br/>
 
## 5.1 USBドライブ
---
D3-Gは、USB 2.0およびUSB 3.0 Type-Aポートを介してUSBストレージデバイスをサポートします。
USBドライブを接続するには:
 
### ステップ 1. USBドライブをD3-Gの利用可能なUSB Type-Aポートのいずれかに差し込みます。
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20D3-G/Software/usb%20storage%20connection%20with%20d3g.png" width="500"></p>
<p align="center"><strong>図 5.1 USBストレージのD3-Gボードへの接続</strong></p> <br/>
 
### ステップ 2. 接続後、デバイスはシステムの状態に応じて、通常 /dev/sda1、/dev/sdb1 などとして認識されます。
 
<br/>
 
### ステップ 3. 次のコマンドを使用して、USBドライブを手動でマウントできます。
   ```
   $ sudo mount /dev/sda1 /mnt
   ```
 
<br/><br/><br/>
 
## 5.2 SDカード
---
D3-Gには、標準のSDHC/SDXCカードをサポートするmicroSDカードスロットが含まれています。
D3-GでSDカードを使用するには:
 
<br/>
 
### ステップ 1. microSDカードをD3-GボードのSDカードスロットに挿入します。
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20D3-G/Software/sd%20card%20connect%20with%20d3g.png" width="500"></p>
<p align="center"><strong>図 5.2 SDカードのD3-Gボードへの接続</strong></p> <br/>
 
### ステップ 2. 挿入後、システムは通常、SDカードを /dev/mmcblk1p1 または同様のデバイスノードとして認識します。
  ```
  $ ls /dev/mmcblk*
  ```
<br/>
 
### ステップ 3. SDカードを手動でマウントするには、次のコマンドを使用します。
```
$ sudo mount /dev/mmcblk1p1 /mnt 
```
### ステップ 4. マウント後、/mnt ディレクトリの下にあるSDカードの内容にアクセスできます。
 
<br/><br/><br/>
 
## 5.3 SATA HDD
---
 
D3-Gは、互換性のあるSATAコントローラーを使用してPCIeスロットを介してHDDやSSDなどのSATAストレージデバイスの使用をサポートします。
 
<br/>
 
#### ステップ 1. PCIe to SATAモジュールの接続
 
PCIe経由でD3-GでSATA HDDを使用するには、まずPCIe-to-SATAアダプターモジュールをD3-GのPCIeスロットに接続する必要があります。
 
次に、HDDをSATAモジュールに接続し、HDDが外部12V電源から電力を供給されていることを確認します。
 
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20D3-G/Software/sata.png" width="500"></p>
<p align="center"><strong>図 5.3 D3-GボードPCIe to SATAモジュールの接続 </strong></p><br/>
 
#### ステップ 2. D3-Gの起動
D3-Gを起動した後、ブートログを観察して、PCIeデバイスがシステムによって認識されていることを確認します。
PCIeリンクが正常に確立されたことを示す **telechips-pcie: Link up** などのメッセージを探します。
 
```
Starting kernel ...
 
[    1.191696] telechips-pcie 11000000.pcie: invalid resource
[    1.230423] telechips-pcie 11000000.pcie: Link up
[    1.693516] debugfs: Directory '16680000.udma' with parent 'dmaengine' already present!
[    1.702282] debugfs: Directory '16681000.udma' with parent 'dmaengine' already present!
[    1.711022] debugfs: Directory '16682000.udma' with parent 'dmaengine' already present!
[    1.719799] debugfs: Directory '16683000.udma' with parent 'dmaengine' already present!
[    1.728562] debugfs: Directory '16684000.udma' with parent 'dmaengine' already present!
[    1.737308] debugfs: Directory '16685000.udma' with parent 'dmaengine' already present!
[    1.746084] debugfs: Directory '16686000.udma' with parent 'dmaengine' already present!
[    1.754824] debugfs: Directory '16687000.udma' with parent 'dmaengine' already present!
 
...
Ubuntu 22.04.5 LTS TOPST ttyAMA0
 
TOPST login: 
```
 
<br/>
 
#### ステップ 3. SATA HDDの認識を確認
```
root@TOPST:~# lspci
00:00.0 PCI bridge: Synopsys, Inc. Device 8040 (rev 01)
01:00.0 SATA controller: ASMedia Technology Inc. Device 1064 (rev 02)
```
**lspci** コマンドが利用できない場合は、次のコマンドを使用してpciutilsをインストールしてください。

```
$ sudo apt-get install pciutils
```

<br/>

#### ステップ 4. SATA HDDのマウント
```
$ fdisk /dev/sda
Welcome to fdisk (util-linux 2.37.4).
Changes will remain in memory only, until you decide to write them.
Be careful before using the write command.

Command (m for help): 
```

fdiskプロンプト内で次のキーを順番に入力します。

- o — 新しい空のDOSパーティションテーブルを作成します (オプション、既存のテーブルをクリアします)

- n — 新しいパーティションを追加します

- p — プライマリパーティションを選択します

- 1 — パーティション番号を1に設定します

- Enterキーを押す — デフォルトの最初のセクタを受け入れます

- Enterキーを押す — デフォルトの最後のセクタを受け入れます (ディスク全体を使用)

- w — パーティションテーブルを書き込んで終了します

```
$ mkfs.ext4 /dev/sda1

$ mkdir -p /mnt/sata

$ mount /dev/sda1 /mnt/sata
```

<br/>

#### ステップ 5. 実行結果
この出力は、SATA SSDパーティション (/dev/sdb1) がext4ファイルシステムで正常にフォーマットされ、/mnt/sataにマウントされたことを確認します。
**df -h** コマンドは、デバイスが認識され、システムで使用可能になったことを示しています。

```
$ df -h

Filesystem      Size  Used Avail Use% Mounted on
/dev/mmcblk0p4   29G  4.0G   25G  14% /
tmpfs           100M     0  100M   0% /dev/shm
tmpfs           592M  976K  591M   1% /run
tmpfs           5.0M  4.0K  5.0M   1% /run/lock
tmpfs           1.5G  4.0K  1.5G   1% /tmp
tmpfs           1.5G     0  1.5G   0% /var/volatile
tmpfs           296M  4.0K  296M   1% /run/user/0
/dev/sdb1       234G   28K  222G   1% /mnt/sata
```

<br/><br/><br/>

## 5.4 NVMe M.2 SSD
---
D3-Gは、PCIeスロットを介したNVMe M.2 SSDの直接接続をサポートしています。
<br/>

#### ステップ 1. SSDの接続
- NVMe SSD (M.2 PCIe): NVMe M.2 SSDをD3-GのPCIeスロットに挿入します。

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20D3-G/Software/M.2%20SSD%20connection.png" width="600"></p>
<p align="center"><strong>図 5.4 NVMe M.2 SSDのD3-Gボードへの接続</strong></p><br/>

#### ステップ 2. D3-Gの起動
**reboot** コマンドを実行した後、ブートログを観察して、PCIeデバイスがシステムによって認識されていることを確認します。
PCIeリンクが正常に確立されたことを示す **telechips-pcie: Link up** などのメッセージを探します。

```
$ reboot
...
Starting kernel ...

[    1.191696] telechips-pcie 11000000.pcie: invalid resource
[    1.230423] telechips-pcie 11000000.pcie: Link up
[    1.693516] debugfs: Directory '16680000.udma' with parent 'dmaengine' already present!
[    1.702282] debugfs: Directory '16681000.udma' with parent 'dmaengine' already present!
[    1.711022] debugfs: Directory '16682000.udma' with parent 'dmaengine' already present!
[    1.719799] debugfs: Directory '16683000.udma' with parent 'dmaengine' already present!
[    1.728562] debugfs: Directory '16684000.udma' with parent 'dmaengine' already present!
[    1.737308] debugfs: Directory '16685000.udma' with parent 'dmaengine' already present!
[    1.746084] debugfs: Directory '16686000.udma' with parent 'dmaengine' already present!
[    1.754824] debugfs: Directory '16687000.udma' with parent 'dmaengine' already present!
 
...
Ubuntu 22.04.5 LTS TOPST ttyAMA0

TOPST login: 
```

<br/>

#### ステップ 3. SSDの認識を確認
```
root@TOPST:~# lspci
00:00.0 PCI bridge: Synopsys, Inc. Device 8040 (rev 01)
01:00.0 Non-Volatile memory controller: Solid State Storage Technology Corporation Device 1007 (rev 03)
```
**lspci** コマンドが利用できない場合は、次のコマンドを使用してpciutilsをインストールしてください。

```
$ sudo apt-get install pciutils
```

<br/>

#### ステップ 4. SSDのマウント
```
$ fdisk /dev/nvme0n1
Welcome to fdisk (util-linux 2.37.4).
Changes will remain in memory only, until you decide to write them.
Be careful before using the write command.

Command (m for help): 
```

fdiskプロンプト内で次のキーを順番に入力します。

- o — 新しい空のDOSパーティションテーブルを作成します (オプション、既存のテーブルをクリアします)

- n — 新しいパーティションを追加します

- p — プライマリパーティションを選択します

- 1 — パーティション番号を1に設定します

- Enterキーを押す — デフォルトの最初のセクタを受け入れます

- Enterキーを押す — デフォルトの最後のセクタを受け入れます (ディスク全体を使用)

- w — パーティションテーブルを書き込んで終了します

```
$ mkfs.ext4 /dev/nvme0n1p1

$ mkdir -p /mnt/nvme

$ mount /dev/nvme0n1p1 /mnt/nvme
```

<br/>

#### ステップ 5. 実行結果
この出力は、NVMe SSDデバイス (/dev/nvme0n1p1) がシステムによって正常に検出され、/mnt/nvmeにマウントされたことを確認します。
```
$ df -h

Filesystem      Size  Used Avail Use% Mounted on
/dev/mmcblk0p4   29G  4.0G   25G  14% /
tmpfs           100M     0  100M   0% /dev/shm
tmpfs           592M  976K  591M   1% /run
tmpfs           5.0M  4.0K  5.0M   1% /run/lock
tmpfs           1.5G  4.0K  1.5G   1% /tmp
tmpfs           1.5G     0  1.5G   0% /var/volatile
tmpfs           296M  4.0K  296M   1% /run/user/0
/dev/nvme0n1p1  234G   28K  222G   1% /mnt/nvme
```
<br/><br/><br/><br/>


# 6. イーサネット接続
---
D3-Gは、オンボードのJ2Cイーサネットポートを介したイーサネット接続をサポートしています。これにより、D3-Gは標準のTCP/IPプロトコルを使用してローカルネットワークまたはインターネットと通信できます。イーサネットは、リモートアクセス、データストリーミング、またはソフトウェアアップデートを必要とするアプリケーションの展開に一般的に使用されます。

<br/><br/><br/>

## 6.1 ルーター経由のネットワーク接続
---
この方法は、標準のルーターを使用してD3-Gをローカルネットワークに接続します。D3-Gは、DHCPを介してIPアドレスを自動的に取得するか、静的IPアドレスで構成できます。

<br/><br/>

### 6.1.1 ネットワーク構成ファイルの作成

1. DHCPによる動的IP
ネットワークがDHCPサーバー (ルーターやICS対応のWindows PCなど) を提供している場合、ファイルの編集は必要ありません。イーサネットケーブルが接続されるとすぐに、システムはIPアドレスを自動的に取得します。

ケーブルを差し込むだけで、すぐにネットワークの使用を開始できます。6.1.3 ネットワーク接続の確認に進んでください。

2. 静的IP構成
静的IPアドレスを割り当てる場合 (たとえば、PC直接接続を使用する場合やDHCPサーバーが利用できない場合)、次の内容で同じファイルを編集します。
```
$ vi /etc/systemd/network/20-wired.network

[Match]
Name=eth0

[Network]
Address=192.168.137.2/24
Gateway=192.168.137.1
DNS=8.8.8.8
```

これにより、IPアドレスが192.168.137.2に設定され、ゲートウェイとして192.168.137.1 (Windows ICSで一般的) が使用され、Google DNSが構成されます。

<br/><br/>

### 6.1.2 ネットワークサービスの再起動
systemd-networkdサービスを再起動して、新しいネットワーク構成を適用します。

```
sudo systemctl restart systemd-networkd
```

<br/><br/>

### 6.1.3 ネットワーク接続の確認
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20D3-G/Software/router%20connection.png"width="500"></p>
<p align="center"><strong>図 6.1 ルーター経由のネットワーク接続</strong></p>

GoogleのパブリックDNSサーバーにpingを実行して、インターネット接続をテストします。

```
$ ping 8.8.8.8
PING 8.8.8.8 (8.8.8.8): 56 data bytes
64 bytes from 8.8.8.8: seq=0 ttl=113 time=30.208 ms
64 bytes from 8.8.8.8: seq=1 ttl=113 time=38.143 ms
64 bytes from 8.8.8.8: seq=2 ttl=113 time=30.969 ms
64 bytes from 8.8.8.8: seq=3 ttl=113 time=33.586 ms
 
```

<br/><br/><br/>

## 6.2 ホストPCとのネットワーク共有
---
Windowsオペレーティングシステムで利用可能なインターネット接続共有 (ICS) 機能を利用することで、ルーターを使用せずにPCのインターネット接続をD3-Gと共有できます。

<br/><br/>

### 6.2.1 ホストPCのネットワーク構成
- コントロールパネル → ネットワークとインターネット → ネットワーク接続 → イーサネットの設定
 
1. インターネットに接続されているネットワークアダプター (Wi-Fiなど) を見つけ、右クリックして **プロパティ** を選択します。

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20AI-G/Available%20Applications/ethernet1.png" width="600"></p>
<p align="center"><strong>図 6.2 プロパティの選択</strong></p><br/>
 
2. 共有タブを選択します。

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20AI-G/Available%20Applications/ethernet2.png" width="400"></p>
<p align="center"><strong>図 6.3 共有タブの選択</strong></p><br/>

3. 「ネットワークのほかのユーザーに、このコンピューターのインターネット接続をとおしての接続を許可する」というチェックボックスをオンにします。
 
4. ホームネットワーク接続のドロップダウンメニューで、D3-Gが接続するイーサネットアダプター (「イーサネット」など) を選択します。

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20AI-G/Available%20Applications/ethernet3.png" width="400"></p>

### 6.2.4 ネットワーク接続の確認
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20D3-G/Software/host%20pc%20ethernet%20connection.png"width="500"></p>
<p align="center"><strong>図 6.5 ホストPCとのネットワーク共有</strong></p>
<br/>

GoogleのパブリックDNSサーバーにpingを実行して、インターネット接続をテストします。

```
$ ping 8.8.8.8
PING 8.8.8.8 (8.8.8.8): 56 data bytes
64 bytes from 8.8.8.8: seq=0 ttl=113 time=30.208 ms
64 bytes from 8.8.8.8: seq=1 ttl=113 time=38.143 ms
64 bytes from 8.8.8.8: seq=2 ttl=113 time=30.969 ms
64 bytes from 8.8.8.8: seq=3 ttl=113 time=33.586 ms
```

<br/><br/><br/><br/>

# 7. 40ピンGPIOヘッダー
---
D3-Gは40ピンGPIOヘッダーを備えており、さまざまなハードウェアプロジェクトに柔軟なI/O機能を提供します。
このヘッダーは汎用入出力 (GPIO) 操作と互換性があり、センサー、LED、ボタン、その他の周辺機器を接続するために使用できます。

構成に応じて、各ピンはデジタルI/O、PWM、I2C、SPI、UARTなどの複数の機能をサポートします。

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/d3g/Assets/TOPST%20D3-G/Software/d3-g%20gpio%2040pinmap.png" width="800"></p>
<p align="center"><strong>図 7.1 D3-Gの40ピンGPIOヘッダーピンマップ </strong></p> <br/>

**注**: 外部ハードウェアを接続する前に、詳細なピン機能と電圧レベルについて公式のピン配置図を参照してください。

<br/><br/><br/>

## 7.1 GPIOデジタル入力/出力
---
D3-Gは、40ピンヘッダーを介したデジタル入力および出力 (GPIO) をサポートしており、ボタン、LED、センサーなどの外部デバイスと対話できます。

### 7.1.1 LED
---
最も単純で一般的なGPIO出力の例の1つは、LEDの制御です。
このセクションでは、D3-Gを使用してLEDセンサーを接続して使用する方法を示します。

#### ステップ 1. ハードウェア要件
- D3-Gボード (x1)
- ブレッドボード (x1)
- LED (x1)
- オス-メスジャンパーワイヤー (x2)
- DC 5V電源アダプター (x1)
- USB to TTLシリアルケーブル (x1)

#### ステップ 2. 回路例
- LED
    - (+) ピンはD3-Gボードのピン12に接続します。
    - (-) ピンはD3-GボードのGNDとして機能するピン14に接続します。

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20D3-G/Software/led.png"></p>

<p align="center"><strong>図 7.2 D3-G GPIO LED回路図 </strong></p> <br/>

##### ステップ 2.1 ピンマッピング
次の表はピンマッピングを示しています。

<div align="center">
  <p><strong>表 7.1 D3-G LEDのピンマッピング</strong></p>
  <table>
      <tr>
          <th colspan="3">ピン名</th>
          <th>D3-G</th>
          <th>GPIO</th>
      </tr>
      <tr>
          <td colspan="3">LED (+) ピン</td>
          <td>12</td>
          <td>89</td>
      </tr>
      <tr>
          <td colspan="3">LED (-) ピン</td>
          <td>14</td>
          <td>GND</td>
      </tr>
  </table>
</div>

#### ステップ 3. 実行方法
D3-GボードのGPIO89に接続されたLEDを操作するには、次のコードを実行します。

```
import time
import os
  
def export_gpio(pin, direction: str):
    # ピンがすでにアクティブな場合は、エクスポートを解除します。
    if os.path.exists(f"/sys/class/gpio/gpio{pin}"):
        with open("/sys/class/gpio/unexport", "w") as f:
            f.write(str(pin))
  
    # ピンをエクスポートしてアクティブにします。
    with open("/sys/class/gpio/export", "w") as f:
        f.write(str(pin))
  
    # ピンの方向を設定します。
    with open(f"/sys/class/gpio/gpio{pin}/direction", "w") as f:
        f.write(direction)

def read_gpio_value(pin: int):
    gpio_value_path = f"/sys/class/gpio/gpio{pin}/value"
    with open(gpio_value_path, "r") as f:
        return f.read().strip()

def write_gpio_value(pin: int, value: int):
    gpio_value_path = f"/sys/class/gpio/gpio{pin}/value"
    with open(gpio_value_path, "w") as f:
        f.write(str(value))

def unexport_gpio(pin: int):
    with open("/sys/class/gpio/unexport", "w") as f:
        f.write(str(pin))

  
def main():
    print("""\
                        +--------+
                    3P3-|-1    2-|-5P0
       I2C_SDA / GPIO82-|-3    4-|-5P0
       I2C_SCL / GPIO81-|-5    6-|-GND
                 GPIO83-|-7    8-|-GPIO87 / UT_TXD
                    GND-|-9   10-|-GPIO88 / UT_RXD
                 GPIO84-|-11  12-|-GPIO89 / PWM 0
                 GPIO85-|-13  14-|-GND
                 GPIO86-|-15  16-|-GPIO90
                    3P3-|-17  18-|-GPIO65
     SPIO_MOSI / GPIO63-|-19  20-|-GND
     SPIO_MISO / GPIO64-|-21  22-|-GPIO66
     SPIO_SCLK / GPIO61-|-23  24-|-GPIO62 / SPIO_CS0
                    GND-|-25  26-|-GPIO67 / SPIO_CS1
              RESERVED0-|-27  28-|-RESERVED1
                GPIO112-|-29  30-|-GND
                GPIO113-|-31  32-|-GPIO115 / PWM 2
         PWM1 / GPIO114-|-33  34-|-GND
    SPI1_MISO / GPIO121-|-35  36-|-GPIO119 / SPI1_CS0
                GPIO117-|-37  38-|-GPIO120 / SPI1_MOSI
                    GND-|-39  40-|-GPIO118 / SPI1_SCLK
                        +--------+""")
  
    LED_PIN = 89  # GPIO 89に接続されたLED
  
    try:
        # GPIOピンの設定
        export_gpio(LED_PIN, direction="out")
        print("GPIO pins initialized.")
        
        count = 0
        while (count < 10):
            write_gpio_value(LED_PIN, 1)  # LEDを点灯
            print("LED ON.")
            count += 1
            time.sleep(1.0)  # ポーリング遅延
            write_gpio_value(LED_PIN, 0)  # LEDを消灯
            print("LED OFF.")
            time.sleep(1.0)  # ポーリング遅延
 
        write_gpio_value(LED_PIN, 0)  # LEDを消灯
 
    except KeyboardInterrupt:
        print("Program interrupted by user.")
  
    finally:
        unexport_gpio(LED_PIN) # LEDピンのエクスポート解除
        print("GPIO pins unexported.")
        print("Program terminated.")

if __name__ == "__main__":
    main()
```

#### ステップ 4. 実行結果
次のコマンドでコードを実行します。

```
$ python3 led_test.py
```

- USB to TTL Serial Cable (x1)

#### Step 2. Example Circuit
- Button switch
    - One leg of the button switch is connected to pin 10 on the D3-G board.
    - The opposite leg above the button is connected to the 3.3V pin.

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20D3-G/Software/button_circuit.png"></p> 
<p align="center"><strong>Figure 7.3 D3-G GPIO Button Circuit Schematic</strong></p>

##### Step 2.1 Pin Mapping
The following table shows pin mapping.

<div align="center">
  <p><strong>Table 7.2 Pin Mapping of D3-G Button</strong></p>
  <table>
      <tr>
          <th colspan="3">Pin Name</th>
          <th>D3-G</th>
          <th>GPIO</th>
      </tr>
      <tr>
          <td colspan="3">One leg pin of button</td>
          <td>10</td>
          <td>88</td>
      </tr>
  </table>
</div>

#### Step 3. How to execute
To monitor the button input connected to GPIO88 on the D3-G board, run the following code:

```
import os
import time
BUTTON_PIN = 88  # button sensor GPIO pin
 
def export_gpio(pin: int, direction: str):
    # If the pin is already active, unexport it.
    if os.path.exists(f"/sys/class/gpio/gpio{pin}"):
        with open("/sys/class/gpio/unexport", "w") as f:
            f.write(str(pin))
  
    # Export the pin to activate it.
    with open("/sys/class/gpio/export", "w") as f:
        f.write(str(pin))
  
    # Set the pin direction.
    with open(f"/sys/class/gpio/gpio{pin}/direction", "w") as f:
        f.write(direction)

def read_gpio_value(pin: int):
    gpio_value_path = f"/sys/class/gpio/gpio{pin}/value"
    with open(gpio_value_path, "r") as f:
        return f.read().strip()

def write_gpio_value(pin: int, value: int):
    gpio_value_path = f"/sys/class/gpio/gpio{pin}/value"
    with open(gpio_value_path, "w") as f:
        f.write(str(value))

def unexport_gpio(pin: int):
    with open("/sys/class/gpio/unexport", "w") as f:
        f.write(str(pin))
def main():
    # GPIOピンの初期化
    export_gpio(BUTTON_PIN, "in")  
    print("gpio pins initialized.")
 
    try:
        while True:
            sensor_value = read_gpio_value(BUTTON_PIN)
 
            if sensor_value == "0":  
                print("button pressed.")
            else:    
                print("button released.")
 
            time.sleep(0.5)  # 500ms delay
 
    except KeyboardInterrupt:
        print("Program interrupted by user.")
 
    finally:
        unexport_gpio(BUTTON_PIN)  # GPIOピンのエクスポート解除
        print("GPIO pins unexported.")
        print("Program terminated.")
         
if __name__ == "__main__":
    main()
```
 
#### ステップ 4. 実行結果
次のコマンドでコードを実行します。
```
$ python3 test_button.py
```
このスクリプトは、GPIO88をデジタル入力として構成し、その値をリアルタイムで継続的に監視します。
実行すると、GPIO88に接続されたボタンを押すと、ボタンが押されたことを示すメッセージが出力されます。
 
スクリプトを停止するには、**[Ctrl+C]** を押します。
スクリプトが終了すると、GPIO88は自動的にエクスポート解除され、クリーンアップされます。
 
**注**: ここでは例としてGPIO88を使用しています。40ピンヘッダーのピン配置に基づいて、D3-Gで利用可能な任意のGPIOピンを使用できます。
公式のピン配置図を参照して、ハードウェア構成に一致するGPIO番号を選択してください。
 
<br/><br/><br/><br/>
 
### 7.1.3 タッチセンサー
---
タッチセンサーは、GPIOを介してデジタル入力信号として人間のタッチを検出するために使用できます。
このセクションでは、D3-Gを使用して基本的なタッチセンサーモジュールを接続し、入力を読み取る方法を示します。
 
#### ステップ 1. ハードウェア要件
- D3-Gボード (x1)
- タッチセンサー (x1)
- メス-メスジャンパーワイヤー (x3)
- DC 5V電源アダプター (x1)
- USB to TTLシリアルケーブル (x1)
 
#### ステップ 2. 回路例
- タッチセンサー
    - タッチセンサーのSIGピンはD3-Gボードのピン88に接続します。
    - タッチセンサーのVCCピンはD3-Gボードの3.3Vに接続します。
    - タッチセンサーのGNDピンはD3-GボードのGNDに接続します。
 
 
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20D3-G/Software/touch%20circuit.png"></p>
<p align="center"><strong>図 7.4 D3-G GPIOタッチセンサー回路図</strong></p>
 
##### ステップ 2.1 ピンマッピング
次の表はピンマッピングを示しています。
 
<div align="center">
  <p><strong>表 7.3 D3-Gタッチセンサーのピンマッピング</strong></p>
  <table>
      <tr>
          <th colspan="3">ピン名</th>
          <th>D3-G</th>
          <th>GPIO</th>
      </tr>
      <tr>
          <td colspan="3">SIG</td>
          <td>10</td>
          <td>88</td>
      </tr>
      <tr>
          <td colspan="3">VCC</td>
          <td>1</td>
          <td>3.3</td>
      </tr>
      <tr>
          <td colspan="3">GND</td>
          <td>20</td>
          <td>GND</td>
      </tr>
  </table>
</div>
 
#### ステップ 3. 実行方法
D3-GボードのGPIO88に接続されたタッチセンサーを監視するには、次のコードを実行するだけです。
```
import os
import time
 
# GPIOピン番号の設定
TOUCH_SENSOR_PIN = 88  # センサーGPIOピン
 
def export_gpio(pin: int, direction: str):
    # ピンがすでにアクティブな場合は、エクスポートを解除します。
    if os.path.exists(f"/sys/class/gpio/gpio{pin}"):
        with open("/sys/class/gpio/unexport", "w") as f:
            f.write(str(pin))
  
    # ピンをエクスポートしてアクティブにします。
    with open("/sys/class/gpio/export", "w") as f:
        f.write(str(pin))
  
    # ピンの方向を設定します。
    with open(f"/sys/class/gpio/gpio{pin}/direction", "w") as f:
        f.write(direction)
 
def read_gpio_value(pin: int):
    gpio_value_path = f"/sys/class/gpio/gpio{pin}/value"
    with open(gpio_value_path, "r") as f:
        return f.read().strip()
 
def write_gpio_value(pin: int, value: int):
    gpio_value_path = f"/sys/class/gpio/gpio{pin}/value"
    with open(gpio_value_path, "w") as f:
        f.write(str(value))
 
def unexport_gpio(pin: int):
    with open("/sys/class/gpio/unexport", "w") as f:
        f.write(str(pin))
def main():
    # GPIOピンの初期化
    export_gpio(TOUCH_SENSOR_PIN, "in")  # タッチセンサーのピン方向 "in"
    print("gpio pins initialized.")
 
    try:
        while True:
            # ボタンセンサーの値の読み取り
            # センサー値が0の場合、タッチが検出されたことを意味します。
            # センサー値が1の場合、タッチが解除されたことを意味します。
            sensor_value = read_gpio_value(TOUCH_SENSOR_PIN)
 
            if sensor_value == "1":  
                print("touch detected.")
            else:    
                print("touch released.")
 
            time.sleep(0.5)  # 500ms delay
 
    except KeyboardInterrupt:
        print("program interrupted by user.")
 
    finally:
        unexport_gpio(TOUCH_SENSOR_PIN)  # GPIOピンのエクスポート解除
        print("GPIO pins unexported.")
        print("program terminated.")
         
if __name__ == "__main__":
    main()
```
 
#### ステップ 4. 実行結果
次のコマンドでコードを実行します。
 
```
$ python3 touch_test.py
```
 
このスクリプトは、GPIO88をデジタル入力として構成し、その値をリアルタイムで継続的に監視します。
 
実行すると、センサーに触れると、ターミナルに次のようなメッセージが出力されます。
```
touch detected.
```
センサーに触れていない場合、出力は次のようになります。
```
touch released.
```
スクリプトを停止するには、**[Ctrl+C]** を押します。
スクリプトが終了すると、GPIO88は自動的にエクスポート解除され、クリーンアップされます。
 
**注**: ここでは例としてGPIO88を使用しています。40ピンヘッダーのピン配置に基づいて、D3-Gで利用可能な任意のGPIOピンを使用できます。
公式のピン配置図を参照して、ハードウェア構成に一致するGPIO番号を選択してください。
 
<br/><br/><br/><br/>
 
### 7.1.4 振動検出センサー
---
振動センサーは、物理的な衝撃や振動を検出し、GPIOを介してデジタル入力信号を出力するために使用できます。
このセクションでは、D3-Gを使用して基本的な振動センサーモジュールを接続し、入力を検出する方法を示します。
 
#### ステップ 1. ハードウェア要件
- D3-Gボード (x1)
- 振動検出センサー (x1)
- メス-メスジャンパーワイヤー (x4)
- DC 5V電源アダプター (x1)
- USB to TTLシリアルケーブル (x1)
 
#### ステップ 2. 回路例
- 振動検出センサー
    - 振動検出センサーのVCCピンはD3-Gボードの3.3Vピンに接続します。
    - 振動検出センサーのGNDピンはD3-GボードのGNDに接続します。
    - 振動検出センサーのDOピンはD3-Gボードの88ピンに接続します。
 
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20D3-G/Software/vibr%20circuit.png"></p>
<p align="center"><strong>図 7.5 D3-G GPIO振動検出センサー回路図</strong></p>
 
##### ステップ 2.1 ピンマッピング
次の表はピンマッピングを示しています。
 
<div align="center">
  <p><strong>表 7.4 D3-G振動検出センサーのピンマッピング</strong></p>
  <table>
      <tr>
          <th colspan="3">ピン名</th>
          <th>D3-G</th>
          <th>GPIO</th>
      </tr>
      <tr>
          <td colspan="3">VCC</td>
          <td>1</td>
          <td>3.3V</td>
      </tr>
      <tr>
          <td colspan="3">GND</td>
          <td>20</td>
          <td>GND</td>
      </tr>
      <tr>
          <td colspan="3">DO</td>
          <td>10</td>
          <td>88</td>
      </tr>
  </table>
</div>
 
#### ステップ 3. 実行方法
D3-GボードのGPIO88に接続された振動センサーを監視するには、次のコードを実行します。
```
import os
import time
VIBRATION_SENSOR_PIN = 88  # 振動センサーGPIOピン
 
def export_gpio(pin: int, direction: str):
    # ピンがすでにアクティブな場合は、エクスポートを解除します。
    if os.path.exists(f"/sys/class/gpio/gpio{pin}"):
        with open("/sys/class/gpio/unexport", "w") as f:
            f.write(str(pin))
  
    # ピンをエクスポートしてアクティブにします。
    with open("/sys/class/gpio/export", "w") as f:
        f.write(str(pin))
  
    # ピンの方向を設定します。
    with open(f"/sys/class/gpio/gpio{pin}/direction", "w") as f:
        f.write(direction)
 
def read_gpio_value(pin: int):
    gpio_value_path = f"/sys/class/gpio/gpio{pin}/value"
    with open(gpio_value_path, "r") as f:
        return f.read().strip()
 
def write_gpio_value(pin: int, value: int):
    gpio_value_path = f"/sys/class/gpio/gpio{pin}/value"
    with open(gpio_value_path, "w") as f:
        f.write(str(value))
 
def unexport_gpio(pin: int):
    with open("/sys/class/gpio/unexport", "w") as f:
        f.write(str(pin))
def main():
    # GPIOピンの初期化
    export_gpio(VIBRATION_SENSOR_PIN, "in")  # 振動センサーのピン方向 "in"
    print("gpio pins initialized.")
 
    try:
        while True:
            sensor_value = read_gpio_value(VIBRATION_SENSOR_PIN)
 
            if sensor_value == "0":  # 振動検出
                print("vibration detected.")
            else:    # 振動なし
                print("no vibration detected.")
 
            time.sleep(0.5)  # 500ms delay
 
    except KeyboardInterrupt:
        print("Program interrupted by user.")
 
    finally:
        unexport_gpio(VIBRATION_SENSOR_PIN)  # GPIOピンのエクスポート解除
        print("GPIO pins unexported.")
        print("Program terminated.")
         
if __name__ == "__main__":
    main()

#### ステップ 4. 実行結果
次のコマンドでコードを実行します。
 
```
$ python3 vibration_test.py
```
 
このスクリプトは、GPIO88をデジタル入力として構成し、その値をリアルタイムで継続的に監視します。
実行すると、センサーによって検出された振動や衝撃により、ターミナルに次のようなメッセージが出力されます。
```
vibration detected.
```
振動がない場合、出力は次のようになります。
```
no vibration detected.
```
スクリプトを停止するには、**[Ctrl+C]** を押します。
終了すると、GPIO88は自動的にエクスポート解除され、クリーンアップされます。
 
**注**: ここでは例としてGPIO88を使用しています。センサーの配線やヘッダーのレイアウトに応じて、他の利用可能なGPIOピンを使用できます。GPIO番号を選択する前に、D3-Gのピン配置を参照してください。
 
<br/><br/><br/><br/>
 
### 7.1.5 赤外線センサー (SZH-SSBH-002)
---
赤外線センサーは、反射された赤外線を感知し、GPIOを介してデジタル信号を出力することで、近くの障害物を検出するために使用できます。
このセクションでは、D3-Gを使用してSZH-SSBH-002赤外線センサーを接続し、入力を読み取る方法を示します。
 
#### ステップ 1. ハードウェア要件
- D3-Gボード (x1)
- ブレッドボード (x1)
- 赤外線センサー (x1)
- オス-メスジャンパーワイヤー (x5)
- DC 5V電源アダプター (x1)
- USB to TTLシリアルケーブル (x1)
 
#### ステップ 2. 回路例
- 赤外線センサー
    - 赤外線センサーのVCCピンはD3-Gボードの3.3Vピンに接続します。
    - 赤外線センサーのGNDピンはD3-GボードのGNDに接続します。
    - 赤外線センサーのOUTピンはD3-Gボードの89ピンに接続します。
 
 
<p align="center">
  <img src="https://raw.githubusercontent.com/topst-development/Documentation/d3g/Assets/TOPST%20D3-G/Software/szh-ssbh-002_circuit.png">
</p> 
<p align="center"><strong>図 7.6 IRセンサー実験回路</strong></p>
 
##### ステップ 2.1 ピンマッピング
次の表はピンマッピングを示しています。
 
<div align="center">
  <p><strong>表 7.5 D3-G IRセンサーのピンマッピング</strong></p>
  <table>
      <tr>
          <th colspan="3">ピン名</th>
          <th>D3-G</th>
          <th>GPIO</th>
      </tr>
      <tr>
          <td colspan="3">VCC</td>
          <td>1</td>
          <td>3.3V</td>
      </tr>
      <tr>
          <td colspan="3">GND</td>
          <td>6</td>
          <td>GND</td>
      </tr>
      <tr>
          <td colspan="3">OUT</td>
          <td>12</td>
          <td>89</td>
      </tr>
  </table>
</div>
 
#### ステップ 3. 実行方法
D3-GボードのGPIO89に接続されたIRセンサーを監視するには、次のコードを実行します。
 
```
import os
import time
 
# GPIOピン番号の設定
IR_SENSOR_PIN = 89  # IRセンサーGPIOピン
 
def export_gpio(pin: int, direction: str):
    # ピンがすでにアクティブな場合は、エクスポートを解除します。
    if os.path.exists(f"/sys/class/gpio/gpio{pin}"):
        with open("/sys/class/gpio/unexport", "w") as f:
            f.write(str(pin))
  
    # ピンをエクスポートしてアクティブにします。
    with open("/sys/class/gpio/export", "w") as f:
        f.write(str(pin))
  
    # ピンの方向を設定します。
    with open(f"/sys/class/gpio/gpio{pin}/direction", "w") as f:
        f.write(direction)
 
def read_gpio_value(pin: int):
    gpio_value_path = f"/sys/class/gpio/gpio{pin}/value"
    with open(gpio_value_path, "r") as f:
        return f.read().strip()
 
def write_gpio_value(pin: int, value: int):
    gpio_value_path = f"/sys/class/gpio/gpio{pin}/value"
    with open(gpio_value_path, "w") as f:
        f.write(str(value))
 
def unexport_gpio(pin: int):
    with open("/sys/class/gpio/unexport", "w") as f:
        f.write(str(pin))
def main():
    # GPIOピンの初期化
    export_gpio(IR_SENSOR_PIN, "in")  # IRセンサーのピン方向 "in"
    print("gpio pins initialized.")
 
    try:
        while True:
            sensor_value = read_gpio_value(IR_SENSOR_PIN)
 
            if sensor_value == "0":  # 障害物検出
                print("obstacle detected.")
            else: 
                print("No obstacle detected.")
 
            time.sleep(0.5)  # 500ms delay
 
    except KeyboardInterrupt:
        print("program interrupted by user.")
 
    finally:
        unexport_gpio(IR_SENSOR_PIN)  # GPIOピンのエクスポート解除
        print("GPIO pins unexported.")
        print("program terminated.")
         
if __name__ == "__main__":
    main()
 
#### ステップ 4. 実行結果
次のコマンドでコードを実行します。
```
$ python3 ir_test.py
```
このスクリプトは、GPIO89をデジタル入力として構成し、その状態を継続的に監視して障害物を検出します。
IRセンサーの前で物体が検出されると、ターミナルに次のように表示されます。
```
obstacle detected.
```
物体が検出されない場合、次のように表示されます。
```
no obstacle detected.
```
スクリプトを停止するには、**[Ctrl+C]** を押します。
スクリプトが終了すると、GPIO89は自動的にエクスポート解除され、クリーンアップされます。
 
**注**: このスクリプトでは、例としてGPIO89を使用しています。
D3-Gの40ピンヘッダーに基づいて、利用可能な任意のGPIOピンを使用できます。正確なピン選択については、公式のピン配置図を参照してください。
 
<br/><br/><br/><br/>
 
### 7.1.6 フォトレジスタ (SZH-SSBH-011)
---
フォトレジスタは、周囲の光レベルを検出し、光強度が特定のしきい値を超えたときにGPIOを介してデジタル信号を出力するために使用できます。
このセクションでは、D3-Gを使用してSZH-SSBH-011フォトレジスタセンサーを接続し、入力を読み取る方法を示します。
 
#### ステップ 1. ハードウェア要件
- D3-Gボード (x1)
- フォトレジスタモジュール (SZH-SSBH-011) (x1)
- LED (x1)
- 220Ω抵抗 (x1)
- ブレッドボード (x1)
- オス-メスジャンパーワイヤー (x7)
- DC 5V電源アダプター (x1)
- USB to TTLシリアルケーブル (x1)
 
#### ステップ 2. 回路例
- フォトレジスタ (SZH-SSBH-011)
    - フォトレジスタのVCCピンはD3-Gボードの3.3Vピンに接続します。
    - フォトレジスタのGNDピンはD3-GボードのGNDに接続します。
    - フォトレジスタのDOピンはD3-Gボードのピン89に接続します。
- LED
    - LEDの (+) ピンはD3-GボードのGNDに接続します。
    - LEDの (-) ピンはD3-Gボードのピン83に接続します。
 
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20D3-G/Software/circuit.png"></p>
<p align="center"><strong>図 7.7 フォトレジスタ実験回路</strong></p>
 
##### ステップ 2.1 ピンマッピング
次の表はピンマッピングを示しています。
 
<div align="center">
  <p><strong>表 7.6 D3-Gフォトレジスタのピンマッピング</strong></p>
  <table>
      <tr>
          <th colspan="3">ピン名</th>
          <th>D3-G</th>
          <th>GPIO</th>
      </tr>
      <tr>
          <td colspan="3">VCC</td>
          <td>1</td>
          <td>3.3V</td>
      </tr>
      <tr>
          <td colspan="3">GND</td>
          <td>6</td>
          <td>GND</td>
      </tr>
      <tr>
          <td colspan="3">DO</td>
          <td>12</td>
          <td>89</td>
      </tr>
  </table>
</div>
 
 
<div align="center">
  <p><strong>表 7.7 D3-G LEDのピンマッピング</strong></p>
  <table>
      <tr>
          <th colspan="3">ピン名</th>
          <th>D3-G</th>
          <th>GPIO</th>
      </tr>
      <tr>
          <td colspan="3">(+)</td>
          <td>7</td>
          <td>83</td>
      </tr>
      <tr>
          <td colspan="3">(-)</td>
          <td>14</td>
          <td>GND</td>
      </tr>
  </table>
</div>
 
### ステップ 3. 実行方法
次のPythonスクリプトを実行して、CDSセンサーで明るさを監視し、それに応じてLEDを制御します。
 
```
import os
import time
LED_PIN = 83           # LED GPIOピン
CDS_SENSOR_PIN = 89    # szh-ssbh-011 CDSセンサーGPIOピン
 
def export_gpio(pin, direction: str):
    # ピンがすでにアクティブな場合は、エクスポートを解除します。
    if os.path.exists(f"/sys/class/gpio/gpio{pin}"):
        with open("/sys/class/gpio/unexport", "w") as f:
            f.write(str(pin))
  
    # ピンをエクスポートしてアクティブにします。
    with open("/sys/class/gpio/export", "w") as f:
        f.write(str(pin))
  
    # ピンの方向を設定します。
    with open(f"/sys/class/gpio/gpio{pin}/direction", "w") as f:
        f.write(direction)
 
def read_gpio_value(pin: int):
    gpio_value_path = f"/sys/class/gpio/gpio{pin}/value"
    with open(gpio_value_path, "r") as f:
        return f.read().strip()
 
def write_gpio_value(pin: int, value: int):
    gpio_value_path = f"/sys/class/gpio/gpio{pin}/value"
    with open(gpio_value_path, "w") as f:
        f.write(str(value))
 
def unexport_gpio(pin: int):
    with open("/sys/class/gpio/unexport", "w") as f:
        f.write(str(pin))
 
def main():
    # GPIOピンの初期化
    export_gpio(LED_PIN, "out")          # LEDピン方向 "out"
    export_gpio(CDS_SENSOR_PIN, "in")     # CDSセンサーピン方向 "in"
    print("gpio pins initialized.")
 
    try:
        while True:
            sensor_value = read_gpio_value(CDS_SENSOR_PIN)
            print("sensor value: {}".format(sensor_value))
            if sensor_value == "0": # 光検出
                print("brightness detected. Turning on the LED.")
                write_gpio_value(LED_PIN, 1)  # LEDを点灯
            else:
                print("no brightness detected. Turning off the LED.")
                write_gpio_value(LED_PIN, 0)  # LEDを消灯
 
            time.sleep(0.5)  #  500ms遅延
 
    except KeyboardInterrupt:
        print("program interrupted by user.")
 
    finally:
        unexport_gpio(LED_PIN)          # LEDピンのエクスポート解除
        unexport_gpio(CDS_SENSOR_PIN)   # CDSセンサーピンのエクスポート解除
        print("GPIO pins unexported.")
        print("program terminated.")
 
if __name__ == "__main__":
    main()

### ステップ 4. 実行結果
次のコマンドでコードを実行します。
```
$ python3 CDS_test.py
```
このスクリプトは、フォトレジスタセンサーの入力としてGPIO89を、LEDの出力としてGPIO83を構成します。
周囲の光が検出されると、ターミナルに次のように出力されます。
```
sensor value: 0
brightness detected. Turning on the LED.
```
そして、LEDが点灯します。
光が検出されない場合、次のように出力されます。
```
sensor value: 1
no brightness detected. Turning off the LED.
```
そして、LEDが消灯します。
スクリプトを停止するには、**[Ctrl+C]** を押します。
スクリプトが終了すると、両方のGPIOピンは自動的にエクスポート解除され、クリーンアップされます。
 
**注**: この例ではGPIO83とGPIO89が使用されています。D3-Gの40ピンヘッダーレイアウトに基づいて、利用可能な任意のGPIOピンを使用できます。正確なピン選択については、公式のピン配置図を参照してください。
 
<br/><br/><br/><br/>
 
### 7.1.7 大気汚染検出センサー
---
大気汚染検出センサーは、環境中の有害ガスや粒子状物質の存在を監視し、GPIOを介してデジタル信号を出力するために使用できます。
このセクションでは、D3-Gを使用して大気汚染検出センサーを接続し、入力を読み取る方法を示します。
 
#### ステップ 1. ハードウェア要件
- D3-Gボード (x1)
- 大気汚染 (ガス) 検出センサーモジュール (x1)
- ブレッドボード (x1)
- オス-メスジャンパーワイヤー (x3)
- DC 5V電源アダプター (x1)
- USB to TTLシリアルケーブル (x1)
 
#### ステップ 2. 回路例
- 大気汚染検出センサー
    - 大気汚染検出センサーのVCCピンはD3-Gボードの3.3Vピンに接続します。
    - 大気汚染検出センサーのGNDピンはD3-GボードのGNDに接続します。
    - 大気汚染検出センサーのDOピンはD3-Gボードのピン88に接続します。
 
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20D3-G/Software/gas%20circuit.png"></p>
<p align="center"><strong>図 7.8 大気汚染検出センサー実験回路</strong></p>
 
##### ステップ 2.1 ピンマッピング
次の表はピンマッピングを示しています。
 
<div align="center">
  <p><strong>表 7.8 D3-G大気汚染検出センサーのピンマッピング</strong></p>
  <table>
      <tr>
          <th colspan="3">ピン名</th>
          <th>D3-G</th>
          <th>GPIO</th>
      </tr>
      <tr>
          <td colspan="3">VCC</td>
          <td>1</td>
          <td>3.3V</td>
      </tr>
      <tr>
          <td colspan="3">GND</td>
          <td>20</td>
          <td>GND</td>
      </tr>
      <tr>
          <td colspan="3">DO</td>
          <td>10</td>
          <td>88</td>
      </tr>
  </table>
</div>
 
#### ステップ 3. 実行方法
次のPythonスクリプトを実行して、GPIO88ピンを使用してガス検出を監視します。
 
```
import os
import time
GAS_SENSOR_PIN = 88  # ガスセンサーGPIOピン
 
def export_gpio(pin: int, direction: str):
    # ピンがすでにアクティブな場合は、エクスポートを解除します。
    if os.path.exists(f"/sys/class/gpio/gpio{pin}"):
        with open("/sys/class/gpio/unexport", "w") as f:
            f.write(str(pin))
  
    # ピンをエクスポートしてアクティブにします。
    with open("/sys/class/gpio/export", "w") as f:
        f.write(str(pin))
  
    # ピンの方向を設定します。
    with open(f"/sys/class/gpio/gpio{pin}/direction", "w") as f:
        f.write(direction)
 
def read_gpio_value(pin: int):
    gpio_value_path = f"/sys/class/gpio/gpio{pin}/value"
    with open(gpio_value_path, "r") as f:
        return f.read().strip()
 
def write_gpio_value(pin: int, value: int):
    gpio_value_path = f"/sys/class/gpio/gpio{pin}/value"
    with open(gpio_value_path, "w") as f:
        f.write(str(value))
 
def unexport_gpio(pin: int):
    with open("/sys/class/gpio/unexport", "w") as f:
        f.write(str(pin))
def main():
    # GPIOピンの初期化
    export_gpio(GAS_SENSOR_PIN, "in")  # ガスセンサーピン方向 "in"
    print("gpio pins initialized.")
 
    try:
        while True:
            # ガスセンサーの値の読み取り
            sensor_value = read_gpio_value(GAS_SENSOR_PIN)
 
            if sensor_value == "0":  # ガス検出
                print("gas detected.")
            else:
                print("no gas detected.")
 
            time.sleep(0.5)  # 500ms遅延
 
    except KeyboardInterrupt:
        print("program interrupted by user.")
 
    finally:
        unexport_gpio(GAS_SENSOR_PIN)  # GPIOピンのエクスポート解除
        print("GPIO pins unexported.")
        print("program terminated.")
         
if __name__ == "__main__":
    main()
```
 
#### ステップ 4. 実行結果
次のコマンドでコードを実行します。
```
$ python3 gas_sensor_test.py
```
このスクリプトは、GPIO88をデジタル入力として構成し、ガス検出ステータスを継続的に監視します。
ガス濃度がセンサーのしきい値に達すると、ターミナルに次のように表示されます。
```
gas detected.
```
ガスが検出されない場合、ターミナルには次のように表示されます。
```
no gas detected.
```
スクリプトを停止するには、**[Ctrl+C]** を押します。
スクリプトが終了すると、GPIO88は自動的にエクスポート解除され、クリーンアップされます。
 
**注**: ここでは例としてGPIO88を使用しています。D3-Gの40ピンヘッダーレイアウトに基づいて、利用可能な任意のGPIOピンを使用できます。正確なピン選択については、公式のピン配置図を参照してください。
 
<br/><br/><br/><br/>
 
### 7.1.8 超音波センサー
---
超音波センサーは、超音波を発信し、反射信号を受信することで近くの物体までの距離を測定し、GPIOを介してデジタル (またはパルスベース) 信号を出力するために使用できます。
このセクションでは、D3-Gを使用して超音波センサーを接続し、入力を読み取る方法を示します。
 
#### ステップ 1. ハードウェア要件
- D3-Gボード (x1)
- 超音波センサー (x1)
- メス-メスジャンパーワイヤー (x4)
- DC 5V電源アダプター (x1)
- USB to TTLシリアルケーブル (x1)
 
#### ステップ 2. 回路例
- 超音波センサー
    - 超音波センサーのVCCピンはD3-Gボードの5Vピンに接続します。
    - 超音波センサーのGNDピンはD3-GボードのGNDに接続します。
    - 超音波センサーのTRIGピンはD3-Gボードのピン82に接続します。
    - 超音波センサーのECHOピンはD3-Gボードのピン88に接続します。

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20D3-G/Software/ultra%20circuit.png"></p>
<p align="center"><strong>図 7.9 超音波センサー実験回路</strong></p>

##### ステップ 2.1 ピンマッピング
次の表はピンマッピングを示しています。

<div align="center">
  <p><strong>表 7.9 D3-G超音波センサーのピンマッピング</strong></p>
  <table>
      <tr>
          <th colspan="3">ピン名</th>
          <th>D3-G</th>
          <th>GPIO</th>
      </tr>
      <tr>
          <td colspan="3">VCC</td>
          <td>2</td>
          <td>5V</td>
      </tr>
      <tr>
          <td colspan="3">GND</td>
          <td>6</td>
          <td>GND</td>
      </tr>
      <tr>
          <td colspan="3">TRIG</td>
          <td>3</td>
          <td>82</td>
      </tr>
      <tr>
          <td colspan="3">ECHO</td>
          <td>10</td>
          <td>88</td>
      </tr>
  </table>
</div>

#### ステップ 3. 実行方法
次のPythonスクリプトを実行して、超音波センサーを使用して距離を測定します。
```
import os
import time

TRIG_PIN = 82  
ECHO_PIN = 88  

def export_gpio(pin: int, direction: str):
    if os.path.exists(f"/sys/class/gpio/gpio{pin}"):
        with open("/sys/class/gpio/unexport", "w") as f:
            f.write(str(pin))
    with open("/sys/class/gpio/export", "w") as f:
        f.write(str(pin))
    with open(f"/sys/class/gpio/gpio{pin}/direction", "w") as f:
        f.write(direction)

def write_gpio_value(pin: int, value: int):
    with open(f"/sys/class/gpio/gpio{pin}/value", "w") as f:
        f.write(str(value))

def read_gpio_value(pin: int) -> str:
    with open(f"/sys/class/gpio/gpio{pin}/value", "r") as f:
        return f.read().strip()

def unexport_gpio(pin: int):
    with open("/sys/class/gpio/unexport", "w") as f:
        f.write(str(pin))

def get_distance_cm():
    write_gpio_value(TRIG_PIN, 0)
    time.sleep(0.00002)  
    write_gpio_value(TRIG_PIN, 1)
    time.sleep(0.00001)  
    write_gpio_value(TRIG_PIN, 0)

    start = time.time()
    while read_gpio_value(ECHO_PIN) == "0":
        start = time.time()
    end = start
    while read_gpio_value(ECHO_PIN) == "1":
        end = time.time()
    duration = end - start
    distance = (duration * 34300) / 2  # cm
    return round(distance, 2)

def main():
    export_gpio(TRIG_PIN, "out")
    export_gpio(ECHO_PIN, "in")
    print("GPIO pins initialized.")

    try:
        while True:
            distance = get_distance_cm()
            print(f"Distance: {distance} cm")
            time.sleep(1)

    except KeyboardInterrupt:
        print("Program interrupted by user.")

    finally:
        unexport_gpio(TRIG_PIN)
        unexport_gpio(ECHO_PIN)
        print("GPIO pins unexported.")
        print("Program terminated.")

if __name__ == "__main__":
    main()
```

#### ステップ 4. 実行結果
次のコマンドでコードを実行します。
```
$ python3 ultrasonic_sensor_test.py
```
このスクリプトは、超音波パルスをトリガーするデジタル出力としてGPIO82を、エコーを受信するデジタル入力としてGPIO88を構成します。
スクリプトを実行すると、センサーの前にある最も近い物体までの距離が1秒ごとに表示されます。例：
```
Distance: 23.45 cm
Distance: 24.12 cm
...
```
スクリプトを停止するには、**[Ctrl+C]** を押します。
スクリプトが終了すると、GPIO82とGPIO88は自動的にエクスポート解除され、クリーンアップされます。
 
**注**: GPIO82とGPIO88は例として使用されています。D3-Gの40ピンヘッダーレイアウトに基づいて、利用可能な任意のGPIOピンを使用できます。正確なピン選択については、公式のピン配置図を参照してください。また、ECHOピンの電圧レベルがD3-Gにとって安全であることを確認してください (一部のモジュールは5Vを出力するため、分圧器またはレベルシフターが必要になる場合があります)。
 
<br/><br/><br/><br/>
 
## 7.2 I2C
---
D3-Gは40ピンGPIOヘッダーを介してI2C通信を提供し、センサー、ディスプレイ、拡張モジュールなどのさまざまな周辺機器とのインターフェースを可能にします。
Inter-Integrated Circuit (I2C) は、データライン (SDA) とクロックライン (SCL) で構成される2線式通信プロトコルであり、複数のデバイスが共有バス上で通信できるようにします。
 
I2C通信はマスター/スレーブアーキテクチャに従い、1つのマスターデバイスが通信を制御し、最大127のスレーブデバイスを同じバスに接続できます。
SDAラインはデータの送受信の両方に使用され、SCLラインはデータ転送のタイミングを同期します。この同期通信モデルにより、デバイスは調整されたクロック駆動方式で情報を交換できます。
 
<br/><br/><br/><br/>
 
### 7.2.1 1602A LCDディスプレイ
---
1602A LCDは、組み込みシステムで一般的に使用される文字表示モジュールです。
D3-Gでは、LCDのSDAおよびSCLラインをI2C用に構成されたGPIOピンに接続できます。接続すると、Linux I2Cツールまたはカスタムソフトウェアを使用してLCDを制御できます。
 
#### ステップ 1. ハードウェア要件
- D3-Gボード (x1)
- 1602A I2C LCDモジュール (x1)
- メス-メスジャンパーワイヤー (x4)
- DC 5V電源アダプター (x1)
- USB to TTLシリアルケーブル (x1)  
 
LCDモジュールにI2Cバックパックがあることを確認してください
 
#### ステップ 2. 回路例
- I2C LCDモジュール
    - I2C LCDモジュールのGNDピンはD3-GボードのGNDピンに接続します。
    - I2C LCDモジュールのVCCピンはD3-Gボードの5Vに接続します。
    - I2C LCDモジュールのSDAピンはD3-Gボードのピン82に接続します。
    - I2C LCDモジュールのSCLピンはD3-Gボードのピン81に接続します。
 
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20D3-G/Software/lcd_circuit.png"></p>
<p align="center"><strong>図 7.10 D3-G I2C LCDモジュール回路図  </strong></p>
 
##### ステップ 2.1 ピンマッピング
次の表はピンマッピングを示しています。
 
<div align="center">
  <p><strong>表 7.10 D3-G I2C LCDモジュールのピンマッピング</strong></p>
  <table>
      <tr>
          <th colspan="3">ピン名</th>
          <th>D3-G</th>
          <th>GPIO</th>
      </tr>
      <tr>
          <td colspan="3">GND</td>
          <td>20</td>
          <td>GND</td>
      </tr>
      <tr>
          <td colspan="3">VCC</td>
          <td>2</td>
          <td>5V</td>
      </tr>
      <tr>
          <td colspan="3">SDA</td>
          <td>3</td>
          <td>82</td>
      </tr>
      <tr>
          <td colspan="3">SCL</td>
          <td>5</td>
          <td>81</td>
      </tr>
  </table>
</div>
 
#### ステップ 3. 実行方法
まず、必要なPythonライブラリをインストールします。
```
$ pip install RPLCD smbus2
```
次に、以下のPythonコードを使用してテキストをLCDに書き込みます。
```
import smbus2
import time
from RPLCD.i2c import CharLCD
 
# I2Cバス番号
I2C_BUS = 3
LCD_ADDRESS = 0x27
 
lcd = CharLCD(i2c_expander='PCF8574', address=LCD_ADDRESS, port=I2C_BUS,
              cols=16, rows=2, dotsize=8,
              charmap='A00', auto_linebreaks=True,
              backlight_enabled=True)
 
def display_text(text):
    lcd.clear()
    lcd.write_string(text)
 
def main():
    while True:
        user_input = input("Enter text to display on LCD: ")
        display_text(user_input)
        time.sleep(4)
        lcd.clear()
if __name__ == "__main__":
    main()
```
 
#### ステップ 4. 実行結果
次のコマンドでコードを実行します。
```
$ python3 lcd_test.py
```
このスクリプトは、RPLCDライブラリを使用してI2Cベースの1602A LCDを初期化し、ユーザーが入力したテキストを画面に表示します。
スクリプトを実行すると、文字列を入力するように求められます。そのテキストはLCDに4秒間表示され、その後消去されます。例：
```
Enter text to display on LCD: Hello D3-G!
```
LCDには次のように表示されます。
```
Hello D3-G!
```
そして4秒後に消去されます。
 
スクリプトを停止するには、**[Ctrl+C]** を押します。
 
**注** : D3-Gでは、デフォルトでGPIO82とGPIO81がI2Cに使用されます。
I2Cアドレス (0x27) が特定のLCDモジュールと一致していることを確認してください。必要に応じて **i2cdetect -y 3** を使用してI2Cデバイスをスキャンします。
 
<br/><br/><br/><br/>
 
## 7.3 SPI
---
D3-Gは40ピンGPIOヘッダーを介してSerial Peripheral Interface (SPI) 通信をサポートし、外部デバイスとD3-G間のデータ交換を可能にします。
 
SPIは、全二重通信 (データを同時に送受信できることを意味します) を可能にする同期シリアル通信プロトコルです。主に4つのラインを使用します：Master Out Slave In (MOSI)、Master In Slave Out (MISO)、Serial Clock (SCLK)、Chip Select (CS)。
 
複数のデバイスでラインを共有するI2Cとは異なり、SPIは各スレーブデバイスに専用のCSラインが必要です。この1対多の構造により、SPIは高速で実装が簡単ですが、複数のデバイスが関与する場合、より多くの物理的な配線が必要になる場合があります。
 
<br/><br/><br/><br/>
 
### 7.3.1 ドットマトリックス
---
8x8ドットマトリックスディスプレイは、組み込みシステムでの単純なテキストまたはパターン出力によく使用されます。D3-Gでは、ドットマトリックスモジュールは、MAX7219などのドライバーチップを使用してSPI経由で制御できます。
 
MAX7219は行と列のスキャンを内部で処理するため、マイクロコントローラーはMOSI (DIN)、SCLK、CS (LOAD) のわずか数本のSPI信号を使用してディスプレイ全体を制御できます。接続すると、ユーザー定義のスクリプトまたはライブラリを介してSPI通信を使用してディスプレイを制御できます。
 
#### ステップ 1. ハードウェア要件
- D3-Gボード (x1)
- ドットマトリックス (x1)
- オス-メスジャンパーワイヤー (x4)
- DC 5V電源アダプター (x1)
- USB to TTLシリアルケーブル (x1)
 
#### ステップ 2. 回路例
- ドットマトリックス
    - ドットマトリックスのVCCピンはD3-Gボードの5Vピンに接続します。
    - ドットマトリックスのGNDピンはD3-GボードのGNDピンに接続します。
    - ドットマトリックスのDINピンはD3-Gボードのピン120に接続します。
    - ドットマトリックスのCSピンはD3-Gボードのピン119に接続します。
    - ドットマトリックスのCLKピンはD3-Gボードのピン118に接続します。
 
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20D3-G/Software/dot%20circuit.png"></p>
<p align="center"><strong>図 7.11 D3-Gドットマトリックスモジュール回路図  </strong></p>
 
##### ステップ 2.1 ピンマッピング
次の表はピンマッピングを示しています。
<div align="center">
  <p><strong>表 7.11 D3-Gドットマトリックスのピンマッピング</strong></p>
  <table>
      <tr>
          <th colspan="3">ピン名</th>
          <th>D3-G</th>
          <th>GPIO</th>
      </tr>
      <tr>
          <td colspan="3">VCC</td>
          <td>2</td>
          <td>5V</td>
      </tr>
      <tr>
          <td colspan="3">GND</td>
          <td>6</td>
          <td>GND</td>
      </tr>
      <tr>
          <td colspan="3">DIN</td>
          <td>19</td>
          <td>63</td>
      </tr>
      <tr>
          <td colspan="3">CS</td>
          <td>24</td>
          <td>62</td>
      </tr>
      <tr>
          <td colspan="3">CLK</td>
          <td>23</td>
          <td>61</td>
      </tr>
  </table>
</div>
 
#### ステップ 3. 実行方法
次のPythonスクリプトは、低レベルのfcntl呼び出しを使用して/dev/spidev3.0経由でMAX7219を直接制御する方法を示しています。この方法は、外部SPIライブラリのないデバイスに適しています。
```
#!/usr/bin/env python3
 
import os
import fcntl
import time
from ctypes import Structure, addressof, create_string_buffer, c_uint64, c_uint32, c_uint16, c_uint8
 
SPI_MODE = 0
SPI_SPEED_HZ = 5000000
SPI_BITS_PER_WORD = 8
 
SPI_IOC_RD_MODE = 0x80016b01
SPI_IOC_WR_MODE = 0x40016b01
SPI_IOC_RD_BITS_PER_WORD = 0x80016b03
SPI_IOC_WR_BITS_PER_WORD = 0x40016b03
SPI_IOC_WR_MAX_SPEED_HZ = 0x40046b04
SPI_IOC_MESSAGE_1 = 0x40206b00
 
class spi_ioc_transfer(Structure):
    _fields_ = [
        ("tx_buf", c_uint64),
        ("rx_buf", c_uint64),
        ("len", c_uint32),
        ("speed_hz", c_uint32),
        ("delay_usecs", c_uint16),
        ("bits_per_word", c_uint8),
        ("cs_change", c_uint8),
        ("pad", c_uint32)
    ]
 
def spi_transfer(fd, tx_data):
    tx_buffer = create_string_buffer(bytes(tx_data))
    rx_buffer = create_string_buffer(len(tx_data))
 
    xfer = spi_ioc_transfer(
        tx_buf=addressof(tx_buffer),
        rx_buf=addressof(rx_buffer),
        len=len(tx_data),
        delay_usecs=0,
        speed_hz=SPI_SPEED_HZ,
        bits_per_word=SPI_BITS_PER_WORD,
        cs_change=0
    )
 
    fcntl.ioctl(fd, SPI_IOC_MESSAGE_1, xfer)
 
    return list(rx_buffer)
 
def MAX7219_write(fd, address, data):
    spi_transfer(fd, [address, data])
 
def MAX7219_init(fd):
    MAX7219_write(fd, 0x09, 0x00)  # Decoding mode: none
    MAX7219_write(fd, 0x0A, 0x03)  # Intensity: 3 (range 0-15)
    MAX7219_write(fd, 0x0B, 0x07)  # Scan limit: 8 LEDs
    MAX7219_write(fd, 0x0C, 0x01)  # Power on
    MAX7219_write(fd, 0x0F, 0x00)  # Display test: off
 
NUMBER_CODE = [
    [0x3C, 0x42, 0x42, 0x42, 0x42, 0x42, 0x42, 0x3C],  # 0
    [0x10, 0x30, 0x50, 0x10, 0x10, 0x10, 0x10, 0x7C],  # 1
    [0x3E, 0x02, 0x02, 0x3E, 0x20, 0x20, 0x3E, 0x00],  # 2
    [0x00, 0x7C, 0x04, 0x04, 0x7C, 0x04, 0x04, 0x7C],  # 3
    [0x08, 0x18, 0x28, 0x48, 0xFE, 0x08, 0x08, 0x08],  # 4
    [0x3C, 0x20, 0x20, 0x3C, 0x04, 0x04, 0x3C, 0x00],  # 5
    [0x3C, 0x20, 0x20, 0x3C, 0x24, 0x24, 0x3C, 0x00],  # 6
    [0x3E, 0x22, 0x04, 0x08, 0x08, 0x08, 0x08, 0x08],  # 7
    [0x00, 0x3E, 0x22, 0x22, 0x3E, 0x22, 0x22, 0x3E],  # 8
    [0x3E, 0x22, 0x22, 0x3E, 0x02, 0x02, 0x02, 0x3E]   # 9
]
 
ALPHABET_CODE = {
    'A': [0x08, 0x14, 0x22, 0x3E, 0x22, 0x22, 0x22, 0x22],
    'B': [0x3C, 0x22, 0x22, 0x3E, 0x22, 0x22, 0x3C, 0x00],
    'C': [0x3C, 0x40, 0x40, 0x40, 0x40, 0x40, 0x3C, 0x00],
    'D': [0x7C, 0x42, 0x42, 0x42, 0x42, 0x42, 0x7C, 0x00],
    'E': [0x7C, 0x40, 0x40, 0x7C, 0x40, 0x40, 0x40, 0x7C],
    'F': [0x7C, 0x40, 0x40, 0x7C, 0x40, 0x40, 0x40, 0x40],
    'G': [0x3C, 0x40, 0x40, 0x40, 0x40, 0x44, 0x44, 0x3C],
    'H': [0x44, 0x44, 0x44, 0x7C, 0x44, 0x44, 0x44, 0x44],
    'I': [0x7C, 0x10, 0x10, 0x10, 0x10, 0x10, 0x10, 0x7C],
    'J': [0x3C, 0x08, 0x08, 0x08, 0x08, 0x08, 0x48, 0x30],
    'K': [0x40, 0x40, 0x40, 0x40, 0x40, 0x40, 0x40, 0x7C],
    'L': [0x40, 0x40, 0x40, 0x40, 0x40, 0x40, 0x40, 0x7C],
    'M': [0x00, 0x42, 0x62, 0x52, 0x4A, 0x46, 0x42, 0x00],
    'N': [0x00, 0x42, 0x62, 0x52, 0x4A, 0x46, 0x42, 0x00],
    'O': [0x3C, 0x42, 0x42, 0x42, 0x42, 0x42, 0x42, 0x3C],
    'P': [0x3C, 0x42, 0x42, 0x3E, 0x02, 0x02, 0x02, 0x3E],
    'Q': [0x3C, 0x42, 0x42, 0x42, 0x42, 0x42, 0x42, 0x3C],
    'R': [0x08, 0x14, 0x22, 0x3E, 0x22, 0x22, 0x22, 0x22],
    'S': [0x7C, 0x40, 0x40, 0x7C, 0x40, 0x40, 0x40, 0x7C],
    'T': [0x7C, 0x10, 0x10, 0x10, 0x10, 0x10, 0x10, 0x7C],
    'U': [0x3C, 0x08, 0x08, 0x08, 0x08, 0x08, 0x48, 0x30],
    'V': [0x40, 0x40, 0x40, 0x40, 0x40, 0x40, 0x40, 0x7C],
    'W': [0x00, 0x41, 0x41, 0x41, 0x49, 0x2a, 0x2a, 0x14],
    'X': [0x40, 0x40, 0x40, 0x40, 0x40, 0x40, 0x40, 0x7C],
    'Y': [0x7C, 0x40, 0x40, 0x7C, 0x40, 0x40, 0x40, 0x7C],
    'Z': [0x7C, 0x40, 0x40, 0x7C, 0x40, 0x40, 0x40, 0x7C],
    'Smile': [0x3c, 0x42, 0xa5, 0x81, 0xa5, 0x99, 0x42, 0x3c],
    'dance0': [0x10, 0x28, 0x10, 0x10, 0xfe, 0x10, 0x28, 0x28],
    'dance1': [0x10, 0x28, 0x92, 0x54, 0x38, 0x10, 0x28, 0x44],
    'angry': [0x00, 0x00, 0xe7, 0x00, 0x00, 0x00, 0x3c, 0x00],
    'Good': [0x30, 0x30, 0x30, 0x3c, 0x32, 0x3c, 0x32, 0x3c]
}
 
 
def main():
    print('*' * 50)
    fd = os.open('/dev/spidev3.0', os.O_RDWR)
 
    fcntl.ioctl(fd, SPI_IOC_RD_BITS_PER_WORD, bytes([SPI_BITS_PER_WORD]))
    fcntl.ioctl(fd, SPI_IOC_WR_BITS_PER_WORD, bytes([SPI_BITS_PER_WORD]))
    fcntl.ioctl(fd, SPI_IOC_WR_MODE, bytes([SPI_MODE]))
    fcntl.ioctl(fd, SPI_IOC_WR_MAX_SPEED_HZ, SPI_SPEED_HZ.to_bytes(4, byteorder='little'))
 
    MAX7219_init(fd)
 
    try:
        while True:
            input_str = input("Enter a number, an uppercase letter (0-9, A-Z), 'Smile', 'Dance', 'Angry', 'Good', 'Nice', 'Emotion': ")
            if input_str.isdigit() and 0 <= int(input_str) <= 9:
                num = int(input_str)
                for col in range(8):
                    MAX7219_write(fd, col + 1, NUMBER_CODE[num][col])
                    time.sleep(0.1)
            elif input_str.isalpha() and input_str.isupper() and len(input_str) == 1:
                char = input_str
                for col in range(8):
                    MAX7219_write(fd, col + 1, ALPHABET_CODE[char][col])
                    time.sleep(0.1)
            elif input_str == 'Smile':
                smile_pattern = ALPHABET_CODE['Smile']
                for col in range(8):
                    MAX7219_write(fd, col + 1, smile_pattern[col])
                    time.sleep(0.1)
            elif input_str == 'Dance': 
                for _ in range(10):
                    for col in range(8):
                        MAX7219_write(fd, col + 1, ALPHABET_CODE['dance0'][col])
                    time.sleep(0.5)
                    for col in range(8):
                        MAX7219_write(fd, col + 1, ALPHABET_CODE['dance1'][col])
                    time.sleep(0.5)
            elif input_str == 'Angry': 
                angry_pattern = ALPHABET_CODE['angry']
                for col in range(8):
                    MAX7219_write(fd, col + 1, angry_pattern[col])
                    time.sleep(0.1)
            elif input_str == 'Good':
                good_pattern = ALPHABET_CODE['Good']
                for col in range(8):
                    MAX7219_write(fd, col + 1, good_pattern[col])
                    time.sleep(0.1)
            elif input_str == 'Nice':
                for _ in range(3):
                    for col in range(8):
                        MAX7219_write(fd, col + 1, ALPHABET_CODE['N'][col])
                    time.sleep(0.5)
                    for col in range(8):
                        MAX7219_write(fd, col + 1, ALPHABET_CODE['I'][col])
                    time.sleep(0.5)
                    for col in range(8):
                        MAX7219_write(fd, col + 1, ALPHABET_CODE['C'][col])
                    time.sleep(0.5)
                    for col in range(8):
                        MAX7219_write(fd, col + 1, ALPHABET_CODE['E'][col])
                    time.sleep(0.5)
            elif input_str == 'Emotion':
                for _ in range (6):
                    for col in range(8):
                        MAX7219_write(fd, col + 1, ALPHABET_CODE['Smile'][col])
                    time.sleep(0.5)
                    for col in range(8):
                        MAX7219_write(fd, col + 1, ALPHABET_CODE['angry'][col])
                    time.sleep(0.5)
            else:
                   print("Invalid input. Please enter a number (0-9), an uppercase letter (A-Z), 'Smile', 'Dance', 'Angry', 'Good', 'Nice', 'Emotion'.")
 
    except KeyboardInterrupt:
        os.close(fd)
    finally:
        os.close(fd)
 
if __name__ == "__main__":
    main()
 
#### ステップ 4. 実行結果
次のコマンドでコードを実行します。
```
$ python3 dot_matrix_test.py
```
このスクリプトは、SPI接続されたMAX7219ドットマトリックスディスプレイを初期化し、値の入力を求めます。入力に応じて、特定のパターンが8x8 LEDマトリックスに表示されます。
 
スクリプトを実行すると、次のように表示されます。
```
Enter a number, an uppercase letter (0-9, A-Z), 'Smile', 'Dance', 'Angry', 'Good', 'Nice', 'Emotion':
```
例：
- Aを入力すると、文字Aが表示されます。
- Smileを入力すると、スマイリーフェイスパターンが表示されます。
- Danceを入力すると、交互のダンスアニメーションがトリガーされます。
- Niceを入力すると、文字N-I-C-Eが順番にアニメーション表示されます。
 
スクリプトを停止するには、**[Ctrl+C]** を押します。
終了すると、SPIデバイスは安全に閉じられ、LEDマトリックスの更新が停止します。
 
**注**: /dev/spidev3.0が存在し、配線がピンマッピングテーブルと一致していることを確認してください。また、MAX7219モジュールには安定した5V電源を供給してください。
 
<br/><br/><br/><br/>
 
## 7.4 PWM
---
パルス幅変調 (PWM) は、パルス信号の幅を変えることで、LED、モーター、ブザーなどのデバイスを制御するために使用されます。D3-Gは、Linuxのsysfsインターフェースを介してPWMをサポートしています。
 
### 7.4.1 LED輝度制御
---
この例では、D3-GでPWMを使用してLEDの輝度を制御する方法を示します。
 
#### ステップ 1. ハードウェア要件
- D3-Gボード (x1)
- LED (x1)
- オス-メスジャンパーワイヤー (x2)
- ブレッドボード
- DC 5V電源アダプター (x1)
- USB to TTLシリアルケーブル (x1)
 
#### ステップ 2. 回路例
- LED
    - LEDの (+) ピンはD3-Gボードのピン89に接続します。
    - LEDの (-) ピンはD3-GボードのGNDピンに接続します。
 
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20D3-G/Software/led.png"></p>
<p align="center"><strong>図 7.12 D3-G LED回路図  </strong></p>
 
##### ステップ 2.1 ピンマッピング
次の表はピンマッピングを示しています。
 
<div align="center">
  <p><strong>表 7.12 D3-G LEDのピンマッピング</strong></p>
  <table>
      <tr>
          <th colspan="3">ピン名</th>
          <th>D3-G</th>
          <th>GPIO</th>
      </tr>
      <tr>
          <td colspan="3">( + )</td>
          <td>12</td>
          <td>89</td>
      </tr>
      <tr>
          <td colspan="3">( – )</td>
          <td>14</td>
          <td>GND</td>
      </tr>
  </table>
</div>
 
#### ステップ 3. 実行方法
D3-GボードのGPIO89に接続されたLED (PWM) を操作するには、次のコードを実行します。
```
import time
 
PWM_CHIP = "pwmchip0"
PWM_CHANNEL = "pwm0"
PWM_PATH = f"/sys/class/pwm/{PWM_CHIP}/{PWM_CHANNEL}"
EXPORT_PATH = f"/sys/class/pwm/{PWM_CHIP}/export"
UNEXPORT_PATH = f"/sys/class/pwm/{PWM_CHIP}/unexport"
 
PERIOD = 1000000  # 1ms = 1kHz
STEP = 10000
SLEEP = 0.01
 
def pwm_setup():
    try:
        with open(EXPORT_PATH, "w") as f:
            f.write("0")
    except Exception:
        pass  # Already exported
    time.sleep(0.1)

    with open(f"{PWM_PATH}/period", "w") as f:
        f.write(str(PERIOD))
        f.flush()

    with open(f"{PWM_PATH}/enable", "w") as f:
        f.write("1")
        f.flush()

def pwm_cleanup():
    try:
        with open(f"{PWM_PATH}/enable", "w") as f:
            f.write("0")
            f.flush()
        with open(UNEXPORT_PATH, "w") as f:
            f.write("0")
    except Exception as e:
        print("PWM cleanup failed:", e)

try:
    pwm_setup()
    print("Starting LED PWM control (press Ctrl+C to stop)")

    while True:
        for duty in range(0, PERIOD, STEP):
            with open(f"{PWM_PATH}/duty_cycle", "w") as f:
                f.write(str(min(duty, PERIOD - 1)))
                f.flush()
            time.sleep(SLEEP)

        for duty in range(PERIOD, 0, -STEP):
            with open(f"{PWM_PATH}/duty_cycle", "w") as f:
                f.write(str(min(duty, PERIOD - 1)))
                f.flush()
            time.sleep(SLEEP)

except KeyboardInterrupt:
    print("\nStopped by user.")

finally:
    pwm_cleanup()
    print("PWM disabled and cleaned up.")
```
 
#### ステップ 4. 実行結果
次のコマンドでコードを実行します。
```
$ python3 led_pwm.py
```
このスクリプトは、LEDピンでPWMを初期化し、LEDの輝度を継続的に上げ下げします。
 
スクリプトを実行すると、次のような出力が表示されます。
```
Starting LED PWM control (press Ctrl+C to stop)
```
LEDは徐々に明るくなり、その後暗くなることを繰り返し、「呼吸」効果をシミュレートします。
 
スクリプトを停止するには、**[Ctrl+C]** を押します。
 
**注**: PWMチャネルがまだ使用されていないこと、およびD3-Gが選択したGPIOでハードウェアPWMをサポートしていることを確認してください。PWMがアクティブにならない場合は、/sys/class/pwm/ でexport、period、duty_cycleの設定を確認してください。
 
<br/><br/><br/><br/>
 
### 7.4.2 ミニサーボモーター
---
ミニサーボモーターは、GPIOを介したパルス幅変調 (PWM) 信号に基づいて正確な角度移動を制御するために使用できます。
このセクションでは、D3-Gを使用してミニサーボモーターを接続して制御する方法を示します。
 
#### ステップ 1. ハードウェア要件
- D3-Gボード (x1)
- サーボモーター (x1)
- オス-メスジャンパーワイヤー (x3)
- DC 5V電源アダプター (x1)
- USB to TTLシリアルケーブル (x1)
 
#### ステップ 2. 回路例
- サーボモーター
    - サーボモーターのVCCピンはD3-Gボードの5Vに接続します。
    - サーボモーターのGNDピンはD3-GボードのGNDに接続します。
    - サーボモーターのSIGピンはD3-Gボードのピン89に接続します。
 
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20D3-G/Software/motor_circuit.png"p>
<p align="center"><strong>図 7.13 D3-Gサーボモーター回路図  </strong></p>
 
##### ステップ 2.1 ピンマッピング
次の表はピンマッピングを示しています。
 
<div align="center">
  <p><strong>表 7.13 D3-Gサーボモーターのピンマッピング</strong></p>
  <table>
      <tr>
          <th colspan="3">ピン名</th>
          <th>D3-G</th>
          <th>GPIO</th>
      </tr>
      <tr>
          <td colspan="3">VCC</td>
          <td>2</td>
          <td>5V</td>
      </tr>
      <tr>
          <td colspan="3">GND</td>
          <td>20</td>
          <td>GND</td>
      </tr>
      <tr>
          <td colspan="3">SIG</td>
          <td>12</td>
          <td>89</td>
      </tr>
  </table>
</div>

#### ステップ 3. 実行方法
次のPythonスクリプトは、D3-Gのsysfsインターフェースを介してPWMを使用してミニサーボモーターを直接制御する方法を示しています。この方法は外部ライブラリを必要とせず、角度ベースの位置決めをきめ細かく制御できます。
```
import time
import os

PWM_CHIP = "pwmchip0"
PWM_CHANNEL = "pwm0"
PWM_PATH = f"/sys/class/pwm/{PWM_CHIP}/{PWM_CHANNEL}"
EXPORT_PATH = f"/sys/class/pwm/{PWM_CHIP}/export"
UNEXPORT_PATH = f"/sys/class/pwm/{PWM_CHIP}/unexport"

PERIOD = 20_000_000  # 20ms (50Hz)

def angle_to_duty(angle):
    pulse_width = 1_000_000 + (angle / 180) * 1_000_000
    return int(pulse_width)

def pwm_setup():
    if not os.path.exists(PWM_PATH):
        with open(EXPORT_PATH, "w") as f:
            f.write("0")
        time.sleep(0.1)
    with open(f"{PWM_PATH}/period", "w") as f:
        f.write(str(PERIOD))
    with open(f"{PWM_PATH}/enable", "w") as f:
        f.write("1")

def pwm_set_angle(angle):
    duty = angle_to_duty(angle)
    with open(f"{PWM_PATH}/duty_cycle", "w") as f:
        f.write(str(duty))

def pwm_cleanup():
    try:
        with open(f"{PWM_PATH}/enable", "w") as f:
            f.write("0")
        with open(UNEXPORT_PATH, "w") as f:
            f.write("0")
    except Exception as e:
        print("PWM cleanup failed:", e)

if __name__ == "__main__":
    pwm_setup()

    try:
        while True:
            user_input = input("Enter 1 (CW) or 0 (CCW), q to quit: ").strip()
            if user_input == 'q':
                break
            elif user_input == '1':
                pwm_set_angle(180)  
                time.sleep(0.5)
            elif user_input == '0':
                pwm_set_angle(0)   
                time.sleep(0.5)
            else:
                print("Invalid input. Use 0, 1, or q.")
    except KeyboardInterrupt:
        print("\nInterrupted by user.")
    finally:
        pwm_cleanup()
        print("PWM cleaned up.")
```

#### ステップ 4. 実行結果
次のコマンドでコードを実行します。
```
$ python3 motor_test.py
```
このスクリプトは、PWMを使用して、ターゲット角度に基づいてデューティサイクルを調整することにより、ミニサーボモーターを制御します。
実行すると、次のように求められます。
```
Enter 1 (CW) or 0 (CCW), q to quit:
```
1を入力するとサーボが時計回りに180°回転し、0を入力するとサーボが反時計回りに0°回転します。これは何度でも繰り返すことができます。
 
スクリプトを停止するには、**[q]** を入力するか、**[Ctrl+C]** を押します。その後、スクリプトはPWMチャネルを無効にしてエクスポートを解除します。
 
**注**: サーボモーターが50 HzのPWM信号をサポートし、安全な動作のために1 ms〜2 msのデューティパルス範囲内で動作することを確認してください。
