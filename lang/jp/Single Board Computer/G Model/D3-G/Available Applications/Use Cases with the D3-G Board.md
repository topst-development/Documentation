# 1. はじめに 
---
本書では、D3-G の使用例について説明します。   
本書には、以下の情報が含まれます。
- 入力デバイス
  - キーボード 
  - マウス
- ビデオ出力
- カメラ接続
  - MIPI CSI
  - USB ウェブカメラ
- ストレージ接続
  - SD カード
  - SATA HDD
  - NVMe M.2 SSD
  - USB ストレージ
- イーサネット接続
- 40 ピン GPIO ヘッダ
  - 使用可能なセンサーおよびデバイス

<br/><br/><br/><br/>


# 2. 入力デバイス
---
D3-G は、入力デバイスを接続するための USB ポートを 2 つサポートします。
USB 2.0 Type-A ポート 1 つと USB 3.0 Type-A ポート 1 つを備えており、マウスやキーボードを接続して D3-G を直接操作できます。 

**注意**: D3-G の USB Type-C ポートはファームウェアのダウンロード専用であり、入力デバイスの接続には使用できません。

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20D3-G/Software/input%20device.png" width="500"></p>
<p align="center"><strong>図 2.1 D3-G ボードへの入力デバイスの接続 </strong></p><br/><br/><br/><br/>


# 3. ビデオ出力
---
D3-G は、DisplayPort (DP) 出力でのみ FHD モニターをサポートします。
また、デイジーチェーン構成によるマルチディスプレイ出力にも対応しており、最大 2 台の FHD モニターと 1 台の HD モニターを同時に接続できます。

**注意**: HDMI を使用するには、別途アクティブコンバータアダプタが必要です。
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20D3-G/Software/monitor.png" width="500"></p>
<p align="center"><strong>図 3.1 D3-G ボードへのモニターの接続 </strong></p>

<br/><br/><br/><br/>

# 4. カメラの接続
---
D3-G はカメラ機能をサポートしており、さまざまなアプリケーションに柔軟に対応します。
プロジェクトの要件に応じて、MIPI CSI カメラまたは USB ウェブカメラのいずれかを接続できます。

<br/><br/><br/>

## 4.1 USB ウェブカメラ
---
D3-G は、最大 Full HD (FHD) 解像度の USB ウェブカメラをサポートします。
以下の手順でウェブカメラをテストできます。


#### ステップ 1. USB カメラをボードの USB ポートに接続します。
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20D3-G/Software/webcam.png" width="400"></p>
<p align="center"><strong>図 4.1 D3-G ボードへのウェブカメラの接続</strong></p><br/>

#### ステップ 2. 入力デバイス（マウスとキーボード）とモニターを D3-G に接続します。
   
#### ステップ 3. D3-G を起動します。

#### ステップ 4. 利用可能な /dev/video デバイスを確認します。
```
$ ls /dev/video*
```

#### ステップ 5. OpenCV（または vutils）を使用してビデオ出力を確認します。
```
$ touch webcam.py
$ chmod a+x webcam.py
```
```
# You can edit the script file using vim or nano editor
# This is a Python camera application using OpenCV
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

    # pressed 'q' key, escape
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
```
```
# Run the script
$ python3 webcam.py
```

<br/><br/><br/>

## 4.2 MIPI CSI
---
CSI は Camera Serial Interface の略で、カメラモジュールをホストプロセッサに接続するために MIPI Alliance が定義した標準インターフェースです。
これにより、カメラからプロセッサへ画像データを高速かつ低消費電力で伝送できます。

D3-G は 2 つの MIPI CSI チャンネル（ch0 と ch1）を備えており、Flat Flexible Cable (FFC) 接続に対応したカメラモジュールを取り付けることができます。
現在、D3-G は ArduCam (5 MP) と Raspberry Pi v1 Camera (5 MP) のモジュールのみをサポートしています。 

**注意**: 現在、D3-G は CSI チャンネル 0 と CSI チャンネル 1 の同時使用をサポートしていません。

<br/><br/>

### 4.2.1 ArduCam
ArduCam は、組み込みシステムや IoT アプリケーション向けに設計された汎用性の高いカメラモジュールです。MIPI CSI を含むさまざまなイメージセンサーやインターフェースをサポートしており、D3-G のような開発ボードへの統合に適しています。
D3-G がサポートする 5 MP の ArduCam モジュールは十分な画質を提供し、基本的なコンピュータビジョン処理、ストリーミング、カメラベースの AI アプリケーションで広く使用されています。FFC ケーブルに対応しているため、D3-G ボードの CSI インターフェースに簡単に接続できます。 

ArduCam モジュールの仕様は次のとおりです。

| 仕様                     | 説明                                 |
| ------------------------ | ------------------------------------------- |
| センサー                   | OV5647 (500 万画素)                        |
| 解像度                    | 2592 × 1944 (Full 5 MP)                      |
| 対応出力フォーマット | RAW, YUV, JPEG (センサーにより異なる)           |
| インターフェース            | MIPI CSI-2                                  |
| フレームレート               | 1080p で最大 30fps、720p で 60fps         |
| レンズマウント               | 固定焦点レンズ (標準)                 |
| 視野角 (FOV)              | 約 54° – 70°（モデルによって異なります）            |
| 接続タイプ                 | Flat Flexible Cable (FFC)                   |
| 動作電圧        | 3.3V (代表値)                              |
| 形状              | 小型 PCB、約 25 mm x 24 mm                   |
| 互換性                    | Raspberry Pi および D3-G（MIPI CSI-2 ポート経由）  |
| 追加機能      | 低消費電力、プラグアンドプレイモジュール |


次の手順に従って ArduCam をテストできます。
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20D3-G/Software/arducam.png" width="400"></p>
<p align="center"><strong>図 4.2 ArduCam </strong></p><br/>

#### ステップ 1. 図 4.3 のように、ArduCam を D3-G ボードの MIPI CSI 0 に接続します。
 
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20D3-G/Software/rasp%20v1%20cam%20to%20d3g.png" width="500"></p>
<p align="center"><strong>図 4.3 D3-G ボードへの ArduCam の接続</strong></p> <br/>

#### ステップ 2. ArduCam を接続した後、D3-G ボード上で次の GStreamer コマンドを使用してビデオストリームを確認できます。
```
$ gst-launch-1.0 v4l2src device=/dev/video0 io-mode=2 ! video/x-raw,format=NV12,width=1920,height=1280,framerate=30/1 ! videoconvert ! waylandsink fullscreen=true
```

このコマンドは、CSI に接続された ArduCam から映像をキャプチャし、表示用に変換して、Wayland ディスプレイサーバーを使用して全画面モードで表示します。  
コマンドを実行する前に、カメラモジュールがしっかりと接続されていることを確認してください。映像が表示されない場合は、ケーブルの接続を確認し、/dev/video0 がシステムで正しく認識されているかを確認してください。

<br/><br/>

### 4.2.2 Raspberry Pi v1 Camera
Raspberry Pi v1 Camera Module は、Raspberry Pi Foundation が開発した小型の 5 MP カメラです。OmniVision OV5647 イメージセンサーをベースとしており、Flat Flexible Cable (FFC) を使用して MIPI CSI-2 インターフェース経由でホストボードに接続します。

もともと Raspberry Pi シリーズ向けに設計されたモジュールですが、D3-G とも互換性があり、画像キャプチャ、動画録画、コンピュータビジョンプロジェクトなどの基本的なカメラアプリケーションに適した選択肢です。

Raspberry Pi v1 Camera モジュールの仕様は次のとおりです。

