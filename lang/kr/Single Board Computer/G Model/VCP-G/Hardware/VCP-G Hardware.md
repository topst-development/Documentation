# 1. 소개
---
이 문서는 TCC7045 애플리케이션 프로세서 기반의 VCP-G에 대한 하드웨어 사용자 가이드입니다. 이 문서에서는 VCP-G의 시스템 설치, 디버깅 및 전체 설계와 사용법에 대한 상세 정보를 설명합니다.


표 1.1은 VCP-G의 특징을 설명합니다.

<p align="center"><strong>표 1.1 VCP-G의 특징</strong></p>
<div align="center">
	<table>
	  <tr>
	    <td colspan="3">부품명</td>
	    <td>TCC7045</td>
	  </tr>
	  <tr>
	    <td colspan="3">패키지</td>
	    <td>패키지	핀 투 핀 호환 FBGA 196-pin (12BD)</td>
	  </tr>
	    <tr>
	    <td colspan="3">CPU 주파수</td>
	    <td>200 MHz (최대 300 MHz)</td>
	  </tr>
	  <tr>
	    <td rowspan="4">온칩 메모리</td>
	    <td colspan="2">프로그램 플래시</td>
	    <td colspan="3">4 MB</td>
	  </tr>
	  <tr>
	    <td colspan="2">SRAM</td>
	    <td colspan="3">512 KB (Retention RAM 16 KB 포함)</td>
	  </tr>
	  <tr>
	    <td colspan="2">DataFlash</td>
	    <td colspan="3">256 KB</td>
	  </tr>
	  <tr>
	    <td colspan="2">DMA 채널</td>
	    <td colspan="3">16채널</td>
	  </tr>
	  <tr>
	    <td rowspan="13">주변장치</td>
	    <td colspan="2">Ethernet</td>
	    <td>1 Gbps (AVB 지원)</td>
	  </tr>
	  <tr>
		<td colspan="2">CAN / CANFD</td>
	    <td>3채널</td>
	  </tr>
	  <tr>
	    <td colspan="2">전용 LIN / UART</td>
	    <td>3채널 (최대 6채널)</td>
	  </tr>
	  <tr>
	    <td colspan="2">전용 I2C</td>
	    <td>3채널 (최대 6채널)</td>
	  </tr>
	  <tr>
	  <tr>
	    <td colspan="2">전용 GPSB (SPI)</td>
	    <td>2채널 (최대 5채널)</td>
	  </tr>
	    <tr>
	    <td colspan="2">MFIO (UART, I2C, GPSB 할당)</td>
	    <td>3채널</td>
	  </tr>
	  <tr>
	    <td rowspan="4">ADC</td> 
	    <td>분해능</td>
	    <td>12비트 SAR 방식</td>
	  </tr>
	  <tr>
	    <td>채널</td>
	    <td>12채널 x 2그룹</td>
	  </tr>
	  <tr>
	    <td>입력 범위</td>
	    <td>3.3V</td>
	  </tr>
	  <tr>
	    <td>샘플링 속도</td>
	    <td>1.0 MSPs 이상</td>
	  </tr>
	  <tr>
	    <td colspan="2">I2S</td>
	    <td>1채널</td>
	  </tr>
	  <tr>
	    <td colspan="2">시리얼 플래시 인터페이스</td>
	    <td>Quad SPI</td>
	  </tr>  
	  <tr>
	    <td colspan="3">전원 시스템</td>
	    <td>3.3V 단일</td>
	  </tr>
	  <tr>
	    <td colspan="3">온도</td>
	    <td>-40 ℃ to 105 ℃</td>
	  </tr>
	</table>
</div>

</br></br></br>

## 1.1 용어
---
<p align="center"><strong>표 1.2 용어 </strong></p>
<div align="center">
	<table>
	  <tr>
	    <td clospan="2"><strong>용어</strong></td>
	    <td><strong>정의</strong></td>
	  </tr>
	  <tr>
	    <td clospan="2">ADC</td>
	    <td>아날로그-디지털 변환기</td>
	  </tr>
	  <tr>
	    <td clospan="2">FWDN</td>
	    <td>펌웨어 다운로드</td>
	  </tr>
	  <tr>
	    <td clospan="2">GPIO</td>
	    <td>범용 입출력</td>
	  </tr>
	  <tr>
	    <td clospan="2">MCU</td>
	    <td>마이크로컨트롤러 유닛</td>
	  </tr>
	  <tr>
	    <td clospan="2">TOPST</td>
	    <td>시스템 개발 및 교육을 위한 통합 개방형 플랫폼</td>
	  </tr>
	  <tr>
	    <td clospan="2">VCP</td>
	    <td>차량 제어 프로세서</td>
	  </tr>
	</table>
</div>

</br></br></br></br>

# 2. 블록 다이어그램
---
## 2.1 시스템 블록 다이어그램
---
그림 2.1은 VCP-G의 시스템 블록 다이어그램을 보여줍니다.
<p align="center"><img src= "https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Hardware/2.1%20VCP-G%20System%20Block%20Diagram.png"></p>
<p align="center"><strong>그림 2.1 시스템 블록 다이어그램</strong></p>

</br></br></br></br>

# 3. VCP-G 개요
---
VCP-G는 다음과 같은 용도로 사용할 수 있습니다:
  - 시스템 개발
  - 교육

표 3.1은 VCP-G의 기본 구성을 설명합니다.

<p align="center"><strong>표 3.1 VCP-G의 기본 구성 </strong></p>
<div align="center">
	<table>
	  <tr>
	    <td colspan="2"><strong>보드 이름</strong></td>
	    <td><strong>설명</strong></p>
	  </tr>
	  <tr>
	    <td colspan="2">TOPST_VCP_V2.1.1</td>
	    <td>TOPST용 MCU 보드</td>
	  </tr>
	</table>
</div>

</br></br></br>

## 3.1 VCP-G
---
그림 3.1은 VCP-G의 윗면을 보여줍니다.
<p align="center"><img src= "https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Hardware/3.1%20TOPST%20VCP-G%20Board%20(Top%20View)%20.png"></p>
<p align="center"><strong>그림 3.1 VCP-G (윗면)</strong></p>

