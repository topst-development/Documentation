# 1. はじめに
---
本書では、VCP-G SDK 向けのソフトウェア開発環境を構築するためのガイドラインを説明します。必要なツール、設定、ツールチェーンについて説明します。

</br></br></br></br>

# 2. ホスト環境の設定
---
## 2.1 Ubuntu のインストール
---
開発環境は Ubuntu 22.04 上に構築することを推奨します。この Ubuntu バージョンは、広範なコミュニティサポートを備えた安定したプラットフォームを提供し、VCP-G および関連するツールチェーンとの互換性と使いやすさを保証します。

Linux ディストリビューションのバージョン:  
- Ubuntu 22.04 (LTS)

</br></br></br>

## 2.2 WSL2 Ubuntu のインストール（Windows 環境のみ）
---
**注意:** Ubuntu ホストを使用している場合は、WSL2 のインストールを省略できます。  

1.	**コントロール パネル -> プログラム -> Windows の機能の有効化または無効化 -> 仮想マシン プラットフォームと Hyper-V を有効化** をクリックして、Windows の機能を設定します。
2.	Windows Powershell を **“管理者権限で実行”.** で起動します。
3.	WSL2 システムを有効にします。
    ```
    dism.exe /online /enable-feature /featurename:Microsoft-Windows-Subsystem-Linux /all /norestart
    ```
4.	仮想マシン機能を有効にします。
    ```
    dism.exe /online /enable-feature /featurename:VirtualMachinePlatform /all /norestart
    ```
5.	WSL の既定のバージョンを 2（WSL2）に設定します。
    ```
    wsl --set-default-version 2
    ```
