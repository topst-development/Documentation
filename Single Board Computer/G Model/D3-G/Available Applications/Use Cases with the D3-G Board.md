# 1. Introduction 
---
This document provides examples of using the D3-G.   
This document includes the following information:
- Input Device
  - Keyboard 
  - Mouse
- Video Output
- Camera Connection
  - MIPI CSI
  - USB Webcam
- Storage Connection
  - SD Card
  - SATA HDD
  - NVMe M.2 SSD
  - USB Storage
- Ethernet Connection
- 40-pin GPIO Header
  - Available Sensor and Device

<br/><br/><br/><br/>


# 2. Input Device
---
The D3-G supports two USB ports for connecting input devices.
It includes one USB 2.0 Type-A port and one USB 3.0 Type-A port, allowing you to connect a mouse or keyboard to control the D3-G directly. 

**Note**: The USB Type-C port on the D3-G is reserved for firmware downloads and cannot be used to connect input devices.

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20D3-G/Software/input%20device.png" width="500"></p>
<p align="center"><strong>Figure 2.1 Connect Input Device to D3-G board </strong></p><br/><br/><br/><br/>


# 3. Video Output
---
The D3-G supports FHD monitors through its DisplayPort (DP) output only.
It also supports multi-display output using a daisy chain setup, allowing  connection of up to two FHD monitors and one HD monitor simultaneously.

**Note**: To use HDMI, a separate active converter adapter is required.
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20D3-G/Software/monitor.png" width="500"></p>
<p align="center"><strong>Figure 3.1 Connect Monitor to D3-G board </strong></p>

<br/><br/><br/><br/>

# 4. Camera Connection
---
The D3-G supports camera functionality, offering flexibility for various applications.
You can connect either a MIPI CSI camera or a USB webcam depending on your project requirements.

<br/><br/><br/>

## 4.1 USB Webcam
---
The D3-G supports USB webcams, with resolutions up to Full HD (FHD).
You can test the webcam by following these steps:


#### Step 1. Connect the USB camera to a USB port on the board.
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20D3-G/Software/webcam.png" width="400"></p>
<p align="center"><strong>Figure 4.1 Connect Webcam to D3-G board</strong></p><br/>

#### Step 2. Connect the input devices (mouse and keyboard) and monitor to D3-G.
   
#### Step 3. Boot the D3-G.

#### Step 4. Check the available /dev/video devices.
```
$ ls /dev/video*
```

#### Step 5. Verify the video output using OpenCV (or vutils).
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
CSI stands for Camera Serial Interface, a standard interface defined by the MIPI Alliance for connecting camera modules to host processors.
It enables high-speed, low-power transmission of image data from the camera to the processor.

The D3-G features two MIPI CSI channels (ch0 and ch1), allowing you to attach camera modules that support Flat Flexible Cable (FFC) connections.
Currently, the D3-G supports only the ArduCam (5 MP) and Raspberry Pi v1 Camera (5 MP) modules. 

**Note**: Currently, the D3-G does not support simultaneous use of CSI channel 0 and CSI channel 1.

<br/><br/>

### 4.2.1 ArduCam
ArduCam is a versatile camera module designed for embedded systems and IoT applications. It supports various image sensors and interfaces, including MIPI CSI, making it suitable for integration with development boards like the D3-G.
The 5 MP ArduCam module supported by the D3-G offers decent image quality and is commonly used for basic computer vision tasks, streaming, and camera-based AI applications. Its compatibility with FFC cables makes it easy to connect to the D3-G board’s CSI interface. 

The specifications for the ArduCam module are as follows.

| Specification                     | Description                                 |
| ------------------------ | ------------------------------------------- |
| Sensor                   | OV5647 (5 Megapixel)                        |
| Resolution               | 2592 × 1944 (Full 5 MP)                      |
| Supported Output Formats | RAW, YUV, JPEG (sensor dependent)           |
| Interface                | MIPI CSI-2                                  |
| Frame Rate               | Up to 30fps at 1080p, 60fps at 720p         |
| Lens Mount               | Fixed-focus lens (standard)                 |
| Field of View (FOV)      | Approximately 54° – 70° (varies by model)         |
| Connection Type          | Flat Flexible Cable (FFC)                   |
| Operating Voltage        | 3.3V (typical)                              |
| Form Factor              | Compact PCB, approximately 25 mm x 24 mm                   |
| Compatibility            | Raspberry Pi and D3-G (through MIPI CSI-2 port)    |
| Additional Features      | Low power consumption, plug-and-play module |


You can test the ArduCam by following these steps:
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20D3-G/Software/arducam.png" width="400"></p>
<p align="center"><strong>Figure 4.2 ArduCam </strong></p><br/>

#### Step 1. Connect ArduCam to D3-G board MIPI CSI 0 as shown in Figure 4.3.
 
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20D3-G/Software/rasp%20v1%20cam%20to%20d3g.png" width="500"></p>
<p align="center"><strong>Figure 4.3 Connect ArduCam to D3-G board</strong></p> <br/>

#### Step 2. After the ArduCam is connected, you can verify the video stream using the following GStreamer command on the D3-G board:
```
$ gst-launch-1.0 v4l2src device=/dev/video0 io-mode=2 ! video/x-raw,format=NV12,width=1920,height=1280,framerate=30/1 ! videoconvert ! waylandsink fullscreen=true
```

This command captures video from the CSI-connected ArduCam, converts it for display, and renders it in fullscreen mode using the Wayland display server.  
Make sure that the camera module is securely connected before running the command. If the video does not appear, check the cable connection and verify that /dev/video0 is properly recognized by the system.

<br/><br/>

### 4.2.2 Raspberry Pi v1 Camera
The Raspberry Pi v1 Camera Module is a compact 5 MP camera developed by the Raspberry Pi Foundation. It is based on the OmniVision OV5647 image sensor and connects to the host board through a MIPI CSI-2 interface using a Flat Flexible Cable (FFC).

Designed originally for the Raspberry Pi series, this module is also compatible with the D3-G, making it a reliable choice for basic camera applications such as image capture, video recording, and computer vision projects.

