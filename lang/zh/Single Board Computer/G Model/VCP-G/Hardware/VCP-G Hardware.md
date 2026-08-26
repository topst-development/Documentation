# 1. 简介
---
本文档是基于 TCC7045 应用处理器的 VCP-G 硬件用户指南。本文档介绍 VCP-G 的系统安装、调试以及整体设计和使用方法的详细信息。


表 1.1 介绍了 VCP-G 的特性。

<p align="center"><strong>表 1.1 VCP-G 的特性</strong></p>
<div align="center">
	<table>
	  <tr>
	    <td colspan="3">元件名称</td>
	    <td>TCC7045</td>
	  </tr>
	  <tr>
	    <td colspan="3">封装</td>
	    <td>封装	引脚对引脚兼容 FBGA 196-pin (12BD)</td>
	  </tr>
	    <tr>
	    <td colspan="3">CPU 频率</td>
	    <td>200 MHz（最高 300 MHz）</td>
	  </tr>
	  <tr>
	    <td rowspan="4">片上存储器</td>
	    <td colspan="2">程序闪存</td>
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
	    <td colspan="3">16 个通道</td>
	  </tr>
	  <tr>
	    <td rowspan="13">外设</td>
	    <td colspan="2">Ethernet</td>
	    <td>1 Gbps，支持 AVB</td>
	  </tr>
	  <tr>
		<td colspan="2">CAN / CANFD</td>
	    <td>3 通道</td>
	  </tr>
	  <tr>
	    <td colspan="2">专用 LIN / UART</td>
	    <td>3 个通道（最多 6 个通道）</td>
	  </tr>
	  <tr>
	    <td colspan="2">专用 I2C</td>
	    <td>3 个通道（最多 6 个通道）</td>
	  </tr>
	  <tr>
	  <tr>
	    <td colspan="2">专用 GPSB (SPI)</td>
	    <td>2 个通道（最多 5 个通道）</td>
	  </tr>
	    <tr>
	    <td colspan="2">MFIO（分配给 UART、I2C、GPSB）</td>
	    <td>3 个通道</td>
	  </tr>
	  <tr>
	    <td rowspan="4">ADC</td> 
	    <td>分辨率</td>
	    <td>12 位 SAR 型</td>
	  </tr>
	  <tr>
	    <td>通道</td>
	    <td>12 通道 x 2 组</td>
	  </tr>
	  <tr>
	    <td>输入范围</td>
	    <td>3.3V</td>
	  </tr>
	  <tr>
	    <td>采样率</td>
	    <td>1.0 MSPs 以上</td>
	  </tr>
	  <tr>
	    <td colspan="2">I2S</td>
	    <td>1 通道</td>
	  </tr>
	  <tr>
	    <td colspan="2">串行闪存接口</td>
	    <td>Quad SPI</td>
	  </tr>  
	  <tr>
	    <td colspan="3">电源系统</td>
	    <td>3.3V 单电源</td>
	  </tr>
	  <tr>
	    <td colspan="3">温度</td>
	    <td>-40 ℃ to 105 ℃</td>
	  </tr>
	</table>
</div>

</br></br></br>

## 1.1 术语
---
<p align="center"><strong>表 1.2 术语 </strong></p>
<div align="center">
	<table>
	  <tr>
	    <td clospan="2"><strong>术语</strong></td>
	    <td><strong>定义</strong></td>
	  </tr>
	  <tr>
	    <td clospan="2">ADC</td>
	    <td>模数转换器</td>
	  </tr>
	  <tr>
	    <td clospan="2">FWDN</td>
	    <td>固件下载</td>
	  </tr>
	  <tr>
	    <td clospan="2">GPIO</td>
	    <td>通用输入输出</td>
	  </tr>
	  <tr>
	    <td clospan="2">MCU</td>
	    <td>微控制器单元</td>
	  </tr>
	  <tr>
	    <td clospan="2">TOPST</td>
	    <td>面向系统开发与培训的整合开放平台</td>
	  </tr>
	  <tr>
	    <td clospan="2">VCP</td>
	    <td>车辆控制处理器</td>
	  </tr>
	</table>
</div>

</br></br></br></br>

# 2. 框图
---
## 2.1 系统框图
---
图 2.1 显示了 VCP-G 的系统框图。
<p align="center"><img src= "https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Hardware/2.1%20VCP-G%20System%20Block%20Diagram.png"></p>
<p align="center"><strong>图 2.1 系统框图</strong></p>

</br></br></br></br>

# 3. VCP-G 概述
---
VCP-G 可用于以下用途：
  - 系统开发
  - 培训

表 3.1 介绍了 VCP-G 的默认配置。

<p align="center"><strong>表 3.1 VCP-G 的默认配置 </strong></p>
<div align="center">
	<table>
	  <tr>
	    <td colspan="2"><strong>开发板名称</strong></td>
	    <td><strong>说明</strong></p>
	  </tr>
	  <tr>
	    <td colspan="2">TOPST_VCP_V2.1.1</td>
	    <td>用于 TOPST 的 MCU 开发板</td>
	  </tr>
	</table>
</div>

</br></br></br>

## 3.1 VCP-G
---
图 3.1 显示了 VCP-G 的顶视图。
<p align="center"><img src= "https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Hardware/3.1%20TOPST%20VCP-G%20Board%20(Top%20View)%20.png"></p>
<p align="center"><strong>图 3.1 VCP-G（顶视图）</strong></p>

