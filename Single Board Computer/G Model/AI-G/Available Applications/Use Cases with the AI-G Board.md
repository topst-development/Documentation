# 1. Introduction 
This document provides usage examples using the TOPST AI-G.   
This document includes information on the following:
- Camera Connection
  - MIPI CSI
- Video Output
  - MIPI DSI
- NN Inference Applications
- 40 Pin GPIO Header
  - Available Sensor & Device
- Storage Connection
  - SATA HDD
  - NVME M.2 SSD
- Ethernet Connection
- JTAG Connection
- CAN Connection
<br/><br/>

# 2. Camera Connection
The AI-G board supports camera input via a MIPI CSI2 interface.
By default, it provides a 2-lane CSI connection through a 15-pin connector. For applications requiring higher bandwidth—such as high-resolution or high-frame-rate AI vision tasks—a 4-lane configuration is also supported via an optional 20-pin connector.
<br/>

## 2.1 MIPI CSI
CSI stands for Camera Serial Interface, a standard interface defined by the MIPI Alliance for connecting camera modules to host processors. It enables high-speed, low-power transmission of image data from the camera to the processor.  
As explained above, the AI-G board provides a 2-lane CSI connection by default, with optional support for a 4-lane configuration via a 20-pin connector for higher data throughput.  

**NOTE**: Currently, the AI-G board supports only the ArduCam (5MP) and Raspberry Pi v1 Camera (5MP) modules.

### 2.1.1 Ardu Cam
ArduCam is a versatile camera module designed for embedded systems and AI applications. It supports various image sensors and interfaces, including MIPI CSI, making it suitable for integration with development boards like the AI-G.  
The AI-G board supports ArduCam modules with 2-lane or 4-lane MIPI CSI interfaces, enabling stable image input for AI vision tasks such as object detection and image classification. Thanks to its compatibility with FFC cables, the ArduCam module can be easily connected to the AI-G board's CSI connector, offering a reliable solution for real-time camera input in edge AI systems.

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

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20AI-G/Available%20Applications/Figure%201.%20arducam.png" width="400"></p>
<p align="center"><strong>Figure 1. Ardu cam </strong></p>

#### Step 1. Connect Ardu cam to AI-G MIPI CSI
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20AI-G/Available%20Applications/Figure%202.%20Connecting%20Cam%20to%20AI-G.png" width="500"></p>
<p align="center"><strong>Figure 2. Connecting the ArduCam to AI-G </strong></p> 

#### Step 2. Verifying MIPI CSI Connection on AI-G Board
To check if the ardu cam is properly connected to the AI-G board, enter the following command and check.  
```
$ dmesg | grep -i "ov5647"
```

**NOTE**: Connect the cam and power up the board, or if it is already powered up, reboot is required after connecting the cam.

### 2.1.2 Raspberry Pi v1 Cam
The Raspberry Pi Camera Module v1 is a compact 5MP camera developed by the Raspberry Pi Foundation. It is based on the OmniVision OV5647 image sensor and connects to the host board via a MIPI CSI-2 interface using an FFC (Flat Flexible Cable).  
Originally designed for the Raspberry Pi series, this module is also compatible with the AI-G board via the 15-pin MIPI CSI connector. It provides a reliable solution for entry-level camera applications such as image capture, video streaming, and AI-powered computer vision tasks on the AI-G platform.

Below are the specifications for the Raspberry pi v1 cam module.

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

You can test the pi cam by following the steps below:

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20AI-G/Available%20Applications/Figure%203.%20raspv1cam.png" width="400"></p>
<p align="center"><strong>Figure 3. Raspberry pi v1 cam </strong></p>

#### Step 1. Connect pi v1 cam to AI-G MIPI CSI
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20AI-G/Available%20Applications/Figure%202.%20Connecting%20Cam%20to%20AI-G.png" width="500"></p>
<p align="center"><strong>Figure 4. Connecting the Raspberry pi v1 cam to AI-G </strong></p> 

#### Step 2. Verifying MIPI CSI Connection on AI-G Board
To check if the pi cam is properly connected to the AI-G board, enter the following command and check.  
```
$ dmesg | grep -i "ov5647"
```

**NOTE**: Connect the cam and power up the board, or if it is already powered up, reboot is required after connecting the cam.

# 3. Video Output
The AI-G board supports video output through a MIPI DSI2 interface.
It provides a 2-lane DSI connection via a 15-pin FFC connector, suitable for connecting to compatible MIPI DSI LCD panels. This interface enables smooth rendering of graphical user interfaces, video playback, and real-time AI visualization on embedded displays.

