# 1. はじめに
---
本書は、TCC7045 アプリケーションプロセッサをベースとした VCP-G のハードウェアユーザーガイドです。本書では、VCP-G のシステム設置、デバッグ、および全体的な設計と使用方法に関する詳細な情報について説明します。


表 1.1 に VCP-G の特長を示します。

<p align="center"><strong>表 1.1 VCP-G の特長</strong></p>
<div align="center">
	<table>
	  <tr>
	    <td colspan="3">部品名</td>
	    <td>TCC7045</td>
	  </tr>
	  <tr>
	    <td colspan="3">パッケージ</td>
	    <td>パッケージ	ピン・ツー・ピン互換 FBGA 196-pin (12BD)</td>
	  </tr>
	    <tr>
	    <td colspan="3">CPU 周波数</td>
	    <td>200 MHz (最大 300 MHz)</td>
	  </tr>
	  <tr>
	    <td rowspan="4">オンチップメモリ</td>
	    <td colspan="2">プログラムフラッシュ</td>
	    <td colspan="3">4 MB</td>
	  </tr>
	  <tr>
	    <td colspan="2">SRAM</td>
	    <td colspan="3">512 KB (Retention RAM 16 KB を含む)</td>
	  </tr>
	  <tr>
	    <td colspan="2">DataFlash</td>
	    <td colspan="3">256 KB</td>
	  </tr>
	  <tr>
	    <td colspan="2">DMA チャネル</td>
	    <td colspan="3">16 チャネル</td>
	  </tr>
	  <tr>
	    <td rowspan="13">周辺機能</td>
	    <td colspan="2">Ethernet</td>
	    <td>1 Gbps (AVB 対応)</td>
	  </tr>
	  <tr>
		<td colspan="2">CAN / CANFD</td>
	    <td>3 チャネル</td>
	  </tr>
	  <tr>
	    <td colspan="2">専用 LIN / UART</td>
	    <td>3 チャネル (最大 6 チャネル)</td>
	  </tr>
	  <tr>
	    <td colspan="2">専用 I2C</td>
	    <td>3 チャネル (最大 6 チャネル)</td>
	  </tr>
	  <tr>
	  <tr>
	    <td colspan="2">専用 GPSB (SPI)</td>
	    <td>2 チャネル (最大 5 チャネル)</td>
	  </tr>
	    <tr>
	    <td colspan="2">MFIO (UART、I2C、GPSB に割り当て)</td>
	    <td>3 チャネル</td>
	  </tr>
	  <tr>
	    <td rowspan="4">ADC</td> 
	    <td>分解能</td>
	    <td>12 ビット SAR 方式</td>
	  </tr>
	  <tr>
	    <td>チャネル</td>
	    <td>12 チャネル x 2 グループ</td>
	  </tr>
	  <tr>
	    <td>入力範囲</td>
	    <td>3.3V</td>
	  </tr>
	  <tr>
	    <td>サンプルレート</td>
	    <td>1.0 MSPs 以上</td>
	  </tr>
	  <tr>
	    <td colspan="2">I2S</td>
	    <td>1 チャネル</td>
	  </tr>
	  <tr>
	    <td colspan="2">シリアルフラッシュインターフェース</td>
	    <td>Quad SPI</td>
	  </tr>  
	  <tr>
	    <td colspan="3">電源システム</td>
	    <td>3.3V シングル</td>
	  </tr>
	  <tr>
	    <td colspan="3">温度</td>
	    <td>-40 ℃ to 105 ℃</td>
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
	    <td>アナログ・デジタル変換器</td>
	  </tr>
	  <tr>
	    <td clospan="2">FWDN</td>
	    <td>ファームウェアダウンロード</td>
	  </tr>
	  <tr>
	    <td clospan="2">GPIO</td>
	    <td>汎用入出力</td>
	  </tr>
	  <tr>
	    <td clospan="2">MCU</td>
	    <td>マイクロコントローラユニット</td>
	  </tr>
	  <tr>
	    <td clospan="2">TOPST</td>
	    <td>システム開発およびトレーニングのための統合オープンプラットフォーム</td>
	  </tr>
	  <tr>
	    <td clospan="2">VCP</td>
	    <td>車両制御プロセッサ</td>
	  </tr>
	</table>
</div>

</br></br></br></br>

# 2. ブロック図
---
## 2.1 システムブロック図
---
図 2.1 に VCP-G のシステムブロック図を示します。
<p align="center"><img src= "https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Hardware/2.1%20VCP-G%20System%20Block%20Diagram.png"></p>
<p align="center"><strong>図 2.1 システムブロック図</strong></p>

</br></br></br></br>

# 3. VCP-G の概要
---
VCP-G は次の用途に使用できます。
  - システム開発
  - トレーニング

表 3.1 に VCP-G のデフォルト構成を示します。

<p align="center"><strong>表 3.1 VCP-G のデフォルト構成 </strong></p>
<div align="center">
	<table>
	  <tr>
	    <td colspan="2"><strong>ボード名</strong></td>
	    <td><strong>説明</strong></p>
	  </tr>
	  <tr>
	    <td colspan="2">TOPST_VCP_V2.1.1</td>
	    <td>TOPST 用 MCU ボード</td>
	  </tr>
	</table>
</div>

</br></br></br>

