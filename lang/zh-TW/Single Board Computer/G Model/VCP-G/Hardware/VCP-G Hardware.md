# 1. 簡介
---
本文件是以 TCC7045 應用處理器為基礎的 VCP-G 硬體使用者指南。本文件說明系統安裝、除錯，以及 VCP-G 整體設計與使用的詳細資訊。


表 1.1 說明 VCP-G 的功能特性。

<p align="center"><strong>表 1.1 VCP-G 的功能特性</strong></p>
<div align="center">
	<table>
	  <tr>
	    <td colspan="3">零件名稱</td>
	    <td>TCC7045</td>
	  </tr>
	  <tr>
	    <td colspan="3">封裝</td>
	    <td>封裝	腳位對腳位相容 FBGA 196-pin (12BD)</td>
	  </tr>
	    <tr>
	    <td colspan="3">CPU 頻率</td>
	    <td>200 MHz（最高 300 MHz）</td>
	  </tr>
	  <tr>
	    <td rowspan="4">晶片內建記憶體</td>
	    <td colspan="2">Program Flash</td>
	    <td colspan="3">4 MB</td>
	  </tr>
	  <tr>
	    <td colspan="2">SRAM</td>
	    <td colspan="3">512 KB（包含 Retention RAM 16 KB）</td>
	  </tr>
	  <tr>
	    <td colspan="2">DataFlash</td>
	    <td colspan="3">256 KB</td>
	  </tr>
	  <tr>
	    <td colspan="2">DMA 通道</td>
	    <td colspan="3">16 通道</td>
	  </tr>
	  <tr>
	    <td rowspan="13">周邊裝置</td>
	    <td colspan="2">乙太網路</td>
	    <td>1 Gbps，支援 AVB</td>
	  </tr>
	  <tr>
		<td colspan="2">CAN / CANFD</td>
	    <td>3 通道</td>
	  </tr>
	  <tr>
	    <td colspan="2">專用 LIN / UART</td>
	    <td>3 通道（最多 6 通道）</td>
	  </tr>
	  <tr>
	    <td colspan="2">專用 I2C</td>
	    <td>3 通道（最多 6 通道）</td>
	  </tr>
	  <tr>
	  <tr>
	    <td colspan="2">專用 GPSB (SPI)</td>
	    <td>2 通道（最多 5 通道）</td>
	  </tr>
	    <tr>
	    <td colspan="2">MFIO（配置 UART、I2C、GPSB）</td>
	    <td>3 通道</td>
	  </tr>
	  <tr>
	    <td rowspan="4">ADC</td> 
	    <td>解析度</td>
	    <td>12-bit SAR 類型</td>
	  </tr>
	  <tr>
	    <td>通道數</td>
	    <td>12 通道 x 2 組</td>
	  </tr>
	  <tr>
	    <td>輸入範圍</td>
	    <td>3.3V</td>
	  </tr>
	  <tr>
	    <td>取樣率</td>
	    <td>超過 1.0 MSPs</td>
	  </tr>
	  <tr>
	    <td colspan="2">I2S</td>
	    <td>1 通道</td>
	  </tr>
	  <tr>
	    <td colspan="2">序列 Flash 介面</td>
	    <td>Quad SPI</td>
	  </tr>  
	  <tr>
	    <td colspan="3">電源系統</td>
	    <td>3.3V 單一電源</td>
	  </tr>
	  <tr>
	    <td colspan="3">溫度</td>
	    <td>-40 ℃ to 105 ℃</td>
	  </tr>
	</table>
</div>

</br></br></br>

## 1.1 術語
---
<p align="center"><strong>表 1.2 術語 </strong></p>
<div align="center">
	<table>
	  <tr>
	    <td clospan="2"><strong>術語</strong></td>
	    <td><strong>定義</strong></td>
	  </tr>
	  <tr>
	    <td clospan="2">ADC</td>
	    <td>類比數位轉換器</td>
	  </tr>
	  <tr>
	    <td clospan="2">FWDN</td>
	    <td>韌體下載</td>
	  </tr>
	  <tr>
	    <td clospan="2">GPIO</td>
	    <td>通用輸入輸出</td>
	  </tr>
	  <tr>
	    <td clospan="2">MCU</td>
	    <td>微控制器</td>
	  </tr>
	  <tr>
	    <td clospan="2">TOPST</td>
	    <td>Total Open-Platform for System development and Training</td>
	  </tr>
	  <tr>
	    <td clospan="2">VCP</td>
	    <td>車輛控制處理器</td>
	  </tr>
	</table>
</div>

</br></br></br></br>

# 2. 方塊圖
---
## 2.1 系統方塊圖
---
圖 2.1 顯示 VCP-G 的系統方塊圖。
<p align="center"><img src= "https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Hardware/2.1%20VCP-G%20System%20Block%20Diagram.png"></p>
<p align="center"><strong>圖 2.1 系統方塊圖</strong></p>

</br></br></br></br>

# 3. VCP-G 概觀
---
VCP-G 可用於下列用途：
  - 系統開發
  - 教育訓練

表 3.1 說明 VCP-G 的預設設定。

<p align="center"><strong>表 3.1 VCP-G 的預設設定 </strong></p>
<div align="center">
	<table>
	  <tr>
	    <td colspan="2"><strong>開發板名稱</strong></td>
	    <td><strong>說明</strong></p>
	  </tr>
	  <tr>
	    <td colspan="2">TOPST_VCP_V2.1.1</td>
	    <td>TOPST 專用 MCU 開發板</td>
	  </tr>
	</table>
</div>

</br></br></br>

## 3.1 VCP-G
---
圖 3.1 顯示 VCP-G 的上視圖。
<p align="center"><img src= "https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Hardware/3.1%20TOPST%20VCP-G%20Board%20(Top%20View)%20.png"></p>
<p align="center"><strong>圖 3.1 VCP-G（上視圖）</strong></p>