The specifications for the Raspberry Pi v1 camera module are as follows.

| Specification                | Description                              |
| ------------------- | ---------------------------------------- |
| Sensor              | OmniVision OV5647                        |
| Resolution          | 2592 × 1944 (5 MP)                        |
| Output Formats      | RAW, YUV, JPEG                           |
| Interface           | MIPI CSI-2                               |
| Frame Rate          | 1080p30, 720p60, VGA90                   |
| Lens                | Fixed-focus                              |
| Field of View (FOV) | Up to 54°                                     |
| Cable Type          | FFC (15-pin)                             |
| Board Dimensions    | 25 mm x 24 mm                              |
| Compatibility       | Raspberry Pi and D3-G (through MIPI CSI-2 port) |

You can test the Raspberry Pi v1 camera by following these steps:

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20D3-G/Software/rasp%20v1%20cam.jpg" width="400"></p>
<p align="center"><strong>Figure 4.4. Raspberry Pi v1 Camera </strong></p><br/>

#### Step 1. Connect Raspberry Pi v1 camera to D3-G board MIPI CSI 1 as shown in Figure 4.5.
 
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20D3-G/Software/rasp%20v1%20cam%20to%20d3g.png" width="500"></p>
<p align="center"><strong>Figure 4.5 Connect Raspberry Pi v1 Camera to D3-G board</strong></p> <br/>

#### Step 2. After the Raspberry Pi camera is connected, you can verify the video stream using the following GStreamer command on the D3-G:
```
$ gst-launch-1.0 v4l2src device=/dev/video0 io-mode=2 ! video/x-raw,format=NV12,width=1920,height=1280,framerate=30/1 ! videoconvert ! waylandsink fullscreen=true
```

This command captures video from the CSI-connected Raspberry Pi camera, converts it for display, and renders it in fullscreen mode using the Wayland display server.  
Make sure that the camera module is securely connected before running the command. If the video does not appear, check the cable connection and verify that /dev/video0 is properly recognized by the system.

<br/><br/><br/><br/>

# 5. Storage Connection
---
This chapter covers how to connect the D3-G to various storage devices. Supported storage options include USB drives, SD cards, and external storage through PCIe.

<br/><br/><br/>

## 5.1 USB Drive
---
The D3-G supports USB storage devices through its USB 2.0 and USB 3.0 Type-A ports.
To connect a USB drive:

### Step 1. Plug the USB drive into one of the available USB Type-A ports on the D3-G.
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20D3-G/Software/usb%20storage%20connection%20with%20d3g.png" width="500"></p>
<p align="center"><strong>Figure 5.1 Connect USB Storage to D3-G board</strong></p> <br/>

### Step 2. After it is connected, the device is typically recognized as /dev/sda1, /dev/sdb1, and so on, depending on the system state.

<br/>

### Step 3. You can manually mount the USB drive using the following command:
   ```
   $ sudo mount /dev/sda1 /mnt
   ```

<br/><br/><br/>

## 5.2 SD Card
---
The D3-G includes a microSD card slot that supports standard SDHC/SDXC cards.
To use an SD card with the D3-G:

<br/>

### Step 1. Insert the microSD card into the SD card slot on the D3-G board.
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20D3-G/Software/sd%20card%20connect%20with%20d3g.png" width="500"></p>
<p align="center"><strong>Figure 5.2 Connect SD Card to D3-G board</strong></p> <br/>

### Step 2. After it is inserted, the system typically recognizes the SD card as /dev/mmcblk1p1 or a similar device node.
  ```
  $ ls /dev/mmcblk*
  ```
<br/>

### Step 3. To mount the SD card manually, use the following command:
```
$ sudo mount /dev/mmcblk1p1 /mnt 
```
### Step 4. After mounting, you can access the SD card contents under the /mnt directory.

<br/><br/><br/>

## 5.3 SATA HDD
---

The D3-G supports the use of SATA storage devices, such as HDDs or SSDs, through its PCIe slot using a compatible SATA controller.

<br/>

#### Step 1. Connect the PCIe to SATA Module

To use a SATA HDD with the D3-G through PCIe, you must first connect a PCIe-to-SATA adapter module to the D3-G's PCIe slot.

Then, connect the HDD to the SATA module and ensure that the HDD is powered by an external 12V power supply.

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20D3-G/Software/sata.png" width="500"></p>
<p align="center"><strong>Figure 5.3 Connect D3-G board PCIe to SATA Module </strong></p><br/>

#### Step 2. Boot the D3-G 
After booting the D3-G, observe the boot log to verify that the PCIe device is recognized by the system.
Look for messages such as **telechips-pcie: Link up**, which indicate that the PCIe link has been successfully established.

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

#### Step 3. Check SATA HDD Recognition
```
root@TOPST:~# lspci
00:00.0 PCI bridge: Synopsys, Inc. Device 8040 (rev 01)
01:00.0 SATA controller: ASMedia Technology Inc. Device 1064 (rev 02)
```
If the **lspci** command is not available, install pciutils by using the following command.

```
$ sudo apt-get install pciutils
```

<br/>

#### Step 4. Mount the SATA HDD
```
$ fdisk /dev/sda
Welcome to fdisk (util-linux 2.37.4).
Changes will remain in memory only, until you decide to write them.
Be careful before using the write command.

Command (m for help): 
```

Type the following keys in order inside the fdisk prompt:

- o — Create a new empty DOS partition table (optional, clears existing table)

- n — Add a new partition

- p — Choose a primary partition

- 1 — Set partition number to 1

- Press Enter — Accept default first sector

- Press Enter — Accept default last sector (uses full disk)

- w — Write the partition table and exit

```
$ mkfs.ext4 /dev/sda1

$ mkdir -p /mnt/sata

$ mount /dev/sda1 /mnt/sata
```

<br/>

#### Step 5. Execution Result
This output confirms that the SATA SSD partition (/dev/sdb1) has been successfully formatted with the ext4 file system and mounted at /mnt/sata.
The **df -h** command shows that the device is now recognized and available for use by the system.

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
The D3-G supports direct connections of NVMe M.2 SSDs through its PCIe slot.
<br/>

