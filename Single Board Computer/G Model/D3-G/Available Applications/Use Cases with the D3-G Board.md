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
One of the simplest and most common GPIO output examples is controlling an LED.  
To demonstrate digital output, an LED can be connected to one of the GPIO pins on the 40 pin header. In this example, the LED's cathode (short leg) is connected to the GND pin on the D3-G board, while the anode (long leg) is directly connected to GPIO89.

#### Step 1. Hardware Requirements
- TOPST D3-G board (x1)
- Breadboard (x1)
- LED (x1)
- male to female jumper wire (x2)
- DC 5V Power Adapter (x1)
- USB to TTL Serial Cable (x1)

#### Step 2. Example Circuit
- LED
    - (+) pin connected to pin 12 on the TOPST D3-G board.
    - (-) pin connected to pin 14 which acts as GND on the TOPST D3-G board.  

<p align="center"><img src="" width="500"></p>
<p align="center"><strong>Figure D3-G GPIO LED Circuit Schematic </strong></p> 
<br/>

##### Step 2.1 Pin Mapping
The following table shows pin mapping.

<p align="center"><strong>Table 2.1 Pin Mapping of AI-G LED</strong></p>
<table align="center">
    <tr>
        <th colspan="3">Pin Name</th>
        <th>D3-G Board</th>
        <th>GPIO</th>
    </tr>
    <tr>
        <td colspan="3">LED (+) pin</td>
        <td>12</td>
        <td>89</td>
    </tr>
</table>

#### Step3. How to execute
To operate the LED connected to GPIO89 on the D3-G board, simply run the following code:

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
#### Step 4. Execution Result
This script configures GPIO89 as a digital output and toggles its state every 1 second.
When executed, the LED connected to GPIO89 will blink 10 times—turning on for 1 second and then off for 1 second repeatedly. After 10 cycles, the script will exit and automatically unexport the GPIO.

To stop the script early, press Ctrl+C.
In either case, the pin will be properly released and cleaned up.

Run the code with the following command.

```
$ python3 led_test.py
```
NOTE: This setup assumes a direct LED connection. For safe and long-term operation, it is strongly recommended to use a current-limiting resistor (e.g., 220Ω) in series with the LED to prevent excessive current draw and protect the GPIO pin from potential damage.
<br/>


<br/>

### 7.1.2 Button
A push button is a basic input device commonly used to demonstrate digital input handling through GPIO.
In this example, one side of the button is connected to a 3.3V power pin on the D3-G board, while the other side is connected to GPIO88. When the button is pressed, GPIO88 reads a HIGH signal 1.

#### Step 1. Hardware Requirements
- TOPST D3-G board (x1)
- Breadboard (x1)
- Button (x1)
- male to female jumper wire (x2)
- DC 5V Power Adapter (x1)
- USB to TTL Serial Cable (x1)
<br/>

#### Step 2. Example Circuit
Button switch
- One leg of the button switch is connected to pin 10 on the TOPST D3-G board.
- The opposite leg above the button is connected to the 3.3V pin.
<br/>

<p align="center"><img src="" width="500"></p> 
<p align="center"><strong>Figure D3-G GPIO Button Circuit Schematic</strong></p>
<br/>

##### Step2.1 Pin Mapping
The following table shows pin mapping.

<p align="center"><strong>Table 2.1 Pin Mapping of D3-G Button</strong></p>
<table align="center">
    <tr>
        <th colspan="3">Pin Name</th>
        <th>D3-G Board</th>
        <th>GPIO</th>
    </tr>
    <tr>
        <td colspan="3">One leg pin of button</td>
        <td>10</td>
        <td>88</td>
    </tr>
</table>

#### Step 3. How to excute

To monitor the button input connected to GPIO88 on the D3-G board, simply run the following code:

```
import os
import time # GPIO pin numbers setting
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
    export_gpio(BUTTON_PIN, "in")  # IR sensor pin direction "in"
    print("gpio pins initialized.")
 
    try:
        while True:
            # button sensor value read
            # If the sensor value is 0, it means an button pressed.
            # If the sensor value is 1, it means no button released.
            sensor_value = read_gpio_value(BUTTON_PIN)
 
            if sensor_value == "0":  
                print("button pressed.")
            else:    
                print("button released.")
 
            time.sleep(0.5)  # 500ms delay

    except KeyboardInterrupt:
        print("program interrupted by user.")
 
    finally:
        unexport_gpio(BUTTON_PIN)  # unexport the GPIO pin
        print("GPIO pins unexported.")
        print("program terminated.")
         
if __name__ == "__main__":
    main()
```
<br/>

