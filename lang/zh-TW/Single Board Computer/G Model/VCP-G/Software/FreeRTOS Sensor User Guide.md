# 1. 簡介
---
本文件提供搭配 FreeRTOS 使用 VCP-G 的指引，內容包含設定說明與範例程式碼，協助您在 FreeRTOS 環境下使用 VCP-G 輕鬆開發嵌入式應用程式。

具體而言，本文件說明 VCP-G 上以 FreeRTOS 為基礎的範例應用程式，包括： 
- 數位輸出/輸入
- SPI
- I2C
- UART
- PWM
- 其他範例

使用 VCP-G 前請參閱圖 1.1。
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/vcp-g%20pinout%20Diagram.png"></p>
<p align="center"><strong>圖 1.1 VCP-G 腳位圖</strong></p>
</br>

若要執行各個範例，您應修改位於下列位置的 `main.c` 檔案：
```
$ ~/vcp/sources/app.sample/app.base/main.c
```
完成必要的變更後，請使用所提供的 Makefile 編譯專案，以產生韌體二進位檔。
</br></br></br></br>

# 2. 數位輸入/輸出
---
本章提供使用 VCP-G 開發板數位腳位控制 LED 的範例。在 VCP-G 中，數位腳位用於傳送或接收二元訊號（HIGH 或 LOW），是控制 LED、開關與感測器等元件的關鍵。 

本章包含兩個範例專案，示範如何使用數位輸出與輸入來控制 LED 與按鈕，讓您對數位腳位的功能有基本的了解。
</br></br></br>

## 2.1 數位輸出
---
本範例示範如何在 FreeRTOS 環境下使用 VCP-G 開發板控制麵包板上的 LED。  
您可以在下列位置找到相關的原始檔：  

```
$ ~/vcp/sources/app.sample/app.base/main.c
```
在繼續之前，請確認已正確安裝 VCP-G FreeRTOS SDK。關於安裝與設定說明，請參閱 VCP-G FreeRTOS SDK 入門指南。

若要實作本範例，請修改 main.c 檔案，將連接至 LED 的 GPIO 腳位設定為數位輸出。應建立一個 FreeRTOS 任務，依序逐一點亮四顆 LED，然後以相反的順序將其熄滅。每次 LED 切換之間應加入 500 ms 的延遲，以便清楚觀察其順序。
</br></br>

### 2.1.1 硬體需求  
- VCP-G 開發板 (x1)
- 麵包板 (x1)
- LED (x4)
- 12V 1A 電源變壓器 (x1)
- USB Type-C 轉 A 傳輸線 (x1) 
- 公對公杜邦線 (x9)
</br></br>

### 2.1.2 電路
- LED01
    - (+) 腳位連接至 VCP-G 開發板上的 7 號腳位。
    - (–) 腳位連接至麵包板上的 GND 匯流排。
- LED02
    - (+) 腳位連接至 VCP-G 開發板上的 6 號腳位。
    - (–) 腳位連接至麵包板上的 GND 匯流排。
- LED03
    - (+) 腳位連接至 VCP-G 開發板上的 5 號腳位。
    - (–) 腳位連接至麵包板上的 GND 匯流排。
- LED04
    - (+) 腳位連接至 VCP-G 開發板上的 4 號腳位。
    - (–) 腳位連接至麵包板上的 GND 匯流排。 

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/F_digital_out.png" width="600"></p>
<p align="center"><strong>圖 2.1 vcp4LED 電路圖</strong></p>

#### 2.1.2.1 腳位對應
下表列出腳位對應。

<p align="center"><strong>表 2.1 vcp4LED 的腳位對應</strong></p>
<div align="center">	
	<table>
		<tr>
			<th colspan="3">腳位名稱</th>
	        <th>VCP-G 開發板</th>
	        <th>GPIO</th>
	    </tr>
	    <tr>
	        <td colspan="3">LED01 (+) 腳位</td>
	        <td>7</td>
	        <td>B[01]</td>
	    </tr>
	        <tr>
	        <td colspan="3">LED02 (+) 腳位</td>
	        <td>6</td>
	        <td>A[13]</td>
	    </tr>
	        <tr>
	        <td colspan="3">LED03 (+) 腳位</td>
	        <td>5</td>
	        <td>B[10]</td>
	    </tr>
	        <tr>
	        <td colspan="3">LED04 (+) 腳位</td>
	        <td>4</td>
	        <td>B[27]</td>
	    </tr>
	</table>
</div>
</br></br>

### 2.1.3 執行方式
若要執行本範例，請如下所示修改 main.c 檔案中的 **Main_StartTask()**。
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
編輯程式碼後，請前往下列目錄並執行建置指令：  
```
$ cd ~/vcp/build/tcc70xx/gcc
$ make
```
此步驟會產生韌體映像檔，並使用 ***FWDN*** 工具將產生的映像檔燒錄至 VCP-G。  
程式碼成功燒錄並執行後，所連接的四顆 LED 會從 LED01 到 LED04 依序點亮，然後以相反的順序熄滅。每次切換之間有 500 ms 的延遲，形成平順的閃爍效果。
</br></br></br>

