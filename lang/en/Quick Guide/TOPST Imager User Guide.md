# TOPST Imager User Guide

TOPST Imager installs an operating system or firmware on a TOPST board. You do not need to know programming or electronics. Keep this guide open and follow one screen at a time.

> **Important:** Flashing can erase everything stored in the board's eMMC. Back up any files you need before you begin.

> **About the screenshots:** Red boxes and numbered circles were added only for this guide. They do not appear in TOPST Imager. The screenshots use the Windows light theme; Linux and dark-theme screens work in the same way.

## 1. Words You Will See

| Word | Simple meaning |
| --- | --- |
| Board / Device | The TOPST product on which the image will be installed. |
| Image | A file containing an operating system or firmware. |
| Flashing | Writing the selected image to the board. |
| Firmware Download Mode / Boot Mode | A special board state used for flashing. |
| FWDN | The tool TOPST Imager runs in the background. You do not run it yourself. |
| COM port | The USB serial connection used by AI-G and VCP-G. Linux displays it as `/dev/ttyUSB...` or `/dev/ttyACM...`. |
| eMMC | Storage built into the board. |

## 2. Supported Boards

| Board | Custom image | Connections used while flashing |
| --- | --- | --- |
| TOPST D3-G | `.fai` | Board power and FWDN USB Type-C data cable |
| TOPST AI-G | `.fai` | Board power, FWDN USB Type-C data cable, and Ethernet cable |
| TOPST VCP-G | `.rom` | Board power and FWDN USB Type-C data cable |

Use a USB Type-C cable that supports **data transfer**. A charge-only cable will not work.

## 3. Prepare Before Starting

- The correct TOPST board and its power adapter
- A USB Type-C data cable
- An Ethernet cable when using AI-G
- A computer connected to the internet when using an official image
- Enough free disk space for both the compressed download and the extracted package
- A backup of important data on the board

While flashing is in progress:

- Do not turn off the board or computer.
- Do not disconnect the USB or Ethernet cable.
- Do not close TOPST Imager.
- Do not let the computer enter sleep mode.

## 4. App Options

Select **App Options** at the bottom-left of the main window.

![TOPST Imager App Options](https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/Quick%20Guide/TOPST%20Imager%20App%20Options.png)