#### Step 4. Execution Result
This script configures GPIO88 as a digital input and continuously monitors its value in real time.
When executed, pressing the button connected to GPIO88 will print a message indicating that the button has been pressed.

To stop the script, press 'Ctrl+C'.
When the script is terminated, GPIO88 will be automatically unexported and cleand up.

Run the code with the following command.
```
$ python3 test_button.py
```
Note: GPIO88 is used here as an example. You may use any available GPIO pin on the D3-G board based on the 40-pin header pinout.
Be sure to refer to the official pinout diagram and select a GPIO number that matches your hardware configuration.
<br/>

### 7.1.3 Touch Sensor
A touch sensor can be used to detect human touch as a digital input signal via GPIO.
This section demonstrates how to connect and read input from a basic touch sensor module using the D3-G board.
<br/>

#### Step 1. Hardware Requirements
- TOPST D3-G board (x1)
- Breadboard (x1)
- Touch sensor (x1)
- male to female jumper wire (x3)
- DC 5V Power Adapter (x1)
- USB to TTL Serial Cable (x1)
<br/>

#### Step 2. Example Circuit
- Touch sensor
    - SIG pin of the touch sensor is connected to pin 88 on the TOPST D3-G board.
    - VCC pin of the touch sensor is connected to the 3.3V on the TOPST D3-G board.
    - GND pin of the touch sensor is connected to GND on the TOPST D3-G board.
<br/>

<p align="center"><img src="" width="500"></p> 
<p align="center"><strong>Figure D3-G GPIO Button Circuit Schematic</strong></p>
<br/>

##### Step2.1 Pin Mapping
The following table shows pin mapping.

<p align="center"><strong>Table 2.1 Pin Mapping of D3-G Touch sensor</strong></p>
<table align="center">
    <tr>
        <th colspan="3">Pin Name</th>
        <th>D3-G Board</th>
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
        <td>9</td>
        <td>GND</td>
    </tr>
</table>

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
    export_gpio(TOUCH_SENSOR_PIN, "in")  # ouch sensor pin direction "in"
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
<br/>

#### Step 4. Execution Result
This script configures GPIO88 as a digital input and continuously monitors its value in real time.
When executed, touching the sensor connected to GPIO88 will print a message indicating that a touch has been detected.
When the sensor is not touched, the terminal will indicate that the touch has been released.

To stop the script, press Ctrl+C.
When the script is terminated, GPIO88 will be automatically unexported and cleaned up.

Run the code with the following command.

```
$ python3 touch_test.py
```
Note: GPIO88 is used here as an example. You may use any available GPIO pin on the D3-G board based on the 40-pin header pinout.
Be sure to refer to the official pinout diagram and select a GPIO number that matches your hardware configuration.
<br/>

### 7.1.4 Vibration Detection Sensor
A vibration sensor can be used to detect physical shocks or vibrations and output a digital input signal via GPIO.
This section demonstrates how to connect and detect input from a basic vibration sensor module using the D3-G board.
#### Step 1. Hardware Requirements

- TOPST D3-G board (x1)
- Vibration Detection Sensor (x1)
- female to female jumper wire (x4)
- DC 5V Power Adapter (x1)
- USB to TTL Serial Cable (x1)

#### Step 2. Example Circuit
- Vibration Detection Sensor
    - VCC pin of the Vibration Detection Sensor is connected to the 3.3V pin on the TOPST D3-G board.
    - GND pin of the Vibration Detection Sensor is connected to the GND on the TOPST D3-G board.
    - DIN pin of the Vibration Detection Sensor is connected to the 88 pin on the TOPST D3-G board.

<br/>

<p align="center"><img src="" width="500"></p> 
<p align="center"><strong>Figure D3-G GPIO Vibration Detection Sensor Circuit Schematic</strong></p>
<br/>