表 3.2 介绍了 VCP-G（顶视图）的连接器。
<p align="center"><strong>表 3.2 VCP-G 的连接器（顶视图）</strong></p>
<div align="center">
	<table>
	  <tr>
	    <td colspan="4"><strong>编号</strong></td>
	    <td><strong>参考编号</strong></td>
	    <td><strong>名称</strong></td>
	    <td><strong>说明</strong></td>
	  </tr>
	  <tr>
	    <td colspan="4">1</td>
	    <td>J18D100</td>
	    <td>36 针母排针</td>
	    <td>用于 GPIO 和 ADC 的排针</td>
	  </tr>
	  <tr>
	    <td colspan="4">2</td>
	    <td>J5D100</td>
	    <td>10 针公排针</td>
	    <td>用于 CAN 的排针</td>
	  </tr>
	  <tr>
	    <td colspan="4">3</td>
	    <td>J3D100</td>
	    <td>6 针公排针</td>
	    <td>用于 SPI 的排针</td>
	  </tr>
	  <tr>
	    <td colspan="4">4</td>
	    <td>J8D104</td>
	    <td>8 针母排针</td>
	    <td>用于 GPIO 和 ADC 的排针</td>
	  </tr>
	  <tr>
	    <td colspan="4">5</td>
	    <td>J8D102</td>
	    <td>8 针母排针</td>
	    <td>用于 GPIO 的排针</td>
	  </tr>
	  <tr>
	    <td colspan="4">6</td>
	    <td>J10D100</td>
	    <td>10 针母排针</td>
	    <td>用于 GPIO 和 ADC 的排针</td>
	  </tr>
	  <tr>
	    <td colspan="4">7</td>
	    <td>J100</td>
	    <td>10 针公排针</td>
	    <td>用于 JTAG 的排针</td>
	  </tr>
	  <tr>
	    <td colspan="4">8</td>
	    <td>SW100</td>
	    <td>RESET 轻触开关</td>
	    <td>GRESETn：初始化 VCP-G 的系统和电源管理</td>
	  </tr>
	  <tr>
	    <td colspan="4">9</td>
	    <td>JC100</td>
	    <td>USB Type-C 连接器</td>
	    <td>用于调试或 FWDN 端口的 UART</td>
	  </tr>
	  <tr>
	    <td colspan="4">10</td>
	    <td>SW101</td>
	    <td>轻触开关</td>
	    <td>FWDN：进入 VCP-G 的固件下载模式</td>
	  </tr>  
	  <tr>
	    <td colspan="4">11</td>
		<td>J101</td>
	    <td>DC 插孔</td>
	    <td>DC 电源输入插孔</td>
	  </tr>  
	  <tr>
	    <td colspan="4">12</td>
	    <td>J8D100</td>
	    <td>8 针母排针</td>
	    <td>用于电源和复位的排针</td>
	  </tr>  
	  <tr>
	    <td colspan="4">13</td>
	    <td>J8D101</td>
	    <td>8 针母排针</td>
	    <td>用于 GPIO 和 ADC 的排针</td>
	  </tr>  
	  <tr>
	    <td colspan="4">14</td>
	    <td>J8D103</td>
	    <td>8 针母排针</td>
	    <td>用于 GPIO 和 ADC 的排针</td>
	  </tr>    
	</table>
</div>

图 3.2 显示了 VCP-G 的底视图。  

**注意：** 图 3.2 当前显示的是 TOPST_VCP-G_V1.1.1 开发板。该图片将更新为 TOPST_VCP-G_V2.1.1 开发板。
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Hardware/3.2%20TOPST%20VCP-G%20Board%20(Bottom%20View).png"></p>
<p align="center"><strong>图 3.2 VCP-G（底视图）</strong></p>

</br></br></br></br>

# 4. 规格
---
## 4.1 Quad SPI 闪存 (U101)
---
Quad SPI 闪存的相关信息如下：
  - 容量 : 64 Mb  
  
**注意：** 默认情况下，VCP-G 上未贴装 SNOR。

</br></br></br>

## 4.2 电源输入连接器 (J101)
---
DC 12V 由 12V 适配器通过 J101 的 DC 插孔供给 VCP-G。  
图 4.1 显示了 J101 的位置。
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Hardware/4.1%20Power%20In%20Connector%20(J101).png"></p>
<p align="center"><strong>图 4.1 电源输入连接器 (J101)</strong><p>

</br></br></br>

## 4.3 JTAG 连接器 (J100)
---
可通过 J100 将 JTAG 仿真器连接到 VCP-G 以进行调试。图 4.2 显示了 J100 的位置。
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Hardware/4.2%20Connector%20for%20JTAG%20(J100).png"></p>
<p align="center"><strong>图 4.2 JTAG 连接器 (J100)</strong><p>
默认情况下 JTAG 处于禁用状态。要启用 JTAG，必须更改 R178 和 R179 的连接。如果通过 R178 将 TRSRn 设置为高电平，MCU 将进入 JTAG 模式。

表 4.1 介绍了 J100 的引脚。
<p align="center"><strong>表 4.1 J100 引脚说明</strong></p>
<div align="center">
	<table>
	  <tr>
	    <th rowspan="2"><strong>引脚编号</strong></th>
	    <th rowspan="2"><strong>原理图网络名称</strong></th>
	    <th><strong>DIR</strong></th>
	    <th rowspan="2"><strong>说明</strong></th>
	  </tr>
	  <tr>
	    <th><strong>MCU ◄► J100</strong></th>
	  </tr>
	  <tr>
	    <td>1</td>
	    <td>SW_VDD_3P3</td>
	    <td>-</td>
	    <td>电源 3.3V</td>
	  </tr>
	  <tr>
	    <td>2</td>
	    <td>TMS</td>
	    <td>◄</td>
	    <td>测试模式状态</td>
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
	    <td>测试时钟</td>
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
	    <td>测试数据输出</td>
	  </tr>
	  <tr>
	    <td>7</td>
	    <td>NC</td>
	    <td>-</td>
	    <td>未连接</td>
	  </tr>
	  <tr>
	    <td>8</td>
	    <td>TDI</td>
	    <td>◄</td>
	    <td>测试数据输入</td>
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
	    <td>系统复位</td>
	  </tr>   
	</table>
