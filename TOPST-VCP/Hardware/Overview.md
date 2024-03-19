<h1 style="color:red">
  Introduction
</h1>


This document is a hardware user guide for TOPST VCP based on the TCC7045 application processors.

Table 1.1 describes the features of the TCC7045.  

**Table 1.1 Features of TCC7045:** 

| Part Name        | TCC7045                                  |
|------------------|------------------------------------------|
| Package          | Pin to Pin Compatible FBGA-196pin (12BD) |
| CPU Frequency    | 200MHz                                   |
| On-chip Memory   |                                          |
| - Program Flash  | 4 MB                                     |
| - SRAM           | 512 KB (Including Retention RAM 16 KB)   |
| - Data Flash     | 128 KB                                   |
| DMA Channel      | 22-channel                               |
| Peripheral       |                                          |
| - Ethernet       | 1 Gbps with AVB                          |
| - CAN/CANFD      | 3-channel                                |
| - Dedicated LIN/UART | 3-channel (Maximum 6-channel)        |
| - Dedicated I2C  | 3-channel (Maximum 6-channel)            |
| - Dedicated GPSB (SPI) | 2-channel (Maximum 5-channel)      |
| - MFIO (Allocated UART, I2C, GPSB) | 3-channel              |
| - ADC            |                                          |
|   - Resolution  | 12-bit SAR type                           |
|   - Channels    | 12-channel x 2 groups                     |
|   - Input Range | 3.3V                                      |
|   - Sample Rate | Over 1.0 MSPs                             |
| - I2S            | 1-channel                                |
| - Serial Flash Interface | Quad SPI                         |
| Power System     | 3.3V single                              |
| Temperature      | -40 ~ 105℃                              |


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
