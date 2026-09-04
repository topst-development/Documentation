# 1. 簡介 
---
本文件提供 D3-G 的使用範例。   
本文件包含下列資訊：
- 輸入裝置
  - 鍵盤 
  - 滑鼠
- 視訊輸出
- 攝影機連接
  - MIPI CSI
  - USB 網路攝影機
- 儲存裝置連接
  - SD 卡
  - SATA HDD
  - NVMe M.2 SSD
  - USB 儲存裝置
- 乙太網路連接
- 40-pin GPIO 排針
  - 可用的感測器與裝置

<br/><br/><br/><br/>


# 2. 輸入裝置
---
D3-G 支援兩個用於連接輸入裝置的 USB 連接埠。
其中包含一個 USB 2.0 Type-A 連接埠與一個 USB 3.0 Type-A 連接埠，讓您可以連接滑鼠或鍵盤直接控制 D3-G。 

**註**：D3-G 上的 USB Type-C 連接埠保留給韌體下載使用，無法用於連接輸入裝置。

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20D3-G/Software/input%20device.png" width="500"></p>
<p align="center"><strong>圖 2.1 將輸入裝置連接至 D3-G 開發板 </strong></p><br/><br/><br/><br/>


# 3. 視訊輸出
---
D3-G 僅透過其 DisplayPort (DP) 輸出支援 FHD 顯示器。
它也支援使用菊鏈 (daisy chain) 設定的多顯示器輸出，可同時連接最多兩台 FHD 顯示器與一台 HD 顯示器。

**註**：若要使用 HDMI，需要另外準備主動式轉接器。
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20D3-G/Software/monitor.png" width="500"></p>
<p align="center"><strong>圖 3.1 將顯示器連接至 D3-G 開發板 </strong></p>

<br/><br/><br/><br/>

# 4. 攝影機連接
---
D3-G 支援攝影機功能，可彈性應用於各種用途。
您可以依照專案需求連接 MIPI CSI 攝影機或 USB 網路攝影機。

<br/><br/><br/>

## 4.1 USB 網路攝影機
---
D3-G 支援 USB 網路攝影機，解析度最高可達 Full HD (FHD)。
您可以依照下列步驟測試網路攝影機：


#### 步驟 1. 將 USB 攝影機連接至開發板上的 USB 連接埠。
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20D3-G/Software/webcam.png" width="400"></p>
<p align="center"><strong>圖 4.1 將網路攝影機連接至 D3-G 開發板</strong></p><br/>

#### 步驟 2. 將輸入裝置（滑鼠與鍵盤）及顯示器連接至 D3-G。
   
#### 步驟 3. 啟動 D3-G。

#### 步驟 4. 檢查可用的 /dev/video 裝置。
```
$ ls /dev/video*
```

#### 步驟 5. 使用 OpenCV（或 vutils）確認視訊輸出。
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
CSI 是 Camera Serial Interface 的縮寫，是由 MIPI Alliance 定義、用於將攝影機模組連接至主處理器的標準介面。
它可將影像資料以高速、低功耗的方式從攝影機傳輸至處理器。

D3-G 具備兩個 MIPI CSI 通道（ch0 與 ch1），可讓您連接支援排線 (Flat Flexible Cable, FFC) 的攝影機模組。
目前 D3-G 僅支援 ArduCam (5 MP) 與 Raspberry Pi v1 Camera (5 MP) 模組。 

**註**：目前 D3-G 不支援同時使用 CSI channel 0 與 CSI channel 1。

<br/><br/>

### 4.2.1 ArduCam
ArduCam 是專為嵌入式系統與 IoT 應用設計的多功能攝影機模組。它支援多種影像感測器與介面，包括 MIPI CSI，因此很適合整合至 D3-G 這類開發板。
D3-G 所支援的 5 MP ArduCam 模組具有良好的影像品質，常用於基本的電腦視覺任務、串流以及以攝影機為基礎的 AI 應用。由於相容於 FFC 排線，可輕鬆連接至 D3-G 開發板的 CSI 介面。 

ArduCam 模組的規格如下。

| 規格 | 說明 |
| ------------------------ | ------------------------------------------- |
| 感測器 | OV5647（500 萬畫素） |
| 解析度                   | 2592 × 1944 (Full 5 MP)                      |
| 支援的輸出格式 | RAW、YUV、JPEG（視感測器而定） |
| 介面                     | MIPI CSI-2                                  |
| 影格率 | 1080p 最高 30fps，720p 最高 60fps |
| 鏡頭座 | 定焦鏡頭（標準） |
| 視野角 (FOV)             | 約 54° – 70°（依型號而異）         |
| 連接方式                 | 排線 (FFC)                   |
| 工作電壓 | 3.3V（典型值） |
| 外型規格 | 精巧 PCB，約 25 mm x 24 mm |
| 相容性                   | Raspberry Pi 與 D3-G（透過 MIPI CSI-2 連接埠）    |
| 其他特性 | 低功耗、隨插即用模組 |


您可以依照下列步驟測試 ArduCam：
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20D3-G/Software/arducam.png" width="400"></p>
<p align="center"><strong>圖 4.2 ArduCam </strong></p><br/>

#### 步驟 1. 依照圖 4.3 所示，將 ArduCam 連接至 D3-G 開發板的 MIPI CSI 0。
 
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20D3-G/Software/rasp%20v1%20cam%20to%20d3g.png" width="500"></p>
<p align="center"><strong>圖 4.3 將 ArduCam 連接至 D3-G 開發板</strong></p> <br/>

#### 步驟 2. 連接 ArduCam 之後，您可以在 D3-G 開發板上使用下列 GStreamer 命令確認視訊串流：
```
$ gst-launch-1.0 v4l2src device=/dev/video0 io-mode=2 ! video/x-raw,format=NV12,width=1920,height=1280,framerate=30/1 ! videoconvert ! waylandsink fullscreen=true
```

此命令會從以 CSI 連接的 ArduCam 擷取視訊，轉換後透過 Wayland 顯示伺服器以全螢幕模式顯示。  
執行命令前請確認攝影機模組已牢固連接。若未顯示視訊，請檢查排線連接，並確認系統已正確辨識 /dev/video0。

<br/><br/>

### 4.2.2 Raspberry Pi v1 Camera
Raspberry Pi v1 Camera Module 是由 Raspberry Pi Foundation 開發的小型 5 MP 攝影機。它採用 OmniVision OV5647 影像感測器，並透過 MIPI CSI-2 介面以排線 (FFC) 連接至主開發板。

此模組原本是為 Raspberry Pi 系列設計，同樣相容於 D3-G，因此是影像擷取、視訊錄影與電腦視覺專案等基本攝影機應用的可靠選擇。

