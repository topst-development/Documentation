# 1. 소개
---
이 문서는 FreeRTOS 환경에서 VCP-G를 사용하는 방법에 대한 지침을 제공합니다. FreeRTOS 환경에서 VCP-G를 사용하여 임베디드 애플리케이션을 손쉽게 개발할 수 있도록 설정 방법과 예제 코드를 포함합니다.

특히 이 문서는 다음을 포함하여 VCP-G용 FreeRTOS 기반 예제 애플리케이션에 대한 안내를 제공합니다. 
- 디지털 출력/입력
- SPI
- I2C
- UART
- PWM
- Additional Example

VCP-G를 사용하기 전에 그림 1.1을 참조하십시오.
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/vcp-g%20pinout%20Diagram.png"></p>
<p align="center"><strong>그림 1.1 VCP-G 핀아웃 다이어그램</strong></p>
</br>

각 예제를 실행하려면 다음 위치에 있는 `main.c` 파일을 수정해야 합니다.
```
$ ~/vcp/sources/app.sample/app.base/main.c
```
필요한 변경을 완료한 후 제공된 Makefile을 사용하여 프로젝트를 컴파일하고 펌웨어 바이너리를 생성합니다.
</br></br></br></br>

# 2. 디지털 입력/출력
---
본 장에서는 VCP-G 보드의 디지털 핀을 사용하여 LED를 제어하는 예제를 제공합니다. VCP-G에서 디지털 핀은 이진 신호(HIGH 또는 LOW)를 송수신하는 데 사용되며, LED, 스위치, 센서와 같은 부품을 제어하는 데 필수적입니다. 

이 장에서는 디지털 출력과 입력을 사용하여 LED와 버튼을 제어하는 방법을 보여주는 두 개의 예제 프로젝트를 다루며, 디지털 핀 기능에 대한 기본적인 이해를 돕습니다.
</br></br></br>

## 2.1 디지털 출력
---
이 예제는 FreeRTOS 환경에서 VCP-G 보드를 사용하여 브레드보드의 LED를 제어하는 방법을 보여줍니다.  
관련 소스 파일은 다음 위치에서 확인할 수 있습니다.  

```
$ ~/vcp/sources/app.sample/app.base/main.c
```
진행하기 전에 VCP-G FreeRTOS SDK가 올바르게 설치되어 있는지 확인하십시오. 설치 및 설정 방법은 VCP-G FreeRTOS SDK Getting Started 가이드를 참조하십시오.

이 예제를 구현하려면 main.c 파일을 수정하여 LED에 연결된 GPIO 핀을 디지털 출력으로 설정합니다. 네 개의 LED를 순서대로 하나씩 켠 다음 역순으로 끄는 FreeRTOS 태스크를 생성해야 합니다. 동작 순서를 명확하게 확인할 수 있도록 각 LED 전환에는 500 ms 지연을 포함해야 합니다.
</br></br>

### 2.1.1 하드웨어 요구 사항  
- VCP-G 보드 (x1)
- 브레드보드 (x1)
- LED (x4)
- 12V 1A 전원 어댑터 (x1)
- USB Type-C to A 케이블 (x1) 
- 수-수 점퍼 와이어 (x9)
</br></br>

### 2.1.2 회로
- LED01
    - (+) 핀은 VCP-G 보드의 7번 핀에 연결됩니다.
    - (–) 핀은 브레드보드의 GND 레일에 연결됩니다.
- LED02
    - (+) 핀은 VCP-G 보드의 6번 핀에 연결됩니다.
    - (–) 핀은 브레드보드의 GND 레일에 연결됩니다.
- LED03
    - (+) 핀은 VCP-G 보드의 5번 핀에 연결됩니다.
    - (–) 핀은 브레드보드의 GND 레일에 연결됩니다.
- LED04
    - (+) 핀은 VCP-G 보드의 4번 핀에 연결됩니다.
    - (–) 핀은 브레드보드의 GND 레일에 연결됩니다. 

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/F_digital_out.png" width="600"></p>
<p align="center"><strong>그림 2.1 vcp4LED 회로도</strong></p>

#### 2.1.2.1 핀 매핑
다음 표는 핀 매핑을 나타냅니다.

<p align="center"><strong>표 2.1 vcp4LED의 핀 매핑</strong></p>
<div align="center">	
	<table>
		<tr>
			<th colspan="3">핀 이름</th>
	        <th>VCP-G 보드</th>
	        <th>GPIO</th>
	    </tr>
	    <tr>
	        <td colspan="3">LED01 (+) 핀</td>
	        <td>7</td>
	        <td>B[01]</td>
	    </tr>
	        <tr>
	        <td colspan="3">LED02 (+) 핀</td>
	        <td>6</td>
	        <td>A[13]</td>
	    </tr>
	        <tr>
	        <td colspan="3">LED03 (+) 핀</td>
	        <td>5</td>
	        <td>B[10]</td>
	    </tr>
	        <tr>
	        <td colspan="3">LED04 (+) 핀</td>
	        <td>4</td>
	        <td>B[27]</td>
	    </tr>
	</table>
</div>
</br></br>

### 2.1.3 실행 방법
이 예제를 실행하려면 main.c 파일의 **Main_StartTask()**를 다음과 같이 수정합니다.
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
코드를 편집한 후 다음 디렉터리로 이동하여 빌드 명령을 실행합니다.  
```
$ cd ~/vcp/build/tcc70xx/gcc
$ make
```
이 명령은 펌웨어 이미지를 생성하고 ***FWDN*** 툴을 사용하여 생성된 이미지를 VCP-G에 플래싱합니다.  
코드가 성공적으로 플래싱되어 실행되면 연결된 네 개의 LED가 LED01부터 LED04까지 순차적으로 켜진 다음 역순으로 꺼집니다. 각 전환은 500 ms 지연을 두고 발생하여 부드러운 점멸 패턴을 만듭니다.
</br></br></br>

