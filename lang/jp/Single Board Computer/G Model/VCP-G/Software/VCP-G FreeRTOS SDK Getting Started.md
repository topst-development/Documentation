# 1. はじめに
---
このドキュメントでは、VCP-G SDKのソフトウェア開発環境をセットアップするためのガイドラインを提供します。必要なツール、構成、およびツールチェーンについて概説します。
 
</br></br></br></br>
 
# 2. ホスト環境の設定
---
## 2.1 Ubuntuのインストール
---
Ubuntu 22.04で開発環境をセットアップすることをお勧めします。このUbuntuバージョンは、幅広いコミュニティサポートを備えた安定したプラットフォームを提供し、VCP-Gおよび関連するツールチェーンとの互換性と使いやすさを保証します。
 
Linuxディストリビューションのバージョン:
- Ubuntu 22.04 (LTS)
 
</br></br></br>
 
## 2.2 WSL2 Ubuntuのインストール (Windows環境のみ)
---
**注:** Ubuntuホストを使用している場合は、WSL2のインストールをスキップできます。
 
1.	**コントロールパネル -> プログラム -> Windowsの機能の有効化または無効化 -> 仮想マシンプラットフォームとHyper-Vを有効にする** をクリックして、Windowsの機能を設定します。
2.	**「管理者として実行」** でWindows Powershellを実行します。
3.	WSL2システムを有効にします。
    ```
    dism.exe /online /enable-feature /featurename:Microsoft-Windows-Subsystem-Linux /all /norestart
    ```
4.	仮想マシン機能を有効にします。
    ```
    dism.exe /online /enable-feature /featurename:VirtualMachinePlatform /all /norestart
    ```
5.	WSLをデフォルトバージョンの2 (WSL2) に設定します。
    ```
    wsl --set-default-version 2
    ```