Raspberry Pi v1 攝影機模組的規格如下。

| 規格 | 說明 |
| ------------------- | ---------------------------------------- |
| 感測器 | OmniVision OV5647 |
| 解析度 | 2592 × 1944（5 MP） |
| 輸出格式 | RAW、YUV、JPEG |
| 介面                | MIPI CSI-2                               |
| 影格率 | 1080p30、720p60、VGA90 |
| 鏡頭 | 定焦 |
| 視野角（FOV） | 最高 54° |
| 排線類型 | FFC（15-pin） |
| 板子尺寸 | 25 mm x 24 mm |
| 相容性              | Raspberry Pi 與 D3-G（透過 MIPI CSI-2 連接埠） |

您可以依照下列步驟測試 Raspberry Pi v1 攝影機：

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20D3-G/Software/rasp%20v1%20cam.jpg" width="400"></p>
<p align="center"><strong>圖 4.4. Raspberry Pi v1 Camera </strong></p><br/>

#### 步驟 1. 依照圖 4.5 所示，將 Raspberry Pi v1 攝影機連接至 D3-G 開發板的 MIPI CSI 1。
 
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20D3-G/Software/rasp%20v1%20cam%20to%20d3g.png" width="500"></p>
<p align="center"><strong>圖 4.5 將 Raspberry Pi v1 Camera 連接至 D3-G 開發板</strong></p> <br/>

#### 步驟 2. 連接 Raspberry Pi 攝影機之後，您可以在 D3-G 上使用下列 GStreamer 命令確認視訊串流：
```
$ gst-launch-1.0 v4l2src device=/dev/video0 io-mode=2 ! video/x-raw,format=NV12,width=1920,height=1280,framerate=30/1 ! videoconvert ! waylandsink fullscreen=true
```

此命令會從以 CSI 連接的 Raspberry Pi 攝影機擷取視訊，轉換後透過 Wayland 顯示伺服器以全螢幕模式顯示。  
執行命令前請確認攝影機模組已牢固連接。若未顯示視訊，請檢查排線連接，並確認系統已正確辨識 /dev/video0。

<br/><br/><br/><br/>

# 5. 儲存裝置連接
---
本章說明如何將 D3-G 連接至各種儲存裝置。支援的儲存選項包括 USB 隨身碟、SD 卡，以及透過 PCIe 連接的外接儲存裝置。

<br/><br/><br/>

## 5.1 USB 隨身碟
---
D3-G 透過其 USB 2.0 與 USB 3.0 Type-A 連接埠支援 USB 儲存裝置。
若要連接 USB 隨身碟：

### 步驟 1. 將 USB 隨身碟插入 D3-G 上任一可用的 USB Type-A 連接埠。
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20D3-G/Software/usb%20storage%20connection%20with%20d3g.png" width="500"></p>
<p align="center"><strong>圖 5.1 將 USB 儲存裝置連接至 D3-G 開發板</strong></p> <br/>

### 步驟 2. 連接之後，該裝置通常會被辨識為 /dev/sda1、/dev/sdb1 等，實際名稱視系統狀態而定。

<br/>

### 步驟 3. 您可以使用下列命令手動掛載 USB 隨身碟：
   ```
   $ sudo mount /dev/sda1 /mnt
   ```

<br/><br/><br/>

## 5.2 SD 卡
---
D3-G 內建 microSD 卡插槽，支援標準的 SDHC/SDXC 卡。
若要在 D3-G 上使用 SD 卡：

<br/>

### 步驟 1. 將 microSD 卡插入 D3-G 開發板上的 SD 卡插槽。
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20D3-G/Software/sd%20card%20connect%20with%20d3g.png" width="500"></p>
<p align="center"><strong>圖 5.2 將 SD 卡連接至 D3-G 開發板</strong></p> <br/>

### 步驟 2. 插入之後，系統通常會將 SD 卡辨識為 /dev/mmcblk1p1 或類似的裝置節點。
  ```
  $ ls /dev/mmcblk*
  ```
<br/>

### 步驟 3. 若要手動掛載 SD 卡，請使用下列命令：
```
$ sudo mount /dev/mmcblk1p1 /mnt 
```
### 步驟 4. 掛載之後，您可以在 /mnt 目錄下存取 SD 卡的內容。

<br/><br/><br/>

## 5.3 SATA HDD
---

D3-G 支援透過其 PCIe 插槽搭配相容的 SATA 控制器使用 SATA 儲存裝置，例如 HDD 或 SSD。

<br/>

#### 步驟 1. 連接 PCIe 轉 SATA 模組

若要透過 PCIe 在 D3-G 上使用 SATA HDD，您必須先將 PCIe 轉 SATA 轉接模組連接至 D3-G 的 PCIe 插槽。

接著將 HDD 連接至 SATA 模組，並確認 HDD 由外部 12V 電源供電。

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20D3-G/Software/sata.png" width="500"></p>
<p align="center"><strong>圖 5.3 將 D3-G 開發板的 PCIe 連接至 SATA 模組 </strong></p><br/>

#### 步驟 2. 啟動 D3-G 
啟動 D3-G 之後，請觀察開機記錄，確認系統已辨識到 PCIe 裝置。
請查看類似 **telechips-pcie: Link up** 的訊息，這表示 PCIe 連線已成功建立。

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

#### 步驟 3. 確認 SATA HDD 是否被辨識
```
root@TOPST:~# lspci
00:00.0 PCI bridge: Synopsys, Inc. Device 8040 (rev 01)
01:00.0 SATA controller: ASMedia Technology Inc. Device 1064 (rev 02)
```
若無法使用 **lspci** 命令，請使用下列命令安裝 pciutils。

```
$ sudo apt-get install pciutils
```

<br/>

#### 步驟 4. 掛載 SATA HDD
```
$ fdisk /dev/sda
Welcome to fdisk (util-linux 2.37.4).
Changes will remain in memory only, until you decide to write them.
Be careful before using the write command.

Command (m for help): 
```

請在 fdisk 提示字元中依序輸入下列按鍵：

- o — 建立新的空白 DOS 分割區表（選用，會清除現有的分割區表）

- n — 新增一個分割區

- p — 選擇主要分割區

- 1 — 將分割區編號設為 1

- 按下 Enter — 接受預設的起始磁區

- 按下 Enter — 接受預設的結束磁區（使用整顆磁碟）

- w — 寫入分割區表並離開

```
$ mkfs.ext4 /dev/sda1

$ mkdir -p /mnt/sata

$ mount /dev/sda1 /mnt/sata
```

<br/>