表 3.2 說明 VCP-G 的接頭（上視圖）。
<p align="center"><strong>表 3.2 VCP-G 的接頭（上視圖）</strong></p>
<div align="center">
	<table>
	  <tr>
	    <td colspan="4"><strong>編號</strong></td>
	    <td><strong>參考編號</strong></td>
	    <td><strong>名稱</strong></td>
	    <td><strong>說明</strong></td>
	  </tr>
	  <tr>
	    <td colspan="4">1</td>
	    <td>J18D100</td>
	    <td>36 針母排針</td>
	    <td>GPIO 與 ADC 用排針</td>
	  </tr>
	  <tr>
	    <td colspan="4">2</td>
	    <td>J5D100</td>
	    <td>10 針公排針</td>
	    <td>CAN 用排針</td>
	  </tr>
	  <tr>
	    <td colspan="4">3</td>
	    <td>J3D100</td>
	    <td>6 針公排針</td>
	    <td>SPI 用排針</td>
	  </tr>
	  <tr>
	    <td colspan="4">4</td>
	    <td>J8D104</td>
	    <td>8 針母排針</td>
	    <td>GPIO 與 ADC 用排針</td>
	  </tr>
	  <tr>
	    <td colspan="4">5</td>
	    <td>J8D102</td>
	    <td>8 針母排針</td>
	    <td>GPIO 用排針</td>
	  </tr>
	  <tr>
	    <td colspan="4">6</td>
	    <td>J10D100</td>
	    <td>10 針母排針</td>
	    <td>GPIO 與 ADC 用排針</td>
	  </tr>
	  <tr>
	    <td colspan="4">7</td>
	    <td>J100</td>
	    <td>10 針公排針</td>
	    <td>JTAG 用排針</td>
	  </tr>
	  <tr>
	    <td colspan="4">8</td>
	    <td>SW100</td>
	    <td>RESET 輕觸開關</td>
	    <td>GRESETn：初始化 VCP-G 的系統與電源管理</td>
	  </tr>
	  <tr>
	    <td colspan="4">9</td>
	    <td>JC100</td>
	    <td>USB Type-C 接頭</td>
	    <td>除錯用 UART 或 FWDN 連接埠</td>
	  </tr>
	  <tr>
	    <td colspan="4">10</td>
	    <td>SW101</td>
	    <td>輕觸開關</td>
	    <td>FWDN：進入 VCP-G 的韌體下載模式</td>
	  </tr>  
	  <tr>
	    <td colspan="4">11</td>
		<td>J101</td>
	    <td>DC 電源插孔</td>
	    <td>DC 電源輸入插孔</td>
	  </tr>  
	  <tr>
	    <td colspan="4">12</td>
	    <td>J8D100</td>
	    <td>8 針母排針</td>
	    <td>電源與重置用排針</td>
	  </tr>  
	  <tr>
	    <td colspan="4">13</td>
	    <td>J8D101</td>
	    <td>8 針母排針</td>
	    <td>GPIO 與 ADC 用排針</td>
	  </tr>  
	  <tr>
	    <td colspan="4">14</td>
	    <td>J8D103</td>
	    <td>8 針母排針</td>
	    <td>GPIO 與 ADC 用排針</td>
	  </tr>    
	</table>
</div>

圖 3.2 顯示 VCP-G 的下視圖。  

**註：** 圖 3.2 目前顯示的是 TOPST_VCP-G_V1.1.1 開發板。此圖片將更新為 TOPST_VCP-G_V2.1.1 開發板。
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Hardware/3.2%20TOPST%20VCP-G%20Board%20(Bottom%20View).png"></p>
<p align="center"><strong>圖 3.2 VCP-G（下視圖）</strong></p>

</br></br></br></br>

# 4. 規格
---
## 4.1 Quad SPI 快閃記憶體 (U101)
---
Quad SPI 快閃記憶體的資訊如下：
  - 容量：64 Mb  
  
**註：** VCP-G 預設未安裝 SNOR。

</br></br></br>

## 4.2 電源輸入接頭 (J101)
---
DC 12V 由 12V 變壓器透過 J101 的 DC 插孔供電給 VCP-G。  
圖 4.1 顯示 J101 的位置。
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Hardware/4.1%20Power%20In%20Connector%20(J101).png"></p>
<p align="center"><strong>圖 4.1 電源輸入接頭 (J101)</strong><p>

</br></br></br>

## 4.3 JTAG 接頭 (J100)
---
JTAG 模擬器可透過 J100 連接至 VCP-G 以進行除錯。圖 4.2 顯示 J100 的位置。
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Hardware/4.2%20Connector%20for%20JTAG%20(J100).png"></p>
<p align="center"><strong>圖 4.2 JTAG 接頭 (J100)</strong><p>
JTAG 預設為停用。若要啟用 JTAG，必須變更 R178 與 R179 的連接方式。若 TRSRn 由 R178 設為高電位，MCU 即進入 JTAG 模式。

表 4.1 說明 J100 的腳位。
<p align="center"><strong>表 4.1 J100 腳位說明</strong></p>
<div align="center">
	<table>
	  <tr>
	    <th rowspan="2"><strong>腳位編號</strong></th>
	    <th rowspan="2"><strong>電路圖網路名稱</strong></th>
	    <th><strong>DIR</strong></th>
	    <th rowspan="2"><strong>說明</strong></th>
	  </tr>
	  <tr>
	    <th><strong>MCU ◄► J100</strong></th>
	  </tr>
	  <tr>
	    <td>1</td>
	    <td>SW_VDD_3P3</td>
	    <td>-</td>
	    <td>電源 3.3V</td>
	  </tr>
	  <tr>
	    <td>2</td>
	    <td>TMS</td>
	    <td>◄</td>
	    <td>測試模式狀態</td>
	  </tr>
	  <tr>
	    <td>3</td>
	    <td>DGND</td>
	    <td>-</td>
	    <td>接地</td>
	  </tr>
	  <tr>
	    <td>4</td>
	    <td>TCK</td>
	    <td>◄</td>
	    <td>測試時脈</td>
	  </tr>
	  <tr>
	    <td>5</td>
		<td>DGND</td>
	    <td>-</td>
	    <td>接地</td>
	  </tr>
	  <tr>
	    <td>6</td>
	    <td>TDO</td>
	    <td>►</td>
	    <td>測試資料輸出</td>
	  </tr>
	  <tr>
	    <td>7</td>
	    <td>NC</td>
	    <td>-</td>
	    <td>未連接</td>
	  </tr>
	  <tr>
	    <td>8</td>
	    <td>TDI</td>
	    <td>◄</td>
	    <td>測試資料輸入</td>
	  </tr>
	  <tr>
	    <td>9</td>
	    <td>DGND</td>
	    <td>-</td>
	    <td>接地</td>
	  </tr>
	  <tr>
	    <td>10</td>
	    <td>JTAG_RESETn</td>
	    <td>◄</td>
	    <td>系統重置</td>
	  </tr>   
	</table>
