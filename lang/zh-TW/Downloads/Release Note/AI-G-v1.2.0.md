# AI-G 版本資訊 - v1.2.0

## 更新的儲存庫

- [tc-nn-app](https://github.com/topst-development/tc-nn-app)
- [libtc-ndnpu](https://github.com/topst-development/libtc-ndnpu)
- [tc-compiled-nn](https://github.com/topst-development/tc-compiled-nn)
- [meta-topst](https://github.com/topst-development/meta-topst)

## 新增功能

- 將 `tcnnapp` 的預設物件偵測模型和 `tcnputestapp` 的預設測試模型從 YOLOv5s 改為 YOLOv8s。

## 改善項目

- 改善了應用程式的記憶體清理、輸入輸出範圍檢查與初始化錯誤提示。
- 更新了 MobileNetV2 模型的二進位檔案和中繼資料。
- 將 Windows 韌體下載指令碼的 COM 連接埠查詢方式從 WMIC 改為 PowerShell。
- 將 `tc-nn-camera-app` 中的預設攝影機輸入路徑從 `/dev/video0` 變更為 `/dev/video2`。

## 使用說明

- 預設模型目錄為 `/usr/share/yolov8s_quantized/`。`tcnnapp` 的第二個預設模型目錄為 `/usr/share/mobilenetv2_10_quantized/`。
- 隨附的 YOLOv8s 模型不包含 `sample/input.ia.bin`。缺少此檔案時，`tcnputestapp` 會使用全零輸入並顯示 `Input file not found. Using zero padding.`。此測試用於檢查 NPU 的執行與效能，不用於評估模型準確度。
- 預先建置的韌體套件包含 Windows 用的 `fwdn_ai.bat` 和 Linux 用的 `fwdn_ai.sh`。

## 韌體

- [AIG-TOPST-Yocto-image-v1.2.0-r01](https://topst-downloads.s3.ap-northeast-2.amazonaws.com/Yocto/v1.2.0/aig-yp4-v1.2.0-r01.zip)