## 2.2 數位輸入
---
本範例示範如何在 FreeRTOS 環境下使用 VCP-G 開發板讀取按鈕的輸入，並以此控制 LED。
相關的原始檔位於：
``` 
$ ~/vcp/sources/app.sample/app.base/main.c
```
若要實作本範例，請修改 main.c，將一個 GPIO 腳位設定為數位輸入（連接至按鈕），並將四個 GPIO 腳位設定為數位輸出（連接至 LED）。  
FreeRTOS 任務會持續監控按鈕狀態，當按鈕被按下時，LED1 與 LED3 會點亮。
當按鈕未被按下時，則改為點亮 LED2 與 LED4。
</br></br>

### 2.2.1 硬體需求
- VCP-G 開發板 (x1)
- 麵包板 (x1)
- LED (x4)
- 按鈕開關（感測器）(x1)
- 12V 1A 電源變壓器 (x1)
- USB Type-C 轉 A 傳輸線 (x1)
- 公對公杜邦線 (x11)
</br></br>

### 2.2.2 電路
- LED01
    - (+) 腳位連接至 VCP-G 開發板上的 7 號腳位。
    - (–) 腳位連接至麵包板上的 GND 匯流排。
- LED02
    - (+) 腳位連接至 VCP-G 開發板上的 6 號腳位。
    - (–) 腳位連接至麵包板上的 GND 匯流排。
- LED03
    - (+) 腳位連接至 VCP-G 開發板上的 5 號腳位。
    - (–) 腳位連接至麵包板上的 GND 匯流排。
- LED04
    - (+) 腳位連接至 VCP-G 開發板上的 4 號腳位。
    - (–) 腳位連接至麵包板上的 GND 匯流排。 
- 按鈕開關
    - 按鈕開關的一支接腳連接至 VCP-G 開發板上的 2 號腳位。
    - 按鈕對角的另一支接腳連接至麵包板上的電源匯流排。

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/F_digital_in.png" width="600"></p>
<p align="center"><strong>圖 2.2 vcp4LED_Button 電路圖</strong></p>

#### 2.2.2.1 腳位對應
下表列出腳位對應。

<p align="center"><strong>表 2.2 vcp4LED_Button 的腳位對應</strong></p>
<div align="center">
	<table>
	    <tr>
	        <th colspan="3">腳位名稱</th>
	        <th>VCP-G 開發板</th>
	        <th>GPIO</th>
	    </tr>
	    <tr>
	        <td colspan="3">LED01 (+) 腳位</td>
	        <td>7</td>
	        <td>B[01]</td>
	    </tr>
	        <tr>
	        <td colspan="3">LED02 (+) 腳位</td>
	        <td>6</td>
	        <td>A[13]</td>
	    </tr>
	        <tr>
	        <td colspan="3">LED03 (+) 腳位</td>
	        <td>5</td>
	        <td>B[10]</td>
	    </tr>
	        <tr>
	        <td colspan="3">LED04 (+) 腳位</td>
	        <td>4</td>
	        <td>B[27]</td>
	    </tr>
	    </tr>
	        <tr>
	        <td colspan="3">按鈕的一隻接腳</td>
	        <td>2</td>
	        <td>B[28]</td>
	    </tr>
	</table>
</div>
</br></br>

### 2.2.3 執行方式
若要執行本範例，請如下所示修改 main.c 檔案中的 **Main_StartTask()**。
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
編輯程式碼後，請前往下列目錄並執行建置指令：  
```
$ cd ~/vcp/build/tcc70xx/gcc
$ make
```
此步驟會產生韌體映像檔，並使用 ***FWDN*** 工具將產生的映像檔燒錄至 VCP-G。  
程式碼成功燒錄並執行後，按下按鈕會點亮 LED01 與 LED03，放開按鈕則會點亮 LED02 與 LED04。
系統會以 50 ms 的輪詢間隔持續監控按鈕狀態，並即時更新 LED 的狀態。
</br></br></br></br>

# 3. VCP-G I2C
---
本章說明如何在執行 FreeRTOS 的 VCP-G 上設定 Inter-integrated Circuit (I2C) 通訊。  
I2C 是一種雙線式同步通訊協定，專為多個裝置之間高效交換資料而設計。它以一條序列資料線 (SDA) 與一條序列時脈線 (SCL) 運作，讓多個週邊裝置能夠使用各自唯一的位址與微控制器通訊。I2C 同時支援主從式通訊與多主控端設定，因此非常適合在盡量減少所需連線數量的情況下，連接感測器、顯示器及其他低速裝置。
</br></br></br>

