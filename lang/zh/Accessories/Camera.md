## 支持的摄像头模块
<div align="center">
    <table>
        <tr>
            <td colspan="8" align="center"><strong>开发板</strong></td>
            <td align="center"><strong>型号</strong></td>
            <td align="center"><strong>传感器</strong></td>
            <td align="center"><strong>传感器分辨率</strong></td>
            <td align="center"><strong>默认分辨率</strong></td>
            <td align="center"><strong>帧率</strong></td>
            <td align="center"><strong>默认视频路径</strong></td>
            <td align="center"><strong>备注</strong></td>
        </tr>
        <tr>
            <td rowspan="4" align="center"><strong>D3-G</strong></td>
            <td colspan="8">Arducam OV5647</td>
            <td>OV5647</td>
            <td>2592x1944 像素(5MP)</td>
            <td>1296x972</td>
            <td>30FPS</td>
            <td>/dev/video0</td>
            <td>默认选择的摄像头</td>
        </tr>
        <tr>
            <td colspan="8">Raspberry Pi Camera v1</td>
            <td>OV5647</td>
            <td>2592x1944 像素(5MP)</td>
            <td>1296x972</td>
            <td>30FPS</td>
            <td>/dev/video0</td>
            <td>默认选择的摄像头</td>
        </tr>
        <tr>
            <td colspan="8">Raspberry Pi Camera v2</td>
            <td>IMX219</td>
            <td>3280x2464 像素(8MP)</td>
            <td>1640x1232</td>
            <td>30FPS</td>
            <td>/dev/video0</td>
            <td>默认禁用。请参阅下方指南以启用。</td>
        </tr>
        <tr>
            <td colspan="8">SEKONIX CXD5700</td>
            <td>CXD5700</td>
            <td>1920x1080 像素(2MP)</td>
            <td>1920x1080</td>
            <td>30FPS</td>
            <td>/dev/video0,1,2,3</td>
            <td>默认禁用。请参阅下方指南以启用。</td>
        </tr>
        <tr>
            <td rowspan="4" align="center"><strong>AI-G</strong></td>
            <td colspan="8">Arducam OV5647</td>
            <td>OV5647</td>
            <td>2592x1944 像素(5MP)</td>
            <td>1296x972</td>
            <td>30FPS</td>
            <td>/dev/video2</td>
            <td>默认选择的摄像头</td>
        </tr>
        <tr>
            <td colspan="8">Raspberry Pi Camera v1</td>
            <td>OV5647</td>
            <td>2592x1944 像素(5MP)</td>
            <td>1296x972</td>
            <td>30FPS</td>
            <td>/dev/video2</td>
            <td>默认选择的摄像头</td>
        </tr>
        <tr>
            <td colspan="8">Raspberry Pi Camera v2</td>
            <td>IMX219</td>
            <td>3280x2464 像素(8MP)</td>
            <td>1640x1232</td>
            <td>30FPS</td>
            <td>/dev/video2</td>
            <td>默认禁用。请参阅下方指南以启用。</td>
        </tr>
        <tr>
            <td colspan="8">SEKONIX CXD5700</td>
            <td>CXD5700</td>
            <td>1920x1080 像素(2MP)</td>
            <td>1920x1080</td>
            <td>30FPS</td>
            <td>/dev/video0,1,2</td>
            <td>默认禁用。请参阅下方指南以启用。</td>
        </tr>
    </table>
</div>

# 1. 简介
本指南旨在帮助工程师在 TOPST D3-G 与 AI-G 平台上快速启用摄像头输入，并针对 AI 视觉工作负载执行快速的初步验证。其目标是降低初始设置的复杂度，包括硬件连接、设备树配置、驱动程序和管线准备，并提供一条清晰、可复现的路径，从上电到获取第一帧视频，直至完成第一次推理。

## 1.1 适用范围
- **支持的接口：** MIPI CSI-2、GMSL（基于 SerDes）、USB UVC
- **软件组件：** 基于 Yocto 的 BSP 配置、设备树覆盖（overlay）、V4L2、GStreamer、OpenCV，以及与 D3-G 和 AI-G SDK 的集成
- **适用场景：** 机器人、无人机，以及检测、安全监控和目标跟踪等工业自动化应用
- **不在范围内的内容：** 摄像头 ISP 调优、高级标定流程（立体/IMU）以及完整的端到端应用框架

## 1.2 目标读者
- 为 PoC 或试点开发将摄像头集成到 D3-G 或 AI-G 平台的嵌入式与 AI 工程师
- 部署或验证依赖多摄像头管线的系统的系统集成商
- 需要可重复的动手实践环境以进行培训和实验的教育工作者与实验室用户

## 1.3 本指南的结构
- **硬件连接：** 连接器引脚定义、通道配置、电源与接地要求、线缆操作准则以及参考接线图
- **软件配置：** 包括驱动程序和设备树配置在内的 BSP 设置，以及通过 udev 和 V4L2 验证设备的方法
- **管线与示例：** 用于单摄像头和多摄像头预览与采集的 GStreamer 和 OpenCV 命令与脚本
- **故障排查：** 常见问题、典型 dmesg 模式、I²C 探测技巧、时序相关问题以及性能验证方法

## 1.4 前提条件
- **硬件：** TOPST D3-G 或 AI-G 开发板、受支持的摄像头模块，以及所需的线缆/适配器（MIPI FPC、用于 GMSL 的同轴线缆、USB 3.0 等）
- **主机工具：** 串口控制台访问、SSH 客户端以及基本的构建/调试工具
- **技术背景：** 熟悉 Linux shell 操作、V4L2 工具以及设备树的基本概念
- **镜像/SDK：** D3-G、AI-G BSP 镜像（d3-g 版本 ≥ v1.3.0，ai-g 版本 ≥1.1.0）
  

# 2. 摄像头接口概述
第 2 章分别介绍 D3-G 和 AI-G 开发板所支持的摄像头类型。  
表 2.1 给出了 D3-G 和 AI-G 平台的开发板支持矩阵。

<p align="center"><strong>表 2.1 开发板支持矩阵</strong></p>
<div align="center">
    <table>
        <tr>
            <td colspan="3" align="center"><strong>项目</strong></td>
            <td align="center"><strong>D3-G</strong></td>
            <td align="center"><strong>AI-G</strong></td>
        </tr>
        <tr>
            <td colspan="3">OS 支持</td>
            <td>Yocto, Ubuntu(desktop)</td>
            <td>Yocto, Ubuntu(Headless)</td>
        </tr>
        <tr>
            <td colspan="3">MIPI CSI-2</td>
            <td>2-4 通道，2.1 Gbps/通道 x2</td>
            <td>2-4 通道，1.5 Gbps/通道 x1</td>
        </tr>
        <tr>
            <td colspan="3">GMSL (SerDes)</td>
            <td>TOPST 4ch SerDes 转接板</td>
            <td>TOPST 4ch SerDes 转接板</td>
        </tr>
        <tr>
            <td colspan="3">USB (UVC)</td>
            <td>USB2.0/USB3.0 </td>
            <td>不支持</td>
        </tr>
    </table>
</div>

## 2.1 MIPI 摄像头概述
MIPI 摄像头是一种基于图像传感器的摄像头模块，通过 **MIPI CSI-2（Mobile Industry Processor Interface – Camera Serial Interface 2）** 标准直接连接到处理器。它是智能手机、嵌入式开发板和基于 AI 的摄像头系统中应用最广泛的摄像头接口，具有低功耗、高带宽和低延迟等优势。  
MIPI CSI-2 摄像头通常将 RAW Bayer 传感器输出直接提供给系统，图像信号处理（ISP）由 SoC 内部 ISP 或外部 ISP 完成。与 USB 摄像头不同，MIPI 传感器需要通过 I2C 寄存器配置进行初始化并设置 ISP 管线，但作为回报，它们能够充分发挥传感器性能，实现高质量的图像处理。  
MIPI 摄像头在嵌入式平台中被广泛使用，原因如下：
- **高带宽：** 借助 2 通道或 4 通道配置，MIPI 摄像头可以可靠地传输高分辨率（4K 及以上）和高帧率数据。
- **低功耗：** 专为移动和嵌入式设备设计，功耗显著低于其他方案。
- **直接控制传感器：** 曝光、增益和帧率等传感器参数可通过 I2C 进行控制，从而实现精细的画质调整。
- **低延迟：** 由于 RAW 数据被直接传输，MIPI 摄像头适用于机器人和嵌入式视觉系统等实时应用。
- **传感器选择广泛：** 包括 Sony IMX 系列（IMX219、IMX708 等）和 Omnivision OV 系列在内的众多传感器均可在同一 CSI-2 标准下使用。  

MIPI 摄像头使用 **15 针（2 通道）** 或 **20 针（4 通道）** FFC 线缆等连接器，通道配置和引脚映射必须与开发板的 CSI 端口相匹配。  
在基于 Linux 的系统上，必须正确设置传感器驱动程序（包括设备树配置），摄像头才能被识别为 /dev/video* 设备或 Media Controller 节点。识别后即可通过 V4L2 框架访问视频流。  
由于这些特性，MIPI 摄像头已成为高质量图像处理、低延迟流传输以及 AI 驱动的嵌入式视觉应用事实上的标准接口。

## 2.2 GMSL 摄像头概述
GMSL 摄像头是一种串行化摄像头模块，采用 Gigabit Multimedia Serial Link（GMSL）标准，通过单根同轴线缆或屏蔽双绞线传输图像数据、控制信号和电源。与需要短距离 FFC 连接的 MIPI 摄像头不同，GMSL 使用串行器–解串器（SerDes）对将 CSI-2 图像数据传输数米之远，从而实现远距离且抗噪声的摄像头集成。  

GMSL 系统在嵌入式和车载环境中具有多项优势：
- **远距离传输：** 支持在长达约 15 m 的线缆上可靠传输视频，适合机器人和车辆传感器布置。
- **高带宽：** GMSL1/2/3 可承载多千兆位的 CSI-2 数据流，支持高分辨率或多摄像头配置。
- **同轴供电（PoC）：** 通过单根线缆同时传输电源和数据，减少连接器数量并简化系统布线。
- **稳健性与抗 EMI 能力：** 同轴线缆和差分信号使 GMSL 在电气噪声较大的环境中保持稳定。
- **标准的传感器控制：** 解串器将 I2C 通信转发至传感器，从而实现常规的曝光、增益和帧率配置。

典型的 GMSL 摄像头链路包括带串行器的图像传感器、同轴电缆、解串器，最后是输出到 SoC 的 CSI-2 接口。在 Linux 上，只要 SerDes 和传感器在设备树中被正确描述，摄像头就会以 V4L2 或 Media Controller 设备的形式出现，这与标准 MIPI 摄像头非常相似，但在布置位置和系统设计方面具有更高的灵活性

## 2.3 USB 摄像头概述
USB 摄像头是一种通过 USB 2.0 或 USB 3.0 接口连接到系统的数字成像设备。其主要优势在于它遵循标准的 UVC (USB Video Class) 协议，因此无需专用驱动程序即可工作。由于 Linux、Windows 和 macOS 等大多数操作系统原生支持 UVC，用户在插入摄像头后即可立即获取视频流，无需任何额外配置。
  
USB 摄像头因以下原因在嵌入式平台中被广泛使用：
- **即插即用能力：** 与 MIPI 传感器不同，USB 摄像头不需要传感器初始化、I2C 寄存器配置或 ISP 流水线设置；连接后即可立即采集视频。
- **高兼容性：** 大多数 USB 摄像头遵循 UVC 规格，因此无论厂商或型号如何，都以一致的方式工作。
- **丰富的分辨率和格式支持：** MJPEG、YUYV 和 NV12 等常见格式均可广泛使用。
- **连接和布线简便：** USB 线缆可简化布线，并支持通常达数米的较长距离。
- **适合嵌入式开发：** 驱动程序相关问题较少，可实现更快速的原型开发。

在基于 Linux 的系统中，USB 摄像头会被自动检测并以 /dev/video* 节点的形式提供。可以使用 v4l2-ctl、ffmpeg 和 GStreamer 等标准工具进行视频采集和控制。  
许多 USB 摄像头内置 ISP，可在内部完成图像处理，例如自动白平衡、自动曝光和色彩校正。这使得即使在没有外部 ISP 的开发板上也能获得稳定的图像质量。由于这些特性，USB 摄像头已成为测试、嵌入式 Linux 开发、机器人技术和快速原型开发等领域中最简单、最通用的摄像头方案之一。

## 2.4 D3-G 上可用的摄像头类型
TOPST D3-G 平台在 Yocto 和 Ubuntu 环境中支持相同的摄像头类型。可用的摄像头接口包括 USB、MIPI、GMSL，具体配置会因所使用的接口而略有差异。  
1. **MIPI 摄像头**  
TOPST D3-G 提供两个 MIPI CSI 端口，每个端口可连接一个 MIPI 摄像头。MIPI CSI 接口支持两种连接器形式：
    - **15-pin(2-Lane)：** 适用于 OV5647 或 IMX219 等较低带宽的传感器。
    - **20-pin (4-Lane)：** 适用于高分辨率或高帧率传感器。
2. **GMSL 摄像头**  
GMSL 摄像头支持长距离传输，常用于汽车和工业应用。要在 TOPST D3-G 上使用 GMSL，需要以下组件：
    1. 将 **20-pin MIPI CSI (4-Lane)** 端口连接到 **TOPST MIPI Gender Board**。
    2. 将 **Deserializer (Des)** 板安装到 Gender Board 上。
    3. 使用 Fakra 线缆将最多四个 GMSL 摄像头连接到 Des 板。
3. **USB 摄像头**  
USB 摄像头提供了最简单的入门方式。连接到开发板上任意 USB 2.0 或 USB 3.0 端口后，即可被自动识别，无需额外配置即可使用。  
如果该设备是兼容 V4L2 的 UVC 摄像头，可使用以下命令确认其是否被检测到：  
    ``` 
    v4l2-ctl --list-devices
    ```

## 2.4 D3-G 上可用的摄像头类型
TOPST AI-G 平台同样支持多种摄像头输入接口，但整体配置比 D3-G 更为简单，并针对高性能 AI 工作负载进行了优化。需要注意的是，该平台不支持 USB 摄像头，仅提供 MIPI、GMSL 输入。  
1. **MIPI 摄像头**  
TOPST D3-G 提供两个 MIPI CSI 端口，每个端口可连接一个 MIPI 摄像头。MIPI CSI 接口支持两种连接器形式：
    - **15-pin(2-Lane)：** 适用于 OV5647 或 IMX219 等较低带宽的传感器。
    - **20-pin (4-Lane)：** 适用于高分辨率或高帧率传感器。
