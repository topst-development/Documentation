## 지원 카메라 모듈
<div align="center">
    <table>
        <tr>
            <td colspan="8" align="center"><strong>보드</strong></td>
            <td align="center"><strong>모델</strong></td>
            <td align="center"><strong>센서</strong></td>
            <td align="center"><strong>센서 해상도</strong></td>
            <td align="center"><strong>기본 해상도</strong></td>
            <td align="center"><strong>프레임 레이트</strong></td>
            <td align="center"><strong>기본 비디오 경로</strong></td>
            <td align="center"><strong>비고</strong></td>
        </tr>
        <tr>
            <td rowspan="4" align="center"><strong>D3-G</strong></td>
            <td colspan="8">Arducam OV5647</td>
            <td>OV5647</td>
            <td>2592x1944 픽셀(5MP)</td>
            <td>1296x972</td>
            <td>30FPS</td>
            <td>/dev/video0</td>
            <td>기본으로 선택되는 카메라</td>
        </tr>
        <tr>
            <td colspan="8">Raspberry Pi Camera v1</td>
            <td>OV5647</td>
            <td>2592x1944 픽셀(5MP)</td>
            <td>1296x972</td>
            <td>30FPS</td>
            <td>/dev/video0</td>
            <td>기본으로 선택되는 카메라</td>
        </tr>
        <tr>
            <td colspan="8">Raspberry Pi Camera v2</td>
            <td>IMX219</td>
            <td>3280x2464 픽셀(8MP)</td>
            <td>1640x1232</td>
            <td>30FPS</td>
            <td>/dev/video0</td>
            <td>기본적으로 비활성화되어 있습니다. 활성화하려면 아래 가이드를 참조하십시오.</td>
        </tr>
        <tr>
            <td colspan="8">SEKONIX CXD5700</td>
            <td>CXD5700</td>
            <td>1920x1080 픽셀(2MP)</td>
            <td>1920x1080</td>
            <td>30FPS</td>
            <td>/dev/video0,1,2,3</td>
            <td>기본적으로 비활성화되어 있습니다. 활성화하려면 아래 가이드를 참조하십시오.</td>
        </tr>
        <tr>
            <td rowspan="4" align="center"><strong>AI-G</strong></td>
            <td colspan="8">Arducam OV5647</td>
            <td>OV5647</td>
            <td>2592x1944 픽셀(5MP)</td>
            <td>1296x972</td>
            <td>30FPS</td>
            <td>/dev/video2</td>
            <td>기본으로 선택되는 카메라</td>
        </tr>
        <tr>
            <td colspan="8">Raspberry Pi Camera v1</td>
            <td>OV5647</td>
            <td>2592x1944 픽셀(5MP)</td>
            <td>1296x972</td>
            <td>30FPS</td>
            <td>/dev/video2</td>
            <td>기본으로 선택되는 카메라</td>
        </tr>
        <tr>
            <td colspan="8">Raspberry Pi Camera v2</td>
            <td>IMX219</td>
            <td>3280x2464 픽셀(8MP)</td>
            <td>1640x1232</td>
            <td>30FPS</td>
            <td>/dev/video2</td>
            <td>기본적으로 비활성화되어 있습니다. 활성화하려면 아래 가이드를 참조하십시오.</td>
        </tr>
        <tr>
            <td colspan="8">SEKONIX CXD5700</td>
            <td>CXD5700</td>
            <td>1920x1080 픽셀(2MP)</td>
            <td>1920x1080</td>
            <td>30FPS</td>
            <td>/dev/video0,1,2</td>
            <td>기본적으로 비활성화되어 있습니다. 활성화하려면 아래 가이드를 참조하십시오.</td>
        </tr>
    </table>
</div>

# 1. 소개
본 가이드는 엔지니어가 TOPST D3-G 및 AI-G 플랫폼에서 카메라 입력을 신속하게 구동하고 AI 비전 워크로드에 대한 예비 검증을 빠르게 수행할 수 있도록 돕기 위해 작성되었습니다. 하드웨어 연결, 디바이스 트리 구성, 드라이버, 파이프라인 준비를 포함한 초기 설정의 복잡성을 줄이고, 전원 인가에서 첫 번째 비디오 프레임까지, 나아가 첫 번째 추론까지 이르는 명확하고 재현 가능한 경로를 제공하는 것을 목표로 합니다.

## 1.1 범위
- **지원 인터페이스:** MIPI CSI-2, GMSL (SerDes 기반), USB UVC
- **소프트웨어 구성 요소:** Yocto 기반 BSP 구성, 디바이스 트리 오버레이, V4L2, GStreamer, OpenCV 및 D3-G, AI-G SDK와의 연동
- **적용 사용 사례:** 로보틱스, 드론, 그리고 검사, 안전 모니터링, 객체 추적과 같은 산업 자동화 애플리케이션
- **범위 외 항목:** 카메라 ISP 튜닝, 고급 캘리브레이션 워크플로(스테레오/IMU), 완전한 엔드투엔드 애플리케이션 프레임워크

## 1.2 대상 독자
- PoC 또는 파일럿 개발을 위해 D3-G 또는 AI-G 플랫폼에 카메라를 통합하는 임베디드 및 AI 엔지니어
- 멀티 카메라 파이프라인에 의존하는 시스템을 배포하거나 검증하는 시스템 통합 담당자
- 교육 및 실험을 위해 반복 가능한 실습 환경이 필요한 교육자 및 실험실 사용자

## 1.3 본 가이드의 구성
- **하드웨어 연결:** 커넥터 핀아웃, 레인 구성, 전원 및 접지 요구 사항, 케이블 취급 지침, 참조 배선도
- **소프트웨어 구성:** 드라이버 및 디바이스 트리 구성을 포함한 BSP 설정과 udev 및 V4L2를 통한 디바이스 확인 방법
- **파이프라인 및 예제:** 단일 및 다중 카메라 프리뷰와 캡처를 위한 GStreamer 및 OpenCV 명령어와 스크립트
- **문제 해결:** 일반적인 문제, 대표적인 dmesg 패턴, I²C 프로빙 팁, 타이밍 관련 문제, 성능 검증 방법

## 1.4 사전 준비 사항
- **하드웨어:** TOPST D3-G 또는 AI-G 보드, 지원되는 카메라 모듈, 필요한 케이블/어댑터(MIPI FPC, GMSL용 동축 케이블, USB 3.0 등)
- **호스트 도구:** 시리얼 콘솔 접속, SSH 클라이언트, 기본적인 빌드/디버그 유틸리티
- **기술적 배경 지식:** Linux 셸 조작, V4L2 유틸리티, 기본적인 디바이스 트리 개념에 대한 이해
- **이미지/SDK:** D3-G, AI-G BSP 이미지(d3-g 버전 ≥ v1.3.0, ai-g 버전 ≥1.1.0)
  

# 2. 카메라 인터페이스 개요
2장에서는 D3-G 및 AI-G 보드에서 각각 지원하는 카메라 유형을 설명합니다.  
표 2.1은 D3-G 및 AI-G 플랫폼의 보드 지원 매트릭스를 나타냅니다.

<p align="center"><strong>표 2.1 보드 지원 매트릭스</strong></p>
<div align="center">
    <table>
        <tr>
            <td colspan="3" align="center"><strong>항목</strong></td>
            <td align="center"><strong>D3-G</strong></td>
            <td align="center"><strong>AI-G</strong></td>
        </tr>
        <tr>
            <td colspan="3">OS 지원</td>
            <td>Yocto, Ubuntu(desktop)</td>
            <td>Yocto, Ubuntu(Headless)</td>
        </tr>
        <tr>
            <td colspan="3">MIPI CSI-2</td>
            <td>2-4 레인, 2.1 Gbps/레인 x2</td>
            <td>2-4 레인, 1.5 Gbps/레인 x1</td>
        </tr>
        <tr>
            <td colspan="3">GMSL (SerDes)</td>
            <td>TOPST 4ch SerDes 캐리어</td>
            <td>TOPST 4ch SerDes 캐리어</td>
        </tr>
        <tr>
            <td colspan="3">USB (UVC)</td>
            <td>USB2.0/USB3.0 </td>
            <td>미지원</td>
        </tr>
    </table>
</div>

## 2.1 MIPI 카메라 개요
MIPI 카메라는 **MIPI CSI-2(Mobile Industry Processor Interface – Camera Serial Interface 2)** 표준을 통해 프로세서에 직접 연결되는 이미지 센서 기반 카메라 모듈입니다. 스마트폰, 임베디드 보드, AI 기반 카메라 시스템에서 가장 널리 사용되는 카메라 인터페이스이며, 저전력, 고대역폭, 저지연이라는 장점을 제공합니다.  
MIPI CSI-2 카메라는 일반적으로 RAW Bayer 센서 출력을 시스템에 직접 제공하며, 이미지 신호 처리(ISP)는 SoC 내부 ISP 또는 외부 ISP에서 수행됩니다. USB 카메라와 달리 MIPI 센서는 I2C 레지스터 설정을 통한 초기화와 ISP 파이프라인 구성이 필요하지만, 그 대신 센서의 성능을 최대한 활용하는 고품질 이미지 처리가 가능합니다.  
MIPI 카메라는 다음과 같은 이유로 임베디드 플랫폼에서 널리 사용됩니다.
- **높은 대역폭:** 2레인 또는 4레인 구성을 통해 MIPI 카메라는 고해상도(4K 이상) 및 고프레임 레이트 데이터를 안정적으로 전송할 수 있습니다.
- **낮은 소비 전력:** 모바일 및 임베디드 기기를 위해 설계되어 소비 전력이 대체 방식보다 현저히 낮습니다.
- **직접적인 센서 제어:** 노출, 게인, 프레임 레이트와 같은 센서 파라미터를 I2C를 통해 제어할 수 있어 세밀한 화질 조정이 가능합니다.
- **낮은 지연 시간:** RAW 데이터가 직접 전달되므로 MIPI 카메라는 로보틱스 및 임베디드 비전 시스템과 같은 실시간 애플리케이션에 적합합니다.
- **다양한 센서 선택:** Sony IMX 시리즈(IMX219, IMX708 등)와 Omnivision OV 시리즈를 포함한 다수의 센서를 동일한 CSI-2 표준에서 사용할 수 있습니다.  

MIPI 카메라는 **15핀(2레인)** 또는 **20핀(4레인)** FFC 케이블과 같은 커넥터를 사용하며, 레인 구성과 핀 매핑이 보드의 CSI 포트와 정확히 일치해야 합니다.  
Linux 기반 시스템에서는 카메라가 /dev/video* 디바이스 또는 Media Controller 노드로 인식되도록 센서 드라이버(디바이스 트리 구성 포함)를 올바르게 설정해야 합니다. 인식된 후에는 V4L2 프레임워크를 통해 비디오 스트리밍에 접근할 수 있습니다.  
이러한 특성으로 인해 MIPI 카메라는 고품질 이미지 처리, 저지연 스트리밍, AI 기반 임베디드 비전 애플리케이션을 위한 사실상의 표준 인터페이스가 되었습니다.

## 2.2 GMSL 카메라 개요
GMSL 카메라는 Gigabit Multimedia Serial Link(GMSL) 표준을 사용하여 이미지 데이터, 제어 신호, 전원을 하나의 동축 케이블 또는 차폐 연선 케이블로 전송하는 직렬화 카메라 모듈입니다. 짧은 FFC 연결이 필요한 MIPI 카메라와 달리, GMSL은 시리얼라이저–디시리얼라이저(SerDes) 쌍을 사용하여 CSI-2 이미지 데이터를 수 미터에 걸쳐 전송함으로써 장거리 및 노이즈에 강한 카메라 연동을 가능하게 합니다.  

GMSL 시스템은 임베디드 및 차량용 환경에서 다음과 같은 여러 장점을 제공합니다.
- **장거리 전송:** 최대 약 15 m 길이의 케이블에서도 안정적인 영상 전송을 지원하여 로보틱스 및 차량 센서 배치에 적합합니다.
- **높은 대역폭:** GMSL1/2/3는 멀티 기가비트 CSI-2 스트림을 전송할 수 있어 고해상도 또는 다중 카메라 구성을 구현할 수 있습니다.
- **Power over Coax (PoC):** 하나의 케이블로 전원과 데이터를 함께 전달하여 커넥터 수를 줄이고 시스템 배선을 단순화합니다.
- **견고성 및 EMI 내성:** 동축 케이블과 차동 신호 방식으로 인해 GMSL은 전기적 노이즈가 많은 환경에서도 안정적으로 동작합니다.
- **표준 센서 제어:** 디시리얼라이저가 I2C 통신을 센서로 전달하므로 일반적인 노출, 게인, 프레임 레이트 설정이 가능합니다.

일반적인 GMSL 카메라 경로는 시리얼라이저가 포함된 이미지 센서, 동축 케이블, 디시리얼라이저, 그리고 최종적으로 SoC로 향하는 CSI-2 출력으로 구성됩니다. Linux에서는 SerDes와 센서가 디바이스 트리에 올바르게 기술되면 카메라가 V4L2 또는 Media Controller 디바이스로 나타나며, 이는 표준 MIPI 카메라와 매우 유사하지만 배치와 시스템 설계 면에서 훨씬 뛰어난 유연성을 제공합니다

## 2.3 USB 카메라 개요
USB 카메라는 USB 2.0 또는 USB 3.0 인터페이스를 통해 시스템에 연결되는 디지털 이미징 장치입니다. 가장 큰 장점은 표준 UVC(USB Video Class) 프로토콜을 따르기 때문에 별도의 전용 드라이버 없이 동작한다는 점입니다. Linux, Windows, macOS 등 대부분의 운영체제가 UVC를 기본적으로 지원하므로, 사용자는 카메라를 연결한 직후 추가 설정 없이 바로 비디오 스트림을 얻을 수 있습니다.
  
USB 카메라는 다음과 같은 이유로 임베디드 플랫폼에서 폭넓게 사용됩니다:
- **플러그 앤 플레이 기능:** MIPI 센서와 달리 USB 카메라는 센서 초기화, I2C 레지스터 설정, ISP 파이프라인 구성이 필요하지 않으며, 연결 즉시 영상을 캡처할 수 있습니다.
- **높은 호환성:** 대부분의 USB 카메라는 UVC 사양을 준수하므로 제조사나 모델에 관계없이 일관된 방식으로 동작합니다.
- **다양한 해상도 및 포맷 지원:** MJPEG, YUYV, NV12와 같은 일반적인 포맷을 폭넓게 사용할 수 있습니다.
- **간편한 연결 및 배선:** USB 케이블은 배선을 단순화하며, 흔히 수 미터에 이르는 긴 거리를 지원합니다.
- **임베디드 개발에 적합:** 드라이버 관련 문제가 적어 더 빠른 프로토타이핑이 가능합니다.

Linux 기반 시스템에서 USB 카메라는 자동으로 감지되어 /dev/video* 노드로 제공됩니다. 영상 캡처와 제어는 v4l2-ctl, ffmpeg, GStreamer와 같은 표준 도구를 사용하여 수행할 수 있습니다.  
많은 USB 카메라는 자동 화이트 밸런스, 자동 노출, 색 보정과 같은 이미지 처리를 내부에서 수행하는 ISP를 내장하고 있습니다. 이를 통해 외장 ISP가 없는 보드에서도 안정적인 화질을 얻을 수 있습니다. 이러한 특성 덕분에 USB 카메라는 테스트, 임베디드 Linux 개발, 로보틱스, 신속한 프로토타이핑과 같은 분야에서 가장 간단하고 범용적인 카메라 솔루션 중 하나로 자리 잡았습니다.

## 2.4 D3-G에서 사용 가능한 카메라 종류
TOPST D3-G 플랫폼은 Yocto와 Ubuntu 환경 모두에서 동일한 카메라 종류를 지원합니다. 사용 가능한 카메라 인터페이스로는 USB, MIPI, GMSL이 있으며, 사용하는 인터페이스에 따라 설정에 약간의 차이가 있습니다.  
1. **MIPI 카메라**  
TOPST D3-G는 두 개의 MIPI CSI 포트를 제공하며, 포트당 하나의 MIPI 카메라를 연결할 수 있습니다. MIPI CSI 인터페이스는 두 가지 커넥터 형식을 지원합니다:
    - **15-pin(2-Lane):** OV5647 또는 IMX219와 같은 저대역폭 센서에 적합합니다.
    - **20-pin (4-Lane):** 고해상도 또는 고프레임레이트 센서를 위한 형식입니다.
2. **GMSL 카메라**  
GMSL 카메라는 장거리 전송을 지원하며 자동차 및 산업용 애플리케이션에서 일반적으로 사용됩니다. TOPST D3-G에서 GMSL을 사용하려면 다음 구성 요소가 필요합니다:
    1. **20-pin MIPI CSI (4-Lane)** 포트를 **TOPST MIPI Gender Board**에 연결합니다.
    2. **Deserializer (Des)** 보드를 Gender Board 위에 장착합니다.
    3. Fakra 케이블을 사용하여 최대 4대의 GMSL 카메라를 Des 보드에 연결합니다.
3. **USB 카메라**  
USB 카메라는 가장 간단하게 시작할 수 있는 방법을 제공합니다. 보드의 USB 2.0 또는 USB 3.0 포트 중 어디에 연결하더라도 자동으로 인식되며 추가 설정 없이 사용할 수 있습니다.  
해당 장치가 V4L2 호환 UVC 카메라인 경우, 다음 명령을 사용하여 인식 여부를 확인할 수 있습니다:  
    ``` 
    v4l2-ctl --list-devices
    ```

## 2.4 D3-G에서 사용 가능한 카메라 종류
TOPST AI-G 플랫폼도 여러 카메라 입력 인터페이스를 지원하지만, 전체적인 구성은 D3-G보다 단순하며 고성능 AI 워크로드에 최적화되어 있습니다. 특히 이 플랫폼에서는 USB 카메라가 지원되지 않습니다. MIPI, GMSL 입력만 사용할 수 있습니다.  
1. **MIPI 카메라**  
TOPST D3-G는 두 개의 MIPI CSI 포트를 제공하며, 포트당 하나의 MIPI 카메라를 연결할 수 있습니다. MIPI CSI 인터페이스는 두 가지 커넥터 형식을 지원합니다:
    - **15-pin(2-Lane):** OV5647 또는 IMX219와 같은 저대역폭 센서에 적합합니다.
    - **20-pin (4-Lane):** 고해상도 또는 고프레임레이트 센서를 위한 형식입니다.
2. **GMSL 카메라**  
GMSL 카메라는 장거리 전송을 지원하며 자동차 및 산업용 애플리케이션에서 일반적으로 사용됩니다. TOPST D3-G에서 GMSL을 사용하려면 다음 구성 요소가 필요합니다:
    1. **20-pin MIPI CSI (4-Lane)** 포트를 **TOPST MIPI Gender Board**에 연결합니다.
    2. **Deserializer (Des)** 보드를 Gender Board 위에 장착합니다.
    3. Fakra 케이블을 사용하여 최대 4대의 GMSL 카메라를 Des 보드에 연결합니다.

# 3. 카메라 연결 가이드
3장에서는 D3-G 및 AI-G 보드에 카메라를 연결하는 방법을 설명합니다.  
이 절은 카메라가 안정적으로 동작할 수 있도록 보드와 카메라가 올바르게 연결되었는지 확인합니다. 사용하려는 카메라를 연결하려면 아래 가이드를 따르십시오.

## 3.1 D3-G에 카메라 연결하기
MIPI CSI-2, GMSL, USB 카메라를 D3-G에 연결하는 방법은 아래 가이드를 따르십시오.  

### 3.1.1 MIPI CSI-2 카메라
그림 3.1은 D3-G의 MIPI CSI 커넥터를 보여줍니다. D3-G는 2채널의 MIPI CSI를 지원하며, 각 채널은 2-lane 인터페이스로 구성됩니다. 4-lane 인터페이스는 선택 사항이며 15-pin 커넥터 대신 20-pin 커넥터가 필요합니다. 핀에 대한 정보는 D3-G Hardware-User Guide를 참조하십시오.

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/accessories/Camera/3.1%20MIPI%20CSI%20Connector%20on%20D3-G.png"></p>
<p align="center"><strong>그림 3.1 D3-G의 MIPI CSI 커넥터</strong></p>

MIPI 카메라를 연결할 때는 FFC(Flat Flexible Cable)를 사용하십시오. 올바른 케이블 유형과 방향은 그림 3.2 및 3.3을 참조하십시오.

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/accessories/Camera/3.2%20FFC%20Type.png"></p>
<p align="center"><strong>그림 3.2 FFC 유형</strong></p>

FFC 케이블은 1.0 mm, 15-pin 유형이며, 한쪽 면에는 다른 색상의 표시(파란색 또는 회색)가 있어야 합니다. 케이블은 B-Forward Direction 방향으로 삽입해야 합니다. FFC 유형은 그림 3.2를 참조하십시오.

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/accessories/Camera/3.3%20An%20example%20of%20an%20FFC%20connected%20to%20the%20D3-G%20MIPI0%2015-pin%20Connector.png"></p>
<p align="center"><strong>그림 3.3 D3-G MIPI0 15-pin 커넥터에 FFC를 연결한 예시</strong></p>

FFC의 15개 은색 접점이 D3-G MIPI 커넥터 내부의 15개 은색 접점과 정렬되도록 하십시오.  
MIPI1 커넥터를 사용할 때도 동일한 연결 방법이 적용되므로, MIPI0 커넥터와 같은 방식으로 연결하십시오.

### 3.1.2 GMSL 카메라
GMSL 카메라는 Fakra 케이블을 사용합니다. 따라서 D3-G 보드에 직접 연결할 수 없습니다. 대신 Deserializer (Des) 보드와 TOPST MIPI Gender Board를 거쳐 D3-G와 인터페이스해야 합니다.  
연결 구조는 다음과 같습니다.  

<p align="center"><strong>< D3-G > ↔ < TOPST MIPI Gender Board > ↔ < Des Board > ↔ < GMSL Camera ></strong></p>

GMSL 카메라를 사용하려면 TOPST MIPI Gender Board가 필요하며, 이는 20-pin MIPI 커넥터를 통해 연결해야 합니다. 예를 들어 4대의 GMSL 카메라를 사용할 계획이라면 그림 3.4와 같이 20-pin MIPI 인터페이스를 사용하여 연결해야 합니다.

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/accessories/Camera/3.4%2020-pin%20MIPI0%20Connector.png"></p>
<p align="center"><strong>그림 3.4 20-pin MIPI0 커넥터</strong></p>  