</div>

表 4.2 介绍了 JTAG 禁用/启用的设置。
<p align="center"><strong>表 4.2 JTAG 禁用/启用的设置</strong></p>
<div align="center">
	<table>
	  <tr>
	    <th colspan="4"><strong>模式</strong></th>
	    <th><strong>TRSTn 值</strong></th>
	    <th><strong>R178</strong></th>
	    <th><strong>R179</strong></th>
	  </tr>
	  <tr>
	    <td colspan="4">JTAG 禁用（默认）</td>
	    <td>Low (1)</td>
	    <td>N.C</td>
	    <td>1K</td>
	  </tr>
	  <tr>
	    <td colspan="4">JTAG 启用（选配）</td>
	    <td>High (1)</td>
	    <td>1K</td>
	    <td>N.C</td>
	  </tr>
	</table>
</div>

</br></br></br>

## 4.4 FWDN 开关 (SW101)
---
VCP-G 有一个使用 Boot Mode (BM) 进行启动配置的引脚，支持 2 种模式：UART FWDN 模式和正常模式。   
图 4.3 显示了用于选择 VCP-G 启动模式的 FWDN 轻触开关 (SW101) 的位置。
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Hardware/4.3%20FWDN%20Tact%20Switch%20(SW101).png"></p>
<p align="center"><strong>图 4.3 FWDN 轻触开关 (SW101)</strong><p>

表 4.3 介绍了如何使用 FWDN 轻触开关 (SW101) 选择启动模式。
<p align="center"><strong>表 4.3 用于启动模式的轻触开关 (SW101) 说明</strong></p>
<div align="center">
	<table>
	  <tr>
	    <th colspan="3"><strong>模式</strong></th>
	    <th><strong>BM00 值</strong></th>
	    <th><strong>SW101 状态</strong></th>
	  </tr>
	  <tr>
	    <td colspan="3">正常（默认）</td>
	    <td>Low (1)</td>
	    <td>默认</td>
	  </tr>
	  <tr>
	    <td colspan="3">FWDN（选配）</td>
	    <td>High (1)</td>
	    <td>按住并上电</td>
	  </tr>
	</table>
</div>
</br></br>

### 4.4.1 进入 FWDN 模式的方法
进入 FWDN 模式有以下两种方法。

#### 4.4.1.1 方法 1
在按住 FWDN 开关 (SW101) 的同时，连接 12V 电源以开启 VCP-G 开发板。  
在按住 FWDN 开关的状态下上电时，FWDN 红色指示灯点亮。松开 FWDN 开关 (SW101) 后，MCU 进入 FWDN 模式。  
图 4.4 显示了如何使用方法 1 进入 FWDN 模式。
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Hardware/4.4%20Entering%20FWDN%20Mode%20by%20Using%20Method%201.png"></p>
<p align="center"><strong>图 4.4 使用方法 1 进入 FWDN 模式</strong><p>

#### 4.4.1.2 方法 2
在 VCP-G 开发板已连接 12V 电源的状态下，按下 FWDN 开关 (SW101)，然后按下 RESET 轻触开关 (SW100)。  
在按住 FWDN 开关的状态下上电时，FWDN 红色指示灯点亮。按住 RESET 轻触开关期间，3.3V 绿色指示灯熄灭。松开 FWDN 开关 (SW101) 后，MCU 进入 FWDN 模式。  
图 4.5 显示了使用方法 2 的 FWDN 模式。

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Hardware/4.5%20Entering%20FWDN%20Mode%20by%20Using%20Method%202.png"></p>
<p align="center"><strong>图 4.5 使用方法 2 进入 FWDN 模式</strong><p>

</br></br></br>

## 4.5 RESET 轻触开关 (SW100)
---
VCP-G 有一个使用 GRESETn 引脚进行 RESET 供电的 RESET 开关。  
图 4.6 显示了 RESET 轻触开关 (SW100)。
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Hardware/4.6%20RESET%20Tact%20Switch%20(SW100).png"></p>
<p align="center"><strong>图 4.6 RESET 轻触开关 (SW100)</strong><p>
</br></br>

### 4.5.1 RESET 轻触开关 (SW100) 的功能
SW100 是用于复位 VCP-G 中电源模块和系统模块的轻触开关。  
该按钮的功能如下：
  - 在上电状态下按下 RESET 轻触开关 (SW100)，将强制复位 VCP-G 的电源模块和系统。

**重要：** 按下轻触开关时请注意，因为电源会突然关闭，数据可能会损坏。

</br></br></br>

## 4.6 用于调试和 FWDN 的连接器 (JC100)
---
JC100 是标准的 USB Type-C 连接器。在 VCP-G 上，JC100 用于通过 UART 进行调试或 FWDN。  
图 4.7 显示了 JC100 的位置。
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Hardware/4.7%20USB%20Type-C%20Connector%20(JC100).png"></p>
<p align="center"><strong>图 4.7 USB Type-C 连接器 (JC100)</strong><p>