## 3.1 VCP-G
---
図 3.1 に VCP-G の上面図を示します。
<p align="center"><img src= "https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Hardware/3.1%20TOPST%20VCP-G%20Board%20(Top%20View)%20.png"></p>
<p align="center"><strong>図 3.1 VCP-G (上面図)</strong></p>

表 3.2 に VCP-G (上面図) のコネクタを示します。
<p align="center"><strong>表 3.2 VCP-G のコネクタ (上面図)</strong></p>
<div align="center">
	<table>
	  <tr>
	    <td colspan="4"><strong>番号</strong></td>
	    <td><strong>参照番号</strong></td>
	    <td><strong>名称</strong></td>
	    <td><strong>説明</strong></td>
	  </tr>
	  <tr>
	    <td colspan="4">1</td>
	    <td>J18D100</td>
	    <td>36 ピンメスヘッダ</td>
	    <td>GPIO および ADC 用ヘッダ</td>
	  </tr>
	  <tr>
	    <td colspan="4">2</td>
	    <td>J5D100</td>
	    <td>10 ピンオスヘッダ</td>
	    <td>CAN 用ヘッダ</td>
	  </tr>
	  <tr>
	    <td colspan="4">3</td>
	    <td>J3D100</td>
	    <td>6 ピンオスヘッダ</td>
	    <td>SPI 用ヘッダ</td>
	  </tr>
	  <tr>
	    <td colspan="4">4</td>
	    <td>J8D104</td>
	    <td>8 ピンメスヘッダ</td>
	    <td>GPIO および ADC 用ヘッダ</td>
	  </tr>
	  <tr>
	    <td colspan="4">5</td>
	    <td>J8D102</td>
	    <td>8 ピンメスヘッダ</td>
	    <td>GPIO 用ヘッダ</td>
	  </tr>
	  <tr>
	    <td colspan="4">6</td>
	    <td>J10D100</td>
	    <td>10 ピンメスヘッダ</td>
	    <td>GPIO および ADC 用ヘッダ</td>
	  </tr>
	  <tr>
	    <td colspan="4">7</td>
	    <td>J100</td>
	    <td>10 ピンオスヘッダ</td>
	    <td>JTAG 用ヘッダ</td>
	  </tr>
	  <tr>
	    <td colspan="4">8</td>
	    <td>SW100</td>
	    <td>RESET タクトスイッチ</td>
	    <td>GRESETn: VCP-G のシステムおよび電源管理を初期化します</td>
	  </tr>
	  <tr>
	    <td colspan="4">9</td>
	    <td>JC100</td>
	    <td>USB Type-C コネクタ</td>
	    <td>デバッグまたは FWDN ポート用 UART</td>
	  </tr>
	  <tr>
	    <td colspan="4">10</td>
	    <td>SW101</td>
	    <td>タクトスイッチ</td>
	    <td>FWDN: VCP-G のファームウェアダウンロードモードに移行します</td>
	  </tr>  
	  <tr>
	    <td colspan="4">11</td>
		<td>J101</td>
	    <td>DC ジャック</td>
	    <td>DC 電源入力ジャック</td>
	  </tr>  
	  <tr>
	    <td colspan="4">12</td>
	    <td>J8D100</td>
	    <td>8 ピンメスヘッダ</td>
	    <td>電源およびリセット用ヘッダ</td>
	  </tr>  
	  <tr>
	    <td colspan="4">13</td>
	    <td>J8D101</td>
	    <td>8 ピンメスヘッダ</td>
	    <td>GPIO および ADC 用ヘッダ</td>
	  </tr>  
	  <tr>
	    <td colspan="4">14</td>
	    <td>J8D103</td>
	    <td>8 ピンメスヘッダ</td>
	    <td>GPIO および ADC 用ヘッダ</td>
	  </tr>    
	</table>
</div>

図 3.2 に VCP-G の底面図を示します。  

**注意:** 図 3.2 は現在 TOPST_VCP-G_V1.1.1 ボードを示しています。この画像は TOPST_VCP-G_V2.1.1 ボードに更新される予定です。
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Hardware/3.2%20TOPST%20VCP-G%20Board%20(Bottom%20View).png"></p>
<p align="center"><strong>図 3.2 VCP-G (底面図)</strong></p>

</br></br></br></br>

# 4. 仕様
---
## 4.1 Quad SPI フラッシュメモリ (U101)
---
Quad SPI フラッシュメモリに関する情報は次のとおりです。
  - 容量 : 64 Mb  
  
**注意:** SNOR はデフォルトでは VCP-G に実装されていません。

</br></br></br>

## 4.2 電源入力コネクタ (J101)
---
12V アダプタから J101 の DC ジャックを通じて VCP-G に DC 12V が供給されます。  
図 4.1 に J101 の位置を示します。
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Hardware/4.1%20Power%20In%20Connector%20(J101).png"></p>
<p align="center"><strong>図 4.1 電源入力コネクタ (J101)</strong><p>

</br></br></br>

## 4.3 JTAG 用コネクタ (J100)
---
デバッグのために、J100 を通じて VCP-G に JTAG エミュレータを接続できます。図 4.2 に J100 の位置を示します。
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Hardware/4.2%20Connector%20for%20JTAG%20(J100).png"></p>
<p align="center"><strong>図 4.2 JTAG 用コネクタ (J100)</strong><p>
JTAG はデフォルトで無効になっています。JTAG を有効にするには、R178 と R179 の接続を変更する必要があります。R178 によって TRSRn が high に設定されると、MCU は JTAG モードに移行します。