| 仕様                | 説明                              |
| ------------------- | ---------------------------------------- |
| センサー              | OmniVision OV5647                        |
| 解像度          | 2592 × 1944 (5 MP)                        |
| 出力フォーマット      | RAW, YUV, JPEG                           |
| インターフェース       | MIPI CSI-2                               |
| フレームレート          | 1080p30, 720p60, VGA90                   |
| レンズ                | 固定焦点                              |
| 画角 (FOV) | 最大 54°                                     |
| ケーブル種類          | FFC (15 ピン)                             |
| ボード寸法    | 25 mm x 24 mm                              |
| 互換性               | Raspberry Pi および D3-G（MIPI CSI-2 ポート経由） |

次の手順に従って Raspberry Pi v1 カメラをテストできます。

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20D3-G/Software/rasp%20v1%20cam.jpg" width="400"></p>
<p align="center"><strong>図 4.4. Raspberry Pi v1 Camera </strong></p><br/>

#### ステップ 1. 図 4.5 のように、Raspberry Pi v1 カメラを D3-G ボードの MIPI CSI 1 に接続します。
 
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20D3-G/Software/rasp%20v1%20cam%20to%20d3g.png" width="500"></p>
<p align="center"><strong>図 4.5 D3-G ボードへの Raspberry Pi v1 Camera の接続</strong></p> <br/>

#### ステップ 2. Raspberry Pi カメラを接続した後、D3-G 上で次の GStreamer コマンドを使用してビデオストリームを確認できます:
```
$ gst-launch-1.0 v4l2src device=/dev/video0 io-mode=2 ! video/x-raw,format=NV12,width=1920,height=1280,framerate=30/1 ! videoconvert ! waylandsink fullscreen=true
```

このコマンドは、CSI で接続された Raspberry Pi カメラからビデオをキャプチャし、表示用に変換して、Wayland ディスプレイサーバーを使用して全画面モードでレンダリングします。  
コマンドを実行する前に、カメラモジュールがしっかりと接続されていることを確認してください。映像が表示されない場合は、ケーブルの接続を確認し、/dev/video0 がシステムで正しく認識されているかを確認してください。

<br/><br/><br/><br/>

# 5. ストレージの接続
---
この章では、D3-G をさまざまなストレージデバイスに接続する方法について説明します。サポートされるストレージオプションには、USB ドライブ、SD カード、および PCIe 経由の外部ストレージがあります。

<br/><br/><br/>

## 5.1 USB ドライブ
---
D3-G は、USB 2.0 および USB 3.0 Type-A ポートを介して USB ストレージデバイスをサポートします。
USB ドライブを接続するには:

### ステップ 1. D3-G の使用可能な USB Type-A ポートのいずれかに USB ドライブを差し込みます。
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20D3-G/Software/usb%20storage%20connection%20with%20d3g.png" width="500"></p>
<p align="center"><strong>図 5.1 D3-G ボードへの USB ストレージの接続</strong></p> <br/>

### ステップ 2. 接続後、デバイスはシステムの状態に応じて通常 /dev/sda1、/dev/sdb1 などとして認識されます。

<br/>

### ステップ 3. 次のコマンドを使用して USB ドライブを手動でマウントできます:
   ```
   $ sudo mount /dev/sda1 /mnt
   ```

<br/><br/><br/>

## 5.2 SD カード
---
D3-G には、標準の SDHC/SDXC カードをサポートする microSD カードスロットが搭載されています。
D3-G で SD カードを使用するには:

<br/>

### ステップ 1. D3-G ボードの SD カードスロットに microSD カードを挿入します。
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20D3-G/Software/sd%20card%20connect%20with%20d3g.png" width="500"></p>
<p align="center"><strong>図 5.2 D3-G ボードへの SD カードの接続</strong></p> <br/>

### ステップ 2. 挿入後、システムは通常、SD カードを /dev/mmcblk1p1 または同様のデバイスノードとして認識します。
  ```
  $ ls /dev/mmcblk*
  ```
<br/>

### ステップ 3. SD カードを手動でマウントするには、次のコマンドを使用します:
```
$ sudo mount /dev/mmcblk1p1 /mnt 
```
### ステップ 4. マウント後、/mnt ディレクトリで SD カードの内容にアクセスできます。

<br/><br/><br/>

## 5.3 SATA HDD
---

D3-G は、互換性のある SATA コントローラを使用して、PCIe スロット経由で HDD や SSD などの SATA ストレージデバイスを使用することをサポートします。

<br/>

#### ステップ 1. PCIe to SATA モジュールの接続

PCIe 経由で D3-G に SATA HDD を使用するには、まず PCIe-to-SATA アダプタモジュールを D3-G の PCIe スロットに接続する必要があります。

次に、HDD を SATA モジュールに接続し、HDD が外部 12V 電源から給電されていることを確認してください。

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20D3-G/Software/sata.png" width="500"></p>
<p align="center"><strong>図 5.3 D3-G ボードの PCIe への SATA モジュールの接続 </strong></p><br/>

#### ステップ 2. D3-G の起動 
D3-G の起動後、起動ログを確認して、PCIe デバイスがシステムに認識されていることを確認してください。
PCIe リンクが正常に確立されたことを示す **telechips-pcie: Link up** などのメッセージを探してください。

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

#### ステップ 3. SATA HDD の認識確認
```
root@TOPST:~# lspci
00:00.0 PCI bridge: Synopsys, Inc. Device 8040 (rev 01)
01:00.0 SATA controller: ASMedia Technology Inc. Device 1064 (rev 02)
```
**lspci** コマンドが使用できない場合は、次のコマンドを使用して pciutils をインストールしてください。

```
$ sudo apt-get install pciutils
```

<br/>

#### ステップ 4. SATA HDD のマウント
```
$ fdisk /dev/sda
Welcome to fdisk (util-linux 2.37.4).
Changes will remain in memory only, until you decide to write them.
Be careful before using the write command.

Command (m for help): 
```

fdisk のプロンプトで次のキーを順に入力してください。

- o — 新しい空の DOS パーティションテーブルを作成する (任意、既存のテーブルを消去)

- n — 新しいパーティションを追加する

- p — 基本パーティションを選択する

- 1 — パーティション番号を 1 に設定する

- Enter キーを押す — 既定の開始セクタを使用する

- Enter キーを押す — 既定の終了セクタを使用する (ディスク全体を使用)

- w — パーティションテーブルを書き込んで終了します

```
$ mkfs.ext4 /dev/sda1

$ mkdir -p /mnt/sata

$ mount /dev/sda1 /mnt/sata
```

<br/>

#### ステップ 5. 実行結果
この出力は、SATA SSD パーティション (/dev/sdb1) が ext4 ファイルシステムで正常にフォーマットされ、/mnt/sata にマウントされたことを示しています。
**df -h** コマンドは、デバイスが認識され、システムで使用可能になったことを示します。

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
D3-G は、PCIe スロットを介した NVMe M.2 SSD の直接接続をサポートします。
<br/>

#### 手順 1. SSD を接続する
- NVMe SSD (M.2 PCIe): NVMe M.2 SSD を D3-G の PCIe スロットに挿入します。 

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20D3-G/Software/M.2%20SSD%20connection.png" width="600"></p>
<p align="center"><strong>図 5.4 D3-G ボードへの NVMe M.2 SSD の接続</strong></p><br/>

#### ステップ 2. D3-G の起動
**reboot** コマンドを実行した後、起動ログを確認し、PCIe デバイスがシステムに認識されていることを確認してください。
PCIe リンクが正常に確立されたことを示す **telechips-pcie: Link up** などのメッセージを探してください。

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

