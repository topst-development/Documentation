# 1. はじめに
---
このドキュメントでは、ホスト環境のセットアップ、SDKのビルド、ファームウェアダウンローダーの使用、Ubuntuのダウンロードなど、D3-G SDKをビルドするためのガイドラインを提供します。

このドキュメントには、以下の情報が含まれています。
- ホスト環境の設定
- イメージビルドガイド
- ファームウェアダウンロードガイド
- D3-GボードとPCの接続

<br/><br/><br/><br/>

# 2. ホスト環境の設定
---
この章では、ホストPC環境をセットアップする方法について説明します。WindowsとUbuntuのガイドは別々に記載されています。
</br><br/><br/>

## 2.1 Windows環境
---
このドキュメントでは、Windows PCでLinuxを使用するためにWindows Subsystem for Linux (WSL) をセットアップする方法について説明します。
D3-G Linux SDKはYocto Projectに基づいているため、D3-G SDKのLinuxバージョンはYocto Projectに従います。
別のバージョンのLinuxをインストールすることもできますが、このドキュメントでは、Ubuntu 22.04に基づいたD3-G Linux SDKについて説明します。
ホストOSがUbuntuの場合は、2.2章に進んでください。

</br><br/>

### 2.1.1 WSL2 Ubuntuのインストール
1. "**管理者権限で実行**"でWindows PowerShellを実行します。
2. WSL2システムを有効にします。
    ```
    dism.exe /online /enable-feature /featurename:Microsoft-Windows-Subsystem-Linux /all /norestart
    ```
3. 仮想マシン機能を有効にします。
    ```
    dism.exe /online /enable-feature /featurename:VirtualMachinePlatform /all /norestart
    ```
4. WSL 2をデフォルトバージョンに設定します。
    ```
    wsl --set-default-version 2
    ```
