# 1. 소개
---
이 문서는 TCC7045를 기반으로 자동차 애플리케이션을 위해 설계된 강력하고 효율적인 프로세서인 TOPST VCP(Vehicle Control Processor)용 Arduino IDE를 사용하는 방법을 설명합니다. 목표는 VCP-G를 Arduino 환경과 통합하여 자동차 반도체에 맞게 특별히 조정된 Arduino의 단순성과 유연성을 갖춘 개발 환경을 제공하고 개발 프로세스를 단순화하고 가속화하는 것입니다.
 
이 문서에는 다음 정보가 포함되어 있습니다:
- 설치 가이드
 
</br></br></br></br>
 
# 2. 설치 가이드
---
이 장에서는 Arduino 통합 개발 환경(IDE)과 함께 사용하기 위해 VCP-G Arduino 패키지를 다운로드하고 설치하는 방법을 설명합니다.
 
</br></br></br>
 
## 2.1 설치 가이드
---
**1단계: Arduino IDE 다운로드**
 
먼저 Arduino 보드를 프로그래밍하는 플랫폼 역할을 하는 Arduino IDE가 필요합니다.
1. 공식 Arduino 웹사이트 방문 : [Arduino Software](https://www.arduino.cc/en/software)
2. 운영 체제(Windows, macOS 또는 Linux)에 적합한 버전을 선택합니다.
3. 설치 프로그램을 다운로드하고 실행합니다.
 
**2단계: Arduino IDE 설치**
운영 체제에 따라 다음 단계에 따라 Arduino IDE를 설치합니다:
 
- Windows:
    1. 다운로드한 .exe 파일을 실행합니다.
    2. 설치 프롬프트를 따릅니다. 필요한 모든 드라이버를 설치했는지 확인하십시오.
- macOS:
    1. .dmg 파일을 엽니다.
    2. Arduino 애플리케이션을 응용 프로그램 폴더로 드래그합니다.
- Linux:
    1. .tar.xz 파일의 압축을 풉니다.
    2. 추출된 디렉토리에서 터미널을 엽니다.
    3. ./install.sh를 실행하여 설치합니다.
 
**3단계: Arduino IDE에 VCP-G .json 파일 추가**
VCP-G를 프로그래밍하려면 보드 관리자를 통해 Arduino IDE에 VCP-G .json 파일을 추가해야 합니다.
1. Arduino IDE를 엽니다.
2. **파일 > 기본 설정**으로 이동합니다.
3. **"추가 보드 관리자 URL"** 필드에 다음 URL을 추가합니다:
    ```
    https://raw.githubusercontent.com/topst-development/VCP-Arduino_Board_Manager/develop/package_topst_vcp_index.json
    ```
4. **확인**을 클릭하여 변경 사항을 저장합니다.
5. **도구 > 보드 > 보드 관리자**로 이동합니다.
6. 보드 관리자에서 "TOPST VCP-G"를 검색합니다.
7. TOPST VCP-G 항목이 나타나면 드롭다운 메뉴에서 v1.0.0을 선택하고 **설치**를 클릭합니다.
 
**4단계: VCP-G 선택**
설치 후 TOPST VCP-G 보드를 선택해야 합니다:
1. Arduino IDE에서 **도구 > 보드**로 이동합니다.
2. 아래로 스크롤하여 "TOPST VCP-G"를 찾아 선택합니다.
 
**5단계: 설치 확인**
간단한 스케치를 업로드하여 설정이 작동하는지 테스트합니다:
1. USB를 사용하여 VCP-G 보드를 PC에 연결합니다.
2. **도구 > 포트**에서 적절한 포트를 선택합니다.
3. **파일 > 예제 > 01.Basics > Blink**를 엽니다.
4. **업로드**를 클릭하여 스케치를 보드로 전송합니다.
    **참고:** 업로드 프로세스가 무한 업로드 상태에서 멈추면 FWDN 모드가 활성화되지 않았기 때문입니다. 전원 케이블을 분리하고 FWDN 스위치를 길게 누른 다음 전원 케이블을 다시 연결하고 버튼을 놓으십시오. 문제가 지속되면 관리자 권한으로 Arduino IDE를 실행해 보십시오.
5. 온보드 LED가 깜박이기 시작하면 보드가 올바르게 설정된 것입니다.
 
</br></br></br>
 
## 2.2 문제 해결
---
설정 중 문제가 발생하면 [Arduino 문제 해결 가이드](https://www.arduino.cc/en/Guide/Troubleshooting)를 참조하십시오.
자세한 정보 및 고급 기능은 VCP-G 문서를 참조하거나 [Arduino 도움말 센터](https://support.arduino.cc/hc/en-us)를 방문하십시오.
 
</br></br></br></br>
 
# 3. 참고 문헌
---
- 자세한 내용은 TOPST에 문의하십시오: topst@topst.ai
 
**참고:** 참조 문서는 계약 조건에 따라 가능한 경우 제공될 수 있습니다. 참조 문서를 사용할 수 없는 경우 개발과 직접 관련된 내용을 안내받을 수 있습니다.