표 3.2는 VCP-G(윗면)의 커넥터를 설명합니다.
<p align="center"><strong>표 3.2 VCP-G의 커넥터 (윗면)</strong></p>
<div align="center">
	<table>
	  <tr>
	    <td colspan="4"><strong>번호</strong></td>
	    <td><strong>참조 번호</strong></td>
	    <td><strong>이름</strong></td>
	    <td><strong>설명</strong></td>
	  </tr>
	  <tr>
	    <td colspan="4">1</td>
	    <td>J18D100</td>
	    <td>36핀 암 헤더</td>
	    <td>GPIO 및 ADC용 헤더</td>
	  </tr>
	  <tr>
	    <td colspan="4">2</td>
	    <td>J5D100</td>
	    <td>10핀 수 헤더</td>
	    <td>CAN용 헤더</td>
	  </tr>
	  <tr>
	    <td colspan="4">3</td>
	    <td>J3D100</td>
	    <td>6핀 수 헤더</td>
	    <td>SPI용 헤더</td>
	  </tr>
	  <tr>
	    <td colspan="4">4</td>
	    <td>J8D104</td>
	    <td>8핀 암 헤더</td>
	    <td>GPIO 및 ADC용 헤더</td>
	  </tr>
	  <tr>
	    <td colspan="4">5</td>
	    <td>J8D102</td>
	    <td>8핀 암 헤더</td>
	    <td>GPIO용 헤더</td>
	  </tr>
	  <tr>
	    <td colspan="4">6</td>
	    <td>J10D100</td>
	    <td>10핀 암 헤더</td>
	    <td>GPIO 및 ADC용 헤더</td>
	  </tr>
	  <tr>
	    <td colspan="4">7</td>
	    <td>J100</td>
	    <td>10핀 수 헤더</td>
	    <td>JTAG용 헤더</td>
	  </tr>
	  <tr>
	    <td colspan="4">8</td>
	    <td>SW100</td>
	    <td>RESET 택트 스위치</td>
	    <td>GRESETn: VCP-G의 시스템 및 전원 관리를 초기화합니다</td>
	  </tr>
	  <tr>
	    <td colspan="4">9</td>
	    <td>JC100</td>
	    <td>USB Type-C 커넥터</td>
	    <td>디버깅 또는 FWDN 포트용 UART</td>
	  </tr>
	  <tr>
	    <td colspan="4">10</td>
	    <td>SW101</td>
	    <td>택트 스위치</td>
	    <td>FWDN: VCP-G의 펌웨어 다운로드 모드로 진입합니다</td>
	  </tr>  
	  <tr>
	    <td colspan="4">11</td>
		<td>J101</td>
	    <td>DC 잭</td>
	    <td>DC 전원 입력 잭</td>
	  </tr>  
	  <tr>
	    <td colspan="4">12</td>
	    <td>J8D100</td>
	    <td>8핀 암 헤더</td>
	    <td>전원 및 리셋용 헤더</td>
	  </tr>  
	  <tr>
	    <td colspan="4">13</td>
	    <td>J8D101</td>
	    <td>8핀 암 헤더</td>
	    <td>GPIO 및 ADC용 헤더</td>
	  </tr>  
	  <tr>
	    <td colspan="4">14</td>
	    <td>J8D103</td>
	    <td>8핀 암 헤더</td>
	    <td>GPIO 및 ADC용 헤더</td>
	  </tr>    
	</table>
</div>

그림 3.2는 VCP-G의 아랫면을 보여줍니다.  

**참고:** 그림 3.2는 현재 TOPST_VCP-G_V1.1.1 보드를 보여줍니다. 이 이미지는 TOPST_VCP-G_V2.1.1 보드로 업데이트될 예정입니다.
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Hardware/3.2%20TOPST%20VCP-G%20Board%20(Bottom%20View).png"></p>
<p align="center"><strong>그림 3.2 VCP-G (아랫면)</strong></p>

</br></br></br></br>

# 4. 사양
---
## 4.1 Quad SPI 플래시 메모리 (U101)
---
Quad SPI 플래시 메모리에 대한 정보는 다음과 같습니다:
  - 용량 : 64 Mb  
  
**참고:** SNOR는 기본적으로 VCP-G에 실장되어 있지 않습니다.

</br></br></br>

## 4.2 전원 입력 커넥터 (J101)
---
12V 어댑터에서 J101의 DC 잭을 통해 VCP-G에 DC 12V가 공급됩니다.  
그림 4.1은 J101의 위치를 보여줍니다.
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Hardware/4.1%20Power%20In%20Connector%20(J101).png"></p>
<p align="center"><strong>그림 4.1 전원 입력 커넥터 (J101)</strong><p>

</br></br></br>

## 4.3 JTAG용 커넥터 (J100)
---
디버깅을 위해 J100을 통해 VCP-G에 JTAG 에뮬레이터를 연결할 수 있습니다. 그림 4.2는 J100의 위치를 보여줍니다.
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Hardware/4.2%20Connector%20for%20JTAG%20(J100).png"></p>
<p align="center"><strong>그림 4.2 JTAG용 커넥터 (J100)</strong><p>
JTAG는 기본적으로 비활성화되어 있습니다. JTAG를 활성화하려면 R178과 R179의 연결을 변경해야 합니다. R178에 의해 TRSRn이 high로 설정되면 MCU는 JTAG 모드로 진입합니다.

