# D3-G 릴리스 노트 - v1.2.0

## 업데이트된 저장소
- [vpu-kernel-library](https://github.com/topst-development/vpu-kernel-library/tree/release/1.2.0-r01)
- [kernel-5.10](https://github.com/topst-development/kernel-5.10/tree/release/d3/1.2.0)
- [meta-topst](https://github.com/topst-development/meta-topst/tree/release/1.2.0)
- [meta-topst-bsp](https://github.com/topst-development/meta-topst-bsp/tree/release/1.2.0)
- [manifests](https://github.com/topst-development/manifests/tree/release/1.2.0)

## 신규 기능
- VPU-AVC 인코더/디코더를 gstreamer에서 사용할 수 있습니다
- VPU-VP9 디코더를 gstreamer에서 사용할 수 있습니다

## 개선 사항
- VPU 인코더가 콘텐츠를 4K로 인코딩하는 것을 지원합니다


## 알려진 이슈
- sdcard가 삽입되어 있는 경우 웜 리부트에 간혹 오랜 시간(약 40초)이 소요됩니다.
- MIPI에 연결된 외부 카메라는 현재 최대 30fps까지 지원합니다(다음 릴리스에서 최대 60fps를 지원할 예정입니다)

## 가이드
- VLC Player
    - 콘텐츠를 재생하기 전에 속성 설정에서 video output을 **'X11 video output(XCB)'** 로 설정해야 합니다.
- firefox
	- 필요한 경우 'sudo apt install --reinstall firefox' 명령으로 Firefox를 다시 설치하십시오.

## 부록.
<p align="center"><strong>표 1.1 USB Bluetooth 동글</strong></p>
<div align="center">
	<table>
	  <tr>
	    <td><strong>제조사 이름</strong></td>
	    <td><strong>칩셋 이름</strong></td>
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


<p align="center"><strong>표 1.2 USB Wifi 동글</strong></p>
<div align="center">
	<table>
	  <tr>
	    <td><strong>제조사 이름</strong></td>
	    <td><strong>칩셋 이름</strong></td>
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
