---
title: TOPST Imager 사용자 가이드
description: Windows 또는 Linux에서 TOPST 보드에 운영체제 이미지를 설치하는 방법을 안내합니다.
---

# TOPST Imager 사용자 가이드

TOPST Imager는 TOPST 보드에 운영체제 또는 펌웨어를 설치하는 애플리케이션입니다.
컴퓨터나 전자 기기에 익숙하지 않아도 됩니다. 이 가이드와 앱에 표시되는 안내를 보며 천천히 한 단계씩 진행하세요.

> **중요:** 플래싱하면 보드의 eMMC에 저장된 모든 데이터가 삭제될 수 있습니다. 시작하기 전에 필요한 파일을 백업하세요.

## 1. 알아두면 좋은 용어

| 앱에 표시되는 용어 | 쉬운 설명 |
| --- | --- |
| Board | 운영체제를 설치할 TOPST 기기입니다. |
| Image | 보드에 설치할 운영체제 파일입니다. |
| Flashing | 이미지 파일을 보드에 설치하는 과정입니다. |
| Boot mode | 컴퓨터에서 보드에 이미지를 설치할 수 있는 특수 상태입니다. |
| FWDN | TOPST 보드에 이미지를 설치하는 내부 도구입니다. 직접 실행할 필요는 없습니다. |
| COM port | USB로 연결된 보드를 컴퓨터에서 식별하는 이름입니다. |
| eMMC | 보드에 내장된 저장장치입니다. |

## 2. 지원 보드와 이미지 파일

| 보드 | 사용자 이미지 형식 | 필요한 연결 |
| --- | --- | --- |
| TOPST D3-G | `.fai` | FWDN USB Type-C 데이터 케이블 |
| TOPST AI-G | `.fai` | FWDN USB Type-C 데이터 케이블과 Ethernet 케이블 |
| TOPST VCP-G | `.rom` | FWDN USB Type-C 데이터 케이블 |

> 충전 전용 USB 케이블은 사용할 수 없습니다. **데이터 전송을 지원하는 USB Type-C 케이블**을 사용하세요.

## 3. 시작 전 준비

- 플래싱할 TOPST 보드와 전원 어댑터
- 데이터 전송을 지원하는 USB Type-C 케이블
- 인터넷에 연결된 컴퓨터
- AI-G를 사용하는 경우 Ethernet 케이블
- 공식 이미지 다운로드 및 압축 해제에 필요한 컴퓨터 저장 공간
- 보드에 저장된 중요한 데이터의 백업

플래싱 중에는 보드 전원을 끄거나 USB/Ethernet 케이블을 분리하지 마세요. TOPST Imager를 종료하거나 컴퓨터를 끄거나 절전 모드로 전환하지 마세요.

## 4. 기본 진행 순서

Windows와 Linux의 기본 절차는 같습니다.

1. TOPST Imager를 실행합니다.
2. 사용할 보드를 선택합니다.
3. 운영체제 또는 **Custom Image**를 선택합니다.
4. 설치할 버전을 선택합니다.
5. 앱의 연결 및 부트 모드 안내를 따릅니다.
6. 플래싱을 시작합니다.
7. **Complete** 화면이 나타날 때까지 기다립니다.

항목을 한 번 클릭한 다음 **Next**를 선택하거나, 항목을 두 번 클릭하여 다음 화면으로 이동할 수 있습니다.

---

# Windows 사용 방법

## 5. Windows에 TOPST Imager 설치

### 5.1 지원 환경

- Windows 10 64비트 이상
- Windows 11 64비트

### 5.2 앱 설치

1. TOPST 공식 웹사이트에서 Windows용 `TOPST Imager.exe`를 다운로드합니다.
2. 다운로드한 파일을 두 번 클릭합니다.
3. 사용권 계약을 읽고 동의합니다.
4. 필요하면 바탕 화면 바로가기 옵션을 선택합니다.
5. **Install**을 선택합니다.
6. 설치가 완료되면 **Launch TOPST Imager**를 선택하고 설치 프로그램을 종료합니다.