5. Microsoft StoreでUbuntu 22.04.3 LTSを検索してダウンロードします。

    * Linuxカーネル更新パッケージをダウンロードする必要がある場合は、[こちら](https://learn.microsoft.com/ko-kr/windows/wsl/install-manual)から最新のパッケージをダウンロードしてください。

6. Ubuntuのインストール中に任意のユーザー名を選択します。
</br><br/>

### 2.1.2 WSL2経由でのUbuntuへのアクセス
Windowsコマンドプロンプトを開き、次のコマンドを入力してUbuntuにアクセスします。
Ubuntuにアクセスすると、デフォルトで/mnt/c/Users/[username]ディレクトリで起動します。
```
wsl  // ubuntuにアクセス
ls   // ディレクトリ内のコンテンツを確認
```
結果を確認するには、図 2.1を参照してください (結果はシステムによって異なる場合があります)。
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20D3-G/Software/1.1%20wsl%20linux.png" width="500"></p>
<p align="center"><strong>図 2.1 WSL2スクリーンショット </strong></p>

<br/><br/>

### 2.1.3 ロケールの設定

WSLでUbuntuを実行した後、適切な言語と地域の設定を確保するためにロケールを設定する必要があります。en_US.UTF-8を使用することをお勧めします。en_US.UTF-8を使用するには、次のコマンドを実行します。

```
sudo locale-gen en_US.UTF-8 && sudo update-locale LANG=en_US.UTF-8 
```

ロケールを設定した後、次のコマンドを使用してロケールタイプを確認できます。

```
echo 'LANG=en_US.UTF-8' | sudo tee -a /etc/default/locale && \  

echo 'LC_ALL=en_US.UTF-8' | sudo tee -a /etc/default/locale 
```
<br/><br/>

### 2.1.4 SSHとSambaのインストール

Ubuntuに入った後、SSHやSambaなどの追加ユーティリティを使用して、より便利な開発環境を構築できます。SSHとSambaを使用すると、リモートコンピュータでコマンドを実行したり、他のコンピュータにファイルをコピーしたりできます。
 - 次の手順では、ホストPCがネットワークに接続されている必要があります。次のコマンドを使用してネットワークの状態を確認してください。
  ```
  $ sudo apt-get update
  $ sudo apt-get install -y net-tools
  $ ifconfig 
  ```

SSHとSambaがすでにインストールされている場合、またはそれらを使用しない場合は、この章をスキップできます。

次のコマンドを使用して、net-tools、SSH、Sambaをインストールします。

```
$ sudo apt-get update 
$ sudo apt install -y net-tools openssh-server samba
```
SSHとSambaをインストールした後、環境に合わせて各プログラムを構成します。
</br><br/>

### 2.1.5 ユーティリティのインストール

次のコマンドを使用して、必要なすべてのユーティリティを一度にインストールします。Yocto Projectを使用するには、ホストPC (個々のコンピュータまたは開発サーバー) に次のユーティリティをインストールする必要があります。


```
$ sudo apt-get install -y gawk wget git diffstat unzip texinfo gcc-multilib build-essential chrpath

$ sudo apt-get install -y socat cpio python3 python3-pip python3-pexpect xz-utils debianutils

$ sudo apt-get install -y iputils-ping python3-git python3-jinja2 libegl1-mesa-dev libsdl1.2-dev pylint

$ sudo apt-get install -y xterm zstd ncftp curl git-lfs vim zip lz4
```

<br/><br/>

### 2.1.6 Repoのインストール

Repoがすでにインストールされている場合は、再インストールせずに使用できます。
Repoをインストールする前に、Pythonバージョン3.6以降がインストールされていることを確認してください。

次のコマンドを使用してRepoをインストールします。
```
$ sudo apt-get install repo
```

'/usr/bin/env 'python' no such file or directory' というエラーメッセージが表示された場合は、次のコマンドを使用して 'python' を 'python3' にリンクします。

```
$ sudo ln -sf /usr/bin/python3 /usr/bin/python
```
Repoエラーが発生した場合は、次のコマンドを使用して最新バージョンをダウンロードし、/usr/bin/ フォルダに配置します。

```
$ mkdir -p ~/bin

$ curl http://commondatastorage.googleapis.com/git-repo-downloads/repo > ~/bin/repo

$ chmod a+x ~/bin/repo

$ sudo mv ~/bin/repo /usr/bin/repo
```
**第3章: イメージビルドガイド**に進みます。

<br/><br/><br/>

## 2.2 Linux環境
---
この章では、ホストOSとしてのUbuntuのセットアッププロセスについて説明します。
</br><br/>

### 2.2.1 環境設定
次の章 (2.2.2〜2.2.5) は、Ubuntuターミナルで実行する必要があります。ターミナルを開くには、ショートカット [Ctrl + Alt + T] を使用します。
<br/><br/>

### 2.2.2 ロケールの設定

WSLでUbuntuを実行した後、適切な言語と地域の設定を確保するためにロケールを設定する必要があります。en_US.UTF-8を使用することをお勧めします。en_US.UTF-8を使用するには、次のコマンドを実行します。

```
sudo locale-gen en_US.UTF-8 && sudo update-locale LANG=en_US.UTF-8 
```

ロケールを設定した後、次のコマンドを使用してロケールタイプを確認できます。

```
echo 'LANG=en_US.UTF-8' | sudo tee -a /etc/default/locale && \  

echo 'LC_ALL=en_US.UTF-8' | sudo tee -a /etc/default/locale 
```
<br/><br/>

### 2.2.3 SSHとSambaのインストール

Ubuntuに入った後、SSHやSambaなどの追加ユーティリティを使用して、より便利な開発環境を構築できます。SSHとSambaを使用すると、リモートコンピュータでコマンドを実行したり、他のコンピュータにファイルをコピーしたりできます。
 - 次の手順では、ホストPCがネットワークに接続されている必要があります。次のコマンドを使用してネットワークの状態を確認してください。
  ```
  $ sudo apt-get update
  $ sudo apt-get install -y net-tools
  $ ifconfig 
  ```

SSHとSambaがすでにインストールされている場合、またはそれらを使用しない場合は、この章をスキップできます。

次のコマンドを使用して、SSH、Sambaをインストールします。

```
$ sudo apt-get update 
$ sudo apt install -y openssh-server samba
```
SSHとSambaをインストールした後、環境に合わせて各プログラムを構成します。

<br/><br/>

### 2.2.4 ユーティリティのインストール

次のコマンドを使用して、必要なすべてのユーティリティを一度にインストールします。Yocto Projectを使用するには、ホストPC (個々のコンピュータまたは開発サーバー) に次のユーティリティをインストールする**必要があります**。
****


```
$ sudo apt-get install -y gawk wget git diffstat unzip texinfo gcc-multilib build-essential chrpath

$ sudo apt-get install -y socat cpio python3 python3-pip python3-pexpect xz-utils debianutils

$ sudo apt-get install -y iputils-ping python3-git python3-jinja2 libegl1-mesa-dev libsdl1.2-dev pylint

$ sudo apt-get install -y xterm zstd ncftp curl git-lfs vim zip lz4
```

<br/><br/>

### 2.2.5 Repoのインストール

Android Repoを介してD3-G SDKをダウンロードできます。
Repoをインストールするには、次のWebサイトを参照してください: https://source.android.com/source/downloading.html。
Repoがすでにインストールされている場合は、再インストールせずに使用できます。
Repoをインストールする前に、Pythonバージョン3.6以降がインストールされていることを確認してください。

次のコマンドを使用してRepoをインストールします。
```
$ sudo apt-get install repo
```

'/usr/bin/env 'python' no such file or directory' というエラーメッセージが表示された場合は、次のコマンドを使用して 'python' を 'python3' にリンクします。

```
$ sudo ln -sf /usr/bin/python3 /usr/bin/python
```
Repoエラーが発生した場合は、次のコマンドを使用して最新バージョンをダウンロードし、/usr/bin/ フォルダに配置します。

```
$ mkdir -p ~/bin

$ curl http://commondatastorage.googleapis.com/git-repo-downloads/repo > ~/bin/repo

$ chmod a+x ~/bin/repo

$ sudo mv ~/bin/repo /usr/bin/repo
```

<br/><br/>

### 2.2.6 Telechips USBデバイスのUdevルール
次のコマンドを実行すると、LinuxでFWDNをダウンロードするときに 'sudo' コマンドを使用する必要がなくなります。
```
$ echo "SUBSYSTEM==\"usb\", ATTR{idVendor}==\"140e\", MODE=\"0666\", OWNER=\"${USER}\"" | sudo tee /etc/udev/rules.d/99-topst.rules
$ sudo udevadm control --reload-rules && sudo udevadm trigger
```
**第3章: イメージビルドガイド**に進みます。

<br/><br/><br/><br/>

# 3. イメージビルドガイド
---
この章では、ホストPCにインストールされているUbuntu OS (WSLかローカルUbuntuインストールかに関係なく) に基づいたガイダンスを提供します。D3-GにアップロードするイメージはYocto Projectを使用してビルドされるため、ビルドプロセスはUbuntu環境で実行する必要があります。
</br></br>

## 3.1 SDKビルドの準備
---
D3-G Linux SDKはYocto Project 4.0 Kirkstoneに基づいています。したがって、D3-G Linux SDKを使用するには、ホストPCでYocto Project環境を構成する必要があります。SDK、ソースミラー、およびツールをダウンロードするには、必要なユーティリティをインストールする必要があります。イメージをスムーズにビルドするには、PCに**少なくとも60 GBの空きストレージ**と**最低16 GBのRAM**が必要です。

</br><br/>  

## 3.2 Yocto Project  
---
Yocto Projectは、組み込みLinux開発に焦点を当てたオープンソースプロジェクトです。
Linuxイメージを作成するためのビルドシステムとして、PokyであるOpen Embeddedプロジェクトと***bitbake***の組み合わせを使用します。
Yocto Projectを使用することで、ブートローダー、カーネル、rootfsを同時にビルドできます。

<br/><br/>

## 3.3 Yocto Projectのタスクプロセス
---
図 3.1は、Yocto Projectのタスクプロセスを示しています。メタデータに基づいてアップストリームからソースをダウンロードしてビルドできます。ビルドが完了すると、パッケージ、イメージ、およびSDKが結果として提供されます。

<p align="center">
    <img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20D3-G/Software/2.1%20yocto%20project%20task%20process.png", width="700">
</p>
<p align="center"><strong>図 3.1 Yocto Projectタスクプロセス</strong></p>

<br/><br/>

## 3.4 D3-G SDKの構成
---
以下は、構成したYocto Projectのコンポーネントです。
表 3.1は、D3-G SDKの構成を示しています。



**表 3.1 D3-G SDKの構成**
<table border="1" cellspacing="0" cellpadding="5">
  <colgroup>
    <col style="width: 10%">
    <col style="width: 10%">
    <col style="width: 10%">
    <col style="width: 56%">
  </colgroup>
  <thead>
    <tr>
      <th colspan="3"style="text-align: center; vertical-align: middle;"><strong>項目</strong></th>
      <th style="text-align: center; vertical-align: middle;" ><strong>説明</strong></th>
    </tr>
  </thead>
  <tbody>
  <tr>
      <td colspan="3"style="text-align: center; vertical-align: middle;">easy-setup.sh</td>
      <td>SDKを自動的にダウンロードしてビルドするためのPythonスクリプト</td>
    </tr>
    <tr>
      <td colspan="3"style="text-align: center; vertical-align: middle;">stitch-fai-ai.sh</td>
      <td>AI-G faiイメージ (最小 + サンプルアプリケーション) を作成するためのスクリプト</td>
    </tr>
    <tr>
      <td colspan="3"style="text-align: center; vertical-align: middle;">stitch-fai-d3.sh</td>
      <td>D3-G faiイメージ (最小 + サンプルアプリケーション) を作成するためのスクリプト</td>
    </tr>
    <tr>
      <td colspan="3"style="text-align: center; vertical-align: middle;">mktcimg</td>
      <td rowspan="2">ビルドプロセスおよび<strong>FWDN</strong>に関連するツール</td>
    </tr>
    <tr>
      <td colspan="3"style="text-align: center; vertical-align: middle;">tools</td>
    </tr>
    <tr>
      <td rowspan="8"style="text-align: center; vertical-align: middle;">poky</td>
      <td colspan="2"style="text-align: center; vertical-align: middle;">poky</td>
      <td>Yocto Project 4.0 Kirkstoneビルドシステム</td>
    </tr>
    <tr>
      <td colspan="2"style="text-align: center; vertical-align: middle;">meta-openembedded</td>
      <td>OE-Coreをサポートするレイヤー</td>
    </tr>
    <tr>
      <td colspan="2"style="text-align: center; vertical-align: middle;">meta-arm</td>
      <td>ARMツールチェーンをサポートするレイヤー</td>
    </tr>
    <tr>
      <td colspan="2"style="text-align: center; vertical-align: middle;">meta-topst-bsp</td>
      <td>TOPST BSPをサポートするレイヤー</td>
    </tr>
    <tr>
      <td colspan="2"style="text-align: center; vertical-align: middle;">meta-gplv2</td>
      <td>GPLv3ライセンスを回避するパッケージを含むレイヤー</td>
    </tr>
    <tr>
      <td colspan="2"style="text-align: center; vertical-align: middle;">meta-topst</td>
      <td>TOPSTレシピ</td>
    </tr>
  </tbody>
</table>
<br/><br/><br/>
 
 
## 3.5 ビルドの準備
---
次の章では、D3-GイメージをビルドするためにYocto Projectを構成する方法について説明します。
 
<br/><br/>
 
### 3.5.1 .gitconfigでのユーザーメールとユーザー名の設定
公式TOPST gitからD3-G SDKをダウンロードするには、メールと名前を設定します。
1. 次のコマンドを入力します。
```
vi ~/.gitconfig
```
2. 次の情報を入力します。
```
[user]
    email = User email
    name = User name
```
 
<br/><br/>
 
### 3.5.2 GitからD3-Gを取得
 
1. **topst-sdk**という名前の新しいディレクトリを作成し、現在のディレクトリを**topst-sdk**に変更します。
 
```
$ mkdir topst-sdk
$ cd topst-sdk
```
 
2. 次のコマンドを実行して、リポジトリを初期化します。
 
```
$ repo init -u https://github.com/topst-development/manifests.git -b release/1.2.0 -m linux_yp4.0_topst.xml
```
 
コマンドを実行すると、次の出力が表示されます。
 
```
Downloading Repo source from https://gerrit.googlesource.com/git-repo
 
... A new version of repo (2.54) is available.
... New version is available at: /home/topst/topst-sdk/.repo/repo/repo
... The launcher is run from: /usr/bin/repo
!!! The launcher is not writable.  Please talk to your sysadmin or distro
!!! to get an update installed.
 
 
Your identity is: TopstDeveloper <topstdeveloper@gmail.com>
If you want to change this, please re-run 'repo init' with --config-name
 
repo has been initialized in /home/topst/topst-sdk
```
 
3. 次のコマンドを実行して、リポジトリを同期します。
 
```
$ repo sync
```
 
コマンドを実行すると、次の出力が表示されます。
 
```
... A new version of repo (2.54) is available.
... New version is available at: /home/topst/topst-sdk/.repo/repo/repo
... The launcher is run from: /usr/bin/repo
!!! The launcher is not writable.  Please talk to your sysadmin or distro
!!! to get an update installed.
 
Fetching: 100% (12/12), done in 33.103s
Checking out:  25% (3/12), done in 0.863s
Checking out:  75% (9/12), done in 0.415s
repo sync has finished successfully.
```
 
<br/><br/><br/>
 
## 3.6 topst-build.shの実行
---
./easy-setup.shスクリプトを実行すると、次の画面が表示されます。
 
**注意: ./easy-setup.shを再実行する場合、yesを選択するとビルドされたソースが削除されるため注意してください。**
```
./easy-setup.sh
```
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20AI-G/Software/Linux%20SDK/license1.png"></p>
<p align="center"><strong>図 3.2 エンドユーザー使用許諾契約</strong></p>
 
画面の一番下までスクロールして、この通知を読んでください。この通知を読んだ後、右矢印キーを押して [Enter] を押します。
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20AI-G/Software/Linux%20SDK/license2.png"></p>
<p align="center"><strong>図 3.3 'Proceed to confirm' に移動</strong></p>
 
 
すると、次の画面が表示されます。
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20AI-G/Software/Linux%20SDK/license3.png" ></p>
<p align="center"><strong>図 3.4 同意画面 </strong></p>
 
 
ビルドイメージは次のパスに作成されます。
 
- {TOPST_PATH}/build/d3-g-topst-main/tmp/deploy/images/d3-g-topst-main
 
topst-build.shは、D3-GおよびAI-Gのイメージをビルドするために必要なコア環境をセットアップするシェルスクリプトです。次のコマンドを実行し、オプション2を選択して、D3-GにメインOSをインストールするためのビルド環境を準備します。
 
 
 
```
$ source poky/meta-topst/topst-build.sh 
Choose MACHINE
  1. ai-g-topst
  2. d3-g-topst-main
  3. d3-g-topst-sub
  4. d5-g-topst-main
  5. d5-g-topst-sub
select number(1-5) => 2
machine(d3-g-topst-main) selected.
You had no conf/local.conf file. This configuration file has therefore been
created for you from /home/topst/topst-sdk/poky/meta-topst/template/d3-g-topst-main/local.conf.sample
You may wish to edit it to, for example, select a different MACHINE (target
hardware). See conf/local.conf for more information as common configuration
options are commented.
 
You had no conf/bblayers.conf file. This configuration file has therefore been
created for you from /home/topst/topst-sdk/poky/meta-topst/template/d3-g-topst-main/bblayers.conf.sample
To add additional metadata layers into your configuration please add entries
to conf/bblayers.conf.
 
The Yocto Project has extensive documentation about OE including a reference
manual which can be found at:
    https://docs.yoctoproject.org
 
For more information about OpenEmbedded see the website:
    https://www.openembedded.org/
 
Yocto Project common targets are:
    core-image-minimal
    core-image-sato
    meta-toolchain
    adt-installer
    meta-ide-support
 
 
Telechips common targets are:
    telechips-topst-image-minimal
    telechips-topst-image-multimedia
    telechips-topst-image
 
    meta-toolchain-topst(Application Development Toolkit)
 
 
You can also run generated TOPST images on D3-G board
 
Other commonly useful commands are:
 - 'devtool' and 'recipetool' handle common recipe tasks
 - 'bitbake-layers' handles common layer tasks
 - 'oe-pkgdata-util' handles common target package tasks
 
```
 
次のコマンドを実行して、メインOSのビルドを開始します。
```
$ bitbake telechips-topst-image
```
 
<br/><br/><br/>
 
## 3.7 ファームウェアダウンローダー (FWDN) イメージの作成
---
このオプションは、バイナリをD3-Gプラットフォームイメージ用の単一のイメージに結合します。
 
**'output_d3g.fai' ビルドイメージ**と**FWDNツール**を含む**output_d3g.fwdn.zip**ファイルは、次のパスに作成されます。
 
-  ~/topst-sdk
 
```
$ cd ~/topst-sdk
 
$ ./stitch-fai-d3.sh -f
Filesystem too small for a journal
[mktcimg] v1.2.1 - Nov 15 2021 19:33:18
location : bl3_ca72_a
location : 4096 sector(2097152 byte)
location : build/d3-g-topst-main/tmp/deploy/images/d3-g-topst-main/ca72_bl3.rom
location : boot
location : 122880 sector(62914560 byte)
location : build/d3-g-topst-main/tmp/deploy/images/d3-g-topst-main/tc-boot-d3-g-topst-main.img
location : system
location : 33554432 sector(17179869184 byte)
location : build/d3-g-topst-main/tmp/deploy/images/d3-g-topst-main/telechips-topst-image-d3-g-topst-main.ext4
location : dtb
location : 400 sector(204800 byte)
location : build/d3-g-topst-main/tmp/deploy/images/d3-g-topst-main/tcc8050-topst-d3-g.dtb
path : build/d3-g-topst-main/tmp/deploy/images/d3-g-topst-main/ca72_bl3.rom
uuid : 7eb23c82-ccc0-44ce-8237-3315fc34e3f5 , part-name : bl3_ca72_a
uuid : 1c76ef36-314d-4548-8207-5ab1d1376ca2 , part-name : boot
uuid : b32eb80f-e014-4f17-b140-77bf3e137ba0 , part-name : system
uuid : 429d8444-87b0-4c1d-8b3f-278dec2616f3 , part-name : dtb
crc32 of header : 2a7c0194
crc32 of partition array : b181e432
idx : 0  bl3_ca72_a
idx : 1  boot
idx : 2  system
idx : 3  dtb
crc32 of header : 2a7c0194
crc32 of partition array : 990446d3
Complete to make fai file
 
===== arguments info =====
 
--storage_size : 17818182656
--parttype : gpt
--area_name : "SD Data"
--outfile : /home/topst/topst-sdk/.stitch_tOPE26E/output_d3g.fai
--gptfile : /home/topst/topst-sdk/.stitch_tOPE26E/output_d3g.gpt
--fplist : /home/topst/topst-sdk/.stitch_tOPE26E/partition.single.list
--sector_size : 512
--sparse_fill : 0
 
===========================
 
[+] Packaging FWDN binaries
  adding: boot-firmware/ (stored 0%)
  adding: boot-firmware/boot.dual.json (deflated 87%)
  adding: boot-firmware/prebuilt/ (stored 0%)
  adding: boot-firmware/prebuilt/subcore_optee.rom (deflated 93%)
  adding: boot-firmware/prebuilt/mcert.bin (deflated 96%)
  adding: boot-firmware/prebuilt/fwdn.rom (deflated 49%)
  adding: boot-firmware/prebuilt/bconf.dual.bin (deflated 95%)
  adding: boot-firmware/prebuilt/ca72_bl1.rom (deflated 53%)
  adding: boot-firmware/prebuilt/dram_params.bin (deflated 81%)
  adding: boot-firmware/prebuilt/hsm.cs.bin (deflated 13%)
  adding: boot-firmware/prebuilt/ca72_bl2.rom (deflated 54%)
  adding: boot-firmware/prebuilt/ca53_bl1.rom (deflated 53%)
  adding: boot-firmware/prebuilt/optee.rom (deflated 93%)
  adding: boot-firmware/prebuilt/ca53_bl2.rom (deflated 52%)
  adding: boot-firmware/prebuilt/hsm.bin (deflated 49%)
  adding: boot-firmware/prebuilt/bconf.single.bin (deflated 93%)
  adding: boot-firmware/prebuilt/scfw.rom (deflated 57%)
  adding: boot-firmware/prebuilt/tcc8050_snor.cs.rom (deflated 93%)
  adding: boot-firmware/boot.single.json (deflated 87%)
  adding: boot-firmware/fwdn.json (deflated 50%)
  adding: fwdn (deflated 69%)
  adding: fwdn.bat (deflated 40%)
  adding: fwdn.exe (deflated 62%)
  adding: fwdn.sh (deflated 40%)
  adding: output_d3g.fai (deflated 73%)
  adding: output_d3g.gpt (deflated 99%)
  adding: output_d3g.gpt.back (deflated 98%)
  adding: output_d3g.gpt.prim (deflated 98%)
  adding: VtcUsbPort.dll (deflated 68%)
 
次のログが表示された場合、"output_d3g.fwdn.zip" ファイルが作成されたことを意味します。
```
$ ls
build  easy-setup.sh  mktcimg  output_d3g.fwdn.zip  poky  stitch-fai-ai.sh  stitch-fai-d3.sh  tools
```
 
</br></br><br/><br/>
 
# 4. ファームウェアのダウンロード
---
この章では、***FWDN***を使用してファームウェアをD3-Gにダウンロードし、Linuxコンソールにログインする方法について説明します。
***FWDN V8***は、Windows 10(11) 64ビットおよびLinux環境の両方でファームウェアをダウンロードするためのPCツールです。この章では、WindowsおよびLinux環境でのダウンロードのケースについて説明します。
 
<br/><br/><br/>
 
## 4.1 ファームウェアダウンロードシーケンス
---
***FWDN***のダウンロードシーケンスは次のとおりです。
 
1. ブートモードスイッチをUSBブートモードに設定します。
2. WindowsプロンプトまたはLinuxコンソールを開きます。
3. ***FWDN V8***をボードに接続します。
4. faiファイルをダウンロードします。
 
<br/><br/><br/>
 
## 4.2 USBブートモードでのD3-GボードとホストPCの接続
---
ファームウェアダウンローダー (FWDN) は、ホストPCとのUSB通信を介してD3-GにROMイメージを書き込みます。
 
D3-Gには1つのブートモードボタンがあり、2種類のブートモードをサポートしています。このガイドではFWDNモードに焦点を当てています。
 
- USBブートモード (FWDNモード) : ホストPC上のFWDNツールを使用してROMイメージを書き込むために使用されます
 
- eMMCブートモード : eMMCデバイスに保存されているROMイメージを使用してD3-Gを起動するために使用されます
 
**注**: USB Type-C FWDNポートは、ファームウェアダウンローダー (FWDN) に使用されます。
 
 
 
FWDNを使用するには、次のようにD3-GボードをホストPCに接続します。
 
1. ホストPCにVTCドライバーがインストールされていることを確認します。VTCドライバーがインストールされていない場合は、4.2.1章に示すようにインストールしてください。
 
2. USB Type-Cケーブルを1本用意します。
 
3. USBブートモードに入るには、FWDNスイッチを押しながら電源ケーブルをD3-Gボードに接続します。
   - 詳細については、サイドバーのハードウェアセクションの**「2. ブートモード」**を参照してください。
 
4. USB Type-CケーブルをD3-GボードのUSB Type-C FWDNポートとホストPCに接続します。
 
<p align="center">
    <img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20D3-G/Hardware/connect%20to%20d3g%20to%20host%20pc%20using%20c%20type.png">
</p>
<p align="center"><strong>図 4.1 USB Cタイプケーブルを使用したD3-GボードとホストPCの接続 </strong></p>
 
<br/><br/>
 
### 4.2.1 VTCドライバーのインストール方法 (Windows/Ubuntu)
管理者として実行して、ホストPCにVendor Telechips Certification (VTC) ドライバー ([telechips driver](https://drive.google.com/file/d/1muQnY8kuKxDsy3p3FUiQqcG34Zjk-mnR/view?usp=sharing)にあります) をインストールします。上記のようにFWDNモードでUSBを接続すると、Telechips VTC USBドライバーが図 4.2および図 4.3に示すように設定されます。
 
<p align="center">
    <img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20D3-G/Software/USB%20Connection%20in%20Windows%20Environment.png", width="700">
</p>
<p align="center"><strong>図 4.2 Windows環境でのUSB接続</strong></p>
 
<p align="center">
    <img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20D3-G/Software/USB%20Connection%20in%20Linux%20System.png", width="700">
</p>
<p align="center"><strong>図 4.3 Linux環境でのUSB接続</strong></p>
 
**注**: VTC Driver V5.0.0.14以降を使用してください。バージョンを確認するには、Windows環境のデバイスマネージャーを確認してください。
 
<br/><br/><br/>
 
## 4.3 FWDNダウンロードの準備
---
FWDNを実行する前に、Ubuntu (WSL2) 環境で作成されたイメージとツールをWindows環境に転送します。
 
 
1. "output_d3g.fwdn.zip" を解凍します。
    ```
    $ cd ~/topst-sdk
    $ mkdir images
    $ mv ./output_d3g.fwdn.zip ./images
    $ cd images
    $ unzip output_d3g.fwdn.zip
    ```
2. "images" フォルダをWindows Cドライブにコピーします。
    ```
    $ cd ..
    $ cp -r ./images /mnt/c/
    ```
 
<br/><br/><br/>
 
## 4.4 Windows環境でのFWDN
---
1. Powershellを実行し、"C:\images\" に移動します。
```
$ cd C:\images 
```
 
2. **.\fwdn.bat** コマンドを入力して、ファームウェアのダウンロードを開始します。“fwdn.bat” は、FWDN V8を使用してファームウェアを自動的にダウンロードする実行可能ファイルです。
 
```
.\fwdn.bat
 
C:\images>fwdn.exe --fwdn boot-firmware\fwdn.json
[main:30] FWDN V8 v1.4.6 - 2021.12.13 13:42:37
[FWDN_V8::LoadFWDNRom:403] Start to load FWDN rom
[FWDN_V8::LoadMCERT:592] C:\images\boot-firmware\mcert.bin
[FWDN_V8::LoadHSM:609] C:\images\boot-firmware\hsm.cs.bin
[FWDN_V8::SendFWDNHeader:634] C:\images\boot-firmware\fwdn.rom - Header
[FWDN_V8::SendFWDNBody_V8:537] C:\images\boot-firmware\fwdn.rom - Body
[FWDN_V8::LoadFWDNRom:414] Complete to load FWDN rom
[FWDN_V8::GetFWDNRomVersion:1526] fwdn.rom version : 21.9.29
[FWDN_V8::GetFileAndWriteCommand:748] C:\images\boot-firmware\dram_params.bin
[FWDN_V8::PrintDeviceInfo:1183] --------------Device info-------------
[FWDN_V8::PrintDeviceInfo:1184]
 
----- Detail of Storages -----
#### eMMC Info ####
Manufacture ID: 0x15
OEM: 0x100
Name: 8GTF4
User Capacity: 7.3 GiB (7818182656 Byte)
Boot Capacity: 4 MiB (4194304 Byte)
RPMB Capacity: 512 KiB (524288 Byte)
Speed Mode: HS200
#### SNOR Info ####
Manufacture ID: 0xc2
Device ID: 0x2016
Name: MXIC-MX25L3233F
Sector Size: 4 KiB (4096 Byte)
Total Capacity: 4 MiB (4194304 Byte)
4Byte Address Mode: Unsupported
 
----- Summary of Storages -----
eMMC : O
SNOR : O
UFS : X
- O : Init success
- X : Init failed or not exist
 
----- Summary of DRAM Init -----
DRAM Init : Success (Result 0x0 )
DRAM Size : 4096MB
 
[FWDN_V8::PrintDeviceInfo:1185] --------------------------------------
[main:142] Complete FWDN
[FWDNLogger::PrintCurTime:111] 24/04/25-09:57:47
 
C:\images>fwdn.exe --storage emmc --low-format
[main:30] FWDN V8 v1.4.6 - 2021.12.13 13:42:37
[FWDN_V8::GetFWDNRomVersion:1526] fwdn.rom version : 21.9.29
[FWDN_V8::LowformatCommand:1352] Start low-format
[FWDN_V8::LowformatCommand:1353] low-format can take a long time
[FWDN_V8::LowformatCommand:1382] Complete low-format
[main:142] Complete FWDN
[FWDNLogger::PrintCurTime:111] 24/04/25-09:57:50
 
C:\images>fwdn.exe -w boot-firmware\boot.single.json
[main:30] FWDN V8 v1.4.6 - 2021.12.13 13:42:37
[FWDN_V8::GetFWDNRomVersion:1526] fwdn.rom version : 21.9.29
[main:117] Start write command
[FWDN_V8::GetFileAndWriteCommand:748] C:\images\boot-firmware\bconf.single.bin
[FWDN_V8::GetFileAndWriteCommand:748] C:\images\boot-firmware\bconf.single.bin
[FWDN_V8::GetFileAndWriteCommand:748] C:\images\boot-firmware\mcert.bin
[FWDN_V8::GetFileAndWriteCommand:748] C:\images\boot-firmware\mcert.bin
[FWDN_V8::GetFileAndWriteCommand:748] C:\images\boot-firmware\dram_params.bin
[FWDN_V8::GetFileAndWriteCommand:748] C:\images\boot-firmware\dram_params.bin
[FWDN_V8::GetFileAndWriteCommand:748] C:\images\boot-firmware\hsm.cs.bin
[FWDN_V8::GetFileAndWriteCommand:748] C:\images\boot-firmware\hsm.cs.bin
[FWDN_V8::GetFileAndWriteCommand:748] C:\images\boot-firmware\scfw.rom
[FWDN_V8::GetFileAndWriteCommand:748] C:\images\boot-firmware\scfw.rom
[FWDN_V8::GetFileAndWriteCommand:748] C:\images\boot-firmware\optee.rom
[FWDN_V8::GetFileAndWriteCommand:748] C:\images\boot-firmware\optee.rom
[FWDN_V8::GetFileAndWriteCommand:748] C:\images\boot-firmware\ca72_bl1.rom
[FWDN_V8::GetFileAndWriteCommand:748] C:\images\boot-firmware\ca72_bl1.rom
[FWDN_V8::GetFileAndWriteCommand:748] C:\images\boot-firmware\ca53_bl1.rom
[FWDN_V8::GetFileAndWriteCommand:748] C:\images\boot-firmware\ca53_bl1.rom
[FWDN_V8::GetFileAndWriteCommand:748] C:\images\boot-firmware\ca72_bl2.rom
[FWDN_V8::GetFileAndWriteCommand:748] C:\images\boot-firmware\ca72_bl2.rom
[FWDN_V8::GetFileAndWriteCommand:748] C:\images\boot-firmware\ca53_bl2.rom
[FWDN_V8::GetFileAndWriteCommand:748] C:\images\boot-firmware\ca53_bl2.rom
[main:125] Complete write command
[main:142] Complete FWDN
[FWDNLogger::PrintCurTime:111] 24/04/25-09:57:53
100% [||||||||||||||||||||||||||||||] 859264/859264
C:\images>fwdn.exe -w "output_d3g.fai" --storage emmc --area user
[main:30] FWDN V8 v1.4.6 - 2021.12.13 13:42:37
[FWDN_V8::GetFWDNRomVersion:1526] fwdn.rom version : 21.9.29
[main:117] Start write command
[FWDN_V8::GetFileAndWriteCommand:748] output_d3g.fai
[main:125] Complete write command
[main:142] Complete FWDN
[FWDNLogger::PrintCurTime:111] 24/04/25-10:05:21
100% [||||||||||||||||||||||||||||||] 7238688960/7238688960
** ローフォーマットなしでFAIファイルを書き込むと、データが書き込まれていないパーティションにガベージ値が含まれる場合があります。
```
 
<br/><br/><br/>
 
## 4.5 Linux環境でのFWDN
---
LinuxでD3-Gイメージをダウンロードするには、次のコマンドを実行します: "./fwdn.sh"。
 
```
$ ./fwdn.sh
```
 
D3-Gを起動する準備が整いました。デバイスとの通信を開始するには、第5章を参照してください。
 
 
<br/><br/><br/><br/>
 
# 5. D3-GボードとホストPCの接続
---
この章では、ファームウェアのダウンロードとシリアル通信のために、UARTを介してホストPCをD3-Gボードに接続する方法について説明します。
 
<br/><br/><br/>
 
## 5.1 UARTを使用したD3-Gボードの接続
---
次の手順に従い、UART接続を使用してファームウェアのダウンロードが正常に完了したことを確認します。
 
1. Windows環境にシリアルポートドライバー (CP210x Windows Driverなど) とPL2303_prolificドライバーをインストールします。
2. Tera TermやPuTTYなどのターミナルエミュレータをインストールします。
3. ホストPCとD3-GボードのUARTピンを接続します。USB-to-TTLケーブルを使用します。
4. 黒いケーブルをGNDピンに接続します。
5. 白いケーブル (RXD) をUARTピンのTXピンに接続し、緑色のケーブル (TXD) をUARTピンのRXピンに接続します。
6. ターミナルエミュレータアプリケーションを実行します。
7. PCでデバイスマネージャーを開き、UARTデバイスに割り当てられているポート番号を確認します。
8. ターミナルエミュレータで、確認したポート番号をシリアルラインフィールドに入力します。**Speed** (bps) を115200に設定し、**Flow control**を**None**に設定します。
9. 電源ケーブルを接続します。すると、D3-GボードがデフォルトのeMMCブートモードで起動します。
 
 
 
<p align="center">
    <img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20D3-G/Software/USB%20to%20TTL%20Connection.png", width="700">
</p>
<p align="center"><strong>図 5.1 ホストPCとのUART接続</strong></p><br/>
 
 
図 5.2は、ログインの成功を示しています。
ログイン用のユーザー名とパスワードはどちらも**root**に設定されています。
 
<p align="center">
    <img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20D3-G/Software/d3-g%20login%20as%20root.png", width="700">
</p>
<p align="center"><strong>図 5.2 接続画面 (IDとパスワードはtopst)</strong></p><br/>
 
<br/><br/><br/>
 
# 6. Ubuntu OSパーティションのサイズ変更
---
Ubuntu OSも提供しています。
この章に従うことで、Ubuntuイメージをダウンロードしてボードにアップロードし、割り当てられたeMMCストレージ容量を拡張できます。
 
<br/><br/><br/>
 
## 6.1 Ubuntuイメージのダウンロード
---
D3-Gの公式はUbuntu 22.04に基づいています。
イメージファイルはこちらからダウンロードできます。
 
<img src="https://github.com/topst-development/Documentation/assets/161264431/83d93c78-6437-4f96-a0bf-23f22da1aba1">  
 
**ダウンロード :**
-	[ダウンロードリンクはこちら](https://drive.google.com/file/d/1oc2qwaXUt6-QDME3s5WXKVHzAg4xqVyc/view?usp=drive_link)
<br>
-	詳細については、[githubページ](https://github.com/topst-development)をご覧ください。
 
**リリースノート :**
 
|Ver|   日付   |
|:-:|:--------:|
|1.0|2024.04.25|
 
TOPSTチームは、他の公式OSバージョンも準備しています。
他のOSのリリースに関する情報については、TOPSTコミュニティを参照してください。
 
<br/><br/><br/>
 
## 6.2 D3-Gへのファームウェアのアップロード
---
“fwdn_ubuntu.batch” ファイルを実行します。
UbuntuイメージをD3-Gにアップロードする方法については、第5章を参照してください。
FWDNが完了したら、FWDNポートからUSB Type-Cケーブルを取り外し、電源ケーブルを取り外します。
 
<br/><br/><br/>
 
## 6.3 eMMCストレージのサイズ変更 (D3-Gのみ)
---
ログインしてボードを起動した後、最初にeMMCストレージのサイズを変更することをお勧めします。
eMMCストレージのサイズ変更については、以下の手順に従ってください。
 
1. パーティションサイズとレイアウトを変更するには、次のコマンドを使用します。
     ```
     $ parted
     ```
 
2. GUIDパーティションテーブル (GPT) を拡張します。
    ```
    $ rescue
    $ Fix 
    $ 0 
    $ 100%
    ```
3. p (print) コマンドを使用して、パーティションタイプがext4であることを確認します。
   ```
   $ p
   ```
4. パーティション4のサイズを変更します。
    ```
    $ resizepart 4
    $ Yes
    $ 100%
    ```
5. ボードを再起動します。
6. パーティション4のext4ファイルシステムのサイズを変更します。
    ```
    $ resize2fs /dev/mmcblk0p4
    ```
7. 次のコマンドを使用して、変更されたパーティションサイズを確認します。
   ```
   $ df -h
   ```
 
サイズ変更後、使用可能なスペースが27GBであることを確認できます。
 
<br/><br/><br/><br/>
 
# 7. 参考文献
---
- 詳細については、TOPSTにお問い合わせください: topst@topst.ai
 
**注:** 参照ドキュメントは、契約条件に応じて、利用可能な場合にいつでも提供できます。参照ドキュメントが利用できない場合は、開発に直接関連するコンテンツを案内できます。
