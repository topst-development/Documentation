# 1. 简介
---
本文档提供了在 FreeRTOS 环境下使用 VCP-G 的指南，其中包含配置说明和示例代码，帮助您在 FreeRTOS 环境下使用 VCP-G 轻松开发嵌入式应用程序。

具体而言，本文档提供了针对 VCP-G 的基于 FreeRTOS 的示例应用程序的指导，包括： 
- 数字输出/输入
- SPI
- I2C
- UART
- PWM
- Additional Example

使用 VCP-G 之前，请参阅图 1.1。
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/vcp-g%20pinout%20Diagram.png"></p>
<p align="center"><strong>图 1.1 VCP-G 引脚分布图</strong></p>
</br>

要运行每个示例，您需要修改位于以下路径的 `main.c` 文件：
```
$ ~/vcp/sources/app.sample/app.base/main.c
```
完成必要的修改后，使用提供的 Makefile 编译工程以生成固件二进制文件。
</br></br></br></br>

# 2. 数字输入/输出
---
本章提供使用 VCP-G 开发板的数字引脚控制 LED 的示例。在 VCP-G 中，数字引脚用于发送或接收二进制信号（HIGH 或 LOW），因此对于控制 LED、开关和传感器等元件至关重要。 

本章包含两个示例工程，演示如何使用数字输出和输入来控制 LED 和按钮，帮助您基本了解数字引脚的功能。
</br></br></br>

## 2.1 数字输出
---
本示例演示如何在 FreeRTOS 环境下使用 VCP-G 开发板控制面包板上的 LED。  
相关源文件位于：  

```
$ ~/vcp/sources/app.sample/app.base/main.c
```
在继续操作之前，请确认已正确安装 VCP-G FreeRTOS SDK。有关安装和设置说明，请参阅 VCP-G FreeRTOS SDK Getting Started 指南。

要实现本示例，请修改 main.c 文件，将连接到 LED 的 GPIO 引脚配置为数字输出。应创建一个 FreeRTOS 任务，按顺序逐个点亮四个 LED，然后按相反顺序熄灭它们。每次 LED 状态切换应包含 500 ms 的延时，以便清楚地观察整个过程。
</br></br>

### 2.1.1 硬件要求  
- VCP-G 开发板 (x1)
- 面包板 (x1)
- LED (x4)
- 12V 1A 电源适配器 (x1)
- USB Type-C 转 A 线缆 (x1) 
- 公对公跳线 (x9)
</br></br>

### 2.1.2 电路
- LED01
    - (+) 引脚连接到 VCP-G 开发板的 7 号引脚。
    - (–) 引脚连接到面包板上的 GND 排。
- LED02
    - (+) 引脚连接到 VCP-G 开发板的 6 号引脚。
    - (–) 引脚连接到面包板上的 GND 排。
- LED03
    - (+) 引脚连接到 VCP-G 开发板的 5 号引脚。
    - (–) 引脚连接到面包板上的 GND 排。
- LED04
    - (+) 引脚连接到 VCP-G 开发板的 4 号引脚。
    - (–) 引脚连接到面包板上的 GND 排。 

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/F_digital_out.png" width="600"></p>
<p align="center"><strong>图 2.1 vcp4LED 电路原理图</strong></p>

#### 2.1.2.1 引脚映射
下表显示了引脚映射。

<p align="center"><strong>表 2.1 vcp4LED 的引脚映射</strong></p>
<div align="center">	
	<table>
		<tr>
			<th colspan="3">引脚名称</th>
	        <th>VCP-G 开发板</th>
	        <th>GPIO</th>
	    </tr>
	    <tr>
	        <td colspan="3">LED01 (+) 引脚</td>
	        <td>7</td>
	        <td>B[01]</td>
	    </tr>
	        <tr>
	        <td colspan="3">LED02 (+) 引脚</td>
	        <td>6</td>
	        <td>A[13]</td>
	    </tr>
	        <tr>
	        <td colspan="3">LED03 (+) 引脚</td>
	        <td>5</td>
	        <td>B[10]</td>
	    </tr>
	        <tr>
	        <td colspan="3">LED04 (+) 引脚</td>
	        <td>4</td>
	        <td>B[27]</td>
	    </tr>
	</table>
</div>
</br></br>

### 2.1.3 执行方法
要运行本示例，请按如下所示修改 main.c 文件中的 **Main_StartTask()**。
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
编辑代码后，进入以下目录并运行构建命令：  
```
$ cd ~/vcp/build/tcc70xx/gcc
$ make
```
该操作会生成固件镜像，并使用 ***FWDN*** 工具将生成的镜像烧录到 VCP-G。  
代码成功烧录并运行后，连接的四个 LED 会从 LED01 到 LED04 依次点亮，然后按相反顺序熄灭。每次切换之间有 500 ms 的延时，形成平滑的闪烁效果。
</br></br></br>