## 3.1 MIPI DSI
DSI stands for Display Serial Interface, a standard defined by the MIPI Alliance for transmitting display data from the processor to an external screen. It enables high-speed, low-power communication suitable for embedded LCD panels.  
As mentioned above, the AI-G board provides a 2-lane DSI connection via a 15-pin FFC connector, allowing connection to compatible MIPI DSI display modules for GUI rendering, video playback, or real-time inference visualization.

### 3.1.1 5 Inch DSI Display
The Elecrow 5 Inch DSI Display is an 800×480 resolution LCD with an IPS panel and capacitive touch support, designed for use with the Raspberry Pi’s MIPI DSI interface. Thanks to its plug-and-play functionality, no additional driver installation is required. The display connects to the AI-G board via the 15-pin MIPI DSI connector and is powered directly through the interface, eliminating the need for an external power supply.  
This module is suitable for GUI-based applications, real-time monitoring, and interactive AI demos on the AI-G platform.

Below are the specifications for the DSI Display.

| Spec                | Description                                |
| ------------------- | -------------------------------------------|
| Display Size        | 5 inch                                     |
| Resolution          | 800 x 480                                  |
| Refresh Rate        | 60 Hz                                      |
| Interface (Display) | MIPI DSI                                   |
| Interface (Panel)   | RGB888 Port                                |
| Operating Voltage   | 3.3 V                                      |
| Operating Temp Range| -20 °C to 70 °C                            |
| Cable Type          | FFC (15-pin)                               |
| Compatibility       | Raspberry Pi, AI-G (via MIPI DSI interface)|

You can test the pi cam by following the steps below:

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20AI-G/Available%20Applications/Figure%205.%20display.png" width="400"></p>
<p align="center"><strong>Figure 5. 5 inch DSI Display </strong></p>

#### Step 1. Connect Display to AI-G MIPI DSI
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20AI-G/Available%20Applications/Figure%206.%20Connecting%20Display%20to%20AI-G.png" width="500"></p>
<p align="center"><strong>Figure 6. Connecting the Display to AI-G </strong></p> 

#### Step 2. Verifying MIPI DSI Connection on AI-G Board
To check if the display is properly connected to the AI-G board, enter the following command and check.  
```
$ --------------------------------
```

# 4. NN Inference Applications


# 5. 40 Pin GPIO Header
The AI-G board features a 40-pin GPIO header, providing flexible I/O capabilities for various hardware projects.
This header is compatible with general-purpose input/output (GPIO) operations and can be used to connect sensors, LEDs, buttons, and other peripheral devices.

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20AI-G/Available%20Applications/3.1%2040%20Pin%20GPIO%20Header%20Pinmap%20of%20AI-G.png" width="600"></p>
<p align="center"><strong>Figure 3.1 40 Pin GPIO Header Pinmap of AI-G  </strong></p>
Each pin supports digital I/O, I2C, SPI, or UART functionality depending on the configuration.
<br/><br/>

**Note**: Please refer to the official pinout diagram for detailed pin functions and voltage levels before connecting external hardware.
<br/>

## 5.1 GPIO Digital In/Out
The AI-G board supports digital input and output (GPIO) through its 40-pin header, enabling users to interact with external devices such as buttons, LEDs, sensors. 

### 5.1.1 LED
One of the simplest and most common GPIO output examples is controlling an LED.  
To demonstrate digital output, an LED can be connected to one of the GPIO pins on the 40 pin header. In this example, the LED's cathode (short leg) is connected to the GND pin on the AI-G board, while the anode (long leg) is directly connected to GPIO72.

#### Step 1. Hardware Requirements
- TOPST AI-G board (x1)
- Breadboard (x1)
- LED (x1)
- male to female jumper wire (x2)
- DC 5V Power Adapter (x1)
- USB to TTL Serial Cable (x1)

#### Step 2. Example Circuit
- LED
    - (+) pin connected to pin 26 on the TOPST AI-G board.
    - (-) pin connected to pin 14 which acts as GND on the TOPST AI-G board.  

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20AI-G/Available%20Applications/3.1.1%20AI-G%20GPIO%20LED%20Circuit%20Schematic.png" width="600"></p>
<p align="center"><strong>Figure 3.1.1 AI-G GPIO LED Circuit Schematic  </strong></p>

##### Step 2.1 Pin Mapping
The following table shows pin mapping.

<p align="center"><strong>Table 2.1 Pin Mapping of AI-G LED</strong></p>
<table align="center">
    <tr>
        <th colspan="3">Pin Name</th>
        <th>AI-G Board</th>
        <th>GPIO</th>
    </tr>
    <tr>
        <td colspan="3">LED (+) pin</td>
        <td>26</td>
        <td>72</td>
    </tr>
</table>

#### Step 3. How to execute
To operate the LED connected to GPIO72 on the AI-G board, simply run the following code:

