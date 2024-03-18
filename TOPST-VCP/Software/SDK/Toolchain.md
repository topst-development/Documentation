# 4 Toolchain

A toolchain is a crucial component in the development process, especially when working with specialized hardware like the TOPST-VCP board. It provides a collection of tools that allow developers to compile, link, and debug their code for the target platform.

## 4.1 Overview of Toolchains

A toolchain typically consists of a compiler, linker, assembler, and debugger, among other tools. These components work in tandem to transform source code into executable programs that can run on the target hardware. Given the variety of hardware architectures and platforms, it's essential to choose and configure the right toolchain tailored for the target board

## 4.2 Choosing the toolchain for board

For the TOPST-VCP board, which is based on the ARM Cortex-R5 architecture, the recommended toolchain is gcc-linaro-7.2.1-2017.11-x86_64_arm-eabi.

This toolchain is optimized for the ARM architecture and ensures compatibility with the TCC7045 chip on the board.

## 4.3 Installing and Setting Up the Toolchain

Follow the steps below to download, extract, and set up the toolchain:

1. **Download the Toolchain** : Use wget command to download the toolchain from the Linaro website :

```bash
wget https://releases.linaro.org/components/toolchain/binaries/7.2-2017.11/arm-eabi/gcc-linaro-7.2.1-2017.11-x86_64_arm-eabi.tar.xz
```

<p align="center">
    <img src="https://github.com/Topst-Dev/Documentation/assets/144076415/da888bbb-e52f-489b-86ec-287429ba98c6" width="800" height="350">
</p>
<p align="center"><strong>Figure 4.1 Toolchain Website</strong></p>

<p align="center">
    <img src="https://github.com/Topst-Dev/Documentation/assets/144076415/bef0f6d4-526d-4422-9234-cfa749080be7" width="750" height="400">
</p>
<p align="center"><strong>Figure 4.2 Download the Toolchain in progress</strong></p>

2. **Extract the Toolchain** : Once the download is complete, extract the contents of the .tar.xz file

```bash
tar -xvf gcc-linaro-7.2.1-2017.11-x86_64_arm-eabi.tar.xz
```


<p align="center">
    <img src="https://github.com/Topst-Dev/Documentation/assets/144076415/049fc4ac-04b2-4896-951c-de758cfd4b08" width="750" height="400">
</p>
<p align="center"><strong>Figure 4.3 Extract the ToolChain</strong></p>

3. **Move the Toolchain to /opt** : The /opt directory is a standard location for optional software on Linux. Move the extracted toolchain to this directory

```bash
sudo mv gcc-linaro-7.2.1-2017.11-x86_64_arm-eabi /opt/
```


<p align="center">
    <img src="https://github.com/Topst-Dev/Documentation/assets/144076415/d83e6951-a739-4dfc-86fe-2a3b39bce7b8" width="750" height="400">
</p>
<p align="center"><strong>Figure 4.4 Move the ToolChain</strong></p>

## 4.4 Verifying the toolchain Installation

To ensure that the toolchain has been installed correctly:

1. **Navigate to the toolchain directory** :

```bash
cd /opt/gcc-linaro-7.2.1-2017.11-x86_64_arm-eabi
```

2. **Check the version of the installed GCC compiler** :

```bash
./bin/arm-eabi-gcc --version
```

If the installation was successful, you should see information about the version of GCC installed, confirming that it aligns with the gcc-linaro-7.2.1-2017.11 version.
