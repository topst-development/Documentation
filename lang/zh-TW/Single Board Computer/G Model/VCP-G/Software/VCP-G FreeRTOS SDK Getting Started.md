# 1. 簡介
---
本文件提供 VCP-G SDK 軟體開發環境的建置指引，說明所需的工具、設定與工具鏈。

</br></br></br></br>

# 2. 設定主機環境
---
## 2.1 安裝 Ubuntu
---
建議在 Ubuntu 22.04 上建置開發環境。此 Ubuntu 版本提供穩定的平台與廣泛的社群支援，可確保與 VCP-G 及相關工具鏈的相容性與易用性。

Linux 發行版本：  
- Ubuntu 22.04 (LTS)

</br></br></br>

## 2.2 安裝 WSL2 Ubuntu（僅限 Windows 環境）
---
**注意：**若您使用 Ubuntu 主機，可略過 WSL2 的安裝。  

1.	依序點選 **Control Panel -> Programs -> Windows Features On/Off -> Enable Virtual Machine Platform & Hyper-V** 以設定 Windows 功能。
2.	以 **“Run with administrator privileges”.** 方式執行 Windows Powershell。
3.	啟用 WSL2 系統。
    ```
    dism.exe /online /enable-feature /featurename:Microsoft-Windows-Subsystem-Linux /all /norestart
    ```
4.	啟用虛擬機器功能。
    ```
    dism.exe /online /enable-feature /featurename:VirtualMachinePlatform /all /norestart
    ```
5.	將 WSL 的預設版本設定為 2（WSL2）。
    ```
    wsl --set-default-version 2
    ```
