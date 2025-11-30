# 1. はじめに
---
このドキュメントでは、FreeRTOSでVCP-Gを使用するためのガイドラインを提供します。FreeRTOS環境下でVCP-Gを使用して組み込みアプリケーションを簡単に開発できるように、構成手順とサンプルコードが含まれています。
 
具体的には、このドキュメントでは、以下を含むVCP-G用のFreeRTOSベースのサンプルアプリケーションに関するガイダンスを提供します。
- デジタル出力/入力
- SPI
- I2C
- UART
- PWM
- その他の例
 
VCP-Gを使用する前に、図 1.1を参照してください。
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/vcp-g%20pinout%20Diagram.png"></p>
<p align="center"><strong>図 1.1 VCP-G ピン配列図</strong></p>
</br>
 
各例を実行するには、次の場所にある `main.c` ファイルを変更する必要があります。
```
$ ~/vcp/sources/app.sample/app.base/main.c
```
必要な変更を行った後、提供されたMakefileを使用してプロジェクトをコンパイルし、ファームウェアバイナリを生成します。
</br></br></br></br>
 
# 2. デジタル入力/出力
---
この章では、VCP-Gボードのデジタルピンを使用してLEDを制御する例を示します。VCP-Gでは、デジタルピンはバイナリ信号（HIGHまたはLOW）の送受信に使用されるため、LED、スイッチ、センサーなどのコンポーネントの制御に不可欠です。
 
この章には、デジタル出力と入力を使用してLEDとボタンを制御する方法を示す2つのサンプルプロジェクトが含まれており、デジタルピン機能の基本的な理解を提供します。
</br></br></br>
 
## 2.1 デジタル出力
---
この例は、FreeRTOS環境下でVCP-Gボードを使用してブレッドボード上のLEDを制御する方法を示しています。
関連するソースファイルは次の場所にあります。
 
```
$ ~/vcp/sources/app.sample/app.base/main.c
```
続行する前に、VCP-G FreeRTOS SDKが正しくインストールされていることを確認してください。インストールとセットアップの手順については、VCP-G FreeRTOS SDK Getting Startedガイドを参照してください。
 
この例を実装するには、main.cファイルを変更して、LEDに接続されたGPIOピンをデジタル出力として構成します。4つのLEDを順番に点灯させ、逆の順序で消灯するFreeRTOSタスクを作成する必要があります。シーケンスを明確に観察するために、各LEDの遷移には500ミリ秒の遅延を含める必要があります。
</br></br>
 
### 2.1.1 ハードウェア要件
- VCP-Gボード (x1)
- ブレッドボード (x1)
- LED (x4)
- 12V 1A電源アダプター (x1)
- USB Type-C to Aケーブル (x1)
- オス-オス ジャンパーワイヤー (x9)
</br></br>
 
### 2.1.2 回路
- LED01
    - (+) ピンはVCP-Gボードのピン7に接続されています。
    - (–) ピンはブレッドボードのGNDレールに接続されています。
- LED02
    - (+) ピンはVCP-Gボードのピン6に接続されています。
    - (–) ピンはブレッドボードのGNDレールに接続されています。
- LED03
    - (+) ピンはVCP-Gボードのピン5に接続されています。
    - (–) ピンはブレッドボードのGNDレールに接続されています。
- LED04
    - (+) ピンはVCP-Gボードのピン4に接続されています。
    - (–) ピンはブレッドボードのGNDレールに接続されています。
 
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/F_digital_out.png" width="600"></p>
<p align="center"><strong>図 2.1 vcp4LED回路図</strong></p>
 
#### 2.1.2.1 ピンマッピング
次の表はピンマッピングを示しています。
 
<p align="center"><strong>表 2.1 vcp4LEDのピンマッピング</strong></p>
<div align="center">	
	<table>
		<tr>
			<th colspan="3">ピン名</th>
	        <th>VCP-Gボード</th>
	        <th>GPIO</th>
	    </tr>
	    <tr>
	        <td colspan="3">LED01 (+) ピン</td>
	        <td>7</td>
	        <td>B[01]</td>
	    </tr>
	        <tr>
	        <td colspan="3">LED02 (+) ピン</td>
	        <td>6</td>
	        <td>A[13]</td>
	    </tr>
	        <tr>
	        <td colspan="3">LED03 (+) ピン</td>
	        <td>5</td>
	        <td>B[10]</td>
	    </tr>
	        <tr>
	        <td colspan="3">LED04 (+) ピン</td>
	        <td>4</td>
	        <td>B[27]</td>
	    </tr>
	</table>
</div>
</br></br>
 
### 2.1.3 実行方法
この例を実行するには、main.cファイルの **Main_StartTask()** を次のように変更します。
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
コードを編集した後、次のディレクトリに移動してビルドコマンドを実行します。
```
$ cd ~/vcp/build/tcc70xx/gcc
$ make
```
これによりファームウェア画像が生成され、***FWDN*** ツールを使用して生成された画像をVCP-Gにフラッシュします。
コードが正常にフラッシュされて実行されると、接続された4つのLEDがLED01からLED04へと順番に点灯し、その後逆の順序で消灯します。各遷移は500ミリ秒の遅延で発生し、スムーズな点滅パターンを作成します。
</br></br></br>
 