```bash
#!/bin/bash

GPIO=72
INTERVAL=1

# GPIO export
if [ ! -e /sys/class/gpio/gpio$GPIO ]; then
    echo "$GPIO" > /sys/class/gpio/export
    sleep 0.1
fi

echo "out" > /sys/class/gpio/gpio$GPIO/direction

trap "echo $GPIO > /sys/class/gpio/unexport; echo -e '\nGPIO$GPIO unexported. Exit.'; exit" SIGINT

echo "Toggling GPIO$GPIO every $INTERVAL second(s). Press Ctrl+C to stop."

while true; do
    echo 1 > /sys/class/gpio/gpio$GPIO/value
    sleep $INTERVAL
    echo 0 > /sys/class/gpio/gpio$GPIO/value
    sleep $INTERVAL
done
```

#### Step 4. Execution Result
This script configures GPIO72 as a digital output and continuously toggles its state every 1 second. When executed, the LED connected to GPIO72 will blink repeatedly-turning on for 1 second and then off for 1 second in an infinite loop.
<br/>

To stop the script, press 'Ctrl+C'.  
When the script is terminated, GPIO72 will be automatically unexported and cleaned up.  
> Make sure to give the script execute permission before running:
> ```bash
> $ chmod +x AI_GPIO_LED_TEST
> $ ./AI_GPIO_LED_TEST
> ```
<br/>

**NOTE**: This setup does not include a current-limiting resistor. While it may work for short-term testing, it is recommended to use a resistor in series with the LED to avoid potential damage to the GPIO pin.

### 5.1.2 Button
A push button is a basic input device commonly used to demonstrate digital input handling through GPIO.  
In this example, one side of the button is connected to a 3.3V power pin on the AI-G board, while the other side is connected to GPIO79. When the button is pressed, GPIO79 reads a HIGH signal 1.

#### Step 1. Hardware Requirements
- TOPST AI-G board (x1)
- Breadboard (x1)
- Button (x1)
- male to female jumper wire (x2)
- DC 5V Power Adapter (x1)
- USB to TTL Serial Cable (x1)

#### Step 2. Example Circuit
- Button switch
    - One leg of the button switch is connected to pin 22 on the TOPST AI-G board.
    - The opposite leg above the button is connected to the 3.3V pin.  

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20AI-G/Available%20Applications/3.1.2%20AI-G%20GPIO%20Button%20Circuit%20Schematic.png" width="600"></p>
<p align="center"><strong>Figure 3.1.2 AI-G GPIO Button Circuit Schematic  </strong></p>

##### Step 2.1 Pin Mapping
The following table shows pin mapping.

<p align="center"><strong>Table 2.1 Pin Mapping of AI-G Button</strong></p>
<table align="center">
    <tr>
        <th colspan="3">Pin Name</th>
        <th>AI-G Board</th>
        <th>GPIO</th>
    </tr>
    <tr>
        <td colspan="3">One leg pin of button</td>
        <td>22</td>
        <td>79</td>
    </tr>
</table>

#### Step 3. How to execute
To monitor the button input connected to GPIO79 on the AI-G board, simply run the following code:

```bash
#!/bin/bash

GPIO=79

# GPIO export
if [ ! -e /sys/class/gpio/gpio$GPIO ]; then
    echo "$GPIO" > /sys/class/gpio/export
    sleep 0.1
fi

echo "in" > /sys/class/gpio/gpio$GPIO/direction

trap "echo $GPIO > /sys/class/gpio/unexport; echo -e '\nGPIO$GPIO unexported. Exit.'; exit" SIGINT

echo "Monitoring GPIO$GPIO for button press..."
echo "Press Ctrl+C to stop."

PREV_VALUE=0

while true; do
    VALUE=$(cat /sys/class/gpio/gpio$GPIO/value)
    if [ "$VALUE" = "1" ] && [ "$PREV_VALUE" = "0" ]; then
        echo "Button pressed (value: 1)"
    fi
    PREV_VALUE=$VALUE
    sleep 0.1
done
```

#### Step 4. Execution Result
This script configures GPIO79 as a digital input and continuously monitors its value in real time.  
When executed, pressing the button connected to GPIO79 will print a message indicating that the button has been pressed.
<br/>

To stop the script, press 'Ctrl+C'.  
When the script is terminated, GPIO79 will be automatically unexported and cleand up.
> Make sure to give the script execute permission before running:
> ```bash
> $ chmod +x AI_GPIO_BUTTON_TEST
> $ ./AI_GPIO_BUTTON_TEST
> ```
<br/>

**Note:** GPIO72 and GPIO79 are used here as examples. You may use any available GPIO pin on the AI-G board based on the 40-pin header pinmap. Make sure to refer to the official pinout diagram and select a GPIO number that suits your hardware configuration.

