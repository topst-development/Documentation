# 1 Software Architecture

Figure 1.1 shows the software architecture of the TCC8050. The three cores consist of the following features, each of which exchanges information over the IPC.

The TCC8050 uses the CA72 (main core) to provide multimedia functionality, and the CA53 (sub-core) provides immediate processing of the main core during operation (for example, rear camera). The CR5 provides a real-time OS to provide the capabilities used to communicate with a car.

<p align="center">
    <img src="https://github.com/Topst-Dev/Documentation/assets/144076415/b561c6cf-5e8c-43db-b9a0-70dd1c871b62" width="1050" height="700">
</p>
<p align="center"><strong>Figure 1.1 TCC8050 Software Architecture</strong></p>