#### 步驟 5. 執行結果
此輸出確認 SATA SSD 分割區 (/dev/sdb1) 已成功格式化為 ext4 檔案系統，並掛載於 /mnt/sata。
**df -h** 命令顯示該裝置已被辨識，且系統可以使用。

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
D3-G 支援透過其 PCIe 插槽直接連接 NVMe M.2 SSD。
<br/>

#### 步驟 1. 連接 SSD
- NVMe SSD (M.2 PCIe)：將 NVMe M.2 SSD 插入 D3-G 的 PCIe 插槽。 

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20D3-G/Software/M.2%20SSD%20connection.png" width="600"></p>
<p align="center"><strong>圖 5.4 將 NVMe M.2 SSD 連接至 D3-G 開發板</strong></p><br/>

#### 步驟 2. 啟動 D3-G
執行 **reboot** 命令後，請觀察開機記錄，確認系統已辨識到 PCIe 裝置。
請查看類似 **telechips-pcie: Link up** 的訊息，這表示 PCIe 連線已成功建立。

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

#### 步驟 3. 確認 SSD 是否被辨識
```
root@TOPST:~# lspci
00:00.0 PCI bridge: Synopsys, Inc. Device 8040 (rev 01)
01:00.0 Non-Volatile memory controller: Solid State Storage Technology Corporation Device 1007 (rev 03)
```
若無法使用 **lspci** 命令，請使用下列命令安裝 pciutils。

```
$ sudo apt-get install pciutils
```

<br/>

#### 步驟 4. 掛載 SSD
```
$ fdisk /dev/nvme0n1
Welcome to fdisk (util-linux 2.37.4).
Changes will remain in memory only, until you decide to write them.
Be careful before using the write command.

Command (m for help): 
```

請在 fdisk 提示字元中依序輸入下列按鍵：

- o — 建立新的空白 DOS 分割區表（選用，會清除現有的分割區表）

- n — 新增一個分割區

- p — 選擇主要分割區

- 1 — 將分割區編號設為 1

- 按下 Enter — 接受預設的起始磁區

- 按下 Enter — 接受預設的結束磁區（使用整顆磁碟）

- w — 寫入分割區表並離開

```
$ mkfs.ext4 /dev/nvme0n1p1

$ mkdir -p /mnt/nvme

$ mount /dev/nvme0n1p1 /mnt/nvme
```

<br/>

#### 步驟 5. 執行結果
此輸出確認系統已成功偵測到 NVMe SSD 裝置 (/dev/nvme0n1p1)，並將其掛載於 /mnt/nvme。
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


# 6. 乙太網路連接
---
D3-G 透過板載的 J2C 乙太網路連接埠支援乙太網路連線。這讓 D3-G 可以使用標準 TCP/IP 通訊協定與區域網路或網際網路通訊。乙太網路常用於部署需要遠端存取、資料串流或軟體更新的應用程式。

<br/><br/><br/>

## 6.1 透過路由器連接網路
---
此方法使用標準路由器將 D3-G 連接至區域網路。D3-G 可透過 DHCP 自動取得 IP 位址，或設定為靜態 IP 位址。

<br/><br/>

### 6.1.1 建立網路設定檔

1. 透過 DHCP 取得動態 IP
若您的網路提供 DHCP 伺服器（例如路由器或已啟用 ICS 的 Windows PC），則不需要編輯檔案。只要接上乙太網路線，系統就會自動取得 IP 位址。

您只要插上網路線即可立即開始使用網路。請前往第 6.1.3 節 驗證網路連線。

2. 靜態 IP 設定
若您想指定靜態 IP 位址（例如直接與 PC 連接，或沒有可用的 DHCP 伺服器時），請以下列內容編輯同一個檔案：
```
$ vi /etc/systemd/network/20-wired.network

[Match]
Name=eth0

[Network]
Address=192.168.137.2/24
Gateway=192.168.137.1
DNS=8.8.8.8
```

這會將 IP 位址設為 192.168.137.2，並使用 192.168.137.1 作為閘道（Windows ICS 常見的設定），同時設定 Google DNS。

<br/><br/>

### 6.1.2 重新啟動網路服務
請重新啟動 systemd-networkd 服務以套用新的網路設定：

```
sudo systemctl restart systemd-networkd
```

<br/><br/>

### 6.1.3 驗證網路連線
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20D3-G/Software/router%20connection.png"width="500"></p>
<p align="center"><strong>圖 6.1 透過路由器連接網路</strong></p>

請 ping Google 的公用 DNS 伺服器以測試網際網路連線：

```
$ ping 8.8.8.8
PING 8.8.8.8 (8.8.8.8): 56 data bytes
64 bytes from 8.8.8.8: seq=0 ttl=113 time=30.208 ms
64 bytes from 8.8.8.8: seq=1 ttl=113 time=38.143 ms
64 bytes from 8.8.8.8: seq=2 ttl=113 time=30.969 ms
64 bytes from 8.8.8.8: seq=3 ttl=113 time=33.586 ms
 
```

<br/><br/><br/>

## 6.2 與主機 PC 共用網路
---
您可以利用 Windows 作業系統提供的網際網路連線共用 (ICS) 功能，不使用路由器也能將 PC 的網際網路連線分享給 D3-G。

<br/><br/>

### 6.2.1 主機 PC 網路設定
- 控制台 → 網路和網際網路 → 網路連線 → 設定乙太網路
 
1. 請找出已連線至網際網路的網路介面卡（例如 Wi-Fi），在其上按一下滑鼠右鍵，然後選擇 **內容**。

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20AI-G/Available%20Applications/ethernet1.png" width="600"></p>
<p align="center"><strong>圖 6.2 選擇內容</strong></p><br/>
 
2. 請選擇「共用」索引標籤。

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20AI-G/Available%20Applications/ethernet2.png" width="400"></p>
<p align="center"><strong>圖 6.3 選擇共用索引標籤</strong></p><br/>

3. 請勾選標示為「允許其他網路使用者透過這台電腦的網際網路連線來連線」的核取方塊。
 
4. 在「家用網路連線」下拉式選單中，選擇 D3-G 將要連接的乙太網路介面卡（例如「Ethernet」）。

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20AI-G/Available%20Applications/ethernet3.png" width="400"></p>
<p align="center"><strong>圖 6.4 選擇乙太網路介面卡</strong></p><br/>
 
5. 請按一下 **確定** 以儲存設定。

<br/><br/>

### 6.2.2 建立網路設定檔 
1. 透過 DHCP 取得動態 IP
若您的網路提供 DHCP 伺服器（例如路由器或已啟用 ICS 的 Windows PC），則不需要編輯檔案。只要接上乙太網路線，系統就會自動取得 IP 位址。

