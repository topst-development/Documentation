<h1>
  Debugging
</h1>


## Debugger I/F Connector (UART/JTAG) to Host PC  

Figure 1.1 shows the 0.5 mm Pitch 20-pin FFC (A side–B side) used for debugging.  
<p align="center"><img src="https://github.com/Topst-Dev/Documentation/assets/161264431/21cef494-2147-4d43-91ca-004d4c8acb16"></p>  


## Debug Port on TOPST D3  

The TOPST D3 uses serial communication for debugging output, and Debug is designed for FFC connector.  

Figure 1.2 shows the appearance of Debug on the TOPST D3.  
<p align="center"><img src="https://github.com/Topst-Dev/Documentation/assets/161264431/490ba306-6322-43f1-9210-581772203890"></p>  


## UART/JTAG Sub-board  

The UART/JTAG sub-board is a debugging board for serial port and JTAG. You can check the serial log by connecting the UART/JTAG sub-board to your Host PC using a USB Type-C cable.   

Figure 1.3 shows the overview of the UART/JTAG sub-board.  
<p align="center"><img src="https://github.com/Topst-Dev/Documentation/assets/161264431/e330d74c-e1a9-45ec-b2a7-c2520ad47e68"></p>  

Table 1 describes the connectors of the UART/JTAG sub-board.  

**Table 1 Description of UART/JTAG Sub-board:**  

| Item | Description                                    |
|:----:|------------------------------------------------|
| u10  | FFC connector to connect the TOPST D3          |
| u20  | Male Pin Header to connect debugger            |
| u30  | Debug port (USB Type-C) for MCU debugging      |
| u40  | Debug port (USB Type-C) for A53 Core debugging |
| u50  | Debug port (USB Type-C) for A72 Core debugging |