6.	Microsoft Store で Ubuntu 22.04 LTS を検索してダウンロードします。

    * Linux カーネル更新パッケージをダウンロードする必要がある場合は、[こちら](https://learn.microsoft.com/ko-kr/windows/wsl/install-manual)から最新のパッケージをダウンロードしてください。
7.	WSL の一覧で Ubuntu 22.04 を確認します。
    ```
    wsl --list -online
    ```
8.	Ubuntu 22.04 をインストールします。
    ```
    wsl --install Ubuntu-22.04
    ```
9.	Windows の検索ボックスで WSL2 を検索して実行します。 

</br></br></br>

## 2.3 Linux 環境の設定
---
ホスト PC に Linux 環境を構築するには、次の手順に従ってください。  

1. WSL2 の実行（Windows 環境のみ）  
    Windows を使用している場合は、Windows PowerShell で次のいずれかのコマンドを実行して WSL2 を起動します。  
    ```
    wsl
    ```
    ```
    ubuntu
    ```

2.	パッケージリストの更新  
新しいソフトウェアをインストールする前に、利用可能なパッケージの一覧を更新して、最新のバージョンと依存関係を取得できるようにしてください。次のコマンドは、リポジトリから利用可能なパッケージの最新一覧を取得します。
    ```
    sudo apt update && /
    sudo apt upgrade
    ```

3.	共通開発ツールのインストール  
    次のコマンドを入力して、共通開発ツールをインストールします。
    ```
    sudo apt install build-essential git
    ```

**注意:** このコマンドは build-essential パッケージと git の両方をインストールします。

</br></br></br></br>

# 3. ツールチェーン
---
VCP-G は **gcc-linaro-7.2.1-2017.11-x86_64_arm-eabi** ツールチェーンを使用します。  
このツールチェーンは ARM アーキテクチャ向けに最適化されており、VCP-G 上の TCC7045 チップとの互換性を保証します。

</br></br></br>

## 3.1 ツールチェーンのインストールと設定
---
次の手順に従って、ツールチェーンのダウンロード、展開、設定を行ってください。  
1. ツールチェーンのダウンロード  
   Linaro の Web サイトからツールチェーンをダウンロードするには、**wget** コマンドを入力します。
    ```
    wget https://releases.linaro.org/components/toolchain/binaries/7.2-2017.11/arm-eabi/gcc-linaro-7.2.1-2017.11-x86_64_arm-eabi.tar.xz
    ```
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/Download%20Toolchain.png"></p>
    <p align="center"><strong>図 3.1 ツールチェーンのダウンロード</strong></p>
    
2. ツールチェーンの展開  
    ダウンロードが完了したら、.tar.xz ファイルの内容を展開します。
    ```
    tar -xvf gcc-linaro-7.2.1-2017.11-x86_64_arm-eabi.tar.xz
    ```
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/Extract%20Toolchain.png"></p>
    <p align="center"><strong>図 3.2 ツールチェーンの展開</strong></p>
    
3. ツールチェーンを /opt へ移動  
    /opt ディレクトリは、Linux におけるオプションソフトウェアの標準的な配置場所です。展開したツールチェーンをこのディレクトリへ移動します。
    ```
    sudo mv gcc-linaro-7.2.1-2017.11-x86_64_arm-eabi /opt/
    ```
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/Move%20Toolchain.png"></p>
    <p align="center"><strong>図 3.3 ツールチェーンの移動</strong></p>

</br></br></br>

## 3.2 ツールチェーンの確認
---
ツールチェーンが正しくインストールされていることを確認します。  
1. ツールチェーンディレクトリへ移動
    ```
    cd /opt/gcc-linaro-7.2.1-2017.11-x86_64_arm-eabi
    ```
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/Navigate%20to%20Toolchain%20Directory.png"></p>
    <p align="center"><strong>図 3.4 ツールチェーンディレクトリへ移動</strong></p>
    
2. インストールされた GCC コンパイラのバージョンの確認
    ```
    ./bin/arm-eabi-gcc --version
    ```
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/Check%20Version%20of%20Installed%20GCC%20Compiler.png"></p>
    <p align="center"><strong>図 3.5 インストールされた GCC コンパイラのバージョンの確認</strong></p>

GCC コンパイラのインストールが完了したら、インストールされた GCC コンパイラのバージョンが **gcc-linaro-7.2.1-2017.11.** と一致することを確認してください。

</br></br></br></br>

# 4. ソースコードのクローン
---
この章では、Git を使用してソースコードをクローンする方法を説明します。

</br></br></br>

## 4.1 VCP-G ソースコードのクローン
---
VCP-G のソースコードを取得するには、**git clone** コマンドを入力します。このコマンドはリモートリポジトリのコピーをローカルマシン上に作成し、コードを直接扱えるようにします。

次の手順に従って、VCP-G のソースコードをクローンしてください。
1. ターミナルを開く  
    Ubuntu 22.04 システムでターミナルアプリケーションを起動します。

2. 目的のディレクトリへ移動  
    ソースコードを保存する適切な場所を選択します。例えば、ホームディレクトリにリポジトリを保存する場合は、次のコマンドを使用します。
    ```
    cd ~
    ```
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/Navigate%20to%20Desired%20Directory.png"></p>
    <p align="center"><strong>図 4.1 目的のディレクトリへ移動</strong></p>

3. リポジトリのクローン  
    次のコマンドを使用して、提供された git アドレスから VCP-G のソースコードをクローンします。
    ```
    git clone https://github.com/topst-development/FreeRTOS-VCP.git topst-vcp
    ```
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/Figure%204.2%20Clone%20Repository.png"></p>
    <p align="center"><strong>図 4.2 リポジトリのクローン</strong></p>

4. クローンしたディレクトリへ移動  
    クローンが完了したら、次のコマンドを使用してソースコードが格納されているディレクトリへ移動します。
    ```
    cd topst-vcp
    ```
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/Navigate%20to%20Cloned%20Directory.png"></p>
    <p align="center"><strong>図 4.3 クローンしたディレクトリへ移動</strong></p>

これで、VCP-G のソースコードをローカルでビルドおよび開発に使用できます。

</br></br></br>

## 4.2 ソースコードの構成
---
クローン後、**ls** コマンドを入力してディレクトリの内容を一覧表示し、主要なファイルを確認してソースコードの構成を把握します。
```
ls

build  documents  easy-setup_vcp.sh  LICENSE  scripts  sources  tools
```

</br></br></br></br>

# 5. ビルドガイド
---
## 5.1 easy-setup_vcp-g.sh の実行
---
./easy-setup_vcp-g.sh スクリプトを実行すると、次の画面が表示されます。

**注意**: ./easy-setup_vcp-g.sh を再実行する場合、yes を選択するとビルド済みのソースが削除されるため注意してください。
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20AI-G/Software/Linux%20SDK/license1.png"></p>
<p align="center"><strong>図 5.1 エンドユーザー使用許諾契約</strong></p>

画面の一番下までスクロールして、この注意事項をお読みください。お読みになった後、右矢印キーを押して [Enter] を押してください。
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20AI-G/Software/Linux%20SDK/license2.png"></p>
<p align="center"><strong>図 5.2 'Proceed to confirm' へ移動</strong></p>


すると、次の画面が表示されます。 
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20AI-G/Software/Linux%20SDK/license3.png" ></p>
<p align="center"><strong>図 5.3 Accept 画面 </strong></p>
[Enter] を押して Accept を選択すると、次のコマンドでビルドできます。

</br></br></br>

## 5.2 Makefile とビルドシステム
---
Makefile は、多くのビルドシステムにおける重要な構成要素です。プログラムをコンパイルおよびリンクするための **make** ユーティリティ向けのルールとディレクティブが記述されています。Makefile を活用することで、ビルド処理を自動化し、一貫性と効率性を確保できます。

</br></br></br>

## 5.3 ビルド処理の開始
---
ソースコードをビルドするには、次の手順に従ってください。  
1. ビルドディレクトリへ移動します。
    ```
    cd build/tcc70xx/gcc/
    ```
2. **make** コマンドを実行します。  
    ```
    make
    ```
    **make** コマンドは、現在のディレクトリにある Makefile を読み込み、ビルド処理を実行します。
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/Run%20make%20Command.png"></p>
    <p align="center"><strong>図 5.4 make コマンドの実行 </strong></p>
    
3. ビルド出力の確認  
    ビルド処理が完了すると、ターミナルに次の出力ファイルが表示されます。
    - output/tcc70xx_pflash_boot.rom
    - output/tcc70xx_pflash_boot_2M_ECC.rom
    - output/tcc70xx_pflash_boot_3M_ECC.rom
    - output/tcc70xx_pflash_boot_4M_ECC.rom
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/Verify%20Build%20Output.png"></p>
    <p align="center"><strong>図 5.5 ビルド出力の確認</strong></p>
   
    出力ファイルの一覧を確認するには、次のコマンドを使用します。
    ```
    ls output/ -al
    ```
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/Build%20Output%20File.png"></p>
    <p align="center"><strong>図 5.6 ビルド出力ファイル</strong></p>

</br></br></br></br>

# 6. ファームウェアのダウンロード
---
この章では、Linux ベースの開発環境で ***FWDN*** を VCP-G にダウンロードする方法を説明します。

</br></br></br>

## 6.1 VCP-G の準備
---
ダウンロードを開始する前に、VCP-G が安定した場所に置かれ、外部からの干渉がないことを確認してください。すべてのスイッチとコネクタに容易にアクセスでき、3.3V 電源ケーブルが正しく接続されていることを確認してください。

</br></br></br>

## 6.2 ハードウェアをホスト PC に接続
---
Ubuntu ホストを使用する場合は、手順 3 に直接進んでください。  
1. usbipd-win のダウンロード  
    WSL2 で USB を使用するには、usbipd-win プロジェクトが必要です。   
    次のリンクから usbipd-win をダウンロードします: https://learn.microsoft.com/ko-kr/windows/wsl/connect-usb#attach-a-usb-device.
2. PowerShell を実行し、VCP-G（Windows では COM ポートとして認識されます）を WSL2 に接続  
    Linux ではなく Windows PowerShell で次のコマンドを実行します。
    ```
    usbipd list
    ```
    ```
    usbipd bind --busid <busid>
    ```
    ```
    usbipd attach --wsl --busid <busid>
    ```
3. USB Type-C ケーブルの接続  
    USB Type-C ケーブルを使用して、VCP-G ボードを開発用ホスト PC に接続します。
4. USB 接続の確認  
    WSL2 で次のコマンドを実行します。
    ```
    sudo apt-get install usbutils && lsusb
    ```
    ```
    sudo dmesg | grep tty
    ```
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/Verify%20USB%20Connection.png"></p>
    <p align="center"><strong>図 6.1 USB 接続の確認</strong></p>

図 6.1 に示す出力が表示されれば、接続は正常に確立されています。

</br></br></br>

## 6.3 VCP-G へのソフトウェアのダウンロード
---

### 6.3.1 Windows 環境での FWDN の実行
1. ボードをダウンロードモードに設定  
   FWDN スイッチを押しながら、VCP-G ボードに電源ケーブルを接続します。
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/Set%20Board%20to%20Download%20Mode.png"></p>
    <p align="center"><strong>図 6.2 ボードをダウンロードモードに設定</strong></p>

2. tcc70xx_pflash_boot_2M_ECC.rom を fwdn_vcp フォルダにコピー
```
cp ~/topst-vcp/build/tcc70xx/gcc/output/tcc70xx_pflash_boot_2M_ECC.rom ~/topst-vcp/tools/fwdn_vcp/
```

3. fwdn_vcp フォルダを C ドライブにコピー
```
cp -r ~/topst-vcp/tools/fwdn_vcp /mnt/c/
```

4. fwdn_vcp.bat をクリック  
    ***FWDN*** を使用して、ビルドしたソフトウェアを VCP-G 上の 4 MB フラッシュにダウンロードします。

    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/Click%20fwdn_vcp.bat.png"></p>
    <p align="center"><strong>図 6.3 fwdn_vcp.bat をクリック</strong></p>
```
[main:27] FWDN VCP v0.1.1 - 2022.8.12 11:38:19
Com port num : 10
[FWDNWindowsUART::OpenPort:34] Complete open port(\\.\COM10)
[ProtocolCB::StartVCPFWDN:45] Complete to receive start res
[FWDN_VCP::LoadFwdnFW:144] Complete to send start msg
[ProtocolCB::CheckResPacket:172] Complete to receive ack for cmd(0xFFFF0000(RECEIVE_HSM_CMD))
[FWDN_VCP::WriteFile:284] Complete to send command(0xFFFF0000(RECEIVE_HSM_CMD))
[ProtocolCB::SendFile:151] Complete to send file
[ProtocolCB::CheckResPacket:172] Complete to receive ack for cmd(0xFFFF0000(RECEIVE_HSM_CMD))
[FWDN_VCP::WriteFile:295] Complete to send file - .\tcc70xx_pflash_boot_2M_ECC.rom
[FWDN_VCP::LoadFwdnFW:163] Complete to send hsm
[ProtocolCB::CheckResPacket:172] Complete to receive ack for cmd(0xFFFF0001(RECEIVE_FWDN_CMD))
[FWDN_VCP::WriteFile:284] Complete to send command(0xFFFF0001(RECEIVE_FWDN_CMD))
[ProtocolCB::SendFile:126] uiRemainSize = 43136
[ProtocolCB::SendFile:151] Complete to send file
[ProtocolCB::CheckResPacket:172] Complete to receive ack for cmd(0xFFFF0001(RECEIVE_FWDN_CMD))
[FWDN_VCP::WriteFile:295] Complete to send file - .\vcp_fwdn.rom
[FWDN_VCP::LoadFwdnFW:173] Complete to send fwdn
[FWDN_VCP::LoadFwdnFW:179] Complete to load FWDN F/W
RM=00000000
MT
MR0=0000a042
MR1=00020018
MR2=00000000
[ProtocolFW::CheckResPacket:260] Complete to receive ack for cmd(0xAAAA0016(VERSION_CMD))
[FWDN_VCP::GetDeviceVersion:77]  FWDN Firmware Version(20230728)
[ProtocolFW::CheckResPacket:260] Complete to receive ack for cmd(0xAAAA0014(STORAGE_INFO_CMD))
[FWDN_VCP::InfoStorage:56]
#### SNOR Info ####
Manufacture ID: 0x9d
Device ID: 0x6015
Name: ISSI-IS25LP016D
Sector Size: 4 KiB (4096 Byte)
Total Capacity: 2 MiB (2097152 Byte)
4Byte Address Mode: Unsupported
#### EFLASH Info ####
DCYCRDCON 0x1e0002
DCYCWRCON 0x20100
Sector Size: 8 KiB
Page Size: 2 KiB

-----Storage init info-----
O : Init success
X : Init failed or not exist
SNOR : O
eFlash : O

[ProtocolFW::CheckResPacket:260] Complete to receive ack for cmd(0xAAAA0017(CHIP_INFO_CMD))
[FWDN_VCP::GetChipInfo:121] ---chip info---
Chip Number : 0x57045
Dual Bank : false
Expand Flash : true
ECC : true
[FWDN_VCP::PrintBankInfo:468] ---bank info---
bank - 0
eFlash offset : 0x0
eFlash size : 2097152 byte
SNOR offset : 0x0
SNOR size : 2097152 byte
[FWDN_VCP::PrintStorageOption:451] ---storage info---
eflash
offset : 0x0
size : 2097152 byte
[ProtocolFW::CheckResPacket:260] Complete to receive ack for cmd(0xAAAA0011(WRITE_CMD))
[FWDN_VCP::WriteFile:284] Complete to send command(0xAAAA0011(WRITE_CMD))
 100% [||||||||||||||||||||||||||||||] 2097152/2097152
```

5. ボードをリセットします  
    ダウンロード処理が完了したら、電源ケーブルを取り外して再接続します。
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/Reset%20the%20Board.png"></p>
    <p align="center"><strong>図 6.4 ボードのリセット</strong></p>

### 6.3.2 Linux 環境での FWDN の実行
1. ボードをダウンロードモードに設定  
   FWDN スイッチを押しながら、VCP-G ボードに電源ケーブルを接続します。
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/Set%20Board%20to%20Download%20Mode.png"></p>
    <p align="center"><strong>図 6.5 ボードをダウンロードモードに設定</strong></p>
    
2. ダウンロードコマンドの実行  
   ***FWDN*** を使用して、ビルドしたソフトウェアを VCP-G 上の 4 MB フラッシュにダウンロードします。
    ```
    sudo ~/topst-vcp/tools/fwdn_vcp/fwdn --fwdn ~/topst-vcp/tools/fwdn_vcp/vcp_fwdn.rom -w output/tcc70xx_pflash_boot_2M_ECC.rom
    ```
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/Execute%20Download%20Command.png"></p>
    <p align="center"><strong>図 6.6 ダウンロードコマンドの実行</strong></p>
    
3. ボードをリセットします  
    ダウンロード処理が完了したら、電源ケーブルを取り外して再接続します。
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/Reset%20the%20Board.png"></p>
    <p align="center"><strong>図 6.7 ボードのリセット</strong></p>

</br></br></br>

## 6.4 ボード上のソフトウェアの確認
---
ソフトウェアをボードにダウンロードした後、次の手順に従って正しく動作していることを確認します。
1. minicom のインストール  
    ```
    sudo apt install minicom
    ```
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/Install%20Minicom.png"></p>
    <p align="center"><strong>図 6.8 minicom のインストール</strong></p>
2. シリアル接続を開く  
    次のコマンドを使用してシリアル接続を開始します。
    ```
    minicom -D /dev/ttyUSB0 -b 115200 -8
    ```
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/Open%20Serial%20Connection.png"></p>
    <p align="center"><strong>図 6.9 シリアル接続を開く</strong></p>

手順 1 と手順 2 が完了すると、ターミナルに次の出力が表示されます。接続に成功すると、ボードは操作に応答し、ソフトウェアが VCP-G にダウンロードされて正しく動作していることを確認できます。
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/Figure%206.7%20Open%20Serial%20Connection.png"></p>
<p align="center"><strong>図 6.10 シリアル接続を開く</strong></p>

</br></br></br>

## 6.5 よくある問題のトラブルシューティング
---
この章では、VCP-G の使用中に発生するよくある問題の解決方法を説明します。

**問題:** ***FWDN*** が ttyUSB0 デバイスへのアクセス権限がないと報告します。  
**解決方法:** この問題は、ご使用のユーザーアカウント (**$USER**) にシリアルデバイスへアクセスするために必要な権限がない場合に発生します。これを解決するには、ユーザーアカウントを dialout グループに追加してください。

1. ユーザーグループの権限を変更する  
    次のコマンドを実行します。
    ```
    sudo usermod -aG dialout $USER
    ```
2. ログアウトして再度ログインする  
    現在のセッションからログアウトし、再度ログインして変更を適用します。その後、ttyUSB0 デバイスへのアクセスを再度試してください。
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/Modify%20User%20Group%20Permissions.png"></p>
    <p align="center"><strong>図 6.11 ユーザーグループの権限の変更 </strong></p>

**問題:** minicom の使用時に、VCP-G と正常に通信できない、または動作が不安定になります。  
**解決方法:** この問題は、minicom のフロー制御のデフォルト設定が **hardware** になっている場合に発生することがあります。正しく動作させるには、ハードウェアフロー制御を No に設定する必要があります。 
1. minicom の起動  
    次のコマンドを使用します。
    ```
    minicom -D /dev/ttyUSB0 -b 115200 -8
    ```
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/Launch%20Minicom.png"></p>
    <p align="center"><strong>図 6.12 minicom の起動</strong></p>
2. セットアップ画面へのアクセス  
    minicom の実行中に **[Ctrl+A]** を押してから **[o]** を押し、セットアップメニューを開きます。
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/Access%20Set%20up%20Screen.png"></p>
    <p align="center"><strong>図 6.13 セットアップ画面へのアクセス</strong></p>
3. Serial port setup への移動  
    オプションから **Serial port setup** を選択します。
4. フロー制御の変更  
    シリアルポート設定の画面で **[F]** を押し、ハードウェアフロー制御を **No** に設定します。
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/Modify%20Flow%20Control.png"></p>
    <p align="center"><strong>図 6.14 フロー制御の変更</strong></p>
5. 終了して保存する  
    セットアップを終了し、設定を保存します。これで minicom は VCP-G と正常に通信できるようになります。
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/Save%20and%20Exit.png"></p>
    <p align="center"><strong>図 6.15 保存して終了</strong></p>

**注:** minicom 以外のシリアル通信ツールを使用する場合は、正しく動作させるために、そのツールのフロー制御設定も **No** に設定してください。
</br></br></br></br>

# 7. 参考資料
---
- 詳細については TOPST にお問い合わせください: topst@topst.ai

**注意:** 参考文書は、契約条件に応じて提供可能な場合に提供されます。参考
文書が入手できない場合は、お客様の開発に直接関連する内容をご案内できます。