## 2.2 デジタル入力
---
この例は、FreeRTOS環境下でVCP-Gボードを使用してプッシュボタンからの入力を読み取り、それを使用してLEDを制御する方法を示しています。
関連するソースファイルは次の場所にあります。
``` 
$ ~/vcp/sources/app.sample/app.base/main.c
```
この例を実装するには、main.cを変更して、1つのGPIOピンをデジタル入力（ボタンに接続）として、4つのGPIOピンをデジタル出力（LEDに接続）として構成します。
FreeRTOSタスクはボタンの状態を継続的に監視し、ボタンが押されるとLED1とLED3が点灯します。
ボタンが押されていないときは、代わりにLED2とLED4が点灯します。
</br></br>
 
### 2.2.1 ハードウェア要件
- VCP-Gボード (x1)
- ブレッドボード (x1)
- LED (x4)
- ボタンスイッチ (センサー) (x1)
- 12V 1A電源アダプター (x1)
- USB Type-C to Aケーブル (x1)
- オス-オス ジャンパーワイヤー (x11)
</br></br>
 
### 2.2.2 回路
- LED01
    - (+) ピンはVCP-Gボードのピン7に接続されています。
    - (–) ピンはブレッドボードのGNDレールに接続されています。
- LED02
    - (+) ピンはVCP-Gボードのピン6に接続されています。
    - (–) ピンはブレッドボードのGNDレールに接続されています。
- LED03
    - (+) ピンはVCP-Gボードのピン5に接続されています。
    - (–) ピンはブレッドボードのGNDレールに接続されています。
- LED04
    - (+) ピンはVCP-Gボードのピン4に接続されています。
    - (–) ピンはブレッドボードのGNDレールに接続されています。
- ボタンスイッチ
    - ボタンスイッチの片方の足はVCP-Gボードのピン2に接続されています。
    - ボタンの対角線上にある反対側の足は、ブレッドボードの電源レールに接続されています。
 
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/F_digital_in.png" width="600"></p>
<p align="center"><strong>図 2.2 vcp4LED_Button回路図</strong></p>
 
#### 2.2.2.1 ピンマッピング
次の表はピンマッピングを示しています。
 
<p align="center"><strong>表 2.2 vcp4LED_Buttonのピンマッピング</strong></p>
<div align="center">
	<table>
	    <tr>
	        <th colspan="3">ピン名</th>
	        <th>VCP-Gボード</th>
	        <th>GPIO</th>
	    </tr>
	    <tr>
	        <td colspan="3">LED01 (+) ピン</td>
	        <td>7</td>
	        <td>B[01]</td>
	    </tr>
	        <tr>
	        <td colspan="3">LED02 (+) ピン</td>
	        <td>6</td>
	        <td>A[13]</td>
	    </tr>
	        <tr>
	        <td colspan="3">LED03 (+) ピン</td>
	        <td>5</td>
	        <td>B[10]</td>
	    </tr>
	        <tr>
	        <td colspan="3">LED04 (+) ピン</td>
	        <td>4</td>
	        <td>B[27]</td>
	    </tr>
	    </tr>
	        <tr>
	        <td colspan="3">ボタンの片方の足のピン</td>
	        <td>2</td>
	        <td>B[28]</td>
	    </tr>
	</table>
</div>
</br></br>
 
### 2.2.3 実行方法
この例を実行するには、main.cファイルの **Main_StartTask()** を次のように変更します。
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
コードを編集した後、次のディレクトリに移動してビルドコマンドを実行します。
```
$ cd ~/vcp/build/tcc70xx/gcc
$ make
```
これによりファームウェア画像が生成され、***FWDN*** ツールを使用して生成された画像をVCP-Gにフラッシュします。
コードが正常にフラッシュされて実行されると、ボタンを押すとLED01とLED03が点灯し、ボタンを放すとLED02とLED04が点灯します。
システムはボタンの状態を継続的に監視し、50ミリ秒のポーリング間隔でLEDの状態をリアルタイムに更新します。
</br></br></br></br>
 
# 3. VCP-G I2C
---
この章では、FreeRTOSを実行しているVCP-GでInter-integrated Circuit (I2C) 通信を構成するための手順を説明します。
I2Cは、複数のデバイス間で効率的にデータを交換するために設計された2線式の同期通信プロトコルです。シリアルデータライン (SDA) とシリアルクロックライン (SCL) で動作し、複数の周辺機器が一意のアドレスを使用してマイクロコントローラーと通信できるようにします。I2Cはマスター/スレーブ通信とマルチマスター構成の両方をサポートしているため、センサー、ディスプレイ、その他の低速デバイスを接続するのに最適であり、必要な接続数を最小限に抑えることができます。
</br></br></br>
 