#### 手順 3. SSD の認識を確認する
```
root@TOPST:~# lspci
00:00.0 PCI bridge: Synopsys, Inc. Device 8040 (rev 01)
01:00.0 Non-Volatile memory controller: Solid State Storage Technology Corporation Device 1007 (rev 03)
```
**lspci** コマンドが使用できない場合は、次のコマンドを使用して pciutils をインストールしてください。

```
$ sudo apt-get install pciutils
```

<br/>

#### 手順 4. SSD をマウントする
```
$ fdisk /dev/nvme0n1
Welcome to fdisk (util-linux 2.37.4).
Changes will remain in memory only, until you decide to write them.
Be careful before using the write command.

Command (m for help): 
```

fdisk のプロンプトで次のキーを順に入力してください。

- o — 新しい空の DOS パーティションテーブルを作成する (任意、既存のテーブルを消去)

- n — 新しいパーティションを追加する

- p — 基本パーティションを選択する

- 1 — パーティション番号を 1 に設定する

- Enter キーを押す — 既定の開始セクタを使用する

- Enter キーを押す — 既定の終了セクタを使用する (ディスク全体を使用)

- w — パーティションテーブルを書き込んで終了します

```
$ mkfs.ext4 /dev/nvme0n1p1

$ mkdir -p /mnt/nvme

$ mount /dev/nvme0n1p1 /mnt/nvme
```

<br/>

#### ステップ 5. 実行結果
この出力は、NVMe SSD デバイス (/dev/nvme0n1p1) がシステムによって正常に検出され、/mnt/nvme にマウントされたことを示しています。
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
D3-G は、オンボードの J2C イーサネットポートを介してイーサネット接続をサポートします。これにより、D3-G は標準の TCP/IP プロトコルを使用してローカルネットワークやインターネットと通信できます。イーサネットは、リモートアクセス、データストリーミング、ソフトウェア更新を必要とするアプリケーションを導入する際に一般的に使用されます。

<br/><br/><br/>

## 6.1 ルーター経由のネットワーク接続
---
この方法では、標準のルーターを使用して D3-G をローカルネットワークに接続します。D3-G は DHCP により自動的に IP アドレスを取得するか、静的 IP アドレスを設定することができます。

<br/><br/>

### 6.1.1 ネットワーク設定ファイルの作成

1. DHCP による動的 IP
ネットワークに DHCP サーバー (ルーターや ICS を有効にした Windows PC など) がある場合、ファイルを編集する必要はありません。イーサネットケーブルを接続すると、システムが自動的に IP アドレスを取得します。

ケーブルを差し込むだけで、すぐにネットワークを使用できます。第 6.1.3 章「ネットワーク接続の確認」に進んでください。

2. 静的 IP の設定
静的 IP アドレスを割り当てたい場合 (例: PC と直接接続する場合や DHCP サーバーが利用できない場合) は、同じファイルを次の内容で編集してください。
```
$ vi /etc/systemd/network/20-wired.network

[Match]
Name=eth0

[Network]
Address=192.168.137.2/24
Gateway=192.168.137.1
DNS=8.8.8.8
```

この設定では、IP アドレスを 192.168.137.2 に設定し、192.168.137.1 をゲートウェイ (Windows ICS で一般的) として使用し、Google DNS を構成します。

<br/><br/>

### 6.1.2 ネットワークサービスの再起動
systemd-networkd サービスを再起動して、新しいネットワーク設定を適用してください。

```
sudo systemctl restart systemd-networkd
```

<br/><br/>

### 6.1.3 ネットワーク接続の確認
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20D3-G/Software/router%20connection.png"width="500"></p>
<p align="center"><strong>図 6.1 ルーター経由のネットワーク接続</strong></p>

Google のパブリック DNS サーバーに ping を送信して、インターネット接続をテストしてください。

```
$ ping 8.8.8.8
PING 8.8.8.8 (8.8.8.8): 56 data bytes
64 bytes from 8.8.8.8: seq=0 ttl=113 time=30.208 ms
64 bytes from 8.8.8.8: seq=1 ttl=113 time=38.143 ms
64 bytes from 8.8.8.8: seq=2 ttl=113 time=30.969 ms
64 bytes from 8.8.8.8: seq=3 ttl=113 time=33.586 ms
 
```

<br/><br/><br/>

## 6.2 ホスト PC とのネットワーク共有
---
Windows オペレーティングシステムで利用できるインターネット接続の共有 (ICS) 機能を利用すると、ルーターを使用せずに PC のインターネット接続を D3-G と共有できます。

<br/><br/>

### 6.2.1 ホスト PC のネットワーク設定
- コントロールパネル → ネットワークとインターネット → ネットワーク接続 → イーサネットの設定
 
1. インターネットに接続されているネットワークアダプター (例: Wi-Fi) を見つけて右クリックし、**プロパティ** を選択します。

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20AI-G/Available%20Applications/ethernet1.png" width="600"></p>
<p align="center"><strong>図 6.2 プロパティの選択</strong></p><br/>
 
2. 共有タブを選択します。

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20AI-G/Available%20Applications/ethernet2.png" width="400"></p>
<p align="center"><strong>図 6.3 共有タブの選択</strong></p><br/>

3. 「ネットワークのほかのユーザーに、このコンピューターのインターネット接続をとおしての接続を許可する」のチェックボックスをオンにします。
 
4. ホームネットワーク接続のドロップダウンメニューで、D3-G を接続するイーサネットアダプタ (例: "Ethernet") を選択します。

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20AI-G/Available%20Applications/ethernet3.png" width="400"></p>
<p align="center"><strong>図 6.4 イーサネットアダプタの選択</strong></p><br/>
 
5. **OK** をクリックして設定を保存します。

<br/><br/>

### 6.2.2 ネットワーク設定ファイルの作成 
1. DHCP による動的 IP
ネットワークに DHCP サーバー (ルーターや ICS を有効にした Windows PC など) がある場合、ファイルを編集する必要はありません。イーサネットケーブルを接続すると、システムが自動的に IP アドレスを取得します。

ケーブルを差し込むだけで、すぐにネットワークを使用できます。第 6.2.4 章「ネットワーク接続の確認」に進んでください。

2. 静的 IP の設定
静的 IP アドレスを割り当てたい場合 (例: PC と直接接続する場合や DHCP サーバーが利用できない場合) は、同じファイルを次の内容で編集してください。
```
$ vi /etc/systemd/network/20-wired.network

[Match]
Name=eth0

[Network]
Address=192.168.137.2/24
Gateway=192.168.137.1
DNS=8.8.8.8
```
この設定では、IP アドレスを 192.168.137.2 に設定し、192.168.137.1 をゲートウェイ (Windows ICS で一般的) として使用し、Google DNS を構成します。

<br/><br/>

### 6.2.3 ネットワークサービスの再起動
systemd-networkd サービスを再起動して、新しいネットワーク設定を適用してください。

```
sudo systemctl restart systemd-networkd
```

<br/><br/>

### 6.2.4 ネットワーク接続の確認
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20D3-G/Software/host%20pc%20ethernet%20connection.png"width="500"></p>
<p align="center"><strong>図 6.5 ホスト PC とのネットワーク共有</strong></p>
<br/>

Google のパブリック DNS サーバーに ping を送信して、インターネット接続をテストしてください。

```
$ ping 8.8.8.8
PING 8.8.8.8 (8.8.8.8): 56 data bytes
64 bytes from 8.8.8.8: seq=0 ttl=113 time=30.208 ms
64 bytes from 8.8.8.8: seq=1 ttl=113 time=38.143 ms
64 bytes from 8.8.8.8: seq=2 ttl=113 time=30.969 ms
64 bytes from 8.8.8.8: seq=3 ttl=113 time=33.586 ms
```