##### Step2.1 Pin Mapping
The following table shows pin mapping.

<p align="center"><strong>Table Pin Mapping of D3-G Vibration Detection Sensor</strong></p>
<table align="center">
    <tr>
        <th colspan="3">Pin Name</th>
        <th>D3-G Board</th>
        <th>GPIO</th>
    </tr>
    <tr>
        <td colspan="3">VCC</td>
        <td>1</td>
        <td>3.3V</td>
    </tr>
    <tr>
        <td colspan="3">GND</td>
        <td>9</td>
        <td>GND</td>
    </tr>
    <tr>
        <td colspan="3">DO</td>
        <td>10</td>
        <td>88</td>
    </tr>
</table>

#### Step 3. How to execute
To monitor the vibration sensor connected to GPIO88 on the D3-G board, run the following code:
```
import os
import time
 
# GPIO pin numbers setting
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
            # VIBRATION IR sensor value read
            # If the sensor value is 0, it means an vibration is detected.
            # If the sensor value is 1, it means no vibration is detected.
            sensor_value = read_gpio_value(VIBRATION_SENSOR_PIN)
 
            if sensor_value == "0":  # vibration detected
                print("vibration detected.")
            else:    # vibration undetected
                print("vibration undetected.")
 
            time.sleep(0.5)  # 500ms delay

    except KeyboardInterrupt:
        print("program interrupted by user.")
 
    finally:
        unexport_gpio(VIBRATION_SENSOR_PIN)  # unexport the GPIO pin
        print("GPIO pins unexported.")
        print("program terminated.")
         
if __name__ == "__main__":
    main()
```

#### Step 4. Execution Result
This script configures GPIO88 as a digital input and continuously monitors its value in real time.
When executed, vibrations or shocks detected by the sensor will cause the terminal to print a message such as:
```
vibration detected.
```
When there is no vibration, the output will be:
```
vibration undetected.
```
To stop the script, press Ctrl+C.
Upon termination, GPIO88 will be automatically unexported and cleaned up.

Run the code with the following command.

```
$ python3 vibration_test.py
```
Note: GPIO88 is used here as an example. You may use any other available GPIO pin depending on your sensor wiring and header layout. Be sure to check the D3-G pinout before choosing a GPIO number.
<br/>

### 7.1.5 Infrared Sensor (SZH-SSBH-002)
This experiment explains how to use the SZH-SSBH-002 infrared sensor with the TOPST D3-G board to detect obstacles through a digital input signal.
<br/>

#### Step 1. Hardware Requirements

- TOPST D3-G board (x1)
- Breadboard (x1)
- Button (x1)
- male to female jumper wire (x3)
- DC 5V Power Adapter (x1)
- USB to TTL Serial Cable (x1)

#### Step 2. Example Circuit
- Infrared Sensor
    - VCC pin of the Infrared Sensor is connected to the 3.3V pin on the TOPST D3-G board.
    - GND pin of the Infrared Sensor is connected to the GND on the TOPST D3-G board.
    - OUT pin of the Infrared Sensor is connected to the 89 pin on the TOPST D3-G board.


<p align="center"><img src="" width="500"></p> 
<p align="center"><strong>Figure IR Sensor(SZH-SSBH-002) Experiment Circuit</strong></p>
<br/>

##### Step 2.1 Pin Mapping
The following table shows pin mapping.

<p align="center"><strong>Table 2.1 Pin Mapping of D3-G Dot Matrix</strong></p>
<table align="center">
    <tr>
        <th colspan="3">Pin Name</th>
        <th>D3-G Board</th>
        <th>GPIO</th>
    </tr>
    <tr>
        <td colspan="3">VCC</td>
        <td>1</td>
        <td>3.3V</td>
    </tr>
    <tr>
        <td colspan="3">GND</td>
        <td>9</td>
        <td>GND</td>
    </tr>
    <tr>
        <td colspan="3">OUT</td>
        <td>12</td>
        <td>89</td>
    </tr>
</table>

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

#### Step 4. Execution Result
This script configures GPIO89 as a digital input and continuously monitors its state to detect obstacles.
When an object is detected in front of the IR sensor, the terminal will display:
```
obstacle detected.
```
When no object is detected, it will display:
```
obstacle undetected.
```
To stop the script, press Ctrl+C.
When the script is terminated, GPIO89 will be automatically unexported and cleaned up.