2. **GMSL 摄像头**  
GMSL 摄像头支持长距离传输，常用于汽车和工业应用。要在 TOPST D3-G 上使用 GMSL，需要以下组件：
    1. 将 **20-pin MIPI CSI (4-Lane)** 端口连接到 **TOPST MIPI Gender Board**。
    2. 将 **Deserializer (Des)** 板安装到 Gender Board 上。
    3. 使用 Fakra 线缆将最多四个 GMSL 摄像头连接到 Des 板。

# 3. 摄像头连接指南
第 3 章说明如何将摄像头连接到 D3-G 和 AI-G 开发板。  
本节用于确保开发板与摄像头正确连接，以使摄像头能够可靠工作。请按照以下指南连接您要使用的摄像头。

## 3.1 将摄像头连接到 D3-G
有关如何将 MIPI CSI-2、GMSL 和 USB 摄像头连接到 D3-G 的说明，请遵循以下指南。  

### 3.1.1 MIPI CSI-2 摄像头
图 3.1 显示了 D3-G 上的 MIPI CSI 连接器。D3-G 支持 2 通道 MIPI CSI，每个通道配置为 2-lane 接口。4-lane 接口为可选项，需要使用 20-pin 连接器而非 15-pin 连接器。有关引脚的信息，请参阅 D3-G Hardware-User Guide。

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/accessories/Camera/3.1%20MIPI%20CSI%20Connector%20on%20D3-G.png"></p>
<p align="center"><strong>图 3.1 D3-G 上的 MIPI CSI 连接器</strong></p>

连接 MIPI 摄像头时，请使用 FFC (Flat Flexible Cable)。有关正确的线缆类型和方向，请参阅图 3.2 和 3.3。

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/accessories/Camera/3.2%20FFC%20Type.png"></p>
<p align="center"><strong>图 3.2 FFC 类型</strong></p>

FFC 线缆为 1.0 mm、15-pin 类型，其中一面必须有不同颜色的标记（蓝色或灰色）。线缆应按 B-Forward Direction 方向插入。有关 FFC 类型，请参阅图 3.2。

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/accessories/Camera/3.3%20An%20example%20of%20an%20FFC%20connected%20to%20the%20D3-G%20MIPI0%2015-pin%20Connector.png"></p>
<p align="center"><strong>图 3.3 将 FFC 连接到 D3-G MIPI0 15-pin 连接器的示例</strong></p>

请确保 FFC 上的 15 个银色触点与 D3-G MIPI 连接器内部的 15 个银色触点对齐。  
使用 MIPI1 连接器时适用相同的连接方法；请按照与 MIPI0 连接器相同的方式进行连接。

### 3.1.2 GMSL 摄像头
GMSL 摄像头使用 Fakra 线缆，因此无法直接连接到 D3-G 开发板。它们必须先通过 Deserializer (Des) 板和 TOPST MIPI Gender Board，然后再与 D3-G 对接。  
连接结构如下。  

<p align="center"><strong>< D3-G > ↔ < TOPST MIPI Gender Board > ↔ < Des Board > ↔ < GMSL Camera ></strong></p>

GMSL 摄像头需要使用 TOPST MIPI Gender Board，并且必须通过 20-pin MIPI 连接器进行连接。例如，如果您计划使用四个 GMSL 摄像头，则必须如图 3.4 所示使用 20-pin MIPI 接口进行连接。

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/accessories/Camera/3.4%2020-pin%20MIPI0%20Connector.png"></p>
<p align="center"><strong>图 3.4 20-pin MIPI0 连接器</strong></p>  

1. 将 D3-G 开发板连接到 TOPST MIPI Gender Board。  
    FFC 线缆为 1.0 mm、20-pin 类型，其中一面必须有不同颜色的标记（蓝色或灰色）。线缆应按 A-Forward Direction 方向插入。有关 FFC 类型，请参阅图 3.5。  
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/accessories/Camera/3.2%20FFC%20Type.png"></p>
    <p align="center"><strong>图 3.5 FFC 类型</strong></p>
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/accessories/Camera/3.6%20Anexample%20of%20an%20FFC%20connected%20to%20the%20D3-G%20MIPI0%2020-pin%20Connector.png"></p>
    <p align="center"><strong>图 3.6 将 FFC 连接到 D3-G MIPI0 20-pin 连接器的示例</strong></p> 
    请确保 FFC 上的 20 个银色触点与 D3-G MIPI 连接器内部的 20 个银色触点对齐
    使用 MIPI1 连接器时适用相同的连接方法；请按照与 MIPI0 连接器相同的方式进行连接。
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/accessories/Camera/3.7%20An%20example%20of%20an%20FFC%20connected%20th%20toe%20TOPST%20MIPI%20Gender%20Board%20MIPI%20Connector.png"></p>
    <p align="center"><strong>图 3.7 将 FFC 连接到 TOPST MIPI Gender Board MIPI 连接器的示例</strong></p>
2. 将 Deserializer 板连接到 MIPI Gender Board。  
    将 MIPI Gender Board 上的 JH2 连接器安装到 SerDes 板底面的 JH1 连接器上。
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/accessories/Camera/3.8%20JH2%20Connector.png"></p>
    <p align="center"><strong>图 3.8 JH2 连接器</strong></p>
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/accessories/Camera/3.9%20JH1%20Connector.png"></p>
    <p align="center"><strong>图 3.9 JH1 连接器</strong></p>
3. GMSL 摄像头连接
    请如图 3.10 所示连接摄像头。该图以两个摄像头为例，但您可以根据需要连接一到四个摄像头。
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/accessories/Camera/3.10%20GMSL%20Camera%20Connection.png"></p>
    <p align="center"><strong>图 3.10 JH2 连接器</strong></p>

### 3.1.3 USB 摄像头
USB 摄像头可通过连接到 D3-G 上的 USB 2.0 或 USB 3.0 端口来使用。当使用需要 USB 3.0 规格的 USB 摄像头时，请务必将其连接到 USB 3.0 端口。

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/accessories/Camera/3.11%20USB%20Camera%20Connection.png"></p>
<p align="center"><strong>图 3.11 USB 摄像头连接</strong></p>

## 3.2 将摄像头连接到 AI-G
### 3.2.1 MIPI CSI-2 摄像头
图 3.12 显示了 AI-G 上的 MIPI CSI 连接器。AI-G 支持 2 通道 MIPI CSI，每个通道配置为 2-lane 接口。

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/accessories/Camera/3.12%20MIPI%20CSI%20Connector%20on%20AI-G.png"></p>
<p align="center"><strong>图 3.12 AI-G 上的 MIPI CSI 连接器</strong></p>

连接 MIPI 摄像头时，请使用 FFC（Flat Flexible Cable）。有关正确的线缆类型和方向，请参见图 3.13 和 3.14。

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/accessories/Camera/3.2%20FFC%20Type.png"></p>
<p align="center"><strong>图 3.13 FFC 类型</strong></p>

FFC 线缆为 1.0 mm、15 针类型，其中一面必须带有不同颜色的标记（蓝色或灰色）。线缆应按 B-Forward Direction 方向插入。有关 FFC 类型，请参见图 3.13。

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/accessories/Camera/3.14%20An%20example%20of%20an%20FFC%20connected%20to%20the%20AI-G%20MIPI%2015-pin%20Connector.png"></p>
<p align="center"><strong>图 3.14 FFC 连接到 AI-G MIPI 15 针连接器的示例</strong></p>

请确保 FFC 上的 15 个银色触点与 AI-G MIPI 连接器内部的 15 个银色触点对齐。

### 3.2.2 GMSL 摄像头
GMSL 摄像头使用 Fakra 线缆，因此无法直接连接到 AI-G 开发板。必须先通过 Deserializer (Des) 板和 TOPST MIPI Gender Board 连接，然后再与 AI-G 对接。  
连接结构如下所示。

<p align="center"><strong>< AI-G > ↔ < TOPST MIPI Gender Board > ↔ < Des Board > ↔ < GMSL Camera ></strong></p>

GMSL 摄像头需要使用 TOPST MIPI Gender Board，并且必须通过 20 针 MIPI 连接器进行连接。例如，如果计划使用四个 GMSL 摄像头，则必须如图 3.15 所示使用 20 针 MIPI 接口进行连接。

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/accessories/Camera/3.15%2020-pin%20MIPI%20Connector.png"></p>
<p align="center"><strong>图 3.15 20 针 MIPI 连接器</strong></p>

1. 将 AI-G 开发板连接到 TOPST MIPI Gender Board。  
    FFC 线缆为 1.0 mm、20 针类型，其中一面必须带有不同颜色的标记（蓝色或灰色）。线缆应按 A-Forward Direction 方向插入。有关 FFC 类型，请参见图 3.16。
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/accessories/Camera/3.2%20FFC%20Type.png"></p>
    <p align="center"><strong>图 3.16 FFC 类型</strong></p>
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/accessories/Camera/3.17%20An%20example%20of%20an%20FFC%20connected%20to%20the%20AI-G%20MIPI%2020-pin%20Connector.png"></p>
    <p align="center"><strong>图 3.17 FFC 连接到 AI-G MIPI 20 针连接器的示例</strong></p>
    请确保 FFC 上的 20 个银色触点与 AI-G MIPI 连接器内部的 20 个银色触点对齐
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/accessories/Camera/3.18%20An%20example%20of%20an%20FFC%20connected%20to%20the%20TOPST%20MIPI%20Gender%20Board%20MIPI%20Connector.png"></p>
    <p align="center"><strong>图 3.18 FFC 连接到 TOPST MIPI Gender Board MIPI 连接器的示例</strong></p>
2. 将 Deserializer 板连接到 MIPI Gender Board。  
    将 MIPI Gender Board 上的 JH2 连接器连接到位于 SerDes 板底面的 JH1 连接器。
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/accessories/Camera/3.19%20JH2%20Connector.png"></p>
    <p align="center"><strong>图 3.19 JH2 连接器</strong></p>
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/accessories/Camera/3.20%20JH1%20Connector.png"></p>
    <p align="center"><strong>图 3.20 JH1 连接器</strong></p>
3. GMSL 摄像头连接
    请按图 3.21 所示连接摄像头。该图以两个摄像头为例进行说明，但您可以根据需要连接一到四个摄像头。
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/accessories/Camera/3.21%20GMSL%20Camera%20Connection.png"></p>
    <p align="center"><strong>图 3.21 GMSL 摄像头连接</strong></p>

# 4. 软件设置
第 4 章介绍摄像头运行所需的软件设置。若要在 D3-G 和 AI-G 平台上配置 MIPI CSI-2 摄像头（OV5647、IMX219）和 GMSL 摄像头，请参见下面提供的 Yocto 设置说明。

## 4.1 MIPI CSI-2 摄像头设置指南
TX 数据速率可使用以下公式计算：

<p align="center"><strong>TX 数据速率 ={ H_active }×{V_active }×{FPS}×{BPP}×{ Number_of_Cameras} × 1.3 （余量）</strong></p>

总数据速率不得超过 D3-G MIPI CSI-2 每通道 2.1 Gbps 的带宽限制。  
并且总数据速率不得超过 AI-G MIPI CSI-2 每通道 1.5 Gbps 的带宽限制

### 4.1.1 D3-G OV5647 设置指南
#### 4.1.1.1 OV5647 传感器概述
##### 4.1.1.1.1 简介
OV5647 是一款 500 万像素 CMOS 图像传感器，因其尺寸紧凑、性能稳定以及与标准 MIPI CSI-2 接口兼容，被广泛用于嵌入式摄像头应用。它也是 Raspberry Pi Camera Module v1 所采用的图像传感器，并可通过各种 Arducam OV5647 摄像头模组获得，这些模组均与 TOPST D3-G 平台兼容。  
用户可将 Raspberry Pi Camera v1 或 Arducam OV5647 模组连接到 MIPI CSI 端口以运行摄像头。

在 TOPST D3-G 平台上，OV5647 通过 15 针或 20 针 MIPI CSI 连接器连接，并通过 V4L2 框架进行控制，从而在 Yocto 和 Ubuntu 环境中提供一致的运行表现。

##### 4.1.1.1.2 支持的分辨率和 FPS
OV5647 摄像头模组（Raspberry Pi v1 或 Arducam OV5647）的规格如下：  

<p align="center"><strong>表 4.1 OV5647 摄像头模组规格</strong></p>
<div align="center">
    <table>
        <tr>
            <td colspan="2" align="center"><strong>规格</strong></td>
            <td align="center"><strong>说明</strong></td>
        </tr>
        <tr>
            <td colspan="2">传感器</td>
            <td>OmniVision OV5647</td>
        </tr>
        <tr>
            <td colspan="2">分辨率</td>
            <td>2592 x 1944 (5MP)</td>
        </tr>
        <tr>
            <td colspan="2">输出格式</td>
            <td>RAW, YUV, JPEG</td>
        </tr>
        <tr>
            <td colspan="2">接口</td>
            <td>MIPI CSI-2</td>
        </tr>
        <tr>
            <td colspan="2">帧率</td>
            <td>1080p30, 720p60, 480p90</td>
        </tr>
        <tr>
            <td colspan="2">镜头</td>
            <td>定焦</td>
        </tr>
        <tr>
            <td colspan="2">视场角 (FOV)</td>
            <td>Up to 54°</td>
        </tr>
        <tr>
            <td colspan="2">线缆类型</td>
            <td>FFC（15 针）</td>
        </tr>
        <tr>
            <td colspan="2">开发板尺寸</td>
            <td>25mm x 24mm</td>
        </tr>
        <tr>
            <td colspan="2">兼容性</td>
            <td>D3-G 和 Rasbperry Pi（通过 MIPI CSI-2 端口）</td>
        </tr>
    </table>
</div>

D3-G 支持的传感器分辨率和 FPS 如下：  
<p align="center"><strong>表 4.2 D3-G 上的 OV5647 传感器分辨率</strong></p>
<div align="center">
    <table>
        <tr>
            <td colspan="3" align="center"><strong>分辨率</strong></td>
            <td align="center"><strong>FPS</strong></td>
            <td align="center"><strong>说明</strong></td>
        </tr>
        <tr>
            <td colspan="3">1920x1080</td>
            <td>30</td>
            <td>通过裁剪全分辨率帧的中心区域输出 1080p 图像</td>
        </tr>
        <tr>
            <td colspan="3">1296x972</td>
            <td>30</td>
            <td>利用 2×2 像素合并提高灵敏度并降低噪声</td>
        </tr>
        <tr>
            <td colspan="3">640x480</td>
            <td>60</td>
            <td>将 2×2 合并与<strong>子采样</strong>相结合，子采样在读出过程中跳过像素，以降低数据吞吐量并实现更高的帧率</td>
        </tr>
    </table>
</div>

**注意：** 如表 4.2 所示，由于 D3-G 的 ISP 规格限制，**无法使用 2592×1944 的全分辨率**。

<p align="center"><strong>表 4.3 各运行模式的最大分辨率</strong></p>
<div align="center">
    <table>
        <tr>
            <td rowspan="2" align="center"><strong>ISP 核心</strong></td>
            <td colspan="2"><strong>各运行模式的分辨率</strong></td>
        </tr>
        <tr>
            <td align="center"><strong>默认模式</strong></td>
            <td align="center"><strong>内存共享模式</strong></td>
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