</div>

表 4.2 說明 JTAG 停用/啟用的設定。
<p align="center"><strong>表 4.2 JTAG 停用/啟用的設定</strong></p>
<div align="center">
	<table>
	  <tr>
	    <th colspan="4"><strong>模式</strong></th>
	    <th><strong>TRSTn 值</strong></th>
	    <th><strong>R178</strong></th>
	    <th><strong>R179</strong></th>
	  </tr>
	  <tr>
	    <td colspan="4">JTAG 停用（預設）</td>
	    <td>低電位 (1)</td>
	    <td>N.C</td>
	    <td>1K</td>
	  </tr>
	  <tr>
	    <td colspan="4">JTAG 啟用（選用）</td>
	    <td>高電位 (1)</td>
	    <td>1K</td>
	    <td>N.C</td>
	  </tr>
	</table>
</div>

</br></br></br>

## 4.4 FWDN 開關 (SW101)
---
VCP-G 具有一個使用開機模式 (BM) 進行開機設定的腳位，並支援 2 種模式：UART FWDN 模式與一般模式。   
圖 4.3 顯示 FWDN 輕觸開關 (SW101) 的位置，該開關用於選擇 VCP-G 的開機模式。
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Hardware/4.3%20FWDN%20Tact%20Switch%20(SW101).png"></p>
<p align="center"><strong>圖 4.3 FWDN 輕觸開關 (SW101)</strong><p>

表 4.3 說明如何使用 FWDN 輕觸開關 (SW101) 選擇開機模式。
<p align="center"><strong>表 4.3 開機模式用輕觸開關 (SW101) 說明</strong></p>
<div align="center">
	<table>
	  <tr>
	    <th colspan="3"><strong>模式</strong></th>
	    <th><strong>BM00 值</strong></th>
	    <th><strong>SW101 狀態</strong></th>
	  </tr>
	  <tr>
	    <td colspan="3">一般（預設）</td>
	    <td>低電位 (1)</td>
	    <td>預設</td>
	  </tr>
	  <tr>
	    <td colspan="3">FWDN（選用）</td>
	    <td>高電位 (1)</td>
	    <td>按住並上電</td>
	  </tr>
	</table>
</div>
</br></br>

### 4.4.1 FWDN 模式進入方式
進入 FWDN 模式有以下兩種方式。

#### 4.4.1.1 方式 1
按住 FWDN 開關 (SW101) 的同時，連接 12V 電源以開啟 VCP-G 開發板。  
按住 FWDN 開關時通電，FWDN 紅色指示燈會亮起。放開 FWDN 開關 (SW101) 後，MCU 即進入 FWDN 模式。  
圖 4.4 顯示如何使用方式 1 進入 FWDN 模式。
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Hardware/4.4%20Entering%20FWDN%20Mode%20by%20Using%20Method%201.png"></p>
<p align="center"><strong>圖 4.4 使用方式 1 進入 FWDN 模式</strong><p>

#### 4.4.1.2 方式 2
在 VCP-G 開發板已連接 12V 電源的狀態下，按住 FWDN 開關 (SW101)，然後按下 RESET 輕觸開關 (SW100)。  
按住 FWDN 開關時通電，FWDN 紅色指示燈會亮起。按住 RESET 輕觸開關時，3.3V 綠色指示燈會熄滅。放開 FWDN 開關 (SW101) 後，MCU 即進入 FWDN 模式。  
圖 4.5 顯示使用方式 2 進入 FWDN 模式。

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Hardware/4.5%20Entering%20FWDN%20Mode%20by%20Using%20Method%202.png"></p>
<p align="center"><strong>圖 4.5 使用方式 2 進入 FWDN 模式</strong><p>

</br></br></br>

## 4.5 RESET 輕觸開關 (SW100)
---
VCP-G 具有一個 RESET 開關，使用 GRESETn 腳位進行電源重置。  
圖 4.6 顯示 RESET 輕觸開關 (SW100)。
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Hardware/4.6%20RESET%20Tact%20Switch%20(SW100).png"></p>
<p align="center"><strong>圖 4.6 RESET 輕觸開關 (SW100)</strong><p>
</br></br>

### 4.5.1 RESET 輕觸開關 (SW100) 功能
SW100 是用於重置 VCP-G 中電源區塊與系統區塊的輕觸開關。  
此按鈕的功能如下：
  - 在通電狀態下按下 RESET 輕觸開關 (SW100)，會強制重置 VCP-G 的電源區塊與系統。

**重要：** 按下輕觸開關時請小心，因為電源會突然關閉，資料可能因此損毀。

</br></br></br>

## 4.6 除錯與 FWDN 接頭 (JC100)
---
JC100 是標準的 USB Type-C 接頭。在 VCP-G 上，JC100 用於透過 UART 進行除錯或 FWDN。  
圖 4.7 顯示 JC100 的位置。
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Hardware/4.7%20USB%20Type-C%20Connector%20(JC100).png"></p>
<p align="center"><strong>圖 4.7 USB Type-C 接頭 (JC100)</strong><p>

您可以透過 JC100 執行 FWDN 或檢視 VCP-G 的除錯訊息。
VCP-G 上的 JC100 內建 USB 轉 UART 橋接控制器，因此您可以使用 USB Type-C 傳輸線將 JC100 直接連接至 PC。