## 2.2 디지털 입력
---
이 예제는 FreeRTOS 환경에서 VCP-G 보드를 사용하여 푸시 버튼의 입력을 읽고 이를 통해 LED를 제어하는 방법을 보여줍니다.
관련 소스 파일은 다음 위치에서 확인할 수 있습니다.
``` 
$ ~/vcp/sources/app.sample/app.base/main.c
```
이 예제를 구현하려면 main.c를 수정하여 GPIO 핀 하나를 디지털 입력(버튼에 연결)으로, GPIO 핀 네 개를 디지털 출력(LED에 연결)으로 설정합니다.  
FreeRTOS 태스크가 버튼 상태를 지속적으로 모니터링하며, 버튼을 누르면 LED1과 LED3이 켜집니다.
버튼을 누르지 않으면 대신 LED2와 LED4가 켜집니다.
</br></br>

### 2.2.1 하드웨어 요구 사항
- VCP-G 보드 (x1)
- 브레드보드 (x1)
- LED (x4)
- 버튼 스위치 (센서) (x1)
- 12V 1A 전원 어댑터 (x1)
- USB Type-C to A 케이블 (x1)
- Male to male 점퍼 와이어 (x11)
</br></br>

### 2.2.2 회로
- LED01
    - (+) 핀은 VCP-G 보드의 7번 핀에 연결됩니다.
    - (–) 핀은 브레드보드의 GND 레일에 연결됩니다.
- LED02
    - (+) 핀은 VCP-G 보드의 6번 핀에 연결됩니다.
    - (–) 핀은 브레드보드의 GND 레일에 연결됩니다.
- LED03
    - (+) 핀은 VCP-G 보드의 5번 핀에 연결됩니다.
    - (–) 핀은 브레드보드의 GND 레일에 연결됩니다.
- LED04
    - (+) 핀은 VCP-G 보드의 4번 핀에 연결됩니다.
    - (–) 핀은 브레드보드의 GND 레일에 연결됩니다. 
- 버튼 스위치
    - 버튼 스위치의 한쪽 다리는 VCP-G 보드의 2번 핀에 연결됩니다.
    - 버튼의 대각선 반대편 다리는 브레드보드의 전원 레일에 연결됩니다.

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/F_digital_in.png" width="600"></p>
<p align="center"><strong>그림 2.2 vcp4LED_Button 회로도</strong></p>

#### 2.2.2.1 핀 매핑
다음 표는 핀 매핑을 나타냅니다.

<p align="center"><strong>표 2.2 vcp4LED_Button의 핀 매핑</strong></p>
<div align="center">
	<table>
	    <tr>
	        <th colspan="3">핀 이름</th>
	        <th>VCP-G 보드</th>
	        <th>GPIO</th>
	    </tr>
	    <tr>
	        <td colspan="3">LED01 (+) 핀</td>
	        <td>7</td>
	        <td>B[01]</td>
	    </tr>
	        <tr>
	        <td colspan="3">LED02 (+) 핀</td>
	        <td>6</td>
	        <td>A[13]</td>
	    </tr>
	        <tr>
	        <td colspan="3">LED03 (+) 핀</td>
	        <td>5</td>
	        <td>B[10]</td>
	    </tr>
	        <tr>
	        <td colspan="3">LED04 (+) 핀</td>
	        <td>4</td>
	        <td>B[27]</td>
	    </tr>
	    </tr>
	        <tr>
	        <td colspan="3">버튼의 한쪽 다리 핀</td>
	        <td>2</td>
	        <td>B[28]</td>
	    </tr>
	</table>
</div>
</br></br>

### 2.2.3 실행 방법
이 예제를 실행하려면 main.c 파일의 **Main_StartTask()**를 다음과 같이 수정합니다.
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
코드를 편집한 후 다음 디렉터리로 이동하여 빌드 명령을 실행합니다.  
```
$ cd ~/vcp/build/tcc70xx/gcc
$ make
```
이 명령은 펌웨어 이미지를 생성하고 ***FWDN*** 툴을 사용하여 생성된 이미지를 VCP-G에 플래싱합니다.  
코드가 성공적으로 플래싱되어 실행되면 버튼을 누를 때 LED01과 LED03이 켜지고, 버튼을 놓으면 LED02와 LED04가 켜집니다.
시스템은 버튼 상태를 지속적으로 모니터링하고 50 ms 폴링 간격으로 LED 상태를 실시간으로 업데이트합니다.
</br></br></br></br>

# 3. VCP-G I2C
---
이 장에서는 FreeRTOS를 실행하는 VCP-G에서 Inter-integrated Circuit (I2C) 통신을 설정하는 방법을 설명합니다.  
I2C는 여러 장치 간의 효율적인 데이터 교환을 위해 설계된 2선식 동기 통신 프로토콜입니다. 시리얼 데이터 라인(SDA)과 시리얼 클록 라인(SCL)으로 동작하며, 여러 주변 장치가 고유한 주소를 사용하여 마이크로컨트롤러와 통신할 수 있습니다. I2C는 마스터-슬레이브 통신과 멀티 마스터 구성을 모두 지원하므로, 필요한 연결 수를 최소화하면서 센서, 디스플레이 및 기타 저속 장치를 연결하는 데 적합합니다.
</br></br></br>