#### 4.1.1.2 在 Yocto 中配置 OV5647 分辨率：驱动程序
若要在 Yocto 构建过程中修改 OV5647 传感器的分辨率，请按照以下说明操作。  

首先，若要启用 OV5647，请确保在以下文件中设置了 TOPST_CAM_MODULE = "ov5647"。  
{build_dir}/build/d3-g-topst-main/conf/local.conf.  
虽然在为首次构建初始化仓库时该项默认已启用，但请再次确认。

此外，为防止源代码在构建过程中被删除，请在以下文件中启用下面这一行：  
{build_dir}/build/d3-g-topst-main/conf/local.conf:
```
INHERIT:remove = “rm_work”
```

启用上述选项后，使用以下命令重新构建镜像。
```
$ bitbake telechips-topst-image
```

其次，构建完成后，打开 ov5647.c 驱动程序文件并进行所需的修改。

请转到以下目录：
```
${build_dir}/build/d3-g-topst-main/tmp/work/d3_g_topst_main-telechips-linux/linux-topst/5.10.205-r0/git/drivers/media/i2c/telechips/
```

在修改代码之前，请注意当前驱动程序支持以下三种模式：
- 1920x1080 @ 30fps
- 1296x972 @ 30fps
- 640x480 @ 60fps  

每种分辨率分别对应 Mode 1、Mode 2 和 Mode 3。  

1920×1080 @ 30fps 模式采用中心裁剪，因此视场角较窄，而 640×480 模式的分辨率不足。相比之下，1296×972 模式采用 2×2 合并，可提供更宽的视场角，因此目前用作默认模式。  
打开 ov5647.c 驱动程序文件，并按下面所示修改 OV5647 的默认模式。
```
#define OV5647_DEFAULT_MODE (&supported_modes_10bit[2])
```
1920×1080 @ 30fps 对应 Mode 1，可以直接使用 **“#define OV5647_DEFAULT_MODE (&supported_modes_10bit[1])”**。  
1296×972 @ 30fps 模式对应 Mode 2，因此 **“#define OV5647_DEFAULT_MODE (&supported_modes_10bit[2])”** 已正确设置。  
对于对应 Mode 3 的 640×480 @ 60fps，请将定义修改为 **“#define OV5647_DEFAULT_MODE (&supported_modes_10bit[3])”**。

第三，重新构建内核并生成 FAI 镜像。  
返回构建目录，并使用以下命令重新构建内核。
```
$ cd ${build_dir}/build/d3-g-topst-main/
$ bitbake -C compile linux-topst
$ cd ${build_dir}
$ ./stitch-fai-d3.sh
```
随后，使用 FWDN 将生成的 output_d3g.fai 烧录到开发板，即可以所需分辨率使用 OV5647 传感器。

**注意：** 如果要使用 MIPI1-CSI 端口，请打开位于以下位置的 tcc805x-videoinput-camera-module.dtsi 文件。
“{build_dir}/build/d3-g-topst-main/tmp/work/d3_g_topst_main-telechips-linux/linux-topst/5.10.205-r0/git/arch/arm64/boot/dts/telechips/tcc805x/override/” and change the included dtsi file from “tcc805x-videoinput-mipi0-ov5647.dtsi” to “tcc805x-videoinput-mipi1-ov5647.dtsi”. + Open the tcc805x-videoinput.dtsi file located in "{build_dir}/build/d3-g-topst-main/tmp/work/d3_g_topst_main-telechips-linux/linux-topst/5.10.205-r0/git/arch/arm64/boot/dts/telechips/tcc805x/" and change the mipi chmux from "mipi-chmux-0 = <0>;" to "mipi-chmux-0 = <1>;".

### 4.1.2 D3-G IMX219 设置指南
#### 4.1.2.1 IMX219 传感器概述
##### 4.1.2.1.1 简介
IMX219 是 Sony 推出的高性能 800 万像素 CMOS 图像传感器，以在小型摄像头模块中提供出色的画质、低功耗和稳定的拍摄性能而闻名。它也是 Raspberry Pi Camera Module v2 所采用的传感器，广泛应用于嵌入式视觉系统、机器人以及基于 AI 的摄像头应用中。

在 TOPST D3-G 平台上，IMX219 传感器可通过 15 针或 20 针 MIPI CSI 连接器连接，并通过 V4L2 框架进行控制。这样可以在 Yocto 和 Ubuntu 两种环境下提供一致的接口和稳定的摄像头运行。

凭借高分辨率（8MP）和低噪声成像特性，IMX219 非常适合在 TOPST D3-G 平台上实现高质量的视频采集和图像处理功能。

##### 4.1.2.1.2 支持的分辨率和 FPS
IMX219 摄像头模块（Raspberry Pi v2）的规格如下：

<p align="center"><strong>表 4.4 IMX219 摄像头模块规格</strong></p>
<div align="center">
    <table>
        <tr>
            <td colspan="2" align="center"><strong>规格</strong></td>
            <td align="center"><strong>说明</strong></td>
        </tr>
        <tr>
            <td colspan="2">传感器</td>
            <td>Sony Imx219</td>
        </tr>
        <tr>
            <td colspan="2">分辨率</td>
            <td>3280 x 2464 (8 MP)</td>
        </tr>
        <tr>
            <td colspan="2">输出格式</td>
            <td>RAW, YUV, JPEG</td>
        </tr>
        <tr>
            <td colspan="2">接口</td>
            <td>MIPI CSI-2</td>
        </tr>
        <tr>
            <td colspan="2">帧率</td>
            <td>1080p60, 720p180, 480p206</td>
        </tr>
        <tr>
            <td colspan="2">镜头</td>
            <td>可调焦</td>
        </tr>
        <tr>
            <td colspan="2">视场角 (FOV)</td>
            <td>Up to 62°</td>
        </tr>
        <tr>
            <td colspan="2">线缆类型</td>
            <td>FFC（15 针）</td>
        </tr>
        <tr>
            <td colspan="2">开发板尺寸</td>
            <td>25mm x 24mm</td>
        </tr>
        <tr>
            <td colspan="2">兼容性</td>
            <td>D3-G 和 Rasbperry Pi（通过 MIPI CSI-2 端口）</td>
        </tr>
    </table>
</div>

D3-G 上支持的传感器分辨率和 FPS 如下：
<p align="center"><strong>表 4.5 D3-G 上的 IMX219 传感器分辨率</strong></p>
<div align="center">
    <table>
        <tr>
            <td colspan="3" align="center"><strong>分辨率</strong></td>
            <td align="center"><strong>FPS</strong></td>
            <td align="center"><strong>说明</strong></td>
        </tr>
        <tr>
            <td colspan="3">1920x1080</td>
            <td>30</td>
            <td>通过裁剪全分辨率帧的中心区域输出 1080p 图像</td>
        </tr>
        <tr>
            <td colspan="3">1640x1232</td>
            <td>30</td>
            <td>利用 2×2 像素合并提高灵敏度并降低噪声</td>
        </tr>
        <tr>
            <td colspan="3">640x480</td>
            <td>30</td>
            <td>将 2×2 合并与<strong>子采样</strong>相结合，在读出过程中跳过部分像素以降低数据吞吐量</td>
        </tr>
    </table>
</div>  

**注意：** 如表 4.5 所示，由于 D3-G 的 ISP 规格限制，**无法使用 3820×2464 的完整分辨率**。

<p align="center"><strong>表 4.6 各工作模式下的最大分辨率</strong></p>
<div align="center">
    <table>
        <tr>
            <td rowspan="2" align="center"><strong>ISP 核心</strong></td>
            <td colspan="2"><strong>各运行模式的分辨率</strong></td>
        </tr>
        <tr>
            <td align="center"><strong>默认模式</strong></td>
            <td align="center"><strong>内存共享模式</strong></td>
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

#### 4.1.2.2 在 Yocto 中启用 IMX219
由于 D3-G SDK 默认配置为启用 OV5647，因此在构建之前必须启用 IMX219。   
需要考虑两种情况：SDK 已经完成构建，以及首次进行构建。

##### 4.1.2.2.1 首次构建前启用 IMX219
对于首次构建，请按照以下步骤启用 IMX219 后再进行构建。
1. source 环境设置脚本并选择选项 2
    ```
    $ source poky/meta-topst/topst-build.sh
    ```
2. 打开位于以下路径的 local.conf 文件
    ```
    ${build_dir}/build/d3-g-topst-main/conf/local.conf
    ```
3. 注释掉 ov5647 对应的 TOPST_CAM_MODULE 条目，并启用 imx219 对应的条目
    ```
    #TOPST_CAM_MODULE = "ov5647"
    TOPST_CAM_MODULE = "imx219"
    ```
4. 执行构建过程
    ```
    $ bitbake telechips-topst-image
    ```
##### 4.1.2.2.2 构建完成后启用 IMX219
现有构建默认启用了 OV5647 传感器。请按照以下步骤启用 IMX219。
1. 打开位于以下路径的 local.conf 文件
    ```
    ${build_dir}/build/d3-g-topst-main/conf/local.conf
    ```
2. 注释掉 ov5647 对应的 TOPST_CAM_MODULE 条目，并启用 imx219 对应的条目
    ```
    #TOPST_CAM_MODULE = "ov5647"
    TOPST_CAM_MODULE = "imx219"
    ```
3. 对 isp-server 和 isp-firmware 执行 cleansstate 操作
    ```
    $ bitbake -c cleansstate isp-firmware
    $ bitbake -c cleansstate isp-server
    ```
