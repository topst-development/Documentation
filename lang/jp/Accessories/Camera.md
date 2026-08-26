## 対応カメラモジュール
<div align="center">
    <table>
        <tr>
            <td colspan="8" align="center"><strong>ボード</strong></td>
            <td align="center"><strong>モデル</strong></td>
            <td align="center"><strong>センサー</strong></td>
            <td align="center"><strong>センサー解像度</strong></td>
            <td align="center"><strong>デフォルト解像度</strong></td>
            <td align="center"><strong>フレームレート</strong></td>
            <td align="center"><strong>デフォルトビデオパス</strong></td>
            <td align="center"><strong>備考</strong></td>
        </tr>
        <tr>
            <td rowspan="4" align="center"><strong>D3-G</strong></td>
            <td colspan="8">Arducam OV5647</td>
            <td>OV5647</td>
            <td>2592x1944 ピクセル(5MP)</td>
            <td>1296x972</td>
            <td>30FPS</td>
            <td>/dev/video0</td>
            <td>デフォルトで選択されるカメラ</td>
        </tr>
        <tr>
            <td colspan="8">Raspberry Pi Camera v1</td>
            <td>OV5647</td>
            <td>2592x1944 ピクセル(5MP)</td>
            <td>1296x972</td>
            <td>30FPS</td>
            <td>/dev/video0</td>
            <td>デフォルトで選択されるカメラ</td>
        </tr>
        <tr>
            <td colspan="8">Raspberry Pi Camera v2</td>
            <td>IMX219</td>
            <td>3280x2464 ピクセル(8MP)</td>
            <td>1640x1232</td>
            <td>30FPS</td>
            <td>/dev/video0</td>
            <td>デフォルトでは無効です。有効にするには以下のガイドを参照してください。</td>
        </tr>
        <tr>
            <td colspan="8">SEKONIX CXD5700</td>
            <td>CXD5700</td>
            <td>1920x1080 ピクセル(2MP)</td>
            <td>1920x1080</td>
            <td>30FPS</td>
            <td>/dev/video0,1,2,3</td>
            <td>デフォルトでは無効です。有効にするには以下のガイドを参照してください。</td>
        </tr>
        <tr>
            <td rowspan="4" align="center"><strong>AI-G</strong></td>
            <td colspan="8">Arducam OV5647</td>
            <td>OV5647</td>
            <td>2592x1944 ピクセル(5MP)</td>
            <td>1296x972</td>
            <td>30FPS</td>
            <td>/dev/video2</td>
            <td>デフォルトで選択されるカメラ</td>
        </tr>
        <tr>
            <td colspan="8">Raspberry Pi Camera v1</td>
            <td>OV5647</td>
            <td>2592x1944 ピクセル(5MP)</td>
            <td>1296x972</td>
            <td>30FPS</td>
            <td>/dev/video2</td>
            <td>デフォルトで選択されるカメラ</td>
        </tr>
        <tr>
            <td colspan="8">Raspberry Pi Camera v2</td>
            <td>IMX219</td>
            <td>3280x2464 ピクセル(8MP)</td>
            <td>1640x1232</td>
            <td>30FPS</td>
            <td>/dev/video2</td>
            <td>デフォルトでは無効です。有効にするには以下のガイドを参照してください。</td>
        </tr>
        <tr>
            <td colspan="8">SEKONIX CXD5700</td>
            <td>CXD5700</td>
            <td>1920x1080 ピクセル(2MP)</td>
            <td>1920x1080</td>
            <td>30FPS</td>
            <td>/dev/video0,1,2</td>
            <td>デフォルトでは無効です。有効にするには以下のガイドを参照してください。</td>
        </tr>
    </table>
</div>

# 1. はじめに
本ガイドは、エンジニアが TOPST D3-G および AI-G プラットフォームでカメラ入力を迅速に立ち上げ、AI ビジョンワークロードの予備検証を素早く実施できるよう支援することを目的としています。ハードウェア接続、デバイスツリー構成、ドライバ、パイプライン準備を含む初期セットアップの複雑さを軽減し、電源投入から最初のビデオフレーム、さらには最初の推論に至るまでの明確で再現可能な手順を提供します。

## 1.1 適用範囲
- **対応インタフェース:** MIPI CSI-2、GMSL (SerDes ベース)、USB UVC
- **ソフトウェアコンポーネント:** Yocto ベースの BSP 構成、デバイスツリーオーバーレイ、V4L2、GStreamer、OpenCV、および D3-G・AI-G SDK との連携
- **適用ユースケース:** ロボティクス、ドローン、ならびに検査、安全監視、物体追跡などの産業オートメーション用途
- **対象外の項目:** カメラ ISP チューニング、高度なキャリブレーションワークフロー(ステレオ/IMU)、および完全なエンドツーエンドのアプリケーションフレームワーク

## 1.2 対象読者
- PoC またはパイロット開発のために D3-G または AI-G プラットフォームへカメラを統合する組込みおよび AI エンジニア
- マルチカメラパイプラインに依存するシステムを導入または検証するシステムインテグレーター
- 教育や実験のために再現可能な実習環境を必要とする教育関係者および研究室の利用者

## 1.3 本ガイドの構成
- **ハードウェア接続:** コネクタのピン配置、レーン構成、電源およびグランド要件、ケーブル取り扱い指針、参考配線図
- **ソフトウェア構成:** ドライバおよびデバイスツリー構成を含む BSP セットアップと、udev および V4L2 によるデバイス確認方法
- **パイプラインと例:** シングルカメラおよびマルチカメラのプレビューとキャプチャのための GStreamer・OpenCV のコマンドとスクリプト
- **トラブルシューティング:** よくある問題、代表的な dmesg のパターン、I²C プローブのヒント、タイミング関連の問題、性能検証の方法

## 1.4 前提条件
- **ハードウェア:** TOPST D3-G または AI-G ボード、対応カメラモジュール、および必要なケーブル/アダプタ(MIPI FPC、GMSL 用同軸ケーブル、USB 3.0 など)
- **ホストツール:** シリアルコンソールへのアクセス、SSH クライアント、基本的なビルド/デバッグユーティリティ
- **技術的な前提知識:** Linux シェル操作、V4L2 ユーティリティ、および基本的なデバイスツリーの概念への習熟
- **イメージ/SDK:** D3-G、AI-G BSP イメージ(d3-g バージョン ≥ v1.3.0、ai-g バージョン ≥1.1.0)
  

# 2. カメラインタフェース概要
第 2 章では、D3-G および AI-G ボードでそれぞれ対応するカメラの種類について説明します。  
表 2.1 に D3-G および AI-G プラットフォームのボードサポートマトリクスを示します。

<p align="center"><strong>表 2.1 ボードサポートマトリクス</strong></p>
<div align="center">
    <table>
        <tr>
            <td colspan="3" align="center"><strong>項目</strong></td>
            <td align="center"><strong>D3-G</strong></td>
            <td align="center"><strong>AI-G</strong></td>
        </tr>
        <tr>
            <td colspan="3">OS サポート</td>
            <td>Yocto, Ubuntu(desktop)</td>
            <td>Yocto, Ubuntu(Headless)</td>
        </tr>
        <tr>
            <td colspan="3">MIPI CSI-2</td>
            <td>2-4 レーン、2.1 Gbps/レーン x2</td>
            <td>2-4 レーン、1.5 Gbps/レーン x1</td>
        </tr>
        <tr>
            <td colspan="3">GMSL (SerDes)</td>
            <td>TOPST 4ch SerDes キャリア</td>
            <td>TOPST 4ch SerDes キャリア</td>
        </tr>
        <tr>
            <td colspan="3">USB (UVC)</td>
            <td>USB2.0/USB3.0 </td>
            <td>非対応</td>
        </tr>
    </table>
</div>

## 2.1 MIPI カメラ概要
MIPI カメラは、**MIPI CSI-2 (Mobile Industry Processor Interface – Camera Serial Interface 2)** 規格を介してプロセッサに直接接続されるイメージセンサーベースのカメラモジュールです。スマートフォン、組込みボード、AI ベースのカメラシステムで最も広く使用されているカメラインタフェースであり、低消費電力、高帯域幅、低遅延といった利点があります。  
MIPI CSI-2 カメラは通常、RAW Bayer のセンサー出力をシステムへ直接供給し、画像信号処理 (ISP) は SoC 内部の ISP または外部 ISP のいずれかで行われます。USB カメラとは異なり、MIPI センサーは I2C レジスタ設定による初期化と ISP パイプラインのセットアップが必要ですが、その代わりにセンサーの性能を最大限に活かした高品質な画像処理が可能になります。  
MIPI カメラが組込みプラットフォームで広く使用されている理由は次のとおりです。
- **高帯域幅:** 2 レーンまたは 4 レーン構成により、MIPI カメラは高解像度 (4K 以上) かつ高フレームレートのデータを安定して伝送できます。
- **低消費電力:** モバイルおよび組込み機器向けに設計されており、消費電力は他の方式に比べて大幅に低くなります。
- **センサーの直接制御:** 露出、ゲイン、フレームレートなどのセンサーパラメータを I2C 経由で制御でき、画質の細かな調整が可能です。
- **低遅延:** RAW データが直接伝送されるため、MIPI カメラはロボティクスや組込みビジョンシステムなどのリアルタイム用途に適しています。
- **豊富なセンサーの選択肢:** Sony IMX シリーズ (IMX219、IMX708 など) や Omnivision OV シリーズを含む多数のセンサーを同一の CSI-2 規格で使用できます。  

MIPI カメラは **15 ピン (2 レーン)** または **20 ピン (4 レーン)** の FFC ケーブルなどのコネクタを使用し、レーン構成とピンマッピングはボードの CSI ポートと一致している必要があります。  
Linux ベースのシステムでは、カメラが /dev/video* デバイスまたは Media Controller ノードとして認識されるよう、センサードライバ (デバイスツリー構成を含む) を正しく設定する必要があります。認識された後は、V4L2 フレームワークを通じてビデオストリーミングを利用できます。  
これらの特性により、MIPI カメラは高品質な画像処理、低遅延ストリーミング、AI を活用した組込みビジョンアプリケーションにおける事実上の標準インタフェースとなっています。

## 2.2 GMSL カメラ概要
GMSL カメラは、Gigabit Multimedia Serial Link (GMSL) 規格を用いて、画像データ、制御信号、電源を 1 本の同軸ケーブルまたはシールド付きツイストペアケーブルで伝送するシリアル化カメラモジュールです。短い FFC 接続を必要とする MIPI カメラとは異なり、GMSL はシリアライザ–デシリアライザ (SerDes) のペアを使用して CSI-2 画像データを数メートルにわたって伝送し、長距離かつノイズに強いカメラ接続を実現します。  

GMSL システムは、組込みおよび車載環境において次のような利点を提供します。
- **長距離伝送:** 最長約 15 m のケーブルでも安定した映像伝送に対応し、ロボティクスや車両へのセンサー配置に適しています。
- **高帯域幅:** GMSL1/2/3 はマルチギガビットの CSI-2 ストリームを伝送でき、高解像度またはマルチカメラ構成を実現します。
- **Power over Coax (PoC):** 1 本のケーブルで電源とデータを供給できるため、コネクタ数を削減しシステム配線を簡素化します。
- **堅牢性と EMI 耐性:** 同軸ケーブルと差動信号方式により、GMSL は電気的ノイズの多い環境でも安定して動作します。
- **標準的なセンサー制御:** デシリアライザが I2C 通信をセンサーへ転送するため、一般的な露出、ゲイン、フレームレートの設定が可能です。

一般的な GMSL カメラの経路は、シリアライザを備えたイメージセンサー、同軸ケーブル、デシリアライザ、そして最終的に SoC への CSI-2 出力で構成されます。Linux では、SerDes とセンサーがデバイスツリーに正しく記述されていれば、カメラは V4L2 または Media Controller デバイスとして認識されます。これは標準的な MIPI カメラとほぼ同様ですが、配置やシステム設計の面ではるかに高い柔軟性を備えています

## 2.3 USB カメラの概要
USB カメラは、USB 2.0 または USB 3.0 インターフェースを介してシステムに接続されるデジタルイメージングデバイスです。最大の利点は、標準の UVC (USB Video Class) プロトコルに準拠しているため、専用のドライバを必要とせずに動作することです。Linux、Windows、macOS など、ほとんどのオペレーティングシステムが UVC を標準でサポートしているため、ユーザーはカメラを接続した直後に、追加の設定なしでビデオストリームを取得できます。
  
USB カメラは、次の理由から組み込みプラットフォームで広く使用されています。
- **プラグアンドプレイ機能:** MIPI センサーとは異なり、USB カメラはセンサーの初期化、I2C レジスタの設定、ISP パイプラインの構成を必要とせず、接続すると同時に映像をキャプチャできます。
- **高い互換性:** ほとんどの USB カメラは UVC 仕様に準拠しているため、メーカーやモデルに関係なく一貫した方法で動作します。
- **豊富な解像度とフォーマットのサポート:** MJPEG、YUYV、NV12 などの一般的なフォーマットを幅広く利用できます。
- **接続と配線の容易さ:** USB ケーブルにより配線を簡素化でき、多くの場合数メートルに及ぶ長距離をサポートします。
- **組み込み開発に最適:** ドライバ関連の問題が少なく、より迅速なプロトタイピングが可能です。

Linux ベースのシステムでは、USB カメラは自動的に検出され、/dev/video* ノードとして公開されます。映像のキャプチャと制御は、v4l2-ctl、ffmpeg、GStreamer などの標準ツールを使用して実行できます。  
多くの USB カメラには ISP が内蔵されており、オートホワイトバランス、自動露出、色補正などの画像処理を内部で行います。これにより、外部 ISP を搭載していないボードでも安定した画質が得られます。こうした特性から、USB カメラはテスト、組み込み Linux 開発、ロボティクス、迅速なプロトタイピングといった分野で最もシンプルかつ汎用性の高いカメラソリューションの一つとなっています。

## 2.4 D3-G で使用可能なカメラの種類
TOPST D3-G プラットフォームは、Yocto と Ubuntu の両方の環境で同一のカメラ種別をサポートします。利用可能なカメラインターフェースには USB、MIPI、GMSL があり、使用するインターフェースによって設定が若干異なります。  
1. **MIPI カメラ**  
TOPST D3-G は 2 つの MIPI CSI ポートを備えており、ポートごとに 1 台の MIPI カメラを接続できます。MIPI CSI インターフェースは 2 種類のコネクタ形式をサポートします。
    - **15-pin(2-Lane):** OV5647 や IMX219 など、低帯域幅のセンサーに適しています。
    - **20-pin (4-Lane):** 高解像度または高フレームレートのセンサーを対象としています。
2. **GMSL カメラ**  
GMSL カメラは長距離伝送に対応しており、車載用途や産業用途で一般的に使用されます。TOPST D3-G で GMSL を使用するには、次の構成要素が必要です。
    1. **20-pin MIPI CSI (4-Lane)** ポートを **TOPST MIPI Gender Board** に接続します。
    2. **Deserializer (Des)** ボードを Gender Board に取り付けます。
    3. Fakra ケーブルを使用して、最大 4 台の GMSL カメラを Des ボードに接続します。
3. **USB カメラ**  
USB カメラは最も簡単に使い始められる方法です。ボード上のいずれかの USB 2.0 または USB 3.0 ポートに接続すると自動的に認識され、追加の設定なしで使用できます。  
デバイスが V4L2 対応の UVC カメラである場合は、次のコマンドを使用して検出状況を確認できます。  
    ``` 
    v4l2-ctl --list-devices
    ```

