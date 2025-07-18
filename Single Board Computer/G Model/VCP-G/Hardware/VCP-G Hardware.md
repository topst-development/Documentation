# 1. Introduction
---
This document is a hardware user guide for the VCP-G based on the TCC7045 application processor. This document describes system installation, debugging, and detailed information on overall design and usage of the VCP-G.


Table 1.1 describes the features of the VCP-G.

<p align="center"><strong>Table 1.1 Features of VCP-G</strong></p>
<div align="center">
	<table>
	  <tr>
	    <td colspan="3">Part Name</td>
	    <td>TCC7045</td>
	  </tr>
	  <tr>
	    <td colspan="3">Package</td>
	    <td>Package	Pin to Pin Compatible FBGA 196-pin (12BD)</td>
	  </tr>
	    <tr>
	    <td colspan="3">CPU Frequency</td>
	    <td>200 MHz (Up to 300 MHz)</td>
	  </tr>
	  <tr>
	    <td rowspan="4">On-chip Memory</td>
	    <td colspan="2">Program Flash</td>
	    <td colspan="3">4 MB</td>
	  </tr>
	  <tr>
	    <td colspan="2">SRAM</td>
	    <td colspan="3">512 KB (Including Retention RAM 16 KB)</td>
	  </tr>
	  <tr>
	    <td colspan="2">DataFlash</td>
	    <td colspan="3">256 KB</td>
	  </tr>
	  <tr>
	    <td colspan="2">DMA Channel</td>
	    <td colspan="3">16 channels</td>
	  </tr>
	  <tr>
	    <td rowspan="13">Peripheral</td>
	    <td colspan="2">Ethernet</td>
	    <td>1 Gbps with AVB</td>
	  </tr>
	  <tr>
		<td colspan="2">CAN / CANFD</td>
	    <td>3-channel</td>
	  </tr>
	  <tr>
	    <td colspan="2">Dedicated LIN / UART</td>
	    <td>3 channels (Maximum 6 channels)</td>
	  </tr>
	  <tr>
	    <td colspan="2">Dedicated I2C</td>
	    <td>3 channels (Maximum 6 channels)</td>
	  </tr>
	  <tr>
	  <tr>
	    <td colspan="2">Dedicated GPSB (SPI)</td>
	    <td>2 channels (Maximum 5 channels)</td>
	  </tr>
	    <tr>
	    <td colspan="2">MFIO (Allocated UART, I2C, GPSB)</td>
	    <td>3 channels</td>
	  </tr>
	  <tr>
	    <td rowspan="4">ADC</td> 
	    <td>Resolution</td>
	    <td>12-bit SAR type</td>
	  </tr>
	  <tr>
	    <td>Channels</td>
	    <td>12-channel x 2 groups</td>
	  </tr>
	  <tr>
	    <td>Input Range</td>
	    <td>3.3V</td>
	  </tr>
	  <tr>
	    <td>Sample Rate</td>
	    <td>Over 1.0 MSPs</td>
	  </tr>
	  <tr>
	    <td colspan="2">I2S</td>
	    <td>1-channel</td>
	  </tr>
	  <tr>
	    <td colspan="2">Serial Flash Interface</td>
	    <td>Quad SPI</td>
	  </tr>  
	  <tr>
	    <td colspan="3">Power System</td>
	    <td>3.3V single</td>
	  </tr>
	  <tr>
	    <td colspan="3">Temperature</td>
	    <td>-40 ℃ to 105 ℃</td>
	  </tr>
	</table>
</div>

</br></br></br>

## 1.1 Terminology
---
<p align="center"><strong>Table 1.2 Terminology </strong></p>
<div align="center">
	<table>
	  <tr>
	    <td clospan="2"><strong>Terminology</strong></td>
	    <td><strong>Definition</strong></td>
	  </tr>
	  <tr>
	    <td clospan="2">ADC</td>
	    <td>Analog to Digital Converter</td>
	  </tr>
	  <tr>
	    <td clospan="2">FWDN</td>
	    <td>Firmware Download</td>
	  </tr>
	  <tr>
	    <td clospan="2">GPIO</td>
	    <td>General Purpose Input Output</td>
	  </tr>
	  <tr>
	    <td clospan="2">MCU</td>
	    <td>Micro-controller Unit</td>
	  </tr>
	  <tr>
	    <td clospan="2">TOPST</td>
	    <td>Total Open-Platform for System development and Training</td>
	  </tr>
	  <tr>
	    <td clospan="2">VCP</td>
	    <td>Vehicle Control Processer</td>
	  </tr>
	</table>
</div>

</br></br></br></br>

# 2. Block Diagram
---
## 2.1 System Block Diagram
---
Figure 2.1 shows the system block diagram of VCP-G.
<p align="center"><img src= "https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Hardware/2.1%20VCP-G%20System%20Block%20Diagram.png"></p>
<p align="center"><strong>Figure 2.1 System Block Diagram</strong></p>

</br></br></br></br>

# 3. VCP-G Overview
---
The VCP-G can used for the following purposes:
  - System development
  - Training

Table 3.1 describes the default configuration of the VCP-G.

<p align="center"><strong>Table 3.1 Default Configuration of VCP-G </strong></p>
<div align="center">
	<table>
	  <tr>
	    <td colspan="2"><strong>Board Name</strong></td>
	    <td><strong>Description</strong></p>
	  </tr>
	  <tr>
	    <td colspan="2">TOPST_VCP_V2.1.1</td>
	    <td>MCU board for TOPST</td>
	  </tr>
	</table>
</div>

</br></br></br>

## 3.1 VCP-G
---
Figure 3.1 shows the top view of VCP-G.
<p align="center"><img src= "https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Hardware/3.1%20TOPST%20VCP-G%20Board%20(Top%20View)%20.png"></p>
<p align="center"><strong>Figure 3.1 VCP-G (Top View)</strong></p>