<br/><br/><br/><br/>

# 7. 40 ピン GPIO ヘッダー
---
D3-G は 40 ピン GPIO ヘッダーを備えており、さまざまなハードウェアプロジェクトに柔軟な I/O 機能を提供します。
このヘッダーは汎用入出力 (GPIO) 動作に対応しており、センサー、LED、ボタン、その他の周辺機器を接続するために使用できます。

各ピンは、設定に応じてデジタル I/O、PWM、I2C、SPI、UART などの複数の機能をサポートします。

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/d3g/Assets/TOPST%20D3-G/Software/d3-g%20gpio%2040pinmap.png" width="800"></p>
<p align="center"><strong>図 7.1 D3-G の 40 ピン GPIO ヘッダーピンマップ </strong></p> <br/>

**注意**: 外部ハードウェアを接続する前に、公式のピンアウト図を参照して、詳細なピン機能と電圧レベルを確認してください。

<br/><br/><br/>

## 7.1 GPIO デジタル入出力
---
D3-G は 40 ピンヘッダーを介してデジタル入力および出力 (GPIO) をサポートしており、ボタン、LED、センサーなどの外部デバイスと連携できます。 

### 7.1.1 LED
---
最も簡単で一般的な GPIO 出力の例の一つは、LED の制御です。  
この節では、D3-G を使用して LED センサーを接続し使用する方法を説明します。

#### ステップ 1. ハードウェア要件
- D3-G ボード (x1)
- ブレッドボード (x1)
- LED (x1)
- オス-メス ジャンパーワイヤー (x2)
- DC 5V 電源アダプター (x1)
- USB-TTL シリアルケーブル (x1)

#### ステップ 2. 回路例
- LED
    - (+) ピンは D3-G ボードの 12 番ピンに接続します。
    - (-) ピンは D3-G ボードで GND として機能する 14 番ピンに接続します。  
    
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20D3-G/Software/led.png"></p>

<p align="center"><strong>図 7.2 D3-G GPIO LED 回路図 </strong></p> <br/>

##### ステップ 2.1 ピンマッピング
次の表はピンマッピングを示しています。

<div align="center">
  <p><strong>表 7.1 D3-G LED のピンマッピング</strong></p>
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
D3-G ボードの GPIO89 に接続された LED を動作させるには、次のコードを実行します:

```
import time
import os
  
def export_gpio(pin, direction: str):
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
  
    LED_PIN = 89  # LED connected to GPIO 89
  
    try:
        # Setup the GPIO pins
        export_gpio(LED_PIN, direction="out")
        print("GPIO pins initialized.")
        
        count = 0
        while (count < 10):
            write_gpio_value(LED_PIN, 1)  # Turn on the LED
            print("LED ON.")
            count += 1
            time.sleep(1.0)  # Polling delay
            write_gpio_value(LED_PIN, 0)  # Turn off the LED
            print("LED OFF.")
            time.sleep(1.0)  # Polling delay
 
        write_gpio_value(LED_PIN, 0)  # Turn off the LED
 
    except KeyboardInterrupt:
        print("Program interrupted by user.")
  
    finally:
        unexport_gpio(LED_PIN) # unexport LED pin
        print("GPIO pins unexported.")
        print("Program terminated.")

if __name__ == "__main__":
    main()
```

#### ステップ 4. 実行結果
次のコマンドでコードを実行してください。

```
$ python3 led_test.py
```

このスクリプトは GPIO89 をデジタル出力として設定し、1 秒ごとにその状態を切り替えます。
実行すると、GPIO89 に接続された LED が 1 秒間点灯し 1 秒間消灯する動作を繰り返し、10 回点滅します。10 回のサイクル後、スクリプトは終了し、GPIO を自動的に unexport します。

スクリプトを途中で停止するには、**[Ctrl+C]** を押してください。
いずれの場合も、ピンは適切に解放されクリーンアップされます。

**注意**: この構成は LED を直接接続することを前提としています。安全かつ長期的な動作のために、過大な電流の発生を防ぎ GPIO ピンを損傷から保護するため、LED と直列に電流制限抵抗 (例: 220Ω) を使用することを強く推奨します。

<br/><br/><br/><br/>

### 7.1.2 ボタン
---
プッシュボタンは、GPIO によるデジタル入力処理を示すためによく使用される基本的な入力デバイスです。
この節では、D3-G で基本的なボタンモジュールを接続し使用する方法を説明します。

#### ステップ 1. ハードウェア要件
- D3-G ボード (x1)
- ブレッドボード (x1)
- ボタン (x1)
- オス-メス ジャンパーワイヤー (x2)
- DC 5V 電源アダプター (x1)
- USB-TTL シリアルケーブル (x1)

#### ステップ 2. 回路例
- ボタンスイッチ
    - ボタンスイッチの一方の脚は D3-G ボードの 10 番ピンに接続します。
    - ボタンの上側にある反対の脚は 3.3V ピンに接続します。

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20D3-G/Software/button_circuit.png"></p> 
<p align="center"><strong>図 7.3 D3-G GPIO ボタン回路図</strong></p>

##### ステップ 2.1 ピンマッピング
次の表はピンマッピングを示しています。

<div align="center">
  <p><strong>表 7.2 D3-G ボタンのピンマッピング</strong></p>
  <table>
      <tr>
          <th colspan="3">ピン名</th>
          <th>D3-G</th>
          <th>GPIO</th>
      </tr>
      <tr>
          <td colspan="3">ボタンの一方の脚のピン</td>
          <td>10</td>
          <td>88</td>
      </tr>
  </table>
</div>

#### ステップ 3. 実行方法
D3-G ボードの GPIO88 に接続されたボタン入力を監視するには、次のコードを実行します:

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
    # initialize GPIO pins
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
        unexport_gpio(BUTTON_PIN)  # unexport the GPIO pin
        print("GPIO pins unexported.")
        print("Program terminated.")
         
if __name__ == "__main__":
    main()
```

#### ステップ 4. 実行結果
次のコマンドでコードを実行してください。
```
$ python3 test_button.py
```
このスクリプトは GPIO88 をデジタル入力として設定し、その値をリアルタイムで継続的に監視します。
実行後、GPIO88 に接続されたボタンを押すと、ボタンが押されたことを示すメッセージが出力されます。

スクリプトを停止するには、**[Ctrl+C]** を押してください。
スクリプトが終了すると、GPIO88 は自動的に unexport されクリーンアップされます。

**注意**: ここでは例として GPIO88 を使用しています。40 ピンヘッダーのピン配置に基づいて、D3-G で使用可能な任意の GPIO ピンを使用できます。
公式のピン配置図を参照し、ハードウェア構成に合った GPIO 番号を選択してください。

<br/><br/><br/><br/>

### 7.1.3 タッチセンサー
---
タッチセンサーは、GPIO を介して人の接触をデジタル入力信号として検出するために使用できます。
この節では、D3-G を使用して基本的なタッチセンサーモジュールを接続し、入力を読み取る方法を説明します。

#### ステップ 1. ハードウェア要件
- D3-G ボード (x1)
- タッチセンサー (x1)
- メス-メス ジャンパーワイヤ (x3)
- DC 5V 電源アダプター (x1)
- USB-TTL シリアルケーブル (x1)

#### ステップ 2. 回路例
- タッチセンサー
    - タッチセンサーの SIG ピンは D3-G ボードの 88 番ピンに接続します。
    - タッチセンサーの VCC ピンは D3-G ボードの 3.3V に接続します。
    - タッチセンサーの GND ピンは D3-G ボードの GND に接続します。


<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20D3-G/Software/touch%20circuit.png"></p>
<p align="center"><strong>図 7.4 D3-G GPIO タッチセンサー回路図</strong></p>

##### ステップ 2.1 ピンマッピング
次の表はピンマッピングを示しています。

<div align="center">
  <p><strong>表 7.3 D3-G タッチセンサーのピンマッピング</strong></p>
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
D3-G ボードの GPIO88 に接続されたタッチセンサーを監視するには、次のコードを実行するだけです:
```
import os
import time
 