## 2.4 D3-G で使用可能なカメラの種類
TOPST AI-G プラットフォームも複数のカメラ入力インターフェースをサポートしますが、全体的な構成は D3-G より簡素で、高性能な AI ワークロードに最適化されています。特に、このプラットフォームでは USB カメラはサポートされません。MIPI、GMSL 入力のみが利用可能です。  
1. **MIPI カメラ**  
TOPST D3-G は 2 つの MIPI CSI ポートを備えており、ポートごとに 1 台の MIPI カメラを接続できます。MIPI CSI インターフェースは 2 種類のコネクタ形式をサポートします。
    - **15-pin(2-Lane):** OV5647 や IMX219 など、低帯域幅のセンサーに適しています。
    - **20-pin (4-Lane):** 高解像度または高フレームレートのセンサーを対象としています。
2. **GMSL カメラ**  
GMSL カメラは長距離伝送に対応しており、車載用途や産業用途で一般的に使用されます。TOPST D3-G で GMSL を使用するには、次の構成要素が必要です。
    1. **20-pin MIPI CSI (4-Lane)** ポートを **TOPST MIPI Gender Board** に接続します。
    2. **Deserializer (Des)** ボードを Gender Board に取り付けます。
    3. Fakra ケーブルを使用して、最大 4 台の GMSL カメラを Des ボードに接続します。

# 3. カメラ接続ガイド
第 3 章では、D3-G および AI-G ボードにカメラを接続する方法について説明します。  
本節では、カメラが確実に動作するように、ボードとカメラが正しく接続されていることを確認します。使用するカメラを接続するには、以下のガイドに従ってください。

## 3.1 D3-G へのカメラの接続
MIPI CSI-2、GMSL、USB カメラを D3-G に接続する方法については、以下のガイドに従ってください。  

### 3.1.1 MIPI CSI-2 カメラ
図 3.1 は D3-G の MIPI CSI コネクタを示しています。D3-G は 2 チャンネルの MIPI CSI をサポートし、各チャンネルは 2-lane インターフェースで構成されます。4-lane インターフェースはオプションであり、15-pin コネクタではなく 20-pin コネクタが必要です。ピンに関する情報は、D3-G Hardware-User Guide を参照してください。

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/accessories/Camera/3.1%20MIPI%20CSI%20Connector%20on%20D3-G.png"></p>
<p align="center"><strong>図 3.1 D3-G の MIPI CSI コネクタ</strong></p>

MIPI カメラを接続する際は、FFC (Flat Flexible Cable) を使用してください。正しいケーブルの種類と向きについては、図 3.2 および 3.3 を参照してください。

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/accessories/Camera/3.2%20FFC%20Type.png"></p>
<p align="center"><strong>図 3.2 FFC の種類</strong></p>

FFC ケーブルは 1.0 mm、15-pin タイプで、片面に異なる色のマーキング (青またはグレー) が必要です。ケーブルは B-Forward Direction の向きで挿入してください。FFC の種類については図 3.2 を参照してください。

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/accessories/Camera/3.3%20An%20example%20of%20an%20FFC%20connected%20to%20the%20D3-G%20MIPI0%2015-pin%20Connector.png"></p>
<p align="center"><strong>図 3.3 D3-G MIPI0 15-pin コネクタに FFC を接続した例</strong></p>

FFC 上の 15 個の銀色の接点が、D3-G MIPI コネクタ内部の 15 個の銀色の接点と位置が合っていることを確認してください。  
MIPI1 コネクタを使用する場合も同じ接続方法が適用されます。MIPI0 コネクタと同じ方法で接続してください。

### 3.1.2 GMSL カメラ
GMSL カメラは Fakra ケーブルを使用します。そのため、D3-G ボードに直接接続することはできません。代わりに、Deserializer (Des) ボードと TOPST MIPI Gender Board を介して D3-G と接続する必要があります。  
接続構成は次のとおりです。  

<p align="center"><strong>< D3-G > ↔ < TOPST MIPI Gender Board > ↔ < Des Board > ↔ < GMSL Camera ></strong></p>

GMSL カメラを使用するには TOPST MIPI Gender Board が必要であり、20-pin MIPI コネクタを介して接続する必要があります。たとえば 4 台の GMSL カメラを使用する場合は、図 3.4 に示すように 20-pin MIPI インターフェースを使用して接続する必要があります。

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/accessories/Camera/3.4%2020-pin%20MIPI0%20Connector.png"></p>
<p align="center"><strong>図 3.4 20-pin MIPI0 コネクタ</strong></p>  

1. D3-G ボードと TOPST MIPI Gender Board の接続。  
    FFC ケーブルは 1.0 mm、20-pin タイプで、片面に異なる色のマーキング (青またはグレー) が必要です。ケーブルは A-Forward Direction の向きで挿入してください。FFC の種類については図 3.5 を参照してください。  
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/accessories/Camera/3.2%20FFC%20Type.png"></p>
    <p align="center"><strong>図 3.5 FFC の種類</strong></p>
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/accessories/Camera/3.6%20Anexample%20of%20an%20FFC%20connected%20to%20the%20D3-G%20MIPI0%2020-pin%20Connector.png"></p>
    <p align="center"><strong>図 3.6 D3-G MIPI0 20-pin コネクタに FFC を接続した例</strong></p> 
    FFC 上の 20 個の銀色の接点が、D3-G MIPI コネクタ内部の 20 個の銀色の接点と位置が合っていることを確認してください
    MIPI1 コネクタを使用する場合も同じ接続方法が適用されます。MIPI0 コネクタと同じ方法で接続してください。
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/accessories/Camera/3.7%20An%20example%20of%20an%20FFC%20connected%20th%20toe%20TOPST%20MIPI%20Gender%20Board%20MIPI%20Connector.png"></p>
    <p align="center"><strong>図 3.7 TOPST MIPI Gender Board の MIPI コネクタに FFC を接続した例</strong></p>
2. Deserializer ボードと MIPI Gender Board の接続。  
    MIPI Gender Board 上の JH2 コネクタを、SerDes ボードの裏面にある JH1 コネクタに取り付けます。
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/accessories/Camera/3.8%20JH2%20Connector.png"></p>
    <p align="center"><strong>図 3.8 JH2 コネクタ</strong></p>
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/accessories/Camera/3.9%20JH1%20Connector.png"></p>
    <p align="center"><strong>図 3.9 JH1 コネクタ</strong></p>
3. GMSL カメラの接続
    図 3.10 に示すようにカメラを接続します。図では 2 台のカメラを使用した例を示していますが、必要に応じて 1 台から 4 台まで任意の台数のカメラを接続できます。
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/accessories/Camera/3.10%20GMSL%20Camera%20Connection.png"></p>
    <p align="center"><strong>図 3.10 JH2 コネクタ</strong></p>

### 3.1.3 USB カメラ
USB カメラは、D3-G の USB 2.0 または USB 3.0 ポートに接続して使用できます。USB 3.0 仕様を必要とする USB カメラを使用する場合は、必ず USB 3.0 ポートに接続してください。

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/accessories/Camera/3.11%20USB%20Camera%20Connection.png"></p>
<p align="center"><strong>図 3.11 USB カメラの接続</strong></p>

## 3.2 AI-G へのカメラの接続
### 3.2.1 MIPI CSI-2 カメラ
図 3.12 は AI-G の MIPI CSI コネクタを示しています。AI-G は 2 チャンネルの MIPI CSI をサポートし、各チャンネルは 2-lane インターフェースで構成されます。

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/accessories/Camera/3.12%20MIPI%20CSI%20Connector%20on%20AI-G.png"></p>
<p align="center"><strong>図 3.12 AI-G の MIPI CSI コネクタ</strong></p>

MIPI カメラを接続する際は、FFC (Flat Flexible Cable) を使用してください。正しいケーブルの種類と向きについては、図 3.13 および 3.14 を参照してください。

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/accessories/Camera/3.2%20FFC%20Type.png"></p>
<p align="center"><strong>図 3.13 FFC タイプ</strong></p>

FFC ケーブルは 1.0 mm、15 ピンタイプで、片面に異なる色のマーキング (青またはグレー) が必要です。ケーブルは B-Forward Direction の向きで挿入してください。FFC のタイプについては図 3.13 を参照してください。

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/accessories/Camera/3.14%20An%20example%20of%20an%20FFC%20connected%20to%20the%20AI-G%20MIPI%2015-pin%20Connector.png"></p>
<p align="center"><strong>図 3.14 AI-G MIPI 15 ピンコネクタに FFC を接続した例</strong></p>

FFC 上の 15 個の銀色の接点が、AI-G MIPI コネクタ内部の 15 個の銀色の接点と合っていることを確認してください。

### 3.2.2 GMSL カメラ
GMSL カメラは Fakra ケーブルを使用します。そのため、AI-G ボードに直接接続することはできません。代わりに、Deserializer (Des) ボードと TOPST MIPI Gender Board を経由して AI-G と接続する必要があります。  
接続構成は次のとおりです。

<p align="center"><strong>< AI-G > ↔ < TOPST MIPI Gender Board > ↔ < Des Board > ↔ < GMSL Camera ></strong></p>

GMSL カメラを使用するには TOPST MIPI Gender Board が必要であり、20 ピン MIPI コネクタを介して接続する必要があります。たとえば、GMSL カメラを 4 台使用する場合は、図 3.15 のように 20 ピン MIPI インターフェースで接続してください。

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/accessories/Camera/3.15%2020-pin%20MIPI%20Connector.png"></p>
<p align="center"><strong>図 3.15 20 ピン MIPI コネクタ</strong></p>

1. AI-G ボードを TOPST MIPI Gender Board に接続します。  
    FFC ケーブルは 1.0 mm、20 ピンタイプで、片面に異なる色のマーキング (青またはグレー) が必要です。ケーブルは A-Forward Direction の向きで挿入してください。FFC のタイプについては図 3.16 を参照してください。
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/accessories/Camera/3.2%20FFC%20Type.png"></p>
    <p align="center"><strong>図 3.16 FFC タイプ</strong></p>
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/accessories/Camera/3.17%20An%20example%20of%20an%20FFC%20connected%20to%20the%20AI-G%20MIPI%2020-pin%20Connector.png"></p>
    <p align="center"><strong>図 3.17 AI-G MIPI 20 ピンコネクタに FFC を接続した例</strong></p>
    FFC 上の 20 個の銀色の接点が、AI-G MIPI コネクタ内部の 20 個の銀色の接点と合っていることを確認してください
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/accessories/Camera/3.18%20An%20example%20of%20an%20FFC%20connected%20to%20the%20TOPST%20MIPI%20Gender%20Board%20MIPI%20Connector.png"></p>
    <p align="center"><strong>図 3.18 TOPST MIPI Gender Board の MIPI コネクタに FFC を接続した例</strong></p>
2. Deserializer ボードと MIPI Gender Board の接続。  
    MIPI Gender Board の JH2 コネクタを、SerDes ボードの底面にある JH1 コネクタに接続してください。
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/accessories/Camera/3.19%20JH2%20Connector.png"></p>
    <p align="center"><strong>図 3.19 JH2 コネクタ</strong></p>
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/accessories/Camera/3.20%20JH1%20Connector.png"></p>
    <p align="center"><strong>図 3.20 JH1 コネクタ</strong></p>
3. GMSL カメラの接続
    図 3.21 のようにカメラを接続してください。図では 2 台のカメラを使用した例を示していますが、必要に応じて 1 台から 4 台まで任意の台数のカメラを接続できます。
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/accessories/Camera/3.21%20GMSL%20Camera%20Connection.png"></p>
    <p align="center"><strong>図 3.21 GMSL カメラの接続</strong></p>

# 4. ソフトウェアセットアップ
第 4 章では、カメラ動作に必要なソフトウェアセットアップについて説明します。D3-G および AI-G プラットフォームで MIPI CSI-2 カメラ (OV5647、IMX219) と GMSL カメラを設定するには、以下に示す Yocto のセットアップ手順を参照してください。

## 4.1 MIPI CSI-2 カメラセットアップガイド
TX データレートは次の式を使用して計算できます。

<p align="center"><strong>TX データレート ={ H_active }×{V_active }×{FPS}×{BPP}×{ Number_of_Cameras} × 1.3 (マージン)</strong></p>

合計データレートは、レーンあたり 2.1 Gbps という D3-G MIPI CSI-2 の帯域幅制限を超えてはなりません。  
また、合計データレートは、レーンあたり 1.5 Gbps という AI-G MIPI CSI-2 の帯域幅制限を超えてはなりません

### 4.1.1 D3-G OV5647 セットアップガイド
#### 4.1.1.1 OV5647 センサー概要
##### 4.1.1.1.1 はじめに
OV5647 は、小型サイズ、安定した性能、標準 MIPI CSI-2 インターフェースとの互換性により、組み込みカメラアプリケーションで広く使用されている 500 万画素 CMOS イメージセンサーです。Raspberry Pi Camera Module v1 に使用されているイメージセンサーでもあり、各種 Arducam OV5647 カメラモジュールを通じて入手できます。これらはすべて TOPST D3-G プラットフォームと互換性があります。  
ユーザーは、カメラを動作させるために Raspberry Pi Camera v1 または Arducam OV5647 モジュールを MIPI CSI ポートに接続できます。

TOPST D3-G プラットフォームでは、OV5647 は 15 ピンまたは 20 ピンの MIPI CSI コネクタを介して接続され、V4L2 フレームワークで制御されるため、Yocto と Ubuntu の両環境で一貫した動作を提供します。

##### 4.1.1.1.2 対応解像度と FPS
OV5647 カメラモジュール (Raspberry Pi v1 または Arducam OV5647) の仕様は次のとおりです。  

<p align="center"><strong>表 4.1 OV5647 カメラモジュールの仕様</strong></p>
<div align="center">
    <table>
        <tr>
            <td colspan="2" align="center"><strong>仕様</strong></td>
            <td align="center"><strong>説明</strong></td>
        </tr>
        <tr>
            <td colspan="2">センサー</td>
            <td>OmniVision OV5647</td>
        </tr>
        <tr>
            <td colspan="2">解像度</td>
            <td>2592 x 1944 (5MP)</td>
        </tr>
        <tr>
            <td colspan="2">出力フォーマット</td>
            <td>RAW, YUV, JPEG</td>
        </tr>
        <tr>
            <td colspan="2">インターフェース</td>
            <td>MIPI CSI-2</td>
        </tr>
        <tr>
            <td colspan="2">フレームレート</td>
            <td>1080p30, 720p60, 480p90</td>
        </tr>
        <tr>
            <td colspan="2">レンズ</td>
            <td>固定焦点</td>
        </tr>
        <tr>
            <td colspan="2">視野角 (FOV)</td>
            <td>Up to 54°</td>
        </tr>
        <tr>
            <td colspan="2">ケーブルタイプ</td>
            <td>FFC (15 ピン)</td>
        </tr>
        <tr>
            <td colspan="2">ボード寸法</td>
            <td>25mm x 24mm</td>
        </tr>
        <tr>
            <td colspan="2">互換性</td>
            <td>D3-G および Rasbperry Pi (MIPI CSI-2 ポート経由)</td>
        </tr>
    </table>
</div>

D3-G でサポートされるセンサーの解像度と FPS は次のとおりです。  
<p align="center"><strong>表 4.2 D3-G における OV5647 センサーの解像度</strong></p>
<div align="center">
    <table>
        <tr>
            <td colspan="3" align="center"><strong>解像度</strong></td>
            <td align="center"><strong>FPS</strong></td>
            <td align="center"><strong>説明</strong></td>
        </tr>
        <tr>
            <td colspan="3">1920x1080</td>
            <td>30</td>
            <td>フル解像度フレームの中央領域をクロップして 1080p 画像を出力します</td>
        </tr>
        <tr>
            <td colspan="3">1296x972</td>
            <td>30</td>
            <td>2×2 ピクセルビニングを利用して感度を高め、ノイズを低減します</td>
        </tr>
        <tr>
            <td colspan="3">640x480</td>
            <td>60</td>
            <td>2×2 ビニングと <strong>サブサンプリング</strong> を組み合わせます。サブサンプリングは読み出し時にピクセルをスキップしてデータスループットを削減し、より高いフレームレートを実現します</td>
        </tr>
    </table>