Table 3.2 describes the connectors of VCP-G (top view).
<p align="center"><strong>Table 3.2 Connectors of VCP-G (Top View)</strong></p>
<div align="center">
	<table>
	  <tr>
	    <td colspan="4"><strong>Number</strong></td>
	    <td><strong>Reference Number</strong></td>
	    <td><strong>Name</strong></td>
	    <td><strong>Description</strong></td>
	  </tr>
	  <tr>
	    <td colspan="4">1</td>
	    <td>J18D100</td>
	    <td>36-pin Female Header</td>
	    <td>Header for GPIO and ADC</td>
	  </tr>
	  <tr>
	    <td colspan="4">2</td>
	    <td>J5D100</td>
	    <td>10-pin Male Header</td>
	    <td>Header for CAN</td>
	  </tr>
	  <tr>
	    <td colspan="4">3</td>
	    <td>J3D100</td>
	    <td>6-pin Male Header</td>
	    <td>Header for SPI</td>
	  </tr>
	  <tr>
	    <td colspan="4">4</td>
	    <td>J8D104</td>
	    <td>8-pin Female Header</td>
	    <td>Header for GPIO and ADC</td>
	  </tr>
	  <tr>
	    <td colspan="4">5</td>
	    <td>J8D102</td>
	    <td>8-pin Female Header</td>
	    <td>Header for GPIO</td>
	  </tr>
	  <tr>
	    <td colspan="4">6</td>
	    <td>J10D100</td>
	    <td>10-pin Female Header</td>
	    <td>Header for GPIO and ADC</td>
	  </tr>
	  <tr>
	    <td colspan="4">7</td>
	    <td>J100</td>
	    <td>10-pin Male Header</td>
	    <td>Header for JTAG</td>
	  </tr>
	  <tr>
	    <td colspan="4">8</td>
	    <td>SW100</td>
	    <td>RESET Tact Switch</td>
	    <td>GRESETn: Initializes the system and the power management of VCP-G</td>
	  </tr>
	  <tr>
	    <td colspan="4">9</td>
	    <td>JC100</td>
	    <td>USB Type-C Connector</td>
	    <td>UART for debugging or FWDN port</td>
	  </tr>
	  <tr>
	    <td colspan="4">10</td>
	    <td>SW101</td>
	    <td>Tact Switch</td>
	    <td>FWDN: Enter the Firmware download mode of VCP-G</td>
	  </tr>  
	  <tr>
	    <td colspan="4">11</td>
		<td>J101</td>
	    <td>DC Jack</td>
	    <td>DC Power Input Jack</td>
	  </tr>  
	  <tr>
	    <td colspan="4">12</td>
	    <td>J8D100</td>
	    <td>8-pin Female Header</td>
	    <td>Header for Power and Reset</td>
	  </tr>  
	  <tr>
	    <td colspan="4">13</td>
	    <td>J8D101</td>
	    <td>8-pin Female Header</td>
	    <td>Header for GPIO and ADC</td>
	  </tr>  
	  <tr>
	    <td colspan="4">14</td>
	    <td>J8D103</td>
	    <td>8-pin Female Header</td>
	    <td>Header for GPIO and ADC</td>
	  </tr>    
	</table>
</div>

Figure 3.2 shows the bottom view of the VCP-G.  

**Note:** Figure 3.2 currently shows the TOPST_VCP-G_V1.1.1 board. This image will be updated to the TOPST_VCP-G_V2.1.1 board.
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Hardware/3.2%20TOPST%20VCP-G%20Board%20(Bottom%20View).png"></p>
<p align="center"><strong>Figure 3.2 VCP-G (Bottom View)</strong></p>

</br></br></br></br>

# 4. Specifications
---
## 4.1 Quad SPI Flash Memory (U101)
---
The information on the Quad SPI flash memory is as follows:
  - Density : 64 Mb  
  
**Note:** SNOR is not mounted on the VCP-G by default.

</br></br></br>

## 4.2 Power-in Connector (J101)
---
DC 12V is supplied to the VCP-G through the DC jack of J101 from a 12V adaptor.  
Figure 4.1 shows the location of J101.
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Hardware/4.1%20Power%20In%20Connector%20(J101).png"></p>
<p align="center"><strong>Figure 4.1 Power-in Connector (J101)</strong><p>

</br></br></br>

## 4.3 Connector for JTAG (J100)
---
A JTAG emulator can be connected to the VCP-G through J100 for debugging. Figure 4.2 shows the location of J100.
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Hardware/4.2%20Connector%20for%20JTAG%20(J100).png"></p>
<p align="center"><strong>Figure 4.2 Connector for JTAG (J100)</strong><p>
JTAG is disabled by default. To enable JTAG, you must change the connections of R178 and R179. If TRSRn is set to high by R178, the MCU enters JTAG mode.

Table 4.1 describes the pins of J100.
<p align="center"><strong>Table 4.1 J100 Pin Description</strong></p>
<div align="center">
	<table>
	  <tr>
	    <th rowspan="2"><strong>Pin Number</strong></th>
	    <th rowspan="2"><strong>Schematic Net Name</strong></th>
	    <th><strong>DIR</strong></th>
	    <th rowspan="2"><strong>Description</strong></th>
	  </tr>
	  <tr>
	    <th><strong>MCU ◄► J100</strong></th>
	  </tr>
	  <tr>
	    <td>1</td>
	    <td>SW_VDD_3P3</td>
	    <td>-</td>
	    <td>Power 3.3V</td>
	  </tr>
	  <tr>
	    <td>2</td>
	    <td>TMS</td>
	    <td>◄</td>
	    <td>Test Mode State</td>
	  </tr>
	  <tr>
	    <td>3</td>
	    <td>DGND</td>
	    <td>-</td>
	    <td>Ground</td>
	  </tr>
	  <tr>
	    <td>4</td>
	    <td>TCK</td>
	    <td>◄</td>
	    <td>Test Clock</td>
	  </tr>
	  <tr>
	    <td>5</td>
		<td>DGND</td>
	    <td>-</td>
	    <td>Ground</td>
	  </tr>
	  <tr>
	    <td>6</td>
	    <td>TDO</td>
	    <td>►</td>
	    <td>Test Data Output</td>
	  </tr>
	  <tr>
	    <td>7</td>
	    <td>NC</td>
	    <td>-</td>
	    <td>Not Connected</td>
	  </tr>
	  <tr>
	    <td>8</td>
	    <td>TDI</td>
	    <td>◄</td>
	    <td>Test Data In</td>
	  </tr>
	  <tr>
	    <td>9</td>
	    <td>DGND</td>
	    <td>-</td>
	    <td>Ground</td>
	  </tr>
	  <tr>
	    <td>10</td>
	    <td>JTAG_RESETn</td>
	    <td>◄</td>
	    <td>System Reset</td>
	  </tr>   
	</table>