1. **Language:** Selecting a language changes the screen immediately so that you can preview it.
2. **TOPST Imager User Guide:** Opens this user guide in your web browser.
3. **Ask the Community:** Opens the [TOPST Community](https://community.topst.ai/).
4. **Save:** Keeps the selected language. **Cancel**, the `Esc` key, or clicking outside the window restores the language that was active before the window opened.

Supported languages are Korean, English, Japanese, Simplified Chinese, Traditional Chinese, Thai, and German. The light or dark appearance follows the operating system theme automatically.

---

# Windows

## 5. Install TOPST Imager

### 5.1 Requirements

- Windows 10 64-bit or later
- Windows 11 64-bit

### 5.2 Installation

1. Download the official TOPST Imager Windows installer.
2. Double-click the installer.
3. Read and accept the license agreement.
4. Select **Install**.
5. When installation is complete, select **Launch TOPST Imager**.

Windows may ask for administrator permission when TOPST Imager or the VTC driver installer starts. Confirm that the file came from the official TOPST distribution before selecting **Yes**.

## 6. Select a Board, Operating System, and Version

### 6.1 Select the Board

![Select a TOPST board](https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/Quick%20Guide/TOPST%20Imager%20Board%20Selection.png)

1. Select the board that matches the product in front of you.
2. Check that the row is highlighted and says **Selected**, and then select **Next**.

You can also double-click a board to continue. If you choose the wrong board, select **Back** and choose again.

### 6.2 Select an Operating System

![Select an official operating system or a custom image](https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/Quick%20Guide/TOPST%20Imager%20OS%20Selection.png)

1. Select an operating system supplied by TOPST.
2. To use a file already stored on the computer, select **Use Custom Image**.
3. Select **Next**, or double-click the selected row.

### 6.3 Select a Version

![Select an image version](https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/Quick%20Guide/TOPST%20Imager%20Version%20Selection.png)

1. Select the required version. Check its description, release date, download size, and extracted size.
2. Select **Flashing**.

- **Download size** is the compressed file size transferred from the internet.
- **Extracted size** is the approximate disk space needed after extraction.

Unless your project requires a specific release, use the latest stable or recommended version.

### 6.4 Confirm Data Erasure

![Confirm the eMMC erase warning](https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/Quick%20Guide/TOPST%20Imager%20eMMC%20Erase%20Warning.png)

1. Select **Cancel** if you need to check the board, image, or backup again.
2. Select **Confirm** only when you understand that the selected board's eMMC data may be deleted.

Selecting **Cancel** at this point does not erase the board.

## 7. Flash D3-G on Windows

D3-G uses three flashing setup steps on Windows.

### Step 1: Install the VTC Driver

![Install the D3-G VTC driver](https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/Quick%20Guide/TOPST%20Imager%20D3-G%20Driver%20Installation.png)

1. Select **Install Driver**.
2. Approve the Windows administrator request.
3. Complete the VTC Driver Installer.
4. Return to TOPST Imager.
5. Select **Driver Installation Complete**.

You normally install this driver only once on each Windows computer. If you cancel the administrator request, no driver is installed; select **Install Driver** again when ready.

### Step 2: Enter Boot Mode and Detect the Board

![Enter D3-G boot mode and detect the board](https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/Quick%20Guide/TOPST%20Imager%20D3-G%20Boot%20Mode.png)

1. Follow the flashing markers in the boot-mode animation.
2. Press and hold the **BOOT** button.
3. While holding BOOT, press and release the **RESET** button.
4. Release the BOOT button.
5. Connect the FWDN USB Type-C data cable firmly.
6. Select **Check Again** if the status does not refresh automatically.
7. When the status changes to connected, select **Start Flashing**.

In Windows Device Manager, a connected D3-G may appear under Universal Serial Bus controllers with a name similar to `Telechips TCCxxxx VTC USB Driver`.

### Step 3: Flashing

For an official image, the screen shows separate progress for:

1. Download
2. Extraction
3. Flashing

Each progress value changes from 0% to 100%. Wait for the **Complete** screen before disconnecting anything.

## 8. Flash AI-G on Windows

AI-G uses three flashing setup steps.

### Step 1: Ethernet Setup

1. Connect the computer directly to AI-G with an Ethernet cable.
2. Select the wired Ethernet adapter connected to AI-G, not Wi-Fi.
3. Allow TOPST Imager to apply the temporary address `192.168.0.8/24` when prompted.
4. Continue when the network status is ready.

TOPST Imager restores the temporary Windows network setting when the operation finishes or is canceled.

### Step 2: Boot Mode and COM Port

1. Follow the on-screen boot-mode animation.
2. Press and hold **BOOT**.
3. Press and release the **RESET** button.
4. Release BOOT.
5. Select the COM port that belongs to AI-G.
6. Check the board power, USB Type-C cable, and Ethernet cable.
7. Continue to flashing.

If several COM ports are listed, disconnect the AI-G USB cable briefly. The port that disappears is normally the AI-G port. Reconnect the cable, repeat boot mode, and select that port.

### Step 3: Flashing

Wait until flashing reaches 100% and the **Complete** screen appears.

## 9. Flash VCP-G on Windows

VCP-G uses two flashing setup steps.

### Step 1: Boot Mode and COM Port

The boot-mode guide and COM-port selection are on the same screen.

1. Follow the board animation to set VCP-G to Firmware Download Mode.
2. Press and release the **RESET** button when the guide tells you to do so.
3. Select the COM port belonging to VCP-G.
4. Recheck the board power and FWDN USB Type-C data cable.
5. Continue to flashing.

### Step 2: Flashing

Wait until flashing reaches 100% and the **Complete** screen appears.

## 10. Use a Custom Image on Windows

1. Select the correct board first.
2. On the operating-system screen, click **Use Custom Image** once.
3. Select **Next**, or double-click **Use Custom Image**.
4. Either drag the file into the drop area or select the browse button.
5. Check the selected file name, and then continue.

Use the correct file type:

- D3-G: `.fai`
- AI-G: `.fai`
- VCP-G: `.rom`

A custom image is already on the computer, so the **Download** and **Extraction** progress rows are hidden. The same board-specific driver, network, boot-mode, COM-port, and flashing steps still apply.

---

# Linux

## 11. Linux Requirements

The current Linux distribution supports **x86_64 Linux**. Windows `.exe` FWDN files cannot be used on Linux.

The distributed application must include executable Linux tools at:

```text
tools/fwdn_d3/fwdn_d3
tools/fwdn_ai/fwdn_ai
tools/fwdn_vcp/fwdn_vcp
```

The computer also needs:

- `unzip` for official ZIP packages
- `policykit-1` for the administrator confirmation window
- `acl` for temporary AI-G and VCP-G serial-port access

On Ubuntu, an administrator can install them with:

```bash
sudo apt update
sudo apt install unzip policykit-1 acl
```

Do **not** run TOPST Imager or FWDN with `sudo`. TOPST Imager requests administrator permission only when it needs to grant temporary access to the selected serial device.

## 12. Install and Start the Linux Package

The exact archive name may vary by release. For a `.tar.gz` package:

```bash
cd ~/Downloads
tar -xzf TOPST-Imager-<version>-Linux-x86_64.tar.gz
cd TOPST-Imager-<version>-Linux-x86_64
chmod +x topst-imager
./topst-imager
```

Use the actual file and folder names from the downloaded package. A user package should include the Qt runtime; if Qt libraries are missing, download the complete official Linux package rather than running the application as root.

## 13. Select the Image on Linux

Board, operating-system, version, custom-image, and eMMC warning screens work the same way as the Windows screens in Sections 6 and 10.

## 14. Flash D3-G on Linux

D3-G has two flashing setup steps on Linux because the Windows VTC Driver Installer step is not shown.

### Step 1: Boot Mode and Board Detection

1. Press and hold **BOOT**.
2. Press and release the **RESET** button.
3. Release BOOT.
4. Connect the FWDN USB Type-C data cable.
5. Select **Check Again** if needed.
6. Continue when D3-G is detected.

Linux detects the D3-G FWDN USB device directly. If it is not detected, check the USB data cable, board power, boot mode, and the installed udev rule supplied with the Linux package.

### Step 2: Flashing

Wait for download, extraction, and flashing to finish. Custom `.fai` images show only flashing progress.

## 15. Flash AI-G on Linux

AI-G has three flashing setup steps.

### Step 1: Ethernet Setup

TOPST Imager does not automatically change the Linux Ethernet address. Set it in the Linux network settings:

1. Open **Settings → Network**.
2. Open the wired connection connected to AI-G.
3. Set IPv4 to **Manual**.
4. Address: `192.168.0.8`
5. Netmask: `255.255.255.0`, or prefix length `24`
6. Leave Gateway and DNS empty unless your network administrator tells you otherwise.
7. Apply the change, reconnect the wired connection, and return to TOPST Imager.

### Step 2: Boot Mode, COM Port, and Temporary Access

1. Follow the boot-mode animation.
2. Select the AI-G port, such as `/dev/ttyUSB0`.
3. If the port is not writable, select **Grant Temporary Access**.
4. Approve the Linux administrator window.
5. When access is ready, the flashing button becomes available.

Temporary access is applied only to the selected serial device and is released after flashing, cancellation, or leaving the flashing screen. You do not need to add the user permanently to the `dialout` group.

### Step 3: Flashing

Wait until the **Complete** screen appears.

## 16. Flash VCP-G on Linux

VCP-G uses two flashing setup steps on Linux, just as it does on Windows.

### Step 1: Boot Mode, COM Port, and Temporary Access

1. Follow the boot-mode guide.
2. Select the VCP-G port, such as `/dev/ttyUSB0`.
3. If shown, select **Grant Temporary Access** and approve the administrator window.
4. Continue when the selected port is accessible.

### Step 2: Flashing

Wait until flashing reaches 100% and the **Complete** screen appears. A custom `.rom` image shows only flashing progress.

## 17. Downloads, Retries, and Temporary Files

For an official image, TOPST Imager:

1. Creates a temporary working folder.
2. Downloads the ZIP package.
3. Extracts the package into the temporary folder.
4. Runs the board-specific FWDN executable.
5. Deletes the downloaded and extracted temporary data after successful flashing or cancellation.

If the internet connection stops during a download, keep TOPST Imager open and reconnect the network. The application automatically retries and resumes from the partial download when the server supports it. The status appears in the selected application language.

Some recoverable flashing errors keep the prepared package temporarily so you can return to the instructed setup step without downloading it again.

## 18. When an Error Window Appears

TOPST Imager detects known FWDN errors and immediately opens an error window. If the window shows a three-second countdown, read the message; after the countdown the app returns to the required recovery step. Select **OK** after checking the listed items.

### D3-G Connection Error

Check:

1. Board power connection
2. FWDN USB Type-C cable connection
3. Firmware Download Mode entry

The application returns to the D3-G boot-mode step.

### AI-G Connection or Synchronization Error

Check:

1. Board power connection
2. Firmware Download Mode entry
3. Correct COM-port selection

If the message specifically says `Failed open port`, check the FWDN USB Type-C cable and selected port. If it says `TCP Socket Open Fail`, check the Ethernet cable, adapter, and `192.168.0.8/24` network setting.

### VCP-G Connection Error

Check:

1. Board power connection
2. Firmware Download Mode entry
3. Correct COM-port selection

If `GetLastError : 22` appears, check the FWDN USB Type-C cable connection.

### No COM Port Appears

1. Check board power.
2. Reconnect the USB data cable.
3. Repeat Firmware Download Mode.
4. Refresh the port list.
5. On Linux, select **Grant Temporary Access** after choosing the port.

### Flashing Fails Completely

If the error says `Failed to write in eFlash` or `Failed FWDN`, follow the message and restart from the first flashing setup step. Do not disconnect the board while a write operation is still active.

## 19. Log Files

When requesting help, include the complete error message, board name, selected image version, operating system, and the log file.

Windows log location:

```text
%LOCALAPPDATA%\Telechips\TOPST Imager\logs\topst-imager.log
```

Typical Linux log location:

```text
~/.local/share/Telechips/TOPST Imager/logs/topst-imager.log
```

If you still need help, use **App Options → Ask the Community** or visit the [TOPST Community](https://community.topst.ai/).

## 20. After Flashing Completes

1. Confirm that the **Complete** screen is visible.
2. Wait until TOPST Imager says the operation is finished.
3. Turn off the board safely.
4. Disconnect the FWDN cable or reconnect the cables for normal use.
5. Turn on the board and check that the new operating system starts.

Remember these three rules:

1. Select the board and image carefully.
2. Never disconnect power or cables while flashing is active.
3. When an error appears, check every listed item from top to bottom.
