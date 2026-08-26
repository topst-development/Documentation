# 1. はじめに
本書では、TOPST D3(オープンプラットフォームボード)のメインコア(CA72)で Ubuntu 環境を開発する方法について説明します。ボードで提供されるネイティブの Ubuntu イメージに加えて、本書ではユーザー独自の特化した Ubuntu 環境を開発する方法について説明します。ユーザーが作成した ubuntu ファイルシステムは、**_FWDN_** ツールを使用してメインコア(CA72)のファイルシステム領域にダウンロードできます。

本書は次の順序で説明します:
* Ubuntu ファイルシステム作成ガイド
* FWDN ガイド
* 起動した Ubuntu GUI 画面 
  
<br><br>

# 2. Ubuntu ファイルシステム作成ガイド

本章では、Host PC 上でメインコア(CA72)用の Ubuntu ファイルシステムをインストールする方法について説明します。

ユーザーの開発環境については、“Documentation/TOPST-D3/Software/SDK/LINUX” を参照してください。

<br><br>

## 2.1. Git で Ubuntu を取得する
Git で提供される Ubuntu のバージョンは、以下に示すとおり Ubuntu 22.04.2 LTS (Jammy Jellyfish) です。

```
$ git clone https://gitlab.com/topst.ai/topst-d3-ubuntu.git
```

<br><br>

# 3. スクリプトの実行


'populate_ubuntu.sh' を実行します。
```
$ sudo ./populate_ubuntu.sh 
[!] Prepare workspace
[!] Initial debian bootstraping
I: Retrieving InRelease 
I: Checking Release signature
I: Valid Release signature (key id F6ECB3762474EDA9D21B7022871920D1991BC93C)
I: Retrieving Packages 
I: Validating Packages 
I: Resolving dependencies of required packages...
I: Resolving dependencies of base packages...
I: Checking component main on http://ports.ubuntu.com/ubuntu-ports...
I: Retrieving adduser 3.118ubuntu5
I: Validating adduser 3.118ubuntu5
I: Retrieving apt 2.4.5
I: Validating apt 2.4.5
I: Retrieving apt-utils 2.4.5
I: Validating apt-utils 2.4.5
I: Retrieving base-files 12ubuntu4
I: Validating base-files 12ubuntu4
I: Retrieving base-passwd 3.5.52build1
I: Validating base-passwd 3.5.52build1
I: Retrieving bash 5.1-6ubuntu1
I: Validating bash 5.1-6ubuntu1
I: Retrieving bsdutils 1:2.37.2-4ubuntu3
I: Validating bsdutils 1:2.37.2-4ubuntu3
I: Retrieving ca-certificates 20211016
I: Validating ca-certificates 20211016
I: Retrieving console-setup 1.205ubuntu3
I: Validating console-setup 1.205ubuntu3
I: Retrieving console-setup-linux 1.205ubuntu3
I: Validating console-setup-linux 1.205ubuntu3
I: Retrieving coreutils 8.32-4.1ubuntu1
I: Validating coreutils 8.32-4.1ubuntu1
I: Retrieving cron 3.0pl1-137ubuntu3
I: Validating cron 3.0pl1-137ubuntu3
I: Retrieving dash 0.5.11+git20210903+057cd650a4ed-3build1
I: Validating dash 0.5.11+git20210903+057cd650a4ed-3build1
I: Retrieving dbus 1.12.20-2ubuntu4

                   ㆍ
                   ㆍ
                   ㆍ
```
以下で etx4 ファイルを確認できます。
```
$ ls
populate_ubuntu.sh  src  ubuntu.ext4
```