6.	Microsoft StoreでUbuntu 22.04 LTSを検索してダウンロードします。
 
    * Linuxカーネル更新パッケージをダウンロードする必要がある場合は、[こちら](https://learn.microsoft.com/ko-kr/windows/wsl/install-manual)から最新のパッケージをダウンロードしてください。
7.	WSLリストでUbuntu 22.04を確認します。
    ```
    wsl --list -online
    ```
8.	Ubuntu 22.04をインストールします。
    ```
    wsl --install Ubuntu-22.04
    ```
9.	Windowsの検索ボックスでWSL2を検索して実行します。
 
</br></br></br>
 
## 2.3 Linux環境の設定
---
ホストPCにLinux環境をセットアップするには、次の手順に従います。
 
1. WSL2を実行する (Windows環境のみ)
    Windowsを使用している場合は、Windows PowerShellで次のいずれかのコマンドを実行してWSL2を起動します。
    ```
    wsl
    ```
    ```
    ubuntu
    ```
 
2.	パッケージリストの更新
    新しいソフトウェアをインストールする前に、利用可能なパッケージのリストを更新して、最新のバージョンと依存関係を取得してください。次のコマンドは、リポジトリから利用可能なパッケージの最新リストを取得します。
    ```
    sudo apt update && /
    sudo apt upgrade
    ```
 
3.	一般的な開発ツールのインストール
    次のコマンドを入力して、一般的な開発ツールをインストールします。
    ```
    sudo apt install build-essential git
    ```
 
**注:** このコマンドは、build-essentialパッケージとgitの両方をインストールします。
 
</br></br></br></br>
 
# 3. ツールチェーン
---
VCP-Gは **gcc-linaro-7.2.1-2017.11-x86_64_arm-eabi** ツールチェーンを使用します。
このツールチェーンはARMアーキテクチャ向けに最適化されており、VCP-G上のTCC7045チップとの互換性を保証します。
 
</br></br></br>
 
## 3.1 ツールチェーンのインストールとセットアップ
---
次の手順に従って、ツールチェーンをダウンロード、解凍、およびセットアップします。
1. ツールチェーンのダウンロード
   **wget** コマンドを入力して、Linaro Webサイトからツールチェーンをダウンロードします。
    ```
    wget https://releases.linaro.org/components/toolchain/binaries/7.2-2017.11/arm-eabi/gcc-linaro-7.2.1-2017.11-x86_64_arm-eabi.tar.xz
    ```
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/Download%20Toolchain.png"></p>
    <p align="center"><strong>図 3.1 ツールチェーンのダウンロード</strong></p>
    
2. ツールチェーンの解凍
    ダウンロードが完了したら、.tar.xzファイルの内容を解凍します。
    ```
    tar -xvf gcc-linaro-7.2.1-2017.11-x86_64_arm-eabi.tar.xz
    ```
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/Extract%20Toolchain.png"></p>
    <p align="center"><strong>図 3.2 ツールチェーンの解凍</strong></p>
    
3. ツールチェーンを/optに移動
    /optディレクトリは、Linux上のオプションソフトウェアの標準的な場所です。解凍したツールチェーンをこのディレクトリに移動します。
    ```
    sudo mv gcc-linaro-7.2.1-2017.11-x86_64_arm-eabi /opt/
    ```
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/Move%20Toolchain.png"></p>
    <p align="center"><strong>図 3.3 ツールチェーンの移動</strong></p>
 
</br></br></br>
 
## 3.2 ツールチェーンの確認
---
ツールチェーンが正しくインストールされていることを確認します。
1. ツールチェーンディレクトリに移動
    ```
    cd /opt/gcc-linaro-7.2.1-2017.11-x86_64_arm-eabi
    ```
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/Navigate%20to%20Toolchain%20Directory.png"></p>
    <p align="center"><strong>図 3.4 ツールチェーンディレクトリへの移動</strong></p>
    
2. インストールされているGCCコンパイラのバージョンを確認
    ```
    ./bin/arm-eabi-gcc --version
    ```
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/Check%20Version%20of%20Installed%20GCC%20Compiler.png"></p>
    <p align="center"><strong>図 3.5 インストールされているGCCコンパイラのバージョンの確認</strong></p>
 
GCCコンパイラを正常にインストールした後、インストールされているGCCコンパイラのバージョンを確認して、**gcc-linaro-7.2.1-2017.11** と一致することを確認します。
 
</br></br></br></br>
 
# 4. ソースコードのクローン
---
この章では、Gitを使用してソースコードをクローンする方法について説明します。
 
</br></br></br>
 
## 4.1 VCP-Gソースコードのクローン
---
VCP-Gのソースコードを取得するには、**git clone** コマンドを入力します。このコマンドは、リモートリポジトリのコピーをローカルマシンに作成し、コードを直接操作できるようにします。
 
次の手順に従って、VCP-Gソースコードをクローンします。
1. ターミナルを開く
    Ubuntu 22.04システムでターミナルアプリケーションを起動します。
 
2. 目的のディレクトリに移動
    ソースコードを保存する適切な場所を選択します。たとえば、リポジトリをホームディレクトリに保存する場合は、次のコマンドを使用します。
    ```
    cd ~
    ```
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/Navigate%20to%20Desired%20Directory.png"></p>
    <p align="center"><strong>図 4.1 目的のディレクトリへの移動</strong></p>
 
3. リポジトリのクローン
    次のコマンドを使用して、提供されたgitアドレスからVCP-Gソースコードをクローンします。
    ```
    git clone https://github.com/topst-development/FreeRTOS-VCP.git topst-vcp
    ```
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/Figure%204.2%20Clone%20Repository.png"></p>
    <p align="center"><strong>図 4.2 リポジトリのクローン</strong></p>
 
4. クローンしたディレクトリに移動
    クローンプロセスが完了したら、次のコマンドを使用して、ソースコードを含むディレクトリに移動します。
    ```
    cd topst-vcp
    ```
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/Navigate%20to%20Cloned%20Directory.png"></p>
    <p align="center"><strong>図 4.3 クローンしたディレクトリへの移動</strong></p>
 
これで、VCP-Gソースコードをローカルでビルドおよび開発に使用できるようになりました。
 
</br></br></br>
 
## 4.2 ソースコード構造
---
クローン後、**ls** コマンドを入力してディレクトリの内容を一覧表示し、主要なファイルを確認してソースコード構造を理解します。
```
ls
 
build  documents  easy-setup_vcp.sh  LICENSE  scripts  sources  tools
```
 
</br></br></br></br>
 
# 5. ビルドガイド
---
## 5.1 easy-setup_vcp-g.shの実行
---
./easy-setup_vcp-g.shスクリプトを実行すると、次の画面が表示されます。
 
**注意**: ./easy-setup_vcp-g.shを再実行する場合、「yes」を選択するとビルドされたソースが削除されるため注意してください。
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20AI-G/Software/Linux%20SDK/license1.png"></p>
<p align="center"><strong>図 5.1 エンドユーザー使用許諾契約</strong></p>
 
画面の一番下までスクロールして、この通知を読んでください。この通知を読んだ後、右矢印キーと[Enter]を押します。
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20AI-G/Software/Linux%20SDK/license2.png"></p>
<p align="center"><strong>図 5.2 「確認に進む」へ移動</strong></p>
 
 
すると、次の画面が表示されます。
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20AI-G/Software/Linux%20SDK/license3.png" ></p>
<p align="center"><strong>図 5.3 同意画面</strong></p>
[Enter]を押して「Accept」を選択すると、次のコマンドを使用してビルドできます。
 
</br></br></br>
 
## 5.2 Makefileとビルドシステム
---
Makefileは、多くのビルドシステムの重要なコンポーネントです。これには、**make** ユーティリティがプログラムをコンパイルおよびリンクするためのルールとディレクティブが含まれています。Makefileを利用することで、ビルドプロセスを自動化し、一貫性と効率を確保できます。
 
</br></br></br>
 
## 5.3 ビルドプロセスの開始
---
ソースコードをビルドするには、次の手順に従います。
1. ビルドディレクトリに移動します。
    ```
    cd build/tcc70xx/gcc/
    ```
2. **make** コマンドを実行します。
    ```
    make
    ```
    **make** コマンドは、現在のディレクトリにあるMakefileを読み取り、ビルドプロセスを実行します。
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/Run%20make%20Command.png"></p>
    <p align="center"><strong>図 5.4 makeコマンドの実行</strong></p>
    
3. ビルド出力の確認
    ビルドプロセスが完了すると、次の出力ファイルがターミナルに一覧表示されます。
    - output/tcc70xx_pflash_boot.rom
    - output/tcc70xx_pflash_boot_2M_ECC.rom
    - output/tcc70xx_pflash_boot_3M_ECC.rom
    - output/tcc70xx_pflash_boot_4M_ECC.rom
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/Verify%20Build%20Output.png"></p>
    <p align="center"><strong>図 5.5 ビルド出力の確認</strong></p>
   
    出力ファイルのリストを確認するには、次のコマンドを使用します。
    ```
    ls output/ -al
    ```
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/Build%20Output%20File.png"></p>
    <p align="center"><strong>図 5.6 ビルド出力ファイル</strong></p>
 
</br></br></br></br>

# 6. ファームウェアのダウンロード
---
この章では、Linuxベースの開発環境でVCP-Gに ***FWDN*** をダウンロードする方法について説明します。
 
</br></br></br>
 
## 6.1 VCP-Gの準備
---
ダウンロードプロセスを開始する前に、VCP-Gが安定した位置にあり、潜在的な障害がないことを確認してください。すべてのスイッチとコネクタに簡単にアクセスでき、3.3V電源ケーブルが正しく接続されていることを確認してください。
 
</br></br></br>
 
## 6.2 ハードウェアとホストPCの接続
---
Ubuntuホストを使用している場合は、手順3に直接進んでください。
1. usbipd-winのダウンロード
    WSL2でUSBを使用するには、usbipd-winプロジェクトが必要です。
    https://learn.microsoft.com/ko-kr/windows/wsl/connect-usb#attach-a-usb-device からusbipd-winをダウンロードします。
2. PowerShellを実行し、VCP-G (WindowsでCOMポートとして認識される) をWSL2に接続します
    Windows PowerShell (Linuxではない) で次のコマンドを実行します。
    ```
    usbipd list
    ```
    ```
    usbipd bind --busid <busid>
    ```
    ```
    usbipd attach --wsl --busid <busid>
    ```
3. USB Type-Cケーブルの接続
    USB Type-Cケーブルを使用して、VCP-Gボードを開発ホストPCに接続します。
4. USB接続の確認
    WSL2で、次のコマンドを実行します。
    ```
    sudo apt-get install usbutils && lsusb
    ```
    ```
    sudo dmesg | grep tty
    ```
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/Verify%20USB%20Connection.png"></p>
    <p align="center"><strong>図 6.1 USB接続の確認</strong></p>
 
図 6.1に表示される出力が表示されれば、接続は正常に確立されています。
 
</br></br></br>
 
## 6.3 VCP-Gへのソフトウェアのダウンロード
---
 
### 6.3.1 Windows環境でのFWDNの実行
1. ボードをダウンロードモードに設定
   FWDNスイッチを押しながら、電源ケーブルをVCP-Gボードに接続します。
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/Set%20Board%20to%20Download%20Mode.png"></p>
    <p align="center"><strong>図 6.2 ボードをダウンロードモードに設定</strong></p>
 
2. tcc70xx_pflash_boot_2M_ECC.romをfwdn_vcpフォルダにコピー
```
cp ~/topst-vcp/build/tcc70xx/gcc/output/tcc70xx_pflash_boot_2M_ECC.rom ~/topst-vcp/tools/fwdn_vcp/
```
 
3. fwdn_vcpフォルダをCドライブにコピー
```
cp -r ~/topst-vcp/tools/fwdn_vcp /mnt/c/
```
 
4. fwdn_vcp.batをクリック
    ***FWDN*** を使用して、ビルドされたソフトウェアをVCP-Gの4 MBフラッシュにダウンロードします。
 
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/Click%20fwdn_vcp.bat.png"></p>
    <p align="center"><strong>図 6.3 fwdn_vcp.batをクリック</strong></p>
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
 
5. ボードのリセット
    ダウンロードプロセスが完了したら、電源ケーブルを抜き差しします。
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/Reset%20the%20Board.png"></p>
    <p align="center"><strong>図 6.4 ボードのリセット</strong></p>
 
### 6.3.2 Linux環境でのFWDNの実行
1. ボードをダウンロードモードに設定
   FWDNスイッチを押しながら、電源ケーブルをVCP-Gボードに接続します。
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/Set%20Board%20to%20Download%20Mode.png"></p>
    <p align="center"><strong>図 6.5 ボードをダウンロードモードに設定</strong></p>
    
2. ダウンロードコマンドの実行
   ***FWDN*** を使用して、ビルドされたソフトウェアをVCP-Gの4 MBフラッシュにダウンロードします。
    ```
    sudo ~/topst-vcp/tools/fwdn_vcp/fwdn --fwdn ~/topst-vcp/tools/fwdn_vcp/vcp_fwdn.rom -w output/tcc70xx_pflash_boot_2M_ECC.rom
    ```
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/Execute%20Download%20Command.png"></p>
    <p align="center"><strong>図 6.6 ダウンロードコマンドの実行</strong></p>
    
3. ボードのリセット
    ダウンロードプロセスが完了したら、電源ケーブルを抜き差しします。
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/Reset%20the%20Board.png"></p>
    <p align="center"><strong>図 6.7 ボードのリセット</strong></p>
 
</br></br></br>
 
## 6.4 ボード上のソフトウェアの確認
---
ソフトウェアをボードにダウンロードした後、次の手順に従って正しく動作していることを確認します。
1. minicomのインストール
    ```
    sudo apt install minicom
    ```
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/Install%20Minicom.png"></p>
    <p align="center"><strong>図 6.8 minicomのインストール</strong></p>
2. シリアル接続を開く
    次のコマンドを使用して、シリアル接続を開始します。
    ```
    minicom -D /dev/ttyUSB0 -b 115200 -8
    ```
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/Open%20Serial%20Connection.png"></p>
    <p align="center"><strong>図 6.9 シリアル接続を開く</strong></p>
 
手順1と2を完了すると、ターミナルに次の出力が表示されます。接続が成功した場合、ボードは対話に応答し、ソフトウェアがダウンロードされ、VCP-G上で正しく動作していることを確認します。
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/Figure%206.7%20Open%20Serial%20Connection.png"></p>
<p align="center"><strong>図 6.10 シリアル接続を開く</strong></p>
 
</br></br></br>
 
## 6.5 一般的な問題のトラブルシューティング
---
この章では、VCP-Gでの作業中に発生する一般的な問題の解決策を提供します。
 
**問題:** ***FWDN*** がttyUSB0デバイスへのアクセス許可がないと報告する。
**解決策:** この問題は、ユーザーアカウント (**$USER**) にシリアルデバイスにアクセスするために必要な権限がない場合に発生します。これを解決するには、ユーザーアカウントをdialoutグループに追加します。
 
1. ユーザーグループ権限の変更
    次のコマンドを実行します。
    ```
    sudo usermod -aG dialout $USER
    ```
2. ログアウトして再度ログイン
    現在のセッションからログアウトし、再度ログインして変更を適用します。その後、ttyUSB0デバイスへのアクセスを再試行してください。
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/Modify%20User%20Group%20Permissions.png"></p>
    <p align="center"><strong>図 6.11 ユーザーグループ権限の変更</strong></p>
 
**問題:** minicomを使用しているときに、VCP-Gとの通信が適切に行われないか、動作が不安定になる。
**解決策:** この問題は、minicomのデフォルトのフロー制御設定が **hardware** に設定されている場合に発生する可能性があります。適切に動作させるには、ハードウェアフロー制御をNoに設定する必要があります。
1. minicomの起動
    次のコマンドを使用します。
    ```
    minicom -D /dev/ttyUSB0 -b 115200 -8
    ```
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/Launch%20Minicom.png"></p>
    <p align="center"><strong>図 6.12 minicomの起動</strong></p>
2. セットアップ画面へのアクセス
    minicomで、**[Ctrl+A]** を押してから **[o]** を押して、セットアップメニューを開きます。
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/Access%20Set%20up%20Screen.png"></p>
    <p align="center"><strong>図 6.13 セットアップ画面へのアクセス</strong></p>
3. シリアルポート設定への移動
    オプションから **Serial port setup** を選択します。
4. フロー制御の変更
    シリアルポート設定内で、**[F]** を押してハードウェアフロー制御を **No** に設定します。
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/Modify%20Flow%20Control.png"></p>
    <p align="center"><strong>図 6.14 フロー制御の変更</strong></p>
5. 終了して保存
    セットアップを終了し、構成を保存します。これで、minicomはVCP-Gと適切に通信するはずです。
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/Save%20and%20Exit.png"></p>
    <p align="center"><strong>図 6.15 保存して終了</strong></p>
 
**注:** minicom以外のシリアル通信ツールを使用している場合は、適切に動作させるために、そのフロー制御設定も **No** に設定されていることを確認してください。
</br></br></br></br>
 
# 7. 参考文献
---
- 詳細については、TOPSTにお問い合わせください: topst@topst.ai
 
**注:** 参考文献は、契約条件に応じて、利用可能な場合にいつでも提供できます。参考文献が利用できない場合は、開発に直接関連する内容をご案内できます。
