## 支援的相機模組
<div align="center">
    <table>
        <tr>
            <td colspan="8" align="center"><strong>開發板</strong></td>
            <td align="center"><strong>型號</strong></td>
            <td align="center"><strong>感測器</strong></td>
            <td align="center"><strong>感測器解析度</strong></td>
            <td align="center"><strong>預設解析度</strong></td>
            <td align="center"><strong>影格率</strong></td>
            <td align="center"><strong>預設視訊路徑</strong></td>
            <td align="center"><strong>備註</strong></td>
        </tr>
        <tr>
            <td rowspan="4" align="center"><strong>D3-G</strong></td>
            <td colspan="8">Arducam OV5647</td>
            <td>OV5647</td>
            <td>2592x1944 pixels(5MP)</td>
            <td>1296x972</td>
            <td>30FPS</td>
            <td>/dev/video0</td>
            <td>預設選取的攝影機</td>
        </tr>
        <tr>
            <td colspan="8">Raspberry Pi Camera v1</td>
            <td>OV5647</td>
            <td>2592x1944 pixels(5MP)</td>
            <td>1296x972</td>
            <td>30FPS</td>
            <td>/dev/video0</td>
            <td>預設選取的攝影機</td>
        </tr>
        <tr>
            <td colspan="8">Raspberry Pi Camera v2</td>
            <td>IMX219</td>
            <td>3280x2464 pixels(8MP)</td>
            <td>1640x1232</td>
            <td>30FPS</td>
            <td>/dev/video0</td>
            <td>預設為停用。若要啟用，請參閱下方指南。</td>
        </tr>
        <tr>
            <td colspan="8">SEKONIX CXD5700</td>
            <td>CXD5700</td>
            <td>1920x1080 pixels(2MP)</td>
            <td>1920x1080</td>
            <td>30FPS</td>
            <td>/dev/video0,1,2,3</td>
            <td>預設為停用。若要啟用，請參閱下方指南。</td>
        </tr>
        <tr>
            <td rowspan="4" align="center"><strong>AI-G</strong></td>
            <td colspan="8">Arducam OV5647</td>
            <td>OV5647</td>
            <td>2592x1944 pixels(5MP)</td>
            <td>1296x972</td>
            <td>30FPS</td>
            <td>/dev/video2</td>
            <td>預設選取的攝影機</td>
        </tr>
        <tr>
            <td colspan="8">Raspberry Pi Camera v1</td>
            <td>OV5647</td>
            <td>2592x1944 pixels(5MP)</td>
            <td>1296x972</td>
            <td>30FPS</td>
            <td>/dev/video2</td>
            <td>預設選取的攝影機</td>
        </tr>
        <tr>
            <td colspan="8">Raspberry Pi Camera v2</td>
            <td>IMX219</td>
            <td>3280x2464 pixels(8MP)</td>
            <td>1640x1232</td>
            <td>30FPS</td>
            <td>/dev/video2</td>
            <td>預設為停用。若要啟用，請參閱下方指南。</td>
        </tr>
        <tr>
            <td colspan="8">SEKONIX CXD5700</td>
            <td>CXD5700</td>
            <td>1920x1080 pixels(2MP)</td>
            <td>1920x1080</td>
            <td>30FPS</td>
            <td>/dev/video0,1,2</td>
            <td>預設為停用。若要啟用，請參閱下方指南。</td>
        </tr>
    </table>
</div>

# 1. 簡介
本指南旨在協助工程師於 TOPST D3-G 與 AI-G 平台上快速啟用攝影機輸入，並針對 AI 視覺工作負載進行快速的初步驗證。本指南期望降低初始設定的複雜度，包括硬體連接、device tree 設定、驅動程式與管線準備，並提供一條從開機到取得第一個視訊影格、最終完成第一次推論的清晰且可重現的路徑。

## 1.1 範圍
- **支援的介面：** MIPI CSI-2、GMSL（以 SerDes 為基礎）、USB UVC
- **軟體元件：** 以 Yocto 為基礎的 BSP 設定、device tree overlay、V4L2、GStreamer、OpenCV，以及與 D3-G 和 AI-G SDK 的整合
- **適用使用案例：** 機器人、無人機，以及檢測、安全監控與物件追蹤等工業自動化應用
- **不在範圍內的項目：** 攝影機 ISP 調校、進階校正流程（立體視覺／IMU），以及完整的端對端應用程式框架

## 1.2 適用對象
- 為 PoC 或試行開發而將攝影機整合至 D3-G 或 AI-G 平台的嵌入式與 AI 工程師
- 部署或驗證依賴多攝影機管線之系統的系統整合商
- 需要可重複、實作導向環境以進行教學與實驗的教育人員與實驗室使用者

## 1.3 本指南的結構
- **硬體連接：** 接頭腳位、通道（lane）設定、電源與接地需求、線材處理準則，以及參考接線圖
- **軟體設定：** 包含驅動程式與 device tree 設定的 BSP 建置，以及透過 udev 與 V4L2 驗證裝置的方法
- **管線與範例：** 用於單一與多攝影機預覽及擷取的 GStreamer 與 OpenCV 指令和指令碼
- **疑難排解：** 常見問題、典型的 dmesg 樣式、I²C 探測技巧、時序相關問題，以及效能驗證方法

## 1.4 先決條件
- **硬體：** TOPST D3-G 或 AI-G 開發板、支援的相機模組，以及所需的線材／轉接器（MIPI FPC、GMSL 用同軸線、USB 3.0 等）
- **主機工具：** 序列主控台存取、SSH 用戶端，以及基本的建置／除錯公用程式
- **技術背景：** 熟悉 Linux shell 操作、V4L2 公用程式，以及基本的 device tree 概念
- **映像檔／SDK：** D3-G、AI-G BSP 映像檔（d3-g 版本 ≥ v1.3.0，ai-g 版本 ≥1.1.0）
  

# 2. 攝影機介面概觀
第 2 章分別說明 D3-G 與 AI-G 開發板所支援的攝影機類型。  
表 2.1 列出 D3-G 與 AI-G 平台的開發板支援矩陣。

<p align="center"><strong>表 2.1 開發板支援矩陣</strong></p>
<div align="center">
    <table>
        <tr>
            <td colspan="3" align="center"><strong>項目</strong></td>
            <td align="center"><strong>D3-G</strong></td>
            <td align="center"><strong>AI-G</strong></td>
        </tr>
        <tr>
            <td colspan="3">作業系統支援</td>
            <td>Yocto, Ubuntu(desktop)</td>
            <td>Yocto, Ubuntu(Headless)</td>
        </tr>
        <tr>
            <td colspan="3">MIPI CSI-2</td>
            <td>2-4 lanes, 2.1 Gbps/lane x2</td>
            <td>2-4 lanes, 1.5 Gbps/lane x1</td>
        </tr>
        <tr>
            <td colspan="3">GMSL (SerDes)</td>
            <td>TOPST 4ch SerDes carrier</td>
            <td>TOPST 4ch SerDes carrier</td>
        </tr>
        <tr>
            <td colspan="3">USB (UVC)</td>
            <td>USB2.0/USB3.0 </td>
            <td>不支援</td>
        </tr>
    </table>
</div>

## 2.1 MIPI 攝影機概觀
MIPI 攝影機是一種以影像感測器為基礎的相機模組，透過 **MIPI CSI-2 (Mobile Industry Processor Interface – Camera Serial Interface 2)** 標準直接連接至處理器。它是智慧型手機、嵌入式開發板與 AI 攝影機系統中最廣泛使用的攝影機介面，具備低功耗、高頻寬與低延遲等優點。  
MIPI CSI-2 攝影機通常直接將 RAW Bayer 感測器輸出提供給系統，影像訊號處理 (ISP) 則由 SoC 內部的 ISP 或外部 ISP 負責。與 USB 攝影機不同，MIPI 感測器需要透過 I2C 暫存器設定進行初始化，並建立 ISP 管線，但相對地，它能充分發揮感測器效能，實現高品質的影像處理。  
MIPI 攝影機廣泛應用於嵌入式平台，原因如下：
- **高頻寬：** 採用 2-lane 或 4-lane 設定時，MIPI 攝影機可穩定傳輸高解析度 (4K 以上) 與高影格率的資料。
- **低功耗：** 專為行動與嵌入式裝置設計，耗電量明顯低於其他方案。
- **直接控制感測器：** 曝光、增益與影格率等感測器參數可透過 I2C 控制，能細緻調整影像品質。
- **低延遲：** 由於直接傳送 RAW 資料，MIPI 攝影機適合機器人與嵌入式視覺系統等即時應用。
- **感測器選擇豐富：** 眾多感測器——包括 Sony IMX 系列 (IMX219、IMX708 等) 與 Omnivision OV 系列——皆可在相同的 CSI-2 標準下使用。  

MIPI 攝影機使用 **15-pin (2-lane)** 或 **20-pin (4-lane)** 等 FFC 排線接頭，且 lane 設定與腳位對應必須與開發板的 CSI 連接埠相符。  
在以 Linux 為基礎的系統上，必須正確設定感測器驅動程式 (包含 device tree 設定)，攝影機才能被辨識為 /dev/video* 裝置或 Media Controller 節點。偵測到之後，即可透過 V4L2 框架存取視訊串流。  
由於這些特性，MIPI 攝影機已成為高品質影像處理、低延遲串流與 AI 嵌入式視覺應用的實質標準介面。

## 2.2 GMSL 攝影機概觀
GMSL 攝影機是一種序列化的相機模組，採用 Gigabit Multimedia Serial Link (GMSL) 標準，透過單一同軸電纜或遮蔽雙絞線傳輸影像資料、控制訊號與電源。與需要短距離 FFC 連接的 MIPI 攝影機不同，GMSL 使用序列器與解序列器 (SerDes) 配對，將 CSI-2 影像資料傳送至數公尺之外，實現長距離且抗雜訊的攝影機整合。  

GMSL 系統在嵌入式與車用環境中具備下列優點：
- **長距離傳輸：** 支援透過長達約 15 m 的纜線穩定傳送視訊，適合機器人與車輛感測器配置。
- **高頻寬：** GMSL1/2/3 可承載多 Gbps 的 CSI-2 串流，實現高解析度或多攝影機設定。
- **同軸供電 (PoC)：** 以單一纜線同時傳輸電源與資料，可減少接頭數量並簡化系統佈線。
- **穩固性與抗 EMI 能力：** 同軸電纜與差動訊號讓 GMSL 在電氣雜訊環境中依然穩定。
- **標準感測器控制：** 解序列器會將 I2C 通訊轉送至感測器，可進行一般的曝光、增益與影格率設定。

典型的 GMSL 攝影機路徑包含內含序列器的影像感測器、同軸電纜、解序列器，最後將 CSI-2 輸出送至 SoC。在 Linux 上，只要 SerDes 與感測器已正確描述於 device tree 中，攝影機就會像一般 MIPI 攝影機一樣顯示為 V4L2 或 Media Controller 裝置，但在配置位置與系統設計上具有更大的彈性

## 2.3 USB 攝影機概觀
USB 攝影機是一種透過 USB 2.0 或 USB 3.0 介面連接至系統的數位影像裝置。其主要優點在於遵循標準的 UVC (USB Video Class) 通訊協定，因此不需要專用的驅動程式即可運作。由於 Linux、Windows 與 macOS 等多數作業系統原生支援 UVC，使用者插上攝影機後即可立即取得視訊串流，無須任何額外設定。
  
USB 攝影機廣泛應用於嵌入式平台，原因如下：
- **隨插即用：** 與 MIPI 感測器不同，USB 攝影機不需要感測器初始化、I2C 暫存器設定或 ISP 管線建置；連接後即可立即擷取視訊。
- **高相容性：** 多數 USB 攝影機皆符合 UVC 規格，因此不論製造商或型號，都能以一致的方式運作。
- **豐富的解析度與格式支援：** 常見的 MJPEG、YUYV 與 NV12 等格式皆普遍可用。
- **連接與佈線容易：** USB 纜線可簡化配線，並支援較長的距離，通常可達數公尺。
- **適合嵌入式開發：** 驅動程式相關問題較少，可加快原型開發速度。

在以 Linux 為基礎的系統上，USB 攝影機會自動被偵測並顯示為 /dev/video* 節點。可使用 v4l2-ctl、ffmpeg 與 GStreamer 等標準工具進行視訊擷取與控制。  
許多 USB 攝影機內建 ISP，可在內部處理自動白平衡、自動曝光與色彩校正等影像處理。即使開發板未配備外部 ISP，也能維持穩定的影像品質。由於這些特性，USB 攝影機已成為測試、嵌入式 Linux 開發、機器人與快速原型開發等領域中最簡單且最具彈性的攝影機方案之一。

## 2.4 D3-G 可用的攝影機類型
TOPST D3-G 平台在 Yocto 與 Ubuntu 環境中皆支援相同的攝影機類型。可用的攝影機介面包括 USB、MIPI、GMSL，並依所使用的介面而有些微的設定差異。  
1. **MIPI 攝影機**  
TOPST D3-G 提供兩個 MIPI CSI 連接埠，每個連接埠可連接一台 MIPI 攝影機。MIPI CSI 介面支援兩種接頭格式：
    - **15-pin(2-Lane)：** 適合 OV5647 或 IMX219 等較低頻寬的感測器。
    - **20-pin (4-Lane)：** 適用於高解析度或高影格率的感測器。
2. **GMSL 攝影機**  
GMSL 攝影機支援長距離傳輸，常用於車用與工業應用。若要在 TOPST D3-G 上使用 GMSL，需要下列元件：
    1. 將 **20-pin MIPI CSI (4-Lane)** 連接埠連接至 **TOPST MIPI Gender Board**。
    2. 將 **Deserializer (Des)** 板安裝至 Gender Board 上。
    3. 使用 Fakra 纜線將最多四台 GMSL 攝影機連接至 Des 板。
3. **USB 攝影機**  
USB 攝影機是最簡單的入門方式。連接至開發板上任一 USB 2.0 或 USB 3.0 連接埠後即可自動被辨識，無須額外設定即可使用。  
若該裝置是相容於 V4L2 的 UVC 攝影機，可使用下列指令確認其是否已被偵測到：  
    ``` 
    v4l2-ctl --list-devices
    ```

## 2.4 D3-G 可用的攝影機類型
TOPST AI-G 平台同樣支援多種攝影機輸入介面，但整體設定比 D3-G 更為簡單，並針對高效能 AI 工作負載進行最佳化。請注意，此平台不支援 USB 攝影機，僅提供 MIPI 與 GMSL 輸入。  
1. **MIPI 攝影機**  
TOPST D3-G 提供兩個 MIPI CSI 連接埠，每個連接埠可連接一台 MIPI 攝影機。MIPI CSI 介面支援兩種接頭格式：
    - **15-pin(2-Lane)：** 適合 OV5647 或 IMX219 等較低頻寬的感測器。
    - **20-pin (4-Lane)：** 適用於高解析度或高影格率的感測器。
2. **GMSL 攝影機**  
GMSL 攝影機支援長距離傳輸，常用於車用與工業應用。若要在 TOPST D3-G 上使用 GMSL，需要下列元件：
    1. 將 **20-pin MIPI CSI (4-Lane)** 連接埠連接至 **TOPST MIPI Gender Board**。
    2. 將 **Deserializer (Des)** 板安裝至 Gender Board 上。
    3. 使用 Fakra 纜線將最多四台 GMSL 攝影機連接至 Des 板。

# 3. 攝影機連接指南
第 3 章說明如何將攝影機連接至 D3-G 與 AI-G 開發板。  
本節旨在確保開發板與攝影機正確連接，使攝影機能穩定運作。請依照下列指南連接您要使用的攝影機。

## 3.1 將攝影機連接至 D3-G
請依照下列指南了解如何將 MIPI CSI-2、GMSL 與 USB 攝影機連接至 D3-G。  

### 3.1.1 MIPI CSI-2 攝影機
圖 3.1 顯示 D3-G 上的 MIPI CSI 接頭。D3-G 支援 2 個 MIPI CSI 通道，每個通道設定為 2-lane 介面。4-lane 介面為選用，需使用 20-pin 接頭而非 15-pin 接頭。腳位相關資訊請參閱 D3-G Hardware-User Guide。

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/accessories/Camera/3.1%20MIPI%20CSI%20Connector%20on%20D3-G.png"></p>
<p align="center"><strong>圖 3.1 D3-G 上的 MIPI CSI 接頭</strong></p>

連接 MIPI 攝影機時，請使用 FFC (Flat Flexible Cable)。正確的纜線類型與方向請參閱圖 3.2 與圖 3.3。

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/accessories/Camera/3.2%20FFC%20Type.png"></p>
<p align="center"><strong>圖 3.2 FFC 類型</strong></p>

FFC 排線為 1.0 mm、15-pin 類型，其中一面必須有不同顏色的標示 (藍色或灰色)。插入時應採用 B-Forward Direction 方向。FFC 類型請參閱圖 3.2。

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/accessories/Camera/3.3%20An%20example%20of%20an%20FFC%20connected%20to%20the%20D3-G%20MIPI0%2015-pin%20Connector.png"></p>
<p align="center"><strong>圖 3.3 FFC 連接至 D3-G MIPI0 15-pin 接頭的範例</strong></p>

請確認 FFC 上的 15 個銀色接點與 D3-G MIPI 接頭內的 15 個銀色接點對齊。  
使用 MIPI1 接頭時的連接方式相同；請以與 MIPI0 接頭相同的方式連接。

### 3.1.2 GMSL 攝影機
GMSL 攝影機使用 Fakra 纜線，因此無法直接連接至 D3-G 開發板。必須先透過 Deserializer (Des) 板與 TOPST MIPI Gender Board 連接，再與 D3-G 介接。  
連接架構如下。  

<p align="center"><strong>< D3-G > ↔ < TOPST MIPI Gender Board > ↔ < Des Board > ↔ < GMSL Camera ></strong></p>

GMSL 攝影機必須使用 TOPST MIPI Gender Board，並透過 20-pin MIPI 接頭連接。例如，若您要使用四台 GMSL 攝影機，就必須依圖 3.4 所示，使用 20-pin MIPI 介面進行連接。

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/accessories/Camera/3.4%2020-pin%20MIPI0%20Connector.png"></p>
<p align="center"><strong>圖 3.4 20-pin MIPI0 接頭</strong></p>  

1. 將 D3-G 開發板連接至 TOPST MIPI Gender Board。  
    FFC 排線為 1.0 mm、20-pin 類型，其中一面必須有不同顏色的標示 (藍色或灰色)。插入時應採用 A-Forward Direction 方向。FFC 類型請參閱圖 3.5。  
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/accessories/Camera/3.2%20FFC%20Type.png"></p>
    <p align="center"><strong>圖 3.5 FFC 類型</strong></p>
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/accessories/Camera/3.6%20Anexample%20of%20an%20FFC%20connected%20to%20the%20D3-G%20MIPI0%2020-pin%20Connector.png"></p>
    <p align="center"><strong>圖 3.6 FFC 連接至 D3-G MIPI0 20-pin 接頭的範例</strong></p> 
    請確認 FFC 上的 20 個銀色接點與 D3-G MIPI 接頭內的 20 個銀色接點對齊
    使用 MIPI1 接頭時的連接方式相同；請以與 MIPI0 接頭相同的方式連接。
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/accessories/Camera/3.7%20An%20example%20of%20an%20FFC%20connected%20th%20toe%20TOPST%20MIPI%20Gender%20Board%20MIPI%20Connector.png"></p>
    <p align="center"><strong>圖 3.7 FFC 連接至 TOPST MIPI Gender Board MIPI 接頭的範例</strong></p>
2. 將 Deserializer 板連接至 MIPI Gender Board。  
    請將 MIPI Gender Board 上的 JH2 接頭與 SerDes 板底面的 JH1 接頭接合。
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/accessories/Camera/3.8%20JH2%20Connector.png"></p>
    <p align="center"><strong>圖 3.8 JH2 接頭</strong></p>
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/accessories/Camera/3.9%20JH1%20Connector.png"></p>
    <p align="center"><strong>圖 3.9 JH1 接頭</strong></p>
3. GMSL 攝影機連接
    請依圖 3.10 所示連接攝影機。圖中以兩台攝影機為例，但您可視需要連接一至四台攝影機。
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/accessories/Camera/3.10%20GMSL%20Camera%20Connection.png"></p>
    <p align="center"><strong>圖 3.10 JH2 接頭</strong></p>

### 3.1.3 USB 攝影機
USB 攝影機可連接至 D3-G 上的 USB 2.0 或 USB 3.0 連接埠使用。若使用需要 USB 3.0 規格的 USB 攝影機，請務必連接至 USB 3.0 連接埠。

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/accessories/Camera/3.11%20USB%20Camera%20Connection.png"></p>
<p align="center"><strong>圖 3.11 USB 攝影機連接</strong></p>

