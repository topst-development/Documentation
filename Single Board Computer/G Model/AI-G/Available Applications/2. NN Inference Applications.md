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

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20D3-G/Software/input%20device.png" width="500"></p>
<p align="center"><strong>Figure 1. Connect input device to D3-G </strong></p>
<br/><br/> 

# 3. Video Output
The D3-G board supports FHD monitors via its only DisplayPort (DP) output.
It also supports multi-display output using a daisy chain setup, allowing connection of up to two FHD monitors and one HD monitor simultaneously.

**Note**: To use HDMI, a separate active converter adapter is required.
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20D3-G/Software/monitor.png" width="500"></p>
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
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20D3-G/Software/webcam.png" width="400"></p>
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
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20D3-G/Software/arducam.png" width="400"></p>
<p align="center"><strong>Figure 4. Ardu cam </strong></p>

1. Connect Ardu cam to D3-G MIPI CSI 0 below figure 5.
 
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20D3-G/Software/Arducam%20to%20D3G.png" width="500"></p>
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

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20D3-G/Software/rasp%20v1%20cam.jpg" width="400"></p>
<p align="center"><strong>Figure 6. Raspberry pi v1 cam </strong></p>


1. Connect Raspbery pi v1 cam to D3-G MIPI CSI 1 below figure 7.
 
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20D3-G/Software/rasp%20v1%20cam%20to%20d3g.png" width="500"></p>
<p align="center"><strong>Figure 7. Connecting the Raspberry pi v1 cam to the D3-G </strong></p> 





# 5. Storage Connection
This chapter covers how to connect the D3-G board to various storage devices.
Supported storage options include USB drives, SD cards, and external storage via PCIe.
<br/>

## 5.1 USB Drive
The D3-G board supports USB storage devices through its USB 2.0 and USB 3.0 Type-A ports.
To connect a USB drive:

1. Plug the USB drive into one of the available USB Type-A ports on the D3-G.
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20D3-G/Software/usb%20storage%20connection%20with%20d3g.png" width="500"></p>
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
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20D3-G/Software/sd%20card%20connect%20with%20d3g.png" width="500"></p>
<p align="center"><strong>Figure 9. Connecting the SD Card to the D3-G </strong></p> 

1. Once inserted, the system will typically recognize the SD card as /dev/mmcblk1p1 or a similar device node.
  ```
  $ls /dev/mmcblk*
  ```
2. To mount the SD card manually, use the following command:
```
$ sudo mount /dev/mmcblk1p1 /mnt 
```
3. After mounting, you can access the SD card contents under the /mnt directory.

<br/>

## 5.3 SATA HDD
#### Step 1. Connect the PCIe to SATA Module

## 5.4 NVME M.2 SSD
#### Step 1. Connect the SSD
- NVMe SSD (M.2 PCIe): Insert the NVMe M.2 SSD into the D3-G board’s PCIe slot. 
<br/>
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20D3-G/Software/M.2%20SSD%20connection.png" width="300"></p>
<p align="center"><strong>Figure D3-G NVME M.2 SSD connection  </strong></p>

#### Step 2. Boot the AI-G Board
After executing the reboot command, observe the boot log to verify that the PCIe device is recognized by the system.
Look for messages such as telechips-pcie: Link up, which indicate that the PCIe link has been successfully established.

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
#### Step 3. Check SSD Recognition

```
root@TOPST:~# lspci
00:00.0 PCI bridge: Synopsys, Inc. Device 8040 (rev 01)
01:00.0 Non-Volatile memory controller: Solid State Storage Technology Corporation Device 1007 (rev 03)
```
If the lspci command is not available, please install pciutils.

```
$ sudo apt-get install pciutils
```

#### Step 4. mount the SSD
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

</br></br>


# 6. Ethernet Connection
The TOPST D3-G board supports Ethernet connectivity through its onboard J2C Ethernet port. This allows the board to communicate with local networks or the internet using standard TCP/IP protocols. Ethernet is commonly used for deploying applications that require remote access, data streaming, or software updates.

## 6.1 Network Connection Via Router
This method connects the D3-G board to a local network using a standard router. The board can obtain an IP address automatically via DHCP or be configured with a static IP address.


### 6.1.1 Create the Network Configuration File

1. Dynamic IP via DHCP

If your network provides a DHCP server (e.g., a router or ICS-enabled Windows PC), no file editing is necessary. The system will automatically obtain an IP address as soon as the Ethernet cable is connected.

You can simply plug in the cable and start using the network right away. Proceed to 6.1.3  verify the ip connection.

2. Static IP Configuration

If you prefer to assign a static IP address (e.g., when using direct PC connection or no DHCP server is available), edit the same file with the following content:
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


### 6.1.2 Restart the Network Service
Apply the new network configuration by restarting the systemd-networkd service:

```
sudo systemctl restart systemd-networkd
```
### 6.1.3 Verify Network Connectivity
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20D3-G/Software/router%20connection.png"></p>
<strong>Network Connection Via Router</strong></p>

Test the internet connection by pinging Google's public DNS server:

```
$ ping 8.8.8.8
PING 8.8.8.8 (8.8.8.8): 56 data bytes
64 bytes from 8.8.8.8: seq=0 ttl=113 time=30.208 ms
64 bytes from 8.8.8.8: seq=1 ttl=113 time=38.143 ms
64 bytes from 8.8.8.8: seq=2 ttl=113 time=30.969 ms
64 bytes from 8.8.8.8: seq=3 ttl=113 time=33.586 ms
 
```
## 6.2 Nework Sharing with the Host PC
You can share your PC's internet connection with the TOPST D3-G board without using a router by utilizing the Internet Connection Sharing (ICS) feature available in Windows operating systems.

### 6.2.1 Host PC Network Configuration
Control Panel → Network and Internet → Network Connectivity → Set Ethernet
 
1. Locate the network adapter connected to the internet (e.g., Wi-Fi), right-click on it, and select Properties.

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20AI-G/Available%20Applications/ethernet1.png" width="600"></p>
<p align="center"><strong>Select properties</strong></p>
 
2. Select sharing tab.

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20AI-G/Available%20Applications/ethernet2.png" width="400"></p>
<p align="center"><strong>Select sharing tab</strong></p>

3. Check the box labeled "Allow other network users to connect through this computer’s Internet connection".
 
4. In the Home networking connection dropdown menu, select the Ethernet adapter that the AI-G board will connect to (e.g., "Ethernet").

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20AI-G/Available%20Applications/ethernet3.png" width="400"></p>
<p align="center"><strong>Select Ethernet adapter</strong></p>
 
5. Click OK to save the settings.

 
### 6.2.2 Create the Network Configuration File 

1. Dynamic IP via DHCP

If your network provides a DHCP server (e.g., a router or ICS-enabled Windows PC), no file editing is necessary. The system will automatically obtain an IP address as soon as the Ethernet cable is connected.

You can simply plug in the cable and start using the network right away. Proceed to 6.2.4  verify the ip connection.


2. Static IP Configuration

If you prefer to assign a static IP address (e.g., when using direct PC connection or no DHCP server is available), edit the same file with the following content:
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
 
### 6.2.3 Restart the Network Service
Apply the new network configuration by restarting the systemd-networkd service:

```
sudo systemctl restart systemd-networkd
```
 
### 6.2.4 Verify Network Connectivity
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20D3-G/Software/host%20pc%20ethernet%20connection.png"></p>
<p align="center"><strong> Nework Sharing with the Host PC</strong></p>

Test the internet connection by pinging Google's public DNS server:

```
$ ping 8.8.8.8
PING 8.8.8.8 (8.8.8.8): 56 data bytes
64 bytes from 8.8.8.8: seq=0 ttl=113 time=30.208 ms
64 bytes from 8.8.8.8: seq=1 ttl=113 time=38.143 ms
64 bytes from 8.8.8.8: seq=2 ttl=113 time=30.969 ms
64 bytes from 8.8.8.8: seq=3 ttl=113 time=33.586 ms
```
<br/><br/>

## 6.3 WIFI Device Connection 


<br/><br/>

# 7. 40 Pin GPIO Header
The D3-G board features a 40-pin GPIO header, providing flexible I/O capabilities for various hardware projects.
This header is compatible with general-purpose input/output (GPIO) operations and can be used to connect sensors, LEDs, buttons, and other peripheral devices.

Each pin supports multiple functions such as digital I/O, PWM, I2C, SPI, and UART, depending on the configuration.

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/d3g/Assets/TOPST%20D3-G/Software/d3-g%20gpio%2040pinmap.png" width="800"></p>
<p align="center"><strong>Figure 10. 40 Pin GPIO Header Pinmap of D3-G </strong></p> 

**Note**: Please refer to the official pinout diagram for detailed pin functions and voltage levels before connecting external hardware.
<br/>

## 7.1 GPIO Digital In/Out

The D3-G board supports digital input and output (GPIO) through its 40-pin header, enabling users to interact with external devices such as buttons, LEDs, sensors. 
<br/>

### 7.1.1 LED
An LED can be tested using the board's GPIO pins.  
The following steps demonstrate how to verify GPIO output functionality.

#### Step1. LED Experiment Circuit
The basic LED example uses GPIO pin 89.  
Please refer to the figure below to wire the circuit correctly.

<p align="center"><img src="" width="500"></p>
<p align="center"><strong>Figure LED Basic Example Circuit </strong></p> 
<br/>

#### Step2. Example Code
The Python script used in this example is shown below.

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
        print("program interrupted by user.")
  
    finally:
        unexport_gpio(LED_PIN) # unexport LED pin
        print("GPIO pins unexported.")
        print("program terminated.")

if __name__ == "__main__":
    main()