1. D3-G 보드를 TOPST MIPI Gender Board에 연결하기.  
    FFC 케이블은 1.0 mm, 20-pin 유형이며, 한쪽 면에는 다른 색상의 표시(파란색 또는 회색)가 있어야 합니다. 케이블은 A-Forward Direction 방향으로 삽입해야 합니다. FFC 유형은 그림 3.5를 참조하십시오.  
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/accessories/Camera/3.2%20FFC%20Type.png"></p>
    <p align="center"><strong>그림 3.5 FFC 유형</strong></p>
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/accessories/Camera/3.6%20Anexample%20of%20an%20FFC%20connected%20to%20the%20D3-G%20MIPI0%2020-pin%20Connector.png"></p>
    <p align="center"><strong>그림 3.6 D3-G MIPI0 20-pin 커넥터에 FFC를 연결한 예시</strong></p> 
    FFC의 20개 은색 접점이 D3-G MIPI 커넥터 내부의 20개 은색 접점과 정렬되도록 하십시오
    MIPI1 커넥터를 사용할 때도 동일한 연결 방법이 적용되므로, MIPI0 커넥터와 같은 방식으로 연결하십시오.
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/accessories/Camera/3.7%20An%20example%20of%20an%20FFC%20connected%20th%20toe%20TOPST%20MIPI%20Gender%20Board%20MIPI%20Connector.png"></p>
    <p align="center"><strong>그림 3.7 TOPST MIPI Gender Board MIPI 커넥터에 FFC를 연결한 예시</strong></p>
2. Deserializer 보드를 MIPI Gender Board에 연결하기.  
    MIPI Gender Board의 JH2 커넥터를 SerDes 보드 하단에 위치한 JH1 커넥터에 결합하십시오.
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/accessories/Camera/3.8%20JH2%20Connector.png"></p>
    <p align="center"><strong>그림 3.8 JH2 커넥터</strong></p>
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/accessories/Camera/3.9%20JH1%20Connector.png"></p>
    <p align="center"><strong>그림 3.9 JH1 커넥터</strong></p>
3. GMSL 카메라 연결
    그림 3.10과 같이 카메라를 연결하십시오. 그림은 2대의 카메라를 사용하는 예시를 보여주지만, 필요에 따라 1대에서 4대까지 원하는 수의 카메라를 연결할 수 있습니다.
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/accessories/Camera/3.10%20GMSL%20Camera%20Connection.png"></p>
    <p align="center"><strong>그림 3.10 JH2 커넥터</strong></p>

### 3.1.3 USB 카메라
USB 카메라는 D3-G의 USB 2.0 또는 USB 3.0 포트에 연결하여 사용할 수 있습니다. USB 3.0 사양이 필요한 USB 카메라를 사용할 때는 반드시 USB 3.0 포트에 연결하십시오.

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/accessories/Camera/3.11%20USB%20Camera%20Connection.png"></p>
<p align="center"><strong>그림 3.11 USB 카메라 연결</strong></p>

## 3.2 AI-G에 카메라 연결하기
### 3.2.1 MIPI CSI-2 카메라
그림 3.12는 AI-G의 MIPI CSI 커넥터를 보여줍니다. AI-G는 2채널의 MIPI CSI를 지원하며, 각 채널은 2-lane 인터페이스로 구성됩니다.

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/accessories/Camera/3.12%20MIPI%20CSI%20Connector%20on%20AI-G.png"></p>
<p align="center"><strong>그림 3.12 AI-G의 MIPI CSI 커넥터</strong></p>

MIPI 카메라를 연결할 때는 FFC(Flat Flexible Cable)를 사용하십시오. 올바른 케이블 종류와 방향은 그림 3.13 및 3.14를 참조하십시오.

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/accessories/Camera/3.2%20FFC%20Type.png"></p>
<p align="center"><strong>그림 3.13 FFC 종류</strong></p>

FFC 케이블은 1.0 mm, 15핀 타입이며, 한쪽 면에 다른 색상의 표시(파란색 또는 회색)가 있어야 합니다. 케이블은 B-Forward Direction 방향으로 삽입해야 합니다. FFC 종류는 그림 3.13을 참조하십시오.

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/accessories/Camera/3.14%20An%20example%20of%20an%20FFC%20connected%20to%20the%20AI-G%20MIPI%2015-pin%20Connector.png"></p>
<p align="center"><strong>그림 3.14 AI-G MIPI 15핀 커넥터에 FFC를 연결한 예</strong></p>

FFC의 은색 접점 15개가 AI-G MIPI 커넥터 내부의 은색 접점 15개와 정렬되는지 확인하십시오.

### 3.2.2 GMSL 카메라
GMSL 카메라는 Fakra 케이블을 사용합니다. 따라서 AI-G 보드에 직접 연결할 수 없습니다. 대신 Deserializer(Des) 보드와 TOPST MIPI Gender Board를 거쳐 AI-G와 연결해야 합니다.  
연결 구조는 다음과 같습니다.

<p align="center"><strong>< AI-G > ↔ < TOPST MIPI Gender Board > ↔ < Des Board > ↔ < GMSL Camera ></strong></p>

GMSL 카메라를 사용하려면 TOPST MIPI Gender Board가 필요하며, 20핀 MIPI 커넥터를 통해 연결해야 합니다. 예를 들어 GMSL 카메라 4대를 사용하려면 그림 3.15와 같이 20핀 MIPI 인터페이스를 사용하여 연결해야 합니다.

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/accessories/Camera/3.15%2020-pin%20MIPI%20Connector.png"></p>
<p align="center"><strong>그림 3.15 20핀 MIPI 커넥터</strong></p>

1. AI-G 보드를 TOPST MIPI Gender Board에 연결합니다.  
    FFC 케이블은 1.0 mm, 20핀 타입이며, 한쪽 면에 다른 색상의 표시(파란색 또는 회색)가 있어야 합니다. 케이블은 A-Forward Direction 방향으로 삽입해야 합니다. FFC 종류는 그림 3.16을 참조하십시오.
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/accessories/Camera/3.2%20FFC%20Type.png"></p>
    <p align="center"><strong>그림 3.16 FFC 종류</strong></p>
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/accessories/Camera/3.17%20An%20example%20of%20an%20FFC%20connected%20to%20the%20AI-G%20MIPI%2020-pin%20Connector.png"></p>
    <p align="center"><strong>그림 3.17 AI-G MIPI 20핀 커넥터에 FFC를 연결한 예</strong></p>
    FFC의 은색 접점 20개가 AI-G MIPI 커넥터 내부의 은색 접점 20개와 정렬되는지 확인하십시오
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/accessories/Camera/3.18%20An%20example%20of%20an%20FFC%20connected%20to%20the%20TOPST%20MIPI%20Gender%20Board%20MIPI%20Connector.png"></p>
    <p align="center"><strong>그림 3.18 TOPST MIPI Gender Board의 MIPI 커넥터에 FFC를 연결한 예</strong></p>
2. Deserializer 보드를 MIPI Gender Board에 연결하기.  
    MIPI Gender Board의 JH2 커넥터를 SerDes 보드 하단에 위치한 JH1 커넥터에 연결하십시오.
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/accessories/Camera/3.19%20JH2%20Connector.png"></p>
    <p align="center"><strong>그림 3.19 JH2 커넥터</strong></p>
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/accessories/Camera/3.20%20JH1%20Connector.png"></p>
    <p align="center"><strong>그림 3.20 JH1 커넥터</strong></p>
3. GMSL 카메라 연결
    그림 3.21과 같이 카메라를 연결하십시오. 그림은 카메라 2대를 사용한 예를 보여주지만, 필요에 따라 1대에서 4대까지 원하는 수의 카메라를 연결할 수 있습니다.
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/accessories/Camera/3.21%20GMSL%20Camera%20Connection.png"></p>
    <p align="center"><strong>그림 3.21 GMSL 카메라 연결</strong></p>

# 4. 소프트웨어 설정
4장에서는 카메라 동작에 필요한 소프트웨어 설정을 설명합니다. D3-G 및 AI-G 플랫폼에서 MIPI CSI-2 카메라(OV5647, IMX219)와 GMSL 카메라를 구성하려면 아래에 제공된 Yocto 설정 지침을 참조하십시오.

## 4.1 MIPI CSI-2 카메라 설정 가이드
TX 데이터 레이트는 다음 수식을 사용하여 계산할 수 있습니다.

<p align="center"><strong>TX 데이터 레이트 ={ H_active }×{V_active }×{FPS}×{BPP}×{ Number_of_Cameras} × 1.3 (마진)</strong></p>

전체 데이터 레이트는 레인당 2.1 Gbps인 D3-G MIPI CSI-2 대역폭 한계를 초과해서는 안 됩니다.  
또한 전체 데이터 레이트는 레인당 1.5 Gbps인 AI-G MIPI CSI-2 대역폭 한계를 초과해서는 안 됩니다

### 4.1.1 D3-G OV5647 설정 가이드
#### 4.1.1.1 OV5647 센서 개요
##### 4.1.1.1.1 소개
OV5647은 작은 크기, 안정적인 성능, 표준 MIPI CSI-2 인터페이스와의 호환성 덕분에 임베디드 카메라 애플리케이션에서 널리 사용되는 500만 화소 CMOS 이미지 센서입니다. 또한 Raspberry Pi Camera Module v1에 사용된 이미지 센서이며 다양한 Arducam OV5647 카메라 모듈을 통해 이용할 수 있고, 이들 모두 TOPST D3-G 플랫폼과 호환됩니다.  
사용자는 카메라 동작을 위해 Raspberry Pi Camera v1 또는 Arducam OV5647 모듈을 MIPI CSI 포트에 연결할 수 있습니다.

TOPST D3-G 플랫폼에서 OV5647은 15핀 또는 20핀 MIPI CSI 커넥터를 통해 연결되며 V4L2 프레임워크로 제어되어 Yocto와 Ubuntu 환경 모두에서 일관된 동작을 제공합니다.

##### 4.1.1.1.2 지원 해상도 및 FPS
OV5647 카메라 모듈(Raspberry Pi v1 또는 Arducam OV5647)의 사양은 다음과 같습니다.  

<p align="center"><strong>표 4.1 OV5647 카메라 모듈 사양</strong></p>
<div align="center">
    <table>
        <tr>
            <td colspan="2" align="center"><strong>사양</strong></td>
            <td align="center"><strong>설명</strong></td>
        </tr>
        <tr>
            <td colspan="2">센서</td>
            <td>OmniVision OV5647</td>
        </tr>
        <tr>
            <td colspan="2">해상도</td>
            <td>2592 x 1944 (5MP)</td>
        </tr>
        <tr>
            <td colspan="2">출력 포맷</td>
            <td>RAW, YUV, JPEG</td>
        </tr>
        <tr>
            <td colspan="2">인터페이스</td>
            <td>MIPI CSI-2</td>
        </tr>
        <tr>
            <td colspan="2">프레임 레이트</td>
            <td>1080p30, 720p60, 480p90</td>
        </tr>
        <tr>
            <td colspan="2">렌즈</td>
            <td>고정 초점</td>
        </tr>
        <tr>
            <td colspan="2">화각(FOV)</td>
            <td>Up to 54°</td>
        </tr>
        <tr>
            <td colspan="2">케이블 종류</td>
            <td>FFC(15핀)</td>
        </tr>
        <tr>
            <td colspan="2">보드 크기</td>
            <td>25mm x 24mm</td>
        </tr>
        <tr>
            <td colspan="2">호환성</td>
            <td>D3-G 및 Rasbperry Pi(MIPI CSI-2 포트를 통해)</td>
        </tr>
    </table>
</div>

D3-G에서 지원하는 센서 해상도 및 FPS는 다음과 같습니다.  
<p align="center"><strong>표 4.2 D3-G의 OV5647 센서 해상도</strong></p>
<div align="center">
    <table>
        <tr>
            <td colspan="3" align="center"><strong>해상도</strong></td>
            <td align="center"><strong>FPS</strong></td>
            <td align="center"><strong>설명</strong></td>
        </tr>
        <tr>
            <td colspan="3">1920x1080</td>
            <td>30</td>
            <td>전체 해상도 프레임의 중앙 영역을 크롭하여 1080p 이미지를 출력합니다</td>
        </tr>
        <tr>
            <td colspan="3">1296x972</td>
            <td>30</td>
            <td>2×2 픽셀 비닝을 사용하여 감도를 높이고 노이즈를 줄입니다</td>
        </tr>
        <tr>
            <td colspan="3">640x480</td>
            <td>60</td>
            <td>2×2 비닝과 <strong>서브샘플링</strong>을 결합합니다. 서브샘플링은 리드아웃 중 픽셀을 건너뛰어 데이터 처리량을 줄이고 더 높은 프레임 레이트를 구현합니다</td>
        </tr>
    </table>
</div>

**참고:** 표 4.2에 나타난 바와 같이 D3-G의 ISP 사양으로 인해 전체 해상도인 **2592×1944는 사용할 수 없습니다**.

<p align="center"><strong>표 4.3 동작 모드별 최대 해상도</strong></p>
<div align="center">
    <table>
        <tr>
            <td rowspan="2" align="center"><strong>ISP 코어</strong></td>
            <td colspan="2"><strong>동작 모드별 해상도</strong></td>
        </tr>
        <tr>
            <td align="center"><strong>기본 모드</strong></td>
            <td align="center"><strong>메모리 공유 모드</strong></td>
        </tr>
        <tr>
            <td>ISP0</td>
            <td>2048x1536 @ 60fps</td>
            <td>2048x1536 @ 60fps</td>
        </tr>
        <tr>
            <td>ISP1</td>
            <td>2560x1440 @ 60fps</td>
            <td>2560x1440 @ 60fps</td>
        </tr>
        <tr>
            <td>ISP2</td>
            <td>1280x720 @ 60fps</td>
            <td>1560x1440 @ 60fps</td>
        </tr>
        <tr>
            <td>ISP3</td>
            <td>1280x720 @ 60fps</td>
            <td>N/A</td>
        </tr>
    </table>
</div>

#### 4.1.1.2 Yocto에서의 OV5647 해상도 설정: 드라이버
Yocto 빌드 과정에서 OV5647 센서의 해상도를 변경하려면 아래 지침을 따르십시오.  

먼저 OV5647을 활성화하려면 다음 위치에 TOPST_CAM_MODULE = "ov5647"이 설정되어 있는지 확인하십시오.  
{build_dir}/build/d3-g-topst-main/conf/local.conf.  
이 항목은 첫 빌드를 위해 저장소를 초기화할 때 기본적으로 활성화되지만, 다시 한 번 확인하십시오.

또한 빌드 과정에서 소스 코드가 삭제되지 않도록 다음 위치에서 아래 줄을 활성화하십시오.  
{build_dir}/build/d3-g-topst-main/conf/local.conf:
```
INHERIT:remove = “rm_work”
```

위 옵션을 활성화한 후 다음 명령으로 이미지를 다시 빌드하십시오.
```
$ bitbake telechips-topst-image
```

두 번째로, 빌드가 완료되면 ov5647.c 드라이버 파일을 열고 필요한 수정을 적용하십시오.

다음 디렉터리로 이동하십시오.
```
${build_dir}/build/d3-g-topst-main/tmp/work/d3_g_topst_main-telechips-linux/linux-topst/5.10.205-r0/git/drivers/media/i2c/telechips/
```

코드를 수정하기 전에, 현재 드라이버가 다음 세 가지 모드를 지원한다는 점에 유의하십시오.
- 1920x1080 @ 30fps
- 1296x972 @ 30fps
- 640x480 @ 60fps  

각 해상도는 순서대로 Mode 1, Mode 2, Mode 3에 해당합니다.  

1920×1080 @ 30fps 모드는 센터 크롭을 사용하므로 화각이 좁아지고, 640×480 모드는 해상도가 충분하지 않습니다. 반면 1296×972 모드는 2×2 비닝을 사용하여 더 넓은 화각을 제공하므로 현재 기본 모드로 사용됩니다.  
ov5647.c 드라이버 파일을 열고 아래와 같이 OV5647 기본 모드를 수정하십시오.
```
#define OV5647_DEFAULT_MODE (&supported_modes_10bit[2])
```
1920×1080 @ 30fps는 Mode 1에 해당하므로 **“#define OV5647_DEFAULT_MODE (&supported_modes_10bit[1])”**를 그대로 사용할 수 있습니다.  
1296×972 @ 30fps 모드는 Mode 2에 해당하므로 **“#define OV5647_DEFAULT_MODE (&supported_modes_10bit[2])”**가 이미 올바르게 설정되어 있습니다.  
Mode 3에 해당하는 640×480 @ 60fps의 경우, 정의를 **“#define OV5647_DEFAULT_MODE (&supported_modes_10bit[3])”**로 변경합니다.

세 번째로, 커널을 다시 빌드하고 FAI 이미지를 생성합니다.  
빌드 디렉터리로 돌아가 아래 명령어를 사용하여 커널을 다시 빌드합니다.
```
$ cd ${build_dir}/build/d3-g-topst-main/
$ bitbake -C compile linux-topst
$ cd ${build_dir}
$ ./stitch-fai-d3.sh
```
그 후 생성된 output_d3g.fai를 FWDN을 사용하여 보드에 플래싱하면 원하는 해상도로 OV5647 센서를 사용할 수 있습니다.

**참고:** MIPI1-CSI 포트를 사용하려면 다음 경로에 있는 tcc805x-videoinput-camera-module.dtsi 파일을 여십시오.
“{build_dir}/build/d3-g-topst-main/tmp/work/d3_g_topst_main-telechips-linux/linux-topst/5.10.205-r0/git/arch/arm64/boot/dts/telechips/tcc805x/override/” and change the included dtsi file from “tcc805x-videoinput-mipi0-ov5647.dtsi” to “tcc805x-videoinput-mipi1-ov5647.dtsi”. + Open the tcc805x-videoinput.dtsi file located in "{build_dir}/build/d3-g-topst-main/tmp/work/d3_g_topst_main-telechips-linux/linux-topst/5.10.205-r0/git/arch/arm64/boot/dts/telechips/tcc805x/" and change the mipi chmux from "mipi-chmux-0 = <0>;" to "mipi-chmux-0 = <1>;".

### 4.1.2 D3-G IMX219 설정 가이드
#### 4.1.2.1 IMX219 센서 개요
##### 4.1.2.1.1 소개
IMX219는 Sony의 고성능 8메가픽셀 CMOS 이미지 센서로, 소형 카메라 모듈에서 뛰어난 화질과 낮은 소비 전력, 안정적인 촬영 성능을 제공하는 것으로 잘 알려져 있습니다. 또한 Raspberry Pi Camera Module v2에 사용된 센서이며, 임베디드 비전 시스템, 로보틱스, AI 기반 카메라 애플리케이션에 널리 채택되고 있습니다.

TOPST D3-G 플랫폼에서 IMX219 센서는 15핀 또는 20핀 MIPI CSI 커넥터를 통해 연결할 수 있으며, V4L2 프레임워크를 통해 제어됩니다. 이를 통해 Yocto와 Ubuntu 환경 모두에서 일관된 인터페이스와 안정적인 카메라 동작을 구현할 수 있습니다.

IMX219는 높은 해상도(8MP)와 저노이즈 이미징 특성을 갖추고 있어 TOPST D3-G 플랫폼에서 고품질 영상 촬영 및 이미지 처리 기능을 구현하는 데 매우 적합합니다.

##### 4.1.2.1.2 지원 해상도 및 FPS
IMX219 카메라 모듈(Raspberry Pi v2)의 사양은 다음과 같습니다.

<p align="center"><strong>표 4.4 IMX219 카메라 모듈 사양</strong></p>
<div align="center">
    <table>
        <tr>
            <td colspan="2" align="center"><strong>사양</strong></td>
            <td align="center"><strong>설명</strong></td>
        </tr>
        <tr>
            <td colspan="2">센서</td>
            <td>Sony Imx219</td>
        </tr>
        <tr>
            <td colspan="2">해상도</td>
            <td>3280 x 2464 (8 MP)</td>
        </tr>
        <tr>
            <td colspan="2">출력 포맷</td>
            <td>RAW, YUV, JPEG</td>
        </tr>
        <tr>
            <td colspan="2">인터페이스</td>
            <td>MIPI CSI-2</td>
        </tr>
        <tr>
            <td colspan="2">프레임 레이트</td>
            <td>1080p60, 720p180, 480p206</td>
        </tr>
        <tr>
            <td colspan="2">렌즈</td>
            <td>초점 조절 가능</td>
        </tr>
        <tr>
            <td colspan="2">화각(FOV)</td>
            <td>Up to 62°</td>
        </tr>
        <tr>
            <td colspan="2">케이블 종류</td>
            <td>FFC(15핀)</td>
        </tr>
        <tr>
            <td colspan="2">보드 크기</td>
            <td>25mm x 24mm</td>
        </tr>
        <tr>
            <td colspan="2">호환성</td>
            <td>D3-G 및 Rasbperry Pi(MIPI CSI-2 포트를 통해)</td>
        </tr>
    </table>
</div>

D3-G에서 지원하는 센서 해상도 및 FPS는 다음과 같습니다.
<p align="center"><strong>표 4.5 D3-G의 IMX219 센서 해상도</strong></p>
<div align="center">
    <table>
        <tr>
            <td colspan="3" align="center"><strong>해상도</strong></td>
            <td align="center"><strong>FPS</strong></td>
            <td align="center"><strong>설명</strong></td>
        </tr>
        <tr>
            <td colspan="3">1920x1080</td>
            <td>30</td>
            <td>전체 해상도 프레임의 중앙 영역을 크롭하여 1080p 이미지를 출력합니다</td>
        </tr>
        <tr>
            <td colspan="3">1640x1232</td>
            <td>30</td>
            <td>2×2 픽셀 비닝을 사용하여 감도를 높이고 노이즈를 줄입니다</td>
        </tr>
        <tr>
            <td colspan="3">640x480</td>
            <td>30</td>
            <td>2×2 비닝과 <strong>서브샘플링</strong>을 결합하여 리드아웃 시 픽셀을 건너뛰어 데이터 처리량을 줄입니다</td>
        </tr>
    </table>
</div>  

**참고:** 표 4.5에 나와 있듯이 D3-G의 ISP 사양으로 인해 **3820×2464 전체 해상도는 사용할 수 없습니다**.

<p align="center"><strong>표 4.6 동작 모드별 최대 해상도</strong></p>
<div align="center">
    <table>
        <tr>
            <td rowspan="2" align="center"><strong>ISP 코어</strong></td>
            <td colspan="2"><strong>동작 모드별 해상도</strong></td>
        </tr>
        <tr>
            <td align="center"><strong>기본 모드</strong></td>
            <td align="center"><strong>메모리 공유 모드</strong></td>
        </tr>
        <tr>
            <td>ISP0</td>
            <td>2048x1536 @ 60fps</td>
            <td>2048x1536 @ 60fps</td>
        </tr>
        <tr>
            <td>ISP1</td>
            <td>2560x1440 @ 60fps</td>
            <td>2560x1440 @ 60fps</td>
        </tr>
        <tr>
            <td>ISP2</td>
            <td>1280x720 @ 60fps</td>
            <td>1560x1440 @ 60fps</td>
        </tr>
        <tr>
            <td>ISP3</td>
            <td>1280x720 @ 60fps</td>
            <td>N/A</td>
        </tr>
    </table>
</div>

#### 4.1.2.2 Yocto에서 IMX219 활성화
D3-G SDK는 기본적으로 OV5647이 활성화되도록 구성되어 있으므로, 빌드하기 전에 IMX219를 활성화해야 합니다.   
SDK가 이미 빌드된 경우와 처음 빌드하는 경우의 두 가지 경우를 고려해야 합니다.

##### 4.1.2.2.1 최초 빌드 전에 IMX219 활성화하기
최초 빌드의 경우 아래 단계에 따라 IMX219를 활성화한 후 빌드를 진행하십시오.
1. 환경 설정 스크립트를 source하고 옵션 2를 선택합니다
    ```
    $ source poky/meta-topst/topst-build.sh
    ```
