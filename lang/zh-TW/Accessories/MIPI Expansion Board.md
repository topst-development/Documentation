# MIPI 擴充板
----

MIPI 擴充板採用 GMSL2 高速序列通訊，以支援 MIPI CSI 與 MIPI DSI 介面（圖 1）。每片開發板皆整合序列器與解序列器晶片組，用以處理攝影機輸入與顯示輸出，確保高解析度資料的可靠傳輸。 
**註：** 零件供應狀況與組態依專案的特定需求以接單生產方式提供。

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/accessories/mipi_expansion_board_crop.png" width="350"></p>
<p align="center"><strong>圖 1. MIPI 擴充板</strong></p><br/>

## MIPI CSI（Camera Serial Interface）

### 開發板資訊
- **尺寸**：71.5 mm × 73.5 mm × 1.6 t / 4 層板
- **解序列器**：MAX96712 (ADI)
- **GMSL 版本**：GMSL2
- **連結數量**：最多 4 通道 MIPI CSI2 輸入
- **解析度 / 頻寬**：最高 1.5 Gbps × 4-lanes × 4 channels
- **電源供應**：1.8V / 3.3V
- **封裝**：64 QFN / 9 mm × 9 mm
- **控制介面**：I²C
- **B2B 連接器**：61083-043402LF (Amphenol)


## MIPI DSI（Display Serial Interface）

### 開發板資訊
- **尺寸**：60 mm × 30 mm × 1.6 t / 4 層板
- **序列器**：MAX96789 (ADI)
- **GMSL 版本**：GMSL2
- **連結數量**：最多 4 通道 MIPI DSI2 輸出
- **解析度 / 頻寬**：最高 6 Gbps
- **電源供應**：1.8V / 3.3V
- **封裝**：56 QFN / 8 mm × 8 mm
- **控制介面**：I²C
- **B2B 連接器**：10132797-067110LF (Amphenol)