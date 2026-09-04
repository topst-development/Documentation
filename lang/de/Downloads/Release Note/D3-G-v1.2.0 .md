# D3-G Versionshinweise - v1.2.0

## Aktualisierte Repositorys
- [vpu-kernel-library](https://github.com/topst-development/vpu-kernel-library/tree/release/1.2.0-r01)
- [kernel-5.10](https://github.com/topst-development/kernel-5.10/tree/release/d3/1.2.0)
- [meta-topst](https://github.com/topst-development/meta-topst/tree/release/1.2.0)
- [meta-topst-bsp](https://github.com/topst-development/meta-topst-bsp/tree/release/1.2.0)
- [manifests](https://github.com/topst-development/manifests/tree/release/1.2.0)

## Neue Funktionen
- VPU-AVC Encoder/Decoder können über gstreamer genutzt werden
- VPU-VP9 Decoder kann über gstreamer genutzt werden

## Verbesserung
- VPU-Encoder unterstützen die Kodierung von Inhalten in 4K


## Bekannte Probleme
- Ein Warmstart dauert gelegentlich lange (etwa 40 Sekunden), wenn eine SD-Karte eingesteckt ist.
- Eine über MIPI angeschlossene externe Kamera unterstützt derzeit bis zu 30fps (in der nächsten Version werden bis zu 60fps unterstützt)

## Anleitungen
- VLC Player
    - Vor der Wiedergabe von Inhalten muss die Videoausgabe in den Eigenschaftseinstellungen auf **'X11 video output(XCB)'** gesetzt werden.
- firefox
	- Installieren Sie Firefox bei Bedarf mit 'sudo apt install --reinstall firefox' neu.

## Anhang.
<p align="center"><strong>Tabelle 1.1 USB-Bluetooth-Dongles</strong></p>
<div align="center">
	<table>
	  <tr>
	    <td><strong>Herstellername</strong></td>
	    <td><strong>Chipsatzname</strong></td>
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


<p align="center"><strong>Tabelle 1.2 USB-WLAN-Dongles</strong></p>
<div align="center">
	<table>
	  <tr>
	    <td><strong>Herstellername</strong></td>
	    <td><strong>Chipsatzname</strong></td>
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
