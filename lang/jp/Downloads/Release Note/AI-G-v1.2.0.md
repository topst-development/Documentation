# AI-G リリースノート - v1.2.0

## 更新されたリポジトリ

- [tc-nn-app](https://github.com/topst-development/tc-nn-app)
- [libtc-ndnpu](https://github.com/topst-development/libtc-ndnpu)
- [tc-compiled-nn](https://github.com/topst-development/tc-compiled-nn)
- [meta-topst](https://github.com/topst-development/meta-topst)

## 新機能

- `tcnnapp`のデフォルトの物体検出モデルと`tcnputestapp`のデフォルトのテストモデルを、YOLOv5sからYOLOv8sに変更しました。

## 改善

- アプリケーションのメモリ解放、入出力範囲の検証、初期化エラーの通知を改善しました。
- MobileNetV2のモデルバイナリとメタデータを更新しました。
- Windows用ファームウェア書き込みスクリプトのCOMポート検出を、WMICからPowerShellに変更しました。
- `tc-nn-camera-app`のデフォルトのカメラ入力パスを、`/dev/video0`から`/dev/video2`に変更しました。

## 使用上の注意

- デフォルトのモデルディレクトリは`/usr/share/yolov8s_quantized/`です。`tcnnapp`の2番目のデフォルトモデルは`/usr/share/mobilenetv2_10_quantized/`です。
- 同梱のYOLOv8sモデルには`sample/input.ia.bin`が含まれていません。このファイルがない場合、`tcnputestapp`はゼロで埋めた入力を使用し、`Input file not found. Using zero padding.`と表示します。このテストはNPUの実行と性能を確認するもので、モデルの精度を評価するものではありません。
- 配布ファームウェアパッケージには、Windows用の`fwdn_ai.bat`とLinux用の`fwdn_ai.sh`が含まれています。

## ファームウェア

- [AIG-TOPST-Yocto-image-v1.2.0-r01](https://topst-downloads.s3.ap-northeast-2.amazonaws.com/Yocto/v1.2.0/aig-yp4-v1.2.0-r01.zip)