</div>

**注:** 表 4.2 に示すとおり、D3-G の ISP 仕様により、フル解像度の **2592×1944 は使用できません**。

<p align="center"><strong>表 4.3 動作モード別の最大解像度</strong></p>
<div align="center">
    <table>
        <tr>
            <td rowspan="2" align="center"><strong>ISP コア</strong></td>
            <td colspan="2"><strong>動作モード別の解像度</strong></td>
        </tr>
        <tr>
            <td align="center"><strong>デフォルトモード</strong></td>
            <td align="center"><strong>メモリ共有モード</strong></td>
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

#### 4.1.1.2 Yocto での OV5647 解像度設定: ドライバ
Yocto のビルド処理中に OV5647 センサーの解像度を変更するには、以下の手順に従ってください。  

まず、OV5647 を有効にするには、次のファイルに TOPST_CAM_MODULE = "ov5647" が設定されていることを確認してください。  
{build_dir}/build/d3-g-topst-main/conf/local.conf.  
これは最初のビルドのためにリポジトリを初期化する際にデフォルトで有効になりますが、再度確認してください。

さらに、ビルド処理中にソースコードが削除されないように、次のファイルで以下の行を有効にしてください。  
{build_dir}/build/d3-g-topst-main/conf/local.conf:
```
INHERIT:remove = “rm_work”
```

上記のオプションを有効にした後、次のコマンドでイメージを再ビルドしてください。
```
$ bitbake telechips-topst-image
```

次に、ビルドが完了したら ov5647.c ドライバファイルを開き、必要な変更を適用してください。

次のディレクトリに移動してください。
```
${build_dir}/build/d3-g-topst-main/tmp/work/d3_g_topst_main-telechips-linux/linux-topst/5.10.205-r0/git/drivers/media/i2c/telechips/
```

コードを変更する前に、現在のドライバが次の 3 つのモードをサポートしていることに注意してください。
- 1920x1080 @ 30fps
- 1296x972 @ 30fps
- 640x480 @ 60fps  

各解像度はそれぞれ Mode 1、Mode 2、Mode 3 に対応します。  

1920×1080 @ 30fps モードはセンタークロップを使用するため視野角が狭くなり、640×480 モードは解像度が不足します。一方、1296×972 モードは 2×2 ビニングを使用してより広い視野角を提供するため、現在デフォルトモードとして使用されています。  
ov5647.c ドライバファイルを開き、以下のように OV5647 のデフォルトモードを変更してください。
```
#define OV5647_DEFAULT_MODE (&supported_modes_10bit[2])
```
1920×1080 @ 30fps は Mode 1 に対応するため、**“#define OV5647_DEFAULT_MODE (&supported_modes_10bit[1])”** をそのまま使用できます。  
1296×972 @ 30fps モードは Mode 2 に対応するため、**“#define OV5647_DEFAULT_MODE (&supported_modes_10bit[2])”** はすでに正しく設定されています。  
Mode 3 に該当する 640×480 @ 60fps の場合は、定義を **“#define OV5647_DEFAULT_MODE (&supported_modes_10bit[3])”** に変更します。

3 番目に、カーネルを再ビルドして FAI イメージを生成します。  
ビルドディレクトリに戻り、以下のコマンドを使用してカーネルを再ビルドします。
```
$ cd ${build_dir}/build/d3-g-topst-main/
$ bitbake -C compile linux-topst
$ cd ${build_dir}
$ ./stitch-fai-d3.sh
```
その後、生成された output_d3g.fai を FWDN でボードに書き込むと、希望する解像度で OV5647 センサーを使用できます。

**注意:** MIPI1-CSI ポートを使用する場合は、次の場所にある tcc805x-videoinput-camera-module.dtsi ファイルを開きます。
“{build_dir}/build/d3-g-topst-main/tmp/work/d3_g_topst_main-telechips-linux/linux-topst/5.10.205-r0/git/arch/arm64/boot/dts/telechips/tcc805x/override/” and change the included dtsi file from “tcc805x-videoinput-mipi0-ov5647.dtsi” to “tcc805x-videoinput-mipi1-ov5647.dtsi”. + Open the tcc805x-videoinput.dtsi file located in "{build_dir}/build/d3-g-topst-main/tmp/work/d3_g_topst_main-telechips-linux/linux-topst/5.10.205-r0/git/arch/arm64/boot/dts/telechips/tcc805x/" and change the mipi chmux from "mipi-chmux-0 = <0>;" to "mipi-chmux-0 = <1>;".

### 4.1.2 D3-G IMX219 セットアップガイド
#### 4.1.2.1 IMX219 センサー概要
##### 4.1.2.1.1 はじめに
IMX219 は Sony 製の高性能な 800 万画素 CMOS イメージセンサーで、小型カメラモジュールにおいて優れた画質、低消費電力、安定した撮影性能を提供することで広く知られています。また、Raspberry Pi Camera Module v2 に採用されているセンサーであり、組み込みビジョンシステム、ロボティクス、AI ベースのカメラアプリケーションで広く利用されています。

TOPST D3-G プラットフォームでは、IMX219 センサーを 15 ピンまたは 20 ピンの MIPI CSI コネクタ経由で接続でき、V4L2 フレームワークによって制御されます。これにより、Yocto と Ubuntu の両方の環境で一貫したインタフェースと安定したカメラ動作が実現します。

IMX219 は高解像度（8MP）と低ノイズの撮像特性を備えているため、TOPST D3-G プラットフォーム上で高品質な映像キャプチャおよび画像処理機能を実装するのに適しています。

##### 4.1.2.1.2 対応解像度と FPS
IMX219 カメラモジュール（Raspberry Pi v2）の仕様は次のとおりです。

<p align="center"><strong>表 4.4 IMX219 カメラモジュールの仕様</strong></p>
<div align="center">
    <table>
        <tr>
            <td colspan="2" align="center"><strong>仕様</strong></td>
            <td align="center"><strong>説明</strong></td>
        </tr>
        <tr>
            <td colspan="2">センサー</td>
            <td>Sony Imx219</td>
        </tr>
        <tr>
            <td colspan="2">解像度</td>
            <td>3280 x 2464 (8 MP)</td>
        </tr>
        <tr>
            <td colspan="2">出力フォーマット</td>
            <td>RAW, YUV, JPEG</td>
        </tr>
        <tr>
            <td colspan="2">インターフェース</td>
            <td>MIPI CSI-2</td>
        </tr>
        <tr>
            <td colspan="2">フレームレート</td>
            <td>1080p60, 720p180, 480p206</td>
        </tr>
        <tr>
            <td colspan="2">レンズ</td>
            <td>フォーカス調整可能</td>
        </tr>
        <tr>
            <td colspan="2">視野角 (FOV)</td>
            <td>Up to 62°</td>
        </tr>
        <tr>
            <td colspan="2">ケーブルタイプ</td>
            <td>FFC (15 ピン)</td>
        </tr>
        <tr>
            <td colspan="2">ボード寸法</td>
            <td>25mm x 24mm</td>
        </tr>
        <tr>
            <td colspan="2">互換性</td>
            <td>D3-G および Rasbperry Pi (MIPI CSI-2 ポート経由)</td>
        </tr>
    </table>
</div>

D3-G でサポートされるセンサー解像度と FPS は次のとおりです。
<p align="center"><strong>表 4.5 D3-G における IMX219 センサー解像度</strong></p>
<div align="center">
    <table>
        <tr>
            <td colspan="3" align="center"><strong>解像度</strong></td>
            <td align="center"><strong>FPS</strong></td>
            <td align="center"><strong>説明</strong></td>
        </tr>
        <tr>
            <td colspan="3">1920x1080</td>
            <td>30</td>
            <td>フル解像度フレームの中央領域をクロップして 1080p 画像を出力します</td>
        </tr>
        <tr>
            <td colspan="3">1640x1232</td>
            <td>30</td>
            <td>2×2 ピクセルビニングを利用して感度を高め、ノイズを低減します</td>
        </tr>
        <tr>
            <td colspan="3">640x480</td>
            <td>30</td>
            <td>2×2 ビニングと<strong>サブサンプリング</strong>を組み合わせ、読み出し時にピクセルを間引いてデータスループットを削減します</td>
        </tr>
    </table>
</div>  

**注意:** 表 4.5 に示すとおり、D3-G の ISP 仕様により、**3820×2464 のフル解像度は使用できません**。

<p align="center"><strong>表 4.6 動作モード別の最大解像度</strong></p>
<div align="center">
    <table>
        <tr>
            <td rowspan="2" align="center"><strong>ISP コア</strong></td>
            <td colspan="2"><strong>動作モード別の解像度</strong></td>
        </tr>
        <tr>
            <td align="center"><strong>デフォルトモード</strong></td>
            <td align="center"><strong>メモリ共有モード</strong></td>
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

#### 4.1.2.2 Yocto での IMX219 の有効化
D3-G SDK はデフォルトで OV5647 が有効になるよう構成されているため、ビルドの前に IMX219 を有効にする必要があります。   
SDK がすでにビルドされている場合と、初めてビルドする場合の 2 つのケースが考えられます。

##### 4.1.2.2.1 初回ビルド前に IMX219 を有効にする
初回ビルドの場合は、以下の手順に従って IMX219 を有効にしてからビルドを実行します。
1. 環境設定スクリプトを source し、オプション 2 を選択します
    ```
    $ source poky/meta-topst/topst-build.sh
    ```
2. 以下のパスにある local.conf ファイルを開きます
    ```
    ${build_dir}/build/d3-g-topst-main/conf/local.conf
    ```
3. ov5647 の TOPST_CAM_MODULE エントリをコメントアウトし、imx219 のエントリを有効にします
    ```
    #TOPST_CAM_MODULE = "ov5647"
    TOPST_CAM_MODULE = "imx219"
    ```
4. ビルドを実行します
    ```
    $ bitbake telechips-topst-image
    ```
##### 4.1.2.2.2 ビルドが完了した後に IMX219 を有効にする
既存のビルドでは、デフォルトで OV5647 センサーが有効に設定されています。以下の手順に従って IMX219 を有効にしてください。
1. 以下のパスにある local.conf ファイルを開きます
    ```
    ${build_dir}/build/d3-g-topst-main/conf/local.conf
    ```
2. ov5647 の TOPST_CAM_MODULE エントリをコメントアウトし、imx219 のエントリを有効にします
    ```
    #TOPST_CAM_MODULE = "ov5647"
    TOPST_CAM_MODULE = "imx219"
    ```
3. isp-server と isp-firmware に対して cleansstate を実行します
    ```
    $ bitbake -c cleansstate isp-firmware
    $ bitbake -c cleansstate isp-server
    ```