您只需插上網路線即可立即開始使用網路。請前往第 6.2.4 章「驗證網路連線」。

2. 靜態 IP 設定
若您想指定靜態 IP 位址（例如直接與 PC 連接，或沒有可用的 DHCP 伺服器時），請以下列內容編輯同一個檔案：
```
$ vi /etc/systemd/network/20-wired.network

[Match]
Name=eth0

[Network]
Address=192.168.137.2/24
Gateway=192.168.137.1
DNS=8.8.8.8
```
這會將 IP 位址設為 192.168.137.2，並使用 192.168.137.1 作為閘道（Windows ICS 常見的設定），同時設定 Google DNS。

<br/><br/>

### 6.2.3 重新啟動網路服務
請重新啟動 systemd-networkd 服務以套用新的網路設定：

```
sudo systemctl restart systemd-networkd
```

<br/><br/>

### 6.2.4 驗證網路連線
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20D3-G/Software/host%20pc%20ethernet%20connection.png"width="500"></p>
<p align="center"><strong>圖 6.5 與主機 PC 共用網路</strong></p>
<br/>

請 ping Google 的公用 DNS 伺服器以測試網際網路連線：

```
$ ping 8.8.8.8
PING 8.8.8.8 (8.8.8.8): 56 data bytes
64 bytes from 8.8.8.8: seq=0 ttl=113 time=30.208 ms
64 bytes from 8.8.8.8: seq=1 ttl=113 time=38.143 ms
64 bytes from 8.8.8.8: seq=2 ttl=113 time=30.969 ms
64 bytes from 8.8.8.8: seq=3 ttl=113 time=33.586 ms
```

<br/><br/><br/><br/>

# 7. 40-pin GPIO 接頭
---
D3-G 配備 40-pin GPIO 接頭，可為各種硬體專案提供彈性的 I/O 功能。
此排針相容於通用輸入／輸出（GPIO）操作，可用於連接感測器、LED、按鈕及其他周邊裝置。

每個腳位可依設定支援多種功能，例如數位 I/O、PWM、I2C、SPI 與 UART。

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/d3g/Assets/TOPST%20D3-G/Software/d3-g%20gpio%2040pinmap.png" width="800"></p>
<p align="center"><strong>圖 7.1 D3-G 的 40-pin GPIO 接頭腳位圖 </strong></p> <br/>

**註**：連接外部硬體前，請參閱官方腳位圖以瞭解詳細的腳位功能與電壓準位。

<br/><br/><br/>

## 7.1 GPIO 數位輸入／輸出
---
D3-G 透過 40-pin 接頭支援數位輸入與輸出（GPIO），讓您能與按鈕、LED 與感測器等外部裝置互動。 

### 7.1.1 LED
---
控制 LED 是最簡單也最常見的 GPIO 輸出範例之一。  
本節示範如何使用 D3-G 連接並使用 LED 感測器。

#### 步驟 1. 硬體需求
- D3-G 開發板（x1）
- 麵包板 (x1)
- LED (x1)
- 公對母杜邦線 (x2)
- DC 5V 電源供應器 (x1)
- USB 轉 TTL 序列傳輸線 (x1)

#### 步驟 2. 範例電路
- LED
    - （+）腳位連接至 D3-G 開發板上的第 12 腳位。
    - （-）腳位連接至 D3-G 開發板上作為 GND 的第 14 腳位。  
    
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20D3-G/Software/led.png"></p>

<p align="center"><strong>圖 7.2 D3-G GPIO LED 電路圖 </strong></p> <br/>

##### 步驟 2.1 腳位對應
下表列出腳位對應。

<div align="center">
  <p><strong>表 7.1 D3-G LED 腳位對應</strong></p>
  <table>
      <tr>
          <th colspan="3">腳位名稱</th>
          <th>D3-G</th>
          <th>GPIO</th>
      </tr>
      <tr>
          <td colspan="3">LED（+）腳位</td>
          <td>12</td>
          <td>89</td>
      </tr>
      <tr>
          <td colspan="3">LED（-）腳位</td>
          <td>14</td>
          <td>GND</td>
      </tr>
  </table>
</div>

#### 步驟 3. 執行方式
若要操作連接至 D3-G 開發板上 GPIO89 的 LED，請執行以下程式碼：

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

#### 步驟 4. 執行結果
請使用下列命令執行程式碼。

```
$ python3 led_test.py
```

此程式會將 GPIO89 設定為數位輸出，並每 1 秒切換一次其狀態。
執行後，連接至 GPIO89 的 LED 會閃爍 10 次，亮 1 秒後再暗 1 秒，如此反覆。經過 10 個循環後，程式會結束並自動取消匯出（unexport）該 GPIO。

若要提前停止程式，請按 **[Ctrl+C]**。
無論是哪一種情況，該腳位都會被正確釋放並清除。

**註**：此設定假設 LED 為直接連接。為了安全與長期運作，強烈建議在 LED 上串聯一顆限流電阻（例如 220Ω），以避免電流過大並保護 GPIO 腳位免於損壞。

<br/><br/><br/><br/>

### 7.1.2 按鈕
---
按壓式按鈕是一種基本的輸入裝置，常用於示範透過 GPIO 處理數位輸入。
本節示範如何在 D3-G 上連接並使用基本的按鈕模組。

#### 步驟 1. 硬體需求
- D3-G 開發板（x1）
- 麵包板 (x1)
- 按鈕 (x1)
- 公對母杜邦線 (x2)
- DC 5V 電源供應器 (x1)
- USB 轉 TTL 序列傳輸線 (x1)

#### 步驟 2. 範例電路
- 按鈕開關
    - 按鈕開關的一支接腳連接至 D3-G 開發板上的第 10 腳位。
    - 按鈕上方另一側的接腳連接至 3.3V 腳位。

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20D3-G/Software/button_circuit.png"></p> 
<p align="center"><strong>圖 7.3 D3-G GPIO 按鈕電路圖</strong></p>

##### 步驟 2.1 腳位對應
下表列出腳位對應。

<div align="center">
  <p><strong>表 7.2 D3-G 按鈕腳位對應</strong></p>
  <table>
      <tr>
          <th colspan="3">腳位名稱</th>
          <th>D3-G</th>
          <th>GPIO</th>
      </tr>
      <tr>
          <td colspan="3">按鈕的一支接腳</td>
          <td>10</td>
          <td>88</td>
      </tr>
  </table>
</div>

#### 步驟 3. 執行方式
若要監控連接至 D3-G 開發板上 GPIO88 的按鈕輸入，請執行以下程式碼：

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

