---
title: TOPST Imager 使用者指南
description: 說明如何在 Windows 或 Linux 上為 TOPST 開發板安裝作業系統映像檔。
---

# TOPST Imager 使用者指南

TOPST Imager 是用於在 TOPST 開發板上安裝作業系統或韌體的應用程式。
不需要熟悉電腦或電子設備。請搭配本指南和應用程式中的提示，慢慢逐步操作。

> **重要：** 燒錄可能會清除開發板 eMMC 中的所有內容。開始前請備份所需檔案。

## 1. 常用術語

| 應用程式中的術語 | 簡單說明 |
| --- | --- |
| Board | 要安裝作業系統的 TOPST 裝置。 |
| Image | 要安裝至開發板的作業系統檔案。 |
| Flashing | 將映像檔寫入開發板的過程。 |
| Boot mode | 允許電腦向開發板安裝映像檔的特殊狀態。 |
| FWDN | 安裝映像檔的內部工具，不需要自行執行。 |
| COM port | 電腦用來識別透過 USB 連接的開發板的名稱。 |
| eMMC | 開發板內建的儲存裝置。 |

## 2. 支援的開發板與映像檔

| 開發板 | 自訂映像檔格式 | 所需連線 |
| --- | --- | --- |
| TOPST D3-G | `.fai` | FWDN USB Type-C 資料傳輸線 |
| TOPST AI-G | `.fai` | FWDN USB Type-C 資料傳輸線與乙太網路線 |
| TOPST VCP-G | `.rom` | FWDN USB Type-C 資料傳輸線 |

> 僅供充電的 USB 線無法使用。請使用**支援資料傳輸的 USB Type-C 線**。

## 3. 開始前的準備

- 要燒錄的 TOPST 開發板及其電源供應器
- 支援資料傳輸的 USB Type-C 線
- 已連接網際網路的電腦
- 使用 AI-G 時所需的乙太網路線
- 足夠下載及解壓縮官方映像檔的電腦儲存空間
- 開發板上重要資料的備份

燒錄期間，請勿關閉開發板、拔除 USB 或乙太網路線、關閉 TOPST Imager、關閉電腦或讓電腦進入睡眠狀態。

## 4. 基本流程

Windows 和 Linux 的基本流程相同。

1. 啟動 TOPST Imager。
2. 選取開發板。
3. 選取作業系統或 **Custom Image**。
4. 選取要安裝的版本。
5. 按照應用程式提示連接並進入開機模式。
6. 開始燒錄。
7. 等待 **Complete** 畫面出現。

可以按一下項目後選取 **Next**，也可以按兩下項目進入下一步。

---

# Windows 使用說明

## 5. 在 Windows 上安裝 TOPST Imager

### 5.1 支援的系統

- Windows 10 64 位元或更新版本
- Windows 11 64 位元

### 5.2 安裝應用程式

1. 從 TOPST 官方網站下載 Windows 版 `TOPST Imager.exe`。
2. 按兩下下載的檔案。
3. 閱讀並接受授權合約。
4. 視需要勾選桌面捷徑選項。
5. 選取 **Install**。
6. 完成後選取 **Launch TOPST Imager**，然後結束安裝精靈。

若 Windows 顯示保護訊息，請先確認安裝程式來自 TOPST 官方網站。無法確認來源時請勿執行。

預設安裝位置：

```text
%LOCALAPPDATA%\Programs\TOPST Imager
```

## 6. 語言與顯示佈景主題

1. 選取視窗左下角的 **App Options**。
2. 選取所需語言。
3. 選取 **Save**。

> 螢幕擷取畫面中的紅框和數字是本指南額外加入的，實際應用程式中不會顯示。

![選取 TOPST Imager 的語言與支援選項](https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/Quick%20Guide/TOPST%20Imager%20App%20Options.png)

1. **Language：** 選取語言。
2. **Ask the Community：** 需要協助時開啟 TOPST 社群。
3. **Save：** 套用所選語言。

支援韓文、英文、日文、簡體中文、繁體中文、泰文和德文。淺色或深色外觀自動跟隨 Windows 系統佈景主題。

## 7. 安裝官方映像檔

### 7.1 選取開發板

1. 核對開發板圖片與名稱。
2. 按一下所需的開發板。
3. 確認選取項目的顏色已變更。
4. 選取 **Next**。

![選取 D3-G 開發板與 Next 按鈕](https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/Quick%20Guide/TOPST%20Imager%20Board%20Selection.png)

1. 選取所需的**開發板項目**。
2. 確認後選取 **Next**。

若選錯，請選取 **Back** 返回重選。

### 7.2 選取作業系統與版本

1. 選取作業系統，然後選取 **Next**。
2. 選取要安裝的版本。
3. 核對發行日期與檔案大小。

