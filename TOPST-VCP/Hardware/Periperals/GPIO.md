<h1 style="color:red">
  Standard 40-pin GPIO header
</h1>


This is a standard 40-pin GPIO header.  

Figure 1.1 shows the appearance of External CPU Interface Connector (J20D1).
<p align="center"><img src="https://github.com/Topst-Dev/Documentation/assets/161264431/2f34173f-32e3-413b-bc76-e545f0fb9205"></p>  

Figure 1.2 shows the schematic of a standard 40-pin GPIO header.
<p align="center"><img src="https://github.com/Topst-Dev/Documentation/assets/161264431/3bafd724-c0d9-4ea3-90d4-1640f28e55c6"></p>  

Table 4.8 shows the pin description of J20D1.  
|  Pin Numbe        | J1431 (TCC7045 Port Name | Signal Name | Dir | Description)                    |
|------------------|-------------------|-------------|-----|--------------------------------|
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