## 2.2 数字输入
---
本示例演示如何在 FreeRTOS 环境下使用 VCP-G 开发板读取按钮的输入，并用它来控制 LED。
相关源文件位于：
``` 
$ ~/vcp/sources/app.sample/app.base/main.c
```
要实现本示例，请修改 main.c，将一个 GPIO 引脚配置为数字输入（连接到按钮），并将四个 GPIO 引脚配置为数字输出（连接到 LED）。  
FreeRTOS 任务会持续监测按钮状态，当按下按钮时，LED1 和 LED3 点亮。
当按钮未被按下时，则 LED2 和 LED4 点亮。
</br></br>

### 2.2.1 硬件要求
- VCP-G 开发板 (x1)
- 面包板 (x1)
- LED (x4)
- 按钮开关（传感器）(x1)
- 12V 1A 电源适配器 (x1)
- USB Type-C 转 A 线缆 (x1)
- 公对公跳线 (x11)
</br></br>

### 2.2.2 电路
- LED01
    - (+) 引脚连接到 VCP-G 开发板的 7 号引脚。
    - (–) 引脚连接到面包板上的 GND 排。
- LED02
    - (+) 引脚连接到 VCP-G 开发板的 6 号引脚。
    - (–) 引脚连接到面包板上的 GND 排。
- LED03
    - (+) 引脚连接到 VCP-G 开发板的 5 号引脚。
    - (–) 引脚连接到面包板上的 GND 排。
- LED04
    - (+) 引脚连接到 VCP-G 开发板的 4 号引脚。
    - (–) 引脚连接到面包板上的 GND 排。 
- 按钮开关
    - 按钮开关的一个引脚连接到 VCP-G 开发板的 2 号引脚。
    - 按钮对角线上的另一个引脚连接到面包板上的电源排。

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/F_digital_in.png" width="600"></p>
<p align="center"><strong>图 2.2 vcp4LED_Button 电路原理图</strong></p>

#### 2.2.2.1 引脚映射
下表显示了引脚映射。

<p align="center"><strong>表 2.2 vcp4LED_Button 的引脚映射</strong></p>
<div align="center">
	<table>
	    <tr>
	        <th colspan="3">引脚名称</th>
	        <th>VCP-G 开发板</th>
	        <th>GPIO</th>
	    </tr>
	    <tr>
	        <td colspan="3">LED01 (+) 引脚</td>
	        <td>7</td>
	        <td>B[01]</td>
	    </tr>
	        <tr>
	        <td colspan="3">LED02 (+) 引脚</td>
	        <td>6</td>
	        <td>A[13]</td>
	    </tr>
	        <tr>
	        <td colspan="3">LED03 (+) 引脚</td>
	        <td>5</td>
	        <td>B[10]</td>
	    </tr>
	        <tr>
	        <td colspan="3">LED04 (+) 引脚</td>
	        <td>4</td>
	        <td>B[27]</td>
	    </tr>
	    </tr>
	        <tr>
	        <td colspan="3">按钮的一个引脚</td>
	        <td>2</td>
	        <td>B[28]</td>
	    </tr>
	</table>
</div>
</br></br>

### 2.2.3 执行方法
要运行本示例，请按如下所示修改 main.c 文件中的 **Main_StartTask()**。
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
编辑代码后，进入以下目录并运行构建命令：  
```
$ cd ~/vcp/build/tcc70xx/gcc
$ make
```
该操作会生成固件镜像，并使用 ***FWDN*** 工具将生成的镜像烧录到 VCP-G。  
代码成功烧录并运行后，按下按钮会点亮 LED01 和 LED03，松开按钮则会点亮 LED02 和 LED04。
系统会持续监测按钮状态，并以 50 ms 的轮询间隔实时更新 LED 状态。
</br></br></br></br>

# 3. VCP-G I2C
---
本章介绍如何在运行 FreeRTOS 的 VCP-G 上配置 Inter-integrated Circuit (I2C) 通信。  
I2C 是一种两线制同步通信协议，专为在多个设备之间高效交换数据而设计。它通过一条串行数据线 (SDA) 和一条串行时钟线 (SCL) 工作，允许多个外围设备使用各自唯一的地址与微控制器通信。I2C 同时支持主从通信和多主机配置，因此非常适合在尽量减少所需连接数量的同时连接传感器、显示屏和其他低速设备。
</br></br></br>