#### Step 1. Connect the SSD
- NVMe SSD (M.2 PCIe): Insert the NVMe M.2 SSD into the D3-G’s PCIe slot. 

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20D3-G/Software/M.2%20SSD%20connection.png" width="400"></p>
<p align="center"><strong>Figure 5.4 Connect NVMe M.2 SSD to D3-G board</strong></p><br/>

#### Step 2. Boot the D3-G
After executing the **reboot** command, observe the boot log to verify that the PCIe device is recognized by the system.
Look for messages such as **telechips-pcie: Link up**, which indicate that the PCIe link has been successfully established.

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

#### Step 3. Check SSD Recognition
```
root@TOPST:~# lspci
00:00.0 PCI bridge: Synopsys, Inc. Device 8040 (rev 01)
01:00.0 Non-Volatile memory controller: Solid State Storage Technology Corporation Device 1007 (rev 03)
```
If the **lspci** command is not available, install pciutils by using the following command.

```
$ sudo apt-get install pciutils
```

<br/>

#### Step 4. Mount the SSD
```
$ fdisk /dev/nvme0n1
Welcome to fdisk (util-linux 2.37.4).
Changes will remain in memory only, until you decide to write them.
Be careful before using the write command.

Command (m for help): 
```

Type the following keys in order inside the fdisk prompt:

- o — Create a new empty DOS partition table (optional, clears existing table)

- n — Add a new partition

- p — Choose a primary partition

- 1 — Set partition number to 1

- Press Enter — Accept default first sector

- Press Enter — Accept default last sector (uses full disk)

- w — Write the partition table and exit

```
$ mkfs.ext4 /dev/nvme0n1p1

$ mkdir -p /mnt/nvme

$ mount /dev/nvme0n1p1 /mnt/nvme
```

<br/>

#### Step 5. Execution Result
This output confirms that the NVMe SSD device (/dev/nvme0n1p1) has been successfully detected and mounted by the system at /mnt/nvme.
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


# 6. Ethernet Connection
---
The D3-G supports Ethernet connectivity through its onboard J2C Ethernet port. This allows the D3-G to communicate with local networks or the internet using standard TCP/IP protocols. Ethernet is commonly used for deploying applications that require remote access, data streaming, or software updates.

<br/><br/><br/>

## 6.1 Network Connection Through Router
---
This method connects the D3-G to a local network using a standard router. The D3-G can obtain an IP address automatically through DHCP or be configured with a static IP address.

<br/><br/>

### 6.1.1 Create Network Configuration File

1. Dynamic IP through DHCP
If your network provides a DHCP server (for example, a router or ICS-enabled Windows PC), no file editing is necessary. The system automatically obtains an IP address as soon as the Ethernet cable is connected.

You can simply plug in the cable and start using the network right away. Proceed to Chapter 6.1.3 Verify Network Connectivity.

2. Static IP Configuration
If you prefer to assign a static IP address (for example, when using direct PC connection or no DHCP server is available), edit the same file with the following content:
```
$ vi /etc/systemd/network/20-wired.network

[Match]
Name=eth0

[Network]
Address=192.168.137.2/24
Gateway=192.168.137.1
DNS=8.8.8.8
```

This sets the IP address to 192.168.137.2, uses 192.168.137.1 as the gateway (common in Windows ICS), and configures Google DNS.

<br/><br/>

### 6.1.2 Restart Network Service
Apply the new network configuration by restarting the systemd-networkd service:

```
sudo systemctl restart systemd-networkd
```

<br/><br/>

### 6.1.3 Verify Network Connectivity
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20D3-G/Software/router%20connection.png"width="500"></p>
<p align="center"><strong>Figure 6.1 Network Connection Through Router</strong></p>

Test the internet connection by pinging Google's public DNS server:

```
$ ping 8.8.8.8
PING 8.8.8.8 (8.8.8.8): 56 data bytes
64 bytes from 8.8.8.8: seq=0 ttl=113 time=30.208 ms
64 bytes from 8.8.8.8: seq=1 ttl=113 time=38.143 ms
64 bytes from 8.8.8.8: seq=2 ttl=113 time=30.969 ms
64 bytes from 8.8.8.8: seq=3 ttl=113 time=33.586 ms
 
```

<br/><br/><br/>

## 6.2 Network Sharing with Host PC
---
You can share your PC's internet connection with the D3-G without using a router by utilizing the Internet Connection Sharing (ICS) feature available in Windows operating systems.

<br/><br/>

### 6.2.1 Host PC Network Configuration
- Control Panel → Network and Internet → Network Connectivity → Set Ethernet
 
1. Locate the network adapter connected to the internet (for example, Wi-Fi), right-click on it, and select **Properties**.

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20AI-G/Available%20Applications/ethernet1.png" width="600"></p>
<p align="center"><strong>Figure 6.2 Select Properties</strong></p><br/>
 
2. Select the sharing tab.

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20AI-G/Available%20Applications/ethernet2.png" width="400"></p>
<p align="center"><strong>Figure 6.3 Select Sharing Tab</strong></p><br/>

3. Check the box labeled "Allow other network users to connect through this computer’s Internet connection".
 
4. In the Home networking connection dropdown menu, select the Ethernet adapter that the D3-G will connect to (for example, "Ethernet").

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20AI-G/Available%20Applications/ethernet3.png" width="400"></p>
<p align="center"><strong>Figure 6.4 Select Ethernet Adapter</strong></p><br/>
 
5. Click **OK** to save the settings.

<br/><br/>

### 6.2.2 Create Network Configuration File 
1. Dynamic IP Through DHCP
If your network provides a DHCP server (for example, a router or ICS-enabled Windows PC), no file editing is necessary. The system automatically obtains an IP address as soon as the Ethernet cable is connected.

You can simply plug in the cable and start using the network right away. Proceed to Chapter 6.2.4 Verify Network Connection.