#### 步驟 4. 執行結果
請使用下列命令執行程式碼。
```
$ python3 test_button.py
```
此程式會將 GPIO88 設定為數位輸入，並即時持續監控其數值。
執行後，按下連接至 GPIO88 的按鈕時，會列印訊息表示按鈕已被按下。

若要停止程式，請按 **[Ctrl+C]**。
程式終止時，GPIO88 會自動取消匯出並清除。

**註**：此處以 GPIO88 為例。您可依據 40-pin 接頭的腳位配置，使用 D3-G 上任何可用的 GPIO 腳位。
請參閱官方腳位圖，並選擇符合您硬體設定的 GPIO 編號。

<br/><br/><br/><br/>

### 7.1.3 觸控感測器
---
觸控感測器可用於偵測人體觸碰，並透過 GPIO 作為數位輸入訊號。
本節示範如何使用 D3-G 連接基本的觸控感測器模組並讀取其輸入。

#### 步驟 1. 硬體需求
- D3-G 開發板（x1）
- 觸控感測器 (x1)
- 母對母杜邦線（x3）
- DC 5V 電源供應器 (x1)
- USB 轉 TTL 序列傳輸線 (x1)

#### 步驟 2. 範例電路
- 觸控感測器
    - 觸控感測器的 SIG 腳位連接至 D3-G 開發板上的第 88 腳位。
    - 觸控感測器的 VCC 腳位連接至 D3-G 開發板上的 3.3V。
    - 觸控感測器的 GND 腳位連接至 D3-G 開發板上的 GND。


<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20D3-G/Software/touch%20circuit.png"></p>
<p align="center"><strong>圖 7.4 D3-G GPIO 觸控感測器電路圖</strong></p>

##### 步驟 2.1 腳位對應
下表列出腳位對應。

<div align="center">
  <p><strong>表 7.3 D3-G 觸控感測器腳位對應</strong></p>
  <table>
      <tr>
          <th colspan="3">腳位名稱</th>
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

#### 步驟 3. 執行方式
若要監控連接至 D3-G 開發板上 GPIO88 的觸控感測器，只需執行以下程式碼：
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

#### 步驟 4. 執行結果
請使用下列命令執行程式碼。

```
$ python3 touch_test.py
```

此程式會將 GPIO88 設定為數位輸入，並即時持續監控其數值。

執行後，觸碰感測器會使終端機列印如下訊息：
```
touch detected.
```
未觸碰感測器時，輸出將為：
```
touch released.
```
若要停止程式，請按 **[Ctrl+C]**。
程式終止時，GPIO88 會自動取消匯出並清除。

**註**：此處以 GPIO88 為例。您可依據 40-pin 接頭的腳位配置，使用 D3-G 上任何可用的 GPIO 腳位。
請參閱官方腳位圖，並選擇符合您硬體設定的 GPIO 編號。

<br/><br/><br/><br/>

### 7.1.4 振動偵測感測器
---
振動感測器可用於偵測實體衝擊或振動，並透過 GPIO 輸出數位輸入訊號。
本節示範如何使用 D3-G 連接基本的振動感測器模組並偵測其輸入。

#### 步驟 1. 硬體需求
- D3-G 開發板（x1）
- 震動偵測感測器 (x1)
- 母對母杜邦線 (x4)
- DC 5V 電源供應器 (x1)
- USB 轉 TTL 序列傳輸線 (x1)

#### 步驟 2. 範例電路
- 震動偵測感測器
    - 振動偵測感測器的 VCC 腳位連接至 D3-G 開發板上的 3.3V 腳位。
    - 振動偵測感測器的 GND 腳位連接至 D3-G 開發板上的 GND。
    - 振動偵測感測器的 DO 腳位連接至 D3-G 開發板上的第 88 腳位。

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20D3-G/Software/vibr%20circuit.png"></p>
<p align="center"><strong>圖 7.5 D3-G GPIO 振動偵測感測器電路圖</strong></p>

##### 步驟 2.1 腳位對應
下表列出腳位對應。

<div align="center">
  <p><strong>表 7.4 D3-G 振動偵測感測器腳位對應</strong></p>
  <table>
      <tr>
          <th colspan="3">腳位名稱</th>
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

#### 步驟 3. 執行方式
若要監控連接至 D3-G 開發板上 GPIO88 的振動感測器，請執行以下程式碼：
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

#### 步驟 4. 執行結果
請使用下列命令執行程式碼。

```
$ python3 vibration_test.py
```

此程式會將 GPIO88 設定為數位輸入，並即時持續監控其數值。
執行後，感測器偵測到振動或衝擊時，會使終端機列印如下訊息：
```
vibration detected.
```
沒有振動時，輸出將為：
```
no vibration detected.
```
若要停止程式，請按 **[Ctrl+C]**。
終止後，GPIO88 會自動取消匯出並清除。

**註**：此處以 GPIO88 為例。您可依感測器的接線與接頭配置，使用其他任何可用的 GPIO 腳位。選擇 GPIO 編號前，請參閱 D3-G 的腳位圖。

<br/><br/><br/><br/>

### 7.1.5 紅外線感測器（SZH-SSBH-002）
---
紅外線感測器可藉由感測反射的紅外線來偵測附近的障礙物，並透過 GPIO 輸出數位訊號。
本節示範如何使用 D3-G 連接 SZH-SSBH-002 紅外線感測器並讀取其輸入。

#### 步驟 1. 硬體需求
- D3-G 開發板（x1）
- 麵包板 (x1)
- 紅外線感測器（x1）
- 公對母杜邦線（x5）
- DC 5V 電源供應器 (x1)
- USB 轉 TTL 序列傳輸線 (x1)

#### 步驟 2. 範例電路
- 紅外線感測器
    - 紅外線感測器的 VCC 腳位連接至 D3-G 開發板上的 3.3V 腳位。
    - 紅外線感測器的 GND 腳位連接至 D3-G 開發板上的 GND。
    - 紅外線感測器的 OUT 腳位連接至 D3-G 開發板上的第 89 腳位。


<p align="center">
  <img src="https://raw.githubusercontent.com/topst-development/Documentation/d3g/Assets/TOPST%20D3-G/Software/szh-ssbh-002_circuit.png">
</p> 
<p align="center"><strong>圖 7.6 IR 感測器實驗電路</strong></p>

##### 步驟 2.1 腳位對應
下表列出腳位對應。

<div align="center">
  <p><strong>表 7.5 D3-G IR 感測器腳位對應</strong></p>
  <table>
      <tr>
          <th colspan="3">腳位名稱</th>
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

#### 步驟 3. 執行方式
若要監控連接至 D3-G 開發板上 GPIO89 的 IR 感測器，請執行以下程式碼：

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