## 3.1 vcpI2C_LCD1602
---
이 예제 프로그램은 VCP-G 보드가 I2C 통신 프로토콜을 사용하여 LCD1602 디스플레이를 제어하는 방법을 보여줍니다. LCD1602는 임베디드 시스템 프로젝트에서 일반적으로 사용되는 16문자 2줄 액정 디스플레이입니다. LiquidCrystal_I2C 라이브러리를 활용하여 보드는 I2C 버스를 통해 명령과 데이터를 전송하고 디스플레이를 효율적으로 제어합니다.  
이 예제에서는 LCD를 초기화하고 선명한 가시성을 위해 백라이트를 켭니다. 그런 다음 프로그램은 커서를 이동하여 화면에 "Hello TOPST" 텍스트를 표시합니다.
</br></br>

### 3.1.1 하드웨어 요구 사항
- VCP-G 보드 (x1)
- LCD1602 (x1)
- 12V 1A 전원 어댑터 (x1)
- USB Type-C to A 케이블 (x1)
- 수-암 점퍼 와이어 (x4)
</br></br>

### 3.1.2 회로
- LCD1602
    - LCD1602의 VCC 핀은 VCP-G 보드의 아날로그 핀 5V에 연결됩니다.
    - LCD1602의 GND 핀은 VCP-G 보드의 GND에 연결됩니다.
    - LCD1602의 SDA 핀은 VCP-G 보드의 7번 핀에 연결됩니다.
    - LCD1602의 SCL 핀은 VCP-G 보드의 8번 핀에 연결됩니다.

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/F_i2c.png" width="600"></p>
<p align="center"><strong>그림 3.1 vcpI2C_LCD1602 회로도</strong></p>

#### 3.1.2.1 핀 매핑
다음 표는 핀 매핑을 나타냅니다.

<p align="center"><strong>표 3.1 vcpI2C_LCD1602의 핀 매핑</strong></p>
<div align="center">
	<table>
	    <tr>
	        <th colspan="3">핀 이름</th>
	        <th>VCP-G 보드</th>
	        <th>GPIO</th>
	    </tr>
	    <tr>
	        <td colspan="3">LCD1602 VCC 핀</td>
	        <td>5V</td>
	        <td>-</td>
	    </tr>
	        <tr>
	        <td colspan="3">LCD1602 GND 핀</td>
	        <td>GND</td>
	        <td>-</td>
	    </tr>
	        <tr>
	        <td colspan="3">LCD1602 SDA 핀</td>
	        <td>7</td>
	        <td>B[01]</td>
	    </tr>
	        <tr>
	        <td colspan="3">LED (-) 핀</td>
	        <td>8</td>
	        <td>B[00]</td>
	    </tr>
	</table>
</div>

</br></br>

### 3.1.3 실행 방법
이 예제를 실행하려면 main.c 파일의 **Main_StartTask()**를 다음과 같이 수정합니다.
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
#### 추가 설정 참고 사항
I2C를 통해 LCD를 테스트하려면 다음 단계를 따르십시오.  

**1. 빌드 시스템에서 lcd.c 활성화**  
- 다음 경로로 이동합니다.
```
$ vi ~/vcp/sources/dev.drivers/i2c/rules.mk
```
- 다음 줄을 찾습니다.
```
#SRCS += lcd.c
```
- 해당 줄의 주석을 해제하여 파일을 활성화합니다.
```
SRCS += lcd.c
```

**2. LCD 함수 로직 확인 또는 수정**  
LCD 초기화, 명령 또는 출력 함수의 로직을 확인하거나 편집해야 하는 경우 다음을 참조하십시오.
```
$ vi ~/vcp/sources/dev.drivers/i2c/lcd.c
```

**3. I2C 채널 및 포트 설정**  
LCD에서 사용하는 I2C 채널 번호와 관련 포트는 다음에서 변경할 수 있습니다.
```
$ vi ~/vcp/sources/dev.drivers/i2c/lcd.h
```

코드를 편집한 후 다음 디렉터리로 이동하여 다음 빌드 명령을 실행합니다.  
```
$ cd ~/vcp/build/tcc70xx/gcc
$ make
```
이 명령은 펌웨어 이미지를 생성하고 ***FWDN*** 툴을 사용하여 생성된 이미지를 VCP-G에 플래싱합니다.  
코드가 성공적으로 플래싱되어 실행되면 LCD 화면에 "Hello TOPST" 메시지가 표시되며, 이를 통해 I2C 통신이 정상적으로 동작함을 확인할 수 있습니다.  
</br></br></br></br>

# 4. VCP SPI
---
이 장에서는 VCP-G에서 Serial Peripheral Interface(SPI) 통신을 구성하는 방법을 설명합니다.  
SPI는 마이크로컨트롤러와 주변 장치 간에 데이터를 교환하는 데 사용되는 고속 동기 통신 프로토콜입니다. 데이터 전송(MOSI 및 MISO), 클록 동기화(SCK), 장치 선택(SS)을 위한 별도의 라인으로 동작하여 효율적이고 신뢰성 있는 통신을 보장합니다.  
</br></br></br>

## 4.1 vcpSPI_Dot8x8
---
이 예제 프로그램은 VCP-G 보드가 SPI를 통해 MAX7219 드라이버를 사용하여 8x8 LED 도트 매트릭스를 제어하는 방법을 보여줍니다.
이 예제에서는 미리 정의된 이진 배열을 사용하여 도트 매트릭스에 문자 "X"를 표시합니다. 디스플레이는 SPI 통신을 통해 갱신되며, MAX7219가 내부적으로 행과 열 제어를 처리합니다.
이 예제는 LED 매트릭스와 같은 외부 디스플레이 장치를 제어하기 위해 SPI를 통해 데이터 패턴을 전송하는 방법을 설명하는 데 도움이 됩니다.
</br></br>

### 4.1.1 하드웨어 요구 사항
- VCP-G 보드 (x1)
- 8x8 도트 매트릭스 (x1)
- 12V 1A 전원 어댑터 (x1)
- USB Type-C to A 케이블 (x1)
- 수-암 점퍼 와이어 (x2)
- 암-암 점퍼 와이어 (x3)
</br></br>