您可以通过 JC100 执行 FWDN 或查看 VCP-G 的调试信息。
VCP-G 上的 JC100 内置了 USB-to-UART 桥接控制器，因此您可以使用 USB Type-C 线缆将 JC100 直接连接到 PC。

</br></br></br>

## 4.7 用于 GPIO、ADC、电源、CAN 和 SPI 的排针
---
VCP-G 有九个 2.54 mm 排针，用于电源、GPIO、ADC、CAN 和 SPI，以连接传感器或子板等其他外设。  

表 4.4 介绍了 VCP-G 上九个排针的用途。
<p align="center"><strong>表 4.4 VCP-G 上的排针 </strong></p>
<div align="center">
	<table>
	  <tr>
	    <td colspan="4"><strong>编号</strong></td>
	    <td><strong>参考编号</strong></td>
	    <td><strong>名称</strong></td>
	    <td><strong>说明</strong></td>
	  </tr>
	  <tr>
	    <td colspan="4">1</td>
	    <td>J18D100</td>
	    <td>36 针母排针</td>
	    <td>用于 GPIO 和 ADC 的排针</td>
	  </tr>
	  <tr>
	    <td colspan="4">2</td>
	    <td>J5D100</td>
	    <td>10 针公排针</td>
	    <td>用于 CAN 的排针</td>
	  </tr>
	  <tr>
	    <td colspan="4">3</td>
	    <td>J3D100</td>
	    <td>6 针公排针</td>
	    <td>用于 SPI 的排针</td>
	  </tr>
	  <tr>
	    <td colspan="4">4</td>
	    <td>J8D104</td>
	    <td>8 针母排针</td>
	    <td>用于 GPIO 和 ADC 的排针</td>
	  </tr>
	  <tr>
	    <td colspan="4">5</td>
	    <td>J8D102</td>
	    <td>8 针母排针</td>
	    <td>用于 GPIO 的排针</td>
	  </tr>
	  <tr>
	    <td colspan="4">6</td>
	    <td>J10D100</td>
	    <td>10 针母排针</td>
	    <td>用于 GPIO 和 ADC 的排针</td>
	  </tr>
	  <tr>
	    <td colspan="4">7</td>
	    <td>J8D100</td>
	    <td>8 针母排针</td>
	    <td>用于电源和复位的排针</td>
	  </tr>
	  <tr>
	    <td colspan="4">8</td>
	    <td>J8D101</td>
	    <td>8 针母排针</td>
	    <td>用于 GPIO 和 ADC 的排针</td>
	  </tr>
	  <tr>
	    <td colspan="4">9</td>
	    <td>J8D103</td>
	    <td>8 针母排针</td>
	    <td>用于 GPIO 和 ADC 的排针</td>
	  </tr>
	</table>
</div>

图 4.8 显示了 VCP-G 上排针的位置。
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Hardware/4.8%20Pin%20Headers%20on%20TOPST%20VCP-G%20Board.png"></p>
<p align="center"><strong>图 4.8 VCP-G 上的排针 </strong><p>

表 4.5 显示了 J10D100 的引脚说明。
<p align="center"><strong>表 4.5 J10D100 引脚说明</strong></p>
<div align="center">
	<table>
	  <tr>
	    <th rowspan="3"><strong>引脚编号</strong></th>
	    <th colspan="4"><strong>J10D100</strong></th>
	  </tr>
	  <tr>
	    <th rowspan="2"><strong>端口名称</strong></th>
	    <th rowspan="2"><strong>信号名称</strong></th>
	    <th><strong>DIR</strong></th>
	    <th rowspan="2"><strong>说明</strong></th>
	  </tr>
	  <tr>
	    <th><strong>MCU ◄► J10D100</strong></th>
	  </tr>
	  <tr>
	    <td>1</td>
	    <td>SCL</td>
	    <td>GPIO_AC07</td>
	    <td>◄►</td>
	    <td>GPIO 或 ADC 信号</td>
	  </tr>
	  <tr>
	    <td>2</td>
	    <td>SDA</td>
	    <td>GPIO_AC06</td>
	    <td>◄►</td>
	    <td>GPIO 或 ADC 信号</td>
	  </tr>
	  <tr>
	    <td>3</td>
	    <td>AREF</td>
	    <td>ADC06</td>
	    <td>◄</td>
	    <td>ADC 信号</td>
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
	    <td>GPIO 信号</td>
	  </tr>
	  <tr>
	    <td>6</td>
	    <td>12</td>
	    <td>GPIO_C15</td>
	    <td>◄►</td>
	    <td>GPIO 信号</td>
	  </tr>
	  <tr>
	    <td>7</td>
	    <td>11</td>
	    <td>GPIO_C14</td>
	    <td>◄►</td>
	    <td>GPIO 信号</td>
	  </tr>
	  <tr>
	    <td>8</td>
	    <td>10</td>
	    <td>GPIO_C13</td>
	    <td>◄►</td>
	    <td>GPIO 信号</td>
	  </tr>
	  <tr>
	    <td>9</td>
	    <td>9</td>
	    <td>GPIO_A12</td>
	    <td>◄►</td>
	    <td>GPIO 信号</td>
	  </tr>
	  <tr>
	    <td>10</td>
	    <td>8</td>
	    <td>GPIO_B00</td>
	    <td>◄►</td>
	    <td>GPIO 信号</td>
	  </tr>
	</table>
</div>