2. 아래 경로에 있는 local.conf 파일을 엽니다
    ```
    ${build_dir}/build/d3-g-topst-main/conf/local.conf
    ```
3. ov5647에 대한 TOPST_CAM_MODULE 항목을 주석 처리하고 imx219 항목을 활성화합니다
    ```
    #TOPST_CAM_MODULE = "ov5647"
    TOPST_CAM_MODULE = "imx219"
    ```
4. 빌드를 실행합니다
    ```
    $ bitbake telechips-topst-image
    ```
##### 4.1.2.2.2 빌드가 이미 완료된 후 IMX219 활성화하기
기존 빌드는 기본적으로 OV5647 센서가 활성화되도록 구성되어 있습니다. 아래 단계에 따라 IMX219를 활성화하십시오.
1. 아래 경로에 있는 local.conf 파일을 엽니다
    ```
    ${build_dir}/build/d3-g-topst-main/conf/local.conf
    ```
2. ov5647에 대한 TOPST_CAM_MODULE 항목을 주석 처리하고 imx219 항목을 활성화합니다
    ```
    #TOPST_CAM_MODULE = "ov5647"
    TOPST_CAM_MODULE = "imx219"
    ```
3. isp-server와 isp-firmware에 대해 cleansstate를 실행합니다
    ```
    $ bitbake -c cleansstate isp-firmware
    $ bitbake -c cleansstate isp-server
    ```