### 4.1.2 회로
- 8x8 도트 매트릭스
    - 8x8 도트 매트릭스의 VCC 핀은 VCP-G 보드의 아날로그 핀 5V에 연결됩니다.
    - 8x8 도트 매트릭스의 GND 핀은 VCP-G 보드의 GND에 연결됩니다.
    - 8x8 도트 매트릭스의 DIN 핀은 VCP-G 보드의 SPI 4번 핀에 연결됩니다.
    - 8x8 도트 매트릭스의 CS 핀은 VCP-G 보드의 SPI 5번 핀에 연결됩니다.
    - 8x8 도트 매트릭스의 CLS 핀은 VCP-G 보드의 SPI 3번 핀에 연결됩니다.

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/F_spi.png" width="600"></p>
<p align="center"><strong>그림 4.1 vcpSPI_Dot8x8 회로도</strong></p>

#### 4.1.2.1 핀맵
다음 표는 핀 매핑을 나타냅니다.

<p align="center"><strong>표 4.1 vcpSPI_Dot8x8의 핀맵</strong></p>
<div align="center">
	<table>
	    <tr>
	        <th colspan="3">핀 이름</th>
	        <th>VCP-G 보드</th>
	        <th>GPIO</th>
	    </tr>
	    <tr>
	        <td colspan="3">8x8 도트 매트릭스 VCC 핀</td>
	        <td>5V</td>
	        <td>-</td>
	    </tr>
	        <tr>
	        <td colspan="3">8x8 도트 매트릭스 GND 핀</td>
	        <td>GND</td>
	        <td>-</td>
	    </tr>
	    <tr>
	        <td colspan="3">8x8 도트 매트릭스 DIN 핀</td>
	        <td>SPI 4</td>
	        <td>B[06]</td>
	    </tr>
	    <tr>
	        <td colspan="3">8x8 도트 매트릭스 CS 핀</td>
	        <td>SPI 5</td>
	        <td>B[05]</td>
	    </tr>
	    <tr>
	        <td colspan="3">8x8 도트 매트릭스 CLK 핀</td>
	        <td>SPI 3</td>
	        <td>B[04]</td>
	    </tr>
	</table>
</div>
</br></br>

### 4.1.3 실행 방법
이 예제를 실행하려면 main.c 파일의 **Main_StartTask()**를 다음과 같이 수정합니다.
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
#### 추가 설정 참고 사항
SPI를 통해 도트 매트릭스 테스트를 활성화하려면 다음 단계를 따르십시오:  
**1. 빌드 시스템에서 dot_matrix.c 활성화**  
- 다음 경로로 이동합니다.
```
$ vi ~/vcp/sources/dev.drivers/gpsb/rules.mk
```
- 다음 줄을 찾습니다:
```
#SRCS += dot_matrix.c
```
- 주석을 해제하여 파일을 활성화합니다:
```
SRCS += dot_matrix.c
```
**2. 도트 매트릭스 기능 로직 확인 또는 수정**  
도트 매트릭스 초기화, 제어 명령 또는 표시 패턴에 대한 로직을 확인하거나 편집하려면 다음 소스 파일을 참조하십시오:
```
$ vi ~/vcp/sources/dev.drivers/gpsb/dot_matrix.c
```
**3. SPI 채널 및 GPIO 구성**  
도트 매트릭스에서 사용하는 SPI 채널과 관련 GPIO 핀은 다음 헤더 파일에서 구성할 수 있습니다:
```
$ vi ~/vcp/sources/dev.drivers/gpsb/dot_matrix.h
```
코드를 편집한 후 다음 디렉터리로 이동하여 빌드 명령을 실행합니다.  
```
$ cd ~/vcp/build/tcc70xx/gcc
$ make
```
이 명령은 펌웨어 이미지를 생성하고 ***FWDN*** 툴을 사용하여 생성된 이미지를 VCP-G에 플래싱합니다.  
코드가 성공적으로 플래싱되어 실행되면 8x8 LED 도트 매트릭스에 문자 "X"가 표시되며, 이는 MAX7219 드라이버와의 SPI 통신이 올바르게 동작하고 있음을 확인시켜 줍니다. 
</br></br></br></br>

# 5. VCP-G UART
---
이 장에서는 VCP-G에서 Universal Asynchronous Receiver-Transmitter(UART) 통신을 구성하는 방법을 설명합니다.  
UART는 송신(TX)과 수신(RX)의 두 개의 선만 사용하여 데이터를 비동기적으로 전송하는 널리 사용되는 직렬 통신 프로토콜입니다. 공통 클록 신호 없이 마이크로컨트롤러, 센서 및 컴퓨터 간에 데이터를 교환하는 데 필수적입니다.  
다음 장에서는 UART를 통해 데이터를 송수신하는 방법을 설명합니다.
</br></br></br>

## 5.1 UART 통신 테스트 (FT232BL)
---
이 예제에서는 FT232BL USB to TTL 시리얼 모듈을 사용하여 VCP-G 보드의 UART 통신을 검증하는 방법을 설명합니다.
VCP-G 보드의 UART TX 및 RX 핀은 FT232BL 모듈에 연결되고, 이 모듈은 다시 USB를 통해 PC에 연결됩니다.
PC에서는 MobaXterm과 같은 터미널 프로그램을 사용하여 전송된 메시지를 확인합니다.
</br></br>

### 5.1.1 하드웨어 요구 사항
- VCP-G 보드 (x1)
- FT232BL USB to TTL 시리얼 모듈 (x1)
- 미니 USB 케이블 (x1)
- 12V 1A 전원 어댑터 (x1)
- USB Type-C to A 케이블 (x1)
- 수-암 점퍼 와이어 (x2)
</br></br>

