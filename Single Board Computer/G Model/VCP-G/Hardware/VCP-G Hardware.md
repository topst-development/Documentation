# 1. Introduction
This document is a hardware user guide for the TOPST VCP-G based on the TCC7045 application processor. This document describes system installation, debugging, and detailed information on overall design and usage of the TOPST VCP-G board.

Table 1.1 describes the features of the TCC7045.

<p align="center"><strong>Table 1.1 Features of TCC7045</strong></p>
<table align="center">
  <tr>
    <td colspan="3">Part Name</td>
    <td>TCC7045</td>
  </tr>
  <tr>
    <td colspan="3">Package</td>
    <td>Package	Pin to Pin Compatible FBGA-196pin (12BD)</td>
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
    <td colspan="3">16-channel</td>
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
    <td>3-channel (Maximum 6-channel)</td>
  </tr>
  <tr>
    <td colspan="2">Dedicated I2C</td>
    <td>3-channel (Maximum 6-channel)</td>
  </tr>
  <tr>
  <tr>
    <td colspan="2">Dedicated GPSB (SPI)</td>
    <td>2-channel (Maximum 5-channel)</td>
  </tr>
    <tr>
    <td colspan="2">MFIO (Allocated UART, I2C, GPSB)</td>
    <td>3-channel</td>
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
    <td>-40 to 105℃</td>
  </tr>
</table>

</br>

## 1.1 Terminology
<p align="center"><strong>Table 1.2 Features of TCC7045</strong></p>
<table align="center">
  <tr>
    <td clospan="2"><strong>Terminology</strong></td>
    <td><strong>Definition</strong></td>
  </tr>
  <tr>
    <td clospan="2">ADC</td>
    <td>Analog to Digital Converter</td>
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
    <td>Micro-Controller Unit</td>
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

</br></br>

# 2. Block Diagram

</br>

## 2.1 System Block Diagram
Figure 2.1 shows the system block diagram of TOPST VCP-G board.
<p align="center"><img src= "../../Assets/TOPST VCP-G/Hardware/2.1 VCP-G System Block Diagram.png"></p>
<p align="center"><strong>Figure 2.1 System Block Diagram</strong></p>

</br></br>

# 3. TOPST VCP-G Overview
The TOPST VCP-G board can used for the following purposes:
  - System development
  - Training  
Table 3.1 describes the default configuration of the TOPST VCP-G board.

<p align="center"><strong>Table 3.1 Default Configuration of TOPST VCP-G Board</strong></p>
<table align="center">
  <tr>
    <td colspan="2"><strong>Board Name</strong></td>
    <td><strong>Description</strong></p>
  </tr>
  <tr>
    <td colspan="2">TOPST_VCP_V2.1.1</td>
    <td>MCU (TCC7045) board for TOPST</td>
  </tr>
</table>

</br>

# 3.1 TOPST VCP-G
Figure 3.1 shows the top view of TOPST VCP-G board
<p align="center"><img src= "../../Assets/TOPST VCP-G/Hardware/3.1 TOPST VCP-G Board (Top View) .png"></p>
<p align="center"><strong>Figure 3.1 TOPST VCP-G Board (Top View)</strong></p>

