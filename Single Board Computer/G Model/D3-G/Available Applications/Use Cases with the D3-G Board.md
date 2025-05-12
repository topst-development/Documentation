# 1. Introduction 
This document provides usage examples using the TOPST D3-G.

This document includes information on the following: 
- Input Device
  - Keyboard 
  - Mouse
- Video Output
- Camera Connection
  - MIPI CSI
  - USB WebCam
- Storage Connection
  - SD Card
  - SATA HDD
  - NVME M.2 SSD
  - USB Storage
- Ethernet Connection
- 40 Pin GPIO Header
  - Available Sensor & Device
- JTAG Connection
- CAN Connection
<br/><br/>

# 2. Input Device
The D3-G supports two USB ports for connecting input devices.
It includes one USB 2.0 Type-A port and one USB 3.0 Type-A port, allowing users to connect a mouse or keyboard to directly control the board. 

***Note**: The USB Type-C port on the board is reserved for firmware downloads and cannot be used to connect input devices.

<p align="center"><img src="https://github.com/topst-development/Documentation/blob/main/Assets/TOPST%20D3-G/Software/input%20device.png?raw=true" width="500"></p>
<p align="center"><strong>Figure 1. Connect input device to D3-G </strong></p>
<br/><br/> 

# 3. Video Output
The D3-G board supports FHD monitors via its only DisplayPort (DP) output.
It also supports multi-display output using a daisy chain setup, allowing connection of up to two FHD monitors and one HD monitor simultaneously.

**Note**: To use HDMI, a separate active converter adapter is required.
<p align="center"><img src="https://github.com/topst-development/Documentation/blob/main/Assets/TOPST%20D3-G/Software/monitor.png?raw=true" width="500"></p>
<p align="center"><strong>Figure 2. Connect Monitor to D3-G </strong></p>
<br/><br/>

# 4. Camera Connection
The D3-G board supports camera functionality, offering flexibility for various applications.
You can connect either a MIPI CSI camera or a USB webcam, depending on your project requirements.
<br/>

## 4.1 USB Webcam
The D3-G board supports USB webcams, with resolutions up to Full HD (FHD).
You can test the webcam by following the steps below:
1. Connect the USB camera to a USB port on the board.
<p align="center"><img src="https://github.com/topst-development/Documentation/blob/main/Assets/TOPST%20D3-G/Software/webcam.png?raw=true" width="400"></p>
<p align="center"><strong>Figure 3. Connect webcam to D3-G </strong></p>

2. Connect the input devices(mouse&keyboard)and monitor to D3-G.
   
3. Boot the D3-G board.

4. Check the available /dev/video devices.
```
ls /dev/video*
```
5. Verify the video output using OpenCV (or vutils).
```
touch webcam.py
chmod a+x webcam.py
```
```
# You can edit the script file using vim or nano editor
# This is camera application python code using OpenCV
import cv2

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("\\@@ Camera open failed!")
    exit()

print("Press 'q' to exit the camera window.")

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
# run webcom.py
python3 webcam.py
```
<br/>

## 4.2 MIPI CSI
CSI stands for Camera Serial Interface, a standard interface defined by the MIPI Alliance for connecting camera modules to host processors.
It enables high-speed, low-power transmission of image data from the camera to the processor.

The D3-G board features two MIPI CSI channels(ch0, ch1), allowing users to attach camera modules that support FFC (Flat Flexible Cable) connections.
Currently, the D3-G board supports only the ArduCam (5MP) and Raspberry Pi v1 Camera (5MP) modules. 

**Note** : Currently, the D3-G board does not support simultaneous use of CSI channel 0 and CSI channel 1.

### 4.2.1 Ardu cam
ArduCam is a versatile camera module designed for embedded systems and IoT applications. It supports various image sensors and interfaces, including MIPI CSI, making it suitable for integration with development boards like the D3-G.
The 5MP ArduCam module supported by the D3-G offers decent image quality and is commonly used for basic computer vision tasks, streaming, and camera-based AI applications. Its compatibility with FFC cables makes it easy to connect to the D3-G’s CSI interface. 

Below are the specifications for the ArduCam module.

| Spec                     | Description                                 |
| ------------------------ | ------------------------------------------- |
| Sensor                   | OV5647 (5 Megapixel)                        |
| Resolution               | 2592 × 1944 (Full 5MP)                      |
| Supported Output Formats | RAW, YUV, JPEG (sensor dependent)           |
| Interface                | MIPI CSI-2                                  |
| Frame Rate               | Up to 30fps at 1080p, 60fps at 720p         |
| Lens Mount               | Fixed-focus lens (standard)                 |
| FOV (Field of View)      | Approx. 54° – 70° (varies by model)         |
| Connection Type          | FFC (Flat Flexible Cable)                   |
| Operating Voltage        | 3.3V (typical)                              |
| Form Factor              | Compact PCB, ~25mm x 24mm                   |
| Compatibility            | Raspberry Pi, D3-G (via MIPI CSI-2 port)    |
| Additional Features      | Low power consumption, plug-and-play module |


You can test the Arducam by following the steps below:
<p align="center"><img src="https://github.com/topst-development/Documentation/blob/main/Assets/TOPST%20D3-G/Software/arducam.png?raw=true" width="400"></p>
<p align="center"><strong>Figure 4. Ardu cam </strong></p>

1. Connect Ardu cam to D3-G MIPI CSI 0 below figure 5.
 
<p align="center"><img src="https://github.com/topst-development/Documentation/blob/main/Assets/TOPST%20D3-G/Software/Arducam%20to%20D3G.png?raw=true" width="500"></p>
<p align="center"><strong>Figure 5. Connecting the ArduCam to the D3-G </strong></p> 

