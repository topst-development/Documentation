# 1. はじめに
---
本ドキュメントでは、FreeRTOS 環境で VCP-G を使用するためのガイドラインを説明します。FreeRTOS 環境で VCP-G を使用して組み込みアプリケーションを容易に開発できるよう、設定手順とサンプルコードを掲載しています。

具体的には、本ドキュメントでは以下を含む VCP-G 向けの FreeRTOS ベースのサンプルアプリケーションについて説明します。 
- デジタル出力/入力
- SPI
- I2C
- UART
- PWM
- Additional Example

VCP-G を使用する前に、図 1.1 を参照してください。
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/vcp-g%20pinout%20Diagram.png"></p>
<p align="center"><strong>図 1.1 VCP-G ピンアウト図</strong></p>
</br>

各サンプルを実行するには、以下の場所にある `main.c` ファイルを変更する必要があります。
```
$ ~/vcp/sources/app.sample/app.base/main.c
```
必要な変更を行った後、提供されている Makefile を使用してプロジェクトをコンパイルし、ファームウェアバイナリを生成します。
</br></br></br></br>

# 2. デジタル入出力
---
本章では、VCP-G ボードのデジタルピンを使用して LED を制御するサンプルを提供します。VCP-G では、デジタルピンはバイナリ信号 (HIGH または LOW) の送受信に使用され、LED、スイッチ、センサーなどの部品を制御するために不可欠です。 

この章では、デジタル出力と入力を使用して LED とボタンを制御する方法を示す 2 つのサンプルプロジェクトを扱い、デジタルピン機能の基本的な理解を深めます。
</br></br></br>

## 2.1 デジタル出力
---
この例では、FreeRTOS 環境で VCP-G ボードを使用してブレッドボード上の LED を制御する方法を説明します。  
関連するソースファイルは以下の場所にあります。  

```
$ ~/vcp/sources/app.sample/app.base/main.c
```
作業を進める前に、VCP-G FreeRTOS SDK が正しくインストールされていることを確認してください。インストールとセットアップの手順については、VCP-G FreeRTOS SDK Getting Started ガイドを参照してください。

この例を実装するには、main.c ファイルを変更し、LED に接続された GPIO ピンをデジタル出力として設定します。4 つの LED を順番に 1 つずつ点灯させ、その後逆の順序で消灯させる FreeRTOS タスクを作成します。動作の順序を明確に確認できるよう、各 LED の切り替えには 500 ms の遅延を入れてください。
</br></br>

### 2.1.1 ハードウェア要件  
- VCP-G ボード (x1)
- ブレッドボード (x1)
- LED (x4)
- 12V 1A 電源アダプター (x1)
- USB Type-C to A ケーブル (x1) 
- オス-オス ジャンパーワイヤー (x9)
</br></br>

### 2.1.2 回路
- LED01
    - (+) ピンは、VCP-G ボードの 7 番ピンに接続します。
    - (–) ピンは、ブレッドボードの GND レールに接続します。
- LED02
    - (+) ピンは、VCP-G ボードの 6 番ピンに接続します。
    - (–) ピンは、ブレッドボードの GND レールに接続します。
- LED03
    - (+) ピンは、VCP-G ボードの 5 番ピンに接続します。
    - (–) ピンは、ブレッドボードの GND レールに接続します。
- LED04
    - (+) ピンは、VCP-G ボードの 4 番ピンに接続します。
    - (–) ピンは、ブレッドボードの GND レールに接続します。 

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/F_digital_out.png" width="600"></p>
<p align="center"><strong>図 2.1 vcp4LED 回路図</strong></p>

#### 2.1.2.1 ピンマッピング
次の表はピンマッピングを示しています。

<p align="center"><strong>表 2.1 vcp4LED のピンマッピング</strong></p>
<div align="center">	
	<table>
		<tr>
			<th colspan="3">ピン名</th>
	        <th>VCP-G ボード</th>
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
この例を実行するには、main.c ファイルの **Main_StartTask()** を以下のように変更します。
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
コードを編集したら、以下のディレクトリに移動してビルドコマンドを実行します。  
```
$ cd ~/vcp/build/tcc70xx/gcc
$ make
```
これによりファームウェアイメージが生成され、***FWDN*** ツールを使用して生成されたイメージが VCP-G に書き込まれます。  
コードが正常に書き込まれて実行されると、接続された 4 つの LED が LED01 から LED04 まで順番に点灯し、その後逆の順序で消灯します。各切り替えは 500 ms の遅延を伴って行われ、滑らかな点滅パターンが得られます。
</br></br></br>