## 3.1 vcpI2C_LCD1602
---
本示例程序演示 VCP-G 开发板如何使用 I2C 通信协议控制 LCD1602 显示屏。LCD1602 是一种 16 字符 2 行的液晶显示屏，常用于嵌入式系统项目中。通过使用 LiquidCrystal_I2C 库，开发板经由 I2C 总线发送命令和数据，从而高效地控制显示屏。  
在本示例中，先初始化 LCD 并开启背光以确保显示清晰。随后程序将光标定位，在屏幕上显示文本 "Hello TOPST"。
</br></br>

### 3.1.1 硬件要求
- VCP-G 开发板 (x1)
- LCD1602（x1）
- 12V 1A 电源适配器 (x1)
- USB Type-C 转 A 线缆 (x1)
- 公对母跳线（x4）
</br></br>

### 3.1.2 电路
- LCD1602
    - LCD1602 的 VCC 引脚连接到 VCP-G 开发板上的模拟引脚 5V。
    - LCD1602 的 GND 引脚连接到 VCP-G 开发板上的 GND。
    - LCD1602 的 SDA 引脚连接到 VCP-G 开发板的 7 号引脚。
    - LCD1602 的 SCL 引脚连接到 VCP-G 开发板的 8 号引脚。

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/F_i2c.png" width="600"></p>
<p align="center"><strong>图 3.1 vcpI2C_LCD1602 电路原理图</strong></p>

#### 3.1.2.1 引脚映射
下表显示了引脚映射。

<p align="center"><strong>表 3.1 vcpI2C_LCD1602 的引脚映射</strong></p>
<div align="center">
	<table>
	    <tr>
	        <th colspan="3">引脚名称</th>
	        <th>VCP-G 开发板</th>
	        <th>GPIO</th>
	    </tr>
	    <tr>
	        <td colspan="3">LCD1602 VCC 引脚</td>
	        <td>5V</td>
	        <td>-</td>
	    </tr>
	        <tr>
	        <td colspan="3">LCD1602 GND 引脚</td>
	        <td>GND</td>
	        <td>-</td>
	    </tr>
	        <tr>
	        <td colspan="3">LCD1602 SDA 引脚</td>
	        <td>7</td>
	        <td>B[01]</td>
	    </tr>
	        <tr>
	        <td colspan="3">LED (-) 引脚</td>
	        <td>8</td>
	        <td>B[00]</td>
	    </tr>
	</table>
</div>

</br></br>

### 3.1.3 执行方法
要运行本示例，请按如下所示修改 main.c 文件中的 **Main_StartTask()**。
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
#### 其他配置注意事项
要通过 I2C 启用 LCD 测试，请按以下步骤操作：  

**1. 在构建系统中启用 lcd.c**  
- 进入以下路径：
```
$ vi ~/vcp/sources/dev.drivers/i2c/rules.mk
```
- 找到以下行：
```
#SRCS += lcd.c
```
- 取消该行的注释以启用该文件：
```
SRCS += lcd.c
```

**2. 检查或修改 LCD 函数逻辑**  
如果需要查看或编辑 LCD 初始化、命令或打印函数的逻辑，请参阅：
```
$ vi ~/vcp/sources/dev.drivers/i2c/lcd.c
```

**3. 配置 I2C 通道和端口**  
LCD 所使用的 I2C 通道号及相关端口可在以下位置修改：
```
$ vi ~/vcp/sources/dev.drivers/i2c/lcd.h
```

编辑代码后，进入以下目录并运行以下构建命令：  
```
$ cd ~/vcp/build/tcc70xx/gcc
$ make
```
该操作会生成固件镜像，并使用 ***FWDN*** 工具将生成的镜像烧录到 VCP-G。  
代码成功烧录并运行后，LCD 屏幕上会显示消息 "Hello TOPST"，表明 I2C 通信工作正常。  
</br></br></br></br>

# 4. VCP SPI
---
本章介绍如何在 VCP-G 上配置 Serial Peripheral Interface (SPI) 通信。  
SPI 是一种高速同步通信协议，用于在微控制器与外围设备之间交换数据。它使用独立的信号线分别进行数据传输（MOSI 和 MISO）、时钟同步（SCK）和设备选择（SS），从而确保通信高效可靠。  
</br></br></br>

## 4.1 vcpSPI_Dot8x8
---
本示例程序演示 VCP-G 开发板如何通过 SPI 使用 MAX7219 驱动程序控制 8x8 LED 点阵。
在本示例中，使用预定义的二进制数组在点阵上显示字母“X”。显示内容通过 SPI 通信进行更新，MAX7219 在内部处理行和列的控制。
本示例有助于说明如何通过 SPI 发送数据模式，以控制 LED 点阵等外部显示设备。
</br></br>

### 4.1.1 硬件要求
- VCP-G 开发板 (x1)
- 8x8 点阵（x1）
- 12V 1A 电源适配器 (x1)
- USB Type-C 转 A 线缆 (x1)
- 公对母跳线 (x2)
- 母对母跳线 (x3)
</br></br>