</div>

Table 4.2 describes the setting of JTAG Disable/Enable.
<p align="center"><strong>Table 4.2 Setting of JTAG Disable/Enable</strong></p>
<div align="center">
	<table>
	  <tr>
	    <th colspan="4"><strong>Mode</strong></th>
	    <th><strong>TRSTn Value</strong></th>
	    <th><strong>R178</strong></th>
	    <th><strong>R179</strong></th>
	  </tr>
	  <tr>
	    <td colspan="4">JTAG Disable (Default)</td>
	    <td>Low (1)</td>
	    <td>N.C</td>
	    <td>1K</td>
	  </tr>
	  <tr>
	    <td colspan="4">JTAG Enable (Option)</td>
	    <td>High (1)</td>
	    <td>1K</td>
	    <td>N.C</td>
	  </tr>
	</table>
</div>

</br></br></br>

## 4.4 FWDN Switch (SW101)
---
The VCP-G has one pin for boot configuration using Boot Mode (BM) and supports 2 modes: UART FWDN mode and normal mode.   
Figure 4.3 shows the location of FWDN tact switch (SW101), which is used to select the boot mode of the VCP-G.
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Hardware/4.3%20FWDN%20Tact%20Switch%20(SW101).png"></p>
<p align="center"><strong>Figure 4.3 FWDN Tact Switch (SW101)</strong><p>

Table 4.3 describes how to use the FWDN tact switch (SW101) to select the boot mode.
<p align="center"><strong>Table 4.3 Description of Tact Switch (SW101) for Boot Mode</strong></p>
<div align="center">
	<table>
	  <tr>
	    <th colspan="3"><strong>Mode</strong></th>
	    <th><strong>BM00 Value</strong></th>
	    <th><strong>SW101 Status</strong></th>
	  </tr>
	  <tr>
	    <td colspan="3">Normal (Default)</td>
	    <td>Low (1)</td>
	    <td>Default</td>
	  </tr>
	  <tr>
	    <td colspan="3">FWDN (Option)</td>
	    <td>High (1)</td>
	    <td>Pushed and Power</td>
	  </tr>
	</table>
</div>
</br></br>

### 4.4.1 FWDN Mode Method
There are two methods to enter FWDN mode as follows.

#### 4.4.1.1 Method 1
While pressing the FWDN switch (SW101), connect the 12V power supply to turn on the VCP-G board.  
The FWDN red indicator turns on when power is applied while the FWDN switch is pressed. After releasing the FWDN switch (SW101), the MCU enters FWDN mode.  
Figure 4.4 shows how to enter FWDN mode by using method 1.
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Hardware/4.4%20Entering%20FWDN%20Mode%20by%20Using%20Method%201.png"></p>
<p align="center"><strong>Figure 4.4 Enter FWDN Mode by using Method 1</strong><p>

#### 4.4.1.2 Method 2
While the VCP-G board is connected to the 12V power supply, press the FWDN switch (SW101) and then press the RESET tact switch (SW100).  
The FWDN red indicator turns on when the power is applied while the FWDN switch is pressed. The 3.3V green indicator turns off while the RESET tact switch is pressed. After releasing the FWDN switch (SW101), the MCU enters FWDN mode.  
Figure 4.5 shows the FWDN mode by using method 2.

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Hardware/4.5%20Entering%20FWDN%20Mode%20by%20Using%20Method%202.png"></p>
<p align="center"><strong>Figure 4.5 Enter FWDN Mode by using Method 2</strong><p>

</br></br></br>

## 4.5 RESET Tact Switch (SW100)
---
The VCP-G has one RESET switch for power of RESET using GRESETn pin.  
Figure 4.6 shows the RESET tact switch (SW100).
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Hardware/4.6%20RESET%20Tact%20Switch%20(SW100).png"></p>
<p align="center"><strong>Figure 4.6 RESET Tact Switch (SW100)</strong><p>
</br></br>

### 4.5.1 RESET Tact Switch (SW100) Function
SW100 is a tact switch to reset the power block and system block in VCP-G.  
The function of this button is as follows:
  - Pressing the RESET tack switch (SW100) while the power is on forces the power block and the system of the VCP-G to reset.

**Important:** Be careful when pressing the tack switch as the power suddenly turns off and data may be corrupted.

</br></br></br>

## 4.6 Connector for Debugging and FWDN (JC100)
---
The JC100 is a standard USB Type-C connector. On the VCP-G, JC100 is used for debugging or FWDN through UART.  
Figure 4.7 shows the location of JC100.
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Hardware/4.7%20USB%20Type-C%20Connector%20(JC100).png"></p>
<p align="center"><strong>Figure 4.7 USB Type-C Connector (JC100)</strong><p>

You can perform FWDN or check debugging message of the VCP-G through JC100.
JC100 on the VCP-G includes a built-in USB-to-UART bridge controller, so you can directly connect JC100 to PC by using the USB Type-C cable.

</br></br></br>