## 3.1 vcpI2C_LCD1602
---
本範例程式示範 VCP-G 開發板如何使用 I2C 通訊協定控制 LCD1602 顯示器。LCD1602 是一款每列 16 個字元、共 2 列的液晶顯示器，常用於嵌入式系統專案。開發板透過 LiquidCrystal_I2C 函式庫，經由 I2C 匯流排傳送指令與資料，以有效率地控制顯示器。  
在本範例中，LCD 會先完成初始化並啟用背光以確保清晰可見。接著程式會定位游標，在螢幕上顯示文字「Hello TOPST」。
</br></br>

### 3.1.1 硬體需求
- VCP-G 開發板 (x1)
- LCD1602（x1）
- 12V 1A 電源變壓器 (x1)
- USB Type-C 轉 A 傳輸線 (x1)
- 公對母跳線（x4）
</br></br>

### 3.1.2 電路
- LCD1602
    - LCD1602 的 VCC 腳位連接至 VCP-G 開發板上的類比腳位 5V。
    - LCD1602 的 GND 腳位連接至 VCP-G 開發板上的 GND。
    - LCD1602 的 SDA 腳位連接至 VCP-G 開發板上的 7 號腳位。
    - LCD1602 的 SCL 腳位連接至 VCP-G 開發板上的 8 號腳位。

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/F_i2c.png" width="600"></p>
<p align="center"><strong>圖 3.1 vcpI2C_LCD1602 電路圖</strong></p>

#### 3.1.2.1 腳位對應
下表列出腳位對應。

<p align="center"><strong>表 3.1 vcpI2C_LCD1602 腳位對應</strong></p>
<div align="center">
	<table>
	    <tr>
	        <th colspan="3">腳位名稱</th>
	        <th>VCP-G 開發板</th>
	        <th>GPIO</th>
	    </tr>
	    <tr>
	        <td colspan="3">LCD1602 VCC 腳位</td>
	        <td>5V</td>
	        <td>-</td>
	    </tr>
	        <tr>
	        <td colspan="3">LCD1602 GND 腳位</td>
	        <td>GND</td>
	        <td>-</td>
	    </tr>
	        <tr>
	        <td colspan="3">LCD1602 SDA 腳位</td>
	        <td>7</td>
	        <td>B[01]</td>
	    </tr>
	        <tr>
	        <td colspan="3">LED (-) 腳位</td>
	        <td>8</td>
	        <td>B[00]</td>
	    </tr>
	</table>
</div>

</br></br>

### 3.1.3 執行方式
若要執行本範例，請如下所示修改 main.c 檔案中的 **Main_StartTask()**。
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
#### 額外設定注意事項
若要透過 I2C 啟用 LCD 測試，請依照下列步驟：  

**1. 在建置系統中啟用 lcd.c**  
- 請前往下列路徑：
```
$ vi ~/vcp/sources/dev.drivers/i2c/rules.mk
```
- 請找出下列這一行：
```
#SRCS += lcd.c
```
- 請取消該行的註解以啟用此檔案：
```
SRCS += lcd.c
```

**2. 檢查或修改 LCD 功能邏輯**  
若您需要檢視或編輯 LCD 初始化、指令或列印函式的邏輯，請參閱：
```
$ vi ~/vcp/sources/dev.drivers/i2c/lcd.c
```

**3. 設定 I2C 通道與連接埠**  
LCD 所使用的 I2C 通道編號與對應的連接埠可於下列檔案中變更：
```
$ vi ~/vcp/sources/dev.drivers/i2c/lcd.h
```

編輯程式碼後，請前往下列目錄並執行下列建置指令：  
```
$ cd ~/vcp/build/tcc70xx/gcc
$ make
```
此步驟會產生韌體映像檔，並使用 ***FWDN*** 工具將產生的映像檔燒錄至 VCP-G。  
程式碼成功燒錄並執行後，LCD 會在螢幕上顯示訊息「Hello TOPST」，確認 I2C 通訊運作正常。  
</br></br></br></br>

# 4. VCP SPI
---
本章說明如何在 VCP-G 上設定序列周邊介面（SPI）通訊。  
SPI 是一種高速的同步通訊協定，用於微控制器與周邊裝置之間的資料交換。它以獨立線路分別進行資料傳輸（MOSI 與 MISO）、時脈同步（SCK）與裝置選擇（SS），確保通訊高效且可靠。  
</br></br></br>

## 4.1 vcpSPI_Dot8x8
---
本範例程式示範 VCP-G 開發板如何透過 SPI 使用 MAX7219 驅動器控制 8x8 LED 點矩陣。
在本範例中，會使用預先定義的二進位陣列在點矩陣上顯示字母「X」。顯示內容會透過 SPI 通訊更新，而列與行的控制則由 MAX7219 在內部處理。
本範例有助於說明如何透過 SPI 傳送資料圖樣，以控制 LED 矩陣等外部顯示裝置。
</br></br>

### 4.1.1 硬體需求
- VCP-G 開發板 (x1)
- 8x8 點矩陣（x1）
- 12V 1A 電源變壓器 (x1)
- USB Type-C 轉 A 傳輸線 (x1)
- 公對母杜邦線 (x2)
- 母對母杜邦線（x3）
</br></br>

