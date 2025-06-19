# 1. Introduction
---
This document provides guidelines on using the VCP-G with FreeRTOS. It includes configuration instructions and example codes to help you easily develop embedded applications by using the VCP-G under the FreeRTOS environment.

Specifically, this document provides guidance on FreeRTOS-based example applications for the VCP-G, including: 
- Digital Out/In
- SPI
- I2C
- UART
- PWM
- Additional Example

Refer to Figure 1.1 before using the VCP-G.
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/vcp-g%20pinout%20Diagram.png"></p>
<p align="center"><strong>Figure 1.1 VCP-G Pinout Diagram</strong></p>
</br>

To run each example, you should modify the `main.c` file located at:
```
$ ~/vcp/sources/app.sample/app.base/main.c
```
After making the necessary changes, compile the project by using the provided Makefile to generate the firmware binary.
</br></br></br></br>

# 2. Digital In/Out
---
This chapter provides examples of controlling LEDs by using the digital pins of the VCP-G board. In VCP-G, digital pins are used to send or receive binary signals (HIGH or LOW), making them essential for controlling components like LEDs, switches, and sensors. 

This chapter contains two example projects that demonstrate how to control LEDs and button by using digital outputs and inputs, giving you a basic understanding of digital pin functions.
</br></br></br>

## 2.1 Digital Out
>!(정정필요)! vcp4LED로 수정해야 하나요? (아래 figure 및 table 모두 vcp4LED)
---
This example demonstrates how to control LEDs on a breadboard by using the VCP-G board under FreeRTOS.  
You can find the relevant source file at:  

```
$ ~/vcp/sources/app.sample/app.base/main.c
```
>!(정정필요)! VCP-G FreeRTOS SDK 설치에 대한 내용을 읽기 위해 VCP-G FreeRTOS SDK Getting Started을 참고하라는 문구 추가 필요

To implement this example, modify the main.c file to configure the GPIO pins connected to the LEDs as digital outputs. A FreeRTOS task should be created to turn on four LEDs one by one in order, then turn them off in reverse order. Each LED transition should include a 500 ms delay to clearly observe the sequence.
</br></br>

### 2.1.1 Hardware Reqirements  
- VCP-G board (x1)
- Breadboard (x1)
- LED (x4)
- 12V 1A Power Adapter (x1)
- USB Type-C to A Cable (x1) 
- Male to male jumper wire (x9)
</br></br>

### 2.1.2 Circuit
- LED01
    - (+) pin is connected to pin 7 on the VCP-G board.
    - (–) pin is connected to the GND rail on the breadboard.
- LED02
    - (+) pin is connected to pin 6 on the VCP-G board.
    - (–) pin is connected to the GND rail on the breadboard.
- LED03
    - (+) pin is connected to pin 5 on the VCP-G board.
    - (–) pin is connected to the GND rail on the breadboard.
- LED04
    - (+) pin is connected to pin 4 on the VCP-G board.
    - (–) pin is connected to the GND rail on the breadboard. 

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/F_digital_out.png" width="600"></p>
<p align="center"><strong>Figure 2.1 vcp4LED Circuit Schematic</strong></p>

#### 2.1.2.1 Pin Mapping
The following table shows pin mapping.

<p align="center"><strong>Table 2.1 Pin Mapping of vcp4LED</strong></p>
<div align="center">	
	<table>
		<tr>
			<th colspan="3">Pin Name</th>
	        <th>VCP-G Board</th>
	        <th>GPIO</th>
	    </tr>
	    <tr>
	        <td colspan="3">LED01 (+) pin</td>
	        <td>7</td>
	        <td>B[01]</td>
	    </tr>
	        <tr>
	        <td colspan="3">LED02 (+) pin</td>
	        <td>6</td>
	        <td>A[13]</td>
	    </tr>
	        <tr>
	        <td colspan="3">LED03 (+) pin</td>
	        <td>5</td>
	        <td>B[10]</td>
	    </tr>
	        <tr>
	        <td colspan="3">LED04 (+) pin</td>
	        <td>4</td>
	        <td>B[27]</td>
	    </tr>
	</table>
</div>
</br></br>

### 2.1.3 How to execute
To run this example, modify **Main_StartTask()** in the main.c file as shown.
```
#include <gpio.h>
static void Main_StartTask(void * pArg)
{
    (void)pArg;
    (void)SAL_OsInitFuncs();

    uint32 led_pins[4] = {
        GPIO_GPB(1),
        GPIO_GPA(13),
        GPIO_GPB(10),
        GPIO_GPB(27)
    };

    for (int i = 0; i < 4; i++) {
        GPIO_Config(led_pins[i], (GPIO_FUNC(0) | GPIO_OUTPUT));
        GPIO_Set(led_pins[i], 1); 
    }

    while (1) {
        for (int i = 0; i < 4; i++) {
            GPIO_Set(led_pins[i], 0); 
            SAL_TaskSleep(500);
        }
        for (int i = 3; i >= 0; i--) {
            GPIO_Set(led_pins[i], 1); 
            SAL_TaskSleep(500);
        }
    }
}
```
After editing the code, go to the following directory and run the build command:  
```
$ cd ~/vcp/build/tcc70xx/gcc
$ make
```
This generates a firmware image and uses the ***FWDN*** tool to flash the generated image to the VCP-G.  
After the code is successfully flashed and executed, the four connected LEDs turn on sequentially from LED01 to LED04, then turn off in reverse order. Each transition occurs with a 500 ms delay, creating a smooth blinking pattern.
</br></br></br>

## 2.2 Digital In
>!(정정필요)! vcp4LED_Button으로 수정해야 하나요?
---
This example demonstrates how to read input from a push button and use it to control an LED by using the VCP-G board under FreeRTOS.
The relevant source file can be found at:
``` 
$ ~/vcp/sources/app.sample/app.base/main.c
```
To implement this example, modify main.c to configure one GPIO pin as a digital input (connected to a button) and four GPIO pins as digital outputs (connected to LEDs).  
A FreeRTOS task continuously monitors the button state and when the button is pressed, LED1 and LED3 turn on.
When the button is not pressed, LED2 and LED4 turn on instead.
</br></br>