# GPIO pin numbers setting
TOUCH_SENSOR_PIN = 88  # sensor GPIO pin
 
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
    # initialize GPIO pins
    export_gpio(TOUCH_SENSOR_PIN, "in")  # touch sensor pin direction "in"
    print("gpio pins initialized.")
 
    try:
        while True:
            # button sensor value read
            # If the sensor value is 0, it means an touch detected.
            # If the sensor value is 1, it means no touch released.
            sensor_value = read_gpio_value(TOUCH_SENSOR_PIN)
 
            if sensor_value == "1":  
                print("touch detected.")
            else:    
                print("touch released.")
 
            time.sleep(0.5)  # 500ms delay

    except KeyboardInterrupt:
        print("program interrupted by user.")
 
    finally:
        unexport_gpio(TOUCH_SENSOR_PIN)  # unexport the GPIO pin
        print("GPIO pins unexported.")
        print("program terminated.")
         
if __name__ == "__main__":
    main()
```

#### ステップ 4. 実行結果
次のコマンドでコードを実行してください。

```
$ python3 touch_test.py
```

このスクリプトは GPIO88 をデジタル入力として設定し、その値をリアルタイムで継続的に監視します。

実行後、センサーに触れると、ターミナルに次のようなメッセージが出力されます:
```
touch detected.
```
センサーに触れていない場合、出力は次のようになります:
```
touch released.
```
スクリプトを停止するには、**[Ctrl+C]** を押してください。
スクリプトが終了すると、GPIO88 は自動的に unexport されクリーンアップされます。

**注意**: ここでは例として GPIO88 を使用しています。40 ピンヘッダーのピン配置に基づいて、D3-G で使用可能な任意の GPIO ピンを使用できます。
公式のピン配置図を参照し、ハードウェア構成に合った GPIO 番号を選択してください。

<br/><br/><br/><br/>

### 7.1.4 振動検出センサー
---
振動センサーは、物理的な衝撃や振動を検出し、GPIO を通じてデジタル入力信号を出力するために使用できます。
本節では、D3-G を使用して基本的な振動センサーモジュールを接続し、入力を検出する方法を説明します。

#### ステップ 1. ハードウェア要件
- D3-G ボード (x1)
- 振動検出センサー (x1)
- メス-メスジャンパーワイヤ (x4)
- DC 5V 電源アダプター (x1)
- USB-TTL シリアルケーブル (x1)

#### ステップ 2. 回路例
- 振動検出センサー
    - 振動検出センサーの VCC ピンは、D3-G ボードの 3.3V ピンに接続します。
    - 振動検出センサーの GND ピンは、D3-G ボードの GND に接続します。
    - 振動検出センサーの DO ピンは、D3-G ボードの 88 番ピンに接続します。

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20D3-G/Software/vibr%20circuit.png"></p>
<p align="center"><strong>図 7.5 D3-G GPIO 振動検出センサー回路図</strong></p>

##### ステップ 2.1 ピンマッピング
次の表はピンマッピングを示しています。

<div align="center">
  <p><strong>表 7.4 D3-G 振動検出センサーのピンマッピング</strong></p>
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
D3-G ボードの GPIO88 に接続された振動センサーを監視するには、次のコードを実行します。
```
import os
import time
VIBRATION_SENSOR_PIN = 88  # VIBRATION_SENSOR sensor GPIO pin
 
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
    # initialize GPIO pins
    export_gpio(VIBRATION_SENSOR_PIN, "in")  # vibration sensor pin direction "in"
    print("gpio pins initialized.")
 
    try:
        while True:
            sensor_value = read_gpio_value(VIBRATION_SENSOR_PIN)
 
            if sensor_value == "0":  # vibration detected
                print("vibration detected.")
            else:    # no vibration detected
                print("no vibration detected.")
 
            time.sleep(0.5)  # 500ms delay

    except KeyboardInterrupt:
        print("Program interrupted by user.")
 
    finally:
        unexport_gpio(VIBRATION_SENSOR_PIN)  # unexport the GPIO pin
        print("GPIO pins unexported.")
        print("Program terminated.")
         
if __name__ == "__main__":
    main()
```

#### ステップ 4. 実行結果
次のコマンドでコードを実行してください。

```
$ python3 vibration_test.py
```

このスクリプトは GPIO88 をデジタル入力として設定し、その値をリアルタイムで継続的に監視します。
実行すると、センサーが検出した振動や衝撃に応じて、ターミナルに次のようなメッセージが表示されます。
```
vibration detected.
```
振動がない場合、出力は次のようになります。
```
no vibration detected.
```
スクリプトを停止するには、**[Ctrl+C]** を押してください。
終了時に、GPIO88 は自動的に unexport されてクリーンアップされます。

**注意**: ここでは GPIO88 を例として使用しています。センサーの配線とヘッダーの配置に応じて、利用可能な他の GPIO ピンを使用できます。GPIO 番号を選択する前に、D3-G のピンマップを参照してください。

<br/><br/><br/><br/>

### 7.1.5 赤外線センサー (SZH-SSBH-002)
---
赤外線センサーは、反射した赤外線を検知して近くの障害物を検出し、GPIO を通じてデジタル信号を出力するために使用できます。
本節では、D3-G を使用して SZH-SSBH-002 赤外線センサーを接続し、入力を読み取る方法を説明します。

#### ステップ 1. ハードウェア要件
- D3-G ボード (x1)
- ブレッドボード (x1)
- 赤外線センサー (x1)
- オス-メス ジャンパーワイヤ (x5)
- DC 5V 電源アダプター (x1)
- USB-TTL シリアルケーブル (x1)

#### ステップ 2. 回路例
- 赤外線センサー
    - 赤外線センサーの VCC ピンは、D3-G ボードの 3.3V ピンに接続します。
    - 赤外線センサーの GND ピンは、D3-G ボードの GND に接続します。
    - 赤外線センサーの OUT ピンは、D3-G ボードの 89 番ピンに接続します。


<p align="center">
  <img src="https://raw.githubusercontent.com/topst-development/Documentation/d3g/Assets/TOPST%20D3-G/Software/szh-ssbh-002_circuit.png">
</p> 
<p align="center"><strong>図 7.6 IR センサー実験回路</strong></p>

##### ステップ 2.1 ピンマッピング
次の表はピンマッピングを示しています。

<div align="center">
  <p><strong>表 7.5 D3-G IR センサーのピンマッピング</strong></p>
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
D3-G ボードの GPIO89 に接続された IR センサーを監視するには、次のコードを実行します。

```
import os
import time
 
# GPIO pin numbers setting
IR_SENSOR_PIN = 89  # IR sensor GPIO pin
 
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
    # initialize GPIO pins
    export_gpio(IR_SENSOR_PIN, "in")  # IR sensor pin direction "in"
    print("gpio pins initialized.")
 
    try:
        while True:
            sensor_value = read_gpio_value(IR_SENSOR_PIN)
 
            if sensor_value == "0":  # obstacle detected
                print("obstacle detected.")
            else: 
                print("No obstacle detected.")
 
            time.sleep(0.5)  # 500ms delay

    except KeyboardInterrupt:
        print("program interrupted by user.")
 
    finally:
        unexport_gpio(IR_SENSOR_PIN)  # unexport the GPIO pin
        print("GPIO pins unexported.")
        print("program terminated.")
         