表 4.6 显示了 J8D100 的引脚说明。
<p align="center"><strong>表 4.6 J8D100 引脚说明</strong></p>
<div align="center">
	<table>
	  <tr>
	    <th rowspan="3"><strong>引脚编号</strong></th>
	    <th colspan="4"><strong>J8D100</strong></th>
	  </tr>
	  <tr>
	    <th rowspan="2"><strong>端口名称</strong></th>
	    <th rowspan="2"><strong>信号名称</strong></th>
	    <th><strong>DIR</strong></th>
	    <th rowspan="2"><strong>说明</strong></th>
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
	    <td>电源 3.3V</td>
	  </tr>
	  <tr>
	    <td>3</td>
	    <td>RST</td>
	    <td>RESET</td>
	    <td>◄</td>
	    <td>复位信号</td>
	  </tr>
	  <tr>
	    <td>4</td>
	    <td>3.3V</td>
	    <td>VCP_3P3</td>
	    <td>-</td>
	    <td>电源 3.3V</td>
	  </tr>
	  <tr>
	    <td>5</td>
	    <td>5V</td>
	    <td>VCP_5P0</td>
	    <td>-</td>
	    <td>电源 5.0V</td>
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
	    <td>VCP-G 的电压输入</td>
	  </tr>
	</table>
</div>

表 4.7 显示了 J8D101 的引脚说明。
<p align="center"><strong>表 4.7 J8D101 引脚说明</strong></p>
<div align="center">
	<table>
	  <tr>
	    <th rowspan="3"><strong>引脚编号</strong></th>
	    <th colspan="4"><strong>J8D101</strong></th>
	  </tr>
	  <tr>
	    <th rowspan="2"><strong>端口名称</strong></th>
	    <th rowspan="2"><strong>信号名称</strong></th>
	    <th><strong>DIR</strong></th>
	    <th rowspan="2"><strong>说明</strong></th>
	  </tr>
	  <tr>
	    <th><strong>MCU ◄► J8D101</strong></th>
	  </tr>
	  <tr>
	    <td>1</td>
	    <td>A0</td>
	    <td>ADC03</td>
	    <td>◄</td>
	    <td>ADC 信号</td>
	  </tr>
	  <tr>
	    <td>2</td>
	    <td>A1</td>
	    <td>ADC04</td>
	    <td>◄</td>
	    <td>ADC 信号</td>
	  </tr>
	  <tr>
	    <td>3</td>
	    <td>A2</td>
	    <td>GPIO_AC02</td>
	    <td>◄►</td>
	    <td>GPIO 信号</td>
	  </tr>
	  <tr>
	    <td>4</td>
	    <td>A3</td>
	    <td>GPIO_AC03</td>
	    <td>◄►</td>
	    <td>GPIO 信号</td>
	  </tr>
	  <tr>
	    <td>5</td>
	    <td>A4</td>
	    <td>GPIO_AC05</td>
	    <td>◄►</td>
	    <td>GPIO 信号</td>
	  </tr>
	  <tr>
	    <td>6</td>
	    <td>A5</td>
	    <td>GPIO_AC04</td>
	    <td>◄►</td>
	    <td>GPIO 信号</td>
	  </tr>
	  <tr>
	    <td>7</td>
	    <td>A6</td>
	    <td>ADC05</td>
	    <td>◄</td>
	    <td>ADC 信号</td>
	  </tr>
	  <tr>
	    <td>8</td>
	    <td>A7</td>
	    <td>ADC01</td>
	    <td>◄</td>
	    <td>ADC 信号</td>
	  </tr>
	</table>
</div>

表 4.8 显示了 J8D102 的引脚说明。
<p align="center"><strong>表 4.8 J8D102 引脚说明</strong></p>
<div align="center">
	<table>
	  <tr>
	    <th rowspan="3"><strong>引脚编号</strong></th>
	    <th colspan="4"><strong>J8D102</strong></th>
	  </tr>
	  <tr>
	    <th rowspan="2"><strong>端口名称</strong></th>
	    <th rowspan="2"><strong>信号名称</strong></th>
	    <th><strong>DIR</strong></th>
	    <th rowspan="2"><strong>说明</strong></th>
	  </tr>
	  <tr>
	    <th><strong>MCU ◄► J8D102</strong></th>
	  </tr>
	  <tr>
	    <td>1</td>
	    <td>7</td>
	    <td>GPIO_B01</td>
	    <td>◄►</td>
	    <td>GPIO 信号</td>
	  </tr>
	  <tr>
	    <td>2</td>
	    <td>6</td>
	    <td>GPIO_A13</td>
	    <td>◄►</td>
	    <td>GPIO 信号</td>
	  </tr>
	  <tr>
	    <td>3</td>
	    <td>5</td>
	    <td>GPIO_B10</td>
	    <td>◄►</td>
	    <td>GPIO 信号</td>
	  </tr>
	  <tr>
	    <td>4</td>
	    <td>4</td>
	    <td>GPIO_B27</td>
	    <td>◄►</td>
	    <td>GPIO 信号</td>
	  </tr>
	  <tr>
	    <td>5</td>
	    <td>3</td>
	    <td>GPIO_B11</td>
	    <td>◄►</td>
	    <td>GPIO 信号</td>
	  </tr>
	  <tr>
	    <td>6</td>
	    <td>2</td>
	    <td>GPIO_B28</td>
	    <td>◄►</td>
	    <td>GPIO 信号</td>
	  </tr>
	  <tr>
	    <td>7</td>
	    <td>1</td>
	    <td>GPIO_B25</td>
	    <td>◄►</td>
	    <td>GPIO 信号</td>
	  </tr>
	  <tr>
	    <td>8</td>
	    <td>0</td>
	    <td>GPIO_B26</td>
	    <td>◄►</td>
	    <td>GPIO 信号</td>
	  </tr>
	</table>
