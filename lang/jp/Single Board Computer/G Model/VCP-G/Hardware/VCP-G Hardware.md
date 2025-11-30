# 1. はじめに
---
このドキュメントは、TCC7045アプリケーションプロセッサに基づいたVCP-Gのハードウェアユーザーガイドです。このドキュメントでは、システムのインストール、デバッグ、およびVCP-Gの全体的な設計と使用法に関する詳細情報について説明します。


表 1.1は、VCP-Gの機能を示しています。

<p align="center"><strong>表 1.1 VCP-Gの機能</strong></p>
<div align="center">
	<table>
	  <tr>
	    <td colspan="3">部品名</td>
	    <td>TCC7045</td>
	  </tr>
	  <tr>
	    <td colspan="3">パッケージ</td>
	    <td>パッケージ ピンツーピン互換 FBGA 196ピン (12BD)</td>
	  </tr>
	    <tr>
	    <td colspan="3">CPU周波数</td>
	    <td>200 MHz (最大300 MHz)</td>
	  </tr>
	  <tr>
	    <td rowspan="4">オンチップメモリ</td>
	    <td colspan="2">プログラムフラッシュ</td>
	    <td colspan="3">4 MB</td>
	  </tr>
	  <tr>
	    <td colspan="2">SRAM</td>
	    <td colspan="3">512 KB (リテンションRAM 16 KBを含む)</td>
	  </tr>
	  <tr>
	    <td colspan="2">データフラッシュ</td>
	    <td colspan="3">256 KB</td>
	  </tr>
	  <tr>
	    <td colspan="2">DMAチャンネル</td>
	    <td colspan="3">16チャンネル</td>
	  </tr>
	  <tr>
	    <td rowspan="13">周辺機器</td>
	    <td colspan="2">イーサネット</td>
	    <td>AVB付き1 Gbps</td>
	  </tr>
	  <tr>
		<td colspan="2">CAN / CANFD</td>
	    <td>3チャンネル</td>
	  </tr>
	  <tr>
	    <td colspan="2">専用LIN / UART</td>
	    <td>3チャンネル (最大6チャンネル)</td>
	  </tr>
	  <tr>
	    <td colspan="2">専用I2C</td>
	    <td>3チャンネル (最大6チャンネル)</td>
	  </tr>
	  <tr>
	  <tr>
	    <td colspan="2">専用GPSB (SPI)</td>
	    <td>2チャンネル (最大5チャンネル)</td>
	  </tr>
	    <tr>
	    <td colspan="2">MFIO (割り当てられたUART、I2C、GPSB)</td>
	    <td>3チャンネル</td>
	  </tr>
	  <tr>
	    <td rowspan="4">ADC</td> 
	    <td>解像度</td>
	    <td>12ビットSARタイプ</td>
	  </tr>
	  <tr>
	    <td>チャンネル</td>
	    <td>12チャンネル x 2グループ</td>
	  </tr>
	  <tr>
	    <td>入力範囲</td>
	    <td>3.3V</td>
	  </tr>
	  <tr>
	    <td>サンプルレート</td>
	    <td>1.0 MSPs以上</td>
	  </tr>
	  <tr>
	    <td colspan="2">I2S</td>
	    <td>1チャンネル</td>
	  </tr>
	  <tr>
	    <td colspan="2">シリアルフラッシュインターフェース</td>
	    <td>Quad SPI</td>
	  </tr>  
	  <tr>
	    <td colspan="3">電源システム</td>
	    <td>3.3Vシングル</td>
	  </tr>
	  <tr>
	    <td colspan="3">温度</td>
	    <td>-40 ℃ 〜 105 ℃</td>
	  </tr>
	</table>
</div>

</br></br></br>

## 1.1 用語
---
<p align="center"><strong>表 1.2 用語 </strong></p>
<div align="center">
	<table>
	  <tr>
	    <td clospan="2"><strong>用語</strong></td>
	    <td><strong>定義</strong></td>
	  </tr>
	  <tr>
	    <td clospan="2">ADC</td>
	    <td>Analog to Digital Converter</td>
	  </tr>
	  <tr>
	    <td clospan="2">FWDN</td>
	    <td>Firmware Download</td>
	  </tr>
	  <tr>
	    <td clospan="2">GPIO</td>
	    <td>General Purpose Input Output</td>
	  </tr>
	  <tr>
	    <td clospan="2">MCU</td>
	    <td>Micro-controller Unit</td>
	  </tr>
	  <tr>
	    <td clospan="2">TOPST</td>
	    <td>Total Open-Platform for System development and Training</td>
	  </tr>
	  <tr>
	    <td clospan="2">VCP</td>
	    <td>Vehicle Control Processer</td>
	  </tr>
	</table>
</div>

</br></br></br></br>

# 2. ブロック図
---
## 2.1 システムブロック図
---
図 2.1は、VCP-Gのシステムブロック図を示しています。
<p align="center"><img src= "https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Hardware/2.1%20VCP-G%20System%20Block%20Diagram.png"></p>
<p align="center"><strong>図 2.1 システムブロック図</strong></p>

</br></br></br></br>

# 3. VCP-Gの概要
---
VCP-Gは、次の目的で使用できます。
  - システム開発
  - トレーニング

表 3.1は、VCP-Gのデフォルト構成を示しています。

<p align="center"><strong>表 3.1 VCP-Gのデフォルト構成 </strong></p>
<div align="center">
	<table>
	  <tr>
	    <td colspan="2"><strong>ボード名</strong></td>
	    <td><strong>説明</strong></p>
	  </tr>
	  <tr>
	    <td colspan="2">TOPST_VCP_V2.1.1</td>
	    <td>TOPST用MCUボード</td>
	  </tr>
	</table>
</div>

</br></br></br>

## 3.1 VCP-G
---
図 3.1は、VCP-Gの上面図を示しています。
<p align="center"><img src= "https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Hardware/3.1%20TOPST%20VCP-G%20Board%20(Top%20View)%20.png"></p>
<p align="center"><strong>図 3.1 VCP-G (上面図)</strong></p>

