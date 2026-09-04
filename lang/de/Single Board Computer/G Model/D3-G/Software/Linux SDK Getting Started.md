# 1. Einführung
---
Dieses Dokument enthält Richtlinien für das Erstellen des D3-G SDK, einschließlich der Einrichtung der Host-Umgebung, des Erstellens des SDK, der Verwendung des Firmware Downloaders und des Herunterladens von Ubuntu.  

Dieses Dokument enthält Informationen zu den folgenden Themen: 
- Einrichten der Host-Umgebung  
- Anleitung zum Erstellen des Image  
- Anleitung zum Firmware-Download 
- Verbinden des D3-G-Boards mit einem PC

<br/><br/><br/><br/>

# 2. Einrichten der Host-Umgebung
---
In diesem Kapitel wird beschrieben, wie Sie die Host-PC-Umgebung einrichten, mit separaten Anleitungen für Windows und Ubuntu.
</br><br/><br/>

## 2.1 Windows-Umgebung 
---
In diesem Dokument wird beschrieben, wie Sie Windows Subsystem for Linux (WSL) einrichten, um Linux auf einem Windows-PC zu verwenden.
Das D3-G Linux SDK basiert auf dem Yocto Project, daher richtet sich die Linux-Version des D3-G SDK nach dem Yocto Project.
Sie können eine andere Version von Linux installieren, dieses Dokument beschreibt jedoch das D3-G Linux SDK auf Basis von Ubuntu 22.04.
Wenn Ihr Host-Betriebssystem Ubuntu ist, fahren Sie mit Kapitel 2.2 fort.

</br><br/>

### 2.1.1 WSL2 Ubuntu installieren
1. Führen Sie Windows PowerShell mit „**Als Administrator ausführen**“ aus.
2. Aktivieren Sie das WSL2-System.
    ```
    dism.exe /online /enable-feature /featurename:Microsoft-Windows-Subsystem-Linux /all /norestart
    ```
3. Aktivieren Sie die Funktion für virtuelle Maschinen.
    ```
    dism.exe /online /enable-feature /featurename:VirtualMachinePlatform /all /norestart
    ```
4. Legen Sie WSL 2 als Standardversion fest.
    ```
    wsl --set-default-version 2
    ```