## 4.7 Pin Headers for GPIO, ADC, Power, CAN, and SPI
---
The VCP-G has nine 2.54 mm pin headers for power, GPIO, ADC, CAN, and SPI to connect to other peripherals such as sensors or sub-boards.  

Table 4.4 describes the purpose of the nine pin headers on the VCP-G.
<p align="center"><strong>Table 4.4 Pin Headers on VCP-G </strong></p>
<div align="center">
	<table>
	  <tr>
	    <td colspan="4"><strong>Number</strong></td>
	    <td><strong>Reference Number</strong></td>
	    <td><strong>Name</strong></td>
	    <td><strong>Description</strong></td>
	  </tr>
	  <tr>
	    <td colspan="4">1</td>
	    <td>J18D100</td>
	    <td>36-pin Female Header</td>
	    <td>Header for GPIO and ADC</td>
	  </tr>
	  <tr>
	    <td colspan="4">2</td>
	    <td>J5D100</td>
	    <td>10-pin Male Header</td>
	    <td>Header for CAN</td>
	  </tr>
	  <tr>
	    <td colspan="4">3</td>
	    <td>J3D100</td>
	    <td>6-pin Male Header</td>
	    <td>Header for SPI</td>
	  </tr>
	  <tr>
	    <td colspan="4">4</td>
	    <td>J8D104</td>
	    <td>8-pin Female Header</td>
	    <td>Header for GPIO and ADC</td>
	  </tr>
	  <tr>
	    <td colspan="4">5</td>
	    <td>J8D102</td>
	    <td>8-pin Female Header</td>
	    <td>Header for GPIO</td>
	  </tr>
	  <tr>
	    <td colspan="4">6</td>
	    <td>J10D100</td>
	    <td>10-pin Female Header</td>
	    <td>Header for GPIO and ADC</td>
	  </tr>
	  <tr>
	    <td colspan="4">7</td>
	    <td>J8D100</td>
	    <td>8-pin Female Header</td>
	    <td>Header for Power and Reset</td>
	  </tr>
	  <tr>
	    <td colspan="4">8</td>
	    <td>J8D101</td>
	    <td>8-pin Female Header</td>
	    <td>Header for GPIO and ADC</td>
	  </tr>
	  <tr>
	    <td colspan="4">9</td>
	    <td>J8D103</td>
	    <td>8-pin Female Header</td>
	    <td>Header for GPIO and ADC</td>
	  </tr>
	</table>
</div>

Figure 4.8 shows the location of pin headers on the VCP-G.
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Hardware/4.8%20Pin%20Headers%20on%20TOPST%20VCP-G%20Board.png"></p>
<p align="center"><strong>Figure 4.8 Pin Headers on VCP-G </strong><p>

Table 4.5 shows the pin description of J10D100.
<p align="center"><strong>Table 4.5 J10D100 Pin Description</strong></p>
<div align="center">
	<table>
	  <tr>
	    <th rowspan="3"><strong>Pin Number</strong></th>
	    <th colspan="4"><strong>J10D100</strong></th>
	  </tr>
	  <tr>
	    <th rowspan="2"><strong>Port Name</strong></th>
	    <th rowspan="2"><strong>Signal Name</strong></th>
	    <th><strong>DIR</strong></th>
	    <th rowspan="2"><strong>Description</strong></th>
	  </tr>
	  <tr>
	    <th><strong>MCU ◄► J10D100</strong></th>
	  </tr>
	  <tr>
	    <td>1</td>
	    <td>SCL</td>
	    <td>GPIO_AC07</td>
	    <td>◄►</td>
	    <td>GPIO or ADC signal</td>
	  </tr>
	  <tr>
	    <td>2</td>
	    <td>SDA</td>
	    <td>GPIO_AC06</td>
	    <td>◄►</td>
	    <td>GPIO or ADC signal</td>
	  </tr>
	  <tr>
	    <td>3</td>
	    <td>AREF</td>
	    <td>ADC06</td>
	    <td>◄</td>
	    <td>ADC signal</td>
	  </tr>
	  <tr>
	    <td>4</td>
	    <td>GND</td>
	    <td>DGND</td>
	    <td>-</td>
	    <td>Ground</td>
	  </tr>
	  <tr>
	    <td>5</td>
	    <td>13</td>
	    <td>GPIO_C12</td>
	    <td>◄►</td>
	    <td>GPIO signal</td>
	  </tr>
	  <tr>
	    <td>6</td>
	    <td>12</td>
	    <td>GPIO_C15</td>
	    <td>◄►</td>
	    <td>GPIO signal</td>
	  </tr>
	  <tr>
	    <td>7</td>
	    <td>11</td>
	    <td>GPIO_C14</td>
	    <td>◄►</td>
	    <td>GPIO signal</td>
	  </tr>
	  <tr>
	    <td>8</td>
	    <td>10</td>
	    <td>GPIO_C13</td>
	    <td>◄►</td>
	    <td>GPIO signal</td>
	  </tr>
	  <tr>
	    <td>9</td>
	    <td>9</td>
	    <td>GPIO_A12</td>
	    <td>◄►</td>
	    <td>GPIO signal</td>
	  </tr>
	  <tr>
	    <td>10</td>
	    <td>8</td>
	    <td>GPIO_B00</td>
	    <td>◄►</td>
	    <td>GPIO signal</td>
	  </tr>
	</table>
</div>

