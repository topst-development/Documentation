# D3-G リリースノート - v1.1.0

## 更新されたリポジトリ
- [kernel-5.10](https://github.com/topst-development/kernel-5.10/tree/release/d3/1.1.0)
- [meta-topst](https://github.com/topst-development/meta-topst/tree/release/1.1.0)
- [meta-topst-bsp](https://github.com/topst-development/meta-topst-bsp/tree/release/1.1.0)
- [tools](https://github.com/topst-development/tools/tree/release/1.1.0)
- [manifests](https://github.com/topst-development/manifests/tree/release/1.1.0)

## 新機能
- Ubuntu Gnome Desktop に対応しました。
- VPU-HEVC エンコーダ/デコーダを gstreamer で利用できます
- 有効化されたカーネル機能
    - docker 用 netfilter
    - スワップパーティション
    - USB wifi ドングルドライバ
    - USB BT ドングルドライバ
 
## 改善
- PCIe のデータ転送のため、高速 IO バスの outstanding パラメータを調整しました。

## バグ修正
- PowerVR GPU ドライバのメモリリーク

## 既知の問題
- VPU-HEVC エンコーダはコンテンツを 4K にエンコードする機能にまだ対応していません（次回リリースで対応予定）
- sdcard が挿入されている場合、ウォームリブートに長い時間（約 40 秒）がかかることがあります。
- MIPI に接続された外部カメラは、現時点では最大 30fps まで対応しています（次回リリースで最大 60fps に対応予定）

## ガイド
- VLC Player
    - コンテンツを再生する前に、プロパティ設定でビデオ出力を **'X11 video output(XCB)'** に設定してください。
- firefox
	- 必要に応じて 'sudo apt install --reinstall firefox' で Firefox を再インストールしてください。

## 付録.
<p align="center"><strong>表 1.1 USB Bluetooth ドングル</strong></p>
<div align="center">
	<table>
	  <tr>
	    <td><strong>メーカー名</strong></td>
	    <td><strong>チップセット名</strong></td>
	  </tr>
	  <tr>
	    <td rowspan="16">RealTek</td>
        <td>rtl8192</td>
	  </tr>
	  <tr>
	    <td>rtl8723</td>
	  </tr>
      <tr>
	    <td>rtl8761a</td>
	  </tr>
      <tr>
	    <td>rtl8761b</td>
	  </tr>
      <tr>
	    <td>rtl8761bu</td>
	  </tr>
      <tr>
	    <td>rtl8812ae</td>
	  </tr>
      <tr>
	    <td>rtl8821a</td>
	  </tr>
      <tr>
	    <td>rtl8821c</td>
	  </tr>
      <tr>
	    <td>rtl8821cs</td>
	  </tr>
      <tr>
	    <td>rtl8822b</td>
	  </tr>
      <tr>
	    <td>rtl8822cs</td>
	  </tr>
      <tr>
	    <td>rtl8822cu</td>
	  </tr>
      <tr>
	    <td>rtl8851bu</td>
	  </tr>
      <tr>
	    <td>rtl8852au</td>
	  </tr>
      <tr>
	    <td>rtl8852bu</td>
	  </tr>
      <tr>
	    <td>rtl8852cu</td>
	  </tr>
      <tr>
        <td>MediaTek</td>
        <td>MT763F</td>
      </tr>
      <tr>
        <td rowspan="3">Broadcom</td>
        <td>bcm2070x</td>
      </tr>
      <tr>
	    <td>bcm4365</td>
	  </tr>
      <tr>
	    <td>bcm4345</td>
	  </tr>
      <tr>
        <td rowspan="3">Intel</td>
        <td>Wireless-AC 7260</td>
      </tr>
      <tr>
	    <td>Wireless-AC 3160</td>
	  </tr>
      <tr>
	    <td>Wireless-AC 8260</td>
	  </tr>
    </table>
</div>  


<p align="center"><strong>表 1.2 USB Wifi ドングル</strong></p>
<div align="center">
	<table>
	  <tr>
	    <td><strong>メーカー名</strong></td>
	    <td><strong>チップセット名</strong></td>
	  </tr>
	  <tr>
	    <td>RealTek</td>
        <td>rtl88x2bu (8812bu, 8822bu)</td>
	  </tr>
	  <tr>
	    <td>MediaTek</td>
        <td>MT7601U</td>
	  </tr>
    </table>
</div>