4. ビルドを実行します
    ```
    $ bitbake telechips-topst-image


#### 4.1.2.3 Yocto での IMX219 解像度設定: ドライバ
Yocto のビルド過程で IMX219 センサーの解像度を変更するには、以下の手順に従ってください。

まず、imx219 を有効にするには、TOPST_CAM_MODULE = "imx219" が設定されていることを確認します
{build_dir}/build/d3-g-topst-main/conf/local.conf.

また、ビルド中にソースコードが削除されないように、次の行を有効にします
{build_dir}/build/d3-g-topst-main/conf/local.conf:
```
INHERIT:remove = “rm_work”
```

上記のオプションを有効にした後、次のコマンドでイメージを再ビルドしてください。
```
$ bitbake telechips-topst-image
```

次に、ビルドが完了したら imx219.c ドライバファイルを開き、必要な修正を適用します。

次のディレクトリに移動してください。
```
${build_dir}/build/d3-g-topst-main/tmp/work/d3_g_topst_main-telechips-linux/linux-topst/5.10.205-r0/git/drivers/media/i2c/telechips/
```

コードを変更する前に、現在のドライバが次の 3 つのモードをサポートしていることに注意してください。
- 1920x1080 @ 30fps
- 1640x1232 @ 30fps
- 640x480 @ 30fps

各解像度はそれぞれ Mode 1、Mode 2、Mode 3 に対応します。

1920×1080 @ 30fps モードはセンタークロップを使用するため画角が狭くなり、640×480 モードは解像度が不十分です。これに対して 1640×1232 モードは 2×2 ビニングを使用し、より広い画角が得られるため、現在は既定のモードとして使用されています。  
imx219.c ドライバファイルを開き、imx219_set_default_format、imx219_open、imx219_probe の各関数内で以下に説明する箇所を修正します。
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

1920×1080 @ 30fps は Mode 1 に対応するため、3 つの関数内のすべての supported_modes の参照を **“supported_modes[1]”** に変更してください。  
1640×1232 @ 30fps モードは Mode 2 に対応するため、それに合わせて **“supported_modes[2]”** に置き換えてください。  
Mode 3 に対応する 640×480 @ 30fps の場合、すべての参照を **“supported_modes [3]”** に変更します。

3 番目に、カーネルを再ビルドして FAI イメージを生成します。  
ビルドディレクトリに戻り、以下のコマンドを使用してカーネルを再ビルドします。
```
$ cd ${build_dir}/build/d3-g-topst-main/
$ bitbake -C compile linux-topst
$ cd ${build_dir}
$ ./stitch-fai-d3.sh
```

その後、生成された output_d3g.fai を FWDN でボードに書き込むと、希望する解像度で IMX219 センサーを使用できます。

**注意:** MIPI1-CSI ポートを使用する場合は、次の場所にある tcc805x-videoinput-camera-module.dtsi ファイルを開きます。
“{build_dir}/build/d3-g-topst-main/tmp/work/d3_g_topst_main-telechips-linux/linux-topst/5.10.205-r0/git/arch/arm64/boot/dts/telechips/tcc805x/override/”and change the included dtsi file from “tcc805x-videoinput-mipi0-imx219.dtsi” to “tcc805x-videoinput-mipi1-imx219.dtsi”. + Open the tcc805x-videoinput.dtsi file located in "{build_dir}/build/d3-g-topst-main/tmp/work/d3_g_topst_main-telechips-linux/linux-topst/5.10.205-r0/git/arch/arm64/boot/dts/telechips/tcc805x/" and change the mipi chmux from "mipi-chmux-0 = <0>;" to "mipi-chmux-0 = <1>;".

#### 4.1.2.4 Yocto で IMX219 の FPS を上げる方法: ドライバとデバイスツリー
IMX219 センサーの説明によると、このセンサーは 1080p60、720p180、VGA206 などの高フレームレートモードをサポートします。したがって、imx219.c ドライバがサポートする解像度である 1920×1080、1640×1232、640×480 の FPS を上げることが可能です。D3-G プラットフォームの ISP コアは最大 60 fps をサポートするため、これらの解像度はそれぞれ最大 60 fps まで上げることができます。 

FPS を計算する式は次のとおりです。
<p align="center"><strong>{fps} = {pixel_rate}/{hts}x{vts}</strong></p>
したがって、FPS を上げるには pixel_rate、hts、vts の値を調整する必要があります。  
現在のドライバ実装では、pixel_rate と hts の両方が固定されています。FPS を上げるには、hts を一定に保ったまま pixel_rate を上げ、それに合わせて vts を調整して目的のフレームレートを得る方法しかありません。

FPS を 60 に変更するには、ドライバとデバイスツリーの両方を更新する必要があります。
FPS を 60 に変更するには、以下のガイドに従ってください。

##### 4.1.2.4.1 1920x1080 @ 60fps
60 fps を達成するには、次の関係が成り立つ必要があります。  
fps = pixel_rate / (hts × vts)
- pixel_rate = 182,400,000
- hts = 3448
- target fps = 60

必要な VTS は次のようになります。
- vts = pixel_rate / (hts × fps) = 182,400,000 / (3448 × 60) ≈ 882

ただし、VTS 値は 1080 より大きくなければならないため、この構成は有効ではありません。  
したがって、60 fps にするには hts を固定したまま、pixel_rate、vts および PLL_VT レジスタを調整する必要があります。

必要な変更は次のとおりです。
1. imx219.c ドライバファイル  
    A. ピクセルレートとリンク周波数を上げます
    ```
    #define IMX219_PIXEL_RATE            182400000    →   #define IMX219_PIXEL_RATE            278400000
    #define IMX219_DEFAULT_LINK_FREQ     456000000   →   #define IMX219_DEFAULT_LINK_FREQ     696000000
    ``` 
    B. 1080p モードの VTS 値を更新します:
    ```
    #define IMX219_VTS_30FPS_1080P       0x06e3       →   #define IMX219_VTS_30FPS_1080P       0x0542
    ```
    C. 1920x1080 モードテーブルの PLL_VT レジスタを変更します:
    ```
    // imx219_reg mode_1920_1080_regs[]
    {0x0307, 0x39}   →   {0x0307, 0x57}
    ```
2. tcc805x-videoinput-mipi0-imx219.dtsi デバイスツリーファイル  
    A. 新しいピクセルレートに合わせてリンク周波数を更新します:
    ```
    // &i2c7
    /bits/ 64 <456000000> → /bits/ 64 <696000000>
    ```
    B. hs-settle 値を更新します:
    ```
    hs-settle = <13> → hs-settle = <35>
    ```
3. カーネルを再ビルドし、FAI イメージを生成します。  
    ビルドディレクトリに戻り、以下のコマンドでカーネルを再ビルドします。
    ```
    $ cd ${build_dir}/build/d3-g-topst-main/
    $ bitbake -C compile linux-topst
    $ cd ${build_dir}
    $ ./stitch-fai-d3.sh
    ```
D3-G で以下のコマンドを使用すると、FPS の出力が 59.9 となり、これが 60 fps に相当することを確認できます。
```
$ v4l2-ctl --stream-mmap=3 --stream-count=300 --stream-to=/dev/null --verbose
```
D3-G でカメラを再生するための GStreamer コマンドを以下に示します。
```
$ gst-launch-1.0 v4l2src device=/dev/video0 io-mode=2 ! video/x-raw,format=NV12,width=1920,height=1080,framerate=60/1 ! videoconvert ! waylandsink sync=false
```

##### 4.1.2.4.2 1640x1232 @ 60fps
60 fps を達成するには、次の関係が成り立つ必要があります。  
fps = pixel_rate / (hts × vts)
- pixel_rate = 182,400,000
- hts = 3448
- target fps = 60

必要な VTS は次のようになります。
- vts = pixel_rate / (hts × fps) = 182,400,000 / (3448 × 60) ≈ 882

ただし、VTS 値は 1080 より大きくなければならないため、この構成は有効ではありません。  
したがって、60 fps にするには hts を固定したまま、pixel_rate、vts および PLL_VT レジスタを調整する必要があります。

必要な変更は次のとおりです。
1. imx219.c ドライバファイル  
    A. ピクセルレートとリンク周波数を上げます
    ```
    #define IMX219_PIXEL_RATE            182400000    →   #define IMX219_PIXEL_RATE            278400000
    #define IMX219_DEFAULT_LINK_FREQ     456000000   →   #define IMX219_DEFAULT_LINK_FREQ     696000000
    ``` 
    B. 1640_1232 モードの VTS 値を更新します:
    ```
    #define IMX219_VTS_30FPS_BINNED       0x06e3       →   #define IMX219_VTS_30FPS_BINNED       0x0542
    ```
    C. 1920x1080 モードテーブルの PLL_VT レジスタを変更します:
    ```
    // imx219_reg mode_1640_1232_regs[]
    {0x0307, 0x39}   →   {0x0307, 0x57}
    ```
2. tcc805x-videoinput-mipi0-imx219.dtsi デバイスツリーファイル  
    A. 新しいピクセルレートに合わせてリンク周波数を更新します:
    ```
    // &i2c7
    /bits/ 64 <456000000> → /bits/ 64 <696000000>
    ```
    B. hs-settle 値を更新します:
    ```
    hs-settle = <13> → hs-settle = <34>
    ```
3. カーネルを再ビルドし、FAI イメージを生成します。  
    ビルドディレクトリに戻り、以下のコマンドでカーネルを再ビルドします。
    ```
    $ cd ${build_dir}/build/d3-g-topst-main/
    $ bitbake -C compile linux-topst
    $ cd ${build_dir}
    $ ./stitch-fai-d3.sh
    ```
D3-G で以下のコマンドを使用すると、FPS の出力が 59.9 となり、これが 60 fps に相当することを確認できます。
```
$ v4l2-ctl --stream-mmap=3 --stream-count=300 --stream-to=/dev/null --verbose
```
D3-G でカメラを再生するための GStreamer コマンドを以下に示します。
```
$ gst-launch-1.0 v4l2src device=/dev/video0 io-mode=2 ! video/x-raw,format=NV12,width=1640,height=1232,framerate=60/1 ! videoconvert ! waylandsink sync=false
```

##### 4.1.2.4.3 640x480 @ 60fps
60 fps を達成するには、次の関係が成り立つ必要があります。  
fps = pixel_rate / (hts × vts)
- pixel_rate = 182,400,000
- hts = 3448
- target fps = 60

必要な VTS は次のようになります。
- vts = pixel_rate / (hts × fps) = 182,400,000 / (3448 × 60) ≈ 882

VTS 値が 480 より大きいため、条件を満たしています。前の例と同様に、HTS を固定したまま pixelrate と VTS を調整して FPS を変更します。  
pixelrate を変更せずに VTS 値のみを修正して FPS を調整することもできます。ただし、IMX219 の 0x0307 レジスタ値は変更してはなりません。

必要な変更は次のとおりです。
1. imx219.c ドライバファイル  
    A. ピクセルレートとリンク周波数を上げます
    ```
    #define IMX219_PIXEL_RATE            182400000    →   #define IMX219_PIXEL_RATE            278400000
    #define IMX219_DEFAULT_LINK_FREQ     456000000   →   #define IMX219_DEFAULT_LINK_FREQ     696000000
    ``` 
    B. 640_480 モードの VTS 値を更新します:
    ```
    #define IMX219_VTS_30FPS_640x480       0x06e3       →   #define IMX219_VTS_30FPS_640x480       0x0542
    ```
    C. 640x480 モードテーブルの PLL_VT レジスタを変更します:
    ```
    // imx219_reg mode_640_480_regs[]
    {0x0307, 0x39}   →   {0x0307, 0x57}
    ```
2. tcc805x-videoinput-mipi0-imx219.dtsi デバイスツリーファイル  
    A. 新しいピクセルレートに合わせてリンク周波数を更新します:
    ```
    // &i2c7
    /bits/ 64 <456000000> → /bits/ 64 <696000000>
    ```
    B. hs-settle 値を更新します:
    ```
    hs-settle = <13> → hs-settle = <26>
    ```
3. カーネルを再ビルドし、FAI イメージを生成します。  
    ビルドディレクトリに戻り、以下のコマンドでカーネルを再ビルドします。
    ```
    $ cd ${build_dir}/build/d3-g-topst-main/
    $ bitbake -C compile linux-topst
    $ cd ${build_dir}
    $ ./stitch-fai-d3.sh
    ```
D3-G で以下のコマンドを使用すると、FPS の出力が 59.9 となり、これが 60 fps に相当することを確認できます。
```
$ v4l2-ctl --stream-mmap=3 --stream-count=300 --stream-to=/dev/null --verbose
```
D3-G でカメラを再生するための GStreamer コマンドを以下に示します。
```
$ gst-launch-1.0 v4l2src device=/dev/video0 io-mode=2 ! video/x-raw,format=NV12,width=640,height=480,framerate=60/1 ! videoconvert ! waylandsink sync=false
```

### 4.1.3 AI-G OV5647 センサーユーザーガイド
#### 4.1.3.1 OV5647 センサー概要
##### 4.1.3.1.1 はじめに
OV5647 は、小型で安定した性能を持ち、標準の MIPI CSI-2 インタフェースと互換性があることから、組み込みカメラアプリケーションで広く使用されている 500 万画素の CMOS イメージセンサーです。また、Raspberry Pi Camera Module v1 に使用されているイメージセンサーであり、各種の Arducam OV5647 カメラモジュールとして入手できます。これらはいずれも TOPST AI-G プラットフォームと互換性があります。  
ユーザーは、カメラを動作させるために Raspberry Pi Camera v1 または Arducam OV5647 モジュールを MIPI CSI ポートに接続できます。

TOPST AI-G プラットフォームでは、OV5647 は 15 ピンまたは 20 ピンの MIPI CSI コネクタを介して接続され、V4L2 フレームワークによって制御されるため、Yocto と Ubuntu の両方の環境で一貫した動作が可能です。

##### 4.1.3.1.2 サポートされる解像度と FPS
OV5647 カメラモジュール（Raspberry Pi v1 または Arducam OV5647）の仕様は次のとおりです。
<p align="center"><strong>表 4.7 OV5647 カメラモジュールの仕様</strong></p>
<div align="center">
    <table>
        <tr>
            <td colspan="2" align="center"><strong>仕様</strong></td>
            <td align="center"><strong>説明</strong></td>
        </tr>
        <tr>
            <td colspan="2">センサー</td>
            <td>OmniVision OV5647</td>
        </tr>
        <tr>
            <td colspan="2">解像度</td>
            <td>2592 x 1944 (5MP)</td>
        </tr>
        <tr>
            <td colspan="2">出力フォーマット</td>
            <td>RAW, YUV, JPEG</td>
        </tr>
        <tr>
            <td colspan="2">インターフェース</td>
            <td>MIPI CSI-2</td>
        </tr>
        <tr>
            <td colspan="2">フレームレート</td>
            <td>1080p30, 720p60, 480p90</td>
        </tr>
        <tr>
            <td colspan="2">レンズ</td>
            <td>固定焦点</td>
        </tr>
        <tr>
            <td colspan="2">視野角 (FOV)</td>
            <td>Up to 54°</td>
        </tr>
        <tr>
            <td colspan="2">ケーブルタイプ</td>
            <td>FFC (15 ピン)</td>
        </tr>
        <tr>
            <td colspan="2">ボード寸法</td>
            <td>25mm x 24mm</td>
        </tr>
        <tr>
            <td colspan="2">互換性</td>
            <td>D3-G および Rasbperry Pi (MIPI CSI-2 ポート経由)</td>
        </tr>
    </table>
</div>

AI-G でサポートされるセンサーの解像度と FPS は次のとおりです。  
<p align="center"><strong>表 4.8 AI-G における OV5647 センサー解像度</strong></p>
<div align="center">
    <table>
        <tr>
            <td colspan="3" align="center"><strong>解像度</strong></td>
            <td align="center"><strong>FPS</strong></td>
            <td align="center"><strong>説明</strong></td>
        </tr>
        <tr>
            <td colspan="3">1920x1080</td>
            <td>30</td>
            <td>フル解像度フレームの中央領域をクロップして 1080p 画像を出力します</td>
        </tr>
        <tr>
            <td colspan="3">1296x972</td>
            <td>30</td>
            <td>2×2 ピクセルビニングを利用して感度を高め、ノイズを低減します</td>
        </tr>
        <tr>
            <td colspan="3">640x480</td>
            <td>60</td>
            <td>2×2 ビニングと <strong>サブサンプリング</strong> を組み合わせます。サブサンプリングは読み出し時にピクセルをスキップしてデータスループットを削減し、より高いフレームレートを実現します</td>
        </tr>
    </table>
</div>

**注:** 表 4.8 に示すとおり、推論性能が大幅に低下するため、**フル 2592×1944 解像度は使用しません**。

<p align="center"><strong>表 4.9 動作モード別の最大解像度</strong></p>
<div align="center">
    <table>
        <tr>
            <td colspan="4" align="center"><strong>使用 CH.</strong></td>
            <td align="center"><strong>動作モード</strong></td>
            <td align="center"><strong>最大解像度</strong></td>
            <td align="center"><strong>入力フォーマット</strong></td>
        </tr>
        <tr>
            <td colspan="4">4CH</td>
            <td>デフォルトモード</td>
            <td>1280 x 720 @ 60fps</td>
            <td>RAW 24</td>
        </tr>
        <tr>
            <td colspan="4" rowspan="2">2CH</td>
            <td rowspan="2">メモリ共有モード</td>
            <td>オプション 1: 2048 x 1280 @ 60fps</td>
            <td>RAW 20</td>
        </tr>
        <tr>
            <td>オプション 2: 2592 x 2048 @ 30fps + 2048 x 1280 @ 30fps</td>
            <td>RAW 24</td>
        </tr>
        <tr>
            <td colspan="4">1CH</td>
            <td>メモリ共有モード</td>
            <td>2592 x 2048 @ 60fps</td>
            <td>RAW 20</td>
        </tr>
    </table>
</div>

#### 4.1.3.2 Yocto での OV5647 解像度設定: ドライバ
Yocto のビルド過程で OV5647 センサーの解像度を変更するには、以下の手順に従ってください。

まず、OV5647 を有効にするには、次のファイルに TOPST_CAM_MODULE = "ov5647" が設定されていることを確認してください。  
{build_dir}/build/ai-g-topst-main/conf/local.conf.  
これは最初のビルドのためにリポジトリを初期化する際にデフォルトで有効になりますが、再度確認してください。

さらに、ビルド処理中にソースコードが削除されないように、次のファイルで以下の行を有効にしてください。  
{build_dir}/build/ai-g-topst-main/conf/local.conf:
```
INHERIT:remove = “rm_work”
```

上記のオプションを有効にした後、次のコマンドでイメージを再ビルドしてください。
```
$ bitbake telechips-topst-image
```

次に、ビルドが完了したら ov5647.c ドライバファイルを開き、必要な変更を適用してください。

次のディレクトリに移動してください。
```
${build_dir}/build/ai-g-topst-main/tmp/work/ai_g_topst-telechips-linux/linux-topst/5.10.223-r0/git/drivers/media/i2c/telechips/
```

コードを変更する前に、現在のドライバが次の 3 つのモードをサポートしていることに注意してください。
- 1920×1080 @ 30fps
- 1296×972 @ 30fps
- 640×480 @ 60fps

各解像度はそれぞれ Mode 1、Mode 2、Mode 3 に対応します。

1920×1080 @ 30fps モードはセンタークロップを使用するため視野角が狭くなり、640×480 モードは解像度が不足します。一方、1296×972 モードは 2×2 ビニングを使用してより広い視野角を提供するため、現在デフォルトモードとして使用されています。  
ov5647.c ドライバファイルを開き、以下のように OV5647 のデフォルトモードを変更してください。
```
#define OV5647_DEFAULT_MODE (&supported_modes_10bit[2])
```
1920×1080 @ 30fps は Mode 1 に対応するため、**“#define OV5647_DEFAULT_MODE (&supported_modes_10bit[1])”** をそのまま使用できます。  
1296×972 @ 30fps モードは Mode 2 に対応するため、**“#define OV5647_DEFAULT_MODE (&supported_modes_10bit[2])”** はすでに正しく設定されています。  
Mode 3 に該当する 640×480 @ 60fps の場合は、定義を **“#define OV5647_DEFAULT_MODE (&supported_modes_10bit[3])”** に変更します。

3 番目に、カーネルを再ビルドして FAI イメージを生成します。  
ビルドディレクトリに戻り、以下のコマンドを使用してカーネルを再ビルドします。
```
$ cd ${build_dir}/build/ai-g-topst-main/
$ bitbake -C compile linux-topst
$ cd ${build_dir}
$ ./stitch-fai-ai.sh
```

その後、生成された output_aig.fai を FWDN でボードに書き込むと、希望する解像度で OV5647 センサーを使用できます。

### 4.1.4 AI-G IMX219 センサーセットアップガイド
#### 4.1.4.1 IMX219 センサー概要
##### 4.1.4.1.1 はじめに
IMX219 は Sony 製の高性能な 800 万画素 CMOS イメージセンサーで、小型カメラモジュールにおいて優れた画質、低消費電力、安定した撮影性能を提供することで広く知られています。また、Raspberry Pi Camera Module v2 に採用されているセンサーであり、組み込みビジョンシステム、ロボティクス、AI ベースのカメラアプリケーションで広く利用されています。

TOPST AI-G プラットフォームでは、IMX219 センサーは 15 ピンまたは 20 ピンの MIPI CSI コネクタを介して接続でき、V4L2 フレームワークによって制御されます。これにより、Yocto と Ubuntu の両方の環境で一貫したインターフェースと安定したカメラ動作が可能になります。

高い解像度（8MP）と低ノイズの撮像特性を備えた IMX219 は、TOPST AI-G プラットフォームで高品質な映像撮影および画像処理機能を実現するのに適しています。

##### 4.1.4.1.2 サポートされる解像度と FPS
IMX219 カメラモジュール（Raspberry Pi v2）の仕様は次のとおりです。
<p align="center"><strong>表 4.10 IMX219 カメラモジュールの仕様</strong></p>
<div align="center">
    <table>
        <tr>
            <td colspan="2" align="center"><strong>仕様</strong></td>
            <td align="center"><strong>説明</strong></td>
        </tr>
        <tr>
            <td colspan="2">センサー</td>
            <td>Sony Imx219</td>
        </tr>
        <tr>
            <td colspan="2">解像度</td>
            <td>3280 x 2464 (8 MP)</td>
        </tr>
        <tr>
            <td colspan="2">出力フォーマット</td>
            <td>RAW, YUV, JPEG</td>
        </tr>
        <tr>
            <td colspan="2">インターフェース</td>
            <td>MIPI CSI-2</td>
        </tr>
        <tr>
            <td colspan="2">フレームレート</td>
            <td>1080p60, 720p180, 480p206</td>
        </tr>
        <tr>
            <td colspan="2">レンズ</td>
            <td>フォーカス調整可能</td>
        </tr>
        <tr>
            <td colspan="2">視野角 (FOV)</td>
            <td>Up to 62°</td>
        </tr>
        <tr>
            <td colspan="2">ケーブルタイプ</td>
            <td>FFC (15 ピン)</td>
        </tr>
        <tr>
            <td colspan="2">ボード寸法</td>
            <td>25mm x 24mm</td>
        </tr>
        <tr>
            <td colspan="2">互換性</td>
            <td>D3-G および Rasbperry Pi (MIPI CSI-2 ポート経由)</td>
        </tr>
    </table>
</div>

AI-G でサポートされるセンサーの解像度と FPS は次のとおりです。
<p align="center"><strong>表 4.11 AI-G における IMX219 センサー解像度</strong></p>
<div align="center">
    <table>
        <tr>
            <td colspan="3" align="center"><strong>解像度</strong></td>
            <td align="center"><strong>FPS</strong></td>
            <td align="center"><strong>説明</strong></td>
        </tr>
        <tr>
            <td colspan="3">1920x1080</td>
            <td>30</td>
            <td>フル解像度フレームの中央領域をクロップして 1080p 画像を出力します</td>
        </tr>
        <tr>
            <td colspan="3">1640x1232</td>
            <td>30</td>
            <td>2×2 ピクセルビニングを利用して感度を高め、ノイズを低減します</td>
        </tr>
        <tr>
            <td colspan="3">640x480</td>
            <td>30</td>
            <td>2×2 ビニングと<strong>サブサンプリング</strong>を組み合わせ、読み出し時にピクセルを間引いてデータスループットを削減します</td>
        </tr>
    </table>
</div>

**注:** 表 4.11 に示すとおり、推論性能が大幅に低下するため、フル 3820×2464 解像度は使用しません。

<p align="center"><strong>表 4.12 動作モード別の最大解像度</strong></p>
<div align="center">
    <table>
        <tr>
            <td colspan="4" align="center"><strong>使用 CH.</strong></td>
            <td align="center"><strong>動作モード</strong></td>
            <td align="center"><strong>最大解像度</strong></td>
            <td align="center"><strong>入力フォーマット</strong></td>
        </tr>
        <tr>
            <td colspan="4">4CH</td>
            <td>デフォルトモード</td>
            <td>1280 x 720 @ 60fps</td>
            <td>RAW 24</td>
        </tr>
        <tr>
            <td colspan="4" rowspan="2">2CH</td>
            <td rowspan="2">メモリ共有モード</td>
            <td>オプション 1: 2048 x 1280 @ 60fps</td>
            <td>RAW 20</td>
        </tr>
        <tr>
            <td>オプション 2: 2592 x 2048 @ 30fps + 2048 x 1280 @ 30fps</td>
            <td>RAW 24</td>
        </tr>
        <tr>
            <td colspan="4">1CH</td>
            <td>メモリ共有モード</td>
            <td>2592 x 2048 @ 60fps</td>
            <td>RAW 20</td>
        </tr>
    </table>
</div>

#### 4.1.4.2 Yocto での IMX219 の有効化
AI-G SDK は既定で OV5647 が有効になるように構成されているため、ビルドの前に IMX219 を有効にする必要があります。  
SDK がすでにビルドされている場合と、初めてビルドする場合の 2 つのケースが考えられます。

##### 4.1.4.2.1 最初のビルドの前に IMX219 を有効化する
初回ビルドの場合は、以下の手順に従って IMX219 を有効にしてからビルドを実行します。
1. 環境設定スクリプトを source して、オプション 1 を選択します
    ```
    $ source poky/meta-topst/topst-build.sh
    ```
2. 以下のパスにある local.conf ファイルを開きます
    ```
    ${build_dir}/build/ai-g-topst-main/conf/local.conf
    ```
3. ov5647 の TOPST_CAM_MODULE エントリをコメントアウトし、imx219 のエントリを有効にします
    ```
    #TOPST_CAM_MODULE = "ov5647"
    TOPST_CAM_MODULE = "imx219"
    ```
4. ビルドを実行します
    ```
    $ bitbake telechips-topst-ai-image
    ```

##### 4.1.4.2.2 ビルドが既に完了した後に IMX219 を有効化する
既存のビルドでは、デフォルトで OV5647 センサーが有効に設定されています。以下の手順に従って IMX219 を有効にしてください。
1. 以下のパスにある local.conf ファイルを開きます
    ```
    ${build_dir}/build/ai-g-topst-main/conf/local.conf
    ```
2. ov5647 の TOPST_CAM_MODULE エントリをコメントアウトし、imx219 のエントリを有効にします
    ```
    #TOPST_CAM_MODULE = "ov5647"
    TOPST_CAM_MODULE = "imx219"
    ```
3. isp-server と isp-firmware に対して cleansstate を実行します
    ```
    $ bitbake -c cleansstate isp-firmware
    $ bitbake -c cleansstate isp-server
    ```
4. ビルドを実行します
    ```
    $ bitbake telechips-topst-ai-image
    ```

#### 4.1.4.3 Yocto での IMX219 解像度設定: ドライバ
Yocto のビルド過程で IMX219 センサーの解像度を変更するには、以下の手順に従ってください。

まず、imx219 を有効にするには、TOPST_CAM_MODULE = "imx219" が設定されていることを確認します
{build_dir}/build/ai-g-topst-main/conf/local.conf.

また、ビルド中にソースコードが削除されないように、次の行を有効にします
{build_dir}/build/ai-g-topst-main/conf/local.conf:
```
INHERIT:remove = “rm_work”
```

上記のオプションを有効にした後、次のコマンドでイメージを再ビルドしてください。
```
$ bitbake telechips-topst-ai-image
```
次に、ビルドが完了したら imx219.c ドライバファイルを開き、必要な修正を適用します。

次のディレクトリに移動してください。
```
${build_dir}/build/ai-g-topst-main /ai-g-topst/tmp/work/ai_g_topst-telechips-linux/linux-topst/5.10.223-r0/git/drivers/media/i2c/telechips/
```
コードを変更する前に、現在のドライバが次の 3 つのモードをサポートしていることに注意してください。
- 1920×1080 @ 30fps
- 1640×1232 @ 30fps
- 640×480 @ 30fps
各解像度はそれぞれ Mode 1、Mode 2、Mode 3 に対応します。

1920×1080 @ 30fps モードはセンタークロップを使用するため画角が狭くなり、640×480 モードは解像度が不十分です。これに対して 1640×1232 モードは 2×2 ビニングを使用し、より広い画角が得られるため、現在は既定のモードとして使用されています。  
imx219.c ドライバファイルを開き、imx219_set_default_format、imx219_open、imx219_probe の各関数内で以下に説明する箇所を修正します。
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

1920×1080 @ 30fps は Mode 1 に対応するため、3 つの関数内のすべての supported_modes の参照を **“supported_modes[1]”** に変更してください。  
1640×1232 @ 30fps モードは Mode 2 に対応するため、それに合わせて **“supported_modes[2]”** に置き換えてください。  
Mode 3 に対応する 640×480 @ 30fps の場合、すべての参照を **“supported_modes [3]”** に変更します。

3 番目に、カーネルを再ビルドして FAI イメージを生成します。  
ビルドディレクトリに戻り、以下のコマンドを使用してカーネルを再ビルドします。
```
$ cd ${build_dir}/build/ai-g-topst-main/
$ bitbake -C compile linux-topst
$ cd ${build_dir}
$ ./stitch-fai-ai.sh
```

その後、生成された output_aig.fai を FWDN でボードに書き込むと、希望する解像度で IMX219 センサーを使用できます。

#### 4.1.4.4 Yocto で IMX219 の FPS を上げる方法: ドライバとデバイスツリー
IMX219 センサーの説明によると、このセンサーは 1080p60、720p180、VGA206 などの高フレームレートモードをサポートします。したがって、imx219.c ドライバがサポートする解像度である 1920×1080、1640×1232、640×480 の FPS を上げることが可能です。AI-G プラットフォームの ISP コアは最大 60 fps をサポートするため、これらの解像度はそれぞれ最大 60 fps まで上げることができます。  

FPS を計算する式は次のとおりです。
<p align="center"><strong>{fps} = {pixel_rate}/{hts}x{vts}</strong></p>
したがって、FPS を上げるには pixel_rate、hts、vts の値を調整する必要があります。  
現在のドライバ実装では、pixel_rate と hts の両方が固定されています。FPS を上げるには、hts を一定に保ったまま pixel_rate を上げ、それに合わせて vts を調整して目的のフレームレートを得る方法しかありません。

FPS を 60 に変更するには、ドライバとデバイスツリーの両方を更新する必要があります。
FPS を 60 に変更するには、以下のガイドに従ってください。

##### 4.1.2.4.1 1920x1080 @ 60fps
60 fps を達成するには、次の関係が成り立つ必要があります。  
fps = pixel_rate / (hts × vts)
- pixel_rate = 182,400,000
- hts = 3448
- target fps = 60

必要な VTS は次のようになります。
- vts = pixel_rate / (hts × fps) = 182,400,000 / (3448 × 60) ≈ 882

ただし、VTS 値は 1080 より大きくなければならないため、この構成は有効ではありません。  
したがって、60 fps にするには hts を固定したまま、pixel_rate、vts および PLL_VT レジスタを調整する必要があります。

必要な変更は次のとおりです。
1. imx219.c ドライバファイル  
    A. ピクセルレートとリンク周波数を上げます
    ```
    #define IMX219_PIXEL_RATE            182400000    →   #define IMX219_PIXEL_RATE            278400000
    #define IMX219_DEFAULT_LINK_FREQ     456000000   →   #define IMX219_DEFAULT_LINK_FREQ     696000000
    ``` 
    B. 1080p モードの VTS 値を更新します:
    ```
    #define IMX219_VTS_30FPS_1080P       0x06e3       →   #define IMX219_VTS_30FPS_1080P       0x0542
    ```
    C. 1920x1080 モードテーブルの PLL_VT レジスタを変更します:
    ```
    // imx219_reg mode_1920_1080_regs[]
    {0x0307, 0x39}   →   {0x0307, 0x57}
    ```
2. tcc805x-videoinput-mipi0-imx219.dtsi デバイスツリーファイル  
    A. 新しいピクセルレートに合わせてリンク周波数を更新します:
    ```
    // &i2c7
    /bits/ 64 <456000000> → /bits/ 64 <696000000>
    ```
    B. hs-settle 値を更新します:
    ```
    hs-settle = <13> → hs-settle = <35>
    ```
3. カーネルを再ビルドし、FAI イメージを生成します。  
    ビルドディレクトリに戻り、以下のコマンドでカーネルを再ビルドします。
    ```
    $ cd ${build_dir}/build/d3-g-topst-main/
    $ bitbake -C compile linux-topst
    $ cd ${build_dir}
    $ ./stitch-fai-d3.sh
    ```
AI-G で以下のコマンドを使用すると、FPS の出力が 59.9 となり、これが 60 fps に相当することを確認できます。
```
$ v4l2-ctl --stream-mmap=3 --stream-count=300 --stream-to=/dev/null --verbose
```

##### 4.1.2.4.2 1640x1232 @ 60fps
60 fps を達成するには、次の関係が成り立つ必要があります。  
fps = pixel_rate / (hts × vts)
- pixel_rate = 182,400,000
- hts = 3448
- target fps = 60

必要な VTS は次のようになります。
- vts = pixel_rate / (hts × fps) = 182,400,000 / (3448 × 60) ≈ 882

ただし、VTS 値は 1080 より大きくなければならないため、この構成は有効ではありません。  
したがって、60 fps にするには hts を固定したまま、pixel_rate、vts および PLL_VT レジスタを調整する必要があります。

必要な変更は次のとおりです。
1. imx219.c ドライバファイル  
    A. ピクセルレートとリンク周波数を上げます
    ```
    #define IMX219_PIXEL_RATE            182400000    →   #define IMX219_PIXEL_RATE            278400000
    #define IMX219_DEFAULT_LINK_FREQ     456000000   →   #define IMX219_DEFAULT_LINK_FREQ     696000000
    ``` 
    B. 1640_1232 モードの VTS 値を更新します:
    ```
    #define IMX219_VTS_30FPS_BINNED       0x06e3       →   #define IMX219_VTS_30FPS_BINNED       0x0542
    ```
    C. 1920x1080 モードテーブルの PLL_VT レジスタを変更します:
    ```
    // imx219_reg mode_1640_1232_regs[]
    {0x0307, 0x39}   →   {0x0307, 0x57}
    ```
2. tcc805x-videoinput-mipi0-imx219.dtsi デバイスツリーファイル  
    A. 新しいピクセルレートに合わせてリンク周波数を更新します:
    ```
    // &i2c7
    /bits/ 64 <456000000> → /bits/ 64 <696000000>
    ```
    B. hs-settle 値を更新します:
    ```
    hs-settle = <13> → hs-settle = <34>
    ```
3. カーネルを再ビルドし、FAI イメージを生成します。  
    ビルドディレクトリに戻り、以下のコマンドでカーネルを再ビルドします。
    ```
    $ cd ${build_dir}/build/d3-g-topst-main/
    $ bitbake -C compile linux-topst
    $ cd ${build_dir}
    $ ./stitch-fai-d3.sh
    ```
AI-G で以下のコマンドを使用すると、FPS の出力が 59.9 となり、これが 60 fps に相当することを確認できます。
```
$ v4l2-ctl --stream-mmap=3 --stream-count=300 --stream-to=/dev/null --verbose
```

##### 4.1.2.4.3 640x480 @ 60fps
60 fps を達成するには、次の関係が成り立つ必要があります。  
fps = pixel_rate / (hts × vts)
- pixel_rate = 182,400,000
- hts = 3448
- target fps = 60

必要な VTS は次のようになります。
- vts = pixel_rate / (hts × fps) = 182,400,000 / (3448 × 60) ≈ 882

VTS 値が 480 より大きいため、条件を満たしています。前の例と同様に、HTS を固定したまま pixelrate と VTS を調整して FPS を変更します。  
pixelrate を変更せずに VTS 値のみを修正して FPS を調整することもできます。ただし、IMX219 の 0x0307 レジスタ値は変更してはなりません。

必要な変更は次のとおりです。
1. imx219.c ドライバファイル  
    A. ピクセルレートとリンク周波数を上げます
    ```
    #define IMX219_PIXEL_RATE            182400000    →   #define IMX219_PIXEL_RATE            278400000
    #define IMX219_DEFAULT_LINK_FREQ     456000000   →   #define IMX219_DEFAULT_LINK_FREQ     696000000
    ``` 
    B. 640_480 モードの VTS 値を更新します:
    ```
    #define IMX219_VTS_30FPS_640x480       0x06e3       →   #define IMX219_VTS_30FPS_640x480       0x0542
    ```
    C. 640x480 モードテーブルの PLL_VT レジスタを変更します:
    ```
    // imx219_reg mode_640_480_regs[]
    {0x0307, 0x39}   →   {0x0307, 0x57}
    ```
2. tcc805x-videoinput-mipi0-imx219.dtsi デバイスツリーファイル  
    A. 新しいピクセルレートに合わせてリンク周波数を更新します:
    ```
    // &i2c7
    /bits/ 64 <456000000> → /bits/ 64 <696000000>
    ```
    B. hs-settle 値を更新します:
    ```
    hs-settle = <13> → hs-settle = <26>
    ```
3. カーネルを再ビルドし、FAI イメージを生成します。  
    ビルドディレクトリに戻り、以下のコマンドでカーネルを再ビルドします。
    ```
    $ cd ${build_dir}/build/d3-g-topst-main/
    $ bitbake -C compile linux-topst
    $ cd ${build_dir}
    $ ./stitch-fai-d3.sh
    ```
AI-G で以下のコマンドを使用すると、FPS の出力が 59.9 となり、これが 60 fps に相当することを確認できます。
```
$ v4l2-ctl --stream-mmap=3 --stream-count=300 --stream-to=/dev/null --verbose
```

## 4.2 GMSL カメラセットアップガイド
### 4.2.1 D3-G GMSL カメラセットアップガイド
Deserializer ボードを使用すると、1 つの MIPI CSI ポートに最大 4 台のカメラを接続できます。D3-G は 2 つの MIPI CSI ポートを備えているため、次の構成のいずれかを選択できます。
- MIPI0 ポートで 4 台のカメラを使用します
- MIPI1 ポートで 4 台のカメラを使用します
- MIPI0 と MIPI1 の両方を使用して、合計 8 台のカメラを接続します

8 台のカメラをすべて構成する場合、最大 4 台のディスプレイをサポートする D3-G のディスプレイ拡張機能を、最大 3 台のディスプレイまで使用できます。

**注:** 本ガイドでは IMX290 (cxd5700) FHD GMSL カメラを使用します。  
別の GMSL カメラを使用する場合は、追加のカメラポーティングが必要になります。

#### 4.2.1.1 MIPI0 ポートの使用方法
まず、GMSL カメラと SerDes ボードの両方についてカーネル設定を有効にする必要があります。  
次の項目を追加します  
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
上記のオプションを変更した後、次のコマンドでイメージを再ビルドします。
```
$ bitbake -c cleansstate isp-firmware
$ bitbake -c cleansstate isp-server
$ bitbake telechips-topst-image
```
次に、カーネル内のデバイスツリーを変更する必要があります。以下のガイドに従って変更を適用し、イメージを再ビルドしてください。
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
7. カーネルを再ビルドし、FAI イメージを生成します。  
    ビルドディレクトリに戻り、以下のコマンドでカーネルを再ビルドします
    ```
    $ cd ${build_dir}/build/ai-g-topst-main/
    $ bitbake -C compile linux-topst
    $ cd ${build_dir}
    $ ./stitch-fai-ai.sh
    ```

上記のガイドに従ってビルドを完了すると、GMSL カメラは /dev/ 配下で video4、video5、video6、video7 として使用できます。

#### 4.2.1.2 MIPI1 ポートの使用方法
まず、GMSL カメラと SerDes ボードの両方についてカーネル設定を有効にする必要があります。  
次の項目を追加します  
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
上記のオプションを変更した後、次のコマンドでイメージを再ビルドします。
```
$ bitbake -c cleansstate isp-firmware
$ bitbake -c cleansstate isp-server
$ bitbake telechips-topst-image
```

次に、カーネル内のデバイスツリーを変更する必要があります。以下のガイドに従って変更を適用し、イメージを再ビルドしてください。
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
4. カーネルを再ビルドし、FAI イメージを生成します。  
    ビルドディレクトリに戻り、以下のコマンドでカーネルを再ビルドします。
    ```
    $ cd ${build_dir}/build/ai-g-topst-main/
    $ bitbake -C compile linux-topst
    $ cd ${build_dir}
    $ ./stitch-fai-ai.sh
    ```

上記のガイドに従ってビルドを完了すると、GMSL カメラは /dev/ 配下で video4、video5、video6、video7 として使用できます。

#### 4.2.1.3 MIPI0、1 ポートの使用方法
まず、GMSL カメラと SerDes ボードの両方についてカーネル設定を有効にする必要があります。  
次の項目を追加します  
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

上記のオプションを変更した後、次のコマンドでイメージを再ビルドします。
```
$ bitbake -c cleansstate isp-firmware
$ bitbake -c cleansstate isp-server
$ bitbake telechips-topst-image
```

VIOC において display と videoinput のパスが重複するため、4-display 拡張は使用できません。したがって、まず display 設定で競合するパスのいずれかを無効にする必要があります。
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

次に、カーネル内のデバイスツリーを変更する必要があります。以下のガイドに従って変更を適用し、イメージを再ビルドしてください。
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
5. カーネルを再ビルドし、FAI イメージを生成します。  
    ビルドディレクトリに戻り、以下のコマンドでカーネルを再ビルドします
    ```
    $ cd ${build_dir}/build/ai-g-topst-main/
    $ bitbake -C compile linux-topst
    $ cd ${build_dir}
    $ ./stitch-fai-ai.sh
    ```
上記のガイドに従ってビルドを完了すると、GMSL カメラは /dev/ 配下で video0、video1、video2、video3、4、video5、video6、video7 として使用できます。

### 4.2.2 AI-G GMSL カメラセットアップガイド
Deserializer ボードを使用すると、1 つの MIPI CSI ポートに最大 4 台のカメラを接続できます。  
AI-G ボードはレーンあたり 1.5 Gbps の MIPI CSI データ帯域幅を提供しており、最大 3 台の FHD カメラを同時に動作させることができます。これに従い、本ガイドでは 3 台の FHD GMSL カメラの接続について説明します。  
HD カメラの場合、最大 4 台までサポートできます。

**注:** 本ガイドでは IMX290 (cxd5700) FHD GMSL カメラを使用します。  
別の GMSL カメラを使用する場合は、追加のカメラポーティングが必要になります。

#### 4.2.2.1 MIPI CSI ポートの使用方法
まず、GMSL カメラと SerDes ボードの両方についてカーネル設定を有効にする必要があります。  
次の項目を追加します  
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
上記のオプションを変更した後、次のコマンドでイメージを再ビルドします。
```
$ bitbake -c cleansstate isp-firmware
$ bitbake -c cleansstate isp-server
$ bitbake telechips-topst-ai-image
```

次に、カーネル内のデバイスツリーを変更する必要があります。以下のガイドに従って変更を適用し、イメージを再ビルドしてください。
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
3. カーネルを再ビルドし、FAI イメージを生成します。  
    ビルドディレクトリに戻り、以下のコマンドでカーネルを再ビルドします
    ```
    $ cd ${build_dir}/build/ai-g-topst-main/
    $ bitbake -C compile linux-topst
    $ cd ${build_dir}
    $ ./stitch-fai-ai.sh
    ```
上記のガイドに従ってビルドを完了すると、GMSL カメラは /dev/ 配下で video0、video1、video2 として使用できます。

# 5. サンプルコードとコマンド
本章では、D3-G および AI-G プラットフォームで MIPI CSI カメラ、GMSL カメラ、USB カメラを使用する方法を示すサンプルコードとコマンドを提供します。本節では、カメラ再生方法の概要を簡単に説明します。  
D3-G では GStreamer または OpenCV を使用してカメラストリームを確認でき、  
AI-G ではアプリケーションフレームワークを通じてカメラ再生が処理されます。

## 5.1 カメラ再生用のサンプルコードとコマンド
### 5.1.1 MIPI CSI カメラユーザーガイド
本節では、Yocto と Ubuntu の両環境で MIPI CSI カメラの映像を表示する方法を説明します。

#### 5.1.1.1 D3-G での MIPI CSI カメラユーザーガイド (OV5647)
##### 5.1.1.1.1 Yocto イメージでの OV5647 の使用
[topst.ai DOCS ページ](https://topst.ai/tech/docs?page=624bd237b3013e87c05c125b8031e2f370ccca2b)で提供されている公式 Yocto イメージ、または Yocto を手動でビルドして生成したイメージを使用する場合、OV5647 カメラは既定の解像度 1296×972、30 fps で動作します。したがって、この環境でのカメラ再生は 1296×972、30 fps で行われます。  
以下の手順に従ってください。
1. 現在実行中の topst-welcome サービスを停止します
    ```
    $ sudo systemctl stop topst-welcome
    ```
2. UART コンソールで次のコマンドを入力します
    ```
    $ export XDG_RUNTIME_DIR=/run/user/root
    ```
3. 以下のように GStreamer コマンドを使用してカメラストリームを再生します
    ```
    $ gst-launch-1.0 v4l2src device=/dev/video0 io-mode=2 ! video/x-raw,format=NV12,width=1296,height=972,framerate=30/1 ! videoconvert ! waylandsink sync=false
    ```
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/accessories/Camera/5.1%201296%C3%97972%20ov5647%20camera%20out%20display%20on%20yocto.png"></p>
<p align="center"><strong>図 5.1 Yocto での 1296×972 OV5647 カメラ出力表示</strong></p>

**注:** 解像度は 1296×972 ですが、コマンドの末尾に fullscreen=true オプションを追加すると全画面で映像を再生できます。

##### 5.1.1.1.2 Ubuntu イメージでの OV5647 の使用
[topst.ai DOCS ページ](https://topst.ai/tech/docs?page=624bd237b3013e87c05c125b8031e2f370ccca2b)で提供されている公式 Ubuntu イメージを使用する場合、OV5647 カメラは既定の解像度 1296×972、30 fps で動作します。したがって、この環境でのカメラ再生は 1296×972、30 fps で行われます。  
以下の手順に従ってください。
1. - UART 経由で接続している場合: topst アカウントでログインした後、UART コンソールで次のコマンドを入力します
    ```
    $ export XDG_RUNTIME_DIR=/run/user/1000
    ```
    - ディスプレイ上で直接操作する場合: ターミナルウィンドウを開きます
2. 以下に示す GStreamer コマンドを使用してカメラストリームを再生します。Ubuntu ではハードウェアアクセラレーションによる Wayland レンダリングが利用できないため、代わりに H.265 エンコード/デコードを使用して VPU アクセラレーションによる再生を活用します
    ```
    $ gst-launch-1.0 v4l2src device=/dev/video0 io-mode=2 ! video/x-raw,format=NV12,width=1280,height=720,framerate=30/1 ! v4l2h265enc ! h265parse ! v4l2h265dec ! videoconvert ! waylandsink sync=false
    ```
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/accessories/Camera/5.2%201296%C3%97972%20ov5647%20camera%20out%20display%20on%20ubuntu.png"></p>
<p align="center"><strong>図 5.2 Ubuntu での 1296×972 OV5647 カメラ出力表示</strong></p>

**注:** 解像度は 1296×972 ですが、コマンドの末尾に fullscreen=true オプションを追加すると全画面で映像を再生できます。

GStreamer に加えて、OpenCV を使用してカメラストリームを表示することもできます。以下の手順に従うと、OpenCV でカメラ映像を簡単にプレビューできます。
1. OpenCV をインストールします
    ```
    $ sudo apt-get install python3-opencv
    ```
2. opencv_cam.py ファイル内に次のコードを記述します
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
3. Python で opencv_cam.py を実行します
    ```
    $ python3 opencv_cam.py
    ```
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/accessories/Camera/5.3%201296%C3%97972%20opencv%20ov5647%20camera%20out%20display%20on%20ubuntu.png"></p>
<p align="center"><strong>図 5.3 Ubuntu 上で OpenCV を使用して実行した 1296×972 OV5647 カメラ出力</strong></p>

##### 5.1.1.1.3 D3-G での解像度ごとの Gstreawmer パイプライン構成
各解像度に適した GStreamer パイプラインオプションを指定してから、カメラストリームを実行してください。
1. 1920x1080 @ 30fps
    ```
    $ gst-launch-1.0 v4l2src device=/dev/video0 io-mode=2 ! video/x-raw,format=NV12,width=1920,height=1080,framerate=30/1 ! videoconvert ! waylandsink sync=false
    ```
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/accessories/Camera/5.4%201920x1080%20ov5647%20camera%20out%20display%20on%20yocto.png"></p>
    <p align="center"><strong>図 5.4 Yocto での 1920x1080 OV5647 カメラ出力表示</strong></p>
2. 1296x972 @ 30fps
    ```
    $ gst-launch-1.0 v4l2src device=/dev/video0 io-mode=2 ! video/x-raw,format=NV12,width=1296,height=972,framerate=30/1 ! videoconvert ! waylandsink sync=false
    ```
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/accessories/Camera/5.1%201296%C3%97972%20ov5647%20camera%20out%20display%20on%20yocto.png"></p>
    <p align="center"><strong>図 5.5 Yocto での 1296x972 OV5647 カメラ出力表示</strong></p>
3. 640x480 @ 60fps
    ```
    $ gst-launch-1.0 v4l2src device=/dev/video0 io-mode=2 ! video/x-raw,format=NV12,width=640,height=480,framerate=60/1 ! videoconvert ! waylandsink sync=false
    ```
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/accessories/Camera/5.6%20640x480%20ov5647%20camera%20out%20display%20on%20yocto.png"></p>
    <p align="center"><strong>図 5.6 Yocto での 640x480 OV5647 カメラ出力表示</strong></p>

また、H.265 エンコーダおよびデコーダを使用するパイプラインを構成して、ハードウェアアクセラレーション再生を有効にすることもできます。
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

    解像度の変更については、セクション 4.1.2.2 を参照してください。

#### 5.1.1.2 D3-G での MIPI CSI カメラユーザーガイド (IMX219)
##### 5.1.1.2.1 Yocto イメージでの IMX219 の使用
[topst.ai DOCS ページ](https://topst.ai/tech/docs?page=624bd237b3013e87c05c125b8031e2f370ccca2b)で提供されている公式 Yocto イメージ、または Yocto を手動でビルドして生成したイメージを使用する場合、IMX219 カメラは既定の解像度 1640×1232、30 fps で動作します。したがって、この環境でのカメラ再生は 1640×1232、30 fps で行われます。  
以下の手順に従ってください。
1. 現在実行中の topst-welcome サービスを停止します
    ```
    $ sudo systemctl stop topst-welcome
    ```
2. UART コンソールで次のコマンドを入力します
    ```
    $ export XDG_RUNTIME_DIR=/run/user/root
    ```
3. 以下のように GSTreamer コマンドを使用してカメラストリームを再生します
    ```
    $ gst-launch-1.0 v4l2src device=/dev/video0 io-mode=2 ! video/x-raw,format=NV12,width=1640,height=1232,framerate=30/1 ! videoconvert ! waylandsink sync=false
    ```
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/accessories/Camera/5.7%201640x1232%20imx219%20camera%20out%20display%20on%20yocto.png"></p>
<p align="center"><strong>図 5.7 Yocto での 1640x972 IMX219 カメラ出力表示</strong></p>

**注:** 解像度は 1640×1232 ですが、コマンドの末尾に fullscreen=true オプションを追加すると全画面で映像を再生できます。

##### 5.1.1.2.2 Ubuntu イメージでの IMX219 の使用
[topst.ai DOCS ページ](https://topst.ai/tech/docs?page=624bd237b3013e87c05c125b8031e2f370ccca2b)で提供されている公式 Ubuntu イメージを使用する場合、IMX219 カメラは既定の解像度 1640×1232、30 fps で動作します。したがって、この環境でのカメラ再生は 1640×1232、30 fps で行われます。  
以下の手順に従ってください。
1. - UART 経由で接続している場合: topst アカウントでログインした後、UART コンソールで次のコマンドを入力します
    ```
    $ export XDG_RUNTIME_DIR=/run/user/1000
    ```
    - ディスプレイ上で直接操作する場合: ターミナルウィンドウを開きます
2. 以下に示す GStreamer コマンドを使用してカメラストリームを再生します。Ubuntu ではハードウェアアクセラレーションによる Wayland レンダリングが利用できないため、代わりに H.265 エンコード/デコードを使用して VPU アクセラレーションによる再生を活用します
    ```
    $ gst-launch-1.0 v4l2src device=/dev/video0 io-mode=2 ! video/x-raw,format=NV12,width=1600,height=1200,framerate=30/1 ! v4l2h265enc ! h265parse ! v4l2h265dec ! videoconvert ! waylandsink sync=false
    ```
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/accessories/Camera/5.8%201640x1232%20imx219%20camera%20out%20display%20on%20ubuntu.png"></p>
<p align="center"><strong>図 5.8 Ubuntu での 1640x972 IMX219 カメラ出力表示</strong></p>

**注:** 解像度は 1640×1232 ですが、コマンドの末尾に fullscreen=true オプションを追加すると全画面で映像を再生できます。

GStreamer に加えて、OpenCV を使用してカメラストリームを表示することもできます。以下の手順に従うと、OpenCV でカメラ映像を簡単にプレビューできます。
1. OpenCV をインストールします
    ```
    $ sudo apt-get install python3-opencv
    ```
2. opencv_cam.py ファイル内に次のコードを記述します。
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
3. Python で opencv_cam.py を実行します
```
$ python3 opencv_cam.py
```
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/accessories/Camera/5.9%201640x1232%20opencv%20imx219%20camera%20out%20display.png"></p>
<p align="center"><strong>図 5.9 Ubuntu 上で OpenCV を使用して実行した 1640×1232 IMX219 カメラ出力</strong></p>

##### 5.1.1.2.3 D3-G での解像度ごとの GStreamer パイプライン構成
各解像度に適した GStreamer パイプラインオプションを指定してから、カメラストリームを実行してください。
1. 1920x1080 @ 30fps
    ```
    $ gst-launch-1.0 v4l2src device=/dev/video0 io-mode=2 ! video/x-raw,format=NV12,width=1920,height=1080,framerate=30/1 ! videoconvert ! waylandsink sync=false
    ```
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/accessories/Camera/5.10%201920x1080%20imx219%20camera%20out%20display%20on%20yocto.png"></p>
    <p align="center"><strong>図 5.10 Yocto での 1920x1080 IMX219 カメラ出力表示</strong></p>
2. 1640x1232 @ 30fps
    ```
    $ gst-launch-1.0 v4l2src device=/dev/video0 io-mode=2 ! video/x-raw,format=NV12,width=1640,height=1232,framerate=30/1 ! videoconvert ! waylandsink sync=false
    ```
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/accessories/Camera/5.7%201640x1232%20imx219%20camera%20out%20display%20on%20yocto.png"></p>
    <p align="center"><strong>図 5.11 Yocto での 1620x1232 IMX219 カメラ出力表示</strong></p>
3. 640x480 @ 30fps
    ```
    $ gst-launch-1.0 v4l2src device=/dev/video0 io-mode=2 ! video/x-raw,format=NV12,width=640,height=480,framerate=30/1 ! videoconvert ! waylandsink sync=false
    ```
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/accessories/Camera/5.12%20640x480%20imx219%20camera%20out%20display%20on%20yocto.png"></p>
    <p align="center"><strong>図 5.12 Yocto での 640x480 IMX219 カメラ出力表示</strong></p>

また、H.265 エンコーダおよびデコーダを使用するパイプラインを構成して、ハードウェアアクセラレーション再生を有効にすることもできます。
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

解像度の変更については、4.1.3.3 節を参照してください。

#### 5.1.1.3 AI-G での MIPI CSI カメラユーザーガイド (OV5647)
##### 5.1.1.3.1 Yocto イメージでの OV5647 の使用
AI-G では 2 つのアプリケーションが利用できます。1 つは推論結果を含むカメラ再生用、もう 1 つは単純なカメラ表示用です。用途に応じてどちらのアプリケーションでも選択できます。
- tcnnapp
    ```
    $ tcnnapp
    ```
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/accessories/Camera/5.13%20ov5647%20camera%20out%20display%20with%20running%20tcnnapp%20on%20yocto.png"></p>
    <p align="center"><strong>図 5.13 Yocto で tcnnapp を実行した際の OV5647 カメラ出力表示</strong></p>
- tcnncameraapp
    ```
    $ tcnncameraapp
    ```
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/accessories/Camera/5.14%20ov5647%20camera%20out%20display%20with%20running%20tcnncameraapp%20on%20yocto.png"></p>
    <p align="center"><strong>図 5.14 Yocto で tcnncameraapp を実行した際の OV5647 カメラ出力表示</strong></p>

##### 5.1.1.3.2 Ubuntu イメージでの使用
AI-G では 2 つのアプリケーションが利用できます。1 つは推論結果を含むカメラ再生用、もう 1 つは単純なカメラ表示用です。用途に応じてどちらのアプリケーションでも選択できます。
- tcnnapp
    ```
    $ tcnnapp
    ```
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/accessories/Camera/5.13%20ov5647%20camera%20out%20display%20with%20running%20tcnnapp%20on%20yocto.png"></p>
    <p align="center"><strong>図 5.15 Ubuntu で tcnnapp を実行した際の OV5647 カメラ出力表示</strong></p>
- tcnncameraapp
    ```
    $ tcnncameraapp
    ```
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/accessories/Camera/5.14%20ov5647%20camera%20out%20display%20with%20running%20tcnncameraapp%20on%20yocto.png"></p>
    <p align="center"><strong>図 5.16 Ubuntu で tcnncameraapp を実行した際の OV5647 カメラ出力表示</strong></p>

#### 5.1.1.4 AI-G での MIPI CSI カメラユーザーガイド (IMX219)
##### 5.1.1.4.1 Yocto イメージでの IMX219 の使用
AI-G では 2 つのアプリケーションが利用できます。1 つは推論結果を含むカメラ再生用、もう 1 つは単純なカメラ表示用です。用途に応じてどちらのアプリケーションでも選択できます。
- tcnnapp
    ```
    $ tcnnapp
    ```
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/accessories/Camera/5.17%20imx219%20camera%20out%20display%20with%20running%20tcnnapp%20on%20yocto.png"></p>
    <p align="center"><strong>図 5.17 Yocto で tcnnapp を実行した際の OV5647 カメラ出力表示</strong></p>
- tcnncameraapp
    ```
    $ tcnncameraapp
    ```
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/accessories/Camera/5.18%20imx219%20camera%20out%20display%20with%20running%20tcnncameraapp%20on%20yocto.png"></p>
    <p align="center"><strong>図 5.18 Yocto で tcnncameraapp を実行した際の OV5647 カメラ出力表示</strong></p>

##### 5.1.1.4.2 Ubuntu イメージでの IMX219 の使用
AI-G では 2 つのアプリケーションが利用できます。1 つは推論結果を含むカメラ再生用、もう 1 つは単純なカメラ表示用です。用途に応じてどちらのアプリケーションでも選択できます。
- tcnnapp
    ```
    $ tcnnapp
    ```
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/accessories/Camera/5.17%20imx219%20camera%20out%20display%20with%20running%20tcnnapp%20on%20yocto.png"></p>
    <p align="center"><strong>図 5.17 Yocto で tcnnapp を実行した際の OV5647 カメラ出力表示</strong></p>
- tcnncameraapp
    ```
    $ tcnncameraapp
    ```
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/accessories/Camera/5.18%20imx219%20camera%20out%20display%20with%20running%20tcnncameraapp%20on%20yocto.png"></p>
    <p align="center"><strong>図 5.18 Yocto で tcnncameraapp を実行した際の OV5647 カメラ出力表示</strong></p>

### 5.1.2 GMSL カメラユーザーガイド
本節では、Yocto と Ubuntu の両環境で GMSL カメラの映像を表示する方法を説明します。

#### 5.1.2.1 D3-G での GMSL カメラユーザーガイド
##### 5.1.2.1.1 Yocto イメージでの GMSL カメラの使用
[topst.ai DOCS ページ](https://topst.ai/tech/docs?page=624bd237b3013e87c05c125b8031e2f370ccca2b)で提供されている公式 Yocto イメージ、または Yocto を手動でビルドして生成したイメージを使用する場合、GMSL カメラは既定の解像度 1920×1080、30 fps で動作します。したがって、この環境でのカメラ再生は 1920×1080、30 fps で行われます。  
以下の手順に従ってください。
1. 現在実行中の topst-welcome サービスを停止します
    ```
    $ sudo systemctl stop topst-welcome
    ```
2. UART コンソールで次のコマンドを入力します
    ```
    $ export XDG_RUNTIME_DIR=/run/user/root
    ```
3. 以下のように GStreamer コマンドを使用してカメラストリームを再生します
    ```
    $ gst-launch-1.0 v4l2src device=/dev/video4 io-mode=2 ! video/x-raw,format=NV12,width=1920,height=1080,framerate=30/1 ! videoconvert ! waylandsink sync=false
    ```

また、以下のスクリプトを実行すると、gpu を使用してカメラ映像を 4 分割表示できます。
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

GMSL カメラは video4、video5、video6、video7 として表示され、必要に応じてこれらのデバイスのいずれかを選択できます。  
8 台のカメラを接続した場合、システムはそれらを video0 から video8 として列挙し、これらのデバイスノードのいずれかを選択できます。

##### 5.1.2.1.2 Ubuntu イメージでの GMSL カメラの使用
[topst.ai DOCS ページ](https://topst.ai/tech/docs?page=624bd237b3013e87c05c125b8031e2f370ccca2b)で提供されている公式 Ubuntu イメージを使用する場合、GMSL カメラは既定の解像度 1920×1080、30 fps で動作します。したがって、この環境でのカメラ再生は 1920×1080、30 fps で行われます。  
以下の手順に従ってください。
1. - UART 経由で接続している場合: topst アカウントでログインした後、UART コンソールで次のコマンドを入力します
    ```
    $ export XDG_RUNTIME_DIR=/run/user/1000
    ```
    - ディスプレイ上で直接操作する場合: ターミナルウィンドウを開きます
2. 以下に示す GStreamer コマンドを使用してカメラストリームを再生します。Ubuntu ではハードウェアアクセラレーションによる Wayland レンダリングが利用できないため、代わりに H.265 エンコード/デコードを使用して VPU アクセラレーションによる再生を活用します
    ```
    $ gst-launch-1.0 v4l2src device=/dev/video0 io-mode=2 ! video/x-raw,format=NV12,width=1920,height=1080,framerate=30/1 ! v4l2h265enc ! h265parse ! v4l2h265dec ! videoconvert ! waylandsink sync=false
    ```

また、以下のスクリプトを実行すると、gpu を使用してカメラ映像を 4 分割表示できます。
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

さらに、OpenCV を使用してカメラストリームを表示することもできます。以下の手順に従うと、OpenCV でカメラ映像を簡単にプレビューできます。
1. OpenCV をインストールします
    ```
    $ sudo apt-get install python3-opencv
    ```
2. opencv_cam.py ファイル内に次のコードを記述します
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
3. Python で opencv_cam.py ファイルを実行します
    ```
    $ python3 opencv_cam.py
    ```

GMSL カメラは video4、video5、video6、video7 として表示され、必要に応じてこれらのデバイスのいずれかを選択できます。  
8 台のカメラを接続した場合、システムはそれらを video0 から video8 として列挙し、これらのデバイスノードのいずれかを選択できます。

#### 5.1.2.2 AI-G での GMSL カメラユーザーガイド
##### 5.1.2.2.1 Yocto イメージでの GMSL カメラの使用
AI-G では 2 つのアプリケーションが利用できます。1 つは推論結果を含むカメラ再生用、もう 1 つは単純なカメラ表示用です。用途に応じてどちらのアプリケーションでも選択できます。
- tcnnapp
- tcnncameraapp

GMSL カメラは **video0**、**video1**、**video2** として表示され、必要に応じてこれらのデバイスのいずれかを選択できます。
各アプリケーションはデフォルトで video2 を使用しますが、**-p オプション**を使用してビデオデバイスを変更できます。
以下の例では、**video0** を選択する方法を示します。

- tcnnapp
    ```
    $ tcnnapp -p /dev/video0
    ```
- tcnncameraapp
    ```
    $ tcnncameraapp -p /dev/video0
    ```

##### 5.1.2.2.2 Ubuntu イメージでの GMSL カメラの使用
AI-G では 2 つのアプリケーションが利用できます。1 つは推論結果を含むカメラ再生用、もう 1 つは単純なカメラ表示用です。用途に応じてどちらのアプリケーションでも選択できます。
- tcnnapp
- tcnncameraapp

GMSL カメラは **video0**、**video1**、**video2** として表示され、必要に応じてこれらのデバイスのいずれかを選択できます。
各アプリケーションはデフォルトで video2 を使用しますが、**-p オプション**を使用してビデオデバイスを変更できます。
以下の例では、**video0** を選択する方法を示します。

- tcnnapp
    ```
    $ tcnnapp -p /dev/video0
    ```
- tcnncameraapp
    ```
    $ tcnncameraapp -p /dev/video0
    ```

### 5.1.3 USB カメラユーザーガイド
本節では、Yocto と Ubuntu の両環境で USB カメラの映像を表示する方法を説明します。
AI-G には USB インタフェースが搭載されていないため、このプラットフォーム向けの USB カメラガイドは提供されません。

#### 5.1.3.1 D3-G での USB カメラユーザーガイド
本書では、1920×1080 で 30 fps をサポートする USB カメラを基準に説明します

**注:** MIPI カメラはデフォルトで **/dev/video0** に割り当てられるため、USB カメラは /dev/video1 として作成されます。
USB カメラを動作させる際は、必ず **/dev/video1** を使用してください。

##### 5.1.3.1.1 Yocto イメージでの USB カメラの使用
[topst.ai DOCS ページ](https://topst.ai/tech/docs?page=624bd237b3013e87c05c125b8031e2f370ccca2b)で提供されている公式 Yocto イメージ、または Yocto を手動でビルドして生成したイメージを使用する場合、USB カメラはカメラ自体の仕様で定義された解像度とフレームレートで動作します。したがって、映像は USB カメラが提供する既定の解像度と FPS で再生されます。  
以下の手順に従ってください。
1. 現在実行中の topst-welcome サービスを停止します
    ```
    $ sudo systemctl stop topst-welcome
    ```
2. UART コンソールで次のコマンドを入力します
    ```
    $ export XDG_RUNTIME_DIR=/run/user/root
    ```
3. 以下のように GStreamer コマンドを使用してカメラストリームを再生します。v4l2-ctl -d /dev/video1 --list-formats-ext で USB カメラ情報を確認すると、サポートされるフォーマットは MJPEG と表示されます。したがって、jpegdec を使用します
    ```
    $ gst-launch-1.0 v4l2src device=/dev/video1 ! image/jpeg,width=1920,height=1080 ! jpegdec ! videoconvert ! waylandsink
    ```

##### 5.1.3.1.2 Ubuntu イメージでの USB カメラの使用
[topst.ai DOCS ページ](https://topst.ai/tech/docs?page=624bd237b3013e87c05c125b8031e2f370ccca2b)で提供されている公式 Ubuntu イメージ、または手動で生成したイメージを使用する場合、USB カメラはカメラ自体の仕様で定義された解像度とフレームレートで動作します。したがって、映像は USB カメラが提供する既定の解像度と FPS で再生されます。  
以下の手順に従ってください。
1. - UART 経由で接続している場合: topst アカウントでログインした後、UART コンソールで次のコマンドを入力します
    ```
    $ export XDG_RUNTIME_DIR=/run/user/1000
    ```
    - ディスプレイ上で直接操作する場合: ターミナルウィンドウを開きます
2. 以下のように GStreamer コマンドを使用してカメラストリームを再生します。v4l2-ctl -d /dev/video1 --list-formats-ext で USB カメラ情報を確認すると、サポートされるフォーマットは MJPEG と表示されます。したがって、jpegdec を使用します
    ```
    $ gst-launch-1.0 v4l2src device=/dev/video1 ! image/jpeg,width=1920,height=1080 ! jpegdec ! videoconvert ! waylandsink
    ```
3. H.265 のエンコードおよびデコードを使用するには、v4l2src がサポートする NV12 フォーマットに映像を変換する必要があります。したがって、以下のようにパイプラインを構成してください
    ```
    $ gst-launch-1.0 v4l2src device=/dev/video1 io-mode=2 ! image/jpeg,width=640,height=480,framerate=30/1 ! jpegdec ! videoconvert ! video/x-raw,format=NV12 !  v4l2h265enc ! h265parse ! v4l2h265dec ! videoconvert ! waylandsink
    ```

**注:** コマンドの末尾に fullscreen=true オプションを追加すると全画面で映像を再生できます。

GStreamer に加えて、OpenCV を使用してカメラストリームを表示することもできます。以下の手順に従うと、OpenCV でカメラ映像を簡単にプレビューできます。
1. OpenCV をインストールします
    ```
    $ sudo apt-get install python3-opencv
    ```
2. opencv_cam.py ファイル内に次のコードを記述します
    ```
    import cv2

    cap = cv2.VideoCapture(1)

    if not cap.isOpened():
        print("\\@@ Camera open failed!")
        exit()

    print("カメラウィンドウを終了するには 'q' を押してください。")

    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

    while True:
        ret, frame = cap.read()
        if not ret:
            print("フレームの読み込みに失敗しました")
            break

        cv2.imshow("Camera Feed", frame)

        # 'q' キーが押されたら終了します
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
    ```
3. Python で opencv_cam.py を実行します
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

    print("パイプラインを開いています...")
    cap = cv2.VideoCapture(pipeline, cv2.CAP_GSTREAMER)

    if not cap.isOpened():
        print("パイプラインのオープンに失敗しました")
        exit()

    print("カメラウィンドウを終了するには 'q' を押してください。")

    while True:
        ret, frame = cap.read()
        if not ret:
            print("フレームの読み込みに失敗しました")
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

# 6. トラブルシューティング
第 6 章では、MIPI CSI カメラ、GMSL カメラ、USB カメラのトラブルシューティングについて説明します。

## 6.1 MIPI CSI および GMSL カメラのトラブルシューティング
MIPI CSI または GMSL カメラで問題が発生した場合は、以下のデバッグガイドを参照して問題を解決してください。

### 6.1.1 起動時の問題 (プローブ段階)
#### 6.1.1.1 センサープローブの失敗
**症状**
- 起動時にセンサーが検出されない
- /dev/videoX ノードが作成されない
- ‘media-ctrl -p’ の出力にセンサーエンティティが表示されない  

**dmesg ログの例**
```
[    3.421000] imx219 2-0010: probing sensor failed
[    3.421120] imx219 2-0010: i2c read failed: addr=0x3000, ret=-5
[    3.200400] imx219 0-0010: reset gpio request failed
[    2.912830] imx219 1-0010: failed to get vddio regulator
```
**考えられる原因**
- I2C アドレスまたはバス構成の誤り
- RESET/PWDN GPIO の極性の誤り
- レギュレータ電源が欠落しているか、正しく構成されていない

**解決方法**
- デバイスツリーの I2C アドレス、バス番号、GPIO 設定を確認してください
- レギュレータノードの欠落や誤った定義がないか確認してください
- センサーモジュールのケーブルの向きとピンの位置を再確認してください

#### 6.1.1.2 I2C 通信の失敗
**dmesg ログの例**
```
[    3.101001] imx219 2-0010: i2c read error: -121
[    4.112121] i2c i2c-2: transfer failed: -110
```
**考えられる原因**
- SDA/SCL ラインが短絡している、または断線している
- デバイスツリーの I2C バス番号が実際のハードウェア構成と一致していない

**解決方法**
- “i2cdetect -y <bus>” を使用して、センサーが想定される I2C アドレスで応答するか確認してください
- ケーブルとコネクタに損傷、挿入不良、接触の緩みがないか点検してください

### 6.1.2 メディアコントローラおよびグラフ構成の問題
(‘media-ctl -p’ を使用して確認)

#### 6.1.2.1 センサーエンティティの欠落またはリンクの未設定
**'media-ctl -p' の出力例**
```
0 entities, 0 interfaces, 0 pads, 0 links
```
**考えられる原因**
- デバイスツリーにエンドポイント（port）ノードがない
- レーン数または ‘bus-type’ 設定の誤り
- ‘link-frequencies’ エントリの欠落

**解決方法**
- ‘port@0/1’ エンドポイント定義が正しいことを確認してください
- ‘data-lanes’ 配列の順序とレーン数が正しいか確認してください
- ‘link-frequencies’ がセンサーの仕様と一致していることを確認してください

#### 6.1.2.2 フォーマット / モードの不一致
**考えられる原因**
- センサードライバの ‘supported_mode[]’ が、DTS で定義された ‘hs-settle’ の値と一致していない
- ドライバとデバイスツリー間で CSI-2 レーン数が一致していない

**解決方法**
- ‘supported_modes[]’ の解像度、ピクセルレート、HTS/VTS の値を確認し、それに応じて DTS の ‘hs-settle’ の値を調整してください
- DTS の設定とセンサードライバの設定に整合性があることを確認してください

### 6.1.3 V4L2 ストリーミングの問題
#### 6.1.3.1 VIDIOC_STREAMON の失敗 (ストリーミングを開始できない)
**考えられる原因**
- センサーレジスタ設定の誤り
- ピクセルレートまたは PLL 設定が期待値と一致していない
- フレームタイミングが不正になる HTS/VTS の競合

**解決方法**
- センサーのモードテーブルにあるピクセルレート、VTS、HTS の値を再検証してください
- PLL 分周値（0x030x レジスタ）が正しいか確認してください
- 選択した解像度と FPS に対して、デバイスツリーに正しい ‘hs-settle’ の値が指定されていることを確認してください。

#### 6.1.3.2 サポートされていないフォーマットの要求
**解決方法**
- 以下のコマンドで実際にサポートされているフォーマットを確認し、サポートされているフォーマットでストリーミングを再試行してください:
    ```
    V4l2-ctl –list-formats-ext
    ```

### 6.1.4 CSI-2 エラー: SoT、CRC および関連する問題
#### 6.1.4.1 SoT (Sync on Transmission) エラー
**考えられる原因**
- MIPI タイミング設定の不一致
- ピクセルレートの設定が高すぎる
- ケーブル品質の低さ、またはケーブル長の過大

**解決方法**
- ピクセルレートまたはリンク周波数を下げてください
- ケーブルを交換するか、長さを短くしてください
- MIPI タイミングパラメータを確認してください

#### 6.1.4.2 CRC エラー
**dmesg ログの例**
```
[   13.700910] tccvin videoinput0: CSI-2 ERROR: CRC error
```
**考えられる原因**
- MIPI 信号品質の劣化
- PLL またはレーン速度の不一致

**解決方法**
- hs-settle 値を調整します
- ケーブルを交換してください
- PLL 構成とレーン速度の設定を確認してください

### 6.1.5 ピクセルレート / リンク周波数のエラー
**考えられる原因**
- 利用可能な CSI-2 レーン帯域幅の超過
- PLL 構成の誤り

**解決方法**
- ピクセルレートを再計算し、許容される CSI-2 帯域幅内に収まることを確認してください
- 有効なタイミングになるように PLL 分周比を調整します
- 必要に応じて、フレームレートを下げる（例: 30 -> 15fps）か解像度を下げてください

### 6.1.6 デバイスツリー (DTS) の構成エラー
#### 6.1.6.1 互換性のない compatible 文字列
**考えられる原因**
- DTS の ‘compatible’ の値が、センサードライバで定義された ‘of_device_id’ と一致していない
- ドライバがデバイスノードを認識せず、プローブが実行されない

**解決方法**
- センサードライバで定義されている正確な ‘compatible’ 文字列（例: “sony,imx219”）で DTS を更新してください
- デバイスツリーを再ビルドし、センサーが正しくプローブされることを確認してください

#### 6.1.6.2 エンドポイント構成の問題
**考えられる原因**
- センサーエンドポイントと CSI エンドポイントの間でポート番号または ‘remote-endpoint’ の参照が一致していない
- ‘data-lanes’ またはバス構成がメディアグラフの要件を満たしていない

**解決方法**
- 両側のポート番号、‘data-lanes’、‘remote-endpoint’ の値が一致していることを確認してください
- ‘media-ctl -p’ を使用して、メディアリンクが正しく確立されていることを確認してください

#### Link-Frequencies プロパティの欠落
**考えられる原因**
- エンドポイントに ‘link-frequencies’ フィールドがないため、MIPI リンク速度を計算できない
- 値のフォーマット（例: /bits/ 64）がドライバの期待するものと一致していない

**解決方法**
- センサーの仕様に従って正しい ‘link-frequencies’ 値 (例: 456000000) を追加します
- 値のフォーマットがドライバの要件と一致していることを確認してください（必要に応じて /bits/ 64 を含めるなど）

### 6.1.7 Gstreamer 再生の問題
#### 6.1.7.1 'not negotiated' エラー
**考えられる原因**
- パイプライン内での Caps ネゴシエーションの失敗
- Wayland コンポジタのフォーマット不一致
- videoconvert が特定の raw フォーマットを処理できない

**解決方法**
- 幅広い互換性を持つ NV12 または YUY2 ベースのパイプラインを使用してください
- ‘v4l2src io-mode=dmabuf’ を利用して、ゼロコピーのバッファ処理と適切なフォーマットネゴシエーションを確保してください

#### 6.1.7.2 Wayland シンクの初期化失敗
**考えられる原因**
- Wayland コンポジタが動作していない、またはアクセス可能なディスプレイ環境がない
- パイプラインが SSH 経由、または無効な DISPLAY/Wayland 環境で起動されているため、シンクを初期化できない

**解決方法**
- Weston コンポジタが動作していることを確認してください
- ローカルセッション内、または適切に構成された Wayland 環境でパイプラインを実行してください

### 6.1.8 ハードウェアの問題
#### 6.1.8.1 ケーブルの向きの誤り
**考えられる原因**
- FFC ケーブルの向きが逆、またはピンがずれているため、I2C/MIPI 信号が正しく伝送されない
- センサーがまったく応答せず、フレームを受信できない

**解決方法**
- コネクタの向きを確認し、接点ピンが仕様どおりに整列していることを確認してください
- ケーブルの損傷や接点の摩耗がないか確認してください

#### 6.1.8.2 電源供給の問題
**考えられる原因**
- センサーの電源レール（例: 1.2V / 2.8V）が不安定、または有効になっていない
- 電源イネーブル GPIO がアサートされていない
- 初期化時にセンサーのパワーアップシーケンスが満たされていない

**解決方法**
- DTS のレギュレータおよび GPIO の設定を確認し、必要なすべての電圧が正しく供給されていることを確認してください
- センサーの電源シーケンス要件が満たされていることを確認してください（RESET _> PWDN -> clock enable）

## 6.2 USB カメラのトラブルシューティング
USB Camera で問題が発生した場合は、以下のデバッグガイドを参照して問題を解決してください。

### 6.2.1 カメラが検出されない (USB デバイスが認識されない)
**dmesg ログの例**
```
usb 1-1: device descriptor read/64, error -71
uvcvideo: Failed to initialize the device
```
**考えられる原因**
- USB 電源の不足または電源供給の不安定により、デバイスの初期化に失敗する
- USB ケーブルまたはポートの不良、あるいは非対応の USB ハブの使用

**解決方法**
- 別の USB ポートを試すか、安定した電源を供給できるポートを使用してください
- USB ケーブルまたはハブを交換し、デバイスを再接続して正しく列挙されることを確認してください

### 6.2.2 v4l2-ctl でフォーマット一覧が制限される、または空になる
**dmesg ログの例**
```
uvcvideo: Failed to query (GET_DEF) UVC control 2 on unit 1: -32
```
**考えられる原因**
- カメラが特定の UVC コントロールに対応していない、または初期化時にそれらを報告しない
- デバイスとドライバ間のプロトコルエラーにより、機能の検出ができない

**解決方法**
- MJPEG や YUYV などの標準フォーマットでテストしてください
- 同じモデルの別のカメラでテストし、UVC の互換性に起因する問題かどうかを判断してください

### 6.2.3 GStreamer 再生: "not negotiated" または Caps の不一致
**考えられる原因**
- パイプラインがカメラの非対応フォーマット（例: NV12、YUY2）を要求しているため、caps ネゴシエーションに失敗する
- 選択した解像度/フレームレートではカメラが MJPEG のみを提供する場合がありますが、パイプラインは raw フォーマットを要求します
- カメラは MJPEG を出力しているが、JPEG デコーダエレメント（jpegdec または avdec_mjpeg）が含まれていないため、デコードできない

**解決方法**
- サポートされているフォーマットを確認してください
    ```
    v4l2-ctl –list-formats-ext
    ```
- カメラが MJPEG を出力する場合:
    ```
    v4l2src ! image/jpeg ! jpegdec ! videoconvert ! …
    ```
- カメラが raw フォーマット（例: YUYV）に対応している場合は、パイプラインの caps をそれに合わせて構成してください:  
    ‘v4l2-ctl –list-formats-ext’ に表示されているとおりの raw フォーマットを使用してください

### 6.2.4 解像度または FPS の設定失敗
**考えられる原因**
- 要求された解像度またはフレームレートにカメラが対応していないため、ネゴシエーションに失敗する

**解決方法**
- ‘v4l2-ctl –list-formats-ext’ を使用して、サポートされている解像度/FPS の組み合わせを確認してください

### 6.2.5 映像のカクつき / フレームドロップ
**考えられる原因**
- USB 帯域幅の不足（ハブの共有または USB 2.0 ポートの使用）
- MJPEG デコードによる CPU 負荷が高く、パイプラインの処理が遅れる

**解決方法**
- USB 3.0 ポートを使用するか、ハブを介さずにカメラを直接接続してください
- MJPEG の解像度またはフレームレートを下げるか、対応している場合は raw フォーマットに切り替えてください

### 6.2.6 色の異常または出力の破損
**考えられる原因**
- MJPEG -> NV12 変換または色空間変換中のエラー
- v4l2convert または videoconvert で特定のフォーマットの組み合わせが失敗する場合があります

**解決方法**
- videoconvert の前に jpegdec または avdec_mjpeg を明示的に挿入してください
- テストのためにパイプラインを簡素化してください。例:
    ```
    V4l2src ! jpegdec ! videoconvert ! waylandsink
    ```

### 6.2.7 予期しないデバイスの切断または再列挙
**dmesg ログの例**
```
usb 1-1: USB disconnect, device number 4
```
**考えられる原因**
- 電源供給の不安定さ、またはケーブルの接触不良
- 長時間の使用中に熱の問題でデバイスがリセットされる

**解決方法**
- USB ケーブルを交換するか、安定して十分な電力を供給できるポートを使用してください
- 発熱の大きいカメラでは、追加の冷却対策を検討してください
