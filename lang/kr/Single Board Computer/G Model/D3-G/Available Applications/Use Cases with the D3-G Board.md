# 1. 소개 
---
이 문서는 D3-G 사용 예제를 제공합니다.   
이 문서는 다음 정보를 포함합니다:
- 입력 장치
  - 키보드 
  - 마우스
- 비디오 출력
- 카메라 연결
  - MIPI CSI
  - USB 웹캠
- 스토리지 연결
  - SD 카드
  - SATA HDD
  - NVMe M.2 SSD
  - USB 저장 장치
- 이더넷 연결
- 40핀 GPIO 헤더
  - 사용 가능한 센서 및 디바이스

<br/><br/><br/><br/>


# 2. 입력 장치
---
D3-G는 입력 장치 연결을 위해 두 개의 USB 포트를 지원합니다.
USB 2.0 Type-A 포트 1개와 USB 3.0 Type-A 포트 1개가 있으며, 마우스나 키보드를 연결하여 D3-G를 직접 제어할 수 있습니다. 

**참고**: D3-G의 USB Type-C 포트는 펌웨어 다운로드 전용이므로 입력 장치 연결에 사용할 수 없습니다.

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20D3-G/Software/input%20device.png" width="500"></p>
<p align="center"><strong>그림 2.1 D3-G 보드에 입력 장치 연결 </strong></p><br/><br/><br/><br/>


# 3. 비디오 출력
---
D3-G는 DisplayPort(DP) 출력을 통해서만 FHD 모니터를 지원합니다.
또한 데이지 체인 구성을 사용한 다중 디스플레이 출력을 지원하여 최대 2대의 FHD 모니터와 1대의 HD 모니터를 동시에 연결할 수 있습니다.

**참고**: HDMI를 사용하려면 별도의 액티브 컨버터 어댑터가 필요합니다.
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20D3-G/Software/monitor.png" width="500"></p>
<p align="center"><strong>그림 3.1 D3-G 보드에 모니터 연결 </strong></p>

<br/><br/><br/><br/>

# 4. 카메라 연결
---
D3-G는 카메라 기능을 지원하여 다양한 애플리케이션에 유연하게 대응합니다.
프로젝트 요구 사항에 따라 MIPI CSI 카메라 또는 USB 웹캠을 연결할 수 있습니다.

<br/><br/><br/>

## 4.1 USB 웹캠
---
D3-G는 최대 Full HD(FHD) 해상도의 USB 웹캠을 지원합니다.
다음 단계에 따라 웹캠을 테스트할 수 있습니다:


#### 단계 1. USB 카메라를 보드의 USB 포트에 연결합니다.
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20D3-G/Software/webcam.png" width="400"></p>
<p align="center"><strong>그림 4.1 D3-G 보드에 웹캠 연결</strong></p><br/>

#### 단계 2. 입력 장치(마우스 및 키보드)와 모니터를 D3-G에 연결합니다.
   
#### 단계 3. D3-G를 부팅합니다.

#### 단계 4. 사용 가능한 /dev/video 장치를 확인합니다.
```
$ ls /dev/video*
```

#### 단계 5. OpenCV(또는 vutils)를 사용하여 비디오 출력을 확인합니다.
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
CSI는 Camera Serial Interface의 약자로, 카메라 모듈을 호스트 프로세서에 연결하기 위해 MIPI Alliance가 정의한 표준 인터페이스입니다.
이를 통해 카메라에서 프로세서로 이미지 데이터를 고속 및 저전력으로 전송할 수 있습니다.

D3-G는 두 개의 MIPI CSI 채널(ch0 및 ch1)을 제공하므로 Flat Flexible Cable(FFC) 연결을 지원하는 카메라 모듈을 장착할 수 있습니다.
현재 D3-G는 ArduCam(5 MP)과 Raspberry Pi v1 Camera(5 MP) 모듈만 지원합니다. 

**참고**: 현재 D3-G는 CSI 채널 0과 CSI 채널 1의 동시 사용을 지원하지 않습니다.

<br/><br/>

### 4.2.1 ArduCam
ArduCam은 임베디드 시스템과 IoT 애플리케이션을 위해 설계된 다목적 카메라 모듈입니다. MIPI CSI를 포함한 다양한 이미지 센서와 인터페이스를 지원하므로 D3-G와 같은 개발 보드에 통합하기에 적합합니다.
D3-G가 지원하는 5 MP ArduCam 모듈은 우수한 화질을 제공하며 기본적인 컴퓨터 비전 작업, 스트리밍, 카메라 기반 AI 애플리케이션에 널리 사용됩니다. FFC 케이블과 호환되므로 D3-G 보드의 CSI 인터페이스에 쉽게 연결할 수 있습니다. 

ArduCam 모듈의 사양은 다음과 같습니다.

| 사양                     | 설명                                 |
| ------------------------ | ------------------------------------------- |
| 센서                   | OV5647 (500만 화소)                        |
| 해상도                    | 2592 × 1944 (Full 5 MP)                      |
| 지원 출력 포맷 | RAW, YUV, JPEG (센서에 따라 다름)           |
| 인터페이스                 | MIPI CSI-2                                  |
| 프레임 레이트               | 1080p에서 최대 30fps, 720p에서 60fps         |
| 렌즈 마운트               | 고정 초점 렌즈 (표준)                 |
| 시야각 (FOV)              | 약 54° – 70° (모델에 따라 다름)                   |
| 연결 방식                  | Flat Flexible Cable (FFC)                   |
| 동작 전압        | 3.3V (일반)                              |
| 폼 팩터              | 소형 PCB, 약 25 mm x 24 mm                   |
| 호환성                    | Raspberry Pi 및 D3-G (MIPI CSI-2 포트를 통해)     |
| 추가 기능      | 저전력 소비, 플러그 앤 플레이 모듈 |


다음 단계에 따라 ArduCam을 테스트할 수 있습니다:
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20D3-G/Software/arducam.png" width="400"></p>
<p align="center"><strong>그림 4.2 ArduCam </strong></p><br/>

#### 단계 1. 그림 4.3과 같이 ArduCam을 D3-G 보드의 MIPI CSI 0에 연결합니다.
 
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20D3-G/Software/rasp%20v1%20cam%20to%20d3g.png" width="500"></p>
<p align="center"><strong>그림 4.3 D3-G 보드에 ArduCam 연결</strong></p> <br/>

#### 단계 2. ArduCam을 연결한 후 D3-G 보드에서 다음 GStreamer 명령을 사용하여 비디오 스트림을 확인할 수 있습니다:
```
$ gst-launch-1.0 v4l2src device=/dev/video0 io-mode=2 ! video/x-raw,format=NV12,width=1920,height=1280,framerate=30/1 ! videoconvert ! waylandsink fullscreen=true
```

이 명령은 CSI로 연결된 ArduCam에서 비디오를 캡처하고 표시용으로 변환한 후 Wayland 디스플레이 서버를 사용하여 전체 화면 모드로 렌더링합니다.  
명령을 실행하기 전에 카메라 모듈이 단단히 연결되어 있는지 확인하십시오. 비디오가 표시되지 않으면 케이블 연결을 확인하고 /dev/video0이 시스템에서 정상적으로 인식되는지 확인하십시오.

<br/><br/>

### 4.2.2 Raspberry Pi v1 Camera
Raspberry Pi v1 Camera Module은 Raspberry Pi Foundation에서 개발한 소형 5 MP 카메라입니다. OmniVision OV5647 이미지 센서를 기반으로 하며, Flat Flexible Cable(FFC)을 사용하여 MIPI CSI-2 인터페이스를 통해 호스트 보드에 연결됩니다.

원래 Raspberry Pi 시리즈용으로 설계되었지만 D3-G와도 호환되므로 이미지 캡처, 비디오 녹화, 컴퓨터 비전 프로젝트와 같은 기본적인 카메라 애플리케이션에 적합한 선택입니다.

