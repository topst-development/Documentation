# 1. 소개
---
본 문서는 자동차용 애플리케이션을 위해 설계된 강력하고 효율적인 프로세서이며 TCC7045를 기반으로 하는 TOPST Vehicle Control Processor(VCP)에서 Arduino IDE를 사용하는 방법을 설명합니다. VCP-G를 Arduino 환경과 통합하여, Arduino의 단순함과 유연성에 상응하면서 자동차용 반도체에 특화된 개발 환경을 제공하고 개발 과정을 단순화하고 가속화하는 것을 목표로 합니다.  

본 문서에는 다음 정보가 포함되어 있습니다:  
- 설치 가이드

</br></br></br></br>

# 2. 설치 가이드
---
본 장에서는 Arduino 통합 개발 환경(IDE)에서 사용할 VCP-G Arduino 패키지를 다운로드하고 설치하는 방법을 설명합니다.

</br></br></br>

## 2.1 설치 가이드
---
**1단계: Arduino IDE 다운로드**

먼저 Arduino 보드를 프로그래밍하기 위한 플랫폼 역할을 하는 Arduino IDE가 필요합니다.  
1. 공식 Arduino 웹사이트를 방문하십시오 : [Arduino Software](https://www.arduino.cc/en/software)
2. 운영 체제(Windoiws, macOS 또는 Linux)에 적합한 버전을 선택하십시오.
3. 설치 프로그램을 다운로드하여 실행하십시오.

**2단계: Arduino IDE 설치**  
운영 체제에 따라 다음 단계를 수행하여 Arduino IDE를 설치하십시오:  

- Windows:
    1. 다운로드한 .exe 파일을 실행하십시오.
    2. 설치 안내에 따라 진행하십시오. 필요한 드라이버를 모두 설치해야 합니다.
- macOS:
    1. .dmg 파일을 여십시오
    2. Arduino 애플리케이션을 Applications 폴더로 끌어다 놓으십시오.
- Linux:
    1. .tar.xz 파일의 압축을 해제하십시오.
    2. 압축을 해제한 디렉터리에서 터미널을 여십시오.
    3. ./install.sh를 실행하여 설치하십시오.

**3단계: Arduino IDE에 VCP-G .json 파일 추가**  
VCP-G를 프로그래밍하려면 Board Manager를 통해 VCP-G .json 파일을 Arduino IDE에 추가해야 합니다.
1. Arduino IDE를 실행하십시오.
2. **File > Preferences**로 이동하십시오.
3. **"Additional Board Manager URLs"** 필드에 다음 URL을 추가하십시오:
    ```
    https://raw.githubusercontent.com/topst-development/VCP-Arduino_Board_Manager/develop/package_topst_vcp_index.json
    ```
4. **OK**를 클릭하여 변경 사항을 저장하십시오.
5. **Tools > Board > Boards Manager.**로 이동하십시오.
6. Boards Manager에서 “TOPST VCP-G”를 검색하십시오.
7. TOPST VCP-G 항목이 나타나면 드롭다운 메뉴에서 v1.0.0을 선택하고 **Install**을 클릭하십시오.

**4단계: VCP-G 선택**  
설치 후 TOPST VCP-G 보드를 선택해야 합니다:  
1. Arduino IDE에서 **Tools > Board**로 이동하십시오.
2. 아래로 스크롤하여 "TOPST VCP-G"를 찾아 선택하십시오.

**5단계: 설치 확인**  
간단한 스케치를 업로드하여 설정이 정상적으로 동작하는지 확인하십시오:
1. USB를 사용하여 VCP-G 보드를 PC에 연결하십시오.
2. **Tools > Port**에서 적절한 포트를 선택하십시오.
3.	**File > Examples > 01.Basics > Blink**를 여십시오.
4.	**Upload**를 클릭하여 스케치를 보드로 전송하십시오.  
    **참고:** 업로드 과정이 무한 업로드 상태에서 멈추는 경우, FWDN 모드가 활성화되지 않았기 때문입니다. 전원 케이블을 분리하고 FWDN 스위치를 누른 상태에서 전원 케이블을 다시 연결한 후 버튼에서 손을 떼십시오. 문제가 계속되면 관리자 권한으로 Arduino IDE를 실행해 보십시오.
5.	온보드 LED가 깜박이기 시작하면 보드가 올바르게 설정된 것입니다.

</br></br></br>

## 2.2 문제 해결
---
설정 중 문제가 발생하면 [Arduino 문제 해결 가이드](https://www.arduino.cc/en/Guide/Troubleshooting).  
자세한 정보 및 고급 기능은 VCP-G 문서를 참조하거나 [Arduino 헬프 센터](https://support.arduino.cc/hc/en-us).

</br></br></br></br>

# 3. 참고 자료
---
- 자세한 내용은 TOPST에 문의하십시오: topst@topst.ai

**참고:** 참고 문서는 계약 조건에 따라 제공 가능한 경우 제공될 수 있습니다. 참고
문서를 제공할 수 없는 경우, 개발과 직접 관련된 내용을 안내받을 수 있습니다.

