# I2C

The inter-integrated circuit (I2C) is easily read as "i-to-c", but the formal pronunciation is "i-square-c".

The I2C communication consists of one line SDA for transmitting and receiving data and one clock line SCL for synchronizing transmission and reception timing. The I2C communication consists of one master and one or more slaves, and up to 127 slaves can be connected.

- I2C communication is a communication method using two lines
- Strengths and weaknesses of connecting multiple slave devices to a single master
- Time-free advantage because it is a synchronous communication method that uses clock signals
- The disadvantage of being unsuitable for long data because address data is always attached for slave selection

```bash
$ man i2cdetect
 
i2cdetect - detect I2C chips
 
i2cdetect [-y] [-a] [-q|-r] i2cbus [first last]
i2cdetect -F i2cbus
i2cdetect -V
i2cdetect -l
```

**Description**
i2cdetect is a userspace program used to scan an I2C bus for devices. i2cdetect outputs a table with the list of detected devices on the specified bus. i2cbus indicates the number or name of the I2C bus to be scanned, and should correspond to one of the buses listed by i2cdetect -l. The optional parameters first and last restrict the scanning range (default: from 0x03 to 0x77).
i2cdetect can also be used to query the functionalities of an I2C bus (see option -F.)
 
**Caution**: This program can confuse your I2C bus, cause data loss or worse.
 
Interpreting the Output
Each cell in the output table will contain one of the following symbols:
  "--". The address was probed but no chip answered.
  "UU". Probing was skipped because this address is currently in use by a driver. This strongly suggests that there is a chip at this address.
  An address number in hexadecimal such as "2d" or "4e". A chip was found at this address.
 
OptionsDescription-yn  Disable interactive mode. By default, i2cdetect will wait for a confirmation from the user before messing with the I2C bus. When this flag is used, it will perform the operation directly. This is mainly meant to be used in scripts.-an  Force scanning of non-regular addresses. Not recommended.-qn  Use SMBus "quick write" commands for probing (by default, the command used is the one believed to be the safest for each address). Not recommended. This is known to corrupt the Atmel AT24RF08 EEPROM found on many IBM Thinkpad laptops.-rn  Use SMBus "read byte" commands for probing (by default, the command used is the one believed to be the safest for each address). Not recommended. 
n  This is known to lock SMBus on various write-only chips (most notably clock chips at address 0x69).-Fn  Display the list of functionalities implemented by the adapter and exit-Vn  Display the version and exit-ln  Output a list of installed buses 

<p align="center">
    <img src="https://github.com/Topst-Dev/Documentation/assets/144076415/27b6d33d-f18f-4f09-bcb8-eeca28109636" width="800" height="150">
</p>
<p align="center"><strong>Figure 1.1 I2C Device</strong></p>

```bash
$ pip install RPLCD
$ rplcd-tests i2c testsuite expander=PCF8574 addr=0x3f port=1 cols=16 rows=2 charmap=A00
```

As shown in Figure 1.2, **addr** should be checked and written appropriately in the above command.

<p align="center">
    <img src="https://github.com/Topst-Dev/Documentation/assets/144076415/7e38a522-177f-447a-82d2-4a219b0319ae" width="600" height="250">
</p>
<p align="center"><strong>Figure 1.2 Check addr</strong></p>

<p align="center">
    <img src="https://github.com/Topst-Dev/Documentation/assets/144076415/1f21dfbe-2983-4983-88ff-a75199a4370d" width="500" height="700">
</p>
<p align="center"><strong>Figure 1.3 I2C LCD Test</strong></p>
