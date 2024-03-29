# Firmware Download

This chapter describes how to download FWDN to the TOPST AI (Open
platform board) and log in the Linux console.

## Fimeware Dowload Sequence

The downloading sequence of FWDN is as follows:

1.  Set the boot mode switch to fwdn boot mode.

2.  Open Windows prompt and test FWDN ND.

3.  Connect FWDN ND to board.

4.  Download fai file.

## Connect TOPST AI and Host PC with Fwdn Boot

You can transfer the built image to TCC750x using FWDN.

TCC750x provides FWDN function by using the ethernet and UART.

<img src="https://github.com/topst-development/Documentation/blob/main/TOPST-AI/Software/media/Firmware Download.image1.png"
style="width:2.21806in;height:2.80208in"
alt="텍스트, 도표, 폰트, 라인이(가) 표시된 사진 자동 생성된 설명" />

Figure 1.1 Connection between Host PC and TOPST AI for FWDN

### Setting Environment for Host PC

Refer to chapter 3. FWDN in the 'TOST-AI-Common-SW-SDK-Getting Started'
document

for detailed configuration settings for FWDN.

### Connect Ethernet and Uart Port Between TOPST AI And Host PC

To download firmware to TEST AI, you must connect between TEST AI and
Host PC using Ethernet and USB A-to-C cables respectively

<img src="https://github.com/topst-development/Documentation/blob/main/TOPST-AI/Software/media/Firmware Download.image2.png"
style="width:2.71875in;height:4.06605in"
alt="전자제품, 전자 공학, 전자 부품, 회로 구성요소이(가) 표시된 사진 자동 생성된 설명" />

Figure 1.2 Connect Port Between TOPST AI And Host PC

### Change Boot Mode

If you press boot mode switch and supply power, the FWDN boot process is
initiated. If you supply power without pressing boot mode switch, the
normal boot process is initiated.

Pressing reset switch causes the system to reset. If you want to
download a firmware, press boot mode switch and reset switch at the same
time to FWDN boot mode.

> <img src="https://github.com/topst-development/Documentation/blob/main/TOPST-AI/Software/media/Firmware Download.image3.jpeg"
> style="width:3.76534in;height:1.76042in" />
>
> Figure 1.3 Boot Mode Switch

### FWDN in Windows

1.  After image build, copy the created fwdn folder to the desktop, and
    save the file below inside the folder.

- fwdn_nd.exe (copy from ~/\<Topst SDK Build
  directory\>/boot-firmware/fwdn_nd.exe )

- fwdn_batch.bat (copy from ~/\<Topst SDK Build
  directory\>/boot-firmware/fwdn_batch.bat )

> <img src="https://github.com/topst-development/Documentation/blob/main/TOPST-AI/Software/media/Firmware Download.image4.png"
> style="width:5.01042in;height:2.05139in"
> alt="텍스트, 스크린샷, 폰트, 번호이(가) 표시된 사진 자동 생성된 설명" />
>
> Figure 1.4 Copy files for FWDN

1.  Run **fwdn_batch.bat** and enter the **port number**.

    <img src="https://github.com/topst-development/Documentation/blob/main/TOPST-AI/Software/media/Firmware Download.image5.png"
    style="width:4.22917in;height:3.62292in"
    alt="텍스트, 전자제품, 스크린샷, 소프트웨어이(가) 표시된 사진 자동 생성된 설명" />

    Figure 1.5 Input Port Number for FWDN

2.  Finish FWDN

    <img src="https://github.com/topst-development/Documentation/blob/main/TOPST-AI/Software/media/Firmware Download.image6.png"
    style="width:5.32292in;height:1.21597in"
    alt="텍스트, 스크린샷, 폰트이(가) 표시된 사진 자동 생성된 설명" />

    Figure 1.6 Finish Firmware Download
