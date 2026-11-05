---
title: TOPST Imager ユーザーガイド
description: Windows または Linux で TOPST ボードに OS イメージをインストールする方法を説明します。
---

# TOPST Imager ユーザーガイド

TOPST Imager は、TOPST ボードに OS やファームウェアをインストールするアプリケーションです。
コンピューターや電子機器に詳しくなくても、このガイドとアプリの案内を確認しながら、ゆっくり一つずつ進めてください。

> **重要:** 書き込みにより、ボードの eMMC に保存されたすべてのデータが消去される場合があります。開始前に必要なファイルをバックアップしてください。

## 1. 基本用語

| アプリの用語 | 意味 |
| --- | --- |
| Board | OS をインストールする TOPST 機器です。 |
| Image | ボードにインストールする OS のファイルです。 |
| Flashing | イメージファイルをボードに書き込む処理です。 |
| Boot mode | コンピューターからボードにイメージを書き込める特別な状態です。 |
| FWDN | TOPST ボードへの書き込みに使う内部ツールです。自分で実行する必要はありません。 |
| COM port | USB 接続したボードをコンピューターが識別するための名前です。 |
| eMMC | ボード内蔵のストレージです。 |

## 2. 対応ボードとイメージファイル

| ボード | カスタムイメージ形式 | 必要な接続 |
| --- | --- | --- |
| TOPST D3-G | `.fai` | FWDN USB Type-C データケーブル |
| TOPST AI-G | `.fai` | FWDN USB Type-C データケーブルと Ethernet ケーブル |
| TOPST VCP-G | `.rom` | FWDN USB Type-C データケーブル |

> 充電専用ケーブルは使用できません。**データ転送に対応した USB Type-C ケーブル**を使用してください。

## 3. 開始前の準備

- 書き込む TOPST ボードと電源アダプター
- データ転送対応 USB Type-C ケーブル
- インターネットに接続したコンピューター
- AI-G の場合は Ethernet ケーブル
- 公式イメージのダウンロードと展開に十分な空き容量
- ボード上の重要なデータのバックアップ

書き込み中は、ボードの電源を切ったり、USB や Ethernet ケーブルを抜いたりしないでください。TOPST Imager を終了せず、コンピューターの電源を切ったりスリープ状態にしたりしないでください。

## 4. 基本的な流れ

Windows と Linux の基本手順は共通です。

1. TOPST Imager を起動します。
2. 使用するボードを選択します。
3. OS または **Custom Image** を選択します。
4. インストールするバージョンを選択します。
5. アプリの接続およびブートモードの案内に従います。
6. 書き込みを開始します。
7. **Complete** 画面が表示されるまで待ちます。

項目を一度クリックして **Next** を選択するか、項目をダブルクリックすると次の画面に進めます。

---

# Windows での使用方法

## 5. Windows へのインストール

### 5.1 対応環境

- Windows 10 64 ビット以降
- Windows 11 64 ビット

### 5.2 アプリのインストール

1. TOPST 公式サイトから Windows 用の `TOPST Imager.exe` をダウンロードします。
2. ダウンロードしたファイルをダブルクリックします。
3. 使用許諾契約を読み、同意します。
4. 必要に応じてデスクトップショートカットを選択します。
5. **Install** を選択します。
6. 完了後、**Launch TOPST Imager** を選択してセットアップを終了します。

Windows の保護メッセージが表示されたら、公式サイトから入手したファイルであることを確認してください。入手元を確認できない場合は実行しないでください。

標準のインストール先:

```text
%LOCALAPPDATA%\Programs\TOPST Imager
```

## 6. 言語と表示テーマ

1. ウィンドウ左下の **App Options** を選択します。
2. 使用する言語を選択します。
3. **Save** を選択します。

> スクリーンショットの赤枠と数字は説明用に追加したもので、実際のアプリには表示されません。