### 2.2.1 Hardware Requirements
- VCP-G Board (x1)
- Breadboard (x1)
- LED (x4)
- Button switch (sensor) (x1)
- 12V 1A Power Adapter (x1)
- USB Type-C to A Cable (x1)
- Male to male jumper wire (x11)
</br></br>

### 2.2.2 Circuit
- LED01
    - (+) pin is connected to pin 7 on the VCP-G board.
    - (–) pin is connected to the GND rail on the breadboard.
- LED02
    - (+) pin is connected to pin 6 on the VCP-G board.
    - (–) pin is connected to the GND rail on the breadboard.
- LED03
    - (+) pin is connected to pin 5 on the VCP-G board.
    - (–) pin is connected to the GND rail on the breadboard.
- LED04
    - (+) pin is connected to pin 4 on the VCP-G board.
    - (–) pin is connected to the GND rail on the breadboard. 
- Button switch
    - One leg of the button switch is connected to pin 2 on the VCP-G board.
    - The diagonally opposite leg of the button is connected to the power rail on the breadboard.

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/F_digital_in.png" width="600"></p>
<p align="center"><strong>Figure 2.2 vcp4LED_Button Circuit Schematic</strong></p>

#### 2.2.2.1 Pin Mapping
The following table shows pin mapping.

<p align="center"><strong>Table 2.2 Pin Mapping of vcp4LED_Button</strong></p>
<div align="center">
	<table>
	    <tr>
	        <th colspan="3">Pin Name</th>
	        <th>VCP-G Board</th>
	        <th>GPIO</th>
	    </tr>
	    <tr>
	        <td colspan="3">LED01 (+) pin</td>
	        <td>7</td>
	        <td>B[01]</td>
	    </tr>
	        <tr>
	        <td colspan="3">LED02 (+) pin</td>
	        <td>6</td>
	        <td>A[13]</td>
	    </tr>
	        <tr>
	        <td colspan="3">LED03 (+) pin</td>
	        <td>5</td>
	        <td>B[10]</td>
	    </tr>
	        <tr>
	        <td colspan="3">LED04 (+) pin</td>
	        <td>4</td>
	        <td>B[27]</td>
	    </tr>
	    </tr>
	        <tr>
	        <td colspan="3">one leg pin of button</td>
	        <td>2</td>
	        <td>B[28]</td>
	    </tr>
	</table>
</div>
</br></br>

### 2.2.3 How to execute
To run this example, modify **Main_StartTask()** in the main.c file as shown.
```
#include <gpio.h>
static void Main_StartTask(void *pArg)
{
    (void)pArg;
    SAL_OsInitFuncs();

    uint32 led_pins[4] = {
        GPIO_GPB(1),   
        GPIO_GPA(13),  
        GPIO_GPB(10),  
        GPIO_GPB(27)   
    };

    uint32 btn_pin = GPIO_GPB(28);   
    for (int i = 0; i < 4; i++) {
        GPIO_Config(led_pins[i], GPIO_FUNC(0) | GPIO_OUTPUT);
        GPIO_Set(led_pins[i], 0); 
    }

    GPIO_Config(btn_pin, GPIO_FUNC(0) | GPIO_INPUT | GPIO_INPUTBUF_EN | GPIO_PULLDN);

    while (1) {
        int btn = GPIO_Get(btn_pin);
        if (btn == 1) {
            GPIO_Set(led_pins[0], 1);  
            GPIO_Set(led_pins[1], 0);  
            GPIO_Set(led_pins[2], 1);  
            GPIO_Set(led_pins[3], 0);  
        } else {
            GPIO_Set(led_pins[0], 0);  
            GPIO_Set(led_pins[1], 1); 
            GPIO_Set(led_pins[2], 0);  
            GPIO_Set(led_pins[3], 1); 
        }
        SAL_TaskSleep(50);  
    }
}
```
After editing the code, go to the following directory and run the build command:  
```
$ cd ~/vcp/build/tcc70xx/gcc
$ make
```
This generates a firmware image and uses the ***FWDN*** tool to flash the generated image to the VCP-G.  
After the code is successfully flashed and executed, pressing the button turns on LED01 and LED03, while releasing the button turns on LED02 and LED04.
The system continuously monitors the button state and updates the LED status in real time with a 50 ms polling interval.
</br></br></br></br>

# 3. VCP-G I2C
---
This chapter provides instructions for configuring Inter-integrated Circuit (I2C) communication on the VCP-G running FreeRTOS.  
I2C is a two-wire, synchronous communication protocol designed for efficient data exchange between multiple devices. It operates with a serial data line (SDA) and a serial clock line (SCL), allowing multiple peripherals to communicate with a microcontroller using unique addresses. I2C supports both master-slave communication and multi-master configurations, making it ideal for connecting sensors, displays, and other low-speed devices while minimizing the number of required connections.
</br></br></br>

## 3.1 vcpI2C_LCD1602
---
This example program demonstrates how the VCP-G board controls an LCD1602 display by using the I2C communication protocol. The LCD1602 is a 16-character, 2-line liquid crystal display commonly used in embedded system projects. By utilizing the LiquidCrystal_I2C library, the board sends commands and data over the I2C bus to efficiently control the display.  
In this example, the LCD is initialized and the backlight is enabled for clear visibility. The program then positions the cursor to display the text "Hello TOPST" on the screen.
</br></br>

### 3.1.1 Hardware Requirements
- VCP-G Board (x1)
- LCD1602 (x1)
- 12V 1A Power Adapter (x1)
- USB Type-C to A Cable (x1)
- Male to female jumper wire (x4)
</br></br>