### 5.1.2 회로
- FT232BL
    - FT232BL 모듈의 RXD 핀은 VCP-G 보드의 18번 핀(TXD)에 연결됩니다.
    - FT232BL 모듈의 TXD 핀은 VCP-G 보드의 19번 핀(RXD)에 연결됩니다.

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/F_uart.png" width="600"></p>
<p align="center"><strong>그림 5.1 vcpUART 회로도</strong></p>

#### 5.1.2.1 핀맵
다음 표는 핀 매핑을 나타냅니다.

<p align="center"><strong>표 4.1 vcpUART의 핀맵</strong></p>
<div align="center">
	<table>
	    <tr>
	        <th colspan="3">핀 이름</th>
	        <th>VCP-G 보드</th>
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

### 5.1.3 실행 방법
이 예제를 실행하려면 main.c 파일의 **Main_StartTask()**를 다음과 같이 수정합니다.
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
#### 추가 설정 참고 사항
UART 테스트를 활성화하려면 다음 단계를 따르십시오:  
**1. 빌드 시스템에서 uart_example.c 활성화**  
- 다음 경로로 이동합니다.
```
$ vi ~/vcp/sources/dev.drivers/uart/rules.mk
```
- 다음 줄을 찾습니다:
```
#SRCS += uart_example.c
```
- 주석을 해제하여 파일을 활성화합니다:
```
SRCS += uart_example.c
```
**2. UART 기능 로직 확인 또는 수정**  
UART 초기화, 데이터 송수신 또는 인터럽트 처리에 대한 로직을 확인하거나 편집하려면 다음 소스 파일을 참조하십시오:
```
$ vi ~/vcp/sources/dev.drivers/uart/tcc70xx/uart_example.c
```
**3. UART 채널 및 GPIO 구성**  
UART 테스트에 사용되는 UART 채널, 보드레이트 및 관련 TX/RX GPIO 핀은 다음 헤더 파일에서 구성할 수 있습니다:
```
$ vi ~/vcp/sources/dev.drivers/uart/uart_example.h
```
코드를 편집한 후 다음 디렉터리로 이동하여 빌드 명령을 실행합니다.  
```
$ cd ~/vcp/build/tcc70xx/gcc
$ make
```
이 명령은 펌웨어 이미지를 생성하고 ***FWDN*** 툴을 사용하여 생성된 이미지를 VCP-G에 플래싱합니다.  
코드가 성공적으로 플래싱되어 실행되면 시리얼 터미널에 "[UART] Hello from UART!" 메시지가 한 번 표시되며, 이는 FT232BL USB to TTL 모듈을 통한 VCP-G 보드의 UART 전송이 정상적으로 동작하고 있음을 확인시켜 줍니다.
</br></br></br></br>

# 6. VCP-G PWM
---
이 장에서는 VCP-G에서 PWM(Pulse Width Modulation)을 구성하는 방법을 설명합니다. PWM은 디지털 신호의 듀티 사이클을 변화시켜 모터, LED, 부저와 같은 장치에 전달되는 전력량을 제어하는 데 사용되는 기법입니다. 출력 핀을 높은 주파수로 켜고 끄는 방식으로 동작하며, 전체 주기에 대한 온타임의 비율이 실효 출력 레벨을 결정합니다. 다음 장에서는 VCP-G에서 FreeRTOS를 사용하여 PWM 신호를 생성하는 방법과 이를 외부 부품 제어에 적용하는 방법을 설명합니다.
</br></br></br>

## 6.1 pwmFade
---
이 예제 프로그램은 VCP 보드가 PWM을 사용하여 브레드보드의 LED 밝기를 반복적으로 점차 높이고 낮추면서 제어하는 방법을 보여줍니다. LED가 최대 밝기에 도달한 후에는 LED의 밝기가 감소하기 시작합니다. 프로그램은 LED의 밝기를 지속적으로 조정하여 페이딩 효과를 만들어냅니다.
</br></br>

### 6.1.1 하드웨어 요구 사항
- VCP-G 보드 (x1)
- 브레드보드 (x1)
- LED (x1)
- 12V 1A 전원 어댑터 (x1)
- USB Type-C to A 케이블 (x1)
- 수-수 점퍼 와이어 (x2)
</br></br>

### 6.1.2 회로
- LED
    - (+) 핀은 VCP-G 보드의 45번 핀에 연결됩니다.
    - (–) 핀은 브레드보드의 GND 레일에 연결됩니다.

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/F_pwm.png" width="600"></p>
<p align="center"><strong>그림 5.1 pwmFade 회로도</strong></p>

#### 6.1.2.1 핀맵
다음 표는 핀 매핑을 나타냅니다.

<p align="center"><strong>표 4.1 pwmFade의 핀맵</strong></p>
<div align="center">
	<table>
	    <tr>
	        <th colspan="3">핀 이름</th>
	        <th>VCP-G 보드</th>
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

### 6.1.3 실행 방법
이 예제를 실행하려면 main.c 파일의 **Main_StartTask()**를 다음과 같이 수정합니다.
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
코드를 편집한 후 다음 디렉터리로 이동하여 빌드 명령을 실행합니다.  
```
$ cd ~/vcp/build/tcc70xx/gcc
$ make
```
이 명령은 펌웨어 이미지를 생성하고 ***FWDN*** 툴을 사용하여 생성된 이미지를 VCP-G에 플래싱합니다.  
코드가 성공적으로 플래싱되어 실행되면 GPIO A10에서 PWM으로 구동되는 LED의 점진적인 페이드인 및 페이드아웃 효과를 관찰할 수 있으며, 이는 VCP-G의 PDM 기반 PWM 출력이 올바르게 동작하고 있음을 확인시켜 줍니다.