2. 























<br/>

### 4.2.2 Raspberry Pi v1 Camera

The Raspberry Pi Camera Module v1 is a compact 5MP camera developed by the Raspberry Pi Foundation. It is based on the OmniVision OV5647 image sensor and connects to the host board via a MIPI CSI-2 interface using an FFC (Flat Flexible Cable).

Designed originally for the Raspberry Pi series, this module is also compatible with the D3-G board, making it a reliable choice for basic camera applications such as image capture, video recording, and computer vision projects.

Below are the specifications for the ArduCam module.

| Spec                | Description                              |
| ------------------- | ---------------------------------------- |
| Sensor              | OmniVision OV5647                        |
| Resolution          | 2592 × 1944 (5MP)                        |
| Output Formats      | RAW, YUV, JPEG                           |
| Interface           | MIPI CSI-2                               |
| Frame Rate          | 1080p30, 720p60, VGA90                   |
| Lens                | Fixed-focus                              |
| FOV (Field of View) | ~54°                                     |
| Cable Type          | FFC (15-pin)                             |
| Board Dimensions    | 25mm x 24mm                              |
| Compatibility       | Raspberry Pi, D3-G (via MIPI CSI-2 port) |


You can test the Arducam by following the steps below:

<p align="center"><img src="../../Assets/TOPST D3-G/Software/rasp v1 cam.jpg" width="400"></p>
<p align="center"><strong>Figure 6. Raspberry pi v1 cam </strong></p>


1. Connect Raspbery pi v1 cam to D3-G MIPI CSI 1 below figure 7.
 
<p align="center"><img src="../../Assets/TOPST D3-G/Software/rasp v1 cam to d3g.png" width="500"></p>
<p align="center"><strong>Figure 7. Connecting the Raspberry pi v1 cam to the D3-G </strong></p> 





# 5. Storage Connection
This chapter covers how to connect the D3-G board to various storage devices.
Supported storage options include USB drives, SD cards, and external storage via PCIe.
<br/>

## 5.1 USB Drive
The D3-G board supports USB storage devices through its USB 2.0 and USB 3.0 Type-A ports.
To connect a USB drive:

1. Plug the USB drive into one of the available USB Type-A ports on the D3-G.
<p align="center"><img src="../../Assets/TOPST D3-G/Software/usb storage connection with d3g.png" width="500"></p>
<p align="center"><strong>Figure 8. Connecting the usb storage to the D3-G </strong></p> 

1. Once connected, the device will typically be recognized as /dev/sda1, /dev/sdb1, etc., depending on the system state.

2. You can manually mount the USB drive using the following command:
   ```
   sudo mount /dev/sda1 /mnt
   ```

<br/>

## 5.2 SD card
The D3-G board includes a microSD card slot that supports standard SDHC/SDXC cards.
To use an SD card with the board:

1. Insert the microSD card into the SD card slot on the D3-G.

1. Plug the USB drive into one of the available USB Type-A ports on the D3-G.
<p align="center"><img src="../../Assets/TOPST D3-G/Software/sd card connect with d3g.png" width="500"></p>
<p align="center"><strong>Figure 9. Connecting the SD Card to the D3-G </strong></p> 

1. Once inserted, the system will typically recognize the SD card as /dev/mmcblk1p1 or a similar device node.
  ```
  ls /dev/mmcblk*

  ```
2. To mount the SD card manually, use the following command:
   ```
   sudo mount /dev/mmcblk1p1 /mnt 
   ```
3. After mounting, you can access the SD card contents under the /mnt directory.

<br/>

## 5.3 SATA HDD

## 5.4 NVME M.2 SSD

</br></br>


# 6. Ethernet Connection

## 6.1 Network Connection Via Router

## 6.2 Nework Sharing with the Host PC

## 6.3 WIFI Device Connection 


<br/><br/>

# 7. 40 Pin GPIO Header
The D3-G board features a 40-pin GPIO header, providing flexible I/O capabilities for various hardware projects.
This header is compatible with general-purpose input/output (GPIO) operations and can be used to connect sensors, LEDs, buttons, and other peripheral devices.

Each pin supports multiple functions such as digital I/O, PWM, I2C, SPI, and UART, depending on the configuration.

<p align="center"><img src="../../Assets/TOPST D3-G/Software/" width="500"></p>
<p align="center"><strong>Figure 10. 40 Pin GPIO Header Pinmap of D3-G </strong></p> 

**Note**: Please refer to the official pinout diagram for detailed pin functions and voltage levels before connecting external hardware.
<br/>

## 7.1 GPIO Digital In/Out

The D3-G board supports digital input and output (GPIO) through its 40-pin header, enabling users to interact with external devices such as buttons, LEDs, sensors. 
<br/>

### 7.1.1 LED

<br/>

### 7.1.2 Button

<br/>

### 7.1.3 Touch Sensor

<br/>

### 7.1.4 Vibration Detection Sensor

<br/>

### 7.1.5 Infrared Sensor

<br/>

### 7.1.6 Phtoregister

<br/>

### 7.1.7 Air Pollution Chect Sensor

<br/>

### 7.1.8 Ultrasonic Sensor

<br/>

## 7.2 I2C

### 7.2.1 9-Axis Gyro
### 7.2.2 1602A LCD Display
### 7.2.3 Photoregister(BH1750)

## 7.3 SPI
### 7.3.1 Dot Matrix

## 7.4 PWM
### 7.4.1 LED
### 7.4.2 Mini Servo Motor

# 8. JTAG Connection

# 9. CAN Connection