## 2.2 デジタル入力
---
この例では、FreeRTOS 環境で VCP-G ボードを使用してプッシュボタンの入力を読み取り、それによって LED を制御する方法を説明します。
関連するソースファイルは以下の場所にあります。
``` 
$ ~/vcp/sources/app.sample/app.base/main.c
```
この例を実装するには、main.c を変更し、1 本の GPIO ピンをデジタル入力 (ボタンに接続) として、4 本の GPIO ピンをデジタル出力 (LED に接続) として設定します。  
FreeRTOS タスクがボタンの状態を継続的に監視し、ボタンが押されると LED1 と LED3 が点灯します。
ボタンが押されていない場合は、代わりに LED2 と LED4 が点灯します。
</br></br>

### 2.2.1 ハードウェア要件
- VCP-G ボード (x1)
- ブレッドボード (x1)
- LED (x4)
- ボタンスイッチ (センサー) (x1)
- 12V 1A 電源アダプター (x1)
- USB Type-C to A ケーブル (x1)
- オス-オス ジャンパーワイヤー (x11)
</br></br>

### 2.2.2 回路
- LED01
    - (+) ピンは、VCP-G ボードの 7 番ピンに接続します。
    - (–) ピンは、ブレッドボードの GND レールに接続します。
- LED02
    - (+) ピンは、VCP-G ボードの 6 番ピンに接続します。
    - (–) ピンは、ブレッドボードの GND レールに接続します。
- LED03
    - (+) ピンは、VCP-G ボードの 5 番ピンに接続します。
    - (–) ピンは、ブレッドボードの GND レールに接続します。
- LED04
    - (+) ピンは、VCP-G ボードの 4 番ピンに接続します。
    - (–) ピンは、ブレッドボードの GND レールに接続します。 
- ボタンスイッチ
    - ボタンスイッチの一方の脚は、VCP-G ボードの 2 番ピンに接続します。
    - ボタンの対角線上にある脚は、ブレッドボードの電源レールに接続します。

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/F_digital_in.png" width="600"></p>
<p align="center"><strong>図 2.2 vcp4LED_Button 回路図</strong></p>

#### 2.2.2.1 ピンマッピング
次の表はピンマッピングを示しています。

<p align="center"><strong>表 2.2 vcp4LED_Button のピンマッピング</strong></p>
<div align="center">
	<table>
	    <tr>
	        <th colspan="3">ピン名</th>
	        <th>VCP-G ボード</th>
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
	        <td colspan="3">ボタンの一方の脚のピン</td>
	        <td>2</td>
	        <td>B[28]</td>
	    </tr>
	</table>
</div>
</br></br>

### 2.2.3 実行方法
この例を実行するには、main.c ファイルの **Main_StartTask()** を以下のように変更します。
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
コードを編集したら、以下のディレクトリに移動してビルドコマンドを実行します。  
```
$ cd ~/vcp/build/tcc70xx/gcc
$ make
```
これによりファームウェアイメージが生成され、***FWDN*** ツールを使用して生成されたイメージが VCP-G に書き込まれます。  
コードが正常に書き込まれて実行されると、ボタンを押している間は LED01 と LED03 が点灯し、ボタンを離すと LED02 と LED04 が点灯します。
システムはボタンの状態を継続的に監視し、50 ms のポーリング間隔で LED の状態をリアルタイムに更新します。
</br></br></br></br>

# 3. VCP-G I2C
---
この章では、FreeRTOS が動作する VCP-G で Inter-integrated Circuit (I2C) 通信を設定する手順を説明します。  
I2C は、複数のデバイス間で効率的にデータを交換するために設計された 2 線式の同期通信プロトコルです。シリアルデータライン (SDA) とシリアルクロックライン (SCL) で動作し、複数の周辺機器が固有のアドレスを使用してマイクロコントローラと通信できます。I2C はマスター・スレーブ通信とマルチマスター構成の両方に対応しているため、必要な接続数を最小限に抑えながら、センサー、ディスプレイ、その他の低速デバイスを接続するのに適しています。
</br></br></br>

## 3.1 vcpI2C_LCD1602
---
このサンプルプログラムでは、VCP-G ボードが I2C 通信プロトコルを使用して LCD1602 ディスプレイを制御する方法を説明します。LCD1602 は、組み込みシステムのプロジェクトで一般的に使用される 16 文字 2 行の液晶ディスプレイです。LiquidCrystal_I2C ライブラリを利用することで、ボードは I2C バス経由でコマンドとデータを送信し、ディスプレイを効率的に制御します。  
この例では、LCD を初期化し、視認性を高めるためにバックライトを有効にします。その後、プログラムはカーソルを移動して画面に "Hello TOPST" というテキストを表示します。
</br></br>

### 3.1.1 ハードウェア要件
- VCP-G ボード (x1)
- LCD1602 (x1)
- 12V 1A 電源アダプター (x1)
- USB Type-C to A ケーブル (x1)
- オス-メス ジャンパーワイヤ (x4)
</br></br>