2. Static IP Configuration
If you prefer to assign a static IP address (for example, when using direct PC connection or no DHCP server is available), edit the same file with the following content:
```
$ vi /etc/systemd/network/20-wired.network

[Match]
Name=eth0

[Network]
Address=192.168.137.2/24
Gateway=192.168.137.1
DNS=8.8.8.8
```
This sets the IP address to 192.168.137.2, uses 192.168.137.1 as the gateway (common in Windows ICS), and configures Google DNS.

<br/><br/>

### 6.2.3 Restart Network Service
Apply the new network configuration by restarting the systemd-networkd service:

```
sudo systemctl restart systemd-networkd
```

<br/><br/>

### 6.2.4 Verify Network Connectivity
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20D3-G/Software/host%20pc%20ethernet%20connection.png"width="500"></p>
<p align="center"><strong>Figure 6.5 Network Sharing with Host PC</strong></p>
<br/>

Test the internet connection by pinging Google's public DNS server:

```
$ ping 8.8.8.8
PING 8.8.8.8 (8.8.8.8): 56 data bytes
64 bytes from 8.8.8.8: seq=0 ttl=113 time=30.208 ms
64 bytes from 8.8.8.8: seq=1 ttl=113 time=38.143 ms
64 bytes from 8.8.8.8: seq=2 ttl=113 time=30.969 ms
64 bytes from 8.8.8.8: seq=3 ttl=113 time=33.586 ms
```

<br/><br/><br/><br/>

# 7. 40-pin GPIO Header
---
The D3-G features a 40-pin GPIO header, providing flexible I/O capabilities for various hardware projects.
This header is compatible with general-purpose input/output (GPIO) operations and can be used to connect sensors, LEDs, buttons, and other peripheral devices.

Each pin supports multiple functions such as digital I/O, PWM, I2C, SPI, and UART, depending on the configuration.

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/d3g/Assets/TOPST%20D3-G/Software/d3-g%20gpio%2040pinmap.png" width="800"></p>
<p align="center"><strong>Figure 7.1 40-pin GPIO Header Pinmap of D3-G </strong></p> <br/>

**Note**: Refer to the official pinout diagram for detailed pin functions and voltage levels before connecting external hardware.

<br/><br/><br/>

## 7.1 GPIO Digital In/Out
---
The D3-G supports digital input and output (GPIO) through its 40-pin header, enabling you to interact with external devices such as buttons, LEDs, and sensors. 

### 7.1.1 LED
---
One of the simplest and most common GPIO output examples is controlling an LED.  
This section demonstrates how to connect and use a LED sensor using the D3-G.

#### Step 1. Hardware Requirements
- D3-G board (x1)
- Breadboard (x1)
- LED (x1)
- Male to female jumper wire (x2)
- DC 5V Power Adapter (x1)
- USB to TTL Serial Cable (x1)

#### Step 2. Example Circuit
- LED
    - (+) pin connected to pin 12 on the D3-G board.
    - (-) pin connected to pin 14 which acts as GND on the D3-G board.  
    
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20D3-G/Software/led.png"></p>

<p align="center"><strong>Figure 7.2 D3-G GPIO LED Circuit Schematic </strong></p> <br/>

##### Step 2.1 Pin Mapping
The following table shows pin mapping.

<div align="center">
  <p><strong>Table 7.1 Pin Mapping of D3-G LED</strong></p>
  <table>
      <tr>
          <th colspan="3">Pin Name</th>
          <th>D3-G</th>
          <th>GPIO</th>
      </tr>
      <tr>
          <td colspan="3">LED (+) pin</td>
          <td>12</td>
          <td>89</td>
      </tr>
      <tr>
          <td colspan="3">LED (-) pin</td>
          <td>14</td>
          <td>GND</td>
      </tr>
  </table>
</div>

#### Step 3. How to execute
To operate the LED connected to GPIO89 on the D3-G board, run the following code:

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

#### Step 4. Execution Result
Run the code with the following command.

```
$ python3 led_test.py
```

This script configures GPIO89 as a digital output and toggles its state every 1 second.
When executed, the LED connected to GPIO89 blinks 10 times, turning on for 1 second and then off for 1 second repeatedly. After 10 cycles, the script exits and automatically unexports the GPIO.

To stop the script early, press **[Ctrl+C]**.
In either case, the pin will be properly released and cleaned up.

**Note**: This setup assumes a direct LED connection. For safe and long-term operation, it is strongly recommended to use a current-limiting resistor (for example, 220Ω) in series with the LED to prevent excessive current draw and protect the GPIO pin from potential damage.

<br/><br/><br/><br/>

### 7.1.2 Button
---
A push button is a basic input device commonly used to demonstrate digital input handling through GPIO.
This section demonstrates how to connect and use a basic button module with the D3-G.

#### Step 1. Hardware Requirements
- D3-G board (x1)
- Breadboard (x1)
- Button (x1)
- Male to female jumper wire (x2)
- DC 5V Power Adapter (x1)
- USB to TTL Serial Cable (x1)

#### Step 2. Example Circuit
- Button switch
    - One leg of the button switch is connected to pin 10 on the D3-G board.
    - The opposite leg above the button is connected to the 3.3V pin.

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20D3-G/Software/button_circuit.png"></p> 
<p align="center"><strong>Figure 7.3 D3-G GPIO Button Circuit Schematic</strong></p>

##### Step 2.1 Pin Mapping
The following table shows pin mapping.

<div align="center">
  <p><strong>Table 7.2 Pin Mapping of D3-G Button</strong></p>
  <table>
      <tr>
          <th colspan="3">Pin Name</th>
          <th>D3-G</th>
          <th>GPIO</th>
      </tr>
      <tr>
          <td colspan="3">One leg pin of button</td>
          <td>10</td>
          <td>88</td>
      </tr>
  </table>
</div>

#### Step 3. How to execute
To monitor the button input connected to GPIO88 on the D3-G board, run the following code:

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

#### Step 4. Execution Result
Run the code with the following command.
```
$ python3 test_button.py
```
This script configures GPIO88 as a digital input and continuously monitors its value in real time.
When executed, pressing the button connected to GPIO88 prints a message indicating that the button has been pressed.