表 3.2は、VCP-G (上面図) のコネクタについて説明しています。
<p align="center"><strong>表 3.2 VCP-G (上面図) のコネクタ</strong></p>
<div align="center">
	<table>
	  <tr>
	    <td colspan="4"><strong>番号</strong></td>
	    <td><strong>参照番号</strong></td>
	    <td><strong>名前</strong></td>
	    <td><strong>説明</strong></td>
	  </tr>
	  <tr>
	    <td colspan="4">1</td>
	    <td>J18D100</td>
	    <td>36ピンメスヘッダー</td>
	    <td>GPIOおよびADC用ヘッダー</td>
	  </tr>
	  <tr>
	    <td colspan="4">2</td>
	    <td>J5D100</td>
	    <td>10ピンオスヘッダー</td>
	    <td>CAN用ヘッダー</td>
	  </tr>
	  <tr>
	    <td colspan="4">3</td>
	    <td>J3D100</td>
	    <td>6ピンオスヘッダー</td>
	    <td>SPI用ヘッダー</td>
	  </tr>
	  <tr>
	    <td colspan="4">4</td>
	    <td>J8D104</td>
	    <td>8ピンメスヘッダー</td>
	    <td>GPIOおよびADC用ヘッダー</td>
	  </tr>
	  <tr>
	    <td colspan="4">5</td>
	    <td>J8D102</td>
	    <td>8ピンメスヘッダー</td>
	    <td>GPIO用ヘッダー</td>
	  </tr>
	  <tr>
	    <td colspan="4">6</td>
	    <td>J10D100</td>
	    <td>10ピンメスヘッダー</td>
	    <td>GPIOおよびADC用ヘッダー</td>
	  </tr>
	  <tr>
	    <td colspan="4">7</td>
	    <td>J100</td>
	    <td>10ピンオスヘッダー</td>
	    <td>JTAG用ヘッダー</td>
	  </tr>
	  <tr>
	    <td colspan="4">8</td>
	    <td>SW100</td>
	    <td>RESETタクトスイッチ</td>
	    <td>GRESETn: VCP-Gのシステムと電源管理を初期化します</td>
	  </tr>
	  <tr>
	    <td colspan="4">9</td>
	    <td>JC100</td>
	    <td>USB Type-Cコネクタ</td>
	    <td>デバッグ用UARTまたはFWDNポート</td>
	  </tr>
	  <tr>
	    <td colspan="4">10</td>
	    <td>SW101</td>
	    <td>タクトスイッチ</td>
	    <td>FWDN: VCP-Gのファームウェアダウンロードモードに入ります</td>
	  </tr>  
	  <tr>
	    <td colspan="4">11</td>
		<td>J101</td>
	    <td>DCジャック</td>
	    <td>DC電源入力ジャック</td>
	  </tr>  
	  <tr>
	    <td colspan="4">12</td>
	    <td>J8D100</td>
	    <td>8ピンメスヘッダー</td>
	    <td>電源およびリセット用ヘッダー</td>
	  </tr>  
	  <tr>
	    <td colspan="4">13</td>
	    <td>J8D101</td>
	    <td>8ピンメスヘッダー</td>
	    <td>GPIOおよびADC用ヘッダー</td>
	  </tr>  
	  <tr>
	    <td colspan="4">14</td>
	    <td>J8D103</td>
	    <td>8ピンメスヘッダー</td>
	    <td>GPIOおよびADC用ヘッダー</td>
	  </tr>    
	</table>
</div>

図 3.2は、VCP-Gの底面図を示しています。

**注:** 図 3.2は現在、TOPST_VCP-G_V1.1.1ボードを示しています。この画像はTOPST_VCP-G_V2.1.1ボードに更新されます。
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Hardware/3.2%20TOPST%20VCP-G%20Board%20(Bottom%20View).png"></p>
<p align="center"><strong>図 3.2 VCP-G (底面図)</strong></p>

</br></br></br></br>

# 4. 仕様
---
## 4.1 Quad SPIフラッシュメモリ (U101)
---
Quad SPIフラッシュメモリに関する情報は次のとおりです。
  - 密度 : 64 Mb  

**注:** SNORはデフォルトではVCP-Gに実装されていません。

</br></br></br>

## 4.2 電源入力コネクタ (J101)
---
DC 12Vは、12VアダプタからJ101のDCジャックを介してVCP-Gに供給されます。
図 4.1は、J101の位置を示しています。
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Hardware/4.1%20Power%20In%20Connector%20(J101).png"></p>
<p align="center"><strong>図 4.1 電源入力コネクタ (J101)</strong><p>

</br></br></br>

## 4.3 JTAG用コネクタ (J100)
---
JTAGエミュレータは、デバッグのためにJ100を介してVCP-Gに接続できます。図 4.2は、J100の位置を示しています。
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Hardware/4.2%20Connector%20for%20JTAG%20(J100).png"></p>
<p align="center"><strong>図 4.2 JTAG用コネクタ (J100)</strong><p>
JTAGはデフォルトで無効になっています。JTAGを有効にするには、R178とR179の接続を変更する必要があります。R178によってTRSRnがHighに設定されると、MCUはJTAGモードに入ります。

表 4.1は、J100のピンについて説明しています。
<p align="center"><strong>表 4.1 J100ピンの説明</strong></p>
<div align="center">
	<table>
	  <tr>
	    <th rowspan="2"><strong>ピン番号</strong></th>
	    <th rowspan="2"><strong>回路図ネット名</strong></th>
	    <th><strong>方向</strong></th>
	    <th rowspan="2"><strong>説明</strong></th>
	  </tr>
	  <tr>
	    <th><strong>MCU ◄► J100</strong></th>
	  </tr>
	  <tr>
	    <td>1</td>
	    <td>SW_VDD_3P3</td>
	    <td>-</td>
	    <td>電源 3.3V</td>
	  </tr>
	  <tr>
	    <td>2</td>
	    <td>TMS</td>
	    <td>◄</td>
	    <td>テストモード状態</td>
	  </tr>
	  <tr>
	    <td>3</td>
	    <td>DGND</td>
	    <td>-</td>
	    <td>グラウンド</td>
	  </tr>
	  <tr>
	    <td>4</td>
	    <td>TCK</td>
	    <td>◄</td>
	    <td>テストクロック</td>
	  </tr>
	  <tr>
	    <td>5</td>
		<td>DGND</td>
	    <td>-</td>
	    <td>グラウンド</td>
	  </tr>
	  <tr>
	    <td>6</td>
	    <td>TDO</td>
	    <td>►</td>
	    <td>テストデータ出力</td>
	  </tr>
	  <tr>
	    <td>7</td>
	    <td>NC</td>
	    <td>-</td>
	    <td>未接続</td>
	  </tr>
	  <tr>
	    <td>8</td>
	    <td>TDI</td>
	    <td>◄</td>
	    <td>テストデータ入力</td>
	  </tr>
	  <tr>
	    <td>9</td>
	    <td>DGND</td>
	    <td>-</td>
	    <td>グラウンド</td>
	  </tr>
	  <tr>
	    <td>10</td>
	    <td>JTAG_RESETn</td>
	    <td>◄</td>
	    <td>システムリセット</td>
	  </tr>   
	</table>