## 3.2 將攝影機連接至 AI-G
### 3.2.1 MIPI CSI-2 攝影機
圖 3.12 顯示 AI-G 上的 MIPI CSI 接頭。AI-G 支援 2 個 MIPI CSI 通道，每個通道設定為 2-lane 介面。

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/accessories/Camera/3.12%20MIPI%20CSI%20Connector%20on%20AI-G.png"></p>
<p align="center"><strong>圖 3.12 AI-G 上的 MIPI CSI 接頭</strong></p>

連接 MIPI 攝影機時，請使用 FFC (Flat Flexible Cable)。正確的纜線類型與方向請參閱圖 3.13 與圖 3.14。

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/accessories/Camera/3.2%20FFC%20Type.png"></p>
<p align="center"><strong>圖 3.13 FFC 類型</strong></p>

FFC 排線為 1.0 mm、15-pin 類型，其中一面必須有不同顏色的標示 (藍色或灰色)。插入時應採用 B-Forward Direction 方向。FFC 類型請參閱圖 3.13。

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/accessories/Camera/3.14%20An%20example%20of%20an%20FFC%20connected%20to%20the%20AI-G%20MIPI%2015-pin%20Connector.png"></p>
<p align="center"><strong>圖 3.14 FFC 連接至 AI-G MIPI 15-pin 接頭的範例</strong></p>

請確認 FFC 上的 15 個銀色接點與 AI-G MIPI 接頭內的 15 個銀色接點對齊。

### 3.2.2 GMSL 攝影機
GMSL 攝影機使用 Fakra 纜線，因此無法直接連接至 AI-G 開發板。必須先透過 Deserializer (Des) 板與 TOPST MIPI Gender Board 連接，再與 AI-G 介接。  
連接架構如下。

<p align="center"><strong>< AI-G > ↔ < TOPST MIPI Gender Board > ↔ < Des Board > ↔ < GMSL Camera ></strong></p>

GMSL 攝影機必須使用 TOPST MIPI Gender Board，並透過 20-pin MIPI 接頭連接。例如，若您要使用四台 GMSL 攝影機，就必須依圖 3.15 所示，使用 20-pin MIPI 介面進行連接。

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/accessories/Camera/3.15%2020-pin%20MIPI%20Connector.png"></p>
<p align="center"><strong>圖 3.15 20-pin MIPI 接頭</strong></p>

1. 將 AI-G 開發板連接至 TOPST MIPI Gender Board。  
    FFC 排線為 1.0 mm、20-pin 類型，其中一面必須有不同顏色的標示 (藍色或灰色)。插入時應採用 A-Forward Direction 方向。FFC 類型請參閱圖 3.16。
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/accessories/Camera/3.2%20FFC%20Type.png"></p>
    <p align="center"><strong>圖 3.16 FFC 類型</strong></p>
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/accessories/Camera/3.17%20An%20example%20of%20an%20FFC%20connected%20to%20the%20AI-G%20MIPI%2020-pin%20Connector.png"></p>
    <p align="center"><strong>圖 3.17 FFC 連接至 AI-G MIPI 20-pin 接頭的範例</strong></p>
    請確認 FFC 上的 20 個銀色接點與 AI-G MIPI 接頭內的 20 個銀色接點對齊
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/accessories/Camera/3.18%20An%20example%20of%20an%20FFC%20connected%20to%20the%20TOPST%20MIPI%20Gender%20Board%20MIPI%20Connector.png"></p>
    <p align="center"><strong>圖 3.18 FFC 連接至 TOPST MIPI Gender Board MIPI 接頭的範例</strong></p>
2. 將 Deserializer 板連接至 MIPI Gender Board。  
    請將 MIPI Gender Board 上的 JH2 接頭與 SerDes 板底面的 JH1 接頭接合。
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/accessories/Camera/3.19%20JH2%20Connector.png"></p>
    <p align="center"><strong>圖 3.19 JH2 接頭</strong></p>
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/accessories/Camera/3.20%20JH1%20Connector.png"></p>
    <p align="center"><strong>圖 3.20 JH1 接頭</strong></p>
3. GMSL 攝影機連接
    請依圖 3.21 所示連接攝影機。圖中以兩台攝影機為例，但您可視需要連接一至四台攝影機。
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/accessories/Camera/3.21%20GMSL%20Camera%20Connection.png"></p>
    <p align="center"><strong>圖 3.21 GMSL 攝影機連接</strong></p>

# 4. 軟體設定
第 4 章說明攝影機運作所需的軟體設定。若要在 D3-G 與 AI-G 平台上設定 MIPI CSI-2 攝影機 (OV5647、IMX219) 與 GMSL 攝影機，請參閱下方提供的 Yocto 設定說明。

## 4.1 MIPI CSI-2 攝影機設定指南
TX 資料速率可使用下列公式計算：

<p align="center"><strong>TX Data Rate ={ H_active }×{V_active }×{FPS}×{BPP}×{ Number_of_Cameras} × 1.3 (Margin)</strong></p>

資料速率總和不得超過 D3-G MIPI CSI-2 每個 lane 2.1 Gbps 的頻寬上限。  
而資料速率總和也不得超過 AI-G MIPI CSI-2 每個 lane 1.5 Gbps 的頻寬上限

### 4.1.1 D3-G OV5647 設定指南
#### 4.1.1.1 OV5647 感測器概觀
##### 4.1.1.1.1 簡介
OV5647 是一款 500 萬畫素的 CMOS 影像感測器，因體積小巧、效能穩定且相容於標準 MIPI CSI-2 介面，廣泛應用於嵌入式攝影機應用。它也是 Raspberry Pi Camera Module v1 所採用的影像感測器，並可透過多款 Arducam OV5647 相機模組取得，這些模組皆相容於 TOPST D3-G 平台。  
使用者可將 Raspberry Pi Camera v1 或 Arducam OV5647 模組連接至 MIPI CSI 連接埠，以進行攝影機操作。

在 TOPST D3-G 平台上，OV5647 透過 15-pin 或 20-pin MIPI CSI 接頭連接，並經由 V4L2 框架控制，在 Yocto 與 Ubuntu 環境中皆提供一致的運作方式。

##### 4.1.1.1.2 支援的解析度與 FPS
OV5647 相機模組 (Raspberry Pi v1 或 Arducam OV5647) 的規格如下：  

<p align="center"><strong>表 4.1 OV5647 相機模組規格</strong></p>
<div align="center">
    <table>
        <tr>
            <td colspan="2" align="center"><strong>規格</strong></td>
            <td align="center"><strong>說明</strong></td>
        </tr>
        <tr>
            <td colspan="2">感測器</td>
            <td>OmniVision OV5647</td>
        </tr>
        <tr>
            <td colspan="2">解析度</td>
            <td>2592 x 1944 (5MP)</td>
        </tr>
        <tr>
            <td colspan="2">輸出格式</td>
            <td>RAW, YUV, JPEG</td>
        </tr>
        <tr>
            <td colspan="2">介面</td>
            <td>MIPI CSI-2</td>
        </tr>
        <tr>
            <td colspan="2">影格率</td>
            <td>1080p30, 720p60, 480p90</td>
        </tr>
        <tr>
            <td colspan="2">鏡頭</td>
            <td>定焦</td>
        </tr>
        <tr>
            <td colspan="2">視野角 (FOV)</td>
            <td>Up to 54°</td>
        </tr>
        <tr>
            <td colspan="2">纜線類型</td>
            <td>FFC (15-pin)</td>
        </tr>
        <tr>
            <td colspan="2">板子尺寸</td>
            <td>25mm x 24mm</td>
        </tr>
        <tr>
            <td colspan="2">相容性</td>
            <td>D3-G 與 Rasbperry Pi (透過 MIPI CSI-2 連接埠)</td>
        </tr>
    </table>
</div>

D3-G 支援的感測器解析度與 FPS 如下：  
<p align="center"><strong>表 4.2 D3-G 上的 OV5647 感測器解析度</strong></p>
<div align="center">
    <table>
        <tr>
            <td colspan="3" align="center"><strong>解析度</strong></td>
            <td align="center"><strong>FPS</strong></td>
            <td align="center"><strong>說明</strong></td>
        </tr>
        <tr>
            <td colspan="3">1920x1080</td>
            <td>30</td>
            <td>裁切全解析度影格的中央區域以輸出 1080p 影像</td>
        </tr>
        <tr>
            <td colspan="3">1296x972</td>
            <td>30</td>
            <td>利用 2×2 像素合併 (binning) 提升感光度並降低雜訊</td>
        </tr>
        <tr>
            <td colspan="3">640x480</td>
            <td>60</td>
            <td>結合 2×2 binning 與<strong>次取樣</strong>，於讀出時略過部分像素，以降低資料傳輸量並達到更高的影格率</td>
        </tr>
    </table>
</div>

**註：** 如表 4.2 所示，由於 D3-G 的 ISP 規格限制，**無法使用 2592×1944 的完整解析度**。

<p align="center"><strong>表 4.3 各操作模式的最大解析度</strong></p>
<div align="center">
    <table>
        <tr>
            <td rowspan="2" align="center"><strong>ISP 核心</strong></td>
            <td colspan="2"><strong>各操作模式的解析度</strong></td>
        </tr>
        <tr>
            <td align="center"><strong>預設模式</strong></td>
            <td align="center"><strong>記憶體共用模式</strong></td>
        </tr>
        <tr>
            <td>ISP0</td>
            <td>2048x1536 @ 60fps</td>
            <td>2048x1536 @ 60fps</td>
        </tr>
        <tr>
            <td>ISP1</td>
            <td>2560x1440 @ 60fps</td>
            <td>2560x1440 @ 60fps</td>
        </tr>
        <tr>
            <td>ISP2</td>
            <td>1280x720 @ 60fps</td>
            <td>1560x1440 @ 60fps</td>
        </tr>
        <tr>
            <td>ISP3</td>
            <td>1280x720 @ 60fps</td>
            <td>N/A</td>
        </tr>
    </table>
</div>

#### 4.1.1.2 在 Yocto 中設定 OV5647 解析度：驅動程式
若要在 Yocto 建置過程中修改 OV5647 感測器的解析度，請依照下列說明操作。  

首先，若要啟用 OV5647，請確認已在下列檔案中設定 TOPST_CAM_MODULE = "ov5647"：  
{build_dir}/build/d3-g-topst-main/conf/local.conf.  
雖然首次建置初始化儲存庫時即會預設啟用此項目，但請再次確認。

此外，為避免程式碼在建置過程中被移除，請於下列檔案中啟用這一行：  
{build_dir}/build/d3-g-topst-main/conf/local.conf:
```
INHERIT:remove = “rm_work”
```

啟用上述選項後，請使用下列指令重新建置映像檔。
```
$ bitbake telechips-topst-image
```

其次，建置完成後，請開啟 ov5647.c 驅動程式檔案並進行必要的修改。

請前往下列目錄：
```
${build_dir}/build/d3-g-topst-main/tmp/work/d3_g_topst_main-telechips-linux/linux-topst/5.10.205-r0/git/drivers/media/i2c/telechips/
```

修改程式碼前，請注意目前的驅動程式支援下列三種模式：
- 1920x1080 @ 30fps
- 1296x972 @ 30fps
- 640x480 @ 60fps  

上述解析度分別對應 Mode 1、Mode 2 與 Mode 3。  

1920×1080 @ 30fps 模式採用中央裁切，視野較窄；640×480 模式的解析度則不足。相較之下，1296×972 模式採用 2×2 binning，可提供較廣的視野，因此目前作為預設模式使用。  
請開啟 ov5647.c 驅動程式檔案，並依下列方式修改 OV5647 的預設模式。
```
#define OV5647_DEFAULT_MODE (&supported_modes_10bit[2])
```
1920×1080 @ 30fps 對應 Mode 1，可直接沿用 **“#define OV5647_DEFAULT_MODE (&supported_modes_10bit[1])”**。  
1296×972 @ 30fps 模式對應 Mode 2，因此 **“#define OV5647_DEFAULT_MODE (&supported_modes_10bit[2])”** 已是正確設定。  
若要使用對應 Mode 3 的 640×480 @ 60fps，請將定義改為 **“#define OV5647_DEFAULT_MODE (&supported_modes_10bit[3])”**。

第三，請重新建置核心並產生 FAI 映像檔。  
請返回建置目錄，並使用下列指令重新建置核心。
```
$ cd ${build_dir}/build/d3-g-topst-main/
$ bitbake -C compile linux-topst
$ cd ${build_dir}
$ ./stitch-fai-d3.sh
```
接著，請使用 FWDN 將產生的 output_d3g.fai 燒錄至開發板，即可以所需的解析度使用 OV5647 感測器。

**註：** 若要使用 MIPI1-CSI 連接埠，請開啟位於下列路徑的 tcc805x-videoinput-camera-module.dtsi 檔案
“{build_dir}/build/d3-g-topst-main/tmp/work/d3_g_topst_main-telechips-linux/linux-topst/5.10.205-r0/git/arch/arm64/boot/dts/telechips/tcc805x/override/” and change the included dtsi file from “tcc805x-videoinput-mipi0-ov5647.dtsi” to “tcc805x-videoinput-mipi1-ov5647.dtsi”. + Open the tcc805x-videoinput.dtsi file located in "{build_dir}/build/d3-g-topst-main/tmp/work/d3_g_topst_main-telechips-linux/linux-topst/5.10.205-r0/git/arch/arm64/boot/dts/telechips/tcc805x/" and change the mipi chmux from "mipi-chmux-0 = <0>;" to "mipi-chmux-0 = <1>;".

### 4.1.2 D3-G IMX219 設定指南
#### 4.1.2.1 IMX219 感測器概觀
##### 4.1.2.1.1 簡介
IMX219 是 Sony 推出的高效能 800 萬畫素 CMOS 影像感測器，以在小型相機模組中提供優異的影像品質、低耗電量與穩定的擷取效能而著稱。它同時也是 Raspberry Pi Camera Module v2 所採用的感測器，並廣泛應用於嵌入式視覺系統、機器人以及以 AI 為基礎的攝影應用。

在 TOPST D3-G 平台上，IMX219 感測器可透過 15-pin 或 20-pin 的 MIPI CSI 接頭連接，並由 V4L2 框架控制。如此可在 Yocto 與 Ubuntu 環境中提供一致的介面與穩定的攝影機運作。

憑藉高解析度（8MP）與低雜訊的成像特性，IMX219 非常適合在 TOPST D3-G 平台上實現高品質的視訊擷取與影像處理功能。

##### 4.1.2.1.2 支援的解析度與 FPS
IMX219 相機模組（Raspberry Pi v2）的規格如下：

<p align="center"><strong>表 4.4 IMX219 相機模組規格</strong></p>
<div align="center">
    <table>
        <tr>
            <td colspan="2" align="center"><strong>規格</strong></td>
            <td align="center"><strong>說明</strong></td>
        </tr>
        <tr>
            <td colspan="2">感測器</td>
            <td>Sony Imx219</td>
        </tr>
        <tr>
            <td colspan="2">解析度</td>
            <td>3280 x 2464 (8 MP)</td>
        </tr>
        <tr>
            <td colspan="2">輸出格式</td>
            <td>RAW, YUV, JPEG</td>
        </tr>
        <tr>
            <td colspan="2">介面</td>
            <td>MIPI CSI-2</td>
        </tr>
        <tr>
            <td colspan="2">影格率</td>
            <td>1080p60, 720p180, 480p206</td>
        </tr>
        <tr>
            <td colspan="2">鏡頭</td>
            <td>可調焦</td>
        </tr>
        <tr>
            <td colspan="2">視野角 (FOV)</td>
            <td>Up to 62°</td>
        </tr>
        <tr>
            <td colspan="2">纜線類型</td>
            <td>FFC (15-pin)</td>
        </tr>
        <tr>
            <td colspan="2">板子尺寸</td>
            <td>25mm x 24mm</td>
        </tr>
        <tr>
            <td colspan="2">相容性</td>
            <td>D3-G 與 Rasbperry Pi (透過 MIPI CSI-2 連接埠)</td>
        </tr>
    </table>
</div>

D3-G 所支援的感測器解析度與 FPS 如下：
<p align="center"><strong>表 4.5 D3-G 上的 IMX219 感測器解析度</strong></p>
<div align="center">
    <table>
        <tr>
            <td colspan="3" align="center"><strong>解析度</strong></td>
            <td align="center"><strong>FPS</strong></td>
            <td align="center"><strong>說明</strong></td>
        </tr>
        <tr>
            <td colspan="3">1920x1080</td>
            <td>30</td>
            <td>裁切全解析度影格的中央區域以輸出 1080p 影像</td>
        </tr>
        <tr>
            <td colspan="3">1640x1232</td>
            <td>30</td>
            <td>利用 2×2 像素合併 (binning) 提升感光度並降低雜訊</td>
        </tr>
        <tr>
            <td colspan="3">640x480</td>
            <td>30</td>
            <td>結合 2×2 binning 與<strong>次取樣</strong>，於讀出時略過部分像素，以降低資料傳輸量</td>
        </tr>
    </table>
</div>  

**註：** 如表 4.5 所示，由於 D3-G 的 ISP 規格限制，**無法使用 3820×2464 的完整解析度**。

<p align="center"><strong>表 4.6 各操作模式的最大解析度</strong></p>
<div align="center">
    <table>
        <tr>
            <td rowspan="2" align="center"><strong>ISP 核心</strong></td>
            <td colspan="2"><strong>各操作模式的解析度</strong></td>
        </tr>
        <tr>
            <td align="center"><strong>預設模式</strong></td>
            <td align="center"><strong>記憶體共用模式</strong></td>
        </tr>
        <tr>
            <td>ISP0</td>
            <td>2048x1536 @ 60fps</td>
            <td>2048x1536 @ 60fps</td>
        </tr>
        <tr>
            <td>ISP1</td>
            <td>2560x1440 @ 60fps</td>
            <td>2560x1440 @ 60fps</td>
        </tr>
        <tr>
            <td>ISP2</td>
            <td>1280x720 @ 60fps</td>
            <td>1560x1440 @ 60fps</td>
        </tr>
        <tr>
            <td>ISP3</td>
            <td>1280x720 @ 60fps</td>
            <td>N/A</td>
        </tr>
    </table>
</div>

#### 4.1.2.2 在 Yocto 中啟用 IMX219
由於 D3-G SDK 預設設定為啟用 OV5647，因此在建置前必須先啟用 IMX219。   
有兩種情況需要考量：SDK 已完成建置，以及首次進行建置。

##### 4.1.2.2.1 在首次建置前啟用 IMX219
若為首次建置，請依照下列步驟啟用 IMX219 並繼續進行建置。
1. 執行 source 環境設定腳本並選擇選項 2
    ```
    $ source poky/meta-topst/topst-build.sh
    ```
2. 開啟位於下列路徑的 local.conf 檔案
    ```
    ${build_dir}/build/d3-g-topst-main/conf/local.conf
    ```
3. 將 ov5647 的 TOPST_CAM_MODULE 項目註解掉，並啟用 imx219 的項目
    ```
    #TOPST_CAM_MODULE = "ov5647"
    TOPST_CAM_MODULE = "imx219"
    ```
4. 執行建置流程
    ```
    $ bitbake telechips-topst-image
    ```
##### 4.1.2.2.2 在建置完成後啟用 IMX219
現有的建置預設啟用 OV5647 感測器。請依照下列步驟啟用 IMX219。
1. 開啟位於下列路徑的 local.conf 檔案
    ```
    ${build_dir}/build/d3-g-topst-main/conf/local.conf
    ```
2. 將 ov5647 的 TOPST_CAM_MODULE 項目註解掉，並啟用 imx219 的項目
    ```
    #TOPST_CAM_MODULE = "ov5647"
    TOPST_CAM_MODULE = "imx219"
    ```
3. 對 isp-server 與 isp-firmware 執行 cleansstate 操作
    ```
    $ bitbake -c cleansstate isp-firmware
    $ bitbake -c cleansstate isp-server
    ```
