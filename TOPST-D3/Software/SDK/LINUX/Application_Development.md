# 1 Development Guide

## 1.1 Software Package

This chapter provides information for further development of new applications and libraries in images and supports development tools or SDKs to enable application development and testing on target hardware.

### 1.1.1 Build Application with Devtool

***Devtool*** is a group of tools that assist you in round-trip development with the OpenEmbedded build system. You can view the official reference manual for ***Devtool*** in the link below. Therefore, this chapter explains only the basic usage.

- Official Reference: [https://docs.yoctoproject.org/3.1.21/singleindex.html#using-devtool-in-your-sdk-workflow](https://docs.yoctoproject.org/3.1.21/singleindex.html%23using-devtool-in-your-sdk-workflow)
- ***Devtool*** Reference: https://docs.yoctoproject.org/ref-manual/devtool-reference.html
<div style="display: flex; justify-content: center;">
    <img src="https://github.com/Topst-Dev/Documentation/assets/144076415/92bb8127-95d6-43ae-9544-39784666ba0c" width="500" height="350" style="margin: auto;">
</div>
<p align="center"><strong>Figure 5.1 Yocto Devtool Process</strong></p>

### 1.1.1.1 BitBake Configuration

Yocto Project builds images by using ***BitBake***. Therefore, you need to change the user development environment to the ***BitBake*** environment.

```bash
$ source poky/oe-init-build-env build/tcc8050-main

Yocto Project common targets are:

core-image-minimal

core-image-sato

meta-toolchain

adt-installer

meta-ide-support

Telechips common targets are:

telechips-ivi-image-minimal

telechips-ivi-image-multimedia(minimal + GStreamer)

telechips-ivi-image(minimal + GStreamer + Qt)

meta-toolchain-telechips(Application Development Toolkit)

meta-toolchain-telechips-ivi(Application Development Toolkit include GStreamer)

meta-toolchain-telechips-qt5(Application Development Toolkit include GStreamer and Qt5)

Telechips Automotive Linux Platform targets are:

automotive-linux-platform-image(telechips-ivi-image + demo applications)

You can also run generated qemu images with a command like 'runqemu qemux86'

or

You can also run generated Telechips images on Telechips EVB Boards

Other commonly useful commands are:

- 'devtool' and 'recipetool' handle common recipe tasks

- 'bitbake-layers' handles common layer tasks

- 'oe-pkgdata-util' handles common target package tasks

Warning: source-mirror not exist!!

The build to be slowler or fail because will be download source code from upstream before build.
```

---

### 1.1.1.2 Add Source Code

If you want to add your source code has no recipe in the SDK, you can use the **devtool add** command. It assists in adding new software to be built to SDK. The **devtool add** command generates a new recipe based on the existing source code.

You can add source code from remote repository and local directory to SDK:

```bash
devtool add {recipe-name} {fetch-url or source-tree}
```

---

Then, the **devtool add** command generates **new_recipe** or **new_recipe2** in workspace/recipes/new_recipe or new_recipe2. And the source code is downloaded or copied in workspace/sources/new_recipe or new_recipes2 directory. You can modify your recipes in workspace.

You can see more information by using the **devtool add --help** command.

### 1.1.1.3 Modify Source Code

***Devtool*** sets up an environment to enable you to modify the existing source code in SDK. The **devtool modify** command supports modifying your recipe and source code:

```bash
devtool modify {recipe-name}
```

---

Then, the **devtool modify** command o generates a “.bbappend” file in workspace/appends/ivi_recipe.bbappend. The source code is downloaded in workspace/sources/ivi_recipe. You can modify your source code and bbappend.

You can see more information by using the **devtool modify --help** command.

### 1.1.1.4 Update Recipe

You can update the existing recipe to build the recipe for an updated set of source files:

```bash
devtool upgrade -V {version} {recipe-name}
```

---

The command above updates the SRCREV of the recipe. In your workspace, "ivi_recipe_1.0.1.bb" is generated in workspace/recipes directory, and "ivi_recipe_1.0.1.bbappend" can be generated in workspace/appends directory.

You can see more information by using the **devtool upgrade –help** command.

### 1.1.1.5 After Setting Environment

If you want to build your source code or recipe, you can build it as follows:

```bash
bitbake {recipe-name} or devtool build {recipe-name}
```

---

You can install your outputs to your target as follows:

```bash
devtool deploy-target {recipe-name} {target}
```

---

After you finish editing recipes and source code, you can apply your recipes to Yocto layer:

```bash
devtool finish {recipe-name} {layer-name}
```

---

In your workspace, the ***devtool*** makes the devtool branch. If you commit your patch to devtool branch and finish executing ***Devtool***, the **devtool finish** command generates the patches and adds the patches to the recipe.

If you want to remove your local outputs, you can reset the recipe:

```bash
devtool reset {recipe-name} or devtool reset –all
```

---

### 1.1.2 Build Application with Eclipse

### 1.1.2.1 Download SDK

Download the toolchain SDK as shown below and extract by using tar.

```bash
$ wget --no-check-certificate https://tost-dl.huconn.com/share/AP/tools/glibc-x86_64-automotive-linux\

-platform-image-aarch64-toolchain.tar.xz

- -2023-07-19 17:42:43-- https://tost-dl.huconn.com/share/AP/tools/glibc-x86_64-automotive-linux-platform-image-aarch64-toolchain.tar.xz

Resolving tost-dl.huconn.com (tost-dl.huconn.com)... 121.182.60.114

Connecting to tost-dl.huconn.com (tost-dl.huconn.com)|121.182.60.114|:443... connected.

WARNING: cannot verify tost-dl.huconn.com's certificate, issued by ‘CN=GoGetSSL RSA DV CA,O=GoGetSSL,L=Riga,C=LV’:

Issued certificate has expired.

HTTP request sent, awaiting response... 200 OK

Length: 218678539 (209M) [application/octet-stream]

Saving to: ‘glibc-x86_64-automotive-linux-platform-image-aarch64-toolchain.tar.xz’

glibc-x86_64-automotive-linux-platform-image-a 100%[=================================================================================================>] 208.55M  41.5MB/s    in 4.9s

2023-07-19 17:42:48 (42.4 MB/s) - ‘glibc-x86_64-automotive-linux-platform-image-aarch64-toolchain.tar.xz’ saved [218678539/218678539]

$ tar -zxvf glibc-x86_64-automotive-linux-platform-image-aarch64-toolchain.tar.xz

glibc-x86_64-automotive-linux-platform-image-aarch64-toolchain/

glibc-x86_64-automotive-linux-platform-image-aarch64-toolchain/poky-telechips-systemd-glibc-x86_64-automotive-linux-platform-image-aarch64-toolchain-nodistro.0.sh

glibc-x86_64-automotive-linux-platform-image-aarch64-toolchain/poky-telechips-systemd-glibc-x86_64-automotive-linux-platform-image-aarch64-toolchain-nodistro.0.testdata.json

glibc-x86_64-automotive-linux-platform-image-aarch64-toolchain/poky-telechips-systemd-glibc-x86_64-automotive-linux-platform-image-aarch64-toolchain-nodistro.0.target.manifest

glibc-x86_64-automotive-linux-platform-image-aarch64-toolchain/poky-telechips-systemd-glibc-x86_64-automotive-linux-platform-image-aarch64-toolchain-nodistro.0.host.manifest
```

---

### 1.1.2.2 Install SDK

Move the SDK to the downloaded directory and install the SDK.

```bash
$ cd glibc-x86_64-automotive-linux-platform-image-aarch64-toolchain

$ ./poky-telechips-systemd-glibc-x86_64-automotive-linux-platform-image-aarch64-toolchain-nodistro.0.sh

Telechips Baseline (Poky/meta-telechips/meta-core) SDK installer version nodistro.0

=========================================================

Enter target directory for SDK (default: /usr/local/oecore-x86_64):

You are about to install the SDK to "/usr/local/oecore-x86_64". Proceed [y/N]? y

Extracting SDK..........................................................done

Setting it up...done

SDK has been successfully set up and is ready to be used.

Each time you wish to use the SDK in a new shell session, you need to source the environment setup script e.g.

$ . /usr/local/oecore-x86_64/environment-setup-aarch64-telechips-linux
```

---

The path to the now installed SDK is used to set up ***Eclipse***.

### 1.1.2.3 Install JDK

Install JDK version 1.8.

```bash
$ sudo apt-get install openjdk-8-jre libcanberra-gtk-module
```

---

If more than one JDK is installed, the command above can be used to change the version to 1.8.

### 1.1.2.4 Eclipse Installation

1. ***Eclipse*** can be installed through the following link:

[Luna SR2 | Eclipse Packages](https://www.eclipse.org/downloads/packages/release/luna/sr2)

2. Download the C/C++ Developers Linux version.

<div style="display: flex; justify-content: center;">
    <img src="https://github.com/Topst-Dev/Documentation/assets/144076415/36ff523a-4f4b-46c4-a92c-51eab6fe1527" width="500" height="350" style="margin: auto;">
</div>

3. Extract and install using tar.

```bash
$ tar -xzvf ~/Downloads/eclipse-cpp-luna-SR2-linux-gtk-x86_64.tar.gz
```

---

1. Run ***Eclipse***.

```bash
$ cd eclipse

$ ./eclipse
```

---

### 1.1.2.5 Eclipse Software Installation

1. Click “Install New Software…” on the Help tab.

<div style="display: flex; justify-content: center;">
    <img src="https://github.com/Topst-Dev/Documentation/assets/144076415/0bec4883-5afc-41d5-864d-05212b576d8f" width="500" height="350" style="margin: auto;">
</div>
<p align="center"><strong>Figure 5.2 Eclipse Window</strong></p>

2. Select "Luna - http://download.eclipse.org/releases/luna" in Work with:

<div style="display: flex; justify-content: center;">
    <img src="https://github.com/Topst-Dev/Documentation/assets/144076415/856a0f9b-8c17-443a-957f-0139fea0a953" width="500" height="350" style="margin: auto;">
</div>
<p align="center"><strong>Figure 5.3 Eclipse Software Installation</strong></p>

3. Select an option according to the table below.

| Linux Tools |  |
| --- | --- |
| 1. Linux Tools LTTng Tracer Control 
| 2. Linux Tools LTTng Userspace Analysis 
| 3. LTTng Kernel Analysis 

| Mobile and Device Development |  |
| --- | --- |
| 1. C/C++ Remote Launch (Requires RSE Remote System Explorer) 
| 2. Remote System Explorer End-user Runtime
| 3.Remote System Explorer User Actions
| 4. Target Management Terminal (Core SDK)
| 5. TCF Remote System Explorer add-in
| 6. TCF Target Explorer 

| Programming Language |  |
| --- | --- |
| 1. C/C++ Autotools Support
| 2. C/C++ Development Tools


4. Click **“**Next**”**, agree to the license, and select Finish.
5. Restart for SW update.

### 1.1.2.6 Yocto Plug-in Installation

1. Click “Install New Software…” on the Help tab again.

<div style="display: flex; justify-content: center;">
    <img src="https://github.com/Topst-Dev/Documentation/assets/144076415/d8d486a8-d33b-4635-ae22-4dc1ae1b28d7" width="500" height="350" style="margin: auto;">
</div>
<p align="center"><strong>Figure 5.4 Eclipse Yocto Installation</strong></p>

2. Press the Add button to add a repository and set it as follows:

Location: http://downloads.yoctoproject.org/releases/eclipse-plugin/1.8/luna

<div style="display: flex; justify-content: center;">
    <img src="https://github.com/Topst-Dev/Documentation/assets/144076415/b320627a-dcef-485d-8893-d20f99d4ccc8" width="500" height="350" style="margin: auto;">
</div>
<p align="center"><strong>Figure 5.5 Add Repository</strong></p>


3. Select the following plug-ins.

```bash
Yocto Project ADT Plug-in

Yocto Project Bitbake Commander Plug-in

Yocto Project Documentation plug-in
```

4. After checking all three plug-ins, repeat the process above.

### 1.1.2.7 Setting Yocto ADT

1. Click Preferences on the Window tab.
<div style="display: flex; justify-content: center;">
    <img src="https://github.com/Topst-Dev/Documentation/assets/144076415/4105db85-2035-4513-bc24-c46fb7525a3f" width="500" height="350" style="margin: auto;">
</div>
<p align="center"><strong>Figure 5.6 Select Preferences</strong></p>

1. Click the Yocto Project ADT on the left tab and set it up.

<div style="display: flex; justify-content: center;">
    <img src="https://github.com/Topst-Dev/Documentation/assets/144076415/06487724-9523-4d31-8045-260f426bb1ec" width="500" height="350" style="margin: auto;">
</div>
<p align="center"><strong>Figure 5.7 Preference Settings</strong></p>

“Cross Compiler Options” are set to Standalone, and “Toolchain Root Location” and “Sysroot Location” select the folder where the SDK was previously installed. (If you followed this example, the folder is \build\tcc8050-main\tmp\deploy\sdk\maincore)

### 1.1.2.8 Create and Debug Project

### 1.1.2.8.1 Create Project

1. Select the project you want and select “Yocto Project ADT Autotools Project” in Project type. Then, click Next and Finish.

<div style="display: flex; justify-content: center;">
    <img src="https://github.com/Topst-Dev/Documentation/assets/144076415/6ef659c1-abf4-4f13-8347-847eede42aff" width="500" height="350" style="margin: auto;">
</div>
<p align="center"><strong>Figure 5.8 Create New Project</strong></p>

<div style="display: flex; justify-content: center;">
    <img src="https://github.com/Topst-Dev/Documentation/assets/144076415/c60445f3-e4d1-41cf-8fe4-9ebfdd9e979d" width="500" height="350" style="margin: auto;">
</div>
<p align="center"><strong>Figure 5.9 Project Preference</strong></p>

2. After creating the project, right-click on the project, and click “Reconfigure Project” to automatically create files.
3. Click the **hammer** button on the top to build.

<div style="display: flex; justify-content: center;">
    <img src="https://github.com/Topst-Dev/Documentation/assets/144076415/b91390ab-5a63-4380-94cb-781e28a2db42" width="500" height="350" style="margin: auto;">
</div>
<p align="center"><strong>Figure 5.10 Reconfigure Project</strong></p>

### 1.1.2.8.2 Debug Project with TCF

1. Select “Debug Configuration” on the Run tab. You can create a new tab by double-clicking the “C/C++ Remote Application” tab.

<div style="display: flex; justify-content: center;">
    <img src="https://github.com/Topst-Dev/Documentation/assets/144076415/957dc0bc-3a9e-40bc-8b9f-d1983f96a27c" width="500" height="350" style="margin: auto;">
</div>
<p align="center"><strong>Figure 5.11 Debug Configuration</strong></p>

2. Connect ***Eclipse*** and the board to each other via Ethernet.
3. Select “New” on the “Connection” tab, and select TCF.

<div style="display: flex; justify-content: center;">
    <img src="https://github.com/Topst-Dev/Documentation/assets/144076415/fe44eec9-d669-4115-8d7a-6d0c1472e386" width="500" height="350" style="margin: auto;">
</div>
<p align="center"><strong>Figure 5.12 Select Target</strong></p>

4. Click IP after connecting SSH with a serial connection. Enter the IP address into “Host name,” fill in “Connection name” and select Finish.

<div style="display: flex; justify-content: center;">
    <img src="https://github.com/Topst-Dev/Documentation/assets/144076415/5229c9ae-db3d-4544-a1a0-cc52894abf26" width="500" height="350" style="margin: auto;">
</div>
<p align="center"><strong>Figure 5.13 Connect Target Network</strong></p>

5. Write in “Remote Absolute File Path for C/C++ Application” the path to create the executable file at the desired location on the board.

<div style="display: flex; justify-content: center;">
    <img src="https://github.com/Topst-Dev/Documentation/assets/144076415/badc573a-f6d3-4576-95f7-09f14f9c408c" width="500" height="350" style="margin: auto;">
</div>
<p align="center"><strong>Figure 5.14 Set Source Path</strong></p>

<div style="display: flex; justify-content: center;">
    <img src="https://github.com/Topst-Dev/Documentation/assets/144076415/356c0acc-d49f-4311-958f-9fc17df67906" width="500" height="350" style="margin: auto;">
</div>
<p align="center"><strong>Figure 5.15 Success Screen</strong></p>

<div style="display: flex; justify-content: center;">
    <img src="https://github.com/Topst-Dev/Documentation/assets/144076415/b4a865d5-a72c-4ba3-ad92-cb66709e8d40" width="500" height="350" style="margin: auto;">
</div>
<p align="center"><strong>Figure 5.16 Board Console Screen</strong></p>

6. An executable file called “HelloWorld” was created, and when executed, the content is printed based on the code written.

## 1.2 Application Test

This chapter describes how to use a demo application for board functional testing.

### 1.2.1 Audio – ALSA

The following example was made by using an ALSA-based demo program for audio testing of the board.

(bb PATH: ./poky/meta-telechips/meta-ivi/recipes-applications/telechips-automotive-linux/audio-example_1.0.0.bb)

The demo program records for 3 seconds and plays the recorded sound.

```bash
$ sudo apt-get install libasound2-dev alsa-utils
```

---

- Check the sound card.



```bash
$ aplay -l
```

<div style="display: flex; justify-content: center;">
    <img src="https://github.com/Topst-Dev/Documentation/assets/144076415/19371066-8a6b-45a0-a8f4-4e0949f7e662" width="500" height="350" style="margin: auto;">
</div>

- Test sound.

```bash
$ speaker-test -c 2
```
<div style="display: flex; justify-content: center;">
    <img src="https://github.com/Topst-Dev/Documentation/assets/144076415/4e28ba09-1d4b-4e53-b25f-dc3dc9ab66fd" width="500" height="350" style="margin: auto;">
</div>

### 1.2.1.1 SoX

Sound eXchange (SoX) is a cross-platform (Windows, Linux, MacOS X, and so on) command line utility that can convert various formats of computer audio files to other formats. It can also apply various effects to these sound files, and, as an added bonus, SoX can play and record audio files on most platforms.

```bash
$ sudo apt-get install sox libsox-fmt-all

$ play ${sample.mp3}
```
<div style="display: flex; justify-content: center;">
    <img src="https://github.com/Topst-Dev/Documentation/assets/144076415/33dc949c-d26c-42dc-bd61-312e5ab7ebe3" width="500" height="350" style="margin: auto;">
</div>

### 1.2.2 Video – VLC

VideoLAN Clients (VLC) is a free and open-source cross-platform multimedia player and framework that plays most multimedia files as well as DVDs, Audio CDs, VCDs, and various streaming protocols.

```bash
$ sudo apt-get install vlc
```
<div style="display: flex; justify-content: center;">
    <img src="https://github.com/Topst-Dev/Documentation/assets/144076415/ae4120fb-cffa-4c1f-8628-8b71df3db294" width="500" height="350" style="margin: auto;">
</div>

<div style="display: flex; justify-content: center;">
    <img src="https://github.com/Topst-Dev/Documentation/assets/144076415/cb1790c0-f06c-4316-bc2b-b58f08f18001" width="500" height="350" style="margin: auto;">
</div>

### 1.2.3 General Purpose Input/Output (GPIO)

General purpose input/output (GPIO) is a digital signal pin on an integrated circuit or electrical circuit board that allows the operation, including input or output, to be controlled by the user at runtime. GPIO is not predefined for a specific purpose and is not used by default. GPIO is implemented by an assembly-level circuit network designer (circuit board designer for integrated circuit GPIO, system integrator for substrate-level GPIO) whose purpose and behavior are defined when used.

The functions that GPIO performs may vary depending on the system, and the functions that are generally provided are as follows:

- Input/output function (high=1, low=0)
- IRQ signal detection: This can also be used to wake up systemd in suspend state on power management.
- Accessible even when Spinlock is jammed.

The above functions allow you to use the MMC/SD card for insertion or removal, write protection, and enable transceiver settings, hardware watchdog functions, or switch sensing.

The pin map is as follows:

<div style="display: flex; justify-content: center;">
    <img src="https://github.com/Topst-Dev/Documentation/assets/144076415/79d68d72-1e4c-41a4-b3a8-f9507b3d7821" width="500" height="350" style="margin: auto;">
</div>

The following is an example of testing the input and output of the board. You can test the input and output by controlling the pin number.

Example:

```bash
$ echo 84 > /sys/class/gpio/export

$ echo out > /sys/class/gpio/gpio84/direction

$ echo 1 > /sys/class/gpio/gpio84/value

$ echo 0 > /sys/class/gpio/gpio84/value
```
<div style="display: flex; justify-content: center;">
    <img src="https://github.com/Topst-Dev/Documentation/assets/144076415/75ea32f8-e75f-4276-8c57-4a4360b9888e" width="500" height="350" style="margin: auto;">
</div>
<p align="center"><strong>Figure 5.17 GPIO Example Board</strong></p>

### 1.2.4 Serial Peripheral Interface (SPI)

Serial Peripheral Interface (SPI) is a serial communication method such as I2C, CAN, and UART. SPI is a function that transfers data between small peripherals such as microcontrollers, shift registers, and SD cards. Simply put, it is one of the communication methods for exchanging data between devices and devices, namely between integrated chips (ICs) and chips. SPI communication is a synchronous communication method that supports one-to-many communication, which has the disadvantage of requiring multiple lines for multiple communication. You can transmit and receive data at the same time. It is easily wired, so it is often used for communication between chips such as simple sensors and memory.

The following is a demo program for accessing standard Linux spidev devices from userspace.

You can use the following command to test a program that controls dot-matrix through actual SPI communication.

```bash
$ apt install python3-pip git

$ pip3 install luma.core luma.led_matrix

$ git clone https://github.com/rm-hull/luma.led_matrix.git

$ python3 luma.led_matrix/examples/matrix_demo.py
```

<div style="display: flex; justify-content: center;">
    <img src="https://github.com/Topst-Dev/Documentation/assets/144076415/61ca0d9a-d2f9-4829-81bc-f6745c60f490" width="500" height="350" style="margin: auto;">
</div>
<p align="center"><strong>Figure 5.18 Dot-matrix Test with SPI</strong></p>

### 1.2.5 Inter-integrated Circuit (I2C)

The inter-integrated circuit (I2C) is easily read as "i-to-c", but the formal pronunciation is "i-square-c".

The I2C communication consists of two lines: one Serial Data (SDA) line for transmitting and receiving data and one Serial Clock line (SCL) for synchronizing transmission and reception timing. It consists of one master and one or more slaves, and up to 127 slaves can be connected. I2C has an advantage of being time-free as it is a synchronous communication method that always uses clock signals. The disadvantage of I2C is that it is unsuitable to use with long data because address data is always attached for slave selection.

```bash
i2cdetect - detect I2C chips

i2cdetect [-y] [-a] [-q|-r] i2cbus [first last]

i2cdetect -F i2cbus

i2cdetect -V

i2cdetect -l

---

**Description**

**i2cdetect** is a userspace program to scan an I2C bus for devices. It outputs a table with the list of detected devices on the specified bus. **i2cbus** indicates the number or name of the I2C bus to be scanned, and should correspond to one of the buses listed by **i2cdetect -l**. The optional parameters first and last restrict the scanning range (default: from 0x03 to 0x77).

**i2cdetect** can also be used to query the functionalities of an I2C bus (see option **-F**.)

**Warning**

This program can confuse your I2C bus, cause data loss or worse.

**Interpreting the Output**

Each cell in the output table will contain one of the following symbols:

n  "--". The address was probed but no chip answered.

n  "UU". Probing was skipped, because this address is currently in use by a driver. This strongly suggests that there is a chip at this address.

An address number in hexadecimal, for example, "2D" or "4E,” means a chip was found at this address.

**Options**

- **y**

Disable interactive mode. By default, **i2cdetect** will wait for a confirmation from the user before messing with the I2C bus. When this flag is used, it will perform the operation directly. This is mainly meant to be used in scripts.

- **a**

Force scanning of non-regular addresses. Not recommended.

- **q**

Use SMBus "quick write" commands for probing (by default, the command used is the one believed to be the safest for each address). Not recommended. This is known to corrupt the Atmel AT24RF08 EEPROM found on many IBM Thinkpad laptops.

- **r**

Use SMBus "read byte" commands for probing (by default, the command used is the one believed to be the safest for each address). Not recommended. This is known to lock SMBus on various write-only chips (most notably clock chips at address 0x69).

- **F**

Display the list of functionalities implemented by the adapter and exit.

- **V**

Display the version and exit.

- **l**

Output a list of installed busses.
```

<div style="display: flex; justify-content: center;">
    <img src="https://github.com/Topst-Dev/Documentation/assets/144076415/e733d7ad-a126-4ffc-97a7-f760d552140d" width="500" height="350" style="margin: auto;">
</div>
<p align="center"><strong>Figure 5.19 I2C Device</strong></p>

```bash
$ pip install smbus2

$ pip install RPLCD

$ rplcd-tests i2c testsuite expander=PCF8574 addr=0x3f port=1 cols=16 rows=2 charmap=A00
```

<div style="display: flex; justify-content: center;">
    <img src="https://github.com/Topst-Dev/Documentation/assets/144076415/e9324725-10f1-4076-b7a2-188082435d80" width="500" height="350" style="margin: auto;">
</div>
<p align="center"><strong>Figure 5.20 I2C LCD Test</strong></p>

### 1.2.6 ROS2

Robot Operating System (ROS) is an open-source, meta-operating system for robots that provides libraries, development, and debugging tools for message passing, package management, and development environments between processes, such as hardware abstraction, sub-device control, and robotics.

Refer to “*TOPST D3 Common SDK-Install Guide for ROS2*” and perform the

```bash
$ sudo apt-get install ros-humble-desktop
```

---

- Set server environment.

```bash
$ source /opt/ros/humble/setup.bash

$ ros2 run demo_nodes_cpp talker
```

<div style="display: flex; justify-content: center;">
    <img src="https://github.com/Topst-Dev/Documentation/assets/144076415/8b4f7fe7-d430-4384-9ac2-c24b7c2618f0" width="500" height="350" style="margin: auto;">
</div>

- Set client environment.

```bash
$ source /opt/ros/humble/setup.bash

$ ros2 run demo_nodes_py listener
```

<div style="display: flex; justify-content: center;">
    <img src="https://github.com/Topst-Dev/Documentation/assets/144076415/26c2d6b5-5992-4e1e-b1f0-695d6ed5e1c3" width="500" height="350" style="margin: auto;">
</div>