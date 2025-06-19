# 1. Introduction
---
This document describes how to use Arduino IDE for the TOPST Vehicle Control Processor (VCP), which is a powerful and efficient processor designed for automotive applications and based on the Telechips TCC7045. The goal is to integrate the VCP-G with the Arduino environment to provide a development environment that parallels the simplicity and flexibility of Arduino, specifically tailored for automotive semiconductors, and simplify and expedite the development process.  

This document includes information on the following:  
- Installation Guide

</br></br></br></br>

# 2. Installation Guide
---
This chapter describes how to download and install the VCP-G Arduino packageto use with the Arduino Integrated Development Environment (IDE).

</br></br></br>

## 2.1 Installation Guide
---
**Step 1: Download the Arduino IDE**

First, you need the Arduino IDE which serves as the platform to program your Arduino boards.  
1. Visit the official Arduino website : [Arduino Software](https://www.arduino.cc/en/software)
2. Select the version suitable for your operating system (Windoiws, macOS, or Linux).
3. Download and run the installer.

**Step 2: Install the Arduino IDE**  
Follow these steps based on your operating system to install the Arduino IDE:  

- Windows:
    1. Execute the downloaded .exe file.
    2. Follow the installation prompts. Ensure you install all the necessary drivers.
- macOS:
    1. Open the .dmg file
    2. Drag the Arduino application to your Applications folder
- Linux:
    1. unpack the .tar.xz file.
    2. Open a terminal in the extracted directory.
    3. Run ./install.sh to install.

**Step 3: Adding the VCP-G**  
To program the VCP-G, you need to add the VCP-G .json file to the Arduino IDE Through the Board Manager.
1. Open the Arduino IDE.
2. Navigate to **File > Preferences**.
3. In the **"Additional Board Manager URLs"** field, add the following URL:
    ```
    https://raw.githubusercontent.com/topst-development/VCP-Arduino_Board_Manager/main/package_topst_vcp_index.json
    ```
4. Click **OK** button to save your changes.
5. Go to **Tools > Board > Boards Manager.**
6. Search for “TOPST VCP-G” in the Boards Manager.
7. When the TOPST VCP-G entry appears, select v1.0.0 from the dropdown menu and click Install button.

**Step 4: Selecting the VCP-G**  
After installation, you need to select the TOPST VCP-G board:  
1. Go to **Tools > Board** in the Arduino IDE.
2. Scroll down to find "TOPST VCP-G" and select it.

**Step 5: Verify Installation**  
Test if your setup works by uploading a simple sketch:
1. Connect the VCP-G board to your PC by USB.
2. Select the appropriate port under **Tools > Port**.
3.	Open **File > Examples > 01.Basics > Blink**.
4.	Click **Upload** button to transfer the sketch to the board.  
    **Note:** If the upload process gets stuck in an infinite uploading state, it may be due to the FWDN mode not being activated. Disconnect the power cable, press and hold the FWDN switch, reconnect the power cable, and then release the button. If the issue persists, try running the Arduino IDE with administrator privileges.
5.	If the onboard LED starts blinking, the board is set up correctly.

</br></br></br>

## 2.2 Troubleshooting
---
If you encounter any issues during the setup, refer to the [Arduino Troubleshooting Guide](https://www.arduino.cc/en/Guide/Troubleshooting).  
For more information and advanced features, refer to VCP-G documentation or visit [Arduino Help Center](https://support.arduino.cc/hc/en-us).

</br></br></br></br>

# 3. References
---
- Contact TOPST for more details: topst@topst.ai

**Note:** Reference documents can be provided whenever available, depending on the terms of a contract. If the reference
documents are unavailable, the contents directly related to your development can be guided.