```

<br/>


#### Step3. Expected Output and Considerations
The LED will blink for 10 seconds and the program will exit automatically.

<br/>

### 7.1.2 Button
A push-button can be used to test digital input functionality using the board's GPIO pins.
The following steps demonstrate how to detect button presses through GPIO input.
<br/>

### Step1. Button Experiment Circuit
This example uses GPIO pin 88 to detect button input.  
Connect one side of the button to GPIO88, and the other side to GND.  
The circuit follows a pull-down resistor configuration to ensure a stable low signal when the button is not pressed.  
Please refer to the figure below to wire the circuit correctly.

<br/>

<p align="center"><img src="" width="500"></p> 
<p align="center"><strong>Figure Button Basic Example Circuit</strong></p>
<br/>

### Step2. Example Code
The Python script used in this example is shown below.

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
  
  
    BUTTON_PIN = 88  # Button connected to GPIO 88
    try:
        export_gpio(BUTTON_PIN, direction="in")
        print("Waiting for button press (CTRL+C to exit)...")
 
        while True:
            if read_gpio_value(BUTTON_PIN):
                print("Button Pressed")
            else:
                print("Button Released")
            time.sleep(0.5)
    except KeyboardInterrupt:
        print("program interrupted by user.")
    finally:
        unexport_gpio(BUTTON_PIN)
        print("GPIO pins unexported.")
        print("program terminated.")
  
if __name__ == "__main__":
    main()
```
<br/>

### Step3. Expected Output and Considerations
The console will continuously display the button state ("Pressed" or "Released") every 0.5 seconds.

<br/>

### 7.1.3 Touch Sensor
A touch sensor can be used to detect human touch as a digital input signal via GPIO.
This section demonstrates how to connect and read input from a basic touch sensor module using the D3-G board.
<br/>

#### Step 1. Experiment Circuit
<br/>

#### Step 2. Example Code
<br/>

#### Step 3. Expected Output and Considerations
<br/>

### 7.1.4 Vibration Detection Sensor

<br/>

### 7.1.5 Infrared Sensor (SZH-SSBH-002)
This experiment explains how to use the SZH-SSBH-002 infrared sensor with the TOPST D3-G board to detect obstacles through a digital input signal.
<br/>


#### Step 1. Experiment Circuit
The SZH-SSBH-002 IR sensor can detect nearby obstacles using infrared reflection.
Connect the sensor's output to GPIO pin 89 on the D3-G.

- IR Sensor (SZH-SSBH-002):
    - VCC → 3.3V
    - GND → GND
    - OUT → GPIO 89 (input)


<p align="center"><img src="" width="500"></p> 
<p align="center"><strong>Figure IR Sensor(SZH-SSBH-002) Experiment Circuit</strong></p>
<br/>


#### Step 2. Example Code
The following Python script reads the IR sensor value from GPIO 89 and prints the detection result:

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
            # IR sensor value read
            # If the sensor value is 0, it means an obstacle is detected.
            # If the sensor value is 1, it means no obstacle is detected.
            sensor_value = read_gpio_value(IR_SENSOR_PIN)
 
            if sensor_value == "0":  # obstacle detected
                print("obstacle detected.")
            else:    # obstacle undetected
                print("obstacle undetected.")
 
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

<br/>

#### Step 3. Expected Output and Considerations
When the IR sensor detects an object in front of it (within its detection range), the terminal will display:
```
Obstacle detected.

```
When nothing is detected, the message will be:

```
No obstacle detected.
```
<br/>

### 7.1.6 Phtoregister (SZH-SSBH-011)
This experiment demonstrates how to use the SZH-SSBH-001 photoresistor (CDS sensor) with the TOPST D3-G board to detect ambient brightness and automatically control an LED.
<br/>

### Step 1. Experiment Circuit
In this setup, we connect the SZH-SSBH-001 photoresistor module to GPIO pin 89, and an LED to GPIO pin 83.

- CDS Sensor : 
  - VCC → 3.3V
  - GND → GND
  - OUT → GPIO 89 (input)

- LED:
    - Anode (+) → GPIO 83 (output) via a resistor (e.g., 220Ω)
    - Cathode (−) → GND

<p align="center"><img src="" width="500"></p> 
<p align="center"><strong>Figure Photoregister(SZH-SSBH-001) Experiment Circuit</strong></p>
<br/>

### Step 2. Example Code
The Python script used in this example is shown below.

```
import os
import time

# GPIO pin numbers setting
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
            # read the sensor value
            # If the sensor value is 0, it means light is detected.
            # If the sensor value is 1, it means no light is detected.
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
<br/>

### Step 3. Expected Output and Consideration
When light is detected by the photoresistor module, the terminal will display: 
```
sensor value: 0
brightness detected. Turning on the LED.
```
and the LED turns ON.


When light is not detected, the output will be:
```
sensor value: 1
no brightness detected. Turning off the LED.
```
and the LED turns OFF.

<br/>



### 7.1.7 Air Pollution Check Sensor

<br/>

### 7.1.8 Ultrasonic Sensor

<br/>

## 7.2 I2C

### 7.2.1 1602A LCD Display
### 7.2.2 9-Axis Gyro 
### 7.2.3 Photoregister(BH1750)

## 7.3 SPI
### 7.3.1 Dot Matrix

## 7.4 PWM
### 7.4.1 LED
### 7.4.2 Mini Servo Motor

# 8. JTAG Connection

# 9. CAN Connection