</br></br></br>

## 4.7 GPIO、ADC、電源、CAN 與 SPI 用排針
---
VCP-G 具有九組 2.54 mm 排針，用於電源、GPIO、ADC、CAN 與 SPI，可連接感測器或子板等其他周邊裝置。  

表 4.4 說明 VCP-G 上九組排針的用途。
<p align="center"><strong>表 4.4 VCP-G 上的排針 </strong></p>
<div align="center">
	<table>
	  <tr>
	    <td colspan="4"><strong>編號</strong></td>
	    <td><strong>參考編號</strong></td>
	    <td><strong>名稱</strong></td>
	    <td><strong>說明</strong></td>
	  </tr>
	  <tr>
	    <td colspan="4">1</td>
	    <td>J18D100</td>
	    <td>36 針母排針</td>
	    <td>GPIO 與 ADC 用排針</td>
	  </tr>
	  <tr>
	    <td colspan="4">2</td>
	    <td>J5D100</td>
	    <td>10 針公排針</td>
	    <td>CAN 用排針</td>
	  </tr>
	  <tr>
	    <td colspan="4">3</td>
	    <td>J3D100</td>
	    <td>6 針公排針</td>
	    <td>SPI 用排針</td>
	  </tr>
	  <tr>
	    <td colspan="4">4</td>
	    <td>J8D104</td>
	    <td>8 針母排針</td>
	    <td>GPIO 與 ADC 用排針</td>
	  </tr>
	  <tr>
	    <td colspan="4">5</td>
	    <td>J8D102</td>
	    <td>8 針母排針</td>
	    <td>GPIO 用排針</td>
	  </tr>
	  <tr>
	    <td colspan="4">6</td>
	    <td>J10D100</td>
	    <td>10 針母排針</td>
	    <td>GPIO 與 ADC 用排針</td>
	  </tr>
	  <tr>
	    <td colspan="4">7</td>
	    <td>J8D100</td>
	    <td>8 針母排針</td>
	    <td>電源與重置用排針</td>
	  </tr>
	  <tr>
	    <td colspan="4">8</td>
	    <td>J8D101</td>
	    <td>8 針母排針</td>
	    <td>GPIO 與 ADC 用排針</td>
	  </tr>
	  <tr>
	    <td colspan="4">9</td>
	    <td>J8D103</td>
	    <td>8 針母排針</td>
	    <td>GPIO 與 ADC 用排針</td>
	  </tr>
	</table>
</div>

圖 4.8 顯示 VCP-G 上排針的位置。
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Hardware/4.8%20Pin%20Headers%20on%20TOPST%20VCP-G%20Board.png"></p>
<p align="center"><strong>圖 4.8 VCP-G 上的排針 </strong><p>

表 4.5 顯示 J10D100 的腳位說明。
<p align="center"><strong>表 4.5 J10D100 腳位說明</strong></p>
<div align="center">
	<table>
	  <tr>
	    <th rowspan="3"><strong>腳位編號</strong></th>
	    <th colspan="4"><strong>J10D100</strong></th>
	  </tr>
	  <tr>
	    <th rowspan="2"><strong>連接埠名稱</strong></th>
	    <th rowspan="2"><strong>訊號名稱</strong></th>
	    <th><strong>DIR</strong></th>
	    <th rowspan="2"><strong>說明</strong></th>
	  </tr>
	  <tr>
	    <th><strong>MCU ◄► J10D100</strong></th>
	  </tr>
	  <tr>
	    <td>1</td>
	    <td>SCL</td>
	    <td>GPIO_AC07</td>
	    <td>◄►</td>
	    <td>GPIO 或 ADC 訊號</td>
	  </tr>
	  <tr>
	    <td>2</td>
	    <td>SDA</td>
	    <td>GPIO_AC06</td>
	    <td>◄►</td>
	    <td>GPIO 或 ADC 訊號</td>
	  </tr>
	  <tr>
	    <td>3</td>
	    <td>AREF</td>
	    <td>ADC06</td>
	    <td>◄</td>
	    <td>ADC 訊號</td>
	  </tr>
	  <tr>
	    <td>4</td>
	    <td>GND</td>
	    <td>DGND</td>
	    <td>-</td>
	    <td>接地</td>
	  </tr>
	  <tr>
	    <td>5</td>
	    <td>13</td>
	    <td>GPIO_C12</td>
	    <td>◄►</td>
	    <td>GPIO 訊號</td>
	  </tr>
	  <tr>
	    <td>6</td>
	    <td>12</td>
	    <td>GPIO_C15</td>
	    <td>◄►</td>
	    <td>GPIO 訊號</td>
	  </tr>
	  <tr>
	    <td>7</td>
	    <td>11</td>
	    <td>GPIO_C14</td>
	    <td>◄►</td>
	    <td>GPIO 訊號</td>
	  </tr>
	  <tr>
	    <td>8</td>
	    <td>10</td>
	    <td>GPIO_C13</td>
	    <td>◄►</td>
	    <td>GPIO 訊號</td>
	  </tr>
	  <tr>
	    <td>9</td>
	    <td>9</td>
	    <td>GPIO_A12</td>
	    <td>◄►</td>
	    <td>GPIO 訊號</td>
	  </tr>
	  <tr>
	    <td>10</td>
	    <td>8</td>
	    <td>GPIO_B00</td>
	    <td>◄►</td>
	    <td>GPIO 訊號</td>
	  </tr>
	</table>
</div>