## 5.2 I2C
The AI-G board provides I2C communication through the 40-pin GPIO header, allowing it to interface with various peripherals such as sensors, displays, and expansion modules.  
I2C (Inter-Integrated Circuit) is a two-wire communication protocol consisting of a data line (SDA) and a clock line (SCL), enabling multiple devices to communicate over a shared bus.

I2C communication follows a master-slave architecture, where one master device controls the communication and up to 127 slave devices can be connected on the same bus.  
The SDA line is used for both transmitting and receiving data, while the SCL line synchronizes the timing of data transfer. This synchronous communication model allows devices to exchange information in a coordinated, clock-driven manner.

### 5.2.1 1602A LCD Display
The 1602A LCD is a character display module commonly used in embedded systems.  
On the AI-G board, the LCD's SDA and SCL lines can be connected to GPIO pins configured for I2C. Once connected, the LCD can be controlled using the Linux I2C tools or custom software.

#### Step 1. Hardware Requirements
- TOPST AI-G board (x1)
- 1602A LCD Display (x1)
- female to female jumper wire (x4)
- DC 5V Power Adapter (x1)
- USB to TTL Serial Cable (x1)

#### Step 2. Example Circuit
- LCD1602A
    - VCC pin of the LCD1602A is connected to the 5V pin on the TOPST AI-G board.
    - GND pin of the LCD1602A is connected to GND on the TOPST AI-G board.
    - SDA pin of the LCD1602A is connected to pin 3 on the TOPST AI-G board.
    - SCL pin of the LCD1602A is connected to pin 5 on the TOPST AI-G board.  

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20AI-G/Available%20Applications/3.2.1%20AI-G%20I2C%20LCD Display%20Circuit%20Schematic.png" width="600"></p>
<p align="center"><strong>Figure 3.2.1 AI-G I2C LCD Display Circuit Schematic  </strong></p>

##### Step 2.1 Pin Mapping
The following table shows pin mapping.

<p align="center"><strong>Table 2.1 Pin Mapping of AI-G LCD Display</strong></p>
<table align="center">
    <tr>
        <th colspan="3">Pin Name</th>
        <th>AI-G Board</th>
        <th>GPIO</th>
    </tr>
    <tr>
        <td colspan="3">GND</td>
        <td>6</td>
        <td>GND</td>
    </tr>
    <tr>
        <td colspan="3">VCC</td>
        <td>4</td>
        <td>5V</td>
    </tr>
    <tr>
        <td colspan="3">SDA</td>
        <td>3</td>
        <td>103</td>
    </tr>
    <tr>
        <td colspan="3">SCL</td>
        <td>5</td>
        <td>102</td>
    </tr>
</table>

#### Step 3. How to execute
To access I2C devices on the AI-G board, you need to write a C program using the i2c-dev interface and cross-compile it for the target architecture.  
Below is a simple example (I2C_TEST.c):

```
#include <stdio.h>
#include <stdlib.h>
#include <fcntl.h>
#include <linux/i2c-dev.h>
#include <sys/ioctl.h>
#include <unistd.h>

#define I2C_DEV "/dev/i2c-1"
#define I2C_ADDR 0x27

// RS: 0 = command, 1 = data
void lcd_send_byte(int fd, unsigned char data, unsigned char mode) {
    unsigned char high = mode | (data & 0xF0) | 0x08; // backlight on
    unsigned char low  = mode | ((data << 4) & 0xF0) | 0x08;
    unsigned char buf[4] = { high | 0x04, high, low | 0x04, low }; // toggle EN bit

    for (int i = 0; i < 4; i++) {
        if (write(fd, &buf[i], 1) != 1) {
            perror("I2C write error");
        }
        usleep(1000); // 1ms delay
    }
}

void lcd_command(int fd, unsigned char cmd) {
    lcd_send_byte(fd, cmd, 0x00);
}

void lcd_data(int fd, unsigned char data) {
    lcd_send_byte(fd, data, 0x01);
}

void lcd_init(int fd) {
    usleep(50000); // wait for LCD power on
    lcd_command(fd, 0x33); // init
    lcd_command(fd, 0x32); // 4-bit mode
    lcd_command(fd, 0x28); // 2 line, 5x8 font
    lcd_command(fd, 0x0C); // display on, cursor off
    lcd_command(fd, 0x06); // entry mode
    lcd_command(fd, 0x01); // clear display
    usleep(2000);
}

void lcd_print(int fd, const char* str) {
    while (*str) {
        lcd_data(fd, *str++);
    }
}

int main() {
    int fd = open(I2C_DEV, O_RDWR);
    if (fd < 0) {
        perror("Failed to open I2C device");
        return 1;
    }

    if (ioctl(fd, I2C_SLAVE, I2C_ADDR) < 0) {
        perror("Failed to set I2C address");
        close(fd);
        return 1;
    }

    lcd_init(fd);
    lcd_print(fd, "test pass!");

    close(fd);
    return 0;
}
```
##### Step 3.1 Install Toolchain(gcc-arm-9.2)
To build binaries for the ARM 64-bit (AArch64) architecture, especially in embedded Linux environments, you need a cross-compilation toolchain.
This step installs the GCC ARM 9.2 toolchain for AArch64.

