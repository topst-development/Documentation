# 1. はじめに
---
本書は、車載アプリケーション向けに設計された強力かつ効率的なプロセッサであり、TCC7045 をベースとする TOPST Vehicle Control Processor (VCP) で Arduino IDE を使用する方法について説明します。VCP-G を Arduino 環境と統合することにより、Arduino の簡潔さと柔軟性に匹敵し、かつ車載半導体に特化した開発環境を提供し、開発プロセスを簡素化および迅速化することを目的としています。  

本書には、以下の情報が含まれています:  
- インストールガイド

</br></br></br></br>

# 2. インストールガイド
---
本章では、Arduino 統合開発環境 (IDE) で使用する VCP-G Arduino パッケージをダウンロードしてインストールする方法について説明します。

</br></br></br>

## 2.1 インストールガイド
---
**ステップ 1: Arduino IDE のダウンロード**

まず、Arduino ボードをプログラミングするためのプラットフォームとなる Arduino IDE が必要です。  
1. Arduino の公式ウェブサイトにアクセスします : [Arduino Software](https://www.arduino.cc/en/software)
2. お使いのオペレーティングシステム (Windoiws、macOS、または Linux) に適したバージョンを選択します。
3. インストーラーをダウンロードして実行します。

**ステップ 2: Arduino IDE のインストール**  
Arduino IDE をインストールするには、お使いのオペレーティングシステムに応じて以下の手順に従ってください:  

- Windows:
    1. ダウンロードした .exe ファイルを実行します。
    2. インストールの指示に従います。必要なドライバがすべてインストールされることを確認してください。
- macOS:
    1. .dmg ファイルを開きます
    2. Arduino アプリケーションを Applications フォルダにドラッグします。
- Linux:
    1. .tar.xz ファイルを展開します。
    2. 展開したディレクトリでターミナルを開きます。
    3. ./install.sh を実行してインストールします。

**ステップ 3: Arduino IDE への VCP-G .json ファイルの追加**  
VCP-G をプログラミングするには、Board Manager から VCP-G .json ファイルを Arduino IDE に追加する必要があります。
1. Arduino IDE を開きます。
2. **File > Preferences** に移動します。
3. **"Additional Board Manager URLs"** フィールドに、次の URL を追加します:
    ```
    https://raw.githubusercontent.com/topst-development/VCP-Arduino_Board_Manager/develop/package_topst_vcp_index.json
    ```
4. **OK** をクリックして変更を保存します。
5. **Tools > Board > Boards Manager.** に移動します。
6. Boards Manager で “TOPST VCP-G” を検索します。
7. TOPST VCP-G の項目が表示されたら、ドロップダウンメニューから v1.0.0 を選択し、**Install** をクリックします。

**ステップ 4: VCP-G の選択**  
インストール後、TOPST VCP-G ボードを選択する必要があります:  
1. Arduino IDE で **Tools > Board** に移動します。
2. 下にスクロールして "TOPST VCP-G" を見つけ、選択します。

**ステップ 5: インストールの確認**  
簡単なスケッチをアップロードして、設定が正しく動作するかテストします:
1. USB を使用して VCP-G ボードを PC に接続します。
2. **Tools > Port** で適切なポートを選択します。
3.	**File > Examples > 01.Basics > Blink** を開きます。
4.	**Upload** をクリックして、スケッチをボードに転送します。  
    **注意:** アップロード処理が無限にアップロード中の状態で止まる場合は、FWDN モードが有効になっていないことが原因です。電源ケーブルを取り外し、FWDN スイッチを押したまま電源ケーブルを再接続し、その後ボタンを離してください。問題が解決しない場合は、管理者権限で Arduino IDE を実行してみてください。
5.	オンボード LED が点滅し始めれば、ボードは正しく設定されています。

</br></br></br>

## 2.2 トラブルシューティング
---
セットアップ中に問題が発生した場合は、[Arduino トラブルシューティングガイド](https://www.arduino.cc/en/Guide/Troubleshooting).  
詳細情報および高度な機能については、VCP-G のドキュメントを参照するか、[Arduino ヘルプセンター](https://support.arduino.cc/hc/en-us).

</br></br></br></br>

# 3. 参考資料
---
- 詳細については TOPST までお問い合わせください: topst@topst.ai

**注意:** 参考ドキュメントは、契約条件に応じて提供可能な場合に提供されます。参考
ドキュメントを提供できない場合は、お客様の開発に直接関連する内容についてご案内できます。