Raspberry Pi v1 Camera 모듈의 사양은 다음과 같습니다.

| 사양                | 설명                              |
| ------------------- | ---------------------------------------- |
| 센서              | OmniVision OV5647                        |
| 해상도          | 2592 × 1944 (5 MP)                        |
| 출력 포맷      | RAW, YUV, JPEG                           |
| 인터페이스            | MIPI CSI-2                               |
| 프레임 레이트          | 1080p30, 720p60, VGA90                   |
| 렌즈                | 고정 초점                              |
| 화각 (FOV) | 최대 54°                                     |
| 케이블 유형          | FFC (15핀)                             |
| 보드 치수    | 25 mm x 24 mm                              |
| 호환성               | Raspberry Pi 및 D3-G (MIPI CSI-2 포트를 통해) |

다음 단계에 따라 Raspberry Pi v1 카메라를 테스트할 수 있습니다:

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20D3-G/Software/rasp%20v1%20cam.jpg" width="400"></p>
<p align="center"><strong>그림 4.4. Raspberry Pi v1 Camera </strong></p><br/>

#### 단계 1. 그림 4.5와 같이 Raspberry Pi v1 카메라를 D3-G 보드의 MIPI CSI 1에 연결합니다.
 
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20D3-G/Software/rasp%20v1%20cam%20to%20d3g.png" width="500"></p>
<p align="center"><strong>그림 4.5 D3-G 보드에 Raspberry Pi v1 Camera 연결</strong></p> <br/>

#### 2단계. Raspberry Pi 카메라를 연결한 후 D3-G에서 다음 GStreamer 명령을 사용하여 비디오 스트림을 확인할 수 있습니다:
```
$ gst-launch-1.0 v4l2src device=/dev/video0 io-mode=2 ! video/x-raw,format=NV12,width=1920,height=1280,framerate=30/1 ! videoconvert ! waylandsink fullscreen=true
```

이 명령은 CSI로 연결된 Raspberry Pi 카메라에서 비디오를 캡처하고 표시용으로 변환한 다음, Wayland 디스플레이 서버를 사용하여 전체 화면 모드로 렌더링합니다.  
명령을 실행하기 전에 카메라 모듈이 단단히 연결되어 있는지 확인하십시오. 비디오가 표시되지 않으면 케이블 연결을 확인하고 /dev/video0이 시스템에서 정상적으로 인식되는지 확인하십시오.

<br/><br/><br/><br/>

# 5. 스토리지 연결
---
이 장에서는 D3-G를 다양한 스토리지 장치에 연결하는 방법을 설명합니다. 지원되는 스토리지 옵션에는 USB 드라이브, SD 카드 및 PCIe를 통한 외장 스토리지가 있습니다.

<br/><br/><br/>

## 5.1 USB 드라이브
---
D3-G는 USB 2.0 및 USB 3.0 Type-A 포트를 통해 USB 스토리지 장치를 지원합니다.
USB 드라이브를 연결하려면:

### 1단계. D3-G에서 사용 가능한 USB Type-A 포트 중 하나에 USB 드라이브를 연결합니다.
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20D3-G/Software/usb%20storage%20connection%20with%20d3g.png" width="500"></p>
<p align="center"><strong>그림 5.1 D3-G 보드에 USB 스토리지 연결</strong></p> <br/>

### 2단계. 연결한 후에는 시스템 상태에 따라 장치가 일반적으로 /dev/sda1, /dev/sdb1 등으로 인식됩니다.

<br/>

### 3단계. 다음 명령을 사용하여 USB 드라이브를 수동으로 마운트할 수 있습니다:
   ```
   $ sudo mount /dev/sda1 /mnt
   ```

<br/><br/><br/>

## 5.2 SD 카드
---
D3-G에는 표준 SDHC/SDXC 카드를 지원하는 microSD 카드 슬롯이 있습니다.
D3-G에서 SD 카드를 사용하려면:

<br/>

### 1단계. D3-G 보드의 SD 카드 슬롯에 microSD 카드를 삽입합니다.
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20D3-G/Software/sd%20card%20connect%20with%20d3g.png" width="500"></p>
<p align="center"><strong>그림 5.2 D3-G 보드에 SD 카드 연결</strong></p> <br/>

### 2단계. 삽입한 후에는 시스템이 일반적으로 SD 카드를 /dev/mmcblk1p1 또는 유사한 장치 노드로 인식합니다.
  ```
  $ ls /dev/mmcblk*
  ```
<br/>

### 3단계. SD 카드를 수동으로 마운트하려면 다음 명령을 사용하십시오:
```
$ sudo mount /dev/mmcblk1p1 /mnt 
```
### 4단계. 마운트한 후에는 /mnt 디렉터리에서 SD 카드의 내용에 접근할 수 있습니다.

<br/><br/><br/>

## 5.3 SATA HDD
---

D3-G는 호환되는 SATA 컨트롤러를 사용하여 PCIe 슬롯을 통해 HDD 또는 SSD와 같은 SATA 스토리지 장치를 사용할 수 있도록 지원합니다.

<br/>

#### 1단계. PCIe to SATA 모듈 연결

PCIe를 통해 D3-G에서 SATA HDD를 사용하려면 먼저 PCIe-to-SATA 어댑터 모듈을 D3-G의 PCIe 슬롯에 연결해야 합니다.

그런 다음 HDD를 SATA 모듈에 연결하고 HDD에 외부 12V 전원 공급 장치로 전원이 공급되는지 확인하십시오.

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20D3-G/Software/sata.png" width="500"></p>
<p align="center"><strong>그림 5.3 D3-G 보드 PCIe에 SATA 모듈 연결 </strong></p><br/>

#### 2단계. D3-G 부팅 
D3-G를 부팅한 후 부팅 로그를 확인하여 PCIe 장치가 시스템에서 인식되는지 확인하십시오.
PCIe 링크가 성공적으로 설정되었음을 나타내는 **telechips-pcie: Link up**과 같은 메시지를 찾으십시오.

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

#### 3단계. SATA HDD 인식 확인
```
root@TOPST:~# lspci
00:00.0 PCI bridge: Synopsys, Inc. Device 8040 (rev 01)
01:00.0 SATA controller: ASMedia Technology Inc. Device 1064 (rev 02)
```
**lspci** 명령을 사용할 수 없는 경우 다음 명령을 사용하여 pciutils를 설치하십시오.

```
$ sudo apt-get install pciutils
```

<br/>

#### 4단계. SATA HDD 마운트
```
$ fdisk /dev/sda
Welcome to fdisk (util-linux 2.37.4).
Changes will remain in memory only, until you decide to write them.
Be careful before using the write command.

Command (m for help): 
```

fdisk 프롬프트에서 다음 키를 순서대로 입력하십시오:

- o — 비어 있는 새 DOS 파티션 테이블 생성 (선택 사항, 기존 테이블 삭제)

- n — 새 파티션 추가

- p — 주 파티션 선택

- 1 — 파티션 번호를 1로 설정

- Enter 키 입력 — 기본 시작 섹터 적용

- Enter 키 입력 — 기본 마지막 섹터 적용 (디스크 전체 사용)

- w — 파티션 테이블을 기록하고 종료합니다

```
$ mkfs.ext4 /dev/sda1

$ mkdir -p /mnt/sata

$ mount /dev/sda1 /mnt/sata
```

<br/>

#### 단계 5. 실행 결과
이 출력은 SATA SSD 파티션(/dev/sdb1)이 ext4 파일 시스템으로 성공적으로 포맷되어 /mnt/sata에 마운트되었음을 확인해 줍니다.
**df -h** 명령은 해당 장치가 이제 인식되어 시스템에서 사용할 수 있음을 보여줍니다.

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
D3-G는 PCIe 슬롯을 통해 NVMe M.2 SSD의 직접 연결을 지원합니다.
<br/>

