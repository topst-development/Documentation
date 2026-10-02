# AI-G 릴리스 노트 - v1.2.0

## 업데이트된 저장소

- [tc-nn-app](https://github.com/topst-development/tc-nn-app)
- [libtc-ndnpu](https://github.com/topst-development/libtc-ndnpu)
- [tc-compiled-nn](https://github.com/topst-development/tc-compiled-nn)
- [meta-topst](https://github.com/topst-development/meta-topst)

## 새로운 기능

- `tcnnapp`의 기본 객체 검출 모델과 `tcnputestapp`의 기본 테스트 모델을 YOLOv5s에서 YOLOv8s로 변경했습니다.

## 개선 사항

- 애플리케이션의 메모리 정리, 입출력 범위 검사, 초기화 오류 안내를 개선했습니다.
- MobileNetV2 모델 바이너리와 메타데이터를 업데이트했습니다.
- Windows 펌웨어 다운로드 스크립트의 COM 포트 조회를 WMIC에서 PowerShell 방식으로 변경했습니다.
- `tc-nn-camera-app`의 기본 카메라 입력 경로를 `/dev/video0`에서 `/dev/video2`로 변경했습니다.

## 사용 시 참고 사항

- 기본 모델 경로는 `/usr/share/yolov8s_quantized/`입니다. `tcnnapp`의 두 번째 기본 모델 경로는 `/usr/share/mobilenetv2_10_quantized/`입니다.
- 내장된 YOLOv8s 모델에는 `sample/input.ia.bin`이 포함되어 있지 않습니다. 이 파일이 없으면 `tcnputestapp`은 0으로 채운 입력을 사용하며 `Input file not found. Using zero padding.`을 출력합니다. 이 테스트는 NPU 실행과 성능을 확인하며 모델 정확도를 평가하지 않습니다.
- 배포 펌웨어 패키지에는 Windows용 `fwdn_ai.bat`과 Linux용 `fwdn_ai.sh`가 포함됩니다.

## 펌웨어

- [AIG-TOPST-Yocto-image-v1.2.0-r01](https://topst-downloads.s3.ap-northeast-2.amazonaws.com/Yocto/v1.2.0/aig-yp4-v1.2.0-r01.zip)