To stop the script, press **[Ctrl+C]**.
When the script is terminated, GPIO88 will be automatically unexported and cleaned up.

**Note**: GPIO88 is used here as an example. You may use any available GPIO pin on the D3-G based on the 40-pin header pinout.
Refer to the official pinout diagram and select a GPIO number that matches your hardware configuration.

<br/><br/><br/><br/>

### 7.1.3 Touch Sensor
---
A touch sensor can be used to detect human touch as a digital input signal through GPIO.
This section demonstrates how to connect and read input from a basic touch sensor module using the D3-G.

#### Step 1. Hardware Requirements
- D3-G board (x1)
- Touch Sensor (x1)
- Female to female jumper wire (x3)
- DC 5V Power Adapter (x1)
- USB to TTL Serial Cable (x1)

#### Step 2. Example Circuit
- Touch sensor
    - SIG pin of the touch sensor is connected to pin 88 on the D3-G board.
    - VCC pin of the touch sensor is connected to the 3.3V on the D3-G board.
    - GND pin of the touch sensor is connected to GND on the D3-G board.


<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20D3-G/Software/touch%20circuit.png"></p>
<p align="center"><strong>Figure 7.4 D3-G GPIO Touch Sensor Circuit Schematic</strong></p>

##### Step 2.1 Pin Mapping
The following table shows pin mapping.

<div align="center">
  <p><strong>Table 7.3 Pin Mapping of D3-G Touch Sensor</strong></p>
  <table>
      <tr>
          <th colspan="3">Pin Name</th>
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

#### Step 3. How to execute
To monitor the touch sensor connected to GPIO88 on the D3-G board, simply run the following code:
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

#### Step 4. Execution Result
Run the code with the following command.

```
$ python3 touch_test.py
```

This script configures GPIO88 as a digital input and continuously monitors its value in real time.

When executed, touching the sensor will cause the terminal to print a message such as:
```
touch detected.
```
When the sensor is not touched, the output will be:
```
touch released.
```
To stop the script, press **[Ctrl+C]**.
When the script is terminated, GPIO88 will be automatically unexported and cleaned up.

**Note**: GPIO88 is used here as an example. You may use any available GPIO pin on the D3-G based on the 40-pin header pinout.
Refer to the official pinout diagram and select a GPIO number that matches your hardware configuration.

<br/><br/><br/><br/>

### 7.1.4 Vibration Detection Sensor
---
A vibration sensor can be used to detect physical shocks or vibrations and output a digital input signal through GPIO.
This section demonstrates how to connect and detect input from a basic vibration sensor module using the D3-G.

#### Step 1. Hardware Requirements
- D3-G board (x1)
- Vibration Detection Sensor (x1)
- Female to female jumper wire (x4)
- DC 5V Power Adapter (x1)
- USB to TTL Serial Cable (x1)

#### Step 2. Example Circuit
- Vibration Detection Sensor
    - VCC pin of the Vibration Detection Sensor is connected to the 3.3V pin on the D3-G board.
    - GND pin of the Vibration Detection Sensor is connected to the GND on the D3-G board.
    - DO pin of the Vibration Detection Sensor is connected to the 88 pin on the D3-G board.

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20D3-G/Software/vibr%20circuit.png"></p>
<p align="center"><strong>Figure 7.5 D3-G GPIO Vibration Detection Sensor Circuit Schematic</strong></p>

##### Step 2.1 Pin Mapping
The following table shows pin mapping.

<div align="center">
  <p><strong>Table 7.4 Pin Mapping of D3-G Vibration Detection Sensor</strong></p>
  <table>
      <tr>
          <th colspan="3">Pin Name</th>
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

#### Step 3. How to execute
To monitor the vibration sensor connected to GPIO88 on the D3-G board, run the following code:
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

#### Step 4. Execution Result
Run the code with the following command.

```
$ python3 vibration_test.py
```

This script configures GPIO88 as a digital input and continuously monitors its value in real time.
When executed, vibrations or shocks detected by the sensor cause the terminal to print a message such as:
```
vibration detected.
```
When there is no vibration, the output will be:
```
no vibration detected.
```
To stop the script, press **[Ctrl+C]**.
Upon termination, GPIO88 is automatically unexported and cleaned up.

**Note**: GPIO88 is used here as an example. You may use any other available GPIO pin depending on your sensor wiring and header layout. Refer to the D3-G pinout before choosing a GPIO number.

<br/><br/><br/><br/>

### 7.1.5 Infrared Sensor (SZH-SSBH-002)
---
An infrared sensor can be used to detect nearby obstacles by sensing reflected infrared light and outputting a digital signal through GPIO.
This section demonstrates how to connect and read input from the SZH-SSBH-002 infrared sensor using the D3-G.

#### Step 1. Hardware Requirements
- D3-G board (x1)
- Breadboard (x1)
- Infrared Sensor (x1)
- Male to female jumper wire (x5)
- DC 5V Power Adapter (x1)
- USB to TTL Serial Cable (x1)

#### Step 2. Example Circuit
- Infrared Sensor
    - VCC pin of the Infrared Sensor is connected to the 3.3V pin on the D3-G board.
    - GND pin of the Infrared Sensor is connected to the GND on the D3-G board.
    - OUT pin of the Infrared Sensor is connected to the 89 pin on the D3-G board.


<p align="center">
  <img src="https://raw.githubusercontent.com/topst-development/Documentation/d3g/Assets/TOPST%20D3-G/Software/szh-ssbh-002_circuit.png">
</p> 
<p align="center"><strong>Figure 7.6 IR Sensor Experiment Circuit</strong></p>

##### Step 2.1 Pin Mapping
The following table shows pin mapping.

<div align="center">
  <p><strong>Table 7.5 Pin Mapping of D3-G IR Sensor</strong></p>
  <table>
      <tr>
          <th colspan="3">Pin Name</th>
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

#### Step 3. How to execute
To monitor the IR sensor connected to GPIO89 on the D3-G board, run the following code:

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