表 4.6 顯示 J8D100 的腳位說明。
<p align="center"><strong>表 4.6 J8D100 腳位說明</strong></p>
<div align="center">
	<table>
	  <tr>
	    <th rowspan="3"><strong>腳位編號</strong></th>
	    <th colspan="4"><strong>J8D100</strong></th>
	  </tr>
	  <tr>
	    <th rowspan="2"><strong>連接埠名稱</strong></th>
	    <th rowspan="2"><strong>訊號名稱</strong></th>
	    <th><strong>DIR</strong></th>
	    <th rowspan="2"><strong>說明</strong></th>
	  </tr>
	  <tr>
	    <th><strong>MCU ◄► J8D100</strong></th>
	  </tr>
	  <tr>
	    <td>1</td>
	    <td>-</td>
	    <td>-</td>
	    <td>-</td>
	    <td>-</td>
	  </tr>
	  <tr>
	    <td>2</td>
	    <td>IOREF</td>
	    <td>VCP_3P3</td>
	    <td>-</td>
	    <td>電源 3.3V</td>
	  </tr>
	  <tr>
	    <td>3</td>
	    <td>RST</td>
	    <td>RESET</td>
	    <td>◄</td>
	    <td>重置訊號</td>
	  </tr>
	  <tr>
	    <td>4</td>
	    <td>3.3V</td>
	    <td>VCP_3P3</td>
	    <td>-</td>
	    <td>電源 3.3V</td>
	  </tr>
	  <tr>
	    <td>5</td>
	    <td>5V</td>
	    <td>VCP_5P0</td>
	    <td>-</td>
	    <td>電源 5.0V</td>
	  </tr>
	  <tr>
	    <td>6</td>
	    <td>GND</td>
	    <td>DGND</td>
	    <td>-</td>
	    <td>接地</td>
	  </tr>
	  <tr>
	    <td>7</td>
	    <td>GND</td>
	    <td>DGND</td>
	    <td>-</td>
	    <td>接地</td>
	  </tr>
	  <tr>
	    <td>8</td>
	    <td>VIN</td>
	    <td>VIN</td>
	    <td>-</td>
	    <td>VCP-G 的電壓輸入</td>
	  </tr>
	</table>
</div>

表 4.7 顯示 J8D101 的腳位說明。
<p align="center"><strong>表 4.7 J8D101 腳位說明</strong></p>
<div align="center">
	<table>
	  <tr>
	    <th rowspan="3"><strong>腳位編號</strong></th>
	    <th colspan="4"><strong>J8D101</strong></th>
	  </tr>
	  <tr>
	    <th rowspan="2"><strong>連接埠名稱</strong></th>
	    <th rowspan="2"><strong>訊號名稱</strong></th>
	    <th><strong>DIR</strong></th>
	    <th rowspan="2"><strong>說明</strong></th>
	  </tr>
	  <tr>
	    <th><strong>MCU ◄► J8D101</strong></th>
	  </tr>
	  <tr>
	    <td>1</td>
	    <td>A0</td>
	    <td>ADC03</td>
	    <td>◄</td>
	    <td>ADC 訊號</td>
	  </tr>
	  <tr>
	    <td>2</td>
	    <td>A1</td>
	    <td>ADC04</td>
	    <td>◄</td>
	    <td>ADC 訊號</td>
	  </tr>
	  <tr>
	    <td>3</td>
	    <td>A2</td>
	    <td>GPIO_AC02</td>
	    <td>◄►</td>
	    <td>GPIO 訊號</td>
	  </tr>
	  <tr>
	    <td>4</td>
	    <td>A3</td>
	    <td>GPIO_AC03</td>
	    <td>◄►</td>
	    <td>GPIO 訊號</td>
	  </tr>
	  <tr>
	    <td>5</td>
	    <td>A4</td>
	    <td>GPIO_AC05</td>
	    <td>◄►</td>
	    <td>GPIO 訊號</td>
	  </tr>
	  <tr>
	    <td>6</td>
	    <td>A5</td>
	    <td>GPIO_AC04</td>
	    <td>◄►</td>
	    <td>GPIO 訊號</td>
	  </tr>
	  <tr>
	    <td>7</td>
	    <td>A6</td>
	    <td>ADC05</td>
	    <td>◄</td>
	    <td>ADC 訊號</td>
	  </tr>
	  <tr>
	    <td>8</td>
	    <td>A7</td>
	    <td>ADC01</td>
	    <td>◄</td>
	    <td>ADC 訊號</td>
	  </tr>
	</table>
</div>

表 4.8 顯示 J8D102 的腳位說明。
<p align="center"><strong>表 4.8 J8D102 腳位說明</strong></p>
<div align="center">
	<table>
	  <tr>
	    <th rowspan="3"><strong>腳位編號</strong></th>
	    <th colspan="4"><strong>J8D102</strong></th>
	  </tr>
	  <tr>
	    <th rowspan="2"><strong>連接埠名稱</strong></th>
	    <th rowspan="2"><strong>訊號名稱</strong></th>
	    <th><strong>DIR</strong></th>
	    <th rowspan="2"><strong>說明</strong></th>
	  </tr>
	  <tr>
	    <th><strong>MCU ◄► J8D102</strong></th>
	  </tr>
	  <tr>
	    <td>1</td>
	    <td>7</td>
	    <td>GPIO_B01</td>
	    <td>◄►</td>
	    <td>GPIO 訊號</td>
	  </tr>
	  <tr>
	    <td>2</td>
	    <td>6</td>
	    <td>GPIO_A13</td>
	    <td>◄►</td>
	    <td>GPIO 訊號</td>
	  </tr>
	  <tr>
	    <td>3</td>
	    <td>5</td>
	    <td>GPIO_B10</td>
	    <td>◄►</td>
	    <td>GPIO 訊號</td>
	  </tr>
	  <tr>
	    <td>4</td>
	    <td>4</td>
	    <td>GPIO_B27</td>
	    <td>◄►</td>
	    <td>GPIO 訊號</td>
	  </tr>
	  <tr>
	    <td>5</td>
	    <td>3</td>
	    <td>GPIO_B11</td>
	    <td>◄►</td>
	    <td>GPIO 訊號</td>
	  </tr>
	  <tr>
	    <td>6</td>
	    <td>2</td>
	    <td>GPIO_B28</td>
	    <td>◄►</td>
	    <td>GPIO 訊號</td>
	  </tr>
	  <tr>
	    <td>7</td>
	    <td>1</td>
	    <td>GPIO_B25</td>
	    <td>◄►</td>
	    <td>GPIO 訊號</td>
	  </tr>
	  <tr>
	    <td>8</td>
	    <td>0</td>
	    <td>GPIO_B26</td>
	    <td>◄►</td>
	    <td>GPIO 訊號</td>
	  </tr>
	</table>