#### 1단계. SSD 연결
- NVMe SSD (M.2 PCIe): NVMe M.2 SSD를 D3-G의 PCIe 슬롯에 삽입합니다. 

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20D3-G/Software/M.2%20SSD%20connection.png" width="600"></p>
<p align="center"><strong>그림 5.4 D3-G 보드에 NVMe M.2 SSD 연결</strong></p><br/>

#### 2단계. D3-G 부팅
**reboot** 명령을 실행한 후 부팅 로그를 확인하여 PCIe 장치가 시스템에서 인식되는지 검증하십시오.
PCIe 링크가 성공적으로 설정되었음을 나타내는 **telechips-pcie: Link up**과 같은 메시지를 찾으십시오.

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

#### 3단계. SSD 인식 확인
```
root@TOPST:~# lspci
00:00.0 PCI bridge: Synopsys, Inc. Device 8040 (rev 01)
01:00.0 Non-Volatile memory controller: Solid State Storage Technology Corporation Device 1007 (rev 03)
```
**lspci** 명령을 사용할 수 없는 경우 다음 명령을 사용하여 pciutils를 설치하십시오.

```
$ sudo apt-get install pciutils
```

<br/>

#### 4단계. SSD 마운트
```
$ fdisk /dev/nvme0n1
Welcome to fdisk (util-linux 2.37.4).
Changes will remain in memory only, until you decide to write them.
Be careful before using the write command.

Command (m for help): 
```

fdisk 프롬프트에서 다음 키를 순서대로 입력하십시오:

- o — 비어 있는 새 DOS 파티션 테이블 생성 (선택 사항, 기존 테이블 삭제)

- n — 새 파티션 추가

- p — 주 파티션 선택

- 1 — 파티션 번호를 1로 설정

- Enter 키 입력 — 기본 시작 섹터 적용

- Enter 키 입력 — 기본 마지막 섹터 적용 (디스크 전체 사용)

- w — 파티션 테이블을 기록하고 종료합니다

```
$ mkfs.ext4 /dev/nvme0n1p1

$ mkdir -p /mnt/nvme

$ mount /dev/nvme0n1p1 /mnt/nvme
```

<br/>

#### 단계 5. 실행 결과
이 출력은 NVMe SSD 장치(/dev/nvme0n1p1)가 시스템에 의해 정상적으로 감지되어 /mnt/nvme에 마운트되었음을 확인해 줍니다.
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


# 6. 이더넷 연결
---
D3-G는 온보드 J2C 이더넷 포트를 통해 이더넷 연결을 지원합니다. 이를 통해 D3-G는 표준 TCP/IP 프로토콜을 사용하여 로컬 네트워크 또는 인터넷과 통신할 수 있습니다. 이더넷은 원격 접속, 데이터 스트리밍 또는 소프트웨어 업데이트가 필요한 애플리케이션을 배포하는 데 일반적으로 사용됩니다.

<br/><br/><br/>

## 6.1 라우터를 통한 네트워크 연결
---
이 방법은 표준 라우터를 사용하여 D3-G를 로컬 네트워크에 연결합니다. D3-G는 DHCP를 통해 자동으로 IP 주소를 할당받거나 고정 IP 주소로 구성할 수 있습니다.

<br/><br/>

### 6.1.1 네트워크 구성 파일 생성

1. DHCP를 통한 동적 IP
네트워크에서 DHCP 서버(예: 라우터 또는 ICS가 활성화된 Windows PC)를 제공하는 경우 파일을 편집할 필요가 없습니다. 이더넷 케이블을 연결하는 즉시 시스템이 자동으로 IP 주소를 할당받습니다.

케이블을 연결하기만 하면 바로 네트워크를 사용할 수 있습니다. 6.1.3 네트워크 연결 확인 장으로 진행하십시오.

2. 고정 IP 구성
고정 IP 주소를 할당하려는 경우(예: PC에 직접 연결하거나 DHCP 서버를 사용할 수 없는 경우), 동일한 파일을 다음 내용으로 편집하십시오:
```
$ vi /etc/systemd/network/20-wired.network

[Match]
Name=eth0

[Network]
Address=192.168.137.2/24
Gateway=192.168.137.1
DNS=8.8.8.8
```

이 설정은 IP 주소를 192.168.137.2로 지정하고, 192.168.137.1을 게이트웨이(Windows ICS에서 일반적으로 사용됨)로 사용하며, Google DNS를 구성합니다.

<br/><br/>

### 6.1.2 네트워크 서비스 재시작
systemd-networkd 서비스를 재시작하여 새 네트워크 구성을 적용하십시오:

```
sudo systemctl restart systemd-networkd
```

<br/><br/>

### 6.1.3 네트워크 연결 확인
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20D3-G/Software/router%20connection.png"width="500"></p>
<p align="center"><strong>그림 6.1 라우터를 통한 네트워크 연결</strong></p>

Google 공용 DNS 서버에 ping을 보내 인터넷 연결을 테스트하십시오:

```
$ ping 8.8.8.8
PING 8.8.8.8 (8.8.8.8): 56 data bytes
64 bytes from 8.8.8.8: seq=0 ttl=113 time=30.208 ms
64 bytes from 8.8.8.8: seq=1 ttl=113 time=38.143 ms
64 bytes from 8.8.8.8: seq=2 ttl=113 time=30.969 ms
64 bytes from 8.8.8.8: seq=3 ttl=113 time=33.586 ms
 
```

<br/><br/><br/>

## 6.2 호스트 PC와 네트워크 공유
---
Windows 운영 체제에서 제공하는 인터넷 연결 공유(ICS) 기능을 활용하면 라우터를 사용하지 않고도 PC의 인터넷 연결을 D3-G와 공유할 수 있습니다.

<br/><br/>

### 6.2.1 호스트 PC 네트워크 구성
- 제어판 → 네트워크 및 인터넷 → 네트워크 연결 → 이더넷 설정
 
1. 인터넷에 연결된 네트워크 어댑터(예: Wi-Fi)를 찾아 마우스 오른쪽 버튼으로 클릭한 후 **속성**을 선택하십시오.

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20AI-G/Available%20Applications/ethernet1.png" width="600"></p>
<p align="center"><strong>그림 6.2 속성 선택</strong></p><br/>
 
2. 공유 탭을 선택하십시오.

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20AI-G/Available%20Applications/ethernet2.png" width="400"></p>
<p align="center"><strong>그림 6.3 공유 탭 선택</strong></p><br/>

3. "다른 네트워크 사용자가 이 컴퓨터의 인터넷 연결을 통해 연결할 수 있도록 허용" 확인란을 선택하십시오.
 
4. 홈 네트워킹 연결 드롭다운 메뉴에서 D3-G가 연결될 이더넷 어댑터(예: "Ethernet")를 선택합니다.

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20AI-G/Available%20Applications/ethernet3.png" width="400"></p>
<p align="center"><strong>그림 6.4 이더넷 어댑터 선택</strong></p><br/>
 
5. **확인**을 클릭하여 설정을 저장하십시오.

<br/><br/>

### 6.2.2 네트워크 구성 파일 생성 
1. DHCP를 통한 동적 IP
네트워크에서 DHCP 서버(예: 라우터 또는 ICS가 활성화된 Windows PC)를 제공하는 경우 파일을 편집할 필요가 없습니다. 이더넷 케이블을 연결하는 즉시 시스템이 자동으로 IP 주소를 할당받습니다.

케이블을 연결하기만 하면 바로 네트워크를 사용할 수 있습니다. 6.2.4 네트워크 연결 확인 장으로 진행하십시오.