</div>

表 4.2は、JTAG無効/有効の設定について説明しています。
<p align="center"><strong>表 4.2 JTAG無効/有効の設定</strong></p>
<div align="center">
	<table>
	  <tr>
	    <th colspan="4"><strong>モード</strong></th>
	    <th><strong>TRSTn値</strong></th>
	    <th><strong>R178</strong></th>
	    <th><strong>R179</strong></th>
	  </tr>
	  <tr>
	    <td colspan="4">JTAG無効 (デフォルト)</td>
	    <td>Low (1)</td>
	    <td>N.C</td>
	    <td>1K</td>
	  </tr>
	  <tr>
	    <td colspan="4">JTAG有効 (オプション)</td>
	    <td>High (1)</td>
	    <td>1K</td>
	    <td>N.C</td>
	  </tr>
	</table>
</div>
 
</br></br></br>
 
## 4.4 FWDNスイッチ (SW101)
---
VCP-Gには、ブートモード (BM) を使用したブート構成用のピンが1つあり、UART FWDNモードとノーマルモードの2つのモードをサポートしています。
図 4.3は、VCP-Gのブートモードを選択するために使用されるFWDNタクトスイッチ (SW101) の位置を示しています。
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Hardware/4.3%20FWDN%20Tact%20Switch%20(SW101).png"></p>
<p align="center"><strong>図 4.3 FWDNタクトスイッチ (SW101)</strong><p>
 
表 4.3は、FWDNタクトスイッチ (SW101) を使用してブートモードを選択する方法について説明しています。
<p align="center"><strong>表 4.3 ブートモード用タクトスイッチ (SW101) の説明</strong></p>
<div align="center">
	<table>
	  <tr>
	    <th colspan="3"><strong>モード</strong></th>
	    <th><strong>BM00値</strong></th>
	    <th><strong>SW101ステータス</strong></th>
	  </tr>
	  <tr>
	    <td colspan="3">ノーマル (デフォルト)</td>
	    <td>Low (1)</td>
	    <td>デフォルト</td>
	  </tr>
	  <tr>
	    <td colspan="3">FWDN (オプション)</td>
	    <td>High (1)</td>
	    <td>押下して電源オン</td>
	  </tr>
	</table>
</div>
</br></br>
 
### 4.4.1 FWDNモードの方法
FWDNモードに入るには、次の2つの方法があります。
 
#### 4.4.1.1 方法1
FWDNスイッチ (SW101) を押しながら、12V電源を接続してVCP-Gボードの電源を入れます。
FWDNスイッチを押しながら電源を投入すると、FWDN赤色インジケータが点灯します。FWDNスイッチ (SW101) を離すと、MCUはFWDNモードに入ります。
図 4.4は、方法1を使用してFWDNモードに入る方法を示しています。
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Hardware/4.4%20Entering%20FWDN%20Mode%20by%20Using%20Method%201.png"></p>
<p align="center"><strong>図 4.4 方法1を使用してFWDNモードに入る</strong><p>
 
#### 4.4.1.2 方法2
VCP-Gボードが12V電源に接続されている状態で、FWDNスイッチ (SW101) を押し、次にRESETタクトスイッチ (SW100) を押します。
FWDNスイッチを押しながら電源を投入すると、FWDN赤色インジケータが点灯します。RESETタクトスイッチを押している間、3.3V緑色インジケータは消灯します。FWDNスイッチ (SW101) を離すと、MCUはFWDNモードに入ります。
図 4.5は、方法2を使用したFWDNモードを示しています。
 
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Hardware/4.5%20Entering%20FWDN%20Mode%20by%20Using%20Method%202.png"></p>
<p align="center"><strong>図 4.5 方法2を使用してFWDNモードに入る</strong><p>
 
</br></br></br>
 
## 4.5 RESETタクトスイッチ (SW100)
---
VCP-Gには、GRESETnピンを使用したリセット用のRESETスイッチが1つあります。
図 4.6は、RESETタクトスイッチ (SW100) を示しています。
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Hardware/4.6%20RESET%20Tact%20Switch%20(SW100).png"></p>
<p align="center"><strong>図 4.6 RESETタクトスイッチ (SW100)</strong><p>
</br></br>
 
### 4.5.1 RESETタクトスイッチ (SW100) の機能
SW100は、VCP-Gの電源ブロックとシステムブロックをリセットするためのタクトスイッチです。
このボタンの機能は次のとおりです。
  - 電源が入っているときにRESETタクトスイッチ (SW100) を押すと、VCP-Gの電源ブロックとシステムが強制的にリセットされます。
 
**重要:** タクトスイッチを押すと、電源が突然オフになり、データが破損する可能性があるため、注意してください。
 
</br></br></br>
 
## 4.6 デバッグおよびFWDN用コネクタ (JC100)
---
JC100は標準のUSB Type-Cコネクタです。VCP-Gでは、JC100はUARTを介したデバッグまたはFWDNに使用されます。
図 4.7は、JC100の位置を示しています。
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Hardware/4.7%20USB%20Type-C%20Connector%20(JC100).png"></p>
<p align="center"><strong>図 4.7 USB Type-Cコネクタ (JC100)</strong><p>
 
JC100を介して、FWDNを実行したり、VCP-Gのデバッグメッセージを確認したりできます。
VCP-GのJC100にはUSB-to-UARTブリッジコントローラが内蔵されているため、USB Type-Cケーブルを使用してJC100をPCに直接接続できます。
 
</br></br></br>
 
## 4.7 GPIO、ADC、電源、CAN、SPI用ピンヘッダー
---
VCP-Gには、センサーやサブボードなどの他の周辺機器に接続するための、電源、GPIO、ADC、CAN、SPI用の9つの2.54 mmピンヘッダーがあります。
 
