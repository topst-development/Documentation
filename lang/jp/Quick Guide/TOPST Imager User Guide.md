# TOPST Imager ユーザーガイド

TOPST Imager は TOPST ボードに OS やファームウェアをインストールします。プログラミングや電子工学の知識は不要です。このガイドを開いたまま、画面を一つずつ確認して進めてください。

> **重要:** 書き込みにより、ボードの eMMC に保存されたすべてのデータが消去される場合があります。開始前に必要なファイルをバックアップしてください。

> **スクリーンショットについて:** 赤枠と番号付きの丸は、このガイド専用の注釈です。TOPST Imager には表示されません。画像は Windows のライトテーマですが、Linux やダークテーマでも操作は同じです。

## 1. 画面に表示される用語

| 用語 | 簡単な意味 |
| --- | --- |
| Board / Device | イメージをインストールする TOPST 製品です。 |
| Image | OS またはファームウェアを含むファイルです。 |
| Flashing | 選択したイメージをボードに書き込むことです。 |
| Firmware Download Mode / Boot Mode | 書き込み用の特別なボード状態です。 |
| FWDN | TOPST Imager がバックグラウンドで実行するツールです。自分で実行する必要はありません。 |
| COM port | AI-G と VCP-G が使用する USB シリアル接続です。Linux では `/dev/ttyUSB...` または `/dev/ttyACM...` と表示されます。 |
| eMMC | ボード内蔵のストレージです。 |

## 2. 対応ボード

| ボード | カスタムイメージ | 書き込み中に使用する接続 |
| --- | --- | --- |
| TOPST D3-G | `.fai` | ボード電源と FWDN USB Type-C データケーブル |
| TOPST AI-G | `.fai` | ボード電源、FWDN USB Type-C データケーブル、Ethernet ケーブル |
| TOPST VCP-G | `.rom` | ボード電源と FWDN USB Type-C データケーブル |

**データ転送**に対応する USB Type-C ケーブルを使用してください。充電専用ケーブルは使用できません。

## 3. 開始前の準備

- 使用する TOPST ボードと電源アダプター
- USB Type-C データケーブル
- AI-G を使用する場合は Ethernet ケーブル
- 公式イメージを使用する場合はインターネット接続のあるコンピューター
- 圧縮ファイルと展開後のパッケージの両方を保存できる空き容量
- ボード上の重要データのバックアップ

書き込み中は次を守ってください。

- ボードやコンピューターの電源を切らないでください。
- USB や Ethernet ケーブルを抜かないでください。
- TOPST Imager を終了しないでください。
- コンピューターをスリープ状態にしないでください。

## 4. アプリのオプション

メイン画面左下の **App Options** を選択します。

![TOPST Imager のアプリオプション](https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/Quick%20Guide/TOPST%20Imager%20App%20Options.png)