![選取官方作業系統或自訂映像檔](https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/Quick%20Guide/TOPST%20Imager%20OS%20Selection.png)

1. 使用官方映像檔時，選取所需的**作業系統**。
2. 使用電腦中的檔案時，選取 **Use Custom Image**。
3. 確認後選取 **Next**。

![選取作業系統版本與 Flashing 按鈕](https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/Quick%20Guide/TOPST%20Imager%20Version%20Selection.png)

1. 選取**版本**，核對下載大小與發行日期。
2. 正確後選取 **Flashing**。

- **Download size：** 從網際網路下載的壓縮檔大小。
- **Extracted size：** 解壓縮後預計占用的電腦空間。

不一定必須使用最新版本。沒有其他指示時，請選取建議版本或最新穩定版本。

### 7.3 確認清除警告

燒錄前，應用程式會警告開發板的 eMMC 內容可能被清除。

1. 再次核對開發板與映像檔。
2. 確認開發板上沒有需要保留的資料。
3. 準備好後選取確認按鈕。

![含 Cancel 與 Confirm 按鈕的 eMMC 清除警告](https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/Quick%20Guide/TOPST%20Imager%20eMMC%20Erase%20Warning.png)

1. 尚未準備好或需要重新檢查時，選取 **Cancel**。
2. 瞭解 eMMC 內容可能被清除後，才選取 **Confirm**。

不確定時選取 **Cancel**。此時取消不會清除開發板。

## 8. 燒錄 D3-G

### 8.1 步驟 1：安裝驅動程式

1. 選取 **Install Driver**。
2. Windows 要求系統管理員權限時，核對訊息並選取 **Yes**。
3. 按 VTC 驅動程式安裝精靈完成全部步驟。
4. 返回 TOPST Imager。
5. 選取 **Driver Installation Complete**。

![D3-G VTC 驅動程式安裝說明](https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/Quick%20Guide/TOPST%20Imager%20D3-G%20Driver%20Installation.png)

1. 先選取 **Install Driver** 啟動安裝程式。
2. 完成所有步驟後再選取 **Driver Installation Complete**。

通常每部電腦只需安裝一次。

### 8.2 步驟 2：進入開機模式並偵測開發板

請觀察開發板圖片與閃爍標記。

1. **按下 BOOT 按鈕。**
2. 持續按住 BOOT。
3. **按下並放開 RESET 按鈕。**
4. 放開 BOOT。
5. 確認 USB Type-C 線與電腦及開發板連接牢固。
6. 檢查應用程式是否偵測到開發板。

![D3-G 開機模式與開發板偵測畫面](https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/Quick%20Guide/TOPST%20Imager%20D3-G%20Boot%20Mode.png)

1. 對照圖片與閃爍標記完成開機模式操作。
2. 變更連線後選取 **Check Again**。
3. 偵測成功後即可使用 **Continue Flashing**。

Windows 裝置管理員中可能顯示類似 `Telechips TCCxxxx VTC USB Driver` 的名稱。

### 8.3 步驟 3：燒錄映像檔

1. 選取 **Start Flashing**。
2. 查看下載、解壓縮與燒錄進度。
3. 等待完成畫面出現。

## 9. 燒錄 AI-G

AI-G 同時使用 USB 與乙太網路連線。

### 9.1 步驟 1：設定乙太網路

1. 用乙太網路線連接電腦與 AI-G。
2. 選取連接 AI-G 的乙太網路介面卡。
3. 按提示將電腦位址設為 `192.168.0.8/24`。
4. 確認網路設定完成。

請選取**連接 AI-G 的有線乙太網路介面卡**，而不是 Wi-Fi。

### 9.2 步驟 2：進入開機模式並選取 COM 連接埠

1. 觀察動畫並按下 BOOT。
2. 按住 BOOT 時按下並放開 RESET。
3. 放開 BOOT。
4. 選取新偵測到的 AI-G USB COM 連接埠。
5. 再次檢查電源、USB Type-C 線與乙太網路線。

若有多個 COM 連接埠，暫時拔下 AI-G USB 線。消失的連接埠就是 AI-G 的連接埠。重新連接後再次進入開機模式，再繼續操作。

### 9.3 步驟 3：燒錄映像檔

1. 選取 **Start Flashing**。
2. 等待進度達到 100%。
3. 完成畫面出現後重新啟動開發板。

## 10. 燒錄 VCP-G

### 10.1 步驟 1：進入開機模式

1. 查看畫面中的開發板圖片。
2. 按住 BOOT。
3. 按下並放開 RESET。
4. 放開 BOOT。
5. 選取 **Next**。

### 10.2 步驟 2：選取 COM 連接埠

1. 選取 VCP-G 的 USB COM 連接埠。
2. 若未列出，重新連接 USB Type-C 線。
3. 重新整理清單並選取正確連接埠。