表 4.4は、VCP-G上の9つのピンヘッダーの目的について説明しています。
<p align="center"><strong>表 4.4 VCP-G上のピンヘッダー </strong></p>
<div align="center">
	<table>
	  <tr>
	    <td colspan="4"><strong>番号</strong></td>
	    <td><strong>参照番号</strong></td>
	    <td><strong>名前</strong></td>
	    <td><strong>説明</strong></td>
	  </tr>
	  <tr>
	    <td colspan="4">1</td>
	    <td>J18D100</td>
	    <td>36ピンメスヘッダー</td>
	    <td>GPIOおよびADC用ヘッダー</td>
	  </tr>
	  <tr>
	    <td colspan="4">2</td>
	    <td>J5D100</td>
	    <td>10ピンオスヘッダー</td>
	    <td>CAN用ヘッダー</td>
	  </tr>
	  <tr>
	    <td colspan="4">3</td>
	    <td>J3D100</td>
	    <td>6ピンオスヘッダー</td>
	    <td>SPI用ヘッダー</td>
	  </tr>
	  <tr>
	    <td colspan="4">4</td>
	    <td>J8D104</td>
	    <td>8ピンメスヘッダー</td>
	    <td>GPIOおよびADC用ヘッダー</td>
	  </tr>
	  <tr>
	    <td colspan="4">5</td>
	    <td>J8D102</td>
	    <td>8ピンメスヘッダー</td>
	    <td>GPIO用ヘッダー</td>
	  </tr>
	  <tr>
	    <td colspan="4">6</td>
	    <td>J10D100</td>
	    <td>10ピンメスヘッダー</td>
	    <td>GPIOおよびADC用ヘッダー</td>
	  </tr>
	  <tr>
	    <td colspan="4">7</td>
	    <td>J8D100</td>
	    <td>8ピンメスヘッダー</td>
	    <td>電源およびリセット用ヘッダー</td>
	  </tr>
	  <tr>
	    <td colspan="4">8</td>
	    <td>J8D101</td>
	    <td>8ピンメスヘッダー</td>
	    <td>GPIOおよびADC用ヘッダー</td>
	  </tr>
	  <tr>
	    <td colspan="4">9</td>
	    <td>J8D103</td>
	    <td>8ピンメスヘッダー</td>
	    <td>GPIOおよびADC用ヘッダー</td>
	  </tr>
	</table>
</div>
 
図 4.8は、VCP-G上のピンヘッダーの位置を示しています。
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Hardware/4.8%20Pin%20Headers%20on%20TOPST%20VCP-G%20Board.png"></p>
<p align="center"><strong>図 4.8 VCP-G上のピンヘッダー </strong><p>
 
表 4.5は、J10D100のピン説明を示しています。
<p align="center"><strong>表 4.5 J10D100ピンの説明</strong></p>
<div align="center">
	<table>
	  <tr>
	    <th rowspan="3"><strong>ピン番号</strong></th>
	    <th colspan="4"><strong>J10D100</strong></th>
	  </tr>
	  <tr>
	    <th rowspan="2"><strong>ポート名</strong></th>
	    <th rowspan="2"><strong>信号名</strong></th>
	    <th><strong>方向</strong></th>
	    <th rowspan="2"><strong>説明</strong></th>
	  </tr>
	  <tr>
	    <th><strong>MCU ◄► J10D100</strong></th>
	  </tr>
	  <tr>
	    <td>1</td>
	    <td>SCL</td>
	    <td>GPIO_AC07</td>
	    <td>◄►</td>
	    <td>GPIOまたはADC信号</td>
	  </tr>
	  <tr>
	    <td>2</td>
	    <td>SDA</td>
	    <td>GPIO_AC06</td>
	    <td>◄►</td>
	    <td>GPIOまたはADC信号</td>
	  </tr>
	  <tr>
	    <td>3</td>
	    <td>AREF</td>
	    <td>ADC06</td>
	    <td>◄</td>
	    <td>ADC信号</td>
	  </tr>
	  <tr>
	    <td>4</td>
	    <td>GND</td>
	    <td>DGND</td>
	    <td>-</td>
	    <td>グラウンド</td>
	  </tr>
	  <tr>
	    <td>5</td>
	    <td>13</td>
	    <td>GPIO_C12</td>
	    <td>◄►</td>
	    <td>GPIO信号</td>
	  </tr>
	  <tr>
	    <td>6</td>
	    <td>12</td>
	    <td>GPIO_C15</td>
	    <td>◄►</td>
	    <td>GPIO信号</td>
	  </tr>
	  <tr>
	    <td>7</td>
	    <td>11</td>
	    <td>GPIO_C14</td>
	    <td>◄►</td>
	    <td>GPIO信号</td>
	  </tr>
	  <tr>
	    <td>8</td>
	    <td>10</td>
	    <td>GPIO_C13</td>
	    <td>◄►</td>
	    <td>GPIO信号</td>
	  </tr>
	  <tr>
	    <td>9</td>
	    <td>9</td>
	    <td>GPIO_A12</td>
	    <td>◄►</td>
	    <td>GPIO信号</td>
	  </tr>
	  <tr>
	    <td>10</td>
	    <td>8</td>
	    <td>GPIO_B00</td>
	    <td>◄►</td>
	    <td>GPIO信号</td>
	  </tr>
	</table>
</div>
 
