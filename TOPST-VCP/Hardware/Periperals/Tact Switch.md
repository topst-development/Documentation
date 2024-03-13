<h1 style="color:red">
  Tact Switch (SW1, SW4, SW6)
</h1>


The TOPST VCP has three tact switches for PORN (SW1), ADC01 (SW4), KEY0 (SW6).  

Figure 1.1 shows the location of the tact switch (SW1).  
<p align="center"><img src="https://github.com/Topst-Dev/Documentation/assets/161264431/6b1f58e9-403e-4198-affc-802f54b9047c"</p>  
<p align="center"><strong>Figure 1.1 Tact Switch (SW1)</strong></p>


Figure 1.2 shows the location of the tact switch (SW4, SW6).
<p align="center"><img src="https://github.com/Topst-Dev/Documentation/assets/161264431/c36b6b47-a028-426e-ad21-ec2f05cc7cd8"</p>
<p align="center"><strong>Figure 1.2 Tact Switch (SW4, SW6)</strong></p>



Figure 1.3 shows the schematic of tack switch (SW1).
<p align="center"><img src="https://github.com/Topst-Dev/Documentation/assets/161264431/8ff11f85-39a5-42cc-827c-32b92b2b6a6e"></p>  
<p align="center"><strong>Figure 1.3 Schematic of Tact Switch</strong></p>


Figure 1.4 shows the schematic of tack switch (SW4, SW6).
<p align="center"><img src="https://github.com/Topst-Dev/Documentation/assets/161264431/d0fe379c-3828-457c-9b2a-d38106b32416"</p>
<p align="center"><strong>Figure 1.4 Schematic of Tact Switch (SW4, SW6)</strong>


## Tact Switch (SW1)  
SW1 is a tact switch to reset the power block and system block in Main Processor Unit, TCC7045. The function of this button is as follows:  
- Pressing the tack switch (SW1) in the power on state forces the power block to reset and the system of the TCC7045 to restart.
- Be careful when pressing the tack switch as the power may suddenly turn off and data may be corrupted.


## Tact Switch (SW4, SW6)
SW4, SW6 is a tact switch to input a low signal in Main Processor Unit, TCC7045. The function of this button is as follows:  
- Pressing the tack switch (SW4, SW6) inputs a low signal to ADC or GPIO port of the TCC7045.
- This allows that multiple operations may be executed.