Run the code with the following command.
```
$ python ir_test.py
```
Note: GPIO89 is used as an example in this script.
You may use any available GPIO pin based on the 40-pin header of the D3-G board. Be sure to consult the official pinout diagram for accurate pin selection.
<br/>


### 7.1.6 Phtoregister (SZH-SSBH-011)
This experiment demonstrates how to use the SZH-SSBH-011 photoresistor (CDS sensor) with the TOPST D3-G board to detect ambient light and automatically control an LED using GPIO.
<br/>


#### Step 1. Hardware Requirements
- TOPST D3-G board (x1)
- Photoresistor module SZH-SSBH-011 (x1)
- LED (x1)
- 220Ω resistor (x1)
- Breadboard (x1)
- Male to Female Jumper Wires (x4)
- DC 5V Power Adapter (x1)
- USB to TTL Serial Cable (x1)

#### Step 2. Example Circuit
- Phtoregister (SZH-SSBH-011)
    - VCC pin of the Phtoregister is connected to the 3.3V pin on the TOPST D3-G board.
    - GND pin of the Phtoregister is connected to the GND on the TOPST D3-G board.
    - DIN pin of the Phtoregister is connected to 89 pin on the TOPST D3-G board.
- LED
    - (+) pin of the LED is connected to the GND on the TOPST D3-G board.
    - (-) pin of the LED is connected to 83 pin on the TOPST D3-G board.


<p align="center"><img src="" width="500"></p> 
<p align="center"><strong>Figure Photoregister(SZH-SSBH-001) Experiment Circuit</strong></p>
<br/>


##### Step 2.1 Pin Mapping
The following table shows pin mapping.

<p align="center"><strong>Table 2.1 Pin Mapping of D3-G </strong></p>
<table align="center">
    <tr>
        <th colspan="3">Pin Name</th>
        <th>D3-G Board</th>
        <th>GPIO</th>
    </tr>
    <tr>
        <td colspan="3">VCC</td>
        <td>1</td>
        <td>3.3V</td>
    </tr>
    <tr>
        <td colspan="3">GND</td>
        <td>9</td>
        <td>GND</td>
    </tr>
    <tr>
        <td colspan="3">OUT</td>
        <td>12</td>
        <td>89</td>
    </tr>
</table>
<p align="center"><strong>Table 2.1 Pin Mapping of D3-G LED</strong></p>
<table align="center">
    <tr>
        <th colspan="3">Pin Name</th>
        <th>D3-G Board</th>
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

### Step 3. How to execute
Run the following Python script to monitor brightness with the CDS sensor and control the LED accordingly:

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

### Step 4. Execution Result
This script configures GPIO89 as an input for the photoresistor sensor and GPIO83 as an output for the LED.
When ambient light is detected, the terminal will print:
```
sensor value: 0
brightness detected. Turning on the LED.
```
and the LED turns ON.
When no light is detected, it will print:
```
sensor value: 1
no brightness detected. Turning off the LED.
```
and the LED turns OFF.
To stop the script, press Ctrl+C.
When the script is terminated, both GPIO pins will be automatically unexported and cleaned up.

Run the code with the following command.
```
$ python3 CDS_test.py
```
Note: GPIO83 and GPIO89 are used in this example. You may use other available GPIOs as needed.
Ensure that the pin mapping aligns with the official 40-pin header layout of the D3-G board.
<br/>



### 7.1.7 Air Pollution Detection Sensor
This experiment demonstrates how to use a gas (air quality) sensor with the TOPST D3-G board to detect the presence of gas or air pollution levels through a digital input signal via GPIO.

#### Step 1. Hardware Requirements
- TOPST D3-G board (x1)
- Air Pollution (Gas) Detection Sensor Module (x1)
- Breadboard (x1)
- Male to Female Jumper Wires (x3)
- DC 5V Power Adapter (x1)
- USB to TTL Serial Cable (x1)