表 4.6は、J8D100のピン説明を示しています。
<p align="center"><strong>表 4.6 J8D100ピンの説明</strong></p>
<div align="center">
	<table>
	  <tr>
	    <th rowspan="3"><strong>ピン番号</strong></th>
	    <th colspan="4"><strong>J8D100</strong></th>
	  </tr>
	  <tr>
	    <th rowspan="2"><strong>ポート名</strong></th>
	    <th rowspan="2"><strong>信号名</strong></th>
	    <th><strong>方向</strong></th>
	    <th rowspan="2"><strong>説明</strong></th>
	  </tr>
	  <tr>
	    <th><strong>MCU ◄► J8D100</strong></th>
	  </tr>
	  <tr>
	    <td>1</td>
	    <td>-</td>
	    <td>-</td>
	    <td>-</td>
	    <td>-</td>
	  </tr>
	  <tr>
	    <td>2</td>
	    <td>IOREF</td>
	    <td>VCP_3P3</td>
	    <td>-</td>
	    <td>電源 3.3V</td>
	  </tr>
	  <tr>
	    <td>3</td>
	    <td>RST</td>
	    <td>RESET</td>
	    <td>◄</td>
	    <td>リセット信号</td>
	  </tr>
	  <tr>
	    <td>4</td>
	    <td>3.3V</td>
	    <td>VCP_3P3</td>
	    <td>-</td>
	    <td>電源 3.3V</td>
	  </tr>
	  <tr>
	    <td>5</td>
	    <td>5V</td>
	    <td>VCP_5P0</td>
	    <td>-</td>
	    <td>電源 5.0V</td>
	  </tr>
	  <tr>
	    <td>6</td>
	    <td>GND</td>
	    <td>DGND</td>
	    <td>-</td>
	    <td>グラウンド</td>
	  </tr>
	  <tr>
	    <td>7</td>
	    <td>GND</td>
	    <td>DGND</td>
	    <td>-</td>
	    <td>グラウンド</td>
	  </tr>
	  <tr>
	    <td>8</td>
	    <td>VIN</td>
	    <td>VIN</td>
	    <td>-</td>
	    <td>VCP-Gの電圧入力</td>
	  </tr>
	</table>
</div>
 
表 4.7は、J8D101のピン説明を示しています。
<p align="center"><strong>表 4.7 J8D101ピンの説明</strong></p>
<div align="center">
	<table>
	  <tr>
	    <th rowspan="3"><strong>ピン番号</strong></th>
	    <th colspan="4"><strong>J8D101</strong></th>
	  </tr>
	  <tr>
	    <th rowspan="2"><strong>ポート名</strong></th>
	    <th rowspan="2"><strong>信号名</strong></th>
	    <th><strong>方向</strong></th>
	    <th rowspan="2"><strong>説明</strong></th>
	  </tr>
	  <tr>
	    <th><strong>MCU ◄► J8D101</strong></th>
	  </tr>
	  <tr>
	    <td>1</td>
	    <td>A0</td>
	    <td>ADC03</td>
	    <td>◄</td>
	    <td>ADC信号</td>
	  </tr>
	  <tr>
	    <td>2</td>
	    <td>A1</td>
	    <td>ADC04</td>
	    <td>◄</td>
	    <td>ADC信号</td>
	  </tr>
	  <tr>
	    <td>3</td>
	    <td>A2</td>
	    <td>GPIO_AC02</td>
	    <td>◄►</td>
	    <td>GPIO信号</td>
	  </tr>
	  <tr>
	    <td>4</td>
	    <td>A3</td>
	    <td>GPIO_AC03</td>
	    <td>◄►</td>
	    <td>GPIO信号</td>
	  </tr>
	  <tr>
	    <td>5</td>
	    <td>A4</td>
	    <td>GPIO_AC05</td>
	    <td>◄►</td>
	    <td>GPIO信号</td>
	  </tr>
	  <tr>
	    <td>6</td>
	    <td>A5</td>
	    <td>GPIO_AC04</td>
	    <td>◄►</td>
	    <td>GPIO信号</td>
	  </tr>
	  <tr>
	    <td>7</td>
	    <td>A6</td>
	    <td>ADC05</td>
	    <td>◄</td>
	    <td>ADC信号</td>
	  </tr>
	  <tr>
	    <td>8</td>
	    <td>A7</td>
	    <td>ADC02</td>
	    <td>◄</td>
	    <td>ADC信号</td>
	  </tr>
	</table>
</div>
 
表 4.8は、J8D103のピン説明を示しています。
<p align="center"><strong>表 4.8 J8D103ピンの説明</strong></p>
<div align="center">
	<table>
	  <tr>
	    <th rowspan="3"><strong>ピン番号</strong></th>
	    <th colspan="4"><strong>J8D103</strong></th>
	  </tr>
	  <tr>
	    <th rowspan="2"><strong>ポート名</strong></th>
	    <th rowspan="2"><strong>信号名</strong></th>
	    <th><strong>方向</strong></th>
	    <th rowspan="2"><strong>説明</strong></th>
	  </tr>
	  <tr>
	    <th><strong>MCU ◄► J8D103</strong></th>
	  </tr>
	  <tr>
	    <td>1</td>
	    <td>0</td>
	    <td>GPIO_B01</td>
	    <td>◄►</td>
	    <td>GPIO信号</td>
	  </tr>
	  <tr>
	    <td>2</td>
	    <td>1</td>
	    <td>GPIO_B02</td>
	    <td>◄►</td>
	    <td>GPIO信号</td>
	  </tr>
	  <tr>
	    <td>3</td>
	    <td>2</td>
	    <td>GPIO_B03</td>
	    <td>◄►</td>
	    <td>GPIO信号</td>
	  </tr>
	  <tr>
	    <td>4</td>
	    <td>3</td>
	    <td>GPIO_B04</td>
	    <td>◄►</td>
	    <td>GPIO信号</td>
	  </tr>
	  <tr>
	    <td>5</td>
	    <td>4</td>
	    <td>GPIO_B05</td>
	    <td>◄►</td>
	    <td>GPIO信号</td>
	  </tr>
	  <tr>
	    <td>6</td>
	    <td>5</td>
	    <td>GPIO_B06</td>
	    <td>◄►</td>
	    <td>GPIO信号</td>
	  </tr>
	  <tr>
	    <td>7</td>
	    <td>6</td>
	    <td>GPIO_B07</td>
	    <td>◄►</td>
	    <td>GPIO信号</td>
	  </tr>
	  <tr>
	    <td>8</td>
	    <td>7</td>
	    <td>GPIO_B08</td>
	    <td>◄►</td>
	    <td>GPIO信号</td>
	  </tr>
	</table>
</div>
 