## 3.1 vcpI2C_LCD1602
---
このサンプルプログラムは、VCP-GボードがI2C通信プロトコルを使用してLCD1602ディスプレイを制御する方法を示しています。LCD1602は、組み込みシステムプロジェクトで一般的に使用される16文字2行の液晶ディスプレイです。LiquidCrystal_I2Cライブラリを利用することで、ボードはI2Cバスを介してコマンドとデータを送信し、ディスプレイを効率的に制御します。
この例では、LCDが初期化され、バックライトが有効になって視認性が向上します。その後、プログラムはカーソルを配置して、画面に「Hello TOPST」というテキストを表示します。
</br></br>
 
### 3.1.1 ハードウェア要件
- VCP-Gボード (x1)
- LCD1602 (x1)
- 12V 1A電源アダプター (x1)
- USB Type-C to Aケーブル (x1)
- オス-メス ジャンパーワイヤー (x4)
</br></br>
 
### 3.1.2 回路
- LCD1602
    - LCD1602のVCCピンは、VCP-Gボードのアナログピン5Vに接続されています。
    - LCD1602のGNDピンは、VCP-GボードのGNDに接続されています。
    - LCD1602のSDAピンは、VCP-Gボードのピン7に接続されています。
    - LCD1602のSCLピンは、VCP-Gボードのピン8に接続されています。
 
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/F_i2c.png" width="600"></p>
<p align="center"><strong>図 3.1 vcpI2C_LCD1602回路図</strong></p>
 
#### 3.1.2.1 ピンマッピング
次の表はピンマッピングを示しています。
 
<p align="center"><strong>表 3.1 vcpI2C_LCD1602のピンマッピング</strong></p>
<div align="center">
	<table>
	    <tr>
	        <th colspan="3">ピン名</th>
	        <th>VCP-Gボード</th>
	        <th>GPIO</th>
	    </tr>
	    <tr>
	        <td colspan="3">LCD1602 VCCピン</td>
	        <td>5V</td>
	        <td>-</td>
	    </tr>
	        <tr>
	        <td colspan="3">LCD1602 GNDピン</td>
	        <td>GND</td>
	        <td>-</td>
	    </tr>
	        <tr>
	        <td colspan="3">LCD1602 SDAピン</td>
	        <td>7</td>
	        <td>B[01]</td>
	    </tr>
	        <tr>
	        <td colspan="3">LED (-) ピン</td>
	        <td>8</td>
	        <td>B[00]</td>
	    </tr>
	</table>
</div>
 
</br></br>
 
### 3.1.3 実行方法
この例を実行するには、main.cファイルの **Main_StartTask()** を次のように変更します。
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
#### 追加の構成に関する注記
I2Cを介したLCDテストを有効にするには、次の手順に従います。
 
**1. ビルドシステムでlcd.cを有効にする**
- 次のパスに移動します。
```
$ vi ~/vcp/sources/dev.drivers/i2c/rules.mk
```
- 次の行を見つけます。
```
#SRCS += lcd.c
```
- コメントを外してファイルをアクティブにします。
```
SRCS += lcd.c
```
 
**2. LCD機能ロジックの確認または変更**
LCDの初期化、コマンド、または印刷機能のロジックを検査または編集する必要がある場合は、以下を参照してください。
```
$ vi ~/vcp/sources/dev.drivers/i2c/lcd.c
```
 
**3. I2Cチャネルとポートの構成**
LCDで使用されるI2Cチャネル番号と関連ポートは、以下で変更できます。
```
$ vi ~/vcp/sources/dev.drivers/i2c/lcd.h
```
 
コードを編集した後、次のディレクトリに移動して次のビルドコマンドを実行します。
```
$ cd ~/vcp/build/tcc70xx/gcc
$ make
```
これによりファームウェア画像が生成され、***FWDN*** ツールを使用して生成された画像をVCP-Gにフラッシュします。
コードが正常にフラッシュされて実行されると、LCD画面に「Hello TOPST」というメッセージが表示され、I2C通信が正常に機能していることが確認されます。
</br></br></br></br>

# 4. VCP SPI
---
この章では、VCP-GでSerial Peripheral Interface (SPI) 通信を構成するための手順を説明します。
SPIは、マイクロコントローラーと周辺機器間でデータを交換するために使用される高速同期通信プロトコルです。データ送信 (MOSIおよびMISO)、クロック同期 (SCK)、およびデバイス選択 (SS) 用の個別のラインで動作し、効率的で信頼性の高い通信を保証します。
</br></br></br>
 
## 4.1 vcpSPI_Dot8x8
---
このサンプルプログラムは、VCP-GボードがSPIを介してMAX7219ドライバーを使用して8x8 LEDドットマトリックスを制御する方法を示しています。
この例では、事前定義されたバイナリ配列を使用して、ドットマトリックスに文字「X」を表示します。ディスプレイはSPI通信を介して更新され、MAX7219は内部で行と列の制御を処理します。
この例は、SPI経由でデータパターンを送信して、LEDマトリックスなどの外部ディスプレイデバイスを制御する方法を説明するのに役立ちます。
</br></br>
 
### 4.1.1 ハードウェア要件
- VCP-Gボード (x1)
- 8x8ドットマトリックス (x1)
- 12V 1A電源アダプター (x1)
- USB Type-C to Aケーブル (x1)
- オス-メス ジャンパーワイヤー (x2)
- メス-メス ジャンパーワイヤー (x3)
</br></br>
 