4. 执行构建过程
    ```
    $ bitbake telechips-topst-image


#### 4.1.2.3 Yocto 中的 IMX219 分辨率配置：驱动程序
若要在 Yocto 构建过程中修改 IMX219 传感器的分辨率，请按照以下说明操作。

首先，要启用 imx219，请确认已设置 TOPST_CAM_MODULE = "imx219"，位置在
{build_dir}/build/d3-g-topst-main/conf/local.conf.

此外，为防止源代码在构建过程中被删除，请启用下面这一行，位于
{build_dir}/build/d3-g-topst-main/conf/local.conf:
```
INHERIT:remove = “rm_work”
```

启用上述选项后，使用以下命令重新构建镜像。
```
$ bitbake telechips-topst-image
```

其次，构建完成后，打开 imx219.c 驱动程序文件并应用所需的修改。

请转到以下目录：
```
${build_dir}/build/d3-g-topst-main/tmp/work/d3_g_topst_main-telechips-linux/linux-topst/5.10.205-r0/git/drivers/media/i2c/telechips/
```

在修改代码之前，请注意当前驱动程序支持以下三种模式：
- 1920x1080 @ 30fps
- 1640x1232 @ 30fps
- 640x480 @ 30fps

各分辨率分别对应 Mode 1、Mode 2 和 Mode 3。

1920×1080 @ 30fps 模式采用中心裁剪，视场角较窄；而 640×480 模式的分辨率不足。相比之下，1640×1232 模式采用 2×2 合并（binning），可提供更宽的视场角，因此当前将其用作默认模式。  
打开 imx219.c 驱动程序文件，并在 imx219_set_default_format、imx219_open 和 imx219_probe 函数内修改下文所述的部分。
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

由于 1920×1080 @ 30fps 对应 Mode 1，请将这三个函数内所有 supported_modes 的引用更新为 **“supported_modes[1]”**。  
1640×1232 @ 30fps 模式对应 Mode 2，因此请相应地将其替换为 **“supported_modes[2]”**。  
对于对应 Mode 3 的 640×480 @ 30fps，请将所有引用更改为 **“supported_modes [3]”**。

第三，重新构建内核并生成 FAI 镜像。  
返回构建目录，并使用以下命令重新构建内核。
```
$ cd ${build_dir}/build/d3-g-topst-main/
$ bitbake -C compile linux-topst
$ cd ${build_dir}
$ ./stitch-fai-d3.sh
```

随后，使用 FWDN 将生成的 output_d3g.fai 烧录到开发板，即可以所需分辨率使用 IMX219 传感器。

**注意：** 如果要使用 MIPI1-CSI 端口，请打开位于以下位置的 tcc805x-videoinput-camera-module.dtsi 文件。
“{build_dir}/build/d3-g-topst-main/tmp/work/d3_g_topst_main-telechips-linux/linux-topst/5.10.205-r0/git/arch/arm64/boot/dts/telechips/tcc805x/override/”and change the included dtsi file from “tcc805x-videoinput-mipi0-imx219.dtsi” to “tcc805x-videoinput-mipi1-imx219.dtsi”. + Open the tcc805x-videoinput.dtsi file located in "{build_dir}/build/d3-g-topst-main/tmp/work/d3_g_topst_main-telechips-linux/linux-topst/5.10.205-r0/git/arch/arm64/boot/dts/telechips/tcc805x/" and change the mipi chmux from "mipi-chmux-0 = <0>;" to "mipi-chmux-0 = <1>;".

#### 4.1.2.4 如何在 Yocto 中提高 IMX219 的 FPS：驱动程序和设备树
根据 IMX219 传感器说明，该传感器支持 1080p60、720p180 和 VGA206 等高帧率模式。因此，可以提高 imx219.c 驱动程序所支持的分辨率（1920×1080、1640×1232 和 640×480）的 FPS。由于 D3-G 平台上的 ISP 核心最高支持 60 fps，这些分辨率均可提升至最高 60 fps。 

FPS 的计算公式如下：
<p align="center"><strong>{fps} = {pixel_rate}/{hts}x{vts}</strong></p>
因此，若要提高 FPS，必须调整 pixel_rate、hts 和 vts 的值。  
在当前驱动程序实现中，pixel_rate 和 hts 均为固定值。要提高 FPS，唯一可行的方法是在保持 hts 不变的情况下增大 pixel_rate，然后相应地调整 vts 以达到所需的帧率。

若要将 FPS 修改为 60，必须同时更新驱动程序和设备树。
请按照以下指南将 FPS 更改为 60。

##### 4.1.2.4.1 1920x1080 @ 60fps
若要达到 60 fps，必须满足以下关系：  
fps = pixel_rate / (hts × vts)
- pixel_rate = 182,400,000
- hts = 3448
- target fps = 60

所需的 VTS 为：
- vts = pixel_rate / (hts × fps) = 182,400,000 / (3448 × 60) ≈ 882

但是，VTS 值必须大于 1080，因此该配置无效。  
因此，若要达到 60 fps，必须保持 hts 固定，转而调整 pixel_rate、vts 和 PLL_VT 寄存器。

所需的更改如下：
1. imx219.c 驱动程序文件  
    A. 提高像素率和链路频率
    ```
    #define IMX219_PIXEL_RATE            182400000    →   #define IMX219_PIXEL_RATE            278400000
    #define IMX219_DEFAULT_LINK_FREQ     456000000   →   #define IMX219_DEFAULT_LINK_FREQ     696000000
    ``` 
    B. 更新 1080p 模式的 VTS 值：
    ```
    #define IMX219_VTS_30FPS_1080P       0x06e3       →   #define IMX219_VTS_30FPS_1080P       0x0542
    ```
    C. 修改 1920x1080 模式表中的 PLL_VT 寄存器：
    ```
    // imx219_reg mode_1920_1080_regs[]
    {0x0307, 0x39}   →   {0x0307, 0x57}
    ```
2. tcc805x-videoinput-mipi0-imx219.dtsi 设备树文件  
    A. 更新链路频率以匹配新的像素率：
    ```
    // &i2c7
    /bits/ 64 <456000000> → /bits/ 64 <696000000>
    ```
    B. 更新 hs-settle 值：
    ```
    hs-settle = <13> → hs-settle = <35>
    ```
3. 重新构建内核并生成 FAI 镜像。  
    返回构建目录，并使用以下命令重新构建内核。
    ```
    $ cd ${build_dir}/build/d3-g-topst-main/
    $ bitbake -C compile linux-topst
    $ cd ${build_dir}
    $ ./stitch-fai-d3.sh
    ```
在 D3-G 上使用以下命令，可以确认 FPS 输出为 59.9，即对应 60 fps。
```
$ v4l2-ctl --stream-mmap=3 --stream-count=300 --stream-to=/dev/null --verbose
```
在 D3-G 上用于摄像头播放的 GStreamer 命令如下所示。
```
$ gst-launch-1.0 v4l2src device=/dev/video0 io-mode=2 ! video/x-raw,format=NV12,width=1920,height=1080,framerate=60/1 ! videoconvert ! waylandsink sync=false
```

##### 4.1.2.4.2 1640x1232 @ 60fps
若要达到 60 fps，必须满足以下关系：  
fps = pixel_rate / (hts × vts)
- pixel_rate = 182,400,000
- hts = 3448
- target fps = 60

所需的 VTS 为：
- vts = pixel_rate / (hts × fps) = 182,400,000 / (3448 × 60) ≈ 882

但是，VTS 值必须大于 1080，因此该配置无效。  
因此，若要达到 60 fps，必须保持 hts 固定，转而调整 pixel_rate、vts 和 PLL_VT 寄存器。

所需的更改如下：
1. imx219.c 驱动程序文件  
    A. 提高像素率和链路频率
    ```
    #define IMX219_PIXEL_RATE            182400000    →   #define IMX219_PIXEL_RATE            278400000
    #define IMX219_DEFAULT_LINK_FREQ     456000000   →   #define IMX219_DEFAULT_LINK_FREQ     696000000
    ``` 
    B. 更新 1640_1232 模式的 VTS 值：
    ```
    #define IMX219_VTS_30FPS_BINNED       0x06e3       →   #define IMX219_VTS_30FPS_BINNED       0x0542
    ```
    C. 修改 1920x1080 模式表中的 PLL_VT 寄存器：
    ```
    // imx219_reg mode_1640_1232_regs[]
    {0x0307, 0x39}   →   {0x0307, 0x57}
    ```
2. tcc805x-videoinput-mipi0-imx219.dtsi 设备树文件  
    A. 更新链路频率以匹配新的像素率：
    ```
    // &i2c7
    /bits/ 64 <456000000> → /bits/ 64 <696000000>
    ```
    B. 更新 hs-settle 值：
    ```
    hs-settle = <13> → hs-settle = <34>
    ```
3. 重新构建内核并生成 FAI 镜像。  
    返回构建目录，并使用以下命令重新构建内核。
    ```
    $ cd ${build_dir}/build/d3-g-topst-main/
    $ bitbake -C compile linux-topst
    $ cd ${build_dir}
    $ ./stitch-fai-d3.sh
    ```
在 D3-G 上使用以下命令，可以确认 FPS 输出为 59.9，即对应 60 fps。
```
$ v4l2-ctl --stream-mmap=3 --stream-count=300 --stream-to=/dev/null --verbose
```
在 D3-G 上用于摄像头播放的 GStreamer 命令如下所示。
```
$ gst-launch-1.0 v4l2src device=/dev/video0 io-mode=2 ! video/x-raw,format=NV12,width=1640,height=1232,framerate=60/1 ! videoconvert ! waylandsink sync=false
```

##### 4.1.2.4.3 640x480 @ 60fps
若要达到 60 fps，必须满足以下关系：  
fps = pixel_rate / (hts × vts)
- pixel_rate = 182,400,000
- hts = 3448
- target fps = 60

所需的 VTS 为：
- vts = pixel_rate / (hts × fps) = 182,400,000 / (3448 × 60) ≈ 882

由于 VTS 值大于 480，因此满足该条件。与前面的示例相同，在保持 HTS 固定的情况下调整 pixelrate 和 VTS 以更改 FPS。  
也可以在不改变 pixelrate 的情况下，仅修改 VTS 值来调整 FPS。但是，IMX219 的 0x0307 寄存器值必须保持不变。

所需的更改如下：
1. imx219.c 驱动程序文件  
    A. 提高像素率和链路频率
    ```
    #define IMX219_PIXEL_RATE            182400000    →   #define IMX219_PIXEL_RATE            278400000
    #define IMX219_DEFAULT_LINK_FREQ     456000000   →   #define IMX219_DEFAULT_LINK_FREQ     696000000
    ``` 
    B. 更新 640_480 模式的 VTS 值：
    ```
    #define IMX219_VTS_30FPS_640x480       0x06e3       →   #define IMX219_VTS_30FPS_640x480       0x0542
    ```
    C. 修改 640x480 模式表中的 PLL_VT 寄存器：
    ```
    // imx219_reg mode_640_480_regs[]
    {0x0307, 0x39}   →   {0x0307, 0x57}
    ```
2. tcc805x-videoinput-mipi0-imx219.dtsi 设备树文件  
    A. 更新链路频率以匹配新的像素率：
    ```
    // &i2c7
    /bits/ 64 <456000000> → /bits/ 64 <696000000>
    ```
    B. 更新 hs-settle 值：
    ```
    hs-settle = <13> → hs-settle = <26>
    ```
3. 重新构建内核并生成 FAI 镜像。  
    返回构建目录，并使用以下命令重新构建内核。
    ```
    $ cd ${build_dir}/build/d3-g-topst-main/
    $ bitbake -C compile linux-topst
    $ cd ${build_dir}
    $ ./stitch-fai-d3.sh
    ```
在 D3-G 上使用以下命令，可以确认 FPS 输出为 59.9，即对应 60 fps。
```
$ v4l2-ctl --stream-mmap=3 --stream-count=300 --stream-to=/dev/null --verbose
```
在 D3-G 上用于摄像头播放的 GStreamer 命令如下所示。
```
$ gst-launch-1.0 v4l2src device=/dev/video0 io-mode=2 ! video/x-raw,format=NV12,width=640,height=480,framerate=60/1 ! videoconvert ! waylandsink sync=false
```

### 4.1.3 AI-G OV5647 传感器用户指南
#### 4.1.3.1 OV5647 传感器概述
##### 4.1.3.1.1 简介
OV5647 是一款 500 万像素 CMOS 图像传感器，因其体积小巧、性能稳定并兼容标准 MIPI CSI-2 接口，被广泛应用于嵌入式摄像头应用。它也是 Raspberry Pi Camera Module v1 所采用的图像传感器，并可通过各种 Arducam OV5647 摄像头模块获得，这些模块均与 TOPST AI-G 平台兼容。  
用户可将 Raspberry Pi Camera v1 或 Arducam OV5647 模组连接到 MIPI CSI 端口以运行摄像头。

在 TOPST AI-G 平台上，OV5647 通过 15 针或 20 针 MIPI CSI 连接器连接，并通过 V4L2 框架进行控制，从而在 Yocto 和 Ubuntu 环境中提供一致的运行表现。

##### 4.1.3.1.2 支持的分辨率和 FPS
OV5647 摄像头模块（Raspberry Pi v1 或 Arducam OV5647）的规格如下：
<p align="center"><strong>表 4.7 OV5647 摄像头模块规格</strong></p>
<div align="center">
    <table>
        <tr>
            <td colspan="2" align="center"><strong>规格</strong></td>
            <td align="center"><strong>说明</strong></td>
        </tr>
        <tr>
            <td colspan="2">传感器</td>
            <td>OmniVision OV5647</td>
        </tr>
        <tr>
            <td colspan="2">分辨率</td>
            <td>2592 x 1944 (5MP)</td>
        </tr>
        <tr>
            <td colspan="2">输出格式</td>
            <td>RAW, YUV, JPEG</td>
        </tr>
        <tr>
            <td colspan="2">接口</td>
            <td>MIPI CSI-2</td>
        </tr>
        <tr>
            <td colspan="2">帧率</td>
            <td>1080p30, 720p60, 480p90</td>
        </tr>
        <tr>
            <td colspan="2">镜头</td>
            <td>定焦</td>
        </tr>
        <tr>
            <td colspan="2">视场角 (FOV)</td>
            <td>Up to 54°</td>
        </tr>
        <tr>
            <td colspan="2">线缆类型</td>
            <td>FFC（15 针）</td>
        </tr>
        <tr>
            <td colspan="2">开发板尺寸</td>
            <td>25mm x 24mm</td>
        </tr>
        <tr>
            <td colspan="2">兼容性</td>
            <td>D3-G 和 Rasbperry Pi（通过 MIPI CSI-2 端口）</td>
        </tr>
    </table>
</div>

AI-G 上支持的传感器分辨率和 FPS 如下：  
<p align="center"><strong>表 4.8 AI-G 上的 OV5647 传感器分辨率</strong></p>
<div align="center">
    <table>
        <tr>
            <td colspan="3" align="center"><strong>分辨率</strong></td>
            <td align="center"><strong>FPS</strong></td>
            <td align="center"><strong>说明</strong></td>
        </tr>
        <tr>
            <td colspan="3">1920x1080</td>
            <td>30</td>
            <td>通过裁剪全分辨率帧的中心区域输出 1080p 图像</td>
        </tr>
        <tr>
            <td colspan="3">1296x972</td>
            <td>30</td>
            <td>利用 2×2 像素合并提高灵敏度并降低噪声</td>
        </tr>
        <tr>
            <td colspan="3">640x480</td>
            <td>60</td>
            <td>将 2×2 合并与<strong>子采样</strong>相结合，子采样在读出过程中跳过像素，以降低数据吞吐量并实现更高的帧率</td>
        </tr>
    </table>
</div>

**注意：** 如表 4.8 所示，由于会显著降低推理性能，因此**不使用完整的 2592×1944 分辨率**。

<p align="center"><strong>表 4.9 各工作模式的最大分辨率</strong></p>
<div align="center">
    <table>
        <tr>
            <td colspan="4" align="center"><strong>已使用 CH.</strong></td>
            <td align="center"><strong>工作模式</strong></td>
            <td align="center"><strong>最大分辨率</strong></td>
            <td align="center"><strong>输入格式</strong></td>
        </tr>
        <tr>
            <td colspan="4">4CH</td>
            <td>默认模式</td>
            <td>1280 x 720 @ 60fps</td>
            <td>RAW 24</td>
        </tr>
        <tr>
            <td colspan="4" rowspan="2">2CH</td>
            <td rowspan="2">内存共享模式</td>
            <td>选项 1: 2048 x 1280 @ 60fps</td>
            <td>RAW 20</td>
        </tr>
        <tr>
            <td>选项 2: 2592 x 2048 @ 30fps + 2048 x 1280 @ 30fps</td>
            <td>RAW 24</td>
        </tr>
        <tr>
            <td colspan="4">1CH</td>
            <td>内存共享模式</td>
            <td>2592 x 2048 @ 60fps</td>
            <td>RAW 20</td>
        </tr>
    </table>
</div>

#### 4.1.3.2 Yocto 中的 OV5647 分辨率配置：驱动程序
若要在 Yocto 构建过程中修改 OV5647 传感器的分辨率，请按照以下说明操作。

首先，若要启用 OV5647，请确保在以下文件中设置了 TOPST_CAM_MODULE = "ov5647"。  
{build_dir}/build/ai-g-topst-main/conf/local.conf.  
虽然在为首次构建初始化仓库时该项默认已启用，但请再次确认。

此外，为防止源代码在构建过程中被删除，请在以下文件中启用下面这一行：  
{build_dir}/build/ai-g-topst-main/conf/local.conf:
```
INHERIT:remove = “rm_work”
```

启用上述选项后，使用以下命令重新构建镜像。
```
$ bitbake telechips-topst-image
```

其次，构建完成后，打开 ov5647.c 驱动程序文件并进行所需的修改。

请转到以下目录：
```
${build_dir}/build/ai-g-topst-main/tmp/work/ai_g_topst-telechips-linux/linux-topst/5.10.223-r0/git/drivers/media/i2c/telechips/
```

在修改代码之前，请注意当前驱动程序支持以下三种模式：
- 1920×1080 @ 30fps
- 1296×972 @ 30fps
- 640×480 @ 60fps

各分辨率分别对应 Mode 1、Mode 2 和 Mode 3。

1920×1080 @ 30fps 模式采用中心裁剪，因此视场角较窄，而 640×480 模式的分辨率不足。相比之下，1296×972 模式采用 2×2 合并，可提供更宽的视场角，因此目前用作默认模式。  
打开 ov5647.c 驱动程序文件，并按下面所示修改 OV5647 的默认模式。
```
#define OV5647_DEFAULT_MODE (&supported_modes_10bit[2])
```
1920×1080 @ 30fps 对应 Mode 1，可以直接使用 **“#define OV5647_DEFAULT_MODE (&supported_modes_10bit[1])”**。  
1296×972 @ 30fps 模式对应 Mode 2，因此 **“#define OV5647_DEFAULT_MODE (&supported_modes_10bit[2])”** 已正确设置。  
对于对应 Mode 3 的 640×480 @ 60fps，请将定义修改为 **“#define OV5647_DEFAULT_MODE (&supported_modes_10bit[3])”**。

第三，重新构建内核并生成 FAI 镜像。  
返回构建目录，并使用以下命令重新构建内核。
```
$ cd ${build_dir}/build/ai-g-topst-main/
$ bitbake -C compile linux-topst
$ cd ${build_dir}
$ ./stitch-fai-ai.sh
```

随后，使用 FWDN 将生成的 output_aig.fai 烧录到开发板，即可以所需分辨率使用 OV5647 传感器。

### 4.1.4 AI-G IMX219 传感器设置指南
#### 4.1.4.1 IMX219 传感器概述
##### 4.1.4.1.1 简介
IMX219 是 Sony 推出的高性能 800 万像素 CMOS 图像传感器，以在小型摄像头模块中提供出色的画质、低功耗和稳定的拍摄性能而闻名。它也是 Raspberry Pi Camera Module v2 所采用的传感器，广泛应用于嵌入式视觉系统、机器人以及基于 AI 的摄像头应用中。

在 TOPST AI-G 平台上，IMX219 传感器可通过 15 针或 20 针 MIPI CSI 连接器连接，并通过 V4L2 框架进行控制。这样可在 Yocto 和 Ubuntu 环境中提供一致的接口和稳定的摄像头运行。

凭借高分辨率（8MP）和低噪声成像特性，IMX219 非常适合在 TOPST AI-G 平台上实现高质量的视频采集和图像处理功能。

##### 4.1.4.1.2 支持的分辨率和 FPS
IMX219 摄像头模块（Raspberry Pi v2）的规格如下：
<p align="center"><strong>表 4.10 IMX219 摄像头模块规格</strong></p>
<div align="center">
    <table>
        <tr>
            <td colspan="2" align="center"><strong>规格</strong></td>
            <td align="center"><strong>说明</strong></td>
        </tr>
        <tr>
            <td colspan="2">传感器</td>
            <td>Sony Imx219</td>
        </tr>
        <tr>
            <td colspan="2">分辨率</td>
            <td>3280 x 2464 (8 MP)</td>
        </tr>
        <tr>
            <td colspan="2">输出格式</td>
            <td>RAW, YUV, JPEG</td>
        </tr>
        <tr>
            <td colspan="2">接口</td>
            <td>MIPI CSI-2</td>
        </tr>
        <tr>
            <td colspan="2">帧率</td>
            <td>1080p60, 720p180, 480p206</td>
        </tr>
        <tr>
            <td colspan="2">镜头</td>
            <td>可调焦</td>
        </tr>
        <tr>
            <td colspan="2">视场角 (FOV)</td>
            <td>Up to 62°</td>
        </tr>
        <tr>
            <td colspan="2">线缆类型</td>
            <td>FFC（15 针）</td>
        </tr>
        <tr>
            <td colspan="2">开发板尺寸</td>
            <td>25mm x 24mm</td>
        </tr>
        <tr>
            <td colspan="2">兼容性</td>
            <td>D3-G 和 Rasbperry Pi（通过 MIPI CSI-2 端口）</td>
        </tr>
    </table>
</div>

AI-G 上支持的传感器分辨率和 FPS 如下：
<p align="center"><strong>表 4.11 AI-G 上的 IMX219 传感器分辨率</strong></p>
<div align="center">
    <table>
        <tr>
            <td colspan="3" align="center"><strong>分辨率</strong></td>
            <td align="center"><strong>FPS</strong></td>
            <td align="center"><strong>说明</strong></td>
        </tr>
        <tr>
            <td colspan="3">1920x1080</td>
            <td>30</td>
            <td>通过裁剪全分辨率帧的中心区域输出 1080p 图像</td>
        </tr>
        <tr>
            <td colspan="3">1640x1232</td>
            <td>30</td>
            <td>利用 2×2 像素合并提高灵敏度并降低噪声</td>
        </tr>
        <tr>
            <td colspan="3">640x480</td>
            <td>30</td>
            <td>将 2×2 合并与<strong>子采样</strong>相结合，在读出过程中跳过部分像素以降低数据吞吐量</td>
        </tr>
    </table>
</div>

**注意：** 如表 4.11 所示，由于会显著降低推理性能，因此不使用完整的 3820×2464 分辨率。

<p align="center"><strong>表 4.12 各工作模式的最大分辨率</strong></p>
<div align="center">
    <table>
        <tr>
            <td colspan="4" align="center"><strong>已使用 CH.</strong></td>
            <td align="center"><strong>工作模式</strong></td>
            <td align="center"><strong>最大分辨率</strong></td>
            <td align="center"><strong>输入格式</strong></td>
        </tr>
        <tr>
            <td colspan="4">4CH</td>
            <td>默认模式</td>
            <td>1280 x 720 @ 60fps</td>
            <td>RAW 24</td>
        </tr>
        <tr>
            <td colspan="4" rowspan="2">2CH</td>
            <td rowspan="2">内存共享模式</td>
            <td>选项 1: 2048 x 1280 @ 60fps</td>
            <td>RAW 20</td>
        </tr>
        <tr>
            <td>选项 2: 2592 x 2048 @ 30fps + 2048 x 1280 @ 30fps</td>
            <td>RAW 24</td>
        </tr>
        <tr>
            <td colspan="4">1CH</td>
            <td>内存共享模式</td>
            <td>2592 x 2048 @ 60fps</td>
            <td>RAW 20</td>
        </tr>
    </table>
</div>

#### 4.1.4.2 在 Yocto 中启用 IMX219
由于 AI-G SDK 默认配置为启用 OV5647，因此在构建之前必须启用 IMX219。  
需要考虑两种情况：SDK 已经完成构建，以及首次进行构建。

##### 4.1.4.2.1 在首次构建之前启用 IMX219
对于首次构建，请按照以下步骤启用 IMX219 后再进行构建。
1. source 环境设置脚本并选择选项 1
    ```
    $ source poky/meta-topst/topst-build.sh
    ```
2. 打开位于以下路径的 local.conf 文件
    ```
    ${build_dir}/build/ai-g-topst-main/conf/local.conf
    ```
3. 注释掉 ov5647 对应的 TOPST_CAM_MODULE 条目，并启用 imx219 对应的条目
    ```
    #TOPST_CAM_MODULE = "ov5647"
    TOPST_CAM_MODULE = "imx219"
    ```
4. 执行构建过程
    ```
    $ bitbake telechips-topst-ai-image
    ```

##### 4.1.4.2.2 在构建已完成之后启用 IMX219
现有构建默认启用了 OV5647 传感器。请按照以下步骤启用 IMX219。
1. 打开位于以下路径的 local.conf 文件
    ```
    ${build_dir}/build/ai-g-topst-main/conf/local.conf
    ```
2. 注释掉 ov5647 对应的 TOPST_CAM_MODULE 条目，并启用 imx219 对应的条目
    ```
    #TOPST_CAM_MODULE = "ov5647"
    TOPST_CAM_MODULE = "imx219"
    ```
3. 对 isp-server 和 isp-firmware 执行 cleansstate 操作
    ```
    $ bitbake -c cleansstate isp-firmware
    $ bitbake -c cleansstate isp-server
    ```
4. 执行构建过程
    ```
    $ bitbake telechips-topst-ai-image
    ```

#### 4.1.4.3 Yocto 中的 IMX219 分辨率配置：驱动程序
若要在 Yocto 构建过程中修改 IMX219 传感器的分辨率，请按照以下说明操作。

首先，要启用 imx219，请确认已设置 TOPST_CAM_MODULE = "imx219"，位置在
{build_dir}/build/ai-g-topst-main/conf/local.conf.

此外，为防止源代码在构建过程中被删除，请启用下面这一行，位于
{build_dir}/build/ai-g-topst-main/conf/local.conf:
```
INHERIT:remove = “rm_work”
```

启用上述选项后，使用以下命令重新构建镜像。
```
$ bitbake telechips-topst-ai-image
```
其次，构建完成后，打开 imx219.c 驱动程序文件并应用所需的修改。

请转到以下目录：
```
${build_dir}/build/ai-g-topst-main /ai-g-topst/tmp/work/ai_g_topst-telechips-linux/linux-topst/5.10.223-r0/git/drivers/media/i2c/telechips/
```
在修改代码之前，请注意当前驱动程序支持以下三种模式：
- 1920×1080 @ 30fps
- 1640×1232 @ 30fps
- 640×480 @ 30fps
各分辨率分别对应 Mode 1、Mode 2 和 Mode 3。

1920×1080 @ 30fps 模式采用中心裁剪，视场角较窄；而 640×480 模式的分辨率不足。相比之下，1640×1232 模式采用 2×2 合并（binning），可提供更宽的视场角，因此当前将其用作默认模式。  
打开 imx219.c 驱动程序文件，并在 imx219_set_default_format、imx219_open 和 imx219_probe 函数内修改下文所述的部分。
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

由于 1920×1080 @ 30fps 对应 Mode 1，请将这三个函数内所有 supported_modes 的引用更新为 **“supported_modes[1]”**。  
1640×1232 @ 30fps 模式对应 Mode 2，因此请相应地将其替换为 **“supported_modes[2]”**。  
对于对应 Mode 3 的 640×480 @ 30fps，请将所有引用更改为 **“supported_modes [3]”**。

第三，重新构建内核并生成 FAI 镜像。  
返回构建目录，并使用以下命令重新构建内核。
```
$ cd ${build_dir}/build/ai-g-topst-main/
$ bitbake -C compile linux-topst
$ cd ${build_dir}
$ ./stitch-fai-ai.sh
```

随后，使用 FWDN 将生成的 output_aig.fai 烧录到开发板，即可以所需分辨率使用 IMX219 传感器。

#### 4.1.4.4 如何在 Yocto 中提高 IMX219 的 FPS：驱动程序和设备树
根据 IMX219 传感器说明，该传感器支持 1080p60、720p180 和 VGA206 等高帧率模式。因此，可以提高 imx219.c 驱动程序所支持的分辨率（1920×1080、1640×1232 和 640×480）的 FPS。由于 AI-G 平台上的 ISP 核心最高支持 60 fps，这些分辨率均可提升至最高 60 fps。  

FPS 的计算公式如下：
<p align="center"><strong>{fps} = {pixel_rate}/{hts}x{vts}</strong></p>
因此，若要提高 FPS，必须调整 pixel_rate、hts 和 vts 的值。  
在当前驱动程序实现中，pixel_rate 和 hts 均为固定值。要提高 FPS，唯一可行的方法是在保持 hts 不变的情况下增大 pixel_rate，然后相应地调整 vts 以达到所需的帧率。

若要将 FPS 修改为 60，必须同时更新驱动程序和设备树。
请按照以下指南将 FPS 更改为 60。

##### 4.1.2.4.1 1920x1080 @ 60fps
若要达到 60 fps，必须满足以下关系：  
fps = pixel_rate / (hts × vts)
- pixel_rate = 182,400,000
- hts = 3448
- target fps = 60

所需的 VTS 为：
- vts = pixel_rate / (hts × fps) = 182,400,000 / (3448 × 60) ≈ 882

但是，VTS 值必须大于 1080，因此该配置无效。  
因此，若要达到 60 fps，必须保持 hts 固定，转而调整 pixel_rate、vts 和 PLL_VT 寄存器。

所需的更改如下：
1. imx219.c 驱动程序文件  
    A. 提高像素率和链路频率
    ```
    #define IMX219_PIXEL_RATE            182400000    →   #define IMX219_PIXEL_RATE            278400000
    #define IMX219_DEFAULT_LINK_FREQ     456000000   →   #define IMX219_DEFAULT_LINK_FREQ     696000000
    ``` 
    B. 更新 1080p 模式的 VTS 值：
    ```
    #define IMX219_VTS_30FPS_1080P       0x06e3       →   #define IMX219_VTS_30FPS_1080P       0x0542
    ```
    C. 修改 1920x1080 模式表中的 PLL_VT 寄存器：
    ```
    // imx219_reg mode_1920_1080_regs[]
    {0x0307, 0x39}   →   {0x0307, 0x57}
    ```
2. tcc805x-videoinput-mipi0-imx219.dtsi 设备树文件  
    A. 更新链路频率以匹配新的像素率：
    ```
    // &i2c7
    /bits/ 64 <456000000> → /bits/ 64 <696000000>
    ```
    B. 更新 hs-settle 值：
    ```
    hs-settle = <13> → hs-settle = <35>
    ```
3. 重新构建内核并生成 FAI 镜像。  
    返回构建目录，并使用以下命令重新构建内核。
    ```
    $ cd ${build_dir}/build/d3-g-topst-main/
    $ bitbake -C compile linux-topst
    $ cd ${build_dir}
    $ ./stitch-fai-d3.sh
    ```
在 AI-G 上使用以下命令，可以确认 FPS 输出为 59.9，即对应 60 fps。
```
$ v4l2-ctl --stream-mmap=3 --stream-count=300 --stream-to=/dev/null --verbose
```

##### 4.1.2.4.2 1640x1232 @ 60fps
若要达到 60 fps，必须满足以下关系：  
fps = pixel_rate / (hts × vts)
- pixel_rate = 182,400,000
- hts = 3448
- target fps = 60

所需的 VTS 为：
- vts = pixel_rate / (hts × fps) = 182,400,000 / (3448 × 60) ≈ 882

但是，VTS 值必须大于 1080，因此该配置无效。  
因此，若要达到 60 fps，必须保持 hts 固定，转而调整 pixel_rate、vts 和 PLL_VT 寄存器。

所需的更改如下：
1. imx219.c 驱动程序文件  
    A. 提高像素率和链路频率
    ```
    #define IMX219_PIXEL_RATE            182400000    →   #define IMX219_PIXEL_RATE            278400000
    #define IMX219_DEFAULT_LINK_FREQ     456000000   →   #define IMX219_DEFAULT_LINK_FREQ     696000000
    ``` 
    B. 更新 1640_1232 模式的 VTS 值：
    ```
    #define IMX219_VTS_30FPS_BINNED       0x06e3       →   #define IMX219_VTS_30FPS_BINNED       0x0542
    ```
    C. 修改 1920x1080 模式表中的 PLL_VT 寄存器：
    ```
    // imx219_reg mode_1640_1232_regs[]
    {0x0307, 0x39}   →   {0x0307, 0x57}
    ```
2. tcc805x-videoinput-mipi0-imx219.dtsi 设备树文件  
    A. 更新链路频率以匹配新的像素率：
    ```
    // &i2c7
    /bits/ 64 <456000000> → /bits/ 64 <696000000>
    ```
    B. 更新 hs-settle 值：
    ```
    hs-settle = <13> → hs-settle = <34>
    ```
3. 重新构建内核并生成 FAI 镜像。  
    返回构建目录，并使用以下命令重新构建内核。
    ```
    $ cd ${build_dir}/build/d3-g-topst-main/
    $ bitbake -C compile linux-topst
    $ cd ${build_dir}
    $ ./stitch-fai-d3.sh
    ```
在 AI-G 上使用以下命令，可以确认 FPS 输出为 59.9，即对应 60 fps。
```
$ v4l2-ctl --stream-mmap=3 --stream-count=300 --stream-to=/dev/null --verbose
```

##### 4.1.2.4.3 640x480 @ 60fps
若要达到 60 fps，必须满足以下关系：  
fps = pixel_rate / (hts × vts)
- pixel_rate = 182,400,000
- hts = 3448
- target fps = 60

所需的 VTS 为：
- vts = pixel_rate / (hts × fps) = 182,400,000 / (3448 × 60) ≈ 882

由于 VTS 值大于 480，因此满足该条件。与前面的示例相同，在保持 HTS 固定的情况下调整 pixelrate 和 VTS 以更改 FPS。  
也可以在不改变 pixelrate 的情况下，仅修改 VTS 值来调整 FPS。但是，IMX219 的 0x0307 寄存器值必须保持不变。

所需的更改如下：
1. imx219.c 驱动程序文件  
    A. 提高像素率和链路频率
    ```
    #define IMX219_PIXEL_RATE            182400000    →   #define IMX219_PIXEL_RATE            278400000
    #define IMX219_DEFAULT_LINK_FREQ     456000000   →   #define IMX219_DEFAULT_LINK_FREQ     696000000
    ``` 
    B. 更新 640_480 模式的 VTS 值：
    ```
    #define IMX219_VTS_30FPS_640x480       0x06e3       →   #define IMX219_VTS_30FPS_640x480       0x0542
    ```
    C. 修改 640x480 模式表中的 PLL_VT 寄存器：
    ```
    // imx219_reg mode_640_480_regs[]
    {0x0307, 0x39}   →   {0x0307, 0x57}
    ```
2. tcc805x-videoinput-mipi0-imx219.dtsi 设备树文件  
    A. 更新链路频率以匹配新的像素率：
    ```
    // &i2c7
    /bits/ 64 <456000000> → /bits/ 64 <696000000>
    ```
    B. 更新 hs-settle 值：
    ```
    hs-settle = <13> → hs-settle = <26>
    ```
3. 重新构建内核并生成 FAI 镜像。  
    返回构建目录，并使用以下命令重新构建内核。
    ```
    $ cd ${build_dir}/build/d3-g-topst-main/
    $ bitbake -C compile linux-topst
    $ cd ${build_dir}
    $ ./stitch-fai-d3.sh
    ```
在 AI-G 上使用以下命令，可以确认 FPS 输出为 59.9，即对应 60 fps。
```
$ v4l2-ctl --stream-mmap=3 --stream-count=300 --stream-to=/dev/null --verbose
```

## 4.2 GMSL 摄像头设置指南
### 4.2.1 D3-G GMSL 摄像头设置指南
使用 Deserializer 开发板，可以将最多四个摄像头连接到单个 MIPI CSI 端口。由于 D3-G 提供两个 MIPI CSI 端口，您可以选择以下配置之一：
- 在 MIPI0 端口上使用四个摄像头
- 在 MIPI1 端口上使用四个摄像头
- 同时使用 MIPI0 和 MIPI1 连接共八个摄像头

在配置全部八路摄像头时，D3-G 最多支持四台显示器的显示扩展功能最多可使用三台显示器。

**注意：** 本指南使用 IMX290 (cxd5700) FHD GMSL 摄像头。  
如果打算使用其他 GMSL 摄像头，则需要进行额外的摄像头移植。

#### 4.2.1.1 如何使用 MIPI0 端口
首先，必须同时启用 GMSL 摄像头和 SerDes 开发板的内核配置。  
将以下条目添加到  
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
修改上述选项后，使用以下命令重新构建镜像。
```
$ bitbake -c cleansstate isp-firmware
$ bitbake -c cleansstate isp-server
$ bitbake telechips-topst-image
```
接下来，必须修改内核中的设备树。请按照以下指南应用更改并重新构建镜像。
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
7. 重新构建内核并生成 FAI 镜像。  
    返回构建目录，并使用以下命令重新构建内核
    ```
    $ cd ${build_dir}/build/ai-g-topst-main/
    $ bitbake -C compile linux-topst
    $ cd ${build_dir}
    $ ./stitch-fai-ai.sh
    ```

按照上述指南完成构建后，GMSL 摄像头将在 /dev/ 下以 video4、video5、video6 和 video7 的形式提供。

#### 4.2.1.2 如何使用 MIPI1 端口
首先，必须同时启用 GMSL 摄像头和 SerDes 开发板的内核配置。  
将以下条目添加到  
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
修改上述选项后，使用以下命令重新构建镜像。
```
$ bitbake -c cleansstate isp-firmware
$ bitbake -c cleansstate isp-server
$ bitbake telechips-topst-image
```

接下来，必须修改内核中的设备树。请按照以下指南应用更改并重新构建镜像。
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
4. 重新构建内核并生成 FAI 镜像。  
    返回构建目录，并使用以下命令重新构建内核。
    ```
    $ cd ${build_dir}/build/ai-g-topst-main/
    $ bitbake -C compile linux-topst
    $ cd ${build_dir}
    $ ./stitch-fai-ai.sh
    ```

按照上述指南完成构建后，GMSL 摄像头将在 /dev/ 下以 video4、video5、video6 和 video7 的形式提供。

#### 4.2.1.3 如何使用 MIPI0、1 端口
首先，必须同时启用 GMSL 摄像头和 SerDes 开发板的内核配置。  
将以下条目添加到  
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

修改上述选项后，使用以下命令重新构建镜像。
```
$ bitbake -c cleansstate isp-firmware
$ bitbake -c cleansstate isp-server
$ bitbake telechips-topst-image
```

由于 VIOC 中 display 与 videoinput 路径存在重叠，因此无法使用 4-display 扩展。所以必须先在 display 配置中禁用其中一条冲突路径。
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

接下来，必须修改内核中的设备树。请按照以下指南应用更改并重新构建镜像。
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
5. 重新构建内核并生成 FAI 镜像。  
    返回构建目录，并使用以下命令重新构建内核
    ```
    $ cd ${build_dir}/build/ai-g-topst-main/
    $ bitbake -C compile linux-topst
    $ cd ${build_dir}
    $ ./stitch-fai-ai.sh
    ```
按照上述指南完成构建后，GMSL 摄像头将在 /dev/ 下以 video0、video1、video2、video3、4、video5、video6 和 video7 的形式提供。

### 4.2.2 AI-G GMSL 摄像头设置指南
使用 Deserializer 开发板，可以将最多四个摄像头连接到单个 MIPI CSI 端口。  
AI-G 开发板提供每通道 1.5 Gbps 的 MIPI CSI 数据带宽，最多可同时运行三路 FHD 摄像头。因此，本指南介绍三路 FHD GMSL 摄像头的连接方法。  
对于 HD 摄像头，最多可支持四台。

**注意：** 本指南使用 IMX290 (cxd5700) FHD GMSL 摄像头。  
如果打算使用其他 GMSL 摄像头，则需要进行额外的摄像头移植。

#### 4.2.2.1 如何使用 MIPI CSI 端口
首先，必须同时启用 GMSL 摄像头和 SerDes 开发板的内核配置。  
将以下条目添加到  
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
修改上述选项后，使用以下命令重新构建镜像。
```
$ bitbake -c cleansstate isp-firmware
$ bitbake -c cleansstate isp-server
$ bitbake telechips-topst-ai-image
```

接下来，必须修改内核中的设备树。请按照以下指南应用更改并重新构建镜像。
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
3. 重新构建内核并生成 FAI 镜像。  
    返回构建目录，并使用以下命令重新构建内核
    ```
    $ cd ${build_dir}/build/ai-g-topst-main/
    $ bitbake -C compile linux-topst
    $ cd ${build_dir}
    $ ./stitch-fai-ai.sh
    ```
按照上述指南完成构建后，GMSL 摄像头将在 /dev/ 下以 video0、video1 和 video2 的形式提供。

# 5. 示例代码和命令
本章提供示例代码和命令，演示如何在 D3-G 和 AI-G 平台上使用 MIPI CSI 摄像头、GMSL 摄像头和 USB 摄像头。本节简要概述摄像头播放方法：  
在 D3-G 上，可以使用 GStreamer 或 OpenCV 查看摄像头数据流，  
而在 AI-G 上，摄像头播放通过应用程序框架处理。

## 5.1 摄像头播放的示例代码和命令
### 5.1.1 MIPI CSI 摄像头用户指南
本节介绍如何在 Yocto 和 Ubuntu 两种环境中显示 MIPI CSI 摄像头视频。

#### 5.1.1.1 D3-G 上的 MIPI CSI 摄像头用户指南（OV5647）
##### 5.1.1.1.1 在 Yocto 镜像上使用 OV5647
使用 [topst.ai DOCS 页面](https://topst.ai/tech/docs?page=624bd237b3013e87c05c125b8031e2f370ccca2b) 提供的官方 Yocto 镜像，或通过手动构建 Yocto 生成的镜像时，OV5647 摄像头以 1296×972、30 fps 的默认分辨率工作。因此，在该环境中的摄像头播放将使用 1296×972、30 fps。  
请按照以下步骤操作：
1. 停止当前正在运行的 topst-welcome 服务
    ```
    $ sudo systemctl stop topst-welcome
    ```
2. 在 UART 控制台中输入以下命令
    ```
    $ export XDG_RUNTIME_DIR=/run/user/root
    ```
3. 按如下所示使用 GStreamer 命令播放摄像头流
    ```
    $ gst-launch-1.0 v4l2src device=/dev/video0 io-mode=2 ! video/x-raw,format=NV12,width=1296,height=972,framerate=30/1 ! videoconvert ! waylandsink sync=false
    ```
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/accessories/Camera/5.1%201296%C3%97972%20ov5647%20camera%20out%20display%20on%20yocto.png"></p>
<p align="center"><strong>图 5.1 Yocto 上的 1296×972 OV5647 摄像头输出显示</strong></p>

**注意：** 虽然分辨率为 1296×972，但在命令末尾添加 fullscreen=true 选项即可全屏播放视频。

##### 5.1.1.1.2 在 Ubuntu 镜像上使用 OV5647
使用 [topst.ai DOCS 页面](https://topst.ai/tech/docs?page=624bd237b3013e87c05c125b8031e2f370ccca2b) 提供的官方 Ubuntu 镜像时，OV5647 摄像头以 1296×972、30 fps 的默认分辨率工作。因此，在该环境中的摄像头播放将使用 1296×972、30 fps。  
请按照以下步骤操作：
1. - 如果通过 UART 连接：使用 topst 账户登录后，在 UART 控制台中输入以下命令
    ```
    $ export XDG_RUNTIME_DIR=/run/user/1000
    ```
    - 如果直接在显示器上进行操作：打开一个终端窗口
2. 使用如下所示的 GStreamer 命令播放摄像头视频流。由于 Ubuntu 上无法使用硬件加速的 Wayland 渲染，因此改用 H.265 编码/解码，以便利用 VPU 加速进行播放
    ```
    $ gst-launch-1.0 v4l2src device=/dev/video0 io-mode=2 ! video/x-raw,format=NV12,width=1280,height=720,framerate=30/1 ! v4l2h265enc ! h265parse ! v4l2h265dec ! videoconvert ! waylandsink sync=false
    ```
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/accessories/Camera/5.2%201296%C3%97972%20ov5647%20camera%20out%20display%20on%20ubuntu.png"></p>
<p align="center"><strong>图 5.2 Ubuntu 上的 1296×972 OV5647 摄像头输出显示</strong></p>

**注意：** 虽然分辨率为 1296×972，但在命令末尾添加 fullscreen=true 选项即可全屏播放视频。

除 GStreamer 外，您还可以使用 OpenCV 显示摄像头流。请按照以下步骤，使用 OpenCV 轻松预览摄像头视频。
1. 安装 OpenCV
    ```
    $ sudo apt-get install python3-opencv
    ```
2. 在 opencv_cam.py 文件中编写以下代码
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
3. 使用 Python 运行 opencv_cam.py
    ```
    $ python3 opencv_cam.py
    ```
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/accessories/Camera/5.3%201296%C3%97972%20opencv%20ov5647%20camera%20out%20display%20on%20ubuntu.png"></p>
<p align="center"><strong>图 5.3 在 Ubuntu 上使用 OpenCV 运行的 1296×972 OV5647 摄像头输出</strong></p>

##### 5.1.1.1.3 D3-G 上各分辨率的 Gstreawmer 管道配置
为每种分辨率指定合适的 GStreamer 管线选项，然后运行摄像头数据流。
1. 1920x1080 @ 30fps
    ```
    $ gst-launch-1.0 v4l2src device=/dev/video0 io-mode=2 ! video/x-raw,format=NV12,width=1920,height=1080,framerate=30/1 ! videoconvert ! waylandsink sync=false
    ```
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/accessories/Camera/5.4%201920x1080%20ov5647%20camera%20out%20display%20on%20yocto.png"></p>
    <p align="center"><strong>图 5.4 Yocto 上 1920x1080 OV5647 摄像头输出显示</strong></p>
2. 1296x972 @ 30fps
    ```
    $ gst-launch-1.0 v4l2src device=/dev/video0 io-mode=2 ! video/x-raw,format=NV12,width=1296,height=972,framerate=30/1 ! videoconvert ! waylandsink sync=false
    ```
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/accessories/Camera/5.1%201296%C3%97972%20ov5647%20camera%20out%20display%20on%20yocto.png"></p>
    <p align="center"><strong>图 5.5 Yocto 上 1296x972 OV5647 摄像头输出显示</strong></p>
3. 640x480 @ 60fps
    ```
    $ gst-launch-1.0 v4l2src device=/dev/video0 io-mode=2 ! video/x-raw,format=NV12,width=640,height=480,framerate=60/1 ! videoconvert ! waylandsink sync=false
    ```
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/accessories/Camera/5.6%20640x480%20ov5647%20camera%20out%20display%20on%20yocto.png"></p>
    <p align="center"><strong>图 5.6 Yocto 上 640x480 OV5647 摄像头输出显示</strong></p>

此外，您可以配置使用 H.265 编码器和解码器的流水线，以启用硬件加速播放。
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

    有关分辨率的更改，请参阅第 4.1.2.2 节。

#### 5.1.1.2 D3-G 上的 MIPI CSI 摄像头用户指南（IMX219）
##### 5.1.1.2.1 在 Yocto 镜像上使用 IMX219
使用 [topst.ai DOCS 页面](https://topst.ai/tech/docs?page=624bd237b3013e87c05c125b8031e2f370ccca2b) 提供的官方 Yocto 镜像，或通过手动构建 Yocto 生成的镜像时，IMX219 摄像头以 1640×1232、30 fps 的默认分辨率工作。因此，在该环境中的摄像头播放将使用 1640×1232、30 fps。  
请按照以下步骤操作：
1. 停止当前正在运行的 topst-welcome 服务
    ```
    $ sudo systemctl stop topst-welcome
    ```
2. 在 UART 控制台中输入以下命令
    ```
    $ export XDG_RUNTIME_DIR=/run/user/root
    ```
3. 按如下所示使用 GSTreamer 命令播放摄像头流
    ```
    $ gst-launch-1.0 v4l2src device=/dev/video0 io-mode=2 ! video/x-raw,format=NV12,width=1640,height=1232,framerate=30/1 ! videoconvert ! waylandsink sync=false
    ```
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/accessories/Camera/5.7%201640x1232%20imx219%20camera%20out%20display%20on%20yocto.png"></p>
<p align="center"><strong>图 5.7 Yocto 上的 1640x972 IMX219 摄像头输出显示</strong></p>

**注意：** 虽然分辨率为 1640×1232，但在命令末尾添加 fullscreen=true 选项即可全屏播放视频。

##### 5.1.1.2.2 在 Ubuntu 镜像上使用 IMX219
使用 [topst.ai DOCS 页面](https://topst.ai/tech/docs?page=624bd237b3013e87c05c125b8031e2f370ccca2b) 提供的官方 Ubuntu 镜像时，IMX219 摄像头以 1640×1232、30 fps 的默认分辨率工作。因此，在该环境中的摄像头播放将使用 1640×1232、30 fps。  
请按照以下步骤操作：
1. - 如果通过 UART 连接：使用 topst 账户登录后，在 UART 控制台中输入以下命令
    ```
    $ export XDG_RUNTIME_DIR=/run/user/1000
    ```
    - 如果直接在显示器上进行操作：打开一个终端窗口
2. 使用如下所示的 GStreamer 命令播放摄像头视频流。由于 Ubuntu 上无法使用硬件加速的 Wayland 渲染，因此改用 H.265 编码/解码，以便利用 VPU 加速进行播放
    ```
    $ gst-launch-1.0 v4l2src device=/dev/video0 io-mode=2 ! video/x-raw,format=NV12,width=1600,height=1200,framerate=30/1 ! v4l2h265enc ! h265parse ! v4l2h265dec ! videoconvert ! waylandsink sync=false
    ```
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/accessories/Camera/5.8%201640x1232%20imx219%20camera%20out%20display%20on%20ubuntu.png"></p>
<p align="center"><strong>图 5.8 Ubuntu 上的 1640x972 IMX219 摄像头输出显示</strong></p>

**注意：** 虽然分辨率为 1640×1232，但在命令末尾添加 fullscreen=true 选项即可全屏播放视频。

除 GStreamer 外，您还可以使用 OpenCV 显示摄像头流。请按照以下步骤，使用 OpenCV 轻松预览摄像头视频。
1. 安装 OpenCV
    ```
    $ sudo apt-get install python3-opencv
    ```
2. 在 opencv_cam.py 文件中编写以下代码。
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
3. 使用 Python 运行 opencv_cam.py
```
$ python3 opencv_cam.py
```
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/accessories/Camera/5.9%201640x1232%20opencv%20imx219%20camera%20out%20display.png"></p>
<p align="center"><strong>图 5.9 在 Ubuntu 上使用 OpenCV 运行的 1640×1232 IMX219 摄像头输出</strong></p>

##### 5.1.1.2.3 D3-G 上各分辨率的 GStreamer 管道配置
为每种分辨率指定合适的 GStreamer 管线选项，然后运行摄像头数据流。
1. 1920x1080 @ 30fps
    ```
    $ gst-launch-1.0 v4l2src device=/dev/video0 io-mode=2 ! video/x-raw,format=NV12,width=1920,height=1080,framerate=30/1 ! videoconvert ! waylandsink sync=false
    ```
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/accessories/Camera/5.10%201920x1080%20imx219%20camera%20out%20display%20on%20yocto.png"></p>
    <p align="center"><strong>图 5.10 Yocto 上 1920x1080 IMX219 摄像头输出显示</strong></p>
2. 1640x1232 @ 30fps
    ```
    $ gst-launch-1.0 v4l2src device=/dev/video0 io-mode=2 ! video/x-raw,format=NV12,width=1640,height=1232,framerate=30/1 ! videoconvert ! waylandsink sync=false
    ```
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/accessories/Camera/5.7%201640x1232%20imx219%20camera%20out%20display%20on%20yocto.png"></p>
    <p align="center"><strong>图 5.11 Yocto 上 1620x1232 IMX219 摄像头输出显示</strong></p>
3. 640x480 @ 30fps
    ```
    $ gst-launch-1.0 v4l2src device=/dev/video0 io-mode=2 ! video/x-raw,format=NV12,width=640,height=480,framerate=30/1 ! videoconvert ! waylandsink sync=false
    ```
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/accessories/Camera/5.12%20640x480%20imx219%20camera%20out%20display%20on%20yocto.png"></p>
    <p align="center"><strong>图 5.12 Yocto 上 640x480 IMX219 摄像头输出显示</strong></p>

此外，您可以配置使用 H.265 编码器和解码器的流水线，以启用硬件加速播放。
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

有关分辨率更改，请参阅第 4.1.3.3 节。

#### 5.1.1.3 AI-G 上的 MIPI CSI 摄像头用户指南（OV5647）
##### 5.1.1.3.1 在 Yocto 镜像上使用 OV5647
在 AI-G 上提供两个应用程序：一个用于带推理结果的摄像头播放，另一个用于简单的摄像头预览。您可以根据使用场景选择其中任一应用程序。
- tcnnapp
    ```
    $ tcnnapp
    ```
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/accessories/Camera/5.13%20ov5647%20camera%20out%20display%20with%20running%20tcnnapp%20on%20yocto.png"></p>
    <p align="center"><strong>图 5.13 在 Yocto 上运行 tcnnapp 时的 OV5647 摄像头输出显示</strong></p>
- tcnncameraapp
    ```
    $ tcnncameraapp
    ```
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/accessories/Camera/5.14%20ov5647%20camera%20out%20display%20with%20running%20tcnncameraapp%20on%20yocto.png"></p>
    <p align="center"><strong>图 5.14 在 Yocto 上运行 tcnncameraapp 时的 OV5647 摄像头输出显示</strong></p>

##### 5.1.1.3.2 在 Ubuntu 镜像上使用
在 AI-G 上提供两个应用程序：一个用于带推理结果的摄像头播放，另一个用于简单的摄像头预览。您可以根据使用场景选择其中任一应用程序。
- tcnnapp
    ```
    $ tcnnapp
    ```
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/accessories/Camera/5.13%20ov5647%20camera%20out%20display%20with%20running%20tcnnapp%20on%20yocto.png"></p>
    <p align="center"><strong>图 5.15 在 Ubuntu 上运行 tcnnapp 时的 OV5647 摄像头输出显示</strong></p>
- tcnncameraapp
    ```
    $ tcnncameraapp
    ```
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/accessories/Camera/5.14%20ov5647%20camera%20out%20display%20with%20running%20tcnncameraapp%20on%20yocto.png"></p>
    <p align="center"><strong>图 5.16 在 Ubuntu 上运行 tcnncameraapp 时的 OV5647 摄像头输出显示</strong></p>

#### 5.1.1.4 AI-G 上的 MIPI CSI 摄像头用户指南（IMX219）
##### 5.1.1.4.1 在 Yocto 镜像上使用 IMX219
在 AI-G 上提供两个应用程序：一个用于带推理结果的摄像头播放，另一个用于简单的摄像头预览。您可以根据使用场景选择其中任一应用程序。
- tcnnapp
    ```
    $ tcnnapp
    ```
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/accessories/Camera/5.17%20imx219%20camera%20out%20display%20with%20running%20tcnnapp%20on%20yocto.png"></p>
    <p align="center"><strong>图 5.17 在 Yocto 上运行 tcnnapp 时的 OV5647 摄像头输出显示</strong></p>
- tcnncameraapp
    ```
    $ tcnncameraapp
    ```
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/accessories/Camera/5.18%20imx219%20camera%20out%20display%20with%20running%20tcnncameraapp%20on%20yocto.png"></p>
    <p align="center"><strong>图 5.18 在 Yocto 上运行 tcnncameraapp 时的 OV5647 摄像头输出显示</strong></p>

##### 5.1.1.4.2 在 Ubuntu 镜像上使用 IMX219
在 AI-G 上提供两个应用程序：一个用于带推理结果的摄像头播放，另一个用于简单的摄像头预览。您可以根据使用场景选择其中任一应用程序。
- tcnnapp
    ```
    $ tcnnapp
    ```
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/accessories/Camera/5.17%20imx219%20camera%20out%20display%20with%20running%20tcnnapp%20on%20yocto.png"></p>
    <p align="center"><strong>图 5.17 在 Yocto 上运行 tcnnapp 时的 OV5647 摄像头输出显示</strong></p>
- tcnncameraapp
    ```
    $ tcnncameraapp
    ```
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/accessories/Camera/5.18%20imx219%20camera%20out%20display%20with%20running%20tcnncameraapp%20on%20yocto.png"></p>
    <p align="center"><strong>图 5.18 在 Yocto 上运行 tcnncameraapp 时的 OV5647 摄像头输出显示</strong></p>

### 5.1.2 GMSL 摄像头用户指南
本节介绍如何在 Yocto 和 Ubuntu 两种环境中显示 GMSL 摄像头视频。

#### 5.1.2.1 D3-G 上的 GMSL 摄像头用户指南
##### 5.1.2.1.1 在 Yocto 镜像上使用 GMSL 摄像头
使用 [topst.ai DOCS 页面](https://topst.ai/tech/docs?page=624bd237b3013e87c05c125b8031e2f370ccca2b) 提供的官方 Yocto 镜像，或通过手动构建 Yocto 生成的镜像时，GMSL 摄像头以 1920×1080、30 fps 的默认分辨率工作。因此，在该环境中的摄像头播放将使用 1920×1080、30 fps。  
请按照以下步骤操作：
1. 停止当前正在运行的 topst-welcome 服务
    ```
    $ sudo systemctl stop topst-welcome
    ```
2. 在 UART 控制台中输入以下命令
    ```
    $ export XDG_RUNTIME_DIR=/run/user/root
    ```
3. 按如下所示使用 GStreamer 命令播放摄像头流
    ```
    $ gst-launch-1.0 v4l2src device=/dev/video4 io-mode=2 ! video/x-raw,format=NV12,width=1920,height=1080,framerate=30/1 ! videoconvert ! waylandsink sync=false
    ```

此外，运行以下脚本可以使用 gpu 以四分屏方式显示摄像头画面。
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

GMSL 摄像头显示为 video4、video5、video6 和 video7，您可以根据需要选择其中任意设备。  
如果连接了八个摄像头，系统会将它们枚举为 video0 至 video8，您可以从这些设备节点中任意选择。

##### 5.1.2.1.2 在 Ubuntu 镜像上使用 GMSL 摄像头
使用 [topst.ai DOCS 页面](https://topst.ai/tech/docs?page=624bd237b3013e87c05c125b8031e2f370ccca2b) 提供的官方 Ubuntu 镜像时，GMSL 摄像头以 1920×1080、30 fps 的默认分辨率工作。因此，在该环境中的摄像头播放将使用 1920×1080、30 fps。  
请按照以下步骤操作：
1. - 如果通过 UART 连接：使用 topst 账户登录后，在 UART 控制台中输入以下命令
    ```
    $ export XDG_RUNTIME_DIR=/run/user/1000
    ```
    - 如果直接在显示器上进行操作：打开一个终端窗口
2. 使用如下所示的 GStreamer 命令播放摄像头视频流。由于 Ubuntu 上无法使用硬件加速的 Wayland 渲染，因此改用 H.265 编码/解码，以便利用 VPU 加速进行播放
    ```
    $ gst-launch-1.0 v4l2src device=/dev/video0 io-mode=2 ! video/x-raw,format=NV12,width=1920,height=1080,framerate=30/1 ! v4l2h265enc ! h265parse ! v4l2h265dec ! videoconvert ! waylandsink sync=false
    ```

此外，运行以下脚本可以使用 gpu 以四分屏方式显示摄像头画面。
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

此外，您还可以使用 OpenCV 显示摄像头流。请按照以下步骤，使用 OpenCV 轻松预览摄像头视频。
1. 安装 OpenCV
    ```
    $ sudo apt-get install python3-opencv
    ```
2. 在 opencv_cam.py 文件中编写以下代码
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
3. 使用 Python 运行 opencv_cam.py 文件
    ```
    $ python3 opencv_cam.py
    ```

GMSL 摄像头显示为 video4、video5、video6 和 video7，您可以根据需要选择其中任意设备。  
如果连接了八个摄像头，系统会将它们枚举为 video0 至 video8，您可以从这些设备节点中任意选择。

#### 5.1.2.2 AI-G 上的 GMSL 摄像头用户指南
##### 5.1.2.2.1 在 Yocto 镜像上使用 GMSL 摄像头
在 AI-G 上提供两个应用程序：一个用于带推理结果的摄像头播放，另一个用于简单的摄像头预览。您可以根据使用场景选择其中任一应用程序。
- tcnnapp
- tcnncameraapp

GMSL 摄像头显示为 **video0**、**video1** 和 **video2**，您可以根据需要选择其中任意设备。
每个应用程序默认使用 video2，但您可以使用 **-p 选项**更改视频设备。
下面的示例演示如何选择 **video0**。

- tcnnapp
    ```
    $ tcnnapp -p /dev/video0
    ```
- tcnncameraapp
    ```
    $ tcnncameraapp -p /dev/video0
    ```

##### 5.1.2.2.2 在 Ubuntu 镜像上使用 GMSL 摄像头
在 AI-G 上提供两个应用程序：一个用于带推理结果的摄像头播放，另一个用于简单的摄像头预览。您可以根据使用场景选择其中任一应用程序。
- tcnnapp
- tcnncameraapp

GMSL 摄像头显示为 **video0**、**video1** 和 **video2**，您可以根据需要选择其中任意设备。
每个应用程序默认使用 video2，但您可以使用 **-p 选项**更改视频设备。
下面的示例演示如何选择 **video0**。

- tcnnapp
    ```
    $ tcnnapp -p /dev/video0
    ```
- tcnncameraapp
    ```
    $ tcnncameraapp -p /dev/video0
    ```

### 5.1.3 USB 摄像头用户指南
本节介绍如何在 Yocto 和 Ubuntu 两种环境中显示 USB 摄像头视频。
AI-G 不包含 USB 接口，因此不为该平台提供 USB 摄像头指南。

#### 5.1.3.1 D3-G 上的 USB 摄像头用户指南
本文档以支持 1920×1080 30 fps 的 USB 摄像头为基础进行说明

**注意：** 由于 MIPI 摄像头默认分配到 **/dev/video0**，因此 USB 摄像头会被创建为 /dev/video1。
操作 USB 摄像头时，请务必使用 **/dev/video1**。

##### 5.1.3.1.1 在 Yocto 镜像上使用 USB 摄像头
使用 [topst.ai DOCS 页面](https://topst.ai/tech/docs?page=624bd237b3013e87c05c125b8031e2f370ccca2b) 提供的官方 Yocto 镜像，或通过手动构建 Yocto 生成的镜像时，USB 摄像头将按照摄像头自身规格所定义的分辨率和帧率工作。因此，视频将以 USB 摄像头提供的默认分辨率和 FPS 播放。  
请按照以下步骤操作：
1. 停止当前正在运行的 topst-welcome 服务
    ```
    $ sudo systemctl stop topst-welcome
    ```
2. 在 UART 控制台中输入以下命令
    ```
    $ export XDG_RUNTIME_DIR=/run/user/root
    ```
3. 按如下所示使用 GStreamer 命令播放摄像头流。使用 v4l2-ctl -d /dev/video1 --list-formats-ext 查看 USB 摄像头信息时，支持的格式显示为 MJPEG。因此使用 jpegdec
    ```
    $ gst-launch-1.0 v4l2src device=/dev/video1 ! image/jpeg,width=1920,height=1080 ! jpegdec ! videoconvert ! waylandsink
    ```

##### 5.1.3.1.2 在 Ubuntu 镜像上使用 USB 摄像头
使用 [topst.ai DOCS 页面](https://topst.ai/tech/docs?page=624bd237b3013e87c05c125b8031e2f370ccca2b) 提供的官方 Ubuntu 镜像或手动生成的镜像时，USB 摄像头将按照摄像头自身规格所定义的分辨率和帧率工作。因此，视频将以 USB 摄像头提供的默认分辨率和 FPS 播放。  
请按照以下步骤操作：
1. - 如果通过 UART 连接：使用 topst 账户登录后，在 UART 控制台中输入以下命令
    ```
    $ export XDG_RUNTIME_DIR=/run/user/1000
    ```
    - 如果直接在显示器上进行操作：打开一个终端窗口
2. 按如下所示使用 GStreamer 命令播放摄像头流。使用 v4l2-ctl -d /dev/video1 --list-formats-ext 查看 USB 摄像头信息时，支持的格式显示为 MJPEG。因此使用 jpegdec
    ```
    $ gst-launch-1.0 v4l2src device=/dev/video1 ! image/jpeg,width=1920,height=1080 ! jpegdec ! videoconvert ! waylandsink
    ```
3. 要使用 H.265 编码和解码，必须将视频转换为 v4l2src 支持的 NV12 格式。因此，应按如下所示配置流水线
    ```
    $ gst-launch-1.0 v4l2src device=/dev/video1 io-mode=2 ! image/jpeg,width=640,height=480,framerate=30/1 ! jpegdec ! videoconvert ! video/x-raw,format=NV12 !  v4l2h265enc ! h265parse ! v4l2h265dec ! videoconvert ! waylandsink
    ```

**注意：** 在命令末尾添加 fullscreen=true 选项即可全屏播放视频。

除 GStreamer 外，您还可以使用 OpenCV 显示摄像头流。请按照以下步骤，使用 OpenCV 轻松预览摄像头视频。
1. 安装 OpenCV
    ```
    $ sudo apt-get install python3-opencv
    ```
2. 在 opencv_cam.py 文件中编写以下代码
    ```
    import cv2

    cap = cv2.VideoCapture(1)

    if not cap.isOpened():
        print("\\@@ Camera open failed!")
        exit()

    print("按 'q' 键退出摄像头窗口。")

    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

    while True:
        ret, frame = cap.read()
        if not ret:
            print("读取帧失败")
            break

        cv2.imshow("Camera Feed", frame)

        # 按下 'q' 键则退出
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
    ```
3. 使用 Python 运行 opencv_cam.py
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

    print("正在打开管道...")
    cap = cv2.VideoCapture(pipeline, cv2.CAP_GSTREAMER)

    if not cap.isOpened():
        print("打开管道失败")
        exit()

    print("按 'q' 键退出摄像头窗口。")

    while True:
        ret, frame = cap.read()
        if not ret:
            print("读取帧失败")
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

# 6. 故障排除
第 6 章介绍 MIPI CSI 摄像头、GMSL 摄像头和 USB 摄像头的故障排除。

## 6.1 MIPI CSI 和 GMSL 摄像头故障排除
如果 MIPI CSI 或 GMSL 摄像头出现问题，请参阅以下调试指南进行故障排除。

### 6.1.1 启动时的问题（探测阶段）
#### 6.1.1.1 传感器探测失败
**症状**
- 启动过程中未检测到传感器
- 未创建 /dev/videoX 节点
- ‘media-ctrl -p’ 的输出中未出现传感器实体  

**dmesg 日志示例**
```
[    3.421000] imx219 2-0010: probing sensor failed
[    3.421120] imx219 2-0010: i2c read failed: addr=0x3000, ret=-5
[    3.200400] imx219 0-0010: reset gpio request failed
[    2.912830] imx219 1-0010: failed to get vddio regulator
```
**可能的原因**
- I2C 地址或总线配置错误
- RESET/PWDN GPIO 极性错误
- 缺少 regulator 供电或其配置不正确

**解决方法**
- 确认设备树中的 I2C 地址、总线编号和 GPIO 设置
- 检查是否存在缺失或定义错误的 regulator 节点
- 重新检查传感器模块线缆的方向和引脚对齐情况

#### 6.1.1.2 I2C 通信失败
**dmesg 日志示例**
```
[    3.101001] imx219 2-0010: i2c read error: -121
[    4.112121] i2c i2c-2: transfer failed: -110
```
**可能的原因**
- SDA/SCL 线短路或断开
- 设备树中的 I2C 总线编号与实际硬件配置不匹配

**解决方法**
- 使用 “i2cdetect -y <bus>” 检查传感器是否在预期的 I2C 地址上响应
- 检查线缆和连接器是否存在损坏、插接不到位或接触松动

### 6.1.2 媒体控制器与图配置问题
（使用 ‘media-ctl -p’ 进行验证）

#### 6.1.2.1 缺少传感器实体或链路未配置
**'media-ctl -p' 输出示例**
```
0 entities, 0 interfaces, 0 pads, 0 links
```
**可能的原因**
- 设备树中缺少 endpoint（port）节点
- 通道数量或 ‘bus-type’ 设置错误
- 缺少 ‘link-frequencies’ 条目

**解决方法**
- 确认 ‘port@0/1’ endpoint 定义是否正确
- 检查 ‘data-lanes’ 数组的顺序和通道数量是否正确
- 确保 ‘link-frequencies’ 与传感器规格一致

#### 6.1.2.2 格式 / 模式不匹配
**可能的原因**
- 传感器驱动程序中的 ‘supported_mode[]’ 与 DTS 中定义的 ‘hs-settle’ 值不匹配
- 驱动程序与设备树之间的 CSI-2 通道数量不一致

**解决方法**
- 检查 ‘supported_modes[]’ 中的分辨率、像素速率和 HTS/VTS 值，然后相应调整 DTS 中的 ‘hs-settle’ 值
- 确保 DTS 配置与传感器驱动程序设置保持一致

### 6.1.3 V4L2 流传输问题
#### 6.1.3.1 VIDIOC_STREAMON 失败（无法开始流传输）
**可能的原因**
- 传感器寄存器配置错误
- 像素速率或 PLL 设置与预期值不符
- HTS/VTS 冲突导致帧时序无效

**解决方法**
- 重新校验传感器模式表中的像素速率、VTS 和 HTS 值
- 检查 PLL 分频值（0x030x 寄存器）是否正确
- 确认设备树为所选分辨率和 FPS 指定了正确的 ‘hs-settle’ 值。

#### 6.1.3.2 请求了不支持的格式
**解决方法**
- 使用下面的命令检查实际支持的格式，然后使用受支持的格式重新尝试推流：
    ```
    V4l2-ctl –list-formats-ext
    ```

### 6.1.4 CSI-2 错误：SoT、CRC 及相关问题
#### 6.1.4.1 SoT (Sync on Transmission) 错误
**可能的原因**
- MIPI 时序配置不匹配
- 像素速率设置过高
- 线缆质量差或线缆长度过长

**解决方法**
- 降低像素速率或链路频率
- 更换线缆或缩短线缆长度
- 确认 MIPI 时序参数

#### 6.1.4.2 CRC 错误
**dmesg 日志示例**
```
[   13.700910] tccvin videoinput0: CSI-2 ERROR: CRC error
```
**可能的原因**
- MIPI 信号质量下降
- PLL 或通道速率不匹配

**解决方法**
- 调整 hs-settle 值
- 更换线缆
- 确认 PLL 配置和通道速率设置

### 6.1.5 像素率 / 链路频率错误
**可能的原因**
- 超出可用的 CSI-2 通道带宽
- PLL 配置错误

**解决方法**
- 重新计算像素速率，确保其处于允许的 CSI-2 带宽范围内
- 调整 PLL 分频系数以获得有效的时序
- 必要时降低帧率（例如 30 -> 15fps）或降低分辨率

### 6.1.6 设备树（DTS）配置错误
#### 6.1.6.1 不兼容的 compatible 字符串
**可能的原因**
- DTS 中的 ‘compatible’ 值与传感器驱动程序中定义的 ‘of_device_id’ 不匹配
- 驱动程序无法识别设备节点，导致 probe 无法运行

**解决方法**
- 使用传感器驱动程序中定义的准确 ‘compatible’ 字符串（例如 “sony,imx219”）更新 DTS
- 重新构建设备树，并确认传感器能够正确 probe

#### 6.1.6.2 端点配置问题
**可能的原因**
- 传感器 endpoint 与 CSI endpoint 之间的端口号或 ‘remote-endpoint’ 引用不匹配
- ‘data-lanes’ 或总线配置不满足媒体图的要求

**解决方法**
- 确保两侧的端口号、‘data-lanes’ 和 ‘remote-endpoint’ 值相互匹配
- 使用 ‘media-ctl -p’ 确认媒体链路已正确建立

#### 缺少 Link-Frequencies 属性
**可能的原因**
- endpoint 中缺少 ‘link-frequencies’ 字段，导致无法计算 MIPI 链路速率
- 取值格式（例如 /bits/ 64）与驱动程序的预期不符

**解决方法**
- 根据传感器规格添加正确的 ‘link-frequencies’ 值（例如 456000000）
- 确保取值格式符合驱动程序的要求（例如在需要时包含 /bits/ 64）

### 6.1.7 Gstreamer 播放问题
#### 6.1.7.1 'not negotiated' 错误
**可能的原因**
- 管道内的 Caps 协商失败
- Wayland 合成器格式不匹配
- videoconvert 无法处理某些 raw 格式

**解决方法**
- 使用兼容性较广的 NV12 或 YUY2 流水线
- 利用 ‘v4l2src io-mode=dmabuf’ 以确保零拷贝缓冲区处理和正确的格式协商

#### 6.1.7.2 Wayland Sink 初始化失败
**可能的原因**
- Wayland 合成器未运行，或没有可访问的显示环境
- 流水线通过 SSH 启动，或 DISPLAY/Wayland 环境无效，导致 sink 无法初始化

**解决方法**
- 确认 Weston 合成器正在运行
- 在本地会话或已正确配置的 Wayland 环境中执行该流水线

### 6.1.8 硬件问题
#### 6.1.8.1 线缆方向不正确
**可能的原因**
- FFC 线缆连接方向错误或引脚未对齐，导致 I2C/MIPI 信号无法正常传输
- 传感器完全无响应，导致接收不到帧

**解决方法**
- 确认连接器方向，并确保触点引脚按照规格对齐
- 检查线缆是否损坏或触点是否磨损

#### 6.1.8.2 供电问题
**可能的原因**
- 传感器电压轨（例如 1.2V / 2.8V）不稳定或未使能
- 未置位电源使能 GPIO
- 初始化期间未满足传感器的上电时序

**解决方法**
- 检查 DTS 中的 regulator 和 GPIO 配置，确认所有所需电压均已正确供给
- 确保满足传感器的电源时序要求（RESET _> PWDN -> clock enable）

## 6.2 USB 摄像头故障排除
如果 USB Camera 出现问题，请参阅以下调试指南进行故障排除。

### 6.2.1 未检测到摄像头（USB 设备未被识别）
**dmesg 日志示例**
```
usb 1-1: device descriptor read/64, error -71
uvcvideo: Failed to initialize the device
```
**可能的原因**
- USB 供电不足或供电不稳定，导致设备初始化失败
- USB 线缆或端口故障，或使用了不兼容的 USB 集线器

**解决方法**
- 尝试其他 USB 端口，或使用电源稳定的端口
- 更换 USB 线缆或集线器并重新连接设备，以确保正确枚举

### 6.2.2 v4l2-ctl 中的格式列表受限或为空
**dmesg 日志示例**
```
uvcvideo: Failed to query (GET_DEF) UVC control 2 on unit 1: -32
```
**可能的原因**
- 摄像头不支持某些 UVC 控制项，或在初始化期间未能报告这些控制项
- 设备与驱动程序之间的协议错误导致无法检测设备能力

**解决方法**
- 使用 MJPEG 或 YUYV 等标准格式进行测试
- 使用同型号的另一台摄像头进行测试，以确定该问题是否与 UVC 兼容性有关

### 6.2.3 GStreamer 播放："not negotiated" 或 Caps 不匹配
**可能的原因**
- 流水线请求了摄像头不支持的格式（例如 NV12、YUY2），导致 caps 协商失败
- 在所选的分辨率/帧率下，摄像头可能仅提供 MJPEG，而管道请求的是 raw 格式
- 摄像头输出 MJPEG，但未包含 JPEG 解码元件（jpegdec 或 avdec_mjpeg），因此无法完成解码

**解决方法**
- 检查支持的格式
    ```
    v4l2-ctl –list-formats-ext
    ```
- 如果摄像头输出 MJPEG：
    ```
    v4l2src ! image/jpeg ! jpegdec ! videoconvert ! …
    ```
- 如果摄像头支持 raw 格式（例如 YUYV），请相应配置流水线的 caps：  
    请完全按照 ‘v4l2-ctl –list-formats-ext’ 中列出的 raw 格式使用

### 6.2.4 分辨率或 FPS 设置失败
**可能的原因**
- 摄像头不支持所请求的分辨率或帧率，导致协商失败

**解决方法**
- 使用 ‘v4l2-ctl –list-formats-ext’ 检查支持的分辨率/FPS 组合

### 6.2.5 视频卡顿 / 丢帧
**可能的原因**
- USB 带宽不足（共享集线器或使用 USB 2.0 端口）
- MJPEG 解码导致 CPU 负载过高，使流水线处理滞后

**解决方法**
- 使用 USB 3.0 端口，或不经集线器直接连接摄像头
- 降低 MJPEG 分辨率或帧率，或在支持的情况下切换为 raw 格式

### 6.2.6 颜色不正确或输出损坏
**可能的原因**
- MJPEG -> NV12 转换或色彩空间转换过程中出错
- 某些格式组合在 v4l2convert 或 videoconvert 中可能会失败

**解决方法**
- 在 videoconvert 之前显式插入 jpegdec 或 avdec_mjpeg
- 为便于测试，请简化流水线，例如：
    ```
    V4l2src ! jpegdec ! videoconvert ! waylandsink
    ```

### 6.2.7 设备意外断开或重新枚举
**dmesg 日志示例**
```
usb 1-1: USB disconnect, device number 4
```
**可能的原因**
- 供电不稳定或线缆接触不良
- 散热问题导致设备在长时间使用过程中复位

**解决方法**
- 更换 USB 线缆，或使用供电稳定且充足的端口
- 对于发热量较大的摄像头，请考虑增加散热方案