표 4.1은 J100의 핀을 설명합니다.
<p align="center"><strong>표 4.1 J100 핀 설명</strong></p>
<div align="center">
	<table>
	  <tr>
	    <th rowspan="2"><strong>핀 번호</strong></th>
	    <th rowspan="2"><strong>회로도 네트 이름</strong></th>
	    <th><strong>DIR</strong></th>
	    <th rowspan="2"><strong>설명</strong></th>
	  </tr>
	  <tr>
	    <th><strong>MCU ◄► J100</strong></th>
	  </tr>
	  <tr>
	    <td>1</td>
	    <td>SW_VDD_3P3</td>
	    <td>-</td>
	    <td>전원 3.3V</td>
	  </tr>
	  <tr>
	    <td>2</td>
	    <td>TMS</td>
	    <td>◄</td>
	    <td>테스트 모드 상태</td>
	  </tr>
	  <tr>
	    <td>3</td>
	    <td>DGND</td>
	    <td>-</td>
	    <td>그라운드</td>
	  </tr>
	  <tr>
	    <td>4</td>
	    <td>TCK</td>
	    <td>◄</td>
	    <td>테스트 클럭</td>
	  </tr>
	  <tr>
	    <td>5</td>
		<td>DGND</td>
	    <td>-</td>
	    <td>그라운드</td>
	  </tr>
	  <tr>
	    <td>6</td>
	    <td>TDO</td>
	    <td>►</td>
	    <td>테스트 데이터 출력</td>
	  </tr>
	  <tr>
	    <td>7</td>
	    <td>NC</td>
	    <td>-</td>
	    <td>연결되지 않음</td>
	  </tr>
	  <tr>
	    <td>8</td>
	    <td>TDI</td>
	    <td>◄</td>
	    <td>테스트 데이터 입력</td>
	  </tr>
	  <tr>
	    <td>9</td>
	    <td>DGND</td>
	    <td>-</td>
	    <td>그라운드</td>
	  </tr>
	  <tr>
	    <td>10</td>
	    <td>JTAG_RESETn</td>
	    <td>◄</td>
	    <td>시스템 리셋</td>
	  </tr>   
	</table>
</div>

표 4.2는 JTAG 비활성화/활성화 설정을 설명합니다.
<p align="center"><strong>표 4.2 JTAG 비활성화/활성화 설정</strong></p>
<div align="center">
	<table>
	  <tr>
	    <th colspan="4"><strong>모드</strong></th>
	    <th><strong>TRSTn 값</strong></th>
	    <th><strong>R178</strong></th>
	    <th><strong>R179</strong></th>
	  </tr>
	  <tr>
	    <td colspan="4">JTAG 비활성화 (기본값)</td>
	    <td>Low (1)</td>
	    <td>N.C</td>
	    <td>1K</td>
	  </tr>
	  <tr>
	    <td colspan="4">JTAG 활성화 (옵션)</td>
	    <td>High (1)</td>
	    <td>1K</td>
	    <td>N.C</td>
	  </tr>
	</table>
</div>

</br></br></br>

## 4.4 FWDN 스위치 (SW101)
---
VCP-G는 Boot Mode (BM)를 사용하는 부팅 설정용 핀을 하나 가지고 있으며, UART FWDN 모드와 일반 모드의 두 가지 모드를 지원합니다.   
그림 4.3은 VCP-G의 부팅 모드를 선택하는 데 사용되는 FWDN 택트 스위치 (SW101)의 위치를 보여줍니다.
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Hardware/4.3%20FWDN%20Tact%20Switch%20(SW101).png"></p>
<p align="center"><strong>그림 4.3 FWDN 택트 스위치 (SW101)</strong><p>

표 4.3은 FWDN 택트 스위치 (SW101)를 사용하여 부팅 모드를 선택하는 방법을 설명합니다.
<p align="center"><strong>표 4.3 부팅 모드용 택트 스위치 (SW101) 설명</strong></p>
<div align="center">
	<table>
	  <tr>
	    <th colspan="3"><strong>모드</strong></th>
	    <th><strong>BM00 값</strong></th>
	    <th><strong>SW101 상태</strong></th>
	  </tr>
	  <tr>
	    <td colspan="3">일반 (기본값)</td>
	    <td>Low (1)</td>
	    <td>기본값</td>
	  </tr>
	  <tr>
	    <td colspan="3">FWDN (옵션)</td>
	    <td>High (1)</td>
	    <td>누른 상태에서 전원 인가</td>
	  </tr>
	</table>
</div>
</br></br>

### 4.4.1 FWDN 모드 진입 방법
FWDN 모드로 진입하는 방법은 다음과 같이 두 가지가 있습니다.

#### 4.4.1.1 방법 1
FWDN 스위치 (SW101)를 누른 상태에서 12V 전원 공급 장치를 연결하여 VCP-G 보드의 전원을 켜십시오.  
FWDN 스위치를 누른 상태에서 전원이 인가되면 FWDN 빨간색 표시등이 켜집니다. FWDN 스위치 (SW101)에서 손을 떼면 MCU가 FWDN 모드로 진입합니다.  
그림 4.4는 방법 1을 사용하여 FWDN 모드로 진입하는 방법을 보여줍니다.
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Hardware/4.4%20Entering%20FWDN%20Mode%20by%20Using%20Method%201.png"></p>
<p align="center"><strong>그림 4.4 방법 1을 사용한 FWDN 모드 진입</strong><p>

#### 4.4.1.2 방법 2
VCP-G 보드가 12V 전원 공급 장치에 연결된 상태에서 FWDN 스위치 (SW101)를 누른 다음 RESET 택트 스위치 (SW100)를 누르십시오.  
FWDN 스위치를 누른 상태에서 전원이 인가되면 FWDN 빨간색 표시등이 켜집니다. RESET 택트 스위치를 누르는 동안 3.3V 초록색 표시등이 꺼집니다. FWDN 스위치 (SW101)에서 손을 떼면 MCU가 FWDN 모드로 진입합니다.  
그림 4.5는 방법 2를 사용한 FWDN 모드를 보여줍니다.

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Hardware/4.5%20Entering%20FWDN%20Mode%20by%20Using%20Method%202.png"></p>
<p align="center"><strong>그림 4.5 방법 2를 사용한 FWDN 모드 진입</strong><p>

</br></br></br>

## 4.5 RESET 택트 스위치 (SW100)
---
VCP-G는 GRESETn 핀을 사용하는 RESET 전원용 RESET 스위치를 하나 가지고 있습니다.  
그림 4.6은 RESET 택트 스위치 (SW100)를 보여줍니다.
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Hardware/4.6%20RESET%20Tact%20Switch%20(SW100).png"></p>
<p align="center"><strong>그림 4.6 RESET 택트 스위치 (SW100)</strong><p>
</br></br>

### 4.5.1 RESET 택트 스위치 (SW100) 기능
SW100은 VCP-G의 전원 블록과 시스템 블록을 리셋하는 택트 스위치입니다.  
이 버튼의 기능은 다음과 같습니다:
  - 전원이 켜진 상태에서 RESET 택트 스위치 (SW100)를 누르면 VCP-G의 전원 블록과 시스템이 강제로 리셋됩니다.