![TOPST Imager の言語とサポート設定](https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/Quick%20Guide/TOPST%20Imager%20App%20Options.png)

1. **Language:** 使用する言語を選択します。
2. **Ask the Community:** 困ったときに TOPST コミュニティを開きます。
3. **Save:** 選択した言語を適用します。

韓国語、英語、日本語、簡体字中国語、繁体字中国語、タイ語、ドイツ語に対応しています。ライト／ダーク表示は Windows のシステムテーマに自動で従います。

## 7. 公式イメージのインストール

### 7.1 ボードの選択

1. ボードの画像と名前を確認します。
2. 使用するボードを一度クリックします。
3. 選択した項目の色が変わったことを確認します。
4. **Next** を選択します。

![D3-G ボードと Next ボタンの選択](https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/Quick%20Guide/TOPST%20Imager%20Board%20Selection.png)

1. 使用する**ボードの項目**を選択します。
2. 選択を確認し、**Next** を選択します。

間違えた場合は **Back** で戻って選び直してください。

### 7.2 OS とバージョンの選択

1. OS を選択して **Next** を選択します。
2. インストールするバージョンを選択します。
3. リリース日とファイルサイズを確認します。

![公式 OS またはカスタムイメージの選択](https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/Quick%20Guide/TOPST%20Imager%20OS%20Selection.png)

1. 公式イメージを使う場合は、希望する **OS** を選択します。
2. コンピューター上のファイルを使う場合は **Use Custom Image** を選択します。
3. 選択を確認して **Next** を選択します。

![OS バージョンと Flashing ボタンの選択](https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/Quick%20Guide/TOPST%20Imager%20Version%20Selection.png)

1. 希望する**バージョン**を選択し、ダウンロードサイズとリリース日を確認します。
2. 正しければ **Flashing** を選択します。

- **Download size:** インターネットから取得する圧縮ファイルのサイズです。
- **Extracted size:** 展開後にコンピューターで必要になる空き容量の目安です。

常に最新版が必要とは限りません。別の指示がなければ推奨版または最新の安定版を選択してください。

### 7.3 消去警告の確認

書き込み前に、ボードの eMMC の内容が消去される可能性を知らせる警告が表示されます。

1. 選択したボードとイメージを再確認します。
2. ボードに必要なデータが残っていないことを確認します。
3. 準備ができたら確認ボタンを選択します。

![Cancel と Confirm ボタンのある eMMC 消去警告](https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/Quick%20Guide/TOPST%20Imager%20eMMC%20Erase%20Warning.png)

1. 準備ができていない場合や再確認する場合は **Cancel** を選択します。
2. eMMC が消去される可能性を理解したうえで **Confirm** を選択します。

不明な場合は **Cancel** を選択してください。この時点でのキャンセルではボードは消去されません。

## 8. D3-G への書き込み

### 8.1 ステップ 1: ドライバーのインストール

1. **Install Driver** を選択します。
2. Windows が管理者権限を求めたら内容を確認して **Yes** を選択します。
3. VTC ドライバーのインストーラーを最後まで実行します。
4. TOPST Imager に戻ります。
5. **Driver Installation Complete** を選択します。

![D3-G VTC ドライバーのインストール案内](https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/Quick%20Guide/TOPST%20Imager%20D3-G%20Driver%20Installation.png)

1. まず **Install Driver** でインストーラーを起動します。
2. すべての手順を終えてから **Driver Installation Complete** を選択します。

通常、各コンピューターで一度だけ必要です。

### 8.2 ステップ 2: ブートモードとボードの検出

画面のボード画像と点滅するマーカーを見ながら進めます。

1. ボードの **BOOT ボタンを押します。**
2. BOOT を押したままにします。
3. **RESET ボタンを押して離します。**
4. BOOT を離します。
5. USB Type-C ケーブルがコンピューターとボードに確実に接続されているか確認します。
6. アプリがボードを検出したか確認します。