### 3.1.2 回路
- LCD1602
    - LCD1602 の VCC ピンは、VCP-G ボードのアナログピン 5V に接続されます。
    - LCD1602 の GND ピンは、VCP-G ボードの GND に接続されます。
    - LCD1602 の SDA ピンは、VCP-G ボードの 7 番ピンに接続します。
    - LCD1602 の SCL ピンは、VCP-G ボードの 8 番ピンに接続します。

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/F_i2c.png" width="600"></p>
<p align="center"><strong>図 3.1 vcpI2C_LCD1602 の回路図</strong></p>

#### 3.1.2.1 ピンマッピング
次の表はピンマッピングを示しています。

<p align="center"><strong>表 3.1 vcpI2C_LCD1602 のピンマッピング</strong></p>
<div align="center">
	<table>
	    <tr>
	        <th colspan="3">ピン名</th>
	        <th>VCP-G ボード</th>
	        <th>GPIO</th>
	    </tr>
	    <tr>
	        <td colspan="3">LCD1602 VCC ピン</td>
	        <td>5V</td>
	        <td>-</td>
	    </tr>
	        <tr>
	        <td colspan="3">LCD1602 GND ピン</td>
	        <td>GND</td>
	        <td>-</td>
	    </tr>
	        <tr>
	        <td colspan="3">LCD1602 SDA ピン</td>
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
この例を実行するには、main.c ファイルの **Main_StartTask()** を以下のように変更します。
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
#### 追加の設定に関する注意事項
I2C 経由で LCD のテストを有効にするには、以下の手順に従ってください。  

**1. ビルドシステムで lcd.c を有効にする**  
- 以下のパスに移動します。
```
$ vi ~/vcp/sources/dev.drivers/i2c/rules.mk
```
- 以下の行を見つけます。
```
#SRCS += lcd.c
```
- その行のコメントを解除してファイルを有効にします。
```
SRCS += lcd.c
```

**2. LCD の関数ロジックを確認または変更する**  
LCD の初期化、コマンド、出力関数のロジックを確認または編集する必要がある場合は、以下を参照してください。
```
$ vi ~/vcp/sources/dev.drivers/i2c/lcd.c
```

**3. I2C チャンネルとポートを設定する**  
LCD が使用する I2C チャンネル番号と関連するポートは、以下で変更できます。
```
$ vi ~/vcp/sources/dev.drivers/i2c/lcd.h
```

コードを編集したら、以下のディレクトリに移動して次のビルドコマンドを実行します。  
```
$ cd ~/vcp/build/tcc70xx/gcc
$ make
```
これによりファームウェアイメージが生成され、***FWDN*** ツールを使用して生成されたイメージが VCP-G に書き込まれます。  
コードが正常に書き込まれて実行されると、LCD の画面に "Hello TOPST" というメッセージが表示され、I2C 通信が正しく動作していることを確認できます。  
</br></br></br></br>

# 4. VCP SPI
---
この章では、VCP-G で Serial Peripheral Interface (SPI) 通信を設定する手順について説明します。  
SPI は、マイクロコントローラと周辺機器の間でデータを交換するために使用される高速の同期通信プロトコルです。データ送信 (MOSI および MISO)、クロック同期 (SCK)、デバイス選択 (SS) 用の独立した信号線で動作し、効率的で信頼性の高い通信を実現します。  
</br></br></br>

## 4.1 vcpSPI_Dot8x8
---
このサンプルプログラムでは、VCP-G ボードが SPI を介して MAX7219 ドライバを使用し、8x8 LED ドットマトリクスを制御する方法を説明します。
この例では、あらかじめ定義されたバイナリ配列を使用して、ドットマトリックスに文字「X」を表示します。表示は SPI 通信を通じて更新され、MAX7219 が内部で行と列の制御を行います。
この例は、LED マトリックスなどの外部表示デバイスを制御するために、SPI 経由でデータパターンを送信する方法を理解するのに役立ちます。
</br></br>

### 4.1.1 ハードウェア要件
- VCP-G ボード (x1)
- 8x8 ドットマトリクス (x1)
- 12V 1A 電源アダプター (x1)
- USB Type-C to A ケーブル (x1)
- オス-メス ジャンパーワイヤー (x2)
- メス-メス ジャンパーワイヤ (x3)
</br></br>