**중요:** 전원이 갑자기 꺼져 데이터가 손상될 수 있으므로 택트 스위치를 누를 때 주의하십시오.

</br></br></br>

## 4.6 디버깅 및 FWDN용 커넥터 (JC100)
---
JC100은 표준 USB Type-C 커넥터입니다. VCP-G에서 JC100은 UART를 통한 디버깅 또는 FWDN에 사용됩니다.  
그림 4.7은 JC100의 위치를 보여줍니다.
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Hardware/4.7%20USB%20Type-C%20Connector%20(JC100).png"></p>
<p align="center"><strong>그림 4.7 USB Type-C 커넥터 (JC100)</strong><p>

JC100을 통해 VCP-G의 FWDN을 수행하거나 디버깅 메시지를 확인할 수 있습니다.
VCP-G의 JC100에는 USB-to-UART 브리지 컨트롤러가 내장되어 있으므로 USB Type-C 케이블을 사용하여 JC100을 PC에 직접 연결할 수 있습니다.

</br></br></br>

## 4.7 GPIO, ADC, 전원, CAN, SPI용 핀 헤더
---
VCP-G에는 센서나 서브 보드와 같은 다른 주변장치에 연결하기 위한 전원, GPIO, ADC, CAN, SPI용 2.54 mm 핀 헤더가 9개 있습니다.  

표 4.4는 VCP-G에 있는 9개 핀 헤더의 용도를 설명합니다.
<p align="center"><strong>표 4.4 VCP-G의 핀 헤더 </strong></p>
<div align="center">
	<table>
	  <tr>
	    <td colspan="4"><strong>번호</strong></td>
	    <td><strong>참조 번호</strong></td>
	    <td><strong>이름</strong></td>
	    <td><strong>설명</strong></td>
	  </tr>
	  <tr>
	    <td colspan="4">1</td>
	    <td>J18D100</td>
	    <td>36핀 암 헤더</td>
	    <td>GPIO 및 ADC용 헤더</td>
	  </tr>
	  <tr>
	    <td colspan="4">2</td>
	    <td>J5D100</td>
	    <td>10핀 수 헤더</td>
	    <td>CAN용 헤더</td>
	  </tr>
	  <tr>
	    <td colspan="4">3</td>
	    <td>J3D100</td>
	    <td>6핀 수 헤더</td>
	    <td>SPI용 헤더</td>
	  </tr>
	  <tr>
	    <td colspan="4">4</td>
	    <td>J8D104</td>
	    <td>8핀 암 헤더</td>
	    <td>GPIO 및 ADC용 헤더</td>
	  </tr>
	  <tr>
	    <td colspan="4">5</td>
	    <td>J8D102</td>
	    <td>8핀 암 헤더</td>
	    <td>GPIO용 헤더</td>
	  </tr>
	  <tr>
	    <td colspan="4">6</td>
	    <td>J10D100</td>
	    <td>10핀 암 헤더</td>
	    <td>GPIO 및 ADC용 헤더</td>
	  </tr>
	  <tr>
	    <td colspan="4">7</td>
	    <td>J8D100</td>
	    <td>8핀 암 헤더</td>
	    <td>전원 및 리셋용 헤더</td>
	  </tr>
	  <tr>
	    <td colspan="4">8</td>
	    <td>J8D101</td>
	    <td>8핀 암 헤더</td>
	    <td>GPIO 및 ADC용 헤더</td>
	  </tr>
	  <tr>
	    <td colspan="4">9</td>
	    <td>J8D103</td>
	    <td>8핀 암 헤더</td>
	    <td>GPIO 및 ADC용 헤더</td>
	  </tr>
	</table>
</div>

그림 4.8은 VCP-G의 핀 헤더 위치를 나타냅니다.
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Hardware/4.8%20Pin%20Headers%20on%20TOPST%20VCP-G%20Board.png"></p>
<p align="center"><strong>그림 4.8 VCP-G의 핀 헤더 </strong><p>

표 4.5는 J10D100의 핀 설명을 나타냅니다.
<p align="center"><strong>표 4.5 J10D100 핀 설명</strong></p>
<div align="center">
	<table>
	  <tr>
	    <th rowspan="3"><strong>핀 번호</strong></th>
	    <th colspan="4"><strong>J10D100</strong></th>
	  </tr>
	  <tr>
	    <th rowspan="2"><strong>포트 이름</strong></th>
	    <th rowspan="2"><strong>신호 이름</strong></th>
	    <th><strong>DIR</strong></th>
	    <th rowspan="2"><strong>설명</strong></th>
	  </tr>
	  <tr>
	    <th><strong>MCU ◄► J10D100</strong></th>
	  </tr>
	  <tr>
	    <td>1</td>
	    <td>SCL</td>
	    <td>GPIO_AC07</td>
	    <td>◄►</td>
	    <td>GPIO 또는 ADC 신호</td>
	  </tr>
	  <tr>
	    <td>2</td>
	    <td>SDA</td>
	    <td>GPIO_AC06</td>
	    <td>◄►</td>
	    <td>GPIO 또는 ADC 신호</td>
	  </tr>
	  <tr>
	    <td>3</td>
	    <td>AREF</td>
	    <td>ADC06</td>
	    <td>◄</td>
	    <td>ADC 신호</td>
	  </tr>
	  <tr>
	    <td>4</td>
	    <td>GND</td>
	    <td>DGND</td>
	    <td>-</td>
	    <td>그라운드</td>
	  </tr>
	  <tr>
	    <td>5</td>
	    <td>13</td>
	    <td>GPIO_C12</td>
	    <td>◄►</td>
	    <td>GPIO 신호</td>
	  </tr>
	  <tr>
	    <td>6</td>
	    <td>12</td>
	    <td>GPIO_C15</td>
	    <td>◄►</td>
	    <td>GPIO 신호</td>
	  </tr>
	  <tr>
	    <td>7</td>
	    <td>11</td>
	    <td>GPIO_C14</td>
	    <td>◄►</td>
	    <td>GPIO 신호</td>
	  </tr>
	  <tr>
	    <td>8</td>
	    <td>10</td>
	    <td>GPIO_C13</td>
	    <td>◄►</td>
	    <td>GPIO 신호</td>
	  </tr>
	  <tr>
	    <td>9</td>
	    <td>9</td>
	    <td>GPIO_A12</td>
	    <td>◄►</td>
	    <td>GPIO 신호</td>
	  </tr>
	  <tr>
	    <td>10</td>
	    <td>8</td>
	    <td>GPIO_B00</td>
	    <td>◄►</td>
	    <td>GPIO 신호</td>
	  </tr>
	</table>
