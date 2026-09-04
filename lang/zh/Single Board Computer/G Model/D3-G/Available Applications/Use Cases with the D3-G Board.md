# 1. 简介 
---
本文档提供 D3-G 的使用示例。   
本文档包含以下信息：
- 输入设备
  - 键盘 
  - 鼠标
- 视频输出
- 摄像头连接
  - MIPI CSI
  - USB 网络摄像头
- 存储连接
  - SD 卡
  - SATA HDD
  - NVMe M.2 SSD
  - USB 存储设备
- 以太网连接
- 40 针 GPIO 排针
  - 可用的传感器和设备

<br/><br/><br/><br/>


# 2. 输入设备
---
D3-G 支持两个用于连接输入设备的 USB 端口。
其中包括一个 USB 2.0 Type-A 端口和一个 USB 3.0 Type-A 端口，可连接鼠标或键盘以直接控制 D3-G。 

**注意**：D3-G 上的 USB Type-C 端口专用于固件下载，不能用于连接输入设备。

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20D3-G/Software/input%20device.png" width="500"></p>
<p align="center"><strong>图 2.1 将输入设备连接到 D3-G 开发板 </strong></p><br/><br/><br/><br/>


# 3. 视频输出
---
D3-G 仅通过其 DisplayPort (DP) 输出支持 FHD 显示器。
它还支持采用菊花链方式的多显示器输出，最多可同时连接两台 FHD 显示器和一台 HD 显示器。

**注意**：要使用 HDMI，需要单独的有源转换适配器。
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20D3-G/Software/monitor.png" width="500"></p>
<p align="center"><strong>图 3.1 将显示器连接到 D3-G 开发板 </strong></p>

<br/><br/><br/><br/>

# 4. 摄像头连接
---
D3-G 支持摄像头功能，可灵活满足各种应用需求。
您可以根据项目需求连接 MIPI CSI 摄像头或 USB 网络摄像头。

<br/><br/><br/>

## 4.1 USB 网络摄像头
---
D3-G 支持 USB 网络摄像头，分辨率最高可达 Full HD (FHD)。
您可以按照以下步骤测试网络摄像头：


#### 步骤 1. 将 USB 摄像头连接到开发板上的 USB 端口。
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20D3-G/Software/webcam.png" width="400"></p>
<p align="center"><strong>图 4.1 将网络摄像头连接到 D3-G 开发板</strong></p><br/>

#### 步骤 2. 将输入设备（鼠标和键盘）以及显示器连接到 D3-G。
   
#### 步骤 3. 启动 D3-G。

#### 步骤 4. 检查可用的 /dev/video 设备。
```
$ ls /dev/video*
```

#### 步骤 5. 使用 OpenCV（或 vutils）验证视频输出。
```
$ touch webcam.py
$ chmod a+x webcam.py
```
```
# You can edit the script file using vim or nano editor
# This is a Python camera application using OpenCV
import cv2

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("\\@@ Camera open failed!")
    exit()

print("Press 'q' to exit the camera window.")

cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

while True:
    ret, frame = cap.read()
    if not ret:
        print("\\@@ Failed to read frame")
        break

    cv2.imshow("Camera Feed", frame)

    # pressed 'q' key, escape
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
```
```
# Run the script
$ python3 webcam.py
```

<br/><br/><br/>

## 4.2 MIPI CSI
---
CSI 是 Camera Serial Interface 的缩写，是 MIPI Alliance 定义的用于将摄像头模块连接到主处理器的标准接口。
它可实现从摄像头到处理器的高速、低功耗图像数据传输。

D3-G 具有两个 MIPI CSI 通道（ch0 和 ch1），可连接支持柔性扁平电缆 (FFC) 的摄像头模块。
目前，D3-G 仅支持 ArduCam (5 MP) 和 Raspberry Pi v1 Camera (5 MP) 模块。 

**注意**：目前，D3-G 不支持同时使用 CSI 通道 0 和 CSI 通道 1。

<br/><br/>

### 4.2.1 ArduCam
ArduCam 是一款专为嵌入式系统和 IoT 应用设计的多功能摄像头模块。它支持包括 MIPI CSI 在内的多种图像传感器和接口，适合与 D3-G 等开发板集成。
D3-G 支持的 5 MP ArduCam 模块具有良好的图像质量，常用于基本的计算机视觉任务、流媒体传输以及基于摄像头的 AI 应用。它兼容 FFC 排线，可轻松连接到 D3-G 开发板的 CSI 接口。 

ArduCam 模块的规格如下。

| 规格                     | 说明                                 |
| ------------------------ | ------------------------------------------- |
| 传感器                   | OV5647 (500 万像素)                        |
| 分辨率                    | 2592 × 1944 (Full 5 MP)                      |
| 支持的输出格式 | RAW、YUV、JPEG (取决于传感器)           |
| 接口                      | MIPI CSI-2                                  |
| 帧率               | 1080p 下最高 30fps，720p 下 60fps         |
| 镜头接口               | 定焦镜头 (标准)                 |
| 视场角 (FOV)              | 约 54° – 70°（因型号而异）                      |
| 连接类型                   | Flat Flexible Cable (FFC)                   |
| 工作电压        | 3.3V (典型值)                              |
| 外形尺寸              | 紧凑型 PCB，约 25 mm x 24 mm                   |
| 兼容性                    | Raspberry Pi 和 D3-G（通过 MIPI CSI-2 端口）      |
| 附加特性      | 低功耗、即插即用模块 |


您可以按照以下步骤测试 ArduCam：
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20D3-G/Software/arducam.png" width="400"></p>
<p align="center"><strong>图 4.2 ArduCam </strong></p><br/>

#### 步骤 1. 如图 4.3 所示，将 ArduCam 连接到 D3-G 开发板的 MIPI CSI 0。
 
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20D3-G/Software/rasp%20v1%20cam%20to%20d3g.png" width="500"></p>
<p align="center"><strong>图 4.3 将 ArduCam 连接到 D3-G 开发板</strong></p> <br/>

#### 步骤 2. 连接 ArduCam 后，可在 D3-G 开发板上使用以下 GStreamer 命令验证视频流：
```
$ gst-launch-1.0 v4l2src device=/dev/video0 io-mode=2 ! video/x-raw,format=NV12,width=1920,height=1280,framerate=30/1 ! videoconvert ! waylandsink fullscreen=true
```

此命令从通过 CSI 连接的 ArduCam 采集视频，将其转换为可显示的格式，并使用 Wayland 显示服务器以全屏模式渲染。  
运行该命令前，请确保摄像头模块已牢固连接。如果视频未显示，请检查线缆连接并确认系统已正确识别 /dev/video0。

<br/><br/>

### 4.2.2 Raspberry Pi v1 Camera
Raspberry Pi v1 Camera Module 是由 Raspberry Pi Foundation 开发的紧凑型 5 MP 摄像头。它基于 OmniVision OV5647 图像传感器，通过柔性扁平电缆 (FFC) 使用 MIPI CSI-2 接口连接到主机开发板。

该模块最初为 Raspberry Pi 系列设计，但同样兼容 D3-G，是图像采集、视频录制和计算机视觉项目等基本摄像头应用的可靠选择。

Raspberry Pi v1 Camera 模块的规格如下。

| 规格                | 说明                              |
| ------------------- | ---------------------------------------- |
| 传感器              | OmniVision OV5647                        |
| 分辨率          | 2592 × 1944 (5 MP)                        |
| 输出格式      | RAW、YUV、JPEG                           |
| 接口                 | MIPI CSI-2                               |
| 帧率          | 1080p30、720p60、VGA90                   |
| 镜头                | 定焦                              |
| 视场角 (FOV) | 最大 54°                                     |
| 线缆类型          | FFC (15 针)                             |
| 板卡尺寸    | 25 mm x 24 mm                              |
| 兼容性               | Raspberry Pi 和 D3-G（通过 MIPI CSI-2 端口） |

您可以按照以下步骤测试 Raspberry Pi v1 摄像头：

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20D3-G/Software/rasp%20v1%20cam.jpg" width="400"></p>
<p align="center"><strong>图 4.4. Raspberry Pi v1 Camera </strong></p><br/>

#### 步骤 1. 如图 4.5 所示，将 Raspberry Pi v1 摄像头连接到 D3-G 开发板的 MIPI CSI 1。
 
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20D3-G/Software/rasp%20v1%20cam%20to%20d3g.png" width="500"></p>
<p align="center"><strong>图 4.5 将 Raspberry Pi v1 Camera 连接到 D3-G 开发板</strong></p> <br/>

#### 步骤 2. 连接 Raspberry Pi 摄像头后，可以在 D3-G 上使用以下 GStreamer 命令验证视频流：
```
$ gst-launch-1.0 v4l2src device=/dev/video0 io-mode=2 ! video/x-raw,format=NV12,width=1920,height=1280,framerate=30/1 ! videoconvert ! waylandsink fullscreen=true
```

此命令从通过 CSI 连接的 Raspberry Pi 摄像头采集视频，将其转换为可显示的格式，并使用 Wayland 显示服务器以全屏模式渲染。  
运行该命令前，请确保摄像头模块已牢固连接。如果视频未显示，请检查线缆连接并确认系统已正确识别 /dev/video0。

<br/><br/><br/><br/>

# 5. 存储连接
---
本章介绍如何将 D3-G 连接到各种存储设备。支持的存储选项包括 USB 驱动器、SD 卡以及通过 PCIe 连接的外部存储。

<br/><br/><br/>

## 5.1 USB 驱动器
---
D3-G 通过其 USB 2.0 和 USB 3.0 Type-A 端口支持 USB 存储设备。
连接 USB 驱动器的方法：

### 步骤 1. 将 USB 驱动器插入 D3-G 上任一可用的 USB Type-A 端口。
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20D3-G/Software/usb%20storage%20connection%20with%20d3g.png" width="500"></p>
<p align="center"><strong>图 5.1 将 USB 存储连接到 D3-G 开发板</strong></p> <br/>

### 步骤 2. 连接后，设备通常会根据系统状态被识别为 /dev/sda1、/dev/sdb1 等。

<br/>

### 步骤 3. 可以使用以下命令手动挂载 USB 驱动器：
   ```
   $ sudo mount /dev/sda1 /mnt
   ```

<br/><br/><br/>

## 5.2 SD 卡
---
D3-G 配备了支持标准 SDHC/SDXC 卡的 microSD 卡插槽。
在 D3-G 上使用 SD 卡的方法：

<br/>

### 步骤 1. 将 microSD 卡插入 D3-G 开发板上的 SD 卡插槽。
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20D3-G/Software/sd%20card%20connect%20with%20d3g.png" width="500"></p>
<p align="center"><strong>图 5.2 将 SD 卡连接到 D3-G 开发板</strong></p> <br/>

### 步骤 2. 插入后，系统通常将 SD 卡识别为 /dev/mmcblk1p1 或类似的设备节点。
  ```
  $ ls /dev/mmcblk*
  ```
<br/>

### 步骤 3. 要手动挂载 SD 卡，请使用以下命令：
```
$ sudo mount /dev/mmcblk1p1 /mnt 
```
### 步骤 4. 挂载后，可以在 /mnt 目录下访问 SD 卡的内容。

<br/><br/><br/>

## 5.3 SATA HDD
---

D3-G 支持通过其 PCIe 插槽并使用兼容的 SATA 控制器来使用 HDD 或 SSD 等 SATA 存储设备。

<br/>

#### 步骤 1. 连接 PCIe 转 SATA 模块