</div>

表 4.9 显示了 J8D103 的引脚说明。
<p align="center"><strong>表 4.9 J8D103 引脚说明</strong></p>
<div align="center">
	<table>
	  <tr>
	    <th rowspan="3"><strong>引脚编号</strong></th>
	    <th colspan="4"><strong>J8D103</strong></th>
	  </tr>
	  <tr>
	    <th rowspan="2"><strong>端口名称</strong></th>
	    <th rowspan="2"><strong>信号名称</strong></th>
	    <th><strong>DIR</strong></th>
	    <th rowspan="2"><strong>说明</strong></th>
	  </tr>
	  <tr>
	    <th><strong>MCU ◄► J8D103</strong></th>
	  </tr>
	  <tr>
	    <td>1</td>
	    <td>A8</td>
	    <td>GPIO_AC08</td>
	    <td>◄►</td>
	    <td>GPIO 或 ADC 信号</td>
	  </tr>
	  <tr>
	    <td>2</td>
	    <td>A9</td>
	    <td>GPIO_AC09</td>
	    <td>◄►</td>
	    <td>GPIO 或 ADC 信号</td>
	  </tr>
	  <tr>
	    <td>3</td>
	    <td>A10</td>
	    <td>GPIO_AC10</td>
	    <td>◄►</td>
	    <td>GPIO 或 ADC 信号</td>
	  </tr>
	  <tr>
	    <td>4</td>
	    <td>A11</td>
	    <td>GPIO_ADC-2</td>
	    <td>◄</td>
	    <td>ADC 信号</td>
	  </tr>
	  <tr>
	    <td>5</td>
	    <td>54</td>
	    <td>GPIO_K14</td>
	    <td>◄►</td>
	    <td>GPIO 信号</td>
	  </tr>
	  <tr>
	    <td>6</td>
	    <td>55</td>
	    <td>GPIO_K15</td>
	    <td>◄►</td>
	    <td>GPIO 信号</td>
	  </tr>
	  <tr>
	    <td>7</td>
	    <td>56</td>
	    <td>GPIO_K01</td>
	    <td>◄</td>
	    <td>GPIO 信号</td>
	  </tr>
	  <tr>
	    <td>8</td>
	    <td>57</td>
	    <td>GPIO_K08</td>
	    <td>◄►</td>
	    <td>GPIO 信号</td>
	  </tr>
	</table>
</div>

表 4.10 显示了 J8D104 的引脚说明。
<p align="center"><strong>表 4.10 J8D104 引脚说明</strong></p>
<div align="center">
	<table>
	  <tr>
	    <th rowspan="3"><strong>引脚编号</strong></th>
	    <th colspan="4"><strong>J8D104</strong></th>
	  </tr>
	  <tr>
	    <th rowspan="2"><strong>端口名称</strong></th>
	    <th rowspan="2"><strong>信号名称</strong></th>
	    <th><strong>DIR</strong></th>
	    <th rowspan="2"><strong>说明</strong></th>
	  </tr>
	  <tr>
	    <th><strong>MCU ◄► J8D104</strong></th>
	  </tr>
	  <tr>
	    <td>1</td>
	    <td>14</td>
	    <td>GPIO_AC00</td>
	    <td>◄►</td>
	    <td>GPIO 或 ADC 信号</td>
	  </tr>
	  <tr>
	    <td>2</td>
	    <td>15</td>
	    <td>GPIO_AC01</td>
	    <td>◄►</td>
	    <td>GPIO 或 ADC 信号</td>
	  </tr>
	  <tr>
	    <td>3</td>
	    <td>16</td>
	    <td>GPIO_A06</td>
	    <td>◄►</td>
	    <td>GPIO 信号</td>
	  </tr>
	  <tr>
	    <td>4</td>
	    <td>17</td>
	    <td>GPIO_A07</td>
		<td>◄►</td>
	    <td>GPIO 信号</td>
	  </tr>
	  <tr>
	    <td>5</td>
	    <td>18</td>
	    <td>GPIO_A28</td>
	    <td>◄►</td>
	    <td>GPIO 信号</td>
	  </tr>
	  <tr>
	    <td>6</td>
	    <td>19</td>
	    <td>GPIO_A29</td>
	    <td>◄►</td>
	    <td>GPIO 信号</td>
	  </tr>
	  <tr>
	    <td>7</td>
	    <td>20</td>
	    <td>GPIO_B03</td>
	    <td>◄►</td>
	    <td>GPIO 信号</td>
	  </tr>
	  <tr>
	    <td>8</td>
	    <td>21</td>
	    <td>GPIO_B02</td>
	    <td>◄►</td>
	    <td>GPIO 信号</td>
	  </tr>
	</table>
</div>

