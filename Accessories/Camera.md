# 1. Introduction
This guide is designed to help engineers quickly bring up camera inputs on the TOPST D3-G and AI-G platforms and perform rapid preliminary validation for AI vision workloads. It aims to reduce the complexity of initial setup including hardware connections, device tree configuration, drivers, and pipeline preparation and provide a clear, reproducible path from power-on to the first video frame and ultimately the first inference.

## 1.1 Scope
- **Supported Interfaces:** MIPI CSI-2, GMSL (SerDes-based), USB UVC
- **Software Components:** Yocto-based BSP configuration, device tree overlays, V4L2, GStreamer, OpenCV, and integration with the D3-G and AI-G SDKs
- **Applicable Use Cases:** Robotics, drones, and industrial automation applications such as inspection, safety monitoring, and object tracking
- **Out-of-Scope Items:** Camera ISP tuning, advanced calibration workflows (stereo/IMU), and complete end-to-end application frameworks

## 1.2 Intended Audience
- Embedded and AI engineers integrating cameras into the D3-G or AI-G platforms for PoC or pilot development
- System integrators deploying or validating systems that rely on multi-camera pipelines
- Educators and laboratory users who require a repeatable, hands-on environment for training and experimentation

## 1.3 Structure of This Guide
- **Hardware Connections:** Connector pinouts, lane configuration, power and ground requirements, cable handling guidelines, and reference wiring diagrams
- **Software Configuration:** BSP setup including drivers and device tree configuration, along with methods to verify devices through udev and V4L2
- **Pipelines and Examples:** GStreamer and OpenCV commands and scripts for single- and multi-camera preview and capture
- **Troubleshooting:** Common issues, typical dmesg patterns, I²C probing tips, timing-related problems, and performance verification methods

## 1.4 Prerequisites
- **Hardware:** TOPST D3-G or AI-G board, supported camera modules, and the required cables/adapters (MIPI FPC, coaxial cables for GMSL, USB 3.0 etc.)
- **Host Tools:** Serial console access, SSH client, and basic build/debug utilities
- **Technical Background:** Familiarity with Linux shell operations, V4L2 utilities, and fundamental device tree concepts
- **Images/SDK:** D3-G, AI-G BSP image(d3-g version ≥ v1.3.0, ai-g version ≥1.1.0)
  

# 2. Camera Interface Overview
Chapter 2 describes the camera types supported on the D3-G and AI-G boards, respectively.  
Table 2.1 presents the board support matrix for the D3-G and AI-G platforms.

<p align="center"><strong>Table 2.1 Board Support matrix</strong></p>
<div align="center">
    <table>
        <tr>
            <td colspan="3" align="center"><strong>Item</strong></td>
            <td align="center"><strong>D3-G</strong></td>
            <td align="center"><strong>AI-G</strong></td>
        </tr>
        <tr>
            <td colspan="3">OS Support</td>
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
            <td>Not support</td>
        </tr>
    </table>
</div>

## 2.1 MIPI Camera Overview
A MIPI camera is an image sensor–based camera module that connects directly to the processor through the **MIPI CSI-2 (Mobile Industry Processor Interface – Camera Serial Interface 2)** standard. It is the most widely used camera interface in smartphones, embedded boards, and AI-based camera systems, offering advantages such as low power consumption, high bandwidth, and low latency.  
MIPI CSI-2 cameras typically provide RAW Bayer sensor output directly to the system, with image signal processing (ISP) handled either by the internal ISP within the SoC or by an external ISP. Unlike USB cameras, MIPI sensors require initialization through I2C register configuration and setup of the ISP pipeline, but in return, they allow high-quality image processing that fully leverages the sensor’s performance.  
MIPI cameras are widely used in embedded platforms for the following reasons:
- **High bandwidth:** With 2-lane or 4-lane configurations, MIPI cameras can reliably transmit high-resolution (4K and above) and high-frame-rate data.
- **Low power consumption:** Designed for mobile and embedded devices, the power usage is significantly lower than alternatives.
- **Direct sensor control:** Sensor parameters such as exposure, gain, and frame rate can be controlled through I2C, allowing fine-tuned image quality adjustments.
- **low latency:** Because RAW data is delivered directly, MIPI cameras are suited for real-time applications such as robotics and embedded vision systems.
- **Wide sensor availability:** Numerous sensors—including Sony IMX series (IMX219, IMX708, etc.) and Omnivision OV series—can be used under the same CSI-2 standard.  

MIPI cameras use connectors such as **15-pin (2-lane)** or **20-pin (4-lane)** FFC cables, and proper lane configuration and pin mapping must match the board’s CSI port.  
On Linux-based systems, the sensor driver (including the device tree configuration) must be properly set up for the camera to be recognized as a /dev/video* device or a Media Controller node. Once detected, video streaming can be accessed through the V4L2 framework.  
Due to these characteristics, MIPI cameras have become the de facto standard interface for high-quality image processing, low-latency streaming, and AI-driven embedded vision applications.

## 2.2 GMSL Camera Overview
A GMSL camera is a serialized camera module that transmits image data, control signals, and power over a single coaxial or shielded twisted-pair cable using the Gigabit Multimedia Serial Link (GMSL) standard. Unlike MIPI cameras, which require short FFC connections, GMSL uses a serializer–deserializer (SerDes) pair to transport CSI-2 image data over several meters, enabling long-distance and noise-resistant camera integration.  

GMSL systems provide several advantages in embedded and automotive environments:
- **Long-distance transmission:** Supports reliable video delivery over cables up to ~15 m, suitable for robotics and vehicle sensor placement.
- **High bandwidth:** GMSL1/2/3 can carry multi-gigabit CSI-2 streams, enabling high-resolution or multi-camera configurations.
- **Power over Coax (PoC):** Allows power and data through a single cable, reducing connector count and simplifying system routing.
- **Robustness and EMI immunity:** Coaxial cables and differential signaling make GMSL stable in electrically noisy environments.
- **Standard sensor control:** The deserializer forwards I2C communication to the sensor, enabling typical exposure, gain, and frame-rate configuration.

A typical GMSL camera path includes the image sensor with a serializer, a coax cable, a deserializer, and finally a CSI-2 output to the SoC. On Linux, once the SerDes and sensor are properly described in the device tree, the camera appears as a V4L2 or Media Controller device—much like a standard MIPI camera, but with far greater flexibility in placement and system design

## 2.3 USB Camera Overview
A USB camera is a digital imaging device that connects to a system through a USB 2.0 or USB 3.0 interface. Its key advantage is that it operates without the need for a dedicated driver because it follows the standard UVC (USB Video Class) protocol. Since most operating systems—Linux, Windows, and macOS—natively support UVC, users can obtain video streams immediately after plugging in the camera, without any additional configuration.
  
USB cameras are widely used in embedded platforms for the following reasons:
- **Plug-and-play capability:** Unlike MIPI sensors, USB cameras do not require sensor initialization, I2C register configuration, or ISP pipeline setup; video can be captured immediately upon connection.
- **High compatibility:** Most USB cameras adhere to the UVC specification, so they operate in a consistent manner regardless of manufacturer or model.
- **Rich resolution and format support:** Common formats such as MJPEG, YUYV, and NV12 are widely available.
- **Ease of connection and cabling:** USB cables allow simplified wiring and support longer distances, often several meters.
- **Suitable for embedded development:** Fewer driver-related issues enable faster prototyping.

In Linux-based systems, USB cameras are automatically detected and exposed as /dev/video* nodes. Video capture and control can be performed using standard tools such as v4l2-ctl, ffmpeg, and GStreamer.  
Many USB cameras include a built-in ISP that handles image processing internally—such as auto white balance, auto exposure, and color correction. This allows stable image quality even on boards that do not feature an external ISP. Because of these characteristics, USB cameras have become one of the simplest and most versatile camera solutions in fields such as testing, embedded Linux development, robotics, and rapid prototyping.

## 2.4 Available Camera Types on D3-G
The TOPST D3-G platform supports the same set of camera types in both Yocto and Ubuntu environments. Available camera interfaces include USB, MIPI, GMSL, with minor configuration differences depending on the interface used.  
1. **MIPI Camera**  
The TOPST D3-G provides two MIPI CSI ports, allowing one MIPI camera per port. The MIPI CSI interface supports two connector formats:
    - **15-pin(2-Lane):** Suitable for lower-bandwidth sensors such as OV5647 or IMX219.
    - **20-pin (4-Lane):** Intended for high-resolution or high-frame-rate sensors.
2. **GMSL Camera**  
GMSL cameras support long-distance transmission and are commonly used in automotive and industrial applications. To use GMSL on TOPST D3-G, the following components are required:
    1. Connect the **20-pin MIPI CSI (4-Lane)** port to the **TOPST MIPI Gender Board**.
    2. Mount the **Deserializer (Des)** board onto the Gender Board.
    3. Connect up to four GMSL cameras to the Des board using Fakra cables.
3. **USB Camera**  
USB cameras offer the simplest way to get started. When connected to any USB 2.0 or USB 3.0 port on the board, they are recognized automatically and can be used without additional configuration.  
If the device is a V4L2-compatible UVC camera, you can verify its detection using the following command:  
    ``` 
    v4l2-ctl --list-devices
    ```

## 2.4 Available Camera Types on D3-G
The TOPST AI-G platform also supports multiple camera input interfaces, but the overall configuration is simpler than on the D3-G and optimized for high-performance AI workloads. Notably, USB cameras are not supported on this platform. Only MIPI, GMSL inputs are available.  
1. **MIPI Camera**  
The TOPST D3-G provides two MIPI CSI ports, allowing one MIPI camera per port. The MIPI CSI interface supports two connector formats:
    - **15-pin(2-Lane):** Suitable for lower-bandwidth sensors such as OV5647 or IMX219.
    - **20-pin (4-Lane):** Intended for high-resolution or high-frame-rate sensors.
2. **GMSL Camera**  
GMSL cameras support long-distance transmission and are commonly used in automotive and industrial applications. To use GMSL on TOPST D3-G, the following components are required:
    1. Connect the **20-pin MIPI CSI (4-Lane)** port to the **TOPST MIPI Gender Board**.
    2. Mount the **Deserializer (Des)** board onto the Gender Board.
    3. Connect up to four GMSL cameras to the Des board using Fakra cables.

# 3. Camera Connection Guide
Chapter 3 explains how to connect cameras to the D3-G and AI-G boards.  
This section ensures that the board and camera are connected correctly so the camera can operate reliably. Please follow the guide below to connect the camera you intend to use.

## 3.1 Connecting a Camera to the D3-G
Follow the guide below for instructions on how to connect MIPI CSI-2, GMSL, and USB cameras to the D3-G.  

### 3.1.1 MIPI CSI-2 Camera
Figure 3.1 shows the MIPI CSI connectors on the D3-G. The D3-G supports 2 channels of MIPI CSI, each configured with a 2-lane interface. A 4-lane interface is optional and requires a 20-pin connector instead of a 15-pin connector. For information on the pins, refer to D3-G Hardware-User Guide.

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/accessories/Camera/3.1%20MIPI%20CSI%20Connector%20on%20D3-G.png"></p>
<p align="center"><strong>Figure 3.1 MIPI CSI Connector on D3-G</strong></p>

When connecting a MIPI camera, use an FFC (Flat Flexible Cable). Refer to Figures 3.2 and 3.3 for the correct cable type and orientation.

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/accessories/Camera/3.2%20FFC%20Type.png"></p>
<p align="center"><strong>Figure 3.2 FFC Type</strong></p>

The FFC cable is a 1.0 mm, 15-pin type, and one side must have a different colored marking (blue or gray). The cable should be inserted using the B-Forward Direction orientation. Refer to Figure 3.2 for the FFC type.

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/accessories/Camera/3.3%20An%20example%20of%20an%20FFC%20connected%20to%20the%20D3-G%20MIPI0%2015-pin%20Connector.png"></p>
<p align="center"><strong>Figure 3.3 An example of an FFC connected to the D3-G MIPI0 15-pin Connector</strong></p>

Ensure that the 15 silver contacts on the FFC align with the 15 silver contacts inside the D3-G MIPI connector.  
The same connection method applies when using the MIPI1 connector; connect it in the same manner as the MIPI0 connector.

### 3.1.2 GMSL Camera
GMSL cameras use Fakra cables. Therfore, they cannot be connected directly to the D3-G board. Instead, they must be connected through the Deserializer (Des) board and the TOPST MIPI Gender Board before interfacing with the D3-G.  
The connection structure is as follows.  

<p align="center"><strong>< D3-G > ↔ < TOPST MIPI Gender Board > ↔ < Des Board > ↔ < GMSL Camera ></strong></p>

GMSL cameras require the use of the TOPST MIPI Gender Board, which must be connected through the 20-pin MIPI connector. For example, if you plan to use four GMSL cameras, you must connect them using the 20-pin MIPI interface as shown in Figure 3.4.

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/accessories/Camera/3.4%2020-pin%20MIPI0%20Connector.png"></p>
<p align="center"><strong>Figure 3.4 20-pin MIPI0 Connector</strong></p>  