### 4.1.2 電路
- 8x8 點矩陣
    - 8x8 點矩陣的 VCC 腳位連接至 VCP-G 開發板上的類比腳位 5V。
    - 8x8 點矩陣的 GND 腳位連接至 VCP-G 開發板上的 GND。
    - 8x8 點矩陣的 DIN 腳位連接至 VCP-G 開發板上的 SPI 4 號腳位。
    - 8x8 點矩陣的 CS 腳位連接至 VCP-G 開發板上的 SPI 5 號腳位。
    - 8x8 點矩陣的 CLS 腳位連接至 VCP-G 開發板上的 SPI 3 號腳位。

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/F_spi.png" width="600"></p>
<p align="center"><strong>圖 4.1 vcpSPI_Dot8x8 電路圖</strong></p>

#### 4.1.2.1 腳位對應
下表列出腳位對應。

<p align="center"><strong>表 4.1 vcpSPI_Dot8x8 的腳位對應</strong></p>
<div align="center">
	<table>
	    <tr>
	        <th colspan="3">腳位名稱</th>
	        <th>VCP-G 開發板</th>
	        <th>GPIO</th>
	    </tr>
	    <tr>
	        <td colspan="3">8x8 點矩陣 VCC 腳位</td>
	        <td>5V</td>
	        <td>-</td>
	    </tr>
	        <tr>
	        <td colspan="3">8x8 點矩陣 GND 腳位</td>
	        <td>GND</td>
	        <td>-</td>
	    </tr>
	    <tr>
	        <td colspan="3">8x8 點矩陣 DIN 腳位</td>
	        <td>SPI 4</td>
	        <td>B[06]</td>
	    </tr>
	    <tr>
	        <td colspan="3">8x8 點矩陣 CS 腳位</td>
	        <td>SPI 5</td>
	        <td>B[05]</td>
	    </tr>
	    <tr>
	        <td colspan="3">8x8 點矩陣 CLK 腳位</td>
	        <td>SPI 3</td>
	        <td>B[04]</td>
	    </tr>
	</table>
</div>
</br></br>

### 4.1.3 執行方式
若要執行本範例，請如下所示修改 main.c 檔案中的 **Main_StartTask()**。
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
#### 額外設定注意事項
若要透過 SPI 啟用點矩陣測試，請依照下列步驟：  
**1. 在建置系統中啟用 dot_matrix.c**  
- 請前往下列路徑：
```
$ vi ~/vcp/sources/dev.drivers/gpsb/rules.mk
```
- 請找出下列這一行：
```
#SRCS += dot_matrix.c
```
- 請取消註解以啟用此檔案：
```
SRCS += dot_matrix.c
```
**2. 檢查或修改點矩陣功能邏輯**  
若要檢視或編輯點矩陣初始化、控制指令或顯示圖樣的邏輯，請參閱下列原始檔：
```
$ vi ~/vcp/sources/dev.drivers/gpsb/dot_matrix.c
```
**3. 設定 SPI 通道與 GPIO**  
點矩陣所使用的 SPI 通道與對應的 GPIO 腳位可於下列標頭檔中設定：
```
$ vi ~/vcp/sources/dev.drivers/gpsb/dot_matrix.h
```
編輯程式碼後，請前往下列目錄並執行建置指令：  
```
$ cd ~/vcp/build/tcc70xx/gcc
$ make
```
此步驟會產生韌體映像檔，並使用 ***FWDN*** 工具將產生的映像檔燒錄至 VCP-G。  
程式碼成功燒錄並執行後，8x8 LED 點矩陣會顯示字母「X」，確認與 MAX7219 驅動器之間的 SPI 通訊運作正常。 
</br></br></br></br>

# 5. VCP-G UART
---
本章說明如何在 VCP-G 上設定通用非同步收發傳輸器（UART）通訊。  
UART 是一種廣泛使用的序列通訊協定，僅使用傳送 (TX) 與接收 (RX) 兩條線路即可非同步傳輸資料。它是在微控制器、感測器與電腦之間交換資料而不需共用時脈訊號的重要方式。  
以下章節說明如何透過 UART 傳送與接收資料。
</br></br></br>

## 5.1 UART 通訊測試 (FT232BL)
---
本範例示範如何使用 FT232BL USB 轉 TTL 序列模組驗證 VCP-G 開發板上的 UART 通訊。
VCP-G 開發板的 UART TX 與 RX 腳位連接至 FT232BL 模組，該模組再透過 USB 連接至 PC。
在 PC 上可使用 MobaXterm 等終端機程式檢視所傳送的訊息。
</br></br>

### 5.1.1 硬體需求
- VCP-G 開發板 (x1)
- FT232BL USB 轉 TTL 序列模組 (x1)
- Mini USB 傳輸線 (x1)
- 12V 1A 電源變壓器 (x1)
- USB Type-C 轉 A 傳輸線 (x1)
- 公對母杜邦線 (x2)
</br></br>