### 4.1.2 回路
- 8x8 ドットマトリクス
    - 8x8 ドットマトリクスの VCC ピンは、VCP-G ボードのアナログピン 5V に接続されます。
    - 8x8 ドットマトリクスの GND ピンは、VCP-G ボードの GND に接続されます。
    - 8x8 ドットマトリックスの DIN ピンは、VCP-G ボードの SPI ピン 4 に接続されています。
    - 8x8 ドットマトリックスの CS ピンは、VCP-G ボードの SPI ピン 5 に接続されています。
    - 8x8 ドットマトリックスの CLS ピンは、VCP-G ボードの SPI ピン 3 に接続されています。

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/F_spi.png" width="600"></p>
<p align="center"><strong>図 4.1 vcpSPI_Dot8x8 回路図</strong></p>

#### 4.1.2.1 ピンマップ
次の表はピンマッピングを示しています。

<p align="center"><strong>表 4.1 vcpSPI_Dot8x8 のピンマップ</strong></p>
<div align="center">
	<table>
	    <tr>
	        <th colspan="3">ピン名</th>
	        <th>VCP-G ボード</th>
	        <th>GPIO</th>
	    </tr>
	    <tr>
	        <td colspan="3">8x8 ドットマトリクス VCC ピン</td>
	        <td>5V</td>
	        <td>-</td>
	    </tr>
	        <tr>
	        <td colspan="3">8x8 ドットマトリクス GND ピン</td>
	        <td>GND</td>
	        <td>-</td>
	    </tr>
	    <tr>
	        <td colspan="3">8x8 ドットマトリクス DIN ピン</td>
	        <td>SPI 4</td>
	        <td>B[06]</td>
	    </tr>
	    <tr>
	        <td colspan="3">8x8 ドットマトリクス CS ピン</td>
	        <td>SPI 5</td>
	        <td>B[05]</td>
	    </tr>
	    <tr>
	        <td colspan="3">8x8 ドットマトリクス CLK ピン</td>
	        <td>SPI 3</td>
	        <td>B[04]</td>
	    </tr>
	</table>
</div>
</br></br>

### 4.1.3 実行方法
この例を実行するには、main.c ファイルの **Main_StartTask()** を以下のように変更します。
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
#### 追加の設定に関する注意事項
SPI によるドットマトリックスのテストを有効にするには、次の手順に従ってください:  
**1. ビルドシステムで dot_matrix.c を有効にする**  
- 以下のパスに移動します。
```
$ vi ~/vcp/sources/dev.drivers/gpsb/rules.mk
```
- 次の行を見つけます:
```
#SRCS += dot_matrix.c
```
- コメントを解除してファイルを有効にします:
```
SRCS += dot_matrix.c
```
**2. ドットマトリックスの機能ロジックの確認または変更**  
ドットマトリックスの初期化、制御コマンド、または表示パターンのロジックを確認または編集するには、次のソースファイルを参照してください:
```
$ vi ~/vcp/sources/dev.drivers/gpsb/dot_matrix.c
```
**3. SPI チャネルと GPIO の設定**  
ドットマトリックスで使用する SPI チャネルおよび関連する GPIO ピンは、次のヘッダファイルで設定できます:
```
$ vi ~/vcp/sources/dev.drivers/gpsb/dot_matrix.h
```
コードを編集したら、以下のディレクトリに移動してビルドコマンドを実行します。  
```
$ cd ~/vcp/build/tcc70xx/gcc
$ make
```
これによりファームウェアイメージが生成され、***FWDN*** ツールを使用して生成されたイメージが VCP-G に書き込まれます。  
コードが正常に書き込まれて実行されると、8x8 LED ドットマトリックスに文字「X」が表示され、MAX7219 ドライバとの SPI 通信が正しく動作していることを確認できます。 
</br></br></br></br>

# 5. VCP-G UART
---
この章では、VCP-G で Universal Asynchronous Receiver-Transmitter (UART) 通信を設定する手順について説明します。  
UART は、送信 (TX) と受信 (RX) の 2 本の線のみを使用してデータを非同期に転送する、広く使用されているシリアル通信プロトコルです。共通のクロック信号を必要とせずに、マイクロコントローラ、センサー、コンピュータ間でデータをやり取りするために不可欠です。  
以降の章では、UART を介してデータを送受信する方法について説明します。
</br></br></br>

## 5.1 UART 通信テスト (FT232BL)
---
この例では、FT232BL USB to TTL シリアルモジュールを使用して、VCP-G ボードの UART 通信を検証する方法を説明します。
VCP-G ボードの UART TX ピンと RX ピンは FT232BL モジュールに接続され、そのモジュールは USB を介して PC に接続されます。
PC 上では MobaXterm などのターミナルプログラムを使用して、送信されたメッセージを確認します。
</br></br>

### 5.1.1 ハードウェア要件
- VCP-G ボード (x1)
- FT232BL USB to TTL シリアルモジュール (x1)
- ミニ USB ケーブル (x1)
- 12V 1A 電源アダプター (x1)
- USB Type-C to A ケーブル (x1)
- オス-メス ジャンパーワイヤー (x2)
</br></br>