Table 3.2 describes connectors of TOPST VCP-G board (top view).
<p align="center"><strong>Table 3.2 Description of TOPST VCP-G Board (Top View)</strong></p>
<table align="center">
  <tr>
    <td colspan="4"><strong>Number</strong></td>
    <td><strong>Reference Number</strong></td>
    <td><strong>Name</strong></td>
    <td><strong>Description</strong></td>
  </tr>
  <tr>
    <td colspan="4">1</td>
    <td>J18D100</td>
    <td>36-Pin Header Female</td>
    <td>Header for GPIO & ADC</td>
  </tr>
  <tr>
    <td colspan="4">2</td>
    <td>J5D100</td>
    <td>10-Pin Header Male</td>
    <td>Header for CAN</td>
  </tr>
  <tr>
    <td colspan="4">3</td>
    <td>J3D100</td>
    <td>6-Pin Header Male</td>
    <td>Header for SPI</td>
  </tr>
  <tr>
    <td colspan="4">4</td>
    <td>J8D104</td>
    <td>8-Pin Header Female</td>
    <td>Header for GPIO & ADC</td>
  </tr>
  <tr>
    <td colspan="4">5</td>
    <td>J8D102</td>
    <td>8-Pin Header Female</td>
    <td>Header for GPIO</td>
  </tr>
  <tr>
    <td colspan="4">6</td>
    <td>J10D100</td>
    <td>10-Pin Header Female</td>
    <td>Header for GPIO & ADC</td>
  </tr>
  <tr>
    <td colspan="4">7</td>
    <td>J100</td>
    <td>10-Pin Header Male</td>
    <td>Header for JTAG</td>
  </tr>
  <tr>
    <td colspan="4">8</td>
    <td>SW100</td>
    <td>Tact Switch</td>
    <td>PORN: Initializes the system and the power management of TCC7045</td>
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
    <td>FWDN: Enter the Firmware download mode of TCC7045</td>
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
    <td>8-Pin Header Female</td>
    <td>Header for Power & Reset</td>
  </tr>  
  <tr>
    <td colspan="4">13</td>
    <td>J8D101</td>
    <td>8-Pin Header Female</td>
    <td>Header for GPIO & ADC</td>
  </tr>  
  <tr>
    <td colspan="4">14</td>
    <td>J8D103</td>
    <td>8-Pin Header Female</td>
    <td>Header for GPIO & ADC</td>
  </tr>    
</table>

Figure 3.2 shows the bottom view of the TOPST VCP-G board.  
**Note:** Figure 3.2 currently shows the TOPST_VCP-G_V1.1.1 board. This image will be updated to the TOPST_VCP-G_V2.1.1 board.
<p align="center"><img src="../../Assets/TOPST VCP-G/Hardware/3.2 TOPST VCP-G Board (Bottom View).png"></p>
<p align="center"><strong>Figure 3.2 TOPST VCP-G Board (Bottom View)</strong></p>

</br></br>

# 4. Specifications

</br>

## 4.1 Quad SPI Flash Memory (U101)
The information on the Quad SPI flash memory is as follows:
  - Density : 64 Mb  
  
**Note:** SNOR is not mounted on the TOPST VCP-G board as default.

</br>

## 4.2 Power In Connector (J101)
DC 12V is supplied to the TOPST VCP-G through the DC jack of J101 from a 12V adaptor.  
Figure 4.1 shows the location of J101.
<p align="center"><img src="../../Assets/TOPST VCP-G/Hardware/4.1 Power In Connector (J101).png"></p>
<p align="center"><strong>Figure 4.1 Power In Connector (J101)</strong><p>

</br>

## 4.3 Connector for JTAG (J100)
A JTAG emulator can be connected to the TOPST VCP-G through J100 for debugging. Figure 4.2 shows the location of J100.
<p align="center"><img src="../../Assets/TOPST VCP-G/Hardware/4.2 Connector for JTAG (J100).png"></p>
<p align="center"><strong>Figure 4.2 Connector for JTAG (J100)</strong><p>
Basically, JTAG is disabled. To enable JTAG, you must change the connections of R178 and R179. If TRSRn is set to high by R178, the MCU enters JTAG mode.

Table 4.1 describes the pins of J100.
<p align="center"><strong>Table 4.1 J100 Pin Description</strong></p>
<table align="center">

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

Table 4.2 describes the setting of JTAG Disable/Enable.
<p align="center"><strong>Table 4.2 Setting of JTAG Disable/Enable</strong></p>
<table align="center">
  <tr>
    <th colspan="4"><strong>Mode</strong></th>
    <th><strong>TRSTn Value</strong></th>
    <th><strong>R178</strong></th>
    <th><strong>R179</strong></th>
  </tr>
  <tr>
    <td colspan="4">Jtag Disable (Default)</td>
    <td>Low (1)</td>
    <td>N.C</td>
    <td>1K</td>
  </tr>
  <tr>
    <td colspan="4">JTAG Disable (Default)</td>
    <td>High (1)</td>
    <td>1K</td>
    <td>N.C</td>
  </tr>
</table>

</br>