#### 步驟 4. 執行結果
請使用下列命令執行程式碼。
```
$ python3 ir_test.py
```
此程式會將 GPIO89 設定為數位輸入，並持續監控其狀態以偵測障礙物。
當 IR 感測器前方偵測到物體時，終端機會顯示：
```
obstacle detected.
```
未偵測到物體時，則顯示：
```
no obstacle detected.
```
若要停止程式，請按 **[Ctrl+C]**。
程式終止時，GPIO89 會自動取消匯出並清除。

**註**：本程式以 GPIO89 為例。
您可依 D3-G 的 40-pin 接頭，使用任何可用的 GPIO 腳位。請參閱官方腳位圖以正確選擇腳位。

<br/><br/><br/><br/>

### 7.1.6 光敏電阻（SZH-SSBH-011）
---
光敏電阻可用於偵測環境光線強度，並在光線強度超過特定門檻時透過 GPIO 輸出數位訊號。
本節示範如何使用 D3-G 連接 SZH-SSBH-011 光敏電阻感測器並讀取其輸入。

#### 步驟 1. 硬體需求
- D3-G 開發板（x1）
- 光敏電阻模組（SZH-SSBH-011）（x1）
- LED (x1)
- 220Ω 電阻（x1）
- 麵包板 (x1)
- 公對母杜邦線（x7）
- DC 5V 電源供應器 (x1)
- USB 轉 TTL 序列傳輸線 (x1)

#### 步驟 2. 範例電路
- 光敏電阻（SZH-SSBH-011）
    - 光敏電阻的 VCC 腳位連接至 D3-G 開發板上的 3.3V 腳位。
    - 光敏電阻的 GND 腳位連接至 D3-G 開發板上的 GND。
    - 光敏電阻的 DO 腳位連接至 D3-G 開發板上的第 89 腳位。
- LED
    - LED 的（+）腳位連接至 D3-G 開發板上的 GND。
    - LED 的（-）腳位連接至 D3-G 開發板上的第 83 腳位。

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20D3-G/Software/circuit.png"></p>
<p align="center"><strong>圖 7.7 光敏電阻實驗電路</strong></p>

##### 步驟 2.1 腳位對應
下表列出腳位對應。

<div align="center">
  <p><strong>表 7.6 D3-G 光敏電阻腳位對應</strong></p>
  <table>
      <tr>
          <th colspan="3">腳位名稱</th>
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
  <p><strong>表 7.7 D3-G LED 腳位對應</strong></p>
  <table>
      <tr>
          <th colspan="3">腳位名稱</th>
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

### 步驟 3. 執行方式
請執行以下 Python 程式，以使用 CDS 感測器監控亮度並據以控制 LED：

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

### 步驟 4. 執行結果
請使用下列命令執行程式碼。
```
$ python3 CDS_test.py
```
此程式會將 GPIO89 設定為光敏電阻感測器的輸入，並將 GPIO83 設定為 LED 的輸出。
偵測到環境光線時，終端機會列印：
```
sensor value: 0
brightness detected. Turning on the LED.
```
接著 LED 會亮起。
未偵測到光線時，則列印：
```
sensor value: 1
no brightness detected. Turning off the LED.
```
接著 LED 會熄滅。
若要停止程式，請按 **[Ctrl+C]**。
程式終止時，兩個 GPIO 腳位都會自動取消匯出並清除。

**註**：本範例使用 GPIO83 與 GPIO89。您可依 D3-G 的 40-pin 接頭配置，使用任何可用的 GPIO 腳位。請參閱官方腳位圖以正確選擇腳位。

<br/><br/><br/><br/>

### 7.1.7 空氣污染偵測感測器
---
空氣污染偵測感測器可用於監測環境中是否存在有害氣體或懸浮微粒，並透過 GPIO 輸出數位訊號。
本節示範如何使用 D3-G 連接空氣污染偵測感測器並讀取其輸入。

#### 步驟 1. 硬體需求
- D3-G 開發板（x1）
- 空氣污染（氣體）偵測感測器模組（x1）
- 麵包板 (x1)
- 公對母杜邦線（x3）
- DC 5V 電源供應器 (x1)
- USB 轉 TTL 序列傳輸線 (x1)

#### 步驟 2. 範例電路
- 空氣污染偵測感測器
    - 空氣污染偵測感測器的 VCC 腳位連接至 D3-G 開發板上的 3.3V 腳位。
    - 空氣污染偵測感測器的 GND 腳位連接至 D3-G 開發板上的 GND。
    - 空氣污染偵測感測器的 DO 腳位連接至 D3-G 開發板上的第 88 腳位。

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20D3-G/Software/gas%20circuit.png"></p>
<p align="center"><strong>圖 7.8 空氣污染偵測感測器實驗電路</strong></p>

##### 步驟 2.1 腳位對應
下表列出腳位對應。

<div align="center">
  <p><strong>表 7.8 D3-G 空氣污染偵測感測器腳位對應</strong></p>
  <table>
      <tr>
          <th colspan="3">腳位名稱</th>
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

#### 步驟 3. 執行方式
請執行以下 Python 程式，以使用 GPIO88 腳位監控氣體偵測狀態：

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

#### 步驟 4. 執行結果
請使用下列命令執行程式碼。
```
$ python3 gas_sensor_test.py
```
此程式會將 GPIO88 設定為數位輸入，並持續監控氣體偵測狀態。
當氣體濃度達到感測器的門檻值時，終端機會顯示：
```
gas detected.
```
未偵測到氣體時，終端機會顯示：
```
no gas detected.
```
若要停止程式，請按 **[Ctrl+C]**。
程式終止時，GPIO88 會自動取消匯出並清除。

**註**：此處以 GPIO88 為例。您可依 D3-G 的 40-pin 接頭配置，使用任何可用的 GPIO 腳位。請參閱官方腳位圖以正確選擇腳位。

<br/><br/><br/><br/>

### 7.1.8 超音波感測器
---
超音波感測器可藉由發射超音波並接收反射訊號來測量與鄰近物體的距離，再透過 GPIO 輸出數位（或脈衝式）訊號。
本節示範如何使用 D3-G 連接超音波感測器並讀取其輸入。

#### 步驟 1. 硬體需求
- D3-G 開發板（x1）
- 超音波感測器（x1）
- 母對母杜邦線（x4）
- DC 5V 電源供應器 (x1)
- USB 轉 TTL 序列傳輸線 (x1)