要通过 PCIe 在 D3-G 上使用 SATA HDD，必须先将 PCIe 转 SATA 适配器模块连接到 D3-G 的 PCIe 插槽。

然后，将 HDD 连接到 SATA 模块，并确保 HDD 由外部 12V 电源供电。

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20D3-G/Software/sata.png" width="500"></p>
<p align="center"><strong>图 5.3 将 SATA 模块连接到 D3-G 开发板的 PCIe </strong></p><br/>

#### 步骤 2. 启动 D3-G 
启动 D3-G 后，查看启动日志以确认系统已识别该 PCIe 设备。
查找诸如 **telechips-pcie: Link up** 之类的消息，此类消息表示 PCIe 链路已成功建立。

```
Starting kernel ...

[    1.191696] telechips-pcie 11000000.pcie: invalid resource
[    1.230423] telechips-pcie 11000000.pcie: Link up
[    1.693516] debugfs: Directory '16680000.udma' with parent 'dmaengine' already present!
[    1.702282] debugfs: Directory '16681000.udma' with parent 'dmaengine' already present!
[    1.711022] debugfs: Directory '16682000.udma' with parent 'dmaengine' already present!
[    1.719799] debugfs: Directory '16683000.udma' with parent 'dmaengine' already present!
[    1.728562] debugfs: Directory '16684000.udma' with parent 'dmaengine' already present!
[    1.737308] debugfs: Directory '16685000.udma' with parent 'dmaengine' already present!
[    1.746084] debugfs: Directory '16686000.udma' with parent 'dmaengine' already present!
[    1.754824] debugfs: Directory '16687000.udma' with parent 'dmaengine' already present!
 
...
Ubuntu 22.04.5 LTS TOPST ttyAMA0

TOPST login: 
```

<br/>

#### 步骤 3. 检查 SATA HDD 识别情况
```
root@TOPST:~# lspci
00:00.0 PCI bridge: Synopsys, Inc. Device 8040 (rev 01)
01:00.0 SATA controller: ASMedia Technology Inc. Device 1064 (rev 02)
```
如果 **lspci** 命令不可用，请使用以下命令安装 pciutils。

```
$ sudo apt-get install pciutils
```

<br/>

#### 步骤 4. 挂载 SATA HDD
```
$ fdisk /dev/sda
Welcome to fdisk (util-linux 2.37.4).
Changes will remain in memory only, until you decide to write them.
Be careful before using the write command.

Command (m for help): 
```

在 fdisk 提示符下依次输入以下按键：

- o — 创建新的空 DOS 分区表 (可选，将清除现有分区表)

- n — 添加新分区

- p — 选择主分区

- 1 — 将分区编号设置为 1

- 按 Enter 键 — 接受默认的起始扇区

- 按 Enter 键 — 接受默认的结束扇区 (使用整个磁盘)

- w — 写入分区表并退出

```
$ mkfs.ext4 /dev/sda1

$ mkdir -p /mnt/sata

$ mount /dev/sda1 /mnt/sata
```

<br/>

#### 步骤 5. 执行结果
此输出确认 SATA SSD 分区 (/dev/sdb1) 已成功格式化为 ext4 文件系统并挂载到 /mnt/sata。
**df -h** 命令表明该设备现已被识别，可供系统使用。

```
$ df -h

Filesystem      Size  Used Avail Use% Mounted on
/dev/mmcblk0p4   29G  4.0G   25G  14% /
tmpfs           100M     0  100M   0% /dev/shm
tmpfs           592M  976K  591M   1% /run
tmpfs           5.0M  4.0K  5.0M   1% /run/lock
tmpfs           1.5G  4.0K  1.5G   1% /tmp
tmpfs           1.5G     0  1.5G   0% /var/volatile
tmpfs           296M  4.0K  296M   1% /run/user/0
/dev/sdb1       234G   28K  222G   1% /mnt/sata
```

<br/><br/><br/>

## 5.4 NVMe M.2 SSD
---
D3-G 支持通过其 PCIe 插槽直接连接 NVMe M.2 SSD。
<br/>

#### 步骤 1. 连接 SSD
- NVMe SSD (M.2 PCIe)：将 NVMe M.2 SSD 插入 D3-G 的 PCIe 插槽。 

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20D3-G/Software/M.2%20SSD%20connection.png" width="600"></p>
<p align="center"><strong>图 5.4 将 NVMe M.2 SSD 连接到 D3-G 开发板</strong></p><br/>

#### 步骤 2. 启动 D3-G
执行 **reboot** 命令后，查看启动日志，确认系统已识别到该 PCIe 设备。
查找诸如 **telechips-pcie: Link up** 之类的消息，此类消息表示 PCIe 链路已成功建立。

```
$ reboot
...
Starting kernel ...

[    1.191696] telechips-pcie 11000000.pcie: invalid resource
[    1.230423] telechips-pcie 11000000.pcie: Link up
[    1.693516] debugfs: Directory '16680000.udma' with parent 'dmaengine' already present!
[    1.702282] debugfs: Directory '16681000.udma' with parent 'dmaengine' already present!
[    1.711022] debugfs: Directory '16682000.udma' with parent 'dmaengine' already present!
[    1.719799] debugfs: Directory '16683000.udma' with parent 'dmaengine' already present!
[    1.728562] debugfs: Directory '16684000.udma' with parent 'dmaengine' already present!
[    1.737308] debugfs: Directory '16685000.udma' with parent 'dmaengine' already present!
[    1.746084] debugfs: Directory '16686000.udma' with parent 'dmaengine' already present!
[    1.754824] debugfs: Directory '16687000.udma' with parent 'dmaengine' already present!
 
...
Ubuntu 22.04.5 LTS TOPST ttyAMA0

TOPST login: 
```

<br/>

#### 步骤 3. 检查 SSD 识别情况
```
root@TOPST:~# lspci
00:00.0 PCI bridge: Synopsys, Inc. Device 8040 (rev 01)
01:00.0 Non-Volatile memory controller: Solid State Storage Technology Corporation Device 1007 (rev 03)
```
如果 **lspci** 命令不可用，请使用以下命令安装 pciutils。

```
$ sudo apt-get install pciutils
```

<br/>

#### 步骤 4. 挂载 SSD
```
$ fdisk /dev/nvme0n1
Welcome to fdisk (util-linux 2.37.4).
Changes will remain in memory only, until you decide to write them.
Be careful before using the write command.

Command (m for help): 
```

在 fdisk 提示符下依次输入以下按键：

- o — 创建新的空 DOS 分区表 (可选，将清除现有分区表)

- n — 添加新分区

- p — 选择主分区

- 1 — 将分区编号设置为 1

- 按 Enter 键 — 接受默认的起始扇区

- 按 Enter 键 — 接受默认的结束扇区 (使用整个磁盘)

- w — 写入分区表并退出

```
$ mkfs.ext4 /dev/nvme0n1p1

$ mkdir -p /mnt/nvme

$ mount /dev/nvme0n1p1 /mnt/nvme
```

<br/>

#### 步骤 5. 执行结果
该输出确认 NVMe SSD 设备 (/dev/nvme0n1p1) 已被系统成功检测并挂载到 /mnt/nvme。
```
$ df -h

Filesystem      Size  Used Avail Use% Mounted on
/dev/mmcblk0p4   29G  4.0G   25G  14% /
tmpfs           100M     0  100M   0% /dev/shm
tmpfs           592M  976K  591M   1% /run
tmpfs           5.0M  4.0K  5.0M   1% /run/lock
tmpfs           1.5G  4.0K  1.5G   1% /tmp
tmpfs           1.5G     0  1.5G   0% /var/volatile
tmpfs           296M  4.0K  296M   1% /run/user/0
/dev/nvme0n1p1  234G   28K  222G   1% /mnt/nvme
```
<br/><br/><br/><br/>


# 6. 以太网连接
---
D3-G 通过板载 J2C 以太网端口支持以太网连接。这使 D3-G 能够使用标准 TCP/IP 协议与局域网或互联网进行通信。以太网通常用于部署需要远程访问、数据流传输或软件更新的应用程序。

<br/><br/><br/>

## 6.1 通过路由器连接网络
---
此方法使用标准路由器将 D3-G 连接到局域网。D3-G 可以通过 DHCP 自动获取 IP 地址，也可以配置为静态 IP 地址。

<br/><br/>

### 6.1.1 创建网络配置文件

1. 通过 DHCP 获取动态 IP
如果您的网络提供 DHCP 服务器（例如路由器或启用了 ICS 的 Windows PC），则无需编辑文件。连接以太网线后，系统会立即自动获取 IP 地址。

只需插入网线即可立即开始使用网络。请转至第 6.1.3 章“验证网络连接”。

2. 静态 IP 配置
如果希望分配静态 IP 地址（例如直接与 PC 连接或没有可用的 DHCP 服务器时），请使用以下内容编辑同一文件：
```
$ vi /etc/systemd/network/20-wired.network

[Match]
Name=eth0

[Network]
Address=192.168.137.2/24
Gateway=192.168.137.1
DNS=8.8.8.8
```

此设置将 IP 地址设为 192.168.137.2，使用 192.168.137.1 作为网关（在 Windows ICS 中较为常见），并配置 Google DNS。

<br/><br/>

### 6.1.2 重启网络服务
重启 systemd-networkd 服务以应用新的网络配置：

```
sudo systemctl restart systemd-networkd
```

<br/><br/>

### 6.1.3 验证网络连接
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20D3-G/Software/router%20connection.png"width="500"></p>
<p align="center"><strong>图 6.1 通过路由器连接网络</strong></p>

通过 ping Google 的公共 DNS 服务器来测试互联网连接：

```
$ ping 8.8.8.8
PING 8.8.8.8 (8.8.8.8): 56 data bytes
64 bytes from 8.8.8.8: seq=0 ttl=113 time=30.208 ms
64 bytes from 8.8.8.8: seq=1 ttl=113 time=38.143 ms
64 bytes from 8.8.8.8: seq=2 ttl=113 time=30.969 ms
64 bytes from 8.8.8.8: seq=3 ttl=113 time=33.586 ms
 
```

<br/><br/><br/>

## 6.2 与主机 PC 共享网络
---
利用 Windows 操作系统提供的 Internet 连接共享 (ICS) 功能，无需使用路由器即可将 PC 的互联网连接共享给 D3-G。

<br/><br/>

### 6.2.1 主机 PC 网络配置
- 控制面板 → 网络和 Internet → 网络连接 → 设置以太网
 
1. 找到已连接到互联网的网络适配器（例如 Wi-Fi），右键单击并选择 **属性**。

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20AI-G/Available%20Applications/ethernet1.png" width="600"></p>
<p align="center"><strong>图 6.2 选择属性</strong></p><br/>
 
2. 选择共享选项卡。

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20AI-G/Available%20Applications/ethernet2.png" width="400"></p>
<p align="center"><strong>图 6.3 选择共享选项卡</strong></p><br/>

3. 勾选“允许其他网络用户通过此计算机的 Internet 连接来连接”复选框。
 
4. 在家庭网络连接下拉菜单中，选择 D3-G 将要连接的以太网适配器（例如 "Ethernet"）。

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20AI-G/Available%20Applications/ethernet3.png" width="400"></p>
<p align="center"><strong>图 6.4 选择以太网适配器</strong></p><br/>
 
5. 单击 **确定** 保存设置。

<br/><br/>

### 6.2.2 创建网络配置文件 
1. 通过 DHCP 获取动态 IP
如果您的网络提供 DHCP 服务器（例如路由器或启用了 ICS 的 Windows PC），则无需编辑文件。连接以太网线后，系统会立即自动获取 IP 地址。