</div>

表 4.9 顯示 J8D103 的腳位說明。
<p align="center"><strong>表 4.9 J8D103 腳位說明</strong></p>
<div align="center">
	<table>
	  <tr>
	    <th rowspan="3"><strong>腳位編號</strong></th>
	    <th colspan="4"><strong>J8D103</strong></th>
	  </tr>
	  <tr>
	    <th rowspan="2"><strong>連接埠名稱</strong></th>
	    <th rowspan="2"><strong>訊號名稱</strong></th>
	    <th><strong>DIR</strong></th>
	    <th rowspan="2"><strong>說明</strong></th>
	  </tr>
	  <tr>
	    <th><strong>MCU ◄► J8D103</strong></th>
	  </tr>
	  <tr>
	    <td>1</td>
	    <td>A8</td>
	    <td>GPIO_AC08</td>
	    <td>◄►</td>
	    <td>GPIO 或 ADC 訊號</td>
	  </tr>
	  <tr>
	    <td>2</td>
	    <td>A9</td>
	    <td>GPIO_AC09</td>
	    <td>◄►</td>
	    <td>GPIO 或 ADC 訊號</td>
	  </tr>
	  <tr>
	    <td>3</td>
	    <td>A10</td>
	    <td>GPIO_AC10</td>
	    <td>◄►</td>
	    <td>GPIO 或 ADC 訊號</td>
	  </tr>
	  <tr>
	    <td>4</td>
	    <td>A11</td>
	    <td>GPIO_ADC-2</td>
	    <td>◄</td>
	    <td>ADC 訊號</td>
	  </tr>
	  <tr>
	    <td>5</td>
	    <td>54</td>
	    <td>GPIO_K14</td>
	    <td>◄►</td>
	    <td>GPIO 訊號</td>
	  </tr>
	  <tr>
	    <td>6</td>
	    <td>55</td>
	    <td>GPIO_K15</td>
	    <td>◄►</td>
	    <td>GPIO 訊號</td>
	  </tr>
	  <tr>
	    <td>7</td>
	    <td>56</td>
	    <td>GPIO_K01</td>
	    <td>◄</td>
	    <td>GPIO 訊號</td>
	  </tr>
	  <tr>
	    <td>8</td>
	    <td>57</td>
	    <td>GPIO_K08</td>
	    <td>◄►</td>
	    <td>GPIO 訊號</td>
	  </tr>
	</table>
</div>

表 4.10 顯示 J8D104 的腳位說明。
<p align="center"><strong>表 4.10 J8D104 腳位說明</strong></p>
<div align="center">
	<table>
	  <tr>
	    <th rowspan="3"><strong>腳位編號</strong></th>
	    <th colspan="4"><strong>J8D104</strong></th>
	  </tr>
	  <tr>
	    <th rowspan="2"><strong>連接埠名稱</strong></th>
	    <th rowspan="2"><strong>訊號名稱</strong></th>
	    <th><strong>DIR</strong></th>
	    <th rowspan="2"><strong>說明</strong></th>
	  </tr>
	  <tr>
	    <th><strong>MCU ◄► J8D104</strong></th>
	  </tr>
	  <tr>
	    <td>1</td>
	    <td>14</td>
	    <td>GPIO_AC00</td>
	    <td>◄►</td>
	    <td>GPIO 或 ADC 訊號</td>
	  </tr>
	  <tr>
	    <td>2</td>
	    <td>15</td>
	    <td>GPIO_AC01</td>
	    <td>◄►</td>
	    <td>GPIO 或 ADC 訊號</td>
	  </tr>
	  <tr>
	    <td>3</td>
	    <td>16</td>
	    <td>GPIO_A06</td>
	    <td>◄►</td>
	    <td>GPIO 訊號</td>
	  </tr>
	  <tr>
	    <td>4</td>
	    <td>17</td>
	    <td>GPIO_A07</td>
		<td>◄►</td>
	    <td>GPIO 訊號</td>
	  </tr>
	  <tr>
	    <td>5</td>
	    <td>18</td>
	    <td>GPIO_A28</td>
	    <td>◄►</td>
	    <td>GPIO 訊號</td>
	  </tr>
	  <tr>
	    <td>6</td>
	    <td>19</td>
	    <td>GPIO_A29</td>
	    <td>◄►</td>
	    <td>GPIO 訊號</td>
	  </tr>
	  <tr>
	    <td>7</td>
	    <td>20</td>
	    <td>GPIO_B03</td>
	    <td>◄►</td>
	    <td>GPIO 訊號</td>
	  </tr>
	  <tr>
	    <td>8</td>
	    <td>21</td>
	    <td>GPIO_B02</td>
	    <td>◄►</td>
	    <td>GPIO 訊號</td>
	  </tr>
	</table>
</div>