### 3.1.2 Circuit
- LCD1602
    - VCC pin of the LCD1602 is connected to the analog pin 5V on the VCP-G board.
    - GND pin of the LCD1602 is connected to GND on the VCP-G board.
    - SDA pin of the LCD1602 is connected to pin 7 on the VCP-G board.
    - SCL pin of the LCD1602 is connected to pin 8 on the VCP-G board.

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/F_i2c.png" width="600"></p>
<p align="center"><strong>Figure 3.1 vcpI2C_LCD1602 Circuit Schematic</strong></p>

#### 3.1.2.1 Pin Mapping
The following table shows pin mapping.

>!(정정필요)! AnalogInOutSerial이 아닌 vcpI2C_LCD1602 아닌지 확인 부탁드립니다
<p align="center"><strong>Table 3.1 Pin Mapping of AnalogInOutSerial</strong></p>
<div align="center">
	<table>
	    <tr>
	        <th colspan="3">Pin Name</th>
	        <th>VCP-G Board</th>
	        <th>GPIO</th>
	    </tr>
	    <tr>
	        <td colspan="3">LCD1602 VCC pin</td>
	        <td>5V</td>
	        <td>-</td>
	    </tr>
	        <tr>
	        <td colspan="3">LCD1602 GND pin</td>
	        <td>GND</td>
	        <td>-</td>
	    </tr>
	        <tr>
	        <td colspan="3">LCD1602 SDA pin</td>
	        <td>7</td>
	        <td>B[01]</td>
	    </tr>
	        <tr>
	        <td colspan="3">LED (-) pin</td>
	        <td>8</td>
	        <td>B[00]</td>
	    </tr>
	</table>
</div>
</br></br>

### 3.1.3 How to execute
To run this example, modify **Main_StartTask()** in the main.c file as shown.
```
#include <i2c.h>
#include <lcd.h>
static void Main_StartTask(void * pArg)
{
    {
        (void)pArg;
        SAL_OsInitFuncs();

        I2C_Init();
        if (I2C_Open(I2C_CH, I2C_PORT, I2C_SPEED, NULL, NULL) != SAL_RET_SUCCESS) {
            mcu_printf("I2C open failed\n");
            return;
        }
        uint32 detected_addr = I2C_ScanSlave(I2C_CH);
        mcu_printf("Detected I2C Slave Address: 0x%02X\n", detected_addr);

        lcd_init();
        lcd_cmd(0x80);
        lcd_print("Hello TOPST");
        while (1) {
            SAL_TaskSleep(1000);
        }
    }
}
```
#### Additional Configuration Notes
To enable LCD testing through I2C, follow these steps:  
**1. Enable lcd.c in the Build System**  
- Navigate to the following path:
```
$ vi ~/vcp/sources/dev.drivers/i2c/rules.mk
```
- Find the following line:
```
#SRCS += lcd.c
```
- Unannotate the line to activate the file:
```
SRCS += lcd.c
```
**2. Check or Modify LCD Function Logic**
If you need to inspect or edit the logic for LCD initialization, commands, or print functions, refer to:
```
$ vi ~/vcp/sources/dev.drivers/i2c/lcd.c
```
**3. Configure I2C Channel and Port**
The I2C channel number and associated port used by the LCD can be changed in:
```
$ vi ~/vcp/sources/dev.drivers/i2c/lcd.h
```

After editing the code, go to the following directory and run the following build command:  
```
$ cd ~/vcp/build/tcc70xx/gcc
$ make
```
This generates a firmware image and uses the ***FWDN*** tool to flash the generated image to the VCP-G.  
After the code is successfully flashed and executed, the LCD displays the message "Hello TOPST" on the screen, confirming that I2C communication is working properly.  
</br></br></br></br>

# 4. VCP SPI
---
This chapter provides instructions for configuring Serial Peripheral Interface (SPI) communication on the VCP-G.  
SPI is a high-speed, synchronous communication protocol used to exchange data between microcontrollers and peripherals. It operates with separate lines for data transmission (MOSI and MISO), clock synchronization (SCK), and device selection (SS), ensuring efficient and reliable communication.  
</br></br></br>

## 4.1 vcpSPI_Dot8x8
---
This example program demonstrates how the VCP-G board controls an 8x8 LED dot matrix using the MAX7219 driver via SPI.
In this example, a predefined binary array is used to display the letter "X" on the dot matrix. The display is updated through SPI communication, and the MAX7219 handles row and column control internally.
This example helps illustrate how to send data patterns over SPI to control external display devices like LED matrices.
</br></br>

### 4.1.1 Hardware Requirements
- VCP-G Board (x1)
- 8x8 Dot Matrix (x1)
- 12V 1A Power Adapter (x1)
- USB Type-C to A Cable (x1)
- Male to female jumper wire (x2)
- Female to female jumper wire (x3)
</br></br>

### 4.1.2 Circuit
- 8x8 Dot Matrix
    - VCC pin of the 8x8 Dot Matrix is connected to the analog pin 5V on the VCP-G board.
    - GND pin of the 8x8 Dot Matrix is connected to GND on the VCP-G board.
    - DIN pin of the 8x8 Dot Matrix is connected to SPI pin 4 on the VCP-G board.
    - CS pin of the 8x8 Dot Matrix is connected to SPI pin 5 on the VCP-G board.
    - CLS pin of the 8x8 Dot Matrix is connected to SPI pin 3 on the VCP-G board.

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/F_spi.png" width="600"></p>
<p align="center"><strong>Figure 4.1 vcpSPI_Dot8x8 Circuit Schematic</strong></p>

#### 4.1.2.1 Pin Mapping
The following table shows pin mapping.