![D3-G のブートモードとボード検出画面](https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/Quick%20Guide/TOPST%20Imager%20D3-G%20Boot%20Mode.png)

1. 画像と点滅するマーカーを見て、ブートモードの順序に従います。
2. 接続を変更したら **Check Again** を選択します。
3. 検出されると **Continue Flashing** が使用可能になります。

Windows のデバイスマネージャーでは `Telechips TCCxxxx VTC USB Driver` のような名前で表示される場合があります。

### 8.3 ステップ 3: イメージの書き込み

1. **Start Flashing** を選択します。
2. ダウンロード、展開、書き込みの進行状況を確認します。
3. 完了画面が表示されるまで待ちます。

## 9. AI-G への書き込み

USB と Ethernet の両方を使用します。

### 9.1 ステップ 1: Ethernet の設定

1. コンピューターと AI-G を Ethernet ケーブルで接続します。
2. AI-G に接続した Ethernet アダプターを選択します。
3. 案内に従い、コンピューターのアドレスを `192.168.0.8/24` に設定します。
4. 設定完了を確認します。

Wi-Fi ではなく、**AI-G に接続した有線 Ethernet アダプター**を選択してください。

### 9.2 ステップ 2: ブートモードと COM ポート

1. アニメーションを見て BOOT を押します。
2. BOOT を押したまま RESET を押して離します。
3. BOOT を離します。
4. 新たに検出された AI-G の USB COM ポートを選択します。
5. ボード電源、USB Type-C、Ethernet ケーブルを再確認します。

複数の COM ポートがある場合は AI-G の USB を一度抜きます。消えたポートが AI-G のポートです。再接続し、ブートモードの手順を繰り返してから続行してください。

### 9.3 ステップ 3: イメージの書き込み

1. **Start Flashing** を選択します。
2. 100% になるまで待ちます。
3. 完了画面が表示されたらボードを再起動します。

## 10. VCP-G への書き込み

### 10.1 ステップ 1: ブートモード

1. 画面のボード画像を確認します。
2. BOOT を押し続けます。
3. RESET を押して離します。
4. BOOT を離します。
5. **Next** を選択します。

### 10.2 ステップ 2: COM ポートの選択

1. VCP-G の USB COM ポートを選択します。
2. 表示されない場合は USB Type-C ケーブルを再接続します。
3. 一覧を更新し、正しいポートを選択します。

### 10.3 ステップ 3: イメージの書き込み

1. **Start Flashing** を選択します。
2. 100% になるまで待ちます。
3. 完了画面が表示されたらボードを再起動します。

## 11. カスタムイメージのインストール

公式カタログにないローカルファイルを使う場合の手順です。

1. OS 選択画面で **Custom Image** を一度クリックします。
2. **Next** を選択するか、項目をダブルクリックします。
3. 点線の領域にファイルをドラッグするか、**Browse for FAI Image** または **Browse for ROM Image** で選択します。
4. ファイル名を確認します。
5. **Next** を選択し、ボードの接続案内に従います。

D3-G と AI-G は `.fai`、VCP-G は `.rom` を選択してください。
ローカルファイルのため、書き込み画面にダウンロードと展開の工程は表示されません。

## 12. Windows のトラブルシューティング

### ボードが検出されない

1. ボードの電源を確認します。
2. USB ケーブルが充電専用でないことを確認します。
3. FWDN USB Type-C ポートへの接続を確認します。
4. ブートモードの手順を繰り返します。
5. D3-G は VTC ドライバーを確認します。

### COM ポートが表示されない

1. USB を抜き差しします。
2. ボードの電源を確認します。
3. ブートモードに入り直します。
4. COM ポート一覧を更新します。

### AI-G のネットワークエラー

1. コンピューターと AI-G 間の Ethernet ケーブルを確認します。
2. Wi-Fi ではなく有線アダプターを選択したか確認します。
3. アドレスが `192.168.0.8/24` であることを確認します。
4. アプリの案内に従ってステップ 1 からやり直します。