4. 執行建置流程
    ```
    $ bitbake telechips-topst-image


#### 4.1.2.3 在 Yocto 中設定 IMX219 解析度：驅動程式
若要在 Yocto 建置過程中修改 IMX219 感測器的解析度，請依照下列說明操作。

首先，若要啟用 imx219，請確認已在下列檔案中設定 TOPST_CAM_MODULE = "imx219"：
{build_dir}/build/d3-g-topst-main/conf/local.conf.

此外，為避免程式碼在建置過程中被移除，請於下列檔案中啟用這一行：
{build_dir}/build/d3-g-topst-main/conf/local.conf:
```
INHERIT:remove = “rm_work”
```

啟用上述選項後，請使用下列指令重新建置映像檔。
```
$ bitbake telechips-topst-image
```

其次，建置完成後，請開啟 imx219.c 驅動程式檔案並進行必要的修改。

請前往下列目錄：
```
${build_dir}/build/d3-g-topst-main/tmp/work/d3_g_topst_main-telechips-linux/linux-topst/5.10.205-r0/git/drivers/media/i2c/telechips/
```

修改程式碼前，請注意目前的驅動程式支援下列三種模式：
- 1920x1080 @ 30fps
- 1640x1232 @ 30fps
- 640x480 @ 30fps

上述解析度分別對應 Mode 1、Mode 2 與 Mode 3。

1920×1080 @ 30fps 模式採用中央裁切，視野較窄；640×480 模式的解析度則不足。相較之下，1640×1232 模式採用 2×2 binning，可提供較廣的視野，因此目前作為預設模式使用。  
請開啟 imx219.c 驅動程式檔案，並修改 imx219_set_default_format、imx219_open 與 imx219_probe 函式中下列所述的部分。
- imx219_set_default_format
    ```
    fmt->width = supported_modes[2].width;
    fmt->height = supported_modes[2].height;
    ```
- imx219_open
    ```
    try_fmt_img->width = supported_modes[2].width;
    try_fmt_img->height = supported_modes[2].height;
    ```
- imx219_probe
    ```
    imx219->mode = &supported_modes[2];
    ```

由於 1920×1080 @ 30fps 對應 Mode 1，請將這三個函式中所有 supported_modes 的參照更新為 **“supported_modes[1]”**。  
1640×1232 @ 30fps 模式對應 Mode 2，因此請據此替換為 **“supported_modes[2]”**。  
若要使用對應 Mode 3 的 640×480 @ 30fps，請將所有參照改為 **“supported_modes [3]”**。

第三，請重新建置核心並產生 FAI 映像檔。  
請返回建置目錄，並使用下列指令重新建置核心。
```
$ cd ${build_dir}/build/d3-g-topst-main/
$ bitbake -C compile linux-topst
$ cd ${build_dir}
$ ./stitch-fai-d3.sh
```

接著，請使用 FWDN 將產生的 output_d3g.fai 燒錄至開發板，即可以所需的解析度使用 IMX219 感測器。

**註：** 若要使用 MIPI1-CSI 連接埠，請開啟位於下列路徑的 tcc805x-videoinput-camera-module.dtsi 檔案
“{build_dir}/build/d3-g-topst-main/tmp/work/d3_g_topst_main-telechips-linux/linux-topst/5.10.205-r0/git/arch/arm64/boot/dts/telechips/tcc805x/override/”and change the included dtsi file from “tcc805x-videoinput-mipi0-imx219.dtsi” to “tcc805x-videoinput-mipi1-imx219.dtsi”. + Open the tcc805x-videoinput.dtsi file located in "{build_dir}/build/d3-g-topst-main/tmp/work/d3_g_topst_main-telechips-linux/linux-topst/5.10.205-r0/git/arch/arm64/boot/dts/telechips/tcc805x/" and change the mipi chmux from "mipi-chmux-0 = <0>;" to "mipi-chmux-0 = <1>;".

#### 4.1.2.4 如何在 Yocto 中提高 IMX219 的 FPS：驅動程式與裝置樹
根據 IMX219 感測器的說明，該感測器支援 1080p60、720p180 與 VGA206 等高影格率模式。因此，可提高 imx219.c 驅動程式所支援之解析度（1920×1080、1640×1232 與 640×480）的 FPS。由於 D3-G 平台上的 ISP 核心最高支援 60 fps，這些解析度最高皆可提升至 60 fps。 

FPS 的計算公式如下：
<p align="center"><strong>{fps} = {pixel_rate}/{hts}x{vts}</strong></p>
因此，若要提高 FPS，必須調整 pixel_rate、hts 與 vts 的值。  
在目前的驅動程式實作中，pixel_rate 與 hts 皆為固定值。若要提高 FPS，唯一可行的方式是在維持 hts 不變的情況下提高 pixel_rate，再據此調整 vts 以達到所需的影格率。

若要將 FPS 修改為 60，必須同時更新驅動程式與裝置樹。
請依照下列指南將 FPS 變更為 60。

##### 4.1.2.4.1 1920x1080 @ 60fps
若要達到 60 fps，必須滿足下列關係：  
fps = pixel_rate / (hts × vts)
- pixel_rate = 182,400,000
- hts = 3448
- 目標 fps = 60

所需的 VTS 為：
- vts = pixel_rate / (hts × fps) = 182,400,000 / (3448 × 60) ≈ 882

然而，VTS 值必須大於 1080，因此此設定無效。  
因此，若要達到 60 fps，必須維持 hts 固定，並改為調整 pixel_rate、vts 與 PLL_VT 暫存器。

需進行的修改如下：
1. imx219.c 驅動程式檔案  
    A. 提高 pixel rate 與 link frequency
    ```
    #define IMX219_PIXEL_RATE            182400000    →   #define IMX219_PIXEL_RATE            278400000
    #define IMX219_DEFAULT_LINK_FREQ     456000000   →   #define IMX219_DEFAULT_LINK_FREQ     696000000
    ``` 
    B. 更新 1080p 模式的 VTS 值：
    ```
    #define IMX219_VTS_30FPS_1080P       0x06e3       →   #define IMX219_VTS_30FPS_1080P       0x0542
    ```
    C. 修改 1920x1080 模式表中的 PLL_VT 暫存器：
    ```
    // imx219_reg mode_1920_1080_regs[]
    {0x0307, 0x39}   →   {0x0307, 0x57}
    ```
2. tcc805x-videoinput-mipi0-imx219.dtsi 裝置樹檔案  
    A. 更新 link frequency 以符合新的 pixel rate：
    ```
    // &i2c7
    /bits/ 64 <456000000> → /bits/ 64 <696000000>
    ```
    B. 更新 hs-settle 值：
    ```
    hs-settle = <13> → hs-settle = <35>
    ```
3. 重新建置核心並產生 FAI 映像檔。  
    請返回建置目錄，並使用下列指令重新建置核心。
    ```
    $ cd ${build_dir}/build/d3-g-topst-main/
    $ bitbake -C compile linux-topst
    $ cd ${build_dir}
    $ ./stitch-fai-d3.sh
    ```
在 D3-G 上使用下列指令，可確認輸出的 FPS 為 59.9，即相當於 60 fps。
```
$ v4l2-ctl --stream-mmap=3 --stream-count=300 --stream-to=/dev/null --verbose
```
D3-G 上用於攝影機播放的 GStreamer 指令如下。
```
$ gst-launch-1.0 v4l2src device=/dev/video0 io-mode=2 ! video/x-raw,format=NV12,width=1920,height=1080,framerate=60/1 ! videoconvert ! waylandsink sync=false
```

##### 4.1.2.4.2 1640x1232 @ 60fps
若要達到 60 fps，必須滿足下列關係：  
fps = pixel_rate / (hts × vts)
- pixel_rate = 182,400,000
- hts = 3448
- 目標 fps = 60

所需的 VTS 為：
- vts = pixel_rate / (hts × fps) = 182,400,000 / (3448 × 60) ≈ 882

然而，VTS 值必須大於 1080，因此此設定無效。  
因此，若要達到 60 fps，必須維持 hts 固定，並改為調整 pixel_rate、vts 與 PLL_VT 暫存器。

需進行的修改如下：
1. imx219.c 驅動程式檔案  
    A. 提高 pixel rate 與 link frequency
    ```
    #define IMX219_PIXEL_RATE            182400000    →   #define IMX219_PIXEL_RATE            278400000
    #define IMX219_DEFAULT_LINK_FREQ     456000000   →   #define IMX219_DEFAULT_LINK_FREQ     696000000
    ``` 
    B. 更新 1640_1232 模式的 VTS 值：
    ```
    #define IMX219_VTS_30FPS_BINNED       0x06e3       →   #define IMX219_VTS_30FPS_BINNED       0x0542
    ```
    C. 修改 1920x1080 模式表中的 PLL_VT 暫存器：
    ```
    // imx219_reg mode_1640_1232_regs[]
    {0x0307, 0x39}   →   {0x0307, 0x57}
    ```
2. tcc805x-videoinput-mipi0-imx219.dtsi 裝置樹檔案  
    A. 更新 link frequency 以符合新的 pixel rate：
    ```
    // &i2c7
    /bits/ 64 <456000000> → /bits/ 64 <696000000>
    ```
    B. 更新 hs-settle 值：
    ```
    hs-settle = <13> → hs-settle = <34>
    ```
3. 重新建置核心並產生 FAI 映像檔。  
    請返回建置目錄，並使用下列指令重新建置核心。
    ```
    $ cd ${build_dir}/build/d3-g-topst-main/
    $ bitbake -C compile linux-topst
    $ cd ${build_dir}
    $ ./stitch-fai-d3.sh
    ```
在 D3-G 上使用下列指令，可確認輸出的 FPS 為 59.9，即相當於 60 fps。
```
$ v4l2-ctl --stream-mmap=3 --stream-count=300 --stream-to=/dev/null --verbose
```
D3-G 上用於攝影機播放的 GStreamer 指令如下。
```
$ gst-launch-1.0 v4l2src device=/dev/video0 io-mode=2 ! video/x-raw,format=NV12,width=1640,height=1232,framerate=60/1 ! videoconvert ! waylandsink sync=false
```

##### 4.1.2.4.3 640x480 @ 60fps
若要達到 60 fps，必須滿足下列關係：  
fps = pixel_rate / (hts × vts)
- pixel_rate = 182,400,000
- hts = 3448
- 目標 fps = 60

所需的 VTS 為：
- vts = pixel_rate / (hts × fps) = 182,400,000 / (3448 × 60) ≈ 882

由於 VTS 值大於 480，因此符合條件。與前一個範例相同，我們將在維持 HTS 固定的情況下，調整 pixelrate 與 VTS 以變更 FPS。  
您也可以在不變更 pixelrate 的情況下，僅修改 VTS 值來調整 FPS。但 IMX219 的 0x0307 暫存器值必須維持不變。

需進行的修改如下：
1. imx219.c 驅動程式檔案  
    A. 提高 pixel rate 與 link frequency
    ```
    #define IMX219_PIXEL_RATE            182400000    →   #define IMX219_PIXEL_RATE            278400000
    #define IMX219_DEFAULT_LINK_FREQ     456000000   →   #define IMX219_DEFAULT_LINK_FREQ     696000000
    ``` 
    B. 更新 640_480 模式的 VTS 值：
    ```
    #define IMX219_VTS_30FPS_640x480       0x06e3       →   #define IMX219_VTS_30FPS_640x480       0x0542
    ```
    C. 修改 640x480 模式表中的 PLL_VT 暫存器：
    ```
    // imx219_reg mode_640_480_regs[]
    {0x0307, 0x39}   →   {0x0307, 0x57}
    ```
2. tcc805x-videoinput-mipi0-imx219.dtsi 裝置樹檔案  
    A. 更新 link frequency 以符合新的 pixel rate：
    ```
    // &i2c7
    /bits/ 64 <456000000> → /bits/ 64 <696000000>
    ```
    B. 更新 hs-settle 值：
    ```
    hs-settle = <13> → hs-settle = <26>
    ```
3. 重新建置核心並產生 FAI 映像檔。  
    請返回建置目錄，並使用下列指令重新建置核心。
    ```
    $ cd ${build_dir}/build/d3-g-topst-main/
    $ bitbake -C compile linux-topst
    $ cd ${build_dir}
    $ ./stitch-fai-d3.sh
    ```
在 D3-G 上使用下列指令，可確認輸出的 FPS 為 59.9，即相當於 60 fps。
```
$ v4l2-ctl --stream-mmap=3 --stream-count=300 --stream-to=/dev/null --verbose
```
D3-G 上用於攝影機播放的 GStreamer 指令如下。
```
$ gst-launch-1.0 v4l2src device=/dev/video0 io-mode=2 ! video/x-raw,format=NV12,width=640,height=480,framerate=60/1 ! videoconvert ! waylandsink sync=false
```

### 4.1.3 AI-G OV5647 感測器使用指南
#### 4.1.3.1 OV5647 感測器概觀
##### 4.1.3.1.1 簡介
OV5647 是一款 500 萬畫素的 CMOS 影像感測器，因體積小巧、效能穩定且相容於標準 MIPI CSI-2 介面，而廣泛應用於嵌入式攝影應用。它同時也是 Raspberry Pi Camera Module v1 所採用的影像感測器，並可透過各種 Arducam OV5647 相機模組取得，這些模組皆與 TOPST AI-G 平台相容。  
使用者可將 Raspberry Pi Camera v1 或 Arducam OV5647 模組連接至 MIPI CSI 連接埠，以進行攝影機操作。

在 TOPST AI-G 平台上，OV5647 透過 15-pin 或 20-pin 的 MIPI CSI 接頭連接，並由 V4L2 框架控制，可在 Yocto 與 Ubuntu 環境中提供一致的運作方式。

##### 4.1.3.1.2 支援的解析度與 FPS
OV5647 相機模組（Raspberry Pi v1 或 Arducam OV5647）的規格如下：
<p align="center"><strong>表 4.7 OV5647 相機模組規格</strong></p>
<div align="center">
    <table>
        <tr>
            <td colspan="2" align="center"><strong>規格</strong></td>
            <td align="center"><strong>說明</strong></td>
        </tr>
        <tr>
            <td colspan="2">感測器</td>
            <td>OmniVision OV5647</td>
        </tr>
        <tr>
            <td colspan="2">解析度</td>
            <td>2592 x 1944 (5MP)</td>
        </tr>
        <tr>
            <td colspan="2">輸出格式</td>
            <td>RAW, YUV, JPEG</td>
        </tr>
        <tr>
            <td colspan="2">介面</td>
            <td>MIPI CSI-2</td>
        </tr>
        <tr>
            <td colspan="2">影格率</td>
            <td>1080p30, 720p60, 480p90</td>
        </tr>
        <tr>
            <td colspan="2">鏡頭</td>
            <td>定焦</td>
        </tr>
        <tr>
            <td colspan="2">視野角 (FOV)</td>
            <td>Up to 54°</td>
        </tr>
        <tr>
            <td colspan="2">纜線類型</td>
            <td>FFC (15-pin)</td>
        </tr>
        <tr>
            <td colspan="2">板子尺寸</td>
            <td>25mm x 24mm</td>
        </tr>
        <tr>
            <td colspan="2">相容性</td>
            <td>D3-G 與 Rasbperry Pi (透過 MIPI CSI-2 連接埠)</td>
        </tr>
    </table>
</div>

AI-G 所支援的感測器解析度與 FPS 如下：  
<p align="center"><strong>表 4.8 AI-G 上的 OV5647 感測器解析度</strong></p>
<div align="center">
    <table>
        <tr>
            <td colspan="3" align="center"><strong>解析度</strong></td>
            <td align="center"><strong>FPS</strong></td>
            <td align="center"><strong>說明</strong></td>
        </tr>
        <tr>
            <td colspan="3">1920x1080</td>
            <td>30</td>
            <td>裁切全解析度影格的中央區域以輸出 1080p 影像</td>
        </tr>
        <tr>
            <td colspan="3">1296x972</td>
            <td>30</td>
            <td>利用 2×2 像素合併 (binning) 提升感光度並降低雜訊</td>
        </tr>
        <tr>
            <td colspan="3">640x480</td>
            <td>60</td>
            <td>結合 2×2 binning 與<strong>次取樣</strong>，於讀出時略過部分像素，以降低資料傳輸量並達到更高的影格率</td>
        </tr>
    </table>
</div>

**註：** 如表 4.8 所示，由於會大幅降低推論效能，因此**未使用 2592×1944 的完整解析度**。

<p align="center"><strong>表 4.9 各操作模式的最大解析度</strong></p>
<div align="center">
    <table>
        <tr>
            <td colspan="4" align="center"><strong>使用的 CH.</strong></td>
            <td align="center"><strong>操作模式</strong></td>
            <td align="center"><strong>最大解析度</strong></td>
            <td align="center"><strong>輸入格式</strong></td>
        </tr>
        <tr>
            <td colspan="4">4CH</td>
            <td>預設模式</td>
            <td>1280 x 720 @ 60fps</td>
            <td>RAW 24</td>
        </tr>
        <tr>
            <td colspan="4" rowspan="2">2CH</td>
            <td rowspan="2">記憶體共用模式</td>
            <td>選項 1：2048 x 1280 @ 60fps</td>
            <td>RAW 20</td>
        </tr>
        <tr>
            <td>選項 2：2592 x 2048 @ 30fps + 2048 x 1280 @ 30fps</td>
            <td>RAW 24</td>
        </tr>
        <tr>
            <td colspan="4">1CH</td>
            <td>記憶體共用模式</td>
            <td>2592 x 2048 @ 60fps</td>
            <td>RAW 20</td>
        </tr>
    </table>
</div>

#### 4.1.3.2 在 Yocto 中設定 OV5647 解析度：驅動程式
若要在 Yocto 建置過程中修改 OV5647 感測器的解析度，請依照下列說明操作。

首先，若要啟用 OV5647，請確認已在下列檔案中設定 TOPST_CAM_MODULE = "ov5647"：  
{build_dir}/build/ai-g-topst-main/conf/local.conf.  
雖然首次建置初始化儲存庫時即會預設啟用此項目，但請再次確認。

此外，為避免程式碼在建置過程中被移除，請於下列檔案中啟用這一行：  
{build_dir}/build/ai-g-topst-main/conf/local.conf:
```
INHERIT:remove = “rm_work”
```

啟用上述選項後，請使用下列指令重新建置映像檔。
```
$ bitbake telechips-topst-image
```

其次，建置完成後，請開啟 ov5647.c 驅動程式檔案並進行必要的修改。

請前往下列目錄：
```
${build_dir}/build/ai-g-topst-main/tmp/work/ai_g_topst-telechips-linux/linux-topst/5.10.223-r0/git/drivers/media/i2c/telechips/
```

修改程式碼前，請注意目前的驅動程式支援下列三種模式：
- 1920×1080 @ 30fps
- 1296×972 @ 30fps
- 640×480 @ 60fps

上述解析度分別對應 Mode 1、Mode 2 與 Mode 3。

1920×1080 @ 30fps 模式採用中央裁切，視野較窄；640×480 模式的解析度則不足。相較之下，1296×972 模式採用 2×2 binning，可提供較廣的視野，因此目前作為預設模式使用。  
請開啟 ov5647.c 驅動程式檔案，並依下列方式修改 OV5647 的預設模式。
```
#define OV5647_DEFAULT_MODE (&supported_modes_10bit[2])
```
1920×1080 @ 30fps 對應 Mode 1，可直接沿用 **“#define OV5647_DEFAULT_MODE (&supported_modes_10bit[1])”**。  
1296×972 @ 30fps 模式對應 Mode 2，因此 **“#define OV5647_DEFAULT_MODE (&supported_modes_10bit[2])”**已是正確設定。  
若要使用對應 Mode 3 的 640×480 @ 60fps，請將定義改為 **“#define OV5647_DEFAULT_MODE (&supported_modes_10bit[3])”**。

第三，請重新建置核心並產生 FAI 映像檔。  
請返回建置目錄，並使用下列指令重新建置核心。
```
$ cd ${build_dir}/build/ai-g-topst-main/
$ bitbake -C compile linux-topst
$ cd ${build_dir}
$ ./stitch-fai-ai.sh
```

接著，請使用 FWDN 將產生的 output_aig.fai 燒錄至開發板，即可以所需的解析度使用 OV5647 感測器。

### 4.1.4 AI-G IMX219 感測器設定指南
#### 4.1.4.1 IMX219 感測器概觀
##### 4.1.4.1.1 簡介
IMX219 是 Sony 推出的高效能 800 萬畫素 CMOS 影像感測器，以在小型相機模組中提供優異的影像品質、低耗電量與穩定的擷取效能而著稱。它同時也是 Raspberry Pi Camera Module v2 所採用的感測器，並廣泛應用於嵌入式視覺系統、機器人以及以 AI 為基礎的攝影應用。

在 TOPST AI-G 平台上，IMX219 感測器可透過 15-pin 或 20-pin 的 MIPI CSI 接頭連接，並由 V4L2 框架控制。如此可在 Yocto 與 Ubuntu 環境中提供一致的介面與穩定的攝影機運作。

憑藉高解析度（8MP）與低雜訊的成像特性，IMX219 非常適合在 TOPST AI-G 平台上實現高品質的視訊擷取與影像處理功能。

##### 4.1.4.1.2 支援的解析度與 FPS
IMX219 相機模組（Raspberry Pi v2）的規格如下：
<p align="center"><strong>表 4.10 IMX219 相機模組規格</strong></p>
<div align="center">
    <table>
        <tr>
            <td colspan="2" align="center"><strong>規格</strong></td>
            <td align="center"><strong>說明</strong></td>
        </tr>
        <tr>
            <td colspan="2">感測器</td>
            <td>Sony Imx219</td>
        </tr>
        <tr>
            <td colspan="2">解析度</td>
            <td>3280 x 2464 (8 MP)</td>
        </tr>
        <tr>
            <td colspan="2">輸出格式</td>
            <td>RAW, YUV, JPEG</td>
        </tr>
        <tr>
            <td colspan="2">介面</td>
            <td>MIPI CSI-2</td>
        </tr>
        <tr>
            <td colspan="2">影格率</td>
            <td>1080p60, 720p180, 480p206</td>
        </tr>
        <tr>
            <td colspan="2">鏡頭</td>
            <td>可調焦</td>
        </tr>
        <tr>
            <td colspan="2">視野角 (FOV)</td>
            <td>Up to 62°</td>
        </tr>
        <tr>
            <td colspan="2">纜線類型</td>
            <td>FFC (15-pin)</td>
        </tr>
        <tr>
            <td colspan="2">板子尺寸</td>
            <td>25mm x 24mm</td>
        </tr>
        <tr>
            <td colspan="2">相容性</td>
            <td>D3-G 與 Rasbperry Pi (透過 MIPI CSI-2 連接埠)</td>
        </tr>
    </table>
</div>

AI-G 所支援的感測器解析度與 FPS 如下：
<p align="center"><strong>表 4.11 AI-G 上的 IMX219 感測器解析度</strong></p>
<div align="center">
    <table>
        <tr>
            <td colspan="3" align="center"><strong>解析度</strong></td>
            <td align="center"><strong>FPS</strong></td>
            <td align="center"><strong>說明</strong></td>
        </tr>
        <tr>
            <td colspan="3">1920x1080</td>
            <td>30</td>
            <td>裁切全解析度影格的中央區域以輸出 1080p 影像</td>
        </tr>
        <tr>
            <td colspan="3">1640x1232</td>
            <td>30</td>
            <td>利用 2×2 像素合併 (binning) 提升感光度並降低雜訊</td>
        </tr>
        <tr>
            <td colspan="3">640x480</td>
            <td>30</td>
            <td>結合 2×2 binning 與<strong>次取樣</strong>，於讀出時略過部分像素，以降低資料傳輸量</td>
        </tr>
    </table>
</div>

**註：** 如表 4.11 所示，由於會大幅降低推論效能，因此未使用 3820×2464 的完整解析度。

<p align="center"><strong>表 4.12 各操作模式的最大解析度</strong></p>
<div align="center">
    <table>
        <tr>
            <td colspan="4" align="center"><strong>使用的 CH.</strong></td>
            <td align="center"><strong>操作模式</strong></td>
            <td align="center"><strong>最大解析度</strong></td>
            <td align="center"><strong>輸入格式</strong></td>
        </tr>
        <tr>
            <td colspan="4">4CH</td>
            <td>預設模式</td>
            <td>1280 x 720 @ 60fps</td>
            <td>RAW 24</td>
        </tr>
        <tr>
            <td colspan="4" rowspan="2">2CH</td>
            <td rowspan="2">記憶體共用模式</td>
            <td>選項 1：2048 x 1280 @ 60fps</td>
            <td>RAW 20</td>
        </tr>
        <tr>
            <td>選項 2：2592 x 2048 @ 30fps + 2048 x 1280 @ 30fps</td>
            <td>RAW 24</td>
        </tr>
        <tr>
            <td colspan="4">1CH</td>
            <td>記憶體共用模式</td>
            <td>2592 x 2048 @ 60fps</td>
            <td>RAW 20</td>
        </tr>
    </table>
</div>

#### 4.1.4.2 在 Yocto 中啟用 IMX219
由於 AI-G SDK 預設設定為啟用 OV5647，因此在建置前必須先啟用 IMX219。  
有兩種情況需要考量：SDK 已完成建置，以及首次進行建置。

##### 4.1.4.2.1 在首次建置前啟用 IMX219
若為首次建置，請依照下列步驟啟用 IMX219 並繼續進行建置。
1. 執行 source 環境設定腳本並選擇選項 1
    ```
    $ source poky/meta-topst/topst-build.sh
    ```
2. 開啟位於下列路徑的 local.conf 檔案
    ```
    ${build_dir}/build/ai-g-topst-main/conf/local.conf
    ```
3. 將 ov5647 的 TOPST_CAM_MODULE 項目註解掉，並啟用 imx219 的項目
    ```
    #TOPST_CAM_MODULE = "ov5647"
    TOPST_CAM_MODULE = "imx219"
    ```
4. 執行建置流程
    ```
    $ bitbake telechips-topst-ai-image
    ```

##### 4.1.4.2.2 在建置完成後啟用 IMX219
現有的建置預設啟用 OV5647 感測器。請依照下列步驟啟用 IMX219。
1. 開啟位於下列路徑的 local.conf 檔案
    ```
    ${build_dir}/build/ai-g-topst-main/conf/local.conf
    ```
2. 將 ov5647 的 TOPST_CAM_MODULE 項目註解掉，並啟用 imx219 的項目
    ```
    #TOPST_CAM_MODULE = "ov5647"
    TOPST_CAM_MODULE = "imx219"
    ```
3. 對 isp-server 與 isp-firmware 執行 cleansstate 操作
    ```
    $ bitbake -c cleansstate isp-firmware
    $ bitbake -c cleansstate isp-server
    ```
4. 執行建置流程
    ```
    $ bitbake telechips-topst-ai-image
    ```

#### 4.1.4.3 在 Yocto 中設定 IMX219 解析度：驅動程式
若要在 Yocto 建置過程中修改 IMX219 感測器的解析度，請依照下列說明操作。

首先，若要啟用 imx219，請確認已在下列檔案中設定 TOPST_CAM_MODULE = "imx219"：
{build_dir}/build/ai-g-topst-main/conf/local.conf.

此外，為避免程式碼在建置過程中被移除，請於下列檔案中啟用這一行：
{build_dir}/build/ai-g-topst-main/conf/local.conf:
```
INHERIT:remove = “rm_work”
```

啟用上述選項後，請使用下列指令重新建置映像檔。
```
$ bitbake telechips-topst-ai-image
```
其次，建置完成後，請開啟 imx219.c 驅動程式檔案並進行必要的修改。

請前往下列目錄：
```
${build_dir}/build/ai-g-topst-main /ai-g-topst/tmp/work/ai_g_topst-telechips-linux/linux-topst/5.10.223-r0/git/drivers/media/i2c/telechips/
```
修改程式碼前，請注意目前的驅動程式支援下列三種模式：
- 1920×1080 @ 30fps
- 1640×1232 @ 30fps
- 640×480 @ 30fps
上述解析度分別對應 Mode 1、Mode 2 與 Mode 3。

1920×1080 @ 30fps 模式採用中央裁切，視野較窄；640×480 模式的解析度則不足。相較之下，1640×1232 模式採用 2×2 binning，可提供較廣的視野，因此目前作為預設模式使用。  
請開啟 imx219.c 驅動程式檔案，並修改 imx219_set_default_format、imx219_open 與 imx219_probe 函式中下列所述的部分。
- imx219_set_default_format
    ```
    fmt->width = supported_modes[2].width;
    fmt->height = supported_modes[2].height;
    ```
- imx219_open
    ```
    try_fmt_img->width = supported_modes[2].width;
    try_fmt_img->height = supported_modes[2].height;
    ```
- imx219_probe
    ```
    imx219->mode = &supported_modes[2];
    ```

由於 1920×1080 @ 30fps 對應 Mode 1，請將這三個函式中所有 supported_modes 的參照更新為 **“supported_modes[1]”**。  
1640×1232 @ 30fps 模式對應 Mode 2，因此請據此替換為 **“supported_modes[2]”**。  
若要使用對應 Mode 3 的 640×480 @ 30fps，請將所有參照改為 **“supported_modes [3]”**。

第三，請重新建置核心並產生 FAI 映像檔。  
請返回建置目錄，並使用下列指令重新建置核心。
```
$ cd ${build_dir}/build/ai-g-topst-main/
$ bitbake -C compile linux-topst
$ cd ${build_dir}
$ ./stitch-fai-ai.sh
```

接著，請使用 FWDN 將產生的 output_aig.fai 燒錄至開發板，即可以所需的解析度使用 IMX219 感測器。

#### 4.1.4.4 如何在 Yocto 中提高 IMX219 的 FPS：驅動程式與裝置樹
根據 IMX219 感測器的說明，該感測器支援 1080p60、720p180 與 VGA206 等高影格率模式。因此，可提高 imx219.c 驅動程式所支援之解析度（1920×1080、1640×1232 與 640×480）的 FPS。由於 AI-G 平台上的 ISP 核心最高支援 60 fps，這些解析度最高皆可提升至 60 fps。  

FPS 的計算公式如下：
<p align="center"><strong>{fps} = {pixel_rate}/{hts}x{vts}</strong></p>
因此，若要提高 FPS，必須調整 pixel_rate、hts 與 vts 的值。  
在目前的驅動程式實作中，pixel_rate 與 hts 皆為固定值。若要提高 FPS，唯一可行的方式是在維持 hts 不變的情況下提高 pixel_rate，再據此調整 vts 以達到所需的影格率。

若要將 FPS 修改為 60，必須同時更新驅動程式與裝置樹。
請依照下列指南將 FPS 變更為 60。

##### 4.1.2.4.1 1920x1080 @ 60fps
若要達到 60 fps，必須滿足下列關係：  
fps = pixel_rate / (hts × vts)
- pixel_rate = 182,400,000
- hts = 3448
- 目標 fps = 60

所需的 VTS 為：
- vts = pixel_rate / (hts × fps) = 182,400,000 / (3448 × 60) ≈ 882

然而，VTS 值必須大於 1080，因此此設定無效。  
因此，若要達到 60 fps，必須維持 hts 固定，並改為調整 pixel_rate、vts 與 PLL_VT 暫存器。

需進行的修改如下：
1. imx219.c 驅動程式檔案  
    A. 提高 pixel rate 與 link frequency
    ```
    #define IMX219_PIXEL_RATE            182400000    →   #define IMX219_PIXEL_RATE            278400000
    #define IMX219_DEFAULT_LINK_FREQ     456000000   →   #define IMX219_DEFAULT_LINK_FREQ     696000000
    ``` 
    B. 更新 1080p 模式的 VTS 值：
    ```
    #define IMX219_VTS_30FPS_1080P       0x06e3       →   #define IMX219_VTS_30FPS_1080P       0x0542
    ```
    C. 修改 1920x1080 模式表中的 PLL_VT 暫存器：
    ```
    // imx219_reg mode_1920_1080_regs[]
    {0x0307, 0x39}   →   {0x0307, 0x57}
    ```
2. tcc805x-videoinput-mipi0-imx219.dtsi 裝置樹檔案  
    A. 更新 link frequency 以符合新的 pixel rate：
    ```
    // &i2c7
    /bits/ 64 <456000000> → /bits/ 64 <696000000>
    ```
    B. 更新 hs-settle 值：
    ```
    hs-settle = <13> → hs-settle = <35>
    ```
3. 重新建置核心並產生 FAI 映像檔。  
    請返回建置目錄，並使用下列指令重新建置核心。
    ```
    $ cd ${build_dir}/build/d3-g-topst-main/
    $ bitbake -C compile linux-topst
    $ cd ${build_dir}
    $ ./stitch-fai-d3.sh
    ```
在 AI-G 上使用下列指令，可確認輸出的 FPS 為 59.9，即相當於 60 fps。
```
$ v4l2-ctl --stream-mmap=3 --stream-count=300 --stream-to=/dev/null --verbose
```

##### 4.1.2.4.2 1640x1232 @ 60fps
若要達到 60 fps，必須滿足下列關係：  
fps = pixel_rate / (hts × vts)
- pixel_rate = 182,400,000
- hts = 3448
- 目標 fps = 60

所需的 VTS 為：
- vts = pixel_rate / (hts × fps) = 182,400,000 / (3448 × 60) ≈ 882

然而，VTS 值必須大於 1080，因此此設定無效。  
因此，若要達到 60 fps，必須維持 hts 固定，並改為調整 pixel_rate、vts 與 PLL_VT 暫存器。

需進行的修改如下：
1. imx219.c 驅動程式檔案  
    A. 提高 pixel rate 與 link frequency
    ```
    #define IMX219_PIXEL_RATE            182400000    →   #define IMX219_PIXEL_RATE            278400000
    #define IMX219_DEFAULT_LINK_FREQ     456000000   →   #define IMX219_DEFAULT_LINK_FREQ     696000000
    ``` 
    B. 更新 1640_1232 模式的 VTS 值：
    ```
    #define IMX219_VTS_30FPS_BINNED       0x06e3       →   #define IMX219_VTS_30FPS_BINNED       0x0542
    ```
    C. 修改 1920x1080 模式表中的 PLL_VT 暫存器：
    ```
    // imx219_reg mode_1640_1232_regs[]
    {0x0307, 0x39}   →   {0x0307, 0x57}
    ```
2. tcc805x-videoinput-mipi0-imx219.dtsi 裝置樹檔案  
    A. 更新 link frequency 以符合新的 pixel rate：
    ```
    // &i2c7
    /bits/ 64 <456000000> → /bits/ 64 <696000000>
    ```
    B. 更新 hs-settle 值：
    ```
    hs-settle = <13> → hs-settle = <34>
    ```
3. 重新建置核心並產生 FAI 映像檔。  
    請返回建置目錄，並使用下列指令重新建置核心。
    ```
    $ cd ${build_dir}/build/d3-g-topst-main/
    $ bitbake -C compile linux-topst
    $ cd ${build_dir}
    $ ./stitch-fai-d3.sh
    ```
在 AI-G 上使用下列指令，可確認輸出的 FPS 為 59.9，即相當於 60 fps。
```
$ v4l2-ctl --stream-mmap=3 --stream-count=300 --stream-to=/dev/null --verbose
```

##### 4.1.2.4.3 640x480 @ 60fps
若要達到 60 fps，必須滿足下列關係：  
fps = pixel_rate / (hts × vts)
- pixel_rate = 182,400,000
- hts = 3448
- 目標 fps = 60

所需的 VTS 為：
- vts = pixel_rate / (hts × fps) = 182,400,000 / (3448 × 60) ≈ 882

由於 VTS 值大於 480，因此符合條件。與前一個範例相同，我們將在維持 HTS 固定的情況下，調整 pixelrate 與 VTS 以變更 FPS。  
您也可以在不變更 pixelrate 的情況下，僅修改 VTS 值來調整 FPS。但 IMX219 的 0x0307 暫存器值必須維持不變。

需進行的修改如下：
1. imx219.c 驅動程式檔案  
    A. 提高 pixel rate 與 link frequency
    ```
    #define IMX219_PIXEL_RATE            182400000    →   #define IMX219_PIXEL_RATE            278400000
    #define IMX219_DEFAULT_LINK_FREQ     456000000   →   #define IMX219_DEFAULT_LINK_FREQ     696000000
    ``` 
    B. 更新 640_480 模式的 VTS 值：
    ```
    #define IMX219_VTS_30FPS_640x480       0x06e3       →   #define IMX219_VTS_30FPS_640x480       0x0542
    ```
    C. 修改 640x480 模式表中的 PLL_VT 暫存器：
    ```
    // imx219_reg mode_640_480_regs[]
    {0x0307, 0x39}   →   {0x0307, 0x57}
    ```
2. tcc805x-videoinput-mipi0-imx219.dtsi 裝置樹檔案  
    A. 更新 link frequency 以符合新的 pixel rate：
    ```
    // &i2c7
    /bits/ 64 <456000000> → /bits/ 64 <696000000>
    ```
    B. 更新 hs-settle 值：
    ```
    hs-settle = <13> → hs-settle = <26>
    ```
3. 重新建置核心並產生 FAI 映像檔。  
    請返回建置目錄，並使用下列指令重新建置核心。
    ```
    $ cd ${build_dir}/build/d3-g-topst-main/
    $ bitbake -C compile linux-topst
    $ cd ${build_dir}
    $ ./stitch-fai-d3.sh
    ```
在 AI-G 上使用下列指令，可確認輸出的 FPS 為 59.9，即相當於 60 fps。
```
$ v4l2-ctl --stream-mmap=3 --stream-count=300 --stream-to=/dev/null --verbose
```

## 4.2 GMSL 攝影機設定指南
### 4.2.1 D3-G GMSL 攝影機設定指南
使用 Deserializer 板可將最多四台攝影機連接至單一 MIPI CSI 連接埠。由於 D3-G 提供兩個 MIPI CSI 連接埠，您可選擇下列其中一種設定：
- 在 MIPI0 連接埠上使用四台攝影機
- 在 MIPI1 連接埠上使用四台攝影機
- 同時使用 MIPI0 與 MIPI1，共連接八台攝影機

當設定全部八台攝影機時，D3-G 的顯示器擴充功能（最多支援四台顯示器）最多僅能使用三台顯示器。

**註：** 本指南使用 IMX290 (cxd5700) FHD GMSL 攝影機。  
若您打算使用其他 GMSL 攝影機，將需要額外的攝影機移植作業。

#### 4.2.1.1 如何使用 MIPI0 連接埠
首先，您必須啟用 GMSL 攝影機與 SerDes 板的核心設定。  
請將下列項目新增至  
**{build_dir}/poky/meta-topst-bsp/recipes-kernel/linux/linux-topst/tcc805x/camera.cfg** file.
```
CONFIG_VIDEO_TCC_CXD5700=y
CONFIG_VIDEO_TCC_MAX9275=y
CONFIG_VIDEO_TCC_MAX96712=y
```
To prevent the source code from being removed during the build process, enable the following line, and comment out all occurrences of `TOPST_CAM_MODULE in {build_dir}/build/d3-g-topst-main/conf/local.conf:
```
#TOPST_CAM_MODULE = "ov5647"
#TOPST_CAM_MODULE = "imx219"
```
修改上述選項後，請使用下列指令重新建置映像檔。
```
$ bitbake -c cleansstate isp-firmware
$ bitbake -c cleansstate isp-server
$ bitbake telechips-topst-image
```
接著，您必須修改核心中的裝置樹。請依照下列指南套用變更並重新建置映像檔。
1. Modify file {build_dir}/build/d3-g-topst-main/tmp/work/d3_g_topst_main-telechips-linux/linux-topst/5.10.205-r0/git/arch/arm64/boot/dts/telechips/tcc805x/override/tcc8050_53-lpd4x322-sv1.0-videoinput.dtsi as shown below
    ```
    @@ -192,7 +192,7 @@ max9295_1: max9295_1@40 {
            max9286_1: max9286_1@48 {
                    status          = "disabled";
                    compatible      = "tcc-maxim,max9286";
    -               pwd-gpios       = <&gpmc 0 1>;
    +               pwd-gpios       = <&gpg 5 1>;
                    reg             = <0x48>;       // 0x90 >> 1
            };
    @@ -200,7 +200,7 @@ max9286_1: max9286_1@48 {
            max96712_1: max96712_1@2a {
                    status          = "disabled";
                    compatible      = "tcc-maxim,max96712";
    -               pwd-gpios       = <&gpmc 0 1>;
    +               pwd-gpios       = <&gpg 5 1>;
                    reg             = <0x2A>;
            };
    };
    @@ -325,7 +325,7 @@ max9295e: max9295e@42 {
            max9286: max9286@48 {
                    status          = "disabled";
                    compatible      = "tcc-maxim,max9286";
    -               pwd-gpios       = <&gpg 5 1>;
    +               pwd-gpios       = <&gpmc 0 1>;
                    reg             = <0x48>;       // 0x90 >> 1
            };
    @@ -333,7 +333,7 @@ max9286: max9286@48 {
            max96712: max96712@2a {
                    status          = "disabled";
                    compatible      = "tcc-maxim,max96712";
    -               pwd-gpios       = <&gpg 5 1>;
    +              pwd-gpios       = <&gpmc 0 1>;
                    reg             = <0x2A>;
            };
    ```