### 5.1.2 電路
- FT232BL
    - FT232BL 模組的 RXD 腳位連接至 VCP-G 開發板上的 18 號腳位 (TXD)。
    - FT232BL 模組的 TXD 腳位連接至 VCP-G 開發板上的 19 號腳位 (RXD)。

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/F_uart.png" width="600"></p>
<p align="center"><strong>圖 5.1 vcpUART 電路圖</strong></p>

#### 5.1.2.1 腳位對應
下表列出腳位對應。

<p align="center"><strong>表 4.1 vcpUART 腳位對應</strong></p>
<div align="center">
	<table>
	    <tr>
	        <th colspan="3">腳位名稱</th>
	        <th>VCP-G 開發板</th>
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

### 5.1.3 執行方式
若要執行本範例，請如下所示修改 main.c 檔案中的 **Main_StartTask()**。
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
#### 額外設定注意事項
若要啟用 UART 測試，請依照下列步驟：  
**1. 在建置系統中啟用 uart_example.c**  
- 請前往下列路徑：
```
$ vi ~/vcp/sources/dev.drivers/uart/rules.mk
```
- 請找出下列這一行：
```
#SRCS += uart_example.c
```
- 請取消註解以啟用此檔案：
```
SRCS += uart_example.c
```
**2. 檢查或修改 UART 功能邏輯**  
若要檢視或編輯 UART 初始化、資料傳送/接收或中斷處理的邏輯，請參閱下列原始檔：
```
$ vi ~/vcp/sources/dev.drivers/uart/tcc70xx/uart_example.c
```
**3. 設定 UART 通道與 GPIO**  
UART 測試所使用的 UART 通道、鮑率以及對應的 TX/RX GPIO 腳位可於下列標頭檔中設定：
```
$ vi ~/vcp/sources/dev.drivers/uart/uart_example.h
```
編輯程式碼後，請前往下列目錄並執行建置指令：  
```
$ cd ~/vcp/build/tcc70xx/gcc
$ make
```
此步驟會產生韌體映像檔，並使用 ***FWDN*** 工具將產生的映像檔燒錄至 VCP-G。  
程式碼成功燒錄並執行後，序列終端機上會出現一次訊息「[UART] Hello from UART!」，確認 VCP-G 開發板透過 FT232BL USB 轉 TTL 模組的 UART 傳輸運作正常。
</br></br></br></br>

# 6. VCP-G PWM
---
本章說明如何在 VCP-G 上設定脈衝寬度調變 (PWM)。PWM 是一種藉由改變數位訊號的工作週期，來控制傳送至馬達、LED 與蜂鳴器等裝置的電力大小的技術。其運作方式是以高頻率切換輸出腳位的開啟與關閉，而導通時間佔整個週期的比例即決定了實際的輸出準位。後續章節將說明如何在 VCP-G 上使用 FreeRTOS 產生 PWM 訊號，以及如何運用這些訊號來控制外部元件。
</br></br></br>

## 6.1 pwmFade
---
本範例程式示範 VCP 開發板如何使用 PWM，以迴圈方式逐漸提高與降低亮度來控制麵包板上的 LED。當 LED 達到最大亮度後，其亮度便會開始下降。程式會持續調整 LED 的亮度，形成漸亮漸暗的效果。
</br></br>

### 6.1.1 硬體需求
- VCP-G 開發板 (x1)
- 麵包板 (x1)
- LED (x1)
- 12V 1A 電源變壓器 (x1)
- USB Type-C 轉 A 傳輸線 (x1)
- 公對公跳線（x2）
</br></br>

### 6.1.2 電路
- LED
    - (+) 腳位連接至 VCP-G 開發板上的 45 號腳位。
    - (–) 腳位連接至麵包板上的 GND 匯流排。

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/F_pwm.png" width="600"></p>
<p align="center"><strong>圖 5.1 pwmFade 電路圖</strong></p>

#### 6.1.2.1 腳位對應
下表列出腳位對應。

<p align="center"><strong>表 4.1 pwmFade 腳位對應</strong></p>
<div align="center">
	<table>
	    <tr>
	        <th colspan="3">腳位名稱</th>
	        <th>VCP-G 開發板</th>
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

### 6.1.3 執行方式
若要執行本範例，請如下所示修改 main.c 檔案中的 **Main_StartTask()**。
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
編輯程式碼後，請前往下列目錄並執行建置指令：  
```
$ cd ~/vcp/build/tcc70xx/gcc
$ make
```
此步驟會產生韌體映像檔，並使用 ***FWDN*** 工具將產生的映像檔燒錄至 VCP-G。  
程式碼成功燒錄並執行後，您可以觀察到由 GPIO A10 上的 PWM 所驅動的 LED 漸亮與漸暗效果，確認 VCP-G 以 PDM 為基礎的 PWM 輸出運作正常。

**註**：若要變更 PWM 輸出所使用的 GPIO 連接埠，請參閱 pdm.c 檔案中的設定。
</br></br></br></br>