表 4.1 に J100 のピンを示します。
<p align="center"><strong>表 4.1 J100 ピンの説明</strong></p>
<div align="center">
	<table>
	  <tr>
	    <th rowspan="2"><strong>ピン番号</strong></th>
	    <th rowspan="2"><strong>回路図ネット名</strong></th>
	    <th><strong>DIR</strong></th>
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
	    <td>テストモードステート</td>
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

表 4.2 に JTAG の無効/有効の設定を示します。
<p align="center"><strong>表 4.2 JTAG の無効/有効の設定</strong></p>
<div align="center">
	<table>
	  <tr>
	    <th colspan="4"><strong>モード</strong></th>
	    <th><strong>TRSTn の値</strong></th>
	    <th><strong>R178</strong></th>
	    <th><strong>R179</strong></th>
	  </tr>
	  <tr>
	    <td colspan="4">JTAG 無効 (デフォルト)</td>
	    <td>Low (1)</td>
	    <td>N.C</td>
	    <td>1K</td>
	  </tr>
	  <tr>
	    <td colspan="4">JTAG 有効 (オプション)</td>
	    <td>High (1)</td>
	    <td>1K</td>
	    <td>N.C</td>
	  </tr>
	</table>
</div>

</br></br></br>

## 4.4 FWDN スイッチ (SW101)
---
VCP-G は Boot Mode (BM) による起動設定用のピンを 1 本備えており、UART FWDN モードと通常モードの 2 つのモードをサポートします。   
図 4.3 に、VCP-G の起動モードを選択するために使用する FWDN タクトスイッチ (SW101) の位置を示します。
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Hardware/4.3%20FWDN%20Tact%20Switch%20(SW101).png"></p>
<p align="center"><strong>図 4.3 FWDN タクトスイッチ (SW101)</strong><p>

表 4.3 に、FWDN タクトスイッチ (SW101) を使用して起動モードを選択する方法を示します。
<p align="center"><strong>表 4.3 起動モード用タクトスイッチ (SW101) の説明</strong></p>
<div align="center">
	<table>
	  <tr>
	    <th colspan="3"><strong>モード</strong></th>
	    <th><strong>BM00 の値</strong></th>
	    <th><strong>SW101 の状態</strong></th>
	  </tr>
	  <tr>
	    <td colspan="3">通常 (デフォルト)</td>
	    <td>Low (1)</td>
	    <td>デフォルト</td>
	  </tr>
	  <tr>
	    <td colspan="3">FWDN (オプション)</td>
	    <td>High (1)</td>
	    <td>押しながら電源投入</td>
	  </tr>
	</table>
</div>
</br></br>

### 4.4.1 FWDN モードへの移行方法
FWDN モードに移行する方法は次の 2 つがあります。

#### 4.4.1.1 方法 1
FWDN スイッチ (SW101) を押しながら 12V 電源を接続し、VCP-G ボードの電源を入れてください。  
FWDN スイッチを押した状態で電源が投入されると、FWDN の赤色インジケータが点灯します。FWDN スイッチ (SW101) を放すと、MCU は FWDN モードに移行します。  
図 4.4 に、方法 1 を使用して FWDN モードに移行する方法を示します。
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Hardware/4.4%20Entering%20FWDN%20Mode%20by%20Using%20Method%201.png"></p>
<p align="center"><strong>図 4.4 方法 1 による FWDN モードへの移行</strong><p>

#### 4.4.1.2 方法 2
VCP-G ボードが 12V 電源に接続された状態で、FWDN スイッチ (SW101) を押し、続いて RESET タクトスイッチ (SW100) を押してください。  
FWDN スイッチを押した状態で電源が投入されると、FWDN の赤色インジケータが点灯します。RESET タクトスイッチを押している間、3.3V の緑色インジケータは消灯します。FWDN スイッチ (SW101) を放すと、MCU は FWDN モードに移行します。  
図 4.5 に、方法 2 による FWDN モードを示します。

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Hardware/4.5%20Entering%20FWDN%20Mode%20by%20Using%20Method%202.png"></p>
<p align="center"><strong>図 4.5 方法 2 による FWDN モードへの移行</strong><p>

</br></br></br>

## 4.5 RESET タクトスイッチ (SW100)
---
VCP-G は、GRESETn ピンを使用する RESET 電源用の RESET スイッチを 1 つ備えています。  
図 4.6 に RESET タクトスイッチ (SW100) を示します。
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Hardware/4.6%20RESET%20Tact%20Switch%20(SW100).png"></p>
<p align="center"><strong>図 4.6 RESET タクトスイッチ (SW100)</strong><p>
</br></br>

### 4.5.1 RESET タクトスイッチ (SW100) の機能
SW100 は、VCP-G の電源ブロックとシステムブロックをリセットするためのタクトスイッチです。  
このボタンの機能は次のとおりです。
  - 電源が入っている状態で RESET タクトスイッチ (SW100) を押すと、VCP-G の電源ブロックとシステムが強制的にリセットされます。

**重要:** 電源が突然切れてデータが破損するおそれがあるため、タクトスイッチを押す際は注意してください。

</br></br></br>