2. Modify file {build_dir}/build/d3-g-topst-main/tmp/work/d3_g_topst_main-telechips-linux/linux-topst/5.10.205-r0/git/arch/arm64/boot/dts/telechips/tcc805x/override/tcc805x-videoinput-camera-module.dtsi as shown below
    ```
    //#include "tcc805x-videoinput-mipi0-ov5647.dtsi"
    //#include "tcc805x-videoinput-mipi0-imx219.dtsi"
    +#include "tcc805x-videoinput-mipi0-fhd.dtsi"
    ```
3. Create file {build_dir}/build/d3-g-topst-main/tmp/work/d3_g_topst_main-telechips-linux/linux-topst/5.10.205-r0/git/arch/arm64/boot/dts/telechips/tcc805x/override/tcc805x-videoinput-mipi0-fhd.dtsi as shown below
    ```
    // SPDX-License-Identifier: (GPL-2.0-or-later OR MIT)
    /*
    * Copyright (C) Telechips Inc.
    */

    &i2c6 {
        status = "okay";
    };

    &cxd5700_1 {
        /* ISP of camera module */
        status          = "okay";
        port {
                cxd5700_1_out: endpoint {
                        remote-endpoint = <&max9275_1_in>;
                        io-direction    = "output";
                };
        };
    };

    &max9275_1 {
        /* serializer */
        status          = "okay";
        ports {
                #address-cells = <1>;
                #size-cells = <0>;
                port@0 {
                        reg = <0>;
                        max9275_1_in: endpoint {
                                remote-endpoint = <&cxd5700_1_out>;
                                io-direction    = "input";
                        };
                };
                port@1 {
                        reg = <1>;
                        max9275_1_out: endpoint {
                                remote-endpoint = <&max96712_1_in0>;
                                io-direction    = "output";
                        };
                };
        };
    };

    &max96712_1 {
        /* deserializer */
        status          = "okay";
        pvd-name        = "fhd";
        /*
            * broadcasting mode access each linked devices
            * by the same I2C slave address.
            *
            * Also,
            * using the serdes I2C address mapping table,
            * each liked devices can be accessed
            * by the unique I2C slave address.
            */
        broadcasting-mode;
        ports {
                #address-cells = <1>;
                #size-cells = <0>;
                /*
                    * 0 ~ 3
                    * input ports. The number is matched with VC
                    *
                    * 4
                    * output port.
                    */
                port@0 {
                        reg = <0>;
                        max96712_1_in0: endpoint {
                                remote-endpoint = <&max9275_1_out>;
                                io-direction    = "input";
                                channel         = <0>;
                        };
                };
                port@1 {
                        reg = <1>;
                        max96712_1_in1: endpoint {
                                remote-endpoint = <&max9275_1_out>;
                                io-direction    = "input";
                                channel         = <1>;
                        };
                };
                port@2 {
                        reg = <2>;
                        max96712_1_in2: endpoint {
                                remote-endpoint = <&max9275_1_out>;
                                io-direction    = "input";
                                channel         = <2>;
                        };
                };
                port@3 {
                        reg = <3>;
                        max96712_1_in3: endpoint {
                                remote-endpoint = <&max9275_1_out>;
                                io-direction    = "input";
                                channel         = <3>;
                        };
                };
                port@4 {
                        reg = <4>;
                        max96712_1_out: endpoint {
                                remote-endpoint = <&mipi_csi2_0_in>;
                                io-direction    = "output";
                                channel         = <0>;
                        };
                };
        };
    };

    &mipi_csi2_0 {
        status = "okay";
        ports {
                #address-cells = <1>;
                #size-cells = <0>;
                /*
                    * 0
                    * input port.
                    *
                    * 1 ~ 4
                    * output ports. (1: VC0 ~ 4: VC3)
                    */
                port@0 {
                        reg = <0>;
                        mipi_csi2_0_in: endpoint {
                                remote-endpoint = <&max96712_1_out>;
                                io-direction    = "input";
                                num-channel     = <4>;

                                   /*
                                    * 0: CH0 only, no data interleave
                                    * 1: DT only
                                    * 2: VC only
                                    * 3: VC and DT
                                    */
                                interleave-mode = <3>;
                                hs-settle = <37>;
                                data-lanes = <1 2 3 4>;
                        };
                };
                port@1 {
                        reg = <1>;
                        mipi_csi2_0_out0: endpoint {
                                remote-endpoint = <&videoinput4_in>;
                                io-direction    = "output";
                                channel         = <0>;
                                /*
                                    * 0: Single pixel mode
                                    * 1: Dual pixel mode (RAW8/10/12, YUV422)
                                    * 2: Quad pixel mode (RAW8/10/12)
                                    * 3: Invalid
                                    */
                                pixel-mode = <1>;
                        };
                };
                port@2 {
                        reg = <2>;
                        mipi_csi2_0_out1: endpoint {
                                remote-endpoint = <&videoinput5_in>;
                                io-direction    = "output";
                                channel         = <1>;
                                pixel-mode = <1>;
                        };
                };
                port@3 {
                        reg = <3>;
                        mipi_csi2_0_out2: endpoint {
                                remote-endpoint = <&videoinput6_in>;
                                io-direction    = "output";
                                channel         = <2>;
                                pixel-mode = <1>;
                        };
                };
                port@4 {
                        reg = <4>;
                        mipi_csi2_0_out3: endpoint {
                                remote-endpoint = <&videoinput7_in>;
                                io-direction    = "output";
                                channel         = <3>;
                                pixel-mode = <1>;
                        };
                };
        };
    };

    &videoinput4 {
        status          = "okay";
        cifport         = <&cifport             9>;
        /* memory-region
            *  - [0]: parking guideline
            *  - [1]: deinterlacing by viqe
            *  - [2]: preview
            *  - [3]: last frame
            */
        memory-region   = <0
                            0
                            &pmap_rearcamera4
                            0>;
        port {
                videoinput4_in: endpoint {
                        remote-endpoint = <&mipi_csi2_0_out0>;
                        io-direction    = "input";
                        stream-enable   = <1>;  // VIN_CTRL.SE
                        flush-vsync     = <1>;  // VIN_MISC.FVS
                };
        };
    };

    &videoinput5 {
        status          = "okay";
        cifport         = <&cifport             10>;
        /* memory-region
            *  - [0]: parking guideline
            *  - [1]: deinterlacing by viqe
            *  - [2]: preview
            *  - [3]: last frame
            */
        memory-region   = <0
                            0
                            &pmap_rearcamera5
                            0>;
        port {
                videoinput5_in: endpoint {
                        remote-endpoint = <&mipi_csi2_0_out1>;
                        io-direction    = "input";
                        stream-enable   = <1>;  // VIN_CTRL.SE
                        flush-vsync     = <1>;  // VIN_MISC.FVS
                };
        };
    };

    &videoinput6 {
        status          = "okay";
        cifport         = <&cifport             11>;
        /* memory-region
            *  - [0]: parking guideline
            *  - [1]: deinterlacing by viqe
            *  - [2]: preview
            *  - [3]: last frame
            */
        memory-region   = <0
                            0
                            &pmap_rearcamera6
                            0>;
        port {
                videoinput6_in: endpoint {
                        remote-endpoint = <&mipi_csi2_0_out2>;
                        io-direction    = "input";
                        stream-enable   = <1>;  // VIN_CTRL.SE
                        flush-vsync     = <1>;  // VIN_MISC.FVS
                };
           };
    };

    &videoinput7 {
        status          = "okay";
        cifport         = <&cifport             12>;
        /* memory-region
            *  - [0]: parking guideline
            *  - [1]: deinterlacing by viqe
            *  - [2]: preview
            *  - [3]: last frame
            */
        memory-region   = <0
                            0
                            &pmap_rearcamera7
                            0>;
        port {
                videoinput7_in: endpoint {
                        remote-endpoint = <&mipi_csi2_0_out3>;
                        io-direction    = "input";
                        stream-enable   = <1>;  // VIN_CTRL.SE
                        flush-vsync     = <1>;  // VIN_MISC.FVS
                };
        };
    };
    ```