# 7. 其他範例
---
本章介紹在 VCP-G 開發板上使用 FreeRTOS 的其他感測器範例，提供如何在 VCP-G 開發板上以 FreeRTOS 使用常見 Arduino 感測器的範例指引，讓您能夠有效地將各種感測器整合到您的專案中。
</br></br></br>

## 7.1 紅外線（IR）感測器（收發器）
---
本範例示範 VCP-G 開發板如何控制麵包板上的紅外線感測器與兩顆 LED。當紅外線感測器偵測到物件時（感測器數值為 LOW），第一顆 LED 會點亮，第二顆 LED 則會熄滅。反之，當未偵測到物件時（感測器數值為 HIGH），第二顆 LED 會點亮，而第一顆 LED 會熄滅。是否偵測到物件也會列印至序列監控視窗。
</br></br>

### 7.1.1 硬體需求
- VCP-G 開發板 (x1)
- 麵包板 (x1)
- IR 收發器感測器（x1）
- LED（x2：建議使用不同顏色）
- 12V 1A 電源變壓器 (x1)
- USB Type-C 轉 A 傳輸線 (x1)
- 公對公杜邦線 (x5)
- 公對母跳線（x3）
</br></br>

### 7.1.2 電路
- IR 收發器感測器
    - 紅外線感測器的 OUT 腳位連接至 VCP-G 開發板上的 38 號腳位。
    - IR 感測器的 VCC 腳位連接至 VCP-G 開發板上的 5V。
    - IR 感測器的 GND 腳位連接至 VCP-G 開發板上的 GND。
- LED01
    - (+) 腳位連接至 VCP-G 開發板上的 16 號腳位。
    - (–) 腳位連接至麵包板上的 GND 匯流排。
- LED02
    - (+) 腳位連接至 VCP-G 開發板上的 17 號腳位。
    - (–) 腳位連接至麵包板上的 GND 匯流排。

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/F_irsensor1.png" width="600"></p>
<p align="center"><strong>圖 7.1 紅外線（IR）感測器電路圖</strong></p>

##### 7.1.2.1 腳位對應
下表列出腳位對應。

<p align="center"><strong>表 7.1 irSensor_LED 的腳位對應</strong></p>
<div align="center">
	<table>
	    <tr>
	        <th colspan="3">腳位名稱</th>
	        <th>VCP-G 開發板</th>
	        <th>GPIO</th>
	    </tr>
	    <tr>
	        <td colspan="3">IR 感測器 OUT 腳位 </td>
	        <td>38</td>
	        <td>K[13]</td>
	    </tr>
	        <tr>
	        <td colspan="3">IR 感測器 VCC 腳位 </td>
	        <td>5V</td>
	        <td>-</td>
	    </tr>
	    <tr>
	        <td colspan="3">IR 感測器 GND 腳位</td>
	        <td>GND</td>
	        <td>-</td>
	    </tr>
	    <tr>
	        <td colspan="3">LED01 (+) 腳位</td>
	        <td>16</td>
	        <td>A[06]</td>
	    </tr>
	    <tr>
	        <td colspan="3">LED01 (-) 腳位</td>
	        <td>GND</td>
	        <td>-</td>
	    </tr>
	    <tr>
	        <td colspan="3">LED02 (+) 腳位</td>
	        <td>17</td>
	        <td>A[07]</td>
	    </tr>
	    <tr>
	        <td colspan="3">LED02 (-) 腳位 </td>
	        <td>GND</td>
	        <td>-</td>
	    </tr>
	</table>
</div>
</br></br>

### 7.1.3 執行方式
若要執行本範例，請如下所示修改 main.c 檔案中的 **Main_StartTask()**。
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
編輯程式碼後，請前往下列目錄並執行建置指令：  
```
$ cd ~/vcp/build/tcc70xx/gcc
$ make
```
此步驟會產生韌體映像檔，並使用 ***FWDN*** 工具將產生的映像檔燒錄至 VCP-G。  
程式碼成功燒錄並執行後，紅外線感測器會偵測物件的有無，並據此控制兩顆 LED。偵測到物件時，第一顆 LED 會點亮；未偵測到物件時，第二顆 LED 會點亮。此行為可確認 VCP-G 開發板上的紅外線感測器輸入與 GPIO 輸出運作正常。

**註**：若您需要變更紅外線感測器或 LED 所使用的 GPIO 腳位，請參閱原始程式碼中的設定區段。
</br></br></br>

## 7.2 紅外線 (IR) 感測器（接收器）
---
本範例示範 VCP-G 開發板如何使用紅外線接收感測器偵測來自遙控器的訊號。當接收到紅外線訊號時，板上的邏輯會點亮連接於麵包板上的 LED。這可確認紅外線接收模組正確解碼了傳入的訊號，且 VCP-G 依預期做出回應。接收狀態也會顯示於序列監控視窗上。
</br></br>

