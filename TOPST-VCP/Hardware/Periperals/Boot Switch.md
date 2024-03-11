<h1 style="color:red">
  Boot Mode (SW2)
</h1>


The TOPST VCP has one pin for boot configuration using Boot Mode (BM) and supports 2 modes:  
UART boot mode and normal mode.

The slide switch (SW2) is used to select the boot modes of the TOPST VCP.


Figure 1.1 shows the appearance of slide switch (SW2).

<p align="center"><img src="https://github.com/Topst-Dev/Documentation/assets/161264431/e26dd2fc-66ff-40d9-ba98-e5590616b00d"></p>


Figure 1.2 shows the schematic of slide switch (SW2).

<p align="center"><img src="https://github.com/Topst-Dev/Documentation/assets/161264431/8a457adc-4d55-4472-bee0-834ac9e5a1a8"></p>

Table 1.1 describes the function slide switch (SW2).  

**Table 1.1 Description of Slide Switch (SW2) for Boot Mode:**  

| Reference Number | Function Name Name | Description                               |
|:----------------:|:------------------:|-------------------------------------------|
|       SW2        |      Boot Mode     |  Boot mode of TCC7045                     |  

  

Figure 1.3 shows circuit connection status according to the slide switch position.
<p align="center"><img src="https://github.com/Topst-Dev/Documentation/assets/161264431/61949a2f-b2cd-4934-8759-2719dc0052a9"></p>


## UART Boot Mode
This mode is mainly for Firmware download (**FWDN**) mode.
In this mode, you can download a program into user-defined area by using the UART port.


Table 1.2 describes the setting of slide switch for UART boot mode.  

 **Table 1.2 Configuration of UART for Boot Mode:**   
 
| Pin | Value | Figure                              |
|:---:|:-----:|-------------------------------------|
| BM (SW2) | High (1) |  ![image](https://github.com/Topst-Dev/Documentation/assets/161264431/e5df491e-1776-4b1f-9e91-1c2dd5e61025)    ![image](https://github.com/Topst-Dev/Documentation/assets/161264431/a66a2c96-fcb8-4f06-b0ca-6ec863292b8b)        |  

 




## Normal Mode
This mode is a typical mode of normal operation.

Table 1.3 descrubes the setting of slide switch for normal mode.  

**Table 1.3 Configuration of Normal Mode:**  

| Pin | Value | Figure                              |
|:---:|:-----:|-------------------------------------|
| BM (SW2) | Low(0) |  ![image](https://github.com/Topst-Dev/Documentation/assets/161264431/e22dedaf-ba40-4d03-8490-60fe2bd6ba5d)     ![image](https://github.com/Topst-Dev/Documentation/assets/161264431/2f871000-ab0c-4f81-bfdb-31fc05373906)      |  

 