4. Modify file {build_dir}/build/d3-g-topst-main/tmp/work/d3_g_topst_main-telechips-linux/linux-topst/5.10.205-r0/git/arch/arm64/boot/dts/telechips/tcc805x/override/topst-d3-g-i2c.dtsi as shown below
    ```
    @@ -62,10 +62,10 @@ MPQ7920_2_LDO4: ldo4 {

    &i2c6 {
            status = "disabled";
    -       port-mux = <35>;
    +       port-mux = <12>;
            pinctrl-names = "default", "sleep";
    -       pinctrl-0 = <&i2c35_bus_active>;
    -       pinctrl-1 = <&i2c35_bus_sleep>;
    +       pinctrl-0 = <&i2c12_bus_active>;
    +       pinctrl-1 = <&i2c12_bus_sleep>;

            #address-cells = <1>;
            #size-cells = <0>;
    @@ -84,10 +84,10 @@ &i2c3 {

    &i2c7 {
            status = "disabled";
    -       port-mux = <12>;
    +       port-mux = <35>;
            pinctrl-names = "default", "sleep";
    -       pinctrl-0 = <&i2c12_bus_active>;
    -       pinctrl-1 = <&i2c12_bus_sleep>;
    +       pinctrl-0 = <&i2c35_bus_active>;
    +       pinctrl-1 = <&i2c35_bus_sleep>;

            #address-cells = <1>;
            #size-cells = <0>;
    ```
5. Modify file {build_dir}/build/d3-g-topst-main/tmp/work/d3_g_topst_main-telechips-linux/linux-topst/5.10.205-r0/git/arch/arm64/boot/dts/telechips/tcc805x/tcc805x-videoinput.dtsi as shown below
    ```
    @@ -40,26 +40,26 @@ mipi_wrap: mipi_wrap {
                    * 0: select output of MIPI0
                    * 1: select output of MIPI1
                    */
    -               mipi-chmux-0 = <0>;
    +               mipi-chmux-0 = <1>;
                    mipi-chmux-1 = <1>;
    -               mipi-chmux-2 = <0>;
    -               mipi-chmux-3 = <0>;
    +               mipi-chmux-2 = <1>;
    +               mipi-chmux-3 = <1>;

                    /*
                    * 0: select output of MIPI1
                    * 1: select output of MIPI0
                    */
    -               mipi-chmux-4 = <0>;
    -               mipi-chmux-5 = <0>;
    -               mipi-chmux-6 = <0>;
    -               mipi-chmux-7 = <0>;
    +               mipi-chmux-4 = <1>;
    +               mipi-chmux-5 = <1>;
    +               mipi-chmux-6 = <1>;
    +               mipi-chmux-7 = <1>;

                    /*
                    * 1: bypass isp
                    * 0: use isp
                    */
                    isp0-bypass = <0>;
    -               isp1-bypass = <0>;
    +               isp1-bypass = <1>;
                    isp2-bypass = <1>;
                    isp3-bypass = <1>;
    ```
6. Modify file {build_dir}/build/d3-g-topst-main/tmp/work/d3_g_topst_main-telechips-linux/linux-topst/5.10.205-r0/git/include/dt-bindings/pmap/tcc805x/pmap-tcc805x-linux-videoinput.h as shown below
    ```
    @@ -21,13 +21,13 @@
     /* The number of buffers */
    #define FRAMES_CAMERA_VIQE             4
    #define FRAMES_CAMERA_PREVIEW0         4
    -#define FRAMES_CAMERA_PREVIEW1         4
    +#define FRAMES_CAMERA_PREVIEW1         0
    #define FRAMES_CAMERA_PREVIEW2         0
    #define FRAMES_CAMERA_PREVIEW3         0
    -#define FRAMES_CAMERA_PREVIEW4         0
    -#define FRAMES_CAMERA_PREVIEW5         0
    -#define FRAMES_CAMERA_PREVIEW6         0
    -#define FRAMES_CAMERA_PREVIEW7         0
    +#define FRAMES_CAMERA_PREVIEW4         4
    +#define FRAMES_CAMERA_PREVIEW5         4
    +#define FRAMES_CAMERA_PREVIEW6         4
    +#define FRAMES_CAMERA_PREVIEW7         4

    /* Reserved memory size */
    #define PMAP_SIZE_CAMERA_VIQE          \
    ```
7. 重新建置核心並產生 FAI 映像檔。  
    請返回建置目錄，並使用下列指令重新建置核心
    ```
    $ cd ${build_dir}/build/ai-g-topst-main/
    $ bitbake -C compile linux-topst
    $ cd ${build_dir}
    $ ./stitch-fai-ai.sh
    ```

依照上述指南完成建置後，GMSL 攝影機將以 video4、video5、video6 與 video7 出現在 /dev/ 之下。