1. Connecting the D3-G Board to the TOPST MIPI Gender Board.  
    The FFC cable is a 1.0 mm, 20-pin type, and one side must have a different colored marking (blue or gray). The cable should be inserted using the A-Forward Direction orientation. Refer to Figure 3.5 for the FFC type.  
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/accessories/Camera/3.2%20FFC%20Type.png"></p>
    <p align="center"><strong>Figure 3.5 FFC Type</strong></p>
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/accessories/Camera/3.6%20Anexample%20of%20an%20FFC%20connected%20to%20the%20D3-G%20MIPI0%2020-pin%20Connector.png"></p>
    <p align="center"><strong>Figure 3.6 An example of an FFC connected to the D3-G MIPI0 20-pin Connector</strong></p> 
    Ensure that the 20 silver contacts on the FFC align with the 20 silver contacts inside the D3-G MIPI connector
    The same connection method applies when using the MIPI1 connector; connect it in the same manner as the MIPI0 connector.
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/accessories/Camera/3.7%20An%20example%20of%20an%20FFC%20connected%20th%20toe%20TOPST%20MIPI%20Gender%20Board%20MIPI%20Connector.png"></p>
    <p align="center"><strong>Figure 3.7 An example of an FFC connected to the TOPST MIPI Gender Board MIPI Connector</strong></p>
2. Connecting the Deserializer Board to the MIPI Gender Board.  
    Attach the JH2 connector on the MIPI Gender Board to the JH1 connector located on the bottom side of the SerDes board.
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/accessories/Camera/3.8%20JH2%20Connector.png"></p>
    <p align="center"><strong>Figure 3.8 JH2 Connector</strong></p>
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/accessories/Camera/3.9%20JH1%20Connector.png"></p>
    <p align="center"><strong>Figure 3.9 JH1 Connector</strong></p>
3. GMSL Camera Connection
    Connect the cameras as shown in Figure 3.10. The figure illustrates an example with two cameras, but you may connect any number of cameras from one to four as needed.
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/accessories/Camera/3.10%20GMSL%20Camera%20Connection.png"></p>
    <p align="center"><strong>Figure 3.10 JH2 Connector</strong></p>

### 3.1.3 USB Camera
USB cameras can be used by connecting them to either USB 2.0 or USB 3.0 ports on the D3-G. When using a USB camera that requires USB 3.0 specifications, be sure to connect it to the USB 3.0 port.

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/accessories/Camera/3.11%20USB%20Camera%20Connection.png"></p>
<p align="center"><strong>Figure 3.11 USB Camera Connection</strong></p>

## 3.2 Connecting a Camera to the AI-G
### 3.2.1 MIPI CSI-2 Camera
Figure 3.12 shows the MIPI CSI connectors on the AI-G. The AI-G supports 2 channels of MIPI CSI, each configured with a 2-lane interface.

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/accessories/Camera/3.12%20MIPI%20CSI%20Connector%20on%20AI-G.png"></p>
<p align="center"><strong>Figure 3.12 MIPI CSI Connector on AI-G</strong></p>

When connecting a MIPI camera, use an FFC (Flat Flexible Cable). Refer to Figures 3.13 and 3.14 for the correct cable type and orientation.

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/accessories/Camera/3.2%20FFC%20Type.png"></p>
<p align="center"><strong>Figure 3.13 FFC Type</strong></p>

The FFC cable is a 1.0 mm, 15-pin type, and one side must have a different colored marking (blue or gray). The cable should be inserted using the B-Forward Direction orientation. Refer to Figure 3.13 for the FFC type.

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/accessories/Camera/3.14%20An%20example%20of%20an%20FFC%20connected%20to%20the%20AI-G%20MIPI%2015-pin%20Connector.png"></p>
<p align="center"><strong>Figure 3.14 An example of an FFC connected to the AI-G MIPI 15-pin Connector</strong></p>

Ensure that the 15 silver contacts on the FFC align with the 15 silver contacts inside the AI-G MIPI connector.

### 3.2.2 GMSL Camera
GMSL cameras use Fakra cables. Therfore, they cannot be connected directly to the AI-G board. Instead, they must be connected through the Deserializer (Des) board and the TOPST MIPI Gender Board before interfacing with the AI-G.  
The connection structure is as follows.

<p align="center"><strong>< AI-G > ↔ < TOPST MIPI Gender Board > ↔ < Des Board > ↔ < GMSL Camera ></strong></p>

GMSL cameras require the use of the TOPST MIPI Gender Board, which must be connected through the 20-pin MIPI connector. For example, if you plan to use four GMSL cameras, you must connect them using the 20-pin MIPI interface as shown in Figure 3.15.

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/accessories/Camera/3.15%2020-pin%20MIPI%20Connector.png"></p>
<p align="center"><strong>Figure 3.15 20-pin MIPI Connector</strong></p>

1. Connecting the AI-G Board to the TOPST MIPI Gender Board.  
    The FFC cable is a 1.0 mm, 20-pin type, and one side must have a different colored marking (blue or gray). The cable should be inserted using the A-Forward Direction orientation. Refer to Figure 3.16 for the FFC type.
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/accessories/Camera/3.2%20FFC%20Type.png"></p>
    <p align="center"><strong>Figure 3.16 FFC Type</strong></p>
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/accessories/Camera/3.17%20An%20example%20of%20an%20FFC%20connected%20to%20the%20AI-G%20MIPI%2020-pin%20Connector.png"></p>
    <p align="center"><strong>Figure 3.17 An example of an FFC connected to the AI-G MIPI 20-pin Connector</strong></p>
    Ensure that the 20 silver contacts on the FFC align with the 20 silver contacts inside the AI-G MIPI connector
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/accessories/Camera/3.18%20An%20example%20of%20an%20FFC%20connected%20to%20the%20TOPST%20MIPI%20Gender%20Board%20MIPI%20Connector.png"></p>
    <p align="center"><strong>Figure 3.18 An example of an FFC connected to the TOPST MIPI Gender Board MIPI Connector</strong></p>
2. Connecting the Deserializer Board to the MIPI Gender Board.  
    Attach the JH2 connector on the MIPI Gender Board to the JH1 Connector located on the bottom side of the SerDes board.
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/accessories/Camera/3.19%20JH2%20Connector.png"></p>
    <p align="center"><strong>Figure 3.19 JH2 Connector</strong></p>
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/accessories/Camera/3.20%20JH1%20Connector.png"></p>
    <p align="center"><strong>Figure 3.20 JH1 Connector</strong></p>
3. GMSL Camera Connection
    Connect the cameras as shown in Figure 3.21. The figure illustrates an example with two cameras, but you may connect any number of cameras from one to four as needed.
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/accessories/Camera/3.21%20GMSL%20Camera%20Connection.png"></p>
    <p align="center"><strong>Figure 3.21 GMSL Camera Connection</strong></p>

# 4. Software Setup
Chapter 4 describes the software setup required for camera operation. For configuring MIPI CSI-2 cameras (OV5647, IMX219) and GMSL cameras on the D3-G and AI-G platforms, refer to the Yocto setup instructions provided below.

## 4.1 MIPI CSI-2 Camera Setup Guide
The TX data rate can be calculated using the following formula:

<p align="center"><strong>TX Data Rate ={ H_active }×{V_active }×{FPS}×{BPP}×{ Number_of_Cameras} × 1.3 (Margin)</strong></p>

The total data rate must not exceed the D3-G MIPI CSI-2 bandwidth limit of 2.1 Gbps per lane.  
And he total data rate must not exceed the AI-G MIPI CSI-2 bandwidth limit of 1.5 Gbps per lane

### 4.1.1 D3-G OV5647 Setup Guide
#### 4.1.1.1 OV5647 Sensor Overview
##### 4.1.1.1.1 Introduction
The OV5647 is a 5-megapixel CMOS image sensor widely used in embedded camera applications due to its compact size, stable performance, and compatibility with standard MIPI CSI-2 interfaces. It is also the image sensor used in the Raspberry Pi Camera Module v1 and is available through various Arducam OV5647 camera modules, all of which are compatible with the TOPST D3-G platform.  
Users may connect either a Raspberry Pi Camera v1 or an Arducam OV5647 module to the MIPI CSI port for camera operation.

On the TOPST D3-G platform, the OV5647 connects through the 15-pin or 20-pin MIPI CSI connector and is controlled via the V4L2 framework, providing consistent operation across both Yocto and Ubuntu environments.

##### 4.1.1.1.2 Supported Resolutions and FPS
The specifications for the OV5647 camera module (Raspberry Pi v1 or Arducam OV5647) are as follows:  

<p align="center"><strong>Table 4.1 Specification for OV5647 camera module</strong></p>
<div align="center">
    <table>
        <tr>
            <td colspan="2" align="center"><strong>Specification</strong></td>
            <td align="center"><strong>Decription</strong></td>
        </tr>
        <tr>
            <td colspan="2">Sensor</td>
            <td>OmniVision OV5647</td>
        </tr>
        <tr>
            <td colspan="2">Resolution</td>
            <td>2592 x 1944 (5MP)</td>
        </tr>
        <tr>
            <td colspan="2">Output Formats</td>
            <td>RAW, YUV, JPEG</td>
        </tr>
        <tr>
            <td colspan="2">Interface</td>
            <td>MIPI CSI-2</td>
        </tr>
        <tr>
            <td colspan="2">Frame Rate</td>
            <td>1080p30, 720p60, 480p90</td>
        </tr>
        <tr>
            <td colspan="2">Lens</td>
            <td>Fixed-focus</td>
        </tr>
        <tr>
            <td colspan="2">Field of View (FOV)</td>
            <td>Up to 54°</td>
        </tr>
        <tr>
            <td colspan="2">Cable Type</td>
            <td>FFC (15-pin)</td>
        </tr>
        <tr>
            <td colspan="2">Board Dimensions</td>
            <td>25mm x 24mm</td>
        </tr>
        <tr>
            <td colspan="2">Compatibility</td>
            <td>D3-G and Rasbperry Pi (through MIPI CSI-2 port)</td>
        </tr>
    </table>
</div>

The sensor resolutions and FPS supported on the D3-G are as follows:  
<p align="center"><strong>Table 4.2 OV5647 Sensor Resolution on D3-G</strong></p>
<div align="center">
    <table>
        <tr>
            <td colspan="3" align="center"><strong>Resolution</strong></td>
            <td align="center"><strong>FPS</strong></td>
            <td align="center"><strong>Description</strong></td>
        </tr>
        <tr>
            <td colspan="3">1920x1080</td>
            <td>30</td>
            <td>Outputs a 1080p image by cropping the center region of the full-resolution frame</td>
        </tr>
        <tr>
            <td colspan="3">1296x972</td>
            <td>30</td>
            <td>Utilizes 2×2 pixel binning to increase sensitivity and reduce noise</td>
        </tr>
        <tr>
            <td colspan="3">640x480</td>
            <td>60</td>
            <td>Combines 2×2 binning with <strong>subsampling</strong>, which skips pixels during readout to reduce data throughput and achieve higher frame rates</td>
        </tr>
    </table>
</div>

**Note:** As shown in Table 4.2, the full resolution of **2592×1944 cannot be used** due to the ISP specifications of the D3-G.

<p align="center"><strong>Table 4.3 Maximum Resolution by Operation Mode</strong></p>
<div align="center">
    <table>
        <tr>
            <td rowspan="2" align="center"><strong>ISP Core</strong></td>
            <td colspan="2"><strong>Resolution by Operation Mode</strong></td>
        </tr>
        <tr>
            <td align="center"><strong>Default Mode</strong></td>
            <td align="center"><strong>Memory Share Mode</strong></td>
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

#### 4.1.1.2 OV5647 Resolution Configuration in Yocto: Driver
To modify the resolution of the OV5647 sensor during the Yocto build process, follow the instructions below.  

First, to enable the OV5647, ensure that TOPST_CAM_MODULE = "ov5647" is set in  
{build_dir}/build/d3-g-topst-main/conf/local.conf.  
Although this is enabled by default when initializing the repository for the first build, please verify it again.

Additionally, to prevent the source code from being removed during the build process, enable the following line in  
{build_dir}/build/d3-g-topst-main/conf/local.conf:
```
INHERIT:remove = “rm_work”
```

After enabling the option above, rebuild the image using the following command.
```
$ bitbake telechips-topst-image
```

Second, after the build is complete, open the ov5647.c driver file and apply the required modifications.

Navigate to the following directory:
```
${build_dir}/build/d3-g-topst-main/tmp/work/d3_g_topst_main-telechips-linux/linux-topst/5.10.205-r0/git/drivers/media/i2c/telechips/
```

Before modifying the code, note that the current driver supports the following three modes:
- 1920x1080 @ 30fps
- 1296x972 @ 30fps
- 640x480 @ 60fps  

Each resolution corresponds to Mode 1, Mode 2, and Mode 3 respectively.  

The 1920×1080 @ 30fps mode uses a center crop, resulting in a narrower field of view, and the 640×480 mode provides insufficient resolution. In contrast, the 1296×972 mode uses 2×2 binning, which provides a wider field of view; therefore, it is currently used as the default mode.  
Open the ov5647.c driver file and modify the OV5647 default mode as shown below.
```
#define OV5647_DEFAULT_MODE (&supported_modes_10bit[2])
```
1920×1080 @ 30fps corresponds to Mode 1, you can use **“#define OV5647_DEFAULT_MODE (&supported_modes_10bit[1])”** as is.  
The 1296×972 @ 30fps mode corresponds to Mode 2, so **“#define OV5647_DEFAULT_MODE (&supported_modes_10bit[2])”** is already correctly set.  
For 640×480 @ 60fps, which corresponds to Mode 3, change the definition to **“#define OV5647_DEFAULT_MODE (&supported_modes_10bit[3])”**.

Third, rebuild the kernel and generate the FAI image.  
Return to the build directory and rebuild the kernel using the command below.
```
$ cd ${build_dir}/build/d3-g-topst-main/
$ bitbake -C compile linux-topst
$ cd ${build_dir}
$ ./stitch-fai-d3.sh
```
Afterwards, flash the generated output_d3g.fai to the board using FWDN, and you will be able to use the OV5647 sensor with the desired resolution.