**참고**: PWM 출력에 사용되는 GPIO 포트를 변경하려면 pdm.c 파일의 설정을 참조하십시오.
</br></br></br></br>

# 7. 추가 예제
---
이 장에서는 VCP-G 보드에서 FreeRTOS를 사용하는 추가 센서 예제를 소개합니다. VCP-G 보드에서 FreeRTOS와 함께 일반적으로 사용되는 Arduino 센서를 사용하는 방법에 대한 예제 가이드를 제공하여 다양한 센서를 프로젝트에 효과적으로 통합할 수 있도록 합니다.
</br></br></br>

## 7.1 적외선(IR) 센서(송수신기)
---
이 예제는 VCP-G 보드가 브레드보드의 IR 센서와 두 개의 LED를 제어하는 방법을 보여줍니다. IR 센서가 물체를 감지하면(센서 값이 LOW), 첫 번째 LED가 켜지고 두 번째 LED가 꺼집니다. 반대로 물체가 감지되지 않으면(센서 값이 HIGH), 두 번째 LED가 켜지고 첫 번째 LED가 꺼집니다. 물체의 유무는 시리얼 모니터에도 출력됩니다.
</br></br>

### 7.1.1 하드웨어 요구 사항
- VCP-G 보드 (x1)
- 브레드보드 (x1)
- IR 송수신 센서 (x1)
- LED (x2: 서로 다른 색상을 권장합니다)
- 12V 1A 전원 어댑터 (x1)
- USB Type-C to A 케이블 (x1)
- 수-수 점퍼 와이어 (x5)
- 수-암 점퍼 와이어 (x3)
</br></br>

### 7.1.2 회로
- IR 송수신 센서
    - IR 센서의 OUT 핀은 VCP-G 보드의 38번 핀에 연결됩니다.
    - IR 센서의 VCC 핀은 VCP-G 보드의 5V에 연결됩니다.
    - IR 센서의 GND 핀은 VCP-G 보드의 GND에 연결됩니다.
- LED01
    - (+) 핀은 VCP-G 보드의 16번 핀에 연결됩니다.
    - (–) 핀은 브레드보드의 GND 레일에 연결됩니다.
- LED02
    - (+) 핀은 VCP-G 보드의 17번 핀에 연결됩니다.
    - (–) 핀은 브레드보드의 GND 레일에 연결됩니다.

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/F_irsensor1.png" width="600"></p>
<p align="center"><strong>그림 7.1 적외선(IR) 센서 회로도</strong></p>

##### 7.1.2.1 핀맵
다음 표는 핀 매핑을 나타냅니다.

<p align="center"><strong>표 7.1 irSensor_LED의 핀맵</strong></p>
<div align="center">
	<table>
	    <tr>
	        <th colspan="3">핀 이름</th>
	        <th>VCP-G 보드</th>
	        <th>GPIO</th>
	    </tr>
	    <tr>
	        <td colspan="3">IR 센서 OUT 핀 </td>
	        <td>38</td>
	        <td>K[13]</td>
	    </tr>
	        <tr>
	        <td colspan="3">IR 센서 VCC 핀 </td>
	        <td>5V</td>
	        <td>-</td>
	    </tr>
	    <tr>
	        <td colspan="3">IR 센서 GND 핀</td>
	        <td>GND</td>
	        <td>-</td>
	    </tr>
	    <tr>
	        <td colspan="3">LED01 (+) 핀</td>
	        <td>16</td>
	        <td>A[06]</td>
	    </tr>
	    <tr>
	        <td colspan="3">LED01 (-) 핀</td>
	        <td>GND</td>
	        <td>-</td>
	    </tr>
	    <tr>
	        <td colspan="3">LED02 (+) 핀</td>
	        <td>17</td>
	        <td>A[07]</td>
	    </tr>
	    <tr>
	        <td colspan="3">LED02 (-) 핀 </td>
	        <td>GND</td>
	        <td>-</td>
	    </tr>
	</table>
</div>
</br></br>

### 7.1.3 실행 방법
이 예제를 실행하려면 main.c 파일의 **Main_StartTask()**를 다음과 같이 수정합니다.
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
코드를 편집한 후 다음 디렉터리로 이동하여 빌드 명령을 실행합니다.  
```
$ cd ~/vcp/build/tcc70xx/gcc
$ make
```
이 명령은 펌웨어 이미지를 생성하고 ***FWDN*** 툴을 사용하여 생성된 이미지를 VCP-G에 플래싱합니다.  
코드가 성공적으로 플래싱되어 실행되면 IR 센서가 물체의 유무를 감지하고 그에 따라 두 개의 LED를 제어합니다. 물체가 감지되면 첫 번째 LED가 켜지고, 물체가 감지되지 않으면 두 번째 LED가 켜집니다. 이 동작은 VCP-G 보드의 IR 센서 입력과 GPIO 출력이 정상적으로 동작하고 있음을 확인시켜 줍니다.

**참고**: IR 센서 또는 LED에 사용되는 GPIO 핀을 변경해야 하는 경우 소스 코드 내부의 설정 섹션을 참조하십시오.
</br></br></br>

## 7.2 적외선(IR) 센서 (수신기)
---
이 예제는 VCP-G 보드가 IR 수신기 센서를 사용하여 리모컨의 신호를 감지하는 방법을 보여줍니다. IR 신호가 수신되면 온보드 로직이 브레드보드에 연결된 LED를 켭니다. 이는 IR 수신기 모듈이 수신 신호를 올바르게 디코딩하고 있으며 VCP-G가 예상대로 응답하고 있음을 확인시켜 줍니다. 수신 상태는 시리얼 모니터에도 표시됩니다.
</br></br>