### 10.3 步驟 3：燒錄映像檔

1. 選取 **Start Flashing**。
2. 等待進度達到 100%。
3. 完成畫面出現後重新啟動開發板。

## 11. 安裝自訂映像檔

此選項用於安裝官方目錄中沒有的本機映像檔。

1. 在作業系統選取畫面按一下 **Custom Image**。
2. 選取 **Next** 或按兩下該項目。
3. 將檔案拖曳到虛線區域，或選取 **Browse for FAI Image** / **Browse for ROM Image** 來選擇檔案。
4. 核對所選檔案名稱。
5. 選取 **Next**，按對應開發板的連線提示操作。

D3-G 和 AI-G 使用 `.fai`，VCP-G 使用 `.rom`，請選取正確格式。
檔案已在本機，因此燒錄畫面不會顯示下載與解壓縮步驟。

## 12. Windows 疑難排解

### 偵測不到開發板

1. 確認開發板已通電。
2. 確認 USB 線不是僅供充電的線材。
3. 確認連接到 FWDN USB Type-C 連接埠。
4. 重新執行進入開機模式的步驟。
5. D3-G 需確認 VTC 驅動程式已安裝。

### 沒有 COM 連接埠

1. 拔下並重新連接 USB 線。
2. 檢查開發板電源。
3. 重新進入開機模式。
4. 重新整理 COM 連接埠清單。

### AI-G 網路錯誤

1. 檢查電腦與 AI-G 之間的乙太網路線。
2. 確認選取有線介面卡而非 Wi-Fi。
3. 確認電腦位址為 `192.168.0.8/24`。
4. 按應用程式提示從步驟 1 重新開始。

### 出現 `Failed open port` 或 `GetLastError : 22`

檢查 FWDN USB Type-C 線，重新連接，再從開機模式步驟重新操作。

### 下載沒有進展

1. 檢查網際網路連線。
2. 檢查電腦剩餘空間。
3. 稍候再選取 **Retry**。

### 燒錄中想返回上一步

燒錄開始後返回會出現取消確認視窗。取消前請確認開發板處於安全狀態，並遵循畫面提示。

### 需要錯誤相關協助