#### Step 4. Execution Result
Run the code with the following command.
```
$ python3 ir_test.py
```
This script configures GPIO89 as a digital input and continuously monitors its state to detect obstacles.
When an object is detected in front of the IR sensor, the terminal displays:
```
obstacle detected.
```
When no object is detected, it displays:
```
no obstacle detected.
```
To stop the script, press **[Ctrl+C]**.
When the script is terminated, GPIO89 is automatically unexported and cleaned up.

**Note**: GPIO89 is used as an example in this script.
You may use any available GPIO pin based on the 40-pin header of the D3-G. Refer to the official pinout diagram for accurate pin selection.

<br/><br/><br/><br/>

### 7.1.6 Photoresistor (SZH-SSBH-011)
---
A photoresistor can be used to detect ambient light levels and output a digital signal when the light intensity crosses a certain threshold through GPIO.
This section demonstrates how to connect and read input from the SZH-SSBH-011 photoresistor sensor using the D3-G.

#### Step 1. Hardware Requirements
- D3-G board (x1)
- Photoresistor module (SZH-SSBH-011) (x1)
- LED (x1)
- 220Ω resistor (x1)
- Breadboard (x1)
- Male to Female Jumper Wires (x7)
- DC 5V Power Adapter (x1)
- USB to TTL Serial Cable (x1)

#### Step 2. Example Circuit
- Photoresistor (SZH-SSBH-011)
    - VCC pin of the Photoresistor is connected to the 3.3V pin on the D3-G board.
    - GND pin of the Photoresistor is connected to the GND on the D3-G board.
    - DO pin of the Photoresistor is connected to pin 89 on the D3-G board.
- LED
    - (+) pin of the LED is connected to the GND on the D3-G board.
    - (-) pin of the LED is connected to pin 83 on the D3-G board.

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20D3-G/Software/circuit.png"></p>
<p align="center"><strong>Figure 7.7 Photoresistor Experiment Circuit</strong></p>

##### Step 2.1 Pin Mapping
The following table shows pin mapping.

<div align="center">
  <p><strong>Table 7.6 Pin Mapping of D3-G Photoresistor</strong></p>
  <table>
      <tr>
          <th colspan="3">Pin Name</th>
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
  <p><strong>Table 7.7 Pin Mapping of D3-G LED</strong></p>
  <table>
      <tr>
          <th colspan="3">Pin Name</th>
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

### Step 3. How to execute
Run the following Python script to monitor brightness with the CDS sensor and control the LED accordingly:

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

### Step 4. Execution Result
Run the code with the following command.
```
$ python3 CDS_test.py
```
This script configures GPIO89 as an input for the photoresistor sensor and GPIO83 as an output for the LED.
When ambient light is detected, the terminal prints:
```
sensor value: 0
brightness detected. Turning on the LED.
```
and the LED turns ON.
When no light is detected, it prints:
```
sensor value: 1
no brightness detected. Turning off the LED.
```
and the LED turns OFF.
To stop the script, press **[Ctrl+C]**.
When the script is terminated, both GPIO pins are automatically unexported and cleaned up.

**Note**: GPIO83 and GPIO89 are used in this example. You may use any available GPIO pin based on the 40-pin header layout of the D3-G. Refer to the official pinout diagram for accurate pin selection.

<br/><br/><br/><br/>

### 7.1.7 Air Pollution Detection Sensor
---
An air pollution detection sensor can be used to monitor the presence of harmful gases or particulate matter in the environment and output a digital signal through GPIO.
This section demonstrates how to connect and read input from an air pollution detection sensor using the D3-G.

#### Step 1. Hardware Requirements
- D3-G board (x1)
- Air Pollution (Gas) Detection Sensor Module (x1)
- Breadboard (x1)
- Male to Female Jumper Wires (x3)
- DC 5V Power Adapter (x1)
- USB to TTL Serial Cable (x1)

#### Step 2. Example Circuit
- Air Pollution Detection Sensor
    - VCC pin of the Air Pollution Detection Sensor is connected to the 3.3V pin on the D3-G board.
    - GND pin of the Air Pollution Detection Sensor is connected to the GND on the D3-G board.
    - DO pin of the Air Pollution Detection Sensor is connected to pin 88 on the D3-G board.

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20D3-G/Software/gas%20circuit.png"></p>
<p align="center"><strong>Figure 7.8 Air Pollution Detection Sensor Experiment Circuit</strong></p>

##### Step 2.1 Pin Mapping
The following table shows pin mapping.

<div align="center">
  <p><strong>Table 7.8 Pin Mapping of D3-G Air Pollution Detection Sensor</strong></p>
  <table>
      <tr>
          <th colspan="3">Pin Name</th>
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

#### Step 3. How to Execute
Run the following Python script to monitor gas detection using the GPIO88 pin:

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

#### Step 4. Execution Result
Run the code with the following command.
```
$ python3 gas_sensor_test.py
```
This script configures GPIO88 as a digital input and continuously monitors gas detection status.
When the gas concentration reaches the sensor’s threshold, the terminal displays:
```
gas detected.
```
When no gas is detected, the terminal shows:
```
no gas detected.
```
To stop the script, press **[Ctrl+C]**.
When the script is terminated, GPIO88 is automatically unexported and cleaned up.

**Note**: GPIO88 is used here as an example. You may use any available GPIO pin based on the 40-pin header layout of the D3-G. Refer to the official pinout diagram for accurate pin selection.

<br/><br/><br/><br/>

### 7.1.8 Ultrasonic Sensor
---
An ultrasonic sensor can be used to measure the distance to nearby objects by emitting ultrasonic waves and receiving the reflected signal, then outputting a digital (or pulse-based) signal through GPIO.
This section demonstrates how to connect and read input from an ultrasonic sensor using the D3-G.

#### Step 1. Hardware Requirements
- D3-G board (x1)
- Ultrasonic Sensor (x1)
- Female to Female Jumper Wires (x4)
- DC 5V Power Adapter (x1)
- USB to TTL Serial Cable (x1)

