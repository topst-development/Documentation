<h1 style="color:red">
  Tact Switch (SW1, SW4, SW6)
</h1>


The TOPST VCP has three tact switches for PORN (SW1), ADC01 (SW4), KEY0 (SW6).  

Figure 1.1 shows the appearance of the tact switch (SW1).  
<p align="center"><img src="https://github.com/Topst-Dev/Documentation/assets/161264431/73f2bd2c-d1f2-42a7-bf6c-efdbecc5b043"</p>  


Figure 1.2 shows the appearance of the tact switch (SW4, SW6).
<p align="center"><img src="https://github.com/Topst-Dev/Documentation/assets/161264431/2fa792e6-9bd3-46c6-b4da-b64d04fc34f3"</p>  


Figure 1.3 shows the schematic of tack switch (SW1).
<p align="center"><img src="https://github.com/Topst-Dev/Documentation/assets/161264431/8f16f6a0-808e-422a-b95f-163efe22bdd3"</p>  


Figure 1.4 shows the schematic of tack switch (SW4, SW6).
<p align="center"><img src="https://github.com/Topst-Dev/Documentation/assets/161264431/c11ffcfe-d45e-4fe4-9e5c-a14c6e307c4a"</p>  


## Tact Switch (SW1)  
SW1 is a tact switch to reset the power block and system block in TCC7045. The function of this button is as follows:  
- Pressing the tack switch (SW1) in the power on state forces the power block to reset and the system of the TCC7045 to restart.
- Be careful when pressing the tack switch as the power may suddenly turn off and data may be corrupted.


## Tact Switch (SW4, SW6)
SW4, SW6 is a tact switch to input a low signal in TCC7045. The function of this button is as follows:  
- Pressing the tack switch (SW4, SW6) inputs a low signal to ADC or GPIO port of the TCC7045.
- This allows that multiple operations may be executed.