### 4.1.2 回路
- 8x8ドットマトリックス
    - 8x8ドットマトリックスのVCCピンは、VCP-Gボードのアナログピン5Vに接続されています。
    - 8x8ドットマトリックスのGNDピンは、VCP-GボードのGNDに接続されています。
    - 8x8ドットマトリックスのDINピンは、VCP-GボードのSPIピン4に接続されています。
    - 8x8ドットマトリックスのCSピンは、VCP-GボードのSPIピン5に接続されています。
    - 8x8ドットマトリックスのCLSピンは、VCP-GボードのSPIピン3に接続されています。
 
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/F_spi.png" width="600"></p>
<p align="center"><strong>図 4.1 vcpSPI_Dot8x8回路図</strong></p>
 
#### 4.1.2.1 ピンマッピング
次の表はピンマッピングを示しています。
 
<p align="center"><strong>表 4.1 vcpSPI_Dot8x8のピンマッピング</strong></p>
<div align="center">
	<table>
	    <tr>
	        <th colspan="3">ピン名</th>
	        <th>VCP-Gボード</th>
	        <th>GPIO</th>
	    </tr>
	    <tr>
	        <td colspan="3">8x8ドットマトリックス VCCピン</td>
	        <td>5V</td>
	        <td>-</td>
	    </tr>
	        <tr>
	        <td colspan="3">8x8ドットマトリックス GNDピン</td>
	        <td>GND</td>
	        <td>-</td>
	    </tr>
	    <tr>
	        <td colspan="3">8x8ドットマトリックス DINピン</td>
	        <td>SPI 4</td>
	        <td>B[06]</td>
	    </tr>
	    <tr>
	        <td colspan="3">8x8ドットマトリックス CSピン</td>
	        <td>SPI 5</td>
	        <td>B[05]</td>
	    </tr>
	    <tr>
	        <td colspan="3">8x8ドットマトリックス CLKピン</td>
	        <td>SPI 3</td>
	        <td>B[04]</td>
	    </tr>
	</table>
</div>
</br></br>
 
### 4.1.3 実行方法
この例を実行するには、main.cファイルの **Main_StartTask()** を次のように変更します。
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
#### 追加の構成に関する注記
SPIを介したドットマトリックスのテストを有効にするには、次の手順に従います。
**1. ビルドシステムでdot_matrix.cを有効にする**
- 次のパスに移動します。
```
$ vi ~/vcp/sources/dev.drivers/gpsb/rules.mk
```
- 次の行を見つけます。
```
#SRCS += dot_matrix.c
```
- コメントを外してファイルをアクティブにします。
```
SRCS += dot_matrix.c
```
**2. ドットマトリックス機能ロジックの確認または変更**
ドットマトリックスの初期化、制御コマンド、または表示パターンのロジックを検査または編集するには、次のソースファイルを参照してください。
```
$ vi ~/vcp/sources/dev.drivers/gpsb/dot_matrix.c
```
**3. SPIチャネルとGPIOの構成**
ドットマトリックスで使用されるSPIチャネルと関連するGPIOピンは、次のヘッダーファイルで構成できます。
```
$ vi ~/vcp/sources/dev.drivers/gpsb/dot_matrix.h
```
コードを編集した後、次のディレクトリに移動してビルドコマンドを実行します。
```
$ cd ~/vcp/build/tcc70xx/gcc
$ make
```
これによりファームウェア画像が生成され、***FWDN*** ツールを使用して生成された画像をVCP-Gにフラッシュします。
コードが正常にフラッシュされて実行されると、8x8 LEDドットマトリックスに文字「X」が表示され、MAX7219ドライバーとのSPI通信が正常に機能していることが確認されます。
</br></br></br></br>
 
# 5. VCP-G UART
---
この章では、VCP-GでUniversal Asynchronous Receiver-Transmitter (UART) 通信を構成するための手順を説明します。
UARTは、送信 (TX) と受信 (RX) の2本のラインのみを使用して非同期でデータを送信する、広く使用されているシリアル通信プロトコルです。共有クロック信号を必要とせずに、マイクロコントローラー、センサー、コンピューター間でデータを交換するために不可欠です。
次の章では、UARTを介してデータを送受信する方法について説明します。
</br></br></br>
 
## 5.1 UART通信テスト (FT232BL)
---
この例は、FT232BL USB-TTLシリアルモジュールを使用して、VCP-GボードでのUART通信を確認する方法を示しています。
VCP-GボードのUART TXおよびRXピンはFT232BLモジュールに接続され、FT232BLモジュールはUSBを介してPCに接続されます。
PC上でMobaXtermなどのターミナルプログラムを使用して、送信されたメッセージを表示します。
</br></br>
 
### 5.1.1 ハードウェア要件
- VCP-Gボード (x1)
- FT232BL USB-TTLシリアルモジュール (x1)
- ミニUSBケーブル (x1)
- 12V 1A電源アダプター (x1)
- USB Type-C to Aケーブル (x1)
- オス-メス ジャンパーワイヤー (x2)
</br></br>
 
