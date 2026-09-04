# MIPI 扩展板
----

MIPI 扩展板采用 GMSL2 高速串行通信来支持 MIPI CSI 和 MIPI DSI 接口（图 1）。每块板卡均集成了串行器和解串器芯片组，用于处理摄像头输入和显示输出，确保高分辨率数据传输的可靠性。 
**注意:** 组件供货情况和配置根据具体项目需求以按订单生产的方式提供。

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/accessories/mipi_expansion_board_crop.png" width="350"></p>
<p align="center"><strong>图 1. MIPI 扩展板</strong></p><br/>

## MIPI CSI (摄像头串行接口)

### 板卡信息
- **尺寸**: 71.5 mm × 73.5 mm × 1.6 t / 4 层
- **解串器**: MAX96712 (ADI)
- **GMSL 版本**: GMSL2
- **链路数量**: 最多 4 通道 MIPI CSI2 输入
- **分辨率 / 带宽**: 最高 1.5 Gbps × 4 条 lane × 4 个通道
- **供电电压**: 1.8V / 3.3V
- **封装**: 64 QFN / 9 mm × 9 mm
- **控制接口**: I²C
- **B2B 连接器**: 61083-043402LF (Amphenol)


## MIPI DSI (显示串行接口)

### 板卡信息
- **尺寸**: 60 mm × 30 mm × 1.6 t / 4 层
- **串行器**: MAX96789 (ADI)
- **GMSL 版本**: GMSL2
- **链路数量**: 最多 4 通道 MIPI DSI2 输出
- **分辨率 / 带宽**: 最高 6 Gbps
- **供电电压**: 1.8V / 3.3V
- **封装**: 56 QFN / 8 mm × 8 mm
- **控制接口**: I²C
- **B2B 连接器**: 10132797-067110LF (Amphenol)