表 4.11 顯示 J3D100 的腳位說明。
<p align="center"><strong>表 4.11 J3D100 腳位說明</strong></p>
<div align="center">
	<table>
	  <tr>
	    <th rowspan="3"><strong>腳位編號</strong></th>
	    <th colspan="4"><strong>J3D100</strong></th>
	  </tr>
	  <tr>
	    <th rowspan="2"><strong>連接埠名稱</strong></th>
	    <th rowspan="2"><strong>訊號名稱</strong></th>
	    <th><strong>DIR</strong></th>
	    <th rowspan="2"><strong>說明</strong></th>
	  </tr>
	  <tr>
	    <th><strong>MCU ◄► J3D100</strong></th>
	  </tr>
	  <tr>
	    <td>1</td>
	    <td>MISO</td>
	    <td>GPIO_B07</td>
	    <td>◄►</td>
	    <td>GPIO 訊號</td>
	  </tr>
	  <tr>
	    <td>2</td>
	    <td>5V</td>
	    <td>VCP_5P0</td>
	    <td>-</td>
	    <td>電源 5.0V</td>
	  </tr>
	  <tr>
	    <td>3</td>
	    <td>SCK</td>
	    <td>GPIO_B04</td>
	    <td>◄►</td>
	    <td>GPIO 訊號</td>
	  </tr>
	  <tr>
	    <td>4</td>
	    <td>MOSI</td>
	    <td>GPIO_B06</td>
	    <td>◄►</td>
	    <td>GPIO 訊號</td>
	  </tr>
	  <tr>
	    <td>5</td>
	    <td>CMD</td>
	    <td>GPIO_B05</td>
	    <td>◄►</td>
	    <td>GPIO 訊號</td>
	  </tr>
	  <tr>
	    <td>6</td>
	    <td>GND</td>
	    <td>DGND</td>
	    <td>-</td>
	    <td>接地</td>
	  </tr>
	</table>
</div>

表 4.12 顯示 J18D100 的腳位說明。
<p align="center"><strong>表 4.12 J18D100 腳位說明</strong></p>
<div align="center">
	<table>
	  <tr>
	    <th rowspan="3"><strong>腳位編號</strong></th>
	    <th colspan="4"><strong>J18D100</strong></th>
	  </tr>
	  <tr>
	    <th rowspan="2"><strong>連接埠名稱</strong></th>
	    <th rowspan="2"><strong>訊號名稱</strong></th>
	    <th><strong>DIR</strong></th>
	    <th rowspan="2"><strong>說明</strong></th>
	  </tr>
	  <tr>
	    <th><strong>MCU ◄► J18D100</strong></th>
	  </tr>
	  <tr>
	    <td>1</td>
	    <td>5V</td>
	    <td>VCP_5P0</td>
	    <td>-</td>
	    <td>電源 5.0V</td>
	  </tr>
	  <tr>
	    <td>2</td>
	   <td>5V</td>
	    <td>VCP_5P0</td>
	    <td>-</td>
	    <td>電源 5.0V</td>
	  </tr>
	  <tr>
	    <td>3</td>
	    <td>22</td>
	    <td>GPIO_B24</td>
	    <td>◄►</td>
	    <td>GPIO 訊號</td>
	  </tr>
	  <tr>
	    <td>4</td>
	    <td>23</td>
	    <td>GPIO_B23</td>
	    <td>◄►</td>
	    <td>GPIO 訊號</td>
	  </tr>
	  <tr>
	    <td>5</td>
	    <td>24</td>
	    <td>GPIO_B22</td>
	    <td>◄►</td>
	    <td>GPIO 訊號</td>
	  </tr>
	  <tr>
	    <td>6</td>
	    <td>25</td>
	    <td>GPIO_B21</td>
	    <td>◄►</td>
	    <td>GPIO 訊號</td>
	  </tr>
	  <tr>
	    <td>7</td>
	    <td>26</td>
	    <td>GPIO_B20</td>
	    <td>◄►</td>
	    <td>GPIO 訊號</td>
	  </tr>
	  <tr>
	    <td>8</td>
	    <td>27</td>
	    <td>GPIO_B19</td>
	    <td>◄►</td>
	    <td>GPIO 訊號</td>
	  </tr>
	  <tr>
	    <td>9</td>
	    <td>28</td>
	    <td>GPIO_A30</td>
	    <td>◄►</td>
	    <td>GPIO 訊號</td>
	  </tr>
	  <tr>
	    <td>10</td>
	    <td>29</td>
	    <td>GPIO_A27</td>
	    <td>◄►</td>
	    <td>GPIO 訊號</td>
	  </tr>
	  <tr>
	    <td>11</td>
	    <td>230</td>
	    <td>GPIO_A26</td>
	    <td>◄►</td>
	    <td>GPIO 訊號</td>
	  </tr>
	  <tr>
	    <td>12</td>
	    <td>31</td>
	    <td>GPIO_A24</td>
	    <td>◄►</td>
	    <td>GPIO 訊號</td>
	  </tr>
	  <tr>
	    <td>13</td>
	    <td>32</td>
	    <td>GPIO_A25</td>
	    <td>◄►</td>
	    <td>GPIO 訊號</td>
	  </tr>
	  <tr>
	    <td>14</td>
	    <td>33</td>
	    <td>GPIO_A23</td>
	    <td>◄►</td>
	    <td>GPIO 訊號</td>
	  </tr>
	  <tr>
	    <td>15</td>
	    <td>34</td>
	    <td>GPIO_A22</td>
	    <td>◄►</td>
	    <td>GPIO 訊號</td>
	  </tr>
	  <tr>
	    <td>16</td>
	    <td>35</td>
	    <td>GPIO_A21</td>
	    <td>◄►</td>
		<td>GPIO 訊號</td>
	  </tr>
	  <tr>
	    <td>17</td>
	    <td>36</td>
	    <td>GPIO_A20</td>
	    <td>◄►</td>
	    <td>GPIO 訊號</td>
	  </tr>
	  <tr>
	    <td>18</td>
	    <td>37</td>
	    <td>GPIO_A19</td>
	    <td>◄►</td>
	    <td>GPIO 訊號</td>
	  </tr>
	  <tr>
	    <td>19</td>
	    <td>38</td>
	    <td>GPIO_K13</td>
	    <td>◄►</td>
		<td>GPIO 訊號</td>
	  </tr>
	  <tr>
	    <td>20</td>
	    <td>39</td>
	    <td>GPIO_K12</td>
	    <td>◄►</td>
	    <td>GPIO 訊號</td>
	  </tr>
	  <tr>
	    <td>21</td>
	    <td>40</td>
	    <td>GPIO_K11</td>
	    <td>◄►</td>
	    <td>GPIO 訊號</td>
	  </tr>
	  <tr>
	    <td>22</td>
	    <td>41</td>
	    <td>GPIO_A18</td>
	    <td>◄►</td>
	    <td>GPIO 訊號</td>
	  </tr>
	  <tr>
	    <td>23</td>
	    <td>42</td>
	    <td>GPIO_A17</td>
	    <td>◄►</td>
	    <td>GPIO 訊號</td>
	  </tr>
	  <tr>
	    <td>24</td>
	    <td>43</td>
	    <td>GPIO_A16</td>
	    <td>◄►</td>
	    <td>GPIO 訊號</td>
	  </tr>
	  <tr>
	    <td>25</td>
	    <td>44</td>
	    <td>GPIO_A11</td>
	    <td>◄►</td>
	    <td>GPIO 訊號</td>
	  </tr>
	  <tr>
	    <td>26</td>
	    <td>45</td>
	    <td>GPIO_A10</td>
	    <td>◄►</td>
	    <td>GPIO 訊號</td>
	  </tr>
	  <tr>
	    <td>27</td>
	    <td>46</td>
	    <td>GPIO_A09</td>
	    <td>◄►</td>
	    <td>GPIO 訊號</td>
	  </tr>
	  <tr>
	    <td>28</td>
	    <td>47</td>
	    <td>GPIO_A08</td>
	    <td>◄►</td>
	    <td>GPIO 訊號</td>
	  </tr>
	  <tr>
	    <td>29</td>
	    <td>48</td>
	    <td>GPIO_A05</td>
	    <td>◄►</td>
	    <td>GPIO 訊號</td>
	  </tr>
	  <tr>
	    <td>30</td>
	    <td>49</td>
	    <td>GPIO_A04</td>
	    <td>◄►</td>
	    <td>GPIO 訊號</td>
	  </tr>
	  <tr>
	    <td>31</td>
	    <td>50</td>
	    <td>GPIO_A03</td>
	    <td>◄►</td>
	    <td>GPIO 訊號</td>
	  </tr>
	  <tr>
	    <td>32</td>
	    <td>51</td>
	    <td>GPIO_A02</td>
	    <td>◄►</td>
	    <td>GPIO 訊號</td>
	  </tr>
	  <tr>
	    <td>33</td>
	    <td>52</td>
	    <td>GPIO_A01</td>
	    <td>◄►</td>
	    <td>GPIO 訊號</td>
	  </tr>
	  <tr>
	    <td>34</td>
	    <td>53</td>
	    <td>GPIO_A00</td>
	    <td>◄►</td>
	    <td>GPIO 訊號</td>
	  </tr>
	  <tr>
	    <td>35</td>
	    <td>GND</td>
	    <td>DGND</td>
	    <td>-</td>
	    <td>接地</td>
	  </tr>
	  <tr>
	    <td>36</td>
	    <td>GND</td>
	    <td>DGND</td>
	    <td>-</td>
	    <td>接地</td>
	  </tr>
	</table>
