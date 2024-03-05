<h1 style="color:red">
  Introduction
</h1>


This document serves as a hardware user guide for TOPST VCP based on the TCC7045 application processors. It provides information on system installation, debugging, and detailed insights into the overall design and usage of TOPST VCP.


## Table 1.1: Features of TCC7045
| Part Name        | TCC7045                              |
|------------------|--------------------------------------|
| Package          | Pin to Pin Compatible FBGA-196pin (12BD) |
| CPU Frequency    | 200MHz                               |
| On-chip Memory   |                                      |
| - Program Flash  | 4 MB                                 |
| - SRAM           | 512 KB (Including Retention RAM 16 KB) |
| - Data Flash     | 128 KB                               |
| DMA Channel      | 22-channel                           |
| Peripheral       |                                      |
| - Ethernet       | 1 Gbps with AVB                      |
| - CAN/CANFD      | 3-channel                            |
| - Dedicated LIN/UART | 3-channel (Maximum 6-channel)    |
| - Dedicated I2C  | 3-channel (Maximum 6-channel)        |
| - Dedicated GPSB (SPI) | 2-channel (Maximum 5-channel)   |
| - MFIO (Allocated UART, I2C, GPSB) | 3-channel     |
| - ADC            |                                      |
|   - Resolution  | 12-bit SAR type                      |
|   - Channels    | 12-channel x 2 groups                |
|   - Input Range | 3.3V                                 |
|   - Sample Rate | Over 1.0 MSPs                        |
| - I2S            | 1-channel                            |
| - Serial Flash Interface | Quad SPI                        |
| Power System     | 3.3V single                          |
| Temperature      | -40 ~ 105℃                          |


## Terminology
| Terminology | Definition                          |
|-------------|-------------------------------------|
| ACC         | Accessories Power                   |
| AP          | Application Processor               |
| AVB         | Audio Video Bridging                |
| BU          | Battery Unit                        |
| EVB         | Evaluation Board                    |
| GPIO        | General Purpose Input Output        |
| ILL         | Illumination                        |
| SDM         | Safe Display Manager                |
| STR         | Suspend to RAM                      |
| TOPST       | Total Open-Platform for System development and Training |
| VCP         | Vehicle Control Processor           |


## Block Diagram

  Figure 2.1 shows the system block diagram of TOPST VCP .
![Figure 2.1: System Block Diagram of TOPST VCP](https://github.com/Topst-Dev/Documentation/assets/161264431/b94d77ad-de93-4ee0-87c3-81dbb346fc02](https://github.com/Topst-Dev/Documentation/assets/161264431/bb5bbfdb-4fe0-4cfa-a8a2-0b7217bc07f7))
### Figure 2.1 System Block Diagram

## TOPST VCP Overview
TOPST VCP can implement the following functions:
- Car Audio Video Navigation (AVN) System
- Digital Cluster
- Head Up Display (HUD)
- Training & ...


## Table 3.1: Default Configuration of TOPST VCP
| Board Name | Description            |
|------------|------------------------|
| TOPST VCP  | TCC7045 MCU module     |


## Figure 3.1: TOPST VCP (Top View)
![Figure 3.1: TOPST VCP (Top View)](https://github.com/Topst-Dev/Documentation/assets/161264431/7c88cc0a-7814-43d8-8931-d10833bc92c2)
### Figure 3.1 TOPST VCP (Top View)

## Table 3.2: Description of TOPST VCP (Top View)
| Number | Reference | Name          | Description                               |
|--------|-----------|---------------|-------------------------------------------|
| 1      | SW7       | Slide Switch  | Test for ACC Signal ON/OFF                |
| 2      | SW3       | Slide Switch  | Test for Illumination (ILL) ON/OFF         |
| 3      | SW8       | Slide Switch  | Test for STR Enable                        |
| ...    | ...       | ...           | ...                                       |


## Figure 3.2: TOPST VCP (Bottom View)
![Figure 3.2: TOPST VCP (Bottom View)](https://github.com/Topst-Dev/Documentation/assets/161264431/6dd493c5-01b5-4425-a711-10c76a24eee2)
### Figure 3.2 TOPST VCP (Bottom View)


## Table 3.3: Description of TOPST VCP (Bottom View)
| Number | Reference Number | Name           | Description                           |
|--------|------------------|----------------|---------------------------------------|
| 1      | J14D1            | 28-pin Header Female | Header for connecting MCU with external CPU |