if __name__ == "__main__":
    main()
```

#### ステップ 4. 実行結果
次のコマンドでコードを実行してください。
```
$ python3 ir_test.py
```
このスクリプトは GPIO89 をデジタル入力として設定し、その状態を継続的に監視して障害物を検出します。
IR センサーの前で物体が検出されると、ターミナルに次のように表示されます。
```
obstacle detected.
```
物体が検出されない場合は、次のように表示されます。
```
no obstacle detected.
```
スクリプトを停止するには、**[Ctrl+C]** を押してください。
スクリプトを終了すると、GPIO89 は自動的に unexport されてクリーンアップされます。

**注意**: このスクリプトでは GPIO89 を例として使用しています。
D3-G の 40 ピンヘッダーに基づいて、利用可能な GPIO ピンを使用できます。正確なピン選択については、公式のピンマップ図を参照してください。

<br/><br/><br/><br/>

### 7.1.6 フォトレジスタ (SZH-SSBH-011)
---
フォトレジスタは、周囲の明るさを検出し、光の強度が一定のしきい値を超えたときに GPIO を通じてデジタル信号を出力するために使用できます。
本節では、D3-G を使用して SZH-SSBH-011 フォトレジスタセンサーを接続し、入力を読み取る方法を説明します。

#### ステップ 1. ハードウェア要件
- D3-G ボード (x1)
- フォトレジスタモジュール (SZH-SSBH-011) (x1)
- LED (x1)
- 220Ω 抵抗 (x1)
- ブレッドボード (x1)
- オス-メス ジャンパーワイヤ (x7)
- DC 5V 電源アダプター (x1)
- USB-TTL シリアルケーブル (x1)

#### ステップ 2. 回路例
- フォトレジスタ (SZH-SSBH-011)
    - フォトレジスタの VCC ピンは、D3-G ボードの 3.3V ピンに接続します。
    - フォトレジスタの GND ピンは、D3-G ボードの GND に接続します。
    - フォトレジスタの DO ピンは、D3-G ボードの 89 番ピンに接続します。
- LED
    - LED の (+) ピンは、D3-G ボードの GND に接続します。
    - LED の (-) ピンは、D3-G ボードの 83 番ピンに接続します。

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20D3-G/Software/circuit.png"></p>
<p align="center"><strong>図 7.7 フォトレジスタ実験回路</strong></p>

##### ステップ 2.1 ピンマッピング
次の表はピンマッピングを示しています。

<div align="center">
  <p><strong>表 7.6 D3-G フォトレジスタのピンマッピング</strong></p>
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
  <p><strong>表 7.7 D3-G LED のピンマッピング</strong></p>
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
CDS センサーで明るさを監視し、それに応じて LED を制御するには、次の Python スクリプトを実行します。

```
import os
import time
LED_PIN = 83           # LED GPIO pin
CDS_SENSOR_PIN = 89    # szh-ssbh-011 CDS sensor GPIO pin

def export_gpio(pin, direction: str):
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
    # initialize GPIO pins
    export_gpio(LED_PIN, "out")          # LED pin direction "out"
    export_gpio(CDS_SENSOR_PIN, "in")     # CDS sensor pin direction "in"
    print("gpio pins initialized.")

    try:
        while True:
            sensor_value = read_gpio_value(CDS_SENSOR_PIN)
            print("sensor value: {}".format(sensor_value))
            if sensor_value == "0": # light detected
                print("brightness detected. Turning on the LED.")
                write_gpio_value(LED_PIN, 1)  # turn on the LED
            else:
                print("no brightness detected. Turning off the LED.")
                write_gpio_value(LED_PIN, 0)  # turn off the LED

            time.sleep(0.5)  #  500ms delay

    except KeyboardInterrupt:
        print("program interrupted by user.")

    finally:
        unexport_gpio(LED_PIN)          # unexport LED pin
        unexport_gpio(CDS_SENSOR_PIN)   # unexport CDS sensor pin
        print("GPIO pins unexported.")
        print("program terminated.")

if __name__ == "__main__":
    main()
```

### ステップ 4. 実行結果
次のコマンドでコードを実行してください。
```
$ python3 CDS_test.py
```
このスクリプトは、GPIO89 をフォトレジスタセンサー用の入力として、GPIO83 を LED 用の出力として設定します。
周囲の光が検出されると、ターミナルに次のように表示されます。
```
sensor value: 0
brightness detected. Turning on the LED.
```
そして LED が点灯します。
光が検出されない場合は、次のように表示されます。
```
sensor value: 1
no brightness detected. Turning off the LED.
```
そして LED が消灯します。
スクリプトを停止するには、**[Ctrl+C]** を押してください。
スクリプトを終了すると、両方の GPIO ピンが自動的に unexport されてクリーンアップされます。

**注意**: この例では GPIO83 と GPIO89 を使用しています。D3-G の 40 ピンヘッダーの配置に基づいて、利用可能な GPIO ピンを使用できます。正確なピン選択については、公式のピンマップ図を参照してください。

<br/><br/><br/><br/>

### 7.1.7 大気汚染検出センサー
---
大気汚染検出センサーは、環境中の有害ガスや粒子状物質の存在を監視し、GPIO を通じてデジタル信号を出力するために使用できます。
本節では、D3-G を使用して大気汚染検出センサーを接続し、入力を読み取る方法を説明します。

#### ステップ 1. ハードウェア要件
- D3-G ボード (x1)
- 大気汚染（ガス）検出センサーモジュール (x1)
- ブレッドボード (x1)
- オス-メス ジャンパーワイヤ (x3)
- DC 5V 電源アダプター (x1)
- USB-TTL シリアルケーブル (x1)

#### ステップ 2. 回路例
- 大気汚染検出センサー
    - 大気汚染検出センサーの VCC ピンは、D3-G ボードの 3.3V ピンに接続します。
    - 大気汚染検出センサーの GND ピンは、D3-G ボードの GND に接続します。
    - 大気汚染検出センサーの DO ピンは、D3-G ボードの 88 番ピンに接続します。

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20D3-G/Software/gas%20circuit.png"></p>
<p align="center"><strong>図 7.8 大気汚染検出センサー実験回路</strong></p>

##### ステップ 2.1 ピンマッピング
次の表はピンマッピングを示しています。

<div align="center">
  <p><strong>表 7.8 D3-G 大気汚染検出センサーのピンマッピング</strong></p>
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
GPIO88 ピンを使用してガス検出を監視するには、次の Python スクリプトを実行します。

```
import os
import time
GAS_SENSOR_PIN = 88  # gas sensor GPIO pin
 
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
    # initialize GPIO pins
    export_gpio(GAS_SENSOR_PIN, "in")  # gas sensor pin direction "in"
    print("gpio pins initialized.")
 
    try:
        while True:
            # gas sensor value read
            sensor_value = read_gpio_value(GAS_SENSOR_PIN)
 
            if sensor_value == "0":  # gas detected
                print("gas detected.")
            else:
                print("no gas detected.")
 
            time.sleep(0.5)  # 500ms delay

    except KeyboardInterrupt:
        print("program interrupted by user.")
 
    finally:
        unexport_gpio(GAS_SENSOR_PIN)  # unexport the GPIO pin
        print("GPIO pins unexported.")
        print("program terminated.")
         
if __name__ == "__main__":
    main()