只需插入网线即可立即开始使用网络。请转至第 6.2.4 章“验证网络连接”。

2. 静态 IP 配置
如果希望分配静态 IP 地址（例如直接与 PC 连接或没有可用的 DHCP 服务器时），请使用以下内容编辑同一文件：
```
$ vi /etc/systemd/network/20-wired.network

[Match]
Name=eth0

[Network]
Address=192.168.137.2/24
Gateway=192.168.137.1
DNS=8.8.8.8
```
此设置将 IP 地址设为 192.168.137.2，使用 192.168.137.1 作为网关（在 Windows ICS 中较为常见），并配置 Google DNS。

<br/><br/>

### 6.2.3 重启网络服务
重启 systemd-networkd 服务以应用新的网络配置：

```
sudo systemctl restart systemd-networkd
```

<br/><br/>

### 6.2.4 验证网络连接
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20D3-G/Software/host%20pc%20ethernet%20connection.png"width="500"></p>
<p align="center"><strong>图 6.5 与主机 PC 共享网络</strong></p>
<br/>

通过 ping Google 的公共 DNS 服务器来测试互联网连接：

```
$ ping 8.8.8.8
PING 8.8.8.8 (8.8.8.8): 56 data bytes
64 bytes from 8.8.8.8: seq=0 ttl=113 time=30.208 ms
64 bytes from 8.8.8.8: seq=1 ttl=113 time=38.143 ms
64 bytes from 8.8.8.8: seq=2 ttl=113 time=30.969 ms
64 bytes from 8.8.8.8: seq=3 ttl=113 time=33.586 ms
```

<br/><br/><br/><br/>

# 7. 40 针 GPIO 排针
---
D3-G 配备 40 针 GPIO 排针，可为各种硬件项目提供灵活的 I/O 功能。
该排针兼容通用输入/输出 (GPIO) 操作，可用于连接传感器、LED、按钮及其他外围设备。

每个引脚可根据配置支持多种功能，例如数字 I/O、PWM、I2C、SPI 和 UART。

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/d3g/Assets/TOPST%20D3-G/Software/d3-g%20gpio%2040pinmap.png" width="800"></p>
<p align="center"><strong>图 7.1 D3-G 的 40 针 GPIO 排针引脚图 </strong></p> <br/>

**注意**：连接外部硬件之前，请参阅官方引脚图以了解详细的引脚功能和电压电平。

<br/><br/><br/>

## 7.1 GPIO 数字输入/输出
---
D3-G 通过其 40 针排针支持数字输入和输出 (GPIO)，使您能够与按钮、LED 和传感器等外部设备进行交互。 

### 7.1.1 LED
---
最简单也最常见的 GPIO 输出示例之一是控制 LED。  
本节演示如何使用 D3-G 连接并使用 LED 传感器。

#### 步骤 1. 硬件要求
- D3-G 开发板 (x1)
- 面包板 (x1)
- LED (x1)
- 公对母跳线 (x2)
- DC 5V 电源适配器 (x1)
- USB 转 TTL 串口线 (x1)

#### 步骤 2. 示例电路
- LED
    - (+) 引脚连接到 D3-G 开发板上的 12 号引脚。
    - (-) 引脚连接到 D3-G 开发板上用作 GND 的 14 号引脚。  
    
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20D3-G/Software/led.png"></p>

<p align="center"><strong>图 7.2 D3-G GPIO LED 电路原理图 </strong></p> <br/>

##### 步骤 2.1 引脚映射
下表显示了引脚映射。

<div align="center">
  <p><strong>表 7.1 D3-G LED 的引脚映射</strong></p>
  <table>
      <tr>
          <th colspan="3">引脚名称</th>
          <th>D3-G</th>
          <th>GPIO</th>
      </tr>
      <tr>
          <td colspan="3">LED (+) 引脚</td>
          <td>12</td>
          <td>89</td>
      </tr>
      <tr>
          <td colspan="3">LED (-) 引脚</td>
          <td>14</td>
          <td>GND</td>
      </tr>
  </table>
</div>

#### 步骤 3. 执行方法
要驱动连接到 D3-G 开发板 GPIO89 的 LED，请运行以下代码：

```
import time
import os
  
def export_gpio(pin, direction: str):
    # If the pin is already active, unexport it.
    if os.path.exists(f"/sys/class/gpio/gpio{pin}"):
        with open("/sys/class/gpio/unexport", "w") as f:
            f.write(str(pin))
  
    # Export the pin to activate it.
    with open("/sys/class/gpio/export", "w") as f:
        f.write(str(pin))
  
    # Set the pin direction.
    with open(f"/sys/class/gpio/gpio{pin}/direction", "w") as f:
        f.write(direction)

def read_gpio_value(pin: int):
    gpio_value_path = f"/sys/class/gpio/gpio{pin}/value"
    with open(gpio_value_path, "r") as f:
        return f.read().strip()

def write_gpio_value(pin: int, value: int):
    gpio_value_path = f"/sys/class/gpio/gpio{pin}/value"
    with open(gpio_value_path, "w") as f:
        f.write(str(value))

def unexport_gpio(pin: int):
    with open("/sys/class/gpio/unexport", "w") as f:
        f.write(str(pin))

  
def main():
    print("""\
                        +--------+
                    3P3-|-1    2-|-5P0
       I2C_SDA / GPIO82-|-3    4-|-5P0
       I2C_SCL / GPIO81-|-5    6-|-GND
                 GPIO83-|-7    8-|-GPIO87 / UT_TXD
                    GND-|-9   10-|-GPIO88 / UT_RXD
                 GPIO84-|-11  12-|-GPIO89 / PWM 0
                 GPIO85-|-13  14-|-GND
                 GPIO86-|-15  16-|-GPIO90
                    3P3-|-17  18-|-GPIO65
     SPIO_MOSI / GPIO63-|-19  20-|-GND
     SPIO_MISO / GPIO64-|-21  22-|-GPIO66
     SPIO_SCLK / GPIO61-|-23  24-|-GPIO62 / SPIO_CS0
                    GND-|-25  26-|-GPIO67 / SPIO_CS1
              RESERVED0-|-27  28-|-RESERVED1
                GPIO112-|-29  30-|-GND
                GPIO113-|-31  32-|-GPIO115 / PWM 2
         PWM1 / GPIO114-|-33  34-|-GND
    SPI1_MISO / GPIO121-|-35  36-|-GPIO119 / SPI1_CS0
                GPIO117-|-37  38-|-GPIO120 / SPI1_MOSI
                    GND-|-39  40-|-GPIO118 / SPI1_SCLK
                        +--------+""")
  
    LED_PIN = 89  # LED connected to GPIO 89
  
    try:
        # Setup the GPIO pins
        export_gpio(LED_PIN, direction="out")
        print("GPIO pins initialized.")
        
        count = 0
        while (count < 10):
            write_gpio_value(LED_PIN, 1)  # Turn on the LED
            print("LED ON.")
            count += 1
            time.sleep(1.0)  # Polling delay
            write_gpio_value(LED_PIN, 0)  # Turn off the LED
            print("LED OFF.")
            time.sleep(1.0)  # Polling delay
 
        write_gpio_value(LED_PIN, 0)  # Turn off the LED
 
    except KeyboardInterrupt:
        print("Program interrupted by user.")
  
    finally:
        unexport_gpio(LED_PIN) # unexport LED pin
        print("GPIO pins unexported.")
        print("Program terminated.")

if __name__ == "__main__":
    main()
```

#### 步骤 4. 执行结果
使用以下命令运行代码。

```
$ python3 led_test.py
```

此脚本将 GPIO89 配置为数字输出，并每隔 1 秒切换一次其状态。
执行后，连接到 GPIO89 的 LED 会闪烁 10 次，亮 1 秒后灭 1 秒，如此反复。完成 10 个周期后，脚本退出并自动取消导出该 GPIO。

要提前停止脚本，请按 **[Ctrl+C]**。
无论哪种情况，引脚都会被正确释放和清理。

**注意**：此设置假定 LED 为直接连接。为了安全和长期运行，强烈建议在 LED 上串联一个限流电阻（例如 220Ω），以防止电流过大并保护 GPIO 引脚免受潜在损坏。

<br/><br/><br/><br/>

### 7.1.2 按钮
---
轻触按钮是一种基本输入设备，常用于演示通过 GPIO 进行的数字输入处理。
本节演示如何在 D3-G 上连接并使用基本的按钮模块。

#### 步骤 1. 硬件要求
- D3-G 开发板 (x1)
- 面包板 (x1)
- 按钮 (x1)
- 公对母跳线 (x2)
- DC 5V 电源适配器 (x1)
- USB 转 TTL 串口线 (x1)

#### 步骤 2. 示例电路
- 按钮开关
    - 按钮开关的一个引脚连接到 D3-G 开发板上的 10 号引脚。
    - 按钮上方的另一侧引脚连接到 3.3V 引脚。

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20D3-G/Software/button_circuit.png"></p> 
<p align="center"><strong>图 7.3 D3-G GPIO 按钮电路原理图</strong></p>

##### 步骤 2.1 引脚映射
下表显示了引脚映射。

<div align="center">
  <p><strong>表 7.2 D3-G 按钮的引脚映射</strong></p>
  <table>
      <tr>
          <th colspan="3">引脚名称</th>
          <th>D3-G</th>
          <th>GPIO</th>
      </tr>
      <tr>
          <td colspan="3">按钮的一侧引脚</td>
          <td>10</td>
          <td>88</td>
      </tr>
  </table>
</div>

#### 步骤 3. 执行方法
要监测连接到 D3-G 开发板 GPIO88 的按钮输入，请运行以下代码：

```
import os
import time
BUTTON_PIN = 88  # button sensor GPIO pin
 
def export_gpio(pin: int, direction: str):
    # If the pin is already active, unexport it.
    if os.path.exists(f"/sys/class/gpio/gpio{pin}"):
        with open("/sys/class/gpio/unexport", "w") as f:
            f.write(str(pin))
  
    # Export the pin to activate it.
    with open("/sys/class/gpio/export", "w") as f:
        f.write(str(pin))
  
    # Set the pin direction.
    with open(f"/sys/class/gpio/gpio{pin}/direction", "w") as f:
        f.write(direction)

def read_gpio_value(pin: int):
    gpio_value_path = f"/sys/class/gpio/gpio{pin}/value"
    with open(gpio_value_path, "r") as f:
        return f.read().strip()

def write_gpio_value(pin: int, value: int):
    gpio_value_path = f"/sys/class/gpio/gpio{pin}/value"
    with open(gpio_value_path, "w") as f:
        f.write(str(value))

def unexport_gpio(pin: int):
    with open("/sys/class/gpio/unexport", "w") as f:
        f.write(str(pin))
def main():
    # initialize GPIO pins
    export_gpio(BUTTON_PIN, "in")  
    print("gpio pins initialized.")
 
    try:
        while True:
            sensor_value = read_gpio_value(BUTTON_PIN)
 
            if sensor_value == "0":  
                print("button pressed.")
            else:    
                print("button released.")
 
            time.sleep(0.5)  # 500ms delay

    except KeyboardInterrupt:
        print("Program interrupted by user.")
 
    finally:
        unexport_gpio(BUTTON_PIN)  # unexport the GPIO pin
        print("GPIO pins unexported.")
        print("Program terminated.")
         
if __name__ == "__main__":
    main()
```

