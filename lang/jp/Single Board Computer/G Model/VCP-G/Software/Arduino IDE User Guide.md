# 1. はじめに
---
このドキュメントでは、TCC7045をベースとした自動車アプリケーション向けに設計された強力で効率的なプロセッサであるTOPST Vehicle Control Processor (VCP) 用のArduino IDEの使用方法について説明します。目標は、VCP-GをArduino環境と統合して、自動車用半導体に特化したArduinoのシンプルさと柔軟性に匹敵する開発環境を提供し、開発プロセスを簡素化および迅速化することです。
 
このドキュメントには、次の情報が含まれています。
- インストールガイド
 
</br></br></br></br>
 
# 2. インストールガイド
---
この章では、Arduino統合開発環境 (IDE) で使用するためのVCP-G Arduinoパッケージをダウンロードしてインストールする方法について説明します。
 
</br></br></br>
 
## 2.1 インストールガイド
---
**ステップ 1: Arduino IDEのダウンロード**
 
まず、Arduinoボードをプログラムするためのプラットフォームとして機能するArduino IDEが必要です。
1. Arduinoの公式ウェブサイトにアクセスします : [Arduino Software](https://www.arduino.cc/en/software)
2. オペレーティングシステム (Windows、macOS、またはLinux) に適したバージョンを選択します。
3. インストーラーをダウンロードして実行します。
 
**ステップ 2: Arduino IDEのインストール**
オペレーティングシステムに基づいて、次の手順に従ってArduino IDEをインストールします。
 
- Windows:
    1. ダウンロードした.exeファイルを実行します。
    2. インストールの指示に従います。必要なすべてのドライバをインストールしてください。
- macOS:
    1. .dmgファイルを開きます。
    2. Arduinoアプリケーションをアプリケーションフォルダにドラッグします。
- Linux:
    1. .tar.xzファイルを解凍します。
    2. 解凍したディレクトリでターミナルを開きます。
    3. ./install.shを実行してインストールします。
 
**ステップ 3: Arduino IDEへのVCP-G .jsonファイルの追加**
VCP-Gをプログラムするには、ボードマネージャーを介してVCP-G .jsonファイルをArduino IDEに追加する必要があります。
1. Arduino IDEを開きます。
2. **File > Preferences**に移動します。
3. **"Additional Board Manager URLs"**フィールドに、次のURLを追加します。
    ```
    https://raw.githubusercontent.com/topst-development/VCP-Arduino_Board_Manager/develop/package_topst_vcp_index.json
    ```
4. **OK**をクリックして変更を保存します。
5. **Tools > Board > Boards Manager**に移動します。
6. Boards Managerで「TOPST VCP-G」を検索します。
7. TOPST VCP-Gエントリが表示されたら、ドロップダウンメニューからv1.0.0を選択し、**Install**をクリックします。
 
**ステップ 4: VCP-Gの選択**
インストール後、TOPST VCP-Gボードを選択する必要があります。
1. Arduino IDEで**Tools > Board**に移動します。
2. 下にスクロールして「TOPST VCP-G」を見つけ、選択します。
 
**ステップ 5: インストールの確認**
簡単なスケッチをアップロードして、セットアップが機能するかどうかをテストします。
1. USBを使用してVCP-GボードをPCに接続します。
2. **Tools > Port**で適切なポートを選択します。
3. **File > Examples > 01.Basics > Blink**を開きます。
4. **Upload**をクリックして、スケッチをボードに転送します。
    **注:** アップロードプロセスが無限アップロード状態で止まる場合は、FWDNモードがアクティブになっていないためです。電源ケーブルを外し、FWDNスイッチを押したまま電源ケーブルを再接続してから、ボタンを放します。問題が解決しない場合は、管理者権限でArduino IDEを実行してみてください。
5. オンボードLEDが点滅し始めたら、ボードは正しくセットアップされています。
 
</br></br></br>
 
## 2.2 トラブルシューティング
---
セットアップ中に問題が発生した場合は、[Arduinoトラブルシューティングガイド](https://www.arduino.cc/en/Guide/Troubleshooting)を参照してください。
詳細および高度な機能については、VCP-Gドキュメントを参照するか、[Arduinoヘルプセンター](https://support.arduino.cc/hc/en-us)にアクセスしてください。
 
</br></br></br></br>
 
# 3. 参考文献
---
- 詳細については、TOPSTにお問い合わせください: topst@topst.ai
 
**注:** 参照ドキュメントは、契約条件に応じて、利用可能な場合はいつでも提供できます。参照ドキュメントが利用できない場合は、開発に直接関連するコンテンツを案内できます。