1. **Language:** 選択すると表示がすぐに切り替わり、言語を確認できます。
2. **TOPST Imager User Guide:** Web ブラウザーでこのガイドを開きます。
3. **Ask the Community:** [TOPST コミュニティ](https://community.topst.ai/)を開きます。
4. **Save:** 選択した言語を保存します。**Cancel**、`Esc` キー、または画面の外側のクリックでは、オプションを開く前の言語に戻ります。

韓国語、英語、日本語、簡体字中国語、繁体字中国語、タイ語、ドイツ語に対応します。ライト／ダーク表示は OS のテーマに自動で従います。

---

# Windows

## 5. TOPST Imager のインストール

### 5.1 必要な環境

- Windows 10 64 ビット以降
- Windows 11 64 ビット

### 5.2 インストール

1. 公式の Windows インストーラーをダウンロードします。
2. インストーラーをダブルクリックします。
3. 使用許諾契約を読み、同意します。
4. **Install** を選択します。
5. 完了後、**Launch TOPST Imager** を選択します。

アプリや VTC ドライバーの起動時に Windows が管理者権限を求める場合があります。公式 TOPST 配布ファイルであることを確認してから **Yes** を選択してください。

## 6. ボード、OS、バージョンの選択

### 6.1 ボードの選択

![TOPST ボードの選択](https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/Quick%20Guide/TOPST%20Imager%20Board%20Selection.png)

1. 手元の製品と一致するボードを選択します。
2. 行が強調表示され **Selected** と表示されていることを確認し、**Next** を選択します。

ダブルクリックでも進めます。間違えたら **Back** で戻って選び直してください。

### 6.2 OS の選択

![公式 OS またはカスタムイメージの選択](https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/Quick%20Guide/TOPST%20Imager%20OS%20Selection.png)

1. TOPST が提供する OS を選択します。
2. コンピューター上のファイルを使う場合は **Use Custom Image** を選択します。
3. **Next** を選択するか、選択した行をダブルクリックします。

### 6.3 バージョンの選択

![イメージのバージョンの選択](https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/Quick%20Guide/TOPST%20Imager%20Version%20Selection.png)

1. 必要なバージョンを選び、説明、リリース日、ダウンロードサイズ、展開後サイズを確認します。
2. **Flashing** を選択します。

- **Download size** はインターネットから取得する圧縮ファイルのサイズです。
- **Extracted size** は展開後に必要なディスク容量の目安です。

プロジェクトで特定の版が必要な場合を除き、最新の安定版または推奨版を使用してください。

### 6.4 データ消去の確認

![eMMC 消去警告の確認](https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/Quick%20Guide/TOPST%20Imager%20eMMC%20Erase%20Warning.png)

1. ボード、イメージ、バックアップを再確認する場合は **Cancel** を選択します。
2. 選択したボードの eMMC データが消去される可能性を理解した場合のみ **Confirm** を選択します。

この時点の **Cancel** ではボードは消去されません。

## 7. Windows で D3-G に書き込む

Windows の D3-G 書き込み設定は 3 ステップです。

### ステップ 1: VTC ドライバーのインストール

![D3-G VTC ドライバーのインストール](https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/Quick%20Guide/TOPST%20Imager%20D3-G%20Driver%20Installation.png)

1. **Install Driver** を選択します。
2. Windows の管理者権限要求を承認します。
3. VTC ドライバーのインストールを完了します。
4. TOPST Imager に戻ります。
5. **Driver Installation Complete** を選択します。

通常は各 Windows コンピューターで一度だけ必要です。権限要求をキャンセルするとインストールされません。準備ができたら **Install Driver** を再選択してください。

### ステップ 2: ブートモードとボードの検出

![D3-G のブートモードとボード検出](https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/Quick%20Guide/TOPST%20Imager%20D3-G%20Boot%20Mode.png)

1. ブートモードのアニメーションの点滅表示に従います。
2. **BOOT** を押し続けます。
3. BOOT を押したまま **RESET** を押して離します。
4. BOOT を離します。
5. FWDN USB Type-C データケーブルを確実に接続します。
6. 状態が自動更新されない場合は **Check Again** を選択します。
7. 接続済みになったら **Start Flashing** を選択します。

Windows デバイスマネージャーの USB コントローラー配下に `Telechips TCCxxxx VTC USB Driver` のような名前で表示される場合があります。

### ステップ 3: 書き込み

公式イメージでは次の進捗が個別に表示されます。

1. ダウンロード
2. 展開
3. 書き込み

各進捗は 0% から 100% になります。**Complete** 画面が出るまで何も外さないでください。

## 8. Windows で AI-G に書き込む

AI-G の書き込み設定は 3 ステップです。

### ステップ 1: Ethernet の設定

1. コンピューターと AI-G を Ethernet ケーブルで直接接続します。
2. Wi-Fi ではなく AI-G に接続した有線アダプターを選択します。
3. 要求されたら一時アドレス `192.168.0.8/24` の適用を許可します。
4. ネットワークが準備できたら進みます。

処理完了時またはキャンセル時に、一時的な Windows ネットワーク設定は元に戻ります。

### ステップ 2: ブートモードと COM ポート

1. 画面のブートモードアニメーションに従います。
2. **BOOT** を押し続けます。
3. **RESET** を押して離します。
4. BOOT を離します。
5. AI-G の COM ポートを選択します。
6. 電源、USB Type-C、Ethernet ケーブルを確認します。
7. 書き込みに進みます。

複数ポートがある場合は AI-G の USB を一度抜きます。消えたものが通常 AI-G のポートです。再接続し、ブートモードを繰り返してそのポートを選択します。

### ステップ 3: 書き込み

100% になり **Complete** 画面が出るまで待ちます。

## 9. Windows で VCP-G に書き込む

VCP-G の書き込み設定は 2 ステップです。

### ステップ 1: ブートモードと COM ポート

ブートモード案内と COM ポート選択は同じ画面にあります。

1. アニメーションに従って Firmware Download Mode にします。
2. 案内されたタイミングで **RESET** を押して離します。
3. VCP-G の COM ポートを選択します。
4. 電源と FWDN USB Type-C データケーブルを再確認します。
5. 書き込みに進みます。

### ステップ 2: 書き込み

100% になり **Complete** 画面が出るまで待ちます。

## 10. Windows でカスタムイメージを使う

1. 正しいボードを先に選択します。
2. OS 画面で **Use Custom Image** を一度クリックします。
3. **Next** を選択するか **Use Custom Image** をダブルクリックします。
4. ドロップ領域にファイルをドラッグするか参照ボタンを選択します。
5. ファイル名を確認して進みます。

正しい形式を使用してください。

- D3-G: `.fai`
- AI-G: `.fai`
- VCP-G: `.rom`

ローカルファイルなので **Download** と **Extraction** の進捗行は非表示です。ボード別のドライバー、ネットワーク、ブートモード、COM ポート、書き込み手順は同じです。

---

# Linux

## 11. Linux の要件

現在の配布版は **x86_64 Linux** に対応します。Windows の `.exe` FWDN ファイルは使用できません。

次の Linux 実行ツールが配布アプリに必要です。

```text
tools/fwdn_d3/fwdn_d3
tools/fwdn_ai/fwdn_ai
tools/fwdn_vcp/fwdn_vcp
```

コンピューターには次も必要です。

- 公式 ZIP パッケージ用の `unzip`
- 管理者確認ウィンドウ用の `policykit-1`
- AI-G／VCP-G の一時的なシリアルアクセス用の `acl`

Ubuntu では管理者が次でインストールできます。

```bash
sudo apt update
sudo apt install unzip policykit-1 acl
```

TOPST Imager や FWDN を `sudo` で実行**しないでください**。選択したシリアル機器への一時アクセスが必要な場合だけ、アプリが管理者権限を要求します。

## 12. Linux パッケージのインストールと起動

アーカイブ名はリリースで異なります。`.tar.gz` の例:

```bash
cd ~/Downloads
tar -xzf TOPST-Imager-<version>-Linux-x86_64.tar.gz
cd TOPST-Imager-<version>-Linux-x86_64
chmod +x topst-imager
./topst-imager
```

ダウンロードした実際のファイル名とフォルダー名を使ってください。ユーザー向けパッケージには Qt ランタイムが必要です。Qt が不足する場合は root で実行せず、完全な公式 Linux パッケージを取得してください。

## 13. Linux でのイメージ選択

ボード、OS、バージョン、カスタムイメージ、eMMC 警告は、第 6 節と第 10 節の Windows 画面と同様に動作します。

## 14. Linux で D3-G に書き込む

Windows VTC ドライバー画面がないため、設定は 2 ステップです。

### ステップ 1: ブートモードとボード検出

1. **BOOT** を押し続けます。
2. **RESET** を押して離します。
3. BOOT を離します。
4. FWDN USB Type-C データケーブルを接続します。
5. 必要なら **Check Again** を選択します。
6. D3-G が検出されたら進みます。

Linux は D3-G FWDN USB 機器を直接検出します。検出されなければデータケーブル、電源、ブートモード、パッケージ付属のインストール済み udev ルールを確認してください。

### ステップ 2: 書き込み

ダウンロード、展開、書き込みの完了を待ちます。カスタム `.fai` では書き込み進捗のみ表示します。

## 15. Linux で AI-G に書き込む

設定は 3 ステップです。

### ステップ 1: Ethernet の設定

アドレスは自動変更されません。Linux のネットワーク設定で指定します。

1. **設定 → ネットワーク**を開きます。
2. AI-G に接続した有線接続を開きます。
3. IPv4 を**手動**にします。
4. アドレス: `192.168.0.8`
5. ネットマスク: `255.255.255.0`、またはプレフィックス長 `24`
6. 管理者の別の指示がなければゲートウェイと DNS は空欄にします。
7. 適用し、有線接続を再接続して TOPST Imager に戻ります。

### ステップ 2: ブートモード、COM ポート、一時アクセス

1. アニメーションに従います。
2. `/dev/ttyUSB0` など AI-G のポートを選択します。
3. 書き込めない場合は **Grant Temporary Access** を選択します。
4. Linux の管理者ウィンドウで承認します。
5. 権限が準備できると書き込みボタンが有効になります。

一時権限は選択したシリアル機器だけに適用され、書き込み後、キャンセル後、書き込み画面を離れた後に解除されます。ユーザーを `dialout` に恒久的に追加する必要はありません。

### ステップ 3: 書き込み

**Complete** 画面を待ちます。

## 16. Linux で VCP-G に書き込む

Windows と同様、設定は 2 ステップです。

### ステップ 1: ブートモード、COM ポート、一時アクセス

1. ブートモード案内に従います。
2. `/dev/ttyUSB0` など VCP-G のポートを選択します。
3. 表示された場合は **Grant Temporary Access** を選択し管理者ウィンドウで承認します。
4. 選択したポートにアクセスできたら進みます。

### ステップ 2: 書き込み

100% になり **Complete** 画面が出るまで待ちます。カスタム `.rom` は書き込み進捗のみ表示します。

## 17. ダウンロード、再試行、一時ファイル

公式イメージでは次のように動作します。

1. 一時作業フォルダーを作成します。
2. ZIP パッケージをダウンロードします。
3. 一時フォルダーに展開します。
4. ボード別の FWDN 実行ファイルを起動します。
5. 書き込み成功またはキャンセル後、一時的な取得・展開データを削除します。

通信が切れた場合はアプリを開いたままネットワークを再接続してください。自動再試行し、サーバーが対応していれば途中から再開します。状態は選択したアプリ言語で表示されます。

復旧可能な一部の書き込みエラーでは準備済みパッケージを一時保持するため、再取得せず案内された設定に戻れます。

## 18. エラーウィンドウが表示された場合

既知の FWDN エラーは直ちに表示されます。3 秒のカウントダウンがあればメッセージを読んでください。終了後、必要な復旧手順に戻ります。項目を確認して **OK** を選択します。

### D3-G 接続エラー

次を確認します。

1. 電源接続
2. FWDN USB Type-C ケーブル
3. Firmware Download Mode への移行

D3-G のブートモード手順に戻ります。

### AI-G 接続／同期エラー

次を確認します。

1. 電源接続
2. Firmware Download Mode への移行
3. 正しい COM ポート

`Failed open port` なら FWDN USB Type-C と選択ポートを確認します。`TCP Socket Open Fail` なら Ethernet ケーブル、アダプター、`192.168.0.8/24` 設定を確認します。

### VCP-G 接続エラー

次を確認します。

1. 電源接続
2. Firmware Download Mode への移行
3. 正しい COM ポート

`GetLastError : 22` なら FWDN USB Type-C 接続を確認します。

### COM ポートがない

1. 電源を確認します。
2. USB データケーブルを再接続します。
3. Firmware Download Mode を繰り返します。
4. 一覧を更新します。
5. Linux ではポート選択後 **Grant Temporary Access** を選択します。

### 書き込みが完全に失敗した場合

`Failed to write in eFlash` または `Failed FWDN` なら案内に従って最初の設定からやり直します。書き込み動作中はボードを外さないでください。

## 19. ログファイル

問い合わせ時はエラー全文、ボード名、イメージのバージョン、OS、ログを添えてください。

Windows のログ:

```text
%LOCALAPPDATA%\Telechips\TOPST Imager\logs\topst-imager.log
```

Linux の標準的なログ:

```text
~/.local/share/Telechips/TOPST Imager/logs/topst-imager.log
```

**App Options → Ask the Community** または [TOPST コミュニティ](https://community.topst.ai/)で相談できます。

## 20. 書き込み完了後

1. **Complete** 画面を確認します。
2. アプリが完了を知らせるまで待ちます。
3. ボードの電源を安全に切ります。
4. FWDN を外すか通常使用の配線に戻します。
5. 電源を入れ、新しい OS の起動を確認します。

次の三つを守ってください。

1. ボードとイメージを慎重に選びます。
2. 書き込み中に電源やケーブルを外しません。
3. エラー時は表示項目を上からすべて確認します。
