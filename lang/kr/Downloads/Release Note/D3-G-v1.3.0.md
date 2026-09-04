# D3-G 릴리스 노트 - v1.3.0

## 업데이트된 저장소
- [isp-server](https://github.com/topst-development/isp-server/tree/feature/d3g-ov5647)
- [isp-frontend](https://github.com/topst-development/isp-frontend/tree/feature/d3g)
- [kernel-5.10](https://github.com/topst-development/kernel-5.10/tree/release/d3/1.3.0)
- [meta-topst](https://github.com/topst-development/meta-topst/tree/release/1.3.0)
- [meta-topst-bsp](https://github.com/topst-development/meta-topst-bsp/tree/release/1.3.0)
- [manifests](https://github.com/topst-development/manifests/tree/release/1.3.0)

## 새로운 기능
- vulkan 드라이버를 지원합니다
- 기본적인 카메라 isp 튜닝 도구를 지원합니다
- 빌드 설정을 통해 PIv2 카메라를 지원합니다
- Ubuntu 데스크톱 릴리스에서 firefox-esr (extended support release)을 지원합니다

## 개선 사항
- pcie 데이터 전송 속도를 개선했습니다
- 부팅 중 pcie 블록 디바이스 인식을 안정화했습니다

## 알려진 문제
- sdcard가 삽입된 상태에서 웜 리부트가 간헐적으로 오래(약 40초) 걸립니다.
- MIPI에 연결된 외부 카메라는 현재 최대 30fps까지 지원합니다(다음 릴리스에서 최대 60fps를 지원할 예정입니다)

## 가이드
 - VLC Player
   - 콘텐츠를 재생하기 전에 환경 설정에서 비디오 출력을 'X11 video output(XCB)'로 설정해야 합니다.
 - Vulkan 드라이버
   - vulkan 예제를 실행하려면 'vkcube' 명령을 실행하십시오.
   - 직접 vulkan 애플리케이션을 프로그래밍하는 방법은 [https://github.com/krh/vkcube.git](https://github.com/krh/vkcube.git)를 참조하십시오.