2. 고정 IP 구성
고정 IP 주소를 할당하려는 경우(예: PC에 직접 연결하거나 DHCP 서버를 사용할 수 없는 경우), 동일한 파일을 다음 내용으로 편집하십시오:
```
$ vi /etc/systemd/network/20-wired.network

[Match]
Name=eth0

[Network]
Address=192.168.137.2/24
Gateway=192.168.137.1
DNS=8.8.8.8
```
이 설정은 IP 주소를 192.168.137.2로 지정하고, 192.168.137.1을 게이트웨이(Windows ICS에서 일반적으로 사용됨)로 사용하며, Google DNS를 구성합니다.

<br/><br/>

### 6.2.3 네트워크 서비스 재시작
systemd-networkd 서비스를 재시작하여 새 네트워크 구성을 적용하십시오:

```
sudo systemctl restart systemd-networkd
```

<br/><br/>

### 6.2.4 네트워크 연결 확인
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20D3-G/Software/host%20pc%20ethernet%20connection.png"width="500"></p>
<p align="center"><strong>그림 6.5 호스트 PC와 네트워크 공유</strong></p>
<br/>

Google 공용 DNS 서버에 ping을 보내 인터넷 연결을 테스트하십시오:

```
$ ping 8.8.8.8
PING 8.8.8.8 (8.8.8.8): 56 data bytes
64 bytes from 8.8.8.8: seq=0 ttl=113 time=30.208 ms
64 bytes from 8.8.8.8: seq=1 ttl=113 time=38.143 ms
64 bytes from 8.8.8.8: seq=2 ttl=113 time=30.969 ms
64 bytes from 8.8.8.8: seq=3 ttl=113 time=33.586 ms
```

<br/><br/><br/><br/>

# 7. 40핀 GPIO 헤더
---
D3-G는 40핀 GPIO 헤더를 갖추고 있어 다양한 하드웨어 프로젝트에 유연한 I/O 기능을 제공합니다.
이 헤더는 범용 입출력(GPIO) 동작과 호환되며 센서, LED, 버튼 및 기타 주변 장치를 연결하는 데 사용할 수 있습니다.

각 핀은 구성에 따라 디지털 I/O, PWM, I2C, SPI, UART 등 여러 기능을 지원합니다.

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/d3g/Assets/TOPST%20D3-G/Software/d3-g%20gpio%2040pinmap.png" width="800"></p>
<p align="center"><strong>그림 7.1 D3-G의 40핀 GPIO 헤더 핀맵 </strong></p> <br/>

**참고**: 외부 하드웨어를 연결하기 전에 공식 핀아웃 다이어그램을 참조하여 자세한 핀 기능과 전압 레벨을 확인하십시오.

<br/><br/><br/>

## 7.1 GPIO 디지털 입출력
---
D3-G는 40핀 헤더를 통해 디지털 입력 및 출력(GPIO)을 지원하므로 버튼, LED, 센서와 같은 외부 장치와 상호 작용할 수 있습니다. 

### 7.1.1 LED
---
가장 간단하고 일반적인 GPIO 출력 예제 중 하나는 LED를 제어하는 것입니다.  
이 절에서는 D3-G를 사용하여 LED 센서를 연결하고 사용하는 방법을 설명합니다.

#### 단계 1. 하드웨어 요구 사항
- D3-G 보드 (x1)
- 브레드보드 (x1)
- LED (x1)
- 수-암 점퍼 와이어 (x2)
- DC 5V 전원 어댑터 (x1)
- USB-TTL 시리얼 케이블 (x1)

#### 단계 2. 예제 회로
- LED
    - (+) 핀은 D3-G 보드의 12번 핀에 연결합니다.
    - (-) 핀은 D3-G 보드에서 GND 역할을 하는 14번 핀에 연결합니다.  
    
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20D3-G/Software/led.png"></p>

<p align="center"><strong>그림 7.2 D3-G GPIO LED 회로도 </strong></p> <br/>

##### 단계 2.1 핀 매핑
다음 표는 핀 매핑을 나타냅니다.

<div align="center">
  <p><strong>표 7.1 D3-G LED 핀 매핑</strong></p>
  <table>
      <tr>
          <th colspan="3">핀 이름</th>
          <th>D3-G</th>
          <th>GPIO</th>
      </tr>
      <tr>
          <td colspan="3">LED (+) 핀</td>
          <td>12</td>
          <td>89</td>
      </tr>
      <tr>
          <td colspan="3">LED (-) 핀</td>
          <td>14</td>
          <td>GND</td>
      </tr>
  </table>
</div>

#### 단계 3. 실행 방법
D3-G 보드의 GPIO89에 연결된 LED를 동작시키려면 다음 코드를 실행하십시오:

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

#### 단계 4. 실행 결과
다음 명령으로 코드를 실행하십시오.

```
$ python3 led_test.py
```

이 스크립트는 GPIO89를 디지털 출력으로 설정하고 1초마다 상태를 전환합니다.
실행하면 GPIO89에 연결된 LED가 1초 동안 켜지고 1초 동안 꺼지기를 반복하며 10회 깜박입니다. 10회 반복 후 스크립트가 종료되고 GPIO가 자동으로 unexport됩니다.

스크립트를 조기에 중지하려면 **[Ctrl+C]**를 누르십시오.
두 경우 모두 핀이 올바르게 해제되고 정리됩니다.

**참고**: 이 설정은 LED를 직접 연결하는 것을 전제로 합니다. 안전하고 장기적인 동작을 위해 과도한 전류 소모를 방지하고 GPIO 핀이 손상되지 않도록 LED와 직렬로 전류 제한 저항(예: 220Ω)을 사용하는 것을 강력히 권장합니다.

<br/><br/><br/><br/>

### 7.1.2 버튼
---
푸시 버튼은 GPIO를 통한 디지털 입력 처리를 시연하는 데 일반적으로 사용되는 기본 입력 장치입니다.
이 절에서는 D3-G에서 기본 버튼 모듈을 연결하고 사용하는 방법을 설명합니다.

#### 단계 1. 하드웨어 요구 사항
- D3-G 보드 (x1)
- 브레드보드 (x1)
- 버튼 (x1)
- 수-암 점퍼 와이어 (x2)
- DC 5V 전원 어댑터 (x1)
- USB-TTL 시리얼 케이블 (x1)

#### 단계 2. 예제 회로
- 버튼 스위치
    - 버튼 스위치의 한쪽 다리는 D3-G 보드의 10번 핀에 연결합니다.
    - 버튼 위쪽의 반대편 다리는 3.3V 핀에 연결합니다.

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20D3-G/Software/button_circuit.png"></p> 
<p align="center"><strong>그림 7.3 D3-G GPIO 버튼 회로도</strong></p>

##### 단계 2.1 핀 매핑
다음 표는 핀 매핑을 나타냅니다.

<div align="center">
  <p><strong>표 7.2 D3-G 버튼 핀 매핑</strong></p>
  <table>
      <tr>
          <th colspan="3">핀 이름</th>
          <th>D3-G</th>
          <th>GPIO</th>
      </tr>
      <tr>
          <td colspan="3">버튼의 한쪽 다리 핀</td>
          <td>10</td>
          <td>88</td>
      </tr>
  </table>
</div>

#### 단계 3. 실행 방법
D3-G 보드의 GPIO88에 연결된 버튼 입력을 모니터링하려면 다음 코드를 실행하십시오:

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

#### 단계 4. 실행 결과
다음 명령으로 코드를 실행하십시오.
```
$ python3 test_button.py
```
이 스크립트는 GPIO88을 디지털 입력으로 설정하고 그 값을 실시간으로 지속적으로 모니터링합니다.
실행한 후 GPIO88에 연결된 버튼을 누르면 버튼이 눌렸음을 나타내는 메시지가 출력됩니다.

스크립트를 중지하려면 **[Ctrl+C]**를 누르십시오.
스크립트가 종료되면 GPIO88은 자동으로 unexport되고 정리됩니다.

**참고**: 여기서는 GPIO88을 예로 사용했습니다. 40핀 헤더 핀 배치에 따라 D3-G에서 사용 가능한 GPIO 핀을 사용할 수 있습니다.
공식 핀 배치도를 참조하여 하드웨어 구성에 맞는 GPIO 번호를 선택하십시오.