</div>

표 4.6은 J8D100의 핀 설명을 나타냅니다.
<p align="center"><strong>표 4.6 J8D100 핀 설명</strong></p>
<div align="center">
	<table>
	  <tr>
	    <th rowspan="3"><strong>핀 번호</strong></th>
	    <th colspan="4"><strong>J8D100</strong></th>
	  </tr>
	  <tr>
	    <th rowspan="2"><strong>포트 이름</strong></th>
	    <th rowspan="2"><strong>신호 이름</strong></th>
	    <th><strong>DIR</strong></th>
	    <th rowspan="2"><strong>설명</strong></th>
	  </tr>
	  <tr>
	    <th><strong>MCU ◄► J8D100</strong></th>
	  </tr>
	  <tr>
	    <td>1</td>
	    <td>-</td>
	    <td>-</td>
	    <td>-</td>
	    <td>-</td>
	  </tr>
	  <tr>
	    <td>2</td>
	    <td>IOREF</td>
	    <td>VCP_3P3</td>
	    <td>-</td>
	    <td>전원 3.3V</td>
	  </tr>
	  <tr>
	    <td>3</td>
	    <td>RST</td>
	    <td>RESET</td>
	    <td>◄</td>
	    <td>리셋 신호</td>
	  </tr>
	  <tr>
	    <td>4</td>
	    <td>3.3V</td>
	    <td>VCP_3P3</td>
	    <td>-</td>
	    <td>전원 3.3V</td>
	  </tr>
	  <tr>
	    <td>5</td>
	    <td>5V</td>
	    <td>VCP_5P0</td>
	    <td>-</td>
	    <td>전원 5.0V</td>
	  </tr>
	  <tr>
	    <td>6</td>
	    <td>GND</td>
	    <td>DGND</td>
	    <td>-</td>
	    <td>그라운드</td>
	  </tr>
	  <tr>
	    <td>7</td>
	    <td>GND</td>
	    <td>DGND</td>
	    <td>-</td>
	    <td>그라운드</td>
	  </tr>
	  <tr>
	    <td>8</td>
	    <td>VIN</td>
	    <td>VIN</td>
	    <td>-</td>
	    <td>VCP-G용 전압 입력</td>
	  </tr>
	</table>
</div>

표 4.7은 J8D101의 핀 설명을 나타냅니다.
<p align="center"><strong>표 4.7 J8D101 핀 설명</strong></p>
<div align="center">
	<table>
	  <tr>
	    <th rowspan="3"><strong>핀 번호</strong></th>
	    <th colspan="4"><strong>J8D101</strong></th>
	  </tr>
	  <tr>
	    <th rowspan="2"><strong>포트 이름</strong></th>
	    <th rowspan="2"><strong>신호 이름</strong></th>
	    <th><strong>DIR</strong></th>
	    <th rowspan="2"><strong>설명</strong></th>
	  </tr>
	  <tr>
	    <th><strong>MCU ◄► J8D101</strong></th>
	  </tr>
	  <tr>
	    <td>1</td>
	    <td>A0</td>
	    <td>ADC03</td>
	    <td>◄</td>
	    <td>ADC 신호</td>
	  </tr>
	  <tr>
	    <td>2</td>
	    <td>A1</td>
	    <td>ADC04</td>
	    <td>◄</td>
	    <td>ADC 신호</td>
	  </tr>
	  <tr>
	    <td>3</td>
	    <td>A2</td>
	    <td>GPIO_AC02</td>
	    <td>◄►</td>
	    <td>GPIO 신호</td>
	  </tr>
	  <tr>
	    <td>4</td>
	    <td>A3</td>
	    <td>GPIO_AC03</td>
	    <td>◄►</td>
	    <td>GPIO 신호</td>
	  </tr>
	  <tr>
	    <td>5</td>
	    <td>A4</td>
	    <td>GPIO_AC05</td>
	    <td>◄►</td>
	    <td>GPIO 신호</td>
	  </tr>
	  <tr>
	    <td>6</td>
	    <td>A5</td>
	    <td>GPIO_AC04</td>
	    <td>◄►</td>
	    <td>GPIO 신호</td>
	  </tr>
	  <tr>
	    <td>7</td>
	    <td>A6</td>
	    <td>ADC05</td>
	    <td>◄</td>
	    <td>ADC 신호</td>
	  </tr>
	  <tr>
	    <td>8</td>
	    <td>A7</td>
	    <td>ADC01</td>
	    <td>◄</td>
	    <td>ADC 신호</td>
	  </tr>
	</table>
</div>

표 4.8은 J8D102의 핀 설명을 나타냅니다.
<p align="center"><strong>표 4.8 J8D102 핀 설명</strong></p>
<div align="center">
	<table>
	  <tr>
	    <th rowspan="3"><strong>핀 번호</strong></th>
	    <th colspan="4"><strong>J8D102</strong></th>
	  </tr>
	  <tr>
	    <th rowspan="2"><strong>포트 이름</strong></th>
	    <th rowspan="2"><strong>신호 이름</strong></th>
	    <th><strong>DIR</strong></th>
	    <th rowspan="2"><strong>설명</strong></th>
	  </tr>
	  <tr>
	    <th><strong>MCU ◄► J8D102</strong></th>
	  </tr>
	  <tr>
	    <td>1</td>
	    <td>7</td>
	    <td>GPIO_B01</td>
	    <td>◄►</td>
	    <td>GPIO 신호</td>
	  </tr>
	  <tr>
	    <td>2</td>
	    <td>6</td>
	    <td>GPIO_A13</td>
	    <td>◄►</td>
	    <td>GPIO 신호</td>
	  </tr>
	  <tr>
	    <td>3</td>
	    <td>5</td>
	    <td>GPIO_B10</td>
	    <td>◄►</td>
	    <td>GPIO 신호</td>
	  </tr>
	  <tr>
	    <td>4</td>
	    <td>4</td>
	    <td>GPIO_B27</td>
	    <td>◄►</td>
	    <td>GPIO 신호</td>
	  </tr>
	  <tr>
	    <td>5</td>
	    <td>3</td>
	    <td>GPIO_B11</td>
	    <td>◄►</td>
	    <td>GPIO 신호</td>
	  </tr>
	  <tr>
	    <td>6</td>
	    <td>2</td>
	    <td>GPIO_B28</td>
	    <td>◄►</td>
	    <td>GPIO 신호</td>
	  </tr>
	  <tr>
	    <td>7</td>
	    <td>1</td>
	    <td>GPIO_B25</td>
	    <td>◄►</td>
	    <td>GPIO 신호</td>
	  </tr>
	  <tr>
	    <td>8</td>
	    <td>0</td>
	    <td>GPIO_B26</td>
	    <td>◄►</td>
	    <td>GPIO 신호</td>
	  </tr>
	</table>
