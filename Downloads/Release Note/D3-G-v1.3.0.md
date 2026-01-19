# D3-G Release Note - v1.3.0

## Updated repositories
- [isp-server](https://github.com/topst-development/isp-server/tree/feature/d3g-ov5647)
- [isp-frontend](https://github.com/topst-development/isp-frontend/tree/feature/d3g)
- [kernel-5.10](https://github.com/topst-development/kernel-5.10/tree/release/d3/1.3.0)
- [meta-topst](https://github.com/topst-development/meta-topst/tree/release/1.3.0)
- [meta-topst-bsp](https://github.com/topst-development/meta-topst-bsp/tree/release/1.3.0)
- [manifests](https://github.com/topst-development/manifests/tree/release/1.3.0)

## New Features
- supports the vulkan driver
- supports a basic camera isp tuning tool
- supports the PIv2 camera via build configuration
- supports firefox-esr (extended support release) in the Ubuntu desktop release

## Improvement
- improves pcie data transmission speed
- stablized pcie block device detection during boot

## Known Issues
- warm reboot takes long (around 40 seconds) from time to time when sdcard is inserted.
- external camera, connected to MIPI, supports up to 30fps for now (will support up to 60fps in the next release)

## Guides
 - VLC Player
   Before playing contents, the video output should be set to 'X11 video output(XCB)' in the preference.
 - Vulkan driver
   run 'vkcube' command to execute the vulkan example.
   refer to [https://github.com/krh/vkcube.git](https://github.com/krh/vkcube.git) to learn how to program your own vulkan application.