Windows 보호 메시지가 나타나면 설치 파일이 TOPST 공식 웹사이트에서 제공된 것인지 먼저 확인하세요. 출처를 확인할 수 없다면 실행하지 마세요.

기본 설치 경로:

```text
%LOCALAPPDATA%\Programs\TOPST Imager
```

## 6. 언어와 화면 테마

1. 창 왼쪽 아래의 **App Options**를 선택합니다.
2. 사용할 언어를 선택합니다.
3. **Save**를 선택합니다.

> 스크린샷의 빨간 상자와 숫자는 설명을 위해 추가한 것으로 실제 앱에는 표시되지 않습니다.

![TOPST Imager의 언어 및 지원 옵션 선택](https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/Quick%20Guide/TOPST%20Imager%20App%20Options.png)

1. **Language:** 사용할 언어를 선택합니다.
2. **Ask the Community:** 도움이 필요하면 TOPST 커뮤니티를 엽니다.
3. **Save:** 선택한 언어를 적용합니다.

한국어, 영어, 일본어, 중국어 간체, 중국어 번체, 태국어, 독일어를 지원합니다. 밝은 테마와 어두운 테마는 Windows 시스템 설정을 자동으로 따릅니다.

## 7. 공식 이미지 설치

### 7.1 보드 선택

1. 보드 그림과 이름을 확인합니다.
2. 사용할 보드를 한 번 클릭합니다.
3. 선택한 항목의 색상이 바뀌었는지 확인합니다.
4. **Next**를 선택합니다.

![TOPST Imager에서 D3-G 보드와 Next 버튼 선택](https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/Quick%20Guide/TOPST%20Imager%20Board%20Selection.png)

1. 사용할 **보드 항목**을 선택합니다.
2. 선택 상태를 확인하고 **Next**를 선택합니다.

잘못 선택했다면 **Back**을 선택하여 다시 고르세요.

### 7.2 운영체제와 버전 선택

1. 설치할 운영체제를 선택하고 **Next**를 선택합니다.
2. 설치할 버전을 선택합니다.
3. 출시일과 파일 크기를 확인합니다.

![공식 운영체제 또는 사용자 이미지 선택](https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/Quick%20Guide/TOPST%20Imager%20OS%20Selection.png)

1. 공식 이미지를 사용하려면 원하는 **운영체제**를 선택합니다.
2. 컴퓨터에 저장된 파일을 사용하려면 **Use Custom Image**를 선택합니다.
3. 선택을 확인하고 **Next**를 선택합니다.

![운영체제 버전과 Flashing 버튼 선택](https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/Quick%20Guide/TOPST%20Imager%20Version%20Selection.png)

1. 원하는 **버전**을 선택하고 다운로드 크기와 출시일을 확인합니다.
2. 선택이 맞으면 **Flashing**을 선택합니다.

- **Download size:** 인터넷에서 다운로드할 압축 파일의 크기입니다.
- **Extracted size:** 압축 해제 후 컴퓨터에서 필요한 예상 저장 공간입니다.

반드시 최신 버전을 사용할 필요는 없습니다. 별도 안내가 없다면 권장 버전 또는 최신 안정 버전을 선택하세요.

### 7.3 삭제 경고 확인

플래싱 전 보드 eMMC의 내용이 삭제될 수 있다는 경고가 표시됩니다.

1. 선택한 보드와 이미지를 다시 확인합니다.
2. 보드에 필요한 데이터가 남아 있지 않은지 확인합니다.
3. 준비되면 확인 버튼을 선택합니다.

![Cancel 및 Confirm 버튼이 있는 eMMC 삭제 경고](https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/Quick%20Guide/TOPST%20Imager%20eMMC%20Erase%20Warning.png)

1. 준비가 되지 않았거나 선택을 다시 확인하려면 **Cancel**을 선택합니다.
2. eMMC 내용이 삭제될 수 있음을 이해한 후에만 **Confirm**을 선택합니다.

확신이 없다면 **Cancel**을 선택하세요. 이 단계에서 취소해도 보드는 삭제되지 않습니다.

## 8. D3-G 플래싱

### 8.1 1단계: 드라이버 설치