#### 步骤 4. 执行结果
使用以下命令运行代码。
```
$ python3 test_button.py
```
此脚本将 GPIO88 配置为数字输入，并实时持续监测其值。
执行后，按下连接到 GPIO88 的按钮时，会打印一条表示按钮已被按下的消息。

要停止脚本，请按 **[Ctrl+C]**。
脚本终止后，GPIO88 将被自动取消导出并清理。

**注意**：此处以 GPIO88 为例。您可以根据 40 针排针的引脚分布，使用 D3-G 上任何可用的 GPIO 引脚。
请参阅官方引脚分布图，并选择与您的硬件配置相匹配的 GPIO 编号。

<br/><br/><br/><br/>

### 7.1.3 触摸传感器
---
触摸传感器可用于通过 GPIO 将人体触摸检测为数字输入信号。
本节演示如何使用 D3-G 连接基本的触摸传感器模块并读取其输入。

#### 步骤 1. 硬件要求
- D3-G 开发板 (x1)
- 触摸传感器 (x1)
- 母对母跳线 (x3)
- DC 5V 电源适配器 (x1)
- USB 转 TTL 串口线 (x1)

#### 步骤 2. 示例电路
- 触摸传感器
    - 触摸传感器的 SIG 引脚连接到 D3-G 开发板上的 88 号引脚。
    - 触摸传感器的 VCC 引脚连接到 D3-G 开发板上的 3.3V。
    - 触摸传感器的 GND 引脚连接到 D3-G 开发板上的 GND。


<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20D3-G/Software/touch%20circuit.png"></p>
<p align="center"><strong>图 7.4 D3-G GPIO 触摸传感器电路原理图</strong></p>

##### 步骤 2.1 引脚映射
下表显示了引脚映射。

<div align="center">
  <p><strong>表 7.3 D3-G 触摸传感器的引脚映射</strong></p>
  <table>
      <tr>
          <th colspan="3">引脚名称</th>
          <th>D3-G</th>
          <th>GPIO</th>
      </tr>
      <tr>
          <td colspan="3">SIG</td>
          <td>10</td>
          <td>88</td>
      </tr>
      <tr>
          <td colspan="3">VCC</td>
          <td>1</td>
          <td>3.3</td>
      </tr>
      <tr>
          <td colspan="3">GND</td>
          <td>20</td>
          <td>GND</td>
      </tr>
  </table>
</div>

#### 步骤 3. 执行方法
要监测连接到 D3-G 开发板 GPIO88 的触摸传感器，只需运行以下代码：
```
import os
import time
 
# GPIO pin numbers setting
TOUCH_SENSOR_PIN = 88  # sensor GPIO pin
 
def export_gpio(pin: int, direction: str):
    # If the pin is already active, unexport it.
    if os.path.exists(f"/sys/class/gpio/gpio{pin}"):
        with open("/sys/class/gpio/unexport", "w") as f:
            f.write(str(pin))
  
    # Export the pin to activate it.
    with open("/sys/class/gpio/export", "w") as f:
        f.write(str(pin))
  
    # Set the pin direction.
    with open(f"/sys/class/gpio/gpio{pin}/direction", "w") as f:
        f.write(direction)

def read_gpio_value(pin: int):
    gpio_value_path = f"/sys/class/gpio/gpio{pin}/value"
    with open(gpio_value_path, "r") as f:
        return f.read().strip()

def write_gpio_value(pin: int, value: int):
    gpio_value_path = f"/sys/class/gpio/gpio{pin}/value"
    with open(gpio_value_path, "w") as f:
        f.write(str(value))

def unexport_gpio(pin: int):
    with open("/sys/class/gpio/unexport", "w") as f:
        f.write(str(pin))
def main():
    # initialize GPIO pins
    export_gpio(TOUCH_SENSOR_PIN, "in")  # touch sensor pin direction "in"
    print("gpio pins initialized.")
 
    try:
        while True:
            # button sensor value read
            # If the sensor value is 0, it means an touch detected.
            # If the sensor value is 1, it means no touch released.
            sensor_value = read_gpio_value(TOUCH_SENSOR_PIN)
 
            if sensor_value == "1":  
                print("touch detected.")
            else:    
                print("touch released.")
 
            time.sleep(0.5)  # 500ms delay

    except KeyboardInterrupt:
        print("program interrupted by user.")
 
    finally:
        unexport_gpio(TOUCH_SENSOR_PIN)  # unexport the GPIO pin
        print("GPIO pins unexported.")
        print("program terminated.")
         
if __name__ == "__main__":
    main()
```

#### 步骤 4. 执行结果
使用以下命令运行代码。

```
$ python3 touch_test.py
```

此脚本将 GPIO88 配置为数字输入，并实时持续监测其值。

执行后，触摸传感器会使终端打印如下消息：
```
touch detected.
```
未触摸传感器时，输出为：
```
touch released.
```
要停止脚本，请按 **[Ctrl+C]**。
脚本终止后，GPIO88 将被自动取消导出并清理。

**注意**：此处以 GPIO88 为例。您可以根据 40 针排针的引脚分布，使用 D3-G 上任何可用的 GPIO 引脚。
请参阅官方引脚分布图，并选择与您的硬件配置相匹配的 GPIO 编号。

<br/><br/><br/><br/>

### 7.1.4 振动检测传感器
---
振动传感器可用于检测物理冲击或振动，并通过 GPIO 输出数字输入信号。
本节介绍如何使用 D3-G 连接基本振动传感器模块并检测其输入。

#### 步骤 1. 硬件要求
- D3-G 开发板 (x1)
- 振动检测传感器 (x1)
- 母对母跳线 (x4)
- DC 5V 电源适配器 (x1)
- USB 转 TTL 串口线 (x1)

#### 步骤 2. 示例电路
- 振动检测传感器
    - 振动检测传感器的 VCC 引脚连接到 D3-G 开发板的 3.3V 引脚。
    - 振动检测传感器的 GND 引脚连接到 D3-G 开发板的 GND。
    - 振动检测传感器的 DO 引脚连接到 D3-G 开发板的 88 号引脚。

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20D3-G/Software/vibr%20circuit.png"></p>
<p align="center"><strong>图 7.5 D3-G GPIO 振动检测传感器电路原理图</strong></p>

##### 步骤 2.1 引脚映射
下表显示了引脚映射。

<div align="center">
  <p><strong>表 7.4 D3-G 振动检测传感器的引脚映射</strong></p>
  <table>
      <tr>
          <th colspan="3">引脚名称</th>
          <th>D3-G</th>
          <th>GPIO</th>
      </tr>
      <tr>
          <td colspan="3">VCC</td>
          <td>1</td>
          <td>3.3V</td>
      </tr>
      <tr>
          <td colspan="3">GND</td>
          <td>20</td>
          <td>GND</td>
      </tr>
      <tr>
          <td colspan="3">DO</td>
          <td>10</td>
          <td>88</td>
      </tr>
  </table>
</div>

#### 步骤 3. 执行方法
要监控连接到 D3-G 开发板 GPIO88 的振动传感器，请运行以下代码：
```
import os
import time
VIBRATION_SENSOR_PIN = 88  # VIBRATION_SENSOR sensor GPIO pin
 
def export_gpio(pin: int, direction: str):
    # If the pin is already active, unexport it.
    if os.path.exists(f"/sys/class/gpio/gpio{pin}"):
        with open("/sys/class/gpio/unexport", "w") as f:
            f.write(str(pin))
  
    # Export the pin to activate it.
    with open("/sys/class/gpio/export", "w") as f:
        f.write(str(pin))
  
    # Set the pin direction.
    with open(f"/sys/class/gpio/gpio{pin}/direction", "w") as f:
        f.write(direction)

def read_gpio_value(pin: int):
    gpio_value_path = f"/sys/class/gpio/gpio{pin}/value"
    with open(gpio_value_path, "r") as f:
        return f.read().strip()

def write_gpio_value(pin: int, value: int):
    gpio_value_path = f"/sys/class/gpio/gpio{pin}/value"
    with open(gpio_value_path, "w") as f:
        f.write(str(value))

def unexport_gpio(pin: int):
    with open("/sys/class/gpio/unexport", "w") as f:
        f.write(str(pin))
def main():
    # initialize GPIO pins
    export_gpio(VIBRATION_SENSOR_PIN, "in")  # vibration sensor pin direction "in"
    print("gpio pins initialized.")
 
    try:
        while True:
            sensor_value = read_gpio_value(VIBRATION_SENSOR_PIN)
 
            if sensor_value == "0":  # vibration detected
                print("vibration detected.")
            else:    # no vibration detected
                print("no vibration detected.")
 
            time.sleep(0.5)  # 500ms delay

    except KeyboardInterrupt:
        print("Program interrupted by user.")
 
    finally:
        unexport_gpio(VIBRATION_SENSOR_PIN)  # unexport the GPIO pin
        print("GPIO pins unexported.")
        print("Program terminated.")
         
if __name__ == "__main__":
    main()
```

#### 步骤 4. 执行结果
使用以下命令运行代码。

```
$ python3 vibration_test.py
```

此脚本将 GPIO88 配置为数字输入，并实时持续监测其值。
执行后，传感器检测到的振动或冲击会使终端打印如下消息：
```
vibration detected.
```
没有振动时，输出如下：
```
no vibration detected.
```
要停止脚本，请按 **[Ctrl+C]**。
终止时，GPIO88 会自动取消导出并被清理。

**注意**：此处以 GPIO88 为例。您可以根据传感器接线和排针布局使用其他任何可用的 GPIO 引脚。选择 GPIO 编号前请参考 D3-G 引脚图。

<br/><br/><br/><br/>

### 7.1.5 红外传感器 (SZH-SSBH-002)
---
红外传感器可通过感应反射的红外光来检测附近的障碍物，并通过 GPIO 输出数字信号。
本节介绍如何使用 D3-G 连接 SZH-SSBH-002 红外传感器并读取其输入。

#### 步骤 1. 硬件要求
- D3-G 开发板 (x1)
- 面包板 (x1)
- 红外传感器 (x1)
- 公对母跳线 (x5)
- DC 5V 电源适配器 (x1)
- USB 转 TTL 串口线 (x1)

#### 步骤 2. 示例电路
- 红外传感器
    - 红外传感器的 VCC 引脚连接到 D3-G 开发板的 3.3V 引脚。
    - 红外传感器的 GND 引脚连接到 D3-G 开发板的 GND。
    - 红外传感器的 OUT 引脚连接到 D3-G 开发板的 89 号引脚。


<p align="center">
  <img src="https://raw.githubusercontent.com/topst-development/Documentation/d3g/Assets/TOPST%20D3-G/Software/szh-ssbh-002_circuit.png">
</p> 
<p align="center"><strong>图 7.6 IR 传感器实验电路</strong></p>

##### 步骤 2.1 引脚映射
下表显示了引脚映射。

<div align="center">
  <p><strong>表 7.5 D3-G IR 传感器的引脚映射</strong></p>
  <table>
      <tr>
          <th colspan="3">引脚名称</th>
          <th>D3-G</th>
          <th>GPIO</th>
      </tr>
      <tr>
          <td colspan="3">VCC</td>
          <td>1</td>
          <td>3.3V</td>
      </tr>
      <tr>
          <td colspan="3">GND</td>
          <td>6</td>
          <td>GND</td>
      </tr>
      <tr>
          <td colspan="3">OUT</td>
          <td>12</td>
          <td>89</td>
      </tr>
  </table>
</div>

#### 步骤 3. 执行方法
要监控连接到 D3-G 开发板 GPIO89 的 IR 传感器，请运行以下代码：