<p align="center"><strong>Table 4.1 Pin Mapping of vcpSPI_Dot8x8</strong></p>
<div align="center">
	<table>
	    <tr>
	        <th colspan="3">Pin Name</th>
	        <th>VCP-G Board</th>
	        <th>GPIO</th>
	    </tr>
	    <tr>
	        <td colspan="3">8x8 Dot Matrix VCC pin</td>
	        <td>5V</td>
	        <td>-</td>
	    </tr>
	        <tr>
	        <td colspan="3">8x8 Dot Matrix GND pin</td>
	        <td>GND</td>
	        <td>-</td>
	    </tr>
	    <tr>
	        <td colspan="3">8x8 Dot Matrix DIN pin</td>
	        <td>SPI 4</td>
	        <td>B[06]</td>
	    </tr>
	    <tr>
	        <td colspan="3">8x8 Dot Matrix CS pin</td>
	        <td>SPI 5</td>
	        <td>B[05]</td>
	    </tr>
	    <tr>
	        <td colspan="3">8x8 Dot Matrix CLK pin</td>
	        <td>SPI 3</td>
	        <td>B[04]</td>
	    </tr>
	</table>
</div>
</br></br>

### 4.1.3 How to execute
To run this example, simply modify the `Main_StartTask()` function in the `main.c` file as shown below.
```
#include <dot_matrix.h>
static void Main_StartTask(void * pArg)
{
    {
        (void)pArg;
        SAL_OsInitFuncs();
   
        mcu_printf("[MAX7219] Init Start\n");
        MAX7219_Init();
        SAL_TaskSleep(200);
        MAX7219_XPattern();
   
        while (1) {
            SAL_TaskSleep(1000);
        }
    }
}
```
#### Additional Configuration Notes
To enable Dot Matrix testing via SPI, follow these steps:  
**1. Enable dot_matrix.c in the Build System**  
- Navigate to the following path:
```
$ vi ~/vcp/sources/dev.drivers/gpsb/rules.mk
```
- Locate the line:
```
#SRCS += dot_matrix.c
```
- Unannotate to activate the file:
```
SRCS += dot_matrix.c
```
**2. Check or Modify Dot Matrix Function Logic**  
If you need to inspect or edit the logic for Dot Matrix initialization, control commands, or display patterns, refer to:
```
$ vi ~/vcp/sources/dev.drivers/gpsb/dot_matrix.c
```
**3. Configure SPI Channel and GPIOs**  
The SPI channel and associated GPIO pins used by the Dot Matrix can be configured in:
```
$ vi ~/vcp/sources/dev.drivers/gpsb/dot_matrix.h
```
After editing the code, go to the following directory and run the build command:  
```
$ cd ~/vcp/build/tcc70xx/gcc
$ make
```
This will generate a firmware image and use the FWDN tool to flash the generated image to the VCP-G.  
Once the code is successfully flashed and executed, the 8x8 LED dot matrix will display the letter "X", confirming that SPI communication with the MAX7219 driver is working correctly. 
</br></br></br></br>

# 5. VCP-G UART
---
This chapter provides instructions for configuring Universal Asynchronous Receiver-Transmitter (UART) communication on the VCP-G.  
UART is a widely used serial communication protocol that transmits data asynchronously using only two lines: Transmit (TX) and Receive (RX). It is essential for exchanging data between microcontrollers, sensors, and computers without requiring a shared clock signal.  
The following chapters describe how to send and receive data through UART.
</br></br></br>

## 5.1 Uart Communication Test (FT232BL)
---
This example demonstrates how to verify UART communication on the VCP-G board using the FT232BL USB to TTL serial module.
The UART TX and RX pins of the VCP-G board are connected to the FT232BL module, which is in turn connected to a PC via USB.
A terminal program such as MobaXterm is used on the PC to view the transmitted messages.
</br></br>

### 5.1.1 Hardware Requirements
- VCP-G Board (x1)
- FT232BL USB to TTL serial module (x1)
- mini USB Cable (x1)
- 12V 1A Power Adapter (x1)
- USB Type-C to A Cable (x1)
- Male to female jumper wire (x2)
</br></br>

### 5.1.2 Circuit
- FT232BL
    - The RXD pin of the FT232BL module is connected to pin 18 (TXD) on the VCP-G board.
    - The TXD pin of the FT232BL module is connected to pin 19 (RXD) on the VCP-G board.

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/F_uart.png" width="600"></p>
<p align="center"><strong>Figure 5.1 vcpUART Circuit Schematic</strong></p>

#### 5.1.2.1 Pin Mapping
The following table shows pin mapping.

<p align="center"><strong>Table 4.1 Pin Mapping of vcpSPI_Dot8x8</strong></p>
<div align="center">
	<table>
	    <tr>
	        <th colspan="3">Pin Name</th>
	        <th>VCP-G Board</th>
	        <th>GPIO</th>
	    </tr>
	    <tr>
	        <td colspan="3">FT232BL RXD</td>
	        <td>18</td>
	        <td>A[28]</td>
	    </tr>
	        <tr>
	        <td colspan="3">FT232BL TXD</td>
	        <td>19</td>
	        <td>A[29]</td>
	    </tr>
	</table>
</div>
</br></br>

### 5.1.3 How to execute
To run this example, simply modify the `Main_StartTask()` function in the `main.c` file as shown below.
```
#include <uart_example.h>
void Main_StartTask(void *pArg)
{
    (void)pArg;
    (void)SAL_OsInitFuncs();

    UART_Test();

    while (1) {
        SAL_TaskSleep(1000);
    }
}
```
#### Additional Configuration Notes
To enable UART testing, follow these steps:  
**1. Enable uart_example.c in the Build System**  
- Navigate to the following path:
```
$ vi ~/vcp/sources/dev.drivers/uart/rules.mk
```
- Locate the line:
```
#SRCS += uart_example.c
```
- Unannotate to activate the file:
```
SRCS += uart_example.c
```
**2. Check or Modify UART Function Logic**  
If you need to inspect or edit the logic for UART initialization, data transmission/reception, or interrupt handling, refer to:
```
$ vi ~/vcp/sources/dev.drivers/uart/tcc70xx/uart_example.c
```
**3. Configure UART Channel and GPIOs**  
The UART channel, baud rate, and associated TX/RX GPIO pins used for the UART test can be configured in:
```
$ vi ~/vcp/sources/dev.drivers/uart/uart_example.h
```
After editing the code, go to the following directory and run the build command:  
```
$ cd ~/vcp/build/tcc70xx/gcc
$ make
```
This will generate a firmware image and use the FWDN tool to flash the generated image to the VCP-G.  
Once the code is successfully flashed and executed, the message "[UART] Hello from UART!" will appear once on the serial terminal, confirming that UART transmission from the VCP-G board is working properly via the FT232BL USB to TTL module.
</br></br></br></br>