表 4.9は、J8D102のピン説明を示しています。
<p align="center"><strong>表 4.9 J8D102ピンの説明</strong></p>
<div align="center">
	<table>
	  <tr>
	    <th rowspan="3"><strong>ピン番号</strong></th>
	    <th colspan="4"><strong>J8D102</strong></th>
	  </tr>
	  <tr>
	    <th rowspan="2"><strong>ポート名</strong></th>
	    <th rowspan="2"><strong>信号名</strong></th>
	    <th><strong>方向</strong></th>
	    <th rowspan="2"><strong>説明</strong></th>
	  </tr>
	  <tr>
	    <th><strong>MCU ◄► J8D102</strong></th>
	  </tr>
	  <tr>
	    <td>1</td>
	    <td>24</td>
	    <td>GPIO_C24</td>
	    <td>◄►</td>
	    <td>GPIO信号</td>
	  </tr>
	  <tr>
	    <td>2</td>
	    <td>25</td>
	    <td>GPIO_C25</td>
	    <td>◄►</td>
	    <td>GPIO信号</td>
	  </tr>
	  <tr>
	    <td>3</td>
	    <td>26</td>
	    <td>GPIO_C26</td>
	    <td>◄►</td>
	    <td>GPIO信号</td>
	  </tr>
	  <tr>
	    <td>4</td>
	    <td>27</td>
	    <td>GPIO_C27</td>
	    <td>◄►</td>
	    <td>GPIO信号</td>
	  </tr>
	  <tr>
	    <td>5</td>
	    <td>28</td>
	    <td>GPIO_C28</td>
	    <td>◄►</td>
	    <td>GPIO信号</td>
	  </tr>
	  <tr>
	    <td>6</td>
	    <td>29</td>
	    <td>GPIO_C29</td>
	    <td>◄►</td>
	    <td>GPIO信号</td>
	  </tr>
	  <tr>
	    <td>7</td>
	    <td>30</td>
	    <td>GPIO_C30</td>
	    <td>◄►</td>
	    <td>GPIO信号</td>
	  </tr>
	  <tr>
	    <td>8</td>
	    <td>31</td>
	    <td>GPIO_C31</td>
	    <td>◄►</td>
	    <td>GPIO信号</td>
	  </tr>
	</table>
</div>
 
表 4.10は、J8D104のピン説明を示しています。
<p align="center"><strong>表 4.10 J8D104ピンの説明</strong></p>
<div align="center">
	<table>
	  <tr>
	    <th rowspan="3"><strong>ピン番号</strong></th>
	    <th colspan="4"><strong>J8D104</strong></th>
	  </tr>
	  <tr>
	    <th rowspan="2"><strong>ポート名</strong></th>
	    <th rowspan="2"><strong>信号名</strong></th>
	    <th><strong>方向</strong></th>
	    <th rowspan="2"><strong>説明</strong></th>
	  </tr>
	  <tr>
	    <th><strong>MCU ◄► J8D104</strong></th>
	  </tr>
	  <tr>
	    <td>1</td>
	    <td>32</td>
	    <td>GPIO_D00</td>
	    <td>◄►</td>
	    <td>GPIO信号</td>
	  </tr>
	  <tr>
	    <td>2</td>
	    <td>33</td>
	    <td>GPIO_D01</td>
	    <td>◄►</td>
	    <td>GPIO信号</td>
	  </tr>
	  <tr>
	    <td>3</td>
	    <td>34</td>
	    <td>GPIO_D02</td>
	    <td>◄►</td>
	    <td>GPIO信号</td>
	  </tr>
	  <tr>
	    <td>4</td>
	    <td>35</td>
	    <td>GPIO_D03</td>
	    <td>◄►</td>
	    <td>GPIO信号</td>
	  </tr>
	  <tr>
	    <td>5</td>
	    <td>36</td>
	    <td>GPIO_D04</td>
	    <td>◄►</td>
	    <td>GPIO信号</td>
	  </tr>
	  <tr>
	    <td>6</td>
	    <td>37</td>
	    <td>GPIO_D05</td>
	    <td>◄►</td>
	    <td>GPIO信号</td>
	  </tr>
	  <tr>
	    <td>7</td>
	    <td>38</td>
	    <td>GPIO_D06</td>
	    <td>◄►</td>
	    <td>GPIO信号</td>
	  </tr>
	  <tr>
	    <td>8</td>
	    <td>39</td>
	    <td>GPIO_D07</td>
	    <td>◄►</td>
	    <td>GPIO信号</td>
	  </tr>
	</table>
</div>
 
表 4.11は、J3D100のピン説明を示しています。
<p align="center"><strong>表 4.11 J3D100ピンの説明</strong></p>
<div align="center">
	<table>
	  <tr>
	    <th rowspan="3"><strong>ピン番号</strong></th>
	    <th colspan="4"><strong>J3D100</strong></th>
	  </tr>
	  <tr>
	    <th rowspan="2"><strong>ポート名</strong></th>
	    <th rowspan="2"><strong>信号名</strong></th>
	    <th><strong>方向</strong></th>
	    <th rowspan="2"><strong>説明</strong></th>
	  </tr>
	  <tr>
	    <th><strong>MCU ◄► J3D100</strong></th>
	  </tr>
	  <tr>
	    <td>1</td>
	    <td>MISO</td>
	    <td>GPIO_C09</td>
	    <td>◄</td>
	    <td>SPI MISO信号</td>
	  </tr>
	  <tr>
	    <td>2</td>
	    <td>VCC</td>
	    <td>VCP_5P0</td>
	    <td>-</td>
	    <td>電源 5.0V</td>
	  </tr>
	  <tr>
	    <td>3</td>
	    <td>SCK</td>
	    <td>GPIO_C10</td>
	    <td>►</td>
	    <td>SPIクロック信号</td>
	  </tr>
	  <tr>
	    <td>4</td>
	    <td>MOSI</td>
	    <td>GPIO_C08</td>
	    <td>►</td>
	    <td>SPI MOSI信号</td>
	  </tr>
	  <tr>
	    <td>5</td>
	    <td>RST</td>
	    <td>RESET</td>
	    <td>◄</td>
	    <td>リセット信号</td>
	  </tr>
	  <tr>
	    <td>6</td>
	    <td>GND</td>
	    <td>DGND</td>
	    <td>-</td>
	    <td>グラウンド</td>
	  </tr>
	</table>
</div>
 
