<h1 style="color:red">
  Standard 40-pin GPIO header
</h1>


This is a standard 40-pin GPIO header.  

Figure 1.1 shows the appearance of External CPU Interface Connector (J20D1).
<p align="center"><img src="https://github.com/Topst-Dev/Documentation/assets/161264431/2f34173f-32e3-413b-bc76-e545f0fb9205"></p>  

Figure 1.2 shows the schematic of a standard 40-pin GPIO header.
<p align="center"><img src="https://github.com/Topst-Dev/Documentation/assets/161264431/3bafd724-c0d9-4ea3-90d4-1640f28e55c6"></p>  

Table 1.1 shows the pin description of J20D1.  

**Table 1.1 J20D1 Pin Description:**  

|  Pin Number | TCC7045 Port Name | Signal Name | Dir(MCU◀▶J20D1)| Description                                   |
|:-----------:|:-----------------:|:-----------:|:--------------:|--------------|
| 1           |         -         | SYS_3P3     |       -        | Power 3.3V      |
| 2           |         -         | B_5P0       |       -        | Power 5.0V |
| 3           |  GPIO_B01         | I2C0_SDA    |      ◀▶      | I2C data       |
| 4           |         -         | B_5P0       |       -        | Power 5.0V       |
| 5           | GPIO_B00          | I2C0_SCL    |  ▶            | I2C Clock     |
| 6           |         -         | DGND        |       -        | Ground        |
| 7           | GPIO_B04          | GPIO_B04    |  ◀            | GPIO Signal  |
| 8           | GPIO_B25          | UT2_Tx      |  ▶            | UART Transmit      |
| 9           |         -         | DGND        |       -        | Ground      |
| 10          | GPIO_B26          | UT2_Rx      |  ▶            | UART Receive        |
| 11          | GPIO_B06          | GPIO_B06    |  ◀            | GPIO Signal     |
| 12          | GPIO_A16          | GPIO_A16    |  ◀            | GPIO Signal      |
| 13          | GPIO_B23          | GPIO_B23    |  ◀            | GPIO Signal       |
| 14          |         -         | DGND        |       -        | Ground     |
| 15          | GPIO_K11          | GPIO_K11    |  ◀            | GPIO Signal        |
| 16          | GPIO_AC04         | GPIO_AC04   |  ◀            | GPIO Signal       |
| 17          |         -         | SYS_3P3     |       -        | Power 3.3V    |
| 18          | GPIO_AC05         | GPIO_AC05   |  ◀            | GPIO Signal        |
| 19          | GPIO_A24          | SPI3_SDO    |  ▶            | SPI Data Output         |
| 20          |         -         | DGND        |       -        | Ground         |
| 21          | GPIO_A25          | SPI3_SDI    |  ◀            | SPI Data Input          |
| 22          | GPIO_K09          | GPIO_K09    |  ◀            | GPIO Signal          | 
| 23          | GPIO_A27          | SPI3_CLK    |  ▶            | SPI Clock           |
| 24          | GPIO_A26          | SPI3_CS     |  ▶            | SPI Chip Selection               |
| 25          |         -         | DGND        |       -        | Ground              |
| 26          | GPIO_C13          | SPI1_CS     |  ▶            | SPI Chip Selection           |
| 27          | GPIO_B03          | I2C1_SDA    |  ◀▶          | I2C data            |
| 28          | GPIO_B02          | I2C1_SCL    |  ▶            | I2C Clock          |
| 29          | GPIO_A29          | GPIO_A29    |  ◀            | GPIO Signal          |
| 30          |         -         | DGND        |       -        | Ground          |
| 31          | GPIO_B19          | GPIO_B19    |  ◀            | GPIO Signal          |
| 32          | GPIO_B11          | GPIO_B11    |  ◀            | GPIO Signal          |
| 33          | GPIO_C11          | GPIO_C11    |  ◀            | GPIO Signal          |
| 34          |         -         | DGND        |       -        | Ground          |
| 35          | GPIO_C15          | SPI1_DI     |  ◀            | SPI Data Input         |
| 36          | GPIO_B18          | GPIO_B18    |  ◀            | GPIO Signal          |
| 37          | GPIO_A18          | GPIO_A18    |  ◀            | GPIO Signal          |
| 38          | GPIO_C14          | SPI1_DO     |  ▶            | SPI Data Output          |
| 39          |         -         | DGND        |       -        | Ground           |
| 40          | GPIO_C12          | SPI1_CLK    |  ▶            | SPI Clock          |