#### Step 2. Example Circuit
- Air Pollution Detection Sensor
    - VCC pin of the Air Pollution Detection Sensor is connected to the 3.3V pin on the TOPST D3-G board.
    - GND pin of the Air Pollution Detection Sensor is connected to the GND on the TOPST D3-G board.
    - DO pin of the Air Pollution Detection Sensor is connected to 88 pin on the TOPST D3-G board.



<p align="center"><img src="" width="500"></p> 
<p align="center"><strong>Figure Air Pollution Detection Sensor Experiment Circuit</strong></p>
<br/>


##### Step 2.1 Pin Mapping
The following table shows pin mapping.

<p align="center"><strong>Table 2.1 Pin Mapping of D3-G </strong></p>
<table align="center">
    <tr>
        <th colspan="3">Pin Name</th>
        <th>D3-G Board</th>
        <th>GPIO</th>
    </tr>
    <tr>
        <td colspan="3">VCC</td>
        <td>1</td>
        <td>3.3V</td>
    </tr>
    <tr>
        <td colspan="3">GND</td>
        <td>9</td>
        <td>GND</td>
    </tr>
    <tr>
        <td colspan="3">OUT</td>
        <td>10</td>
        <td>88</td>
    </tr>
</table>

#### Step 3. How to Execute
Run the following Python script to monitor gas detection using the GPIO88 pin:

```
import os
import time
 
# GPIO pin numbers setting
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
            # If the sensor value is 0, it means an vibration is detected.
            # If the sensor value is 1, it means no vibration is detected.
            sensor_value = read_gpio_value(GAS_SENSOR_PIN)
 
            if sensor_value == "0":  # gas detected
                print("gas detected.")
            else:    # gas undetected
                print("gas undetected.")
 
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
This script configures GPIO88 as a digital input and continuously monitors gas detection status.
When the gas concentration reaches the sensor’s threshold, the terminal will display:
```
gas detected.
```
When no gas is detected, the terminal will show:
```
gas undetected.
```
To stop the script, press Ctrl+C.
When the script is terminated, GPIO88 will be automatically unexported and cleaned up.

Run the code with the following command.
```
$ python3 gas_sensor_test.py
```
Note: GPIO88 is used here as an example. You may choose another available GPIO pin according to your wiring setup.
Be sure to consult the official D3-G 40-pin header pinout before selecting GPIO numbers.
<br/>

### 7.1.8 Ultrasonic Sensor
This experiment demonstrates how to use an ultrasonic distance sensor (e.g., HC-SR04) with the TOPST D3-G board to measure the distance to an object using GPIO pins.

#### Step 1. Hardware Requirements
- TOPST D3-G board (x1)
- Ultrasonic Sensor (x1)
- Breadboard (x1)
- Male to Female Jumper Wires (x4)
- DC 5V Power Adapter (x1)
- USB to TTL Serial Cable (x1)

#### Step 2. Example Circuit
- Ultrasonic Sensor
    - VCC pin of the Ultrasonic Sensor is connected to the 5V pin on the TOPST D3-G board.
    - GND pin of the Ultrasonic Sensor is connected to the GND on the TOPST D3-G board.
    - TRIG pin of the Ultrasonic Sensor is connected to 82 pin on the TOPST D3-G board.
    - ECHO pin of the Ultrasonic Sensor is connected to 88 pin on the TOPST D3-G board.


<p align="center"><img src="" width="500"></p> 
<p align="center"><strong>Figure Air Pollution Detection Sensor Experiment Circuit</strong></p>
<br/>

##### Step 2.1 Pin Mapping
The following table shows pin mapping.

<p align="center"><strong>Table 2.1 Pin Mapping of D3-G </strong></p>
<table align="center">
    <tr>
        <th colspan="3">Pin Name</th>
        <th>D3-G Board</th>
        <th>GPIO</th>
    </tr>
    <tr>
        <td colspan="3">VCC</td>
        <td>2</td>
        <td>5V</td>
    </tr>
    <tr>
        <td colspan="3">GND</td>
        <td>9</td>
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

#### Step 3. How to Execute
Run the following Python script to measure distance using the ultrasonic sensor:
```
import os
import time