**Note:** If you want to use the MIPI1-CSI port, open the tcc805x-videoinput-camera-module.dtsi file located in
“{build_dir}/build/d3-g-topst-main/tmp/work/d3_g_topst_main-telechips-linux/linux-topst/5.10.205-r0/git/arch/arm64/boot/dts/telechips/tcc805x/override/” and change the included dtsi file from “tcc805x-videoinput-mipi0-ov5647.dtsi” to “tcc805x-videoinput-mipi1-ov5647.dtsi”. + Open the tcc805x-videoinput.dtsi file located in "{build_dir}/build/d3-g-topst-main/tmp/work/d3_g_topst_main-telechips-linux/linux-topst/5.10.205-r0/git/arch/arm64/boot/dts/telechips/tcc805x/" and change the mipi chmux from "mipi-chmux-0 = <0>;" to "mipi-chmux-0 = <1>;".

### 4.1.2 D3-G IMX219 Setup Guide
#### 4.1.2.1 IMX219 Sensor Overview
##### 4.1.2.1.1 Introduction
The IMX219 is a high-performance 8-megapixel CMOS image sensor from Sony, well-known for delivering excellent image quality, low power consumption, and stable capture performance in compact camera modules. It is also the sensor used in the Raspberry Pi Camera Module v2 and is widely adopted in embedded vision systems, robotics, and AI-based camera applications.

On the TOPST D3-G platform, the IMX219 sensor can be connected through either the 15-pin or 20-pin MIPI CSI connector, and it is controlled via the V4L2 framework. This allows for a consistent interface and stable camera operation across both Yocto and Ubuntu environments.

With its high resolution (8MP) and low-noise imaging characteristics, the IMX219 is well suited for implementing high-quality video capture and image processing capabilities on the TOPST D3-G platform.

##### 4.1.2.1.2 Supported Resolutions and FPS
The specifications for the IMX219 camera module (Raspberry Pi v2) are as follows:

<p align="center"><strong>Table 4.4 Specification for IMX219 camera module</strong></p>
<div align="center">
    <table>
        <tr>
            <td colspan="2" align="center"><strong>Specification</strong></td>
            <td align="center"><strong>Decription</strong></td>
        </tr>
        <tr>
            <td colspan="2">Sensor</td>
            <td>Sony Imx219</td>
        </tr>
        <tr>
            <td colspan="2">Resolution</td>
            <td>3280 x 2464 (8 MP)</td>
        </tr>
        <tr>
            <td colspan="2">Output Formats</td>
            <td>RAW, YUV, JPEG</td>
        </tr>
        <tr>
            <td colspan="2">Interface</td>
            <td>MIPI CSI-2</td>
        </tr>
        <tr>
            <td colspan="2">Frame Rate</td>
            <td>1080p60, 720p180, 480p206</td>
        </tr>
        <tr>
            <td colspan="2">Lens</td>
            <td>Adjustable-focus</td>
        </tr>
        <tr>
            <td colspan="2">Field of View (FOV)</td>
            <td>Up to 62°</td>
        </tr>
        <tr>
            <td colspan="2">Cable Type</td>
            <td>FFC (15-pin)</td>
        </tr>
        <tr>
            <td colspan="2">Board Dimensions</td>
            <td>25mm x 24mm</td>
        </tr>
        <tr>
            <td colspan="2">Compatibility</td>
            <td>D3-G and Rasbperry Pi (through MIPI CSI-2 port)</td>
        </tr>
    </table>
</div>

The sensor resolutions and FPS supported on the D3-G are as follows:
<p align="center"><strong>Table 4.5 IMX219 Sensor Resolution on D3-G</strong></p>
<div align="center">
    <table>
        <tr>
            <td colspan="3" align="center"><strong>Resolution</strong></td>
            <td align="center"><strong>FPS</strong></td>
            <td align="center"><strong>Description</strong></td>
        </tr>
        <tr>
            <td colspan="3">1920x1080</td>
            <td>30</td>
            <td>Outputs a 1080p image by cropping the center region of the full-resolution frame</td>
        </tr>
        <tr>
            <td colspan="3">1640x1232</td>
            <td>30</td>
            <td>Utilizes 2×2 pixel binning to increase sensitivity and reduce noise</td>
        </tr>
        <tr>
            <td colspan="3">640x480</td>
            <td>30</td>
            <td>Combines 2×2 binning with <strong>subsampling</strong>, which skips pixels during readout to reduce data throughput</td>
        </tr>
    </table>
</div>  

**Note:** As shown in Table 4.5, the full resolution of **3820×2464 cannot be used** due to the ISP specifications of the D3-G.

<p align="center"><strong>Table 4.6 Maximum Resolution by Operation Mode</strong></p>
<div align="center">
    <table>
        <tr>
            <td rowspan="2" align="center"><strong>ISP Core</strong></td>
            <td colspan="2"><strong>Resolution by Operation Mode</strong></td>
        </tr>
        <tr>
            <td align="center"><strong>Default Mode</strong></td>
            <td align="center"><strong>Memory Share Mode</strong></td>
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

#### 4.1.2.2 Enable IMX219 in Yocto
Since the D3-G SDK is configured to enable the OV5647 by default, you must enable the IMX219 before building.   
There are two cases to consider: when the SDK has already been built, and when it is being built for the first time.

##### 4.1.2.2.1 Enable IMX219 Before the First Build
For the initial build, follow the steps below to enable the IMX219 and proceed with the build.
1. Source the environment setup script and select option 2
    ```
    $ source poky/meta-topst/topst-build.sh
    ```
2. Open the local.conf file located at the path below
    ```
    ${build_dir}/build/d3-g-topst-main/conf/local.conf
    ```
3. Comment out the TOPST_CAM_MODULE entry for ov5647 and enable the entry for imx219
    ```
    #TOPST_CAM_MODULE = "ov5647"
    TOPST_CAM_MODULE = "imx219"
    ```
4. Run the build process
    ```
    $ bitbake telechips-topst-image
    ```
    
#### 4.1.2.3 IMX219 Resolution Configuration in Yocto: Driver
To modify the resolution of the IMX219 sensor during the Yocto build process, follow the instructions below.

First, to enable the imx219, ensure that TOPST_CAM_MODULE = "imx219" is set in
{build_dir}/build/d3-g-topst-main/conf/local.conf.

Additionally, to prevent the source code from being removed during the build process, enable the following line in
{build_dir}/build/d3-g-topst-main/conf/local.conf:
```
INHERIT:remove = “rm_work”
```

After enabling the option above, rebuild the image using the following command.
```
$ bitbake telechips-topst-image
```

Second, after the build is complete, open the imx219.c driver file and apply the required modifications.

Navigate to the following directory:
```
${build_dir}/build/d3-g-topst-main/tmp/work/d3_g_topst_main-telechips-linux/linux-topst/5.10.205-r0/git/drivers/media/i2c/telechips/
```

Before modifying the code, note that the current driver supports the following three modes:
- 1920x1080 @ 30fps
- 1640x1232 @ 30fps
- 640x480 @ 30fps

Each resolution corresponds to Mode 1, Mode 2, and Mode 3 respectively.

The 1920×1080 @ 30fps mode uses a center crop, resulting in a narrower field of view, and the 640×480 mode provides insufficient resolution. In contrast, the 1640×1232 mode uses 2×2 binning, which provides a wider field of view; therefore, it is currently used as the default mode.  
Open the imx219.c driver file, and modify the sections described below inside the imx219_set_default_format, imx219_open, and imx219_probe functions.
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

Since 1920×1080 @ 30fps corresponds to Mode 1, update all supported_modes references inside the three functions to **“supported_modes[1]”**.  
The 1640×1232 @ 30fps mode corresponds to Mode 2, so replace them with **“supported_modes[2]”** accordingly.  
For 640×480 @ 30fps, which corresponds to Mode 3, change all references to **“supported_modes [3]”**.

Third, rebuild the kernel and generate the FAI image.  
Return to the build directory and rebuild the kernel using the command below.
```
$ cd ${build_dir}/build/d3-g-topst-main/
$ bitbake -C compile linux-topst
$ cd ${build_dir}
$ ./stitch-fai-d3.sh
```

Afterwards, flash the generated output_d3g.fai to the board using FWDN, and you will be able to use the IMX219 sensor with the desired resolution.

**Note:** If you want to use the MIPI1-CSI port, open the tcc805x-videoinput-camera-module.dtsi file located in
“{build_dir}/build/d3-g-topst-main/tmp/work/d3_g_topst_main-telechips-linux/linux-topst/5.10.205-r0/git/arch/arm64/boot/dts/telechips/tcc805x/override/”and change the included dtsi file from “tcc805x-videoinput-mipi0-imx219.dtsi” to “tcc805x-videoinput-mipi1-imx219.dtsi”. + Open the tcc805x-videoinput.dtsi file located in "{build_dir}/build/d3-g-topst-main/tmp/work/d3_g_topst_main-telechips-linux/linux-topst/5.10.205-r0/git/arch/arm64/boot/dts/telechips/tcc805x/" and change the mipi chmux from "mipi-chmux-0 = <0>;" to "mipi-chmux-0 = <1>;".

#### 4.1.2.4 How to Increase the FPS of the IMX219 in Yocto: Driver and Device Tree
According to the IMX219 sensor description, the sensor supports high-framerate modes such as 1080p60, 720p180, and VGA206. Therefore, it is possible to increase the FPS for the resolutions supported by the imx219.c driver—1920×1080, 1640×1232, and 640×480. Since the ISP core on the D3-G platform supports up to 60 fps, each of these resolutions can be raised to a maximum of 60 fps. 

The formula for calculating FPS is:
<p align="center"><strong>{fps} = {pixel_rate}/{hts}x{vts}</strong></p>
Therefore, to increase the FPS, the pixel_rate, hts, and vts values must be adjusted.  
In the current driver implementation, both pixel_rate and hts are fixed. To raise the FPS, the only feasible approach is to increase the pixel_rate while keeping hts constant, and then adjust vts accordingly to achieve the desired frame rate.

To modify the FPS to 60, both the driver and the device tree must be updated.
Follow the guide below to change the FPS to 60.

##### 4.1.2.4.1 1920x1080 @ 60fps
To achieve 60 fps, the following relationship must hold:  
fps = pixel_rate / (hts × vts)
- pixel_rate = 182,400,000
- hts = 3448
- target fps = 60

the required VTS would be:
- vts = pixel_rate / (hts × fps) = 182,400,000 / (3448 × 60) ≈ 882

However, the VTS value must be greater than 1080, so this configuration is not valid.  
Therefore, to reach 60 fps, we must keep hts fixed, and instead adjust pixel_rate, vts, and the PLL_VT register.

The required changes are as follows:
1. imx219.c driver file  
    A. Increase the pixel rate and link frequency
    ```
    #define IMX219_PIXEL_RATE            182400000    →   #define IMX219_PIXEL_RATE            278400000
    #define IMX219_DEFAULT_LINK_FREQ     456000000   →   #define IMX219_DEFAULT_LINK_FREQ     696000000
    ``` 
    B. Update the VTS value for the 1080p mode:
    ```
    #define IMX219_VTS_30FPS_1080P       0x06e3       →   #define IMX219_VTS_30FPS_1080P       0x0542
    ```
    C. Modify the PLL_VT register in the 1920x1080 mode table:
    ```
    // imx219_reg mode_1920_1080_regs[]
    {0x0307, 0x39}   →   {0x0307, 0x57}
    ```
2. tcc805x-videoinput-mipi0-imx219.dtsi device tree file  
    A. Update the link frequency to match the new pixel rate:
    ```
    // &i2c7
    /bits/ 64 <456000000> → /bits/ 64 <696000000>
    ```
    B. Update the hs-settle value:
    ```
    hs-settle = <13> → hs-settle = <35>
    ```
3. Rebuild the kernel and generate the FAI image.  
    Return to the build directory and rebuild the kernel using the command below.
    ```
    $ cd ${build_dir}/build/d3-g-topst-main/
    $ bitbake -C compile linux-topst
    $ cd ${build_dir}
    $ ./stitch-fai-d3.sh
    ```
Using the command below on D3-G, you can confirm that the FPS output is 59.9, which corresponds to 60 fps.
```
$ v4l2-ctl --stream-mmap=3 --stream-count=300 --stream-to=/dev/null --verbose
```
The GStreamer command on D3-G for camera playback is shown below.
```
$ gst-launch-1.0 v4l2src device=/dev/video0 io-mode=2 ! video/x-raw,format=NV12,width=1920,height=1080,framerate=60/1 ! videoconvert ! waylandsink sync=false
```

##### 4.1.2.4.2 1640x1232 @ 60fps
To achieve 60 fps, the following relationship must hold:  
fps = pixel_rate / (hts × vts)
- pixel_rate = 182,400,000
- hts = 3448
- target fps = 60

the required VTS would be:
- vts = pixel_rate / (hts × fps) = 182,400,000 / (3448 × 60) ≈ 882

However, the VTS value must be greater than 1080, so this configuration is not valid.  
Therefore, to reach 60 fps, we must keep hts fixed, and instead adjust pixel_rate, vts, and the PLL_VT register.