```
$ wget https://developer.arm.com/-/media/Files/downloads/gnu-a/9.2-2019.12/binrel/gcc-arm-9.2-2019.12-x86_64-aarch64-none-linux-gnu.tar.xz

$ tar -xvf gcc-arm-9.2-2019.12-x86_64-aarch64-none-linux-gnu.tar.xz

$ echo "export PATH=~/gcc-arm-9.2-2019.12-x86_64-aarch64-none-linux-gnu/bin:\$PATH" >> ~/.bashrc
$ source ~/.bashrc

$ aarch64-none-linux-gnu-gcc --version
aarch64-none-linux-gnu-gcc (GNU Toolchain for the A-profile Architecture 9.2-2019.12 (arm-9.10)) 9.2.1 20191025
Copyright (C) 2019 Free Software Foundation, Inc.
This is free software; see the source for copying conditions.  There is NO
warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
```

##### Step 3.2 Cross-Compile the I2C_TEST.c Source File for AArch64
Prepare the cross-compilation toolchain for the AI-G board, then compile the program using the following command:

```
$ aarch64-none-linux-gnu-gcc -o I2C_TEST I2C_TEST.c
$ ls
I2C_TEST.c I2C_TEST
```
##### Step 3.3 Transfer and Execute the program on the AI-G Board
After cross-compiling the binary on your host system, transfer it to the AI-G board and execute it using the following commands:

```
$ scp I2C_TEST root@192.168.0.100:/home/root/
```

On the AI-G board
```
$ chmod + x I2C_TEST
$ ./I2C_TEST
```

#### Step 4. Execution Result
This program initializes the 1602A I2C LCD Display and prints a test message via the I2C interface on the AI-G board. When executed, the message "test pass!" will appear on the LCD screen.  
If the message does not appear, please check the following:
- Ensure the SDA and SCL pins are correctly connected.
- Confirm the I2C device address matches your LCD module.
- Check that power (5V, GND) is properly supplied.

## 5.3 SPI
The AI-G board supports SPI (Serial Peripheral Interface) communication through a 40-pin GPIO header, enabling data exchange between external devices and the board.  

SPI is a synchronous serial communication protocol that enables full-duplex communication - meaning data can be transmitted and received simultaneously. It uses four main lines: MOSI (Master Out Slave In), MISO (Master In Slave Out), SCLK (Serial Clock), and SS (Slave Select).

Unlike I2C, which uses shared lines for multiple devices, SPI requires a dedicated SS line for each slave device. This one-to-many structure makes SPI fast and straightforward to implement, but it can require more physical wiring when multiple devices are involved.

### 5.3.1 Dot Matrix
8x8 dot matrix display is commonly used for simple text or pattern output in embedded systems. On the AI-G board, the dot matrix module can be controlled via SPI using a driver chip such as the MAX7219.

The MAX7219 handles row and column scanning internally, allowing the microcontroller to control the entire display using only a few SPI signals: MOSI (DIN), SCLK and, CS (LOAD). Once connected, the display can be controlled using SPI communication through user-defined scripts or libraries.

#### Step 1. Hardware Requirements
- TOPST AI-G board (x1)
- 8x8 Dot Matrix
- female to female jumper wire (x5)
- DC 5V Power Adapter (x1)
- USB to TTL Serial Cable (x1)

#### Step 2. Example Circuit
- 8x8 Dot Matrix
    - VCC pin of the 8x8 Dot Matrix is connected to the 5V pin on the TOPST AI-G board.
    - GND pin of the 8x8 Dot Matrix is connected to the GND on the TOPST AI-G board.
    - DIN pin of the 8x8 Dot Matrix is connected to the 19 pin on the TOPST AI-G board.
    - CS pin of the 8x8 Dot Matrix is connected to the 24 pin on the TOPST AI-G board.
    - CLK pin of the 8x8 Dot Matrix is connected to the 23 pin on the TOPST AI-G board.

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20AI-G/Available%20Applications/3.3.1%20AI-G%20SPI%20Dot Matrix%20Circuit%20Schematic.png" width="600"></p>
<p align="center"><strong>Figure 3.3.1 AI-G SPI Dot Matrix Circuit Schematic  </strong></p>