Table 4.6 shows the pin description of J8D100.
<p align="center"><strong>Table 4.6 J8D100 Pin Description</strong></p>
<div align="center">
	<table>
	  <tr>
	    <th rowspan="3"><strong>Pin Number</strong></th>
	    <th colspan="4"><strong>J8D100</strong></th>
	  </tr>
	  <tr>
	    <th rowspan="2"><strong>Port Name</strong></th>
	    <th rowspan="2"><strong>Signal Name</strong></th>
	    <th><strong>DIR</strong></th>
	    <th rowspan="2"><strong>Description</strong></th>
	  </tr>
	  <tr>
	    <th><strong>MCU ◄► J8D100</strong></th>
	  </tr>
	  <tr>
	    <td>1</td>
	    <td>-</td>
	    <td>-</td>
	    <td>-</td>
	    <td>-</td>
	  </tr>
	  <tr>
	    <td>2</td>
	    <td>IOREF</td>
	    <td>VCP_3P3</td>
	    <td>-</td>
	    <td>Power 3.3V</td>
	  </tr>
	  <tr>
	    <td>3</td>
	    <td>RST</td>
	    <td>RESET</td>
	    <td>◄</td>
	    <td>Reset signal</td>
	  </tr>
	  <tr>
	    <td>4</td>
	    <td>3.3V</td>
	    <td>VCP_3P3</td>
	    <td>-</td>
	    <td>Power 3.3V</td>
	  </tr>
	  <tr>
	    <td>5</td>
	    <td>5V</td>
	    <td>VCP_5P0</td>
	    <td>-</td>
	    <td>Power 5.0V</td>
	  </tr>
	  <tr>
	    <td>6</td>
	    <td>GND</td>
	    <td>DGND</td>
	    <td>-</td>
	    <td>Ground</td>
	  </tr>
	  <tr>
	    <td>7</td>
	    <td>GND</td>
	    <td>DGND</td>
	    <td>-</td>
	    <td>Ground</td>
	  </tr>
	  <tr>
	    <td>8</td>
	    <td>VIN</td>
	    <td>VIN</td>
	    <td>-</td>
	    <td>Voltage input for VCP-G</td>
	  </tr>
	</table>
</div>

Table 4.7 shows the pin description of J8D101.
<p align="center"><strong>Table 4.7 J8D101 Pin Description</strong></p>
<div align="center">
	<table>
	  <tr>
	    <th rowspan="3"><strong>Pin Number</strong></th>
	    <th colspan="4"><strong>J8D101</strong></th>
	  </tr>
	  <tr>
	    <th rowspan="2"><strong>Port Name</strong></th>
	    <th rowspan="2"><strong>Signal Name</strong></th>
	    <th><strong>DIR</strong></th>
	    <th rowspan="2"><strong>Description</strong></th>
	  </tr>
	  <tr>
	    <th><strong>MCU ◄► J8D101</strong></th>
	  </tr>
	  <tr>
	    <td>1</td>
	    <td>A0</td>
	    <td>ADC03</td>
	    <td>◄</td>
	    <td>ADC signal</td>
	  </tr>
	  <tr>
	    <td>2</td>
	    <td>A1</td>
	    <td>ADC04</td>
	    <td>◄</td>
	    <td>ADC signal</td>
	  </tr>
	  <tr>
	    <td>3</td>
	    <td>A2</td>
	    <td>GPIO_AC02</td>
	    <td>◄►</td>
	    <td>GPIO signal</td>
	  </tr>
	  <tr>
	    <td>4</td>
	    <td>A3</td>
	    <td>GPIO_AC03</td>
	    <td>◄►</td>
	    <td>GPIO signal</td>
	  </tr>
	  <tr>
	    <td>5</td>
	    <td>A4</td>
	    <td>GPIO_AC05</td>
	    <td>◄►</td>
	    <td>GPIO signal</td>
	  </tr>
	  <tr>
	    <td>6</td>
	    <td>A5</td>
	    <td>GPIO_AC04</td>
	    <td>◄►</td>
	    <td>GPIO signal</td>
	  </tr>
	  <tr>
	    <td>7</td>
	    <td>A6</td>
	    <td>ADC05</td>
	    <td>◄</td>
	    <td>ADC signal</td>
	  </tr>
	  <tr>
	    <td>8</td>
	    <td>A7</td>
	    <td>ADC01</td>
	    <td>◄</td>
	    <td>ADC signal</td>
	  </tr>
	</table>
</div>

Table 4.8 shows the pin description of J8D102.
<p align="center"><strong>Table 4.8 J8D102 Pin Description</strong></p>
<div align="center">
	<table>
	  <tr>
	    <th rowspan="3"><strong>Pin Number</strong></th>
	    <th colspan="4"><strong>J8D102</strong></th>
	  </tr>
	  <tr>
	    <th rowspan="2"><strong>Port Name</strong></th>
	    <th rowspan="2"><strong>Signal Name</strong></th>
	    <th><strong>DIR</strong></th>
	    <th rowspan="2"><strong>Description</strong></th>
	  </tr>
	  <tr>
	    <th><strong>MCU ◄► J8D102</strong></th>
	  </tr>
	  <tr>
	    <td>1</td>
	    <td>7</td>
	    <td>GPIO_B01</td>
	    <td>◄►</td>
	    <td>GPIO signal</td>
	  </tr>
	  <tr>
	    <td>2</td>
	    <td>6</td>
	    <td>GPIO_A13</td>
	    <td>◄►</td>
	    <td>GPIO signal</td>
	  </tr>
	  <tr>
	    <td>3</td>
	    <td>5</td>
	    <td>GPIO_B10</td>
	    <td>◄►</td>
	    <td>GPIO signal</td>
	  </tr>
	  <tr>
	    <td>4</td>
	    <td>4</td>
	    <td>GPIO_B27</td>
	    <td>◄►</td>
	    <td>GPIO signal</td>
	  </tr>
	  <tr>
	    <td>5</td>
	    <td>3</td>
	    <td>GPIO_B11</td>
	    <td>◄►</td>
	    <td>GPIO signal</td>
	  </tr>
	  <tr>
	    <td>6</td>
	    <td>2</td>
	    <td>GPIO_B28</td>
	    <td>◄►</td>
	    <td>GPIO signal</td>
	  </tr>
	  <tr>
	    <td>7</td>
	    <td>1</td>
	    <td>GPIO_B25</td>
	    <td>◄►</td>
	    <td>GPIO signal</td>
	  </tr>
	  <tr>
	    <td>8</td>
	    <td>0</td>
	    <td>GPIO_B26</td>
	    <td>◄►</td>
	    <td>GPIO signal</td>
	  </tr>
	</table>