TRIG_PIN = 82  # GPIO 출력 (초음파 발생)
ECHO_PIN = 88  # GPIO 입력 (초음파 반사 수신)

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
    # 1. TRIG LOW
    write_gpio_value(TRIG_PIN, 0)
    time.sleep(0.00002)  # 20μs 안정화

    # 2. TRIG HIGH for 10μs
    write_gpio_value(TRIG_PIN, 1)
    time.sleep(0.00001)  # 10μs 펄스
    write_gpio_value(TRIG_PIN, 0)

    # 3. ECHO HIGH 감지 대기 (start time)
    start = time.time()
    while read_gpio_value(ECHO_PIN) == "0":
        start = time.time()

    # 4. ECHO LOW 감지 대기 (end time)
    end = start
    while read_gpio_value(ECHO_PIN) == "1":
        end = time.time()

    # 5. 거리 계산
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
<br/>

#### Step 4. Execution Result
This script configures GPIO82 as a digital output to trigger the ultrasonic pulse, and GPIO88 as a digital input to receive the echo.
When the script runs, the distance to the nearest object in front of the sensor will be printed every second, for example:
```
Distance: 23.45 cm
Distance: 24.12 cm
...
```
To stop the script, press Ctrl+C.
When the script is terminated, GPIO82 and GPIO88 will be automatically unexported and cleaned up.

Run the code with the following command.
```
$ python3 ultrasonic_sensor_test.py
```
Note: GPIO82 and GPIO88 are used as examples. You may modify the pins based on your wiring and available GPIOs on the D3-G board.
Also, ensure your ECHO pin's voltage level is safe for the board (some modules output 5V and may need a voltage divider or level shifter).

## 7.2 I2C
The D3-G board provides I2C communication through the 40-pin GPIO header, allowing it to interface with various peripherals such as sensors, displays, and expansion modules.
I2C (Inter-Integrated Circuit) is a two-wire communication protocol consisting of a data line (SDA) and a clock line (SCL), enabling multiple devices to communicate over a shared bus.

I2C communication follows a master-slave architecture, where one master device controls the communication and up to 127 slave devices can be connected on the same bus.
The SDA line is used for both transmitting and receiving data, while the SCL line synchronizes the timing of data transfer. This synchronous communication model allows devices to exchange information in a coordinated, clock-driven manner.

### 7.2.1 1602A LCD Display
The 1602A LCD is a character display module commonly used in embedded systems.
On the D3-G board, the LCD's SDA and SCL lines can be connected to GPIO pins configured for I2C. Once connected, the LCD can be controlled using the Linux I2C tools or custom software.

#### Step 1. Hardware Requirements
- TOPST D3-G board (x1)
- 1602A I2C LCD Module (x1)
- Male to Female Jumper Wires (x4)
- DC 5V Power Adapter (x1)
- USB to TTL Serial Cable (x1)
Make sure the LCD module has an I2C backpack

#### Step 2. Example Circuit
- I2C LCD Module
    - GND pin of the I2C LCD Module is connected to the GND pin on the TOPST D3-G board.
    - VCC pin of the I2C LCD Module is connected to the 5V on the TOPST D3-G board.
    - SDA pin of the I2C LCD Module is connected to the 82 pin on the TOPST D3-G board.
    - SCL pin of the I2C LCD Module is connected to the 81 pin on the TOPST D3-G board.

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20AI-G/Available%20Applications/3.3.1%20AI-G%20SPI%20Dot Matrix%20Circuit%20Schematic.png" width="600"></p>
<p align="center"><strong>Figure D3-G I2C LCD Module Circuit Schematic  </strong></p>

##### Step 2.1 Pin Mapping
The following table shows pin mapping.

<p align="center"><strong>Table Pin Mapping of D3-G I2C LCD Module</strong></p>
<table align="center">
    <tr>
        <th colspan="3">Pin Name</th>
        <th>D3-G Board</th>
        <th>GPIO</th>
    </tr>
    <tr>
        <td colspan="3">GND</td>
        <td>9</td>
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
This script initializes an I2C-based 1602A LCD using the RPLCD library and displays user-entered text on the screen.
When you run the script, you’ll be prompted to enter a string. That text will be shown on the LCD for 4 seconds and then cleared. For example:
```
Enter text to display on LCD: Hello D3-G!
```
The LCD will display:
```
Hello D3-G!
```
and then clear after 4 seconds.

To stop the script, press Ctrl+C.