##### Step 2.1 Pin Mapping
The following table shows pin mapping.

<p align="center"><strong>Table 2.1 Pin Mapping of AI-G Dot Matrix</strong></p>
<table align="center">
    <tr>
        <th colspan="3">Pin Name</th>
        <th>AI-G Board</th>
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
        <td>94</td>
    </tr>
    <tr>
        <td colspan="3">CS</td>
        <td>24</td>
        <td>93</td>
    </tr>
    <tr>
        <td colspan="3">CLK</td>
        <td>23</td>
        <td>92</td>
    </tr>
</table>

#### Step 3. How to execute
To communicate with SPI devices on the AI-G board, you need to write a C program using the spidev interface and cross-compile it for the target architecture.  
Below is a simple example (SPI_TEST.c) that sends data to a MAX7219 LED matrix display:

```
#include <stdio.h>
#include <stdint.h>
#include <fcntl.h>
#include <unistd.h>
#include <linux/spi/spidev.h>
#include <sys/ioctl.h>
#include <string.h>

#define SPI_DEV "/dev/spidev3.0"

int spi_fd = -1;

void spi_send(uint8_t address, uint8_t data) {
    uint8_t tx[2] = { address, data };
    struct spi_ioc_transfer tr = {
        .tx_buf = (uintptr_t)tx,
        .rx_buf = 0,
        .len = 2,
        .delay_usecs = 0,
        .speed_hz = 1000000,
        .bits_per_word = 8,
    };

    if (ioctl(spi_fd, SPI_IOC_MESSAGE(1), &tr) < 1) {
        perror("SPI send failed");
    }
}

void max7219_init() {
    spi_send(0x09, 0x00); // Decode mode off
    spi_send(0x0A, 0x08); // Brightness (0x00 ~ 0x0F)
    spi_send(0x0B, 0x07); // Scan limit: display all 8 digits
    spi_send(0x0C, 0x01); // Shutdown register: normal operation
    spi_send(0x0F, 0x00); // Display test: off
}

void max7219_clear() {
    for (int i = 1; i <= 8; i++) {
        spi_send(i, 0x00);
    }
}


const uint8_t letter_P[8] = {
    0b00000000,  
    0b01111110, 
    0b01000010,  
    0b01000010,  
    0b01111110,  
    0b01000000,  
    0b01000000,  
    0b01000000   
};


void draw_letter_P() {
    for (int row = 0; row < 8; row++) {
        spi_send(row + 1, letter_P[row]);
    }
}

int main() {
    spi_fd = open(SPI_DEV, O_RDWR);
    if (spi_fd < 0) {
        perror("Failed to open SPI device");
        return 1;
    }

    max7219_init();
    max7219_clear();
    draw_letter_P();

    close(spi_fd);
    return 0;
}


```
##### Step 3.1 Install Toolchain(gcc-arm-9.2)
To build binaries for the ARM 64-bit (AArch64) architecture, especially in embedded Linux environments, you need a cross-compilation toolchain.
This step installs the GCC ARM 9.2 toolchain for AArch64.
```
$ wget https://developer.arm.com/-/media/Files/downloads/gnu-a/9.2-2019.12/binrel/gcc-arm-9.2-2019.12-x86_64-aarch64-none-linux-gnu.tar.xz

$ tar -xvf gcc-arm-9.2-2019.12-x86_64-aarch64-none-linux-gnu.tar.xz

$ echo "export PATH=~/gcc-arm-9.2-2019.12-x86_64-aarch64-none-linux-gnu/bin:\$PATH" >> ~/.bashrc
$ source ~/.bashrc

$ aarch64-none-linux-gnu-gcc --version
aarch64-none-linux-gnu-gcc (GNU Toolchain for the A-profile Architecture 9.2-2019.12 (arm-9.10)) 9.2.1 20191025
Copyright (C) 2019 Free Software Foundation, Inc.
This is free software; see the source for copying conditions.  There is NO
warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
```

##### Step 3.2 Cross-Compile the SPI_TEST.c Source File for AArch64
Prepare the cross-compilation toolchain for the AI-G board, then compile the program using the following command:

```
$ aarch64-none-linux-gnu-gcc -o SPI_TEST SPI_TEST.c
$ ls
SPI_TEST.c SPI_TEST
```

##### Step 3.3 Transfer and Execute the program on the AI-G Board
After cross-compiling the binary on your host system, transfer it to the AI-G board and execute it using the following commands:

```
$ scp SPI_TEST root@192.168.0.100:/home/root/
```

On the AI-G board
```
$ chmod + x SPI_TEST
$ ./SPI_TEST
```

