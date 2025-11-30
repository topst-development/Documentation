# MIPI 확장 보드
----

MIPI 확장 보드는 GMSL2 고속 직렬 통신을 활용하여 MIPI CSI 및 MIPI DSI 인터페이스를 지원합니다(그림 1). 각 보드는 카메라 입력 및 디스플레이 출력을 처리하기 위해 직렬화기(Serializer) 및 역직렬화기(Deserializer) 칩셋을 통합하여 안정적인 고해상도 데이터 전송을 보장합니다. 
**참고:** 구성 요소 가용성 및 구성은 특정 프로젝트 요구 사항에 따라 주문 제작 방식으로 제공됩니다.

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/accessories/mipi_expansion_board_crop.png" width="350"></p>
<p align="center"><strong>그림 1. MIPI 확장 보드</strong></p><br/>

## MIPI CSI (카메라 직렬 인터페이스)

### 보드 정보
- **크기**: 71.5 mm × 73.5 mm × 1.6 t / 4 Layer
- **역직렬화기(Deserializer)**: MAX96712 (ADI)
- **GMSL 버전**: GMSL2
- **링크 수량**: 최대 4채널 MIPI CSI2 입력
- **해상도 / 대역폭**: 최대 1.5 Gbps × 4-lanes × 4 channels
- **전원 공급**: 1.8V / 3.3V
- **패키지**: 64 QFN / 9 mm × 9 mm
- **제어 인터페이스**: I²C
- **B2B 커넥터**: 61083-043402LF (Amphenol)


## MIPI DSI (디스플레이 직렬 인터페이스)

### 보드 정보
- **크기**: 60 mm × 30 mm × 1.6 t / 4 Layer
- **직렬화기(Serializer)**: MAX96789 (ADI)
- **GMSL 버전**: GMSL2
- **링크 수량**: 최대 4채널 MIPI DSI2 출력
- **해상도 / 대역폭**: 최대 6 Gbps
- **전원 공급**: 1.8V / 3.3V
- **패키지**: 56 QFN / 8 mm × 8 mm
- **제어 인터페이스**: I²C
- **B2B 커넥터**: 10132797-067110LF (Amphenol)