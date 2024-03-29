<h1 style="color:red">
  Introduction
</h1>


This document is a hardware user guide for TOPST VCP based on the TCC7045 application processors.

Table 1.1 describes the features of the TCC7045.  

**Table 1.1 Features of TCC7045:**   

<table align="center">
  <td colspan="3">Part Name</td>
    <td>TCC7045</td>
  </tr>
  <td colspan="3">Package</td>
    <td>Pin to Pin Compatible FBGA-196pin (12BD)</td>
  </tr>
  <td colspan="3">CPU Frequency</td>
    <td>200MHz</td>
  </tr>
  <tr>
    <td rowspan="4">On-chip Memory</td>
    <td colspan="2">Program Flash</td>
    <td>4MB</td>
  </tr>
  <tr>
    <td colspan="2">SRAM</td>
    <td>512KB (Including Retention RAM 16KB</td>
  </tr>
  <tr>
    <td colspan="2">Data Flash</td>
    <td>128KB</td>
  </tr>
  <tr>
    <td colspan="2">DMA Channel</td>
    <td>22-channel</td>
  </tr>
  <tr>
    <td rowspan="12">Peripheral</td>
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
    <td colspan="2">Dedicated GPSB (SPI)</td>
    <td>2-channel (Maximum 5-channel)</td>
  </tr>
  <tr>
    <td colspan="2">MFIO (Allocated UART, I2C, GPSB)</td>
    <td>3-channel</td>
  <tr>
    <td rowspan="4">ADC</td>
    <td>Resulution</td>
    <td>12-bit SAR type</td>
  </tr>
  <tr>
    <td>Channels</td>
    <td>12-channel x 2groups</td>
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
  <td colspan="3">Power System</td>
    <td>3.3V Single</td>
  </tr>
  <td colspan="3">Temperature</td>
    <td>-40 ~ 105°C</td>
  </tr>
</table>




## Terminology  

**Table 1.2 terminology:**  

| Terminology | Definition                                              |
|-------------|---------------------------------------------------------|
| ACC         | Accessories Power                                       |
| GPIO        | General Purpose Input Output                            |
| ILL         | Illumination                                            |
| STR         | Suspend to RAM                                          |
| TOPST       | Total Open-Platform for System development and Training |
| VCP         | Vehicle Control Processor                               |


## Block Diagram

Figure 1.1 shows the system block diagram of TOPST VCP.  

<p align="center"><img src="https://github.com/Topst-Dev/Documentation/assets/161264431/176d5d74-3786-488c-95c3-30229d3babf9"></p>
<p align="center"><strong>Figure 1.1 Block Diagram</strong></p>

## TOPST VCP Overview
TOPST VCP can implement the following functions:
- Automotive Application
  - Car Audio Video Navigation (AVN)System, Digital Cluster, Head Up Display (HUD), etc.
- IOT Application
  - Smart Factory, Etc.
- Training & Education
  - Sensor, Actuator Application, CAN Application, Etc.


Table 1.3 Describes the default configuration of TOPST VCP.  

**Table 1.3 Default Configuration of TOPST VCP:**  

| Board Name | Description            |
|------------|------------------------|
| TOPST VCP  | TCC7045 MCU module     |  


Figure 1.2 shows the top view of TOPST VCP.  

<p align="center"><img src="https://github.com/Topst-Dev/Documentation/assets/161264431/e63e3885-df53-43d5-8807-12e5a016e677"></p>  


Table 1.4 describes connectors of TOPST VCP(top view).  

**Table 1.4 Description of TOPST VCP (Top View):**  

| Number | Reference  | Name                    | Description                                                       | 
|--------|------------|-------------------------|-------------------------------------------------------------------|
| 1      | SW7        | Slide Switch            | Test for ACC Signal ON/OFF                                        |
| 2      | SW3        | Slide Switch            | Test for Illumination (ILL) ON/OFF                                |
| 3      | SW8        | Slide Switch            | Test for STR Enable                                               |
| 4      | SW4, 6     | Tact Switch             | Test for ADC01 and KEY                                            |
| 5      | J2         | DC Jack                 | DC Power Input Jack                                               |
| 6      | RJ290      | Potentiometer           | Test for Illumination (ILL)                                       |
| 7      | J10D1      | 20-pin Pin Header Male  | Header for connecting MCU module with key sub-board               |
| 8      | SW1        | Tact Switch             | PORN: Initializes the system and the power management of TCC7045  |
| 9      | JC1        | USB Type-C Connector    | UART for debugging or FWDN port                                   |
| 10     | SW2        | Slide Switch            | Selects the boot mode of system                                   |
| 11     | J20D1      | 40-pin Pin Header Male  | Header for GPIO expander                                          |
| 12     | LED2, LED4 | LED                     | LED that indicates the status of MCU module                       |  

 
Figure 1.3 shows the bottom view of TOPST VCP.
<p align="center"><img src="https://github.com/Topst-Dev/Documentation/assets/161264431/18fea623-8eef-45a0-850b-f370c7881389"></p>  


Table 1.5 describes the connectors of TOPST VCP (bottom view).  

**Table 1.5 Description of TOPST VCP (Bottom View):**
| Number | Reference Number | Name           | Description                           |
|--------|------------------|----------------|---------------------------------------|
| 1      | J14D1            | 28-pin Header Female | Header for connecting MCU with external CPU |