#### Step 4. Execution Result
This program initializes the MAX7219 LED dot matrix display and sends data over the SPI interface to render the character P on the display. When execution, the 8x8 LED matrix should display the letter P based on the predefined bit pattern.  
If nothing appears or the pattern is distorted, please check the following:
- Verify correct wiring for SPI pins (MOSI, SCK, CS).
- Confirm the MAX7219 module is powered properly (5V, GND) and all data/clock lines are stable.

## 5.4 UART
The AI-G board supports UART (Universal Asynchronous Receiver/Transmitter) communication through its 40-pin GPIO header, enabling serial communication with devices such as serial consoles, and other microcontrollers.  

UART is a widely used asynchronous communication protocol that transmits data one bit at a time over two lines: TX (transmit) and RX (receive). Unlike I2C or SPI, UART does not use a clock line. Instead, the two devices must use a common communication speed for timing.

### 5.4.1 UART Loopback Test
UART loopback test is a simple way to verify that UART communications is functioning correctly on the AI-G board.  
By connecting the TX and RX pins together, any data sent from the board will be immediately received back.  
This test can be performed using the Linux terminal by writing data to the UART device and reading it back.

#### Step 1. Hardware Requirements
- TOPST AI-G board (x1)
- female to female jumper wire (x1)
- DC 5V Power Adapter (x1)
- USB to TTL Serial Cable (x1)

#### Step 2. Example Circuit
**Wiring:** Connect TX <-> RX

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20AI-G/Available%20Applications/3.4.1%20AI-G%20UART%20Circuit%20Schematic.png" width="600"></p>
<p align="center"><strong>Figure 3.4.1 AI-G UART Circuit Schematic  </strong></p>

##### Step 2.1 Pin Mapping
The following table shows pin mapping.

<p align="center"><strong>Table 2.1 Pin Mapping of AI-G UART</strong></p>
<table align="center">
    <tr>
        <th colspan="2">Pin Name</th>
        <th>AI-G Board</th>
    </tr>
    <tr>
        <td colspan="2">TX</td>
        <td>10</td>
    </tr>
        <tr>
        <td colspan="2">RX</td>
        <td>8</td>
    </tr>
</table>

#### Step 3. How to execute
This script sends a test message to the UART port and checks if the same message is received back.  
To test UART loopback on the AI-G board, simply run the following script after connecting the TX and RX pins together.

```bash
#!/bin/bash
# ===================== user setting =====================
UART_DEV="/dev/ttyAMA1"       # uart
BAUD=115200                   # Baudrate
TEST_MSG="Hello from UART"    # msg
TEMP_FILE="/tmp/uart_rx.txt"  # file
# =====================================================

if [ ! -e "$UART_DEV" ]; then
    echo "Error: $UART_DEV does not exist"
    exit 1
fi

chmod 666 $UART_DEV

stty -F $UART_DEV $BAUD cs8 -cstopb -parenb -icanon -echo -ixon -ixoff
echo "UART setup compete: port=$UART_DEV, speed=$BAUD"

cat $UART_DEV > $TEMP_FILE &
RX_PID=$!

sleep 0.2
echo -n "$TEST_MSG" > $UART_DEV
echo "Transmission complete: \"$TEST_MSG\""

sleep 1
kill $RX_PID 2>/dev/null

if [ -f "$TEMP_FILE" ]; then
    RECEIVED=$(cat $TEMP_FILE)
    rm $TEMP_FILE
    if [ "$RECEIVED" = "$TEST_MSG" ]; then
        echo "Loopback Success! Received Message: \"$RECEIVED\""
    else
        echo "Received mismatch"
        echo "Sent: \"$TEST_MSG\""
        echo "Received: \"$RECEIVED\""
    fi
else
    echo "Failed to receive: No received file"
fi
```

#### Step 4. Execution Result
This script configures the specified UART port and sends a test message. If the TX and RX pins are correctly connected, the same message will be received back and printed to the terminal, confirming that UART transmission and reception are working properly.

> Make sure to give the script execute permission before running:
> ```bash
> chmod +x AI_UART_LOOPBACK_TEST
> ./AI_UART_LOOPBACK_TEST
> ```
<br/>

# 6. Storage Connection
This chapter covers how to connect the AI-G board to various storage devices.
Supported storage options include external storage via PCIe.

## 6.1 SATA HDD

to be continue

## 6.2 NVME M.2 SSD
#### Step 1. Connect the SSD
- NVMe SSD (M.2 PCIe): Insert the NVMe M.2 SSD into the AI-G board’s PCIe slot. 
<br/>
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20AI-G/Available%20Applications/4.2.1%20AI-G%20NVME%20M.2%20SSD%20connection.png" width="300"></p>
<p align="center"><strong>Figure 4.2.1 AI-G NVME M.2 SSD connection  </strong></p>