The required changes are as follows:
1. imx219.c driver file  
    A. Increase the pixel rate and link frequency
    ```
    #define IMX219_PIXEL_RATE            182400000    →   #define IMX219_PIXEL_RATE            278400000
    #define IMX219_DEFAULT_LINK_FREQ     456000000   →   #define IMX219_DEFAULT_LINK_FREQ     696000000
    ``` 
    B. Update the VTS value for the 1640_1232 mode:
    ```
    #define IMX219_VTS_30FPS_BINNED       0x06e3       →   #define IMX219_VTS_30FPS_BINNED       0x0542
    ```
    C. Modify the PLL_VT register in the 1920x1080 mode table:
    ```
    // imx219_reg mode_1640_1232_regs[]
    {0x0307, 0x39}   →   {0x0307, 0x57}
    ```
2. tcc805x-videoinput-mipi0-imx219.dtsi device tree file  
    A. Update the link frequency to match the new pixel rate:
    ```
    // &i2c7
    /bits/ 64 <456000000> → /bits/ 64 <696000000>
    ```
    B. Update the hs-settle value:
    ```
    hs-settle = <13> → hs-settle = <34>
    ```
3. Rebuild the kernel and generate the FAI image.  
    Return to the build directory and rebuild the kernel using the command below.
    ```
    $ cd ${build_dir}/build/d3-g-topst-main/
    $ bitbake -C compile linux-topst
    $ cd ${build_dir}
    $ ./stitch-fai-d3.sh
    ```
Using the command below on D3-G, you can confirm that the FPS output is 59.9, which corresponds to 60 fps.
```
$ v4l2-ctl --stream-mmap=3 --stream-count=300 --stream-to=/dev/null --verbose
```
The GStreamer command on D3-G for camera playback is shown below.
```
$ gst-launch-1.0 v4l2src device=/dev/video0 io-mode=2 ! video/x-raw,format=NV12,width=1640,height=1232,framerate=60/1 ! videoconvert ! waylandsink sync=false
```

##### 4.1.2.4.3 640x480 @ 60fps
To achieve 60 fps, the following relationship must hold:  
fps = pixel_rate / (hts × vts)
- pixel_rate = 182,400,000
- hts = 3448
- target fps = 60

the required VTS would be:
- vts = pixel_rate / (hts × fps) = 182,400,000 / (3448 × 60) ≈ 882

Since the VTS value is greater than 480, the condition is satisfied. As in the previous example, we will adjust the pixelrate and VTS to change the FPS while keeping HTS fixed.  
You may also adjust the FPS by modifying only the VTS value without changing the pixelrate. However, the 0x0307 register value of the IMX219 must remain unchanged.

The required changes are as follows:
1. imx219.c driver file  
    A. Increase the pixel rate and link frequency
    ```
    #define IMX219_PIXEL_RATE            182400000    →   #define IMX219_PIXEL_RATE            278400000
    #define IMX219_DEFAULT_LINK_FREQ     456000000   →   #define IMX219_DEFAULT_LINK_FREQ     696000000
    ``` 
    B. Update the VTS value for the 640_480 mode:
    ```
    #define IMX219_VTS_30FPS_640x480       0x06e3       →   #define IMX219_VTS_30FPS_640x480       0x0542
    ```
    C. Modify the PLL_VT register in the 640x480 mode table:
    ```
    // imx219_reg mode_640_480_regs[]
    {0x0307, 0x39}   →   {0x0307, 0x57}
    ```
2. tcc805x-videoinput-mipi0-imx219.dtsi device tree file  
    A. Update the link frequency to match the new pixel rate:
    ```
    // &i2c7
    /bits/ 64 <456000000> → /bits/ 64 <696000000>
    ```
    B. Update the hs-settle value:
    ```
    hs-settle = <13> → hs-settle = <26>
    ```
3. Rebuild the kernel and generate the FAI image.  
    Return to the build directory and rebuild the kernel using the command below.
    ```
    $ cd ${build_dir}/build/d3-g-topst-main/
    $ bitbake -C compile linux-topst
    $ cd ${build_dir}
    $ ./stitch-fai-d3.sh
    ```
Using the command below on D3-G, you can confirm that the FPS output is 59.9, which corresponds to 60 fps.
```
$ v4l2-ctl --stream-mmap=3 --stream-count=300 --stream-to=/dev/null --verbose
```
The GStreamer command on D3-G for camera playback is shown below.
```
$ gst-launch-1.0 v4l2src device=/dev/video0 io-mode=2 ! video/x-raw,format=NV12,width=640,height=480,framerate=60/1 ! videoconvert ! waylandsink sync=false
```

### 4.1.3 AI-G OV5647 Sensor User Guide
#### 4.1.3.1 OV5647 Sensor Overview
##### 4.1.3.1.1 Introduction
The OV5647 is a 5-megapixel CMOS image sensor widely used in embedded camera applications due to its compact size, stable performance, and compatibility with standard MIPI CSI-2 interfaces. It is also the image sensor used in the Raspberry Pi Camera Module v1 and is available through various Arducam OV5647 camera modules, all of which are compatible with the TOPST AI-G platform.  
Users may connect either a Raspberry Pi Camera v1 or an Arducam OV5647 module to the MIPI CSI port for camera operation.

On the TOPST AI-G platform, the OV5647 connects through the 15-pin or 20-pin MIPI CSI connector and is controlled via the V4L2 framework, providing consistent operation across both Yocto and Ubuntu environments.

##### 4.1.3.1.2 Supported Resolutions and FPS
The specifications for the OV5647 camera module (Raspberry Pi v1 or Arducam OV5647) are as follows:
<p align="center"><strong>Table 4.7 Specification for OV5647 camera module</strong></p>
<div align="center">
    <table>
        <tr>
            <td colspan="2" align="center"><strong>Specification</strong></td>
            <td align="center"><strong>Decription</strong></td>
        </tr>
        <tr>
            <td colspan="2">Sensor</td>
            <td>OmniVision OV5647</td>
        </tr>
        <tr>
            <td colspan="2">Resolution</td>
            <td>2592 x 1944 (5MP)</td>
        </tr>
        <tr>
            <td colspan="2">Output Formats</td>
            <td>RAW, YUV, JPEG</td>
        </tr>
        <tr>
            <td colspan="2">Interface</td>
            <td>MIPI CSI-2</td>
        </tr>
        <tr>
            <td colspan="2">Frame Rate</td>
            <td>1080p30, 720p60, 480p90</td>
        </tr>
        <tr>
            <td colspan="2">Lens</td>
            <td>Fixed-focus</td>
        </tr>
        <tr>
            <td colspan="2">Field of View (FOV)</td>
            <td>Up to 54°</td>
        </tr>
        <tr>
            <td colspan="2">Cable Type</td>
            <td>FFC (15-pin)</td>
        </tr>
        <tr>
            <td colspan="2">Board Dimensions</td>
            <td>25mm x 24mm</td>
        </tr>
        <tr>
            <td colspan="2">Compatibility</td>
            <td>D3-G and Rasbperry Pi (through MIPI CSI-2 port)</td>
        </tr>
    </table>
</div>

The sensor resolutions and FPS supported on the AI-G are as follows:  
<p align="center"><strong>Table 4.8 OV5647 Sensor Resolution on AI-G</strong></p>
<div align="center">
    <table>
        <tr>
            <td colspan="3" align="center"><strong>Resolution</strong></td>
            <td align="center"><strong>FPS</strong></td>
            <td align="center"><strong>Description</strong></td>
        </tr>
        <tr>
            <td colspan="3">1920x1080</td>
            <td>30</td>
            <td>Outputs a 1080p image by cropping the center region of the full-resolution frame</td>
        </tr>
        <tr>
            <td colspan="3">1296x972</td>
            <td>30</td>
            <td>Utilizes 2×2 pixel binning to increase sensitivity and reduce noise</td>
        </tr>
        <tr>
            <td colspan="3">640x480</td>
            <td>60</td>
            <td>Combines 2×2 binning with <strong>subsampling</strong>, which skips pixels during readout to reduce data throughput and achieve higher frame rates</td>
        </tr>
    </table>
</div>

**Note:** As shown in Table 4.8, the full **2592×1944 resolution is not used** because it significantly slows down inference performance.

<p align="center"><strong>Table 4.9 Maximum Resolution by Operation Mode</strong></p>
<div align="center">
    <table>
        <tr>
            <td colspan="4" align="center"><strong>CH. Used</strong></td>
            <td align="center"><strong>Operation Mode</strong></td>
            <td align="center"><strong>Max Resolution</strong></td>
            <td align="center"><strong>Input Format</strong></td>
        </tr>
        <tr>
            <td colspan="4">4CH</td>
            <td>Default Mode</td>
            <td>1280 x 720 @ 60fps</td>
            <td>RAW 24</td>
        </tr>
        <tr>
            <td colspan="4" rowspan="2">2CH</td>
            <td rowspan="2">Memory Shared Mode</td>
            <td>Option 1: 2048 x 1280 @ 60fps</td>
            <td>RAW 20</td>
        </tr>
        <tr>
            <td>Option 2: 2592 x 2048 @ 30fps + 2048 x 1280 @ 30fps</td>
            <td>RAW 24</td>
        </tr>
        <tr>
            <td colspan="4">1CH</td>
            <td>Memory Shared Mode</td>
            <td>2592 x 2048 @ 60fps</td>
            <td>RAW 20</td>
        </tr>
    </table>
</div>

#### 4.1.3.2 OV5647 Resolution Configuration in Yocto: Driver
To modify the resolution of the OV5647 sensor during the Yocto build process, follow the instructions below.

First, to enable the OV5647, ensure that TOPST_CAM_MODULE = "ov5647" is set in  
{build_dir}/build/ai-g-topst-main/conf/local.conf.  
Although this is enabled by default when initializing the repository for the first build, please verify it again.

Additionally, to prevent the source code from being removed during the build process, enable the following line in  
{build_dir}/build/ai-g-topst-main/conf/local.conf:
```
INHERIT:remove = “rm_work”
```

After enabling the option above, rebuild the image using the following command.
```
$ bitbake telechips-topst-image
```

Second, after the build is complete, open the ov5647.c driver file and apply the required modifications.

Navigate to the following directory:
```
${build_dir}/build/ai-g-topst-main/tmp/work/ai_g_topst-telechips-linux/linux-topst/5.10.223-r0/git/drivers/media/i2c/telechips/
```

Before modifying the code, note that the current driver supports the following three modes:
- 1920×1080 @ 30fps
- 1296×972 @ 30fps
- 640×480 @ 60fps

Each resolution corresponds to Mode 1, Mode 2, and Mode 3 respectively.

The 1920×1080 @ 30fps mode uses a center crop, resulting in a narrower field of view, and the 640×480 mode provides insufficient resolution. In contrast, the 1296×972 mode uses 2×2 binning, which provides a wider field of view; therefore, it is currently used as the default mode.  
Open the ov5647.c driver file and modify the OV5647 default mode as shown below.
```
#define OV5647_DEFAULT_MODE (&supported_modes_10bit[2])
```
1920×1080 @ 30fps corresponds to Mode 1, you can use **“#define OV5647_DEFAULT_MODE (&supported_modes_10bit[1])”** as is.  
The 1296×972 @ 30fps mode corresponds to Mode 2, so **“#define OV5647_DEFAULT_MODE (&supported_modes_10bit[2])”**is already correctly set.  
For 640×480 @ 60fps, which corresponds to Mode 3, change the definition to **“#define OV5647_DEFAULT_MODE (&supported_modes_10bit[3])”**.

Third, rebuild the kernel and generate the FAI image.  
Return to the build directory and rebuild the kernel using the command below.
```
$ cd ${build_dir}/build/ai-g-topst-main/
$ bitbake -C compile linux-topst
$ cd ${build_dir}
$ ./stitch-fai-ai.sh
```

Afterwards, flash the generated output_aig.fai to the board using FWDN, and you will be able to use the OV5647 sensor with the desired resolution.

### 4.1.4 AI-G IMX219 Sensor User Guide
#### 4.1.4.1 IMX219 Sensor Overview
##### 4.1.4.1.1 Introduction
The IMX219 is a high-performance 8-megapixel CMOS image sensor from Sony, well-known for delivering excellent image quality, low power consumption, and stable capture performance in compact camera modules. It is also the sensor used in the Raspberry Pi Camera Module v2 and is widely adopted in embedded vision systems, robotics, and AI-based camera applications.

On the TOPST AI-G platform, the IMX219 sensor can be connected through either the 15-pin or 20-pin MIPI CSI connector, and it is controlled via the V4L2 framework. This allows for a consistent interface and stable camera operation across both Yocto and Ubuntu environments.

With its high resolution (8MP) and low-noise imaging characteristics, the IMX219 is well suited for implementing high-quality video capture and image processing capabilities on the TOPST AI-G platform.

##### 4.1.4.1.2 Supported Resolutions and FPS
The specifications for the IMX219 camera module (Raspberry Pi v2) are as follows:
<p align="center"><strong>Table 4.10 Specification for IMX219 camera module</strong></p>
<div align="center">
    <table>
        <tr>
            <td colspan="2" align="center"><strong>Specification</strong></td>
            <td align="center"><strong>Decription</strong></td>
        </tr>
        <tr>
            <td colspan="2">Sensor</td>
            <td>Sony Imx219</td>
        </tr>
        <tr>
            <td colspan="2">Resolution</td>
            <td>3280 x 2464 (8 MP)</td>
        </tr>
        <tr>
            <td colspan="2">Output Formats</td>
            <td>RAW, YUV, JPEG</td>
        </tr>
        <tr>
            <td colspan="2">Interface</td>
            <td>MIPI CSI-2</td>
        </tr>
        <tr>
            <td colspan="2">Frame Rate</td>
            <td>1080p60, 720p180, 480p206</td>
        </tr>
        <tr>
            <td colspan="2">Lens</td>
            <td>Adjustable-focus</td>
        </tr>
        <tr>
            <td colspan="2">Field of View (FOV)</td>
            <td>Up to 62°</td>
        </tr>
        <tr>
            <td colspan="2">Cable Type</td>
            <td>FFC (15-pin)</td>
        </tr>
        <tr>
            <td colspan="2">Board Dimensions</td>
            <td>25mm x 24mm</td>
        </tr>
        <tr>
            <td colspan="2">Compatibility</td>
            <td>D3-G and Rasbperry Pi (through MIPI CSI-2 port)</td>
        </tr>
    </table>