# 6. VCP-G PWM
---
This chapter provides instructions for configuring Pulse Width Modulation (PWM) on the VCP-G. PWM is a technique used to control the amount of power delivered to devices such as motors, LEDs, and buzzers by varying the duty cycle of a digital signal. It operates by switching the output pin on and off at a high frequency, where the ratio of on-time to the total period determines the effective output level. The following chapters describe how to generate PWM signals using FreeRTOS on the VCP-G and how to apply them to control external components.
</br></br></br>

## 6.1 pwmFade
---
This example program demonstrates how the VCP board controls an LED on the breadboard by gradually increasing and decreasing its brightness in a loop using PWM. When the brightness reaches its limits, the direction of fading reverses. The program continuously adjusts the LED's brightness, creating a fading effect.
</br></br>

### 6.1.1 Hardware Requirements
- VCP-G Board (x1)
- Breadboard (x1)
- LED (x1)
- 12V 1A Power Adapter (x1)
- USB Type-C to A Cable (x1)
- Male to male jumper wire (x2)
</br></br>

### 6.1.2 Circuit
- LED
    - (+) pin is connected to pin 45 on the VCP-G board.
    - (–) pin is connected to the GND rail on the breadboard.

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/F_pwm.png" width="600"></p>
<p align="center"><strong>Figure 5.1 vcpPWM Circuit Schematic</strong></p>

#### 6.1.2.1 Pin Mapping
The following table shows pin mapping.

<p align="center"><strong>Table 4.1 Pin Mapping of vcpSPI_Dot8x8</strong></p>
<div align="center">
	<table>
	    <tr>
	        <th colspan="3">Pin Name</th>
	        <th>VCP-G Board</th>
	        <th>GPIO</th>
	    </tr>
	    <tr>
	        <td colspan="3">LED</td>
	        <td>45</td>
	        <td>A[10]</td>
	    </tr>
	</table>
</div>
</br></br>

### 6.1.3 How to execute
To run this example, simply modify the `Main_StartTask()` function in the `main.c` file as shown below.
```
#include <gpio.h>
#include <pdm.h>
void Main_StartTask(void * pArg)
{
    PDMModeConfig_t pwm_cfg;
    uint32 duty_ns;
    uint32 wait_cnt;

    PDM_Init();

    pwm_cfg.mcPortNumber      = GPIO_PERICH_CH0;  // GPIO A10
    pwm_cfg.mcOperationMode   = PDM_OUTPUT_MODE_PHASE_1;
    pwm_cfg.mcInversedSignal  = 0;
    pwm_cfg.mcOutSignalInIdle = 0;
    pwm_cfg.mcLoopCount       = 0;
    pwm_cfg.mcOutputCtrl      = 0;

    pwm_cfg.mcPeriodNanoSec1  = 1000000; 
    pwm_cfg.mcDutyNanoSec2    = 0;
    pwm_cfg.mcPeriodNanoSec2  = 0;

    while (1)
    {
        // Fade-in
        for (duty_ns = 0; duty_ns <= pwm_cfg.mcPeriodNanoSec1; duty_ns += 10000)
        {
            pwm_cfg.mcDutyNanoSec1 = duty_ns;
            PDM_Disable(0, PMM_ON);
            wait_cnt = 0;
            while (PDM_GetChannelStatus(0))
            {
                SAL_TaskSleep(1); 
                wait_cnt++;
                if (wait_cnt > 100)
                {
                    mcu_printf("Timeout waiting for PDM to disable\n");
                    break;
                }
            }
            if (PDM_SetConfig(0, &pwm_cfg) != SAL_RET_SUCCESS)
            {
                mcu_printf("PDM_SetConfig failed\n");
                return;
            }
            if (PDM_Enable(0, PMM_ON) != SAL_RET_SUCCESS)
            {
                mcu_printf("PDM_Enable failed\n");
                return;
            }
            SAL_TaskSleep(10);
        }
        // Fade-out
        for (duty_ns = pwm_cfg.mcPeriodNanoSec1; duty_ns > 0; duty_ns -= 10000)
        {
            pwm_cfg.mcDutyNanoSec1 = duty_ns;

            PDM_Disable(0, PMM_ON);

            wait_cnt = 0;
            while (PDM_GetChannelStatus(0))
            {
                SAL_TaskSleep(1);
                wait_cnt++;
                if (wait_cnt > 100)
                {
                    mcu_printf("Timeout waiting for PDM to disable\n");
                    break;
                }
            }

            if (PDM_SetConfig(0, &pwm_cfg) != SAL_RET_SUCCESS)
            {
                mcu_printf("PDM_SetConfig failed\n");
                return;
            }
            if (PDM_Enable(0, PMM_ON) != SAL_RET_SUCCESS)
            {
                mcu_printf("PDM_Enable failed\n");
                return;
            }
            SAL_TaskSleep(10);
        }
    }
}
```
After editing the code, go to the following directory and run the build command:  
```
$ cd ~/vcp/build/tcc70xx/gcc
$ make
```
This will generate a firmware image and use the FWDN tool to flash the generated image to the VCP-G.  
Once the code is successfully flashed and executed, you will observe a gradual LED fade-in and fade-out effect driven by PWM on GPIO A10, confirming that the PDM-based PWM output from the VCP-G is functioning correctly.