### 5.1.2 回路
- FT232BL
    - FT232BLモジュールのRXDピンは、VCP-Gボードのピン18 (TXD) に接続されています。
    - FT232BLモジュールのTXDピンは、VCP-Gボードのピン19 (RXD) に接続されています。
 
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/F_uart.png" width="600"></p>
<p align="center"><strong>図 5.1 vcpUART回路図</strong></p>
 
#### 5.1.2.1 ピンマッピング
次の表はピンマッピングを示しています。
 
<p align="center"><strong>表 4.1 vcpUARTのピンマッピング</strong></p>
<div align="center">
	<table>
	    <tr>
	        <th colspan="3">ピン名</th>
	        <th>VCP-Gボード</th>
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
 
### 5.1.3 実行方法
この例を実行するには、main.cファイルの **Main_StartTask()** を次のように変更します。
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
#### 追加の構成に関する注記
UARTテストを有効にするには、次の手順に従います。
**1. ビルドシステムでuart_example.cを有効にする**
- 次のパスに移動します。
```
$ vi ~/vcp/sources/dev.drivers/uart/rules.mk
```
- 次の行を見つけます。
```
#SRCS += uart_example.c
```
- コメントを外してファイルをアクティブにします。
```
SRCS += uart_example.c
```
**2. UART機能ロジックの確認または変更**
UARTの初期化、データ送受信、または割り込み処理のロジックを検査または編集するには、次のソースファイルを参照してください。
```
$ vi ~/vcp/sources/dev.drivers/uart/tcc70xx/uart_example.c
```
**3. UARTチャネルとGPIOの構成**
UARTテストに使用されるUARTチャネル、ボーレート、および関連するTX/RX GPIOピンは、次のヘッダーファイルで構成できます。
```
$ vi ~/vcp/sources/dev.drivers/uart/uart_example.h
```
コードを編集した後、次のディレクトリに移動してビルドコマンドを実行します。
```
$ cd ~/vcp/build/tcc70xx/gcc
$ make
```
これによりファームウェア画像が生成され、***FWDN*** ツールを使用して生成された画像をVCP-Gにフラッシュします。
コードが正常にフラッシュされて実行されると、シリアルターミナルに「[UART] Hello from UART!」というメッセージが1回表示され、VCP-GボードからのUART送信がFT232BL USB-TTLモジュールを介して正常に機能していることが確認されます。
</br></br></br></br>
 
# 6. VCP-G PWM
---
この章では、VCP-GでPulse Width Modulation (PWM) を構成するための手順を説明します。PWMは、デジタル信号のデューティサイクルを変更することにより、モーター、LED、ブザーなどのデバイスに供給される電力量を制御するために使用される手法です。出力ピンを高周波でオンとオフに切り替えることによって動作し、全周期に対するオン時間の比率が実効出力レベルを決定します。次の章では、VCP-G上のFreeRTOSを使用してPWM信号を生成する方法と、それらを外部コンポーネントの制御に適用する方法について説明します。
</br></br></br>
 
## 6.1 pwmFade
---
このサンプルプログラムは、VCPボードがPWMを使用してループ内で明るさを徐々に上げたり下げたりすることで、ブレッドボード上のLEDを制御する方法を示しています。LEDが最大輝度に達した後、LEDの輝度は低下し始めます。プログラムはLEDの明るさを継続的に調整し、フェード効果を作成します。
</br></br>
 
### 6.1.1 ハードウェア要件
- VCP-Gボード (x1)
- ブレッドボード (x1)
- LED (x1)
- 12V 1A電源アダプター (x1)
- USB Type-C to Aケーブル (x1)
- オス-オス ジャンパーワイヤー (x2)
</br></br>
 
### 6.1.2 回路
- LED
    - (+) ピンはVCP-Gボードのピン45に接続されています。
    - (–) ピンはブレッドボードのGNDレールに接続されています。
 
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/F_pwm.png" width="600"></p>
<p align="center"><strong>図 5.1 pwmFade回路図</strong></p>
 
#### 6.1.2.1 ピンマッピング
次の表はピンマッピングを示しています。
 
<p align="center"><strong>表 4.1 pwmFadeのピンマッピング</strong></p>
<div align="center">
	<table>
	    <tr>
	        <th colspan="3">ピン名</th>
	        <th>VCP-Gボード</th>
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
 
### 6.1.3 実行方法
この例を実行するには、main.cファイルの **Main_StartTask()** を次のように変更します。
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
コードを編集した後、次のディレクトリに移動してビルドコマンドを実行します。
```
$ cd ~/vcp/build/tcc70xx/gcc
$ make
```
これによりファームウェア画像が生成され、***FWDN*** ツールを使用して生成された画像をVCP-Gにフラッシュします。
コードが正常にフラッシュされて実行されると、GPIO A10のPWMによって駆動される段階的なLEDのフェードインおよびフェードアウト効果を観察でき、VCP-GからのPDMベースのPWM出力が正常に機能していることが確認できます。
 
**注**: PWM出力に使用されるGPIOポートを変更するには、pdm.cファイルの構成を参照してください。
</br></br></br></br>
 
