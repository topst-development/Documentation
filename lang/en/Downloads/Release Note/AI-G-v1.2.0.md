# AI-G Release Note - v1.2.0

## Updated repositories

- [tc-nn-app](https://github.com/topst-development/tc-nn-app)
- [libtc-ndnpu](https://github.com/topst-development/libtc-ndnpu)
- [tc-compiled-nn](https://github.com/topst-development/tc-compiled-nn)
- [meta-topst](https://github.com/topst-development/meta-topst)

## New Features

- Changed the default object detection model in `tcnnapp` and the default test model in `tcnputestapp` from YOLOv5s to YOLOv8s.

## Improvement

- Improved application memory cleanup, input/output range checks, and initialization error reporting.
- Updated the MobileNetV2 model binaries and metadata.
- Replaced WMIC with PowerShell for COM port detection in the Windows firmware download script.
- Corrected the default camera input path shown in `tc-nn-camera-app` help to match the actual default, `/dev/video2`.

## Usage Notes

- The default model directory is `/usr/share/yolov8s_quantized/`. The second default model in `tcnnapp` is `/usr/share/mobilenetv2_10_quantized/`.
- The bundled YOLOv8s model does not include `sample/input.ia.bin`. When this file is missing, `tcnputestapp` uses zero-filled input and prints `Input file not found. Using zero padding.` This tests NPU execution and performance; it does not evaluate model accuracy.
- The prebuilt firmware package provides `fwdn_ai.bat` for Windows and `fwdn_ai.sh` for Linux.

## Firmware

- [AIG-TOPST-Yocto-image-v1.2.0-r01](https://topst-downloads.s3.ap-northeast-2.amazonaws.com/Yocto/v1.2.0/aig-yp4-v1.2.0-r01.zip)
