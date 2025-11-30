# MIPI拡張ボード
----

MIPI拡張ボードは、GMSL2高速シリアル通信を利用して、MIPI CSIおよびMIPI DSIインターフェースをサポートします（図1）。各ボードには、カメラ入力とディスプレイ出力を処理するためのシリアライザおよびデシリアライザチップセットが統合されており、信頼性の高い高解像度データ転送を保証します。
**注:** コンポーネントの入手可能性と構成は、特定のプロジェクト要件に応じて受注生産ベースで提供されます。

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/accessories/mipi_expansion_board_crop.png" width="350"></p>
<p align="center"><strong>図 1. MIPI拡張ボード</strong></p><br/>

## MIPI CSI (カメラシリアルインターフェース)

### ボード情報
- **サイズ**: 71.5 mm × 73.5 mm × 1.6 t / 4層
- **デシリアライザ**: MAX96712 (ADI)
- **GMSLバージョン**: GMSL2
- **リンク数**: 最大4チャンネルのMIPI CSI2入力
- **解像度 / 帯域幅**: 最大1.5 Gbps × 4レーン × 4チャンネル
- **電源**: 1.8V / 3.3V
- **パッケージ**: 64 QFN / 9 mm × 9 mm
- **制御インターフェース**: I²C
- **B2Bコネクタ**: 61083-043402LF (Amphenol)


## MIPI DSI (ディスプレイシリアルインターフェース)

### ボード情報
- **サイズ**: 60 mm × 30 mm × 1.6 t / 4層
- **シリアライザ**: MAX96789 (ADI)
- **GMSLバージョン**: GMSL2
- **リンク数**: 最大4チャンネルのMIPI DSI2出力
- **解像度 / 帯域幅**: 最大6 Gbps
- **電源**: 1.8V / 3.3V
- **パッケージ**: 56 QFN / 8 mm × 8 mm
- **制御インターフェース**: I²C
- **B2Bコネクタ**: 10132797-067110LF (Amphenol)