4. 빌드를 실행합니다
    ```
    $ bitbake telechips-topst-image


#### 4.1.2.3 Yocto에서의 IMX219 해상도 구성: 드라이버
Yocto 빌드 과정에서 IMX219 센서의 해상도를 변경하려면 아래 지침을 따르십시오.

먼저 imx219를 활성화하려면 TOPST_CAM_MODULE = "imx219"가 설정되어 있는지 확인합니다
{build_dir}/build/d3-g-topst-main/conf/local.conf.

또한 빌드 과정에서 소스 코드가 제거되지 않도록 다음 줄을 활성화합니다
{build_dir}/build/d3-g-topst-main/conf/local.conf:
```
INHERIT:remove = “rm_work”
```

위 옵션을 활성화한 후 다음 명령으로 이미지를 다시 빌드하십시오.
```
$ bitbake telechips-topst-image
```

두 번째로, 빌드가 완료된 후 imx219.c 드라이버 파일을 열고 필요한 수정 사항을 적용합니다.

다음 디렉터리로 이동하십시오.
```
${build_dir}/build/d3-g-topst-main/tmp/work/d3_g_topst_main-telechips-linux/linux-topst/5.10.205-r0/git/drivers/media/i2c/telechips/
```

코드를 수정하기 전에, 현재 드라이버가 다음 세 가지 모드를 지원한다는 점에 유의하십시오.
- 1920x1080 @ 30fps
- 1640x1232 @ 30fps
- 640x480 @ 30fps

각 해상도는 순서대로 Mode 1, Mode 2, Mode 3에 해당합니다.

1920×1080 @ 30fps 모드는 센터 크롭을 사용하므로 화각이 좁아지고, 640×480 모드는 해상도가 충분하지 않습니다. 반면 1640×1232 모드는 2×2 비닝을 사용하여 더 넓은 화각을 제공하므로, 현재 기본 모드로 사용되고 있습니다.  
imx219.c 드라이버 파일을 열고, imx219_set_default_format, imx219_open, imx219_probe 함수 내부에서 아래에 설명된 부분을 수정합니다.
- imx219_set_default_format
    ```
    fmt->width = supported_modes[2].width;
    fmt->height = supported_modes[2].height;
    ```
- imx219_open
    ```
    try_fmt_img->width = supported_modes[2].width;
    try_fmt_img->height = supported_modes[2].height;
    ```
- imx219_probe
    ```
    imx219->mode = &supported_modes[2];
    ```

1920×1080 @ 30fps는 Mode 1에 해당하므로, 세 함수 내부의 모든 supported_modes 참조를 **“supported_modes[1]”**로 변경하십시오.  
1640×1232 @ 30fps 모드는 Mode 2에 해당하므로, 이에 맞추어 **“supported_modes[2]”**로 변경하십시오.  
Mode 3에 해당하는 640×480 @ 30fps의 경우 모든 참조를 **“supported_modes [3]”**으로 변경합니다.

세 번째로, 커널을 다시 빌드하고 FAI 이미지를 생성합니다.  
빌드 디렉터리로 돌아가 아래 명령어를 사용하여 커널을 다시 빌드합니다.
```
$ cd ${build_dir}/build/d3-g-topst-main/
$ bitbake -C compile linux-topst
$ cd ${build_dir}
$ ./stitch-fai-d3.sh
```

그런 다음 생성된 output_d3g.fai를 FWDN으로 보드에 플래싱하면 원하는 해상도로 IMX219 센서를 사용할 수 있습니다.

**참고:** MIPI1-CSI 포트를 사용하려면 다음 경로에 있는 tcc805x-videoinput-camera-module.dtsi 파일을 여십시오.
“{build_dir}/build/d3-g-topst-main/tmp/work/d3_g_topst_main-telechips-linux/linux-topst/5.10.205-r0/git/arch/arm64/boot/dts/telechips/tcc805x/override/”and change the included dtsi file from “tcc805x-videoinput-mipi0-imx219.dtsi” to “tcc805x-videoinput-mipi1-imx219.dtsi”. + Open the tcc805x-videoinput.dtsi file located in "{build_dir}/build/d3-g-topst-main/tmp/work/d3_g_topst_main-telechips-linux/linux-topst/5.10.205-r0/git/arch/arm64/boot/dts/telechips/tcc805x/" and change the mipi chmux from "mipi-chmux-0 = <0>;" to "mipi-chmux-0 = <1>;".

#### 4.1.2.4 Yocto에서 IMX219의 FPS를 높이는 방법: 드라이버 및 디바이스 트리
IMX219 센서 설명에 따르면 이 센서는 1080p60, 720p180, VGA206과 같은 고프레임레이트 모드를 지원합니다. 따라서 imx219.c 드라이버가 지원하는 해상도인 1920×1080, 1640×1232, 640×480에서 FPS를 높일 수 있습니다. D3-G 플랫폼의 ISP 코어는 최대 60fps를 지원하므로 이러한 해상도는 각각 최대 60fps까지 높일 수 있습니다. 

FPS를 계산하는 공식은 다음과 같습니다:
<p align="center"><strong>{fps} = {pixel_rate}/{hts}x{vts}</strong></p>
따라서 FPS를 높이려면 pixel_rate, hts, vts 값을 조정해야 합니다.  
현재 드라이버 구현에서는 pixel_rate와 hts가 모두 고정되어 있습니다. FPS를 높이려면 hts를 그대로 유지한 채 pixel_rate를 높이고, 이에 맞춰 vts를 조정하여 원하는 프레임 레이트를 얻는 방법이 유일합니다.

FPS를 60으로 변경하려면 드라이버와 디바이스 트리를 모두 수정해야 합니다.
FPS를 60으로 변경하려면 아래 가이드를 따르십시오.

##### 4.1.2.4.1 1920x1080 @ 60fps
60 fps를 달성하려면 다음 관계가 성립해야 합니다:  
fps = pixel_rate / (hts × vts)
- pixel_rate = 182,400,000
- hts = 3448
- target fps = 60

필요한 VTS는 다음과 같습니다:
- vts = pixel_rate / (hts × fps) = 182,400,000 / (3448 × 60) ≈ 882

다만 VTS 값은 1080보다 커야 하므로 이 구성은 유효하지 않습니다.  
따라서 60 fps에 도달하려면 hts는 고정한 상태에서 pixel_rate, vts 및 PLL_VT 레지스터를 조정해야 합니다.

필요한 변경 사항은 다음과 같습니다:
1. imx219.c 드라이버 파일  
    A. 픽셀 레이트와 링크 주파수를 높입니다
    ```
    #define IMX219_PIXEL_RATE            182400000    →   #define IMX219_PIXEL_RATE            278400000
    #define IMX219_DEFAULT_LINK_FREQ     456000000   →   #define IMX219_DEFAULT_LINK_FREQ     696000000
    ``` 
    B. 1080p 모드의 VTS 값을 업데이트합니다:
    ```
    #define IMX219_VTS_30FPS_1080P       0x06e3       →   #define IMX219_VTS_30FPS_1080P       0x0542
    ```
    C. 1920x1080 모드 테이블에서 PLL_VT 레지스터를 수정합니다:
    ```
    // imx219_reg mode_1920_1080_regs[]
    {0x0307, 0x39}   →   {0x0307, 0x57}
    ```
2. tcc805x-videoinput-mipi0-imx219.dtsi 디바이스 트리 파일  
    A. 새로운 픽셀 레이트에 맞게 링크 주파수를 업데이트합니다:
    ```
    // &i2c7
    /bits/ 64 <456000000> → /bits/ 64 <696000000>
    ```
    B. hs-settle 값을 업데이트합니다:
    ```
    hs-settle = <13> → hs-settle = <35>
    ```
3. 커널을 다시 빌드하고 FAI 이미지를 생성합니다.  
    빌드 디렉터리로 돌아가 아래 명령어로 커널을 다시 빌드합니다.
    ```
    $ cd ${build_dir}/build/d3-g-topst-main/
    $ bitbake -C compile linux-topst
    $ cd ${build_dir}
    $ ./stitch-fai-d3.sh
    ```
D3-G에서 아래 명령어를 사용하면 FPS 출력이 59.9로 표시되며, 이는 60 fps에 해당함을 확인할 수 있습니다.
```
$ v4l2-ctl --stream-mmap=3 --stream-count=300 --stream-to=/dev/null --verbose
```
D3-G에서 카메라 재생을 위한 GStreamer 명령어는 아래와 같습니다.
```
$ gst-launch-1.0 v4l2src device=/dev/video0 io-mode=2 ! video/x-raw,format=NV12,width=1920,height=1080,framerate=60/1 ! videoconvert ! waylandsink sync=false
```

##### 4.1.2.4.2 1640x1232 @ 60fps
60 fps를 달성하려면 다음 관계가 성립해야 합니다:  
fps = pixel_rate / (hts × vts)
- pixel_rate = 182,400,000
- hts = 3448
- target fps = 60

필요한 VTS는 다음과 같습니다:
- vts = pixel_rate / (hts × fps) = 182,400,000 / (3448 × 60) ≈ 882

다만 VTS 값은 1080보다 커야 하므로 이 구성은 유효하지 않습니다.  
따라서 60 fps에 도달하려면 hts는 고정한 상태에서 pixel_rate, vts 및 PLL_VT 레지스터를 조정해야 합니다.

필요한 변경 사항은 다음과 같습니다:
1. imx219.c 드라이버 파일  
    A. 픽셀 레이트와 링크 주파수를 높입니다
    ```
    #define IMX219_PIXEL_RATE            182400000    →   #define IMX219_PIXEL_RATE            278400000
    #define IMX219_DEFAULT_LINK_FREQ     456000000   →   #define IMX219_DEFAULT_LINK_FREQ     696000000
    ``` 
    B. 1640_1232 모드의 VTS 값을 업데이트합니다:
    ```
    #define IMX219_VTS_30FPS_BINNED       0x06e3       →   #define IMX219_VTS_30FPS_BINNED       0x0542
    ```
    C. 1920x1080 모드 테이블에서 PLL_VT 레지스터를 수정합니다:
    ```
    // imx219_reg mode_1640_1232_regs[]
    {0x0307, 0x39}   →   {0x0307, 0x57}
    ```
2. tcc805x-videoinput-mipi0-imx219.dtsi 디바이스 트리 파일  
    A. 새로운 픽셀 레이트에 맞게 링크 주파수를 업데이트합니다:
    ```
    // &i2c7
    /bits/ 64 <456000000> → /bits/ 64 <696000000>
    ```
    B. hs-settle 값을 업데이트합니다:
    ```
    hs-settle = <13> → hs-settle = <34>
    ```
3. 커널을 다시 빌드하고 FAI 이미지를 생성합니다.  
    빌드 디렉터리로 돌아가 아래 명령어로 커널을 다시 빌드합니다.
    ```
    $ cd ${build_dir}/build/d3-g-topst-main/
    $ bitbake -C compile linux-topst
    $ cd ${build_dir}
    $ ./stitch-fai-d3.sh
    ```
D3-G에서 아래 명령어를 사용하면 FPS 출력이 59.9로 표시되며, 이는 60 fps에 해당함을 확인할 수 있습니다.
```
$ v4l2-ctl --stream-mmap=3 --stream-count=300 --stream-to=/dev/null --verbose
```
D3-G에서 카메라 재생을 위한 GStreamer 명령어는 아래와 같습니다.
```
$ gst-launch-1.0 v4l2src device=/dev/video0 io-mode=2 ! video/x-raw,format=NV12,width=1640,height=1232,framerate=60/1 ! videoconvert ! waylandsink sync=false
```

##### 4.1.2.4.3 640x480 @ 60fps
60 fps를 달성하려면 다음 관계가 성립해야 합니다:  
fps = pixel_rate / (hts × vts)
- pixel_rate = 182,400,000
- hts = 3448
- target fps = 60

필요한 VTS는 다음과 같습니다:
- vts = pixel_rate / (hts × fps) = 182,400,000 / (3448 × 60) ≈ 882

VTS 값이 480보다 크므로 조건을 만족합니다. 앞의 예제와 마찬가지로 HTS는 고정한 상태에서 pixelrate와 VTS를 조정하여 FPS를 변경합니다.  
pixelrate를 변경하지 않고 VTS 값만 수정하여 FPS를 조정할 수도 있습니다. 다만 IMX219의 0x0307 레지스터 값은 변경하지 않아야 합니다.

필요한 변경 사항은 다음과 같습니다:
1. imx219.c 드라이버 파일  
    A. 픽셀 레이트와 링크 주파수를 높입니다
    ```
    #define IMX219_PIXEL_RATE            182400000    →   #define IMX219_PIXEL_RATE            278400000
    #define IMX219_DEFAULT_LINK_FREQ     456000000   →   #define IMX219_DEFAULT_LINK_FREQ     696000000
    ``` 
    B. 640_480 모드의 VTS 값을 업데이트합니다:
    ```
    #define IMX219_VTS_30FPS_640x480       0x06e3       →   #define IMX219_VTS_30FPS_640x480       0x0542
    ```
    C. 640x480 모드 테이블에서 PLL_VT 레지스터를 수정합니다:
    ```
    // imx219_reg mode_640_480_regs[]
    {0x0307, 0x39}   →   {0x0307, 0x57}
    ```
2. tcc805x-videoinput-mipi0-imx219.dtsi 디바이스 트리 파일  
    A. 새로운 픽셀 레이트에 맞게 링크 주파수를 업데이트합니다:
    ```
    // &i2c7
    /bits/ 64 <456000000> → /bits/ 64 <696000000>
    ```
    B. hs-settle 값을 업데이트합니다:
    ```
    hs-settle = <13> → hs-settle = <26>
    ```
3. 커널을 다시 빌드하고 FAI 이미지를 생성합니다.  
    빌드 디렉터리로 돌아가 아래 명령어로 커널을 다시 빌드합니다.
    ```
    $ cd ${build_dir}/build/d3-g-topst-main/
    $ bitbake -C compile linux-topst
    $ cd ${build_dir}
    $ ./stitch-fai-d3.sh
    ```
D3-G에서 아래 명령어를 사용하면 FPS 출력이 59.9로 표시되며, 이는 60 fps에 해당함을 확인할 수 있습니다.
```
$ v4l2-ctl --stream-mmap=3 --stream-count=300 --stream-to=/dev/null --verbose
```
D3-G에서 카메라 재생을 위한 GStreamer 명령어는 아래와 같습니다.
```
$ gst-launch-1.0 v4l2src device=/dev/video0 io-mode=2 ! video/x-raw,format=NV12,width=640,height=480,framerate=60/1 ! videoconvert ! waylandsink sync=false
```

### 4.1.3 AI-G OV5647 센서 사용자 가이드
#### 4.1.3.1 OV5647 센서 개요
##### 4.1.3.1.1 소개
OV5647은 소형 크기, 안정적인 성능, 표준 MIPI CSI-2 인터페이스와의 호환성 덕분에 임베디드 카메라 애플리케이션에서 널리 사용되는 500만 화소 CMOS 이미지 센서입니다. 또한 Raspberry Pi Camera Module v1에 사용된 이미지 센서이며, 다양한 Arducam OV5647 카메라 모듈을 통해 사용할 수 있습니다. 이들 모두 TOPST AI-G 플랫폼과 호환됩니다.  
사용자는 카메라 동작을 위해 Raspberry Pi Camera v1 또는 Arducam OV5647 모듈을 MIPI CSI 포트에 연결할 수 있습니다.

TOPST AI-G 플랫폼에서 OV5647은 15핀 또는 20핀 MIPI CSI 커넥터를 통해 연결되며 V4L2 프레임워크로 제어되어 Yocto와 Ubuntu 환경 모두에서 일관된 동작을 제공합니다.

##### 4.1.3.1.2 지원 해상도 및 FPS
OV5647 카메라 모듈(Raspberry Pi v1 또는 Arducam OV5647)의 사양은 다음과 같습니다:
<p align="center"><strong>표 4.7 OV5647 카메라 모듈 사양</strong></p>
<div align="center">
    <table>
        <tr>
            <td colspan="2" align="center"><strong>사양</strong></td>
            <td align="center"><strong>설명</strong></td>
        </tr>
        <tr>
            <td colspan="2">센서</td>
            <td>OmniVision OV5647</td>
        </tr>
        <tr>
            <td colspan="2">해상도</td>
            <td>2592 x 1944 (5MP)</td>
        </tr>
        <tr>
            <td colspan="2">출력 포맷</td>
            <td>RAW, YUV, JPEG</td>
        </tr>
        <tr>
            <td colspan="2">인터페이스</td>
            <td>MIPI CSI-2</td>
        </tr>
        <tr>
            <td colspan="2">프레임 레이트</td>
            <td>1080p30, 720p60, 480p90</td>
        </tr>
        <tr>
            <td colspan="2">렌즈</td>
            <td>고정 초점</td>
        </tr>
        <tr>
            <td colspan="2">화각(FOV)</td>
            <td>Up to 54°</td>
        </tr>
        <tr>
            <td colspan="2">케이블 종류</td>
            <td>FFC(15핀)</td>
        </tr>
        <tr>
            <td colspan="2">보드 크기</td>
            <td>25mm x 24mm</td>
        </tr>
        <tr>
            <td colspan="2">호환성</td>
            <td>D3-G 및 Rasbperry Pi(MIPI CSI-2 포트를 통해)</td>
        </tr>
    </table>
</div>

AI-G에서 지원하는 센서 해상도 및 FPS는 다음과 같습니다:  
<p align="center"><strong>표 4.8 AI-G의 OV5647 센서 해상도</strong></p>
<div align="center">
    <table>
        <tr>
            <td colspan="3" align="center"><strong>해상도</strong></td>
            <td align="center"><strong>FPS</strong></td>
            <td align="center"><strong>설명</strong></td>
        </tr>
        <tr>
            <td colspan="3">1920x1080</td>
            <td>30</td>
            <td>전체 해상도 프레임의 중앙 영역을 크롭하여 1080p 이미지를 출력합니다</td>
        </tr>
        <tr>
            <td colspan="3">1296x972</td>
            <td>30</td>
            <td>2×2 픽셀 비닝을 사용하여 감도를 높이고 노이즈를 줄입니다</td>
        </tr>
        <tr>
            <td colspan="3">640x480</td>
            <td>60</td>
            <td>2×2 비닝과 <strong>서브샘플링</strong>을 결합합니다. 서브샘플링은 리드아웃 중 픽셀을 건너뛰어 데이터 처리량을 줄이고 더 높은 프레임 레이트를 구현합니다</td>
        </tr>
    </table>
</div>

**참고:** 표 4.8에 나와 있듯이, 추론 성능이 크게 저하되므로 **전체 2592×1944 해상도는 사용하지 않습니다**.

<p align="center"><strong>표 4.9 동작 모드별 최대 해상도</strong></p>
<div align="center">
    <table>
        <tr>
            <td colspan="4" align="center"><strong>사용 CH.</strong></td>
            <td align="center"><strong>동작 모드</strong></td>
            <td align="center"><strong>최대 해상도</strong></td>
            <td align="center"><strong>입력 포맷</strong></td>
        </tr>
        <tr>
            <td colspan="4">4CH</td>
            <td>기본 모드</td>
            <td>1280 x 720 @ 60fps</td>
            <td>RAW 24</td>
        </tr>
        <tr>
            <td colspan="4" rowspan="2">2CH</td>
            <td rowspan="2">메모리 공유 모드</td>
            <td>옵션 1: 2048 x 1280 @ 60fps</td>
            <td>RAW 20</td>
        </tr>
        <tr>
            <td>옵션 2: 2592 x 2048 @ 30fps + 2048 x 1280 @ 30fps</td>
            <td>RAW 24</td>
        </tr>
        <tr>
            <td colspan="4">1CH</td>
            <td>메모리 공유 모드</td>
            <td>2592 x 2048 @ 60fps</td>
            <td>RAW 20</td>
        </tr>
    </table>
</div>

#### 4.1.3.2 Yocto에서의 OV5647 해상도 구성: 드라이버
Yocto 빌드 과정에서 OV5647 센서의 해상도를 변경하려면 아래 지침을 따르십시오.

먼저 OV5647을 활성화하려면 다음 위치에 TOPST_CAM_MODULE = "ov5647"이 설정되어 있는지 확인하십시오.  
{build_dir}/build/ai-g-topst-main/conf/local.conf.  
이 항목은 첫 빌드를 위해 저장소를 초기화할 때 기본적으로 활성화되지만, 다시 한 번 확인하십시오.

또한 빌드 과정에서 소스 코드가 삭제되지 않도록 다음 위치에서 아래 줄을 활성화하십시오.  
{build_dir}/build/ai-g-topst-main/conf/local.conf:
```
INHERIT:remove = “rm_work”
```

위 옵션을 활성화한 후 다음 명령으로 이미지를 다시 빌드하십시오.
```
$ bitbake telechips-topst-image
```

두 번째로, 빌드가 완료되면 ov5647.c 드라이버 파일을 열고 필요한 수정을 적용하십시오.

다음 디렉터리로 이동하십시오.
```
${build_dir}/build/ai-g-topst-main/tmp/work/ai_g_topst-telechips-linux/linux-topst/5.10.223-r0/git/drivers/media/i2c/telechips/
```

코드를 수정하기 전에, 현재 드라이버가 다음 세 가지 모드를 지원한다는 점에 유의하십시오.
- 1920×1080 @ 30fps
- 1296×972 @ 30fps
- 640×480 @ 60fps

각 해상도는 순서대로 Mode 1, Mode 2, Mode 3에 해당합니다.

1920×1080 @ 30fps 모드는 센터 크롭을 사용하므로 화각이 좁아지고, 640×480 모드는 해상도가 충분하지 않습니다. 반면 1296×972 모드는 2×2 비닝을 사용하여 더 넓은 화각을 제공하므로 현재 기본 모드로 사용됩니다.  
ov5647.c 드라이버 파일을 열고 아래와 같이 OV5647 기본 모드를 수정하십시오.
```
#define OV5647_DEFAULT_MODE (&supported_modes_10bit[2])
```
1920×1080 @ 30fps는 Mode 1에 해당하므로 **“#define OV5647_DEFAULT_MODE (&supported_modes_10bit[1])”**를 그대로 사용할 수 있습니다.  
1296×972 @ 30fps 모드는 Mode 2에 해당하므로, **“#define OV5647_DEFAULT_MODE (&supported_modes_10bit[2])”**는 이미 올바르게 설정되어 있습니다.  
Mode 3에 해당하는 640×480 @ 60fps의 경우, 정의를 **“#define OV5647_DEFAULT_MODE (&supported_modes_10bit[3])”**로 변경합니다.

세 번째로, 커널을 다시 빌드하고 FAI 이미지를 생성합니다.  
빌드 디렉터리로 돌아가 아래 명령어를 사용하여 커널을 다시 빌드합니다.
```
$ cd ${build_dir}/build/ai-g-topst-main/
$ bitbake -C compile linux-topst
$ cd ${build_dir}
$ ./stitch-fai-ai.sh
```

그런 다음 생성된 output_aig.fai를 FWDN으로 보드에 플래싱하면 원하는 해상도로 OV5647 센서를 사용할 수 있습니다.

### 4.1.4 AI-G IMX219 센서 설정 가이드
#### 4.1.4.1 IMX219 센서 개요
##### 4.1.4.1.1 소개
IMX219는 Sony의 고성능 8메가픽셀 CMOS 이미지 센서로, 소형 카메라 모듈에서 뛰어난 화질과 낮은 소비 전력, 안정적인 촬영 성능을 제공하는 것으로 잘 알려져 있습니다. 또한 Raspberry Pi Camera Module v2에 사용된 센서이며, 임베디드 비전 시스템, 로보틱스, AI 기반 카메라 애플리케이션에 널리 채택되고 있습니다.

TOPST AI-G 플랫폼에서 IMX219 센서는 15핀 또는 20핀 MIPI CSI 커넥터를 통해 연결할 수 있으며 V4L2 프레임워크로 제어됩니다. 이를 통해 Yocto와 Ubuntu 환경 모두에서 일관된 인터페이스와 안정적인 카메라 동작을 제공합니다.

높은 해상도(8MP)와 저노이즈 이미징 특성을 갖춘 IMX219는 TOPST AI-G 플랫폼에서 고품질 영상 촬영 및 이미지 처리 기능을 구현하는 데 적합합니다.

##### 4.1.4.1.2 지원 해상도 및 FPS
IMX219 카메라 모듈(Raspberry Pi v2)의 사양은 다음과 같습니다.
<p align="center"><strong>표 4.10 IMX219 카메라 모듈 사양</strong></p>
<div align="center">
    <table>
        <tr>
            <td colspan="2" align="center"><strong>사양</strong></td>
            <td align="center"><strong>설명</strong></td>
        </tr>
        <tr>
            <td colspan="2">센서</td>
            <td>Sony Imx219</td>
        </tr>
        <tr>
            <td colspan="2">해상도</td>
            <td>3280 x 2464 (8 MP)</td>
        </tr>
        <tr>
            <td colspan="2">출력 포맷</td>
            <td>RAW, YUV, JPEG</td>
        </tr>
        <tr>
            <td colspan="2">인터페이스</td>
            <td>MIPI CSI-2</td>
        </tr>
        <tr>
            <td colspan="2">프레임 레이트</td>
            <td>1080p60, 720p180, 480p206</td>
        </tr>
        <tr>
            <td colspan="2">렌즈</td>
            <td>초점 조절 가능</td>
        </tr>
        <tr>
            <td colspan="2">화각(FOV)</td>
            <td>Up to 62°</td>
        </tr>
        <tr>
            <td colspan="2">케이블 종류</td>
            <td>FFC(15핀)</td>
        </tr>
        <tr>
            <td colspan="2">보드 크기</td>
            <td>25mm x 24mm</td>
        </tr>
        <tr>
            <td colspan="2">호환성</td>
            <td>D3-G 및 Rasbperry Pi(MIPI CSI-2 포트를 통해)</td>
        </tr>
    </table>
</div>

AI-G에서 지원하는 센서 해상도 및 FPS는 다음과 같습니다:
<p align="center"><strong>표 4.11 AI-G의 IMX219 센서 해상도</strong></p>
<div align="center">
    <table>
        <tr>
            <td colspan="3" align="center"><strong>해상도</strong></td>
            <td align="center"><strong>FPS</strong></td>
            <td align="center"><strong>설명</strong></td>
        </tr>
        <tr>
            <td colspan="3">1920x1080</td>
            <td>30</td>
            <td>전체 해상도 프레임의 중앙 영역을 크롭하여 1080p 이미지를 출력합니다</td>
        </tr>
        <tr>
            <td colspan="3">1640x1232</td>
            <td>30</td>
            <td>2×2 픽셀 비닝을 사용하여 감도를 높이고 노이즈를 줄입니다</td>
        </tr>
        <tr>
            <td colspan="3">640x480</td>
            <td>30</td>
            <td>2×2 비닝과 <strong>서브샘플링</strong>을 결합하여 리드아웃 시 픽셀을 건너뛰어 데이터 처리량을 줄입니다</td>
        </tr>
    </table>
</div>

**참고:** 표 4.11에 나와 있듯이, 추론 성능이 크게 저하되므로 전체 3820×2464 해상도는 사용하지 않습니다.

<p align="center"><strong>표 4.12 동작 모드별 최대 해상도</strong></p>
<div align="center">
    <table>
        <tr>
            <td colspan="4" align="center"><strong>사용 CH.</strong></td>
            <td align="center"><strong>동작 모드</strong></td>
            <td align="center"><strong>최대 해상도</strong></td>
            <td align="center"><strong>입력 포맷</strong></td>
        </tr>
        <tr>
            <td colspan="4">4CH</td>
            <td>기본 모드</td>
            <td>1280 x 720 @ 60fps</td>
            <td>RAW 24</td>
        </tr>
        <tr>
            <td colspan="4" rowspan="2">2CH</td>
            <td rowspan="2">메모리 공유 모드</td>
            <td>옵션 1: 2048 x 1280 @ 60fps</td>
            <td>RAW 20</td>
        </tr>
        <tr>
            <td>옵션 2: 2592 x 2048 @ 30fps + 2048 x 1280 @ 30fps</td>
            <td>RAW 24</td>
        </tr>
        <tr>
            <td colspan="4">1CH</td>
            <td>메모리 공유 모드</td>
            <td>2592 x 2048 @ 60fps</td>
            <td>RAW 20</td>
        </tr>
    </table>
</div>

#### 4.1.4.2 Yocto에서 IMX219 활성화
AI-G SDK는 기본적으로 OV5647이 활성화되도록 구성되어 있으므로, 빌드하기 전에 IMX219를 활성화해야 합니다.  
SDK가 이미 빌드된 경우와 처음 빌드하는 경우의 두 가지 경우를 고려해야 합니다.

##### 4.1.4.2.1 첫 빌드 전에 IMX219 활성화하기
최초 빌드의 경우 아래 단계에 따라 IMX219를 활성화한 후 빌드를 진행하십시오.
1. 환경 설정 스크립트를 source하고 옵션 1을 선택합니다
    ```
    $ source poky/meta-topst/topst-build.sh
    ```
2. 아래 경로에 있는 local.conf 파일을 엽니다
    ```
    ${build_dir}/build/ai-g-topst-main/conf/local.conf
    ```
3. ov5647에 대한 TOPST_CAM_MODULE 항목을 주석 처리하고 imx219 항목을 활성화합니다
    ```
    #TOPST_CAM_MODULE = "ov5647"
    TOPST_CAM_MODULE = "imx219"
    ```
4. 빌드를 실행합니다
    ```
    $ bitbake telechips-topst-ai-image
    ```

##### 4.1.4.2.2 빌드가 이미 완료된 후에 IMX219 활성화하기
기존 빌드는 기본적으로 OV5647 센서가 활성화되도록 구성되어 있습니다. 아래 단계에 따라 IMX219를 활성화하십시오.
1. 아래 경로에 있는 local.conf 파일을 엽니다
    ```
    ${build_dir}/build/ai-g-topst-main/conf/local.conf
    ```
2. ov5647에 대한 TOPST_CAM_MODULE 항목을 주석 처리하고 imx219 항목을 활성화합니다
    ```
    #TOPST_CAM_MODULE = "ov5647"
    TOPST_CAM_MODULE = "imx219"
    ```
3. isp-server와 isp-firmware에 대해 cleansstate를 실행합니다
    ```
    $ bitbake -c cleansstate isp-firmware
    $ bitbake -c cleansstate isp-server
    ```
4. 빌드를 실행합니다
    ```
    $ bitbake telechips-topst-ai-image
    ```

#### 4.1.4.3 Yocto에서의 IMX219 해상도 구성: 드라이버
Yocto 빌드 과정에서 IMX219 센서의 해상도를 변경하려면 아래 지침을 따르십시오.

먼저 imx219를 활성화하려면 TOPST_CAM_MODULE = "imx219"가 설정되어 있는지 확인합니다
{build_dir}/build/ai-g-topst-main/conf/local.conf.

또한 빌드 과정에서 소스 코드가 제거되지 않도록 다음 줄을 활성화합니다
{build_dir}/build/ai-g-topst-main/conf/local.conf:
```
INHERIT:remove = “rm_work”
```

위 옵션을 활성화한 후 다음 명령으로 이미지를 다시 빌드하십시오.
```
$ bitbake telechips-topst-ai-image
```
두 번째로, 빌드가 완료된 후 imx219.c 드라이버 파일을 열고 필요한 수정 사항을 적용합니다.

다음 디렉터리로 이동하십시오.
```
${build_dir}/build/ai-g-topst-main /ai-g-topst/tmp/work/ai_g_topst-telechips-linux/linux-topst/5.10.223-r0/git/drivers/media/i2c/telechips/
```
코드를 수정하기 전에, 현재 드라이버가 다음 세 가지 모드를 지원한다는 점에 유의하십시오.
- 1920×1080 @ 30fps
- 1640×1232 @ 30fps
- 640×480 @ 30fps
각 해상도는 순서대로 Mode 1, Mode 2, Mode 3에 해당합니다.

1920×1080 @ 30fps 모드는 센터 크롭을 사용하므로 화각이 좁아지고, 640×480 모드는 해상도가 충분하지 않습니다. 반면 1640×1232 모드는 2×2 비닝을 사용하여 더 넓은 화각을 제공하므로, 현재 기본 모드로 사용되고 있습니다.  
imx219.c 드라이버 파일을 열고, imx219_set_default_format, imx219_open, imx219_probe 함수 내부에서 아래에 설명된 부분을 수정합니다.
- imx219_set_default_format
    ```
    fmt->width = supported_modes[2].width;
    fmt->height = supported_modes[2].height;
    ```
- imx219_open
    ```
    try_fmt_img->width = supported_modes[2].width;
    try_fmt_img->height = supported_modes[2].height;
    ```
- imx219_probe
    ```
    imx219->mode = &supported_modes[2];
    ```

1920×1080 @ 30fps는 Mode 1에 해당하므로, 세 함수 내부의 모든 supported_modes 참조를 **“supported_modes[1]”**로 변경하십시오.  
1640×1232 @ 30fps 모드는 Mode 2에 해당하므로, 이에 맞추어 **“supported_modes[2]”**로 변경하십시오.  
Mode 3에 해당하는 640×480 @ 30fps의 경우 모든 참조를 **“supported_modes [3]”**으로 변경합니다.

세 번째로, 커널을 다시 빌드하고 FAI 이미지를 생성합니다.  
빌드 디렉터리로 돌아가 아래 명령어를 사용하여 커널을 다시 빌드합니다.
```
$ cd ${build_dir}/build/ai-g-topst-main/
$ bitbake -C compile linux-topst
$ cd ${build_dir}
$ ./stitch-fai-ai.sh
```

그런 다음 생성된 output_aig.fai를 FWDN으로 보드에 플래싱하면 원하는 해상도로 IMX219 센서를 사용할 수 있습니다.

#### 4.1.4.4 Yocto에서 IMX219의 FPS를 높이는 방법: 드라이버 및 디바이스 트리
IMX219 센서 설명에 따르면 이 센서는 1080p60, 720p180, VGA206과 같은 고프레임레이트 모드를 지원합니다. 따라서 imx219.c 드라이버가 지원하는 해상도인 1920×1080, 1640×1232, 640×480에서 FPS를 높일 수 있습니다. AI-G 플랫폼의 ISP 코어는 최대 60fps를 지원하므로 이러한 해상도는 각각 최대 60fps까지 높일 수 있습니다.  

FPS를 계산하는 공식은 다음과 같습니다:
<p align="center"><strong>{fps} = {pixel_rate}/{hts}x{vts}</strong></p>
따라서 FPS를 높이려면 pixel_rate, hts, vts 값을 조정해야 합니다.  
현재 드라이버 구현에서는 pixel_rate와 hts가 모두 고정되어 있습니다. FPS를 높이려면 hts를 그대로 유지한 채 pixel_rate를 높이고, 이에 맞춰 vts를 조정하여 원하는 프레임 레이트를 얻는 방법이 유일합니다.

FPS를 60으로 변경하려면 드라이버와 디바이스 트리를 모두 수정해야 합니다.
FPS를 60으로 변경하려면 아래 가이드를 따르십시오.

##### 4.1.2.4.1 1920x1080 @ 60fps
60 fps를 달성하려면 다음 관계가 성립해야 합니다:  
fps = pixel_rate / (hts × vts)
- pixel_rate = 182,400,000
- hts = 3448
- target fps = 60

필요한 VTS는 다음과 같습니다:
- vts = pixel_rate / (hts × fps) = 182,400,000 / (3448 × 60) ≈ 882

다만 VTS 값은 1080보다 커야 하므로 이 구성은 유효하지 않습니다.  
따라서 60 fps에 도달하려면 hts는 고정한 상태에서 pixel_rate, vts 및 PLL_VT 레지스터를 조정해야 합니다.

필요한 변경 사항은 다음과 같습니다:
1. imx219.c 드라이버 파일  
    A. 픽셀 레이트와 링크 주파수를 높입니다
    ```
    #define IMX219_PIXEL_RATE            182400000    →   #define IMX219_PIXEL_RATE            278400000
    #define IMX219_DEFAULT_LINK_FREQ     456000000   →   #define IMX219_DEFAULT_LINK_FREQ     696000000
    ``` 
    B. 1080p 모드의 VTS 값을 업데이트합니다:
    ```
    #define IMX219_VTS_30FPS_1080P       0x06e3       →   #define IMX219_VTS_30FPS_1080P       0x0542
    ```
    C. 1920x1080 모드 테이블에서 PLL_VT 레지스터를 수정합니다:
    ```
    // imx219_reg mode_1920_1080_regs[]
    {0x0307, 0x39}   →   {0x0307, 0x57}
    ```
2. tcc805x-videoinput-mipi0-imx219.dtsi 디바이스 트리 파일  
    A. 새로운 픽셀 레이트에 맞게 링크 주파수를 업데이트합니다:
    ```
    // &i2c7
    /bits/ 64 <456000000> → /bits/ 64 <696000000>
    ```
    B. hs-settle 값을 업데이트합니다:
    ```
    hs-settle = <13> → hs-settle = <35>
    ```
3. 커널을 다시 빌드하고 FAI 이미지를 생성합니다.  
    빌드 디렉터리로 돌아가 아래 명령어로 커널을 다시 빌드합니다.
    ```
    $ cd ${build_dir}/build/d3-g-topst-main/
    $ bitbake -C compile linux-topst
    $ cd ${build_dir}
    $ ./stitch-fai-d3.sh
    ```
AI-G에서 아래 명령어를 사용하면 FPS 출력이 59.9로 표시되며, 이는 60 fps에 해당함을 확인할 수 있습니다.
```
$ v4l2-ctl --stream-mmap=3 --stream-count=300 --stream-to=/dev/null --verbose
```

##### 4.1.2.4.2 1640x1232 @ 60fps
60 fps를 달성하려면 다음 관계가 성립해야 합니다:  
fps = pixel_rate / (hts × vts)
- pixel_rate = 182,400,000
- hts = 3448
- target fps = 60

필요한 VTS는 다음과 같습니다:
- vts = pixel_rate / (hts × fps) = 182,400,000 / (3448 × 60) ≈ 882

다만 VTS 값은 1080보다 커야 하므로 이 구성은 유효하지 않습니다.  
따라서 60 fps에 도달하려면 hts는 고정한 상태에서 pixel_rate, vts 및 PLL_VT 레지스터를 조정해야 합니다.

필요한 변경 사항은 다음과 같습니다:
1. imx219.c 드라이버 파일  
    A. 픽셀 레이트와 링크 주파수를 높입니다
    ```
    #define IMX219_PIXEL_RATE            182400000    →   #define IMX219_PIXEL_RATE            278400000
    #define IMX219_DEFAULT_LINK_FREQ     456000000   →   #define IMX219_DEFAULT_LINK_FREQ     696000000
    ``` 
    B. 1640_1232 모드의 VTS 값을 업데이트합니다:
    ```
    #define IMX219_VTS_30FPS_BINNED       0x06e3       →   #define IMX219_VTS_30FPS_BINNED       0x0542
    ```
    C. 1920x1080 모드 테이블에서 PLL_VT 레지스터를 수정합니다:
    ```
    // imx219_reg mode_1640_1232_regs[]
    {0x0307, 0x39}   →   {0x0307, 0x57}
    ```
2. tcc805x-videoinput-mipi0-imx219.dtsi 디바이스 트리 파일  
    A. 새로운 픽셀 레이트에 맞게 링크 주파수를 업데이트합니다:
    ```
    // &i2c7
    /bits/ 64 <456000000> → /bits/ 64 <696000000>
    ```
    B. hs-settle 값을 업데이트합니다:
    ```
    hs-settle = <13> → hs-settle = <34>
    ```
3. 커널을 다시 빌드하고 FAI 이미지를 생성합니다.  
    빌드 디렉터리로 돌아가 아래 명령어로 커널을 다시 빌드합니다.
    ```
    $ cd ${build_dir}/build/d3-g-topst-main/
    $ bitbake -C compile linux-topst
    $ cd ${build_dir}
    $ ./stitch-fai-d3.sh
    ```
AI-G에서 아래 명령어를 사용하면 FPS 출력이 59.9로 표시되며, 이는 60 fps에 해당함을 확인할 수 있습니다.
```
$ v4l2-ctl --stream-mmap=3 --stream-count=300 --stream-to=/dev/null --verbose
```

##### 4.1.2.4.3 640x480 @ 60fps
60 fps를 달성하려면 다음 관계가 성립해야 합니다:  
fps = pixel_rate / (hts × vts)
- pixel_rate = 182,400,000
- hts = 3448
- target fps = 60

필요한 VTS는 다음과 같습니다:
- vts = pixel_rate / (hts × fps) = 182,400,000 / (3448 × 60) ≈ 882

VTS 값이 480보다 크므로 조건을 만족합니다. 앞의 예제와 마찬가지로 HTS는 고정한 상태에서 pixelrate와 VTS를 조정하여 FPS를 변경합니다.  
pixelrate를 변경하지 않고 VTS 값만 수정하여 FPS를 조정할 수도 있습니다. 다만 IMX219의 0x0307 레지스터 값은 변경하지 않아야 합니다.

필요한 변경 사항은 다음과 같습니다:
1. imx219.c 드라이버 파일  
    A. 픽셀 레이트와 링크 주파수를 높입니다
    ```
    #define IMX219_PIXEL_RATE            182400000    →   #define IMX219_PIXEL_RATE            278400000
    #define IMX219_DEFAULT_LINK_FREQ     456000000   →   #define IMX219_DEFAULT_LINK_FREQ     696000000
    ``` 
    B. 640_480 모드의 VTS 값을 업데이트합니다:
    ```
    #define IMX219_VTS_30FPS_640x480       0x06e3       →   #define IMX219_VTS_30FPS_640x480       0x0542
    ```
    C. 640x480 모드 테이블에서 PLL_VT 레지스터를 수정합니다:
    ```
    // imx219_reg mode_640_480_regs[]
    {0x0307, 0x39}   →   {0x0307, 0x57}
    ```
2. tcc805x-videoinput-mipi0-imx219.dtsi 디바이스 트리 파일  
    A. 새로운 픽셀 레이트에 맞게 링크 주파수를 업데이트합니다:
    ```
    // &i2c7
    /bits/ 64 <456000000> → /bits/ 64 <696000000>
    ```
    B. hs-settle 값을 업데이트합니다:
    ```
    hs-settle = <13> → hs-settle = <26>
    ```
3. 커널을 다시 빌드하고 FAI 이미지를 생성합니다.  
    빌드 디렉터리로 돌아가 아래 명령어로 커널을 다시 빌드합니다.
    ```
    $ cd ${build_dir}/build/d3-g-topst-main/
    $ bitbake -C compile linux-topst
    $ cd ${build_dir}
    $ ./stitch-fai-d3.sh
    ```
AI-G에서 아래 명령어를 사용하면 FPS 출력이 59.9로 표시되며, 이는 60 fps에 해당함을 확인할 수 있습니다.
```
$ v4l2-ctl --stream-mmap=3 --stream-count=300 --stream-to=/dev/null --verbose
```

## 4.2 GMSL 카메라 설정 가이드
### 4.2.1 D3-G GMSL 카메라 설정 가이드
Deserializer 보드를 사용하면 하나의 MIPI CSI 포트에 최대 4개의 카메라를 연결할 수 있습니다. D3-G는 2개의 MIPI CSI 포트를 제공하므로 다음 구성 중 하나를 선택할 수 있습니다:
- MIPI0 포트에 4대의 카메라를 사용합니다
- MIPI1 포트에 4대의 카메라를 사용합니다
- MIPI0과 MIPI1을 모두 사용하여 총 8대의 카메라를 연결합니다

8대의 카메라를 모두 구성하는 경우, 최대 4개의 디스플레이를 지원하는 D3-G의 디스플레이 확장 기능을 최대 3개의 디스플레이까지 사용할 수 있습니다.

**참고:** 본 가이드에서는 IMX290 (cxd5700) FHD GMSL 카메라를 사용합니다.  
다른 GMSL 카메라를 사용하려면 추가적인 카메라 포팅이 필요합니다.

#### 4.2.1.1 MIPI0 포트 사용 방법
먼저 GMSL 카메라와 SerDes 보드에 대한 커널 설정을 모두 활성화해야 합니다.  
다음 항목을 추가합니다  
**{build_dir}/poky/meta-topst-bsp/recipes-kernel/linux/linux-topst/tcc805x/camera.cfg** file.
```
CONFIG_VIDEO_TCC_CXD5700=y
CONFIG_VIDEO_TCC_MAX9275=y
CONFIG_VIDEO_TCC_MAX96712=y
```
To prevent the source code from being removed during the build process, enable the following line, and comment out all occurrences of `TOPST_CAM_MODULE in {build_dir}/build/d3-g-topst-main/conf/local.conf:
```
#TOPST_CAM_MODULE = "ov5647"
#TOPST_CAM_MODULE = "imx219"
```
위 옵션을 수정한 후 다음 명령어로 이미지를 다시 빌드합니다.
```
$ bitbake -c cleansstate isp-firmware
$ bitbake -c cleansstate isp-server
$ bitbake telechips-topst-image
```
다음으로 커널의 디바이스 트리를 수정해야 합니다. 아래 가이드에 따라 변경 사항을 적용하고 이미지를 다시 빌드하십시오.
1. Modify file {build_dir}/build/d3-g-topst-main/tmp/work/d3_g_topst_main-telechips-linux/linux-topst/5.10.205-r0/git/arch/arm64/boot/dts/telechips/tcc805x/override/tcc8050_53-lpd4x322-sv1.0-videoinput.dtsi as shown below
    ```
    @@ -192,7 +192,7 @@ max9295_1: max9295_1@40 {
            max9286_1: max9286_1@48 {
                    status          = "disabled";
                    compatible      = "tcc-maxim,max9286";
    -               pwd-gpios       = <&gpmc 0 1>;
    +               pwd-gpios       = <&gpg 5 1>;
                    reg             = <0x48>;       // 0x90 >> 1
            };
    @@ -200,7 +200,7 @@ max9286_1: max9286_1@48 {
            max96712_1: max96712_1@2a {
                    status          = "disabled";
                    compatible      = "tcc-maxim,max96712";
    -               pwd-gpios       = <&gpmc 0 1>;
    +               pwd-gpios       = <&gpg 5 1>;
                    reg             = <0x2A>;
            };
    };
    @@ -325,7 +325,7 @@ max9295e: max9295e@42 {
            max9286: max9286@48 {
                    status          = "disabled";
                    compatible      = "tcc-maxim,max9286";
    -               pwd-gpios       = <&gpg 5 1>;
    +               pwd-gpios       = <&gpmc 0 1>;
                    reg             = <0x48>;       // 0x90 >> 1
            };
    @@ -333,7 +333,7 @@ max9286: max9286@48 {
            max96712: max96712@2a {
                    status          = "disabled";
                    compatible      = "tcc-maxim,max96712";
    -               pwd-gpios       = <&gpg 5 1>;
    +              pwd-gpios       = <&gpmc 0 1>;
                    reg             = <0x2A>;
            };
    ```