## 4.6 デバッグおよび FWDN 用コネクタ (JC100)
---
JC100 は標準の USB Type-C コネクタです。VCP-G では、JC100 は UART を通じたデバッグまたは FWDN に使用されます。  
図 4.7 に JC100 の位置を示します。
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Hardware/4.7%20USB%20Type-C%20Connector%20(JC100).png"></p>
<p align="center"><strong>図 4.7 USB Type-C コネクタ (JC100)</strong><p>

JC100 を通じて VCP-G の FWDN を実行したり、デバッグメッセージを確認したりできます。
VCP-G の JC100 には USB-to-UART ブリッジコントローラが内蔵されているため、USB Type-C ケーブルを使用して JC100 を PC に直接接続できます。

</br></br></br>

## 4.7 GPIO、ADC、電源、CAN、SPI 用ピンヘッダ
---
VCP-G には、センサーやサブボードなどの他の周辺機器に接続するための電源、GPIO、ADC、CAN、SPI 用の 2.54 mm ピンヘッダが 9 個あります。  

表 4.4 に、VCP-G 上の 9 個のピンヘッダの用途を示します。
<p align="center"><strong>表 4.4 VCP-G のピンヘッダ </strong></p>
<div align="center">
	<table>
	  <tr>
	    <td colspan="4"><strong>番号</strong></td>
	    <td><strong>参照番号</strong></td>
	    <td><strong>名称</strong></td>
	    <td><strong>説明</strong></td>
	  </tr>
	  <tr>
	    <td colspan="4">1</td>
	    <td>J18D100</td>
	    <td>36 ピンメスヘッダ</td>
	    <td>GPIO および ADC 用ヘッダ</td>
	  </tr>
	  <tr>
	    <td colspan="4">2</td>
	    <td>J5D100</td>
	    <td>10 ピンオスヘッダ</td>
	    <td>CAN 用ヘッダ</td>
	  </tr>
	  <tr>
	    <td colspan="4">3</td>
	    <td>J3D100</td>
	    <td>6 ピンオスヘッダ</td>
	    <td>SPI 用ヘッダ</td>
	  </tr>
	  <tr>
	    <td colspan="4">4</td>
	    <td>J8D104</td>
	    <td>8 ピンメスヘッダ</td>
	    <td>GPIO および ADC 用ヘッダ</td>
	  </tr>
	  <tr>
	    <td colspan="4">5</td>
	    <td>J8D102</td>
	    <td>8 ピンメスヘッダ</td>
	    <td>GPIO 用ヘッダ</td>
	  </tr>
	  <tr>
	    <td colspan="4">6</td>
	    <td>J10D100</td>
	    <td>10 ピンメスヘッダ</td>
	    <td>GPIO および ADC 用ヘッダ</td>
	  </tr>
	  <tr>
	    <td colspan="4">7</td>
	    <td>J8D100</td>
	    <td>8 ピンメスヘッダ</td>
	    <td>電源およびリセット用ヘッダ</td>
	  </tr>
	  <tr>
	    <td colspan="4">8</td>
	    <td>J8D101</td>
	    <td>8 ピンメスヘッダ</td>
	    <td>GPIO および ADC 用ヘッダ</td>
	  </tr>
	  <tr>
	    <td colspan="4">9</td>
	    <td>J8D103</td>
	    <td>8 ピンメスヘッダ</td>
	    <td>GPIO および ADC 用ヘッダ</td>
	  </tr>
	</table>
</div>

図 4.8 は VCP-G のピンヘッダの位置を示します。
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Hardware/4.8%20Pin%20Headers%20on%20TOPST%20VCP-G%20Board.png"></p>
<p align="center"><strong>図 4.8 VCP-G のピンヘッダ </strong><p>

表 4.5 は J10D100 のピン説明を示します。
<p align="center"><strong>表 4.5 J10D100 ピン説明</strong></p>
<div align="center">
	<table>
	  <tr>
	    <th rowspan="3"><strong>ピン番号</strong></th>
	    <th colspan="4"><strong>J10D100</strong></th>
	  </tr>
	  <tr>
	    <th rowspan="2"><strong>ポート名</strong></th>
	    <th rowspan="2"><strong>信号名</strong></th>
	    <th><strong>DIR</strong></th>
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
	    <td>GPIO または ADC 信号</td>
	  </tr>
	  <tr>
	    <td>2</td>
	    <td>SDA</td>
	    <td>GPIO_AC06</td>
	    <td>◄►</td>
	    <td>GPIO または ADC 信号</td>
	  </tr>
	  <tr>
	    <td>3</td>
	    <td>AREF</td>
	    <td>ADC06</td>
	    <td>◄</td>
	    <td>ADC 信号</td>
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
	    <td>GPIO 信号</td>
	  </tr>
	  <tr>
	    <td>6</td>
	    <td>12</td>
	    <td>GPIO_C15</td>
	    <td>◄►</td>
	    <td>GPIO 信号</td>
	  </tr>
	  <tr>
	    <td>7</td>
	    <td>11</td>
	    <td>GPIO_C14</td>
	    <td>◄►</td>
	    <td>GPIO 信号</td>
	  </tr>
	  <tr>
	    <td>8</td>
	    <td>10</td>
	    <td>GPIO_C13</td>
	    <td>◄►</td>
	    <td>GPIO 信号</td>
	  </tr>
	  <tr>
	    <td>9</td>
	    <td>9</td>
	    <td>GPIO_A12</td>
	    <td>◄►</td>
	    <td>GPIO 信号</td>
	  </tr>
	  <tr>
	    <td>10</td>
	    <td>8</td>
	    <td>GPIO_B00</td>
	    <td>◄►</td>
	    <td>GPIO 信号</td>
	  </tr>
	</table>