表 4.12は、J5D100のピン説明を示しています。
<p align="center"><strong>表 4.12 J5D100ピンの説明</strong></p>
<div align="center">
	<table>
	  <tr>
	    <th rowspan="3"><strong>ピン番号</strong></th>
	    <th colspan="4"><strong>J5D100</strong></th>
	  </tr>
	  <tr>
	    <th rowspan="2"><strong>ポート名</strong></th>
	    <th rowspan="2"><strong>信号名</strong></th>
	    <th><strong>方向</strong></th>
	    <th rowspan="2"><strong>説明</strong></th>
	  </tr>
	  <tr>
	    <th><strong>MCU ◄► J5D100</strong></th>
	  </tr>
	  <tr>
	    <td>1</td>
	    <td>RX</td>
	    <td>GPIO_C01</td>
	    <td>◄</td>
	    <td>UART RX信号</td>
	  </tr>
	  <tr>
	    <td>2</td>
	    <td>TX</td>
	    <td>GPIO_C00</td>
	    <td>►</td>
	    <td>UART TX信号</td>
	  </tr>
	  <tr>
	    <td>3</td>
	    <td>2</td>
	    <td>GPIO_C02</td>
	    <td>◄►</td>
	    <td>GPIO信号</td>
	  </tr>
	  <tr>
	    <td>4</td>
	    <td>3</td>
	    <td>GPIO_C03</td>
	    <td>◄►</td>
	    <td>GPIO信号</td>
	  </tr>
	  <tr>
	    <td>5</td>
	    <td>CANH</td>
	    <td>CAN0_H</td>
	    <td>◄►</td>
	    <td>CAN High信号</td>
	  </tr>
	  <tr>
	    <td>6</td>
	    <td>CANL</td>
	    <td>CAN0_L</td>
	    <td>◄►</td>
	    <td>CAN Low信号</td>
	  </tr>
	  <tr>
	    <td>7</td>
	    <td>GND</td>
	    <td>DGND</td>
	    <td>-</td>
	    <td>グラウンド</td>
	  </tr>
	  <tr>
	    <td>8</td>
	    <td>GND</td>
	    <td>DGND</td>
	    <td>-</td>
	    <td>グラウンド</td>
	  </tr>
	  <tr>
	    <td>9</td>
	    <td>I2C_SCL</td>
	    <td>GPIO_C05</td>
	    <td>◄►</td>
	    <td>I2Cクロック信号</td>
	  </tr>
	  <tr>
	    <td>10</td>
	    <td>I2C_SDA</td>
	    <td>GPIO_C04</td>
	    <td>◄►</td>
	    <td>I2Cデータ信号</td>
	  </tr>
	</table>
</div>
 
表 4.13は、J18D100のピン説明を示しています。
<p align="center"><strong>表 4.13 J18D100ピンの説明</strong></p>
<div align="center">
	<table>
	  <tr>
	    <th rowspan="3"><strong>ピン番号</strong></th>
	    <th colspan="4"><strong>J18D100</strong></th>
	  </tr>
	  <tr>
	    <th rowspan="2"><strong>ポート名</strong></th>
	    <th rowspan="2"><strong>信号名</strong></th>
	    <th><strong>方向</strong></th>
	    <th rowspan="2"><strong>説明</strong></th>
	  </tr>
	  <tr>
	    <th><strong>MCU ◄► J18D100</strong></th>
	  </tr>
	  <tr>
	    <td>1</td>
	    <td>3.3V</td>
	    <td>VCP_3P3</td>
	    <td>-</td>
	    <td>電源 3.3V</td>
	  </tr>
	  <tr>
	    <td>2</td>
	    <td>5V</td>
	    <td>VCP_5P0</td>
	    <td>-</td>
	    <td>電源 5.0V</td>
	  </tr>
	  <tr>
	    <td>3</td>
	    <td>22</td>
	    <td>GPIO_C22</td>
	    <td>◄►</td>
	    <td>GPIO信号</td>
	  </tr>
	  <tr>
	    <td>4</td>
	    <td>5V</td>
	    <td>VCP_5P0</td>
	    <td>-</td>
	    <td>電源 5.0V</td>
	  </tr>
	  <tr>
	    <td>5</td>
	    <td>23</td>
	    <td>GPIO_C23</td>
	    <td>◄►</td>
	    <td>GPIO信号</td>
	  </tr>
	  <tr>
	    <td>6</td>
	    <td>GND</td>
	    <td>DGND</td>
	    <td>-</td>
	    <td>グラウンド</td>
	  </tr>
	  <tr>
	    <td>7</td>
	    <td>24</td>
	    <td>GPIO_C24</td>
	    <td>◄►</td>
	    <td>GPIO信号</td>
	  </tr>
	  <tr>
	    <td>8</td>
	    <td>25</td>
	    <td>GPIO_C25</td>
	    <td>◄►</td>
	    <td>GPIO信号</td>
	  </tr>
	  <tr>
	    <td>9</td>
	    <td>GND</td>
	    <td>DGND</td>
	    <td>-</td>
	    <td>グラウンド</td>
	  </tr>
	  <tr>
	    <td>10</td>
	    <td>26</td>
	    <td>GPIO_C26</td>
	    <td>◄►</td>
	    <td>GPIO信号</td>
	  </tr>
	  <tr>
	    <td>11</td>
	    <td>27</td>
	    <td>GPIO_C27</td>
	    <td>◄►</td>
	    <td>GPIO信号</td>
	  </tr>
	  <tr>
	    <td>12</td>
	    <td>28</td>
	    <td>GPIO_C28</td>
	    <td>◄►</td>
	    <td>GPIO信号</td>
	  </tr>
	  <tr>
	    <td>13</td>
	    <td>29</td>
	    <td>GPIO_C29</td>
	    <td>◄►</td>
	    <td>GPIO信号</td>
	  </tr>
	  <tr>
	    <td>14</td>
	    <td>GND</td>
	    <td>DGND</td>
	    <td>-</td>
	    <td>グラウンド</td>
	  </tr>
	  <tr>
	    <td>15</td>
	    <td>30</td>
	    <td>GPIO_C30</td>
	    <td>◄►</td>
	    <td>GPIO信号</td>
	  </tr>
	  <tr>
	    <td>16</td>
	    <td>31</td>
	    <td>GPIO_C31</td>
	    <td>◄►</td>
	    <td>GPIO信号</td>
	  </tr>
	  <tr>
	    <td>17</td>
	    <td>3.3V</td>
	    <td>VCP_3P3</td>
	    <td>-</td>
	    <td>電源 3.3V</td>
	  </tr>
	  <tr>
	    <td>18</td>
	    <td>32</td>
	    <td>GPIO_D00</td>
	    <td>◄►</td>
	    <td>GPIO信号</td>
	  </tr>
	  <tr>
	    <td>19</td>
	    <td>33</td>
	    <td>GPIO_D01</td>
	    <td>◄►</td>
	    <td>GPIO信号</td>
	  </tr>
	  <tr>
	    <td>20</td>
	    <td>GND</td>
	    <td>DGND</td>
	    <td>-</td>
	    <td>グラウンド</td>
	  </tr>
	  <tr>
	    <td>21</td>
	    <td>34</td>
	    <td>GPIO_D02</td>
	    <td>◄►</td>
	    <td>GPIO信号</td>
	  </tr>
	  <tr>
	    <td>22</td>
	    <td>35</td>
	    <td>GPIO_D03</td>
	    <td>◄►</td>
	    <td>GPIO信号</td>
	  </tr>
	  <tr>
	    <td>23</td>
	    <td>36</td>
	    <td>GPIO_D04</td>
	    <td>◄►</td>
	    <td>GPIO信号</td>
	  </tr>
	  <tr>
	    <td>24</td>
	    <td>37</td>
	    <td>GPIO_D05</td>
	    <td>◄►</td>
	    <td>GPIO信号</td>
	  </tr>
	  <tr>
	    <td>25</td>
	    <td>GND</td>
	    <td>DGND</td>
	    <td>-</td>
	    <td>グラウンド</td>
	  </tr>
	  <tr>
	    <td>26</td>
	    <td>38</td>
	    <td>GPIO_D06</td>
	    <td>◄►</td>
	    <td>GPIO信号</td>
	  </tr>
	  <tr>
	    <td>27</td>
	    <td>39</td>
	    <td>GPIO_D07</td>
	    <td>◄►</td>
	    <td>GPIO信号</td>
	  </tr>
	  <tr>
	    <td>28</td>
	    <td>40</td>
	    <td>GPIO_D08</td>
	    <td>◄►</td>
	    <td>GPIO信号</td>
	  </tr>
	  <tr>
	    <td>29</td>
	    <td>41</td>
	    <td>GPIO_D09</td>
	    <td>◄►</td>
	    <td>GPIO信号</td>
	  </tr>
	  <tr>
	    <td>30</td>
	    <td>GND</td>
	    <td>DGND</td>
	    <td>-</td>
	    <td>グラウンド</td>
	  </tr>
	  <tr>
	    <td>31</td>
	    <td>42</td>
	    <td>GPIO_D10</td>
	    <td>◄►</td>
	    <td>GPIO信号</td>
	  </tr>
	  <tr>
	    <td>32</td>
	    <td>43</td>
	    <td>GPIO_D11</td>
	    <td>◄►</td>
	    <td>GPIO信号</td>
	  </tr>
	  <tr>
	    <td>33</td>
	    <td>44</td>
	    <td>GPIO_D12</td>
	    <td>◄►</td>
	    <td>GPIO信号</td>
	  </tr>
	  <tr>
	    <td>34</td>
	    <td>GND</td>
	    <td>DGND</td>
	    <td>-</td>
	    <td>グラウンド</td>
	  </tr>
	  <tr>
	    <td>35</td>
	    <td>45</td>
	    <td>GPIO_D13</td>
	    <td>◄►</td>
	    <td>GPIO信号</td>
	  </tr>
	  <tr>
	    <td>36</td>
	    <td>46</td>