**NOTE**: If you need to change the GPIO port used for PWM output, refer to the configuration in `pdm.c`.
</br></br></br></br>

# 7. Additional Examples
---
This chapter introduces additional sensor examples using FreeRTOS on the VCP-G board. It provides example guides on how to use commonly used Arduino sensors with freertos on the VCP-G board, helping users effectively integrate various sensors into their projects.
</br></br></br>

## 7.1 Infrared (IR) Sensor (Transceiver)
---
This example demonstrates how the VCP-G board controls an IR sensor and two LEDs on a breadboard. When the IR sensor detects an object (sensor value is LOW), the first LED turns on, and the second LED turns off. Conversely, when no object is detected (sensor value is HIGH), the second LED turns on while the first LED turns off. The presence or absence of an object is also printed to the serial monitor.
</br></br>

### 7.1.1 Hardware Requirements
- VCP-G Board (x1)
- Breadboard (x1)
- IR transceiver sensor (x1)
- LED (x2: Different colors are recommended)
- 12V 1A Power Adapter (x1)
- USB Type-C to A Cable (x1)
- Male to male jumper wire (x5)
- Male to female jumper wire (x3)
</br></br>

### 7.1.2 Circuit
- IR Transceiver sensor
    - OUT pin of the IR sensor is connected to pin 38 on the VCP-G board.
    - VCC pin of the IR sensor is connected to 5V on the VCP-G board.
    - GND pin of the IR sensor is connected to GND on the VCP-G board.
- LED01
    - (+) pin is connected to pin 16 on the VCP-G board.
    - (–) pin is connected to the GND rail on the breadboard.
- LED02
    - (+) pin is connected to pin 17 on the VCP-G board.
    - (–) pin is connected to the GND rail on the breadboard.

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/F_irsensor1.png" width="600"></p>
<p align="center"><strong>Figure 7.1 IR Transceiver Sensor Circuit Schematic</strong></p>

##### 7.1.2.1 Pin Mapping
The following table shows pin mapping.

<p align="center"><strong>Table 7.1 Pin Mapping of irSensor_LED</strong></p>
<div align="center">
	<table>
	    <tr>
	        <th colspan="3">Pin Name</th>
	        <th>VCP-G Board</th>
	        <th>GPIO</th>
	    </tr>
	    <tr>
	        <td colspan="3">IR Sensor OUT pin </td>
	        <td>38</td>
	        <td>K[13]</td>
	    </tr>
	        <tr>
	        <td colspan="3">IR Sensor VCC pin </td>
	        <td>5V</td>
	        <td>-</td>
	    </tr>
	    <tr>
	        <td colspan="3">IR Sensor GND pin</td>
	        <td>GND</td>
	        <td>-</td>
	    </tr>
	    <tr>
	        <td colspan="3">LED01 (+) pin</td>
	        <td>16</td>
	        <td>A[06]</td>
	    </tr>
	    <tr>
	        <td colspan="3">LED01 (-) pin</td>
	        <td>GND</td>
	        <td>-</td>
	    </tr>
	    <tr>
	        <td colspan="3">LED02 (+) pin</td>
	        <td>17</td>
	        <td>A[07]</td>
	    </tr>
	    <tr>
	        <td colspan="3">LED02 (-) pin </td>
	        <td>GND</td>
	        <td>-</td>
	    </tr>
	</table>
</div>
</br></br>

### 7.1.3 How to execute
To run this example, simply modify the `Main_StartTask()` function in the `main.c` file as shown below.
```
#include <gpio.h>
#define PIR_SENSOR_PIN   GPIO_GPK(13)
static void Main_StartTask(void * pArg)
{
    (void)pArg;
    (void)SAL_OsInitFuncs();

    GPIO_Config(PIR_SENSOR_PIN, GPIO_FUNC(0) | GPIO_INPUT | GPIO_INPUTBUF_EN | GPIO_PULLDN);
    GPIO_Config(GPIO_GPA(6), GPIO_FUNC(0) | GPIO_OUTPUT);  
    GPIO_Config(GPIO_GPA(7), GPIO_FUNC(0) | GPIO_OUTPUT);  

    while (1)
    {
        if (GPIO_Get(GPIO_GPK(13))) {
            mcu_printf("No\n");

            GPIO_Set(GPIO_GPA(6), 0); // LED1 OFF
            GPIO_Set(GPIO_GPA(7), 1); // LED2 ON
        } else {
            mcu_printf("Detected!\n");

            GPIO_Set(GPIO_GPA(6), 1); // LED1 ON
            GPIO_Set(GPIO_GPA(7), 0); // LED2 OFF
        }
        SAL_TaskSleep(500); 
    }
}
```
After editing the code, go to the following directory and run the build command:  
```
$ cd ~/vcp/build/tcc70xx/gcc
$ make
```
This will generate a firmware image and use the FWDN tool to flash the generated image to the VCP-G.  
Once the code is successfully flashed and executed, the IR sensor will detect the presence or absence of an object and control two LEDs accordingly. When an object is detected, the first LED turns on; when no object is detected, the second LED turns on. This behavior confirms that the IR sensor input and GPIO output on the VCP-G board are working properly.

**NOTE**: If you need to change the GPIO pins used for the IR sensor or LEDs, refer to the configuration section inside the source code.
</br></br></br>

## 7.2 Infrared (IR) Sensor (Receiver)
---
This example demonstrates how the VCP-G board uses an IR receiver sensor to detect signals from a remote control. When an IR signal is received, the onboard logic turns on an LED connected to the breadboard. This confirms that the IR receiver module is correctly decoding incoming signals, and the VCP-G is responding as expected. The reception status is also printed to the serial monitor.
</br></br>