## 4.4 FWDN Switch (SW101)
The TOPST VCP-G board has one pin for boot configuration using Boot Mode (BM) and supports 2 modes: UART FWDN mode and normal mode.   
Figure 4.3 shows the location of FWDN tact switch (SW101) and is used to select the boot modes of the TOPST VCP-G board.
<p align="center"><img src="../../Assets/TOPST VCP-G/Hardware/4.3 FWDN Tact Switch (SW101).png"></p>
<p align="center"><strong>Figure 4.3 FWDN Tact Switch (SW101)</strong><p>

Table 4.3 describes the boot mode selection using the FWDN tact switch (SW101).
<p align="center"><strong>Table 4.3 Description of Tact Switch (SW101) for Boot Mode</strong></p>
<table align="center">
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

### 4.4.1 FWDN Mode Method
There are two methods to enter FWDN mode.

#### 4.4.1.1 Method 1
While pressing the FWDN switch (SW101), connect the 12V power supply to turn on the TOPST VCP-G board.  
The FWDN red indicator  turns on when power is applied while the FWDN switch is pressed. After releasing FWDN switch (SW101), the MCU enters FWDN mode.  
Figure 4.4 shows how to enter FWDN mode by using method 1.
<p align="center"><img src="../../Assets/TOPST VCP-G/Hardware/4.4 Entering FWDN Mode by Using Method 1.png"></p>
<p align="center"><strong>Figure 4.4 Entering FWDN Mode by Using Method 1</strong><p>

#### 4.4.1.2 Method 2
While connecting the 12V power supply, press the FWDN switch (SW101) and then press the RESET switch (SW100).  
The FWDN red indicator turns on when the power is applied while the FWDN switch is pressed. The 3.3V green indicator turns off while the RESET switch is pressed. After releasing the FWDN switch (SW101), the MCU enters FWDN mode.  
Figure 4.5 shows the FWDN mode by using method 2.

<p align="center"><img src="../../Assets/TOPST VCP-G/Hardware/4.5 Entering FWDN Mode by Using Method 2.png"></p>
<p align="center"><strong>Figure 4.5 Entering FWDN Mode by Using Method 2</strong><p>

</br>

## 4.5 RESET Switch (SW100)
The TOPST VCP-G board has one RESET switch for power of RESET using PORN pin.  
Figure 4.6 shows the RESET tact switch (SW100).
<p align="center"><img src="../../Assets/TOPST VCP-G/Hardware/4.6 RESET Tact Switch (SW100).png"></p>
<p align="center"><strong>Figure 4.6 RESET Tact Switch (SW100)</strong><p>

### 4.5.1 4.5.1	RESET Tact Switch (SW100) Function
SW100 is a tact switch to reset the power block and system block in TCC7045.  
The function of this button is as follows:
  - Pressing the tack switch (SW100) while the power is on forces the power block to reset and the system of the TCC7045.

**Important:** Be careful when pressing the tack switch as the power suddenly turns off and data may be corrupted.

</br>

## 4.6 Connector for Debugging and FWDN (JC100)
The JC100 is a standard USB Type-C connector. On the TOPST VCP-G board, JC100 is used for debugging or FWDN via UART.  
Figure 4.7 shows the location of JC100.
<p align="center"><img src="../../Assets/TOPST VCP-G/Hardware/4.7 USB Type-C Connector (JC100).png"></p>
<p align="center"><strong>Figure 4.7 USB Type-C Connector (JC100)</strong><p>

You can perform FWDN or check debugging message of the TCC7045 through JC100.
JC100 on the TOPST VCP-G board includes a built-in USB-to-UART bridge controller, so you can directly connect JC100 to PC by using the USB Type-C cable.

</br>