</div>

표 4.9는 J8D103의 핀 설명을 나타냅니다.
<p align="center"><strong>표 4.9 J8D103 핀 설명</strong></p>
<div align="center">
	<table>
	  <tr>
	    <th rowspan="3"><strong>핀 번호</strong></th>
	    <th colspan="4"><strong>J8D103</strong></th>
	  </tr>
	  <tr>
	    <th rowspan="2"><strong>포트 이름</strong></th>
	    <th rowspan="2"><strong>신호 이름</strong></th>
	    <th><strong>DIR</strong></th>
	    <th rowspan="2"><strong>설명</strong></th>
	  </tr>
	  <tr>
	    <th><strong>MCU ◄► J8D103</strong></th>
	  </tr>
	  <tr>
	    <td>1</td>
	    <td>A8</td>
	    <td>GPIO_AC08</td>
	    <td>◄►</td>
	    <td>GPIO 또는 ADC 신호</td>
	  </tr>
	  <tr>
	    <td>2</td>
	    <td>A9</td>
	    <td>GPIO_AC09</td>
	    <td>◄►</td>
	    <td>GPIO 또는 ADC 신호</td>
	  </tr>
	  <tr>
	    <td>3</td>
	    <td>A10</td>
	    <td>GPIO_AC10</td>
	    <td>◄►</td>
	    <td>GPIO 또는 ADC 신호</td>
	  </tr>
	  <tr>
	    <td>4</td>
	    <td>A11</td>
	    <td>GPIO_ADC-2</td>
	    <td>◄</td>
	    <td>ADC 신호</td>
	  </tr>
	  <tr>
	    <td>5</td>
	    <td>54</td>
	    <td>GPIO_K14</td>
	    <td>◄►</td>
	    <td>GPIO 신호</td>
	  </tr>
	  <tr>
	    <td>6</td>
	    <td>55</td>
	    <td>GPIO_K15</td>
	    <td>◄►</td>
	    <td>GPIO 신호</td>
	  </tr>
	  <tr>
	    <td>7</td>
	    <td>56</td>
	    <td>GPIO_K01</td>
	    <td>◄</td>
	    <td>GPIO 신호</td>
	  </tr>
	  <tr>
	    <td>8</td>
	    <td>57</td>
	    <td>GPIO_K08</td>
	    <td>◄►</td>
	    <td>GPIO 신호</td>
	  </tr>
	</table>
</div>

표 4.10은 J8D104의 핀 설명을 나타냅니다.
<p align="center"><strong>표 4.10 J8D104 핀 설명</strong></p>
<div align="center">
	<table>
	  <tr>
	    <th rowspan="3"><strong>핀 번호</strong></th>
	    <th colspan="4"><strong>J8D104</strong></th>
	  </tr>
	  <tr>
	    <th rowspan="2"><strong>포트 이름</strong></th>
	    <th rowspan="2"><strong>신호 이름</strong></th>
	    <th><strong>DIR</strong></th>
	    <th rowspan="2"><strong>설명</strong></th>
	  </tr>
	  <tr>
	    <th><strong>MCU ◄► J8D104</strong></th>
	  </tr>
	  <tr>
	    <td>1</td>
	    <td>14</td>
	    <td>GPIO_AC00</td>
	    <td>◄►</td>
	    <td>GPIO 또는 ADC 신호</td>
	  </tr>
	  <tr>
	    <td>2</td>
	    <td>15</td>
	    <td>GPIO_AC01</td>
	    <td>◄►</td>
	    <td>GPIO 또는 ADC 신호</td>
	  </tr>
	  <tr>
	    <td>3</td>
	    <td>16</td>
	    <td>GPIO_A06</td>
	    <td>◄►</td>
	    <td>GPIO 신호</td>
	  </tr>
	  <tr>
	    <td>4</td>
	    <td>17</td>
	    <td>GPIO_A07</td>
		<td>◄►</td>
	    <td>GPIO 신호</td>
	  </tr>
	  <tr>
	    <td>5</td>
	    <td>18</td>
	    <td>GPIO_A28</td>
	    <td>◄►</td>
	    <td>GPIO 신호</td>
	  </tr>
	  <tr>
	    <td>6</td>
	    <td>19</td>
	    <td>GPIO_A29</td>
	    <td>◄►</td>
	    <td>GPIO 신호</td>
	  </tr>
	  <tr>
	    <td>7</td>
	    <td>20</td>
	    <td>GPIO_B03</td>
	    <td>◄►</td>
	    <td>GPIO 신호</td>
	  </tr>
	  <tr>
	    <td>8</td>
	    <td>21</td>
	    <td>GPIO_B02</td>
	    <td>◄►</td>
	    <td>GPIO 신호</td>
	  </tr>
	</table>
</div>