# 7. その他の例
---
この章では、VCP-Gボード上のFreeRTOSを使用した追加のセンサー例を紹介します。VCP-Gボード上のFreeRTOSで一般的に使用されるArduinoセンサーを使用する方法に関するサンプルガイドを提供し、さまざまなセンサーをプロジェクトに効果的に統合できるようにします。
</br></br></br>
 
## 7.1 赤外線 (IR) センサー (トランシーバー)
---
この例は、VCP-Gボードがブレッドボード上のIRセンサーと2つのLEDを制御する方法を示しています。IRセンサーが物体を検出すると（センサー値はLOW）、最初のLEDが点灯し、2番目のLEDが消灯します。逆に、物体が検出されない場合（センサー値はHIGH）、2番目のLEDが点灯し、最初のLEDが消灯します。物体の有無もシリアルモニタに出力されます。
</br></br>
 
### 7.1.1 ハードウェア要件
- VCP-Gボード (x1)
- ブレッドボード (x1)
- IRトランシーバーセンサー (x1)
- LED (x2: 異なる色を推奨)
- 12V 1A電源アダプター (x1)
- USB Type-C to Aケーブル (x1)
- オス-オス ジャンパーワイヤー (x5)
- オス-メス ジャンパーワイヤー (x3)
</br></br>
 
### 7.1.2 回路
- IRトランシーバーセンサー
    - IRセンサーのOUTピンは、VCP-Gボードのピン38に接続されています。
    - IRセンサーのVCCピンは、VCP-Gボードの5Vに接続されています。
    - IRセンサーのGNDピンは、VCP-GボードのGNDに接続されています。
- LED01
    - (+) ピンはVCP-Gボードのピン16に接続されています。
    - (–) ピンはブレッドボードのGNDレールに接続されています。
- LED02
    - (+) ピンはVCP-Gボードのピン17に接続されています。
    - (–) ピンはブレッドボードのGNDレールに接続されています。
 
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/F_irsensor1.png" width="600"></p>
<p align="center"><strong>図 7.1 赤外線 (IR) センサー回路図</strong></p>
 
##### 7.1.2.1 ピンマッピング
次の表はピンマッピングを示しています。
 
<p align="center"><strong>表 7.1 irSensor_LEDのピンマッピング</strong></p>
<div align="center">
	<table>
	    <tr>
	        <th colspan="3">ピン名</th>
	        <th>VCP-Gボード</th>
	        <th>GPIO</th>
	    </tr>
	    <tr>
	        <td colspan="3">IRセンサー OUTピン</td>
	        <td>38</td>
	        <td>K[13]</td>
	    </tr>
	        <tr>
	        <td colspan="3">IRセンサー VCCピン</td>
	        <td>5V</td>
	        <td>-</td>
	    </tr>
	    <tr>
	        <td colspan="3">IRセンサー GNDピン</td>
	        <td>GND</td>
	        <td>-</td>
	    </tr>
	    <tr>
	        <td colspan="3">LED01 (+) ピン</td>
	        <td>16</td>
	        <td>A[06]</td>
	    </tr>
	    <tr>
	        <td colspan="3">LED01 (-) ピン</td>
	        <td>GND</td>
	        <td>-</td>
	    </tr>
	    <tr>
	        <td colspan="3">LED02 (+) ピン</td>
	        <td>17</td>
	        <td>A[07]</td>
	    </tr>
	    <tr>
	        <td colspan="3">LED02 (-) ピン</td>
	        <td>GND</td>
	        <td>-</td>
	    </tr>
	</table>
</div>
</br></br>
 
### 7.1.3 実行方法
この例を実行するには、main.cファイルの **Main_StartTask()** を次のように変更します。
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
コードを編集した後、次のディレクトリに移動してビルドコマンドを実行します。
```
$ cd ~/vcp/build/tcc70xx/gcc
$ make
```
これによりファームウェア画像が生成され、***FWDN*** ツールを使用して生成された画像をVCP-Gにフラッシュします。
コードが正常にフラッシュされて実行されると、IRセンサーは物体の有無を検出し、それに応じて2つのLEDを制御します。物体が検出されると、最初のLEDが点灯します。物体が検出されない場合は、2番目のLEDが点灯します。この動作により、VCP-Gボード上のIRセンサー入力とGPIO出力が正常に機能していることが確認されます。
 
**注**: IRセンサーまたはLEDに使用されるGPIOピンを変更する必要がある場合は、ソースコード内の構成セクションを参照してください。
</br></br></br>
 
## 7.2 赤外線 (IR) センサー (レシーバー)
---
この例は、VCP-GボードがIRレシーバーセンサーを使用してリモコンからの信号を検出する方法を示しています。IR信号が受信されると、オンボードロジックがブレッドボードに接続されたLEDを点灯させます。これにより、IRレシーバーモジュールが着信信号を正しくデコードしており、VCP-Gが期待どおりに応答していることが確認されます。受信ステータスもシリアルモニタに表示されます。
</br></br>
 