</div>

表 4.13 顯示 J5D100 的腳位說明。
<p align="center"><strong>表 4.13 J5D100 腳位說明</strong></p>
<div align="center">
	<table>
	  <tr>
	    <th rowspan="3"><strong>腳位編號</strong></th>
	    <th colspan="4"><strong>J5D100</strong></th>
	  </tr>
	  <tr>
	    <th rowspan="2"><strong>連接埠名稱</strong></th>
	    <th rowspan="2"><strong>訊號名稱</strong></th>
	    <th><strong>DIR</strong></th>
	    <th rowspan="2"><strong>說明</strong></th>
	  </tr>
	  <tr>
	    <th><strong>MCU ◄► J5D100</strong></th>
	  </tr>
	  <tr>
	    <td>1</td>
	    <td>3.3V</td>
	    <td>VCP_3P3</td>
	    <td>-</td>
	    <td>電源 3.3V</td>
	  </tr>
	  <tr>
	    <td>2</td>
	    <td>3.3V</td>
	    <td>VCP_3P3</td>
	    <td>-</td>
    <td>電源 3.3V</td>
	  </tr>
	  <tr>
	    <td>3</td>
	    <td>TX0</td>
	    <td>GPIO_K08</td>
	    <td>◄►</td>
	    <td>GPIO 訊號</td>
	  </tr>
	  <tr>
	    <td>4</td>
	    <td>RX0</td>
	    <td>GPIO_K01</td>
	    <td>◄</td>
	    <td>GPIO 訊號</td>
	  </tr>
	  <tr>
	    <td>5</td>
	    <td>TX1</td>
	    <td>GPIO_K09</td>
	    <td>◄►</td>
	    <td>GPIO 訊號</td>
	  </tr>
	  <tr>
	    <td>6</td>
	    <td>RX1</td>
	    <td>GPIO_K02</td>
	    <td>◄</td>
	    <td>GPIO 訊號</td>
	  </tr>
	  <tr>
	    <td>7</td>
	    <td>TX2</td>
	    <td>GPIO_K10</td>
	    <td>◄►</td>
	    <td>GPIO 訊號</td>
	  </tr>
	  <tr>
	    <td>8</td>
	    <td>RX2</td>
	    <td>GPIO_K03</td>
	    <td>◄</td>
	    <td>GPIO 訊號</td>
	  </tr>
	  <tr>
	    <td>9</td>
	    <td>GND</td>
	    <td>DGND</td>
	    <td>-</td>
	    <td>DGND</td>
	  </tr>
	  <tr>
	    <td>10</td>
	    <td>GND</td>
	    <td>DGND</td>
	    <td>-</td>
	    <td>DGND</td>
	  </tr>
	</table>
</div>

圖 4.9 顯示 VCP-G 上十組排針的完整腳位配置。
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Hardware/4.9%20Total%20Pin%20Assignment%20of%20Pin%20Headers%20on%20TOPST%20VCP-G%20Board.png"></p>
<p align="center"><strong>圖 4.9 VCP-G 上排針的完整腳位配置 </strong><p>

# 參考資料
  - 如需更多詳細資訊，請聯絡 TOPST：topst@topst.ai

**註：** 參考文件可依合約條款於可提供時提供。若無法提供參考文件，則可就與您開發直接相關的內容提供指引。