1. **Install Driver**를 선택합니다.
2. Windows에서 관리자 권한을 요청하면 내용을 확인하고 **Yes**를 선택합니다.
3. VTC 드라이버 설치 프로그램의 안내를 끝까지 따릅니다.
4. TOPST Imager로 돌아옵니다.
5. **Driver Installation Complete**를 선택합니다.

![D3-G VTC 드라이버 설치 안내](https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/Quick%20Guide/TOPST%20Imager%20D3-G%20Driver%20Installation.png)

1. 먼저 **Install Driver**를 선택하여 설치 프로그램을 실행합니다.
2. 모든 설치 단계를 마친 다음 **Driver Installation Complete**를 선택합니다.

일반적으로 컴퓨터마다 한 번만 설치하면 됩니다.

### 8.2 2단계: 부트 모드 진입 및 보드 감지

화면의 보드 그림과 깜박이는 표시를 보면서 진행하세요.

1. 보드의 **BOOT 버튼을 누릅니다.**
2. BOOT 버튼을 계속 누르고 있습니다.
3. **RESET 버튼을 눌렀다 놓습니다.**
4. BOOT 버튼을 놓습니다.
5. USB Type-C 케이블이 컴퓨터와 보드에 단단히 연결되었는지 확인합니다.
6. 앱에서 보드를 감지하는지 확인합니다.

![D3-G 부트 모드 및 보드 감지 화면](https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/Quick%20Guide/TOPST%20Imager%20D3-G%20Boot%20Mode.png)

1. 보드 그림과 깜박이는 표시를 보며 부트 모드 순서를 따릅니다.
2. 연결을 변경했다면 **Check Again**을 선택합니다.
3. 보드가 감지되면 **Continue Flashing**을 사용할 수 있습니다.

Windows 장치 관리자에서 `Telechips TCCxxxx VTC USB Driver`와 비슷한 이름으로 표시될 수 있습니다.

### 8.3 3단계: 이미지 플래싱

1. **Start Flashing**을 선택합니다.
2. 다운로드, 압축 해제, 플래싱 진행 상황을 확인합니다.
3. 완료 화면이 나타날 때까지 기다립니다.

## 9. AI-G 플래싱

AI-G는 USB와 Ethernet 연결을 모두 사용합니다.

### 9.1 1단계: Ethernet 설정

1. 컴퓨터와 AI-G를 Ethernet 케이블로 연결합니다.
2. AI-G에 연결된 Ethernet 어댑터를 선택합니다.
3. 안내에 따라 컴퓨터 주소를 `192.168.0.8/24`로 설정합니다.
4. 네트워크 설정이 완료되었는지 확인합니다.

Wi-Fi가 아닌 **AI-G에 연결된 유선 Ethernet 어댑터**를 선택하세요.

### 9.2 2단계: 부트 모드 진입 및 COM 포트 선택

1. 애니메이션을 보며 BOOT 버튼을 누릅니다.
2. BOOT을 누른 상태에서 RESET을 눌렀다 놓습니다.
3. BOOT을 놓습니다.
4. 새로 감지된 AI-G USB COM 포트를 선택합니다.
5. 보드 전원, USB Type-C 및 Ethernet 케이블을 다시 확인합니다.

COM 포트가 여러 개면 AI-G USB 케이블을 잠시 분리하세요. 사라지는 포트가 AI-G 포트입니다. 다시 연결하고 부트 모드 진입을 반복한 다음 진행하세요.

### 9.3 3단계: 이미지 플래싱

1. **Start Flashing**을 선택합니다.
2. 진행률이 100%가 될 때까지 기다립니다.
3. 완료 화면이 나타나면 보드를 다시 시작합니다.

## 10. VCP-G 플래싱

### 10.1 1단계: 부트 모드 진입

1. 화면의 보드 그림을 확인합니다.
2. BOOT 버튼을 길게 누릅니다.
3. RESET을 눌렀다 놓습니다.
4. BOOT을 놓습니다.
5. **Next**를 선택합니다.

### 10.2 2단계: COM 포트 선택