### 4.1.2 电路
- 8x8 点阵屏
    - 8x8 点阵的 VCC 引脚连接到 VCP-G 开发板上的模拟引脚 5V。
    - 8x8 点阵的 GND 引脚连接到 VCP-G 开发板上的 GND。
    - 8x8 点阵的 DIN 引脚连接到 VCP-G 开发板的 SPI 引脚 4。
    - 8x8 点阵的 CS 引脚连接到 VCP-G 开发板的 SPI 引脚 5。
    - 8x8 点阵的 CLS 引脚连接到 VCP-G 开发板的 SPI 引脚 3。

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/F_spi.png" width="600"></p>
<p align="center"><strong>图 4.1 vcpSPI_Dot8x8 电路原理图</strong></p>

#### 4.1.2.1 引脚图
下表显示了引脚映射。

<p align="center"><strong>表 4.1 vcpSPI_Dot8x8 的引脚图</strong></p>
<div align="center">
	<table>
	    <tr>
	        <th colspan="3">引脚名称</th>
	        <th>VCP-G 开发板</th>
	        <th>GPIO</th>
	    </tr>
	    <tr>
	        <td colspan="3">8x8 点阵 VCC 引脚</td>
	        <td>5V</td>
	        <td>-</td>
	    </tr>
	        <tr>
	        <td colspan="3">8x8 点阵 GND 引脚</td>
	        <td>GND</td>
	        <td>-</td>
	    </tr>
	    <tr>
	        <td colspan="3">8x8 点阵 DIN 引脚</td>
	        <td>SPI 4</td>
	        <td>B[06]</td>
	    </tr>
	    <tr>
	        <td colspan="3">8x8 点阵 CS 引脚</td>
	        <td>SPI 5</td>
	        <td>B[05]</td>
	    </tr>
	    <tr>
	        <td colspan="3">8x8 点阵 CLK 引脚</td>
	        <td>SPI 3</td>
	        <td>B[04]</td>
	    </tr>
	</table>
</div>
</br></br>

### 4.1.3 执行方法
要运行本示例，请按如下所示修改 main.c 文件中的 **Main_StartTask()**。
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
#### 其他配置注意事项
要通过 SPI 启用点阵测试，请按以下步骤操作：  
**1. 在构建系统中启用 dot_matrix.c**  
- 进入以下路径：
```
$ vi ~/vcp/sources/dev.drivers/gpsb/rules.mk
```
- 找到以下行：
```
#SRCS += dot_matrix.c
```
- 取消注释以激活该文件：
```
SRCS += dot_matrix.c
```
**2. 检查或修改点阵功能逻辑**  
要检查或编辑点阵初始化、控制命令或显示模式的逻辑，请参阅以下源文件：
```
$ vi ~/vcp/sources/dev.drivers/gpsb/dot_matrix.c
```
**3. 配置 SPI 通道和 GPIO**  
点阵所使用的 SPI 通道及相关 GPIO 引脚可在以下头文件中配置：
```
$ vi ~/vcp/sources/dev.drivers/gpsb/dot_matrix.h
```
编辑代码后，进入以下目录并运行构建命令：  
```
$ cd ~/vcp/build/tcc70xx/gcc
$ make
```
该操作会生成固件镜像，并使用 ***FWDN*** 工具将生成的镜像烧录到 VCP-G。  
代码成功烧录并执行后，8x8 LED 点阵会显示字母“X”，确认与 MAX7219 驱动程序之间的 SPI 通信工作正常。 
</br></br></br></br>

# 5. VCP-G UART
---
本章介绍如何在 VCP-G 上配置 Universal Asynchronous Receiver-Transmitter (UART) 通信。  
UART 是一种广泛使用的串行通信协议，仅使用发送 (TX) 和接收 (RX) 两条线路异步传输数据。它对于在微控制器、传感器和计算机之间交换数据而无需共享时钟信号至关重要。  
以下各章介绍如何通过 UART 发送和接收数据。
</br></br></br>

## 5.1 UART 通信测试 (FT232BL)
---
本示例演示如何使用 FT232BL USB 转 TTL 串口模块验证 VCP-G 开发板上的 UART 通信。
VCP-G 开发板的 UART TX 和 RX 引脚连接到 FT232BL 模块，该模块再通过 USB 连接到 PC。
在 PC 上使用 MobaXterm 等终端程序查看发送的消息。
</br></br>

### 5.1.1 硬件要求
- VCP-G 开发板 (x1)
- FT232BL USB 转 TTL 串口模块 (x1)
- Mini USB 线 (x1)
- 12V 1A 电源适配器 (x1)
- USB Type-C 转 A 线缆 (x1)
- 公对母跳线 (x2)
</br></br>