</div>

表 4.6 は J8D100 のピン説明を示します。
<p align="center"><strong>表 4.6 J8D100 ピン説明</strong></p>
<div align="center">
	<table>
	  <tr>
	    <th rowspan="3"><strong>ピン番号</strong></th>
	    <th colspan="4"><strong>J8D100</strong></th>
	  </tr>
	  <tr>
	    <th rowspan="2"><strong>ポート名</strong></th>
	    <th rowspan="2"><strong>信号名</strong></th>
	    <th><strong>DIR</strong></th>
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
	    <td>VCP-G 用の電圧入力</td>
	  </tr>
	</table>
</div>

表 4.7 は J8D101 のピン説明を示します。
<p align="center"><strong>表 4.7 J8D101 ピン説明</strong></p>
<div align="center">
	<table>
	  <tr>
	    <th rowspan="3"><strong>ピン番号</strong></th>
	    <th colspan="4"><strong>J8D101</strong></th>
	  </tr>
	  <tr>
	    <th rowspan="2"><strong>ポート名</strong></th>
	    <th rowspan="2"><strong>信号名</strong></th>
	    <th><strong>DIR</strong></th>
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
	    <td>ADC 信号</td>
	  </tr>
	  <tr>
	    <td>2</td>
	    <td>A1</td>
	    <td>ADC04</td>
	    <td>◄</td>
	    <td>ADC 信号</td>
	  </tr>
	  <tr>
	    <td>3</td>
	    <td>A2</td>
	    <td>GPIO_AC02</td>
	    <td>◄►</td>
	    <td>GPIO 信号</td>
	  </tr>
	  <tr>
	    <td>4</td>
	    <td>A3</td>
	    <td>GPIO_AC03</td>
	    <td>◄►</td>
	    <td>GPIO 信号</td>
	  </tr>
	  <tr>
	    <td>5</td>
	    <td>A4</td>
	    <td>GPIO_AC05</td>
	    <td>◄►</td>
	    <td>GPIO 信号</td>
	  </tr>
	  <tr>
	    <td>6</td>
	    <td>A5</td>
	    <td>GPIO_AC04</td>
	    <td>◄►</td>
	    <td>GPIO 信号</td>
	  </tr>
	  <tr>
	    <td>7</td>
	    <td>A6</td>
	    <td>ADC05</td>
	    <td>◄</td>
	    <td>ADC 信号</td>
	  </tr>
	  <tr>
	    <td>8</td>
	    <td>A7</td>
	    <td>ADC01</td>
	    <td>◄</td>
	    <td>ADC 信号</td>
	  </tr>
	</table>
</div>

表 4.8 は J8D102 のピン説明を示します。
<p align="center"><strong>表 4.8 J8D102 ピン説明</strong></p>
<div align="center">
	<table>
	  <tr>
	    <th rowspan="3"><strong>ピン番号</strong></th>
	    <th colspan="4"><strong>J8D102</strong></th>
	  </tr>
	  <tr>
	    <th rowspan="2"><strong>ポート名</strong></th>
	    <th rowspan="2"><strong>信号名</strong></th>
	    <th><strong>DIR</strong></th>
	    <th rowspan="2"><strong>説明</strong></th>
	  </tr>
	  <tr>
	    <th><strong>MCU ◄► J8D102</strong></th>
	  </tr>
	  <tr>
	    <td>1</td>
	    <td>7</td>
	    <td>GPIO_B01</td>
	    <td>◄►</td>
	    <td>GPIO 信号</td>
	  </tr>
	  <tr>
	    <td>2</td>
	    <td>6</td>
	    <td>GPIO_A13</td>
	    <td>◄►</td>
	    <td>GPIO 信号</td>
	  </tr>
	  <tr>
	    <td>3</td>
	    <td>5</td>
	    <td>GPIO_B10</td>
	    <td>◄►</td>
	    <td>GPIO 信号</td>
	  </tr>
	  <tr>
	    <td>4</td>
	    <td>4</td>
	    <td>GPIO_B27</td>
	    <td>◄►</td>
	    <td>GPIO 信号</td>
	  </tr>
	  <tr>
	    <td>5</td>
	    <td>3</td>
	    <td>GPIO_B11</td>
	    <td>◄►</td>
	    <td>GPIO 信号</td>
	  </tr>
	  <tr>
	    <td>6</td>
	    <td>2</td>
	    <td>GPIO_B28</td>
	    <td>◄►</td>
	    <td>GPIO 信号</td>
	  </tr>
	  <tr>
	    <td>7</td>
	    <td>1</td>
	    <td>GPIO_B25</td>
	    <td>◄►</td>
	    <td>GPIO 信号</td>
	  </tr>
	  <tr>
	    <td>8</td>
	    <td>0</td>
	    <td>GPIO_B26</td>
	    <td>◄►</td>
	    <td>GPIO 信号</td>
	  </tr>
	</table>
</div>