Note : GPIO82 and GPIO81 are used for I2C by default on the D3-G board.
Make sure the I2C address (0x27) matches your specific LCD module. Use i2cdetect -y 3 to scan I2C devices if needed.

## 7.3 SPI
The D3-G board supports SPI (Serial Peripheral Interface) communication through a 40-pin GPIO header, enabling data exchange between external devices and the board.

SPI is a synchronous serial communication protocol that enables full-duplex communication - meaning data can be transmitted and received simultaneously. It uses four main lines: MOSI (Master Out Slave In), MISO (Master In Slave Out), SCLK (Serial Clock), and CS (Chip Select).

Unlike I2C, which uses shared lines for multiple devices, SPI requires a dedicated CS line for each slave device. This one-to-many structure makes SPI fast and straightforward to implement, but it can require more physical wiring when multiple devices are involved.

### 7.3.1 Dot Matrix
8x8 dot matrix display is commonly used for simple text or pattern output in embedded systems. On the D3-G board, the dot matrix module can be controlled via SPI using a driver chip such as the MAX7219.

The MAX7219 handles row and column scanning internally, allowing the microcontroller to control the entire display using only a few SPI signals: MOSI (DIN), SCLK and, CS (LOAD). Once connected, the display can be controlled using SPI communication through user-defined scripts or libraries.

#### Step 1. Hardware Requirements
- TOPST D3-G board (x1)
- Dot Matrix (x1)
- Male to Female Jumper Wires (x4)
- DC 5V Power Adapter (x1)
- USB to TTL Serial Cable (x1)
Make sure the LCD module has an I2C backpack

#### Step 2. Example Circuit
- Dot Matrix
    - VCC pin of the Dot Matrix is connected to the 5V on the TOPST D3-G board.
    - GND pin of the Dot Matrix is connected to the GND on the TOPST D3-G board.
    - DIN pin of the Dot Matrix is connected to the 120 pin on the TOPST D3-G board.
    - CS pin of the Dot Matrix is connected to the 119 pin on the TOPST D3-G board.
    - CLK pin of the Dot Matrix is connected to the 118 pin on the TOPST D3-G board.

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20AI-G/Available%20Applications/3.3.1%20AI-G%20SPI%20Dot Matrix%20Circuit%20Schematic.png" width="600"></p>
<p align="center"><strong>Figure D3-G Dot Matrix Module Circuit Schematic  </strong></p>

##### Step 2.1 Pin Mapping
The following table shows pin mapping.

<p align="center"><strong>Table Pin Mapping of D3-G I2C Dot Matrix</strong></p>
<table align="center">
    <tr>
        <th colspan="3">Pin Name</th>
        <th>D3-G Board</th>
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
        <td>38</td>
        <td>120</td>
    </tr>
    <tr>
        <td colspan="3">CS</td>
        <td>36</td>
        <td>119</td>
    </tr>
    <tr>
        <td colspan="3">CLK</td>
        <td>40</td>
        <td>118</td>
    </tr>
</table>

#### Step 3. How to execute
The following Python script shows how to directly control the MAX7219 via /dev/spidev3.0 using low-level fcntl calls. This method is suitable for devices without external SPI libraries:
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
This script initializes the SPI-connected MAX7219 dot matrix display and prompts the user to input a value. Depending on the input, a specific pattern is shown on the 8x8 LED matrix.

When the script runs, you will see:
```
Enter a number, an uppercase letter (0-9, A-Z), 'Smile', 'Dance', 'Angry', 'Good', 'Nice', 'Emotion':
```
Examples:
- Entering A will display the letter A.
- Entering Smile will show a smiley face pattern.
- Entering Dance will trigger alternating dance animations.
- Entering Nice will animate the letters N-I-C-E in sequence.

To stop the script, press Ctrl+C.
On termination, the SPI device is safely closed, and the LED matrix stops updating.

Note: Ensure that /dev/spidev3.0 exists and the wiring matches the pin mapping table. Also, power the MAX7219 module with a stable 5V source.

## 7.4 PWM
PWM (Pulse Width Modulation) is used to control devices like LEDs, motors, and buzzers by varying the width of the pulse signal. The D3-G board supports PWM through the sysfs interface in Linux.