1. VCP-G에 연결된 USB COM 포트를 선택합니다.
2. 포트가 없으면 USB Type-C 케이블을 다시 연결합니다.
3. 목록을 새로 고치고 올바른 포트를 선택합니다.

### 10.3 3단계: 이미지 플래싱

1. **Start Flashing**을 선택합니다.
2. 진행률이 100%가 될 때까지 기다립니다.
3. 완료 화면이 나타나면 보드를 다시 시작합니다.

## 11. 사용자 이미지 설치

공식 목록에 없는 로컬 이미지 파일을 설치할 때 사용합니다.

1. 운영체제 선택 화면에서 **Custom Image**를 한 번 클릭합니다.
2. **Next**를 선택하거나 항목을 두 번 클릭합니다.
3. 파일을 점선 영역으로 끌어 놓거나 **Browse for FAI Image** 또는 **Browse for ROM Image**를 선택하여 파일을 찾습니다.
4. 선택한 파일 이름을 확인합니다.
5. **Next**를 선택하고 보드별 연결 안내를 따릅니다.

올바른 형식을 선택하세요: D3-G와 AI-G는 `.fai`, VCP-G는 `.rom`입니다.
로컬 파일이므로 플래싱 화면에 다운로드 및 압축 해제 단계가 표시되지 않습니다.

## 12. Windows 문제 해결

### 보드가 감지되지 않음

1. 보드 전원을 확인합니다.
2. 충전 전용이 아닌 데이터 USB 케이블인지 확인합니다.
3. FWDN USB Type-C 포트에 연결되었는지 확인합니다.
4. 부트 모드 진입 순서를 반복합니다.
5. D3-G는 VTC 드라이버 설치 여부를 확인합니다.

### COM 포트가 표시되지 않음

1. USB 케이블을 분리했다 다시 연결합니다.
2. 보드 전원을 확인합니다.
3. 부트 모드에 다시 진입합니다.
4. COM 포트 목록을 새로 고칩니다.

### AI-G 네트워크 오류

1. AI-G와 컴퓨터 사이의 Ethernet 케이블을 확인합니다.
2. Wi-Fi가 아닌 유선 Ethernet 어댑터를 선택했는지 확인합니다.
3. 컴퓨터 주소가 `192.168.0.8/24`인지 확인합니다.
4. 앱 안내에 따라 1단계부터 다시 진행합니다.

### `Failed open port` 또는 `GetLastError : 22` 표시

FWDN USB Type-C 케이블을 확인하고 다시 연결한 다음 부트 모드 단계부터 반복합니다.

### 다운로드가 진행되지 않음

1. 인터넷 연결을 확인합니다.
2. 컴퓨터의 여유 저장 공간을 확인합니다.
3. 잠시 기다렸다가 **Retry**를 선택합니다.

### 플래싱 도중 이전 단계로 돌아가려는 경우

플래싱이 시작된 후 뒤로 이동하면 취소 확인 창이 표시됩니다. 취소하기 전에 보드가 안전한 상태인지 확인하고 화면 안내를 따르세요.

### 오류에 대한 도움이 필요한 경우