<br/><br/><br/><br/>

### 7.1.3 터치 센서
---
터치 센서는 GPIO를 통해 사람의 터치를 디지털 입력 신호로 감지하는 데 사용할 수 있습니다.
이 절에서는 D3-G를 사용하여 기본 터치 센서 모듈을 연결하고 입력을 읽는 방법을 설명합니다.

#### 단계 1. 하드웨어 요구 사항
- D3-G 보드 (x1)
- 터치 센서 (x1)
- 암-암 점퍼 와이어 (x3)
- DC 5V 전원 어댑터 (x1)
- USB-TTL 시리얼 케이블 (x1)

#### 단계 2. 예제 회로
- 터치 센서
    - 터치 센서의 SIG 핀은 D3-G 보드의 88번 핀에 연결합니다.
    - 터치 센서의 VCC 핀은 D3-G 보드의 3.3V에 연결합니다.
    - 터치 센서의 GND 핀은 D3-G 보드의 GND에 연결합니다.


<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20D3-G/Software/touch%20circuit.png"></p>
<p align="center"><strong>그림 7.4 D3-G GPIO 터치 센서 회로도</strong></p>

##### 단계 2.1 핀 매핑
다음 표는 핀 매핑을 나타냅니다.

<div align="center">
  <p><strong>표 7.3 D3-G 터치 센서 핀 매핑</strong></p>
  <table>
      <tr>
          <th colspan="3">핀 이름</th>
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

#### 단계 3. 실행 방법
D3-G 보드의 GPIO88에 연결된 터치 센서를 모니터링하려면 다음 코드를 실행하기만 하면 됩니다:
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

#### 단계 4. 실행 결과
다음 명령으로 코드를 실행하십시오.

```
$ python3 touch_test.py
```

이 스크립트는 GPIO88을 디지털 입력으로 설정하고 그 값을 실시간으로 지속적으로 모니터링합니다.

실행한 후 센서를 터치하면 터미널에 다음과 같은 메시지가 출력됩니다:
```
touch detected.
```
센서를 터치하지 않으면 출력은 다음과 같습니다:
```
touch released.
```
스크립트를 중지하려면 **[Ctrl+C]**를 누르십시오.
스크립트가 종료되면 GPIO88은 자동으로 unexport되고 정리됩니다.

**참고**: 여기서는 GPIO88을 예로 사용했습니다. 40핀 헤더 핀 배치에 따라 D3-G에서 사용 가능한 GPIO 핀을 사용할 수 있습니다.
공식 핀 배치도를 참조하여 하드웨어 구성에 맞는 GPIO 번호를 선택하십시오.

<br/><br/><br/><br/>

### 7.1.4 진동 감지 센서
---
진동 센서는 물리적 충격이나 진동을 감지하여 GPIO를 통해 디지털 입력 신호를 출력하는 데 사용할 수 있습니다.
이 절에서는 D3-G를 사용하여 기본 진동 센서 모듈을 연결하고 입력을 감지하는 방법을 설명합니다.

#### 단계 1. 하드웨어 요구 사항
- D3-G 보드 (x1)
- 진동 감지 센서 (x1)
- 암-암 점퍼 와이어 (x4)
- DC 5V 전원 어댑터 (x1)
- USB-TTL 시리얼 케이블 (x1)

#### 단계 2. 예제 회로
- 진동 감지 센서
    - 진동 감지 센서의 VCC 핀은 D3-G 보드의 3.3V 핀에 연결합니다.
    - 진동 감지 센서의 GND 핀은 D3-G 보드의 GND에 연결합니다.
    - 진동 감지 센서의 DO 핀은 D3-G 보드의 88번 핀에 연결합니다.

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20D3-G/Software/vibr%20circuit.png"></p>
<p align="center"><strong>그림 7.5 D3-G GPIO 진동 감지 센서 회로도</strong></p>

##### 단계 2.1 핀 매핑
다음 표는 핀 매핑을 나타냅니다.

<div align="center">
  <p><strong>표 7.4 D3-G 진동 감지 센서의 핀 매핑</strong></p>
  <table>
      <tr>
          <th colspan="3">핀 이름</th>
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

#### 단계 3. 실행 방법
D3-G 보드의 GPIO88에 연결된 진동 센서를 모니터링하려면 다음 코드를 실행하십시오.
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

#### 단계 4. 실행 결과
다음 명령으로 코드를 실행하십시오.

```
$ python3 vibration_test.py
```

이 스크립트는 GPIO88을 디지털 입력으로 설정하고 그 값을 실시간으로 지속적으로 모니터링합니다.
실행하면 센서가 감지한 진동이나 충격에 따라 터미널에 다음과 같은 메시지가 출력됩니다.
```
vibration detected.
```
진동이 없으면 출력은 다음과 같습니다.
```
no vibration detected.
```
스크립트를 중지하려면 **[Ctrl+C]**를 누르십시오.
종료 시 GPIO88은 자동으로 unexport되어 정리됩니다.

**참고**: 여기서는 GPIO88을 예로 사용합니다. 센서 배선과 헤더 배치에 따라 사용 가능한 다른 GPIO 핀을 사용할 수 있습니다. GPIO 번호를 선택하기 전에 D3-G 핀맵을 참조하십시오.

<br/><br/><br/><br/>

### 7.1.5 적외선 센서 (SZH-SSBH-002)
---
적외선 센서는 반사된 적외선을 감지하여 근처의 장애물을 검출하고 GPIO를 통해 디지털 신호를 출력하는 데 사용할 수 있습니다.
이 절에서는 D3-G를 사용하여 SZH-SSBH-002 적외선 센서를 연결하고 입력을 읽는 방법을 설명합니다.

#### 단계 1. 하드웨어 요구 사항
- D3-G 보드 (x1)
- 브레드보드 (x1)
- 적외선 센서 (x1)
- 수-암 점퍼 와이어 (x5)
- DC 5V 전원 어댑터 (x1)
- USB-TTL 시리얼 케이블 (x1)

#### 단계 2. 예제 회로
- 적외선 센서
    - 적외선 센서의 VCC 핀은 D3-G 보드의 3.3V 핀에 연결합니다.
    - 적외선 센서의 GND 핀은 D3-G 보드의 GND에 연결합니다.
    - 적외선 센서의 OUT 핀은 D3-G 보드의 89번 핀에 연결합니다.


<p align="center">
  <img src="https://raw.githubusercontent.com/topst-development/Documentation/d3g/Assets/TOPST%20D3-G/Software/szh-ssbh-002_circuit.png">
</p> 
<p align="center"><strong>그림 7.6 IR 센서 실험 회로</strong></p>

##### 단계 2.1 핀 매핑
다음 표는 핀 매핑을 나타냅니다.

<div align="center">
  <p><strong>표 7.5 D3-G IR 센서의 핀 매핑</strong></p>
  <table>
      <tr>
          <th colspan="3">핀 이름</th>
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

#### 단계 3. 실행 방법
D3-G 보드의 GPIO89에 연결된 IR 센서를 모니터링하려면 다음 코드를 실행하십시오.

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

#### 단계 4. 실행 결과
다음 명령으로 코드를 실행하십시오.
```
$ python3 ir_test.py
```
이 스크립트는 GPIO89를 디지털 입력으로 설정하고 상태를 지속적으로 모니터링하여 장애물을 감지합니다.
IR 센서 앞에서 물체가 감지되면 터미널에 다음이 표시됩니다.
```
obstacle detected.
```
물체가 감지되지 않으면 다음이 표시됩니다.
```
no obstacle detected.
```
스크립트를 중지하려면 **[Ctrl+C]**를 누르십시오.
스크립트를 종료하면 GPIO89는 자동으로 unexport되어 정리됩니다.