### 5.1.2 电路
- FT232BL
    - FT232BL 模块的 RXD 引脚连接到 VCP-G 开发板的引脚 18 (TXD)。
    - FT232BL 模块的 TXD 引脚连接到 VCP-G 开发板的引脚 19 (RXD)。

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/F_uart.png" width="600"></p>
<p align="center"><strong>图 5.1 vcpUART 电路原理图</strong></p>

#### 5.1.2.1 引脚图
下表显示了引脚映射。

<p align="center"><strong>表 4.1 vcpUART 引脚图</strong></p>
<div align="center">
	<table>
	    <tr>
	        <th colspan="3">引脚名称</th>
	        <th>VCP-G 开发板</th>
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

### 5.1.3 执行方法
要运行本示例，请按如下所示修改 main.c 文件中的 **Main_StartTask()**。
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
#### 其他配置注意事项
要启用 UART 测试，请按以下步骤操作：  
**1. 在构建系统中启用 uart_example.c**  
- 进入以下路径：
```
$ vi ~/vcp/sources/dev.drivers/uart/rules.mk
```
- 找到以下行：
```
#SRCS += uart_example.c
```
- 取消注释以激活该文件：
```
SRCS += uart_example.c
```
**2. 检查或修改 UART 功能逻辑**  
要检查或编辑 UART 初始化、数据收发或中断处理的逻辑，请参阅以下源文件：
```
$ vi ~/vcp/sources/dev.drivers/uart/tcc70xx/uart_example.c
```
**3. 配置 UART 通道和 GPIO**  
UART 测试所使用的 UART 通道、波特率以及相关的 TX/RX GPIO 引脚可在以下头文件中配置：
```
$ vi ~/vcp/sources/dev.drivers/uart/uart_example.h
```
编辑代码后，进入以下目录并运行构建命令：  
```
$ cd ~/vcp/build/tcc70xx/gcc
$ make
```
该操作会生成固件镜像，并使用 ***FWDN*** 工具将生成的镜像烧录到 VCP-G。  
代码成功烧录并执行后，串口终端上会出现一次“[UART] Hello from UART!”消息，确认 VCP-G 开发板通过 FT232BL USB 转 TTL 模块进行的 UART 传输工作正常。
</br></br></br></br>

# 6. VCP-G PWM
---
本章介绍如何在 VCP-G 上配置脉宽调制 (PWM)。PWM 是一种通过改变数字信号的占空比来控制向电机、LED 和蜂鸣器等设备输送功率大小的技术。它以高频率开关输出引脚，导通时间与总周期之比决定了有效输出电平。后续章节介绍如何在 VCP-G 上使用 FreeRTOS 生成 PWM 信号，以及如何将其应用于控制外部元件。
</br></br></br>

## 6.1 pwmFade
---
本示例程序演示 VCP 开发板如何使用 PWM 循环地逐渐增强和减弱面包板上 LED 的亮度。LED 达到最大亮度后，其亮度开始下降。程序持续调节 LED 的亮度，从而产生渐变效果。
</br></br>

### 6.1.1 硬件要求
- VCP-G 开发板 (x1)
- 面包板 (x1)
- LED (x1)
- 12V 1A 电源适配器 (x1)
- USB Type-C 转 A 线缆 (x1)
- 公对公跳线（x2）
</br></br>

### 6.1.2 电路
- LED
    - (+) 引脚连接到 VCP-G 开发板的引脚 45。
    - (–) 引脚连接到面包板上的 GND 排。

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/F_pwm.png" width="600"></p>
<p align="center"><strong>图 5.1 pwmFade 电路原理图</strong></p>

#### 6.1.2.1 引脚图
下表显示了引脚映射。

<p align="center"><strong>表 4.1 pwmFade 引脚图</strong></p>
<div align="center">
	<table>
	    <tr>
	        <th colspan="3">引脚名称</th>
	        <th>VCP-G 开发板</th>
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

### 6.1.3 执行方法
要运行本示例，请按如下所示修改 main.c 文件中的 **Main_StartTask()**。
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
编辑代码后，进入以下目录并运行构建命令：  
```
$ cd ~/vcp/build/tcc70xx/gcc
$ make
```
该操作会生成固件镜像，并使用 ***FWDN*** 工具将生成的镜像烧录到 VCP-G。  
代码成功烧录并执行后，可以观察到由 GPIO A10 上的 PWM 驱动的 LED 逐渐淡入和淡出效果，确认 VCP-G 基于 PDM 的 PWM 输出功能正常。

**注意**：要更改用于 PWM 输出的 GPIO 端口，请参阅 pdm.c 文件中的配置。
</br></br></br></br>