1. 오류 창의 상세 내용을 복사합니다.
2. **App Options**에서 로그 폴더를 엽니다.
3. 오류 메시지와 로그 파일을 준비합니다.
4. [TOPST 커뮤니티](https://community.topst.ai/)에 질문합니다.

Windows의 일반적인 로그 경로:

```text
%LOCALAPPDATA%\Telechips\TOPST Imager\logs\topst-imager.log
```

---

# Linux 사용 방법

## 13. Linux 사용 전 확인 사항

화면과 기본 절차는 Windows와 같지만 사전 준비가 다릅니다. 보드, 운영체제, 버전 버튼의 위치는 위 Windows 스크린샷과 같습니다. Linux에서는 D3-G의 Windows 드라이버 설치 화면을 건너뛰고 부트 모드 및 보드 감지로 바로 이동합니다.

- Windows VTC 드라이버를 설치하지 마세요.
- D3-G에는 Linux USB 접근 권한이 필요합니다.
- AI-G와 VCP-G에는 시리얼 포트 접근 권한이 필요합니다.
- 배포 패키지에 Linux FWDN 실행 파일이 포함되어 있어야 합니다.
- 공식 이미지 압축 해제에는 `unzip` 또는 `bsdtar`가 필요합니다.

명령어 입력이 익숙하지 않다면 관리자나 개발자에게 아래 **Linux 관리자 설정**을 한 번 진행해 달라고 요청하세요. 이후에는 일반 사용자가 화면 안내를 따르면 됩니다.

## 14. Linux 설치 및 실행

다음 예시는 Ubuntu 기준입니다.

### 14.1 패키지 압축 해제

1. TOPST 공식 웹사이트에서 컴퓨터에 맞는 Linux 패키지를 다운로드합니다.
2. 다운로드 폴더를 엽니다.
3. 터미널에서 다음 명령을 실행합니다.

```bash
cd ~/Downloads
tar -xzf TOPST-Imager-<version>-Linux-<architecture>.tar.gz
```

`<version>`과 `<architecture>`를 실제 파일 이름의 값으로 바꾸세요. 파일 이름의 앞부분을 입력하고 `Tab`으로 자동 완성할 수 있습니다.

### 14.2 앱 실행

압축을 푼 폴더로 이동하여 앱을 실행합니다.

```bash
cd TOPST-Imager-<version>-Linux-<architecture>
chmod +x topst-imager
./topst-imager
```

`Qt` 라이브러리가 없다는 오류가 나오면 현재 패키지에 Qt 런타임이 포함되지 않은 것입니다. 일반 사용자는 직접 설치하려 하지 말고 배포자에게 **Qt 6.12 런타임이 포함된 Linux 패키지**를 요청하세요.

## 15. Linux 관리자 설정

일반적으로 한 번만 설정하면 됩니다.

### 15.1 압축 해제 도구 설치

```bash
sudo apt update
sudo apt install unzip
```

### 15.2 AI-G 및 VCP-G 시리얼 포트 권한

```bash
sudo usermod -aG dialout "$USER"
```

명령 실행 후 로그아웃했다 다시 로그인하거나 컴퓨터를 다시 시작하세요.

### 15.3 D3-G USB 권한

1. D3-G를 부트 모드로 연결합니다.
2. 터미널에서 USB ID를 확인합니다.

```bash
lsusb
```

3. 확인한 공급업체 ID와 제품 ID로 `/etc/udev/rules.d/99-topst.rules`를 생성합니다.

```text
SUBSYSTEM=="usb", ATTR{idVendor}=="VENDOR_ID", ATTR{idProduct}=="PRODUCT_ID", MODE="0666"
```

4. 규칙을 다시 불러옵니다.

```bash
sudo udevadm control --reload-rules
sudo udevadm trigger
```

`VENDOR_ID`와 `PRODUCT_ID`에 임의의 값을 입력하지 마세요. D3-G의 올바른 값을 모르면 TOPST 지원팀에 문의하세요.

### 15.4 Linux FWDN 파일 확인

배포 패키지의 다음 위치에 확장자가 없는 Linux 실행 파일이 있어야 합니다.

```text
tools/fwdn_d3/fwdn_d3
tools/fwdn_ai/fwdn_ai
tools/fwdn_vcp/fwdn_vcp
```

파일이 있으면 실행 권한을 부여합니다.

```bash
chmod +x tools/fwdn_d3/fwdn_d3
chmod +x tools/fwdn_ai/fwdn_ai
chmod +x tools/fwdn_vcp/fwdn_vcp
```

이 파일들이 없으면 Linux에서 플래싱할 수 없습니다. Windows `.exe` 파일로 대체할 수 없습니다.

## 16. Linux에서 D3-G 플래싱

Windows VTC 드라이버 설치 단계는 사용하지 않습니다.

1. D3-G 이미지를 선택합니다.
2. 화면 애니메이션을 보며 BOOT 버튼을 누릅니다.
3. BOOT을 누른 상태에서 RESET을 눌렀다 놓습니다.
4. BOOT을 놓습니다.
5. 보드가 감지되는지 확인합니다.
6. 플래싱을 시작하고 완료될 때까지 기다립니다.

감지되지 않으면 USB 권한 규칙, Type-C 케이블, 보드 전원, 부트 모드를 확인하세요.

## 17. Linux에서 AI-G 플래싱

Linux에서는 TOPST Imager가 Ethernet 주소를 자동 변경하지 않습니다. Ubuntu 설정에서 수동으로 설정하세요.

1. Ubuntu의 **설정 → 네트워크**를 엽니다.
2. AI-G에 연결된 유선 네트워크 설정을 엽니다.
3. IPv4 방식을 **수동**으로 설정합니다.
4. 주소에 `192.168.0.8`을 입력합니다.
5. 넷마스크에 `255.255.255.0`을 입력합니다. 접두사 길이 형식이면 `24`를 입력합니다.
6. 별도 안내가 없다면 게이트웨이와 DNS는 비워 둡니다.
7. 적용한 다음 유선 연결을 껐다 켭니다.
8. TOPST Imager로 돌아와 Ethernet 상태를 확인합니다.
9. 화면 안내에 따라 부트 모드에 진입합니다.
10. AI-G의 `/dev/ttyUSB...` 또는 `/dev/ttyACM...` 포트를 선택합니다.
11. 플래싱을 시작합니다.

## 18. Linux에서 VCP-G 플래싱

1. 화면 안내에 따라 VCP-G를 부트 모드로 전환합니다.
2. `/dev/ttyUSB...` 또는 `/dev/ttyACM...` 형식의 포트를 선택합니다.
3. 올바른 포트인지 확인하고 플래싱을 시작합니다.
4. 완료 화면이 나타날 때까지 기다립니다.

포트가 없다면 `dialout` 그룹에 가입한 후 로그아웃 및 재로그인했는지 확인하세요.

## 19. Linux 문제 해결

### `Permission denied` 표시

- AI-G 또는 VCP-G: 사용자가 `dialout` 그룹에 속하는지 확인합니다.
- D3-G: udev USB 권한 규칙이 활성화되었는지 확인합니다.
- FWDN 파일: `chmod +x`로 실행 권한을 부여했는지 확인합니다.

### Linux FWDN 파일을 찾을 수 없음

배포 폴더의 `tools/fwdn_*` 아래에 Linux 실행 파일이 있는지 확인하세요. Windows `.exe` 파일은 Linux에서 실행되지 않습니다.

### 보드 포트가 표시되지 않음

다음 명령으로 포트를 확인합니다.

```bash
ls /dev/ttyUSB* /dev/ttyACM* 2>/dev/null
```

USB 연결 전후의 목록을 비교하세요. 새로 나타난 포트가 보통 보드 포트입니다.

### 밝은 테마 또는 어두운 테마가 적용되지 않음

Linux 데스크톱이 Qt를 통해 제공하는 테마 정보를 사용합니다. 일부 환경은 시스템 테마를 바로 적용하지 않을 수 있으므로 앱을 다시 시작해 보세요.

## 20. 플래싱 완료 후

1. 성공 메시지가 표시되었는지 확인합니다.
2. TOPST Imager의 모든 작업이 끝날 때까지 기다립니다.
3. 보드 전원을 안전하게 끕니다.
4. FWDN 케이블을 분리하거나 일반 사용에 맞게 케이블을 연결합니다.
5. 보드를 켜고 새 운영체제가 시작되는지 확인합니다.

공식 이미지는 임시 폴더에 다운로드 및 압축 해제됩니다. 플래싱이 성공하면 다운로드 파일과 압축 해제 폴더는 자동 삭제됩니다.

## 21. 꼭 기억할 세 가지

1. **보드와 이미지를 올바르게 선택했는지 확인하세요.**
2. **플래싱 중 전원이나 케이블을 분리하지 마세요.**
3. **오류가 나면 화면의 목록을 위에서부터 하나씩 확인하세요.**

도움이 필요하면 오류 메시지와 로그 파일을 준비하여 [TOPST 커뮤니티](https://community.topst.ai/)에 질문하세요.