**참고**: 이 스크립트에서는 GPIO89를 예로 사용합니다.
D3-G의 40핀 헤더에 따라 사용 가능한 GPIO 핀을 사용할 수 있습니다. 정확한 핀 선택을 위해 공식 핀맵 도면을 참조하십시오.

<br/><br/><br/><br/>

### 7.1.6 광저항 센서 (SZH-SSBH-011)
---
광저항 센서는 주변 조도를 감지하여 광량이 특정 임계값을 넘을 때 GPIO를 통해 디지털 신호를 출력하는 데 사용할 수 있습니다.
이 절에서는 D3-G를 사용하여 SZH-SSBH-011 광저항 센서를 연결하고 입력을 읽는 방법을 설명합니다.

#### 단계 1. 하드웨어 요구 사항
- D3-G 보드 (x1)
- 광저항 모듈 (SZH-SSBH-011) (x1)
- LED (x1)
- 220Ω 저항 (x1)
- 브레드보드 (x1)
- 수-암 점퍼 와이어 (x7)
- DC 5V 전원 어댑터 (x1)
- USB-TTL 시리얼 케이블 (x1)

#### 단계 2. 예제 회로
- 광저항 센서 (SZH-SSBH-011)
    - 광저항 센서의 VCC 핀은 D3-G 보드의 3.3V 핀에 연결합니다.
    - 광저항 센서의 GND 핀은 D3-G 보드의 GND에 연결합니다.
    - 광저항 센서의 DO 핀은 D3-G 보드의 89번 핀에 연결합니다.
- LED
    - LED의 (+) 핀은 D3-G 보드의 GND에 연결합니다.
    - LED의 (-) 핀은 D3-G 보드의 83번 핀에 연결합니다.

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20D3-G/Software/circuit.png"></p>
<p align="center"><strong>그림 7.7 광저항 센서 실험 회로</strong></p>

##### 단계 2.1 핀 매핑
다음 표는 핀 매핑을 나타냅니다.

<div align="center">
  <p><strong>표 7.6 D3-G 광저항 센서의 핀 매핑</strong></p>
  <table>
      <tr>
          <th colspan="3">핀 이름</th>
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
  <p><strong>표 7.7 D3-G LED의 핀 매핑</strong></p>
  <table>
      <tr>
          <th colspan="3">핀 이름</th>
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

### 3단계. 실행 방법
CDS 센서로 밝기를 모니터링하고 그에 따라 LED를 제어하려면 다음 Python 스크립트를 실행하십시오.

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

### 4단계. 실행 결과
다음 명령으로 코드를 실행하십시오.
```
$ python3 CDS_test.py
```
이 스크립트는 GPIO89를 광저항 센서용 입력으로, GPIO83을 LED용 출력으로 설정합니다.
주변 광이 감지되면 터미널에 다음이 출력됩니다.
```
sensor value: 0
brightness detected. Turning on the LED.
```
그리고 LED가 켜집니다.
빛이 감지되지 않으면 다음이 출력됩니다.
```
sensor value: 1
no brightness detected. Turning off the LED.
```
그리고 LED가 꺼집니다.
스크립트를 중지하려면 **[Ctrl+C]**를 누르십시오.
스크립트를 종료하면 두 GPIO 핀 모두 자동으로 unexport되어 정리됩니다.

**참고**: 이 예제에서는 GPIO83과 GPIO89를 사용합니다. D3-G의 40핀 헤더 배치에 따라 사용 가능한 GPIO 핀을 사용할 수 있습니다. 정확한 핀 선택을 위해 공식 핀맵 도면을 참조하십시오.

<br/><br/><br/><br/>

### 7.1.7 대기 오염 감지 센서
---
대기 오염 감지 센서는 환경 내 유해 가스나 미세먼지의 존재를 모니터링하고 GPIO를 통해 디지털 신호를 출력하는 데 사용할 수 있습니다.
이 절에서는 D3-G를 사용하여 대기 오염 감지 센서를 연결하고 입력을 읽는 방법을 설명합니다.

#### 단계 1. 하드웨어 요구 사항
- D3-G 보드 (x1)
- 대기 오염(가스) 감지 센서 모듈 (x1)
- 브레드보드 (x1)
- 수-암 점퍼 와이어 (x3)
- DC 5V 전원 어댑터 (x1)
- USB-TTL 시리얼 케이블 (x1)

#### 단계 2. 예제 회로
- 대기 오염 감지 센서
    - 대기 오염 감지 센서의 VCC 핀은 D3-G 보드의 3.3V 핀에 연결합니다.
    - 대기 오염 감지 센서의 GND 핀은 D3-G 보드의 GND에 연결합니다.
    - 대기 오염 감지 센서의 DO 핀은 D3-G 보드의 88번 핀에 연결합니다.

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20D3-G/Software/gas%20circuit.png"></p>
<p align="center"><strong>그림 7.8 대기 오염 감지 센서 실험 회로</strong></p>

##### 단계 2.1 핀 매핑
다음 표는 핀 매핑을 나타냅니다.

<div align="center">
  <p><strong>표 7.8 D3-G 대기 오염 감지 센서의 핀 매핑</strong></p>
  <table>
      <tr>
          <th colspan="3">핀 이름</th>
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

#### 3단계. 실행 방법
GPIO88 핀을 사용하여 가스 감지를 모니터링하려면 다음 Python 스크립트를 실행하십시오.

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

#### 단계 4. 실행 결과
다음 명령으로 코드를 실행하십시오.
```
$ python3 gas_sensor_test.py
```
이 스크립트는 GPIO88을 디지털 입력으로 설정하고 가스 감지 상태를 지속적으로 모니터링합니다.
가스 농도가 센서의 임계값에 도달하면 터미널에 다음이 표시됩니다.
```
gas detected.
```
가스가 감지되지 않으면 터미널에 다음이 표시됩니다.
```
no gas detected.
```
스크립트를 중지하려면 **[Ctrl+C]**를 누르십시오.
스크립트를 종료하면 GPIO88은 자동으로 unexport되어 정리됩니다.

**참고**: 여기서는 GPIO88을 예로 사용합니다. D3-G의 40핀 헤더 배치에 따라 사용 가능한 GPIO 핀을 사용할 수 있습니다. 정확한 핀 선택을 위해 공식 핀맵 도면을 참조하십시오.

<br/><br/><br/><br/>

### 7.1.8 초음파 센서
---
초음파 센서는 초음파를 발신하고 반사된 신호를 수신하여 주변 물체까지의 거리를 측정한 후, GPIO를 통해 디지털(또는 펄스 기반) 신호를 출력하는 데 사용할 수 있습니다.
이 절에서는 D3-G를 사용하여 초음파 센서를 연결하고 입력을 읽는 방법을 설명합니다.

#### 단계 1. 하드웨어 요구 사항
- D3-G 보드 (x1)
- 초음파 센서 (x1)
- 암-암 점퍼 와이어 (x4)
- DC 5V 전원 어댑터 (x1)
- USB-TTL 시리얼 케이블 (x1)

#### 단계 2. 예제 회로
- 초음파 센서
    - 초음파 센서의 VCC 핀은 D3-G 보드의 5V 핀에 연결합니다.
    - 초음파 센서의 GND 핀은 D3-G 보드의 GND에 연결합니다.
    - 초음파 센서의 TRIG 핀은 D3-G 보드의 82번 핀에 연결합니다.
    - 초음파 센서의 ECHO 핀은 D3-G 보드의 88번 핀에 연결합니다.

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20D3-G/Software/ultra%20circuit.png"></p>
<p align="center"><strong>그림 7.9 초음파 센서 실험 회로</strong></p>

##### 단계 2.1 핀 매핑
다음 표는 핀 매핑을 나타냅니다.

<div align="center">
  <p><strong>표 7.9 D3-G 초음파 센서의 핀 매핑</strong></p>
  <table>
      <tr>
          <th colspan="3">핀 이름</th>
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