```
import os
import time
 
# GPIO pin numbers setting
IR_SENSOR_PIN = 89  # IR sensor GPIO pin
 
def export_gpio(pin: int, direction: str):
    # If the pin is already active, unexport it.
    if os.path.exists(f"/sys/class/gpio/gpio{pin}"):
        with open("/sys/class/gpio/unexport", "w") as f:
            f.write(str(pin))
  
    # Export the pin to activate it.
    with open("/sys/class/gpio/export", "w") as f:
        f.write(str(pin))
  
    # Set the pin direction.
    with open(f"/sys/class/gpio/gpio{pin}/direction", "w") as f:
        f.write(direction)

def read_gpio_value(pin: int):
    gpio_value_path = f"/sys/class/gpio/gpio{pin}/value"
    with open(gpio_value_path, "r") as f:
        return f.read().strip()

def write_gpio_value(pin: int, value: int):
    gpio_value_path = f"/sys/class/gpio/gpio{pin}/value"
    with open(gpio_value_path, "w") as f:
        f.write(str(value))

def unexport_gpio(pin: int):
    with open("/sys/class/gpio/unexport", "w") as f:
        f.write(str(pin))
def main():
    # initialize GPIO pins
    export_gpio(IR_SENSOR_PIN, "in")  # IR sensor pin direction "in"
    print("gpio pins initialized.")
 
    try:
        while True:
            sensor_value = read_gpio_value(IR_SENSOR_PIN)
 
            if sensor_value == "0":  # obstacle detected
                print("obstacle detected.")
            else: 
                print("No obstacle detected.")
 
            time.sleep(0.5)  # 500ms delay

    except KeyboardInterrupt:
        print("program interrupted by user.")
 
    finally:
        unexport_gpio(IR_SENSOR_PIN)  # unexport the GPIO pin
        print("GPIO pins unexported.")
        print("program terminated.")
         
if __name__ == "__main__":
    main()
```

#### 步骤 4. 执行结果
使用以下命令运行代码。
```
$ python3 ir_test.py
```
该脚本将 GPIO89 配置为数字输入，并持续监控其状态以检测障碍物。
当在 IR 传感器前检测到物体时，终端显示：
```
obstacle detected.
```
未检测到物体时，显示：
```
no obstacle detected.
```
要停止脚本，请按 **[Ctrl+C]**。
脚本终止时，GPIO89 会自动取消导出并被清理。

**注意**：本脚本以 GPIO89 为例。
您可以根据 D3-G 的 40 针排针使用任何可用的 GPIO 引脚。请参考官方引脚图以正确选择引脚。

<br/><br/><br/><br/>

### 7.1.6 光敏电阻 (SZH-SSBH-011)
---
光敏电阻可用于检测环境光照强度，并在光强超过特定阈值时通过 GPIO 输出数字信号。
本节介绍如何使用 D3-G 连接 SZH-SSBH-011 光敏电阻传感器并读取其输入。

#### 步骤 1. 硬件要求
- D3-G 开发板 (x1)
- 光敏电阻模块 (SZH-SSBH-011) (x1)
- LED (x1)
- 220Ω 电阻 (x1)
- 面包板 (x1)
- 公对母跳线 (x7)
- DC 5V 电源适配器 (x1)
- USB 转 TTL 串口线 (x1)

#### 步骤 2. 示例电路
- 光敏电阻 (SZH-SSBH-011)
    - 光敏电阻的 VCC 引脚连接到 D3-G 开发板的 3.3V 引脚。
    - 光敏电阻的 GND 引脚连接到 D3-G 开发板的 GND。
    - 光敏电阻的 DO 引脚连接到 D3-G 开发板的 89 号引脚。
- LED
    - LED 的 (+) 引脚连接到 D3-G 开发板的 GND。
    - LED 的 (-) 引脚连接到 D3-G 开发板的 83 号引脚。

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20D3-G/Software/circuit.png"></p>
<p align="center"><strong>图 7.7 光敏电阻实验电路</strong></p>

##### 步骤 2.1 引脚映射
下表显示了引脚映射。

<div align="center">
  <p><strong>表 7.6 D3-G 光敏电阻的引脚映射</strong></p>
  <table>
      <tr>
          <th colspan="3">引脚名称</th>
          <th>D3-G</th>
          <th>GPIO</th>
      </tr>
      <tr>
          <td colspan="3">VCC</td>
          <td>1</td>
          <td>3.3V</td>
      </tr>
      <tr>
          <td colspan="3">GND</td>
          <td>6</td>
          <td>GND</td>
      </tr>
      <tr>
          <td colspan="3">DO</td>
          <td>12</td>
          <td>89</td>
      </tr>
  </table>
</div>


<div align="center">
  <p><strong>表 7.7 D3-G LED 的引脚映射</strong></p>
  <table>
      <tr>
          <th colspan="3">引脚名称</th>
          <th>D3-G</th>
          <th>GPIO</th>
      </tr>
      <tr>
          <td colspan="3">(+)</td>
          <td>7</td>
          <td>83</td>
      </tr>
      <tr>
          <td colspan="3">(-)</td>
          <td>14</td>
          <td>GND</td>
      </tr>
  </table>
</div>

### 步骤 3. 执行方法
运行以下 Python 脚本，使用 CDS 传感器监控亮度并相应地控制 LED：

```
import os
import time
LED_PIN = 83           # LED GPIO pin
CDS_SENSOR_PIN = 89    # szh-ssbh-011 CDS sensor GPIO pin

def export_gpio(pin, direction: str):
    # If the pin is already active, unexport it.
    if os.path.exists(f"/sys/class/gpio/gpio{pin}"):
        with open("/sys/class/gpio/unexport", "w") as f:
            f.write(str(pin))
  
    # Export the pin to activate it.
    with open("/sys/class/gpio/export", "w") as f:
        f.write(str(pin))
  
    # Set the pin direction.
    with open(f"/sys/class/gpio/gpio{pin}/direction", "w") as f:
        f.write(direction)

def read_gpio_value(pin: int):
    gpio_value_path = f"/sys/class/gpio/gpio{pin}/value"
    with open(gpio_value_path, "r") as f:
        return f.read().strip()

def write_gpio_value(pin: int, value: int):
    gpio_value_path = f"/sys/class/gpio/gpio{pin}/value"
    with open(gpio_value_path, "w") as f:
        f.write(str(value))

def unexport_gpio(pin: int):
    with open("/sys/class/gpio/unexport", "w") as f:
        f.write(str(pin))

def main():
    # initialize GPIO pins
    export_gpio(LED_PIN, "out")          # LED pin direction "out"
    export_gpio(CDS_SENSOR_PIN, "in")     # CDS sensor pin direction "in"
    print("gpio pins initialized.")

    try:
        while True:
            sensor_value = read_gpio_value(CDS_SENSOR_PIN)
            print("sensor value: {}".format(sensor_value))
            if sensor_value == "0": # light detected
                print("brightness detected. Turning on the LED.")
                write_gpio_value(LED_PIN, 1)  # turn on the LED
            else:
                print("no brightness detected. Turning off the LED.")
                write_gpio_value(LED_PIN, 0)  # turn off the LED

            time.sleep(0.5)  #  500ms delay

    except KeyboardInterrupt:
        print("program interrupted by user.")

    finally:
        unexport_gpio(LED_PIN)          # unexport LED pin
        unexport_gpio(CDS_SENSOR_PIN)   # unexport CDS sensor pin
        print("GPIO pins unexported.")
        print("program terminated.")

if __name__ == "__main__":
    main()
```

### 步骤 4. 执行结果
使用以下命令运行代码。
```
$ python3 CDS_test.py
```
该脚本将 GPIO89 配置为光敏电阻传感器的输入，将 GPIO83 配置为 LED 的输出。
检测到环境光时，终端打印：
```
sensor value: 0
brightness detected. Turning on the LED.
```
同时 LED 点亮。
未检测到光时，打印：
```
sensor value: 1
no brightness detected. Turning off the LED.
```
同时 LED 熄灭。
要停止脚本，请按 **[Ctrl+C]**。
脚本终止时，两个 GPIO 引脚都会自动取消导出并被清理。

**注意**：本示例使用 GPIO83 和 GPIO89。您可以根据 D3-G 的 40 针排针布局使用任何可用的 GPIO 引脚。请参考官方引脚图以正确选择引脚。

<br/><br/><br/><br/>

### 7.1.7 空气污染检测传感器
---
空气污染检测传感器可用于监测环境中有害气体或颗粒物的存在，并通过 GPIO 输出数字信号。
本节介绍如何使用 D3-G 连接空气污染检测传感器并读取其输入。

#### 步骤 1. 硬件要求
- D3-G 开发板 (x1)
- 空气污染（气体）检测传感器模块 (x1)
- 面包板 (x1)
- 公对母跳线 (x3)
- DC 5V 电源适配器 (x1)
- USB 转 TTL 串口线 (x1)

#### 步骤 2. 示例电路
- 空气污染检测传感器
    - 空气污染检测传感器的 VCC 引脚连接到 D3-G 开发板的 3.3V 引脚。
    - 空气污染检测传感器的 GND 引脚连接到 D3-G 开发板的 GND。
    - 空气污染检测传感器的 DO 引脚连接到 D3-G 开发板的 88 号引脚。

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20D3-G/Software/gas%20circuit.png"></p>
<p align="center"><strong>图 7.8 空气污染检测传感器实验电路</strong></p>

##### 步骤 2.1 引脚映射
下表显示了引脚映射。

<div align="center">
  <p><strong>表 7.8 D3-G 空气污染检测传感器的引脚映射</strong></p>
  <table>
      <tr>
          <th colspan="3">引脚名称</th>
          <th>D3-G</th>
          <th>GPIO</th>
      </tr>
      <tr>
          <td colspan="3">VCC</td>
          <td>1</td>
          <td>3.3V</td>
      </tr>
      <tr>
          <td colspan="3">GND</td>
          <td>20</td>
          <td>GND</td>
      </tr>
      <tr>
          <td colspan="3">DO</td>
          <td>10</td>
          <td>88</td>
      </tr>
  </table>
</div>

#### 步骤 3. 执行方法
运行以下 Python 脚本，使用 GPIO88 引脚监控气体检测：

```
import os
import time
GAS_SENSOR_PIN = 88  # gas sensor GPIO pin
 
def export_gpio(pin: int, direction: str):
    # If the pin is already active, unexport it.
    if os.path.exists(f"/sys/class/gpio/gpio{pin}"):
        with open("/sys/class/gpio/unexport", "w") as f:
            f.write(str(pin))
  
    # Export the pin to activate it.
    with open("/sys/class/gpio/export", "w") as f:
        f.write(str(pin))
  
    # Set the pin direction.
    with open(f"/sys/class/gpio/gpio{pin}/direction", "w") as f:
        f.write(direction)

def read_gpio_value(pin: int):
    gpio_value_path = f"/sys/class/gpio/gpio{pin}/value"
    with open(gpio_value_path, "r") as f:
        return f.read().strip()

def write_gpio_value(pin: int, value: int):
    gpio_value_path = f"/sys/class/gpio/gpio{pin}/value"
    with open(gpio_value_path, "w") as f:
        f.write(str(value))

def unexport_gpio(pin: int):
    with open("/sys/class/gpio/unexport", "w") as f:
        f.write(str(pin))
def main():
    # initialize GPIO pins
    export_gpio(GAS_SENSOR_PIN, "in")  # gas sensor pin direction "in"
    print("gpio pins initialized.")
 
    try:
        while True:
            # gas sensor value read
            sensor_value = read_gpio_value(GAS_SENSOR_PIN)
 
            if sensor_value == "0":  # gas detected
                print("gas detected.")
            else:
                print("no gas detected.")
 
            time.sleep(0.5)  # 500ms delay

    except KeyboardInterrupt:
        print("program interrupted by user.")
 
    finally:
        unexport_gpio(GAS_SENSOR_PIN)  # unexport the GPIO pin
        print("GPIO pins unexported.")
        print("program terminated.")
         
if __name__ == "__main__":
    main()
```