### 7.4.1 LED Brightness Control
This example demonstrates controlling an LED's brightness using PWM on the D3-G board.

#### Step 1. Hardware Requirements
- TOPST D3-G board (x1)
- LED (x1)
- Male to Female Jumper Wires (x2)
- Breadboard
- DC 5V Power Adapter (x1)
- USB to TTL Serial Cable (x1)

#### Step 2. Example Circuit
- LED
    - (+) pin of the LED is connected to the 89 on the TOPST D3-G board.
    - (-) pin of the LED is connected to GND on the TOPST D3-G board.


<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20AI-G/Available%20Applications/3.3.1%20AI-G%20SPI%20Dot Matrix%20Circuit%20Schematic.png" width="600"></p>
<p align="center"><strong>Figure D3-G LED Circuit Schematic  </strong></p>

##### Step 2.1 Pin Mapping
The following table shows pin mapping.

<p align="center"><strong>Table Pin Mapping of D3-G LED</strong></p>
<table align="center">
    <tr>
        <th colspan="3">Pin Name</th>
        <th>D3-G Board</th>
        <th>GPIO</th>
    </tr>
    <tr>
        <td colspan="3">(+)</td>
        <td>12</td>
        <td>89</td>
    </tr>
    <tr>
        <td colspan="3">(-)</td>
        <td>6</td>
        <td>GND</td>
    </tr>
</table>

#### Step 3. How to execute
To operate the LED(PWM) connected to GPIO89 on the D3-G board, simply run the following code:
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
This script initializes PWM on the LED pin and continuously fades the LED brightness up and down.

Once the script is executed, you will see output like:
```
Starting LED PWM control (press Ctrl+C to stop)
```
The LED will gradually brighten and then dim repeatedly, simulating a "breathing" effect.

To stop the script, press Ctrl+C.

Note: Ensure the PWM channel is not already in use and that the D3-G board supports hardware PWM on the selected GPIO. If PWM does not activate, verify the export, period, and duty_cycle settings in /sys/class/pwm/.


### 7.4.2 Mini Servo Motor
This example demonstrates controlling an LED's brightness using PWM on the D3-G board.

#### Step 1. Hardware Requirements
- TOPST D3-G board (x1)
- Servo Motor (x1)
- Male to Female Jumper Wires (x3)
- DC 5V Power Adapter (x1)
- USB to TTL Serial Cable (x1)

#### Step 2. Example Circuit
- Servo Motor
    - VCC pin of the Servo Motor is connected to 5V on the TOPST D3-G board.
    - GND pin of the Servo Motor is connected to GND on the TOPST D3-G board.
    - SIG pin of the Servo Motor is connected to the 89 on the TOPST D3-G board.


<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20AI-G/Available%20Applications/3.3.1%20AI-G%20SPI%20Dot Matrix%20Circuit%20Schematic.png" width="600"></p>
<p align="center"><strong>Figure D3-G Servo Motor Circuit Schematic  </strong></p>

##### Step 2.1 Pin Mapping
The following table shows pin mapping.

<p align="center"><strong>Table Pin Mapping of D3-G Servo Motor</strong></p>
<table align="center">
    <tr>
        <th colspan="3">Pin Name</th>
        <th>D3-G Board</th>
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
        <td colspan="3">SIG</td>
        <td>12</td>
        <td>89</td>
    </tr>
</table>

#### Step 3. How to execute
The following Python script shows how to directly control a mini servo motor using PWM through the sysfs interface on the D3-G board. This method requires no external libraries and provides fine-grained control over angle-based positioning.
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
    pulse_width = 1_000_000 + (angle / 180) * _000_000
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
This script uses PWM to control a mini servo motor by adjusting the duty cycle based on the target angle.
Once executed, you will be prompted with:
```
Enter 1 (CW) or 0 (CCW), q to quit:
```
Entering 1 will rotate the servo clockwise to 180°, and entering 0 will rotate it counter-clockwise to 0°. You can repeat this as many times as needed.

To stop the script, enter q or press Ctrl+C. The script will then disable and unexport the PWM channel.

⚠️ Note: Ensure your servo motor supports a 50Hz PWM signal and operates within the 1ms–2ms duty pulse range for safe operation.