表 4.11 显示了 J3D100 的引脚说明。
<p align="center"><strong>表 4.11 J3D100 引脚说明</strong></p>
<div align="center">
	<table>
	  <tr>
	    <th rowspan="3"><strong>引脚编号</strong></th>
	    <th colspan="4"><strong>J3D100</strong></th>
	  </tr>
	  <tr>
	    <th rowspan="2"><strong>端口名称</strong></th>
	    <th rowspan="2"><strong>信号名称</strong></th>
	    <th><strong>DIR</strong></th>
	    <th rowspan="2"><strong>说明</strong></th>
	  </tr>
	  <tr>
	    <th><strong>MCU ◄► J3D100</strong></th>
	  </tr>
	  <tr>
	    <td>1</td>
	    <td>MISO</td>
	    <td>GPIO_B07</td>
	    <td>◄►</td>
	    <td>GPIO 信号</td>
	  </tr>
	  <tr>
	    <td>2</td>
	    <td>5V</td>
	    <td>VCP_5P0</td>
	    <td>-</td>
	    <td>电源 5.0V</td>
	  </tr>
	  <tr>
	    <td>3</td>
	    <td>SCK</td>
	    <td>GPIO_B04</td>
	    <td>◄►</td>
	    <td>GPIO 信号</td>
	  </tr>
	  <tr>
	    <td>4</td>
	    <td>MOSI</td>
	    <td>GPIO_B06</td>
	    <td>◄►</td>
	    <td>GPIO 信号</td>
	  </tr>
	  <tr>
	    <td>5</td>
	    <td>CMD</td>
	    <td>GPIO_B05</td>
	    <td>◄►</td>
	    <td>GPIO 信号</td>
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

表 4.12 显示了 J18D100 的引脚说明。
<p align="center"><strong>表 4.12 J18D100 引脚说明</strong></p>
<div align="center">
	<table>
	  <tr>
	    <th rowspan="3"><strong>引脚编号</strong></th>
	    <th colspan="4"><strong>J18D100</strong></th>
	  </tr>
	  <tr>
	    <th rowspan="2"><strong>端口名称</strong></th>
	    <th rowspan="2"><strong>信号名称</strong></th>
	    <th><strong>DIR</strong></th>
	    <th rowspan="2"><strong>说明</strong></th>
	  </tr>
	  <tr>
	    <th><strong>MCU ◄► J18D100</strong></th>
	  </tr>
	  <tr>
	    <td>1</td>
	    <td>5V</td>
	    <td>VCP_5P0</td>
	    <td>-</td>
	    <td>电源 5.0V</td>
	  </tr>
	  <tr>
	    <td>2</td>
	   <td>5V</td>
	    <td>VCP_5P0</td>
	    <td>-</td>
	    <td>电源 5.0V</td>
	  </tr>
	  <tr>
	    <td>3</td>
	    <td>22</td>
	    <td>GPIO_B24</td>
	    <td>◄►</td>
	    <td>GPIO 信号</td>
	  </tr>
	  <tr>
	    <td>4</td>
	    <td>23</td>
	    <td>GPIO_B23</td>
	    <td>◄►</td>
	    <td>GPIO 信号</td>
	  </tr>
	  <tr>
	    <td>5</td>
	    <td>24</td>
	    <td>GPIO_B22</td>
	    <td>◄►</td>
	    <td>GPIO 信号</td>
	  </tr>
	  <tr>
	    <td>6</td>
	    <td>25</td>
	    <td>GPIO_B21</td>
	    <td>◄►</td>
	    <td>GPIO 信号</td>
	  </tr>
	  <tr>
	    <td>7</td>
	    <td>26</td>
	    <td>GPIO_B20</td>
	    <td>◄►</td>
	    <td>GPIO 信号</td>
	  </tr>
	  <tr>
	    <td>8</td>
	    <td>27</td>
	    <td>GPIO_B19</td>
	    <td>◄►</td>
	    <td>GPIO 信号</td>
	  </tr>
	  <tr>
	    <td>9</td>
	    <td>28</td>
	    <td>GPIO_A30</td>
	    <td>◄►</td>
	    <td>GPIO 信号</td>
	  </tr>
	  <tr>
	    <td>10</td>
	    <td>29</td>
	    <td>GPIO_A27</td>
	    <td>◄►</td>
	    <td>GPIO 信号</td>
	  </tr>
	  <tr>
	    <td>11</td>
	    <td>230</td>
	    <td>GPIO_A26</td>
	    <td>◄►</td>
	    <td>GPIO 信号</td>
	  </tr>
	  <tr>
	    <td>12</td>
	    <td>31</td>
	    <td>GPIO_A24</td>
	    <td>◄►</td>
	    <td>GPIO 信号</td>
	  </tr>
	  <tr>
	    <td>13</td>
	    <td>32</td>
	    <td>GPIO_A25</td>
	    <td>◄►</td>
	    <td>GPIO 信号</td>
	  </tr>
	  <tr>
	    <td>14</td>
	    <td>33</td>
	    <td>GPIO_A23</td>
	    <td>◄►</td>
	    <td>GPIO 信号</td>
	  </tr>
	  <tr>
	    <td>15</td>
	    <td>34</td>
	    <td>GPIO_A22</td>
	    <td>◄►</td>
	    <td>GPIO 信号</td>
	  </tr>
	  <tr>
	    <td>16</td>
	    <td>35</td>
	    <td>GPIO_A21</td>
	    <td>◄►</td>
		<td>GPIO 信号</td>
	  </tr>
	  <tr>
	    <td>17</td>
	    <td>36</td>
	    <td>GPIO_A20</td>
	    <td>◄►</td>
	    <td>GPIO 信号</td>
	  </tr>
	  <tr>
	    <td>18</td>
	    <td>37</td>
	    <td>GPIO_A19</td>
	    <td>◄►</td>
	    <td>GPIO 信号</td>
	  </tr>
	  <tr>
	    <td>19</td>
	    <td>38</td>
	    <td>GPIO_K13</td>
	    <td>◄►</td>
		<td>GPIO 信号</td>
	  </tr>
	  <tr>
	    <td>20</td>
	    <td>39</td>
	    <td>GPIO_K12</td>
	    <td>◄►</td>
	    <td>GPIO 信号</td>
	  </tr>
	  <tr>
	    <td>21</td>
	    <td>40</td>
	    <td>GPIO_K11</td>
	    <td>◄►</td>
	    <td>GPIO 信号</td>
	  </tr>
	  <tr>
	    <td>22</td>
	    <td>41</td>
	    <td>GPIO_A18</td>
	    <td>◄►</td>
	    <td>GPIO 信号</td>
	  </tr>
	  <tr>
	    <td>23</td>
	    <td>42</td>
	    <td>GPIO_A17</td>
	    <td>◄►</td>
	    <td>GPIO 信号</td>
	  </tr>
	  <tr>
	    <td>24</td>
	    <td>43</td>
	    <td>GPIO_A16</td>
	    <td>◄►</td>
	    <td>GPIO 信号</td>
	  </tr>
	  <tr>
	    <td>25</td>
	    <td>44</td>
	    <td>GPIO_A11</td>
	    <td>◄►</td>
	    <td>GPIO 信号</td>
	  </tr>
	  <tr>
	    <td>26</td>
	    <td>45</td>
	    <td>GPIO_A10</td>
	    <td>◄►</td>
	    <td>GPIO 信号</td>
	  </tr>
	  <tr>
	    <td>27</td>
	    <td>46</td>
	    <td>GPIO_A09</td>
	    <td>◄►</td>
	    <td>GPIO 信号</td>
	  </tr>
	  <tr>
	    <td>28</td>
	    <td>47</td>
	    <td>GPIO_A08</td>
	    <td>◄►</td>
	    <td>GPIO 信号</td>
	  </tr>
	  <tr>
	    <td>29</td>
	    <td>48</td>
	    <td>GPIO_A05</td>
	    <td>◄►</td>
	    <td>GPIO 信号</td>
	  </tr>
	  <tr>
	    <td>30</td>
	    <td>49</td>
	    <td>GPIO_A04</td>
	    <td>◄►</td>
	    <td>GPIO 信号</td>
	  </tr>
	  <tr>
	    <td>31</td>
	    <td>50</td>
	    <td>GPIO_A03</td>
	    <td>◄►</td>
	    <td>GPIO 信号</td>
	  </tr>
	  <tr>
	    <td>32</td>
	    <td>51</td>
	    <td>GPIO_A02</td>
	    <td>◄►</td>
	    <td>GPIO 信号</td>
	  </tr>
	  <tr>
	    <td>33</td>
	    <td>52</td>
	    <td>GPIO_A01</td>
	    <td>◄►</td>
	    <td>GPIO 信号</td>
	  </tr>
	  <tr>
	    <td>34</td>
	    <td>53</td>
	    <td>GPIO_A00</td>
	    <td>◄►</td>
	    <td>GPIO 信号</td>
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