</div>

The sensor resolutions and FPS supported on the AI-G are as follows:
<p align="center"><strong>Table 4.11 IMX219 Sensor Resolution on AI-G</strong></p>
<div align="center">
    <table>
        <tr>
            <td colspan="3" align="center"><strong>Resolution</strong></td>
            <td align="center"><strong>FPS</strong></td>
            <td align="center"><strong>Description</strong></td>
        </tr>
        <tr>
            <td colspan="3">1920x1080</td>
            <td>30</td>
            <td>Outputs a 1080p image by cropping the center region of the full-resolution frame</td>
        </tr>
        <tr>
            <td colspan="3">1640x1232</td>
            <td>30</td>
            <td>Utilizes 2×2 pixel binning to increase sensitivity and reduce noise</td>
        </tr>
        <tr>
            <td colspan="3">640x480</td>
            <td>30</td>
            <td>Combines 2×2 binning with <strong>subsampling</strong>, which skips pixels during readout to reduce data throughput</td>
        </tr>
    </table>
</div>

**Note:** As shown in Table 4.11, the full 3820×2464 resolution is not used because it significantly slows down inference performance.

<p align="center"><strong>Table 4.12 Maximum Resolution by Operation Mode</strong></p>
<div align="center">
    <table>
        <tr>
            <td colspan="4" align="center"><strong>CH. Used</strong></td>
            <td align="center"><strong>Operation Mode</strong></td>
            <td align="center"><strong>Max Resolution</strong></td>
            <td align="center"><strong>Input Format</strong></td>
        </tr>
        <tr>
            <td colspan="4">4CH</td>
            <td>Default Mode</td>
            <td>1280 x 720 @ 60fps</td>
            <td>RAW 24</td>
        </tr>
        <tr>
            <td colspan="4" rowspan="2">2CH</td>
            <td rowspan="2">Memory Shared Mode</td>
            <td>Option 1: 2048 x 1280 @ 60fps</td>
            <td>RAW 20</td>
        </tr>
        <tr>
            <td>Option 2: 2592 x 2048 @ 30fps + 2048 x 1280 @ 30fps</td>
            <td>RAW 24</td>
        </tr>
        <tr>
            <td colspan="4">1CH</td>
            <td>Memory Shared Mode</td>
            <td>2592 x 2048 @ 60fps</td>
            <td>RAW 20</td>
        </tr>
    </table>
</div>

#### 4.1.4.2 Enable IMX219 in Yocto
Since the AI-G SDK is configured to enable the OV5647 by default, you must enable the IMX219 before building.  
There are two cases to consider: when the SDK has already been built, and when it is being built for the first time.

##### 4.1.4.2.1 Enable IMX219 Before the First Build
For the initial build, follow the steps below to enable the IMX219 and proceed with the build.
1. Source the environment setup script and select option 1
    ```
    $ source poky/meta-topst/topst-build.sh
    ```
2. Open the local.conf file located at the path below
    ```
    ${build_dir}/build/ai-g-topst-main/conf/local.conf
    ```
3. Comment out the TOPST_CAM_MODULE entry for ov5647 and enable the entry for imx219
    ```
    #TOPST_CAM_MODULE = "ov5647"
    TOPST_CAM_MODULE = "imx219"
    ```
4. Run the build process
    ```
    $ bitbake telechips-topst-ai-image
    ```

##### 4.1.4.2.2 Enable IMX219 After the Build Has Already Been Completed
The existing build is configured with the OV5647 sensor enabled by default. Follow the steps below to enable the IMX219.
1. Open the local.conf file located at the path below
    ```
    ${build_dir}/build/ai-g-topst-main/conf/local.conf
    ```
2. Comment out the TOPST_CAM_MODULE entry for ov5647 and enable the entry for imx219
    ```
    #TOPST_CAM_MODULE = "ov5647"
    TOPST_CAM_MODULE = "imx219"
    ```
3. Run a cleansstate operation for isp-server and isp-firmware
    ```
    $ bitbake -c cleansstate isp-firmware
    $ bitbake -c cleansstate isp-server
    ```
4. Run the build process
    ```
    $ bitbake telechips-topst-ai-image
    ```

#### 4.1.4.3 IMX219 Resolution Configuration in Yocto: Driver
To modify the resolution of the IMX219 sensor during the Yocto build process, follow the instructions below.

First, to enable the imx219, ensure that TOPST_CAM_MODULE = "imx219" is set in
{build_dir}/build/ai-g-topst-main/conf/local.conf.

Additionally, to prevent the source code from being removed during the build process, enable the following line in
{build_dir}/build/ai-g-topst-main/conf/local.conf:
```
INHERIT:remove = “rm_work”
```

After enabling the option above, rebuild the image using the following command.
```
$ bitbake telechips-topst-ai-image
```
Second, after the build is complete, open the imx219.c driver file and apply the required modifications.

Navigate to the following directory:
```
${build_dir}/build/ai-g-topst-main /ai-g-topst/tmp/work/ai_g_topst-telechips-linux/linux-topst/5.10.223-r0/git/drivers/media/i2c/telechips/
```
Before modifying the code, note that the current driver supports the following three modes:
- 1920×1080 @ 30fps
- 1640×1232 @ 30fps
- 640×480 @ 30fps
Each resolution corresponds to Mode 1, Mode 2, and Mode 3 respectively.

The 1920×1080 @ 30fps mode uses a center crop, resulting in a narrower field of view, and the 640×480 mode provides insufficient resolution. In contrast, the 1640×1232 mode uses 2×2 binning, which provides a wider field of view; therefore, it is currently used as the default mode.  
Open the imx219.c driver file, and modify the sections described below inside the imx219_set_default_format, imx219_open, and imx219_probe functions.
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

Since 1920×1080 @ 30fps corresponds to Mode 1, update all supported_modes references inside the three functions to **“supported_modes[1]”**.  
The 1640×1232 @ 30fps mode corresponds to Mode 2, so replace them with **“supported_modes[2]”** accordingly.  
For 640×480 @ 30fps, which corresponds to Mode 3, change all references to **“supported_modes [3]”**.

Third, rebuild the kernel and generate the FAI image.  
Return to the build directory and rebuild the kernel using the command below.
```
$ cd ${build_dir}/build/ai-g-topst-main/
$ bitbake -C compile linux-topst
$ cd ${build_dir}
$ ./stitch-fai-ai.sh
```

Afterwards, flash the generated output_aig.fai to the board using FWDN, and you will be able to use the IMX219 sensor with the desired resolution.

#### 4.1.4.4 How to Increase the FPS of the IMX219 in Yocto: Driver and Device Tree
According to the IMX219 sensor description, the sensor supports high-framerate modes such as 1080p60, 720p180, and VGA206. Therefore, it is possible to increase the FPS for the resolutions supported by the imx219.c driver—1920×1080, 1640×1232, and 640×480. Since the ISP core on the AI-G platform supports up to 60 fps, each of these resolutions can be raised to a maximum of 60 fps.  

The formula for calculating FPS is:
<p align="center"><strong>{fps} = {pixel_rate}/{hts}x{vts}</strong></p>
Therefore, to increase the FPS, the pixel_rate, hts, and vts values must be adjusted.  
In the current driver implementation, both pixel_rate and hts are fixed. To raise the FPS, the only feasible approach is to increase the pixel_rate while keeping hts constant, and then adjust vts accordingly to achieve the desired frame rate.

To modify the FPS to 60, both the driver and the device tree must be updated.
Follow the guide below to change the FPS to 60.

##### 4.1.2.4.1 1920x1080 @ 60fps
To achieve 60 fps, the following relationship must hold:  
fps = pixel_rate / (hts × vts)
- pixel_rate = 182,400,000
- hts = 3448
- target fps = 60

the required VTS would be:
- vts = pixel_rate / (hts × fps) = 182,400,000 / (3448 × 60) ≈ 882

However, the VTS value must be greater than 1080, so this configuration is not valid.  
Therefore, to reach 60 fps, we must keep hts fixed, and instead adjust pixel_rate, vts, and the PLL_VT register.

The required changes are as follows:
1. imx219.c driver file  
    A. Increase the pixel rate and link frequency
    ```
    #define IMX219_PIXEL_RATE            182400000    →   #define IMX219_PIXEL_RATE            278400000
    #define IMX219_DEFAULT_LINK_FREQ     456000000   →   #define IMX219_DEFAULT_LINK_FREQ     696000000
    ``` 
    B. Update the VTS value for the 1080p mode:
    ```
    #define IMX219_VTS_30FPS_1080P       0x06e3       →   #define IMX219_VTS_30FPS_1080P       0x0542
    ```
    C. Modify the PLL_VT register in the 1920x1080 mode table:
    ```
    // imx219_reg mode_1920_1080_regs[]
    {0x0307, 0x39}   →   {0x0307, 0x57}
    ```
2. tcc805x-videoinput-mipi0-imx219.dtsi device tree file  
    A. Update the link frequency to match the new pixel rate:
    ```
    // &i2c7
    /bits/ 64 <456000000> → /bits/ 64 <696000000>
    ```
    B. Update the hs-settle value:
    ```
    hs-settle = <13> → hs-settle = <35>
    ```
3. Rebuild the kernel and generate the FAI image.  
    Return to the build directory and rebuild the kernel using the command below.
    ```
    $ cd ${build_dir}/build/d3-g-topst-main/
    $ bitbake -C compile linux-topst
    $ cd ${build_dir}
    $ ./stitch-fai-d3.sh
    ```
Using the command below on AI-G, you can confirm that the FPS output is 59.9, which corresponds to 60 fps.
```
$ v4l2-ctl --stream-mmap=3 --stream-count=300 --stream-to=/dev/null --verbose
```

##### 4.1.2.4.2 1640x1232 @ 60fps
To achieve 60 fps, the following relationship must hold:  
fps = pixel_rate / (hts × vts)
- pixel_rate = 182,400,000
- hts = 3448
- target fps = 60

the required VTS would be:
- vts = pixel_rate / (hts × fps) = 182,400,000 / (3448 × 60) ≈ 882

However, the VTS value must be greater than 1080, so this configuration is not valid.  
Therefore, to reach 60 fps, we must keep hts fixed, and instead adjust pixel_rate, vts, and the PLL_VT register.

The required changes are as follows:
1. imx219.c driver file  
    A. Increase the pixel rate and link frequency
    ```
    #define IMX219_PIXEL_RATE            182400000    →   #define IMX219_PIXEL_RATE            278400000
    #define IMX219_DEFAULT_LINK_FREQ     456000000   →   #define IMX219_DEFAULT_LINK_FREQ     696000000
    ``` 
    B. Update the VTS value for the 1640_1232 mode:
    ```
    #define IMX219_VTS_30FPS_BINNED       0x06e3       →   #define IMX219_VTS_30FPS_BINNED       0x0542
    ```
    C. Modify the PLL_VT register in the 1920x1080 mode table:
    ```
    // imx219_reg mode_1640_1232_regs[]
    {0x0307, 0x39}   →   {0x0307, 0x57}
    ```
2. tcc805x-videoinput-mipi0-imx219.dtsi device tree file  
    A. Update the link frequency to match the new pixel rate:
    ```
    // &i2c7
    /bits/ 64 <456000000> → /bits/ 64 <696000000>
    ```
    B. Update the hs-settle value:
    ```
    hs-settle = <13> → hs-settle = <34>
    ```
3. Rebuild the kernel and generate the FAI image.  
    Return to the build directory and rebuild the kernel using the command below.
    ```
    $ cd ${build_dir}/build/d3-g-topst-main/
    $ bitbake -C compile linux-topst
    $ cd ${build_dir}
    $ ./stitch-fai-d3.sh
    ```
Using the command below on AI-G, you can confirm that the FPS output is 59.9, which corresponds to 60 fps.
```
$ v4l2-ctl --stream-mmap=3 --stream-count=300 --stream-to=/dev/null --verbose
```

##### 4.1.2.4.3 640x480 @ 60fps
To achieve 60 fps, the following relationship must hold:  
fps = pixel_rate / (hts × vts)
- pixel_rate = 182,400,000
- hts = 3448
- target fps = 60

the required VTS would be:
- vts = pixel_rate / (hts × fps) = 182,400,000 / (3448 × 60) ≈ 882

Since the VTS value is greater than 480, the condition is satisfied. As in the previous example, we will adjust the pixelrate and VTS to change the FPS while keeping HTS fixed.  
You may also adjust the FPS by modifying only the VTS value without changing the pixelrate. However, the 0x0307 register value of the IMX219 must remain unchanged.