### 5.1.2 回路
- FT232BL
    - FT232BL モジュールの RXD ピンは、VCP-G ボードのピン 18 (TXD) に接続されています。
    - FT232BL モジュールの TXD ピンは、VCP-G ボードのピン 19 (RXD) に接続されています。

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/F_uart.png" width="600"></p>
<p align="center"><strong>図 5.1 vcpUART 回路図</strong></p>

#### 5.1.2.1 ピンマップ
次の表はピンマッピングを示しています。

<p align="center"><strong>表 4.1 vcpUART のピンマップ</strong></p>
<div align="center">
	<table>
	    <tr>
	        <th colspan="3">ピン名</th>
	        <th>VCP-G ボード</th>
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
この例を実行するには、main.c ファイルの **Main_StartTask()** を以下のように変更します。
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
#### 追加の設定に関する注意事項
UART テストを有効にするには、次の手順に従ってください:  
**1. ビルドシステムで uart_example.c を有効にする**  
- 以下のパスに移動します。
```
$ vi ~/vcp/sources/dev.drivers/uart/rules.mk
```
- 次の行を見つけます:
```
#SRCS += uart_example.c
```
- コメントを解除してファイルを有効にします:
```
SRCS += uart_example.c
```
**2. UART の機能ロジックの確認または変更**  
UART の初期化、データの送受信、または割り込み処理のロジックを確認または編集するには、次のソースファイルを参照してください:
```
$ vi ~/vcp/sources/dev.drivers/uart/tcc70xx/uart_example.c
```
**3. UART チャネルと GPIO の設定**  
UART テストで使用する UART チャネル、ボーレート、および関連する TX/RX GPIO ピンは、次のヘッダファイルで設定できます:
```
$ vi ~/vcp/sources/dev.drivers/uart/uart_example.h
```
コードを編集したら、以下のディレクトリに移動してビルドコマンドを実行します。  
```
$ cd ~/vcp/build/tcc70xx/gcc
$ make
```
これによりファームウェアイメージが生成され、***FWDN*** ツールを使用して生成されたイメージが VCP-G に書き込まれます。  
コードが正常に書き込まれて実行されると、シリアルターミナルに「[UART] Hello from UART!」というメッセージが 1 回表示され、FT232BL USB to TTL モジュールを介した VCP-G ボードからの UART 送信が正常に動作していることを確認できます。
</br></br></br></br>

# 6. VCP-G PWM
---
この章では、VCP-G で PWM (Pulse Width Modulation) を設定する手順を説明します。PWM は、デジタル信号のデューティ比を変化させることで、モーター、LED、ブザーなどのデバイスに供給される電力量を制御する技術です。出力ピンを高い周波数でオン・オフすることで動作し、全周期に対するオン時間の比率が実効的な出力レベルを決定します。以降の章では、VCP-G 上で FreeRTOS を使用して PWM 信号を生成する方法と、それを外部部品の制御に適用する方法を説明します。
</br></br></br>

## 6.1 pwmFade
---
このサンプルプログラムは、VCP ボードが PWM を使用してブレッドボード上の LED の明るさをループ内で徐々に上げ下げして制御する方法を示します。LED が最大の明るさに達すると、LED の明るさは減少し始めます。プログラムは LED の明るさを継続的に調整し、フェード効果を作り出します。
</br></br>

### 6.1.1 ハードウェア要件
- VCP-G ボード (x1)
- ブレッドボード (x1)
- LED (x1)
- 12V 1A 電源アダプター (x1)
- USB Type-C to A ケーブル (x1)
- オス-オス ジャンパーワイヤ (x2)
</br></br>

### 6.1.2 回路
- LED
    - (+) ピンは、VCP-G ボードのピン 45 に接続されています。
    - (–) ピンは、ブレッドボードの GND レールに接続します。

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/F_pwm.png" width="600"></p>
<p align="center"><strong>図 5.1 pwmFade 回路図</strong></p>

#### 6.1.2.1 ピンマップ
次の表はピンマッピングを示しています。

<p align="center"><strong>表 4.1 pwmFade のピンマップ</strong></p>
<div align="center">
	<table>
	    <tr>
	        <th colspan="3">ピン名</th>
	        <th>VCP-G ボード</th>
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
この例を実行するには、main.c ファイルの **Main_StartTask()** を以下のように変更します。
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
コードを編集したら、以下のディレクトリに移動してビルドコマンドを実行します。  
```
$ cd ~/vcp/build/tcc70xx/gcc
$ make
```
これによりファームウェアイメージが生成され、***FWDN*** ツールを使用して生成されたイメージが VCP-G に書き込まれます。  
コードが正常に書き込まれて実行されると、GPIO A10 の PWM によって駆動される LED の緩やかなフェードインおよびフェードアウト効果を確認でき、VCP-G の PDM ベースの PWM 出力が正しく機能していることを確認できます。