#### 步驟 2. 範例電路
- 超音波感測器
    - 超音波感測器的 VCC 腳位連接至 D3-G 開發板上的 5V 腳位。
    - 超音波感測器的 GND 腳位連接至 D3-G 開發板上的 GND。
    - 超音波感測器的 TRIG 腳位連接至 D3-G 開發板上的第 82 腳位。
    - 超音波感測器的 ECHO 腳位連接至 D3-G 開發板上的第 88 腳位。

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20D3-G/Software/ultra%20circuit.png"></p>
<p align="center"><strong>圖 7.9 超音波感測器實驗電路</strong></p>

##### 步驟 2.1 腳位對應
下表列出腳位對應。

<div align="center">
  <p><strong>表 7.9 D3-G 超音波感測器腳位對應</strong></p>
  <table>
      <tr>
          <th colspan="3">腳位名稱</th>
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

#### 步驟 3. 執行方式
請執行以下 Python 程式，以使用超音波感測器測量距離：
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

#### 步驟 4. 執行結果
請使用下列命令執行程式碼。
```
$ python3 ultrasonic_sensor_test.py
```
此程式會將 GPIO82 設定為數位輸出以觸發超音波脈衝，並將 GPIO88 設定為數位輸入以接收回波。
程式執行時，會每秒列印感測器前方最近物體的距離，例如：
```
Distance: 23.45 cm
Distance: 24.12 cm
...
```
若要停止程式，請按 **[Ctrl+C]**。
程式終止時，GPIO82 與 GPIO88 會自動取消匯出並清除。

**註**：此處以 GPIO82 與 GPIO88 為例。您可依 D3-G 的 40-pin 接頭配置，使用任何可用的 GPIO 腳位。請參閱官方腳位圖以正確選擇腳位。此外，請確認您的 ECHO 腳位電壓準位對 D3-G 而言是安全的（部分模組輸出 5V，可能需要分壓電路或準位轉換器）。

<br/><br/><br/><br/>

## 7.2 I2C
---
D3-G 透過 40-pin GPIO 接頭提供 I2C 通訊，可與感測器、顯示器與擴充模組等各種周邊裝置介接。
Inter-integrated Circuit（I2C）是一種雙線式通訊協定，由資料線（SDA）與時脈線（SCL）組成，可讓多個裝置透過共用匯流排進行通訊。

I2C 通訊採用主從式架構，由一個主控裝置控制通訊，同一匯流排上最多可連接 127 個從屬裝置。
SDA 線同時用於傳送與接收資料，SCL 線則負責同步資料傳輸的時序。這種同步通訊模式可讓裝置以協調且由時脈驅動的方式交換資訊。

<br/><br/><br/><br/>

### 7.2.1 1602A LCD 顯示器
---
1602A LCD 是嵌入式系統中常用的字元顯示模組。
在 D3-G 上，可將 LCD 的 SDA 與 SCL 線連接至設定為 I2C 的 GPIO 腳位。連接完成後，即可使用 Linux I2C 工具或自訂軟體控制此 LCD。

#### 步驟 1. 硬體需求
- D3-G 開發板（x1）
- 1602A I2C LCD 模組（x1）
- 母對母杜邦線（x4）
- DC 5V 電源供應器 (x1)
- USB 轉 TTL 序列傳輸線（x1）  

請確認 LCD 模組具備 I2C 轉接板

#### 步驟 2. 範例電路
- I2C LCD 模組
    - I2C LCD 模組的 GND 腳位連接至 D3-G 開發板上的 GND 腳位。
    - I2C LCD 模組的 VCC 腳位連接至 D3-G 開發板上的 5V。
    - I2C LCD 模組的 SDA 腳位連接至 D3-G 開發板上的第 82 腳位。
    - I2C LCD 模組的 SCL 腳位連接至 D3-G 開發板上的第 81 腳位。

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20D3-G/Software/lcd_circuit.png"></p>
<p align="center"><strong>圖 7.10 D3-G I2C LCD 模組電路圖  </strong></p>

##### 步驟 2.1 腳位對應
下表列出腳位對應。

<div align="center">
  <p><strong>表 7.10 D3-G I2C LCD 模組腳位對應</strong></p>
  <table>
      <tr>
          <th colspan="3">腳位名稱</th>
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

#### 步驟 3. 執行方式
請先安裝所需的 Python 函式庫：
```
$ pip install RPLCD smbus2
```
接著使用以下 Python 程式碼將文字寫入 LCD：
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

#### 步驟 4. 執行結果
請使用下列命令執行程式碼。
```
$ python3 lcd_test.py
```
此程式會使用 RPLCD 函式庫初始化以 I2C 連接的 1602A LCD，並在螢幕上顯示使用者輸入的文字。
執行此程式時，系統會提示您輸入一段字串。該文字會在 LCD 上顯示 4 秒後清除。例如：
```
Enter text to display on LCD: Hello D3-G!
```
LCD 將顯示：
```
Hello D3-G!
```
接著在 4 秒後清除。

若要停止程式，請按 **[Ctrl+C]**。

**註** ：在 D3-G 上，GPIO82 與 GPIO81 預設用於 I2C。
請確認 I2C 位址（0x27）與您的 LCD 模組相符。必要時可使用 **i2cdetect -y 3** 掃描 I2C 裝置。

<br/><br/><br/><br/>

## 7.3 SPI
---
D3-G 透過 40-pin GPIO 接頭支援序列周邊介面（SPI）通訊，可在外部裝置與 D3-G 之間交換資料。

SPI 是一種同步序列通訊協定，可實現全雙工通訊，意即資料能同時傳送與接收。它使用四條主要訊號線：Master Out Slave In（MOSI）、Master In Slave Out（MISO）、Serial Clock（SCLK）與 Chip Select（CS）。

與 I2C 讓多個裝置共用訊號線不同，SPI 需要為每個從屬裝置配置獨立的 CS 線。這種一對多的結構使 SPI 快速且易於實作，但在連接多個裝置時可能需要較多的實體接線。

<br/><br/><br/><br/>

### 7.3.1 點矩陣
---
8x8 點矩陣顯示器常用於嵌入式系統中的簡易文字或圖案輸出。在 D3-G 上，可透過 SPI 並搭配 MAX7219 之類的驅動晶片來控制點矩陣模組。

MAX7219 會在內部處理列與行的掃描，讓微控制器只需使用少數幾條 SPI 訊號即可控制整個顯示器：MOSI（DIN）、SCLK 與 CS（LOAD）。連接完成後，即可透過使用者自訂的程式或函式庫，以 SPI 通訊控制此顯示器。

#### 步驟 1. 硬體需求
- D3-G 開發板（x1）
- 點矩陣（x1）
- 公對母杜邦線（x4）
- DC 5V 電源供應器 (x1)
- USB 轉 TTL 序列傳輸線 (x1)