The required changes are as follows:
1. imx219.c driver file  
    A. Increase the pixel rate and link frequency
    ```
    #define IMX219_PIXEL_RATE            182400000    →   #define IMX219_PIXEL_RATE            278400000
    #define IMX219_DEFAULT_LINK_FREQ     456000000   →   #define IMX219_DEFAULT_LINK_FREQ     696000000
    ``` 
    B. Update the VTS value for the 640_480 mode:
    ```
    #define IMX219_VTS_30FPS_640x480       0x06e3       →   #define IMX219_VTS_30FPS_640x480       0x0542
    ```
    C. Modify the PLL_VT register in the 640x480 mode table:
    ```
    // imx219_reg mode_640_480_regs[]
    {0x0307, 0x39}   →   {0x0307, 0x57}
    ```
2. tcc805x-videoinput-mipi0-imx219.dtsi device tree file  
    A. Update the link frequency to match the new pixel rate:
    ```
    // &i2c7
    /bits/ 64 <456000000> → /bits/ 64 <696000000>
    ```
    B. Update the hs-settle value:
    ```
    hs-settle = <13> → hs-settle = <26>
    ```
3. Rebuild the kernel and generate the FAI image.  
    Return to the build directory and rebuild the kernel using the command below.
    ```
    $ cd ${build_dir}/build/d3-g-topst-main/
    $ bitbake -C compile linux-topst
    $ cd ${build_dir}
    $ ./stitch-fai-d3.sh
    ```
Using the command below on AI-G, you can confirm that the FPS output is 59.9, which corresponds to 60 fps.
```
$ v4l2-ctl --stream-mmap=3 --stream-count=300 --stream-to=/dev/null --verbose
```

## 4.2 GMSL Camera Setup Guide
### 4.2.1 D3-G GMSL Camera Setup Guide
By using a Deserializer board, you can connect up to four cameras to a single MIPI CSI port. Since the D3-G provides two MIPI CSI ports, you may choose one of the following configurations:
- Use four cameras on the MIPI0 port
- Use four cameras on the MIPI1 port
- Use both MIPI0 and MIPI1 to connect a total of eight cameras

When configuring all eight cameras, the D3-G's display expansion feature—which supports up to four displays—can be used with up to three displays.

**Note:** This guide uses the IMX290 (cxd5700) FHD GMSL camera.  
If you intend to use a different GMSL camera, additional camera porting will be required.

#### 4.2.1.1 How to use the MIPI0 Port
First, you must enable the kernel configuration for both the GMSL cameras and the SerDes board.  
Add the following entries to the  
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
After modifying the option above, rebuild the image using the following command.
```
$ bitbake -c cleansstate isp-firmware
$ bitbake -c cleansstate isp-server
$ bitbake telechips-topst-image
```
Next, you must modify the device tree in the kernel. Follow the guide below to apply the changes and rebuild the image.
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
7. Rebuild the kernel and generate the FAI image.  
    Return to the build directory and rebuild the kernel using the command below
    ```
    $ cd ${build_dir}/build/ai-g-topst-main/
    $ bitbake -C compile linux-topst
    $ cd ${build_dir}
    $ ./stitch-fai-ai.sh
    ```

After completing the build according to the guide above, the GMSL cameras will be available under /dev/ as video4, video5, video6, and video7.

#### 4.2.1.2 How to use the MIPI1 Port
First, you must enable the kernel configuration for both the GMSL cameras and the SerDes board.  
Add the following entries to the  
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
After modifying the option above, rebuild the image using the following command.
```
$ bitbake -c cleansstate isp-firmware
$ bitbake -c cleansstate isp-server
$ bitbake telechips-topst-image
```

Next, you must modify the device tree in the kernel. Follow the guide below to apply the changes and rebuild the image.
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
4. Rebuild the kernel and generate the FAI image.  
    Return to the build directory and rebuild the kernel using the command below.
    ```
    $ cd ${build_dir}/build/ai-g-topst-main/
    $ bitbake -C compile linux-topst
    $ cd ${build_dir}
    $ ./stitch-fai-ai.sh
    ```

After completing the build according to the guide above, the GMSL cameras will be available under /dev/ as video4, video5, video6, and video7.

#### 4.2.1.3 How to use the MIPI0, 1 Port
First, you must enable the kernel configuration for both the GMSL cameras and the SerDes board.  
Add the following entries to the  
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

After modifying the option above, rebuild the image using the following command.
```
$ bitbake -c cleansstate isp-firmware
$ bitbake -c cleansstate isp-server
$ bitbake telechips-topst-image
```

Because the display and videoinput paths overlap in VIOC, the 4-display expansion cannot be used. Therefore, you must first disable one of the conflicting paths in the display configuration.
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

Next, you must modify the device tree in the kernel. Follow the guide below to apply the changes and rebuild the image.
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
5. Rebuild the kernel and generate the FAI image.  
    Return to the build directory and rebuild the kernel using the command below
    ```
    $ cd ${build_dir}/build/ai-g-topst-main/
    $ bitbake -C compile linux-topst
    $ cd ${build_dir}
    $ ./stitch-fai-ai.sh
    ```
After completing the build according to the guide above, the GMSL cameras will be available under /dev/ as video0, video1, video2, video3, 4, video5, video6, and video7.

### 4.2.2 AI-G GMSL Camera Setup Guide
By using a Deserializer board, you can connect up to four cameras to a single MIPI CSI port.  
The AI-G board provides a MIPI CSI data bandwidth of 1.5 Gbps per lane, allowing up to three FHD cameras to operate simultaneously. Accordingly, this guide covers the connection of three FHD GMSL cameras.  
For HD cameras, up to four units can be supported.

**Note:** This guide uses the IMX290 (cxd5700) FHD GMSL camera.  
If you intend to use a different GMSL camera, additional camera porting will be required.

#### 4.2.2.1 How to use the MIPI CSI Port
First, you must enable the kernel configuration for both the GMSL cameras and the SerDes board.  
Add the following entries to the  
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
After modifying the option above, rebuild the image using the following command.
```
$ bitbake -c cleansstate isp-firmware
$ bitbake -c cleansstate isp-server
$ bitbake telechips-topst-ai-image
```

Next, you must modify the device tree in the kernel. Follow the guide below to apply the changes and rebuild the image.
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
3. Rebuild the kernel and generate the FAI image.  
    Return to the build directory and rebuild the kernel using the command below
    ```
    $ cd ${build_dir}/build/ai-g-topst-main/
    $ bitbake -C compile linux-topst
    $ cd ${build_dir}
    $ ./stitch-fai-ai.sh
    ```
After completing the build according to the guide above, the GMSL cameras will be available under /dev/ as video0, video1 and video2.

# 5. Sample Codes and Commands
This chapter provides sample codes and commands demonstrating how to use MIPI CSI cameras, GMSL cameras, and USB cameras on both the D3-G and AI-G platforms. This section provides a brief overview of camera playback methods:  
on the D3-G, camera streams can be viewed using GStreamer or OpenCV,  
while on the AI-G, camera playback is handled through the application framework.

## 5.1 Sample Codes and Commands for Camera Playback
### 5.1.1 MIPI CSI Camera User Guide
This section describes how to display MIPI CSI camera video on both Yocto and Ubuntu environments.