**注意**: PWM 出力に使用する GPIO ポートを変更するには、pdm.c ファイル内の設定を参照してください。
</br></br></br></br>

# 7. 追加のサンプル
---
この章では、VCP-G ボード上で FreeRTOS を使用する追加のセンサー例を紹介します。VCP-G ボードで FreeRTOS とともによく使用される Arduino のセンサーを使用する方法のサンプルガイドを提供し、さまざまなセンサーをプロジェクトに効果的に統合できるようにします。
</br></br></br>

## 7.1 赤外線 (IR) センサー（トランシーバー）
---
この例では、VCP-G ボードがブレッドボード上の IR センサーと 2 つの LED を制御する方法を示します。IR センサーが物体を検出すると (センサー値が LOW)、1 番目の LED が点灯し、2 番目の LED が消灯します。逆に物体が検出されない場合 (センサー値が HIGH)、2 番目の LED が点灯し、1 番目の LED が消灯します。物体の有無はシリアルモニタにも出力されます。
</br></br>

### 7.1.1 ハードウェア要件
- VCP-G ボード (x1)
- ブレッドボード (x1)
- IR トランシーバーセンサー (x1)
- LED (x2: 異なる色を推奨します)
- 12V 1A 電源アダプター (x1)
- USB Type-C to A ケーブル (x1)
- オス-オス ジャンパワイヤ (x5)
- オス-メス ジャンパーワイヤ (x3)
</br></br>

### 7.1.2 回路
- IR トランシーバーセンサー
    - IR センサーの OUT ピンは、VCP-G ボードのピン 38 に接続されています。
    - IR センサーの VCC ピンは、VCP-G ボードの 5V に接続します。
    - IR センサーの GND ピンは、VCP-G ボードの GND に接続します。
- LED01
    - (+) ピンは、VCP-G ボードのピン 16 に接続されています。
    - (–) ピンは、ブレッドボードの GND レールに接続します。
- LED02
    - (+) ピンは、VCP-G ボードのピン 17 に接続されています。
    - (–) ピンは、ブレッドボードの GND レールに接続します。

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/F_irsensor1.png" width="600"></p>
<p align="center"><strong>図 7.1 赤外線 (IR) センサー回路図</strong></p>

##### 7.1.2.1 ピンマップ
次の表はピンマッピングを示しています。

<p align="center"><strong>表 7.1 irSensor_LED のピンマップ</strong></p>
<div align="center">
	<table>
	    <tr>
	        <th colspan="3">ピン名</th>
	        <th>VCP-G ボード</th>
	        <th>GPIO</th>
	    </tr>
	    <tr>
	        <td colspan="3">IR センサー OUT ピン </td>
	        <td>38</td>
	        <td>K[13]</td>
	    </tr>
	        <tr>
	        <td colspan="3">IR センサー VCC ピン </td>
	        <td>5V</td>
	        <td>-</td>
	    </tr>
	    <tr>
	        <td colspan="3">IR センサー GND ピン</td>
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
	        <td colspan="3">LED02 (-) ピン </td>
	        <td>GND</td>
	        <td>-</td>
	    </tr>
	</table>
</div>
</br></br>

### 7.1.3 実行方法
この例を実行するには、main.c ファイルの **Main_StartTask()** を以下のように変更します。
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
コードを編集したら、以下のディレクトリに移動してビルドコマンドを実行します。  
```
$ cd ~/vcp/build/tcc70xx/gcc
$ make
```
これによりファームウェアイメージが生成され、***FWDN*** ツールを使用して生成されたイメージが VCP-G に書き込まれます。  
コードが正常に書き込まれて実行されると、IR センサーが物体の有無を検出し、それに応じて 2 つの LED を制御します。物体が検出されると 1 番目の LED が点灯し、検出されない場合は 2 番目の LED が点灯します。この動作により、VCP-G ボードの IR センサー入力と GPIO 出力が正常に動作していることを確認できます。

**注意**: IR センサーまたは LED に使用する GPIO ピンを変更する必要がある場合は、ソースコード内の設定セクションを参照してください。
</br></br></br>

## 7.2 赤外線 (IR) センサー (受信機)
---
この例では、VCP-G ボードが IR 受信センサーを使用してリモコンからの信号を検出する方法を示します。IR 信号を受信すると、オンボードのロジックがブレッドボードに接続された LED を点灯させます。これにより、IR 受信モジュールが受信信号を正しくデコードし、VCP-G が期待どおりに応答していることを確認できます。受信状態はシリアルモニタにも表示されます。
</br></br>

