# TOPST Imager User Guide

TOPST Imager is an application for installing an operating system or firmware on a TOPST board.

You do not need to be familiar with computers or electronic devices. Follow this guide slowly, one step at a time, together with the instructions shown in the application.

> **Important:** Flashing may erase everything stored in the board's eMMC. Back up any files you need before you begin.

## 1. Helpful Terms

| Term shown in the application | Simple meaning |
| --- | --- |
| Board | The TOPST device on which you will install the operating system. |
| Image | The operating system file that will be installed on the board. |
| Flashing | The process of installing an image file on the board. |
| Boot mode | A special state that allows the computer to install an image on the board. |
| FWDN | The internal tool that installs an image on a TOPST board. You do not need to run it yourself. |
| COM port | The name the computer uses to identify a board connected by USB. |
| eMMC | Storage built into the board. |

## 2. Supported Boards and Image Files

| Board | Custom image format | Required connection |
| --- | --- | --- |
| TOPST D3-G | `.fai` | FWDN USB Type-C data cable |
| TOPST AI-G | `.fai` | FWDN USB Type-C data cable and Ethernet cable |
| TOPST VCP-G | `.rom` | FWDN USB Type-C data cable |

> A charge-only USB cable will not work. Use a **USB Type-C cable that supports data transfer**.

## 3. Before You Begin

Check each item below.

- The TOPST board you want to flash
- The board's power adapter
- A USB Type-C cable that supports data transfer
- A computer connected to the internet
- An Ethernet cable if you are using AI-G
- Enough free space on the computer to download and extract the official image
- A backup of any important data stored on the board

Do not do any of the following while flashing is in progress.

- Do not turn off the board.
- Do not disconnect the USB or Ethernet cable.
- Do not close TOPST Imager.
- Do not turn off the computer or let it enter sleep mode.

## 4. Basic Process

The basic process is the same on Windows and Linux.

1. Start TOPST Imager.
2. Select the board you want to use.
3. Select an operating system or **Custom Image**.
4. Select the version you want to install.
5. Follow the connection and boot mode instructions shown in the application.
6. Start flashing.
7. Wait until the **Complete** screen appears.

You can click an item once and then select **Next**, or double-click the item to move to the next screen.

---

# Windows Instructions

## 1. Installing TOPST Imager on Windows

### 1.1 Supported Systems

- Windows 10 64-bit or later
- Windows 11 64-bit

### 1.2 Install the Application

1. Download the Windows version of `TOPST Imager.exe` from the official TOPST website.
2. Double-click the downloaded `TOPST Imager.exe` file.
3. Read and accept the license agreement.
4. Select the desktop shortcut option if you want a shortcut.
5. Select **Install**.
6. When installation is complete, select **Launch TOPST Imager**, and then finish the setup.

If Windows displays a protection message, first make sure the installer came from the official TOPST website. Do not run an installer if you cannot confirm its source.

The default installation location is:

```text
%LOCALAPPDATA%\Programs\TOPST Imager
```

## 2. Language and Display Theme

1. Select **App Options** at the bottom-left corner of the window.
2. Select the language you want to use.
3. Select **Save**.

> The red boxes and numbers in the screenshots were added for this guide. They do not appear in the actual application.

![Selecting the language and support options in TOPST Imager](https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/Quick%20Guide/TOPST%20Imager%20App%20Options.png)

1. **Language:** Select the language you want to use.
2. **Ask the Community:** Open the TOPST community when you need help.
3. **Save:** Apply the selected language.

TOPST Imager supports Korean, English, Japanese, Simplified Chinese, Traditional Chinese, Thai, and German. The light or dark appearance follows the Windows system theme automatically.

## 3. Installing an Official Image

### 3.1 Select a Board

1. Check the board picture and name.
2. Click the board you want to use once.
3. Make sure the selected item changes color.
4. Select **Next**.

![Selecting the D3-G board and the Next button in TOPST Imager](https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/Quick%20Guide/TOPST%20Imager%20Board%20Selection.png)

1. Select the **board item** you want to use.
2. Confirm that it is selected, and then select **Next**.

If you selected the wrong board, select **Back** and choose again.

### 3.2 Select an Operating System and Version

1. Select the operating system you want to install, and then select **Next**.
2. Select the version you want to install.
3. Check the release date and file sizes.

![Selecting an official operating system or custom image in TOPST Imager](https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/Quick%20Guide/TOPST%20Imager%20OS%20Selection.png)