### 7.2.1 硬體需求
- VCP-G 開發板 (x1)
- 麵包板 (x1)
- 紅外線接收感測器 (x1)
- Arduino 遙控器 (x1)
- LED (x1)
- 12V 1A 電源變壓器 (x1)
- USB Type-C 轉 A 傳輸線 (x1)
- 公對公杜邦線 (x5)
</br></br>

### 7.2.2 電路
- 紅外線接收感測器
    - 紅外線感測器的 SIG 腳位連接至 VCP-G 開發板上的 40 號腳位。
    - IR 感測器的 GND 腳位連接至 VCP-G 開發板上的 GND。
    - IR 感測器的 VCC 腳位連接至 VCP-G 開發板上的 5V。
- LED
    - (+) 腳位連接至 VCP-G 開發板上的 7 號腳位。
    - (–) 腳位連接至麵包板上的 GND 匯流排。

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/F_irsensor2.png" width="600"></p>
<p align="center"><strong>圖 7.2 紅外線接收感測器電路圖</strong></p>

##### 7.2.2.1 腳位對應
下表列出腳位對應。

<p align="center"><strong>表 7.1 irSensor_LED 的腳位對應</strong></p>
<div align="center">
	<table>
	    <tr>
	        <th colspan="3">腳位名稱</th>
	        <th>VCP-G 開發板</th>
	        <th>GPIO</th>
	    </tr>
	    <tr>
	        <td colspan="3">紅外線感測器 SIG 腳位 </td>
	        <td>40</td>
	        <td>K[11]</td>
	    </tr>
	        <tr>
	        <td colspan="3">紅外線感測器 GND 腳位 </td>
	        <td>GND</td>
	        <td>-</td>
	    </tr>
	    <tr>
	        <td colspan="3">紅外線感測器 VCC 腳位</td>
	        <td>VCC</td>
	        <td>-</td>
	    </tr>
	    <tr>
	        <td colspan="3">LED (+) 腳位</td>
	        <td>7</td>
	        <td>B[01]</td>
	    </tr>
	    <tr>
	        <td colspan="3">LED (-) 腳位</td>
	        <td>GND</td>
	        <td>-</td>
	    </tr>
	</table>
</div>

</br></br>

### 7.2.3 執行方式
若要執行本範例，請如下所示修改 main.c 檔案中的 **Main_StartTask()**。
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
編輯程式碼後，請前往下列目錄並執行建置指令：  
```
$ cd ~/vcp/build/tcc70xx/gcc
$ make
```
此步驟會產生韌體映像檔，並使用 ***FWDN*** 工具將產生的映像檔燒錄至 VCP-G。  
程式碼成功燒錄並執行後，紅外線接收器會偵測來自遙控器的訊號，並短暫點亮 LED。這可確認 VCP-G 正確讀取紅外線輸入，並依據所接收到的訊號控制 GPIO 輸出。

**註**：若要變更紅外線感測器或 LED 所使用的 GPIO 腳位，請參閱原始程式碼中的設定區段。
</br></br></br>

## 7.3 氣體感測器
---
此範例示範 VCP-G 開發板如何使用氣體感測器（MQ 135）偵測空氣中的各種有害氣體。程式會讀取連接至 VCP-G 開發板類比腳位之感測器的類比數值，將其換算為電壓，然後以小數點後一位列印至序列監控視窗。

**註：** 氣體感測器（MQ-135）為 Winsen® 的產品。其設計、商標及相關智慧財產權皆歸 Winsen 所有。
</br></br>

### 7.3.1 硬體需求
- VCP-G 開發板 (x1)
- 氣體感測器（MQ135）（x1）
- 12V 1A 電源變壓器 (x1)
- USB Type-C 轉 A 傳輸線 (x1)
- 公對母跳線（x3）
</br></br>

### 7.3.2 電路
- 氣體感測器
    - 氣體感測器的 A0 腳位連接至 VCP-G 開發板上的類比腳位 55。 
    - 氣體感測器的 VCC 腳位連接至 VCP-G 開發板上的 5V。
    - 氣體感測器的 GND 腳位連接至 VCP-G 開發板上的 GND。

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/F_gassensor.png" width="600"></p>
<p align="center"><strong>圖 7.3 氣體感測器電路圖</strong></p>

#### 7.3.2.1 腳位對應
下表列出腳位對應。

<p align="center"><strong>表 7.3 氣體感測器腳位對應</strong></p>
<div align="center">
	<table>
	    <tr>
	        <th colspan="3">腳位名稱</th>
	        <th>VCP-G 開發板</th>
	        <th>GPIO</th>
	    </tr>
	    <tr>
	        <td colspan="3">氣體感測器 A0 腳位</td>
	        <td>55</td>
	        <td>K[15]</td>
	    </tr>
	        <tr>
	        <td colspan="3">氣體感測器 VCC 腳位</td>
	        <td>5V</td>
	        <td>-</td>
	    </tr>
	    <tr>
	        <td colspan="3">氣體感測器 GND 腳位</td>
	        <td>GND</td>
	        <td>-</td>
	    </tr>
	</table>
</div>
</br></br>