#### Step 2. Example Circuit
- Ultrasonic Sensor
    - VCC pin of the Ultrasonic Sensor is connected to the 5V pin on the D3-G board.
    - GND pin of the Ultrasonic Sensor is connected to the GND on the D3-G board.
    - TRIG pin of the Ultrasonic Sensor is connected to pin 82 on the D3-G board.
    - ECHO pin of the Ultrasonic Sensor is connected to pin 88 on the D3-G board.

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20D3-G/Software/ultra%20circuit.png"></p>
<p align="center"><strong>Figure 7.9 Ultrasonic Sensor Experiment Circuit</strong></p>

##### Step 2.1 Pin Mapping
The following table shows pin mapping.

<div align="center">
  <p><strong>Table 7.9 Pin Mapping of D3-G Ultrasonic Sensor</strong></p>
  <table>
      <tr>
          <th colspan="3">Pin Name</th>
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

#### Step 3. How to Execute
Run the following Python script to measure distance using the ultrasonic sensor:
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

#### Step 4. Execution Result
Run the code with the following command.
```
$ python3 ultrasonic_sensor_test.py
```
This script configures GPIO82 as a digital output to trigger the ultrasonic pulse, and GPIO88 as a digital input to receive the echo.
When the script runs, the distance to the nearest object in front of the sensor is printed every second, for example:
```
Distance: 23.45 cm
Distance: 24.12 cm
...
```
To stop the script, press **[Ctrl+C]**.
When the script is terminated, GPIO82 and GPIO88 are automatically unexported and cleaned up.

**Note**: GPIO82 and GPIO88 are used as examples. You may use any available GPIO pin based on the 40-pin header layout of the D3-G. Refer to the official pinout diagram for accurate pin selection. Also, ensure your ECHO pin's voltage level is safe for the D3-G (some modules output 5V and may need a voltage divider or level shifter).

<br/><br/><br/><br/>

## 7.2 I2C
---
The D3-G provides I2C communication through the 40-pin GPIO header, allowing it to interface with various peripherals such as sensors, displays, and expansion modules.
Inter-integrated Circuit (I2C) is a two-wire communication protocol consisting of a data line (SDA) and a clock line (SCL), enabling multiple devices to communicate over a shared bus.

I2C communication follows a master-slave architecture, where one master device controls the communication and up to 127 slave devices can be connected on the same bus.
The SDA line is used for both transmitting and receiving data, while the SCL line synchronizes the timing of data transfer. This synchronous communication model allows devices to exchange information in a coordinated, clock-driven manner.

<br/><br/><br/><br/>

### 7.2.1 1602A LCD Display
---
The 1602A LCD is a character display module commonly used in embedded systems.
On the D3-G, the LCD's SDA and SCL lines can be connected to GPIO pins configured for I2C. Once connected, the LCD can be controlled using the Linux I2C tools or custom software.

#### Step 1. Hardware Requirements
- D3-G board (x1)
- 1602A I2C LCD Module (x1)
- Female to Female Jumper Wires (x4)
- DC 5V Power Adapter (x1)
- USB to TTL Serial Cable (x1)  

Make sure the LCD module has an I2C backpack

#### Step 2. Example Circuit
- I2C LCD Module
    - GND pin of the I2C LCD Module is connected to the GND pin on the D3-G board.
    - VCC pin of the I2C LCD Module is connected to the 5V on the D3-G board.
    - SDA pin of the I2C LCD Module is connected to pin 82 on the D3-G board.
    - SCL pin of the I2C LCD Module is connected to pin 81 pin on the D3-G board.

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20D3-G/Software/lcd_circuit.png"></p>
<p align="center"><strong>Figure 7.10 D3-G I2C LCD Module Circuit Schematic  </strong></p>

##### Step 2.1 Pin Mapping
The following table shows pin mapping.

<div align="center">
  <p><strong>Table 7.10 Pin Mapping of D3-G I2C LCD Module</strong></p>
  <table>
      <tr>
          <th colspan="3">Pin Name</th>
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

#### Step 3. How to execute
Install required Python libraries first:
```
$ pip install RPLCD smbus2
```
Then use the following Python code to write text to the LCD:
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

#### Step 4. Execution Result
Run the code with the following command.
```
$ python3 lcd_test.py
```
This script initializes an I2C-based 1602A LCD using the RPLCD library and displays user-entered text on the screen.
When you run the script, you are prompted to enter a string. That text is shown on the LCD for 4 seconds and then cleared. For example:
```
Enter text to display on LCD: Hello D3-G!
```
The LCD will display:
```
Hello D3-G!
```
and then clear after 4 seconds.

To stop the script, press **[Ctrl+C]**.

**Note** : GPIO82 and GPIO81 are used for I2C by default on the D3-G.
Make sure the I2C address (0x27) matches your specific LCD module. Use **i2cdetect -y 3** to scan I2C devices if needed.

<br/><br/><br/><br/>

## 7.3 SPI
---
The D3-G supports Serial Peripheral Interface (SPI) communication through a 40-pin GPIO header, enabling data exchange between external devices and the D3-G.

SPI is a synchronous serial communication protocol that enables full-duplex communication - meaning data can be transmitted and received simultaneously. It uses four main lines: Master Out Slave In (MOSI), Master In Slave Out (MISO), Serial Clock (SCLK), and Chip Select (CS).

Unlike I2C, which uses shared lines for multiple devices, SPI requires a dedicated CS line for each slave device. This one-to-many structure makes SPI fast and straightforward to implement, but it can require more physical wiring when multiple devices are involved.

<br/><br/><br/><br/>

### 7.3.1 Dot Matrix
---
8x8 dot matrix display is commonly used for simple text or pattern output in embedded systems. On the D3-G, the dot matrix module can be controlled through SPI using a driver chip such as the MAX7219.

The MAX7219 handles row and column scanning internally, allowing the microcontroller to control the entire display using only a few SPI signals: MOSI (DIN), SCLK, and CS (LOAD). Once connected, the display can be controlled using SPI communication through user-defined scripts or libraries.

#### Step 1. Hardware Requirements
- D3-G board (x1)
- Dot Matrix (x1)
- Male to Female Jumper Wires (x4)
- DC 5V Power Adapter (x1)
- USB to TTL Serial Cable (x1)