1. To use an official image, select the **operating system** you want.
2. To use a file already stored on your computer, select **Use Custom Image**.
3. Confirm the selection, and then select **Next**.

![Selecting an operating system version and the Flashing button in TOPST Imager](https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/Quick%20Guide/TOPST%20Imager%20Version%20Selection.png)

1. Select the **version** you want to install and check its download size and release date.
2. If the selection is correct, select **Flashing**.

The sizes shown on the screen have the following meanings.

- **Download size:** The size of the compressed file downloaded from the internet
- **Extracted size:** The estimated space needed on the computer after the file is extracted

The newest version is not always required. Unless you have received different instructions, select the recommended version or the latest stable version.

### 3.3 Confirm the Erase Warning

Before flashing starts, TOPST Imager warns you that the contents of the board's eMMC may be erased.

1. Check the selected board and image again.
2. Make sure there is no data on the board that you still need.
3. When you are ready, select the confirmation button.

![The eMMC erase warning with Cancel and Confirm buttons](https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/Quick%20Guide/TOPST%20Imager%20eMMC%20Erase%20Warning.png)

1. Select **Cancel** if you are not ready or want to check your selection again.
2. Select **Confirm** only after you understand that the eMMC contents may be erased.

If you are unsure, select **Cancel**. Canceling at this point will not erase the board.

## 4. Flashing D3-G

### 4.1 Step 1: Install the Driver

1. Select **Install Driver**.
2. If Windows asks for administrator permission, check the message and select **Yes**.
3. Follow the VTC driver installer until installation is complete.
4. Return to TOPST Imager.
5. Select **Driver Installation Complete**.

![D3-G VTC driver installation instructions in TOPST Imager](https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/Quick%20Guide/TOPST%20Imager%20D3-G%20Driver%20Installation.png)

1. First select **Install Driver** to start the installer.
2. Complete every step in the installer, and then select **Driver Installation Complete**.

You normally need to install the driver only once on each computer.

### 4.2 Step 2: Enter Boot Mode and Detect the Board

Watch the board picture and the flashing markers on the screen, and follow these steps.

1. **Press the BOOT button** on the board.
2. Keep holding the BOOT button.
3. **Press and release the RESET button.**
4. Release the BOOT button.
5. Make sure the USB Type-C cable is firmly connected to the computer and the board.
6. Check whether the application detects the board.

![D3-G boot mode and board detection screen in TOPST Imager](https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/Quick%20Guide/TOPST%20Imager%20D3-G%20Boot%20Mode.png)

1. Follow the boot mode sequence while watching the board picture and flashing markers.
2. After changing a connection, select **Check Again**.
3. When the board is detected, **Continue Flashing** becomes available.

In Windows Device Manager, the board may appear with a name similar to `Telechips TCCxxxx VTC USB Driver`.

### 4.3 Step 3: Flash the Image

1. Select **Start Flashing**.
2. Watch the download, extraction, and flashing progress.
3. Wait until the completion screen appears.

## 5. Flashing AI-G

AI-G uses both a USB connection and an Ethernet connection.

### 5.1 Step 1: Set Up Ethernet

1. Connect the computer and AI-G with an Ethernet cable.
2. Select the Ethernet adapter connected to AI-G.
3. Follow the instructions to set the computer's address to `192.168.0.8/24`.
4. Confirm that the network setup is complete.

Select the **wired Ethernet adapter connected to AI-G**, not the Wi-Fi adapter.

### 5.2 Step 2: Enter Boot Mode and Select a COM Port

1. Press the BOOT button while watching the animation.
2. While holding BOOT, press and release the RESET button.
3. Release the BOOT button.
4. Select the newly detected AI-G USB COM port.
5. Check the board power, USB Type-C cable, and Ethernet cable again.

If several COM ports are listed, temporarily disconnect the AI-G USB cable. The port that disappears is the AI-G port. Reconnect the cable and repeat the boot mode sequence before continuing.

### 5.3 Step 3: Flash the Image

1. Select **Start Flashing**.
2. Wait until the progress reaches 100%.
3. Restart the board after the completion screen appears.

## 6. Flashing VCP-G

### 6.1 Step 1: Enter Boot Mode

1. Check the board picture on the screen.
2. Press and hold the BOOT button.
3. Press and release the RESET button.
4. Release the BOOT button.
5. Select **Next**.

### 6.2 Step 2: Select a COM Port

1. Select the USB COM port connected to VCP-G.
2. If the port is not listed, reconnect the USB Type-C cable.
3. Refresh the list and select the correct port.