2. Modify file {build_dir}/build/d3-g-topst-main/tmp/work/d3_g_topst_main-telechips-linux/linux-topst/5.10.205-r0/git/arch/arm64/boot/dts/telechips/tcc805x/override/tcc805x-videoinput-camera-module.dtsi as shown below
    ```
    //#include "tcc805x-videoinput-mipi0-ov5647.dtsi"
    //#include "tcc805x-videoinput-mipi0-imx219.dtsi"
    +#include "tcc805x-videoinput-mipi0-fhd.dtsi"
    ```
3. Create file {build_dir}/build/d3-g-topst-main/tmp/work/d3_g_topst_main-telechips-linux/linux-topst/5.10.205-r0/git/arch/arm64/boot/dts/telechips/tcc805x/override/tcc805x-videoinput-mipi0-fhd.dtsi as shown below
    ```
    // SPDX-License-Identifier: (GPL-2.0-or-later OR MIT)
    /*
    * Copyright (C) Telechips Inc.
    */

    &i2c6 {
        status = "okay";
    };

    &cxd5700_1 {
        /* ISP of camera module */
        status          = "okay";
        port {
                cxd5700_1_out: endpoint {
                        remote-endpoint = <&max9275_1_in>;
                        io-direction    = "output";
                };
        };
    };

    &max9275_1 {
        /* serializer */
        status          = "okay";
        ports {
                #address-cells = <1>;
                #size-cells = <0>;
                port@0 {
                        reg = <0>;
                        max9275_1_in: endpoint {
                                remote-endpoint = <&cxd5700_1_out>;
                                io-direction    = "input";
                        };
                };
                port@1 {
                        reg = <1>;
                        max9275_1_out: endpoint {
                                remote-endpoint = <&max96712_1_in0>;
                                io-direction    = "output";
                        };
                };
        };
    };

    &max96712_1 {
        /* deserializer */
        status          = "okay";
        pvd-name        = "fhd";
        /*
            * broadcasting mode access each linked devices
            * by the same I2C slave address.
            *
            * Also,
            * using the serdes I2C address mapping table,
            * each liked devices can be accessed
            * by the unique I2C slave address.
            */
        broadcasting-mode;
        ports {
                #address-cells = <1>;
                #size-cells = <0>;
                /*
                    * 0 ~ 3
                    * input ports. The number is matched with VC
                    *
                    * 4
                    * output port.
                    */
                port@0 {
                        reg = <0>;
                        max96712_1_in0: endpoint {
                                remote-endpoint = <&max9275_1_out>;
                                io-direction    = "input";
                                channel         = <0>;
                        };
                };
                port@1 {
                        reg = <1>;
                        max96712_1_in1: endpoint {
                                remote-endpoint = <&max9275_1_out>;
                                io-direction    = "input";
                                channel         = <1>;
                        };
                };
                port@2 {
                        reg = <2>;
                        max96712_1_in2: endpoint {
                                remote-endpoint = <&max9275_1_out>;
                                io-direction    = "input";
                                channel         = <2>;
                        };
                };
                port@3 {
                        reg = <3>;
                        max96712_1_in3: endpoint {
                                remote-endpoint = <&max9275_1_out>;
                                io-direction    = "input";
                                channel         = <3>;
                        };
                };
                port@4 {
                        reg = <4>;
                        max96712_1_out: endpoint {
                                remote-endpoint = <&mipi_csi2_0_in>;
                                io-direction    = "output";
                                channel         = <0>;
                        };
                };
        };
    };

    &mipi_csi2_0 {
        status = "okay";
        ports {
                #address-cells = <1>;
                #size-cells = <0>;
                /*
                    * 0
                    * input port.
                    *
                    * 1 ~ 4
                    * output ports. (1: VC0 ~ 4: VC3)
                    */
                port@0 {
                        reg = <0>;
                        mipi_csi2_0_in: endpoint {
                                remote-endpoint = <&max96712_1_out>;
                                io-direction    = "input";
                                num-channel     = <4>;

                                   /*
                                    * 0: CH0 only, no data interleave
                                    * 1: DT only
                                    * 2: VC only
                                    * 3: VC and DT
                                    */
                                interleave-mode = <3>;
                                hs-settle = <37>;
                                data-lanes = <1 2 3 4>;
                        };
                };
                port@1 {
                        reg = <1>;
                        mipi_csi2_0_out0: endpoint {
                                remote-endpoint = <&videoinput4_in>;
                                io-direction    = "output";
                                channel         = <0>;
                                /*
                                    * 0: Single pixel mode
                                    * 1: Dual pixel mode (RAW8/10/12, YUV422)
                                    * 2: Quad pixel mode (RAW8/10/12)
                                    * 3: Invalid
                                    */
                                pixel-mode = <1>;
                        };
                };
                port@2 {
                        reg = <2>;
                        mipi_csi2_0_out1: endpoint {
                                remote-endpoint = <&videoinput5_in>;
                                io-direction    = "output";
                                channel         = <1>;
                                pixel-mode = <1>;
                        };
                };
                port@3 {
                        reg = <3>;
                        mipi_csi2_0_out2: endpoint {
                                remote-endpoint = <&videoinput6_in>;
                                io-direction    = "output";
                                channel         = <2>;
                                pixel-mode = <1>;
                        };
                };
                port@4 {
                        reg = <4>;
                        mipi_csi2_0_out3: endpoint {
                                remote-endpoint = <&videoinput7_in>;
                                io-direction    = "output";
                                channel         = <3>;
                                pixel-mode = <1>;
                        };
                };
        };
    };

    &videoinput4 {
        status          = "okay";
        cifport         = <&cifport             9>;
        /* memory-region
            *  - [0]: parking guideline
            *  - [1]: deinterlacing by viqe
            *  - [2]: preview
            *  - [3]: last frame
            */
        memory-region   = <0
                            0
                            &pmap_rearcamera4
                            0>;
        port {
                videoinput4_in: endpoint {
                        remote-endpoint = <&mipi_csi2_0_out0>;
                        io-direction    = "input";
                        stream-enable   = <1>;  // VIN_CTRL.SE
                        flush-vsync     = <1>;  // VIN_MISC.FVS
                };
        };
    };

    &videoinput5 {
        status          = "okay";
        cifport         = <&cifport             10>;
        /* memory-region
            *  - [0]: parking guideline
            *  - [1]: deinterlacing by viqe
            *  - [2]: preview
            *  - [3]: last frame
            */
        memory-region   = <0
                            0
                            &pmap_rearcamera5
                            0>;
        port {
                videoinput5_in: endpoint {
                        remote-endpoint = <&mipi_csi2_0_out1>;
                        io-direction    = "input";
                        stream-enable   = <1>;  // VIN_CTRL.SE
                        flush-vsync     = <1>;  // VIN_MISC.FVS
                };
        };
    };

    &videoinput6 {
        status          = "okay";
        cifport         = <&cifport             11>;
        /* memory-region
            *  - [0]: parking guideline
            *  - [1]: deinterlacing by viqe
            *  - [2]: preview
            *  - [3]: last frame
            */
        memory-region   = <0
                            0
                            &pmap_rearcamera6
                            0>;
        port {
                videoinput6_in: endpoint {
                        remote-endpoint = <&mipi_csi2_0_out2>;
                        io-direction    = "input";
                        stream-enable   = <1>;  // VIN_CTRL.SE
                        flush-vsync     = <1>;  // VIN_MISC.FVS
                };
           };
    };

    &videoinput7 {
        status          = "okay";
        cifport         = <&cifport             12>;
        /* memory-region
            *  - [0]: parking guideline
            *  - [1]: deinterlacing by viqe
            *  - [2]: preview
            *  - [3]: last frame
            */
        memory-region   = <0
                            0
                            &pmap_rearcamera7
                            0>;
        port {
                videoinput7_in: endpoint {
                        remote-endpoint = <&mipi_csi2_0_out3>;
                        io-direction    = "input";
                        stream-enable   = <1>;  // VIN_CTRL.SE
                        flush-vsync     = <1>;  // VIN_MISC.FVS
                };
        };
    };
    ```
4. Modify file {build_dir}/build/d3-g-topst-main/tmp/work/d3_g_topst_main-telechips-linux/linux-topst/5.10.205-r0/git/arch/arm64/boot/dts/telechips/tcc805x/override/topst-d3-g-i2c.dtsi as shown below
    ```
    @@ -62,10 +62,10 @@ MPQ7920_2_LDO4: ldo4 {

    &i2c6 {
            status = "disabled";
    -       port-mux = <35>;
    +       port-mux = <12>;
            pinctrl-names = "default", "sleep";
    -       pinctrl-0 = <&i2c35_bus_active>;
    -       pinctrl-1 = <&i2c35_bus_sleep>;
    +       pinctrl-0 = <&i2c12_bus_active>;
    +       pinctrl-1 = <&i2c12_bus_sleep>;

            #address-cells = <1>;
            #size-cells = <0>;
    @@ -84,10 +84,10 @@ &i2c3 {

    &i2c7 {
            status = "disabled";
    -       port-mux = <12>;
    +       port-mux = <35>;
            pinctrl-names = "default", "sleep";
    -       pinctrl-0 = <&i2c12_bus_active>;
    -       pinctrl-1 = <&i2c12_bus_sleep>;
    +       pinctrl-0 = <&i2c35_bus_active>;
    +       pinctrl-1 = <&i2c35_bus_sleep>;

            #address-cells = <1>;
            #size-cells = <0>;
    ```
5. Modify file {build_dir}/build/d3-g-topst-main/tmp/work/d3_g_topst_main-telechips-linux/linux-topst/5.10.205-r0/git/arch/arm64/boot/dts/telechips/tcc805x/tcc805x-videoinput.dtsi as shown below
    ```
    @@ -40,26 +40,26 @@ mipi_wrap: mipi_wrap {
                    * 0: select output of MIPI0
                    * 1: select output of MIPI1
                    */
    -               mipi-chmux-0 = <0>;
    +               mipi-chmux-0 = <1>;
                    mipi-chmux-1 = <1>;
    -               mipi-chmux-2 = <0>;
    -               mipi-chmux-3 = <0>;
    +               mipi-chmux-2 = <1>;
    +               mipi-chmux-3 = <1>;

                    /*
                    * 0: select output of MIPI1
                    * 1: select output of MIPI0
                    */
    -               mipi-chmux-4 = <0>;
    -               mipi-chmux-5 = <0>;
    -               mipi-chmux-6 = <0>;
    -               mipi-chmux-7 = <0>;
    +               mipi-chmux-4 = <1>;
    +               mipi-chmux-5 = <1>;
    +               mipi-chmux-6 = <1>;
    +               mipi-chmux-7 = <1>;

                    /*
                    * 1: bypass isp
                    * 0: use isp
                    */
                    isp0-bypass = <0>;
    -               isp1-bypass = <0>;
    +               isp1-bypass = <1>;
                    isp2-bypass = <1>;
                    isp3-bypass = <1>;
    ```
6. Modify file {build_dir}/build/d3-g-topst-main/tmp/work/d3_g_topst_main-telechips-linux/linux-topst/5.10.205-r0/git/include/dt-bindings/pmap/tcc805x/pmap-tcc805x-linux-videoinput.h as shown below
    ```
    @@ -21,13 +21,13 @@
     /* The number of buffers */
    #define FRAMES_CAMERA_VIQE             4
    #define FRAMES_CAMERA_PREVIEW0         4
    -#define FRAMES_CAMERA_PREVIEW1         4
    +#define FRAMES_CAMERA_PREVIEW1         0
    #define FRAMES_CAMERA_PREVIEW2         0
    #define FRAMES_CAMERA_PREVIEW3         0
    -#define FRAMES_CAMERA_PREVIEW4         0
    -#define FRAMES_CAMERA_PREVIEW5         0
    -#define FRAMES_CAMERA_PREVIEW6         0
    -#define FRAMES_CAMERA_PREVIEW7         0
    +#define FRAMES_CAMERA_PREVIEW4         4
    +#define FRAMES_CAMERA_PREVIEW5         4
    +#define FRAMES_CAMERA_PREVIEW6         4
    +#define FRAMES_CAMERA_PREVIEW7         4

    /* Reserved memory size */
    #define PMAP_SIZE_CAMERA_VIQE          \
    ```
7. 커널을 다시 빌드하고 FAI 이미지를 생성합니다.  
    빌드 디렉터리로 돌아가 아래 명령어로 커널을 다시 빌드합니다
    ```
    $ cd ${build_dir}/build/ai-g-topst-main/
    $ bitbake -C compile linux-topst
    $ cd ${build_dir}
    $ ./stitch-fai-ai.sh
    ```

위 가이드에 따라 빌드를 완료하면 GMSL 카메라를 /dev/ 아래에서 video4, video5, video6, video7로 사용할 수 있습니다.

