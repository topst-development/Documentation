# D3-G 版本資訊 - v1.1.0

## 已更新的儲存庫
- [kernel-5.10](https://github.com/topst-development/kernel-5.10/tree/release/d3/1.1.0)
- [meta-topst](https://github.com/topst-development/meta-topst/tree/release/1.1.0)
- [meta-topst-bsp](https://github.com/topst-development/meta-topst-bsp/tree/release/1.1.0)
- [tools](https://github.com/topst-development/tools/tree/release/1.1.0)
- [manifests](https://github.com/topst-development/manifests/tree/release/1.1.0)

## 新功能
- 現已支援 Ubuntu Gnome Desktop。
- VPU-HEVC 編碼器/解碼器可透過 gstreamer 使用
- 已啟用的核心功能
    - 適用於 docker 的 netfilter
    - 交換分割區
    - USB wifi 傳輸器驅動程式
    - USB BT 傳輸器驅動程式
 
## 改善項目
- 已針對 PCIe 資料傳輸調整高速 IO 匯流排的 outstanding 參數。

## 錯誤修正
- PowerVR GPU 驅動程式的記憶體洩漏

## 已知問題
- VPU-HEVC 編碼器尚未支援將內容編碼為 4K（將於下一版本支援）
- 插入 sdcard 時，暖開機有時會花費較長時間（約 40 秒）。
- 連接至 MIPI 的外接攝影機目前最高支援 30fps（將於下一版本支援至 60fps）

## 指南
- VLC Player
    - 播放內容前，應於屬性設定中將視訊輸出設為 **'X11 video output(XCB)'**。
- firefox
	- 如有需要，請以 'sudo apt install --reinstall firefox' 重新安裝 Firefox。

## 附錄
<p align="center"><strong>表 1.1 USB 藍牙傳輸器</strong></p>
<div align="center">
	<table>
	  <tr>
	    <td><strong>製造商名稱</strong></td>
	    <td><strong>晶片組名稱</strong></td>
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


<p align="center"><strong>表 1.2 USB Wifi 傳輸器</strong></p>
<div align="center">
	<table>
	  <tr>
	    <td><strong>製造商名稱</strong></td>
	    <td><strong>晶片組名稱</strong></td>
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