### `Failed open port` または `GetLastError : 22`

FWDN USB Type-C ケーブルを確認して再接続し、ブートモードの手順からやり直してください。

### ダウンロードが進まない

1. インターネット接続を確認します。
2. 空き容量を確認します。
3. 少し待って **Retry** を選択します。

### 書き込み中に前の手順へ戻りたい

開始後に戻るとキャンセル確認が表示されます。キャンセル前にボードが安全な状態であることを確認し、画面の案内に従ってください。

### エラーについて相談する

1. エラー画面の詳細をコピーします。
2. **App Options** からログフォルダーを開きます。
3. エラーメッセージとログファイルを用意します。
4. [TOPST コミュニティ](https://community.topst.ai/)で質問します。

Windows の標準的なログ保存先:

```text
%LOCALAPPDATA%\Telechips\TOPST Imager\logs\topst-imager.log
```

---

# Linux での使用方法

## 13. Linux の事前準備

画面と基本操作は Windows と共通ですが、準備が異なります。ボード、OS、バージョンのボタンは上の Windows 画像と同じ位置にあります。D3-G の Windows ドライバー画面は省略され、ブートモードと検出に直接進みます。

- Windows VTC ドライバーはインストールしません。
- D3-G には USB アクセス権限が必要です。
- AI-G と VCP-G にはシリアルポートの権限が必要です。
- パッケージに Linux 用 FWDN 実行ファイルが必要です。
- 公式イメージの展開に `unzip` または `bsdtar` が必要です。

コマンド操作に慣れていない場合は、管理者や開発者に下記の **Linux 管理者設定**を依頼してください。一度設定すれば、一般ユーザーは画面の案内で操作できます。

## 14. Linux でのインストールと起動

以下は Ubuntu の例です。

### 14.1 パッケージの展開

1. 公式サイトからコンピューターに合う Linux パッケージを取得します。
2. ダウンロードフォルダーを開きます。
3. ターミナルで次を実行します。

```bash
cd ~/Downloads
tar -xzf TOPST-Imager-<version>-Linux-<architecture>.tar.gz
```

`<version>` と `<architecture>` は実際のファイル名の値に置き換えてください。名前の先頭を入力し、`Tab` で補完できます。

### 14.2 アプリの起動

展開先へ移動して起動します。

```bash
cd TOPST-Imager-<version>-Linux-<architecture>
chmod +x topst-imager
./topst-imager
```

`Qt` ライブラリ不足のエラーは、パッケージに Qt ランタイムが含まれていないことを示します。一般ユーザーは手動導入せず、配布元に **Qt 6.12 ランタイムを含む Linux パッケージ**を依頼してください。

## 15. Linux 管理者設定

通常は一度だけ必要です。

### 15.1 展開ツールのインストール

```bash
sudo apt update
sudo apt install unzip
```

### 15.2 AI-G と VCP-G のシリアルポート権限

```bash
sudo usermod -aG dialout "$USER"
```

実行後にログアウトしてログインし直すか、コンピューターを再起動してください。

### 15.3 D3-G の USB 権限

1. D3-G をブートモードで接続します。
2. USB ID を確認します。

```bash
lsusb
```

3. 検出したベンダー ID と製品 ID で `/etc/udev/rules.d/99-topst.rules` を作成します。

```text
SUBSYSTEM=="usb", ATTR{idVendor}=="VENDOR_ID", ATTR{idProduct}=="PRODUCT_ID", MODE="0666"
```

4. ルールを再読み込みします。

```bash
sudo udevadm control --reload-rules
sudo udevadm trigger
```

`VENDOR_ID` と `PRODUCT_ID` に適当な値を入れないでください。D3-G の値が不明なら TOPST サポートに問い合わせてください。

### 15.4 Linux FWDN ファイルの確認

次の場所に、拡張子のない Linux 実行ファイルが必要です。

```text
tools/fwdn_d3/fwdn_d3
tools/fwdn_ai/fwdn_ai
tools/fwdn_vcp/fwdn_vcp
```

存在する場合は実行権限を付けます。

```bash
chmod +x tools/fwdn_d3/fwdn_d3
chmod +x tools/fwdn_ai/fwdn_ai
chmod +x tools/fwdn_vcp/fwdn_vcp
```

これらがないと Linux で書き込みできません。Windows の `.exe` で代用できません。

## 16. Linux で D3-G に書き込む

Windows VTC ドライバーの工程は使用しません。

1. D3-G イメージを選択します。
2. アニメーションを見て BOOT を押します。
3. BOOT を押したまま RESET を押して離します。
4. BOOT を離します。
5. ボードの検出を確認します。
6. 書き込みを開始して完了を待ちます。

検出されない場合は USB 権限ルール、Type-C ケーブル、電源、ブートモードを確認してください。

## 17. Linux で AI-G に書き込む

Linux では Ethernet アドレスは自動変更されません。Ubuntu の設定で手動設定します。

1. **設定 → ネットワーク**を開きます。
2. AI-G に接続した有線ネットワークの設定を開きます。
3. IPv4 を**手動**に設定します。
4. アドレスを `192.168.0.8` にします。
5. ネットマスクを `255.255.255.0` にします。プレフィックス長なら `24` です。
6. 別の指示がなければゲートウェイと DNS は空欄にします。
7. 適用し、有線接続をオフにしてからオンにします。
8. TOPST Imager に戻り、Ethernet 状態を確認します。
9. 画面の案内でブートモードに入ります。
10. AI-G の `/dev/ttyUSB...` または `/dev/ttyACM...` を選択します。
11. 書き込みを開始します。

## 18. Linux で VCP-G に書き込む

1. 案内に従ってブートモードにします。
2. `/dev/ttyUSB...` または `/dev/ttyACM...` のポートを選択します。
3. 正しいポートを確認して書き込みます。
4. 完了画面を待ちます。

ポートがなければ `dialout` に参加し、ログインし直したか確認してください。

## 19. Linux のトラブルシューティング

### `Permission denied`

- AI-G／VCP-G: ユーザーが `dialout` グループに属するか確認します。
- D3-G: udev USB 権限ルールを確認します。
- FWDN: `chmod +x` による実行権限を確認します。

### Linux FWDN が見つからない

配布フォルダーの `tools/fwdn_*` に Linux 実行ファイルがあるか確認します。Windows の `.exe` は Linux では実行できません。

### ボードのポートが表示されない

次のコマンドで一覧を確認します。

```bash
ls /dev/ttyUSB* /dev/ttyACM* 2>/dev/null
```

USB 接続前後を比較してください。通常、新たに現れたポートがボードのものです。

### ライト／ダークテーマが反映されない

Linux デスクトップが Qt を通じて提供するテーマ情報を使用します。環境によって反映が遅れるため、アプリを再起動してください。

## 20. 書き込み完了後

1. 成功メッセージを確認します。
2. TOPST Imager のすべての処理が終わるまで待ちます。
3. ボードの電源を安全に切ります。
4. FWDN ケーブルを外すか、通常使用の配線に戻します。
5. 電源を入れて新しい OS が起動するか確認します。

公式イメージは一時フォルダーにダウンロード・展開されます。成功後、取得ファイルと展開フォルダーは自動削除されます。

## 21. 覚えておく三つのこと

1. **ボードとイメージを正しく選んでください。**
2. **書き込み中に電源やケーブルを外さないでください。**
3. **エラー時は画面の一覧を上から順番に確認してください。**

相談するときはエラーメッセージとログを用意し、[TOPST コミュニティ](https://community.topst.ai/)へ投稿してください。