#### 4.2.1.2 如何使用 MIPI1 連接埠
首先，您必須啟用 GMSL 攝影機與 SerDes 板的核心設定。  
請將下列項目新增至  
**{build_dir}/poky/meta-topst-bsp/recipes-kernel/linux/linux-topst/tcc805x/camera.cfg** file.
```
CONFIG_VIDEO_TCC_CXD5700=y
CONFIG_VIDEO_TCC_MAX9275=y
CONFIG_VIDEO_TCC_MAX96712=y
```
To prevent the source code from being removed during the build process, enable the following line, and comment out all occurrences of `TOPST_CAM_MODULE in {build_dir}/build/d3-g-topst-main/conf/local.conf:
```
#TOPST_CAM_MODULE = "ov5647"
#TOPST_CAM_MODULE = "imx219"
```
修改上述選項後，請使用下列指令重新建置映像檔。
```
$ bitbake -c cleansstate isp-firmware
$ bitbake -c cleansstate isp-server
$ bitbake telechips-topst-image
```

接著，您必須修改核心中的裝置樹。請依照下列指南套用變更並重新建置映像檔。
1. Modify file {build_dir}/build/d3-g-topst-main/tmp/work/d3_g_topst_main-telechips-linux/linux-topst/5.10.205-r0/git/arch/arm64/boot/dts/telechips/tcc805x/override/tcc805x-videoinput-camera-module.dtsi as shown below
    ```
    //#include "tcc805x-videoinput-mipi0-ov5647.dtsi"
    //#include "tcc805x-videoinput-mipi0-imx219.dtsi"
    +#include "tcc805x-videoinput-mipi1-fhd.dtsi"
    ```
2. Modify file {build_dir}/build/d3-g-topst-main/tmp/work/d3_g_topst_main-telechips-linux/linux-topst/5.10.205-r0/git/arch/arm64/boot/dts/telechips/tcc805x/tcc805x-videoinput.dtsi as shown below
    ```
    @@ -40,26 +40,26 @@ mipi_wrap: mipi_wrap {
                     * 0: select output of MIPI0
                     * 1: select output of MIPI1
                    */
                    mipi-chmux-0 = <0>;
                    mipi-chmux-1 = <1>;
    +               mipi-chmux-1 = <0>;
                    mipi-chmux-2 = <0>;
                    mipi-chmux-3 = <0>;

                    /*
                    * 0: select output of MIPI1
                    * 1: select output of MIPI0
                    */
                    mipi-chmux-4 = <0>;
                    mipi-chmux-5 = <0>;
                    mipi-chmux-6 = <0>;
                    mipi-chmux-7 = <0>;

                    /*
                    * 1: bypass isp
                    * 0: use isp
                    */
                    isp0-bypass = <0>;
    -               isp1-bypass = <0>;
    +               isp1-bypass = <1>;
                    isp2-bypass = <1>;
                    isp3-bypass = <1>;
    ```
3. Modify file {build_dir}/build/d3-g-topst-main/tmp/work/d3_g_topst_main-telechips-linux/linux-topst/5.10.205-r0/git/include/dt-bindings/pmap/tcc805x/pmap-tcc805x-linux-videoinput.h as shown below
    ```
    @@ -21,13 +21,13 @@
    /* The number of buffers */
    #define FRAMES_CAMERA_VIQE             4
    #define FRAMES_CAMERA_PREVIEW0         4
    -#define FRAMES_CAMERA_PREVIEW1         4
    +#define FRAMES_CAMERA_PREVIEW1         0
    #define FRAMES_CAMERA_PREVIEW2         0
    #define FRAMES_CAMERA_PREVIEW3         0
    -#define FRAMES_CAMERA_PREVIEW4         0
    -#define FRAMES_CAMERA_PREVIEW5         0
    -#define FRAMES_CAMERA_PREVIEW6         0
    -#define FRAMES_CAMERA_PREVIEW7         0
    +#define FRAMES_CAMERA_PREVIEW4         4
    +#define FRAMES_CAMERA_PREVIEW5         4
    +#define FRAMES_CAMERA_PREVIEW6         4
    +#define FRAMES_CAMERA_PREVIEW7         4

    /* Reserved memory size */
    #define PMAP_SIZE_CAMERA_VIQE          \
    ```
4. 重新建置核心並產生 FAI 映像檔。  
    請返回建置目錄，並使用下列指令重新建置核心。
    ```
    $ cd ${build_dir}/build/ai-g-topst-main/
    $ bitbake -C compile linux-topst
    $ cd ${build_dir}
    $ ./stitch-fai-ai.sh
    ```

依照上述指南完成建置後，GMSL 攝影機將以 video4、video5、video6 與 video7 出現在 /dev/ 之下。

#### 4.2.1.3 如何使用 MIPI0、1 連接埠
首先，您必須啟用 GMSL 攝影機與 SerDes 板的核心設定。  
請將下列項目新增至  
**{build_dir}/poky/meta-topst-bsp/recipes-kernel/linux/linux-topst/tcc805x/camera.cfg** file.
```
CONFIG_VIDEO_TCC_CXD5700=y
CONFIG_VIDEO_TCC_MAX9275=y
CONFIG_VIDEO_TCC_MAX96712=y
```

To prevent the source code from being removed during the build process, enable the following line, and comment out all occurrences of `TOPST_CAM_MODULE in {build_dir}/build/d3-g-topst-main/conf/local.conf:
```
#TOPST_CAM_MODULE = "ov5647"
#TOPST_CAM_MODULE = "imx219"
```

修改上述選項後，請使用下列指令重新建置映像檔。
```
$ bitbake -c cleansstate isp-firmware
$ bitbake -c cleansstate isp-server
$ bitbake telechips-topst-image
```

由於顯示與 videoinput 路徑在 VIOC 中重疊，因此無法使用四顯示器擴充功能。所以您必須先在顯示設定中停用其中一條衝突的路徑。
1. Modify file {build_dir}/build/d3-g-topst-main/tmp/work/d3_g_topst_main-telechips-linux/linux-topst/5.10.205-r0/git/arch/arm64/boot/dts/telechips/tcc805x/override/topst-d3-g-disp.dtsi as shown below
    ```
    @@ -437,7 +437,7 @@ dpv14_tx: dpv14_tx@12400000 {
                    sink_vcp_id = <1 2 3 4>;

                    /* default displayport configuration */
    -               dp-video-codes = <0 16 0 16 0 16 0 16>; /* video standard video codes */
    +               dp-video-codes = <0 16 0 16 0 16>; /* video standard video codes */
                    dp-phy-lane-swap = <1>;
                    dp-max-lane = <4>;
                    dp-max-rate = <3>;
    ```
2. Modify file {build_dir}/build/d3-g-topst-main/tmp/work/d3_g_topst_main-telechips-linux/linux-topst/5.10.205-r0/git/arch/arm64/boot/dts/telechips/tcc805x/override/topst-d3-g-display.dtsi as shown below
    ```
    @@ -34,9 +32,6 @@ &tccdrm_vioc2 {
            status = "okay";
    };

    -&tccdrm_vioc3 {
    -       status = "okay";
    -};

    &vioc0_out {
            vioc0_output_dp0: endpoint@0 {
    @@ -59,13 +54,6 @@ vioc2_output_dp2: endpoint@0 {
            };
    };

    -&vioc3_out {
    -       vioc3_output_dp3: endpoint@0 {
    -               reg = <0>;
    -               remote-endpoint = <&dp3_in_vioc3>;
    -       };
    -};
    -

    /* tcdrm dp */
    &tccdrm_dp0 {
    @@ -80,9 +68,6 @@ &tccdrm_dp2 {
            status = "okay";
    };

    -&tccdrm_dp3 {
    -       status = "okay";
    -};

    /* vioc0_output_dp0 -> dp0_in_vioc0 */
    &dp0_in {
    @@ -108,14 +93,6 @@ dp2_in_vioc2: endpoint@0 {
            };
    };

    -/* vioc3_output_dp3 -> dp3_in_vioc3 */
    -&dp3_in {
    -       dp3_in_vioc3: endpoint@0 {
    -               reg = <0>;
    -               remote-endpoint = <&vioc3_output_dp3>;
    -       };
    -};
    -
    /* screen_share_display_out -> tcc_drm_dummy0  */
    /* screen share */
    &tccdrm_screen_share {
    --
    ```

接著，您必須修改核心中的裝置樹。請依照下列指南套用變更並重新建置映像檔。
1. Modify file {build_dir}/build/d3-g-topst-main/tmp/work/d3_g_topst_main-telechips-linux/linux-topst/5.10.205-r0/git/arch/arm64/boot/dts/telechips/tcc805x/override/tcc805x-videoinput-camera-module.dtsi as shown below
    ```
    //#include "tcc805x-videoinput-mipi0-ov5647.dtsi"
    //#include "tcc805x-videoinput-mipi0-imx219.dtsi"
    +#include "tcc805x-videoinput-mipi0-fhd.dtsi"
    +#include "tcc805x-videoinput-mipi1-fhd.dtsi"
    ```
2. Create file {build_dir}/build/d3-g-topst-main/tmp/work/d3_g_topst_main-telechips-linux/linux-topst/5.10.205-r0/git/arch/arm64/boot/dts/telechips/tcc805x/override/tcc805x-videoinput-mipi0-fhd.dtsi as shown below
    ```
    // SPDX-License-Identifier: (GPL-2.0-or-later OR MIT)
    /*
    * Copyright (C) Telechips Inc.
    */

    &i2c7 {
    	status = "okay";
    };

    &cxd5700 {
    	/* ISP of camera module */
    	status		= "okay";
    	port {
		    cxd5700_out: endpoint {
    			remote-endpoint = <&max9275_in>;
			    io-direction	= "output";
		    };
	    };
    };

    &max9275 {
    	/* serializer */
    	status		= "okay";
    	ports {
		    #address-cells = <1>;
		    #size-cells = <0>;
		    port@0 {
    			reg = <0>;
			    max9275_in: endpoint {
    				remote-endpoint = <&cxd5700_out>;
				    io-direction	= "input";
			    };
		    };
		    port@1 {
    			reg = <1>;
			    max9275_out: endpoint {
    				remote-endpoint = <&max96712_in0>;
				    io-direction	= "output";
			    };
		    };
	    };
    };

    &max96712 {
    	/* deserializer */
    	status		= "okay";
    	pvd-name	= "fhd";
    	/*
	    * broadcasting mode access each linked devices
	    * by the same I2C slave address.
	    *
	    * Also,
	    * using the serdes I2C address mapping table,
	    * each liked devices can be accessed
	    * by the unique I2C slave address.
	    */
	    broadcasting-mode;
	    ports {
    		#address-cells = <1>;
		    #size-cells = <0>;
		    /*
		    * 0 ~ 3
		    * input ports. The number is matched with VC
		    *
		    * 4
		    * output port.
		    */
		    port@0 {
    			reg = <0>;
			    max96712_in0: endpoint {
    				remote-endpoint = <&max9275_out>;
				    io-direction	= "input";
				    channel		= <0>;
			    };
		    };
		    port@1 {
    			reg = <1>;
			    max96712_in1: endpoint {
    				remote-endpoint = <&max9275_out>;
				    io-direction	= "input";
				    channel		= <1>;
			    };
		    };
		    port@2 {
    			reg = <2>;
			    max96712_in2: endpoint {
    				remote-endpoint = <&max9275_out>;
				    io-direction	= "input";
				    channel		= <2>;
			    };  
		    };
		    port@3 {
    			reg = <3>;
			    max96712_in3: endpoint {
    				remote-endpoint = <&max9275_out>;
				    io-direction	= "input";
				    channel		= <3>;
			    };
		    };
		    port@4 {
    			reg = <4>;
			    max96712_out: endpoint {
    				remote-endpoint = <&mipi_csi2_0_in>;
				    io-direction	= "output";
				    channel		= <0>;
			    };
		    };
	    };
    };

    &mipi_csi2_0 {
    	status = "okay";
    	ports {
		    #address-cells = <1>;
		    #size-cells = <0>;
		    /*
		    * 0
		    * input port.
		    *
		    * 1 ~ 4
		    * output ports. (1: VC0 ~ 4: VC3)
		    */
		    port@0 {
    			reg = <0>;
			    mipi_csi2_0_in: endpoint {
    				remote-endpoint	= <&max96712_out>;
				    io-direction	= "input";
				    num-channel	= <4>;

				    /*
				    * 0: CH0 only, no data interleave
				    * 1: DT only
				    * 2: VC only
				    * 3: VC and DT
				    */
				    interleave-mode = <3>;
				    hs-settle = <37>;
				    data-lanes = <1 2 3 4>;
			    };
		    };
		    port@1 {
    			reg = <1>;
			    mipi_csi2_0_out0: endpoint {
    				remote-endpoint	= <&videoinput0_in>;
				    io-direction	= "output";
				    channel		= <0>;
				    /*
				    * 0: Single pixel mode
				    * 1: Dual pixel mode (RAW8/10/12, YUV422)
				    * 2: Quad pixel mode (RAW8/10/12)
				    * 3: Invalid
				    */
				    pixel-mode = <1>;
			    };
		    };
		    port@2 {
    			reg = <2>;
	    		mipi_csi2_0_out1: endpoint {
    				remote-endpoint	= <&videoinput1_in>;
				    io-direction	= "output";
				    channel		= <1>;
				    pixel-mode = <1>;
			    };
		    };
		    port@3 {
    			reg = <3>;
			    mipi_csi2_0_out2: endpoint {
    				remote-endpoint	= <&videoinput2_in>;
				    io-direction	= "output";
				    channel		= <2>;
				    pixel-mode = <1>;
			    };
		    };
		    port@4 {
    			reg = <4>;
			    mipi_csi2_0_out3: endpoint {
    				remote-endpoint	= <&videoinput3_in>;
				    io-direction	= "output";
				    channel		= <3>;
				    pixel-mode = <1>;
			    };
		    };
	    };
    };

    &videoinput0 {
    	status		= "okay";
    	cifport		= <&cifport		5>;
    	/* memory-region
	    *  - [0]: parking guideline
	    *  - [1]: deinterlacing by viqe
	    *  - [2]: preview
	    *  - [3]: last frame
	    */
	    memory-region	= <0
			    0
			    &pmap_rearcamera
			    0>;
	    port {
    		videoinput0_in: endpoint {
			    remote-endpoint	= <&mipi_csi2_0_out0>;
			    io-direction	= "input";
			    stream-enable	= <1>;	// VIN_CTRL.SE
			    flush-vsync	= <1>;	// VIN_MISC.FVS
		    };
	    };
    };

    &videoinput1 {
    	status		= "okay";
    	cifport		= <&cifport		6>;
    	/* memory-region
	    *  - [0]: parking guideline
	    *  - [1]: deinterlacing by viqe
	    *  - [2]: preview
	    *  - [3]: last frame
	    */
	    memory-region	= <0
			    0
			    &pmap_rearcamera1
			    0>;
	    port {
    		videoinput1_in: endpoint {
			    remote-endpoint	= <&mipi_csi2_0_out1>;
    			io-direction	= "input";
			    stream-enable	= <1>;	// VIN_CTRL.SE
    			flush-vsync	= <1>;	// VIN_MISC.FVS
		    };
	    };
    };

    &videoinput2 {
    	status		= "okay";
    	cifport		= <&cifport		7>;
    	/* memory-region
	    *  - [0]: parking guideline
	    *  - [1]: deinterlacing by viqe
	    *  - [2]: preview
	    *  - [3]: last frame
	    */
	    memory-region	= <0
			    0
			    &pmap_rearcamera2
			    0>;
	    port {
    		videoinput2_in: endpoint {
			    remote-endpoint	= <&mipi_csi2_0_out2>;
			    io-direction	= "input";
			    stream-enable	= <1>;	// VIN_CTRL.SE
			    flush-vsync	= <1>;	// VIN_MISC.FVS
		    };
	    };
    };

    &videoinput3 {
    	status		= "okay";
	    cifport		= <&cifport		8>;
	    /* memory-region
	    *  - [0]: parking guideline
	    *  - [1]: deinterlacing by viqe
	    *  - [2]: preview
	    *  - [3]: last frame
	    */
	    memory-region	= <0
			    0
			    &pmap_rearcamera3
			    0>;
	    port {
    		videoinput3_in: endpoint {
			    remote-endpoint	= <&mipi_csi2_0_out3>;
			    io-direction	= "input";
			    stream-enable	= <1>;	// VIN_CTRL.SE
			    flush-vsync	= <1>;	// VIN_MISC.FVS
		    };
	    };
    };
    ```
3. Modify file {build_dir}/build/d3-g-topst-main/tmp/work/d3_g_topst_main-telechips-linux/linux-topst/5.10.205-r0/git/arch/arm64/boot/dts/telechips/tcc805x/tcc805x-videoinput.dtsi as shown below
    ```
    @@ -40,26 +40,26 @@ mipi_wrap: mipi_wrap {
                     * 0: select output of MIPI0
                    * 1: select output of MIPI1
                    */
                    mipi-chmux-0 = <0>;
    -               mipi-chmux-1 = <1>;
    +               mipi-chmux-1 = <0>;
                    mipi-chmux-2 = <0>;
                    mipi-chmux-3 = <0>;

                    /*
                    * 0: select output of MIPI1
                    * 1: select output of MIPI0
                    */
                    mipi-chmux-4 = <0>;
                    mipi-chmux-5 = <0>;
                    mipi-chmux-6 = <0>;
                    mipi-chmux-7 = <0>;

                    /*
                    * 1: bypass isp
                    * 0: use isp
                    */
    -               isp0-bypass = <0>;
    -               isp1-bypass = <0>;
    +               isp0-bypass = <1>;
    +               isp1-bypass = <1>;
                    isp2-bypass = <1>;
                    isp3-bypass = <1>;
    ```
4. Modify file {build_dir}/build/d3-g-topst-main/tmp/work/d3_g_topst_main-telechips-linux/linux-topst/5.10.205-r0/git/ include/dt-bindings/pmap/tcc805x/pmap-tcc805x-linux-videoinput.h as shown below
    ```
    @@ -21,13 +21,13 @@
     /* The number of buffers */
    #define FRAMES_CAMERA_VIQE             4
    #define FRAMES_CAMERA_PREVIEW0         4
    #define FRAMES_CAMERA_PREVIEW1         4
    -#define FRAMES_CAMERA_PREVIEW2         0
    -#define FRAMES_CAMERA_PREVIEW3         0
    -#define FRAMES_CAMERA_PREVIEW4         0
    -#define FRAMES_CAMERA_PREVIEW5         0
    -#define FRAMES_CAMERA_PREVIEW6         0
    -#define FRAMES_CAMERA_PREVIEW7         0
    +#define FRAMES_CAMERA_PREVIEW2         0
    +#define FRAMES_CAMERA_PREVIEW3         0
    +#define FRAMES_CAMERA_PREVIEW4         4
    +#define FRAMES_CAMERA_PREVIEW5         4
    +#define FRAMES_CAMERA_PREVIEW6         4
    +#define FRAMES_CAMERA_PREVIEW7         4

    /* Reserved memory size */
    #define PMAP_SIZE_CAMERA_VIQE          \
    ```
5. 重新建置核心並產生 FAI 映像檔。  
    請返回建置目錄，並使用下列指令重新建置核心
    ```
    $ cd ${build_dir}/build/ai-g-topst-main/
    $ bitbake -C compile linux-topst
    $ cd ${build_dir}
    $ ./stitch-fai-ai.sh
    ```
依照上述指南完成建置後，GMSL 攝影機將以 video0、video1、video2、video3、4、video5、video6 與 video7 出現在 /dev/ 之下。

### 4.2.2 AI-G GMSL 攝影機設定指南
使用 Deserializer 板可將最多四台攝影機連接至單一 MIPI CSI 連接埠。  
AI-G 開發板提供每 lane 1.5 Gbps 的 MIPI CSI 資料頻寬，可讓最多三台 FHD 攝影機同時運作。因此，本指南說明三台 FHD GMSL 攝影機的連接方式。  
若使用 HD 攝影機，最多可支援四台。

**註：** 本指南使用 IMX290 (cxd5700) FHD GMSL 攝影機。  
若您打算使用其他 GMSL 攝影機，將需要額外的攝影機移植作業。

#### 4.2.2.1 如何使用 MIPI CSI 連接埠
首先，您必須啟用 GMSL 攝影機與 SerDes 板的核心設定。  
請將下列項目新增至  
**{build_dir}/poky/meta-topst-bsp/recipes-kernel/linux/linux-topst/tcc750x/camera.cfg** file.
```
CONFIG_VIDEO_TCC_CXD5700=y
CONFIG_VIDEO_TCC_MAX9275=y
CONFIG_VIDEO_TCC_MAX96712=y
```
To prevent the source code from being removed during the build process, enable the following line, and comment out all occurrences of `TOPST_CAM_MODULE in {build_dir}/build/ai-g-topst-main/conf/local.conf:
```
#TOPST_CAM_MODULE = "ov5647"
#TOPST_CAM_MODULE = "imx219"
```
修改上述選項後，請使用下列指令重新建置映像檔。
```
$ bitbake -c cleansstate isp-firmware
$ bitbake -c cleansstate isp-server
$ bitbake telechips-topst-ai-image
```

接著，您必須修改核心中的裝置樹。請依照下列指南套用變更並重新建置映像檔。
1. Modify file {build_dir}/build/d3-g-topst-main/tmp/work/d3_g_topst_main-telechips-linux/linux-topst/5.10.205-r0/git/arch/arm64/boot/dts/telechips/tcc805x/override/tcc805x-videoinput-camera-module.dtsi as shown below
    ```
    //#include "tcc805x-videoinput-mipi0-ov5647.dtsi"
    //#include "tcc805x-videoinput-mipi0-imx219.dtsi"
    +#include " tcc750x-videoinput-odw-mipi0-fhd.dtsi"
    ```
2. Modify file {build_dir}/build/d3-g-topst-main/tmp/work/d3_g_topst_main-telechips-linux/linux-topst/5.10.205-r0/git/drivers/media/platform/tcc-mipi-csi2/csi2_s/v2.0/ tcc-mipi-csi2-csis-reg.h. as shown below
    ```
    @@ -6,7 +6,7 @@
    #ifndef TCC_MIPI_CSI2_CSIS_REG_H
    #define TCC_MIPI_CSI2_CSIS_REG_H
    
    -#define MAX_VC                         ((uint32_t)1)
    +#define MAX_VC                         ((uint32_t)4U)
    ```
3. 重新建置核心並產生 FAI 映像檔。  
    請返回建置目錄，並使用下列指令重新建置核心
    ```
    $ cd ${build_dir}/build/ai-g-topst-main/
    $ bitbake -C compile linux-topst
    $ cd ${build_dir}
    $ ./stitch-fai-ai.sh
    ```
依照上述指南完成建置後，GMSL 攝影機將以 video0、video1 與 video2 出現在 /dev/ 之下。

# 5. 範例程式碼與指令
本章提供範例程式碼與指令，示範如何在 D3-G 與 AI-G 平台上使用 MIPI CSI 攝影機、GMSL 攝影機與 USB 攝影機。本節簡要說明攝影機的播放方式：  
在 D3-G 上，可使用 GStreamer 或 OpenCV 檢視攝影機串流，  
而在 AI-G 上，攝影機播放則透過應用程式框架處理。

## 5.1 攝影機播放的範例程式碼與指令
### 5.1.1 MIPI CSI 攝影機使用指南
本節說明如何在 Yocto 與 Ubuntu 環境中顯示 MIPI CSI 攝影機視訊。

#### 5.1.1.1 D3-G 上的 MIPI CSI 攝影機使用指南 (OV5647)
##### 5.1.1.1.1 在 Yocto 映像檔上使用 OV5647
使用 [topst.ai DOCS 頁面](https://topst.ai/tech/docs?page=624bd237b3013e87c05c125b8031e2f370ccca2b) 提供的官方 Yocto 映像檔，或自行建置 Yocto 所產生的映像檔時，OV5647 攝影機會以 1296×972 @ 30 fps 的預設解析度運作。因此，在此環境中的攝影機播放將使用 1296×972 @ 30 fps。  
請依照以下步驟操作：
1. 停止目前執行中的 topst-welcome 服務
    ```
    $ sudo systemctl stop topst-welcome
    ```
2. 在 UART 主控台中輸入以下指令
    ```
    $ export XDG_RUNTIME_DIR=/run/user/root
    ```
3. 使用如下所示的 GStreamer 指令播放攝影機串流
    ```
    $ gst-launch-1.0 v4l2src device=/dev/video0 io-mode=2 ! video/x-raw,format=NV12,width=1296,height=972,framerate=30/1 ! videoconvert ! waylandsink sync=false
    ```
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/accessories/Camera/5.1%201296%C3%97972%20ov5647%20camera%20out%20display%20on%20yocto.png"></p>
<p align="center"><strong>圖 5.1 Yocto 上 1296×972 OV5647 攝影機輸出顯示</strong></p>

**註：** 雖然解析度為 1296×972，但您可以在指令結尾加上 fullscreen=true 選項，以全螢幕播放視訊。

##### 5.1.1.1.2 在 Ubuntu 映像檔上使用 OV5647
使用 [topst.ai DOCS 頁面](https://topst.ai/tech/docs?page=624bd237b3013e87c05c125b8031e2f370ccca2b) 提供的官方 Ubuntu 映像檔時，OV5647 攝影機會以 1296×972 @ 30 fps 的預設解析度運作。因此，在此環境中的攝影機播放將使用 1296×972 @ 30 fps。  
請依照以下步驟操作：
1. - 若透過 UART 連接：請在以 topst 帳號登入後，於 UART 主控台中輸入以下指令
    ```
    $ export XDG_RUNTIME_DIR=/run/user/1000
    ```
    - 若直接在顯示器上操作：請開啟終端機視窗
2. 使用如下所示的 GStreamer 指令播放攝影機串流。由於 Ubuntu 上無法使用硬體加速的 Wayland 算繪，因此改以 H.265 編碼／解碼，利用 VPU 加速進行播放
    ```
    $ gst-launch-1.0 v4l2src device=/dev/video0 io-mode=2 ! video/x-raw,format=NV12,width=1280,height=720,framerate=30/1 ! v4l2h265enc ! h265parse ! v4l2h265dec ! videoconvert ! waylandsink sync=false
    ```
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/accessories/Camera/5.2%201296%C3%97972%20ov5647%20camera%20out%20display%20on%20ubuntu.png"></p>
<p align="center"><strong>圖 5.2 Ubuntu 上 1296×972 OV5647 攝影機輸出顯示</strong></p>

**註：** 雖然解析度為 1296×972，但您可以在指令結尾加上 fullscreen=true 選項，以全螢幕播放視訊。

除了 GStreamer 之外，您也可以使用 OpenCV 顯示攝影機串流。請依照以下步驟，輕鬆使用 OpenCV 預覽攝影機視訊。
1. 安裝 OpenCV
    ```
    $ sudo apt-get install python3-opencv
    ```
2. 在 opencv_cam.py 檔案中寫入以下程式碼
    ```
    import cv2
    
    pipeline = (
        "v4l2src device=/dev/video0 io-mode=2 ! "
        "video/x-raw,format=NV12,width=1296,height=972,framerate=30/1 ! "
        "videoconvert ! video/x-raw,format=BGR ! appsink sync=false"
    )
    
    cap = cv2.VideoCapture(pipeline, cv2.CAP_GSTREAMER)
    
    if not cap.isOpened():
        print("ERROR: cannot open camera via GStreamer")
        exit()
    
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Frame read error")
            break
    
        cv2.imshow("Camera", frame)
        if cv2.waitKey(1) == 27:
            break
    
    cap.release()
    cv2.destroyAllWindows()
    ```
3. 使用 Python 執行 opencv_cam.py
    ```
    $ python3 opencv_cam.py
    ```
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/accessories/Camera/5.3%201296%C3%97972%20opencv%20ov5647%20camera%20out%20display%20on%20ubuntu.png"></p>
<p align="center"><strong>圖 5.3 在 Ubuntu 上以 OpenCV 執行的 1296×972 OV5647 攝影機輸出</strong></p>

##### 5.1.1.1.3 D3-G 上各解析度的 Gstreawmer 管線設定
請為每個解析度指定適當的 GStreamer 管線選項，然後執行攝影機串流。
1. 1920x1080 @ 30fps
    ```
    $ gst-launch-1.0 v4l2src device=/dev/video0 io-mode=2 ! video/x-raw,format=NV12,width=1920,height=1080,framerate=30/1 ! videoconvert ! waylandsink sync=false
    ```
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/accessories/Camera/5.4%201920x1080%20ov5647%20camera%20out%20display%20on%20yocto.png"></p>
    <p align="center"><strong>圖 5.4 Yocto 上 1920x1080 OV5647 攝影機輸出顯示</strong></p>
2. 1296x972 @ 30fps
    ```
    $ gst-launch-1.0 v4l2src device=/dev/video0 io-mode=2 ! video/x-raw,format=NV12,width=1296,height=972,framerate=30/1 ! videoconvert ! waylandsink sync=false
    ```
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/accessories/Camera/5.1%201296%C3%97972%20ov5647%20camera%20out%20display%20on%20yocto.png"></p>
    <p align="center"><strong>圖 5.5 Yocto 上 1296x972 OV5647 攝影機輸出顯示</strong></p>
3. 640x480 @ 60fps
    ```
    $ gst-launch-1.0 v4l2src device=/dev/video0 io-mode=2 ! video/x-raw,format=NV12,width=640,height=480,framerate=60/1 ! videoconvert ! waylandsink sync=false
    ```
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/accessories/Camera/5.6%20640x480%20ov5647%20camera%20out%20display%20on%20yocto.png"></p>
    <p align="center"><strong>圖 5.6 Yocto 上 640x480 OV5647 攝影機輸出顯示</strong></p>

此外，您也可以設定使用 H.265 編碼器與解碼器的管線，以啟用硬體加速播放。
1. 1920x1080 @ 30fps
    ```
    $ gst-launch-1.0 v4l2src device=/dev/video0 io-mode=2 ! video/x-raw,format=NV12,width=1920,height=1080,framerate=30/1 ! v4l2h265enc ! h265parse ! v4l2h265dec ! videoconvert ! waylandsink sync=false
    ```
2. 1296x972 @ 30fps
    ```
    $ gst-launch-1.0 v4l2src device=/dev/video0 io-mode=2 ! video/x-raw,format=NV12,width=1280,height=720,framerate=30/1 !  v4l2h265enc ! h265parse ! v4l2h265dec ! videoconvert ! waylandsink sync=false
    ```
3. 640x480 @ 60fps
    ```
    $ gst-launch-1.0 v4l2src device=/dev/video0 io-mode=2 ! video/x-raw,format=NV12,width=640,height=480,framerate=60/1 ! v4l2h265enc ! h265parse ! v4l2h265dec ! videoconvert ! waylandsink sync=false
    ```

    如需變更解析度，請參閱第 4.1.2.2 節。

#### 5.1.1.2 D3-G 上的 MIPI CSI 攝影機使用指南 (IMX219)
##### 5.1.1.2.1 在 Yocto 映像檔上使用 IMX219
使用 [topst.ai DOCS 頁面](https://topst.ai/tech/docs?page=624bd237b3013e87c05c125b8031e2f370ccca2b) 提供的官方 Yocto 映像檔，或自行建置 Yocto 所產生的映像檔時，IMX219 攝影機會以 1640×1232 @ 30 fps 的預設解析度運作。因此，在此環境中的攝影機播放將使用 1640×1232 @ 30 fps。  
請依照以下步驟操作：
1. 停止目前執行中的 topst-welcome 服務
    ```
    $ sudo systemctl stop topst-welcome
    ```
2. 在 UART 主控台中輸入以下指令
    ```
    $ export XDG_RUNTIME_DIR=/run/user/root
    ```
3. 使用如下所示的 GSTreamer 指令播放攝影機串流
    ```
    $ gst-launch-1.0 v4l2src device=/dev/video0 io-mode=2 ! video/x-raw,format=NV12,width=1640,height=1232,framerate=30/1 ! videoconvert ! waylandsink sync=false
    ```
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/accessories/Camera/5.7%201640x1232%20imx219%20camera%20out%20display%20on%20yocto.png"></p>
<p align="center"><strong>圖 5.7 Yocto 上 1640x972 IMX219 攝影機輸出顯示</strong></p>

**註：** 雖然解析度為 1640×1232，但您可以在指令結尾加上 fullscreen=true 選項，以全螢幕播放視訊。

##### 5.1.1.2.2 在 Ubuntu 映像檔上使用 IMX219
使用 [topst.ai DOCS 頁面](https://topst.ai/tech/docs?page=624bd237b3013e87c05c125b8031e2f370ccca2b) 提供的官方 Ubuntu 映像檔時，IMX219 攝影機會以 1640×1232 @ 30 fps 的預設解析度運作。因此，在此環境中的攝影機播放將使用 1640×1232 @ 30 fps。  
請依照以下步驟操作：
1. - 若透過 UART 連接：請在以 topst 帳號登入後，於 UART 主控台中輸入以下指令
    ```
    $ export XDG_RUNTIME_DIR=/run/user/1000
    ```
    - 若直接在顯示器上操作：請開啟終端機視窗
2. 使用如下所示的 GStreamer 指令播放攝影機串流。由於 Ubuntu 上無法使用硬體加速的 Wayland 算繪，因此改以 H.265 編碼／解碼，利用 VPU 加速進行播放
    ```
    $ gst-launch-1.0 v4l2src device=/dev/video0 io-mode=2 ! video/x-raw,format=NV12,width=1600,height=1200,framerate=30/1 ! v4l2h265enc ! h265parse ! v4l2h265dec ! videoconvert ! waylandsink sync=false
    ```
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/accessories/Camera/5.8%201640x1232%20imx219%20camera%20out%20display%20on%20ubuntu.png"></p>
<p align="center"><strong>圖 5.8 Ubuntu 上 1640x972 IMX219 攝影機輸出顯示</strong></p>

**註：** 雖然解析度為 1640×1232，但您可以在指令結尾加上 fullscreen=true 選項，以全螢幕播放視訊。

除了 GStreamer 之外，您也可以使用 OpenCV 顯示攝影機串流。請依照以下步驟，輕鬆使用 OpenCV 預覽攝影機視訊。
1. 安裝 OpenCV
    ```
    $ sudo apt-get install python3-opencv
    ```
2. 在 opencv_cam.py 檔案中寫入以下程式碼。
    ```
    import cv2
    
    pipeline = (
        "v4l2src device=/dev/video0 io-mode=2 ! "
        "video/x-raw,format=NV12,width=1640,height=1232,framerate=30/1 ! "
        "videoconvert ! video/x-raw,format=BGR ! appsink sync=false"
    )
    
    cap = cv2.VideoCapture(pipeline, cv2.CAP_GSTREAMER)
    
    if not cap.isOpened():
        print("ERROR: cannot open camera via GStreamer")
        exit()
    
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Frame read error")
            break
    
        cv2.imshow("Camera", frame)
        if cv2.waitKey(1) == 27:
            break
    
    cap.release()
    cv2.destroyAllWindows()
    ```
3. 使用 Python 執行 opencv_cam.py
```
$ python3 opencv_cam.py
```
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/accessories/Camera/5.9%201640x1232%20opencv%20imx219%20camera%20out%20display.png"></p>
<p align="center"><strong>圖 5.9 在 Ubuntu 上以 OpenCV 執行的 1640×1232 IMX219 攝影機輸出</strong></p>

##### 5.1.1.2.3 D3-G 上各解析度的 GStreamer 管線設定
請為每個解析度指定適當的 GStreamer 管線選項，然後執行攝影機串流。
1. 1920x1080 @ 30fps
    ```
    $ gst-launch-1.0 v4l2src device=/dev/video0 io-mode=2 ! video/x-raw,format=NV12,width=1920,height=1080,framerate=30/1 ! videoconvert ! waylandsink sync=false
    ```
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/accessories/Camera/5.10%201920x1080%20imx219%20camera%20out%20display%20on%20yocto.png"></p>
    <p align="center"><strong>圖 5.10 Yocto 上 1920x1080 IMX219 攝影機輸出顯示</strong></p>
2. 1640x1232 @ 30fps
    ```
    $ gst-launch-1.0 v4l2src device=/dev/video0 io-mode=2 ! video/x-raw,format=NV12,width=1640,height=1232,framerate=30/1 ! videoconvert ! waylandsink sync=false
    ```
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/accessories/Camera/5.7%201640x1232%20imx219%20camera%20out%20display%20on%20yocto.png"></p>
    <p align="center"><strong>圖 5.11 Yocto 上 1620x1232 IMX219 攝影機輸出顯示</strong></p>
3. 640x480 @ 30fps
    ```
    $ gst-launch-1.0 v4l2src device=/dev/video0 io-mode=2 ! video/x-raw,format=NV12,width=640,height=480,framerate=30/1 ! videoconvert ! waylandsink sync=false
    ```
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/accessories/Camera/5.12%20640x480%20imx219%20camera%20out%20display%20on%20yocto.png"></p>
    <p align="center"><strong>圖 5.12 Yocto 上 640x480 IMX219 攝影機輸出顯示</strong></p>

此外，您也可以設定使用 H.265 編碼器與解碼器的管線，以啟用硬體加速播放。
1. 1920x1080 @ 30fps
    ```
    $ gst-launch-1.0 v4l2src device=/dev/video0 io-mode=2 ! video/x-raw,format=NV12,width=1920,height=1080,framerate=30/1 ! v4l2h265enc ! h265parse ! v4l2h265dec ! videoconvert ! waylandsink sync=false
    ```
2. 1640x1232 @ 30fps
    ```
    $ gst-launch-1.0 v4l2src device=/dev/video0 io-mode=2 ! video/x-raw,format=NV12,width=1600,height=1200,framerate=30/1 !  v4l2h265enc ! h265parse ! v4l2h265dec ! videoconvert ! waylandsink sync=false
    ```
3. 640x480 @ 30fps
    ```
    $ gst-launch-1.0 v4l2src device=/dev/video0 io-mode=2 ! video/x-raw,format=NV12,width=640,height=480,framerate=30/1 ! v4l2h265enc ! h265parse ! v4l2h265dec ! videoconvert ! waylandsink sync=false
    ```

如需變更解析度，請參閱第 4.1.3.3 節。

#### 5.1.1.3 AI-G 上的 MIPI CSI 攝影機使用指南 (OV5647)
##### 5.1.1.3.1 在 Yocto 映像檔上使用 OV5647
在 AI-G 上有兩種應用程式可供使用：一種用於播放攝影機影像並顯示推論結果，另一種則僅供單純檢視攝影機畫面。您可依使用情境選擇任一應用程式。
- tcnnapp
    ```
    $ tcnnapp
    ```
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/accessories/Camera/5.13%20ov5647%20camera%20out%20display%20with%20running%20tcnnapp%20on%20yocto.png"></p>
    <p align="center"><strong>圖 5.13 Yocto 上執行 tcnnapp 的 OV5647 攝影機輸出顯示</strong></p>
- tcnncameraapp
    ```
    $ tcnncameraapp
    ```
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/accessories/Camera/5.14%20ov5647%20camera%20out%20display%20with%20running%20tcnncameraapp%20on%20yocto.png"></p>
    <p align="center"><strong>圖 5.14 Yocto 上執行 tcnncameraapp 的 OV5647 攝影機輸出顯示</strong></p>

##### 5.1.1.3.2 在 Ubuntu 映像檔上使用
在 AI-G 上有兩種應用程式可供使用：一種用於播放攝影機影像並顯示推論結果，另一種則僅供單純檢視攝影機畫面。您可依使用情境選擇任一應用程式。
- tcnnapp
    ```
    $ tcnnapp
    ```
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/accessories/Camera/5.13%20ov5647%20camera%20out%20display%20with%20running%20tcnnapp%20on%20yocto.png"></p>
    <p align="center"><strong>圖 5.15 Ubuntu 上執行 tcnnapp 的 OV5647 攝影機輸出顯示</strong></p>
- tcnncameraapp
    ```
    $ tcnncameraapp
    ```
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/accessories/Camera/5.14%20ov5647%20camera%20out%20display%20with%20running%20tcnncameraapp%20on%20yocto.png"></p>
    <p align="center"><strong>圖 5.16 Ubuntu 上執行 tcnncameraapp 的 OV5647 攝影機輸出顯示</strong></p>

#### 5.1.1.4 AI-G 上的 MIPI CSI 攝影機使用指南 (IMX219)
##### 5.1.1.4.1 在 Yocto 映像檔上使用 IMX219
在 AI-G 上有兩種應用程式可供使用：一種用於播放攝影機影像並顯示推論結果，另一種則僅供單純檢視攝影機畫面。您可依使用情境選擇任一應用程式。
- tcnnapp
    ```
    $ tcnnapp
    ```
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/accessories/Camera/5.17%20imx219%20camera%20out%20display%20with%20running%20tcnnapp%20on%20yocto.png"></p>
    <p align="center"><strong>圖 5.17 Yocto 上執行 tcnnapp 的 OV5647 攝影機輸出顯示</strong></p>
- tcnncameraapp
    ```
    $ tcnncameraapp
    ```
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/accessories/Camera/5.18%20imx219%20camera%20out%20display%20with%20running%20tcnncameraapp%20on%20yocto.png"></p>
    <p align="center"><strong>圖 5.18 Yocto 上執行 tcnncameraapp 的 OV5647 攝影機輸出顯示</strong></p>

##### 5.1.1.4.2 在 Ubuntu 映像檔上使用 IMX219
在 AI-G 上有兩種應用程式可供使用：一種用於播放攝影機影像並顯示推論結果，另一種則僅供單純檢視攝影機畫面。您可依使用情境選擇任一應用程式。
- tcnnapp
    ```
    $ tcnnapp
    ```
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/accessories/Camera/5.17%20imx219%20camera%20out%20display%20with%20running%20tcnnapp%20on%20yocto.png"></p>
    <p align="center"><strong>圖 5.17 Yocto 上執行 tcnnapp 的 OV5647 攝影機輸出顯示</strong></p>
- tcnncameraapp
    ```
    $ tcnncameraapp
    ```
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/accessories/Camera/5.18%20imx219%20camera%20out%20display%20with%20running%20tcnncameraapp%20on%20yocto.png"></p>
    <p align="center"><strong>圖 5.18 Yocto 上執行 tcnncameraapp 的 OV5647 攝影機輸出顯示</strong></p>

### 5.1.2 GMSL 攝影機使用指南
本節說明如何在 Yocto 與 Ubuntu 環境中顯示 GMSL 攝影機視訊。

#### 5.1.2.1 D3-G 上的 GMSL 攝影機使用指南
##### 5.1.2.1.1 在 Yocto 映像檔上使用 GMSL 攝影機
使用 [topst.ai DOCS 頁面](https://topst.ai/tech/docs?page=624bd237b3013e87c05c125b8031e2f370ccca2b) 提供的官方 Yocto 映像檔，或自行建置 Yocto 所產生的映像檔時，GMSL 攝影機會以 1920×1080 @ 30 fps 的預設解析度運作。因此，在此環境中的攝影機播放將使用 1920×1080 @ 30 fps。  
請依照以下步驟操作：
1. 停止目前執行中的 topst-welcome 服務
    ```
    $ sudo systemctl stop topst-welcome
    ```
2. 在 UART 主控台中輸入以下指令
    ```
    $ export XDG_RUNTIME_DIR=/run/user/root
    ```
3. 使用如下所示的 GStreamer 指令播放攝影機串流
    ```
    $ gst-launch-1.0 v4l2src device=/dev/video4 io-mode=2 ! video/x-raw,format=NV12,width=1920,height=1080,framerate=30/1 ! videoconvert ! waylandsink sync=false
    ```

此外，執行下方的指令碼，即可利用 gpu 以四分割畫面顯示各路攝影機影像。
```
#/bin/bash
 
set -euo pipefail
 
export GST_GL_WINDOW=wayland
export GST_GL_API=gles2
# glimagesink force-aspect-ratio=false sync=false \
 
gst-launch-1.0 -v \
  glvideomixer name=m background=black \
    sink_0::xpos=0   sink_0::ypos=0 \
    sink_1::xpos=960 sink_1::ypos=0 \
    sink_2::xpos=0   sink_2::ypos=540 \
    sink_3::xpos=960 sink_3::ypos=540 ! \
    "video/x-raw,format=RGBA,width=1920,height=1080,framerate=30/1" ! \
  waylandsink sync=false \
  v4l2src device=/dev/video4 io-mode=4 ! \
    video/x-raw,format=NV12,width=1920,height=1080,framerate=30/1 ! \
    glupload ! \
    glcolorscale ! "video/x-raw(memory:GLMemory),width=960,height=540" ! \
    m.sink_0 \
  \
  v4l2src device=/dev/video5 io-mode=4 ! \
    video/x-raw,format=NV12,width=1920,height=1080,framerate=30/1 ! \
    glupload ! \
    glcolorscale ! "video/x-raw(memory:GLMemory),width=960,height=540" ! \
    m.sink_1 \
  \
  v4l2src device=/dev/video6 io-mode=4 ! \
    video/x-raw,format=NV12,width=1920,height=1080,framerate=30/1 ! \
    glupload ! \
    glcolorscale ! "video/x-raw(memory:GLMemory),width=960,height=540" ! \
    m.sink_2 \
  \
  v4l2src device=/dev/video7 io-mode=4 ! \
    video/x-raw,format=NV12,width=1920,height=1080,framerate=30/1 ! \
    glupload ! \
    glcolorscale ! "video/x-raw(memory:GLMemory),width=960,height=540" ! \
    m.sink_3
```

GMSL 攝影機會顯示為 video4、video5、video6 與 video7，您可依需求選擇其中任一裝置。  
若連接八台攝影機，系統會將其列舉為 video0 至 video8，您可從這些裝置節點中任選其一。

##### 5.1.2.1.2 在 Ubuntu 映像檔上使用 GMSL 攝影機
使用 [topst.ai DOCS 頁面](https://topst.ai/tech/docs?page=624bd237b3013e87c05c125b8031e2f370ccca2b) 提供的官方 Ubuntu 映像檔時，GMSL 攝影機會以 1920×1080 @ 30 fps 的預設解析度運作。因此，在此環境中的攝影機播放將使用 1920×1080 @ 30 fps。  
請依照以下步驟操作：
1. - 若透過 UART 連接：請在以 topst 帳號登入後，於 UART 主控台中輸入以下指令
    ```
    $ export XDG_RUNTIME_DIR=/run/user/1000
    ```
    - 若直接在顯示器上操作：請開啟終端機視窗
2. 使用如下所示的 GStreamer 指令播放攝影機串流。由於 Ubuntu 上無法使用硬體加速的 Wayland 算繪，因此改以 H.265 編碼／解碼，利用 VPU 加速進行播放
    ```
    $ gst-launch-1.0 v4l2src device=/dev/video0 io-mode=2 ! video/x-raw,format=NV12,width=1920,height=1080,framerate=30/1 ! v4l2h265enc ! h265parse ! v4l2h265dec ! videoconvert ! waylandsink sync=false
    ```

此外，執行下方的指令碼，即可利用 gpu 以四分割畫面顯示各路攝影機影像。
```
#/bin/bash

set -euo pipefail

export GST_GL_WINDOW=wayland
export GST_GL_API=gles2

gst-launch-1.0 -v \
  glvideomixer name=m background=black \
    sink_0::xpos=0   sink_0::ypos=0 \
    sink_1::xpos=960 sink_1::ypos=0 \
    sink_2::xpos=0   sink_2::ypos=540 \
    sink_3::xpos=960 sink_3::ypos=540 ! \
    glcolorconvert ! "video/x-raw(memory:GLMemory),format=RGBA,width=1920,height=1080,framerate=30/1,pixel-aspect-ratio=1/1" ! \
  glimagesink force-aspect-ratio=false sync=false \
  \
  v4l2src device=/dev/video4 io-mode=4 ! video/x-raw,format=NV12,framerate=30/1,pixel-aspect-ratio=1/1 ! \
    videoconvert ! glupload ! glcolorscale ! \
    "video/x-raw(memory:GLMemory),format=RGBA,width=960,height=540,pixel-aspect-ratio=1/1" ! m.sink_0 \
  \
  v4l2src device=/dev/video5 io-mode=4 ! video/x-raw,format=NV12,framerate=30/1,pixel-aspect-ratio=1/1 ! \
    videoconvert ! glupload ! glcolorscale ! \
    "video/x-raw(memory:GLMemory),format=RGBA,width=960,height=540,pixel-aspect-ratio=1/1" ! m.sink_1 \
  \
  v4l2src device=/dev/video6 io-mode=4 ! video/x-raw,format=NV12,framerate=30/1,pixel-aspect-ratio=1/1 ! \
    videoconvert ! glupload ! glcolorscale ! \
    "video/x-raw(memory:GLMemory),format=RGBA,width=960,height=540,pixel-aspect-ratio=1/1" ! m.sink_2 \
  \
  v4l2src device=/dev/video7 io-mode=4 ! video/x-raw,format=NV12,framerate=30/1,pixel-aspect-ratio=1/1 ! \
    videoconvert ! glupload ! glcolorscale ! \
    "video/x-raw(memory:GLMemory),format=RGBA,width=960,height=540,pixel-aspect-ratio=1/1" ! m.sink_3
```

此外，您也可以使用 OpenCV 顯示攝影機串流。請依照以下步驟，輕鬆使用 OpenCV 預覽攝影機視訊。
1. 安裝 OpenCV
    ```
    $ sudo apt-get install python3-opencv
    ```
2. 在 opencv_cam.py 檔案中寫入以下程式碼
    ```
    import cv2
    
    pipeline = (
        "v4l2src device=/dev/video4 io-mode=2 ! "
        "video/x-raw,format=NV12,width=1920,height=1080,framerate=30/1 ! "
        "videoconvert ! video/x-raw,format=BGR ! appsink sync=false"
    )
    
    cap = cv2.VideoCapture(pipeline, cv2.CAP_GSTREAMER)
    
    if not cap.isOpened():
        print("ERROR: cannot open camera via GStreamer")
        exit()
    
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Frame read error")
            break
    
        cv2.imshow("Camera", frame)
        if cv2.waitKey(1) == 27:
            break
    
    cap.release()
    cv2.destroyAllWindows()
    ```
3. 使用 Python 執行 opencv_cam.py 檔案
    ```
    $ python3 opencv_cam.py
    ```

GMSL 攝影機會顯示為 video4、video5、video6 與 video7，您可依需求選擇其中任一裝置。  
若連接八台攝影機，系統會將其列舉為 video0 至 video8，您可從這些裝置節點中任選其一。

#### 5.1.2.2 AI-G 上的 GMSL 攝影機使用指南
##### 5.1.2.2.1 在 Yocto 映像檔上使用 GMSL 攝影機
在 AI-G 上有兩種應用程式可供使用：一種用於播放攝影機影像並顯示推論結果，另一種則僅供單純檢視攝影機畫面。您可依使用情境選擇任一應用程式。
- tcnnapp
- tcnncameraapp

GMSL 攝影機會顯示為 **video0**、**video1** 與 **video2**，您可依需求選擇其中任一裝置。
每個應用程式預設使用 video2，但您可以透過 **-p 選項** 變更視訊裝置。
以下範例示範如何選擇 **video0**。

- tcnnapp
    ```
    $ tcnnapp -p /dev/video0
    ```
- tcnncameraapp
    ```
    $ tcnncameraapp -p /dev/video0
    ```

##### 5.1.2.2.2 在 Ubuntu 映像檔上使用 GMSL 攝影機
在 AI-G 上有兩種應用程式可供使用：一種用於播放攝影機影像並顯示推論結果，另一種則僅供單純檢視攝影機畫面。您可依使用情境選擇任一應用程式。
- tcnnapp
- tcnncameraapp

GMSL 攝影機會顯示為 **video0**、**video1** 與 **video2**，您可依需求選擇其中任一裝置。
每個應用程式預設使用 video2，但您可以透過 **-p 選項** 變更視訊裝置。
以下範例示範如何選擇 **video0**。

- tcnnapp
    ```
    $ tcnnapp -p /dev/video0
    ```
- tcnncameraapp
    ```
    $ tcnncameraapp -p /dev/video0
    ```

### 5.1.3 USB 攝影機使用指南
本節說明如何在 Yocto 與 Ubuntu 環境中顯示 USB 攝影機視訊。
AI-G 未內建 USB 介面，因此本平台不提供 USB 攝影機指南。

#### 5.1.3.1 D3-G 上的 USB 攝影機使用指南
本文件的說明以支援 1920×1080 @ 30 fps 的 USB 攝影機為基礎

**註：** 由於 MIPI 攝影機預設指派為 **/dev/video0**，因此 USB 攝影機會建立為 /dev/video1。
操作 USB 攝影機時，請務必使用 **/dev/video1**。

##### 5.1.3.1.1 在 Yocto 映像檔上使用 USB 攝影機
使用 [topst.ai DOCS 頁面](https://topst.ai/tech/docs?page=624bd237b3013e87c05c125b8031e2f370ccca2b) 提供的官方 Yocto 映像檔，或自行建置 Yocto 所產生的映像檔時，USB 攝影機會依照攝影機本身規格所定義的解析度與影格率運作。因此，視訊將以 USB 攝影機提供的預設解析度與 FPS 播放。  
請依照以下步驟操作：
1. 停止目前執行中的 topst-welcome 服務
    ```
    $ sudo systemctl stop topst-welcome
    ```
2. 在 UART 主控台中輸入以下指令
    ```
    $ export XDG_RUNTIME_DIR=/run/user/root
    ```
3. 使用如下所示的 GStreamer 指令播放攝影機串流。以 v4l2-ctl -d /dev/video1 --list-formats-ext 檢查 USB 攝影機資訊時，顯示支援的格式為 MJPEG，因此使用 jpegdec
    ```
    $ gst-launch-1.0 v4l2src device=/dev/video1 ! image/jpeg,width=1920,height=1080 ! jpegdec ! videoconvert ! waylandsink
    ```

##### 5.1.3.1.2 在 Ubuntu 映像檔上使用 USB 攝影機
使用 [topst.ai DOCS 頁面](https://topst.ai/tech/docs?page=624bd237b3013e87c05c125b8031e2f370ccca2b) 提供的官方 Ubuntu 映像檔，或自行產生的映像檔時，USB 攝影機會依照攝影機本身規格所定義的解析度與影格率運作。因此，視訊將以 USB 攝影機提供的預設解析度與 FPS 播放。  
請依照以下步驟操作：
1. - 若透過 UART 連接：請在以 topst 帳號登入後，於 UART 主控台中輸入以下指令
    ```
    $ export XDG_RUNTIME_DIR=/run/user/1000
    ```
    - 若直接在顯示器上操作：請開啟終端機視窗
2. 使用如下所示的 GStreamer 指令播放攝影機串流。以 v4l2-ctl -d /dev/video1 --list-formats-ext 檢查 USB 攝影機資訊時，顯示支援的格式為 MJPEG，因此使用 jpegdec
    ```
    $ gst-launch-1.0 v4l2src device=/dev/video1 ! image/jpeg,width=1920,height=1080 ! jpegdec ! videoconvert ! waylandsink
    ```
3. 若要使用 H.265 編碼與解碼，必須將視訊轉換為 v4l2src 支援的 NV12 格式。因此，管線應如下所示進行設定
    ```
    $ gst-launch-1.0 v4l2src device=/dev/video1 io-mode=2 ! image/jpeg,width=640,height=480,framerate=30/1 ! jpegdec ! videoconvert ! video/x-raw,format=NV12 !  v4l2h265enc ! h265parse ! v4l2h265dec ! videoconvert ! waylandsink
    ```

**註：** 您可以在指令結尾加上 fullscreen=true 選項，以全螢幕播放視訊。

除了 GStreamer 之外，您也可以使用 OpenCV 顯示攝影機串流。請依照以下步驟，輕鬆使用 OpenCV 預覽攝影機視訊。
1. 安裝 OpenCV
    ```
    $ sudo apt-get install python3-opencv
    ```
2. 在 opencv_cam.py 檔案中寫入以下程式碼
    ```
    import cv2

    cap = cv2.VideoCapture(1)

    if not cap.isOpened():
        print("\\@@ Camera open failed!")
        exit()

    print("Press 'q' to exit the camera window.")

    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Failed to read frame")
            break

        cv2.imshow("Camera Feed", frame)

        # pressed 'q' key, escape
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
    ```
3. 使用 Python 執行 opencv_cam.py
    ```
    $ python3 opencv_cam.py
    ```

The USB camera used in this guide operates over USB 2.0, which imposes bandwidth limitations. As a result, higher-resolution video capture is not supported when using OpenCV. If higher resolutions are required, it is recommended to use a USB 3.0 camera, which provides sufficient bandwidth for high-definition video streams.  
Alternatively, OpenCV can be used with higher resolutions by constructing the capture pipeline through GStreamer, as shown below.
1. Write the following code inside the gstreamer_opencv_cam.py file
    ```
    import cv2

    pipeline = (
        "v4l2src device=/dev/video1 ! "
        "image/jpeg,width=1920,height=1080,framerate=30/1 ! "
        "jpegdec ! videoconvert ! video/x-raw,format=BGR ! "
        "appsink drop=1 max-buffers=2"
    )

    print("Opening pipeline...")
    cap = cv2.VideoCapture(pipeline, cv2.CAP_GSTREAMER)

    if not cap.isOpened():
        print("Failed to open pipeline")
        exit()

    print("Press 'q' to exit the camera window.")

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Failed to read frame")
            break

        cv2.imshow("USB Camera 1080p MJPG", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
    ```
2. Run gstreamer_opencv_cam.py with Python
    ```
    $ python3 gstreamer_opencv_cam.py
    ```

# 6. 疑難排解
第 6 章說明 MIPI CSI 攝影機、GMSL 攝影機與 USB 攝影機的疑難排解。

## 6.1 MIPI CSI 與 GMSL 攝影機疑難排解
若您在使用 MIPI CSI 或 GMSL 攝影機時遇到問題，請參閱以下除錯指南排解問題。

### 6.1.1 開機階段的問題（Probe 階段）
#### 6.1.1.1 感測器 Probe 失敗
**症狀**
- 開機期間未偵測到感測器
- 未建立 /dev/videoX 節點
- 感測器 entity 未出現在 ‘media-ctrl -p’ 的輸出中  

**dmesg 記錄範例**
```
[    3.421000] imx219 2-0010: probing sensor failed
[    3.421120] imx219 2-0010: i2c read failed: addr=0x3000, ret=-5
[    3.200400] imx219 0-0010: reset gpio request failed
[    2.912830] imx219 1-0010: failed to get vddio regulator
```
**可能原因**
- I2C 位址或匯流排設定不正確
- RESET/PWDN GPIO 的極性不正確
- 缺少 regulator 電源供應，或其設定不正確

**解決方式**
- 請確認 device tree 中的 I2C 位址、匯流排編號與 GPIO 設定
- 檢查是否有缺少或定義錯誤的 regulator 節點
- 重新檢查感測器模組排線的方向與腳位對位

#### 6.1.1.2 I2C 通訊失敗
**dmesg 記錄範例**
```
[    3.101001] imx219 2-0010: i2c read error: -121
[    4.112121] i2c i2c-2: transfer failed: -110
```
**可能原因**
- SDA/SCL 線路短路或斷線
- device tree 中的 I2C 匯流排編號與實際硬體設定不符

**解決方式**
- 請使用 “i2cdetect -y <bus>” 檢查感測器是否在預期的 I2C 位址上回應
- 檢查排線與接頭是否損壞、未確實插入或接觸不良

### 6.1.2 Media Controller 與 Graph 設定問題
（使用 ‘media-ctl -p’ 進行確認）

#### 6.1.2.1 缺少感測器 entity 或連結未設定
**'media-ctl -p' 輸出範例**
```
0 entities, 0 interfaces, 0 pads, 0 links
```
**可能原因**
- device tree 中缺少 endpoint (port) 節點
- lane 數量或 ‘bus-type’ 設定不正確
- 缺少 ‘link-frequencies’ 項目

**解決方式**
- 請確認 ‘port@0/1’ endpoint 定義是否正確
- 檢查 ‘data-lanes’ 陣列的順序與 lane 數量是否正確
- 確認 ‘link-frequencies’ 與感測器規格相符

#### 6.1.2.2 格式 / 模式不相符
**可能原因**
- 感測器驅動程式中的 ‘supported_mode[]’ 與 DTS 中定義的 ‘hs-settle’ 值不相符
- 驅動程式與 device tree 之間的 CSI-2 lane 數量不一致

**解決方式**
- 請檢視 ‘supported_modes[]’ 中的解析度、pixel rate 與 HTS/VTS 值，再據此調整 DTS 中的 ‘hs-settle’ 值
- 確保 DTS 設定與感測器驅動程式的設定一致

### 6.1.3 V4L2 串流問題
#### 6.1.3.1 VIDIOC_STREAMON 失敗（無法開始串流）
**可能原因**
- 感測器暫存器設定不正確
- pixel rate 或 PLL 設定與預期值不符
- HTS/VTS 衝突導致影格時序無效

**解決方式**
- 重新驗證感測器模式表中的 pixel rate、VTS 與 HTS 值
- 檢查 PLL 除頻值（0x030x 暫存器）是否正確
- 確認 device tree 針對所選的解析度與 FPS 指定了正確的 ‘hs-settle’ 值。

#### 6.1.3.2 要求不支援的格式
**解決方式**
- 請使用下方指令檢查實際支援的格式，然後以支援的格式重新嘗試串流：
    ```
    V4l2-ctl –list-formats-ext
    ```

### 6.1.4 CSI-2 錯誤：SoT、CRC 與相關問題
#### 6.1.4.1 SoT (Sync on Transmission) 錯誤
**可能原因**
- MIPI 時序設定不相符
- pixel rate 設定過高
- 排線品質不佳或線長過長

**解決方式**
- 降低 pixel rate 或 link frequency
- 更換排線或縮短其長度
- 確認 MIPI 時序參數

#### 6.1.4.2 CRC 錯誤
**dmesg 記錄範例**
```
[   13.700910] tccvin videoinput0: CSI-2 ERROR: CRC error
```
**可能原因**
- MIPI 訊號品質劣化
- PLL 或 lane 速度不相符

**解決方式**
- 調整 hs-settle 值
- 更換排線
- 確認 PLL 設定與 lane 速度設定

### 6.1.5 Pixelrate / Link-Frequency 錯誤
**可能原因**
- 超出可用的 CSI-2 lane 頻寬
- PLL 設定不正確

**解決方式**
- 重新計算 pixel rate，並確保其落在允許的 CSI-2 頻寬範圍內
- 調整 PLL 除頻值以取得有效的時序
- 必要時，請降低影格率（例如 30 -> 15fps）或降低解析度

### 6.1.6 Device Tree (DTS) 設定錯誤
#### 6.1.6.1 不相容的 compatible 字串
**可能原因**
- DTS 中的 ‘compatible’ 值與感測器驅動程式中定義的 ‘of_device_id’ 不相符
- 驅動程式無法辨識該裝置節點，導致 probe 無法執行

**解決方式**
- 請以感測器驅動程式中定義的確切 ‘compatible’ 字串更新 DTS（例如 “sony,imx219”）
- 重新建置 device tree，並確認感測器能正確完成 probe

#### 6.1.6.2 Endpoint 設定問題
**可能原因**
- 感測器 endpoint 與 CSI endpoint 之間的 port 編號或 ‘remote-endpoint’ 參照不相符
- ‘data-lanes’ 或匯流排設定不符合 media graph 的需求

**解決方式**
- 請確認兩端的 port 編號、‘data-lanes’ 與 ‘remote-endpoint’ 值一致
- 請使用 ‘media-ctl -p’ 確認 media 連結已正確建立

#### 缺少 Link-Frequencies 屬性
**可能原因**
- endpoint 中缺少 ‘link-frequencies’ 欄位，導致無法計算 MIPI 連結速度
- 該值的格式（例如 /bits/ 64）與驅動程式預期的格式不符

**解決方式**
- 請依感測器規格加入正確的 ‘link-frequencies’ 值（例如 456000000）
- 確認值的格式符合驅動程式需求（例如必要時須包含 /bits/ 64）

### 6.1.7 Gstreamer 播放問題
#### 6.1.7.1 'not negotiated' 錯誤
**可能原因**
- 管線內的 caps 協商失敗
- Wayland compositor 格式不相符
- Videoconvert 無法處理某些 raw 格式

**解決方式**
- 請使用以 NV12 或 YUY2 為基礎的管線，這些格式具有廣泛的相容性
- 使用 ‘v4l2src io-mode=dmabuf’ 以確保零複製的緩衝區處理與正確的格式協商

#### 6.1.7.2 Wayland Sink 初始化失敗
**可能原因**
- Wayland compositor 未執行，或沒有可存取的顯示環境
- 管線是透過 SSH 啟動，或 DISPLAY/Wayland 環境無效，導致 sink 無法初始化

**解決方式**
- 請確認 Weston compositor 正在執行
- 請在本機工作階段或已正確設定的 Wayland 環境中執行管線

### 6.1.8 硬體問題
#### 6.1.8.1 排線方向錯誤
**可能原因**
- FFC 排線的連接方向錯誤或腳位未對齊，導致 I2C/MIPI 訊號無法正常傳輸
- 感測器完全沒有回應，因此未接收到任何影格

**解決方式**
- 請確認接頭方向，並確保接觸腳位依規格對齊
- 請檢查排線是否損壞或接點是否磨損

#### 6.1.8.2 電源供應問題
**可能原因**
- 感測器電源軌（例如 1.2V / 2.8V）不穩定或未啟用
- 電源啟用 GPIO 未被設定為有效狀態
- 初始化期間未滿足感測器的上電時序需求

**解決方式**
- 請檢視 DTS 中的穩壓器與 GPIO 設定，並確認所有必要電壓皆正確供應
- 請確保滿足感測器的電源時序需求（RESET _> PWDN -> clock enable）

## 6.2 USB 攝影機疑難排解
若您在使用 USB 攝影機時遇到問題，請參閱下方的除錯指南來排除問題。

### 6.2.1 未偵測到攝影機（無法辨識 USB 裝置）
**dmesg 記錄範例**
```
usb 1-1: device descriptor read/64, error -71
uvcvideo: Failed to initialize the device
```
**可能原因**
- USB 供電不足或供電不穩定，導致裝置初始化失敗
- USB 傳輸線或連接埠故障，或使用了不相容的 USB 集線器

**解決方式**
- 請嘗試改用其他 USB 連接埠，或使用供電穩定的連接埠
- 請更換 USB 傳輸線或集線器並重新連接裝置，以確保能正確列舉

### 6.2.2 v4l2-ctl 中的格式清單受限或為空
**dmesg 記錄範例**
```
uvcvideo: Failed to query (GET_DEF) UVC control 2 on unit 1: -32
```
**可能原因**
- 攝影機不支援某些 UVC 控制項，或在初始化期間未能回報這些項目
- 裝置與驅動程式之間的通訊協定錯誤，導致無法偵測功能

**解決方式**
- 請使用 MJPEG 或 YUYV 等標準格式進行測試
- 請使用另一台相同型號的攝影機進行測試，以判斷問題是否與 UVC 相容性有關

### 6.2.3 GStreamer 播放："not negotiated" 或 Caps 不相符
**可能原因**
- pipeline 要求攝影機不支援的格式（例如 NV12、YUY2），導致 caps 協商失敗
- 在所選的解析度／影格率下，攝影機可能僅提供 MJPEG，但 pipeline 卻要求 raw 格式
- 攝影機輸出 MJPEG，但未加入 JPEG 解碼元件（jpegdec 或 avdec_mjpeg），因此無法進行解碼

**解決方式**
- 請檢查支援的格式
    ```
    v4l2-ctl –list-formats-ext
    ```
- 若攝影機輸出 MJPEG：
    ```
    v4l2src ! image/jpeg ! jpegdec ! videoconvert ! …
    ```
- 若攝影機支援 raw 格式（例如 YUYV），請據此設定 pipeline 的 caps：  
    請完全依照 ‘v4l2-ctl –list-formats-ext’ 中所列出的 raw 格式使用

### 6.2.4 解析度或 FPS 設定失敗
**可能原因**
- 攝影機不支援所要求的解析度或影格率，導致協商失敗

**解決方式**
- 請使用 ‘v4l2-ctl –list-formats-ext’ 檢查支援的解析度／FPS 組合

### 6.2.5 視訊卡頓／掉格
**可能原因**
- USB 頻寬不足（共用集線器或使用 USB 2.0 連接埠）
- MJPEG 解碼造成 CPU 負載過高，導致 pipeline 處理落後

**解決方式**
- 請使用 USB 3.0 連接埠，或不透過集線器直接連接攝影機
- 請降低 MJPEG 的解析度或影格率，或在支援的情況下改用 raw 格式

### 6.2.6 色彩不正確或輸出畫面損毀
**可能原因**
- MJPEG -> NV12 轉換或色彩空間轉換期間發生錯誤
- 某些格式組合可能在 v4l2convert 或 videoconvert 中失敗

**解決方式**
- 請在 videoconvert 之前明確插入 jpegdec 或 avdec_mjpeg
- 請簡化 pipeline 進行測試，例如：
    ```
    V4l2src ! jpegdec ! videoconvert ! waylandsink
    ```

### 6.2.7 裝置意外斷線或重新列舉
**dmesg 記錄範例**
```
usb 1-1: USB disconnect, device number 4
```
**可能原因**
- 供電不穩定或排線接觸不良
- 長時間使用時因散熱問題導致裝置重設

**解決方式**
- 請更換 USB 傳輸線，或使用供電穩定且充足的連接埠
- 對於發熱明顯的攝影機，請考慮採用額外的散熱方案
