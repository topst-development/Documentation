# FWDN Guide

This chapter describes how to download the Firmware Downloader (***FWDN***) to the TOPST D3 and log in to the Linux console.

## **1.1   Firmware Download Sequence**

The download sequence of ***FWDN*** is as follows:

1. Enter FWDN Mode.
2. Connect the USB A-to-A cable to the USB 2.0 FWDN port.
3. Download the TOPST image.

## **1.2   Enter FWDN Mode**

Press the **SW2** (FWDN Mode Convert) button and connect the power to enter ***FWDN*** mode. Alternatively, if power is connected, press the **SW2** button (FWDN Mode Convert) and press the **SW1** button (System Reset) to enter the ***FWDN*** mode.

<br>
<div align="center">
    <img src="https://github.com/Topst-Dev/Documentation/assets/161264431/ca2d9960-3ba9-494c-bc27-424607cd7305" >
    <p><strong>Figure 1.1 Board Connection</strong></p>
</div>
<br>

Install the Vendor Telechips Certification (VTC) driver (found on [https://gsmusbdriver.com/install-telechips-vtc-usb-driver](https://gsmusbdriver.com/install-telechips-vtc-usb-driver)) on the host PC by running as administrator. When you connect the USB in the FWDN mode as shown above, the Telechips VTC USB driver is set as shown in the Figure 1.2 and Figure 1.3.

<br>
<div align="center">
    <img src="https://github.com/Topst-Dev/Documentation/assets/16188136/8bc46265-f0c6-4eb8-aea6-c58128ef5d4b" alt="USB Connection in Windows Environment" >
    <p><strong>Figure 1.2 USB Connection in Windows Environment</strong></p>
</div>
<br>
<div align="center">
    <img src="https://github.com/Topst-Dev/Documentation/assets/16188136/cfa3e2b4-ff2a-4d50-ac19-28e247f6af8b" alt="USB Connection in Linux Environment" >
    <p><strong>Figure 1.3 USB Connection in Linux Environment</strong></p>
</div>
<br>

## 1.3 Run FWDN with CLI Tool

To use ***FWDN***, download the firmware tool from the link below:

- [https://topst.ai](https://topst.ai/)
- MATERIAL→TOPST D3→Software ***FWDN***

You can download each of the following TOPST images by using the as follows.

- Script location: fwdn\fwdn.bat
1. **all**: TOPST full image
2. **main**: Main core (CA72) image
3. **sub**: Sub-core (CA53) image
4. **mcu**: CR5 image

<br><div align="center">
    <img src="https://github.com/Topst-Dev/Documentation/assets/16188136/99514737-ddfa-4670-9173-73749f00a72c" alt="Load FWDN CLI Tool" >
    <p><strong>Figure 1.4 Load FWDN CLI Tool</strong></p>
</div><br>

In the following figure, the entire TOPST image is downloaded by using the **all** command.
When the TOPST D3 is rebooted by pressing the SW1 (Reset) button, Ubuntu launcher is executed.

<br><div align="center">
    <img src="https://github.com/Topst-Dev/Documentation/assets/16188136/74414924-906e-48f8-a8b4-b48a2cf7ccc9" alt="Download Image by using FWDN CLI Tool" >
    <p><strong>Figure 1.5 Download Image by using FWDN CLI Tool</strong></p>
</div><br>

## 1.4 Run FWDN with TOPST Tool

To use ***FWDN***, download the firmware tool from the link below:

- [https://topst.ai](https://topst.ai/)
- MATERIAL→TOPST D3→Software ***FWDN***

To use ***FWDN***, run the script as follows:

- Tool location:

<div align="center">

| OS | Location | Script |
| --- | --- | --- |
| Linux | fwdn/fwdn | sudo ./fwdn.sh |
| Windows | fwdn\TOPST.exe | TOPST.exe |
</div>

<br><div align="center">
     <img src="https://github.com/Topst-Dev/Documentation/assets/16188136/c7a036d1-2da4-4814-add5-1efeab88733f" alt="Load FWDN Application" width="600" height="400">
    <p><strong>Figure 1.6 Load FWDN Application</strong></p>
</div><br>

Press the **Check Status** button to check the connection state with the board. If the USB is connected to the board normally in ***FWDN*** mode, a notification window appears and the state turns on.

<br><div align="center">
    <img src="https://github.com/Topst-Dev/Documentation/assets/16188136/a096ee2d-dfb7-4b7e-a340-ef819af49f93" alt="Check FWDN Connection Status" width="1200" height="330">
    <p><strong>Figure 1.7 Check FWDN Connection Status</strong></p>
</div><br>

If the state is not ON, the **Write** button is disabled, so you cannot continue with the installation. After checking the connection state, press the **Select Image** button to download the image.

<br><div align="center">
    <img src="https://github.com/Topst-Dev/Documentation/assets/16188136/2efc2264-e603-40bd-b10e-cf49b93300cd" alt="Select TOPST Image by using FWDN Application" width="600" height="400">
    <p><strong>Figure 1.8 Select TOPST Image by using FWDN Application</strong></p>
</div><br>

Press the **Select Image** button to display a screen where you can select an image. You can download the image directly from the server and proceed with the installation, or you can select the path to the image that you built and created.

<br><div align="center">
    <img src="https://github.com/Topst-Dev/Documentation/assets/16188136/2df2ab47-34fb-4a5d-955d-2da9e2bfb752" alt="Download TOPST Image by using FWDN Application" width="600" height="400">
    <p><strong>Figure 1.9 Download TOPST Image by using FWDN Application</strong></p>
</div><br>

Then, return to the main screen and press the activated **Write** button to proceed with the installation.

<br><div align="center">
    <img src="https://github.com/Topst-Dev/Documentation/assets/16188136/2109d102-bd2b-40fe-a609-fa5ac34d6ae1" alt="Completed Downloading TOPST Image" width="600" height="400">
    <p><strong>Figure 1.10 Completed Downloading TOPST Image</strong></p>
</div><br>

As shown above, a notification window appears when the installation is complete. Now exit the ***FWDN*** tool and press the SW1 (System Reset) button on the board to reboot.