#### 3단계. 실행 방법
초음파 센서를 사용하여 거리를 측정하려면 다음 Python 스크립트를 실행하십시오.
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

#### 단계 4. 실행 결과
다음 명령으로 코드를 실행하십시오.
```
$ python3 ultrasonic_sensor_test.py
```
이 스크립트는 초음파 펄스를 발생시키기 위해 GPIO82를 디지털 출력으로, 에코를 수신하기 위해 GPIO88을 디지털 입력으로 설정합니다.
스크립트를 실행하면 센서 앞의 가장 가까운 물체까지의 거리가 1초마다 출력됩니다. 예를 들면 다음과 같습니다.
```
Distance: 23.45 cm
Distance: 24.12 cm
...
```
스크립트를 중지하려면 **[Ctrl+C]**를 누르십시오.
스크립트를 종료하면 GPIO82와 GPIO88은 자동으로 unexport되어 정리됩니다.

**참고**: 여기서는 GPIO82와 GPIO88을 예로 사용합니다. D3-G의 40핀 헤더 배치에 따라 사용 가능한 GPIO 핀을 사용할 수 있습니다. 정확한 핀 선택을 위해 공식 핀맵 도면을 참조하십시오. 또한 ECHO 핀의 전압 레벨이 D3-G에 안전한지 확인하십시오(일부 모듈은 5V를 출력하므로 전압 분배기나 레벨 시프터가 필요할 수 있습니다).

<br/><br/><br/><br/>

## 7.2 I2C
---
D3-G는 40핀 GPIO 헤더를 통해 I2C 통신을 제공하므로 센서, 디스플레이, 확장 모듈 등 다양한 주변 장치와 인터페이스할 수 있습니다.
I2C(Inter-integrated Circuit)는 데이터 라인(SDA)과 클록 라인(SCL)으로 구성된 2선식 통신 프로토콜로, 여러 장치가 공유 버스를 통해 통신할 수 있게 합니다.

I2C 통신은 마스터-슬레이브 구조를 따르며, 하나의 마스터 장치가 통신을 제어하고 동일한 버스에 최대 127개의 슬레이브 장치를 연결할 수 있습니다.
SDA 라인은 데이터 송신과 수신에 모두 사용되며, SCL 라인은 데이터 전송 타이밍을 동기화합니다. 이러한 동기식 통신 방식을 통해 장치들은 클록에 기반하여 정렬된 방식으로 정보를 교환할 수 있습니다.

<br/><br/><br/><br/>

### 7.2.1 1602A LCD 디스플레이
---
1602A LCD는 임베디드 시스템에서 일반적으로 사용되는 문자 표시 모듈입니다.
D3-G에서는 LCD의 SDA 및 SCL 라인을 I2C용으로 설정된 GPIO 핀에 연결할 수 있습니다. 연결한 후에는 Linux I2C 도구나 사용자 정의 소프트웨어를 사용하여 LCD를 제어할 수 있습니다.

#### 단계 1. 하드웨어 요구 사항
- D3-G 보드 (x1)
- 1602A I2C LCD 모듈 (x1)
- 암-암 점퍼 와이어 (x4)
- DC 5V 전원 어댑터 (x1)
- USB to TTL 시리얼 케이블 (x1)  

LCD 모듈에 I2C 백팩이 있는지 확인하십시오

#### 단계 2. 예제 회로
- I2C LCD 모듈
    - I2C LCD 모듈의 GND 핀은 D3-G 보드의 GND 핀에 연결합니다.
    - I2C LCD 모듈의 VCC 핀은 D3-G 보드의 5V에 연결합니다.
    - I2C LCD 모듈의 SDA 핀은 D3-G 보드의 82번 핀에 연결합니다.
    - I2C LCD 모듈의 SCL 핀은 D3-G 보드의 81번 핀에 연결합니다.

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20D3-G/Software/lcd_circuit.png"></p>
<p align="center"><strong>그림 7.10 D3-G I2C LCD 모듈 회로도  </strong></p>

##### 단계 2.1 핀 매핑
다음 표는 핀 매핑을 나타냅니다.

<div align="center">
  <p><strong>표 7.10 D3-G I2C LCD 모듈의 핀 매핑</strong></p>
  <table>
      <tr>
          <th colspan="3">핀 이름</th>
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

#### 단계 3. 실행 방법
필요한 Python 라이브러리를 먼저 설치합니다:
```
$ pip install RPLCD smbus2
```
그런 다음 아래 Python 코드를 사용하여 LCD에 텍스트를 출력합니다:
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

#### 단계 4. 실행 결과
다음 명령으로 코드를 실행하십시오.
```
$ python3 lcd_test.py
```
이 스크립트는 RPLCD 라이브러리를 사용하여 I2C 기반 1602A LCD를 초기화하고 사용자가 입력한 텍스트를 화면에 표시합니다.
스크립트를 실행하면 문자열을 입력하라는 메시지가 표시됩니다. 입력한 텍스트는 LCD에 4초 동안 표시된 후 지워집니다. 예를 들면 다음과 같습니다:
```
Enter text to display on LCD: Hello D3-G!
```
LCD에 다음이 표시됩니다:
```
Hello D3-G!
```
그리고 4초 후에 지워집니다.

스크립트를 중지하려면 **[Ctrl+C]**를 누르십시오.

**참고** : D3-G에서는 기본적으로 GPIO82와 GPIO81이 I2C용으로 사용됩니다.
I2C 주소(0x27)가 사용 중인 LCD 모듈과 일치하는지 확인하십시오. 필요한 경우 **i2cdetect -y 3** 명령으로 I2C 장치를 검색하십시오.

<br/><br/><br/><br/>

## 7.3 SPI
---
D3-G는 40핀 GPIO 헤더를 통해 Serial Peripheral Interface(SPI) 통신을 지원하므로 외부 장치와 D3-G 간에 데이터를 교환할 수 있습니다.

SPI는 전이중 통신을 지원하는 동기식 직렬 통신 프로토콜로, 데이터를 동시에 송수신할 수 있습니다. Master Out Slave In(MOSI), Master In Slave Out(MISO), Serial Clock(SCLK), Chip Select(CS)의 네 가지 주요 신호선을 사용합니다.

여러 장치가 공용 신호선을 사용하는 I2C와 달리 SPI는 각 슬레이브 장치마다 전용 CS 신호선이 필요합니다. 이러한 일대다 구조 덕분에 SPI는 속도가 빠르고 구현이 간단하지만, 여러 장치를 연결하는 경우 물리적인 배선이 더 많이 필요할 수 있습니다.

<br/><br/><br/><br/>

### 7.3.1 도트 매트릭스
---
8x8 도트 매트릭스 디스플레이는 임베디드 시스템에서 간단한 텍스트나 패턴을 출력하는 데 일반적으로 사용됩니다. D3-G에서는 MAX7219와 같은 드라이버 칩을 사용하여 SPI를 통해 도트 매트릭스 모듈을 제어할 수 있습니다.

MAX7219는 행과 열 스캔을 내부적으로 처리하므로 마이크로컨트롤러는 MOSI(DIN), SCLK, CS(LOAD)의 몇 가지 SPI 신호만으로 전체 디스플레이를 제어할 수 있습니다. 연결이 완료되면 사용자 정의 스크립트나 라이브러리를 통해 SPI 통신으로 디스플레이를 제어할 수 있습니다.

#### 단계 1. 하드웨어 요구 사항
- D3-G 보드 (x1)
- 도트 매트릭스 (x1)
- 수-암 점퍼 와이어 (x4)
- DC 5V 전원 어댑터 (x1)
- USB-TTL 시리얼 케이블 (x1)