6.	在 Microsoft Store 中搜尋 Ubuntu 22.04 LTS 並下載。

    * 若您需要下載 Linux 核心更新套件，請於[此處](https://learn.microsoft.com/ko-kr/windows/wsl/install-manual)下載最新的套件。
7.	在 WSL 清單中確認 Ubuntu 22.04。
    ```
    wsl --list -online
    ```
8.	安裝 Ubuntu 22.04。
    ```
    wsl --install Ubuntu-22.04
    ```
9.	在 Windows 搜尋方塊中搜尋 WSL2 並執行。 

</br></br></br>

## 2.3 設定 Linux 環境
---
若要在主機 PC 上建置 Linux 環境，請依照下列步驟操作：  

1. 執行 WSL2（僅限 Windows 環境）  
    若您使用 Windows，請在 Windows PowerShell 中執行下列其中一個命令以啟動 WSL2。  
    ```
    wsl
    ```
    ```
    ubuntu
    ```

2.	更新套件清單  
在安裝任何新軟體之前，請先更新可用套件清單，以確保取得最新版本與相依套件。下列命令會從套件庫取得最新的可用套件清單。
    ```
    sudo apt update && /
    sudo apt upgrade
    ```

3.	安裝常用開發工具  
    請輸入下列命令以安裝常用開發工具：
    ```
    sudo apt install build-essential git
    ```

**注意：**此命令會同時安裝 build-essential 套件與 git。

</br></br></br></br>

# 3. 工具鏈
---
VCP-G 使用 **gcc-linaro-7.2.1-2017.11-x86_64_arm-eabi** 工具鏈。  
此工具鏈針對 ARM 架構最佳化，可確保與 VCP-G 上 TCC7045 晶片的相容性。

</br></br></br>

## 3.1 安裝與設定工具鏈
---
請依照下列步驟下載、解壓縮並設定工具鏈：  
1. 下載工具鏈  
   請輸入 **wget** 命令，從 Linaro 網站下載工具鏈：
    ```
    wget https://releases.linaro.org/components/toolchain/binaries/7.2-2017.11/arm-eabi/gcc-linaro-7.2.1-2017.11-x86_64_arm-eabi.tar.xz
    ```
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/Download%20Toolchain.png"></p>
    <p align="center"><strong>圖 3.1 下載工具鏈</strong></p>
    
2. 解壓縮工具鏈  
    下載完成後，請解壓縮 .tar.xz 檔案的內容。
    ```
    tar -xvf gcc-linaro-7.2.1-2017.11-x86_64_arm-eabi.tar.xz
    ```
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/Extract%20Toolchain.png"></p>
    <p align="center"><strong>圖 3.2 解壓縮工具鏈</strong></p>
    
3. 將工具鏈移至 /opt  
    /opt 目錄是 Linux 上選用軟體的標準存放位置。請將解壓縮後的工具鏈移至此目錄。
    ```
    sudo mv gcc-linaro-7.2.1-2017.11-x86_64_arm-eabi /opt/
    ```
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/Move%20Toolchain.png"></p>
    <p align="center"><strong>圖 3.3 移動工具鏈</strong></p>

</br></br></br>

## 3.2 驗證工具鏈
---
以確保工具鏈已正確安裝。  
1. 前往工具鏈目錄
    ```
    cd /opt/gcc-linaro-7.2.1-2017.11-x86_64_arm-eabi
    ```
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/Navigate%20to%20Toolchain%20Directory.png"></p>
    <p align="center"><strong>圖 3.4 前往工具鏈目錄</strong></p>
    
2. 檢查已安裝的 GCC 編譯器版本
    ```
    ./bin/arm-eabi-gcc --version
    ```
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/Check%20Version%20of%20Installed%20GCC%20Compiler.png"></p>
    <p align="center"><strong>圖 3.5 檢查已安裝的 GCC 編譯器版本</strong></p>

成功安裝 GCC 編譯器後，請驗證已安裝的 GCC 編譯器版本，以確認其符合 **gcc-linaro-7.2.1-2017.11.**

</br></br></br></br>

# 4. 複製原始碼
---
本章說明如何使用 Git 複製原始碼。

</br></br></br>

## 4.1 複製 VCP-G 原始碼
---
若要取得 VCP-G 的原始碼，請輸入 **git clone** 命令。此命令會在您的本機建立遠端儲存庫的副本，讓您可以直接使用該程式碼。

請依照下列步驟複製 VCP-G 原始碼：
1. 開啟終端機  
    請在您的 Ubuntu 22.04 系統上啟動終端機應用程式。

2. 前往所需的目錄  
    請選擇適當的位置來儲存原始碼。例如，若您想將儲存庫存放在家目錄中，請使用下列命令。
    ```
    cd ~
    ```
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/Navigate%20to%20Desired%20Directory.png"></p>
    <p align="center"><strong>圖 4.1 前往所需的目錄</strong></p>

3. 複製儲存庫  
    請使用下列命令，從提供的 git 位址複製 VCP-G 原始碼。
    ```
    git clone https://github.com/topst-development/FreeRTOS-VCP.git topst-vcp
    ```
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/Figure%204.2%20Clone%20Repository.png"></p>
    <p align="center"><strong>圖 4.2 複製儲存庫</strong></p>

4. 前往複製後的目錄  
    複製程序完成後，請使用下列命令前往包含原始碼的目錄。
    ```
    cd topst-vcp
    ```
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/Navigate%20to%20Cloned%20Directory.png"></p>
    <p align="center"><strong>圖 4.3 前往複製後的目錄</strong></p>

VCP-G 原始碼現已可在本機進行建置與開發。

</br></br></br>

## 4.2 原始碼結構
---
複製完成後，請輸入 **ls** 命令列出目錄內容，並檢視主要檔案以了解原始碼結構。
```
ls

build  documents  easy-setup_vcp.sh  LICENSE  scripts  sources  tools
```

</br></br></br></br>

# 5. 建置指南
---
## 5.1 執行 easy-setup_vcp-g.sh
---
若您執行 ./easy-setup_vcp-g.sh 腳本，將會看到下列畫面。

**警告**：若您重新執行 ./easy-setup_vcp-g.sh，請特別注意，若選擇 yes，已建置的原始碼將會被刪除。
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20AI-G/Software/Linux%20SDK/license1.png"></p>
<p align="center"><strong>圖 5.1 使用者授權合約</strong></p>

請向下捲動至畫面底部並閱讀此聲明。閱讀完畢後，請按右方向鍵，然後按 [Enter]。
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20AI-G/Software/Linux%20SDK/license2.png"></p>
<p align="center"><strong>圖 5.2 前往 'Proceed to confirm'</strong></p>


接著會看到以下畫面。 
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20AI-G/Software/Linux%20SDK/license3.png" ></p>
<p align="center"><strong>圖 5.3 接受畫面 </strong></p>
若您按下 [Enter] 選擇 Accept，即可使用下列命令進行建置。

</br></br></br>

## 5.2 Makefile 與建置系統
---
Makefile 是許多建置系統的關鍵組成部分，其中包含供 **make** 工具編譯與連結程式的規則與指示。透過使用 Makefile，您可以將建置流程自動化，確保一致性與效率。

</br></br></br>

## 5.3 啟動建置流程
---
若要建置原始碼，請依照下列步驟操作：  
1. 前往建置目錄。
    ```
    cd build/tcc70xx/gcc/
    ```
2. 執行 **make** 命令。  
    ```
    make
    ```
    **make** 命令會讀取目前目錄中的 Makefile 並執行建置流程。
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/Run%20make%20Command.png"></p>
    <p align="center"><strong>圖 5.4 執行 make 命令 </strong></p>
    
3. 驗證建置輸出  
    建置流程完成後，終端機中應會列出下列輸出檔案。
    - output/tcc70xx_pflash_boot.rom
    - output/tcc70xx_pflash_boot_2M_ECC.rom
    - output/tcc70xx_pflash_boot_3M_ECC.rom
    - output/tcc70xx_pflash_boot_4M_ECC.rom
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/Verify%20Build%20Output.png"></p>
    <p align="center"><strong>圖 5.5 驗證建置輸出</strong></p>
   
    若要檢查輸出檔案清單，請使用下列命令：
    ```
    ls output/ -al
    ```
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/Build%20Output%20File.png"></p>
    <p align="center"><strong>圖 5.6 建置輸出檔案</strong></p>

</br></br></br></br>

# 6. 韌體下載
---
本章說明如何在以 Linux 為基礎的開發環境中，將 ***FWDN*** 下載至 VCP-G。

</br></br></br>

## 6.1 準備 VCP-G
---
在開始下載程序之前，請確認 VCP-G 位於穩固的位置且不受任何潛在干擾。請確認所有開關與接頭皆易於操作，且 3.3V 電源線已正確連接。

</br></br></br>

## 6.2 將硬體連接至主機 PC
---
若您使用 Ubuntu 主機，請直接前往步驟 3。  
1. 下載 usbipd-win  
    在 WSL2 中使用 USB 需要 usbipd-win 專案。   
    請從 https://learn.microsoft.com/ko-kr/windows/wsl/connect-usb#attach-a-usb-device 下載 usbipd-win。
2. 執行 PowerShell，並將 VCP-G（在 Windows 中辨識為 COM 連接埠）掛載至 WSL2  
    請在 Windows PowerShell（而非 Linux）中執行下列命令。
    ```
    usbipd list
    ```
    ```
    usbipd bind --busid <busid>
    ```
    ```
    usbipd attach --wsl --busid <busid>
    ```
3. 連接 USB Type-C 傳輸線  
    請使用 USB Type-C 傳輸線將 VCP-G 開發板連接至開發主機 PC。
4. 驗證 USB 連線  
    請在 WSL2 中執行下列命令。
    ```
    sudo apt-get install usbutils && lsusb
    ```
    ```
    sudo dmesg | grep tty
    ```
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/Verify%20USB%20Connection.png"></p>
    <p align="center"><strong>圖 6.1 驗證 USB 連線</strong></p>

若出現圖 6.1 所示的輸出，表示連線已成功建立。

</br></br></br>

## 6.3 將軟體下載至 VCP-G
---

### 6.3.1 在 Windows 環境中執行 FWDN
1. 將開發板設為下載模式  
   請在按住 FWDN 開關的同時，將電源線連接至 VCP-G 開發板。
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/Set%20Board%20to%20Download%20Mode.png"></p>
    <p align="center"><strong>圖 6.2 將開發板設為下載模式</strong></p>

2. 將 tcc70xx_pflash_boot_2M_ECC.rom 複製到 fwdn_vcp 資料夾
```
cp ~/topst-vcp/build/tcc70xx/gcc/output/tcc70xx_pflash_boot_2M_ECC.rom ~/topst-vcp/tools/fwdn_vcp/
```

3. 將 fwdn_vcp 資料夾複製到 C 磁碟機
```
cp -r ~/topst-vcp/tools/fwdn_vcp /mnt/c/
```

4. 點選 fwdn_vcp.bat  
    請使用 ***FWDN*** 將建置完成的軟體下載至 VCP-G 上的 4 MB flash。

    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/Click%20fwdn_vcp.bat.png"></p>
    <p align="center"><strong>圖 6.3 點選 fwdn_vcp.bat</strong></p>
```
[main:27] FWDN VCP v0.1.1 - 2022.8.12 11:38:19
Com port num : 10
[FWDNWindowsUART::OpenPort:34] Complete open port(\\.\COM10)
[ProtocolCB::StartVCPFWDN:45] Complete to receive start res
[FWDN_VCP::LoadFwdnFW:144] Complete to send start msg
[ProtocolCB::CheckResPacket:172] Complete to receive ack for cmd(0xFFFF0000(RECEIVE_HSM_CMD))
[FWDN_VCP::WriteFile:284] Complete to send command(0xFFFF0000(RECEIVE_HSM_CMD))
[ProtocolCB::SendFile:151] Complete to send file
[ProtocolCB::CheckResPacket:172] Complete to receive ack for cmd(0xFFFF0000(RECEIVE_HSM_CMD))
[FWDN_VCP::WriteFile:295] Complete to send file - .\tcc70xx_pflash_boot_2M_ECC.rom
[FWDN_VCP::LoadFwdnFW:163] Complete to send hsm
[ProtocolCB::CheckResPacket:172] Complete to receive ack for cmd(0xFFFF0001(RECEIVE_FWDN_CMD))
[FWDN_VCP::WriteFile:284] Complete to send command(0xFFFF0001(RECEIVE_FWDN_CMD))
[ProtocolCB::SendFile:126] uiRemainSize = 43136
[ProtocolCB::SendFile:151] Complete to send file
[ProtocolCB::CheckResPacket:172] Complete to receive ack for cmd(0xFFFF0001(RECEIVE_FWDN_CMD))
[FWDN_VCP::WriteFile:295] Complete to send file - .\vcp_fwdn.rom
[FWDN_VCP::LoadFwdnFW:173] Complete to send fwdn
[FWDN_VCP::LoadFwdnFW:179] Complete to load FWDN F/W
RM=00000000
MT
MR0=0000a042
MR1=00020018
MR2=00000000
[ProtocolFW::CheckResPacket:260] Complete to receive ack for cmd(0xAAAA0016(VERSION_CMD))
[FWDN_VCP::GetDeviceVersion:77]  FWDN Firmware Version(20230728)
[ProtocolFW::CheckResPacket:260] Complete to receive ack for cmd(0xAAAA0014(STORAGE_INFO_CMD))
[FWDN_VCP::InfoStorage:56]
#### SNOR Info ####
Manufacture ID: 0x9d
Device ID: 0x6015
Name: ISSI-IS25LP016D
Sector Size: 4 KiB (4096 Byte)
Total Capacity: 2 MiB (2097152 Byte)
4Byte Address Mode: Unsupported
#### EFLASH Info ####
DCYCRDCON 0x1e0002
DCYCWRCON 0x20100
Sector Size: 8 KiB
Page Size: 2 KiB

-----Storage init info-----
O : Init success
X : Init failed or not exist
SNOR : O
eFlash : O

[ProtocolFW::CheckResPacket:260] Complete to receive ack for cmd(0xAAAA0017(CHIP_INFO_CMD))
[FWDN_VCP::GetChipInfo:121] ---chip info---
Chip Number : 0x57045
Dual Bank : false
Expand Flash : true
ECC : true
[FWDN_VCP::PrintBankInfo:468] ---bank info---
bank - 0
eFlash offset : 0x0
eFlash size : 2097152 byte
SNOR offset : 0x0
SNOR size : 2097152 byte
[FWDN_VCP::PrintStorageOption:451] ---storage info---
eflash
offset : 0x0
size : 2097152 byte
[ProtocolFW::CheckResPacket:260] Complete to receive ack for cmd(0xAAAA0011(WRITE_CMD))
[FWDN_VCP::WriteFile:284] Complete to send command(0xAAAA0011(WRITE_CMD))
 100% [||||||||||||||||||||||||||||||] 2097152/2097152
```

5. 重設開發板  
    下載程序完成後，請拔除電源線後再重新連接。
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/Reset%20the%20Board.png"></p>
    <p align="center"><strong>圖 6.4 重設開發板</strong></p>

### 6.3.2 在 Linux 環境中執行 FWDN
1. 將開發板設為下載模式  
   請在按住 FWDN 開關的同時，將電源線連接至 VCP-G 開發板。
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/Set%20Board%20to%20Download%20Mode.png"></p>
    <p align="center"><strong>圖 6.5 將開發板設為下載模式</strong></p>
    
2. 執行下載命令  
   請使用 ***FWDN*** 將建置完成的軟體下載至 VCP-G 上的 4 MB flash。
    ```
    sudo ~/topst-vcp/tools/fwdn_vcp/fwdn --fwdn ~/topst-vcp/tools/fwdn_vcp/vcp_fwdn.rom -w output/tcc70xx_pflash_boot_2M_ECC.rom
    ```
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/Execute%20Download%20Command.png"></p>
    <p align="center"><strong>圖 6.6 執行下載命令</strong></p>
    
3. 重設開發板  
    下載程序完成後，請拔除電源線後再重新連接。
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/Reset%20the%20Board.png"></p>
    <p align="center"><strong>圖 6.7 重設開發板</strong></p>

</br></br></br>

## 6.4 在開發板上驗證軟體
---
將軟體下載至開發板後，請依照下列步驟驗證其是否正常運作。
1. 安裝 minicom  
    ```
    sudo apt install minicom
    ```
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/Install%20Minicom.png"></p>
    <p align="center"><strong>圖 6.8 安裝 minicom</strong></p>
2. 開啟序列連線  
    請使用下列命令啟動序列連線。
    ```
    minicom -D /dev/ttyUSB0 -b 115200 -8
    ```
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/Open%20Serial%20Connection.png"></p>
    <p align="center"><strong>圖 6.9 開啟序列連線</strong></p>

完成步驟 1 與 2 後，終端機上會出現下列輸出。若連線成功，開發板應會回應操作，確認軟體已下載且在 VCP-G 上正常運作。
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/Figure%206.7%20Open%20Serial%20Connection.png"></p>
<p align="center"><strong>圖 6.10 開啟序列連線</strong></p>

</br></br></br>

## 6.5 常見問題排解
---
本章提供使用 VCP-G 時常見問題的解決方法。

**問題：** ***FWDN*** 回報沒有存取 ttyUSB0 裝置的權限。  
**解決方法：**當您的使用者帳號（**$USER**）沒有存取序列裝置的必要權限時，就會發生此問題。若要解決此問題，請將該使用者帳號加入 dialout 群組。

1. 修改使用者群組權限  
    請執行下列命令。
    ```
    sudo usermod -aG dialout $USER
    ```
2. 登出後重新登入  
    請登出目前的工作階段後重新登入以套用變更。之後請再次嘗試存取 ttyUSB0 裝置。
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/Modify%20User%20Group%20Permissions.png"></p>
    <p align="center"><strong>圖 6.11 修改使用者群組權限 </strong></p>

**問題：**使用 minicom 時，與 VCP-G 之間無法正常通訊或出現異常行為。  
**解決方法：**若 minicom 的預設流量控制設定為 **hardware**，就可能發生此問題。硬體流量控制必須設為 No 才能正常運作。 
1. 啟動 minicom  
    請使用下列命令。
    ```
    minicom -D /dev/ttyUSB0 -b 115200 -8
    ```
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/Launch%20Minicom.png"></p>
    <p align="center"><strong>圖 6.12 啟動 minicom</strong></p>
2. 進入設定畫面  
    在 minicom 中，請按下 **[Ctrl+A]** 再按 **[o]** 以開啟設定選單。
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/Access%20Set%20up%20Screen.png"></p>
    <p align="center"><strong>圖 6.13 進入設定畫面</strong></p>
3. 前往 Serial Port Setup  
    請從選項中選擇 **Serial port setup**。
4. 修改流量控制  
    在序列埠設定中，請按下 **[F]** 將硬體流量控制設為 **No**。
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/Modify%20Flow%20Control.png"></p>
    <p align="center"><strong>圖 6.14 修改流量控制</strong></p>
5. 結束並儲存  
    請結束設定並儲存設定內容。minicom 現在應可與 VCP-G 正常通訊。
    <p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20VCP-G/Software/Save%20and%20Exit.png"></p>
    <p align="center"><strong>圖 6.15 儲存並結束</strong></p>

**注意：**若您使用 minicom 以外的其他序列通訊工具，請確認其流量控制設定同樣設為 **No**，以確保正常運作。
</br></br></br></br>

# 7. 參考資料
---
- 如需更多詳細資訊，請聯絡 TOPST：topst@topst.ai

**註：**參考文件可依合約條款於可提供時提供。若參考
文件無法提供，則可就與您的開發直接相關的內容提供指引。