### 6.3 Step 3: Flash the Image

1. Select **Start Flashing**.
2. Wait until the progress reaches 100%.
3. Restart the board after the completion screen appears.

## 7. Installing a Custom Image

Use this option to install a local image file that is not listed in the official catalog.

1. On the operating system selection screen, click **Custom Image** once.
2. Select **Next**, or double-click the item.
3. Use either of the following methods.
   - Drag the file into the dotted area.
   - Select **Browse for FAI Image** or **Browse for ROM Image**, and then select the file.
4. Check the selected file name.
5. Select **Next** and follow the connection instructions for your board.

Make sure you select the correct file type.

- D3-G: `.fai`
- AI-G: `.fai`
- VCP-G: `.rom`

Because a custom image is already stored on your computer, the download and extraction steps are not shown on the flashing screen.

## 8. Troubleshooting on Windows

### The Board Is Not Detected

Check the following items in order.

1. Make sure the board has power.
2. Make sure the USB cable is not a charge-only cable.
3. Make sure the cable is connected to the FWDN USB Type-C port.
4. Repeat the boot mode sequence.
5. For D3-G, make sure the VTC driver is installed.

### No COM Port Is Listed

1. Disconnect and reconnect the USB cable.
2. Check the board power.
3. Enter boot mode again.
4. Refresh the COM port list.

### AI-G Shows a Network Error

1. Check the Ethernet cable between AI-G and the computer.
2. Make sure you selected the wired Ethernet adapter, not Wi-Fi.
3. Make sure the computer's address is `192.168.0.8/24`.
4. Follow the application instructions and start again from Step 1.

### A `Failed open port` or `GetLastError : 22` Message Appears

Check the FWDN USB Type-C cable connection. Reconnect the cable, and then repeat the process from the boot mode step.

### The Download Does Not Progress

1. Check the internet connection.
2. Check the free storage space on the computer.
3. Wait a moment, and then select **Retry**.

### You Want to Return to the Previous Step While Flashing

If flashing has started, a cancellation confirmation window appears when you go back. Before canceling, check that the board is in a safe state and follow the instructions shown on the screen.

### You Need Help with an Error

