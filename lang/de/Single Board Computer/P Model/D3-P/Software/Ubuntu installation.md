# 1. Einleitung
In diesem Dokument wird beschrieben, wie Sie die Ubuntu-Umgebung im Hauptkern (CA72) des TOPST D3 (Open-Platform-Board) entwickeln. Neben dem auf dem Board bereitgestellten nativen Ubuntu-Image wird in diesem Dokument beschrieben, wie Sie Ihre eigene spezialisierte Ubuntu-Umgebung entwickeln. Von Benutzern erstellte Ubuntu-Dateisysteme können mit dem Werkzeug **_FWDN_** in den Dateisystembereich des Hauptkerns (CA72) heruntergeladen werden.

Dieses Dokument ist in der folgenden Reihenfolge aufgebaut:
* Anleitung zur Erstellung des Ubuntu-Dateisystems
* FWDN-Anleitung
* Gebooteter Ubuntu-GUI-Bildschirm 
  
<br><br>

# 2. Anleitung zur Erstellung des Ubuntu-Dateisystems

In diesem Kapitel wird beschrieben, wie Sie das Ubuntu-Dateisystem für den Hauptkern (CA72) auf dem Host-PC installieren.

Informationen zur Entwicklungsumgebung des Benutzers finden Sie unter „Documentation/TOPST-D3/Software/SDK/LINUX“.

<br><br>

## 2.1. Ubuntu mit Git beziehen
Die über Git bereitgestellte Ubuntu-Version ist Ubuntu 22.04.2 LTS (Jammy Jellyfish), wie unten gezeigt.

```
$ git clone https://gitlab.com/topst.ai/topst-d3-ubuntu.git
```

<br><br>

# 3. Skript ausführen


Führen Sie 'populate_ubuntu.sh' aus.
```
$ sudo ./populate_ubuntu.sh 
[!] Prepare workspace
[!] Initial debian bootstraping
I: Retrieving InRelease 
I: Checking Release signature
I: Valid Release signature (key id F6ECB3762474EDA9D21B7022871920D1991BC93C)
I: Retrieving Packages 
I: Validating Packages 
I: Resolving dependencies of required packages...
I: Resolving dependencies of base packages...
I: Checking component main on http://ports.ubuntu.com/ubuntu-ports...
I: Retrieving adduser 3.118ubuntu5
I: Validating adduser 3.118ubuntu5
I: Retrieving apt 2.4.5
I: Validating apt 2.4.5
I: Retrieving apt-utils 2.4.5
I: Validating apt-utils 2.4.5
I: Retrieving base-files 12ubuntu4
I: Validating base-files 12ubuntu4
I: Retrieving base-passwd 3.5.52build1
I: Validating base-passwd 3.5.52build1
I: Retrieving bash 5.1-6ubuntu1
I: Validating bash 5.1-6ubuntu1
I: Retrieving bsdutils 1:2.37.2-4ubuntu3
I: Validating bsdutils 1:2.37.2-4ubuntu3
I: Retrieving ca-certificates 20211016
I: Validating ca-certificates 20211016
I: Retrieving console-setup 1.205ubuntu3
I: Validating console-setup 1.205ubuntu3
I: Retrieving console-setup-linux 1.205ubuntu3
I: Validating console-setup-linux 1.205ubuntu3
I: Retrieving coreutils 8.32-4.1ubuntu1
I: Validating coreutils 8.32-4.1ubuntu1
I: Retrieving cron 3.0pl1-137ubuntu3
I: Validating cron 3.0pl1-137ubuntu3
I: Retrieving dash 0.5.11+git20210903+057cd650a4ed-3build1
I: Validating dash 0.5.11+git20210903+057cd650a4ed-3build1
I: Retrieving dbus 1.12.20-2ubuntu4

                   ㆍ
                   ㆍ
                   ㆍ
```
Sie können die etx4-Datei wie unten gezeigt prüfen.
```
$ ls
populate_ubuntu.sh  src  ubuntu.ext4
```