#### 5.1.1.1 MIPI CSI Camera User Guide on D3-G (OV5647)
##### 5.1.1.1.1 Using OV5647 on Yocto Image
When using the official Yocto image provided on the [topst.ai DOCS page](https://topst.ai/tech/docs?page=624bd237b3013e87c05c125b8031e2f370ccca2b), or an image generated by building Yocto manually, the OV5647 camera operates with a default resolution of 1296×972 at 30 fps. Therefore, camera playback in this environment will use 1296×972 at 30 fps.  
Follow the steps below:
1. Stop the currently running topst-welcome service
    ```
    $ sudo systemctl stop topst-welcome
    ```
2. Enter the following command in the UART console
    ```
    $ export XDG_RUNTIME_DIR=/run/user/root
    ```
3. Play the camera stream using a GStreamer command as shown below
    ```
    $ gst-launch-1.0 v4l2src device=/dev/video0 io-mode=2 ! video/x-raw,format=NV12,width=1296,height=972,framerate=30/1 ! videoconvert ! waylandsink sync=false
    ```
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/accessories/Camera/5.1%201296%C3%97972%20ov5647%20camera%20out%20display%20on%20yocto.png"></p>
<p align="center"><strong>Figure 5.1 1296×972 OV5647 Camera Out Display on Yocto</strong></p>

**Note:** Although the resolution is 1296×972, you can play the video in full screen by adding the fullscreen=true option at the end of the command.

##### 5.1.1.1.2 Using OV5647 on Ubuntu Image
When using the official Ubuntu image provided on the [topst.ai DOCS page](https://topst.ai/tech/docs?page=624bd237b3013e87c05c125b8031e2f370ccca2b), the OV5647 camera operates with a default resolution of 1296×972 at 30 fps. Therefore, camera playback in this environment will use 1296×972 at 30 fps.  
Follow the steps below:
1. - If connected via UART: Enter the following command in the UART console when you logged in with your topst account
    ```
    $ export XDG_RUNTIME_DIR=/run/user/1000
    ```
    - If controlling directly on the display: Open a terminal window
2. Play the camera stream using a GStreamer command as shown below. Because hardware-accelerated Wayland rendering is not available on Ubuntu, H.265 encoding/decoding is used instead to leverage VPU acceleration for playback
    ```
    $ gst-launch-1.0 v4l2src device=/dev/video0 io-mode=2 ! video/x-raw,format=NV12,width=1280,height=720,framerate=30/1 ! v4l2h265enc ! h265parse ! v4l2h265dec ! videoconvert ! waylandsink sync=false
    ```
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/accessories/Camera/5.2%201296%C3%97972%20ov5647%20camera%20out%20display%20on%20ubuntu.png"></p>
<p align="center"><strong>Figure 5.2 1296×972 OV5647 Camera Out Display on Ubuntu</strong></p>

**Note:** Although the resolution is 1296×972, you can play the video in full screen by adding the fullscreen=true option at the end of the command.

In addition to GStreamer, you can also use OpenCV to display the camera stream. Follow the steps below to easily preview the camera video using OpenCV.
1. Install OpenCV
    ```
    $ sudo apt-get install python3-opencv
    ```
2. Write the following code inside the opencv_cam.py file
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
3. Run opencv_cam.py with Python
    ```
    $ python3 opencv_cam.py
    ```
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/accessories/Camera/5.3%201296%C3%97972%20opencv%20ov5647%20camera%20out%20display%20on%20ubuntu.png"></p>
<p align="center"><strong>Figure 5.3 1296×972 OV5647 Camera Output Running on Ubuntu with OpenCV</strong></p>

##### 5.1.1.1.3 Gstreawmer Pipeline Configuration for Each Resolution on D3-G
Specify the appropriate GStreamer pipeline options for each resolution, and then run the camera stream.
1. 1920x1080 @ 30fps
    ```
    $ gst-launch-1.0 v4l2src device=/dev/video0 io-mode=2 ! video/x-raw,format=NV12,width=1920,height=1080,framerate=30/1 ! videoconvert ! waylandsink sync=false
    ```
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/accessories/Camera/5.4%201920x1080%20ov5647%20camera%20out%20display%20on%20yocto.png"></p>
    <p align="center"><strong>Figure 5.4 1920x1080 OV5647 Camera Out Display on Yocto</strong></p>
2. 1296x972 @ 30fps
    ```
    $ gst-launch-1.0 v4l2src device=/dev/video0 io-mode=2 ! video/x-raw,format=NV12,width=1296,height=972,framerate=30/1 ! videoconvert ! waylandsink sync=false
    ```
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/accessories/Camera/5.1%201296%C3%97972%20ov5647%20camera%20out%20display%20on%20yocto.png"></p>
    <p align="center"><strong>Figure 5.5 1296x972 OV5647 Camera Out Display on Yocto</strong></p>
3. 640x480 @ 60fps
    ```
    $ gst-launch-1.0 v4l2src device=/dev/video0 io-mode=2 ! video/x-raw,format=NV12,width=640,height=480,framerate=60/1 ! videoconvert ! waylandsink sync=false
    ```
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/accessories/Camera/5.6%20640x480%20ov5647%20camera%20out%20display%20on%20yocto.png"></p>
    <p align="center"><strong>Figure 5.6 640x480 OV5647 Camera Out Display on Yocto</strong></p>

Additionally, you can configure a pipeline that uses the H.265 encoder and decoder to enable hardware-accelerated playback.
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

    For resolution changes, refer to Section 4.1.2.2.

#### 5.1.1.2 MIPI CSI Camera User Guide on D3-G (IMX219)
##### 5.1.1.2.1 Using IMX219 on Yocto Image
When using the official Yocto image provided on the [topst.ai DOCS page](https://topst.ai/tech/docs?page=624bd237b3013e87c05c125b8031e2f370ccca2b), or an image generated by building Yocto manually, the IMX219 camera operates with a default resolution of 1640×1232 at 30 fps. Therefore, camera playback in this environment will use 1640×1232 at 30 fps.  
Follow the steps below:
1. Stop the currently running topst-welcome service
    ```
    $ sudo systemctl stop topst-welcome
    ```
2. Enter the following command in the UART console
    ```
    $ export XDG_RUNTIME_DIR=/run/user/root
    ```
3. Play the camera stream using a GSTreamer command as shown below
    ```
    $ gst-launch-1.0 v4l2src device=/dev/video0 io-mode=2 ! video/x-raw,format=NV12,width=1640,height=1232,framerate=30/1 ! videoconvert ! waylandsink sync=false
    ```
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/accessories/Camera/5.7%201640x1232%20imx219%20camera%20out%20display%20on%20yocto.png"></p>
<p align="center"><strong>Figure 5.7 1640x972 IMX219 Camera Out Display on Yocto</strong></p>

**Note:** Although the resolution is 1640×1232, you can play the video in full screen by adding the fullscreen=true option at the end of the command.

##### 5.1.1.2.2 Using IMX219 on Ubuntu Image
When using the official Ubuntu image provided on the [topst.ai DOCS page](https://topst.ai/tech/docs?page=624bd237b3013e87c05c125b8031e2f370ccca2b), the IMX219 camera operates with a default resolution of 1640×1232 at 30 fps. Therefore, camera playback in this environment will use 1640×1232 at 30 fps.  
Follow the steps below:
1. - If connected via UART: Enter the following command in the UART console when you logged in with your topst account
    ```
    $ export XDG_RUNTIME_DIR=/run/user/1000
    ```
    - If controlling directly on the display: Open a terminal window
2. Play the camera stream using a GStreamer command as shown below. Because hardware-accelerated Wayland rendering is not available on Ubuntu, H.265 encoding/decoding is used instead to leverage VPU acceleration for playback
    ```
    $ gst-launch-1.0 v4l2src device=/dev/video0 io-mode=2 ! video/x-raw,format=NV12,width=1600,height=1200,framerate=30/1 ! v4l2h265enc ! h265parse ! v4l2h265dec ! videoconvert ! waylandsink sync=false
    ```
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/accessories/Camera/5.8%201640x1232%20imx219%20camera%20out%20display%20on%20ubuntu.png"></p>
<p align="center"><strong>Figure 5.8 1640x972 IMX219 Camera Out Display on Ubuntu</strong></p>

**Note:** Although the resolution is 1640×1232, you can play the video in full screen by adding the fullscreen=true option at the end of the command.

In addition to GStreamer, you can also use OpenCV to display the camera stream. Follow the steps below to easily preview the camera video using OpenCV.
1. Install OpenCV
    ```
    $ sudo apt-get install python3-opencv
    ```
2. Write the following code inside the opencv_cam.py file.
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
3. Run opencv_cam.py with Python
```
$ python3 opencv_cam.py
```
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/accessories/Camera/5.9%201640x1232%20opencv%20imx219%20camera%20out%20display.png"></p>
<p align="center"><strong>Figure 5.9 1640×1232 IMX219 Camera Output Running on Ubuntu with OpenCV</strong></p>

##### 5.1.1.2.3 GStreamer Pipeline Configuration for Each Resolution on D3-G
Specify the appropriate GStreamer pipeline options for each resolution, and then run the camera stream.
1. 1920x1080 @ 30fps
    ```
    $ gst-launch-1.0 v4l2src device=/dev/video0 io-mode=2 ! video/x-raw,format=NV12,width=1920,height=1080,framerate=30/1 ! videoconvert ! waylandsink sync=false
    ```
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/accessories/Camera/5.10%201920x1080%20imx219%20camera%20out%20display%20on%20yocto.png"></p>
    <p align="center"><strong>Figure 5.10 1920x1080 IMX219 Camera Out Display on Yocto</strong></p>
2. 1640x1232 @ 30fps
    ```
    $ gst-launch-1.0 v4l2src device=/dev/video0 io-mode=2 ! video/x-raw,format=NV12,width=1640,height=1232,framerate=30/1 ! videoconvert ! waylandsink sync=false
    ```
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/accessories/Camera/5.7%201640x1232%20imx219%20camera%20out%20display%20on%20yocto.png"></p>
    <p align="center"><strong>Figure 5.11 1620x1232 IMX219 Camera Out Display on Yocto</strong></p>
3. 640x480 @ 30fps
    ```
    $ gst-launch-1.0 v4l2src device=/dev/video0 io-mode=2 ! video/x-raw,format=NV12,width=640,height=480,framerate=30/1 ! videoconvert ! waylandsink sync=false
    ```
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/accessories/Camera/5.12%20640x480%20imx219%20camera%20out%20display%20on%20yocto.png"></p>
    <p align="center"><strong>Figure 5.12 640x480 IMX219 Camera Out Display on Yocto</strong></p>

Additionally, you can configure a pipeline that uses the H.265 encoder and decoder to enable hardware-accelerated playback.
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

For resolution changes, refer to Section 4.1.3.3.

#### 5.1.1.3 MIPI CSI Camera User Guide on AI-G (OV5647)
##### 5.1.1.3.1 Using OV5647 on Yocto Image
On the AI-G, two applications are available: one for camera playback with inference results, and another for simple camera viewing. You may choose either application depending on your use case.
- tcnnapp
    ```
    $ tcnnapp
    ```
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/accessories/Camera/5.13%20ov5647%20camera%20out%20display%20with%20running%20tcnnapp%20on%20yocto.png"></p>
    <p align="center"><strong>Figure 5.13 OV5647 Camera Out Display with running tcnnapp on Yocto</strong></p>
- tcnncameraapp
    ```
    $ tcnncameraapp
    ```
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/accessories/Camera/5.14%20ov5647%20camera%20out%20display%20with%20running%20tcnncameraapp%20on%20yocto.png"></p>
    <p align="center"><strong>Figure 5.14 OV5647 Camera Out Display with running tcnncameraapp on Yocto</strong></p>

##### 5.1.1.3.2 Using on Ubuntu Image
On the AI-G, two applications are available: one for camera playback with inference results, and another for simple camera viewing. You may choose either application depending on your use case.
- tcnnapp
    ```
    $ tcnnapp
    ```
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/accessories/Camera/5.13%20ov5647%20camera%20out%20display%20with%20running%20tcnnapp%20on%20yocto.png"></p>
    <p align="center"><strong>Figure 5.15 OV5647 Camera Out Display with running tcnnapp on Ubuntu</strong></p>
- tcnncameraapp
    ```
    $ tcnncameraapp
    ```
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/accessories/Camera/5.14%20ov5647%20camera%20out%20display%20with%20running%20tcnncameraapp%20on%20yocto.png"></p>
    <p align="center"><strong>Figure 5.16 OV5647 Camera Out Display with running tcnncameraapp on Ubuntu</strong></p>

#### 5.1.1.4 MIPI CSI Camera User Guide on AI-G (IMX219)
##### 5.1.1.4.1 Using IMX219 on Yocto Image
On the AI-G, two applications are available: one for camera playback with inference results, and another for simple camera viewing. You may choose either application depending on your use case.
- tcnnapp
    ```
    $ tcnnapp
    ```
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/accessories/Camera/5.17%20imx219%20camera%20out%20display%20with%20running%20tcnnapp%20on%20yocto.png"></p>
    <p align="center"><strong>Figure 5.17 OV5647 Camera Out Display with running tcnnapp on Yocto</strong></p>
- tcnncameraapp
    ```
    $ tcnncameraapp
    ```
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/accessories/Camera/5.18%20imx219%20camera%20out%20display%20with%20running%20tcnncameraapp%20on%20yocto.png"></p>
    <p align="center"><strong>Figure 5.18 OV5647 Camera Out Display with running tcnncameraapp on Yocto</strong></p>

##### 5.1.1.4.2 Using IMX219 on Ubuntu Image
On the AI-G, two applications are available: one for camera playback with inference results, and another for simple camera viewing. You may choose either application depending on your use case.
- tcnnapp
    ```
    $ tcnnapp
    ```
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/accessories/Camera/5.17%20imx219%20camera%20out%20display%20with%20running%20tcnnapp%20on%20yocto.png"></p>
    <p align="center"><strong>Figure 5.17 OV5647 Camera Out Display with running tcnnapp on Yocto</strong></p>
- tcnncameraapp
    ```
    $ tcnncameraapp
    ```
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/accessories/Camera/5.18%20imx219%20camera%20out%20display%20with%20running%20tcnncameraapp%20on%20yocto.png"></p>
    <p align="center"><strong>Figure 5.18 OV5647 Camera Out Display with running tcnncameraapp on Yocto</strong></p>

### 5.1.2 GMSL Camera User Guide
This section describes how to display GMSL camera video on both Yocto and Ubuntu environments.

#### 5.1.2.1 GMSL Camera User Guide on D3-G
##### 5.1.2.1.1 Using GMSL Camera on Yocto Image
When using the official Yocto image provided on the [topst.ai DOCS page](https://topst.ai/tech/docs?page=624bd237b3013e87c05c125b8031e2f370ccca2b), or an image generated by building Yocto manually, the GMSL camera operates with a default resolution of 1920×1080 at 30 fps. Therefore, camera playback in this environment will use 1920×1080 at 30 fps.  
Follow the steps below:
1. Stop the currently running topst-welcome service
    ```
    $ sudo systemctl stop topst-welcome
    ```
2. Enter the following command in the UART console
    ```
    $ export XDG_RUNTIME_DIR=/run/user/root
    ```
3. Play the camera stream using a GStreamer command as shown below
    ```
    $ gst-launch-1.0 v4l2src device=/dev/video4 io-mode=2 ! video/x-raw,format=NV12,width=1920,height=1080,framerate=30/1 ! videoconvert ! waylandsink sync=false
    ```

Additionally, by running the script below, you can display the camera feeds in a four-way split view by using gpu.
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

GMSL cameras appear as video4, video5, video6, and video7, and you can select any of these devices as needed.  
If eight cameras are connected, the system will enumerate them as video0 through video8, allowing you to choose from any of those device nodes.

##### 5.1.2.1.2 Using GMSL Camera on Ubuntu Image
When using the official Ubuntu image provided on the [topst.ai DOCS page](https://topst.ai/tech/docs?page=624bd237b3013e87c05c125b8031e2f370ccca2b), the GMSL camera operates with a default resolution of 1920×1080 at 30 fps. Therefore, camera playback in this environment will use 1920×1080 at 30 fps.  
Follow the steps below:
1. - If connected via UART: Enter the following command in the UART console when you logged in with your topst account
    ```
    $ export XDG_RUNTIME_DIR=/run/user/1000
    ```
    - If controlling directly on the display: Open a terminal window
2. Play the camera stream using a GStreamer command as shown below. Because hardware-accelerated Wayland rendering is not available on Ubuntu, H.265 encoding/decoding is used instead to leverage VPU acceleration for playback
    ```
    $ gst-launch-1.0 v4l2src device=/dev/video0 io-mode=2 ! video/x-raw,format=NV12,width=1920,height=1080,framerate=30/1 ! v4l2h265enc ! h265parse ! v4l2h265dec ! videoconvert ! waylandsink sync=false
    ```

Additionally, by running the script below, you can display the camera feeds in a four-way split view by using gpu.
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

Moreover you can also use OpenCV to display the camera stream. Follow the steps below to easily preview the camera video using OpenCV.
1. Install OpenCV
    ```
    $ sudo apt-get install python3-opencv
    ```
2. Write the following code inside the opencv_cam.py file
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
3. Run opencv_cam.py file with Python
    ```
    $ python3 opencv_cam.py
    ```

GMSL cameras appear as video4, video5, video6, and video7, and you can select any of these devices as needed.  
If eight cameras are connected, the system will enumerate them as video0 through video8, allowing you to choose from any of those device nodes.

#### 5.1.2.2 GMSL Camera User Guide on AI-G
##### 5.1.2.2.1 Using GMSL Camera on Yocto Image
On the AI-G, two applications are available: one for camera playback with inference results, and another for simple camera viewing. You may choose either application depending on your use case.
- tcnnapp
- tcnncameraapp

GMSL cameras appear as **video0**, **video1**, and **video2**, and you may select any of these devices as needed.
Each application defaults to using video2, but you can change the video device using the **-p option**.
The example below demonstrates how to select **video0**.

- tcnnapp
    ```
    $ tcnnapp -p /dev/video0
    ```
- tcnncameraapp
    ```
    $ tcnncameraapp -p /dev/video0
    ```

##### 5.1.2.2.2 Using GMSL Camera on Ubuntu Image
On the AI-G, two applications are available: one for camera playback with inference results, and another for simple camera viewing. You may choose either application depending on your use case.
- tcnnapp
- tcnncameraapp

GMSL cameras appear as **video0**, **video1**, and **video2**, and you may select any of these devices as needed.
Each application defaults to using video2, but you can change the video device using the **-p option**.
The example below demonstrates how to select **video0**.

- tcnnapp
    ```
    $ tcnnapp -p /dev/video0
    ```
- tcnncameraapp
    ```
    $ tcnncameraapp -p /dev/video0
    ```

### 5.1.3 USB Camera User Guide
This section describes how to display USB camera video on both Yocto and Ubuntu environments.
The AI-G does not include a USB interface; therefore, no USB camera guide is provided for this platform.

#### 5.1.3.1 USB Camera User Guide on D3-G
In this document, the explanations will be based on a USB camera that supports 1920×1080 at 30 fps

**Note:** Since the MIPI camera is assigned to **/dev/video0** by default, the USB camera is created as /dev/video1.
Please ensure that you use **/dev/video1** when operating the USB camera.

##### 5.1.3.1.1 Using USB Camera on Yocto Image
When using the official Yocto image provided on the [topst.ai DOCS page](https://topst.ai/tech/docs?page=624bd237b3013e87c05c125b8031e2f370ccca2b), or an image generated by building Yocto manually, the USB camera operates using the resolution and frame rate defined by the camera’s own specifications. Therefore, the video will be played back at the default resolution and FPS provided by the USB camera.  
Follow the steps below:
1. Stop the currently running topst-welcome service
    ```
    $ sudo systemctl stop topst-welcome
    ```
2. Enter the following command in the UART console
    ```
    $ export XDG_RUNTIME_DIR=/run/user/root
    ```
3. Play the camera stream using a GStreamer command as shown below. When checking the USB camera information with v4l2-ctl -d /dev/video1 --list-formats-ext, the supported format is shown as MJPEG. Therefore, jpegdec is used
    ```
    $ gst-launch-1.0 v4l2src device=/dev/video1 ! image/jpeg,width=1920,height=1080 ! jpegdec ! videoconvert ! waylandsink
    ```

##### 5.1.3.1.2 Using USB Camera on Ubuntu Image
When using the official Ubuntu image provided on the [topst.ai DOCS page](https://topst.ai/tech/docs?page=624bd237b3013e87c05c125b8031e2f370ccca2b), or an image generated manually, the USB camera operates using the resolution and frame rate defined by the camera’s own specifications. Therefore, the video will be played back at the default resolution and FPS provided by the USB camera.  
Follow the steps below:
1. - If connected via UART: Enter the following command in the UART console when you logged in with your topst account
    ```
    $ export XDG_RUNTIME_DIR=/run/user/1000
    ```
    - If controlling directly on the display: Open a terminal window
2. Play the camera stream using a GStreamer command as shown below. When checking the USB camera information with v4l2-ctl -d /dev/video1 --list-formats-ext, the supported format is shown as MJPEG. Therefore, jpegdec is used
    ```
    $ gst-launch-1.0 v4l2src device=/dev/video1 ! image/jpeg,width=1920,height=1080 ! jpegdec ! videoconvert ! waylandsink
    ```
3. To use H.265 encoding and decoding, the video must be converted to the NV12 format, which is supported by v4l2src. Therefore, the pipeline should be configured as shown below
    ```
    $ gst-launch-1.0 v4l2src device=/dev/video1 io-mode=2 ! image/jpeg,width=640,height=480,framerate=30/1 ! jpegdec ! videoconvert ! video/x-raw,format=NV12 !  v4l2h265enc ! h265parse ! v4l2h265dec ! videoconvert ! waylandsink
    ```

**Note:** you can play the video in full screen by adding the fullscreen=true option at the end of the command.

In addition to GStreamer, you can also use OpenCV to display the camera stream. Follow the steps below to easily preview the camera video using OpenCV.
1. Install OpenCV
    ```
    $ sudo apt-get install python3-opencv
    ```
2. Write the following code inside the opencv_cam.py file
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
3. Run opencv_cam.py with Python
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

# 6. Troubleshooting
Chapter 6 covers troubleshooting for MIPI CSI cameras, GMSL cameras, and USB cameras.

## 6.1 MIPI CSI and GMSL Camera Troubleshooting
If you encounter issues with MIPI CSI or GMSL cameras, refer to the debugging guide below to troubleshoot the problem.

### 6.1.1 Boot-Time Issues (Probe Stage)
#### 6.1.1.1 Sensor Probe Fail
**Symptoms**
- The sensor is not detected during boot
- /dev/videoX nodes are not created
- The sensor entity does not appear in ‘media-ctrl -p’ output  

**Example dmesg Logs**
```
[    3.421000] imx219 2-0010: probing sensor failed
[    3.421120] imx219 2-0010: i2c read failed: addr=0x3000, ret=-5
[    3.200400] imx219 0-0010: reset gpio request failed
[    2.912830] imx219 1-0010: failed to get vddio regulator
```
**Possible Causes**
- Incorrect I2C address or bus configuration
- Incorrect polarity for RESET/PWDN GPIO
- Missing or incorrectly configured regulator power supplies

**Resolution**
- Verify I2C address, bus number, and GPIO settings in the device tree
- Check for missing or wrongly defined regulator nodes
- Recheck sensor module cable orientation and pin alignment

#### 6.1.1.2 I2C Communication Failure
**Example dmesg Logs**
```
[    3.101001] imx219 2-0010: i2c read error: -121
[    4.112121] i2c i2c-2: transfer failed: -110
```
**Possible Causes**
- SDA/SCL lines are shorted or disconnected
- I2C bus number in the device tree does not match the actual hardware configuration

**Resolution**
- Use “i2cdetect -y <bus>” to check whether the sensor responds at the expected I2C address
- Inspect the cable and connector for damage, improper seating, or loose contacts

### 6.1.2 Media Controller & Graph Configuration Issues
(verified using ‘media-ctl -p’)

#### 6.1.2.1 Missing Sensor Entity or Unconfigured Links
**Example 'media-ctl -p' Output**
```
0 entities, 0 interfaces, 0 pads, 0 links
```
**Possible Causes**
- Missing endpoint (port) node in the device tree
- Incorrect land count or ‘bus-type’ settings
- Missing ‘link-frequencies’ entry

**Resolution**
- Verify the correctness of ‘port@0/1’ endpoint definitions
- Check the ‘data-lanes’ array for proper order and number of lanes
- Ensure that ‘link-frequencies’ matches the sensor specifications

#### 6.1.2.2 Format / Mode Mismatch
**Possible Causes**
- The ‘supported_mode[]’ in the sensor driver does not match the ‘hs-settle’ value defined in the DTS
- Mismatch in the number of CSI-2 lanes between the driver and the device tree

**Resolution**
- Review the resolution, pixel rate, and HTS/VTS values in ‘supported_modes[]’, then adjust the ‘hs-settle’ value in the DTS accordingly
- Ensure consistency between the DTS configuration and the sensor driver settings

### 6.1.3 V4L2 Streaming Issues
#### 6.1.3.1 VIDIOC_STREAMON Failure (Unable to Start Streaming)
**Possible Causes**
- Incorrect sensor register configuration
- Pixel rate or PLL settings do not match expected values
- HTS/VTS conflicts causing invalid frame timing

**Resolution**
- Revalidate the pixel rate, VTS, and HTS values in the sensor’s mode table
- Check PLL divisors (0x030x registers) for correctness
- Verify that the device tree specifies the correct ‘hs-settle’ value for the selected resolution and FPS.

#### 6.1.3.2 Unsupported Format Request
**Resolution**
- heck the actual supported formats using the command velow, then retry streaming with a supported format:
    ```
    V4l2-ctl –list-formats-ext
    ```

### 6.1.4 CSI-2 Errors: SoT, CRC, and Related Issues
#### 6.1.4.1 SoT (Sync on Transmission) Error
**Possible Causes**
- MIPI timing configuration mismatch
- Pixel rate set too high
- Poor cable quality or excessive cable length

**Resolution**
- Reduce the pixel rate or link frequency
- Replace the cable or shorten its length
- Verify MIPI timing parameters

#### 6.1.4.2 CRC Error
**Example dmesg Logs**
```
[   13.700910] tccvin videoinput0: CSI-2 ERROR: CRC error
```
**Possible Causes**
- Degraded MIPI signal quality
- PLL or lane-speed mismatch

**Resolution**
- Adjust the hs-settle value
- Replace the cable
- Verify PLL configuration and lane speed settings

### 6.1.5 Pixelrate / Link-Frequency Errors
**Possible Causes**
- Exceeding the available CSI-2 lane bandwidth
- Incorrect PLL configuration

**Resolution**
- Recalculate the pixel rate and ensure it falls within the allowable CSI-2 bandwidth
- Adjust PLL divisors to achieve valid timing
- If necessary, reduce the frame rate (e.g., 30 -> 15fps) or lower the resolution

### 6.1.6 Device Tree (DTS) Configuration Errors
#### 6.1.6.1 Incompatible compatible String
**Possible Causes**
- The ‘compatible’ value in the DTS does not match the ‘of_device_id’ defined in the sensor driver
- The driver does not recognize the device node, preventing the probe from running

**Resolution**
- Update the DTS with the exact ‘compatible’ string defined in the sensor driver (e.g., “sony,imx219”)
- Rebuild the device tree and verify that the sensor probes correctly

#### 6.1.6.2 Endpoint Configuration Issues
**Possible Causes**
- Port numbers or ‘remote-endpoint’ references do not match between the sensor endpoint and the CSI endpoint
- ‘data-lanes’ or bus configuration does not meet the media graph requirements

**Resolution**
- Ensure the port numbers, ‘data-lanes’, and ‘remote-endpoint’ values match on both sides
- Use ‘media-ctl -p’ to verify that the media links are correctly established

#### Missing Link-Frequencies Property
**Possible Causes**
- The ‘link-frequencies’ field is missing from the endpoint, preventing the MIPI link speed from being calculated
- The format of the value (e.g., /bits/ 64) does not match what the driver expects

**Resolution**
- Add the correct ‘link-frequencies’ value (e.g., 456000000) according to the sensor specification
- Ensure the value format matches the driver requirements (such ad including /bits/ 64 if required)

### 6.1.7 Gstreamer Playback Issues
#### 6.1.7.1 'not negotiated' Error
**Possible Causes**
- Caps negotiation failure within the pipeline
- Wayland compositor format mismatch
- Videoconvert cannot handle certain raw formats

**Resolution**
- Use pipelines based on NV12 or YUY2, which provide broad compatibility
- Utilize ‘v4l2src io-mode=dmabuf’ to ensure zero-copy buffer handling and proper format negotiation

#### 6.1.7.2 Wayland Sink Initialization Failure
**Possible Causes**
- The Wayland compositor is not running, or no accessible display environment is available
- The pipeline is being launched over SSH or with an invalid DISPLAY/Wayland environment, preventing sink initialization

**Resolution**
- Verify that the Weston compositor is running
- Execute the pipeline within a local session or a properly configured Wayland environment

### 6.1.8 Hardware Issues
#### 6.1.8.1 Incorrect Cable Orientation
**Possible Causes**
- The FFC cable is connected in the wrong orientation or its pins are misaligned, preventing proper I2C/MIPI signal transmission
- The Sensor does not respond at all, resulting in no frames being received

**Resolution**
- Verify the connector orientation and ensure that the contact pins align according to the specification
- Check for cable damage or worn-out contacts

#### 6.1.8.2 Power Supply Issues
**Possible Causes**
- Sensor voltage rails (e.g., 1.2V / 2.8V) are unstable or not enabled
- Power enable GPIO is not asserted
- The sensor’s power-up sequence is not satisfied during initialization

**Resolution**
- Review regulator and GPIO configurations in the DTS and confirm that all required voltages are supplied correctly
- Ensure the sensor’s power sequence requirements are met (RESET _> PWDN -> clock enable)

## 6.2 USB Camera Troubleshooting
If you encounter issues with USB Camera, refer to the debugging guide below to troubleshoot the problem.

### 6.2.1 Camera Not Detected (USB DeviceNot Recognized)
**Example dmesg Logs**
```
usb 1-1: device descriptor read/64, error -71
uvcvideo: Failed to initialize the device
```
**Possible Causes**
- Insufficient USB Power or unstable power delivery, causing device initialization failure
- Faulty USB cable or port, or use of an incompatible USB hub

**Resolution**
- Try a different USB port or use a port with a stable power source
- Replace the USB cable or hub and reconnect the device to ensure proper enumeration

### 6.2.2 Limited or Empty Format List in v4l2-ctl
**Example dmesg Logs**
```
uvcvideo: Failed to query (GET_DEF) UVC control 2 on unit 1: -32
```
**Possible Causes**
- The camera does not support certain UVC controls or fails to report them during initialization
- Protocol errors between the device and driver prevent capability detection

**Resolution**
- Test using standard formats such as MJPEG or YUYV
- Test with another camera of the same model to determine whether the issue is related to UVC compatibility

### 6.2.3 GStreamer Playback: "not negotiated" or Caps Mismatch
**Possible Causes**
- The pipeline requests a format that the camera does not support (e.g., NV12, YUY2), resulting in caps negotiation failure
- At the selected resolution/frame rate, the camera may only provide MJPEG, but the pipeline requests a raw format
- The camera outputs MJPEG, but no JPEG decoder element (jpegdec or avdec_mjpeg) is included, so decoding cannot proceed

**Resolution**
- Check supported formats
    ```
    v4l2-ctl –list-formats-ext
    ```
- If the camera outputs MJPEG:
    ```
    v4l2src ! image/jpeg ! jpegdec ! videoconvert ! …
    ```
- If the camera supports raw formats (e.g., YUYV), configure the pipeline caps accordingly:  
    Use the raw format exactly as listed in ‘v4l2-ctl –list-formats-ext’

### 6.2.4 Resolution or FPS Setting Failure
**Possible Causes**
- The requested resolution or frame rate is not supported by the camera, resulting in negotiation failure

**Resolution**
- Check supported resolution/FPS combinations using ‘v4l2-ctl –list-formats-ext’

### 6.2.5 Video stuttering / Frame Drops
**Possible Causes**
- Insufficient USB bandwidth (shared hub or use of a USB 2.0 port)
- High CPU load from MJPEG decoding, causing the pipeline to fall behind

**Resolution**
- Use a USB 3.0 port or connect the camera directly without a hub
- Lower the MJPEG resolution or frame rate, or switch to a raw format if supported

### 6.2.6 Incorrect Colors or Corrupted Output
**Possible Causes**
- Errors during MJPEG -> NV12 conversion or colorspace conversion
- Certain format combinations may fail in v4l2convert or videoconvert

**Resolution**
- Explicitly insert jpegdec or avdec_mjpeg before videoconvert
- Simplify the pipeline for testing, for example:
    ```
    V4l2src ! jpegdec ! videoconvert ! waylandsink
    ```

### 6.2.7 Unexpected Device Disconnection or Re-Enumeration
**Example dmesg Logs**
```
usb 1-1: USB disconnect, device number 4
```
**Possible Causes**
- Unstable power delivery or poor cable contact
- Thermal issues causing the device to reset during prolonged use

**Resolution**
- Replace the USB cable or use a port with stable and sufficient power
- For cameras that generate significant heat, consider additional cooling solutions