</div>

Table 4.9 shows the pin description of J8D103.
<p align="center"><strong>Table 4.9 J8D103 Pin Description</strong></p>
<div align="center">
	<table>
	  <tr>
	    <th rowspan="3"><strong>Pin Number</strong></th>
	    <th colspan="4"><strong>J8D103</strong></th>
	  </tr>
	  <tr>
	    <th rowspan="2"><strong>Port Name</strong></th>
	    <th rowspan="2"><strong>Signal Name</strong></th>
	    <th><strong>DIR</strong></th>
	    <th rowspan="2"><strong>Description</strong></th>
	  </tr>
	  <tr>
	    <th><strong>MCU ◄► J8D103</strong></th>
	  </tr>
	  <tr>
	    <td>1</td>
	    <td>A8</td>
	    <td>GPIO_AC08</td>
	    <td>◄►</td>
	    <td>GPIO or ADC signal</td>
	  </tr>
	  <tr>
	    <td>2</td>
	    <td>A9</td>
	    <td>GPIO_AC09</td>
	    <td>◄►</td>
	    <td>GPIO or ADC signal</td>
	  </tr>
	  <tr>
	    <td>3</td>
	    <td>A10</td>
	    <td>GPIO_AC10</td>
	    <td>◄►</td>
	    <td>GPIO or ADC signal</td>
	  </tr>
	  <tr>
	    <td>4</td>
	    <td>A11</td>
	    <td>GPIO_ADC-2</td>
	    <td>◄</td>
	    <td>ADC signal</td>
	  </tr>
	  <tr>
	    <td>5</td>
	    <td>54</td>
	    <td>GPIO_K14</td>
	    <td>◄►</td>
	    <td>GPIO signal</td>
	  </tr>
	  <tr>
	    <td>6</td>
	    <td>55</td>
	    <td>GPIO_K15</td>
	    <td>◄►</td>
	    <td>GPIO signal</td>
	  </tr>
	  <tr>
	    <td>7</td>
	    <td>56</td>
	    <td>GPIO_K01</td>
	    <td>◄</td>
	    <td>GPIO signal</td>
	  </tr>
	  <tr>
	    <td>8</td>
	    <td>57</td>
	    <td>GPIO_K08</td>
	    <td>◄►</td>
	    <td>GPIO signal</td>
	  </tr>
	</table>
</div>

Table 4.10 shows the pin description of J8D104.
<p align="center"><strong>Table 4.10 J8D104 Pin Description</strong></p>
<div align="center">
	<table>
	  <tr>
	    <th rowspan="3"><strong>Pin Number</strong></th>
	    <th colspan="4"><strong>J8D104</strong></th>
	  </tr>
	  <tr>
	    <th rowspan="2"><strong>Port Name</strong></th>
	    <th rowspan="2"><strong>Signal Name</strong></th>
	    <th><strong>DIR</strong></th>
	    <th rowspan="2"><strong>Description</strong></th>
	  </tr>
	  <tr>
	    <th><strong>MCU ◄► J8D104</strong></th>
	  </tr>
	  <tr>
	    <td>1</td>
	    <td>14</td>
	    <td>GPIO_AC00</td>
	    <td>◄►</td>
	    <td>GPIO or ADC signal</td>
	  </tr>
	  <tr>
	    <td>2</td>
	    <td>15</td>
	    <td>GPIO_AC01</td>
	    <td>◄►</td>
	    <td>GPIO or ADC signal</td>
	  </tr>
	  <tr>
	    <td>3</td>
	    <td>16</td>
	    <td>GPIO_A06</td>
	    <td>◄►</td>
	    <td>GPIO signal</td>
	  </tr>
	  <tr>
	    <td>4</td>
	    <td>17</td>
	    <td>GPIO_A07</td>
		<td>◄►</td>
	    <td>GPIO signal</td>
	  </tr>
	  <tr>
	    <td>5</td>
	    <td>18</td>
	    <td>GPIO_A28</td>
	    <td>◄►</td>
	    <td>GPIO signal</td>
	  </tr>
	  <tr>
	    <td>6</td>
	    <td>19</td>
	    <td>GPIO_A29</td>
	    <td>◄►</td>
	    <td>GPIO signal</td>
	  </tr>
	  <tr>
	    <td>7</td>
	    <td>20</td>
	    <td>GPIO_B03</td>
	    <td>◄►</td>
	    <td>GPIO signal</td>
	  </tr>
	  <tr>
	    <td>8</td>
	    <td>21</td>
	    <td>GPIO_B02</td>
	    <td>◄►</td>
	    <td>GPIO signal</td>
	  </tr>
	</table>
</div>

Table 4.11 shows the pin description of J3D100.
<p align="center"><strong>Table 4.11 J3D100 Pin Description</strong></p>
<div align="center">
	<table>
	  <tr>
	    <th rowspan="3"><strong>Pin Number</strong></th>
	    <th colspan="4"><strong>J3D100</strong></th>
	  </tr>
	  <tr>
	    <th rowspan="2"><strong>Port Name</strong></th>
	    <th rowspan="2"><strong>Signal Name</strong></th>
	    <th><strong>DIR</strong></th>
	    <th rowspan="2"><strong>Description</strong></th>
	  </tr>
	  <tr>
	    <th><strong>MCU ◄► J3D100</strong></th>
	  </tr>
	  <tr>
	    <td>1</td>
	    <td>MISO</td>
	    <td>GPIO_B07</td>
	    <td>◄►</td>
	    <td>GPIO signal</td>
	  </tr>
	  <tr>
	    <td>2</td>
	    <td>5V</td>
	    <td>VCP_5P0</td>
	    <td>-</td>
	    <td>Power 5.0V</td>
	  </tr>
	  <tr>
	    <td>3</td>
	    <td>SCK</td>
	    <td>GPIO_B04</td>
	    <td>◄►</td>
	    <td>GPIO signal</td>
	  </tr>
	  <tr>
	    <td>4</td>
	    <td>MOSI</td>
	    <td>GPIO_B06</td>
	    <td>◄►</td>
	    <td>GPIO signal</td>
	  </tr>
	  <tr>
	    <td>5</td>
	    <td>CMD</td>
	    <td>GPIO_B05</td>
	    <td>◄►</td>
	    <td>GPIO signal</td>
	  </tr>
	  <tr>
	    <td>6</td>
	    <td>GND</td>
	    <td>DGND</td>
	    <td>-</td>
	    <td>Ground</td>
	  </tr>
	</table>