# 7. 附加示例
---
本章介绍在 VCP-G 开发板上使用 FreeRTOS 的其他传感器示例。它提供了在 VCP-G 开发板上通过 FreeRTOS 使用常见 Arduino 传感器的示例指南，使您能够有效地将各种传感器集成到项目中。
</br></br></br>

## 7.1 红外 (IR) 传感器（收发器）
---
本示例演示 VCP-G 开发板如何控制面包板上的 IR 传感器和两个 LED。当 IR 传感器检测到物体时（传感器值为 LOW），第一个 LED 点亮，第二个 LED 熄灭。反之，当未检测到物体时（传感器值为 HIGH），第二个 LED 点亮，第一个 LED 熄灭。是否存在物体也会打印到串口监视器上。
</br></br>

### 7.1.1 硬件要求
- VCP-G 开发板 (x1)
- 面包板 (x1)
- IR 收发传感器 (x1)
- LED (x2：建议使用不同颜色)
- 12V 1A 电源适配器 (x1)
- USB Type-C 转 A 线缆 (x1)
- 公对公跳线 (x5)
- 公对母跳线 (x3)
</br></br>

### 7.1.2 电路
- IR 收发传感器
    - IR 传感器的 OUT 引脚连接到 VCP-G 开发板的引脚 38。
    - IR 传感器的 VCC 引脚连接到 VCP-G 开发板上的 5V。
    - IR 传感器的 GND 引脚连接到 VCP-G 开发板上的 GND。
- LED01
    - (+) 引脚连接到 VCP-G 开发板的引脚 16。
    - (–) 引脚连接到面包板上的 GND 排。
- LED02
    - (+) 引脚连接到 VCP-G 开发板的引脚 17。
    - (–) 引脚连接到面包板上的 GND 排。

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/F_irsensor1.png" width="600"></p>
<p align="center"><strong>图 7.1 红外 (IR) 传感器电路原理图</strong></p>

##### 7.1.2.1 引脚图
下表显示了引脚映射。

<p align="center"><strong>表 7.1 irSensor_LED 的引脚图</strong></p>
<div align="center">
	<table>
	    <tr>
	        <th colspan="3">引脚名称</th>
	        <th>VCP-G 开发板</th>
	        <th>GPIO</th>
	    </tr>
	    <tr>
	        <td colspan="3">IR 传感器 OUT 引脚 </td>
	        <td>38</td>
	        <td>K[13]</td>
	    </tr>
	        <tr>
	        <td colspan="3">IR 传感器 VCC 引脚 </td>
	        <td>5V</td>
	        <td>-</td>
	    </tr>
	    <tr>
	        <td colspan="3">IR 传感器 GND 引脚</td>
	        <td>GND</td>
	        <td>-</td>
	    </tr>
	    <tr>
	        <td colspan="3">LED01 (+) 引脚</td>
	        <td>16</td>
	        <td>A[06]</td>
	    </tr>
	    <tr>
	        <td colspan="3">LED01 (-) 引脚</td>
	        <td>GND</td>
	        <td>-</td>
	    </tr>
	    <tr>
	        <td colspan="3">LED02 (+) 引脚</td>
	        <td>17</td>
	        <td>A[07]</td>
	    </tr>
	    <tr>
	        <td colspan="3">LED02 (-) 引脚 </td>
	        <td>GND</td>
	        <td>-</td>
	    </tr>
	</table>
</div>
</br></br>

### 7.1.3 执行方法
要运行本示例，请按如下所示修改 main.c 文件中的 **Main_StartTask()**。
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
编辑代码后，进入以下目录并运行构建命令：  
```
$ cd ~/vcp/build/tcc70xx/gcc
$ make
```
该操作会生成固件镜像，并使用 ***FWDN*** 工具将生成的镜像烧录到 VCP-G。  
代码成功烧录并执行后，IR 传感器会检测物体的有无并相应地控制两个 LED。检测到物体时第一个 LED 点亮；未检测到物体时第二个 LED 点亮。该行为确认 VCP-G 开发板上的 IR 传感器输入和 GPIO 输出工作正常。

**注意**：如果需要更改用于 IR 传感器或 LED 的 GPIO 引脚，请参阅源代码内的配置部分。
</br></br></br>

## 7.2 红外 (IR) 传感器（接收器）
---
本示例演示 VCP-G 开发板如何使用红外接收传感器检测来自遥控器的信号。接收到 IR 信号时，板载逻辑会点亮连接在面包板上的 LED。这确认红外接收模块正确解码了接收到的信号，并且 VCP-G 按预期做出响应。接收状态也会显示在串口监视器上。
</br></br>