#### Step 2. Example Circuit
- Dot Matrix
    - VCC pin of the Dot Matrix is connected to the 5V pin on the D3-G board.
    - GND pin of the Dot Matrix is connected to the GND pin on the D3-G board.
    - DIN pin of the Dot Matrix is connected to the pin 120 on the D3-G board.
    - CS pin of the Dot Matrix is connected to the pin 119 on the D3-G board.
    - CLK pin of the Dot Matrix is connected to the pin 118 on the D3-G board.

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20D3-G/Software/dot%20circuit.png"></p>
<p align="center"><strong>Figure 7.11 D3-G Dot Matrix Module Circuit Schematic  </strong></p>

##### Step 2.1 Pin Mapping
The following table shows pin mapping.
<div align="center">
  <p><strong>Table 7.11 Pin Mapping of D3-G Dot Matrix</strong></p>
  <table>
      <tr>
          <th colspan="3">Pin Name</th>
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

#### Step 3. How to execute
The following Python script shows how to directly control the MAX7219 through /dev/spidev3.0 using low-level fcntl calls. This method is suitable for devices without external SPI libraries:
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

#### Step 4. Execution Result
Run the code with the following command.
```
$ python3 dot_matrix_test.py
```
This script initializes the SPI-connected MAX7219 dot matrix display and prompts you to input a value. Depending on the input, a specific pattern is shown on the 8x8 LED matrix.

When the script runs, you will see:
```
Enter a number, an uppercase letter (0-9, A-Z), 'Smile', 'Dance', 'Angry', 'Good', 'Nice', 'Emotion':
```
Examples:
- Entering A will display the letter A.
- Entering Smile will show a smiley face pattern.
- Entering Dance will trigger alternating dance animations.
- Entering Nice will animate the letters N-I-C-E in sequence.

To stop the script, press **[Ctrl+C]**.
On termination, the SPI device is safely closed, and the LED matrix stops updating.

**Note**: Ensure that /dev/spidev3.0 exists and the wiring matches the pin mapping table. Also, power the MAX7219 module with a stable 5V source.

<br/><br/><br/><br/>

## 7.4 PWM
---
Pulse Width Modulation (PWM) is used to control devices like LEDs, motors, and buzzers by varying the width of the pulse signal. The D3-G supports PWM through the sysfs interface in Linux.

### 7.4.1 LED Brightness Control
---
This example demonstrates controlling an LED's brightness using PWM on the D3-G.

#### Step 1. Hardware Requirements
- D3-G board (x1)
- LED (x1)
- Male to Female Jumper Wires (x2)
- Breadboard
- DC 5V Power Adapter (x1)
- USB to TTL Serial Cable (x1)

#### Step 2. Example Circuit
- LED
    - (+) pin of the LED is connected to pin 89 on the D3-G board.
    - (-) pin of the LED is connected to the GND pin on the D3-G board.

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20D3-G/Software/led.png"></p>
<p align="center"><strong>Figure 7.12 D3-G LED Circuit Schematic  </strong></p>

##### Step 2.1 Pin Mapping
The following table shows pin mapping.

<div align="center">
  <p><strong>Table 7.12 Pin Mapping of D3-G LED</strong></p>
  <table>
      <tr>
          <th colspan="3">Pin Name</th>
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

#### Step 3. How to execute
To operate the LED (PWM) connected to GPIO89 on the D3-G board, run the following code:
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

#### Step 4. Execution Result
Run the code with the following command.
```
$ python3 led_pwm.py
```
This script initializes PWM on the LED pin and continuously fades the LED brightness up and down.

Once the script is executed, you will see an output like:
```
Starting LED PWM control (press Ctrl+C to stop)
```
The LED will gradually brighten and then dim repeatedly, simulating a "breathing" effect.

To stop the script, press **[Ctrl+C]**.

**Note**: Ensure the PWM channel is not already in use and that the D3-G supports hardware PWM on the selected GPIO. If PWM does not activate, verify the export, period, and duty_cycle settings in /sys/class/pwm/.

<br/><br/><br/><br/>

### 7.4.2 Mini Servo Motor
---
A mini servo motor can be used to control precise angular movement based on a Pulse Width Modulation (PWM) signal through GPIO.
This section demonstrates how to connect and control a mini servo motor using the D3-G.

#### Step 1. Hardware Requirements
- D3-G board (x1)
- Servo Motor (x1)
- Male to Female Jumper Wires (x3)
- DC 5V Power Adapter (x1)
- USB to TTL Serial Cable (x1)

#### Step 2. Example Circuit
- Servo Motor
    - VCC pin of the Servo Motor is connected to the 5V on the D3-G board.
    - GND pin of the Servo Motor is connected to the GND on the D3-G board.
    - SIG pin of the Servo Motor is connected to pin 89 on the D3-G board.

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20D3-G/Software/motor_circuit.png"p>
<p align="center"><strong>Figure 7.13 D3-G Servo Motor Circuit Schematic  </strong></p>

##### Step 2.1 Pin Mapping
The following table shows pin mapping.

<div align="center">
  <p><strong>Table 7.13 Pin Mapping of D3-G Servo Motor</strong></p>
  <table>
      <tr>
          <th colspan="3">Pin Name</th>
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

#### Step 3. How to execute
The following Python script shows how to directly control a mini servo motor using PWM through the sysfs interface on the D3-G. This method requires no external libraries and provides fine-grained control over angle-based positioning.
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

#### Step 4. Execution Result
Run the code with the following command.
```
$ python3 motor_test.py
```
This script uses PWM to control a mini servo motor by adjusting the duty cycle based on the target angle.
Once executed, you will be prompted with:
```
Enter 1 (CW) or 0 (CCW), q to quit:
```
Entering 1 rotates the servo clockwise to 180°, and entering 0 rotates the servo counter-clockwise to 0°. You can repeat this as many times as needed.

To stop the script, enter **[q]** or press **[Ctrl+C]**. The script will then disable and unexport the PWM channel.

**Note**: Ensure your servo motor supports a 50 Hz PWM signal and operates within the 1 ms to 2 ms duty pulse range for safe operation.