</div>

Table 4.12 shows the pin description of J18D100.
<p align="center"><strong>Table 4.12 J18D100 Pin Description</strong></p>
<div align="center">
	<table>
	  <tr>
	    <th rowspan="3"><strong>Pin Number</strong></th>
	    <th colspan="4"><strong>J18D100</strong></th>
	  </tr>
	  <tr>
	    <th rowspan="2"><strong>Port Name</strong></th>
	    <th rowspan="2"><strong>Signal Name</strong></th>
	    <th><strong>DIR</strong></th>
	    <th rowspan="2"><strong>Description</strong></th>
	  </tr>
	  <tr>
	    <th><strong>MCU ◄► J18D100</strong></th>
	  </tr>
	  <tr>
	    <td>1</td>
	    <td>5V</td>
	    <td>VCP_5P0</td>
	    <td>-</td>
	    <td>Power 5.0V</td>
	  </tr>
	  <tr>
	    <td>2</td>
	   <td>5V</td>
	    <td>VCP_5P0</td>
	    <td>-</td>
	    <td>Power 5.0V</td>
	  </tr>
	  <tr>
	    <td>3</td>
	    <td>22</td>
	    <td>GPIO_B24</td>
	    <td>◄►</td>
	    <td>GPIO signal</td>
	  </tr>
	  <tr>
	    <td>4</td>
	    <td>23</td>
	    <td>GPIO_B23</td>
	    <td>◄►</td>
	    <td>GPIO signal</td>
	  </tr>
	  <tr>
	    <td>5</td>
	    <td>24</td>
	    <td>GPIO_B22</td>
	    <td>◄►</td>
	    <td>GPIO signal</td>
	  </tr>
	  <tr>
	    <td>6</td>
	    <td>25</td>
	    <td>GPIO_B21</td>
	    <td>◄►</td>
	    <td>GPIO signal</td>
	  </tr>
	  <tr>
	    <td>7</td>
	    <td>26</td>
	    <td>GPIO_B20</td>
	    <td>◄►</td>
	    <td>GPIO signal</td>
	  </tr>
	  <tr>
	    <td>8</td>
	    <td>27</td>
	    <td>GPIO_B19</td>
	    <td>◄►</td>
	    <td>GPIO signal</td>
	  </tr>
	  <tr>
	    <td>9</td>
	    <td>28</td>
	    <td>GPIO_A30</td>
	    <td>◄►</td>
	    <td>GPIO signal</td>
	  </tr>
	  <tr>
	    <td>10</td>
	    <td>29</td>
	    <td>GPIO_A27</td>
	    <td>◄►</td>
	    <td>GPIO signal</td>
	  </tr>
	  <tr>
	    <td>11</td>
	    <td>230</td>
	    <td>GPIO_A26</td>
	    <td>◄►</td>
	    <td>GPIO signal</td>
	  </tr>
	  <tr>
	    <td>12</td>
	    <td>31</td>
	    <td>GPIO_A24</td>
	    <td>◄►</td>
	    <td>GPIO signal</td>
	  </tr>
	  <tr>
	    <td>13</td>
	    <td>32</td>
	    <td>GPIO_A25</td>
	    <td>◄►</td>
	    <td>GPIO signal</td>
	  </tr>
	  <tr>
	    <td>14</td>
	    <td>33</td>
	    <td>GPIO_A23</td>
	    <td>◄►</td>
	    <td>GPIO signal</td>
	  </tr>
	  <tr>
	    <td>15</td>
	    <td>34</td>
	    <td>GPIO_A22</td>
	    <td>◄►</td>
	    <td>GPIO signal</td>
	  </tr>
	  <tr>
	    <td>16</td>
	    <td>35</td>
	    <td>GPIO_A21</td>
	    <td>◄►</td>
		<td>GPIO signal</td>
	  </tr>
	  <tr>
	    <td>17</td>
	    <td>36</td>
	    <td>GPIO_A20</td>
	    <td>◄►</td>
	    <td>GPIO signal</td>
	  </tr>
	  <tr>
	    <td>18</td>
	    <td>37</td>
	    <td>GPIO_A19</td>
	    <td>◄►</td>
	    <td>GPIO signal</td>
	  </tr>
	  <tr>
	    <td>19</td>
	    <td>38</td>
	    <td>GPIO_K13</td>
	    <td>◄►</td>
		<td>GPIO signal</td>
	  </tr>
	  <tr>
	    <td>20</td>
	    <td>39</td>
	    <td>GPIO_K12</td>
	    <td>◄►</td>
	    <td>GPIO signal</td>
	  </tr>
	  <tr>
	    <td>21</td>
	    <td>40</td>
	    <td>GPIO_K11</td>
	    <td>◄►</td>
	    <td>GPIO signal</td>
	  </tr>
	  <tr>
	    <td>22</td>
	    <td>41</td>
	    <td>GPIO_A18</td>
	    <td>◄►</td>
	    <td>GPIO signal</td>
	  </tr>
	  <tr>
	    <td>23</td>
	    <td>42</td>
	    <td>GPIO_A17</td>
	    <td>◄►</td>
	    <td>GPIO signal</td>
	  </tr>
	  <tr>
	    <td>24</td>
	    <td>43</td>
	    <td>GPIO_A16</td>
	    <td>◄►</td>
	    <td>GPIO signal</td>
	  </tr>
	  <tr>
	    <td>25</td>
	    <td>44</td>
	    <td>GPIO_A11</td>
	    <td>◄►</td>
	    <td>GPIO signal</td>
	  </tr>
	  <tr>
	    <td>26</td>
	    <td>45</td>
	    <td>GPIO_A10</td>
	    <td>◄►</td>
	    <td>GPIO signal</td>
	  </tr>
	  <tr>
	    <td>27</td>
	    <td>46</td>
	    <td>GPIO_A09</td>
	    <td>◄►</td>
	    <td>GPIO signal</td>
	  </tr>
	  <tr>
	    <td>28</td>
	    <td>47</td>
	    <td>GPIO_A08</td>
	    <td>◄►</td>
	    <td>GPIO signal</td>
	  </tr>
	  <tr>
	    <td>29</td>
	    <td>48</td>
	    <td>GPIO_A05</td>
	    <td>◄►</td>
	    <td>GPIO signal</td>
	  </tr>
	  <tr>
	    <td>30</td>
	    <td>49</td>
	    <td>GPIO_A04</td>
	    <td>◄►</td>
	    <td>GPIO signal</td>
	  </tr>
	  <tr>
	    <td>31</td>
	    <td>50</td>
	    <td>GPIO_A03</td>
	    <td>◄►</td>
	    <td>GPIO signal</td>
	  </tr>
	  <tr>
	    <td>32</td>
	    <td>51</td>
	    <td>GPIO_A02</td>
	    <td>◄►</td>
	    <td>GPIO signal</td>
	  </tr>
	  <tr>
	    <td>33</td>
	    <td>52</td>
	    <td>GPIO_A01</td>
	    <td>◄►</td>
	    <td>GPIO signal</td>
	  </tr>
	  <tr>
	    <td>34</td>
	    <td>53</td>
	    <td>GPIO_A00</td>
	    <td>◄►</td>
	    <td>GPIO signal</td>
	  </tr>
	  <tr>
	    <td>35</td>
	    <td>GND</td>
	    <td>DGND</td>
	    <td>-</td>
	    <td>Ground</td>
	  </tr>
	  <tr>
	    <td>36</td>
	    <td>GND</td>
	    <td>DGND</td>
	    <td>-</td>
	    <td>Ground</td>
	  </tr>
	</table>