表 4.13 显示了 J5D100 的引脚说明。
<p align="center"><strong>表 4.13 J5D100 引脚说明</strong></p>
<div align="center">
	<table>
	  <tr>
	    <th rowspan="3"><strong>引脚编号</strong></th>
	    <th colspan="4"><strong>J5D100</strong></th>
	  </tr>
	  <tr>
	    <th rowspan="2"><strong>端口名称</strong></th>
	    <th rowspan="2"><strong>信号名称</strong></th>
	    <th><strong>DIR</strong></th>
	    <th rowspan="2"><strong>说明</strong></th>
	  </tr>
	  <tr>
	    <th><strong>MCU ◄► J5D100</strong></th>
	  </tr>
	  <tr>
	    <td>1</td>
	    <td>3.3V</td>
	    <td>VCP_3P3</td>
	    <td>-</td>
	    <td>电源 3.3V</td>
	  </tr>
	  <tr>
	    <td>2</td>
	    <td>3.3V</td>
	    <td>VCP_3P3</td>
	    <td>-</td>
    <td>电源 3.3V</td>
	  </tr>
	  <tr>
	    <td>3</td>
	    <td>TX0</td>
	    <td>GPIO_K08</td>
	    <td>◄►</td>
	    <td>GPIO 信号</td>
	  </tr>
	  <tr>
	    <td>4</td>
	    <td>RX0</td>
	    <td>GPIO_K01</td>
	    <td>◄</td>
	    <td>GPIO 信号</td>
	  </tr>
	  <tr>
	    <td>5</td>
	    <td>TX1</td>
	    <td>GPIO_K09</td>
	    <td>◄►</td>
	    <td>GPIO 信号</td>
	  </tr>
	  <tr>
	    <td>6</td>
	    <td>RX1</td>
	    <td>GPIO_K02</td>
	    <td>◄</td>
	    <td>GPIO 信号</td>
	  </tr>
	  <tr>
	    <td>7</td>
	    <td>TX2</td>
	    <td>GPIO_K10</td>
	    <td>◄►</td>
	    <td>GPIO 信号</td>
	  </tr>
	  <tr>
	    <td>8</td>
	    <td>RX2</td>
	    <td>GPIO_K03</td>
	    <td>◄</td>
	    <td>GPIO 信号</td>
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

图 4.9 显示了 VCP-G 上十个排针的全部引脚分配。
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Hardware/4.9%20Total%20Pin%20Assignment%20of%20Pin%20Headers%20on%20TOPST%20VCP-G%20Board.png"></p>
<p align="center"><strong>图 4.9 VCP-G 上排针的全部引脚分配 </strong><p>

# 参考资料
  - 如需更多详细信息，请联系 TOPST：topst@topst.ai

**注意：** 参考文档可根据合同条款在可提供时提供。如果无法提供参考文档，则可以就与您的开发直接相关的内容进行指导。