<div align="center">
	<table>
	  <tr>
	    <th rowspan="3"><strong>Pin Number</strong></th>
	    <th colspan="4"><strong>J5D100</strong></th>
	  </tr>
	  <tr>
	    <th rowspan="2"><strong>Port Name</strong></th>
	    <th rowspan="2"><strong>Signal Name</strong></th>
	    <th><strong>DIR</strong></th>
	    <th rowspan="2"><strong>Description</strong></th>
	  </tr>
	  <tr>
	    <th><strong>MCU ◄► J5D100</strong></th>
	  </tr>
	  <tr>
	    <td>1</td>
	    <td>3.3V</td>
	    <td>VCP_3P3</td>
	    <td>-</td>
	    <td>Power 3.3V</td>
	  </tr>
	  <tr>
	    <td>2</td>
	    <td>3.3V</td>
	    <td>VCP_3P3</td>
	    <td>-</td>
    <td>Power 3.3V</td>
	  </tr>
	  <tr>
	    <td>3</td>
	    <td>TX0</td>
	    <td>GPIO_K08</td>
	    <td>◄►</td>
	    <td>GPIO signal</td>
	  </tr>
	  <tr>
	    <td>4</td>
	    <td>RX0</td>
	    <td>GPIO_K01</td>
	    <td>◄</td>
	    <td>GPIO signal</td>
	  </tr>
	  <tr>
	    <td>5</td>
	    <td>TX1</td>
	    <td>GPIO_K09</td>
	    <td>◄►</td>
	    <td>GPIO signal</td>
	  </tr>
	  <tr>
	    <td>6</td>
	    <td>RX1</td>
	    <td>GPIO_K02</td>
	    <td>◄</td>
	    <td>GPIO signal</td>
	  </tr>
	  <tr>
	    <td>7</td>
	    <td>TX2</td>
	    <td>GPIO_K10</td>
	    <td>◄►</td>
	    <td>GPIO signal</td>
	  </tr>
	  <tr>
	    <td>8</td>
	    <td>RX2</td>
	    <td>GPIO_K03</td>
	    <td>◄</td>
	    <td>GPIO signal</td>
	  </tr>
	  <tr>
	    <td>9</td>
	    <td>GND</td>
	    <td>DGND</td>
	    <td>-</td>
	    <td>DGND</td>
	  </tr>
	  <tr>
	    <td>10</td>
	    <td>GND</td>
	    <td>DGND</td>
	    <td>-</td>
	    <td>DGND</td>
	  </tr>
	</table>
</div>

Figure 4.9 shows the total pin assignment of ten pin headers on the VCP-G.
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Hardware/4.9%20Total%20Pin%20Assignment%20of%20Pin%20Headers%20on%20TOPST%20VCP-G%20Board.png"></p>
<p align="center"><strong>Figure 4.9 Total Pin Assignment of Pin Headers on VCP-G </strong><p>

# References
  - Contact TOPST for more details: topst@topst.ai

**Note:** Reference documents can be provided whenever available, depending on the terms of a contract. If the reference documents are unavailable, the contents directly related to your development can be guided.