### 7.2.1 ハードウェア要件
- VCP-G ボード (x1)
- ブレッドボード (x1)
- IR 受信センサー (x1)
- Arduino リモコン (x1)
- LED (x1)
- 12V 1A 電源アダプター (x1)
- USB Type-C to A ケーブル (x1)
- オス-オス ジャンパワイヤ (x5)
</br></br>

### 7.2.2 回路
- IR 受信センサー
    - IR センサーの SIG ピンは、VCP-G ボードのピン 40 に接続されています。
    - IR センサーの GND ピンは、VCP-G ボードの GND に接続します。
    - IR センサーの VCC ピンは、VCP-G ボードの 5V に接続します。
- LED
    - (+) ピンは、VCP-G ボードの 7 番ピンに接続します。
    - (–) ピンは、ブレッドボードの GND レールに接続します。

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/F_irsensor2.png" width="600"></p>
<p align="center"><strong>図 7.2 IR 受信センサー回路図</strong></p>

##### 7.2.2.1 ピンマップ
次の表はピンマッピングを示しています。

<p align="center"><strong>表 7.1 irSensor_LED のピンマップ</strong></p>
<div align="center">
	<table>
	    <tr>
	        <th colspan="3">ピン名</th>
	        <th>VCP-G ボード</th>
	        <th>GPIO</th>
	    </tr>
	    <tr>
	        <td colspan="3">IR センサー SIG ピン </td>
	        <td>40</td>
	        <td>K[11]</td>
	    </tr>
	        <tr>
	        <td colspan="3">IR センサー GND ピン </td>
	        <td>GND</td>
	        <td>-</td>
	    </tr>
	    <tr>
	        <td colspan="3">IR センサー VCC ピン</td>
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
この例を実行するには、main.c ファイルの **Main_StartTask()** を以下のように変更します。
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
コードを編集したら、以下のディレクトリに移動してビルドコマンドを実行します。  
```
$ cd ~/vcp/build/tcc70xx/gcc
$ make
```
これによりファームウェアイメージが生成され、***FWDN*** ツールを使用して生成されたイメージが VCP-G に書き込まれます。  
コードが正常に書き込まれて実行されると、IR 受信機がリモコンからの信号を検出し、短時間 LED を点灯させます。これにより、VCP-G が IR 入力を正しく読み取り、受信した信号に応じて GPIO 出力を制御していることを確認できます。

**注意**: IR センサーまたは LED に使用する GPIO ピンを変更するには、ソースコード内の設定セクションを参照してください。
</br></br></br>

## 7.3 ガスセンサー
---
このサンプルは、VCP-G ボードがガスセンサー (MQ 135) を使用して空気中のさまざまな有害ガスを検知する方法を示します。VCP-G ボードのアナログピンに接続されたセンサーからアナログ値を読み取り、電圧に変換した後、小数点以下 1 桁でシリアルモニタに出力します。

**注:** Gas Sensor (MQ-135) は Winsen® の製品です。そのデザイン、商標および関連する知的財産に関するすべての権利は Winsen が所有しています。
</br></br>

### 7.3.1 ハードウェア要件
- VCP-G ボード (x1)
- ガスセンサー (MQ135) (x1)
- 12V 1A 電源アダプター (x1)
- USB Type-C to A ケーブル (x1)
- オス-メス ジャンパーワイヤ (x3)
</br></br>

### 7.3.2 回路
- ガスセンサー
    - ガスセンサーの A0 ピンは、VCP-G ボードのアナログピン 55 に接続されています。 
    - ガスセンサーの VCC ピンは、VCP-G ボードの 5V に接続します。
    - ガスセンサーの GND ピンは、VCP-G ボードの GND に接続します。

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/F_gassensor.png" width="600"></p>
<p align="center"><strong>図 7.3 ガスセンサー回路図</strong></p>

#### 7.3.2.1 ピンマップ
次の表はピンマッピングを示しています。

<p align="center"><strong>表 7.3 ガスセンサーのピンマップ</strong></p>
<div align="center">
	<table>
	    <tr>
	        <th colspan="3">ピン名</th>
	        <th>VCP-G ボード</th>
	        <th>GPIO</th>
	    </tr>
	    <tr>
	        <td colspan="3">ガスセンサー A0 ピン</td>
	        <td>55</td>
	        <td>K[15]</td>
	    </tr>
	        <tr>
	        <td colspan="3">ガスセンサー VCC ピン</td>
	        <td>5V</td>
	        <td>-</td>
	    </tr>
	    <tr>
	        <td colspan="3">ガスセンサー GND ピン</td>
	        <td>GND</td>
	        <td>-</td>
	    </tr>
	</table>
</div>
</br></br>

