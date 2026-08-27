# 1. 簡介
---
本文件說明如何針對 TOPST 車輛控制處理器（VCP）使用 Arduino IDE。VCP 是一款專為車用應用設計、以 TCC7045 為基礎的高效能處理器。其目標是將 VCP-G 整合至 Arduino 環境，提供一個兼具 Arduino 簡易性與彈性、並針對車用半導體量身打造的開發環境，以簡化並加速開發流程。  

本文件包含下列資訊：  
- 安裝指南

</br></br></br></br>

# 2. 安裝指南
---
本章說明如何下載並安裝 VCP-G Arduino 套件，以搭配 Arduino 整合開發環境（IDE）使用。

</br></br></br>

## 2.1 安裝指南
---
**步驟 1：下載 Arduino IDE**

首先，您需要 Arduino IDE，它是用來為 Arduino 開發板撰寫程式的平台。  
1. 請造訪 Arduino 官方網站：[Arduino Software](https://www.arduino.cc/en/software)
2. 選擇適合您作業系統的版本（Windoiws、macOS 或 Linux）。
3. 下載並執行安裝程式。

**步驟 2：安裝 Arduino IDE**  
請依照您的作業系統，按下列步驟安裝 Arduino IDE：  

- Windows：
    1. 執行下載的 .exe 檔案。
    2. 依照安裝提示進行。請確認已安裝所有必要的驅動程式。
- macOS：
    1. 開啟 .dmg 檔案
    2. 將 Arduino 應用程式拖曳至您的「應用程式」資料夾。
- Linux：
    1. 解開 .tar.xz 檔案。
    2. 在解壓縮後的目錄中開啟終端機。
    3. 執行 ./install.sh 進行安裝。

**步驟 3：將 VCP-G .json 檔案加入 Arduino IDE**  
若要為 VCP-G 撰寫程式，您必須透過開發板管理員（Board Manager）將 VCP-G .json 檔案加入 Arduino IDE。
1. 開啟 Arduino IDE。
2. 前往 **File > Preferences**。
3. 在 **"Additional Board Manager URLs"** 欄位中，加入下列 URL：
    ```
    https://raw.githubusercontent.com/topst-development/VCP-Arduino_Board_Manager/develop/package_topst_vcp_index.json
    ```
4. 按一下 **OK** 儲存變更。
5. 前往 **Tools > Board > Boards Manager.**
6. 在開發板管理員中搜尋「TOPST VCP-G」。
7. 當 TOPST VCP-G 項目出現時，請從下拉式選單選擇 v1.0.0，然後按一下 **Install**。

**步驟 4：選擇 VCP-G**  
安裝完成後，您需要選擇 TOPST VCP-G 開發板：  
1. 在 Arduino IDE 中前往 **Tools > Board**。
2. 向下捲動找到 "TOPST VCP-G" 並選取它。

**步驟 5：驗證安裝**  
請上傳一個簡單的 sketch，測試您的設定是否正常運作：
1. 使用 USB 將 VCP-G 開發板連接至您的 PC。
2. 在 **Tools > Port** 下選擇適當的連接埠。
3.	開啟 **File > Examples > 01.Basics > Blink**。
4.	按一下 **Upload**，將 sketch 傳送至開發板。  
    **註：** 若上傳過程卡在無止盡的上傳狀態，是因為未啟用 FWDN 模式。請拔除電源線，按住 FWDN 開關，重新接上電源線，然後放開按鈕。若問題仍然存在，請嘗試以系統管理員權限執行 Arduino IDE。
5.	若開發板上的 LED 開始閃爍，表示開發板已正確設定完成。

</br></br></br>

## 2.2 疑難排解
---
若您在設定過程中遇到任何問題，請參閱 [Arduino Troubleshooting Guide](https://www.arduino.cc/en/Guide/Troubleshooting)。  
如需更多資訊與進階功能，請參閱 VCP-G 文件，或造訪 [Arduino Help Center](https://support.arduino.cc/hc/en-us)。

</br></br></br></br>

# 3. 參考資料
---
- 如需更多詳細資訊，請聯絡 TOPST：topst@topst.ai

**註：** 參考文件可於條件允許時提供，實際情形視合約條款而定。若參考
文件無法提供，則可就與您開發工作直接相關的內容提供指引。