#### 步驟 2. 範例電路
- 點矩陣
    - 點矩陣的 VCC 腳位連接至 D3-G 開發板上的 5V 腳位。
    - 點矩陣的 GND 腳位連接至 D3-G 開發板上的 GND 腳位。
    - 點矩陣的 DIN 腳位連接至 D3-G 開發板上的第 120 腳位。
    - 點矩陣的 CS 腳位連接至 D3-G 開發板上的第 119 腳位。
    - 點矩陣的 CLK 腳位連接至 D3-G 開發板上的第 118 腳位。

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20D3-G/Software/dot%20circuit.png"></p>
<p align="center"><strong>圖 7.11 D3-G 點矩陣模組電路圖  </strong></p>

##### 步驟 2.1 腳位對應
下表列出腳位對應。
<div align="center">
  <p><strong>表 7.11 D3-G 點矩陣腳位對應</strong></p>
  <table>
      <tr>
          <th colspan="3">腳位名稱</th>
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

#### 步驟 3. 執行方式
以下 Python 程式示範如何透過 /dev/spidev3.0 使用低階 fcntl 呼叫直接控制 MAX7219。此方法適用於沒有外部 SPI 函式庫的裝置：
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

#### 步驟 4. 執行結果
請使用下列命令執行程式碼。
```
$ python3 dot_matrix_test.py
```
此程式會初始化以 SPI 連接的 MAX7219 點矩陣顯示器，並提示您輸入一個值。程式會依輸入的內容在 8x8 LED 矩陣上顯示對應的圖案。

程式執行時，您會看到：
```
Enter a number, an uppercase letter (0-9, A-Z), 'Smile', 'Dance', 'Angry', 'Good', 'Nice', 'Emotion':
```
範例：
- 輸入 A 會顯示字母 A。
- 輸入 Smile 會顯示笑臉圖案。
- 輸入 Dance 會觸發交替的舞動動畫。
- 輸入 Nice 會依序顯示 N-I-C-E 的字母動畫。

若要停止程式，請按 **[Ctrl+C]**。
終止時，SPI 裝置會安全關閉，LED 矩陣也會停止更新。

**註**：請確認 /dev/spidev3.0 存在，且接線符合腳位對應表。此外，請以穩定的 5V 電源供電給 MAX7219 模組。

<br/><br/><br/><br/>

## 7.4 PWM
---
脈衝寬度調變（PWM）透過改變脈衝訊號的寬度來控制 LED、馬達與蜂鳴器等裝置。D3-G 在 Linux 中透過 sysfs 介面支援 PWM。

### 7.4.1 LED 亮度控制
---
本範例示範如何在 D3-G 上使用 PWM 控制 LED 的亮度。

#### 步驟 1. 硬體需求
- D3-G 開發板（x1）
- LED (x1)
- 公對母杜邦線（x2）
- 麵包板
- DC 5V 電源供應器 (x1)
- USB 轉 TTL 序列傳輸線 (x1)

#### 步驟 2. 範例電路
- LED
    - LED 的 (+) 腳位連接到 D3-G 開發板的 pin 89。
    - LED 的 (-) 腳位連接到 D3-G 開發板的 GND 腳位。

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20D3-G/Software/led.png"></p>
<p align="center"><strong>圖 7.12 D3-G LED 電路圖  </strong></p>

##### 步驟 2.1 腳位對應
下表列出腳位對應。

<div align="center">
  <p><strong>表 7.12 D3-G LED 腳位對應</strong></p>
  <table>
      <tr>
          <th colspan="3">腳位名稱</th>
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

#### 步驟 3. 執行方式
若要操作連接到 D3-G 開發板 GPIO89 的 LED（PWM），請執行以下程式碼：
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

#### 步驟 4. 執行結果
請使用下列命令執行程式碼。
```
$ python3 led_pwm.py
```
此腳本會初始化 LED 腳位上的 PWM，並持續讓 LED 亮度漸亮與漸暗。

執行腳本後，您會看到如下輸出：
```
Starting LED PWM control (press Ctrl+C to stop)
```
LED 會反覆逐漸變亮再變暗，模擬「呼吸」效果。

若要停止程式，請按 **[Ctrl+C]**。

**註**：請確認該 PWM 通道尚未被使用，且 D3-G 在所選的 GPIO 上支援硬體 PWM。若 PWM 未啟動，請檢查 /sys/class/pwm/ 中的 export、period 與 duty_cycle 設定。

<br/><br/><br/><br/>

### 7.4.2 迷你伺服馬達
---
迷你伺服馬達可透過 GPIO 的脈衝寬度調變（PWM）訊號來控制精確的角度運動。
本節示範如何使用 D3-G 連接並控制迷你伺服馬達。

#### 步驟 1. 硬體需求
- D3-G 開發板（x1）
- 伺服馬達（x1）
- 公對母杜邦線（x3）
- DC 5V 電源供應器 (x1)
- USB 轉 TTL 序列傳輸線 (x1)

#### 步驟 2. 範例電路
- 伺服馬達
    - 伺服馬達的 VCC 腳位連接到 D3-G 開發板的 5V。
    - 伺服馬達的 GND 腳位連接到 D3-G 開發板的 GND。
    - 伺服馬達的 SIG 腳位連接到 D3-G 開發板的 pin 89。

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20D3-G/Software/motor_circuit.png"p>
<p align="center"><strong>圖 7.13 D3-G 伺服馬達電路圖  </strong></p>

##### 步驟 2.1 腳位對應
下表列出腳位對應。

<div align="center">
  <p><strong>表 7.13 D3-G 伺服馬達腳位對應</strong></p>
  <table>
      <tr>
          <th colspan="3">腳位名稱</th>
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

#### 步驟 3. 執行方式
以下 Python 腳本示範如何在 D3-G 上透過 sysfs 介面使用 PWM 直接控制迷你伺服馬達。此方法不需要任何外部函式庫，並可對角度定位進行精細控制。
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

#### 步驟 4. 執行結果
請使用下列命令執行程式碼。
```
$ python3 motor_test.py
```
此腳本會依據目標角度調整工作週期（duty cycle），以 PWM 控制迷你伺服馬達。
執行後，畫面會出現以下提示：
```
Enter 1 (CW) or 0 (CCW), q to quit:
```
輸入 1 會讓伺服馬達順時針旋轉至 180°，輸入 0 則會讓伺服馬達逆時針旋轉至 0°。您可以視需要重複操作。

若要停止腳本，請輸入 **[q]** 或按下 **[Ctrl+C]**。腳本接著會停用並取消匯出（unexport）該 PWM 通道。

**註**：請確認您的伺服馬達支援 50 Hz PWM 訊號，並在 1 ms 至 2 ms 的工作脈衝範圍內運作，以確保安全。