</div>

Table 4.13 shows the pin description of J5D100.
<p align="center"><strong>Table 4.13 J5D100 Pin Description</strong></p>
<div align="center">
	<table>
	  <tr>
	    <th rowspan="3"><strong>Pin Number</strong></th>
	    <th colspan="4"><strong>J5D100</strong></th>
	  </tr>
	  <tr>
	    <th rowspan="2"><strong>Port Name</strong></th>
	    <th rowspan="2"><strong>Signal Name</strong></th>
	    <th><strong>DIR</strong></th>
	    <th rowspan="2"><strong>Description</strong></th>
	  </tr>
	  <tr>
	    <th><strong>MCU ◄► J5D100</strong></th>
	  </tr>
	  <tr>
	    <td>1</td>
	    <td>3.3V</td>
	    <td>VCP_3P3</td>
	    <td>-</td>
	    <td>Power 3.3V</td>
	  </tr>
	  <tr>
	    <td>2</td>
	    <td>3.3V</td>
	    <td>VCP_3P3</td>
	    <td>-</td>
    <td>Power 3.3V</td>
	  </tr>
	  <tr>
	    <td>3</td>
	    <td>TX0</td>
	    <td>GPIO_K08</td>
	    <td>◄►</td>
	    <td>GPIO signal</td>
	  </tr>
	  <tr>
	    <td>4</td>
	    <td>RX0</td>
	    <td>GPIO_K01</td>
	    <td>◄</td>
	    <td>GPIO signal</td>
	  </tr>
	  <tr>
	    <td>5</td>
	    <td>TX1</td>
	    <td>GPIO_K09</td>
	    <td>◄►</td>
	    <td>GPIO signal</td>
	  </tr>
	  <tr>
	    <td>6</td>
	    <td>RX1</td>
	    <td>GPIO_K02</td>
	    <td>◄</td>
	    <td>GPIO signal</td>
	  </tr>
	  <tr>
	    <td>7</td>
	    <td>TX2</td>
	    <td>GPIO_K10</td>
	    <td>◄►</td>
	    <td>GPIO signal</td>
	  </tr>
	  <tr>
	    <td>8</td>
	    <td>RX2</td>
	    <td>GPIO_K03</td>
	    <td>◄</td>
	    <td>GPIO signal</td>
	  </tr>
	  <tr>
	    <td>9</td>
	    <td>GND</td>
	    <td>DGND</td>
	    <td>-</td>
	    <td>DGND</td>
	  </tr>
	  <tr>
	    <td>10</td>
	    <td>GND</td>
	    <td>DGND</td>
	    <td>-</td>
	    <td>DGND</td>
	  </tr>
	</table>
</div>

Figure 4.9 shows the total pin assignment of ten pin headers on the VCP-G.
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Hardware/4.9%20Total%20Pin%20Assignment%20of%20Pin%20Headers%20on%20TOPST%20VCP-G%20Board.png"></p>
<p align="center"><strong>Figure 4.9 Total Pin Assignment of Pin Headers on VCP-G </strong><p>

# References
  - Contact TOPST for more details: topst@topst.ai

**Note:** Reference documents can be provided whenever available, depending on the terms of a contract. If the reference documents are unavailable, the contents directly related to your development can be guided.