#### 단계 2. 예제 회로
- 도트 매트릭스
    - 도트 매트릭스의 VCC 핀은 D3-G 보드의 5V 핀에 연결됩니다.
    - 도트 매트릭스의 GND 핀은 D3-G 보드의 GND 핀에 연결됩니다.
    - 도트 매트릭스의 DIN 핀은 D3-G 보드의 120번 핀에 연결됩니다.
    - 도트 매트릭스의 CS 핀은 D3-G 보드의 119번 핀에 연결됩니다.
    - 도트 매트릭스의 CLK 핀은 D3-G 보드의 118번 핀에 연결됩니다.

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20D3-G/Software/dot%20circuit.png"></p>
<p align="center"><strong>그림 7.11 D3-G 도트 매트릭스 모듈 회로도  </strong></p>

##### 단계 2.1 핀 매핑
다음 표는 핀 매핑을 나타냅니다.
<div align="center">
  <p><strong>표 7.11 D3-G 도트 매트릭스 핀 매핑</strong></p>
  <table>
      <tr>
          <th colspan="3">핀 이름</th>
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

#### 단계 3. 실행 방법
다음 Python 스크립트는 저수준 fcntl 호출을 사용하여 /dev/spidev3.0을 통해 MAX7219를 직접 제어하는 방법을 보여 줍니다. 이 방법은 외부 SPI 라이브러리가 없는 장치에 적합합니다:
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

#### 단계 4. 실행 결과
다음 명령으로 코드를 실행하십시오.
```
$ python3 dot_matrix_test.py
```
이 스크립트는 SPI로 연결된 MAX7219 도트 매트릭스 디스플레이를 초기화하고 값을 입력하라는 메시지를 표시합니다. 입력값에 따라 8x8 LED 매트릭스에 특정 패턴이 표시됩니다.

스크립트를 실행하면 다음이 표시됩니다:
```
Enter a number, an uppercase letter (0-9, A-Z), 'Smile', 'Dance', 'Angry', 'Good', 'Nice', 'Emotion':
```
예:
- A를 입력하면 문자 A가 표시됩니다.
- Smile을 입력하면 웃는 얼굴 패턴이 표시됩니다.
- Dance를 입력하면 번갈아 나타나는 댄스 애니메이션이 실행됩니다.
- Nice를 입력하면 N-I-C-E 문자가 순서대로 애니메이션됩니다.

스크립트를 중지하려면 **[Ctrl+C]**를 누르십시오.
종료 시 SPI 장치가 안전하게 닫히고 LED 매트릭스 업데이트가 중지됩니다.

**참고**: /dev/spidev3.0이 존재하는지, 배선이 핀 매핑 표와 일치하는지 확인하십시오. 또한 MAX7219 모듈에는 안정적인 5V 전원을 공급하십시오.

<br/><br/><br/><br/>

## 7.4 PWM
---
Pulse Width Modulation(PWM)은 펄스 신호의 폭을 변화시켜 LED, 모터, 부저와 같은 장치를 제어하는 데 사용됩니다. D3-G는 Linux의 sysfs 인터페이스를 통해 PWM을 지원합니다.

### 7.4.1 LED 밝기 제어
---
이 예제에서는 D3-G에서 PWM을 사용하여 LED의 밝기를 제어하는 방법을 설명합니다.

#### 단계 1. 하드웨어 요구 사항
- D3-G 보드 (x1)
- LED (x1)
- 수-암 점퍼 와이어 (x2)
- 브레드보드
- DC 5V 전원 어댑터 (x1)
- USB-TTL 시리얼 케이블 (x1)

#### 단계 2. 예제 회로
- LED
    - LED의 (+) 핀은 D3-G 보드의 89번 핀에 연결됩니다.
    - LED의 (-) 핀은 D3-G 보드의 GND 핀에 연결됩니다.

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20D3-G/Software/led.png"></p>
<p align="center"><strong>그림 7.12 D3-G LED 회로도  </strong></p>

##### 단계 2.1 핀 매핑
다음 표는 핀 매핑을 나타냅니다.

<div align="center">
  <p><strong>표 7.12 D3-G LED 핀 매핑</strong></p>
  <table>
      <tr>
          <th colspan="3">핀 이름</th>
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

#### 단계 3. 실행 방법
D3-G 보드의 GPIO89에 연결된 LED(PWM)를 동작시키려면 다음 코드를 실행하십시오:
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

#### 단계 4. 실행 결과
다음 명령으로 코드를 실행하십시오.
```
$ python3 led_pwm.py
```
이 스크립트는 LED 핀에서 PWM을 초기화하고 LED 밝기를 지속적으로 밝아졌다 어두워지도록 조절합니다.

스크립트를 실행하면 다음과 같은 출력이 표시됩니다:
```
Starting LED PWM control (press Ctrl+C to stop)
```
LED가 점차 밝아졌다가 어두워지는 동작을 반복하여 "숨쉬는" 효과를 냅니다.

스크립트를 중지하려면 **[Ctrl+C]**를 누르십시오.

**참고**: PWM 채널이 이미 사용 중이지 않은지, 선택한 GPIO에서 D3-G가 하드웨어 PWM을 지원하는지 확인하십시오. PWM이 동작하지 않으면 /sys/class/pwm/의 export, period, duty_cycle 설정을 확인하십시오.

<br/><br/><br/><br/>

### 7.4.2 미니 서보 모터
---
미니 서보 모터는 GPIO를 통한 Pulse Width Modulation(PWM) 신호를 기반으로 정밀한 각도 이동을 제어하는 데 사용할 수 있습니다.
이 절에서는 D3-G를 사용하여 미니 서보 모터를 연결하고 제어하는 방법을 설명합니다.

#### 단계 1. 하드웨어 요구 사항
- D3-G 보드 (x1)
- 서보 모터 (x1)
- 수-암 점퍼 와이어 (x3)
- DC 5V 전원 어댑터 (x1)
- USB-TTL 시리얼 케이블 (x1)

#### 단계 2. 예제 회로
- 서보 모터
    - 서보 모터의 VCC 핀은 D3-G 보드의 5V에 연결됩니다.
    - 서보 모터의 GND 핀은 D3-G 보드의 GND에 연결됩니다.
    - 서보 모터의 SIG 핀은 D3-G 보드의 89번 핀에 연결됩니다.

<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20D3-G/Software/motor_circuit.png"p>
<p align="center"><strong>그림 7.13 D3-G 서보 모터 회로도  </strong></p>

##### 단계 2.1 핀 매핑
다음 표는 핀 매핑을 나타냅니다.

<div align="center">
  <p><strong>표 7.13 D3-G 서보 모터 핀 매핑</strong></p>
  <table>
      <tr>
          <th colspan="3">핀 이름</th>
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

#### 단계 3. 실행 방법
다음 Python 스크립트는 D3-G에서 sysfs 인터페이스를 통해 PWM으로 미니 서보 모터를 직접 제어하는 방법을 보여 줍니다. 이 방법은 외부 라이브러리가 필요 없으며 각도 기반 위치 제어를 세밀하게 수행할 수 있습니다.
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

#### 단계 4. 실행 결과
다음 명령으로 코드를 실행하십시오.
```
$ python3 motor_test.py
```
이 스크립트는 목표 각도에 따라 듀티 사이클을 조정하여 PWM으로 미니 서보 모터를 제어합니다.
실행하면 다음과 같은 입력 메시지가 표시됩니다:
```
Enter 1 (CW) or 0 (CCW), q to quit:
```
1을 입력하면 서보가 시계 방향으로 180°까지 회전하고, 0을 입력하면 반시계 방향으로 0°까지 회전합니다. 필요한 만큼 반복할 수 있습니다.

스크립트를 중지하려면 **[q]**를 입력하거나 **[Ctrl+C]**를 누르십시오. 그러면 스크립트가 PWM 채널을 비활성화하고 unexport합니다.

**참고**: 안전한 동작을 위해 서보 모터가 50 Hz PWM 신호를 지원하고 1 ms~2 ms 듀티 펄스 범위에서 동작하는지 확인하십시오.