表 4.9 は J8D103 のピン説明を示します。
<p align="center"><strong>表 4.9 J8D103 ピン説明</strong></p>
<div align="center">
	<table>
	  <tr>
	    <th rowspan="3"><strong>ピン番号</strong></th>
	    <th colspan="4"><strong>J8D103</strong></th>
	  </tr>
	  <tr>
	    <th rowspan="2"><strong>ポート名</strong></th>
	    <th rowspan="2"><strong>信号名</strong></th>
	    <th><strong>DIR</strong></th>
	    <th rowspan="2"><strong>説明</strong></th>
	  </tr>
	  <tr>
	    <th><strong>MCU ◄► J8D103</strong></th>
	  </tr>
	  <tr>
	    <td>1</td>
	    <td>A8</td>
	    <td>GPIO_AC08</td>
	    <td>◄►</td>
	    <td>GPIO または ADC 信号</td>
	  </tr>
	  <tr>
	    <td>2</td>
	    <td>A9</td>
	    <td>GPIO_AC09</td>
	    <td>◄►</td>
	    <td>GPIO または ADC 信号</td>
	  </tr>
	  <tr>
	    <td>3</td>
	    <td>A10</td>
	    <td>GPIO_AC10</td>
	    <td>◄►</td>
	    <td>GPIO または ADC 信号</td>
	  </tr>
	  <tr>
	    <td>4</td>
	    <td>A11</td>
	    <td>GPIO_ADC-2</td>
	    <td>◄</td>
	    <td>ADC 信号</td>
	  </tr>
	  <tr>
	    <td>5</td>
	    <td>54</td>
	    <td>GPIO_K14</td>
	    <td>◄►</td>
	    <td>GPIO 信号</td>
	  </tr>
	  <tr>
	    <td>6</td>
	    <td>55</td>
	    <td>GPIO_K15</td>
	    <td>◄►</td>
	    <td>GPIO 信号</td>
	  </tr>
	  <tr>
	    <td>7</td>
	    <td>56</td>
	    <td>GPIO_K01</td>
	    <td>◄</td>
	    <td>GPIO 信号</td>
	  </tr>
	  <tr>
	    <td>8</td>
	    <td>57</td>
	    <td>GPIO_K08</td>
	    <td>◄►</td>
	    <td>GPIO 信号</td>
	  </tr>
	</table>
</div>

表 4.10 は J8D104 のピン説明を示します。
<p align="center"><strong>表 4.10 J8D104 ピン説明</strong></p>
<div align="center">
	<table>
	  <tr>
	    <th rowspan="3"><strong>ピン番号</strong></th>
	    <th colspan="4"><strong>J8D104</strong></th>
	  </tr>
	  <tr>
	    <th rowspan="2"><strong>ポート名</strong></th>
	    <th rowspan="2"><strong>信号名</strong></th>
	    <th><strong>DIR</strong></th>
	    <th rowspan="2"><strong>説明</strong></th>
	  </tr>
	  <tr>
	    <th><strong>MCU ◄► J8D104</strong></th>
	  </tr>
	  <tr>
	    <td>1</td>
	    <td>14</td>
	    <td>GPIO_AC00</td>
	    <td>◄►</td>
	    <td>GPIO または ADC 信号</td>
	  </tr>
	  <tr>
	    <td>2</td>
	    <td>15</td>
	    <td>GPIO_AC01</td>
	    <td>◄►</td>
	    <td>GPIO または ADC 信号</td>
	  </tr>
	  <tr>
	    <td>3</td>
	    <td>16</td>
	    <td>GPIO_A06</td>
	    <td>◄►</td>
	    <td>GPIO 信号</td>
	  </tr>
	  <tr>
	    <td>4</td>
	    <td>17</td>
	    <td>GPIO_A07</td>
		<td>◄►</td>
	    <td>GPIO 信号</td>
	  </tr>
	  <tr>
	    <td>5</td>
	    <td>18</td>
	    <td>GPIO_A28</td>
	    <td>◄►</td>
	    <td>GPIO 信号</td>
	  </tr>
	  <tr>
	    <td>6</td>
	    <td>19</td>
	    <td>GPIO_A29</td>
	    <td>◄►</td>
	    <td>GPIO 信号</td>
	  </tr>
	  <tr>
	    <td>7</td>
	    <td>20</td>
	    <td>GPIO_B03</td>
	    <td>◄►</td>
	    <td>GPIO 信号</td>
	  </tr>
	  <tr>
	    <td>8</td>
	    <td>21</td>
	    <td>GPIO_B02</td>
	    <td>◄►</td>
	    <td>GPIO 信号</td>
	  </tr>
	</table>
</div>

表 4.11 は J3D100 のピン説明を示します。
<p align="center"><strong>表 4.11 J3D100 ピン説明</strong></p>
<div align="center">
	<table>
	  <tr>
	    <th rowspan="3"><strong>ピン番号</strong></th>
	    <th colspan="4"><strong>J3D100</strong></th>
	  </tr>
	  <tr>
	    <th rowspan="2"><strong>ポート名</strong></th>
	    <th rowspan="2"><strong>信号名</strong></th>
	    <th><strong>DIR</strong></th>
	    <th rowspan="2"><strong>説明</strong></th>
	  </tr>
	  <tr>
	    <th><strong>MCU ◄► J3D100</strong></th>
	  </tr>
	  <tr>
	    <td>1</td>
	    <td>MISO</td>
	    <td>GPIO_B07</td>
	    <td>◄►</td>
	    <td>GPIO 信号</td>
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
	    <td>SCK</td>
	    <td>GPIO_B04</td>
	    <td>◄►</td>
	    <td>GPIO 信号</td>
	  </tr>
	  <tr>
	    <td>4</td>
	    <td>MOSI</td>
	    <td>GPIO_B06</td>
	    <td>◄►</td>
	    <td>GPIO 信号</td>
	  </tr>
	  <tr>
	    <td>5</td>
	    <td>CMD</td>
	    <td>GPIO_B05</td>
	    <td>◄►</td>
	    <td>GPIO 信号</td>
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