#### 步骤 4. 执行结果
使用以下命令运行代码。
```
$ python3 gas_sensor_test.py
```
该脚本将 GPIO88 配置为数字输入，并持续监控气体检测状态。
当气体浓度达到传感器的阈值时，终端显示：
```
gas detected.
```
未检测到气体时，终端显示：
```
no gas detected.
```
要停止脚本，请按 **[Ctrl+C]**。
脚本终止时，GPIO88 会自动取消导出并被清理。

**注意**：此处以 GPIO88 为例。您可以根据 D3-G 的 40 针排针布局使用任何可用的 GPIO 引脚。请参考官方引脚图以正确选择引脚。

<br/><br/><br/><br/>

### 7.1.8 超声波传感器
---
超声波传感器可通过发射超声波并接收反射信号来测量与附近物体的距离，然后通过 GPIO 输出数字（或基于脉冲的）信号。
本节介绍如何使用 D3-G 连接超声波传感器并读取其输入。

#### 步骤 1. 硬件要求
- D3-G 开发板 (x1)
- 超声波传感器 (x1)
- 母对母跳线 (x4)
- DC 5V 电源适配器 (x1)
- USB 转 TTL 串口线 (x1)

#### 步骤 2. 示例电路
- 超声波传感器
    - 超声波传感器的 VCC 引脚连接到 D3-G 开发板的 5V 引脚。
    - 超声波传感器的 GND 引脚连接到 D3-G 开发板的 GND。
    - 超声波传感器的 TRIG 引脚连接到 D3-G 开发板的 82 号引脚。
    - 超声波传感器的 ECHO 引脚连接到 D3-G 开发板的 88 号引脚。

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20D3-G/Software/ultra%20circuit.png"></p>
<p align="center"><strong>图 7.9 超声波传感器实验电路</strong></p>

##### 步骤 2.1 引脚映射
下表显示了引脚映射。

<div align="center">
  <p><strong>表 7.9 D3-G 超声波传感器的引脚映射</strong></p>
  <table>
      <tr>
          <th colspan="3">引脚名称</th>
          <th>D3-G</th>
          <th>GPIO</th>
      </tr>
      <tr>
          <td colspan="3">VCC</td>
          <td>2</td>
          <td>5V</td>
      </tr>
      <tr>
          <td colspan="3">GND</td>
          <td>6</td>
          <td>GND</td>
      </tr>
      <tr>
          <td colspan="3">TRIG</td>
          <td>3</td>
          <td>82</td>
      </tr>
      <tr>
          <td colspan="3">ECHO</td>
          <td>10</td>
          <td>88</td>
      </tr>
  </table>
</div>

#### 步骤 3. 执行方法
运行以下 Python 脚本，使用超声波传感器测量距离：
```
import os
import time

TRIG_PIN = 82  
ECHO_PIN = 88  

def export_gpio(pin: int, direction: str):
    if os.path.exists(f"/sys/class/gpio/gpio{pin}"):
        with open("/sys/class/gpio/unexport", "w") as f:
            f.write(str(pin))
    with open("/sys/class/gpio/export", "w") as f:
        f.write(str(pin))
    with open(f"/sys/class/gpio/gpio{pin}/direction", "w") as f:
        f.write(direction)

def write_gpio_value(pin: int, value: int):
    with open(f"/sys/class/gpio/gpio{pin}/value", "w") as f:
        f.write(str(value))

def read_gpio_value(pin: int) -> str:
    with open(f"/sys/class/gpio/gpio{pin}/value", "r") as f:
        return f.read().strip()

def unexport_gpio(pin: int):
    with open("/sys/class/gpio/unexport", "w") as f:
        f.write(str(pin))

def get_distance_cm():
    write_gpio_value(TRIG_PIN, 0)
    time.sleep(0.00002)  
    write_gpio_value(TRIG_PIN, 1)
    time.sleep(0.00001)  
    write_gpio_value(TRIG_PIN, 0)

    start = time.time()
    while read_gpio_value(ECHO_PIN) == "0":
        start = time.time()
    end = start
    while read_gpio_value(ECHO_PIN) == "1":
        end = time.time()
    duration = end - start
    distance = (duration * 34300) / 2  # cm
    return round(distance, 2)

def main():
    export_gpio(TRIG_PIN, "out")
    export_gpio(ECHO_PIN, "in")
    print("GPIO pins initialized.")

    try:
        while True:
            distance = get_distance_cm()
            print(f"Distance: {distance} cm")
            time.sleep(1)

    except KeyboardInterrupt:
        print("Program interrupted by user.")

    finally:
        unexport_gpio(TRIG_PIN)
        unexport_gpio(ECHO_PIN)
        print("GPIO pins unexported.")
        print("Program terminated.")

if __name__ == "__main__":
    main()
```

#### 步骤 4. 执行结果
使用以下命令运行代码。
```
$ python3 ultrasonic_sensor_test.py
```
该脚本将 GPIO82 配置为数字输出以触发超声波脉冲，将 GPIO88 配置为数字输入以接收回波。
脚本运行时，每秒打印一次传感器前方最近物体的距离，例如：
```
Distance: 23.45 cm
Distance: 24.12 cm
...
```
要停止脚本，请按 **[Ctrl+C]**。
脚本终止时，GPIO82 和 GPIO88 会自动取消导出并被清理。

**注意**：此处以 GPIO82 和 GPIO88 为例。您可以根据 D3-G 的 40 针排针布局使用任何可用的 GPIO 引脚。请参考官方引脚图以正确选择引脚。此外，请确保 ECHO 引脚的电压电平对 D3-G 是安全的（某些模块输出 5V，可能需要分压电路或电平转换器）。

<br/><br/><br/><br/>

## 7.2 I2C
---
D3-G 通过 40 针 GPIO 排针提供 I2C 通信，可与传感器、显示屏和扩展模块等各种外设连接。
I2C（Inter-integrated Circuit）是一种由数据线 (SDA) 和时钟线 (SCL) 组成的两线制通信协议，可使多个设备通过共享总线进行通信。

I2C 通信采用主从架构，由一个主设备控制通信，同一总线上最多可连接 127 个从设备。
SDA 线用于数据的发送和接收，SCL 线则同步数据传输的时序。这种同步通信模型使各设备能够以时钟驱动的协调方式交换信息。

<br/><br/><br/><br/>

### 7.2.1 1602A LCD 显示屏
---
1602A LCD 是嵌入式系统中常用的字符显示模块。
在 D3-G 上，可将 LCD 的 SDA 和 SCL 线连接到配置为 I2C 的 GPIO 引脚。连接完成后，即可使用 Linux I2C 工具或自定义软件控制该 LCD。

#### 步骤 1. 硬件要求
- D3-G 开发板 (x1)
- 1602A I2C LCD 模块 (x1)
- 母对母跳线 (x4)
- DC 5V 电源适配器 (x1)
- USB 转 TTL 串口线 (x1)  

请确认 LCD 模块带有 I2C 转接板

#### 步骤 2. 示例电路
- I2C LCD 模块
    - I2C LCD 模块的 GND 引脚连接到 D3-G 开发板的 GND 引脚。
    - I2C LCD 模块的 VCC 引脚连接到 D3-G 开发板的 5V。
    - I2C LCD 模块的 SDA 引脚连接到 D3-G 开发板的 82 号引脚。
    - I2C LCD 模块的 SCL 引脚连接到 D3-G 开发板的 81 号引脚。

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20D3-G/Software/lcd_circuit.png"></p>
<p align="center"><strong>图 7.10 D3-G I2C LCD 模块电路原理图  </strong></p>

##### 步骤 2.1 引脚映射
下表显示了引脚映射。

<div align="center">
  <p><strong>表 7.10 D3-G I2C LCD 模块的引脚映射</strong></p>
  <table>
      <tr>
          <th colspan="3">引脚名称</th>
          <th>D3-G</th>
          <th>GPIO</th>
      </tr>
      <tr>
          <td colspan="3">GND</td>
          <td>20</td>
          <td>GND</td>
      </tr>
      <tr>
          <td colspan="3">VCC</td>
          <td>2</td>
          <td>5V</td>
      </tr>
      <tr>
          <td colspan="3">SDA</td>
          <td>3</td>
          <td>82</td>
      </tr>
      <tr>
          <td colspan="3">SCL</td>
          <td>5</td>
          <td>81</td>
      </tr>
  </table>
</div>

#### 步骤 3. 执行方法
首先安装所需的 Python 库：
```
$ pip install RPLCD smbus2
```
然后使用以下 Python 代码在 LCD 上显示文本：
```
import smbus2
import time
from RPLCD.i2c import CharLCD
 
# I2C bus num
I2C_BUS = 3
LCD_ADDRESS = 0x27

lcd = CharLCD(i2c_expander='PCF8574', address=LCD_ADDRESS, port=I2C_BUS,
              cols=16, rows=2, dotsize=8,
              charmap='A00', auto_linebreaks=True,
              backlight_enabled=True)
 
def display_text(text):
    lcd.clear()
    lcd.write_string(text)

def main():
    while True:
        user_input = input("Enter text to display on LCD: ")
        display_text(user_input)
        time.sleep(4)
        lcd.clear()
if __name__ == "__main__":
    main()
```

#### 步骤 4. 执行结果
使用以下命令运行代码。
```
$ python3 lcd_test.py
```
该脚本使用 RPLCD 库初始化基于 I2C 的 1602A LCD，并在屏幕上显示用户输入的文本。
运行该脚本时，系统会提示输入字符串。输入的文本会在 LCD 上显示 4 秒，然后清除。例如：
```
Enter text to display on LCD: Hello D3-G!
```
LCD 将显示：
```
Hello D3-G!
```
然后在 4 秒后清除。

要停止脚本，请按 **[Ctrl+C]**。

**注意** ：在 D3-G 上，默认使用 GPIO82 和 GPIO81 作为 I2C。
请确认 I2C 地址 (0x27) 与所使用的 LCD 模块一致。如有需要，可使用 **i2cdetect -y 3** 扫描 I2C 设备。

<br/><br/><br/><br/>

## 7.3 SPI
---
D3-G 通过 40 针 GPIO 排针支持 Serial Peripheral Interface (SPI) 通信，可在外部设备与 D3-G 之间交换数据。

SPI 是一种同步串行通信协议，支持全双工通信，即可以同时发送和接收数据。它使用四条主要信号线：Master Out Slave In (MOSI)、Master In Slave Out (MISO)、Serial Clock (SCLK) 和 Chip Select (CS)。

与多个设备共用信号线的 I2C 不同，SPI 需要为每个从设备提供独立的 CS 信号线。这种一对多结构使 SPI 速度快且易于实现，但在连接多个设备时可能需要更多的物理接线。

<br/><br/><br/><br/>

### 7.3.1 点阵屏
---
8x8 点阵屏常用于嵌入式系统中输出简单的文本或图案。在 D3-G 上，可以使用 MAX7219 等驱动芯片通过 SPI 控制点阵屏模块。

