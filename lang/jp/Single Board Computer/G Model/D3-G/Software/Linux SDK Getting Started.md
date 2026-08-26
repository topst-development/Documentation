# 1. はじめに
---
本書では、ホスト環境の設定、SDK のビルド、ファームウェアダウンローダーの使用、Ubuntu のダウンロードなど、D3-G SDK をビルドするためのガイドラインを説明します。  

本書には次の内容が含まれています。 
- ホスト環境の設定  
- イメージビルドガイド  
- ファームウェアダウンロードガイド 
- D3-G ボードと PC の接続

<br/><br/><br/><br/>

# 2. ホスト環境の設定
---
この章では、ホスト PC 環境を設定する方法について、Windows と Ubuntu に分けて説明します。
</br><br/><br/>

## 2.1 Windows 環境 
---
本書では、Windows PC で Linux を使用するために Windows Subsystem for Linux (WSL) を設定する方法を説明します。
D3-G Linux SDK は Yocto Project をベースとしているため、D3-G SDK の Linux バージョンは Yocto Project に準拠します。
別のバージョンの Linux をインストールすることもできますが、本書では Ubuntu 22.04 をベースとした D3-G Linux SDK について説明します。
ホスト OS が Ubuntu の場合は、第 2.2 章に進んでください。

</br><br/>

### 2.1.1 WSL2 Ubuntu のインストール
1. "**管理者権限で実行**" で Windows PowerShell を実行します。
2. WSL2 システムを有効にします。
    ```
    dism.exe /online /enable-feature /featurename:Microsoft-Windows-Subsystem-Linux /all /norestart
    ```
3. 仮想マシン機能を有効にします。
    ```
    dism.exe /online /enable-feature /featurename:VirtualMachinePlatform /all /norestart
    ```
4. WSL 2 をデフォルトバージョンに設定します。
    ```
    wsl --set-default-version 2
    ```