#### Step 2. Boot the AI-G Board
After executing the reboot command, observe the boot log to verify that the PCIe device is recognized by the system.
Look for messages such as telechips-pcie: Link up, which indicate that the PCIe link has been successfully established.

```
$ reboot
...
Starting kernel ...

[    1.207844] telechips-pcie 12000000.pcie: invalid resource
[    1.232395] telechips-pcie 12000000.pcie: Link up
[    1.521983] debugfs: Directory '18300000.dma' with parent 'dmaengine' already present!
[    1.531159] debugfs: Directory '18310000.dma' with parent 'dmaengine' already present!
[    1.540282] debugfs: Directory '18320000.dma' with parent 
...
ai-g-topst login: 
```
#### Step 3. Check SSD Recognition

```
root@ai-g-topst:~# lspci
00:00.0 PCI bridge: Synopsys, Inc. Device 750b (rev 01)
01:00.0 Non-Volatile memory controller: Silicon Motion, Inc. SM2263EN SM2263XT SSD Controller (rev 03)
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

Filesystem            Size  Used Avail Use% Mounted on
devtmpfs              426M     0  426M   0% /dev
/dev/mmcblk0p4        330M  201M  103M  67% /
tmpfs                 100M     0  100M   0% /dev/shm
tmpfs                 274M  8.6M  265M   4% /run
tmpfs                 4.0M     0  4.0M   0% /sys/fs/cgroup
tmpfs                 684M     0  684M   0% /tmp
tmpfs                 684M   12K  684M   1% /var/volatile
tmpfs                 137M     0  137M   0% /run/user/0
/dev/nvme0n1p1        117G   24K  111G   1% /mnt/nvme
```

</br></br>

# 7. Ethernet Connection
The TOPST AI-G board supports Ethernet connectivity through its onboard RJ45 Ethernet port. This allows the board to communicate with local networks or the internet using standard TCP/IP protocols. Ethernet is commonly used for deploying AI applications that require remote access, data streaming, or software updates.

## 7.1 Network Connection Via Router
This method connects the AI-G board to a local network using a standard router. The board can obtain an IP address automatically via DHCP or be configured with a static IP address.

### 7.1.1 Remount the Root Filesystem as Read/Write
root filesystem is mounted as read-only, remount it with write permissions to allow editing configuration files:

```
$ mount -o remount,rw /
```
### 7.1.2 Create the Network Configuration File
Create or edit the /etc/systemd/network/20-wired.network file with the following content to enable DHCP on the eth0 interface

```
$ vi /etc/systemd/network/20-wired.network
 
[Match]
Name=eth0
 
[Network]
DHCP=yes
 
```

This configuration instructs systemd-networkd to use DHCP for the eth0 interface.

### 7.1.3 Restart the Network Service
Apply the new network configuration by restarting the systemd-networkd service:

```
sudo systemctl restart systemd-networkd
```
 
### 7.1.4 Verify Network Connectivity
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20AI-G/Available%20Applications/ethernet4.png" width="400"></p>
<p align="center"><strong>Network Connection Via Router</strong></p>

Test the internet connection by pinging Google's public DNS server:

```
$ ping 8.8.8.8
PING 8.8.8.8 (8.8.8.8): 56 data bytes
64 bytes from 8.8.8.8: seq=0 ttl=113 time=30.208 ms
64 bytes from 8.8.8.8: seq=1 ttl=113 time=38.143 ms
64 bytes from 8.8.8.8: seq=2 ttl=113 time=30.969 ms
64 bytes from 8.8.8.8: seq=3 ttl=113 time=33.586 ms
 
```

## 7.2 Nework Sharing with the Host PC
You can share your PC's internet connection with the TOPST AI-G board without using a router by utilizing the Internet Connection Sharing (ICS) feature available in Windows operating systems.

### 7.2.1 Host PC Network Configuration
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
 
### 7.2.2 Remount the Root Filesystem as Read/Write
root filesystem is mounted as read-only, remount it with write permissions to allow editing configuration files:

```
$ mount -o remount,rw /
```
 
### 7.2.3 Create the Network Configuration File
Create or edit the /etc/systemd/network/20-wired.network file with the following content to enable DHCP on the eth0 interface

```
$ vi /etc/systemd/network/20-wired.network
 
[Match]
Name=eth0
 
[Network]
DHCP=yes
```

This configuration instructs systemd-networkd to use DHCP for the eth0 interface.
 
### 7.2.4 Restart the Network Service
Apply the new network configuration by restarting the systemd-networkd service:

```
sudo systemctl restart systemd-networkd
```
 
### 7.2.5 Verify Network Connectivity
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20AI-G/Available%20Applications/ethernet5.png" width="400"></p>
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

# 8. JTAG Connection
# 9. CAN Connection