표 4.11은 J3D100의 핀 설명을 나타냅니다.
<p align="center"><strong>표 4.11 J3D100 핀 설명</strong></p>
<div align="center">
	<table>
	  <tr>
	    <th rowspan="3"><strong>핀 번호</strong></th>
	    <th colspan="4"><strong>J3D100</strong></th>
	  </tr>
	  <tr>
	    <th rowspan="2"><strong>포트 이름</strong></th>
	    <th rowspan="2"><strong>신호 이름</strong></th>
	    <th><strong>DIR</strong></th>
	    <th rowspan="2"><strong>설명</strong></th>
	  </tr>
	  <tr>
	    <th><strong>MCU ◄► J3D100</strong></th>
	  </tr>
	  <tr>
	    <td>1</td>
	    <td>MISO</td>
	    <td>GPIO_B07</td>
	    <td>◄►</td>
	    <td>GPIO 신호</td>
	  </tr>
	  <tr>
	    <td>2</td>
	    <td>5V</td>
	    <td>VCP_5P0</td>
	    <td>-</td>
	    <td>전원 5.0V</td>
	  </tr>
	  <tr>
	    <td>3</td>
	    <td>SCK</td>
	    <td>GPIO_B04</td>
	    <td>◄►</td>
	    <td>GPIO 신호</td>
	  </tr>
	  <tr>
	    <td>4</td>
	    <td>MOSI</td>
	    <td>GPIO_B06</td>
	    <td>◄►</td>
	    <td>GPIO 신호</td>
	  </tr>
	  <tr>
	    <td>5</td>
	    <td>CMD</td>
	    <td>GPIO_B05</td>
	    <td>◄►</td>
	    <td>GPIO 신호</td>
	  </tr>
	  <tr>
	    <td>6</td>
	    <td>GND</td>
	    <td>DGND</td>
	    <td>-</td>
	    <td>그라운드</td>
	  </tr>
	</table>
</div>

표 4.12는 J18D100의 핀 설명을 나타냅니다.
<p align="center"><strong>표 4.12 J18D100 핀 설명</strong></p>
<div align="center">
	<table>
	  <tr>
	    <th rowspan="3"><strong>핀 번호</strong></th>
	    <th colspan="4"><strong>J18D100</strong></th>
	  </tr>
	  <tr>
	    <th rowspan="2"><strong>포트 이름</strong></th>
	    <th rowspan="2"><strong>신호 이름</strong></th>
	    <th><strong>DIR</strong></th>
	    <th rowspan="2"><strong>설명</strong></th>
	  </tr>
	  <tr>
	    <th><strong>MCU ◄► J18D100</strong></th>
	  </tr>
	  <tr>
	    <td>1</td>
	    <td>5V</td>
	    <td>VCP_5P0</td>
	    <td>-</td>
	    <td>전원 5.0V</td>
	  </tr>
	  <tr>
	    <td>2</td>
	   <td>5V</td>
	    <td>VCP_5P0</td>
	    <td>-</td>
	    <td>전원 5.0V</td>
	  </tr>
	  <tr>
	    <td>3</td>
	    <td>22</td>
	    <td>GPIO_B24</td>
	    <td>◄►</td>
	    <td>GPIO 신호</td>
	  </tr>
	  <tr>
	    <td>4</td>
	    <td>23</td>
	    <td>GPIO_B23</td>
	    <td>◄►</td>
	    <td>GPIO 신호</td>
	  </tr>
	  <tr>
	    <td>5</td>
	    <td>24</td>
	    <td>GPIO_B22</td>
	    <td>◄►</td>
	    <td>GPIO 신호</td>
	  </tr>
	  <tr>
	    <td>6</td>
	    <td>25</td>
	    <td>GPIO_B21</td>
	    <td>◄►</td>
	    <td>GPIO 신호</td>
	  </tr>
	  <tr>
	    <td>7</td>
	    <td>26</td>
	    <td>GPIO_B20</td>
	    <td>◄►</td>
	    <td>GPIO 신호</td>
	  </tr>
	  <tr>
	    <td>8</td>
	    <td>27</td>
	    <td>GPIO_B19</td>
	    <td>◄►</td>
	    <td>GPIO 신호</td>
	  </tr>
	  <tr>
	    <td>9</td>
	    <td>28</td>
	    <td>GPIO_A30</td>
	    <td>◄►</td>
	    <td>GPIO 신호</td>
	  </tr>
	  <tr>
	    <td>10</td>
	    <td>29</td>
	    <td>GPIO_A27</td>
	    <td>◄►</td>
	    <td>GPIO 신호</td>
	  </tr>
	  <tr>
	    <td>11</td>
	    <td>230</td>
	    <td>GPIO_A26</td>
	    <td>◄►</td>
	    <td>GPIO 신호</td>
	  </tr>
	  <tr>
	    <td>12</td>
	    <td>31</td>
	    <td>GPIO_A24</td>
	    <td>◄►</td>
	    <td>GPIO 신호</td>
	  </tr>
	  <tr>
	    <td>13</td>
	    <td>32</td>
	    <td>GPIO_A25</td>
	    <td>◄►</td>
	    <td>GPIO 신호</td>
	  </tr>
	  <tr>
	    <td>14</td>
	    <td>33</td>
	    <td>GPIO_A23</td>
	    <td>◄►</td>
	    <td>GPIO 신호</td>
	  </tr>
	  <tr>
	    <td>15</td>
	    <td>34</td>
	    <td>GPIO_A22</td>
	    <td>◄►</td>
	    <td>GPIO 신호</td>
	  </tr>
	  <tr>
	    <td>16</td>
	    <td>35</td>
	    <td>GPIO_A21</td>
	    <td>◄►</td>
		<td>GPIO 신호</td>
	  </tr>
	  <tr>
	    <td>17</td>
	    <td>36</td>
	    <td>GPIO_A20</td>
	    <td>◄►</td>
	    <td>GPIO 신호</td>
	  </tr>
	  <tr>
	    <td>18</td>
	    <td>37</td>
	    <td>GPIO_A19</td>
	    <td>◄►</td>
	    <td>GPIO 신호</td>
	  </tr>
	  <tr>
	    <td>19</td>
	    <td>38</td>
	    <td>GPIO_K13</td>
	    <td>◄►</td>
		<td>GPIO 신호</td>
	  </tr>
	  <tr>
	    <td>20</td>
	    <td>39</td>
	    <td>GPIO_K12</td>
	    <td>◄►</td>
	    <td>GPIO 신호</td>
	  </tr>
	  <tr>
	    <td>21</td>
	    <td>40</td>
	    <td>GPIO_K11</td>
	    <td>◄►</td>
	    <td>GPIO 신호</td>
	  </tr>
	  <tr>
	    <td>22</td>
	    <td>41</td>
	    <td>GPIO_A18</td>
	    <td>◄►</td>
	    <td>GPIO 신호</td>
	  </tr>
	  <tr>
	    <td>23</td>
	    <td>42</td>
	    <td>GPIO_A17</td>
	    <td>◄►</td>
	    <td>GPIO 신호</td>
	  </tr>
	  <tr>
	    <td>24</td>
	    <td>43</td>
	    <td>GPIO_A16</td>
	    <td>◄►</td>
	    <td>GPIO 신호</td>
	  </tr>
	  <tr>
	    <td>25</td>
	    <td>44</td>
	    <td>GPIO_A11</td>
	    <td>◄►</td>
	    <td>GPIO 신호</td>
	  </tr>
	  <tr>
	    <td>26</td>
	    <td>45</td>
	    <td>GPIO_A10</td>
	    <td>◄►</td>
	    <td>GPIO 신호</td>
	  </tr>
	  <tr>
	    <td>27</td>
	    <td>46</td>
	    <td>GPIO_A09</td>
	    <td>◄►</td>
	    <td>GPIO 신호</td>
	  </tr>
	  <tr>
	    <td>28</td>
	    <td>47</td>
	    <td>GPIO_A08</td>
	    <td>◄►</td>
	    <td>GPIO 신호</td>
	  </tr>
	  <tr>
	    <td>29</td>
	    <td>48</td>
	    <td>GPIO_A05</td>
	    <td>◄►</td>
	    <td>GPIO 신호</td>
	  </tr>
	  <tr>
	    <td>30</td>
	    <td>49</td>
	    <td>GPIO_A04</td>
	    <td>◄►</td>
	    <td>GPIO 신호</td>
	  </tr>
	  <tr>
	    <td>31</td>
	    <td>50</td>
	    <td>GPIO_A03</td>
	    <td>◄►</td>
	    <td>GPIO 신호</td>
	  </tr>
	  <tr>
	    <td>32</td>
	    <td>51</td>
	    <td>GPIO_A02</td>
	    <td>◄►</td>
	    <td>GPIO 신호</td>
	  </tr>
	  <tr>
	    <td>33</td>
	    <td>52</td>
	    <td>GPIO_A01</td>
	    <td>◄►</td>
	    <td>GPIO 신호</td>
	  </tr>
	  <tr>
	    <td>34</td>
	    <td>53</td>
	    <td>GPIO_A00</td>
	    <td>◄►</td>
	    <td>GPIO 신호</td>
	  </tr>
	  <tr>
	    <td>35</td>
	    <td>GND</td>
	    <td>DGND</td>
	    <td>-</td>
	    <td>그라운드</td>
	  </tr>
	  <tr>
	    <td>36</td>
	    <td>GND</td>
	    <td>DGND</td>
	    <td>-</td>
	    <td>그라운드</td>
	  </tr>
	</table>