### 7.2.1 하드웨어 요구 사항
- VCP-G 보드 (x1)
- 브레드보드 (x1)
- IR 수신기 센서 (x1)
- Arduino 리모컨 (x1)
- LED (x1)
- 12V 1A 전원 어댑터 (x1)
- USB Type-C to A 케이블 (x1)
- 수-수 점퍼 와이어 (x5)
</br></br>

### 7.2.2 회로
- IR 수신기 센서
    - IR 센서의 SIG 핀은 VCP-G 보드의 40번 핀에 연결됩니다.
    - IR 센서의 GND 핀은 VCP-G 보드의 GND에 연결됩니다.
    - IR 센서의 VCC 핀은 VCP-G 보드의 5V에 연결됩니다.
- LED
    - (+) 핀은 VCP-G 보드의 7번 핀에 연결됩니다.
    - (–) 핀은 브레드보드의 GND 레일에 연결됩니다.

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/F_irsensor2.png" width="600"></p>
<p align="center"><strong>그림 7.2 IR 수신기 센서 회로도</strong></p>

##### 7.2.2.1 핀맵
다음 표는 핀 매핑을 나타냅니다.

<p align="center"><strong>표 7.1 irSensor_LED의 핀맵</strong></p>
<div align="center">
	<table>
	    <tr>
	        <th colspan="3">핀 이름</th>
	        <th>VCP-G 보드</th>
	        <th>GPIO</th>
	    </tr>
	    <tr>
	        <td colspan="3">IR 센서 SIG 핀 </td>
	        <td>40</td>
	        <td>K[11]</td>
	    </tr>
	        <tr>
	        <td colspan="3">IR 센서 GND 핀 </td>
	        <td>GND</td>
	        <td>-</td>
	    </tr>
	    <tr>
	        <td colspan="3">IR 센서 VCC 핀</td>
	        <td>VCC</td>
	        <td>-</td>
	    </tr>
	    <tr>
	        <td colspan="3">LED (+) 핀</td>
	        <td>7</td>
	        <td>B[01]</td>
	    </tr>
	    <tr>
	        <td colspan="3">LED (-) 핀</td>
	        <td>GND</td>
	        <td>-</td>
	    </tr>
	</table>
</div>

</br></br>

### 7.2.3 실행 방법
이 예제를 실행하려면 main.c 파일의 **Main_StartTask()**를 다음과 같이 수정합니다.
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
코드를 편집한 후 다음 디렉터리로 이동하여 빌드 명령을 실행합니다.  
```
$ cd ~/vcp/build/tcc70xx/gcc
$ make
```
이 명령은 펌웨어 이미지를 생성하고 ***FWDN*** 툴을 사용하여 생성된 이미지를 VCP-G에 플래싱합니다.  
코드가 성공적으로 플래싱되어 실행되면 IR 수신기가 리모컨의 신호를 감지하고 짧은 시간 동안 LED를 켭니다. 이는 VCP-G가 IR 입력을 올바르게 읽고 수신된 신호에 따라 GPIO 출력을 제어하고 있음을 확인시켜 줍니다.

**참고**: IR 센서 또는 LED에 사용되는 GPIO 핀을 변경하려면 소스 코드 내부의 설정 섹션을 참조하십시오.
</br></br></br>

## 7.3 가스 센서
---
이 예제는 VCP-G 보드가 가스 센서(MQ 135)를 사용하여 공기 중의 다양한 유해 가스를 감지하는 방법을 보여줍니다. VCP-G 보드의 아날로그 핀에 연결된 센서에서 아날로그 값을 읽어 전압으로 변환한 다음 소수점 한 자리까지 시리얼 모니터에 출력합니다.

**참고:** Gas Sensor (MQ-135)는 Winsen®의 제품입니다. 해당 디자인, 상표 및 관련 지식 재산권에 대한 모든 권리는 Winsen이 보유합니다.
</br></br>

### 7.3.1 하드웨어 요구 사항
- VCP-G 보드 (x1)
- 가스 센서 (MQ135) (x1)
- 12V 1A 전원 어댑터 (x1)
- USB Type-C to A 케이블 (x1)
- 수-암 점퍼 와이어 (x3)
</br></br>

### 7.3.2 회로
- 가스 센서
    - 가스 센서의 A0 핀은 VCP-G 보드의 아날로그 55번 핀에 연결됩니다. 
    - 가스 센서의 VCC 핀은 VCP-G 보드의 5V에 연결됩니다.
    - 가스 센서의 GND 핀은 VCP-G 보드의 GND에 연결됩니다.

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/F_gassensor.png" width="600"></p>
<p align="center"><strong>그림 7.3 가스 센서 회로도</strong></p>

#### 7.3.2.1 핀맵
다음 표는 핀 매핑을 나타냅니다.

<p align="center"><strong>표 7.3 가스 센서의 핀맵</strong></p>
<div align="center">
	<table>
	    <tr>
	        <th colspan="3">핀 이름</th>
	        <th>VCP-G 보드</th>
	        <th>GPIO</th>
	    </tr>
	    <tr>
	        <td colspan="3">가스 센서 A0 핀</td>
	        <td>55</td>
	        <td>K[15]</td>
	    </tr>
	        <tr>
	        <td colspan="3">가스 센서 VCC 핀</td>
	        <td>5V</td>
	        <td>-</td>
	    </tr>
	    <tr>
	        <td colspan="3">가스 센서 GND 핀</td>
	        <td>GND</td>
	        <td>-</td>
	    </tr>
	</table>
</div>
</br></br>