5. Suchen Sie im Microsoft Store nach Ubuntu 22.04.3 LTS und laden Sie es herunter.

    * Wenn Sie das Linux-Kernel-Updatepaket herunterladen müssen, laden Sie das neueste Paket [hier](https://learn.microsoft.com/ko-kr/windows/wsl/install-manual) herunter.

6. Wählen Sie während der Ubuntu-Installation einen beliebigen Benutzernamen.
</br><br/>

### 2.1.2 Zugriff auf Ubuntu über WSL2
Öffnen Sie die Windows-Eingabeaufforderung und geben Sie den folgenden Befehl ein, um auf Ubuntu zuzugreifen.
Wenn Sie auf Ubuntu zugreifen, startet es standardmäßig im Verzeichnis /mnt/c/Users/[username].
```
wsl  // access ubuntu 
ls   // check contents in your directory
```
Siehe Abbildung 2.1, um das Ergebnis zu überprüfen (die Ergebnisse können je nach System variieren).
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20D3-G/Software/1.1%20wsl%20linux.png" width="500"></p>
<p align="center"><strong>Abbildung 2.1 WSL2-Screenshot </strong></p>

<br/><br/>

### 2.1.3 Locale festlegen

Nachdem Sie Ubuntu unter WSL gestartet haben, sollten Sie die Locale festlegen, um korrekte Sprach- und Regionaleinstellungen sicherzustellen. Es wird empfohlen, en_US.UTF-8 zu verwenden. Führen Sie die folgenden Befehle aus, um en_US.UTF-8 zu verwenden. 

```
sudo locale-gen en_US.UTF-8 && sudo update-locale LANG=en_US.UTF-8 
```

Nachdem Sie die Locale festgelegt haben, können Sie den Locale-Typ mit den folgenden Befehlen prüfen. 

```
echo 'LANG=en_US.UTF-8' | sudo tee -a /etc/default/locale && \  

echo 'LC_ALL=en_US.UTF-8' | sudo tee -a /etc/default/locale 
```
<br/><br/>

### 2.1.4 SSH und Samba installieren

Nachdem Sie Ubuntu gestartet haben, können Sie zusätzliche Dienstprogramme wie SSH und Samba für eine komfortablere Entwicklungsumgebung verwenden. SSH und Samba ermöglichen es Ihnen, Befehle auf entfernten Computern auszuführen und Dateien auf andere Computer zu kopieren.
 - Für die folgenden Schritte muss der Host-PC mit dem Netzwerk verbunden sein. Überprüfen Sie Ihren Netzwerkzustand mit den folgenden Befehlen.
  ```
  $ sudo apt-get update
  $ sudo apt-get install -y net-tools
  $ ifconfig 
  ```

Wenn SSH und Samba bereits installiert sind oder Sie sie nicht verwenden möchten, können Sie dieses Kapitel überspringen.

Verwenden Sie den folgenden Befehl, um net-tools, SSH und Samba zu installieren.

```
$ sudo apt-get update 
$ sudo apt install -y net-tools openssh-server samba
```
Konfigurieren Sie nach der Installation von SSH und Samba jedes Programm entsprechend den Anforderungen Ihrer Umgebung.
</br><br/>

### 2.1.5 Dienstprogramme installieren

Verwenden Sie die folgenden Befehle, um alle erforderlichen Dienstprogramme auf einmal zu installieren. Um das Yocto Project zu verwenden, müssen die folgenden Dienstprogramme auf dem Host-PC  (Einzelcomputer oder Entwicklungsserver) installiert sein.


```
$ sudo apt-get install -y gawk wget git diffstat unzip texinfo gcc-multilib build-essential chrpath

$ sudo apt-get install -y socat cpio python3 python3-pip python3-pexpect xz-utils debianutils

$ sudo apt-get install -y iputils-ping python3-git python3-jinja2 libegl1-mesa-dev libsdl1.2-dev pylint

$ sudo apt-get install -y xterm zstd ncftp curl git-lfs vim zip lz4
```

<br/><br/>

### 2.1.6 Repo installieren

Wenn Repo bereits installiert ist, können Sie es ohne Neuinstallation verwenden.  
Stellen Sie vor der Installation von Repo sicher, dass Python Version 3.6 oder höher installiert ist.

Verwenden Sie den folgenden Befehl, um Repo zu installieren.
```
$ sudo apt-get install repo
```

Wenn die Fehlermeldung '/usr/bin/env 'python' no such file or directory' angezeigt wird, verwenden Sie den folgenden Befehl, um 'python' mit 'python3' zu verknüpfen.

```
$ sudo ln -sf /usr/bin/python3 /usr/bin/python
```
Wenn ein Repo-Fehler auftritt, verwenden Sie die folgenden Befehle, um die neueste Version herunterzuladen und sie im Ordner /usr/bin/ abzulegen.

```
$ mkdir -p ~/bin

$ curl http://commondatastorage.googleapis.com/git-repo-downloads/repo > ~/bin/repo

$ chmod a+x ~/bin/repo

$ sudo mv ~/bin/repo /usr/bin/repo
```
Fahren Sie mit **Kapitel 3: Anleitung zum Erstellen des Image** fort.

<br/><br/><br/>

## 2.2 Linux-Umgebung
---
In diesem Kapitel wird der Einrichtungsprozess für Ubuntu als Host-Betriebssystem erläutert.
</br><br/>

### 2.2.1 Einrichten der Umgebung
Die folgenden Kapitel (2.2.2 bis 2.2.5) müssen im Ubuntu-Terminal ausgeführt werden. Um das Terminal zu öffnen, verwenden Sie die Tastenkombination: [Ctrl + Alt + T].
<br/><br/>

### 2.2.2 Locale festlegen

Nachdem Sie Ubuntu unter WSL gestartet haben, sollten Sie die Locale festlegen, um korrekte Sprach- und Regionaleinstellungen sicherzustellen. Es wird empfohlen, en_US.UTF-8 zu verwenden. Führen Sie die folgenden Befehle aus, um en_US.UTF-8 zu verwenden. 

```
sudo locale-gen en_US.UTF-8 && sudo update-locale LANG=en_US.UTF-8 
```

Nachdem Sie die Locale festgelegt haben, können Sie den Locale-Typ mit den folgenden Befehlen prüfen. 

```
echo 'LANG=en_US.UTF-8' | sudo tee -a /etc/default/locale && \  

echo 'LC_ALL=en_US.UTF-8' | sudo tee -a /etc/default/locale 
```
<br/><br/>

### 2.2.3 SSH und Samba installieren

Nachdem Sie Ubuntu gestartet haben, können Sie zusätzliche Dienstprogramme wie SSH und Samba für eine komfortablere Entwicklungsumgebung verwenden. SSH und Samba ermöglichen es Ihnen, Befehle auf entfernten Computern auszuführen und Dateien auf andere Computer zu kopieren.
 - Für die folgenden Schritte muss der Host-PC mit dem Netzwerk verbunden sein. Überprüfen Sie Ihren Netzwerkzustand mit den folgenden Befehlen
  ```
  $ sudo apt-get update
  $ sudo apt-get install -y net-tools
  $ ifconfig 
  ```

Wenn SSH und Samba bereits installiert sind oder Sie sie nicht verwenden möchten, können Sie dieses Kapitel überspringen.

Verwenden Sie den folgenden Befehl, um SSH und Samba zu installieren.

```
$ sudo apt-get update 
$ sudo apt install -y openssh-server samba
```
Konfigurieren Sie nach der Installation von SSH und Samba jedes Programm entsprechend den Anforderungen Ihrer Umgebung.

<br/><br/>

### 2.2.4 Dienstprogramme installieren

Verwenden Sie die folgenden Befehle, um alle erforderlichen Dienstprogramme auf einmal zu installieren. Um das Yocto Project zu verwenden, **müssen** die folgenden Dienstprogramme auf dem Host-PC (Einzelcomputer oder Entwicklungsserver) installiert sein.
****


```
$ sudo apt-get install -y gawk wget git diffstat unzip texinfo gcc-multilib build-essential chrpath

$ sudo apt-get install -y socat cpio python3 python3-pip python3-pexpect xz-utils debianutils

$ sudo apt-get install -y iputils-ping python3-git python3-jinja2 libegl1-mesa-dev libsdl1.2-dev pylint

$ sudo apt-get install -y xterm zstd ncftp curl git-lfs vim zip lz4
```

<br/><br/>

### 2.2.5 Repo installieren

Sie können das D3-G SDK über Android Repo herunterladen.  
Informationen zur Installation von Repo finden Sie auf der folgenden Website: https://source.android.com/source/downloading.html.  
Wenn Repo bereits installiert ist, können Sie es ohne Neuinstallation verwenden.  
Stellen Sie vor der Installation von Repo sicher, dass Python Version 3.6 oder höher installiert ist.

Verwenden Sie den folgenden Befehl, um Repo zu installieren.
```
$ sudo apt-get install repo
```

Wenn die Fehlermeldung '/usr/bin/env 'python' no such file or directory' angezeigt wird, verwenden Sie den folgenden Befehl, um 'python' mit 'python3' zu verknüpfen.

```
$ sudo ln -sf /usr/bin/python3 /usr/bin/python
```
Wenn ein Repo-Fehler auftritt, verwenden Sie den folgenden Befehl, um die neueste Version herunterzuladen und sie im Ordner /usr/bin/ abzulegen.

```
$ mkdir -p ~/bin

$ curl http://commondatastorage.googleapis.com/git-repo-downloads/repo > ~/bin/repo

$ chmod a+x ~/bin/repo

$ sudo mv ~/bin/repo /usr/bin/repo
```

<br/><br/>

### 2.2.6 Udev-Regeln für Telechips USB-Gerät
Nachdem Sie die folgenden Befehle ausgeführt haben, müssen Sie beim Herunterladen von FWDN unter Linux den Befehl 'sudo' nicht mehr verwenden.
```
$ echo "SUBSYSTEM==\"usb\", ATTR{idVendor}==\"140e\", MODE=\"0666\", OWNER=\"${USER}\"" | sudo tee /etc/udev/rules.d/99-topst.rules
$ sudo udevadm control --reload-rules && sudo udevadm trigger
```
Fahren Sie mit **Kapitel 3: Anleitung zum Erstellen des Image** fort.

<br/><br/><br/><br/>

# 3. Anleitung zum Erstellen des Image
---
Dieses Kapitel bietet eine Anleitung auf Basis des auf dem Host-PC installierten Ubuntu-Betriebssystems (unabhängig davon, ob es sich um WSL oder eine lokale Ubuntu-Installation handelt). Das auf das D3-G hochzuladende Image wird mit dem Yocto Project erstellt, daher muss der Build-Vorgang in der Ubuntu-Umgebung durchgeführt werden.
</br></br>

## 3.1 Vorbereitung des SDK-Builds
---
Das D3-G Linux SDK basiert auf Yocto Project 4.0 Kirkstone . Daher müssen Sie die Yocto-Project-Umgebung auf dem Host-PC konfigurieren, um das D3-G Linux SDK zu verwenden. Um SDK, source-mirror und Tools herunterzuladen, müssen Sie die erforderlichen Dienstprogramme installieren. Damit das Image reibungslos erstellt werden kann, muss Ihr PC über **mindestens 60 GB freien Speicherplatz** und **mindestens 16 GB RAM** verfügen.

</br><br/>  

## 3.2 Yocto Project  
---
Das Yocto Project ist ein Open-Source-Projekt, das sich auf die Entwicklung von Embedded Linux konzentriert.  
Es verwendet eine Kombination aus dem Open Embedded Project, nämlich Poky, und ***bitbake*** als Build-System, um Linux-Images zu erstellen.  
Mit dem Yocto Project können Sie Bootloader, Kernel und rootfs gleichzeitig erstellen.  

<br/><br/>

## 3.3 Task-Prozess des Yocto Project
---
Abbildung 3.1 zeigt den Aufgabenablauf des Yocto Project. Sie können den Quellcode basierend auf Metadaten von Upstream herunterladen und erstellen. Nach Abschluss des Builds werden Package, Image und SDK als Ergebnisse bereitgestellt.

<p align="center">
    <img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20D3-G/Software/2.1%20yocto%20project%20task%20process.png", width="700">
</p>
<p align="center"><strong>Abbildung 3.1 Task-Prozess des Yocto Project</strong></p>

<br/><br/>

## 3.4 Aufbau des D3-G SDK
---
Im Folgenden sind die Komponenten des von uns konfigurierten Yocto Project aufgeführt.
Tabelle 3.1 zeigt den Aufbau des D3-G SDK.



**Tabelle 3.1 Aufbau des D3-G SDK**
<table border="1" cellspacing="0" cellpadding="5">
  <colgroup>
    <col style="width: 10%">
    <col style="width: 10%">
    <col style="width: 10%">
    <col style="width: 56%">
  </colgroup>
  <thead>
    <tr>
      <th colspan="3"style="text-align: center; vertical-align: middle;"><strong>Element</strong></th>
      <th style="text-align: center; vertical-align: middle;" ><strong>Beschreibung</strong></th>
    </tr>
  </thead>
  <tbody>
  <tr>
      <td colspan="3"style="text-align: center; vertical-align: middle;">easy-setup.sh</td>
      <td>Python-Skript zum automatischen Herunterladen und Erstellen des SDK</td>
    </tr>
    <tr>
      <td colspan="3"style="text-align: center; vertical-align: middle;">stitch-fai-ai.sh</td>
      <td>Skript zum Erstellen von AI-G fai-Images (minimal + Beispielanwendung)</td>
    </tr>
    <tr>
      <td colspan="3"style="text-align: center; vertical-align: middle;">stitch-fai-d3.sh</td>
      <td>Skript zum Erstellen von D3-G fai-Images (minimal + Beispielanwendung)</td>
    </tr>
    <tr>
      <td colspan="3"style="text-align: center; vertical-align: middle;">mktcimg</td>
      <td rowspan="2">Werkzeuge im Zusammenhang mit dem Build-Prozess und <strong>FWDN</strong></td>
    </tr>
    <tr>
      <td colspan="3"style="text-align: center; vertical-align: middle;">tools</td>
    </tr>
    <tr>
      <td rowspan="8"style="text-align: center; vertical-align: middle;">poky</td>
      <td colspan="2"style="text-align: center; vertical-align: middle;">poky</td>
      <td>Yocto Project 4.0 Kirkstone Build-System</td>
    </tr>
    <tr>
      <td colspan="2"style="text-align: center; vertical-align: middle;">meta-openembedded</td>
      <td>Layer, der OE-Core unterstützt</td>
    </tr>
    <tr>
      <td colspan="2"style="text-align: center; vertical-align: middle;">meta-arm</td>
      <td>Layer, der die ARM-Toolchain unterstützt</td>
    </tr>
    <tr>
      <td colspan="2"style="text-align: center; vertical-align: middle;">meta-topst-bsp</td>
      <td>Layer, der TOPST BSP unterstützt</td>
    </tr>
    <tr>
      <td colspan="2"style="text-align: center; vertical-align: middle;">meta-gplv2</td>
      <td>Layer, der Pakete enthält, die die GPLv3-Lizenz vermeiden</td>
    </tr>
    <tr>
      <td colspan="2"style="text-align: center; vertical-align: middle;">meta-topst</td>
      <td>TOPST-Rezept</td>
    </tr>
  </tbody>
</table>
<br/><br/><br/>


## 3.5 Vorbereitung des Builds
---
In den folgenden Kapiteln wird beschrieben, wie Sie das Yocto Project konfigurieren, um das D3-G Image zu erstellen.

<br/><br/>

### 3.5.1 Benutzer-E-Mail und Benutzernamen in .gitconfig festlegen
Um das D3-G SDK vom offiziellen TOPST git herunterzuladen, konfigurieren Sie Ihre E-Mail-Adresse und Ihren Namen.
1. Geben Sie den folgenden Befehl ein.
```
vi ~/.gitconfig
```
2. Geben Sie die folgenden Informationen ein
```
[user]
    email = User email
    name = User name
```

<br/><br/>

### 3.5.2 D3-G von Git beziehen

1. Erstellen Sie ein neues Verzeichnis mit dem Namen **topst-sdk** und wechseln Sie in das Verzeichnis **topst-sdk**.

```
$ mkdir topst-sdk
$ cd topst-sdk
```

2. Führen Sie den folgenden Befehl aus, um das Repository zu initialisieren.

```
$ repo init -u https://github.com/topst-development/manifests.git -b release/1.3.0 -m linux_yp4.0_topst.xml
```

Nach dem Ausführen des Befehls wird die folgende Ausgabe angezeigt.

```
Downloading Repo source from https://gerrit.googlesource.com/git-repo

... A new version of repo (2.54) is available.
... New version is available at: /home/topst/topst-sdk/.repo/repo/repo
... The launcher is run from: /usr/bin/repo
!!! The launcher is not writable.  Please talk to your sysadmin or distro
!!! to get an update installed.


Your identity is: TopstDeveloper <topstdeveloper@gmail.com>
If you want to change this, please re-run 'repo init' with --config-name

repo has been initialized in /home/topst/topst-sdk
```

3. Führen Sie den folgenden Befehl aus, um das Repository zu synchronisieren.

```
$ repo sync
```

Nach dem Ausführen des Befehls wird die folgende Ausgabe angezeigt.

```
... A new version of repo (2.54) is available.
... New version is available at: /home/topst/topst-sdk/.repo/repo/repo
... The launcher is run from: /usr/bin/repo
!!! The launcher is not writable.  Please talk to your sysadmin or distro
!!! to get an update installed.

Fetching: 100% (12/12), done in 33.103s
Checking out:  25% (3/12), done in 0.863s
Checking out:  75% (9/12), done in 0.415s
repo sync has finished successfully.
```

<br/><br/><br/>

## 3.6 topst-build.sh ausführen 
---
Wenn Sie das Skript ./easy-setup.sh ausführen, wird der folgende Bildschirm angezeigt. 

**Achtung: Wenn Sie ./easy-setup.sh erneut ausführen, seien Sie vorsichtig, da die erstellten Quellen gelöscht werden, wenn Sie yes auswählen.**
```
./easy-setup.sh
```
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20AI-G/Software/Linux%20SDK/license1.png"></p>
<p align="center"><strong>Abbildung 3.2 Endbenutzer-Lizenzvertrag</strong></p>

Scrollen Sie zum unteren Rand des Bildschirms und lesen Sie diesen Hinweis. Nachdem Sie diesen Hinweis gelesen haben, drücken Sie die Rechtspfeiltaste und [Enter].
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20AI-G/Software/Linux%20SDK/license2.png"></p>
<p align="center"><strong>Abbildung 3.3 Gehen Sie zu 'Proceed to confirm'</strong></p>


Anschließend wird der folgende Bildschirm angezeigt. 
<p align="center"><img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20AI-G/Software/Linux%20SDK/license3.png" ></p>
<p align="center"><strong>Abbildung 3.4 Bestätigungsbildschirm </strong></p>


Das erstellte Image wird unter folgendem Pfad abgelegt:

- {TOPST_PATH}/build/d3-g-topst-main/tmp/deploy/images/d3-g-topst-main

topst-build.sh ist ein Shell-Skript, das die Kernumgebung einrichtet, die zum Erstellen von Images für D3-G und AI-G erforderlich ist. Führen Sie die folgenden Befehle aus und wählen Sie Option 2, um die Build-Umgebung für die Installation des Haupt-Betriebssystems auf dem D3-G vorzubereiten.



```
$ source poky/meta-topst/topst-build.sh 
Choose MACHINE
  1. ai-g-topst
  2. d3-g-topst-main
  3. d3-g-topst-sub
  4. d5-g-topst-main
  5. d5-g-topst-sub
select number(1-5) => 2
machine(d3-g-topst-main) selected.
You had no conf/local.conf file. This configuration file has therefore been
created for you from /home/topst/topst-sdk/poky/meta-topst/template/d3-g-topst-main/local.conf.sample
You may wish to edit it to, for example, select a different MACHINE (target
hardware). See conf/local.conf for more information as common configuration
options are commented.

You had no conf/bblayers.conf file. This configuration file has therefore been
created for you from /home/topst/topst-sdk/poky/meta-topst/template/d3-g-topst-main/bblayers.conf.sample
To add additional metadata layers into your configuration please add entries
to conf/bblayers.conf.

The Yocto Project has extensive documentation about OE including a reference
manual which can be found at:
    https://docs.yoctoproject.org

For more information about OpenEmbedded see the website:
    https://www.openembedded.org/

Yocto Project common targets are:
    core-image-minimal
    core-image-sato
    meta-toolchain
    adt-installer
    meta-ide-support


Telechips common targets are:
    telechips-topst-image-minimal
    telechips-topst-image-multimedia
    telechips-topst-image

    meta-toolchain-topst(Application Development Toolkit)


You can also run generated TOPST images on D3-G board

Other commonly useful commands are:
 - 'devtool' and 'recipetool' handle common recipe tasks
 - 'bitbake-layers' handles common layer tasks
 - 'oe-pkgdata-util' handles common target package tasks

```

Führen Sie den folgenden Befehl aus, um mit dem Erstellen des Haupt-Betriebssystems zu beginnen.
```
$ bitbake telechips-topst-image
```

<br/><br/><br/>

## 3.7 Firmware Downloader (FWDN) Image erstellen 
---
Diese Option kombiniert die Binärdateien zu einem einzigen Image für das D3-G Plattform-Image.

Die Datei **output_d3g.fwdn.zip**, die das **Build-Image 'output_d3g.fai'** und die **FWDN-Tools** enthält, wird unter dem folgenden Pfad erstellt:

-  ~/topst-sdk

```
$ cd ~/topst-sdk

$ ./stitch-fai-d3.sh -f
Filesystem too small for a journal
[mktcimg] v1.2.1 - Nov 15 2021 19:33:18
location : bl3_ca72_a
location : 4096 sector(2097152 byte)
location : build/d3-g-topst-main/tmp/deploy/images/d3-g-topst-main/ca72_bl3.rom
location : boot
location : 122880 sector(62914560 byte)
location : build/d3-g-topst-main/tmp/deploy/images/d3-g-topst-main/tc-boot-d3-g-topst-main.img
location : system
location : 33554432 sector(17179869184 byte)
location : build/d3-g-topst-main/tmp/deploy/images/d3-g-topst-main/telechips-topst-image-d3-g-topst-main.ext4
location : dtb
location : 400 sector(204800 byte)
location : build/d3-g-topst-main/tmp/deploy/images/d3-g-topst-main/tcc8050-topst-d3-g.dtb
path : build/d3-g-topst-main/tmp/deploy/images/d3-g-topst-main/ca72_bl3.rom
uuid : 7eb23c82-ccc0-44ce-8237-3315fc34e3f5 , part-name : bl3_ca72_a
uuid : 1c76ef36-314d-4548-8207-5ab1d1376ca2 , part-name : boot
uuid : b32eb80f-e014-4f17-b140-77bf3e137ba0 , part-name : system
uuid : 429d8444-87b0-4c1d-8b3f-278dec2616f3 , part-name : dtb
crc32 of header : 2a7c0194
crc32 of partition array : b181e432
idx : 0  bl3_ca72_a
idx : 1  boot
idx : 2  system
idx : 3  dtb
crc32 of header : 2a7c0194
crc32 of partition array : 990446d3
Complete to make fai file
 
===== arguments info =====
 
--storage_size : 17818182656
--parttype : gpt
--area_name : "SD Data"
--outfile : /home/topst/topst-sdk/.stitch_tOPE26E/output_d3g.fai
--gptfile : /home/topst/topst-sdk/.stitch_tOPE26E/output_d3g.gpt
--fplist : /home/topst/topst-sdk/.stitch_tOPE26E/partition.single.list
--sector_size : 512
--sparse_fill : 0
 
===========================
 
[+] Packaging FWDN binaries
  adding: boot-firmware/ (stored 0%)
  adding: boot-firmware/boot.dual.json (deflated 87%)
  adding: boot-firmware/prebuilt/ (stored 0%)
  adding: boot-firmware/prebuilt/subcore_optee.rom (deflated 93%)
  adding: boot-firmware/prebuilt/mcert.bin (deflated 96%)
  adding: boot-firmware/prebuilt/fwdn.rom (deflated 49%)
  adding: boot-firmware/prebuilt/bconf.dual.bin (deflated 95%)
  adding: boot-firmware/prebuilt/ca72_bl1.rom (deflated 53%)
  adding: boot-firmware/prebuilt/dram_params.bin (deflated 81%)
  adding: boot-firmware/prebuilt/hsm.cs.bin (deflated 13%)
  adding: boot-firmware/prebuilt/ca72_bl2.rom (deflated 54%)
  adding: boot-firmware/prebuilt/ca53_bl1.rom (deflated 53%)
  adding: boot-firmware/prebuilt/optee.rom (deflated 93%)
  adding: boot-firmware/prebuilt/ca53_bl2.rom (deflated 52%)
  adding: boot-firmware/prebuilt/hsm.bin (deflated 49%)
  adding: boot-firmware/prebuilt/bconf.single.bin (deflated 93%)
  adding: boot-firmware/prebuilt/scfw.rom (deflated 57%)
  adding: boot-firmware/prebuilt/tcc8050_snor.cs.rom (deflated 93%)
  adding: boot-firmware/boot.single.json (deflated 87%)
  adding: boot-firmware/fwdn.json (deflated 50%)
  adding: fwdn (deflated 69%)
  adding: fwdn.bat (deflated 40%)
  adding: fwdn.exe (deflated 62%)
  adding: fwdn.sh (deflated 40%)
  adding: output_d3g.fai (deflated 73%)
  adding: output_d3g.gpt (deflated 99%)
  adding: output_d3g.gpt.back (deflated 98%)
  adding: output_d3g.gpt.prim (deflated 98%)
  adding: VtcUsbPort.dll (deflated 68%)

```

Wenn Sie das folgende Protokoll sehen, bedeutet dies, dass die Datei "output_d3g.fwdn.zip" erstellt wurde. 
```
$ ls
build  easy-setup.sh  mktcimg  output_d3g.fwdn.zip  poky  stitch-fai-ai.sh  stitch-fai-d3.sh  tools
```

</br></br><br/><br/>

# 4. Firmware-Download
---
In diesem Kapitel wird beschrieben, wie Sie mit ***FWDN*** Firmware auf das D3-G herunterladen und sich an der Linux-Konsole anmelden.  
***FWDN V8*** ist ein PC-Tool zum Herunterladen von Firmware sowohl in Windows 10(11) 64-Bit- als auch in Linux-Umgebungen. In diesem Kapitel wird der Fall des Herunterladens in Windows- und Linux-Umgebungen beschrieben.

<br/><br/><br/>

## 4.1 Ablauf des Firmware-Downloads
---
Der Ablauf des Herunterladens mit ***FWDN*** ist wie folgt:

1. Stellen Sie den Boot-Modus-Schalter auf den USB-Boot-Modus.
2. Öffnen Sie eine Windows-Eingabeaufforderung oder eine Linux-Konsole.
3. Verbinden Sie ***FWDN V8*** mit dem Board.
4. Laden Sie die fai-Datei herunter.

<br/><br/><br/>

## 4.2 D3-G-Board und Host-PC im USB-Boot-Modus verbinden
---
Der Firmware Downloader (FWDN) schreibt ein ROM-Image über die USB-Kommunikation mit dem Host-PC auf das D3-G. 

Das D3-G verfügt über eine Boot-Modus-Taste und unterstützt zwei Arten von Boot-Modi. Dieses Handbuch konzentriert sich auf den FWDN-Modus.

- USB-Boot-Modus (FWDN-Modus) : Wird verwendet, um ein ROM-Image mit dem FWDN-Tool auf Ihrem Host-PC zu schreiben 

- eMMC-Boot-Modus : Wird verwendet, um das D3-G mit einem ROM-Image zu starten, das auf einem eMMC-Gerät gespeichert ist 

**Hinweis**: Der USB-Type-C-FWDN-Anschluss wird für den Firmware Downloader (FWDN) verwendet. 



Um FWDN zu verwenden, verbinden Sie das D3-G-Board wie folgt mit dem Host-PC: 

1. Prüfen Sie, ob der VTC-Treiber auf dem Host-PC installiert ist. Falls der VTC-Treiber nicht installiert ist, installieren Sie ihn wie in Kapitel 4.2.1 beschrieben.  

2. Halten Sie ein USB-Type-C-Kabel bereit. 

3. Um in den USB-Boot-Modus zu gelangen, schließen Sie das Stromkabel an das D3-G-Board an, während Sie den FWDN-Schalter gedrückt halten.
   - Weitere Informationen finden Sie unter **"2. Boot-Modus"** im Abschnitt Hardware der Seitenleiste.

4. Verbinden Sie das USB-Type-C-Kabel mit dem USB-Type-C-FWDN-Anschluss auf dem D3-G-Board und dem Host-PC. 

<p align="center">
    <img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20D3-G/Hardware/connect%20to%20d3g%20to%20host%20pc%20using%20c%20type.png">
</p>
<p align="center"><strong>Abbildung 4.1 Verbindung des D3-G-Boards mit dem Host-PC über ein USB-C-Type-Kabel </strong></p>

<br/><br/>

### 4.2.1 So installieren Sie den VTC-Treiber (Windows/Ubuntu)
Installieren Sie den Vendor Telechips Certification (VTC) Treiber (zu finden unter [telechips driver](https://drive.google.com/file/d/1muQnY8kuKxDsy3p3FUiQqcG34Zjk-mnR/view?usp=sharing)) auf dem Host-PC, indem Sie ihn als Administrator ausführen. Wenn Sie den USB im FWDN-Modus wie oben gezeigt anschließen, wird der Telechips VTC USB-Treiber wie in Abbildung 4.2 und Abbildung 4.3 dargestellt eingerichtet.

<p align="center">
    <img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20D3-G/Software/USB%20Connection%20in%20Windows%20Environment.png", width="700">
</p>
<p align="center"><strong>Abbildung 4.2 USB-Verbindung in der Windows-Umgebung</strong></p>

<p align="center">
    <img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20D3-G/Software/USB%20Connection%20in%20Linux%20System.png", width="700">
</p>
<p align="center"><strong>Abbildung 4.3 USB-Verbindung in der Linux-Umgebung</strong></p>  

**Hinweis**: Verwenden Sie den VTC-Treiber V5.0.0.14 oder höher. Um die Version zu überprüfen, sehen Sie im Geräte-Manager in der Windows-Umgebung nach.  

<br/><br/><br/>

## 4.3 Vorbereitung für den FWDN-Download
---
Bevor Sie FWDN ausführen, übertragen Sie das Image und die Tools, die in der Ubuntu-(WSL2)-Umgebung erstellt wurden, in die Windows-Umgebung.


1. Entpacken Sie "output_d3g.fwdn.zip".   
    ```
    $ cd ~/topst-sdk
    $ mkdir images
    $ mv ./output_d3g.fwdn.zip ./images
    $ cd images
    $ unzip output_d3g.fwdn.zip
    ```
2. Kopieren Sie den Ordner "images" auf das Windows-Laufwerk C.  
    ```
    $ cd ..
    $ cp -r ./images /mnt/c/
    ```

<br/><br/><br/>

## 4.4 FWDN in der Windows-Umgebung
---
1. Führen Sie Powershell aus und wechseln Sie zu "C:\images\".
```
$ cd C:\images 
```

2. Geben Sie den Befehl **.\fwdn.bat** ein, um den Firmware-Download zu starten. Die „fwdn.bat“ ist eine ausführbare Datei, die automatisch Firmware mithilfe von FWDN V8 herunterlädt. 

```
.\fwdn.bat

C:\images>fwdn.exe --fwdn boot-firmware\fwdn.json
[main:30] FWDN V8 v1.4.6 - 2021.12.13 13:42:37
[FWDN_V8::LoadFWDNRom:403] Start to load FWDN rom
[FWDN_V8::LoadMCERT:592] C:\images\boot-firmware\mcert.bin
[FWDN_V8::LoadHSM:609] C:\images\boot-firmware\hsm.cs.bin
[FWDN_V8::SendFWDNHeader:634] C:\images\boot-firmware\fwdn.rom - Header
[FWDN_V8::SendFWDNBody_V8:537] C:\images\boot-firmware\fwdn.rom - Body
[FWDN_V8::LoadFWDNRom:414] Complete to load FWDN rom
[FWDN_V8::GetFWDNRomVersion:1526] fwdn.rom version : 21.9.29
[FWDN_V8::GetFileAndWriteCommand:748] C:\images\boot-firmware\dram_params.bin
[FWDN_V8::PrintDeviceInfo:1183] --------------Device info-------------
[FWDN_V8::PrintDeviceInfo:1184]

----- Detail of Storages -----
#### eMMC Info ####
Manufacture ID: 0x15
OEM: 0x100
Name: 8GTF4
User Capacity: 7.3 GiB (7818182656 Byte)
Boot Capacity: 4 MiB (4194304 Byte)
RPMB Capacity: 512 KiB (524288 Byte)
Speed Mode: HS200
#### SNOR Info ####
Manufacture ID: 0xc2
Device ID: 0x2016
Name: MXIC-MX25L3233F
Sector Size: 4 KiB (4096 Byte)
Total Capacity: 4 MiB (4194304 Byte)
4Byte Address Mode: Unsupported

----- Summary of Storages -----
eMMC : O
SNOR : O
UFS : X
- O : Init success
- X : Init failed or not exist

----- Summary of DRAM Init -----
DRAM Init : Success (Result 0x0 )
DRAM Size : 4096MB

[FWDN_V8::PrintDeviceInfo:1185] --------------------------------------
[main:142] Complete FWDN
[FWDNLogger::PrintCurTime:111] 24/04/25-09:57:47

C:\images>fwdn.exe --storage emmc --low-format
[main:30] FWDN V8 v1.4.6 - 2021.12.13 13:42:37
[FWDN_V8::GetFWDNRomVersion:1526] fwdn.rom version : 21.9.29
[FWDN_V8::LowformatCommand:1352] Start low-format
[FWDN_V8::LowformatCommand:1353] low-format can take a long time
[FWDN_V8::LowformatCommand:1382] Complete low-format
[main:142] Complete FWDN
[FWDNLogger::PrintCurTime:111] 24/04/25-09:57:50

C:\images>fwdn.exe -w boot-firmware\boot.single.json
[main:30] FWDN V8 v1.4.6 - 2021.12.13 13:42:37
[FWDN_V8::GetFWDNRomVersion:1526] fwdn.rom version : 21.9.29
[main:117] Start write command
[FWDN_V8::GetFileAndWriteCommand:748] C:\images\boot-firmware\bconf.single.bin
[FWDN_V8::GetFileAndWriteCommand:748] C:\images\boot-firmware\bconf.single.bin
[FWDN_V8::GetFileAndWriteCommand:748] C:\images\boot-firmware\mcert.bin
[FWDN_V8::GetFileAndWriteCommand:748] C:\images\boot-firmware\mcert.bin
[FWDN_V8::GetFileAndWriteCommand:748] C:\images\boot-firmware\dram_params.bin
[FWDN_V8::GetFileAndWriteCommand:748] C:\images\boot-firmware\dram_params.bin
[FWDN_V8::GetFileAndWriteCommand:748] C:\images\boot-firmware\hsm.cs.bin
[FWDN_V8::GetFileAndWriteCommand:748] C:\images\boot-firmware\hsm.cs.bin
[FWDN_V8::GetFileAndWriteCommand:748] C:\images\boot-firmware\scfw.rom
[FWDN_V8::GetFileAndWriteCommand:748] C:\images\boot-firmware\scfw.rom
[FWDN_V8::GetFileAndWriteCommand:748] C:\images\boot-firmware\optee.rom
[FWDN_V8::GetFileAndWriteCommand:748] C:\images\boot-firmware\optee.rom
[FWDN_V8::GetFileAndWriteCommand:748] C:\images\boot-firmware\ca72_bl1.rom
[FWDN_V8::GetFileAndWriteCommand:748] C:\images\boot-firmware\ca72_bl1.rom
[FWDN_V8::GetFileAndWriteCommand:748] C:\images\boot-firmware\ca53_bl1.rom
[FWDN_V8::GetFileAndWriteCommand:748] C:\images\boot-firmware\ca53_bl1.rom
[FWDN_V8::GetFileAndWriteCommand:748] C:\images\boot-firmware\ca72_bl2.rom
[FWDN_V8::GetFileAndWriteCommand:748] C:\images\boot-firmware\ca72_bl2.rom
[FWDN_V8::GetFileAndWriteCommand:748] C:\images\boot-firmware\ca53_bl2.rom
[FWDN_V8::GetFileAndWriteCommand:748] C:\images\boot-firmware\ca53_bl2.rom
[main:125] Complete write command
[main:142] Complete FWDN
[FWDNLogger::PrintCurTime:111] 24/04/25-09:57:53
100% [||||||||||||||||||||||||||||||] 859264/859264
C:\images>fwdn.exe -w "output_d3g.fai" --storage emmc --area user
[main:30] FWDN V8 v1.4.6 - 2021.12.13 13:42:37
[FWDN_V8::GetFWDNRomVersion:1526] fwdn.rom version : 21.9.29
[main:117] Start write command
[FWDN_V8::GetFileAndWriteCommand:748] output_d3g.fai
[main:125] Complete write command
[main:142] Complete FWDN
[FWDNLogger::PrintCurTime:111] 24/04/25-10:05:21
100% [||||||||||||||||||||||||||||||] 7238688960/7238688960
** When writing FAI files without low-format, there may be garbage values in partition where data is not written.
```

<br/><br/><br/>

## 4.5  FWDN in der Linux-Umgebung
---
Um das D3-G Image unter Linux herunterzuladen, führen Sie den folgenden Befehl aus: "./fwdn.sh".

```
$ ./fwdn.sh
```

Sie sind bereit, das D3-G zu starten. Weitere Informationen zum Beginn der Kommunikation mit dem Gerät finden Sie in Kapitel 5.


<br/><br/><br/><br/>

# 5. Verbinden des D3-G-Boards mit einem Host-PC
---
In diesem Kapitel wird erläutert, wie Sie den Host-PC über UART mit dem D3-G-Board verbinden, um Firmware herunterzuladen und seriell zu kommunizieren.

<br/><br/><br/>

## 5.1 Verbindung des D3-G-Boards über UART 
---
Führen Sie die folgenden Schritte aus und überprüfen Sie über die UART-Verbindung, ob der Firmware-Download erfolgreich abgeschlossen wurde. 

1. Installieren Sie den Treiber für die serielle Schnittstelle (zum Beispiel CP210x Windows Driver) und den PL2303_prolific-Treiber in der Windows-Umgebung. 
2. Installieren Sie einen Terminal-Emulator wie Tera Term oder PuTTY. 
3. Verbinden Sie den Host-PC und den UART-Pin auf dem D3-G-Board. Verwenden Sie ein USB-zu-TTL-Kabel. 
4. Verbinden Sie das schwarze Kabel mit dem GND-Pin. 
5. Schließen Sie das weiße Kabel (RXD) an den TX-Pin der UART-Pins an und das grüne Kabel (TXD) an den RX-Pin der UART-Pins.
6. Starten Sie die Terminal-Emulator-Anwendung.
7. Öffnen Sie den Geräte-Manager auf Ihrem PC und überprüfen Sie die dem UART-Gerät zugewiesene Portnummer.
8. Geben Sie im Terminal-Emulator die überprüfte Portnummer in das Feld Serial line ein. Setzen Sie **Speed** (bps) auf 115200 und **Flow control** auf **None.**
9. Schließen Sie das Stromkabel an. Anschließend startet das D3-G-Board im standardmäßigen eMMC-Boot-Modus.


 
<p align="center">
    <img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20D3-G/Software/USB%20to%20TTL%20Connection.png", width="700">
</p>
<p align="center"><strong>Abbildung 5.1 UART-Verbindung mit dem Host-PC</strong></p><br/>  


Abbildung 5.2 zeigt eine erfolgreiche Anmeldung.  
Sowohl der Benutzername als auch das Passwort für die Anmeldung sind auf **root** festgelegt.

<p align="center">
    <img src="https://raw.githubusercontent.com/topst-development/Documentation/refs/heads/main/Assets/TOPST%20D3-G/Software/d3-g%20login%20as%20root.png", width="700">
</p>
<p align="center"><strong>Abbildung 5.2 Verbundener Bildschirm (ID und Passwort lauten topst)</strong></p><br/>

<br/><br/><br/>

# 6. Größenänderung der Ubuntu-OS-Partition
---
Wir stellen auch ein Ubuntu-Betriebssystem bereit.
Wenn Sie diesem Kapitel folgen, können Sie das Ubuntu-Image herunterladen, es auf das Board hochladen und die zugewiesene eMMC-Speicherkapazität erweitern.

<br/><br/><br/>

## 6.1 Ubuntu-Image herunterladen
---
Die offizielle Version des D3-G basiert auf Ubuntu 22.04.  
Sie können die Image-Datei hier herunterladen.  

<img src="https://github.com/topst-development/Documentation/assets/161264431/83d93c78-6437-4f96-a0bf-23f22da1aba1">  

**Download :**  
-	[Download-Link hier](https://drive.google.com/file/d/1oc2qwaXUt6-QDME3s5WXKVHzAg4xqVyc/view?usp=drive_link)
<br>
-	Weitere Informationen finden Sie auf unserer [GitHub-Seite](https://github.com/topst-development).

**Versionshinweise :**  

|Ver|   Datum   |
|:-:|:--------:|
|1.0|2024.04.25|  

Das TOPST-Team bereitet auch weitere offizielle OS-Versionen vor.  
Informationen zu Releases anderer Betriebssysteme finden Sie in der TOPST-Community.  

<br/><br/><br/>

## 6.2 Firmware-Upload auf das D3-G
---
Führen Sie die Datei „fwdn_ubuntu.batch“ aus. 
Informationen zum Hochladen des Ubuntu-Images auf das D3-G finden Sie in Kapitel 5.
Entfernen Sie nach Abschluss von FWDN das USB-Type-C-Kabel vom FWDN-Anschluss und ziehen Sie das Stromkabel ab. 

<br/><br/><br/>

## 6.3 Größe des eMMC-Speichers ändern (nur D3-G)
---
Nach dem Anmelden und Starten des Boards wird empfohlen, zuerst die Größe des eMMC-Speichers zu ändern.
Führen Sie die folgenden Schritte aus, um die Größe des eMMC-Speichers zu ändern.

1. Um die Partitionsgröße und das Layout zu ändern, verwenden Sie den folgenden Befehl.
     ```
     $ parted
     ```

2. Erweitern Sie die GUID Partition Table(GPT). 
    ```
    $ rescue
    $ Fix 
    $ 0 
    $ 100%
    ```
3. Verwenden Sie den Befehl p (print), um zu überprüfen, ob der Partitionstyp ext4 ist. 
   ```
   $ p
   ```
4. Ändern Sie die Größe von Partition 4.
    ```
    $ resizepart 4
    $ Yes
    $ 100%
    ```
5. Starten Sie das Board neu.
6. Ändern Sie die Größe des ext4-Dateisystems auf Partition 4.
    ```
    $ resize2fs /dev/mmcblk0p4
    ```
7. Überprüfen Sie die geänderte Partitionsgröße mit dem folgenden Befehl.
   ```
   $ df -h
   ```

Sie können bestätigen, dass der verfügbare Speicherplatz nach der Größenänderung 27GB beträgt.

<br/><br/><br/><br/>

# 7. Referenzen
---
- Kontaktieren Sie TOPST für weitere Einzelheiten: topst@topst.ai

**Hinweis:** Referenzdokumente können, sofern verfügbar, je nach Vertragsbedingungen bereitgestellt werden. Wenn die Referenzdokumente
nicht verfügbar sind, können die Inhalte, die sich direkt auf Ihre Entwicklung beziehen, erläutert werden.
