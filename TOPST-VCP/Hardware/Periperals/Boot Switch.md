<h1 style="color:red">
  Boot Mode (SW2)
</h1>


The TOPST VCP has one pin for boot configuration using Boot Mode (BM) and supports 2 modes:  
UART boot mode and normal mode.

The slide switch (SW2) is used to select the boot modes of the TOPST VCP.


Figure 1.1 shows the appearance of slide switch (SW2).

<p align="center"><img src="https://github.com/Topst-Dev/Documentation/assets/161264431/bb2f0001-5311-4c3c-b0dc-13944167bc1e"></p>
<p align="center"><strong>Figure 1.1 Slide Switch (SW2) </strong> </p>



Figure 1.2 shows the schematic of slide switch (SW2).

<p align="center"><img src="https://github.com/Topst-Dev/Documentation/assets/161264431/bed66745-24db-45f6-959f-cb8142ec0ca7"></p>
<p align="center"><strong>Figure 1.2 Schematic of Slide Switch (SW2) for Boot Mode </strong> </p>


Table 1.1 describes the function slide switch (SW2).  

**Table 1.1 Description of Slide Switch (SW2) for Boot Mode:**  

| Reference Number | Function Name Name | Description                               |
|:----------------:|:------------------:|-------------------------------------------|
|       SW2        |      Boot Mode     |  Boot mode of TCC7045                     |  

  

Figure 1.3 shows circuit connection status according to the slide switch position.
<p align="center"><img src="https://github.com/Topst-Dev/Documentation/assets/161264431/c1df3c91-8367-443a-aebf-fffe8129bf75"></p>
<p align="center"><strong> Figure 1.3 Slide Switch Position (SW2) </strong> </p>


## UART Boot Mode
This mode is mainly for Firmware download (**FWDN**) mode.
In this mode, you can download a program into user-defined area by using the UART port.


Table 1.2 describes the setting of slide switch for UART boot mode.  

 **Table 1.2 Configuration of UART for Boot Mode:**   
 
| Pin | Value | Figure                              |
|:---:|:-----:|-------------------------------------|
| BM (SW2) | High (1) |  ![image](https://github.com/Topst-Dev/Documentation/assets/161264431/e5df491e-1776-4b1f-9e91-1c2dd5e61025)   ![image](https://github.com/Topst-Dev/Documentation/assets/161264431/17beb32a-cc49-45b7-9a79-f528759baf49)        |  

 




## Normal Mode
This mode is a typical mode of normal operation.

Table 1.3 descrubes the setting of slide switch for normal mode.  

**Table 1.3 Configuration of Normal Mode:**  

| Pin | Value | Figure                              |
|:---:|:-----:|-------------------------------------|
| BM (SW2) | Low(0) |  ![image](https://github.com/Topst-Dev/Documentation/assets/161264431/e22dedaf-ba40-4d03-8490-60fe2bd6ba5d)  ![image](https://github.com/Topst-Dev/Documentation/assets/161264431/d8749701-a756-4f5d-88d4-e6bffc79a26b) |  

 