### 7.2.1 ハードウェア要件
- VCP-Gボード (x1)
- ブレッドボード (x1)
- IRレシーバーセンサー (x1)
- Arduinoリモコン (x1)
- LED (x1)
- 12V 1A電源アダプター (x1)
- USB Type-C to Aケーブル (x1)
- オス-オス ジャンパーワイヤー (x5)
</br></br>
 
### 7.2.2 回路
- IRレシーバーセンサー
    - IRセンサーのSIGピンは、VCP-Gボードのピン40に接続されています。
    - IRセンサーのGNDピンは、VCP-GボードのGNDに接続されています。
    - IRセンサーのVCCピンは、VCP-Gボードの5Vに接続されています。
- LED
    - (+) ピンはVCP-Gボードのピン7に接続されています。
    - (–) ピンはブレッドボードのGNDレールに接続されています。
 
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/F_irsensor2.png" width="600"></p>
<p align="center"><strong>図 7.2 IRレシーバーセンサー回路図</strong></p>
 
##### 7.2.2.1 ピンマッピング
次の表はピンマッピングを示しています。
 
<p align="center"><strong>表 7.1 irSensor_LEDのピンマッピング</strong></p>
<div align="center">
	<table>
	    <tr>
	        <th colspan="3">ピン名</th>
	        <th>VCP-Gボード</th>
	        <th>GPIO</th>
	    </tr>
	    <tr>
	        <td colspan="3">IRセンサー SIGピン</td>
	        <td>40</td>
	        <td>K[11]</td>
	    </tr>
	        <tr>
	        <td colspan="3">IRセンサー GNDピン</td>
	        <td>GND</td>
	        <td>-</td>
	    </tr>
	    <tr>
	        <td colspan="3">IRセンサー VCCピン</td>
	        <td>VCC</td>
	        <td>-</td>
	    </tr>
	    <tr>
	        <td colspan="3">LED (+) ピン</td>
	        <td>7</td>
	        <td>B[01]</td>
	    </tr>
	    <tr>
	        <td colspan="3">LED (-) ピン</td>
	        <td>GND</td>
	        <td>-</td>
	    </tr>
	</table>
</div>
 
</br></br>
 
### 7.2.3 実行方法
この例を実行するには、main.cファイルの **Main_StartTask()** を次のように変更します。
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
コードを編集した後、次のディレクトリに移動してビルドコマンドを実行します。
```
$ cd ~/vcp/build/tcc70xx/gcc
$ make
```
これによりファームウェア画像が生成され、***FWDN*** ツールを使用して生成された画像をVCP-Gにフラッシュします。
コードが正常にフラッシュされて実行されると、IRレシーバーはリモコンからの信号を検出し、短時間LEDを点灯させます。これにより、VCP-GがIR入力を正しく読み取り、受信した信号に応じてGPIO出力を制御していることが確認されます。
 
**注**: IRセンサーまたはLEDに使用されるGPIOピンを変更するには、ソースコード内の構成セクションを参照してください。
</br></br></br>
 
## 7.3 ガスセンサー
---
この例は、VCP-Gボードがガスセンサー (MQ 135) を使用して空気中のさまざまな有害ガスを検出する方法を示しています。VCP-Gボードのアナログピンに接続されたセンサーからアナログ値を読み取り、電圧に変換してから、小数点以下1桁でシリアルモニタに出力します。
 
**注:** ガスセンサー (MQ-135) はWinsen®の製品です。そのデザイン、商標、および関連する知的財産に対するすべての権利はWinsenが所有しています。
</br></br>
 
### 7.3.1 ハードウェア要件
- VCP-Gボード (x1)
- ガスセンサー (MQ135) (x1)
- 12V 1A電源アダプター (x1)
- USB Type-C to Aケーブル (x1)
- オス-メス ジャンパーワイヤー (x3)
</br></br>
 
### 7.3.2 回路
- ガスセンサー
    - ガスセンサーのA0ピンは、VCP-Gボードのアナログピン55に接続されています。
    - ガスセンサーのVCCピンは、VCP-Gボードの5Vに接続されています。
    - ガスセンサーのGNDピンは、VCP-GボードのGNDに接続されています。
 
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/F_gassensor.png" width="600"></p>
<p align="center"><strong>図 7.3 ガスセンサー回路図</strong></p>
 
#### 7.3.2.1 ピンマッピング
次の表はピンマッピングを示しています。
 
<p align="center"><strong>表 7.3 ガスセンサーのピンマッピング</strong></p>
<div align="center">
	<table>
	    <tr>
	        <th colspan="3">ピン名</th>
	        <th>VCP-Gボード</th>
	        <th>GPIO</th>
	    </tr>
	    <tr>
	        <td colspan="3">ガスセンサー A0ピン</td>
	        <td>55</td>
	        <td>K[15]</td>
	    </tr>
	        <tr>
	        <td colspan="3">ガスセンサー VCCピン</td>
	        <td>5V</td>
	        <td>-</td>
	    </tr>
	    <tr>
	        <td colspan="3">ガスセンサー GNDピン</td>
	        <td>GND</td>
	        <td>-</td>
	    </tr>
	</table>
</div>
</br></br>
 