### 7.2.1 Hardware Requirements
- VCP-G Board (x1)
- Breadboard (x1)
- IR Receiver sensor (x1)
- Arduino Remote (x1)
- LED (x1)
- 12V 1A Power Adapter (x1)
- USB Type-C to A Cable (x1)
- Male to male jumper wire (x5)
</br></br>

### 7.2.2 Circuit
- IR Receiver sensor
    - SIG pin of the IR sensor is connected to pin 40 on the VCP-G board.
    - GND pin of the IR sensor is connected to GND on the VCP-G board.
    - VCC pin of the IR sensor is connected to 5V on the VCP-G board.
- LED
    - (+) pin is connected to pin 7 on the VCP-G board.
    - (–) pin is connected to the GND rail on the breadboard.

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/F_irsensor2.png" width="600"></p>
<p align="center"><strong>Figure 7.2 IR Receiver Sensor Circuit Schematic</strong></p>

##### 7.2.2.1 Pin Mapping
The following table shows pin mapping.

<p align="center"><strong>Table 7.1 Pin Mapping of irSensor_LED</strong></p>
<div align="center">
	<table>
	    <tr>
	        <th colspan="3">Pin Name</th>
	        <th>VCP-G Board</th>
	        <th>GPIO</th>
	    </tr>
	    <tr>
	        <td colspan="3">IR Sensor SIG pin </td>
	        <td>40</td>
	        <td>K[11]</td>
	    </tr>
	        <tr>
	        <td colspan="3">IR Sensor GND pin </td>
	        <td>GND</td>
	        <td>-</td>
	    </tr>
	    <tr>
	        <td colspan="3">IR Sensor VCC pin</td>
	        <td>VCC</td>
	        <td>-</td>
	    </tr>
	    <tr>
	        <td colspan="3">LED (+) pin</td>
	        <td>7</td>
	        <td>B[01]</td>
	    </tr>
	    <tr>
	        <td colspan="3">LED (-) pin</td>
	        <td>GND</td>
	        <td>-</td>
	    </tr>
	</table>
</div>
</br></br>

### 7.2.3 How to execute
To run this example, simply modify the `Main_StartTask()` function in the `main.c` file as shown below.
```
#include <gpio.h>
#define PIR_SENSOR_PIN   GPIO_GPK(11)
static void Main_StartTask(void * pArg)
{
    (void)pArg;
    (void)SAL_OsInitFuncs();

    GPIO_Config(PIR_SENSOR_PIN, GPIO_FUNC(0) | GPIO_INPUT | GPIO_INPUTBUF_EN);
    GPIO_Config(GPIO_GPB(1), GPIO_FUNC(0) | GPIO_OUTPUT);

    uint32 prev_state = 0xFFFFFFFF;
    uint32 curr_state;

    while (1)
    {
        curr_state = GPIO_Get(PIR_SENSOR_PIN);
        if (curr_state != prev_state)
        {
            if (curr_state == 0)
            {
                mcu_printf("IR Signal Detected!\n");
                GPIO_Set(GPIO_GPB(1), 1);  // LED ON
            }
            else
            {
                GPIO_Set(GPIO_GPB(1), 0);  // LED OFF
            }
            prev_state = curr_state;
        }
        SAL_TaskSleep(50);
    }
}
```
After editing the code, go to the following directory and run the build command:  
```
$ cd ~/vcp/build/tcc70xx/gcc
$ make
```
This will generate a firmware image and use the FWDN tool to flash the generated image to the VCP-G.  
Once the code is successfully flashed and executed, the IR receiver detects signals from a remote control and turns on an LED for a short duration. This confirms that the VCP-G is correctly reading IR input and controlling the GPIO output in response to received signals.

**NOTE**: If you need to change the GPIO pins used for the IR sensor or LED, refer to the configuration section inside the source code.
</br></br></br>

## 7.3 Gas Sensor
---
This example demonstrates how the VCP-G board uses a Gas sensor (MQ 135) to detect various harmful gases in the air. It reads the analog value from a sensor connected to the analog pin on the VCP-G board, converts it to a voltage, and then prints it to the serial monitor with one decimal place.

**Note:** Gas Sensor (MQ-135) is a product of Winsen®. All rights to its design, trademark, and related intellectual property are owned by Winsen.
</br></br>

### 7.3.1 Hardware Requirements
- VCP-G Board (x1)
- Gas sensor (MQ135) (x1)
- 12V 1A Power Adapter (x1)
- USB Type-C to A Cable (x1)
- Male to female jumper wire (x3)
</br></br>

### 7.3.2 Circuit
- Gas sensor
    - A0 pin of the gas sensor is connected to the analog pin 55 on the VCP-G board. 
    - VCC pin of the gas sensor is connected to 5V on the VCP-G board.
    - GND pin of the gas sensor is connected to GND on the VCP-G board.


<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/F_gassensor.png" width="600"></p>
<p align="center"><strong>Figure 7.3 Gas Sensor Circuit Schematic</strong></p>

#### 7.3.2.1 Pin Mapping
The following table shows pin mapping.

<p align="center"><strong>Table 7.3 Pin Mapping of Gas Sensor</strong></p>
<div align="center">
	<table>
	    <tr>
	        <th colspan="3">Pin Name</th>
	        <th>VCP-G Board</th>
	        <th>GPIO</th>
	    </tr>
	    <tr>
	        <td colspan="3">Gas Sensor A0 pin</td>
	        <td>55</td>
	        <td>K[15]</td>
	    </tr>
	        <tr>
	        <td colspan="3">Gas Sensor VCC pin</td>
	        <td>5V</td>
	        <td>-</td>
	    </tr>
	    <tr>
	        <td colspan="3">Gas Sensor GND pin</td>
	        <td>GND</td>
	        <td>-</td>
	    </tr>
	</table>
</div>
</br></br>