### 7.3.3 実行方法
この例を実行するには、main.c ファイルの **Main_StartTask()** を以下のように変更します。
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
コードを編集したら、以下のディレクトリに移動してビルドコマンドを実行します。  
```
$ cd ~/vcp/build/tcc70xx/gcc
$ make
```
これによりファームウェアイメージが生成され、**FWDN** ツールを使用して生成されたイメージを VCP-G に書き込みます。  
コードが正常に書き込まれて実行されると、ガスセンサーが周囲の空気の状態を継続的に監視します。ガスが検出されると (センサー出力が LOW)、ガス検出を示すメッセージがシリアルモニタに表示され、そうでない場合はクリーンな空気であることが報告されます。これにより、VCP-G がガスセンサーからのデジタル入力を正しく読み取っていることを確認できます。

**注意**: ガスセンサーに使用する GPIO ピンを変更するには、ソースコード内の設定セクションを参照してください。ほとんどのガスセンサーモジュールには、感度調整用の小さな調整ネジ (ポテンショメータ) が付いています。センサーが安定して反応しない場合は、このネジを調整してガス検出のしきい値を微調整してください。
</br></br></br>

## 7.4 静電容量式タッチセンサー
---
この例では、VCP-G ボードが静電容量式タッチセンサーと接続し、ブレッドボード上の LED を制御する方法を示します。静電容量式タッチセンサーは、静電容量の変化を検知することで指による物理的な接触を検出します。  
タッチが検出されると、センサーは VCP-G にデジタルの HIGH 信号を出力し、VCP-G はそれに応じて LED を点灯させます。この例により、タッチ入力が正しく認識され、GPIO 出力がそれに応じて反応することを確認できます。タッチ検出状態はシリアルモニタにも表示されます。
</br></br>

### 7.4.1 ハードウェア要件
- VCP-G ボード (x1)
- ブレッドボード (x1)
- 静電容量式タッチセンサー (x1)
- LED (x1)
- 12V 1A 電源アダプター (x1)
- USB Type-C to A ケーブル (x1)
- オス-オス ジャンパーワイヤ (x6)
</br></br>

### 7.4.2 回路
- タッチセンサー 
    - タッチセンサーモジュールの SIG ピンは、VCP-G ボードのピン 39 に接続されています。
    - タッチセンサーモジュールの VCC ピンは、VCP-G ボードの 5V に接続されています。
    - タッチセンサーモジュールの GND ピンは、VCP-G ボードの GND に接続されます。
- LED
    - LED の (+) ピンは、VCP-G ボードの 7 番ピンに接続されます。
    - LED の (–) ピンは、ブレッドボードの GND レールに接続されます。

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/F_touchsensor.png" width="600"></p>
<p align="center"><strong>図 7.4 タッチセンサー回路図</strong></p>

#### 7.4.2.1 ピンマッピング
次の表はピンマッピングを示しています。

<p align="center"><strong>表 7.5 タッチセンサーのピンマッピング</strong></p>
<div align="center">
	<table>
	    <tr>
	        <th colspan="3">ピン名</th>
	        <th>VCP-G ボード</th>
	        <th>GPIO</th>
	    </tr>
	    <tr>
	        <td colspan="3">タッチセンサー SIG ピン</td>
	        <td>39</td>
	        <td>K[12]</td>
	    </tr>
	        <tr>
	        <td colspan="3">タッチセンサー VCC ピン</td>
	        <td>5V</td>
	        <td>-</td>
	    </tr>
	    <tr>
	        <td colspan="3">タッチセンサー GND ピン</td>
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
この例を実行するには、main.c ファイルの **Main_StartTask()** を以下のように変更します。
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
コードを編集したら、以下のディレクトリに移動してビルドコマンドを実行します。  
```
$ cd ~/vcp/build/tcc70xx/gcc
$ make
```
これによりファームウェアイメージが生成され、FWDN ツールを使用して生成されたイメージを VCP-G に書き込みます。  
コードが正常に書き込まれて実行されると、静電容量式タッチセンサーが人の指によるタッチ入力を検出します。タッチが検出されると（センサー出力が HIGH）、シリアルモニタにメッセージが表示され、LED が点灯します。タッチが検出されない場合、LED は消灯します。これにより、VCP-G がタッチセンサーからの入力を正しく読み取り、GPIO 出力を適切に制御していることを確認できます。

**注意**: タッチセンサーまたは LED に使用する GPIO ピンを変更する場合は、ソースコード内の設定部分を参照してください。
</br></br></br></br>

# 8. 参考資料
---
- 詳細については TOPST にお問い合わせください: topst@topst.ai

**注意:** 参考文書は、契約条件に応じて提供可能な場合に提供されます。参考
文書が入手できない場合は、お客様の開発に直接関連する内容をご案内できます。