</div>

표 4.13은 J5D100의 핀 설명을 나타냅니다.
<p align="center"><strong>표 4.13 J5D100 핀 설명</strong></p>
<div align="center">
	<table>
	  <tr>
	    <th rowspan="3"><strong>핀 번호</strong></th>
	    <th colspan="4"><strong>J5D100</strong></th>
	  </tr>
	  <tr>
	    <th rowspan="2"><strong>포트 이름</strong></th>
	    <th rowspan="2"><strong>신호 이름</strong></th>
	    <th><strong>DIR</strong></th>
	    <th rowspan="2"><strong>설명</strong></th>
	  </tr>
	  <tr>
	    <th><strong>MCU ◄► J5D100</strong></th>
	  </tr>
	  <tr>
	    <td>1</td>
	    <td>3.3V</td>
	    <td>VCP_3P3</td>
	    <td>-</td>
	    <td>전원 3.3V</td>
	  </tr>
	  <tr>
	    <td>2</td>
	    <td>3.3V</td>
	    <td>VCP_3P3</td>
	    <td>-</td>
    <td>전원 3.3V</td>
	  </tr>
	  <tr>
	    <td>3</td>
	    <td>TX0</td>
	    <td>GPIO_K08</td>
	    <td>◄►</td>
	    <td>GPIO 신호</td>
	  </tr>
	  <tr>
	    <td>4</td>
	    <td>RX0</td>
	    <td>GPIO_K01</td>
	    <td>◄</td>
	    <td>GPIO 신호</td>
	  </tr>
	  <tr>
	    <td>5</td>
	    <td>TX1</td>
	    <td>GPIO_K09</td>
	    <td>◄►</td>
	    <td>GPIO 신호</td>
	  </tr>
	  <tr>
	    <td>6</td>
	    <td>RX1</td>
	    <td>GPIO_K02</td>
	    <td>◄</td>
	    <td>GPIO 신호</td>
	  </tr>
	  <tr>
	    <td>7</td>
	    <td>TX2</td>
	    <td>GPIO_K10</td>
	    <td>◄►</td>
	    <td>GPIO 신호</td>
	  </tr>
	  <tr>
	    <td>8</td>
	    <td>RX2</td>
	    <td>GPIO_K03</td>
	    <td>◄</td>
	    <td>GPIO 신호</td>
	  </tr>
	  <tr>
	    <td>9</td>
	    <td>GND</td>
	    <td>DGND</td>
	    <td>-</td>
	    <td>DGND</td>
	  </tr>
	  <tr>
	    <td>10</td>
	    <td>GND</td>
	    <td>DGND</td>
	    <td>-</td>
	    <td>DGND</td>
	  </tr>
	</table>
</div>

그림 4.9는 VCP-G에 있는 10개 핀 헤더의 전체 핀 할당을 나타냅니다.
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Hardware/4.9%20Total%20Pin%20Assignment%20of%20Pin%20Headers%20on%20TOPST%20VCP-G%20Board.png"></p>
<p align="center"><strong>그림 4.9 VCP-G 핀 헤더의 전체 핀 할당 </strong><p>

# 참고 문헌
  - 자세한 내용은 TOPST에 문의하십시오: topst@topst.ai

**참고:** 참고 문서는 계약 조건에 따라 제공이 가능한 경우 제공될 수 있습니다. 참고 문서를 제공할 수 없는 경우에는 개발과 직접 관련된 내용을 안내해 드릴 수 있습니다.