表 4.12 は J18D100 のピン説明を示します。
<p align="center"><strong>表 4.12 J18D100 ピン説明</strong></p>
<div align="center">
	<table>
	  <tr>
	    <th rowspan="3"><strong>ピン番号</strong></th>
	    <th colspan="4"><strong>J18D100</strong></th>
	  </tr>
	  <tr>
	    <th rowspan="2"><strong>ポート名</strong></th>
	    <th rowspan="2"><strong>信号名</strong></th>
	    <th><strong>DIR</strong></th>
	    <th rowspan="2"><strong>説明</strong></th>
	  </tr>
	  <tr>
	    <th><strong>MCU ◄► J18D100</strong></th>
	  </tr>
	  <tr>
	    <td>1</td>
	    <td>5V</td>
	    <td>VCP_5P0</td>
	    <td>-</td>
	    <td>電源 5.0V</td>
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
	    <td>GPIO_B24</td>
	    <td>◄►</td>
	    <td>GPIO 信号</td>
	  </tr>
	  <tr>
	    <td>4</td>
	    <td>23</td>
	    <td>GPIO_B23</td>
	    <td>◄►</td>
	    <td>GPIO 信号</td>
	  </tr>
	  <tr>
	    <td>5</td>
	    <td>24</td>
	    <td>GPIO_B22</td>
	    <td>◄►</td>
	    <td>GPIO 信号</td>
	  </tr>
	  <tr>
	    <td>6</td>
	    <td>25</td>
	    <td>GPIO_B21</td>
	    <td>◄►</td>
	    <td>GPIO 信号</td>
	  </tr>
	  <tr>
	    <td>7</td>
	    <td>26</td>
	    <td>GPIO_B20</td>
	    <td>◄►</td>
	    <td>GPIO 信号</td>
	  </tr>
	  <tr>
	    <td>8</td>
	    <td>27</td>
	    <td>GPIO_B19</td>
	    <td>◄►</td>
	    <td>GPIO 信号</td>
	  </tr>
	  <tr>
	    <td>9</td>
	    <td>28</td>
	    <td>GPIO_A30</td>
	    <td>◄►</td>
	    <td>GPIO 信号</td>
	  </tr>
	  <tr>
	    <td>10</td>
	    <td>29</td>
	    <td>GPIO_A27</td>
	    <td>◄►</td>
	    <td>GPIO 信号</td>
	  </tr>
	  <tr>
	    <td>11</td>
	    <td>230</td>
	    <td>GPIO_A26</td>
	    <td>◄►</td>
	    <td>GPIO 信号</td>
	  </tr>
	  <tr>
	    <td>12</td>
	    <td>31</td>
	    <td>GPIO_A24</td>
	    <td>◄►</td>
	    <td>GPIO 信号</td>
	  </tr>
	  <tr>
	    <td>13</td>
	    <td>32</td>
	    <td>GPIO_A25</td>
	    <td>◄►</td>
	    <td>GPIO 信号</td>
	  </tr>
	  <tr>
	    <td>14</td>
	    <td>33</td>
	    <td>GPIO_A23</td>
	    <td>◄►</td>
	    <td>GPIO 信号</td>
	  </tr>
	  <tr>
	    <td>15</td>
	    <td>34</td>
	    <td>GPIO_A22</td>
	    <td>◄►</td>
	    <td>GPIO 信号</td>
	  </tr>
	  <tr>
	    <td>16</td>
	    <td>35</td>
	    <td>GPIO_A21</td>
	    <td>◄►</td>
		<td>GPIO 信号</td>
	  </tr>
	  <tr>
	    <td>17</td>
	    <td>36</td>
	    <td>GPIO_A20</td>
	    <td>◄►</td>
	    <td>GPIO 信号</td>
	  </tr>
	  <tr>
	    <td>18</td>
	    <td>37</td>
	    <td>GPIO_A19</td>
	    <td>◄►</td>
	    <td>GPIO 信号</td>
	  </tr>
	  <tr>
	    <td>19</td>
	    <td>38</td>
	    <td>GPIO_K13</td>
	    <td>◄►</td>
		<td>GPIO 信号</td>
	  </tr>
	  <tr>
	    <td>20</td>
	    <td>39</td>
	    <td>GPIO_K12</td>
	    <td>◄►</td>
	    <td>GPIO 信号</td>
	  </tr>
	  <tr>
	    <td>21</td>
	    <td>40</td>
	    <td>GPIO_K11</td>
	    <td>◄►</td>
	    <td>GPIO 信号</td>
	  </tr>
	  <tr>
	    <td>22</td>
	    <td>41</td>
	    <td>GPIO_A18</td>
	    <td>◄►</td>
	    <td>GPIO 信号</td>
	  </tr>
	  <tr>
	    <td>23</td>
	    <td>42</td>
	    <td>GPIO_A17</td>
	    <td>◄►</td>
	    <td>GPIO 信号</td>
	  </tr>
	  <tr>
	    <td>24</td>
	    <td>43</td>
	    <td>GPIO_A16</td>
	    <td>◄►</td>
	    <td>GPIO 信号</td>
	  </tr>
	  <tr>
	    <td>25</td>
	    <td>44</td>
	    <td>GPIO_A11</td>
	    <td>◄►</td>
	    <td>GPIO 信号</td>
	  </tr>
	  <tr>
	    <td>26</td>
	    <td>45</td>
	    <td>GPIO_A10</td>
	    <td>◄►</td>
	    <td>GPIO 信号</td>
	  </tr>
	  <tr>
	    <td>27</td>
	    <td>46</td>
	    <td>GPIO_A09</td>
	    <td>◄►</td>
	    <td>GPIO 信号</td>
	  </tr>
	  <tr>
	    <td>28</td>
	    <td>47</td>
	    <td>GPIO_A08</td>
	    <td>◄►</td>
	    <td>GPIO 信号</td>
	  </tr>
	  <tr>
	    <td>29</td>
	    <td>48</td>
	    <td>GPIO_A05</td>
	    <td>◄►</td>
	    <td>GPIO 信号</td>
	  </tr>
	  <tr>
	    <td>30</td>
	    <td>49</td>
	    <td>GPIO_A04</td>
	    <td>◄►</td>
	    <td>GPIO 信号</td>
	  </tr>
	  <tr>
	    <td>31</td>
	    <td>50</td>
	    <td>GPIO_A03</td>
	    <td>◄►</td>
	    <td>GPIO 信号</td>
	  </tr>
	  <tr>
	    <td>32</td>
	    <td>51</td>
	    <td>GPIO_A02</td>
	    <td>◄►</td>
	    <td>GPIO 信号</td>
	  </tr>
	  <tr>
	    <td>33</td>
	    <td>52</td>
	    <td>GPIO_A01</td>
	    <td>◄►</td>
	    <td>GPIO 信号</td>
	  </tr>
	  <tr>
	    <td>34</td>
	    <td>53</td>
	    <td>GPIO_A00</td>
	    <td>◄►</td>
	    <td>GPIO 信号</td>
	  </tr>
	  <tr>
	    <td>35</td>
	    <td>GND</td>
	    <td>DGND</td>
	    <td>-</td>
	    <td>グラウンド</td>
	  </tr>
	  <tr>
	    <td>36</td>
	    <td>GND</td>
	    <td>DGND</td>
	    <td>-</td>
	    <td>グラウンド</td>
	  </tr>
	</table>