### 7.3.3 실행 방법
이 예제를 실행하려면 main.c 파일의 **Main_StartTask()**를 다음과 같이 수정합니다.
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
코드를 편집한 후 다음 디렉터리로 이동하여 빌드 명령을 실행합니다.  
```
$ cd ~/vcp/build/tcc70xx/gcc
$ make
```
이 과정에서 펌웨어 이미지가 생성되며, **FWDN** 도구를 사용하여 생성된 이미지를 VCP-G에 플래싱합니다.  
코드가 성공적으로 플래싱되어 실행되면 가스 센서가 주변 공기 질을 지속적으로 모니터링합니다. 가스가 감지되면(센서 출력이 LOW) 가스 감지를 나타내는 메시지가 시리얼 모니터에 표시되고, 그렇지 않으면 깨끗한 공기임을 보고합니다. 이는 VCP-G가 가스 센서의 디지털 입력을 올바르게 읽고 있음을 확인시켜 줍니다.

**참고**: 가스 센서에 사용되는 GPIO 핀을 변경하려면 소스 코드 내부의 설정 섹션을 참조하십시오. 대부분의 가스 센서 모듈에는 감도 조절용 작은 조정 나사(가변 저항)가 포함되어 있습니다. 센서가 안정적으로 반응하지 않는 경우 이 나사를 조정하여 가스 감지 임계값을 미세 조정해 보십시오.
</br></br></br>

## 7.4 정전식 터치 센서
---
이 예제는 VCP-G 보드가 정전식 터치 센서와 인터페이스하고 브레드보드의 LED를 제어하는 방법을 보여줍니다. 정전식 터치 센서는 정전 용량의 변화를 감지하여 손가락의 물리적 접촉을 감지합니다.  
터치가 감지되면 센서는 VCP-G에 디지털 HIGH 신호를 출력하고, VCP-G는 이에 따라 LED를 켭니다. 이 예제는 터치 입력이 올바르게 인식되고 GPIO 출력이 그에 따라 응답하는지 확인시켜 줍니다. 터치 감지 상태는 시리얼 모니터에도 표시됩니다.
</br></br>

### 7.4.1 하드웨어 요구 사항
- VCP-G 보드 (x1)
- 브레드보드 (x1)
- 정전식 터치 센서 (x1)
- LED (x1)
- 12V 1A 전원 어댑터 (x1)
- USB Type-C to A 케이블 (x1)
- 수-수 점퍼 와이어 (x6)
</br></br>

### 7.4.2 회로
- 터치 센서 
    - 터치 센서 모듈의 SIG 핀은 VCP-G 보드의 39번 핀에 연결됩니다.
    - 터치 센서 모듈의 VCC 핀은 VCP-G 보드의 5V에 연결됩니다.
    - 터치 센서 모듈의 GND 핀은 VCP-G 보드의 GND에 연결됩니다.
- LED
    - LED의 (+) 핀은 VCP-G 보드의 7번 핀에 연결됩니다.
    - LED의 (–) 핀은 브레드보드의 GND 레일에 연결됩니다.

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/F_touchsensor.png" width="600"></p>
<p align="center"><strong>그림 7.4 터치 센서 회로도</strong></p>

#### 7.4.2.1 핀 매핑
다음 표는 핀 매핑을 나타냅니다.

<p align="center"><strong>표 7.5 터치 센서 핀 매핑</strong></p>
<div align="center">
	<table>
	    <tr>
	        <th colspan="3">핀 이름</th>
	        <th>VCP-G 보드</th>
	        <th>GPIO</th>
	    </tr>
	    <tr>
	        <td colspan="3">터치 센서 SIG 핀</td>
	        <td>39</td>
	        <td>K[12]</td>
	    </tr>
	        <tr>
	        <td colspan="3">터치 센서 VCC 핀</td>
	        <td>5V</td>
	        <td>-</td>
	    </tr>
	    <tr>
	        <td colspan="3">터치 센서 GND 핀</td>
	        <td>GND</td>
		    <td>-</td>
		</tr>
	    <tr>
	        <td colspan="3">LED (+) 핀</td>
	        <td>7</td>
	        <td>B[01]</td>
	    </tr>
	    <tr>
	        <td colspan="3">LED (-) 핀</td>
	        <td>GND</td>
	        <td>-</td>
	    </tr>
	</table>
</div>

</br></br>

### 7.4.3 실행 방법
이 예제를 실행하려면 main.c 파일의 **Main_StartTask()**를 다음과 같이 수정합니다.
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
코드를 편집한 후 다음 디렉터리로 이동하여 빌드 명령을 실행합니다.  
```
$ cd ~/vcp/build/tcc70xx/gcc
$ make
```
이 과정을 통해 펌웨어 이미지가 생성되며, FWDN 도구를 사용하여 생성된 이미지를 VCP-G에 플래싱합니다.  
코드가 정상적으로 플래싱되어 실행되면 정전식 터치 센서가 사람 손가락의 터치 입력을 감지합니다. 터치가 감지되면(센서 출력이 HIGH) 시리얼 모니터에 메시지가 출력되고 LED가 켜집니다. 터치가 감지되지 않으면 LED는 꺼집니다. 이를 통해 VCP-G가 터치 센서의 입력을 올바르게 읽고 GPIO 출력을 정상적으로 제어하고 있음을 확인할 수 있습니다.

**참고**: 터치 센서나 LED에 사용되는 GPIO 핀을 변경하려면 소스 코드 내의 설정 부분을 참조하십시오.
</br></br></br></br>

# 8. 참고 자료
---
- 자세한 내용은 TOPST에 문의하십시오: topst@topst.ai

**참고:** 참조 문서는 계약 조건에 따라 제공이 가능한 경우 제공될 수 있습니다. 참조
문서를 이용할 수 없는 경우에는 개발과 직접 관련된 내용을 안내받을 수 있습니다.