### 7.3.3 実行方法
この例を実行するには、main.cファイルの **Main_StartTask()** を次のように変更します。
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
コードを編集した後、次のディレクトリに移動してビルドコマンドを実行します。
```
$ cd ~/vcp/build/tcc70xx/gcc
$ make
```
これによりファームウェア画像が生成され、**FWDN** ツールを使用して生成された画像をVCP-Gにフラッシュします。
コードが正常にフラッシュされて実行されると、ガスセンサーは周囲の空気品質を継続的に監視します。ガスが検出されると（センサー出力がLOW）、ガス検出を示すメッセージがシリアルモニタに表示されます。それ以外の場合は、きれいな空気を報告します。これにより、VCP-Gがガスセンサーからのデジタル入力を正しく読み取っていることが確認されます。
 
**注**: ガスセンサーに使用されるGPIOピンを変更するには、ソースコード内の構成セクションを参照してください。ほとんどのガスセンサーモジュールには、感度調整用の小さな調整ネジ（ポテンショメータ）が含まれています。センサーが確実に反応しない場合は、このネジを調整してガス検出のしきい値を微調整してみてください。
</br></br></br>
 
## 7.4 静電容量式タッチセンサー
---
この例は、VCP-Gボードが静電容量式タッチセンサーとインターフェースし、ブレッドボード上のLEDを制御する方法を示しています。静電容量式タッチセンサーは、静電容量の変化を感知することで指からの物理的な接触を検出します。
タッチが検出されると、センサーはデジタルHIGH信号をVCP-Gに出力し、VCP-GはLEDを点灯させます。この例では、タッチ入力が正しく認識され、GPIO出力がそれに応じて応答することを確認します。タッチ検出ステータスもシリアルモニタに表示されます。
</br></br>
 
### 7.4.1 ハードウェア要件
- VCP-Gボード (x1)
- ブレッドボード (x1)
- 静電容量式タッチセンサー (x1)
- LED (x1)
- 12V 1A電源アダプター (x1)
- USB Type-C to Aケーブル (x1)
- オス-オス ジャンパーワイヤー (x6)
</br></br>
 
### 7.4.2 回路
- タッチセンサー
    - タッチセンサーモジュールのSIGピンは、VCP-Gボードのピン39に接続されています。
    - タッチセンサーモジュールのVCCピンは、VCP-Gボードの5Vに接続されています。
    - タッチセンサーモジュールのGNDピンは、VCP-GボードのGNDに接続されています。
- LED
    - LEDの(+) ピンは、VCP-Gボードのピン7に接続されています。
    - LEDの(-) ピンは、ブレッドボードのGNDレールに接続されています。
 
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/F_touchsensor.png" width="600"></p>
<p align="center"><strong>図 7.4 タッチセンサー回路図</strong></p>
 
#### 7.4.2.1 ピンマッピング
次の表はピンマッピングを示しています。
 
<p align="center"><strong>表 7.5 タッチセンサーのピンマッピング</strong></p>
<div align="center">
	<table>
	    <tr>
	        <th colspan="3">ピン名</th>
	        <th>VCP-Gボード</th>
	        <th>GPIO</th>
	    </tr>
	    <tr>
	        <td colspan="3">タッチセンサー SIGピン</td>
	        <td>39</td>
	        <td>K[12]</td>
	    </tr>
	        <tr>
	        <td colspan="3">タッチセンサー VCCピン</td>
	        <td>5V</td>
	        <td>-</td>
	    </tr>
	    <tr>
	        <td colspan="3">タッチセンサー GNDピン</td>
	        <td>GND</td>
		    <td>-</td>
		</tr>
	    <tr>
	        <td colspan="3">LED (+) ピン</td>
	        <td>7</td>
	        <td>B[01]</td>
	    </tr>
	    <tr>
	        <td colspan="3">LED (-) ピン</td>
	        <td>GND</td>
	        <td>-</td>
	    </tr>
	</table>
</div>
 
</br></br>
 
### 7.4.3 実行方法
この例を実行するには、main.cファイルの **Main_StartTask()** を次のように変更します。
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
コードを編集した後、次のディレクトリに移動してビルドコマンドを実行します。
```
$ cd ~/vcp/build/tcc70xx/gcc
$ make
```
これによりファームウェア画像が生成され、FWDNツールを使用して生成された画像をVCP-Gにフラッシュします。
コードが正常にフラッシュされて実行されると、静電容量式タッチセンサーは人間の指からのタッチ入力を監視します。タッチが検出されると（センサー出力がHIGH）、メッセージがシリアルモニタに表示され、LEDが点灯します。タッチが検出されない場合、LEDは消灯します。これにより、VCP-Gがタッチセンサーからの入力を正しく読み取り、それに応じてGPIO出力を制御していることが確認されます。
 
**注**: タッチセンサーまたはLEDに使用されるGPIOピンを変更するには、ソースコード内の構成セクションを参照してください。
</br></br></br></br>
 
# 8. 参考文献
---
- 詳細については、TOPSTにお問い合わせください: topst@topst.ai
 
**注:** 参考文献は、契約条件に応じて、利用可能な場合にいつでも提供できます。参考文献が利用できない場合は、開発に直接関連する内容をご案内できます。