1. 複製錯誤視窗中的詳細資訊。
2. 從 **App Options** 開啟記錄檔資料夾。
3. 準備錯誤訊息與記錄檔。
4. 在 [TOPST 社群](https://community.topst.ai/)提問。

Windows 上的常見記錄檔位置：

```text
%LOCALAPPDATA%\Telechips\TOPST Imager\logs\topst-imager.log
```

---

# Linux 使用說明

## 13. Linux 使用前準備

畫面與基本流程和 Windows 相同，但準備工作不同。開發板、作業系統和版本按鈕的位置與上方 Windows 畫面相同。Linux 會跳過 D3-G 的 Windows 驅動程式安裝畫面，直接進入開機模式與開發板偵測。

- 不要安裝 Windows VTC 驅動程式。
- D3-G 需要 Linux USB 權限。
- AI-G 和 VCP-G 需要序列埠權限。
- 發行套件必須包含 Linux FWDN 執行檔。
- 解壓縮官方映像檔需要 `unzip` 或 `bsdtar`。

不熟悉指令操作時，請系統管理員或開發人員完成下方的 **Linux 系統管理員設定**。一次性設定後，一般使用者即可按畫面提示操作。

## 14. 在 Linux 上安裝與執行

以下範例使用 Ubuntu。

### 14.1 解壓縮套件

1. 從官方網站下載適合電腦的 Linux 套件。
2. 開啟下載資料夾。
3. 開啟終端機並執行：

```bash
cd ~/Downloads
tar -xzf TOPST-Imager-<version>-Linux-<architecture>.tar.gz
```

將 `<version>` 和 `<architecture>` 替換成實際檔案名稱中的值。輸入檔名前幾個字元後，可按 `Tab` 自動完成。

### 14.2 執行應用程式

進入解壓縮後的資料夾並執行：

```bash
cd TOPST-Imager-<version>-Linux-<architecture>
chmod +x topst-imager
./topst-imager
```

若提示缺少 `Qt` 程式庫，表示目前套件不含 Qt 執行階段。一般使用者應向發行方索取**包含 Qt 6.12 執行階段的 Linux 套件**，不要嘗試手動安裝。

## 15. Linux 系統管理員設定

通常只需執行一次。

### 15.1 安裝解壓縮工具

```bash
sudo apt update
sudo apt install unzip
```

### 15.2 AI-G 和 VCP-G 序列埠權限

```bash
sudo usermod -aG dialout "$USER"
```

執行後登出並重新登入，或重新啟動電腦。

### 15.3 D3-G USB 權限

1. 將 D3-G 以開機模式連接。
2. 在終端機查找 USB ID：

```bash
lsusb
```

3. 使用偵測到的廠商 ID 和產品 ID 建立 `/etc/udev/rules.d/99-topst.rules`。

```text
SUBSYSTEM=="usb", ATTR{idVendor}=="VENDOR_ID", ATTR{idProduct}=="PRODUCT_ID", MODE="0666"
```

4. 重新載入規則：

```bash
sudo udevadm control --reload-rules
sudo udevadm trigger
```

不要任意填寫 `VENDOR_ID` 和 `PRODUCT_ID`。若不清楚 D3-G 的正確值，請聯絡 TOPST 支援團隊。

### 15.4 檢查 Linux FWDN 檔案

發行套件的以下位置必須包含不帶副檔名的 Linux 執行檔：

```text
tools/fwdn_d3/fwdn_d3
tools/fwdn_ai/fwdn_ai
tools/fwdn_vcp/fwdn_vcp
```

若檔案存在，請授予執行權限：

```bash
chmod +x tools/fwdn_d3/fwdn_d3
chmod +x tools/fwdn_ai/fwdn_ai
chmod +x tools/fwdn_vcp/fwdn_vcp
```

缺少這些檔案時，Linux 無法燒錄。不能使用 Windows `.exe` 檔案替代。

## 16. 在 Linux 上燒錄 D3-G

Linux 不使用 Windows VTC 驅動程式安裝步驟。

1. 選取 D3-G 映像檔。
2. 觀看動畫並按下 BOOT。
3. 按住 BOOT 時按下並放開 RESET。
4. 放開 BOOT。
5. 檢查是否偵測到開發板。
6. 開始燒錄並等待完成。

若未偵測到，請檢查 USB 權限規則、Type-C 線、電源與開機模式。

## 17. 在 Linux 上燒錄 AI-G

TOPST Imager 不會在 Linux 上自動修改乙太網路位址。請在 Ubuntu 設定中手動設定。

1. 開啟 **設定 → 網路**。
2. 開啟連接 AI-G 的有線網路設定。
3. 將 IPv4 方法設為**手動**。
4. 位址輸入 `192.168.0.8`。
5. 子網路遮罩輸入 `255.255.255.0`；若使用前綴長度則輸入 `24`。
6. 如無其他指示，閘道與 DNS 留空。
7. 套用設定後關閉並重新開啟有線連線。
8. 返回 TOPST Imager，檢查乙太網路狀態。
9. 按畫面提示進入開機模式。
10. 選取 AI-G 的 `/dev/ttyUSB...` 或 `/dev/ttyACM...` 連接埠。
11. 開始燒錄。

## 18. 在 Linux 上燒錄 VCP-G

1. 按畫面提示進入開機模式。
2. 選取 `/dev/ttyUSB...` 或 `/dev/ttyACM...` 格式的連接埠。
3. 確認連接埠正確後開始燒錄。
4. 等待完成畫面。

若沒有連接埠，請確認已加入 `dialout` 群組，並已登出後重新登入。

## 19. Linux 疑難排解

### 出現 `Permission denied`

- AI-G 或 VCP-G：確認使用者屬於 `dialout` 群組。
- D3-G：確認 udev USB 權限規則已生效。
- FWDN 檔案：確認已透過 `chmod +x` 授予執行權限。

### 找不到 Linux FWDN 檔案

檢查發行資料夾的 `tools/fwdn_*` 中是否有 Linux 執行檔。Windows `.exe` 無法在 Linux 上執行。

### 沒有開發板連接埠

執行以下指令列出連接埠：

```bash
ls /dev/ttyUSB* /dev/ttyACM* 2>/dev/null
```

比較連接 USB 前後的清單。新出現的通常就是開發板連接埠。

### 未跟隨淺色或深色佈景主題

應用程式使用 Linux 桌面透過 Qt 提供的佈景主題資訊。某些環境可能不會立即套用，請嘗試重新啟動應用程式。

## 20. 燒錄完成後

1. 確認顯示成功訊息。
2. 等待 TOPST Imager 完成所有工作。
3. 安全關閉開發板電源。
4. 拔除 FWDN 線，或重新連接日常使用所需的線材。
5. 開機並確認新作業系統正常啟動。

官方映像檔會下載並解壓縮至暫存資料夾。燒錄成功後，下載檔案與解壓縮資料夾會自動刪除。

## 21. 請記住三件事

1. **確認選取了正確的開發板與映像檔。**
2. **燒錄時不要斷電或拔線。**
3. **發生錯誤時，依畫面清單從上到下逐項檢查。**

需要協助時，請準備錯誤訊息與記錄檔，在 [TOPST 社群](https://community.topst.ai/)提問。