5. Microsoft Store で Ubuntu 22.04.3 LTS を検索してダウンロードします。

    * Linux カーネル更新パッケージをダウンロードする必要がある場合は、[こちら](https://learn.microsoft.com/ko-kr/windows/wsl/install-manual)から最新のパッケージをダウンロードしてください。

6. Ubuntu のインストール中に任意のユーザー名を指定します。
</br><br/>

### 2.1.2 WSL2 による Ubuntu へのアクセス
Windows のコマンドプロンプトを開き、次のコマンドを入力して Ubuntu にアクセスします。
Ubuntu にアクセスすると、デフォルトで /mnt/c/Users/[username] ディレクトリから開始します。
```
wsl  // access ubuntu 
ls   // check contents in your directory
```
結果を確認するには図 2.1 を参照してください (結果はシステムによって異なる場合があります)。
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20D3-G/Software/1.1%20wsl%20linux.png" width="500"></p>
<p align="center"><strong>図 2.1 WSL2 スクリーンショット </strong></p>

<br/><br/>

### 2.1.3 ロケールの設定

WSL で Ubuntu を実行した後は、言語および地域の設定が正しく適用されるようにロケールを設定する必要があります。en_US.UTF-8 の使用を推奨します。en_US.UTF-8 を使用するには、次のコマンドを実行してください。 

```
sudo locale-gen en_US.UTF-8 && sudo update-locale LANG=en_US.UTF-8 
```

ロケールを設定した後は、次のコマンドを使用してロケールの種類を確認できます。 

```
echo 'LANG=en_US.UTF-8' | sudo tee -a /etc/default/locale && \  

echo 'LC_ALL=en_US.UTF-8' | sudo tee -a /etc/default/locale 
```
<br/><br/>

### 2.1.4 SSH と Samba のインストール

Ubuntu にアクセスした後は、SSH や Samba などの追加ユーティリティを使用して、より便利な開発環境を構築できます。SSH と Samba を使用すると、リモートコンピュータでコマンドを実行したり、他のコンピュータにファイルをコピーしたりできます。
 - 以下の手順では、ホスト PC がネットワークに接続されている必要があります。次のコマンドを使用してネットワークの状態を確認してください。
  ```
  $ sudo apt-get update
  $ sudo apt-get install -y net-tools
  $ ifconfig 
  ```

SSH と Samba が既にインストールされている場合、または使用しない場合は、この章をスキップできます。

次のコマンドを使用して net-tools、SSH、Samba をインストールします。

```
$ sudo apt-get update 
$ sudo apt install -y net-tools openssh-server samba
```
SSH と Samba をインストールした後、ご使用の環境に合わせて各プログラムを設定してください。
</br><br/>

### 2.1.5 ユーティリティのインストール

次のコマンドを使用して、必要なユーティリティを一度にすべてインストールします。Yocto Project を使用するには、ホスト PC (個人のコンピュータまたは開発サーバー) に以下のユーティリティがインストールされている必要があります。


```
$ sudo apt-get install -y gawk wget git diffstat unzip texinfo gcc-multilib build-essential chrpath

$ sudo apt-get install -y socat cpio python3 python3-pip python3-pexpect xz-utils debianutils

$ sudo apt-get install -y iputils-ping python3-git python3-jinja2 libegl1-mesa-dev libsdl1.2-dev pylint

$ sudo apt-get install -y xterm zstd ncftp curl git-lfs vim zip lz4
```

<br/><br/>

### 2.1.6 Repo のインストール

Repo が既にインストールされている場合は、再インストールせずにそのまま使用できます。  
Repo をインストールする前に、Python 3.6 以上のバージョンがインストールされていることを確認してください。

次のコマンドを使用して Repo をインストールします。
```
$ sudo apt-get install repo
```

'/usr/bin/env 'python' no such file or directory' というエラーメッセージが表示された場合は、次のコマンドを使用して 'python' を 'python3' にリンクしてください。

```
$ sudo ln -sf /usr/bin/python3 /usr/bin/python
```
Repo のエラーが発生した場合は、次のコマンドを使用して最新バージョンをダウンロードし、/usr/bin/ フォルダに配置してください。

```
$ mkdir -p ~/bin

$ curl http://commondatastorage.googleapis.com/git-repo-downloads/repo > ~/bin/repo

$ chmod a+x ~/bin/repo

$ sudo mv ~/bin/repo /usr/bin/repo
```
**第 3 章: イメージビルドガイド** に進んでください。

<br/><br/><br/>

## 2.2 Linux 環境
---
この章では、ホスト OS として Ubuntu を使用する場合の設定手順を説明します。
</br><br/>

### 2.2.1 環境の設定
以下の章 (2.2.2 から 2.2.5) は Ubuntu のターミナルで実行する必要があります。ターミナルを開くには、ショートカット [Ctrl + Alt + T] を使用してください。
<br/><br/>

### 2.2.2 ロケールの設定

WSL で Ubuntu を実行した後は、言語および地域の設定が正しく適用されるようにロケールを設定する必要があります。en_US.UTF-8 の使用を推奨します。en_US.UTF-8 を使用するには、次のコマンドを実行してください。 

```
sudo locale-gen en_US.UTF-8 && sudo update-locale LANG=en_US.UTF-8 
```

ロケールを設定した後は、次のコマンドを使用してロケールの種類を確認できます。 

```
echo 'LANG=en_US.UTF-8' | sudo tee -a /etc/default/locale && \  

echo 'LC_ALL=en_US.UTF-8' | sudo tee -a /etc/default/locale 
```
<br/><br/>

### 2.2.3 SSH と Samba のインストール

Ubuntu にアクセスした後は、SSH や Samba などの追加ユーティリティを使用して、より便利な開発環境を構築できます。SSH と Samba を使用すると、リモートコンピュータでコマンドを実行したり、他のコンピュータにファイルをコピーしたりできます。
 - 以下の手順では、ホスト PC がネットワークに接続されている必要があります。次のコマンドを使用してネットワークの状態を確認してください
  ```
  $ sudo apt-get update
  $ sudo apt-get install -y net-tools
  $ ifconfig 
  ```

SSH と Samba が既にインストールされている場合、または使用しない場合は、この章をスキップできます。

次のコマンドを使用して SSH、Samba をインストールします。

```
$ sudo apt-get update 
$ sudo apt install -y openssh-server samba
```
SSH と Samba をインストールした後、ご使用の環境に合わせて各プログラムを設定してください。

<br/><br/>

### 2.2.4 ユーティリティのインストール

次のコマンドを使用して、必要なユーティリティを一度にすべてインストールします。Yocto Project を使用するには、以下のユーティリティをホスト PC (個人のコンピュータまたは開発サーバー) に**必ず**インストールする必要があります。
****


```
$ sudo apt-get install -y gawk wget git diffstat unzip texinfo gcc-multilib build-essential chrpath

$ sudo apt-get install -y socat cpio python3 python3-pip python3-pexpect xz-utils debianutils

$ sudo apt-get install -y iputils-ping python3-git python3-jinja2 libegl1-mesa-dev libsdl1.2-dev pylint

$ sudo apt-get install -y xterm zstd ncftp curl git-lfs vim zip lz4
```

<br/><br/>

### 2.2.5 Repo のインストール

Android Repo を通じて D3-G SDK をダウンロードできます。  
Repo をインストールするには、次の Web サイトを参照してください: https://source.android.com/source/downloading.html.  
Repo が既にインストールされている場合は、再インストールせずにそのまま使用できます。  
Repo をインストールする前に、Python 3.6 以上のバージョンがインストールされていることを確認してください。

次のコマンドを使用して Repo をインストールします。
```
$ sudo apt-get install repo
```

'/usr/bin/env 'python' no such file or directory' というエラーメッセージが表示された場合は、次のコマンドを使用して 'python' を 'python3' にリンクしてください。

```
$ sudo ln -sf /usr/bin/python3 /usr/bin/python
```
Repo のエラーが発生した場合は、次のコマンドを使用して最新バージョンをダウンロードし、/usr/bin/ フォルダに配置してください。

```
$ mkdir -p ~/bin

$ curl http://commondatastorage.googleapis.com/git-repo-downloads/repo > ~/bin/repo

$ chmod a+x ~/bin/repo

$ sudo mv ~/bin/repo /usr/bin/repo
```

<br/><br/>

### 2.2.6 Telechips USB デバイス用の Udev Rules
次のコマンドを実行すると、Linux で FWDN をダウンロードする際に 'sudo' コマンドを使用する必要がなくなります。
```
$ echo "SUBSYSTEM==\"usb\", ATTR{idVendor}==\"140e\", MODE=\"0666\", OWNER=\"${USER}\"" | sudo tee /etc/udev/rules.d/99-topst.rules
$ sudo udevadm control --reload-rules && sudo udevadm trigger
```
**第 3 章: イメージビルドガイド** に進んでください。

<br/><br/><br/><br/>

# 3. イメージビルドガイド
---
この章では、ホスト PC にインストールされた Ubuntu OS（WSL かローカルの Ubuntu インストールかを問わず）に基づいて説明します。D3-G にアップロードするイメージは Yocto Project を使用してビルドされるため、ビルド作業は Ubuntu 環境で実行する必要があります。
</br></br>

## 3.1 SDK ビルドの準備
---
D3-G Linux SDK は Yocto Project 4.0 Kirkstone をベースとしています。したがって、D3-G Linux SDK を使用するには、ホスト PC に Yocto Project 環境を構成する必要があります。SDK、source-mirror、およびツールをダウンロードするには、必要なユーティリティをインストールする必要があります。イメージを問題なくビルドするには、PC に **60 GB 以上の空きストレージ**と **16 GB 以上の RAM** が必要です。

</br><br/>  

## 3.2 Yocto Project  
---
Yocto Project は、組み込み Linux 開発に重点を置いたオープンソースプロジェクトです。  
Linux イメージを作成するために、Open Embedded プロジェクトである Poky と ***bitbake*** をビルドシステムとして組み合わせて使用します。  
Yocto Project を使用すると、ブートローダー、カーネル、rootfs を同時にビルドできます。  

<br/><br/>

## 3.3 Yocto Project の作業プロセス
---
図 3.1 は Yocto Project のタスクプロセスを示しています。メタデータに基づいてアップストリームからソースをダウンロードし、ビルドできます。ビルドが完了すると、パッケージ、イメージ、SDK が結果として提供されます。

<p align="center">
    <img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20D3-G/Software/2.1%20yocto%20project%20task%20process.png", width="700">
</p>
<p align="center"><strong>図 3.1 Yocto Project の作業プロセス</strong></p>

<br/><br/>

## 3.4 D3-G SDK の構成
---
以下は、当社が構成した Yocto Project の構成要素です。
表 3.1 は D3-G SDK の構成を示しています。



**表 3.1 D3-G SDK の構成**
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
      <td>SDK を自動的にダウンロードしてビルドする Python スクリプト</td>
    </tr>
    <tr>
      <td colspan="3"style="text-align: center; vertical-align: middle;">stitch-fai-ai.sh</td>
      <td>AI-G の fai イメージを作成するスクリプト (minimal + サンプルアプリケーション)</td>
    </tr>
    <tr>
      <td colspan="3"style="text-align: center; vertical-align: middle;">stitch-fai-d3.sh</td>
      <td>D3-G の fai イメージを作成するスクリプト (minimal + サンプルアプリケーション)</td>
    </tr>
    <tr>
      <td colspan="3"style="text-align: center; vertical-align: middle;">mktcimg</td>
      <td rowspan="2">ビルドプロセスおよび <strong>FWDN</strong> に関連するツール</td>
    </tr>
    <tr>
      <td colspan="3"style="text-align: center; vertical-align: middle;">tools</td>
    </tr>
    <tr>
      <td rowspan="8"style="text-align: center; vertical-align: middle;">poky</td>
      <td colspan="2"style="text-align: center; vertical-align: middle;">poky</td>
      <td>Yocto Project 4.0 Kirkstone ビルドシステム</td>
    </tr>
    <tr>
      <td colspan="2"style="text-align: center; vertical-align: middle;">meta-openembedded</td>
      <td>OE-Core をサポートするレイヤ</td>
    </tr>
    <tr>
      <td colspan="2"style="text-align: center; vertical-align: middle;">meta-arm</td>
      <td>ARM ツールチェーンをサポートするレイヤー</td>
    </tr>
    <tr>
      <td colspan="2"style="text-align: center; vertical-align: middle;">meta-topst-bsp</td>
      <td>TOPST BSP をサポートするレイヤ</td>
    </tr>
    <tr>
      <td colspan="2"style="text-align: center; vertical-align: middle;">meta-gplv2</td>
      <td>GPLv3 ライセンスを回避するパッケージを含むレイヤー</td>
    </tr>
    <tr>
      <td colspan="2"style="text-align: center; vertical-align: middle;">meta-topst</td>
      <td>TOPST レシピ</td>
    </tr>
  </tbody>
</table>
<br/><br/><br/>


## 3.5 ビルドの準備
---
以降の章では、D3-G イメージをビルドするために Yocto Project を構成する方法を説明します。

<br/><br/>

### 3.5.1 .gitconfig にユーザーのメールアドレスとユーザー名を設定する
公式 TOPST git から D3-G SDK をダウンロードするには、メールアドレスと名前を設定してください。
1. 次のコマンドを入力します。
```
vi ~/.gitconfig
```
2. 次の情報を入力してください
```
[user]
    email = User email
    name = User name
```

<br/><br/>

### 3.5.2 Git から D3-G を取得する

1. **topst-sdk** という名前の新しいディレクトリを作成し、カレントディレクトリを **topst-sdk** に変更します。

```
$ mkdir topst-sdk
$ cd topst-sdk
```

2. 次のコマンドを実行してリポジトリを初期化します。

```
$ repo init -u https://github.com/topst-development/manifests.git -b release/1.3.0 -m linux_yp4.0_topst.xml
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

3. 次のコマンドを実行してリポジトリを同期します。

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

## 3.6 topst-build.sh の実行 
---
./easy-setup.sh スクリプトを実行すると、次の画面が表示されます。 

**注意: ./easy-setup.sh を再実行する場合、yes を選択するとビルド済みのソースが削除されるため注意してください。**
```
./easy-setup.sh
```
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20AI-G/Software/Linux%20SDK/license1.png"></p>
<p align="center"><strong>図 3.2 エンドユーザーライセンス契約</strong></p>

画面の一番下までスクロールして、この注意事項をお読みください。お読みになった後、右矢印キーを押して [Enter] を押してください。
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20AI-G/Software/Linux%20SDK/license2.png"></p>
<p align="center"><strong>図 3.3 'Proceed to confirm' へ移動</strong></p>


すると、次の画面が表示されます。 
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20AI-G/Software/Linux%20SDK/license3.png" ></p>
<p align="center"><strong>図 3.4 同意画面 </strong></p>


ビルドイメージは次のパスに作成されます:

- {TOPST_PATH}/build/d3-g-topst-main/tmp/deploy/images/d3-g-topst-main

topst-build.sh は、D3-G および AI-G 用のイメージをビルドするために必要なコア環境を設定するシェルスクリプトです。次のコマンドを実行し、D3-G にメイン OS をインストールするためのビルド環境を準備するには、オプション 2 を選択してください。



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

メイン OS のビルドを開始するには、次のコマンドを実行してください。
```
$ bitbake telechips-topst-image
```

<br/><br/><br/>

## 3.7 Firmware Downloader (FWDN) イメージの作成 
---
このオプションは、D3-G プラットフォームイメージ用にバイナリを 1 つのイメージに結合します。

**'output_d3g.fai' ビルドイメージ**と **FWDN ツール**を含む **output_d3g.fwdn.zip** ファイルが、次のパスに作成されます:

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

```

次のログが表示された場合、"output_d3g.fwdn.zip" ファイルが作成されたことを意味します。 
```
$ ls
build  easy-setup.sh  mktcimg  output_d3g.fwdn.zip  poky  stitch-fai-ai.sh  stitch-fai-d3.sh  tools
```

</br></br><br/><br/>

# 4. ファームウェアのダウンロード
---
この章では、***FWDN*** を使用して D3-G にファームウェアをダウンロードし、Linux コンソールにログインする方法を説明します。  
***FWDN V8*** は、Windows 10(11) 64 ビットおよび Linux 環境の両方でファームウェアをダウンロードするための PC ツールです。この章では、Windows および Linux 環境でダウンロードする場合について説明します。

<br/><br/><br/>

## 4.1 ファームウェアダウンロードの手順
---
***FWDN*** のダウンロード手順は次のとおりです:

1. 起動モードスイッチを USB 起動モードに設定してください。
2. Windows のプロンプトまたは Linux のコンソールを開いてください。
3. ***FWDN V8*** をボードに接続してください。
4. fai ファイルをダウンロードしてください。

<br/><br/><br/>

## 4.2 USB 起動モードで D3-G ボードとホスト PC を接続する
---
Firmware Downloader (FWDN) は、ホスト PC との USB 通信を通じて D3-G に ROM イメージを書き込みます。 

D3-G には Boot Mode ボタンが 1 つあり、2 種類の起動モードをサポートしています。本ガイドでは FWDN モードを中心に説明します。

- USB Boot Mode (FWDN Mode) : ホスト PC の FWDN ツールを使用して ROM イメージを書き込む際に使用します 

- eMMC Boot Mode : eMMC デバイスに保存された ROM イメージを使用して D3-G を起動する際に使用します 

**注**: USB Type-C FWDN ポートは firmware downloader (FWDN) に使用されます。 



FWDN を使用するには、次のように D3-G ボードをホスト PC に接続してください: 

1. ホスト PC に VTC ドライバがインストールされていることを確認します。VTC ドライバがインストールされていない場合は、第 4.2.1 章のようにインストールしてください。  

2. USB Type-C ケーブルを 1 本準備してください。 

3. USB 起動モードに入るには、FWDN スイッチを押しながら D3-G ボードに電源ケーブルを接続してください。
   - 詳細については、サイドバーの Hardware セクションにある **"2. Boot Mode"** を参照してください。

4. USB Type-C ケーブルを D3-G ボードの USB Type-C FWDN ポートとホスト PC に接続してください。 

<p align="center">
    <img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20D3-G/Hardware/connect%20to%20d3g%20to%20host%20pc%20using%20c%20type.png">
</p>
<p align="center"><strong>図 4.1 USB C-Type ケーブルを使用した D3-G ボードとホスト PC の接続 </strong></p>

<br/><br/>

### 4.2.1 VTC ドライバのインストール方法 (Windows/Ubuntu)
ホスト PC で管理者として実行し、Vendor Telechips Certification (VTC) ドライバ（[telechips driver](https://drive.google.com/file/d/1muQnY8kuKxDsy3p3FUiQqcG34Zjk-mnR/view?usp=sharing) にあります）をインストールしてください。上記のように FWDN モードで USB を接続すると、図 4.2 および図 4.3 のように Telechips VTC USB ドライバが設定されます。

<p align="center">
    <img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20D3-G/Software/USB%20Connection%20in%20Windows%20Environment.png", width="700">
</p>
<p align="center"><strong>図 4.2 Windows 環境での USB 接続</strong></p>

<p align="center">
    <img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20D3-G/Software/USB%20Connection%20in%20Linux%20System.png", width="700">
</p>
<p align="center"><strong>図 4.3 Linux 環境での USB 接続</strong></p>  

**注**: VTC ドライバ V5.0.0.14 以上を使用してください。バージョンを確認するには、Windows 環境でデバイスマネージャーを確認してください。  

<br/><br/><br/>

## 4.3 FWDN ダウンロードの準備
---
FWDN を実行する前に、Ubuntu (WSL2) 環境で作成したイメージとツールを Windows 環境に転送してください。


1. "output_d3g.fwdn.zip" を解凍してください。   
    ```
    $ cd ~/topst-sdk
    $ mkdir images
    $ mv ./output_d3g.fwdn.zip ./images
    $ cd images
    $ unzip output_d3g.fwdn.zip
    ```
2. "images" フォルダを Windows の C ドライブにコピーしてください。  
    ```
    $ cd ..
    $ cp -r ./images /mnt/c/
    ```

<br/><br/><br/>

## 4.4 Windows 環境での FWDN
---
1. Powershell を実行し、"C:\images\" に移動してください。
```
$ cd C:\images 
```

2. ファームウェアのダウンロードを開始するには、**.\fwdn.bat** コマンドを入力してください。「fwdn.bat」は、FWDN V8 を使用してファームウェアを自動的にダウンロードする実行ファイルです。 

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
** When writing FAI files without low-format, there may be garbage values in partition where data is not written.
```

<br/><br/><br/>

## 4.5  Linux 環境での FWDN
---
Linux で D3-G イメージをダウンロードするには、次のコマンドを実行してください: "./fwdn.sh"。

```
$ ./fwdn.sh
```

これで D3-G を起動する準備が整いました。デバイスとの通信を開始するには、第 5 章を参照してください。


<br/><br/><br/><br/>

# 5. D3-G ボードとホスト PC の接続
---
この章では、ファームウェアのダウンロードとシリアル通信のために、UART を通じてホスト PC を D3-G ボードに接続する方法を説明します。

<br/><br/><br/>

## 5.1 UART による D3-G ボードの接続 
---
次の手順に従い、UART 接続を使用してファームウェアのダウンロードが正常に完了したことを確認してください。 

1. Windows 環境でシリアルポートドライバ（例: CP210x Windows Driver）と PL2303_prolific ドライバをインストールしてください。 
2. Tera Term や PuTTY などのターミナルエミュレータをインストールします。 
3. ホスト PC と D3-G ボードの UART ピンを接続してください。USB-to-TTL ケーブルを使用してください。 
4. 黒色のケーブルを GND ピンに接続してください。 
5. 白色のケーブル(RXD)を UART ピンの TX ピンに、緑色のケーブル(TXD)を UART ピンの RX ピンに接続します。
6. ターミナルエミュレータアプリケーションを実行します。
7. PC でデバイスマネージャーを開き、UART デバイスに割り当てられたポート番号を確認してください。
8. ターミナルエミュレータで、確認したポート番号を Serial line フィールドに入力してください。**Speed** (bps) を 115200 に、**Flow control** を **None** に設定してください。
9. 電源ケーブルを接続してください。すると、D3-G ボードはデフォルトの eMMC 起動モードで起動します。


 
<p align="center">
    <img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20D3-G/Software/USB%20to%20TTL%20Connection.png", width="700">
</p>
<p align="center"><strong>図 5.1 ホスト PC との UART 接続</strong></p><br/>  


図 5.2 はログインが成功した状態を示しています。  
ログイン用のユーザー名とパスワードは、どちらも **root** に設定されています。

<p align="center">
    <img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20D3-G/Software/d3-g%20login%20as%20root.png", width="700">
</p>
<p align="center"><strong>図 5.2 接続された画面 (ID とパスワードは topst です)</strong></p><br/>

<br/><br/><br/>

# 6. Ubuntu OS パーティションのサイズ変更
---
当社は Ubuntu OS も提供しています。
この章に従うことで、Ubuntu イメージをダウンロードしてボードにアップロードし、割り当てられた eMMC のストレージ容量を拡張できます。

<br/><br/><br/>

## 6.1 Ubuntu イメージのダウンロード
---
D3-G の公式 OS は Ubuntu 22.04 をベースとしています。  
イメージファイルはこちらからダウンロードできます。  

<img src="https://github.com/topst-development/Documentation/assets/161264431/83d93c78-6437-4f96-a0bf-23f22da1aba1">  

**ダウンロード :**  
-	[こちらからダウンロード](https://drive.google.com/file/d/1oc2qwaXUt6-QDME3s5WXKVHzAg4xqVyc/view?usp=drive_link)
<br>
-	詳細については、当社の [github ページ](https://github.com/topst-development) をご覧ください。

**リリースノート :**  

|Ver|   日付   |
|:-:|:--------:|
|1.0|2024.04.25|  

TOPST チームは、他の公式 OS バージョンも準備しています。  
他の OS のリリースに関する情報は、TOPST コミュニティを参照してください。  

<br/><br/><br/>

## 6.2 D3-G へのファームウェアのアップロード
---
「fwdn_ubuntu.batch」ファイルを実行してください。 
Ubuntu イメージを D3-G にアップロードする方法については、第 5 章を参照してください。
FWDN が完了したら、FWDN ポートから USB Type-C ケーブルを取り外し、電源ケーブルを取り外してください。 

<br/><br/><br/>

## 6.3 eMMC ストレージのサイズ変更 (D3-G のみ)
---
ボードにログインして起動した後は、まず eMMC ストレージのサイズを変更することをお勧めします。
eMMC ストレージのサイズ変更については、以下の手順に従ってください。

1. パーティションのサイズとレイアウトを変更するには、次のコマンドを使用してください。
     ```
     $ parted
     ```

2. GUID Partition Table(GPT) を拡張してください。 
    ```
    $ rescue
    $ Fix 
    $ 0 
    $ 100%
    ```
3. p (print) コマンドを使用して、パーティションタイプが ext4 であることを確認してください。 
   ```
   $ p
   ```
4. パーティション 4 のサイズを変更してください。
    ```
    $ resizepart 4
    $ Yes
    $ 100%
    ```
5. ボードを再起動してください。
6. パーティション 4 の ext4 ファイルシステムのサイズを変更してください。
    ```
    $ resize2fs /dev/mmcblk0p4
    ```
7. 次のコマンドを使用して、変更後のパーティションサイズを確認してください。
   ```
   $ df -h
   ```

サイズ変更後、利用可能な容量が 27GB になっていることを確認できます。

<br/><br/><br/><br/>

# 7. 参考資料
---
- 詳細については TOPST にお問い合わせください: topst@topst.ai

**注意:** 参考文書は、契約条件に応じて提供可能な場合に提供されます。参考
文書が入手できない場合は、お客様の開発に直接関連する内容をご案内できます。