```

#### ステップ 4. 実行結果
次のコマンドでコードを実行してください。
```
$ python3 gas_sensor_test.py
```
このスクリプトは GPIO88 をデジタル入力として設定し、ガス検出の状態を継続的に監視します。
ガス濃度がセンサーのしきい値に達すると、ターミナルに次のように表示されます。
```
gas detected.
```
ガスが検出されない場合、ターミナルには次のように表示されます。
```
no gas detected.
```
スクリプトを停止するには、**[Ctrl+C]** を押してください。
スクリプトを終了すると、GPIO88 は自動的に unexport されてクリーンアップされます。

**注意**: ここでは GPIO88 を例として使用しています。D3-G の 40 ピンヘッダーの配置に基づいて、利用可能な GPIO ピンを使用できます。正確なピン選択については、公式のピンマップ図を参照してください。

<br/><br/><br/><br/>

### 7.1.8 超音波センサー
---
超音波センサーは、超音波を発信して反射信号を受信することで近くの物体までの距離を測定し、GPIO を通じてデジタル（またはパルスベース）信号を出力するために使用できます。
本節では、D3-G を使用して超音波センサーを接続し、入力を読み取る方法を説明します。

#### ステップ 1. ハードウェア要件
- D3-G ボード (x1)
- 超音波センサー (x1)
- メス-メス ジャンパーワイヤ (x4)
- DC 5V 電源アダプター (x1)
- USB-TTL シリアルケーブル (x1)

#### ステップ 2. 回路例
- 超音波センサー
    - 超音波センサーの VCC ピンは、D3-G ボードの 5V ピンに接続します。
    - 超音波センサーの GND ピンは、D3-G ボードの GND に接続します。
    - 超音波センサーの TRIG ピンは、D3-G ボードの 82 番ピンに接続します。
    - 超音波センサーの ECHO ピンは、D3-G ボードの 88 番ピンに接続します。

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20D3-G/Software/ultra%20circuit.png"></p>
<p align="center"><strong>図 7.9 超音波センサー実験回路</strong></p>

##### ステップ 2.1 ピンマッピング
次の表はピンマッピングを示しています。

<div align="center">
  <p><strong>表 7.9 D3-G 超音波センサーのピンマッピング</strong></p>
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
超音波センサーを使用して距離を測定するには、次の Python スクリプトを実行します。
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
次のコマンドでコードを実行してください。
```
$ python3 ultrasonic_sensor_test.py
```
このスクリプトは、超音波パルスを発生させるために GPIO82 をデジタル出力として、エコーを受信するために GPIO88 をデジタル入力として設定します。
スクリプトを実行すると、センサーの前にある最も近い物体までの距離が 1 秒ごとに表示されます。例:
```
Distance: 23.45 cm
Distance: 24.12 cm
...
```
スクリプトを停止するには、**[Ctrl+C]** を押してください。
スクリプトを終了すると、GPIO82 と GPIO88 は自動的に unexport されてクリーンアップされます。

**注意**: ここでは GPIO82 と GPIO88 を例として使用しています。D3-G の 40 ピンヘッダーの配置に基づいて、利用可能な GPIO ピンを使用できます。正確なピン選択については、公式のピンマップ図を参照してください。また、ECHO ピンの電圧レベルが D3-G にとって安全であることを確認してください（一部のモジュールは 5V を出力するため、分圧回路またはレベルシフタが必要になる場合があります）。

<br/><br/><br/><br/>

## 7.2 I2C
---
D3-G は 40 ピン GPIO ヘッダーを通じて I2C 通信を提供しており、センサー、ディスプレイ、拡張モジュールなどのさまざまな周辺機器と接続できます。
I2C（Inter-integrated Circuit）は、データライン（SDA）とクロックライン（SCL）から成る 2 線式通信プロトコルであり、複数のデバイスが共有バス上で通信できるようにします。

I2C 通信はマスター・スレーブ方式に従い、1 台のマスターデバイスが通信を制御し、同一バス上に最大 127 台のスレーブデバイスを接続できます。
SDA ラインはデータの送信と受信の両方に使用され、SCL ラインはデータ転送のタイミングを同期します。この同期通信モデルにより、デバイスはクロックに基づいて協調的に情報を交換できます。

<br/><br/><br/><br/>

### 7.2.1 1602A LCD ディスプレイ
---
1602A LCD は、組み込みシステムで一般的に使用される文字表示モジュールです。
D3-G では、LCD の SDA および SCL ラインを I2C 用に設定された GPIO ピンに接続できます。接続後は、Linux の I2C ツールまたは独自のソフトウェアを使用して LCD を制御できます。

#### ステップ 1. ハードウェア要件
- D3-G ボード (x1)
- 1602A I2C LCD モジュール (x1)
- メス-メス ジャンパーワイヤ (x4)
- DC 5V 電源アダプター (x1)
- USB to TTL シリアルケーブル (x1)  

LCD モジュールに I2C バックパックが付いていることを確認してください

#### ステップ 2. 回路例
- I2C LCD モジュール
    - I2C LCD モジュールの GND ピンは、D3-G ボードの GND ピンに接続します。
    - I2C LCD モジュールの VCC ピンは、D3-G ボードの 5V に接続します。
    - I2C LCD モジュールの SDA ピンは、D3-G ボードの 82 番ピンに接続します。
    - I2C LCD モジュールの SCL ピンは、D3-G ボードの 81 番ピンに接続します。

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20D3-G/Software/lcd_circuit.png"></p>
<p align="center"><strong>図 7.10 D3-G I2C LCD モジュール回路図  </strong></p>

##### ステップ 2.1 ピンマッピング
次の表はピンマッピングを示しています。

<div align="center">
  <p><strong>表 7.10 D3-G I2C LCD モジュールのピンマッピング</strong></p>
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
最初に必要な Python ライブラリをインストールします:
```
$ pip install RPLCD smbus2
```
次に、以下の Python コードを使用して LCD にテキストを表示します:
```
import smbus2
import time
from RPLCD.i2c import CharLCD
 
# I2C bus num
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
次のコマンドでコードを実行してください。
```
$ python3 lcd_test.py
```
このスクリプトは、RPLCD ライブラリを使用して I2C ベースの 1602A LCD を初期化し、ユーザーが入力したテキストを画面に表示します。
スクリプトを実行すると、文字列の入力を求められます。入力したテキストは LCD に 4 秒間表示された後、消去されます。例を次に示します:
```
Enter text to display on LCD: Hello D3-G!
```
LCD には次のように表示されます:
```
Hello D3-G!
```
その後、4 秒後に消去されます。

スクリプトを停止するには、**[Ctrl+C]** を押してください。

**注意** : D3-G では、デフォルトで GPIO82 と GPIO81 が I2C 用に使用されます。
I2C アドレス (0x27) が使用している LCD モジュールと一致していることを確認してください。必要に応じて **i2cdetect -y 3** を使用して I2C デバイスをスキャンしてください。

<br/><br/><br/><br/>

## 7.3 SPI
---
D3-G は 40 ピンの GPIO ヘッダーを介して Serial Peripheral Interface (SPI) 通信をサポートしており、外部デバイスと D3-G の間でデータをやり取りできます。

SPI は全二重通信が可能な同期式シリアル通信プロトコルであり、データの送信と受信を同時に行うことができます。Master Out Slave In (MOSI)、Master In Slave Out (MISO)、Serial Clock (SCLK)、Chip Select (CS) の 4 本の主要な信号線を使用します。

複数のデバイスで信号線を共有する I2C とは異なり、SPI ではスレーブデバイスごとに専用の CS 信号線が必要です。この一対多の構成により、SPI は高速で実装が容易ですが、複数のデバイスを接続する場合は物理的な配線が多く必要になることがあります。

<br/><br/><br/><br/>