MAX7219 在内部处理行列扫描，因此微控制器仅需使用少量 SPI 信号即可控制整个显示屏：MOSI (DIN)、SCLK 和 CS (LOAD)。连接完成后，即可通过用户自定义脚本或库使用 SPI 通信控制显示屏。

#### 步骤 1. 硬件要求
- D3-G 开发板 (x1)
- 点阵屏 (x1)
- 公对母杜邦线 (x4)
- DC 5V 电源适配器 (x1)
- USB 转 TTL 串口线 (x1)

#### 步骤 2. 示例电路
- 点阵屏
    - 点阵屏的 VCC 引脚连接到 D3-G 开发板的 5V 引脚。
    - 点阵屏的 GND 引脚连接到 D3-G 开发板的 GND 引脚。
    - 点阵屏的 DIN 引脚连接到 D3-G 开发板的 120 号引脚。
    - 点阵屏的 CS 引脚连接到 D3-G 开发板的 119 号引脚。
    - 点阵屏的 CLK 引脚连接到 D3-G 开发板的 118 号引脚。

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20D3-G/Software/dot%20circuit.png"></p>
<p align="center"><strong>图 7.11 D3-G 点阵屏模块电路原理图  </strong></p>

##### 步骤 2.1 引脚映射
下表显示了引脚映射。
<div align="center">
  <p><strong>表 7.11 D3-G 点阵屏引脚映射</strong></p>
  <table>
      <tr>
          <th colspan="3">引脚名称</th>
          <th>D3-G</th>
          <th>GPIO</th>
      </tr>
      <tr>
          <td colspan="3">VCC</td>
          <td>2</td>
          <td>5V</td>
      </tr>
      <tr>
          <td colspan="3">GND</td>
          <td>6</td>
          <td>GND</td>
      </tr>
      <tr>
          <td colspan="3">DIN</td>
          <td>19</td>
          <td>63</td>
      </tr>
      <tr>
          <td colspan="3">CS</td>
          <td>24</td>
          <td>62</td>
      </tr>
      <tr>
          <td colspan="3">CLK</td>
          <td>23</td>
          <td>61</td>
      </tr>
  </table>
</div>

#### 步骤 3. 执行方法
以下 Python 脚本演示了如何通过底层 fcntl 调用经由 /dev/spidev3.0 直接控制 MAX7219。该方法适用于没有外部 SPI 库的设备：
```
#!/usr/bin/env python3
 
import os
import fcntl
import time
from ctypes import Structure, addressof, create_string_buffer, c_uint64, c_uint32, c_uint16, c_uint8
 
SPI_MODE = 0
SPI_SPEED_HZ = 5000000
SPI_BITS_PER_WORD = 8
 
SPI_IOC_RD_MODE = 0x80016b01
SPI_IOC_WR_MODE = 0x40016b01
SPI_IOC_RD_BITS_PER_WORD = 0x80016b03
SPI_IOC_WR_BITS_PER_WORD = 0x40016b03
SPI_IOC_WR_MAX_SPEED_HZ = 0x40046b04
SPI_IOC_MESSAGE_1 = 0x40206b00
 
class spi_ioc_transfer(Structure):
    _fields_ = [
        ("tx_buf", c_uint64),
        ("rx_buf", c_uint64),
        ("len", c_uint32),
        ("speed_hz", c_uint32),
        ("delay_usecs", c_uint16),
        ("bits_per_word", c_uint8),
        ("cs_change", c_uint8),
        ("pad", c_uint32)
    ]
 
def spi_transfer(fd, tx_data):
    tx_buffer = create_string_buffer(bytes(tx_data))
    rx_buffer = create_string_buffer(len(tx_data))
 
    xfer = spi_ioc_transfer(
        tx_buf=addressof(tx_buffer),
        rx_buf=addressof(rx_buffer),
        len=len(tx_data),
        delay_usecs=0,
        speed_hz=SPI_SPEED_HZ,
        bits_per_word=SPI_BITS_PER_WORD,
        cs_change=0
    )
 
    fcntl.ioctl(fd, SPI_IOC_MESSAGE_1, xfer)
 
    return list(rx_buffer)
 
def MAX7219_write(fd, address, data):
    spi_transfer(fd, [address, data])
 
def MAX7219_init(fd):
    MAX7219_write(fd, 0x09, 0x00)  # Decoding mode: none
    MAX7219_write(fd, 0x0A, 0x03)  # Intensity: 3 (range 0-15)
    MAX7219_write(fd, 0x0B, 0x07)  # Scan limit: 8 LEDs
    MAX7219_write(fd, 0x0C, 0x01)  # Power on
    MAX7219_write(fd, 0x0F, 0x00)  # Display test: off
 
NUMBER_CODE = [
    [0x3C, 0x42, 0x42, 0x42, 0x42, 0x42, 0x42, 0x3C],  # 0
    [0x10, 0x30, 0x50, 0x10, 0x10, 0x10, 0x10, 0x7C],  # 1
    [0x3E, 0x02, 0x02, 0x3E, 0x20, 0x20, 0x3E, 0x00],  # 2
    [0x00, 0x7C, 0x04, 0x04, 0x7C, 0x04, 0x04, 0x7C],  # 3
    [0x08, 0x18, 0x28, 0x48, 0xFE, 0x08, 0x08, 0x08],  # 4
    [0x3C, 0x20, 0x20, 0x3C, 0x04, 0x04, 0x3C, 0x00],  # 5
    [0x3C, 0x20, 0x20, 0x3C, 0x24, 0x24, 0x3C, 0x00],  # 6
    [0x3E, 0x22, 0x04, 0x08, 0x08, 0x08, 0x08, 0x08],  # 7
    [0x00, 0x3E, 0x22, 0x22, 0x3E, 0x22, 0x22, 0x3E],  # 8
    [0x3E, 0x22, 0x22, 0x3E, 0x02, 0x02, 0x02, 0x3E]   # 9
]
 
ALPHABET_CODE = {
    'A': [0x08, 0x14, 0x22, 0x3E, 0x22, 0x22, 0x22, 0x22],
    'B': [0x3C, 0x22, 0x22, 0x3E, 0x22, 0x22, 0x3C, 0x00],
    'C': [0x3C, 0x40, 0x40, 0x40, 0x40, 0x40, 0x3C, 0x00],
    'D': [0x7C, 0x42, 0x42, 0x42, 0x42, 0x42, 0x7C, 0x00],
    'E': [0x7C, 0x40, 0x40, 0x7C, 0x40, 0x40, 0x40, 0x7C],
    'F': [0x7C, 0x40, 0x40, 0x7C, 0x40, 0x40, 0x40, 0x40],
    'G': [0x3C, 0x40, 0x40, 0x40, 0x40, 0x44, 0x44, 0x3C],
    'H': [0x44, 0x44, 0x44, 0x7C, 0x44, 0x44, 0x44, 0x44],
    'I': [0x7C, 0x10, 0x10, 0x10, 0x10, 0x10, 0x10, 0x7C],
    'J': [0x3C, 0x08, 0x08, 0x08, 0x08, 0x08, 0x48, 0x30],
    'K': [0x40, 0x40, 0x40, 0x40, 0x40, 0x40, 0x40, 0x7C],
    'L': [0x40, 0x40, 0x40, 0x40, 0x40, 0x40, 0x40, 0x7C],
    'M': [0x00, 0x42, 0x62, 0x52, 0x4A, 0x46, 0x42, 0x00],
    'N': [0x00, 0x42, 0x62, 0x52, 0x4A, 0x46, 0x42, 0x00],
    'O': [0x3C, 0x42, 0x42, 0x42, 0x42, 0x42, 0x42, 0x3C],
    'P': [0x3C, 0x42, 0x42, 0x3E, 0x02, 0x02, 0x02, 0x3E],
    'Q': [0x3C, 0x42, 0x42, 0x42, 0x42, 0x42, 0x42, 0x3C],
    'R': [0x08, 0x14, 0x22, 0x3E, 0x22, 0x22, 0x22, 0x22],
    'S': [0x7C, 0x40, 0x40, 0x7C, 0x40, 0x40, 0x40, 0x7C],
    'T': [0x7C, 0x10, 0x10, 0x10, 0x10, 0x10, 0x10, 0x7C],
    'U': [0x3C, 0x08, 0x08, 0x08, 0x08, 0x08, 0x48, 0x30],
    'V': [0x40, 0x40, 0x40, 0x40, 0x40, 0x40, 0x40, 0x7C],
    'W': [0x00, 0x41, 0x41, 0x41, 0x49, 0x2a, 0x2a, 0x14],
    'X': [0x40, 0x40, 0x40, 0x40, 0x40, 0x40, 0x40, 0x7C],
    'Y': [0x7C, 0x40, 0x40, 0x7C, 0x40, 0x40, 0x40, 0x7C],
    'Z': [0x7C, 0x40, 0x40, 0x7C, 0x40, 0x40, 0x40, 0x7C],
    'Smile': [0x3c, 0x42, 0xa5, 0x81, 0xa5, 0x99, 0x42, 0x3c],
    'dance0': [0x10, 0x28, 0x10, 0x10, 0xfe, 0x10, 0x28, 0x28],
    'dance1': [0x10, 0x28, 0x92, 0x54, 0x38, 0x10, 0x28, 0x44],
    'angry': [0x00, 0x00, 0xe7, 0x00, 0x00, 0x00, 0x3c, 0x00],
    'Good': [0x30, 0x30, 0x30, 0x3c, 0x32, 0x3c, 0x32, 0x3c]
}
 
 
def main():
    print('*' * 50)
    fd = os.open('/dev/spidev3.0', os.O_RDWR)
 
    fcntl.ioctl(fd, SPI_IOC_RD_BITS_PER_WORD, bytes([SPI_BITS_PER_WORD]))
    fcntl.ioctl(fd, SPI_IOC_WR_BITS_PER_WORD, bytes([SPI_BITS_PER_WORD]))
    fcntl.ioctl(fd, SPI_IOC_WR_MODE, bytes([SPI_MODE]))
    fcntl.ioctl(fd, SPI_IOC_WR_MAX_SPEED_HZ, SPI_SPEED_HZ.to_bytes(4, byteorder='little'))
 
    MAX7219_init(fd)
 
    try:
        while True:
            input_str = input("Enter a number, an uppercase letter (0-9, A-Z), 'Smile', 'Dance', 'Angry', 'Good', 'Nice', 'Emotion': ")
            if input_str.isdigit() and 0 <= int(input_str) <= 9:
                num = int(input_str)
                for col in range(8):
                    MAX7219_write(fd, col + 1, NUMBER_CODE[num][col])
                    time.sleep(0.1)
            elif input_str.isalpha() and input_str.isupper() and len(input_str) == 1:
                char = input_str
                for col in range(8):
                    MAX7219_write(fd, col + 1, ALPHABET_CODE[char][col])
                    time.sleep(0.1)
            elif input_str == 'Smile':
                smile_pattern = ALPHABET_CODE['Smile']
                for col in range(8):
                    MAX7219_write(fd, col + 1, smile_pattern[col])
                    time.sleep(0.1)
            elif input_str == 'Dance': 
                for _ in range(10):
                    for col in range(8):
                        MAX7219_write(fd, col + 1, ALPHABET_CODE['dance0'][col])
                    time.sleep(0.5)
                    for col in range(8):
                        MAX7219_write(fd, col + 1, ALPHABET_CODE['dance1'][col])
                    time.sleep(0.5)
            elif input_str == 'Angry': 
                angry_pattern = ALPHABET_CODE['angry']
                for col in range(8):
                    MAX7219_write(fd, col + 1, angry_pattern[col])
                    time.sleep(0.1)
            elif input_str == 'Good':
                good_pattern = ALPHABET_CODE['Good']
                for col in range(8):
                    MAX7219_write(fd, col + 1, good_pattern[col])
                    time.sleep(0.1)
            elif input_str == 'Nice':
                for _ in range(3):
                    for col in range(8):
                        MAX7219_write(fd, col + 1, ALPHABET_CODE['N'][col])
                    time.sleep(0.5)
                    for col in range(8):
                        MAX7219_write(fd, col + 1, ALPHABET_CODE['I'][col])
                    time.sleep(0.5)
                    for col in range(8):
                        MAX7219_write(fd, col + 1, ALPHABET_CODE['C'][col])
                    time.sleep(0.5)
                    for col in range(8):
                        MAX7219_write(fd, col + 1, ALPHABET_CODE['E'][col])
                    time.sleep(0.5)
            elif input_str == 'Emotion':
                for _ in range (6):
                    for col in range(8):
                        MAX7219_write(fd, col + 1, ALPHABET_CODE['Smile'][col])
                    time.sleep(0.5)
                    for col in range(8):
                        MAX7219_write(fd, col + 1, ALPHABET_CODE['angry'][col])
                    time.sleep(0.5)
            else:
                   print("Invalid input. Please enter a number (0-9), an uppercase letter (A-Z), 'Smile', 'Dance', 'Angry', 'Good', 'Nice', 'Emotion'.")
 
    except KeyboardInterrupt:
        os.close(fd)
    finally:
        os.close(fd)
 
if __name__ == "__main__":
    main()
```