#### 4.2.1.2 MIPI1 포트 사용 방법
먼저 GMSL 카메라와 SerDes 보드에 대한 커널 설정을 모두 활성화해야 합니다.  
다음 항목을 추가합니다  
**{build_dir}/poky/meta-topst-bsp/recipes-kernel/linux/linux-topst/tcc805x/camera.cfg** file.
```
CONFIG_VIDEO_TCC_CXD5700=y
CONFIG_VIDEO_TCC_MAX9275=y
CONFIG_VIDEO_TCC_MAX96712=y
```
To prevent the source code from being removed during the build process, enable the following line, and comment out all occurrences of `TOPST_CAM_MODULE in {build_dir}/build/d3-g-topst-main/conf/local.conf:
```
#TOPST_CAM_MODULE = "ov5647"
#TOPST_CAM_MODULE = "imx219"
```
위 옵션을 수정한 후 다음 명령어로 이미지를 다시 빌드합니다.
```
$ bitbake -c cleansstate isp-firmware
$ bitbake -c cleansstate isp-server
$ bitbake telechips-topst-image
```

다음으로 커널의 디바이스 트리를 수정해야 합니다. 아래 가이드에 따라 변경 사항을 적용하고 이미지를 다시 빌드하십시오.
1. Modify file {build_dir}/build/d3-g-topst-main/tmp/work/d3_g_topst_main-telechips-linux/linux-topst/5.10.205-r0/git/arch/arm64/boot/dts/telechips/tcc805x/override/tcc805x-videoinput-camera-module.dtsi as shown below
    ```
    //#include "tcc805x-videoinput-mipi0-ov5647.dtsi"
    //#include "tcc805x-videoinput-mipi0-imx219.dtsi"
    +#include "tcc805x-videoinput-mipi1-fhd.dtsi"
    ```
2. Modify file {build_dir}/build/d3-g-topst-main/tmp/work/d3_g_topst_main-telechips-linux/linux-topst/5.10.205-r0/git/arch/arm64/boot/dts/telechips/tcc805x/tcc805x-videoinput.dtsi as shown below
    ```
    @@ -40,26 +40,26 @@ mipi_wrap: mipi_wrap {
                     * 0: select output of MIPI0
                     * 1: select output of MIPI1
                    */
                    mipi-chmux-0 = <0>;
                    mipi-chmux-1 = <1>;
    +               mipi-chmux-1 = <0>;
                    mipi-chmux-2 = <0>;
                    mipi-chmux-3 = <0>;

                    /*
                    * 0: select output of MIPI1
                    * 1: select output of MIPI0
                    */
                    mipi-chmux-4 = <0>;
                    mipi-chmux-5 = <0>;
                    mipi-chmux-6 = <0>;
                    mipi-chmux-7 = <0>;

                    /*
                    * 1: bypass isp
                    * 0: use isp
                    */
                    isp0-bypass = <0>;
    -               isp1-bypass = <0>;
    +               isp1-bypass = <1>;
                    isp2-bypass = <1>;
                    isp3-bypass = <1>;
    ```
3. Modify file {build_dir}/build/d3-g-topst-main/tmp/work/d3_g_topst_main-telechips-linux/linux-topst/5.10.205-r0/git/include/dt-bindings/pmap/tcc805x/pmap-tcc805x-linux-videoinput.h as shown below
    ```
    @@ -21,13 +21,13 @@
    /* The number of buffers */
    #define FRAMES_CAMERA_VIQE             4
    #define FRAMES_CAMERA_PREVIEW0         4
    -#define FRAMES_CAMERA_PREVIEW1         4
    +#define FRAMES_CAMERA_PREVIEW1         0
    #define FRAMES_CAMERA_PREVIEW2         0
    #define FRAMES_CAMERA_PREVIEW3         0
    -#define FRAMES_CAMERA_PREVIEW4         0
    -#define FRAMES_CAMERA_PREVIEW5         0
    -#define FRAMES_CAMERA_PREVIEW6         0
    -#define FRAMES_CAMERA_PREVIEW7         0
    +#define FRAMES_CAMERA_PREVIEW4         4
    +#define FRAMES_CAMERA_PREVIEW5         4
    +#define FRAMES_CAMERA_PREVIEW6         4
    +#define FRAMES_CAMERA_PREVIEW7         4

    /* Reserved memory size */
    #define PMAP_SIZE_CAMERA_VIQE          \
    ```
4. 커널을 다시 빌드하고 FAI 이미지를 생성합니다.  
    빌드 디렉터리로 돌아가 아래 명령어로 커널을 다시 빌드합니다.
    ```
    $ cd ${build_dir}/build/ai-g-topst-main/
    $ bitbake -C compile linux-topst
    $ cd ${build_dir}
    $ ./stitch-fai-ai.sh
    ```

위 가이드에 따라 빌드를 완료하면 GMSL 카메라를 /dev/ 아래에서 video4, video5, video6, video7로 사용할 수 있습니다.

#### 4.2.1.3 MIPI0, 1 포트 사용 방법
먼저 GMSL 카메라와 SerDes 보드에 대한 커널 설정을 모두 활성화해야 합니다.  
다음 항목을 추가합니다  
**{build_dir}/poky/meta-topst-bsp/recipes-kernel/linux/linux-topst/tcc805x/camera.cfg** file.
```
CONFIG_VIDEO_TCC_CXD5700=y
CONFIG_VIDEO_TCC_MAX9275=y
CONFIG_VIDEO_TCC_MAX96712=y
```

To prevent the source code from being removed during the build process, enable the following line, and comment out all occurrences of `TOPST_CAM_MODULE in {build_dir}/build/d3-g-topst-main/conf/local.conf:
```
#TOPST_CAM_MODULE = "ov5647"
#TOPST_CAM_MODULE = "imx219"
```

위 옵션을 수정한 후 다음 명령어로 이미지를 다시 빌드합니다.
```
$ bitbake -c cleansstate isp-firmware
$ bitbake -c cleansstate isp-server
$ bitbake telechips-topst-image
```

VIOC에서 display 경로와 videoinput 경로가 겹치기 때문에 4-display 확장은 사용할 수 없습니다. 따라서 먼저 display 설정에서 충돌하는 경로 중 하나를 비활성화해야 합니다.
1. Modify file {build_dir}/build/d3-g-topst-main/tmp/work/d3_g_topst_main-telechips-linux/linux-topst/5.10.205-r0/git/arch/arm64/boot/dts/telechips/tcc805x/override/topst-d3-g-disp.dtsi as shown below
    ```
    @@ -437,7 +437,7 @@ dpv14_tx: dpv14_tx@12400000 {
                    sink_vcp_id = <1 2 3 4>;

                    /* default displayport configuration */
    -               dp-video-codes = <0 16 0 16 0 16 0 16>; /* video standard video codes */
    +               dp-video-codes = <0 16 0 16 0 16>; /* video standard video codes */
                    dp-phy-lane-swap = <1>;
                    dp-max-lane = <4>;
                    dp-max-rate = <3>;
    ```
2. Modify file {build_dir}/build/d3-g-topst-main/tmp/work/d3_g_topst_main-telechips-linux/linux-topst/5.10.205-r0/git/arch/arm64/boot/dts/telechips/tcc805x/override/topst-d3-g-display.dtsi as shown below
    ```
    @@ -34,9 +32,6 @@ &tccdrm_vioc2 {
            status = "okay";
    };

    -&tccdrm_vioc3 {
    -       status = "okay";
    -};

    &vioc0_out {
            vioc0_output_dp0: endpoint@0 {
    @@ -59,13 +54,6 @@ vioc2_output_dp2: endpoint@0 {
            };
    };

    -&vioc3_out {
    -       vioc3_output_dp3: endpoint@0 {
    -               reg = <0>;
    -               remote-endpoint = <&dp3_in_vioc3>;
    -       };
    -};
    -

    /* tcdrm dp */
    &tccdrm_dp0 {
    @@ -80,9 +68,6 @@ &tccdrm_dp2 {
            status = "okay";
    };

    -&tccdrm_dp3 {
    -       status = "okay";
    -};

    /* vioc0_output_dp0 -> dp0_in_vioc0 */
    &dp0_in {
    @@ -108,14 +93,6 @@ dp2_in_vioc2: endpoint@0 {
            };
    };

    -/* vioc3_output_dp3 -> dp3_in_vioc3 */
    -&dp3_in {
    -       dp3_in_vioc3: endpoint@0 {
    -               reg = <0>;
    -               remote-endpoint = <&vioc3_output_dp3>;
    -       };
    -};
    -
    /* screen_share_display_out -> tcc_drm_dummy0  */
    /* screen share */
    &tccdrm_screen_share {
    --
    ```

다음으로 커널의 디바이스 트리를 수정해야 합니다. 아래 가이드에 따라 변경 사항을 적용하고 이미지를 다시 빌드하십시오.
1. Modify file {build_dir}/build/d3-g-topst-main/tmp/work/d3_g_topst_main-telechips-linux/linux-topst/5.10.205-r0/git/arch/arm64/boot/dts/telechips/tcc805x/override/tcc805x-videoinput-camera-module.dtsi as shown below
    ```
    //#include "tcc805x-videoinput-mipi0-ov5647.dtsi"
    //#include "tcc805x-videoinput-mipi0-imx219.dtsi"
    +#include "tcc805x-videoinput-mipi0-fhd.dtsi"
    +#include "tcc805x-videoinput-mipi1-fhd.dtsi"
    ```
2. Create file {build_dir}/build/d3-g-topst-main/tmp/work/d3_g_topst_main-telechips-linux/linux-topst/5.10.205-r0/git/arch/arm64/boot/dts/telechips/tcc805x/override/tcc805x-videoinput-mipi0-fhd.dtsi as shown below
    ```
    // SPDX-License-Identifier: (GPL-2.0-or-later OR MIT)
    /*
    * Copyright (C) Telechips Inc.
    */

    &i2c7 {
    	status = "okay";
    };

    &cxd5700 {
    	/* ISP of camera module */
    	status		= "okay";
    	port {
		    cxd5700_out: endpoint {
    			remote-endpoint = <&max9275_in>;
			    io-direction	= "output";
		    };
	    };
    };

    &max9275 {
    	/* serializer */
    	status		= "okay";
    	ports {
		    #address-cells = <1>;
		    #size-cells = <0>;
		    port@0 {
    			reg = <0>;
			    max9275_in: endpoint {
    				remote-endpoint = <&cxd5700_out>;
				    io-direction	= "input";
			    };
		    };
		    port@1 {
    			reg = <1>;
			    max9275_out: endpoint {
    				remote-endpoint = <&max96712_in0>;
				    io-direction	= "output";
			    };
		    };
	    };
    };

    &max96712 {
    	/* deserializer */
    	status		= "okay";
    	pvd-name	= "fhd";
    	/*
	    * broadcasting mode access each linked devices
	    * by the same I2C slave address.
	    *
	    * Also,
	    * using the serdes I2C address mapping table,
	    * each liked devices can be accessed
	    * by the unique I2C slave address.
	    */
	    broadcasting-mode;
	    ports {
    		#address-cells = <1>;
		    #size-cells = <0>;
		    /*
		    * 0 ~ 3
		    * input ports. The number is matched with VC
		    *
		    * 4
		    * output port.
		    */
		    port@0 {
    			reg = <0>;
			    max96712_in0: endpoint {
    				remote-endpoint = <&max9275_out>;
				    io-direction	= "input";
				    channel		= <0>;
			    };
		    };
		    port@1 {
    			reg = <1>;
			    max96712_in1: endpoint {
    				remote-endpoint = <&max9275_out>;
				    io-direction	= "input";
				    channel		= <1>;
			    };
		    };
		    port@2 {
    			reg = <2>;
			    max96712_in2: endpoint {
    				remote-endpoint = <&max9275_out>;
				    io-direction	= "input";
				    channel		= <2>;
			    };  
		    };
		    port@3 {
    			reg = <3>;
			    max96712_in3: endpoint {
    				remote-endpoint = <&max9275_out>;
				    io-direction	= "input";
				    channel		= <3>;
			    };
		    };
		    port@4 {
    			reg = <4>;
			    max96712_out: endpoint {
    				remote-endpoint = <&mipi_csi2_0_in>;
				    io-direction	= "output";
				    channel		= <0>;
			    };
		    };
	    };
    };

    &mipi_csi2_0 {
    	status = "okay";
    	ports {
		    #address-cells = <1>;
		    #size-cells = <0>;
		    /*
		    * 0
		    * input port.
		    *
		    * 1 ~ 4
		    * output ports. (1: VC0 ~ 4: VC3)
		    */
		    port@0 {
    			reg = <0>;
			    mipi_csi2_0_in: endpoint {
    				remote-endpoint	= <&max96712_out>;
				    io-direction	= "input";
				    num-channel	= <4>;

				    /*
				    * 0: CH0 only, no data interleave
				    * 1: DT only
				    * 2: VC only
				    * 3: VC and DT
				    */
				    interleave-mode = <3>;
				    hs-settle = <37>;
				    data-lanes = <1 2 3 4>;
			    };
		    };
		    port@1 {
    			reg = <1>;
			    mipi_csi2_0_out0: endpoint {
    				remote-endpoint	= <&videoinput0_in>;
				    io-direction	= "output";
				    channel		= <0>;
				    /*
				    * 0: Single pixel mode
				    * 1: Dual pixel mode (RAW8/10/12, YUV422)
				    * 2: Quad pixel mode (RAW8/10/12)
				    * 3: Invalid
				    */
				    pixel-mode = <1>;
			    };
		    };
		    port@2 {
    			reg = <2>;
	    		mipi_csi2_0_out1: endpoint {
    				remote-endpoint	= <&videoinput1_in>;
				    io-direction	= "output";
				    channel		= <1>;
				    pixel-mode = <1>;
			    };
		    };
		    port@3 {
    			reg = <3>;
			    mipi_csi2_0_out2: endpoint {
    				remote-endpoint	= <&videoinput2_in>;
				    io-direction	= "output";
				    channel		= <2>;
				    pixel-mode = <1>;
			    };
		    };
		    port@4 {
    			reg = <4>;
			    mipi_csi2_0_out3: endpoint {
    				remote-endpoint	= <&videoinput3_in>;
				    io-direction	= "output";
				    channel		= <3>;
				    pixel-mode = <1>;
			    };
		    };
	    };
    };

    &videoinput0 {
    	status		= "okay";
    	cifport		= <&cifport		5>;
    	/* memory-region
	    *  - [0]: parking guideline
	    *  - [1]: deinterlacing by viqe
	    *  - [2]: preview
	    *  - [3]: last frame
	    */
	    memory-region	= <0
			    0
			    &pmap_rearcamera
			    0>;
	    port {
    		videoinput0_in: endpoint {
			    remote-endpoint	= <&mipi_csi2_0_out0>;
			    io-direction	= "input";
			    stream-enable	= <1>;	// VIN_CTRL.SE
			    flush-vsync	= <1>;	// VIN_MISC.FVS
		    };
	    };
    };

    &videoinput1 {
    	status		= "okay";
    	cifport		= <&cifport		6>;
    	/* memory-region
	    *  - [0]: parking guideline
	    *  - [1]: deinterlacing by viqe
	    *  - [2]: preview
	    *  - [3]: last frame
	    */
	    memory-region	= <0
			    0
			    &pmap_rearcamera1
			    0>;
	    port {
    		videoinput1_in: endpoint {
			    remote-endpoint	= <&mipi_csi2_0_out1>;
    			io-direction	= "input";
			    stream-enable	= <1>;	// VIN_CTRL.SE
    			flush-vsync	= <1>;	// VIN_MISC.FVS
		    };
	    };
    };

    &videoinput2 {
    	status		= "okay";
    	cifport		= <&cifport		7>;
    	/* memory-region
	    *  - [0]: parking guideline
	    *  - [1]: deinterlacing by viqe
	    *  - [2]: preview
	    *  - [3]: last frame
	    */
	    memory-region	= <0
			    0
			    &pmap_rearcamera2
			    0>;
	    port {
    		videoinput2_in: endpoint {
			    remote-endpoint	= <&mipi_csi2_0_out2>;
			    io-direction	= "input";
			    stream-enable	= <1>;	// VIN_CTRL.SE
			    flush-vsync	= <1>;	// VIN_MISC.FVS
		    };
	    };
    };

    &videoinput3 {
    	status		= "okay";
	    cifport		= <&cifport		8>;
	    /* memory-region
	    *  - [0]: parking guideline
	    *  - [1]: deinterlacing by viqe
	    *  - [2]: preview
	    *  - [3]: last frame
	    */
	    memory-region	= <0
			    0
			    &pmap_rearcamera3
			    0>;
	    port {
    		videoinput3_in: endpoint {
			    remote-endpoint	= <&mipi_csi2_0_out3>;
			    io-direction	= "input";
			    stream-enable	= <1>;	// VIN_CTRL.SE
			    flush-vsync	= <1>;	// VIN_MISC.FVS
		    };
	    };
    };
    ```
3. Modify file {build_dir}/build/d3-g-topst-main/tmp/work/d3_g_topst_main-telechips-linux/linux-topst/5.10.205-r0/git/arch/arm64/boot/dts/telechips/tcc805x/tcc805x-videoinput.dtsi as shown below
    ```
    @@ -40,26 +40,26 @@ mipi_wrap: mipi_wrap {
                     * 0: select output of MIPI0
                    * 1: select output of MIPI1
                    */
                    mipi-chmux-0 = <0>;
    -               mipi-chmux-1 = <1>;
    +               mipi-chmux-1 = <0>;
                    mipi-chmux-2 = <0>;
                    mipi-chmux-3 = <0>;

                    /*
                    * 0: select output of MIPI1
                    * 1: select output of MIPI0
                    */
                    mipi-chmux-4 = <0>;
                    mipi-chmux-5 = <0>;
                    mipi-chmux-6 = <0>;
                    mipi-chmux-7 = <0>;

                    /*
                    * 1: bypass isp
                    * 0: use isp
                    */
    -               isp0-bypass = <0>;
    -               isp1-bypass = <0>;
    +               isp0-bypass = <1>;
    +               isp1-bypass = <1>;
                    isp2-bypass = <1>;
                    isp3-bypass = <1>;
    ```
4. Modify file {build_dir}/build/d3-g-topst-main/tmp/work/d3_g_topst_main-telechips-linux/linux-topst/5.10.205-r0/git/ include/dt-bindings/pmap/tcc805x/pmap-tcc805x-linux-videoinput.h as shown below
    ```
    @@ -21,13 +21,13 @@
     /* The number of buffers */
    #define FRAMES_CAMERA_VIQE             4
    #define FRAMES_CAMERA_PREVIEW0         4
    #define FRAMES_CAMERA_PREVIEW1         4
    -#define FRAMES_CAMERA_PREVIEW2         0
    -#define FRAMES_CAMERA_PREVIEW3         0
    -#define FRAMES_CAMERA_PREVIEW4         0
    -#define FRAMES_CAMERA_PREVIEW5         0
    -#define FRAMES_CAMERA_PREVIEW6         0
    -#define FRAMES_CAMERA_PREVIEW7         0
    +#define FRAMES_CAMERA_PREVIEW2         0
    +#define FRAMES_CAMERA_PREVIEW3         0
    +#define FRAMES_CAMERA_PREVIEW4         4
    +#define FRAMES_CAMERA_PREVIEW5         4
    +#define FRAMES_CAMERA_PREVIEW6         4
    +#define FRAMES_CAMERA_PREVIEW7         4

    /* Reserved memory size */
    #define PMAP_SIZE_CAMERA_VIQE          \
    ```
5. 커널을 다시 빌드하고 FAI 이미지를 생성합니다.  
    빌드 디렉터리로 돌아가 아래 명령어로 커널을 다시 빌드합니다
    ```
    $ cd ${build_dir}/build/ai-g-topst-main/
    $ bitbake -C compile linux-topst
    $ cd ${build_dir}
    $ ./stitch-fai-ai.sh
    ```
위 가이드에 따라 빌드를 완료하면 GMSL 카메라를 /dev/ 아래에서 video0, video1, video2, video3, 4, video5, video6, video7로 사용할 수 있습니다.

### 4.2.2 AI-G GMSL 카메라 설정 가이드
Deserializer 보드를 사용하면 하나의 MIPI CSI 포트에 최대 4개의 카메라를 연결할 수 있습니다.  
AI-G 보드는 레인당 1.5 Gbps의 MIPI CSI 데이터 대역폭을 제공하므로 최대 3대의 FHD 카메라를 동시에 동작시킬 수 있습니다. 이에 따라 본 가이드에서는 3대의 FHD GMSL 카메라 연결을 다룹니다.  
HD 카메라의 경우 최대 4대까지 지원할 수 있습니다.

**참고:** 본 가이드에서는 IMX290 (cxd5700) FHD GMSL 카메라를 사용합니다.  
다른 GMSL 카메라를 사용하려면 추가적인 카메라 포팅이 필요합니다.

#### 4.2.2.1 MIPI CSI 포트 사용 방법
먼저 GMSL 카메라와 SerDes 보드에 대한 커널 설정을 모두 활성화해야 합니다.  
다음 항목을 추가합니다  
**{build_dir}/poky/meta-topst-bsp/recipes-kernel/linux/linux-topst/tcc750x/camera.cfg** file.
```
CONFIG_VIDEO_TCC_CXD5700=y
CONFIG_VIDEO_TCC_MAX9275=y
CONFIG_VIDEO_TCC_MAX96712=y
```
To prevent the source code from being removed during the build process, enable the following line, and comment out all occurrences of `TOPST_CAM_MODULE in {build_dir}/build/ai-g-topst-main/conf/local.conf:
```
#TOPST_CAM_MODULE = "ov5647"
#TOPST_CAM_MODULE = "imx219"
```
위 옵션을 수정한 후 다음 명령어로 이미지를 다시 빌드합니다.
```
$ bitbake -c cleansstate isp-firmware
$ bitbake -c cleansstate isp-server
$ bitbake telechips-topst-ai-image
```

다음으로 커널의 디바이스 트리를 수정해야 합니다. 아래 가이드에 따라 변경 사항을 적용하고 이미지를 다시 빌드하십시오.
1. Modify file {build_dir}/build/d3-g-topst-main/tmp/work/d3_g_topst_main-telechips-linux/linux-topst/5.10.205-r0/git/arch/arm64/boot/dts/telechips/tcc805x/override/tcc805x-videoinput-camera-module.dtsi as shown below
    ```
    //#include "tcc805x-videoinput-mipi0-ov5647.dtsi"
    //#include "tcc805x-videoinput-mipi0-imx219.dtsi"
    +#include " tcc750x-videoinput-odw-mipi0-fhd.dtsi"
    ```
2. Modify file {build_dir}/build/d3-g-topst-main/tmp/work/d3_g_topst_main-telechips-linux/linux-topst/5.10.205-r0/git/drivers/media/platform/tcc-mipi-csi2/csi2_s/v2.0/ tcc-mipi-csi2-csis-reg.h. as shown below
    ```
    @@ -6,7 +6,7 @@
    #ifndef TCC_MIPI_CSI2_CSIS_REG_H
    #define TCC_MIPI_CSI2_CSIS_REG_H
    
    -#define MAX_VC                         ((uint32_t)1)
    +#define MAX_VC                         ((uint32_t)4U)
    ```
3. 커널을 다시 빌드하고 FAI 이미지를 생성합니다.  
    빌드 디렉터리로 돌아가 아래 명령어로 커널을 다시 빌드합니다
    ```
    $ cd ${build_dir}/build/ai-g-topst-main/
    $ bitbake -C compile linux-topst
    $ cd ${build_dir}
    $ ./stitch-fai-ai.sh
    ```
위 가이드에 따라 빌드를 완료하면 GMSL 카메라를 /dev/ 아래에서 video0, video1, video2로 사용할 수 있습니다.

# 5. 샘플 코드 및 명령어
이 장에서는 D3-G와 AI-G 플랫폼에서 MIPI CSI 카메라, GMSL 카메라 및 USB 카메라를 사용하는 방법을 보여 주는 샘플 코드와 명령어를 제공합니다. 이 절에서는 카메라 재생 방법에 대한 간단한 개요를 설명합니다:  
D3-G에서는 GStreamer 또는 OpenCV를 사용하여 카메라 스트림을 확인할 수 있으며,  
AI-G에서는 애플리케이션 프레임워크를 통해 카메라 재생이 처리됩니다.

## 5.1 카메라 재생을 위한 샘플 코드 및 명령어
### 5.1.1 MIPI CSI 카메라 사용자 가이드
이 절에서는 Yocto 및 Ubuntu 환경에서 MIPI CSI 카메라 영상을 표시하는 방법을 설명합니다.

#### 5.1.1.1 D3-G에서의 MIPI CSI 카메라 사용자 가이드 (OV5647)
##### 5.1.1.1.1 Yocto 이미지에서 OV5647 사용하기
[topst.ai DOCS 페이지](https://topst.ai/tech/docs?page=624bd237b3013e87c05c125b8031e2f370ccca2b)에서 제공되는 공식 Yocto 이미지 또는 Yocto를 직접 빌드하여 생성한 이미지를 사용하는 경우, OV5647 카메라는 기본 해상도 1296×972, 30 fps로 동작합니다. 따라서 이 환경에서의 카메라 재생은 1296×972, 30 fps로 이루어집니다.  
아래 단계를 따르십시오:
1. 현재 실행 중인 topst-welcome 서비스를 중지합니다
    ```
    $ sudo systemctl stop topst-welcome
    ```
2. UART 콘솔에 다음 명령을 입력합니다
    ```
    $ export XDG_RUNTIME_DIR=/run/user/root
    ```
3. 아래와 같이 GStreamer 명령어를 사용하여 카메라 스트림을 재생합니다
    ```
    $ gst-launch-1.0 v4l2src device=/dev/video0 io-mode=2 ! video/x-raw,format=NV12,width=1296,height=972,framerate=30/1 ! videoconvert ! waylandsink sync=false
    ```
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/accessories/Camera/5.1%201296%C3%97972%20ov5647%20camera%20out%20display%20on%20yocto.png"></p>
<p align="center"><strong>그림 5.1 Yocto에서 1296×972 OV5647 카메라 출력 표시</strong></p>

**참고:** 해상도가 1296×972이지만, 명령어 끝에 fullscreen=true 옵션을 추가하면 전체 화면으로 영상을 재생할 수 있습니다.

##### 5.1.1.1.2 Ubuntu 이미지에서 OV5647 사용하기
[topst.ai DOCS 페이지](https://topst.ai/tech/docs?page=624bd237b3013e87c05c125b8031e2f370ccca2b)에서 제공되는 공식 Ubuntu 이미지를 사용하는 경우, OV5647 카메라는 기본 해상도 1296×972, 30 fps로 동작합니다. 따라서 이 환경에서의 카메라 재생은 1296×972, 30 fps로 이루어집니다.  
아래 단계를 따르십시오:
1. - UART로 연결한 경우: topst 계정으로 로그인한 상태에서 UART 콘솔에 다음 명령을 입력하십시오
    ```
    $ export XDG_RUNTIME_DIR=/run/user/1000
    ```
    - 디스플레이에서 직접 제어하는 경우: 터미널 창을 엽니다
2. 아래와 같이 GStreamer 명령을 사용하여 카메라 스트림을 재생합니다. Ubuntu에서는 하드웨어 가속 Wayland 렌더링을 사용할 수 없으므로, 대신 H.265 인코딩/디코딩을 사용하여 VPU 가속을 통한 재생을 활용합니다
    ```
    $ gst-launch-1.0 v4l2src device=/dev/video0 io-mode=2 ! video/x-raw,format=NV12,width=1280,height=720,framerate=30/1 ! v4l2h265enc ! h265parse ! v4l2h265dec ! videoconvert ! waylandsink sync=false
    ```
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/accessories/Camera/5.2%201296%C3%97972%20ov5647%20camera%20out%20display%20on%20ubuntu.png"></p>
<p align="center"><strong>그림 5.2 Ubuntu에서 1296×972 OV5647 카메라 출력 표시</strong></p>

**참고:** 해상도가 1296×972이지만, 명령어 끝에 fullscreen=true 옵션을 추가하면 전체 화면으로 영상을 재생할 수 있습니다.

GStreamer 외에 OpenCV를 사용하여 카메라 스트림을 표시할 수도 있습니다. 아래 단계를 따르면 OpenCV로 카메라 영상을 간편하게 미리 볼 수 있습니다.
1. OpenCV 설치
    ```
    $ sudo apt-get install python3-opencv
    ```
2. opencv_cam.py 파일 안에 다음 코드를 작성합니다
    ```
    import cv2
    
    pipeline = (
        "v4l2src device=/dev/video0 io-mode=2 ! "
        "video/x-raw,format=NV12,width=1296,height=972,framerate=30/1 ! "
        "videoconvert ! video/x-raw,format=BGR ! appsink sync=false"
    )
    
    cap = cv2.VideoCapture(pipeline, cv2.CAP_GSTREAMER)
    
    if not cap.isOpened():
        print("ERROR: cannot open camera via GStreamer")
        exit()
    
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Frame read error")
            break
    
        cv2.imshow("Camera", frame)
        if cv2.waitKey(1) == 27:
            break
    
    cap.release()
    cv2.destroyAllWindows()
    ```
3. Python으로 opencv_cam.py를 실행합니다
    ```
    $ python3 opencv_cam.py
    ```
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/accessories/Camera/5.3%201296%C3%97972%20opencv%20ov5647%20camera%20out%20display%20on%20ubuntu.png"></p>
<p align="center"><strong>그림 5.3 Ubuntu에서 OpenCV로 실행한 1296×972 OV5647 카메라 출력</strong></p>

##### 5.1.1.1.3 D3-G에서 해상도별 Gstreawmer 파이프라인 구성
각 해상도에 맞는 GStreamer 파이프라인 옵션을 지정한 후 카메라 스트림을 실행하십시오.
1. 1920x1080 @ 30fps
    ```
    $ gst-launch-1.0 v4l2src device=/dev/video0 io-mode=2 ! video/x-raw,format=NV12,width=1920,height=1080,framerate=30/1 ! videoconvert ! waylandsink sync=false
    ```
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/accessories/Camera/5.4%201920x1080%20ov5647%20camera%20out%20display%20on%20yocto.png"></p>
    <p align="center"><strong>그림 5.4 Yocto에서의 1920x1080 OV5647 카메라 출력 화면</strong></p>
2. 1296x972 @ 30fps
    ```
    $ gst-launch-1.0 v4l2src device=/dev/video0 io-mode=2 ! video/x-raw,format=NV12,width=1296,height=972,framerate=30/1 ! videoconvert ! waylandsink sync=false
    ```
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/accessories/Camera/5.1%201296%C3%97972%20ov5647%20camera%20out%20display%20on%20yocto.png"></p>
    <p align="center"><strong>그림 5.5 Yocto에서의 1296x972 OV5647 카메라 출력 화면</strong></p>
3. 640x480 @ 60fps
    ```
    $ gst-launch-1.0 v4l2src device=/dev/video0 io-mode=2 ! video/x-raw,format=NV12,width=640,height=480,framerate=60/1 ! videoconvert ! waylandsink sync=false
    ```
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/accessories/Camera/5.6%20640x480%20ov5647%20camera%20out%20display%20on%20yocto.png"></p>
    <p align="center"><strong>그림 5.6 Yocto에서의 640x480 OV5647 카메라 출력 화면</strong></p>

또한 H.265 인코더 및 디코더를 사용하는 파이프라인을 구성하여 하드웨어 가속 재생을 활성화할 수 있습니다.
1. 1920x1080 @ 30fps
    ```
    $ gst-launch-1.0 v4l2src device=/dev/video0 io-mode=2 ! video/x-raw,format=NV12,width=1920,height=1080,framerate=30/1 ! v4l2h265enc ! h265parse ! v4l2h265dec ! videoconvert ! waylandsink sync=false
    ```
2. 1296x972 @ 30fps
    ```
    $ gst-launch-1.0 v4l2src device=/dev/video0 io-mode=2 ! video/x-raw,format=NV12,width=1280,height=720,framerate=30/1 !  v4l2h265enc ! h265parse ! v4l2h265dec ! videoconvert ! waylandsink sync=false
    ```
3. 640x480 @ 60fps
    ```
    $ gst-launch-1.0 v4l2src device=/dev/video0 io-mode=2 ! video/x-raw,format=NV12,width=640,height=480,framerate=60/1 ! v4l2h265enc ! h265parse ! v4l2h265dec ! videoconvert ! waylandsink sync=false
    ```

    해상도 변경에 대해서는 4.1.2.2절을 참조하십시오.

#### 5.1.1.2 D3-G에서의 MIPI CSI 카메라 사용자 가이드 (IMX219)
##### 5.1.1.2.1 Yocto 이미지에서 IMX219 사용하기
[topst.ai DOCS 페이지](https://topst.ai/tech/docs?page=624bd237b3013e87c05c125b8031e2f370ccca2b)에서 제공되는 공식 Yocto 이미지 또는 Yocto를 직접 빌드하여 생성한 이미지를 사용하는 경우, IMX219 카메라는 기본 해상도 1640×1232, 30 fps로 동작합니다. 따라서 이 환경에서의 카메라 재생은 1640×1232, 30 fps로 이루어집니다.  
아래 단계를 따르십시오:
1. 현재 실행 중인 topst-welcome 서비스를 중지합니다
    ```
    $ sudo systemctl stop topst-welcome
    ```
2. UART 콘솔에 다음 명령을 입력합니다
    ```
    $ export XDG_RUNTIME_DIR=/run/user/root
    ```
3. 아래와 같이 GSTreamer 명령어를 사용하여 카메라 스트림을 재생합니다
    ```
    $ gst-launch-1.0 v4l2src device=/dev/video0 io-mode=2 ! video/x-raw,format=NV12,width=1640,height=1232,framerate=30/1 ! videoconvert ! waylandsink sync=false
    ```
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/accessories/Camera/5.7%201640x1232%20imx219%20camera%20out%20display%20on%20yocto.png"></p>
<p align="center"><strong>그림 5.7 Yocto에서 1640x972 IMX219 카메라 출력 표시</strong></p>

**참고:** 해상도가 1640×1232이지만, 명령어 끝에 fullscreen=true 옵션을 추가하면 전체 화면으로 영상을 재생할 수 있습니다.

##### 5.1.1.2.2 Ubuntu 이미지에서 IMX219 사용하기
[topst.ai DOCS 페이지](https://topst.ai/tech/docs?page=624bd237b3013e87c05c125b8031e2f370ccca2b)에서 제공되는 공식 Ubuntu 이미지를 사용하는 경우, IMX219 카메라는 기본 해상도 1640×1232, 30 fps로 동작합니다. 따라서 이 환경에서의 카메라 재생은 1640×1232, 30 fps로 이루어집니다.  
아래 단계를 따르십시오:
1. - UART로 연결한 경우: topst 계정으로 로그인한 상태에서 UART 콘솔에 다음 명령을 입력하십시오
    ```
    $ export XDG_RUNTIME_DIR=/run/user/1000
    ```
    - 디스플레이에서 직접 제어하는 경우: 터미널 창을 엽니다
2. 아래와 같이 GStreamer 명령을 사용하여 카메라 스트림을 재생합니다. Ubuntu에서는 하드웨어 가속 Wayland 렌더링을 사용할 수 없으므로, 대신 H.265 인코딩/디코딩을 사용하여 VPU 가속을 통한 재생을 활용합니다
    ```
    $ gst-launch-1.0 v4l2src device=/dev/video0 io-mode=2 ! video/x-raw,format=NV12,width=1600,height=1200,framerate=30/1 ! v4l2h265enc ! h265parse ! v4l2h265dec ! videoconvert ! waylandsink sync=false
    ```
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/accessories/Camera/5.8%201640x1232%20imx219%20camera%20out%20display%20on%20ubuntu.png"></p>
<p align="center"><strong>그림 5.8 Ubuntu에서 1640x972 IMX219 카메라 출력 표시</strong></p>

**참고:** 해상도가 1640×1232이지만, 명령어 끝에 fullscreen=true 옵션을 추가하면 전체 화면으로 영상을 재생할 수 있습니다.

GStreamer 외에 OpenCV를 사용하여 카메라 스트림을 표시할 수도 있습니다. 아래 단계를 따르면 OpenCV로 카메라 영상을 간편하게 미리 볼 수 있습니다.
1. OpenCV 설치
    ```
    $ sudo apt-get install python3-opencv
    ```
2. opencv_cam.py 파일 안에 다음 코드를 작성합니다.
    ```
    import cv2
    
    pipeline = (
        "v4l2src device=/dev/video0 io-mode=2 ! "
        "video/x-raw,format=NV12,width=1640,height=1232,framerate=30/1 ! "
        "videoconvert ! video/x-raw,format=BGR ! appsink sync=false"
    )
    
    cap = cv2.VideoCapture(pipeline, cv2.CAP_GSTREAMER)
    
    if not cap.isOpened():
        print("ERROR: cannot open camera via GStreamer")
        exit()
    
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Frame read error")
            break
    
        cv2.imshow("Camera", frame)
        if cv2.waitKey(1) == 27:
            break
    
    cap.release()
    cv2.destroyAllWindows()
    ```
3. Python으로 opencv_cam.py를 실행합니다
```
$ python3 opencv_cam.py
```
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/accessories/Camera/5.9%201640x1232%20opencv%20imx219%20camera%20out%20display.png"></p>
<p align="center"><strong>그림 5.9 Ubuntu에서 OpenCV로 실행한 1640×1232 IMX219 카메라 출력</strong></p>

##### 5.1.1.2.3 D3-G에서 해상도별 GStreamer 파이프라인 구성
각 해상도에 맞는 GStreamer 파이프라인 옵션을 지정한 후 카메라 스트림을 실행하십시오.
1. 1920x1080 @ 30fps
    ```
    $ gst-launch-1.0 v4l2src device=/dev/video0 io-mode=2 ! video/x-raw,format=NV12,width=1920,height=1080,framerate=30/1 ! videoconvert ! waylandsink sync=false
    ```
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/accessories/Camera/5.10%201920x1080%20imx219%20camera%20out%20display%20on%20yocto.png"></p>
    <p align="center"><strong>그림 5.10 Yocto에서의 1920x1080 IMX219 카메라 출력 화면</strong></p>
2. 1640x1232 @ 30fps
    ```
    $ gst-launch-1.0 v4l2src device=/dev/video0 io-mode=2 ! video/x-raw,format=NV12,width=1640,height=1232,framerate=30/1 ! videoconvert ! waylandsink sync=false
    ```
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/accessories/Camera/5.7%201640x1232%20imx219%20camera%20out%20display%20on%20yocto.png"></p>
    <p align="center"><strong>그림 5.11 Yocto에서의 1620x1232 IMX219 카메라 출력 화면</strong></p>
3. 640x480 @ 30fps
    ```
    $ gst-launch-1.0 v4l2src device=/dev/video0 io-mode=2 ! video/x-raw,format=NV12,width=640,height=480,framerate=30/1 ! videoconvert ! waylandsink sync=false
    ```
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/accessories/Camera/5.12%20640x480%20imx219%20camera%20out%20display%20on%20yocto.png"></p>
    <p align="center"><strong>그림 5.12 Yocto에서의 640x480 IMX219 카메라 출력 화면</strong></p>

또한 H.265 인코더 및 디코더를 사용하는 파이프라인을 구성하여 하드웨어 가속 재생을 활성화할 수 있습니다.
1. 1920x1080 @ 30fps
    ```
    $ gst-launch-1.0 v4l2src device=/dev/video0 io-mode=2 ! video/x-raw,format=NV12,width=1920,height=1080,framerate=30/1 ! v4l2h265enc ! h265parse ! v4l2h265dec ! videoconvert ! waylandsink sync=false
    ```
2. 1640x1232 @ 30fps
    ```
    $ gst-launch-1.0 v4l2src device=/dev/video0 io-mode=2 ! video/x-raw,format=NV12,width=1600,height=1200,framerate=30/1 !  v4l2h265enc ! h265parse ! v4l2h265dec ! videoconvert ! waylandsink sync=false
    ```
3. 640x480 @ 30fps
    ```
    $ gst-launch-1.0 v4l2src device=/dev/video0 io-mode=2 ! video/x-raw,format=NV12,width=640,height=480,framerate=30/1 ! v4l2h265enc ! h265parse ! v4l2h265dec ! videoconvert ! waylandsink sync=false
    ```

해상도 변경은 4.1.3.3절을 참조하십시오.

#### 5.1.1.3 AI-G에서의 MIPI CSI 카메라 사용자 가이드 (OV5647)
##### 5.1.1.3.1 Yocto 이미지에서 OV5647 사용하기
AI-G에서는 두 가지 애플리케이션을 사용할 수 있습니다. 하나는 추론 결과와 함께 카메라 영상을 재생하는 애플리케이션이고, 다른 하나는 단순히 카메라 영상을 보는 애플리케이션입니다. 사용 사례에 따라 둘 중 하나를 선택할 수 있습니다.
- tcnnapp
    ```
    $ tcnnapp
    ```
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/accessories/Camera/5.13%20ov5647%20camera%20out%20display%20with%20running%20tcnnapp%20on%20yocto.png"></p>
    <p align="center"><strong>그림 5.13 Yocto에서 tcnnapp 실행 시 OV5647 카메라 출력 화면</strong></p>
- tcnncameraapp
    ```
    $ tcnncameraapp
    ```
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/accessories/Camera/5.14%20ov5647%20camera%20out%20display%20with%20running%20tcnncameraapp%20on%20yocto.png"></p>
    <p align="center"><strong>그림 5.14 Yocto에서 tcnncameraapp 실행 시 OV5647 카메라 출력 화면</strong></p>

##### 5.1.1.3.2 Ubuntu 이미지에서 사용하기
AI-G에서는 두 가지 애플리케이션을 사용할 수 있습니다. 하나는 추론 결과와 함께 카메라 영상을 재생하는 애플리케이션이고, 다른 하나는 단순히 카메라 영상을 보는 애플리케이션입니다. 사용 사례에 따라 둘 중 하나를 선택할 수 있습니다.
- tcnnapp
    ```
    $ tcnnapp
    ```
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/accessories/Camera/5.13%20ov5647%20camera%20out%20display%20with%20running%20tcnnapp%20on%20yocto.png"></p>
    <p align="center"><strong>그림 5.15 Ubuntu에서 tcnnapp 실행 시 OV5647 카메라 출력 화면</strong></p>
- tcnncameraapp
    ```
    $ tcnncameraapp
    ```
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/accessories/Camera/5.14%20ov5647%20camera%20out%20display%20with%20running%20tcnncameraapp%20on%20yocto.png"></p>
    <p align="center"><strong>그림 5.16 Ubuntu에서 tcnncameraapp 실행 시 OV5647 카메라 출력 화면</strong></p>

#### 5.1.1.4 AI-G에서의 MIPI CSI 카메라 사용자 가이드 (IMX219)
##### 5.1.1.4.1 Yocto 이미지에서 IMX219 사용하기
AI-G에서는 두 가지 애플리케이션을 사용할 수 있습니다. 하나는 추론 결과와 함께 카메라 영상을 재생하는 애플리케이션이고, 다른 하나는 단순히 카메라 영상을 보는 애플리케이션입니다. 사용 사례에 따라 둘 중 하나를 선택할 수 있습니다.
- tcnnapp
    ```
    $ tcnnapp
    ```
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/accessories/Camera/5.17%20imx219%20camera%20out%20display%20with%20running%20tcnnapp%20on%20yocto.png"></p>
    <p align="center"><strong>그림 5.17 Yocto에서 tcnnapp 실행 시 OV5647 카메라 출력 화면</strong></p>
- tcnncameraapp
    ```
    $ tcnncameraapp
    ```
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/accessories/Camera/5.18%20imx219%20camera%20out%20display%20with%20running%20tcnncameraapp%20on%20yocto.png"></p>
    <p align="center"><strong>그림 5.18 Yocto에서 tcnncameraapp 실행 시 OV5647 카메라 출력 화면</strong></p>

##### 5.1.1.4.2 Ubuntu 이미지에서 IMX219 사용하기
AI-G에서는 두 가지 애플리케이션을 사용할 수 있습니다. 하나는 추론 결과와 함께 카메라 영상을 재생하는 애플리케이션이고, 다른 하나는 단순히 카메라 영상을 보는 애플리케이션입니다. 사용 사례에 따라 둘 중 하나를 선택할 수 있습니다.
- tcnnapp
    ```
    $ tcnnapp
    ```
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/accessories/Camera/5.17%20imx219%20camera%20out%20display%20with%20running%20tcnnapp%20on%20yocto.png"></p>
    <p align="center"><strong>그림 5.17 Yocto에서 tcnnapp 실행 시 OV5647 카메라 출력 화면</strong></p>
- tcnncameraapp
    ```
    $ tcnncameraapp
    ```
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/accessories/Camera/5.18%20imx219%20camera%20out%20display%20with%20running%20tcnncameraapp%20on%20yocto.png"></p>
    <p align="center"><strong>그림 5.18 Yocto에서 tcnncameraapp 실행 시 OV5647 카메라 출력 화면</strong></p>

### 5.1.2 GMSL 카메라 사용자 가이드
이 절에서는 Yocto 및 Ubuntu 환경에서 GMSL 카메라 영상을 표시하는 방법을 설명합니다.

#### 5.1.2.1 D3-G에서의 GMSL 카메라 사용자 가이드
##### 5.1.2.1.1 Yocto 이미지에서 GMSL 카메라 사용하기
[topst.ai DOCS 페이지](https://topst.ai/tech/docs?page=624bd237b3013e87c05c125b8031e2f370ccca2b)에서 제공되는 공식 Yocto 이미지 또는 Yocto를 직접 빌드하여 생성한 이미지를 사용하는 경우, GMSL 카메라는 기본 해상도 1920×1080, 30 fps로 동작합니다. 따라서 이 환경에서의 카메라 재생은 1920×1080, 30 fps로 이루어집니다.  
아래 단계를 따르십시오:
1. 현재 실행 중인 topst-welcome 서비스를 중지합니다
    ```
    $ sudo systemctl stop topst-welcome
    ```
2. UART 콘솔에 다음 명령을 입력합니다
    ```
    $ export XDG_RUNTIME_DIR=/run/user/root
    ```
3. 아래와 같이 GStreamer 명령어를 사용하여 카메라 스트림을 재생합니다
    ```
    $ gst-launch-1.0 v4l2src device=/dev/video4 io-mode=2 ! video/x-raw,format=NV12,width=1920,height=1080,framerate=30/1 ! videoconvert ! waylandsink sync=false
    ```

또한 아래 스크립트를 실행하면 gpu를 사용하여 카메라 영상을 4분할 화면으로 표시할 수 있습니다.
```
#/bin/bash
 
set -euo pipefail
 
export GST_GL_WINDOW=wayland
export GST_GL_API=gles2
# glimagesink force-aspect-ratio=false sync=false \
 
gst-launch-1.0 -v \
  glvideomixer name=m background=black \
    sink_0::xpos=0   sink_0::ypos=0 \
    sink_1::xpos=960 sink_1::ypos=0 \
    sink_2::xpos=0   sink_2::ypos=540 \
    sink_3::xpos=960 sink_3::ypos=540 ! \
    "video/x-raw,format=RGBA,width=1920,height=1080,framerate=30/1" ! \
  waylandsink sync=false \
  v4l2src device=/dev/video4 io-mode=4 ! \
    video/x-raw,format=NV12,width=1920,height=1080,framerate=30/1 ! \
    glupload ! \
    glcolorscale ! "video/x-raw(memory:GLMemory),width=960,height=540" ! \
    m.sink_0 \
  \
  v4l2src device=/dev/video5 io-mode=4 ! \
    video/x-raw,format=NV12,width=1920,height=1080,framerate=30/1 ! \
    glupload ! \
    glcolorscale ! "video/x-raw(memory:GLMemory),width=960,height=540" ! \
    m.sink_1 \
  \
  v4l2src device=/dev/video6 io-mode=4 ! \
    video/x-raw,format=NV12,width=1920,height=1080,framerate=30/1 ! \
    glupload ! \
    glcolorscale ! "video/x-raw(memory:GLMemory),width=960,height=540" ! \
    m.sink_2 \
  \
  v4l2src device=/dev/video7 io-mode=4 ! \
    video/x-raw,format=NV12,width=1920,height=1080,framerate=30/1 ! \
    glupload ! \
    glcolorscale ! "video/x-raw(memory:GLMemory),width=960,height=540" ! \
    m.sink_3
```

GMSL 카메라는 video4, video5, video6, video7로 표시되며 필요에 따라 이 장치 중 하나를 선택할 수 있습니다.  
8대의 카메라를 연결하면 시스템은 이를 video0부터 video8까지 열거하며, 해당 장치 노드 중 원하는 것을 선택할 수 있습니다.

##### 5.1.2.1.2 Ubuntu 이미지에서 GMSL 카메라 사용하기
[topst.ai DOCS 페이지](https://topst.ai/tech/docs?page=624bd237b3013e87c05c125b8031e2f370ccca2b)에서 제공되는 공식 Ubuntu 이미지를 사용하는 경우, GMSL 카메라는 기본 해상도 1920×1080, 30 fps로 동작합니다. 따라서 이 환경에서의 카메라 재생은 1920×1080, 30 fps로 이루어집니다.  
아래 단계를 따르십시오:
1. - UART로 연결한 경우: topst 계정으로 로그인한 상태에서 UART 콘솔에 다음 명령을 입력하십시오
    ```
    $ export XDG_RUNTIME_DIR=/run/user/1000
    ```
    - 디스플레이에서 직접 제어하는 경우: 터미널 창을 엽니다
2. 아래와 같이 GStreamer 명령을 사용하여 카메라 스트림을 재생합니다. Ubuntu에서는 하드웨어 가속 Wayland 렌더링을 사용할 수 없으므로, 대신 H.265 인코딩/디코딩을 사용하여 VPU 가속을 통한 재생을 활용합니다
    ```
    $ gst-launch-1.0 v4l2src device=/dev/video0 io-mode=2 ! video/x-raw,format=NV12,width=1920,height=1080,framerate=30/1 ! v4l2h265enc ! h265parse ! v4l2h265dec ! videoconvert ! waylandsink sync=false
    ```

또한 아래 스크립트를 실행하면 gpu를 사용하여 카메라 영상을 4분할 화면으로 표시할 수 있습니다.
```
#/bin/bash

set -euo pipefail

export GST_GL_WINDOW=wayland
export GST_GL_API=gles2

gst-launch-1.0 -v \
  glvideomixer name=m background=black \
    sink_0::xpos=0   sink_0::ypos=0 \
    sink_1::xpos=960 sink_1::ypos=0 \
    sink_2::xpos=0   sink_2::ypos=540 \
    sink_3::xpos=960 sink_3::ypos=540 ! \
    glcolorconvert ! "video/x-raw(memory:GLMemory),format=RGBA,width=1920,height=1080,framerate=30/1,pixel-aspect-ratio=1/1" ! \
  glimagesink force-aspect-ratio=false sync=false \
  \
  v4l2src device=/dev/video4 io-mode=4 ! video/x-raw,format=NV12,framerate=30/1,pixel-aspect-ratio=1/1 ! \
    videoconvert ! glupload ! glcolorscale ! \
    "video/x-raw(memory:GLMemory),format=RGBA,width=960,height=540,pixel-aspect-ratio=1/1" ! m.sink_0 \
  \
  v4l2src device=/dev/video5 io-mode=4 ! video/x-raw,format=NV12,framerate=30/1,pixel-aspect-ratio=1/1 ! \
    videoconvert ! glupload ! glcolorscale ! \
    "video/x-raw(memory:GLMemory),format=RGBA,width=960,height=540,pixel-aspect-ratio=1/1" ! m.sink_1 \
  \
  v4l2src device=/dev/video6 io-mode=4 ! video/x-raw,format=NV12,framerate=30/1,pixel-aspect-ratio=1/1 ! \
    videoconvert ! glupload ! glcolorscale ! \
    "video/x-raw(memory:GLMemory),format=RGBA,width=960,height=540,pixel-aspect-ratio=1/1" ! m.sink_2 \
  \
  v4l2src device=/dev/video7 io-mode=4 ! video/x-raw,format=NV12,framerate=30/1,pixel-aspect-ratio=1/1 ! \
    videoconvert ! glupload ! glcolorscale ! \
    "video/x-raw(memory:GLMemory),format=RGBA,width=960,height=540,pixel-aspect-ratio=1/1" ! m.sink_3
```

또한 OpenCV를 사용하여 카메라 스트림을 표시할 수도 있습니다. 아래 단계를 따르면 OpenCV로 카메라 영상을 간편하게 미리 볼 수 있습니다.
1. OpenCV 설치
    ```
    $ sudo apt-get install python3-opencv
    ```
2. opencv_cam.py 파일 안에 다음 코드를 작성합니다
    ```
    import cv2
    
    pipeline = (
        "v4l2src device=/dev/video4 io-mode=2 ! "
        "video/x-raw,format=NV12,width=1920,height=1080,framerate=30/1 ! "
        "videoconvert ! video/x-raw,format=BGR ! appsink sync=false"
    )
    
    cap = cv2.VideoCapture(pipeline, cv2.CAP_GSTREAMER)
    
    if not cap.isOpened():
        print("ERROR: cannot open camera via GStreamer")
        exit()
    
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Frame read error")
            break
    
        cv2.imshow("Camera", frame)
        if cv2.waitKey(1) == 27:
            break
    
    cap.release()
    cv2.destroyAllWindows()
    ```
3. Python으로 opencv_cam.py 파일을 실행합니다
    ```
    $ python3 opencv_cam.py
    ```

GMSL 카메라는 video4, video5, video6, video7로 표시되며 필요에 따라 이 장치 중 하나를 선택할 수 있습니다.  
8대의 카메라를 연결하면 시스템은 이를 video0부터 video8까지 열거하며, 해당 장치 노드 중 원하는 것을 선택할 수 있습니다.

#### 5.1.2.2 AI-G에서의 GMSL 카메라 사용자 가이드
##### 5.1.2.2.1 Yocto 이미지에서 GMSL 카메라 사용하기
AI-G에서는 두 가지 애플리케이션을 사용할 수 있습니다. 하나는 추론 결과와 함께 카메라 영상을 재생하는 애플리케이션이고, 다른 하나는 단순히 카메라 영상을 보는 애플리케이션입니다. 사용 사례에 따라 둘 중 하나를 선택할 수 있습니다.
- tcnnapp
- tcnncameraapp

GMSL 카메라는 **video0**, **video1**, **video2**로 표시되며 필요에 따라 이 장치 중 하나를 선택할 수 있습니다.
각 애플리케이션은 기본적으로 video2를 사용하지만 **-p 옵션**을 사용하여 비디오 장치를 변경할 수 있습니다.
아래 예제는 **video0**을 선택하는 방법을 보여 줍니다.

- tcnnapp
    ```
    $ tcnnapp -p /dev/video0
    ```
- tcnncameraapp
    ```
    $ tcnncameraapp -p /dev/video0
    ```

##### 5.1.2.2.2 Ubuntu 이미지에서 GMSL 카메라 사용하기
AI-G에서는 두 가지 애플리케이션을 사용할 수 있습니다. 하나는 추론 결과와 함께 카메라 영상을 재생하는 애플리케이션이고, 다른 하나는 단순히 카메라 영상을 보는 애플리케이션입니다. 사용 사례에 따라 둘 중 하나를 선택할 수 있습니다.
- tcnnapp
- tcnncameraapp

GMSL 카메라는 **video0**, **video1**, **video2**로 표시되며 필요에 따라 이 장치 중 하나를 선택할 수 있습니다.
각 애플리케이션은 기본적으로 video2를 사용하지만 **-p 옵션**을 사용하여 비디오 장치를 변경할 수 있습니다.
아래 예제는 **video0**을 선택하는 방법을 보여 줍니다.

- tcnnapp
    ```
    $ tcnnapp -p /dev/video0
    ```
- tcnncameraapp
    ```
    $ tcnncameraapp -p /dev/video0
    ```

### 5.1.3 USB 카메라 사용자 가이드
이 절에서는 Yocto 및 Ubuntu 환경에서 USB 카메라 영상을 표시하는 방법을 설명합니다.
AI-G에는 USB 인터페이스가 없으므로, 해당 플랫폼에 대한 USB 카메라 가이드는 제공되지 않습니다.

#### 5.1.3.1 D3-G에서의 USB 카메라 사용자 가이드
본 문서에서는 1920×1080, 30fps를 지원하는 USB 카메라를 기준으로 설명합니다

**참고:** MIPI 카메라가 기본적으로 **/dev/video0**에 할당되므로, USB 카메라는 /dev/video1로 생성됩니다.
USB 카메라를 동작시킬 때는 반드시 **/dev/video1** 을 사용하십시오.

##### 5.1.3.1.1 Yocto 이미지에서 USB 카메라 사용하기
[topst.ai DOCS 페이지](https://topst.ai/tech/docs?page=624bd237b3013e87c05c125b8031e2f370ccca2b)에서 제공되는 공식 Yocto 이미지 또는 Yocto를 직접 빌드하여 생성한 이미지를 사용하는 경우, USB 카메라는 카메라 자체 사양에 정의된 해상도와 프레임 레이트로 동작합니다. 따라서 영상은 USB 카메라가 제공하는 기본 해상도와 FPS로 재생됩니다.  
아래 단계를 따르십시오:
1. 현재 실행 중인 topst-welcome 서비스를 중지합니다
    ```
    $ sudo systemctl stop topst-welcome
    ```
2. UART 콘솔에 다음 명령을 입력합니다
    ```
    $ export XDG_RUNTIME_DIR=/run/user/root
    ```
3. 아래와 같이 GStreamer 명령어를 사용하여 카메라 스트림을 재생합니다. v4l2-ctl -d /dev/video1 --list-formats-ext로 USB 카메라 정보를 확인하면 지원 포맷이 MJPEG으로 표시됩니다. 따라서 jpegdec을 사용합니다
    ```
    $ gst-launch-1.0 v4l2src device=/dev/video1 ! image/jpeg,width=1920,height=1080 ! jpegdec ! videoconvert ! waylandsink
    ```

##### 5.1.3.1.2 Ubuntu 이미지에서 USB 카메라 사용하기
[topst.ai DOCS 페이지](https://topst.ai/tech/docs?page=624bd237b3013e87c05c125b8031e2f370ccca2b)에서 제공되는 공식 Ubuntu 이미지 또는 직접 생성한 이미지를 사용하는 경우, USB 카메라는 카메라 자체 사양에 정의된 해상도와 프레임 레이트로 동작합니다. 따라서 영상은 USB 카메라가 제공하는 기본 해상도와 FPS로 재생됩니다.  
아래 단계를 따르십시오:
1. - UART로 연결한 경우: topst 계정으로 로그인한 상태에서 UART 콘솔에 다음 명령을 입력하십시오
    ```
    $ export XDG_RUNTIME_DIR=/run/user/1000
    ```
    - 디스플레이에서 직접 제어하는 경우: 터미널 창을 엽니다
2. 아래와 같이 GStreamer 명령어를 사용하여 카메라 스트림을 재생합니다. v4l2-ctl -d /dev/video1 --list-formats-ext로 USB 카메라 정보를 확인하면 지원 포맷이 MJPEG으로 표시됩니다. 따라서 jpegdec을 사용합니다
    ```
    $ gst-launch-1.0 v4l2src device=/dev/video1 ! image/jpeg,width=1920,height=1080 ! jpegdec ! videoconvert ! waylandsink
    ```
3. H.265 인코딩 및 디코딩을 사용하려면 v4l2src가 지원하는 NV12 포맷으로 영상을 변환해야 합니다. 따라서 아래와 같이 파이프라인을 구성해야 합니다
    ```
    $ gst-launch-1.0 v4l2src device=/dev/video1 io-mode=2 ! image/jpeg,width=640,height=480,framerate=30/1 ! jpegdec ! videoconvert ! video/x-raw,format=NV12 !  v4l2h265enc ! h265parse ! v4l2h265dec ! videoconvert ! waylandsink
    ```

**참고:** 명령어 끝에 fullscreen=true 옵션을 추가하면 전체 화면으로 영상을 재생할 수 있습니다.

GStreamer 외에 OpenCV를 사용하여 카메라 스트림을 표시할 수도 있습니다. 아래 단계를 따르면 OpenCV로 카메라 영상을 간편하게 미리 볼 수 있습니다.
1. OpenCV 설치
    ```
    $ sudo apt-get install python3-opencv
    ```
2. opencv_cam.py 파일 안에 다음 코드를 작성합니다
    ```
    import cv2

    cap = cv2.VideoCapture(1)

    if not cap.isOpened():
        print("\\@@ Camera open failed!")
        exit()

    print("카메라 창을 종료하려면 'q'를 누르십시오.")

    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

    while True:
        ret, frame = cap.read()
        if not ret:
            print("프레임 읽기에 실패했습니다")
            break

        cv2.imshow("Camera Feed", frame)

        # 'q' 키를 누르면 종료합니다
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
    ```
3. Python으로 opencv_cam.py를 실행합니다
    ```
    $ python3 opencv_cam.py
    ```

The USB camera used in this guide operates over USB 2.0, which imposes bandwidth limitations. As a result, higher-resolution video capture is not supported when using OpenCV. If higher resolutions are required, it is recommended to use a USB 3.0 camera, which provides sufficient bandwidth for high-definition video streams.  
Alternatively, OpenCV can be used with higher resolutions by constructing the capture pipeline through GStreamer, as shown below.
1. Write the following code inside the gstreamer_opencv_cam.py file
    ```
    import cv2

    pipeline = (
        "v4l2src device=/dev/video1 ! "
        "image/jpeg,width=1920,height=1080,framerate=30/1 ! "
        "jpegdec ! videoconvert ! video/x-raw,format=BGR ! "
        "appsink drop=1 max-buffers=2"
    )

    print("파이프라인을 여는 중입니다...")
    cap = cv2.VideoCapture(pipeline, cv2.CAP_GSTREAMER)

    if not cap.isOpened():
        print("파이프라인 열기에 실패했습니다")
        exit()

    print("카메라 창을 종료하려면 'q'를 누르십시오.")

    while True:
        ret, frame = cap.read()
        if not ret:
            print("프레임 읽기에 실패했습니다")
            break

        cv2.imshow("USB Camera 1080p MJPG", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
    ```
2. Run gstreamer_opencv_cam.py with Python
    ```
    $ python3 gstreamer_opencv_cam.py
    ```

# 6. 문제 해결
6장에서는 MIPI CSI 카메라, GMSL 카메라, USB 카메라의 문제 해결 방법을 다룹니다.

## 6.1 MIPI CSI 및 GMSL 카메라 문제 해결
MIPI CSI 또는 GMSL 카메라에서 문제가 발생하면 아래 디버깅 가이드를 참조하여 문제를 해결하십시오.

### 6.1.1 부팅 시 문제 (프로브 단계)
#### 6.1.1.1 센서 프로브 실패
**증상**
- 부팅 중에 센서가 감지되지 않음
- /dev/videoX 노드가 생성되지 않습니다
- ‘media-ctrl -p’ 출력에 센서 엔티티가 나타나지 않음  

**dmesg 로그 예시**
```
[    3.421000] imx219 2-0010: probing sensor failed
[    3.421120] imx219 2-0010: i2c read failed: addr=0x3000, ret=-5
[    3.200400] imx219 0-0010: reset gpio request failed
[    2.912830] imx219 1-0010: failed to get vddio regulator
```
**가능한 원인**
- 잘못된 I2C 주소 또는 버스 구성
- RESET/PWDN GPIO의 잘못된 극성
- 레귤레이터 전원 공급이 누락되었거나 잘못 구성됨

**해결 방법**
- 디바이스 트리에서 I2C 주소, 버스 번호, GPIO 설정을 확인하십시오
- 레귤레이터 노드가 누락되었거나 잘못 정의되었는지 확인하십시오
- 센서 모듈 케이블의 방향과 핀 정렬을 다시 확인하십시오

#### 6.1.1.2 I2C 통신 실패
**dmesg 로그 예시**
```
[    3.101001] imx219 2-0010: i2c read error: -121
[    4.112121] i2c i2c-2: transfer failed: -110
```
**가능한 원인**
- SDA/SCL 라인이 단락되었거나 연결이 끊어짐
- 디바이스 트리의 I2C 버스 번호가 실제 하드웨어 구성과 일치하지 않음

**해결 방법**
- “i2cdetect -y <bus>”를 사용하여 센서가 예상 I2C 주소에서 응답하는지 확인하십시오
- 케이블과 커넥터의 손상, 잘못된 삽입, 접점 헐거움 여부를 점검하십시오

### 6.1.2 미디어 컨트롤러 및 그래프 구성 문제
(‘media-ctl -p’를 사용하여 확인)

#### 6.1.2.1 센서 엔티티 누락 또는 링크 미구성
**'media-ctl -p' 출력 예시**
```
0 entities, 0 interfaces, 0 pads, 0 links
```
**가능한 원인**
- 디바이스 트리에 엔드포인트(port) 노드 누락
- 잘못된 레인 개수 또는 ‘bus-type’ 설정
- ‘link-frequencies’ 항목 누락

**해결 방법**
- ‘port@0/1’ 엔드포인트 정의가 올바른지 확인하십시오
- ‘data-lanes’ 배열의 순서와 레인 개수가 올바른지 확인하십시오
- ‘link-frequencies’가 센서 사양과 일치하는지 확인하십시오

#### 6.1.2.2 포맷 / 모드 불일치
**가능한 원인**
- 센서 드라이버의 ‘supported_mode[]’가 DTS에 정의된 ‘hs-settle’ 값과 일치하지 않음
- 드라이버와 디바이스 트리 간 CSI-2 레인 개수 불일치

**해결 방법**
- ‘supported_modes[]’의 해상도, 픽셀 레이트, HTS/VTS 값을 검토한 후 DTS의 ‘hs-settle’ 값을 그에 맞게 조정하십시오
- DTS 설정과 센서 드라이버 설정 간의 일관성을 확인하십시오

### 6.1.3 V4L2 스트리밍 문제
#### 6.1.3.1 VIDIOC_STREAMON 실패 (스트리밍을 시작할 수 없음)
**가능한 원인**
- 잘못된 센서 레지스터 구성
- 픽셀 레이트 또는 PLL 설정이 예상 값과 일치하지 않음
- 잘못된 프레임 타이밍을 유발하는 HTS/VTS 충돌

**해결 방법**
- 센서의 모드 테이블에서 픽셀 레이트, VTS, HTS 값을 다시 검증하십시오
- PLL 분주값(0x030x 레지스터)이 올바른지 확인하십시오
- 선택한 해상도와 FPS에 맞는 올바른 ‘hs-settle’ 값이 디바이스 트리에 지정되어 있는지 확인하십시오.

#### 6.1.3.2 지원되지 않는 포맷 요청
**해결 방법**
- 아래 명령을 사용하여 실제로 지원되는 포맷을 확인한 후, 지원되는 포맷으로 스트리밍을 다시 시도하십시오:
    ```
    V4l2-ctl –list-formats-ext
    ```

### 6.1.4 CSI-2 오류: SoT, CRC 및 관련 문제
#### 6.1.4.1 SoT (Sync on Transmission) 오류
**가능한 원인**
- MIPI 타이밍 설정 불일치
- 픽셀 레이트가 너무 높게 설정됨
- 케이블 품질 불량 또는 과도한 케이블 길이

**해결 방법**
- 픽셀 레이트 또는 링크 주파수를 낮추십시오
- 케이블을 교체하거나 길이를 줄이십시오
- MIPI 타이밍 파라미터를 확인하십시오

#### 6.1.4.2 CRC 오류
**dmesg 로그 예시**
```
[   13.700910] tccvin videoinput0: CSI-2 ERROR: CRC error
```
**가능한 원인**
- MIPI 신호 품질 저하
- PLL 또는 레인 속도 불일치

**해결 방법**
- hs-settle 값을 조정하십시오
- 케이블을 교체하십시오
- PLL 구성 및 레인 속도 설정을 확인하십시오

### 6.1.5 픽셀 레이트 / 링크 주파수 오류
**가능한 원인**
- 사용 가능한 CSI-2 레인 대역폭 초과
- 잘못된 PLL 구성

**해결 방법**
- 픽셀 레이트를 다시 계산하여 허용 가능한 CSI-2 대역폭 이내인지 확인하십시오
- 유효한 타이밍을 얻을 수 있도록 PLL 분주기를 조정하십시오
- 필요한 경우 프레임 레이트를 낮추거나(예: 30 -> 15fps) 해상도를 낮추십시오

### 6.1.6 디바이스 트리(DTS) 구성 오류
#### 6.1.6.1 호환되지 않는 compatible 문자열
**가능한 원인**
- DTS의 ‘compatible’ 값이 센서 드라이버에 정의된 ‘of_device_id’와 일치하지 않음
- 드라이버가 디바이스 노드를 인식하지 못하여 프로브가 실행되지 않음

**해결 방법**
- 센서 드라이버에 정의된 정확한 ‘compatible’ 문자열(예: “sony,imx219”)로 DTS를 업데이트하십시오
- 디바이스 트리를 다시 빌드하고 센서가 정상적으로 프로브되는지 확인하십시오

#### 6.1.6.2 엔드포인트 구성 문제
**가능한 원인**
- 센서 엔드포인트와 CSI 엔드포인트 간에 포트 번호 또는 ‘remote-endpoint’ 참조가 일치하지 않음
- ‘data-lanes’ 또는 버스 구성이 미디어 그래프 요구 사항을 충족하지 않음

**해결 방법**
- 양쪽의 포트 번호, ‘data-lanes’, ‘remote-endpoint’ 값이 일치하는지 확인하십시오
- ‘media-ctl -p’를 사용하여 미디어 링크가 올바르게 설정되었는지 확인하십시오

#### Link-Frequencies 속성 누락
**가능한 원인**
- 엔드포인트에 ‘link-frequencies’ 필드가 없어 MIPI 링크 속도를 계산할 수 없음
- 값의 형식(예: /bits/ 64)이 드라이버가 기대하는 형식과 일치하지 않음

**해결 방법**
- 센서 사양에 따라 올바른 ‘link-frequencies’ 값(예: 456000000)을 추가하십시오
- 값 형식이 드라이버 요구 사항과 일치하는지 확인하십시오 (필요한 경우 /bits/ 64 포함 등)

### 6.1.7 Gstreamer 재생 문제
#### 6.1.7.1 'not negotiated' 오류
**가능한 원인**
- 파이프라인 내에서 Caps 협상 실패
- Wayland 컴포지터 포맷 불일치
- videoconvert가 특정 raw 포맷을 처리하지 못함

**해결 방법**
- 폭넓은 호환성을 제공하는 NV12 또는 YUY2 기반 파이프라인을 사용하십시오
- ‘v4l2src io-mode=dmabuf’를 활용하여 제로 카피 버퍼 처리와 올바른 포맷 협상을 보장하십시오

#### 6.1.7.2 Wayland 싱크 초기화 실패
**가능한 원인**
- Wayland 컴포지터가 실행되고 있지 않거나 접근 가능한 디스플레이 환경이 없음
- 파이프라인이 SSH를 통해 실행되거나 잘못된 DISPLAY/Wayland 환경에서 실행되어 싱크 초기화가 불가능함

**해결 방법**
- Weston 컴포지터가 실행 중인지 확인하십시오
- 로컬 세션 또는 올바르게 구성된 Wayland 환경에서 파이프라인을 실행하십시오

### 6.1.8 하드웨어 문제
#### 6.1.8.1 잘못된 케이블 방향
**가능한 원인**
- FFC 케이블이 잘못된 방향으로 연결되었거나 핀이 어긋나 I2C/MIPI 신호가 정상적으로 전송되지 않음
- 센서가 전혀 응답하지 않아 프레임이 수신되지 않음

**해결 방법**
- 커넥터 방향을 확인하고 접점 핀이 사양에 따라 정렬되어 있는지 확인하십시오
- 케이블 손상 또는 접점 마모 여부를 확인하십시오

#### 6.1.8.2 전원 공급 문제
**가능한 원인**
- 센서 전압 레일(예: 1.2V / 2.8V)이 불안정하거나 활성화되지 않음
- 전원 활성화 GPIO가 어서트되지 않음
- 초기화 중에 센서의 파워업 시퀀스가 충족되지 않음

**해결 방법**
- DTS의 레귤레이터 및 GPIO 설정을 검토하고 필요한 모든 전압이 올바르게 공급되는지 확인하십시오
- 센서의 전원 시퀀스 요구 사항이 충족되는지 확인하십시오 (RESET _> PWDN -> clock enable)

## 6.2 USB 카메라 문제 해결
USB Camera에서 문제가 발생하면 아래 디버깅 가이드를 참조하여 문제를 해결하십시오.

### 6.2.1 카메라가 감지되지 않음 (USB 장치가 인식되지 않음)
**dmesg 로그 예시**
```
usb 1-1: device descriptor read/64, error -71
uvcvideo: Failed to initialize the device
```
**가능한 원인**
- USB 전원 부족 또는 불안정한 전원 공급으로 인한 디바이스 초기화 실패
- 불량 USB 케이블 또는 포트, 혹은 호환되지 않는 USB 허브 사용

**해결 방법**
- 다른 USB 포트를 사용하거나 안정적인 전원을 공급하는 포트를 사용하십시오
- USB 케이블 또는 허브를 교체하고 디바이스를 다시 연결하여 정상적으로 열거되는지 확인하십시오

### 6.2.2 v4l2-ctl에서 포맷 목록이 제한되거나 비어 있음
**dmesg 로그 예시**
```
uvcvideo: Failed to query (GET_DEF) UVC control 2 on unit 1: -32
```
**가능한 원인**
- 카메라가 특정 UVC 컨트롤을 지원하지 않거나 초기화 중에 이를 보고하지 못함
- 디바이스와 드라이버 간 프로토콜 오류로 인해 기능 감지가 불가능함

**해결 방법**
- MJPEG 또는 YUYV와 같은 표준 포맷으로 테스트하십시오
- 동일한 모델의 다른 카메라로 테스트하여 UVC 호환성 관련 문제인지 확인하십시오

### 6.2.3 GStreamer 재생: "not negotiated" 또는 Caps 불일치
**가능한 원인**
- 파이프라인이 카메라에서 지원하지 않는 포맷(예: NV12, YUY2)을 요청하여 caps 협상에 실패함
- 선택한 해상도/프레임 레이트에서 카메라가 MJPEG만 제공하지만, 파이프라인은 raw 포맷을 요청할 수 있습니다
- 카메라가 MJPEG를 출력하지만 JPEG 디코더 엘리먼트(jpegdec 또는 avdec_mjpeg)가 포함되지 않아 디코딩을 진행할 수 없음

**해결 방법**
- 지원되는 포맷을 확인하십시오
    ```
    v4l2-ctl –list-formats-ext
    ```
- 카메라가 MJPEG를 출력하는 경우:
    ```
    v4l2src ! image/jpeg ! jpegdec ! videoconvert ! …
    ```
- 카메라가 raw 포맷(예: YUYV)을 지원하는 경우 파이프라인 caps를 그에 맞게 구성하십시오:  
    ‘v4l2-ctl –list-formats-ext’에 표시된 raw 포맷을 그대로 정확히 사용하십시오

### 6.2.4 해상도 또는 FPS 설정 실패
**가능한 원인**
- 요청한 해상도 또는 프레임 레이트를 카메라가 지원하지 않아 협상에 실패함

**해결 방법**
- ‘v4l2-ctl –list-formats-ext’를 사용하여 지원되는 해상도/FPS 조합을 확인하십시오

### 6.2.5 영상 끊김 / 프레임 드롭
**가능한 원인**
- USB 대역폭 부족(허브 공유 또는 USB 2.0 포트 사용)
- MJPEG 디코딩으로 인한 높은 CPU 부하로 파이프라인이 지연됨

**해결 방법**
- USB 3.0 포트를 사용하거나 허브 없이 카메라를 직접 연결하십시오
- MJPEG 해상도 또는 프레임 레이트를 낮추거나, 지원되는 경우 raw 포맷으로 전환하십시오

### 6.2.6 색상 이상 또는 출력 손상
**가능한 원인**
- MJPEG -> NV12 변환 또는 색 공간 변환 중 오류 발생
- v4l2convert 또는 videoconvert에서 특정 포맷 조합이 실패할 수 있습니다

**해결 방법**
- videoconvert 앞에 jpegdec 또는 avdec_mjpeg를 명시적으로 삽입하십시오
- 테스트를 위해 파이프라인을 단순화하십시오. 예:
    ```
    V4l2src ! jpegdec ! videoconvert ! waylandsink
    ```

### 6.2.7 예기치 않은 장치 연결 해제 또는 재열거
**dmesg 로그 예시**
```
usb 1-1: USB disconnect, device number 4
```
**가능한 원인**
- 불안정한 전원 공급 또는 불량한 케이블 접촉
- 장시간 사용 중 발열 문제로 디바이스가 리셋됨

**해결 방법**
- USB 케이블을 교체하거나 안정적이고 충분한 전원을 공급하는 포트를 사용하십시오
- 발열이 심한 카메라의 경우 추가적인 냉각 방안을 고려하십시오