### 7.3.1 ドットマトリクス
---
8x8 ドットマトリクスディスプレイは、組み込みシステムで簡単なテキストやパターンを出力する用途で広く使用されています。D3-G では、MAX7219 などのドライバチップを使用して、SPI 経由でドットマトリクスモジュールを制御できます。

MAX7219 は行と列のスキャンを内部で処理するため、マイクロコントローラは MOSI (DIN)、SCLK、CS (LOAD) というわずかな SPI 信号だけでディスプレイ全体を制御できます。接続が完了すると、ユーザー定義のスクリプトやライブラリを使用して SPI 通信でディスプレイを制御できます。

#### ステップ 1. ハードウェア要件
- D3-G ボード (x1)
- ドットマトリクス (x1)
- オス-メス ジャンパーワイヤ (x4)
- DC 5V 電源アダプター (x1)
- USB-TTL シリアルケーブル (x1)

#### ステップ 2. 回路例
- ドットマトリクス
    - ドットマトリクスの VCC ピンは、D3-G ボードの 5V ピンに接続します。
    - ドットマトリクスの GND ピンは、D3-G ボードの GND ピンに接続します。
    - ドットマトリクスの DIN ピンは、D3-G ボードの 120 番ピンに接続します。
    - ドットマトリクスの CS ピンは、D3-G ボードの 119 番ピンに接続します。
    - ドットマトリクスの CLK ピンは、D3-G ボードの 118 番ピンに接続します。

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20D3-G/Software/dot%20circuit.png"></p>
<p align="center"><strong>図 7.11 D3-G ドットマトリクスモジュールの回路図  </strong></p>

##### ステップ 2.1 ピンマッピング
次の表はピンマッピングを示しています。
<div align="center">
  <p><strong>表 7.11 D3-G ドットマトリクスのピンマッピング</strong></p>
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
次の Python スクリプトは、低レベルの fcntl 呼び出しを使用して /dev/spidev3.0 経由で MAX7219 を直接制御する方法を示しています。この方法は、外部 SPI ライブラリを利用できないデバイスに適しています:
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
```

#### ステップ 4. 実行結果
次のコマンドでコードを実行してください。
```
$ python3 dot_matrix_test.py
```
このスクリプトは、SPI で接続された MAX7219 ドットマトリクスディスプレイを初期化し、値の入力を求めます。入力内容に応じて、8x8 LED マトリクスに特定のパターンが表示されます。

スクリプトを実行すると、次のように表示されます:
```
Enter a number, an uppercase letter (0-9, A-Z), 'Smile', 'Dance', 'Angry', 'Good', 'Nice', 'Emotion':
```
例:
- A を入力すると、文字 A が表示されます。
- Smile を入力すると、スマイルフェイスのパターンが表示されます。
- Dance を入力すると、交互に切り替わるダンスアニメーションが実行されます。
- Nice を入力すると、N-I-C-E の文字が順番にアニメーション表示されます。

スクリプトを停止するには、**[Ctrl+C]** を押してください。
終了時には SPI デバイスが安全にクローズされ、LED マトリクスの更新が停止します。

**注意**: /dev/spidev3.0 が存在すること、および配線がピンマッピング表と一致していることを確認してください。また、MAX7219 モジュールには安定した 5V 電源を供給してください。

<br/><br/><br/><br/>

## 7.4 PWM
---
Pulse Width Modulation (PWM) は、パルス信号の幅を変化させることで LED、モーター、ブザーなどのデバイスを制御するために使用されます。D3-G は Linux の sysfs インターフェースを介して PWM をサポートしています。

### 7.4.1 LED の明るさ制御
---
この例では、D3-G で PWM を使用して LED の明るさを制御する方法を説明します。

#### ステップ 1. ハードウェア要件
- D3-G ボード (x1)
- LED (x1)
- オス-メス ジャンパーワイヤ (x2)
- ブレッドボード
- DC 5V 電源アダプター (x1)
- USB-TTL シリアルケーブル (x1)

#### ステップ 2. 回路例
- LED
    - LED の (+) ピンは、D3-G ボードの 89 番ピンに接続します。
    - LED の (-) ピンは、D3-G ボードの GND ピンに接続します。

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20D3-G/Software/led.png"></p>
<p align="center"><strong>図 7.12 D3-G LED の回路図  </strong></p>

##### ステップ 2.1 ピンマッピング
次の表はピンマッピングを示しています。

<div align="center">
  <p><strong>表 7.12 D3-G LED のピンマッピング</strong></p>
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
D3-G ボードの GPIO89 に接続した LED (PWM) を動作させるには、次のコードを実行します:
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
次のコマンドでコードを実行してください。
```
$ python3 led_pwm.py
```
このスクリプトは LED ピンの PWM を初期化し、LED の明るさを連続的に上下させてフェードさせます。

スクリプトを実行すると、次のような出力が表示されます:
```
Starting LED PWM control (press Ctrl+C to stop)
```
LED は徐々に明るくなり、その後暗くなる動作を繰り返し、"呼吸" のような効果を再現します。

スクリプトを停止するには、**[Ctrl+C]** を押してください。

**注意**: PWM チャンネルが既に使用されていないこと、および選択した GPIO で D3-G がハードウェア PWM をサポートしていることを確認してください。PWM が動作しない場合は、/sys/class/pwm/ の export、period、duty_cycle の設定を確認してください。

<br/><br/><br/><br/>

### 7.4.2 ミニサーボモーター
---
ミニサーボモーターは、GPIO を介した Pulse Width Modulation (PWM) 信号に基づいて精密な角度移動を制御するために使用できます。
この節では、D3-G を使用してミニサーボモーターを接続し、制御する方法を説明します。

#### ステップ 1. ハードウェア要件
- D3-G ボード (x1)
- サーボモーター (x1)
- オス-メス ジャンパーワイヤ (x3)
- DC 5V 電源アダプター (x1)
- USB-TTL シリアルケーブル (x1)

#### ステップ 2. 回路例
- サーボモーター
    - サーボモーターの VCC ピンは、D3-G ボードの 5V に接続します。
    - サーボモーターの GND ピンは、D3-G ボードの GND に接続します。
    - サーボモーターの SIG ピンは、D3-G ボードの 89 番ピンに接続します。

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20D3-G/Software/motor_circuit.png"p>
<p align="center"><strong>図 7.13 D3-G サーボモーターの回路図  </strong></p>

##### ステップ 2.1 ピンマッピング
次の表はピンマッピングを示しています。

<div align="center">
  <p><strong>表 7.13 D3-G サーボモーターのピンマッピング</strong></p>
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
次の Python スクリプトは、D3-G の sysfs インターフェースを介した PWM でミニサーボモーターを直接制御する方法を示しています。この方法では外部ライブラリが不要で、角度に基づく位置決めをきめ細かく制御できます。
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
次のコマンドでコードを実行してください。
```
$ python3 motor_test.py
```
このスクリプトは、目標角度に応じてデューティサイクルを調整することで、PWM によりミニサーボモーターを制御します。
実行すると、次の入力プロンプトが表示されます:
```
Enter 1 (CW) or 0 (CCW), q to quit:
```
1 を入力するとサーボは時計回りに 180° まで回転し、0 を入力すると反時計回りに 0° まで回転します。必要な回数だけ繰り返すことができます。

スクリプトを停止するには、**[q]** を入力するか **[Ctrl+C]** を押してください。その後、スクリプトは PWM チャンネルを無効化し、unexport します。

**注意**: 安全に動作させるため、サーボモーターが 50 Hz の PWM 信号に対応し、1 ms～2 ms のデューティパルス範囲で動作することを確認してください。
