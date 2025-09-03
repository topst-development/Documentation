# D3G Release Note - v1.1.0

## New Features
- Ubuntu Gnome Desktop is enabled.
- VPU-HEVC encoder/decoder can be utilized by gstreamer
- Activated Kernel features
    - netfilter for docker
    - swap partition
    - USB wifi dongle drivers
    - USB BT dongle drivers

## Improvement
- High-speed IO bus outstanding param has been adjusted for PCIe data transfer.

## Bug Fixes
- Memory Leakage from PowerVR GPU Driver

## Known Issues
- VPU-HEVC encoder doesn't support encoding content into 4K yet (will support in the next release)
- warm reboot takes long (around 40 seconds) from time to time when sdcard is inserted.
- external camera, connected to MIPI, supports up to 30fps for now (will support up to 60fps in the next release)

## Guides
- VLC Player
    - video output should be set to **'X11 video output(XCB)'** in property settings before playing contents.

## Appendix.
<p align="center"><strong>Table 1.1 USB Bluetooth dongles</strong></p>
<div align="center">
	<table>
	  <tr>
	    <td><strong>Manufacturer Name</strong></td>
	    <td><strong>Chipset Name</strong></td>
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


<p align="center"><strong>Table 1.2 USB Wifi dongles</strong></p>
<div align="center">
	<table>
	  <tr>
	    <td><strong>Manufacturer Name</strong></td>
	    <td><strong>Chipset Name</strong></td>
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