### 7.2.1 硬件要求
- VCP-G 开发板 (x1)
- 面包板 (x1)
- 红外接收传感器 (x1)
- Arduino 遥控器 (x1)
- LED (x1)
- 12V 1A 电源适配器 (x1)
- USB Type-C 转 A 线缆 (x1)
- 公对公跳线 (x5)
</br></br>

### 7.2.2 电路
- 红外接收传感器
    - IR 传感器的 SIG 引脚连接到 VCP-G 开发板的引脚 40。
    - IR 传感器的 GND 引脚连接到 VCP-G 开发板上的 GND。
    - IR 传感器的 VCC 引脚连接到 VCP-G 开发板上的 5V。
- LED
    - (+) 引脚连接到 VCP-G 开发板的 7 号引脚。
    - (–) 引脚连接到面包板上的 GND 排。

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/F_irsensor2.png" width="600"></p>
<p align="center"><strong>图 7.2 红外接收传感器电路原理图</strong></p>

##### 7.2.2.1 引脚图
下表显示了引脚映射。

<p align="center"><strong>表 7.1 irSensor_LED 的引脚图</strong></p>
<div align="center">
	<table>
	    <tr>
	        <th colspan="3">引脚名称</th>
	        <th>VCP-G 开发板</th>
	        <th>GPIO</th>
	    </tr>
	    <tr>
	        <td colspan="3">IR 传感器 SIG 引脚 </td>
	        <td>40</td>
	        <td>K[11]</td>
	    </tr>
	        <tr>
	        <td colspan="3">IR 传感器 GND 引脚 </td>
	        <td>GND</td>
	        <td>-</td>
	    </tr>
	    <tr>
	        <td colspan="3">IR 传感器 VCC 引脚</td>
	        <td>VCC</td>
	        <td>-</td>
	    </tr>
	    <tr>
	        <td colspan="3">LED (+) 引脚</td>
	        <td>7</td>
	        <td>B[01]</td>
	    </tr>
	    <tr>
	        <td colspan="3">LED (-) 引脚</td>
	        <td>GND</td>
	        <td>-</td>
	    </tr>
	</table>
</div>

</br></br>

### 7.2.3 执行方法
要运行本示例，请按如下所示修改 main.c 文件中的 **Main_StartTask()**。
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
编辑代码后，进入以下目录并运行构建命令：  
```
$ cd ~/vcp/build/tcc70xx/gcc
$ make
```
该操作会生成固件镜像，并使用 ***FWDN*** 工具将生成的镜像烧录到 VCP-G。  
代码成功烧录并执行后，红外接收器会检测来自遥控器的信号并短暂点亮 LED。这确认 VCP-G 正确读取了 IR 输入，并根据接收到的信号控制 GPIO 输出。

**注意**：要更改用于 IR 传感器或 LED 的 GPIO 引脚，请参阅源代码内的配置部分。
</br></br></br>

## 7.3 气体传感器
---
本示例演示 VCP-G 开发板如何使用气体传感器 (MQ 135) 检测空气中的各种有害气体。它从连接到 VCP-G 开发板模拟引脚的传感器读取模拟值，将其转换为电压，然后以一位小数打印到串口监视器。

**注意：** Gas Sensor (MQ-135) 是 Winsen® 的产品。其设计、商标及相关知识产权的所有权利均归 Winsen 所有。
</br></br>

### 7.3.1 硬件要求
- VCP-G 开发板 (x1)
- 气体传感器 (MQ135) (x1)
- 12V 1A 电源适配器 (x1)
- USB Type-C 转 A 线缆 (x1)
- 公对母跳线 (x3)
</br></br>

### 7.3.2 电路
- 气体传感器
    - 气体传感器的 A0 引脚连接到 VCP-G 开发板的模拟引脚 55。 
    - 气体传感器的 VCC 引脚连接到 VCP-G 开发板上的 5V。
    - 气体传感器的 GND 引脚连接到 VCP-G 开发板上的 GND。

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/F_gassensor.png" width="600"></p>
<p align="center"><strong>图 7.3 气体传感器电路原理图</strong></p>

#### 7.3.2.1 引脚图
下表显示了引脚映射。

<p align="center"><strong>表 7.3 气体传感器引脚图</strong></p>
<div align="center">
	<table>
	    <tr>
	        <th colspan="3">引脚名称</th>
	        <th>VCP-G 开发板</th>
	        <th>GPIO</th>
	    </tr>
	    <tr>
	        <td colspan="3">气体传感器 A0 引脚</td>
	        <td>55</td>
	        <td>K[15]</td>
	    </tr>
	        <tr>
	        <td colspan="3">气体传感器 VCC 引脚</td>
	        <td>5V</td>
	        <td>-</td>
	    </tr>
	    <tr>
	        <td colspan="3">气体传感器 GND 引脚</td>
	        <td>GND</td>
	        <td>-</td>
	    </tr>
	</table>