#### 步骤 4. 执行结果
使用以下命令运行代码。
```
$ python3 dot_matrix_test.py
```
该脚本初始化通过 SPI 连接的 MAX7219 点阵屏，并提示输入一个值。根据输入内容，8x8 LED 点阵会显示相应的图案。

运行该脚本时，将看到：
```
Enter a number, an uppercase letter (0-9, A-Z), 'Smile', 'Dance', 'Angry', 'Good', 'Nice', 'Emotion':
```
示例：
- 输入 A 将显示字母 A。
- 输入 Smile 将显示笑脸图案。
- 输入 Dance 将触发交替播放的舞蹈动画。
- 输入 Nice 将依次动态显示字母 N-I-C-E。

要停止脚本，请按 **[Ctrl+C]**。
终止时，SPI 设备会被安全关闭，LED 点阵停止刷新。

**注意**：请确认 /dev/spidev3.0 存在，且接线与引脚映射表一致。此外，请为 MAX7219 模块提供稳定的 5V 电源。

<br/><br/><br/><br/>

## 7.4 PWM
---
Pulse Width Modulation (PWM) 通过改变脉冲信号的宽度来控制 LED、电机和蜂鸣器等设备。D3-G 通过 Linux 中的 sysfs 接口支持 PWM。

### 7.4.1 LED 亮度控制
---
本示例演示如何在 D3-G 上使用 PWM 控制 LED 的亮度。

#### 步骤 1. 硬件要求
- D3-G 开发板 (x1)
- LED (x1)
- 公对母杜邦线 (x2)
- 面包板
- DC 5V 电源适配器 (x1)
- USB 转 TTL 串口线 (x1)

#### 步骤 2. 示例电路
- LED
    - LED 的 (+) 引脚连接到 D3-G 开发板的 89 号引脚。
    - LED 的 (-) 引脚连接到 D3-G 开发板的 GND 引脚。

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20D3-G/Software/led.png"></p>
<p align="center"><strong>图 7.12 D3-G LED 电路原理图  </strong></p>

##### 步骤 2.1 引脚映射
下表显示了引脚映射。

<div align="center">
  <p><strong>表 7.12 D3-G LED 引脚映射</strong></p>
  <table>
      <tr>
          <th colspan="3">引脚名称</th>
          <th>D3-G</th>
          <th>GPIO</th>
      </tr>
      <tr>
          <td colspan="3">( + )</td>
          <td>12</td>
          <td>89</td>
      </tr>
      <tr>
          <td colspan="3">( – )</td>
          <td>14</td>
          <td>GND</td>
      </tr>
  </table>
</div>

#### 步骤 3. 执行方法
要驱动连接在 D3-G 开发板 GPIO89 上的 LED (PWM)，请运行以下代码：
```
import time

PWM_CHIP = "pwmchip0"
PWM_CHANNEL = "pwm0"
PWM_PATH = f"/sys/class/pwm/{PWM_CHIP}/{PWM_CHANNEL}"
EXPORT_PATH = f"/sys/class/pwm/{PWM_CHIP}/export"
UNEXPORT_PATH = f"/sys/class/pwm/{PWM_CHIP}/unexport"

PERIOD = 1000000  # 1ms = 1kHz
STEP = 10000
SLEEP = 0.01

def pwm_setup():
    try:
        with open(EXPORT_PATH, "w") as f:
            f.write("0")
    except Exception:
        pass  # Already exported
    time.sleep(0.1)

    with open(f"{PWM_PATH}/period", "w") as f:
        f.write(str(PERIOD))
        f.flush()

    with open(f"{PWM_PATH}/enable", "w") as f:
        f.write("1")
        f.flush()

def pwm_cleanup():
    try:
        with open(f"{PWM_PATH}/enable", "w") as f:
            f.write("0")
            f.flush()
        with open(UNEXPORT_PATH, "w") as f:
            f.write("0")
    except Exception as e:
        print("PWM cleanup failed:", e)

try:
    pwm_setup()
    print("Starting LED PWM control (press Ctrl+C to stop)")

    while True:
        for duty in range(0, PERIOD, STEP):
            with open(f"{PWM_PATH}/duty_cycle", "w") as f:
                f.write(str(min(duty, PERIOD - 1)))
                f.flush()
            time.sleep(SLEEP)

        for duty in range(PERIOD, 0, -STEP):
            with open(f"{PWM_PATH}/duty_cycle", "w") as f:
                f.write(str(min(duty, PERIOD - 1)))
                f.flush()
            time.sleep(SLEEP)

except KeyboardInterrupt:
    print("\nStopped by user.")

finally:
    pwm_cleanup()
    print("PWM disabled and cleaned up.")
```

#### 步骤 4. 执行结果
使用以下命令运行代码。
```
$ python3 led_pwm.py
```
该脚本在 LED 引脚上初始化 PWM，并持续使 LED 亮度由亮变暗、由暗变亮。

执行该脚本后，将看到如下输出：
```
Starting LED PWM control (press Ctrl+C to stop)
```
LED 会逐渐变亮然后变暗，如此反复，模拟"呼吸"效果。

要停止脚本，请按 **[Ctrl+C]**。

**注意**：请确认 PWM 通道未被占用，且 D3-G 在所选 GPIO 上支持硬件 PWM。如果 PWM 未启动，请检查 /sys/class/pwm/ 中的 export、period 和 duty_cycle 设置。

<br/><br/><br/><br/>

### 7.4.2 微型舵机
---
微型舵机可通过 GPIO 输出的 Pulse Width Modulation (PWM) 信号实现精确的角度运动控制。
本节演示如何使用 D3-G 连接并控制微型舵机。

#### 步骤 1. 硬件要求
- D3-G 开发板 (x1)
- 舵机 (x1)
- 公对母跳线 (x3)
- DC 5V 电源适配器 (x1)
- USB 转 TTL 串口线 (x1)

#### 步骤 2. 示例电路
- 舵机
    - 舵机的 VCC 引脚连接到 D3-G 开发板的 5V。
    - 舵机的 GND 引脚连接到 D3-G 开发板的 GND。
    - 舵机的 SIG 引脚连接到 D3-G 开发板的 89 号引脚。

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20D3-G/Software/motor_circuit.png"p>
<p align="center"><strong>图 7.13 D3-G 舵机电路原理图  </strong></p>

##### 步骤 2.1 引脚映射
下表显示了引脚映射。

<div align="center">
  <p><strong>表 7.13 D3-G 舵机引脚映射</strong></p>
  <table>
      <tr>
          <th colspan="3">引脚名称</th>
          <th>D3-G</th>
          <th>GPIO</th>
      </tr>
      <tr>
          <td colspan="3">VCC</td>
          <td>2</td>
          <td>5V</td>
      </tr>
      <tr>
          <td colspan="3">GND</td>
          <td>20</td>
          <td>GND</td>
      </tr>
      <tr>
          <td colspan="3">SIG</td>
          <td>12</td>
          <td>89</td>
      </tr>
  </table>
</div>

#### 步骤 3. 执行方法
以下 Python 脚本演示了如何在 D3-G 上通过 sysfs 接口使用 PWM 直接控制微型舵机。该方法无需外部库，并可对基于角度的定位进行精细控制。
```
import time
import os

PWM_CHIP = "pwmchip0"
PWM_CHANNEL = "pwm0"
PWM_PATH = f"/sys/class/pwm/{PWM_CHIP}/{PWM_CHANNEL}"
EXPORT_PATH = f"/sys/class/pwm/{PWM_CHIP}/export"
UNEXPORT_PATH = f"/sys/class/pwm/{PWM_CHIP}/unexport"

PERIOD = 20_000_000  # 20ms (50Hz)

def angle_to_duty(angle):
    pulse_width = 1_000_000 + (angle / 180) * 1_000_000
    return int(pulse_width)

def pwm_setup():
    if not os.path.exists(PWM_PATH):
        with open(EXPORT_PATH, "w") as f:
            f.write("0")
        time.sleep(0.1)
    with open(f"{PWM_PATH}/period", "w") as f:
        f.write(str(PERIOD))
    with open(f"{PWM_PATH}/enable", "w") as f:
        f.write("1")

def pwm_set_angle(angle):
    duty = angle_to_duty(angle)
    with open(f"{PWM_PATH}/duty_cycle", "w") as f:
        f.write(str(duty))

def pwm_cleanup():
    try:
        with open(f"{PWM_PATH}/enable", "w") as f:
            f.write("0")
        with open(UNEXPORT_PATH, "w") as f:
            f.write("0")
    except Exception as e:
        print("PWM cleanup failed:", e)

if __name__ == "__main__":
    pwm_setup()

    try:
        while True:
            user_input = input("Enter 1 (CW) or 0 (CCW), q to quit: ").strip()
            if user_input == 'q':
                break
            elif user_input == '1':
                pwm_set_angle(180)  
                time.sleep(0.5)
            elif user_input == '0':
                pwm_set_angle(0)   
                time.sleep(0.5)
            else:
                print("Invalid input. Use 0, 1, or q.")
    except KeyboardInterrupt:
        print("\nInterrupted by user.")
    finally:
        pwm_cleanup()
        print("PWM cleaned up.")
```

#### 步骤 4. 执行结果
使用以下命令运行代码。
```
$ python3 motor_test.py
```
该脚本使用 PWM 控制微型舵机，根据目标角度调整占空比。
执行后，将出现如下提示：
```
Enter 1 (CW) or 0 (CCW), q to quit:
```
输入 1 时舵机顺时针旋转至 180°，输入 0 时舵机逆时针旋转至 0°。可根据需要反复操作。

要停止该脚本，请输入 **[q]** 或按 **[Ctrl+C]**。随后脚本会禁用并 unexport PWM 通道。

**注意**：为确保安全运行，请确认舵机支持 50 Hz 的 PWM 信号，并在 1 ms 至 2 ms 的占空脉冲范围内工作。
