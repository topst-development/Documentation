# 1. 简介
---
本文档介绍如何在 TOPST Vehicle Control Processor (VCP) 上使用 Arduino IDE。VCP 是一款专为汽车应用设计的强大而高效的处理器，基于 TCC7045。其目标是将 VCP-G 与 Arduino 环境集成，提供一个既具备 Arduino 的简洁性与灵活性、又专门针对汽车半导体的开发环境，从而简化并加快开发流程。  

本文档包含以下信息:  
- 安装指南

</br></br></br></br>

# 2. 安装指南
---
本章介绍如何下载并安装用于 Arduino 集成开发环境 (IDE) 的 VCP-G Arduino 软件包。

</br></br></br>

## 2.1 安装指南
---
**步骤 1: 下载 Arduino IDE**

首先，您需要 Arduino IDE，它是用于对 Arduino 开发板进行编程的平台。  
1. 访问 Arduino 官方网站 : [Arduino Software](https://www.arduino.cc/en/software)
2. 选择适合您操作系统 (Windoiws、macOS 或 Linux) 的版本。
3. 下载并运行安装程序。

**步骤 2: 安装 Arduino IDE**  
请根据您的操作系统按照以下步骤安装 Arduino IDE:  

- Windows:
    1. 运行下载的 .exe 文件。
    2. 按照安装提示进行操作。请确保安装所有必需的驱动程序。
- macOS:
    1. 打开 .dmg 文件
    2. 将 Arduino 应用程序拖到 Applications 文件夹中。
- Linux:
    1. 解压 .tar.xz 文件。
    2. 在解压后的目录中打开终端。
    3. 运行 ./install.sh 进行安装。

**步骤 3: 将 VCP-G .json 文件添加到 Arduino IDE**  
要对 VCP-G 进行编程，您需要通过 Board Manager 将 VCP-G .json 文件添加到 Arduino IDE。
1. 打开 Arduino IDE。
2. 转到 **File > Preferences**。
3. 在 **"Additional Board Manager URLs"** 字段中添加以下 URL:
    ```
    https://raw.githubusercontent.com/topst-development/VCP-Arduino_Board_Manager/develop/package_topst_vcp_index.json
    ```
4. 单击 **OK** 保存更改。
5. 转到 **Tools > Board > Boards Manager.**
6. 在 Boards Manager 中搜索 “TOPST VCP-G”。
7. 当出现 TOPST VCP-G 条目时，从下拉菜单中选择 v1.0.0 并单击 **Install**。

**步骤 4: 选择 VCP-G**  
安装完成后，您需要选择 TOPST VCP-G 开发板:  
1. 在 Arduino IDE 中转到 **Tools > Board**。
2. 向下滚动找到 "TOPST VCP-G" 并选择它。

**步骤 5: 验证安装**  
通过上传一个简单的示例程序测试您的设置是否正常工作:
1. 使用 USB 将 VCP-G 开发板连接到您的 PC。
2. 在 **Tools > Port** 下选择相应的端口。
3.	打开 **File > Examples > 01.Basics > Blink**。
4.	单击 **Upload** 将示例程序传输到开发板。  
    **注意:** 如果上传过程卡在无限上传状态，是因为未激活 FWDN 模式。请拔下电源线，按住 FWDN 开关，重新连接电源线，然后松开按钮。如果问题仍然存在，请尝试以管理员权限运行 Arduino IDE。
5.	如果板载 LED 开始闪烁，则说明开发板设置正确。

</br></br></br>

## 2.2 故障排除
---
如果您在设置过程中遇到任何问题，请参阅 [Arduino 故障排除指南](https://www.arduino.cc/en/Guide/Troubleshooting).  
有关更多信息和高级功能，请参阅 VCP-G 文档或访问 [Arduino 帮助中心](https://support.arduino.cc/hc/en-us).

</br></br></br></br>

# 3. 参考资料
---
- 如需了解更多详情，请联系 TOPST: topst@topst.ai

**注意:** 参考文档可根据合同条款在可提供时提供。如果无法提供参考
文档，则可就与您的开发直接相关的内容提供指导。

