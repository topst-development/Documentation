# D3-G リリースノート - v1.3.0

## 更新されたリポジトリ
- [isp-server](https://github.com/topst-development/isp-server/tree/feature/d3g-ov5647)
- [isp-frontend](https://github.com/topst-development/isp-frontend/tree/feature/d3g)
- [kernel-5.10](https://github.com/topst-development/kernel-5.10/tree/release/d3/1.3.0)
- [meta-topst](https://github.com/topst-development/meta-topst/tree/release/1.3.0)
- [meta-topst-bsp](https://github.com/topst-development/meta-topst-bsp/tree/release/1.3.0)
- [manifests](https://github.com/topst-development/manifests/tree/release/1.3.0)

## 新機能
- vulkan ドライバをサポートします
- 基本的なカメラ isp チューニングツールをサポートします
- ビルド設定を通じて PIv2 カメラをサポートします
- Ubuntu デスクトップリリースで firefox-esr (extended support release) をサポートします

## 改善点
- pcie のデータ転送速度を改善しました
- 起動時の pcie ブロックデバイス検出を安定化しました

## 既知の問題
- sdcard が挿入されている場合、ウォームリブートに時間がかかることがあります (約 40 秒)。
- MIPI に接続された外部カメラは、現時点では最大 30fps までサポートします (次回リリースで最大 60fps をサポート予定です)

## ガイド
 - VLC Player
   - コンテンツを再生する前に、環境設定でビデオ出力を 'X11 video output(XCB)' に設定する必要があります。
 - Vulkan ドライバ
   - vulkan のサンプルを実行するには 'vkcube' コマンドを実行してください。
   - 独自の vulkan アプリケーションをプログラミングする方法については、[https://github.com/krh/vkcube.git](https://github.com/krh/vkcube.git) を参照してください。