</div>

表 4.13 は J5D100 のピン説明を示します。
<p align="center"><strong>表 4.13 J5D100 ピン説明</strong></p>
<div align="center">
	<table>
	  <tr>
	    <th rowspan="3"><strong>ピン番号</strong></th>
	    <th colspan="4"><strong>J5D100</strong></th>
	  </tr>
	  <tr>
	    <th rowspan="2"><strong>ポート名</strong></th>
	    <th rowspan="2"><strong>信号名</strong></th>
	    <th><strong>DIR</strong></th>
	    <th rowspan="2"><strong>説明</strong></th>
	  </tr>
	  <tr>
	    <th><strong>MCU ◄► J5D100</strong></th>
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
	    <td>3.3V</td>
	    <td>VCP_3P3</td>
	    <td>-</td>
    <td>電源 3.3V</td>
	  </tr>
	  <tr>
	    <td>3</td>
	    <td>TX0</td>
	    <td>GPIO_K08</td>
	    <td>◄►</td>
	    <td>GPIO 信号</td>
	  </tr>
	  <tr>
	    <td>4</td>
	    <td>RX0</td>
	    <td>GPIO_K01</td>
	    <td>◄</td>
	    <td>GPIO 信号</td>
	  </tr>
	  <tr>
	    <td>5</td>
	    <td>TX1</td>
	    <td>GPIO_K09</td>
	    <td>◄►</td>
	    <td>GPIO 信号</td>
	  </tr>
	  <tr>
	    <td>6</td>
	    <td>RX1</td>
	    <td>GPIO_K02</td>
	    <td>◄</td>
	    <td>GPIO 信号</td>
	  </tr>
	  <tr>
	    <td>7</td>
	    <td>TX2</td>
	    <td>GPIO_K10</td>
	    <td>◄►</td>
	    <td>GPIO 信号</td>
	  </tr>
	  <tr>
	    <td>8</td>
	    <td>RX2</td>
	    <td>GPIO_K03</td>
	    <td>◄</td>
	    <td>GPIO 信号</td>
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

図 4.9 は VCP-G にある 10 個のピンヘッダの全ピン割り当てを示します。
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Hardware/4.9%20Total%20Pin%20Assignment%20of%20Pin%20Headers%20on%20TOPST%20VCP-G%20Board.png"></p>
<p align="center"><strong>図 4.9 VCP-G のピンヘッダの全ピン割り当て </strong><p>

# 参考資料
  - 詳細については TOPST にお問い合わせください: topst@topst.ai

**注:** 参考資料は、契約条件に応じて、提供可能な場合に提供されます。参考資料を提供できない場合は、お客様の開発に直接関連する内容をご案内いたします。