### 7.3.3 執行方式
若要執行本範例，請如下所示修改 main.c 檔案中的 **Main_StartTask()**。
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
編輯程式碼後，請前往下列目錄並執行建置指令：  
```
$ cd ~/vcp/build/tcc70xx/gcc
$ make
```
此步驟會產生韌體映像檔，並使用 **FWDN** 工具將產生的映像檔燒錄至 VCP-G。  
程式碼成功燒錄並執行後，氣體感測器會持續監控周圍的空氣品質。當偵測到氣體時（感測器輸出為 LOW），序列監控視窗上會顯示表示偵測到氣體的訊息；否則會回報空氣潔淨。這可確認 VCP-G 正確讀取來自氣體感測器的數位輸入。

**註**：若要變更氣體感測器所使用的 GPIO 腳位，請參閱原始程式碼中的設定區段。多數氣體感測器模組都內建一個用於控制靈敏度的小調整螺絲（可變電阻）。若感測器的反應不夠穩定，請嘗試調整此螺絲，以微調氣體偵測的門檻值。
</br></br></br>

## 7.4 電容式觸控感測器
---
本範例示範 VCP-G 開發板如何與電容式觸控感測器介接，並控制麵包板上的 LED。電容式觸控感測器會藉由感測電容值的變化來偵測手指的實體接觸。  
當偵測到觸碰時，感測器會向 VCP-G 輸出數位 HIGH 訊號，進而點亮 LED。此範例可確認觸碰輸入已正確辨識，且 GPIO 輸出會隨之反應。觸碰偵測狀態也會顯示在序列埠監控視窗上。
</br></br>

### 7.4.1 硬體需求
- VCP-G 開發板 (x1)
- 麵包板 (x1)
- 電容式觸碰感測器 (x1)
- LED (x1)
- 12V 1A 電源變壓器 (x1)
- USB Type-C 轉 A 傳輸線 (x1)
- 公對公杜邦線 (x6)
</br></br>

### 7.4.2 電路
- 觸碰感測器 
    - 觸碰感測器模組的 SIG 腳位連接至 VCP-G 開發板上的 39 號腳位。
    - 觸碰感測器模組的 VCC 腳位連接至 VCP-G 開發板上的 5V。
    - 觸碰感測器模組的 GND 腳位連接至 VCP-G 開發板上的 GND。
- LED
    - LED 的 (+) 腳位連接至 VCP-G 開發板上的 7 號腳位。
    - LED 的 (–) 腳位連接至麵包板上的 GND 排。

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/F_touchsensor.png" width="600"></p>
<p align="center"><strong>圖 7.4 觸碰感測器電路圖</strong></p>

#### 7.4.2.1 腳位對應
下表列出腳位對應。

<p align="center"><strong>表 7.5 觸碰感測器腳位對應</strong></p>
<div align="center">
	<table>
	    <tr>
	        <th colspan="3">腳位名稱</th>
	        <th>VCP-G 開發板</th>
	        <th>GPIO</th>
	    </tr>
	    <tr>
	        <td colspan="3">觸碰感測器 SIG 腳位</td>
	        <td>39</td>
	        <td>K[12]</td>
	    </tr>
	        <tr>
	        <td colspan="3">觸碰感測器 VCC 腳位</td>
	        <td>5V</td>
	        <td>-</td>
	    </tr>
	    <tr>
	        <td colspan="3">觸碰感測器 GND 腳位</td>
	        <td>GND</td>
		    <td>-</td>
		</tr>
	    <tr>
	        <td colspan="3">LED (+) 腳位</td>
	        <td>7</td>
	        <td>B[01]</td>
	    </tr>
	    <tr>
	        <td colspan="3">LED (-) 腳位</td>
	        <td>GND</td>
	        <td>-</td>
	    </tr>
	</table>
</div>

</br></br>

### 7.4.3 執行方式
若要執行本範例，請如下所示修改 main.c 檔案中的 **Main_StartTask()**。
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
編輯程式碼後，請前往下列目錄並執行建置指令：  
```
$ cd ~/vcp/build/tcc70xx/gcc
$ make
```
這會產生韌體映像檔，並使用 FWDN 工具將產生的映像檔燒錄至 VCP-G。  
程式碼成功燒錄並執行後，電容式觸碰感測器會監控來自人體手指的觸碰輸入。當偵測到觸碰時（感測器輸出為 HIGH），序列埠監控視窗會列印訊息並點亮 LED。當未偵測到觸碰時，LED 會熄滅。這可確認 VCP-G 正確讀取觸碰感測器的輸入，並據以控制 GPIO 輸出。

**註**：若要變更觸碰感測器或 LED 所使用的 GPIO 腳位，請參閱原始碼中的設定區段。
</br></br></br></br>

# 8. 參考資料
---
- 如需更多詳細資訊，請聯絡 TOPST：topst@topst.ai

**註：**參考文件可依合約條款於可提供時提供。若參考
文件無法提供，則可就與您的開發直接相關的內容提供指引。