### 7.3.3 How to execute
To run this example, simply modify the `Main_StartTask()` function in the `main.c` file as shown below.
```
#include <gpio.h>
#define GAS_SENSOR_PIN  GPIO_GPK(15)
static void Main_StartTask(void * pArg)
{
    (void)pArg;
    (void)SAL_OsInitFuncs();

    GPIO_Config(GAS_SENSOR_PIN, GPIO_FUNC(0) | GPIO_INPUT | GPIO_INPUTBUF_EN | GPIO_PULLUP);
    while (1)
    {
        if (GPIO_Get(GAS_SENSOR_PIN) == 0) 
            mcu_printf("Gas Detected!\n");
        else
            mcu_printf("Clean Air\n");
        SAL_TaskSleep(500); 
    }
}
```
After editing the code, go to the following directory and run the build command:  
```
$ cd ~/vcp/build/tcc70xx/gcc
$ make
```
This will generate a firmware image and use the FWDN tool to flash the generated image to the VCP-G.  
Once the code is successfully flashed and executed, the gas sensor continuously monitors the surrounding air quality. When gas is detected (sensor output is LOW), a message indicating gas detection is printed to the serial monitor; otherwise, it reports clean air. This confirms that the VCP-G is correctly reading digital input from the gas sensor.

**NOTE**: If you need to change the GPIO pin used for the gas sensor, refer to the configuration section inside the source code. Most gas sensor modules include a small adjustment screw (potentiometer) for sensitivity control. If the sensor does not respond reliably, try adjusting this screw to fine-tune the gas detection threshold.
</br></br></br>

## 7.4 Capacitive Touch Sensor
---
This example demonstrates how the VCP-G board interfaces with a capacitive touch sensor and controls an LED on a breadboard. The capacitive touch sensor detects physical contact from a finger by sensing changes in capacitance.  
When a touch is detected, the sensor outputs a digital HIGH signal to the VCP-G, which in turn turns on an LED. This example confirms that the touch input is correctly recognized and that the GPIO output responds accordingly. The touch detection status is also printed to the serial monitor.
</br></br>

### 7.4.1 Hardware Requirements
- VCP-G Board (x1)
- Breadboard (x1)
- Capacitive Touch sensor (x1)
- LED (x1)
- 12V 1A Power Adapter (x1)
- USB Type-C to A Cable (x1)
- Male to male jumper wire (x6)
</br></br>

### 7.4.2 Circuit
- Touch Sensor 
    - SIG pin of the Touch Sensor Module is connected to the pin 39 on the VCP-G board.
    - VCC pin of the Touch Sensor Module is connected to 5V on the VCP-G board.
    - GND pin of the Touch Sensor Module is connected to GND on the VCP-G board.
- LED
    - (+) pin of the LED is connected to pin 7 on the VCP-G board.
    - (–) pin of the LED is connected to the GND rail on the breadboard.

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/F_touchsensor.png" width="600"></p>
<p align="center"><strong>Figure 7.4 Touch Sensor Circuit Schematic</strong></p>

#### 7.4.2.1 Pin Mapping
The following table shows pin mapping.

<p align="center"><strong>Table 7.5 Pin Mapping of Touch Sensor</strong></p>
<div align="center">
	<table>
	    <tr>
	        <th colspan="3">Pin Name</th>
	        <th>VCP-G Board</th>
	        <th>GPIO</th>
	    </tr>
	    <tr>
	        <td colspan="3">Touch sensor SIG pin</td>
	        <td>39</td>
	        <td>K[12]</td>
	    </tr>
	        <tr>
	        <td colspan="3">Touch sensor VCC pin</td>
	        <td>5V</td>
	        <td>-</td>
	    </tr>
	    <tr>
	        <td colspan="3">Touch sensor GND pin</td>
	        <td>GND</td>
		    <td>-</td>
		</tr>
	    <tr>
	        <td colspan="3">LED (+) pin</td>
	        <td>7</td>
	        <td>B[01]</td>
	    </tr>
	    <tr>
	        <td colspan="3">LED (-) pin</td>
	        <td>GND</td>
	        <td>-</td>
	    </tr>
	</table>
</div>
</br></br>

### 7.4.3 How to execute
To run this example, simply modify the `Main_StartTask()` function in the `main.c` file as shown below.
```
#include <gpio.h>
#define TOUCH_SENSOR_PIN GPIO_GPK(12) 
void Main_StartTask(void * pArg)
{
    (void)pArg;
    (void)SAL_OsInitFuncs();

    GPIO_Config(TOUCH_SENSOR_PIN, GPIO_FUNC(0) | GPIO_INPUT | GPIO_INPUTBUF_EN | GPIO_PULLDN);
    GPIO_Config(GPIO_GPB(1), GPIO_FUNC(0) | GPIO_OUTPUT);

    while (1)
    {
        if (GPIO_Get(TOUCH_SENSOR_PIN)) {
            mcu_printf("Touch Detected!\n");
            GPIO_Set(GPIO_GPB(1), 1); // LED ON
        }
        else {
            mcu_printf("Not touched\n");
            GPIO_Set(GPIO_GPB(1), 0); // LED OFF
        }

        SAL_TaskSleep(300);
    }
}
```
After editing the code, go to the following directory and run the build command:  
```
$ cd ~/vcp/build/tcc70xx/gcc
$ make
```
This will generate a firmware image and use the FWDN tool to flash the generated image to the VCP-G.  
Once the code is successfully flashed and executed, the capacitive touch sensor monitors touch input from a human finger. When a touch is detected (sensor output is HIGH), a message is printed to the serial monitor and an LED is turned on. When no touch is detected, the LED is turned off. This confirms that the VCP-G is correctly reading input from the touch sensor and controlling GPIO output accordingly.

**NOTE**: If you need to change the GPIO pin used for the touch sensor or LED, refer to the configuration section inside the source code.
</br></br></br></br>

# 8. References
---
- Contact TOPST for more details: topst@topst.ai

**Note:** Reference documents can be provided whenever available, depending on the terms of a contract. If the reference
documents are unavailable, the contents directly related to your development can be guided.