1. Copy the details from the error window.
2. Open the log folder from **App Options**.
3. Prepare the error message and log file.
4. Ask a question in the [TOPST Community](https://community.topst.ai/).

On Windows, logs are normally stored in:

```text
%LOCALAPPDATA%\Telechips\TOPST Imager\logs\topst-imager.log
```

---

# Linux Instructions

## 1. Before Using TOPST Imager on Linux

The screens and basic process are the same on Linux and Windows, but some preparation steps are different.

The board, operating system, and version buttons are in the same locations shown in the Windows screenshots above. On Linux, the Windows driver installation screen for D3-G is skipped, and the application moves directly to boot mode and board detection.

- Do not install the Windows VTC driver.
- D3-G requires Linux USB permissions.
- AI-G and VCP-G require serial port permissions.
- The distribution package must include Linux FWDN executables.
- `unzip` or `bsdtar` is required to extract official images.

If you are not comfortable entering commands, ask a system administrator or developer to complete the **Linux Administrator Setup** section below. After this one-time setup, a general user can follow the on-screen instructions.

## 2. Installing and Running TOPST Imager on Linux

The examples below use Ubuntu.

### 2.1 Extract the Package

1. Download the correct Linux package for your computer from the official TOPST website.
2. Open the Downloads folder.
3. Open a terminal and enter the following commands.

```bash
cd ~/Downloads
tar -xzf TOPST-Imager-<version>-Linux-<architecture>.tar.gz
```

Replace `<version>` and `<architecture>` with the values in the actual file name. You can type the beginning of the file name and press `Tab` to complete it automatically.

### 2.2 Run the Application

Move to the extracted folder, and then start the application.

```bash
cd TOPST-Imager-<version>-Linux-<architecture>
chmod +x topst-imager
./topst-imager
```

If an error says that a `Qt` library is missing, the current Linux package does not include the Qt runtime. General users should ask the distributor for a **Linux package that includes the Qt 6.12 runtime** instead of trying to install it manually.

## 3. Linux Administrator Setup

These settings normally need to be completed only once.

### 3.1 Install an Extraction Tool

```bash
sudo apt update
sudo apt install unzip
```

### 3.2 Serial Port Permissions for AI-G and VCP-G

```bash
sudo usermod -aG dialout "$USER"
```

After running the command, sign out and sign in again, or restart the computer.

### 3.3 USB Permissions for D3-G

1. Connect D3-G in boot mode.
2. Run the following command in a terminal to find the board's USB IDs.

```bash
lsusb
```

3. Use the detected vendor ID and product ID to create `/etc/udev/rules.d/99-topst.rules`.

```text
SUBSYSTEM=="usb", ATTR{idVendor}=="VENDOR_ID", ATTR{idProduct}=="PRODUCT_ID", MODE="0666"
```

4. Reload the rules.

```bash
sudo udevadm control --reload-rules
sudo udevadm trigger
```

Do not enter random values for `VENDOR_ID` and `PRODUCT_ID`. If you do not know the correct values for D3-G, contact TOPST support.

### 3.4 Check the Linux FWDN Files

The Linux distribution must contain executable files without an extension in the following locations.

```text
tools/fwdn_d3/fwdn_d3
tools/fwdn_ai/fwdn_ai
tools/fwdn_vcp/fwdn_vcp
```

If the files are present, give them execute permission.

```bash
chmod +x tools/fwdn_d3/fwdn_d3
chmod +x tools/fwdn_ai/fwdn_ai
chmod +x tools/fwdn_vcp/fwdn_vcp
```

Flashing cannot work on Linux without these files. Windows `.exe` files cannot be used instead.

## 4. Flashing D3-G on Linux

Linux does not use the Windows VTC driver installation step.

1. Select a D3-G image.
2. Press the BOOT button while watching the on-screen animation.
3. While holding BOOT, press and release the RESET button.
4. Release the BOOT button.
5. Check whether the board is detected.
6. Start flashing and wait until it is complete.

If D3-G is not detected, check the USB permission rule, Type-C cable, board power, and boot mode.

## 5. Flashing AI-G on Linux

TOPST Imager does not automatically change the Ethernet address on Linux. Set it manually in Ubuntu Settings.

1. Open **Settings → Network** in Ubuntu.
2. Open the settings for the wired network connected to AI-G.
3. Set the IPv4 method to **Manual**.
4. Enter `192.168.0.8` as the address.
5. Enter `255.255.255.0` as the netmask. If the screen uses prefix length notation, enter `24`.
6. Leave Gateway and DNS empty unless you have received different instructions.
7. Apply the settings, and then turn the wired connection off and on again.
8. Return to TOPST Imager and check the Ethernet status.
9. Follow the on-screen instructions to enter boot mode.
10. Select the `/dev/ttyUSB...` or `/dev/ttyACM...` port for AI-G.
11. Start flashing.

## 6. Flashing VCP-G on Linux

1. Follow the on-screen instructions to put VCP-G into boot mode.
2. Select a port in the form `/dev/ttyUSB...` or `/dev/ttyACM...`.
3. Confirm the correct port, and then start flashing.
4. Wait until the completion screen appears.

If no port is listed, make sure you joined the `dialout` group and signed out and back in afterward.

## 7. Troubleshooting on Linux

### `Permission denied` Appears

- AI-G or VCP-G: Make sure the user belongs to the `dialout` group.
- D3-G: Make sure the udev USB permission rule is active.
- FWDN file: Make sure you gave it execute permission with `chmod +x`.

### The Linux FWDN File Cannot Be Found

Check for the Linux executable under `tools/fwdn_*` in the distribution folder. A Windows `.exe` file cannot run on Linux.

### No Board Port Is Listed

Run the following command to list available ports.

```bash
ls /dev/ttyUSB* /dev/ttyACM* 2>/dev/null
```

Compare the list before and after connecting the USB cable. The newly added port is usually the board port.

### The Application Does Not Follow the Light or Dark Theme

TOPST Imager uses the theme information provided by the Linux desktop through Qt. Some desktop environments may not apply the system theme immediately. Try restarting the application.

## 8. After Flashing Is Complete

1. Make sure the success message appears.
2. Wait for TOPST Imager to finish all work.
3. Turn off the board safely.
4. Disconnect the FWDN cable or reconnect the cables for normal use.
5. Turn on the board and make sure the new operating system starts.

Official images are downloaded and extracted in a temporary folder. After flashing completes successfully, the downloaded files and extracted folder are deleted automatically.

## 9. Three Things to Remember

1. **Make sure you selected the correct board and image.**
2. **Do not disconnect power or cables while flashing is in progress.**
3. **If an error occurs, check every item in the on-screen list from top to bottom.**

If you need help, prepare the error message and log file, and ask a question in the [TOPST Community](https://community.topst.ai/).