## 4.7 Pin Headers for GPIO, ADC, Power, CAN, SPI
The TOPST VCP-G board have nine 2.54mm pin headers for power, GPIO, ADC, CAN, and SPI to connect others such as sensor or sub-board.  
Table 4.4 describes purpose of nine pin headers on the TOPST VCP-G board.
<p align="center"><strong>Table 4.4 Pin Headers on TOPST VCP-G Board</strong></p>
<table align="center">
  <tr>
    <td colspan="4"><strong>Number</strong></td>
    <td><strong>Reference Number</strong></td>
    <td><strong>Name</strong></td>
    <td><strong>Description</strong></td>
  </tr>
  <tr>
    <td colspan="4">1</td>
    <td>J18D100</td>
    <td>36-Pin Header Female</td>
    <td>Header for GPIO & ADC</td>
  </tr>
  <tr>
    <td colspan="4">2</td>
    <td>J5D100</td>
    <td>10-Pin Header Male</td>
    <td>Header for CAN</td>
  </tr>
  <tr>
    <td colspan="4">3</td>
    <td>J3D100</td>
    <td>6-Pin Header Male</td>
    <td>Header for SPI</td>
  </tr>
  <tr>
    <td colspan="4">4</td>
    <td>J8D104</td>
    <td>8-Pin Header Female</td>
    <td>Header for GPIO & ADC</td>
  </tr>
  <tr>
    <td colspan="4">5</td>
    <td>J8D102</td>
    <td>8-Pin Header Female</td>
    <td>Header for GPIO</td>
  </tr>
  <tr>
    <td colspan="4">6</td>
    <td>J10D100</td>
    <td>10-Pin Header Female</td>
    <td>Header for GPIO & ADC</td>
  </tr>
  <tr>
    <td colspan="4">7</td>
    <td>J8D100</td>
    <td>8-Pin Header FeMale</td>
    <td>Header for Power & Reset</td>
  </tr>
  <tr>
    <td colspan="4">8</td>
    <td>J8D101</td>
    <td>8-Pin Header Female</td>
    <td>Header for GPIO & ADC</td>
  </tr>
  <tr>
    <td colspan="4">9</td>
    <td>J8D103</td>
    <td>8-Pin Header Female</td>
    <td>Header for GPIO & ADC</td>
  </tr>
</table>

Figure 4.8 shows the location of pin headers on the TOPST VCP-G board.
<p align="center"><img src="../../Assets/TOPST VCP-G/Hardware/4.8 Pin Headers on TOPST VCP-G Board.png"></p>
<p align="center"><strong>Figure 4.8 Pin Headers on TOPST VCP-G Board</strong><p>

Table 4.5 shows the pin description of J10D100.
<p align="center"><strong>Table 4.5 J10D100 Pin Description</strong></p>
<table align="center">
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

Table 4.6 shows the pin description of J8D100.
<p align="center"><strong>Table 4.6 J8D100 Pin Description</strong></p>
<table align="center">
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
    <td>Voltage input for TOPST VCP-G</td>
  </tr>
</table>

Table 4.7 shows the pin description of J8D101.
<p align="center"><strong>Table 4.7 J8D101 Pin Description</strong></p>
<table align="center">
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

Table 4.8 shows the pin description of J8D102.
<p align="center"><strong>Table 4.8 J8D102 Pin Description</strong></p>
<table align="center">
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

Table 4.9 shows the pin description of J8D103.
<p align="center"><strong>Table 4.9 J8D103 Pin Description</strong></p>
<table align="center">
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

Table 4.10 shows the pin description of J8D104.
<p align="center"><strong>Table 4.10 J8D104 Pin Description</strong></p>
<table align="center">
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

Table 4.11 shows the pin description of J3D100.
<p align="center"><strong>Table 4.11 J3D100 Pin Description</strong></p>
<table align="center">
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

Table 4.12 shows the pin description of J18D100.
<p align="center"><strong>Table 4.12 J18D100 Pin Description</strong></p>
<table align="center">
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

Table 4.13 shows the pin description of J5D100.
<p align="center"><strong>Table 4.13 J5D100 Pin Description</strong></p>
<table align="center">
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

Figure 4.9 shows the total pin assignment of ten pin headers on the TOPST VCP-G.
<p align="center"><img src="../../Assets/TOPST VCP-G/Hardware/4.9 Total Pin Assignment of Pin Headers on TOPST VCP-G Board.png"></p>
<p align="center"><strong>Figure 4.9 Total Pin Assignment of Pin Headers on TOPST VCP-G Board</strong><p>

# References
  - Contact TOPST for more details: topst@topst.ai

**Note:** Reference documents can be provided whenever available, depending on the terms of a contract. If the reference documents are unavailable, the contents directly related to your development can be guided.
