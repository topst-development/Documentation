# D3-G 发行说明 - v1.1.0

## 已更新的仓库
- [kernel-5.10](https://github.com/topst-development/kernel-5.10/tree/release/d3/1.1.0)
- [meta-topst](https://github.com/topst-development/meta-topst/tree/release/1.1.0)
- [meta-topst-bsp](https://github.com/topst-development/meta-topst-bsp/tree/release/1.1.0)
- [tools](https://github.com/topst-development/tools/tree/release/1.1.0)
- [manifests](https://github.com/topst-development/manifests/tree/release/1.1.0)

## 新增功能
- 现已支持 Ubuntu Gnome Desktop。
- VPU-HEVC 编码器/解码器可通过 gstreamer 使用
- 已启用的内核功能
    - 用于 docker 的 netfilter
    - 交换分区
    - USB wifi 适配器驱动程序
    - USB BT 适配器驱动程序
 
## 改进
- 针对 PCIe 数据传输，已调整高速 IO 总线的 outstanding 参数。

## 缺陷修复
- PowerVR GPU 驱动程序的内存泄漏

## 已知问题
- VPU-HEVC 编码器尚不支持将内容编码为 4K（将在下一版本中支持）
- 插入 sdcard 时，热重启有时需要较长时间（约 40 秒）。
- 连接到 MIPI 的外部摄像头目前最高支持 30fps（将在下一版本中支持最高 60fps）

## 指南
- VLC Player
    - 播放内容前，应在属性设置中将视频输出设置为 **'X11 video output(XCB)'**。
- firefox
	- 如有需要，请使用 'sudo apt install --reinstall firefox' 重新安装 Firefox。

## 附录.
<p align="center"><strong>表 1.1 USB Bluetooth 适配器</strong></p>
<div align="center">
	<table>
	  <tr>
	    <td><strong>制造商名称</strong></td>
	    <td><strong>芯片组名称</strong></td>
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


<p align="center"><strong>表 1.2 USB Wifi 适配器</strong></p>
<div align="center">
	<table>
	  <tr>
	    <td><strong>制造商名称</strong></td>
	    <td><strong>芯片组名称</strong></td>
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