</div>
</br></br>

### 7.3.3 执行方法
要运行本示例，请按如下所示修改 main.c 文件中的 **Main_StartTask()**。
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
编辑代码后，进入以下目录并运行构建命令：  
```
$ cd ~/vcp/build/tcc70xx/gcc
$ make
```
此过程会生成固件镜像，并使用 **FWDN** 工具将生成的镜像烧录到 VCP-G。  
代码成功烧录并执行后，气体传感器会持续监测周围的空气质量。检测到气体时（传感器输出为 LOW），串口监视器上会显示表示检测到气体的消息；否则报告空气清洁。这确认 VCP-G 正确读取了来自气体传感器的数字输入。

**注意**：要更改用于气体传感器的 GPIO 引脚，请参阅源代码内的配置部分。大多数气体传感器模块都带有一个用于调节灵敏度的小调节螺丝（电位器）。如果传感器响应不稳定，请尝试调节该螺丝以微调气体检测阈值。
</br></br></br>

## 7.4 电容式触摸传感器
---
本示例演示 VCP-G 开发板如何与电容式触摸传感器连接并控制面包板上的 LED。电容式触摸传感器通过感应电容的变化来检测手指的物理接触。  
检测到触摸时，传感器向 VCP-G 输出数字 HIGH 信号，VCP-G 随即点亮 LED。本示例确认触摸输入被正确识别，并且 GPIO 输出做出相应响应。触摸检测状态也会显示在串口监视器上。
</br></br>

### 7.4.1 硬件要求
- VCP-G 开发板 (x1)
- 面包板 (x1)
- 电容式触摸传感器 (x1)
- LED (x1)
- 12V 1A 电源适配器 (x1)
- USB Type-C 转 A 线缆 (x1)
- 公对公跳线（x6）
</br></br>

### 7.4.2 电路
- 触摸传感器 
    - 触摸传感器模块的 SIG 引脚连接到 VCP-G 开发板的引脚 39。
    - 触摸传感器模块的 VCC 引脚连接到 VCP-G 开发板的 5V。
    - 触摸传感器模块的 GND 引脚连接到 VCP-G 开发板上的 GND。
- LED
    - LED 的 (+) 引脚连接到 VCP-G 开发板上的 7 号引脚。
    - LED 的 (–) 引脚连接到面包板上的 GND 排。

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/F_touchsensor.png" width="600"></p>
<p align="center"><strong>图 7.4 触摸传感器电路原理图</strong></p>

#### 7.4.2.1 引脚映射
下表显示了引脚映射。

<p align="center"><strong>表 7.5 触摸传感器引脚映射</strong></p>
<div align="center">
	<table>
	    <tr>
	        <th colspan="3">引脚名称</th>
	        <th>VCP-G 开发板</th>
	        <th>GPIO</th>
	    </tr>
	    <tr>
	        <td colspan="3">触摸传感器 SIG 引脚</td>
	        <td>39</td>
	        <td>K[12]</td>
	    </tr>
	        <tr>
	        <td colspan="3">触摸传感器 VCC 引脚</td>
	        <td>5V</td>
	        <td>-</td>
	    </tr>
	    <tr>
	        <td colspan="3">触摸传感器 GND 引脚</td>
	        <td>GND</td>
		    <td>-</td>
		</tr>
	    <tr>
	        <td colspan="3">LED (+) 引脚</td>
	        <td>7</td>
	        <td>B[01]</td>
	    </tr>
	    <tr>
	        <td colspan="3">LED (-) 引脚</td>
	        <td>GND</td>
	        <td>-</td>
	    </tr>
	</table>
</div>

</br></br>

### 7.4.3 执行方法
要运行本示例，请按如下所示修改 main.c 文件中的 **Main_StartTask()**。
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
编辑代码后，进入以下目录并运行构建命令：  
```
$ cd ~/vcp/build/tcc70xx/gcc
$ make
```
此操作会生成固件镜像，并使用 FWDN 工具将生成的镜像烧录到 VCP-G。  
代码成功烧录并执行后，电容式触摸传感器会检测人手指的触摸输入。检测到触摸时（传感器输出为 HIGH），串口监视器会打印一条消息，并点亮 LED。未检测到触摸时，LED 熄灭。这表明 VCP-G 能够正确读取触摸传感器的输入，并相应地控制 GPIO 输出。

**注意**：如需更改触摸传感器或 LED 所使用的 GPIO 引脚，请参考源代码中的配置部分。
</br></br></br></br>

# 8. 参考资料
---
- 有关更多详细信息，请联系 TOPST：topst@topst.ai

**注意：** 参考文档可根据合同条款在可提供时提供。如果参考
文档无法提供，则可就与您的开发直接相关的内容提供指导。
