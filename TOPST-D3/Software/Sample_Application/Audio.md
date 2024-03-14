# Audio Example

```c
#include <stdio.h>
#include <stdlib.h>

int main (void)
{
        int re;

        printf("Recording for 3 seconds\n");
        if (re = system("arecord -f S16_LE -d 3 -c 2 -r 16000 --device=\"hw:0,0\" ./test-mic.wav\n") < 0) {
                printf("Record failed, error code : %d\n", re);
        }

        printf("playing\n");
        if (re = system("aplay ./test-mic.wav\n") < 0) {
                printf("Play failed, error code : %d\n", re);
        }

        if ( re = system("rm -rf test-mic.wav\n") < 0 ) {
                printf("Remove failed, error code : %d\n", re);
        }
        printf("Closing\n");

        return 0;
}

```


An example was made by using a demo program based on Advanced Linux Sound Architecture (ALSA) for audio testing of the board.

(bb PATH: ./poky/meta-telechips/meta-ivi/recipes-applications/telechips-automotive-linux/audio-example_1.0.0.bb)

The example program records sound for 3 seconds and plays the recorded sound.

```bash
$
```
<p align="center">
    <img src="https://github.com/Topst-Dev/Documentation/assets/144076415/bc5def05-31bd-462b-8401-a1c14542eb02" width="800" height="100">
</p>
<p align="center"><strong>Figure 1.1 Audio Example</strong></p>

```bash
$ man aplay

arecord, aplay - command-line sound recorder and player for ALSA soundcard driver

arecord [flags] [filename]
aplay [flags] [filename [filename]] ...

```

**Description**

**arecord** is a command-line sound file recorder for the ALSA soundcard driver. **arecord** supports several file formats and multiple soundcards with multiple devices. When recording with interleaved mode samples, the file is automatically split before the 2 GB file size.

**aplay** is almost the same as **arecord**, except it plays sound instead of recording. For supported sound file formats, the sampling rate, bit depth, and so forth can be automatically determined from the sound file header.

If the filename is not specified, the standard output or input is used. The **aplay** utility accepts multiple filenames.

<table align="center">
  <tr>
    <th>Option</th>
    <th>Description</th>
  </tr>
  <tr>
    <td>-h, --help</td>
    <td><li><strong>Help: show syntax</strong></td>
  </tr>
  <tr>
    <td>--version </td>
    <td><li><strong>Print current version</strong></td>
  </tr>
  <tr>
    <td>-l, --list-devices</td>
    <td><li><strong>List all soundcards and digital audio devices</strong></td>
  </tr>
  <tr>
    <td>-L, --list-pcms</td>
    <td><li><strong>List all PCMs defined</strong></td>
  </tr>
  <tr>
    <td>-D, --device=NAME</td>
    <td><li><strong>Select PCM by name</strong></td>
  </tr>
  <tr>
    <td>-q --quiet</td>
    <td><li><strong>Quiet mode. Suppress messages (not sound)</strong></td>
  </tr>
  <tr>
    <td>-t, --file-type TYPE</td>
    <td><li><strong>File type (voc, wav, raw or au). If this parameter is omitted, the WAVE format is used.</strong></td>
  </tr>
  <tr>
    <td>-c, --channels=#</td>
    <td><li><strong>The number of channels. The default is one channel.</strong> <li><strong>Valid values are 1 through 32.</strong></td>
  </tr>
  <tr>
    <td>-f, --format=FORMAT</td>
    <td>
      <li><strong>Sample format</strong>
      <li><strong>Recognized sample foramts are:</strong><br>
          <pre>
  - S8
  - U8 
  - S16_LE
  - S16_BE
  - U16_LE
  - U16_BE
  - S24_LE
  - S24_BE
  - U24_LE
  - U24_BE
  - S32_LE
  - S32_BE
  - U32_LE
  - U32_BE
  - FLOAT_LE
  - FLOAT_BE
  - FLOAT64_LE
  - FLOAT64_BE
  - IEC958_SUBFRAME_LE
  - IEC958_SUBFRAME_BE
  - MU_LAW
  - A_LAW
  - IMA_ADPCM
  - MPEG
  - GSM
  - SPECIAL
  - S24_3LE
  - S24_3BE
  - U24_3LE
  - U24_3BE
  - S20_3LE
  - S20_3BE
  - U20_3LE
  - U20_3BE
  - S18_3LE
  - S18_3BE
  - U18_3LE
  - <strong>Some of these formats may not be available on selected hardware.</strong>
      </pre>
      <li><strong>The available format shortcuts are:</strong><br>
      <pre>
  <strong>-f cd (16-bit little-endian, 44100, stereo) [-f S16_LE -c2 -r44100]</strong>
  <strong>-f cdr (16-bit big-endian, 44100, stereo) [-f S16_BE -c2 -f44100]</strong>
  <strong>-f dat (16-bit little-endian, 48000, stereo) [-f S16_LE -c2 -r48000]</strong>
      </pre>
      <li><strong>If no format is given, U8 is used.</strong>
    </td>
  </tr>
  <tr>
    <td>-r, --rate=#<Hz></td>
    <td><li><strong>Sampling rate in Hz. The default rate is 8000 Hz. If the value specified is less than 300, it is taken as the rate in kHz. Valid values are 2000 through 192000 Hz.</strong></td>
  </tr>
  <tr>
    <td>-d, --duration=#</td>
    <td><li><strong>Interrupt after # seconds. A value of zero means infinity. The default is zero, so if this option is omitted, then the arecord process will run until it is killed.</strong></td>
  </tr>
  <tr>
    <td>-s, --sleep-min=#</td>
    <td><li><strong>Minimum ticks to sleep. The default is not to sleep.</strong></td>
  </tr>
  <tr>
    <td>-M, --mmap</td>
    <td><li><strong>Use memory-mapped (mmap) I/O mode for the audio stream. If this option is not set, the read/write I/O mode will be used.</strong></td>
  </tr>
  <tr>
    <td>-N, --nonblock</td>
    <td><li><strong>Open the audio device in non-blocking mode. If the device is busy, the program will exit immediately. If this option is not set, the program will until the audio device is available again.</strong></td>
  </tr>
  <tr>
    <td>-F, --period-time=#</td>
    <td><li><strong>Distance between interrupts is # microseconds. If no period time and no period size is given, then a quarter of the buffer time is set.</strong></td>
  </tr>
  <tr>
    <td>-B, --buffer-time=#</td>
    <td><li><strong>Buffer duration is # microseconds. If no buffer time and no buffer size is given, then the maximum allowed buffer time that is not more than 500 ms is set.</strong></td>
  </tr>
  <tr>
    <td>--period-size=#</td>
    <td><li><strong>Distance between interrupts is # frames. If no period size and no period time is given, then a quarter of the buffer size is set.</strong></td>
  </tr>
  <tr>
    <td>--buffer-size=#</td>
    <td><li><strong>Buffer duration is # frames. If no buffer time and no buffer size is given, then the maximal allowed buffer time that is not more than 500 ms is set.</strong></td>
  </tr>
  <tr>
    <td>-A, --avail-min=#</td>
    <td><li><strong>Minimum available space for wakeup is # microseconds.</strong></td>
  </tr>
  <tr>
    <td>-R, --start-delay=#</td>
    <td><li><strong>Delay for automatic PCM start is # microseconds (relative to buffer size if <= 0)</strong></td>
  </tr>
  <tr>
    <td>-T, --stop-delay=#</td>
    <td><li><strong>Delay for automatic PCM stop is # microseconds from xrun</strong></td>
  </tr>
  <tr>
    <td>-v, --verbose</td>
    <td><li><strong>Show PCM structure and setup. This option is accumulative. The VU meter is displayed when is given twice or three times.</strong></td>
  </tr>
  <tr>
    <td>-V, --vumeter=TYPE</td>
    <td><li><strong>Specify the VU-meter type, either stereo or mono. The stereo VU-meter is available only for 2-channel stereo samples with interleaved format.</strong></td>
  </tr>
  <tr>
    <td>-I, --separate-channels</td>
    <td><li><strong>One file for each channel. This option disables max-file-time and use-strftime, and ignores SIGUSR1. The stereo VU meter is not available with separate channels.</strong></td>
  </tr>
  <tr>
    <td>-P</td>
    <td><li><strong>Playback. This is the default if the program is invoked by typing aplay.</strong></td>
  </tr>
  <tr>
    <td>-C</td>
    <td><li><strong>Record. This is the default if the program is invoked by typing arecord.</strong></td>
  </tr>
  <tr>
    <td>-i, --interactive</td>
    <td><li><strong>Allow interactive operation via stdin. Currently only pause/resume via space or enter key is implemented.</strong></td>
  </tr>
  <tr>
    <td>--disable-resample</td>
    <td><li><strong>Disable automatic rate resample.</strong></td>
  </tr>
  <tr>
    <td>--disable-channels</td>
    <td><li><strong>Disable automatic channel conversions</strong></td>
  </tr>
  <tr>
    <td>--disable-format</td>
    <td><li><strong>Disable automatic format conversions.</strong></td>
  </tr>
  <tr>
    <td>--disable-softvol</td>
    <td><li><strong>Disable software volume control (softvol)</strong></td>
  </tr>
  <tr>
    <td>--test-position</td>
    <td><li><strong>Test ring buffer position</strong></td>
  </tr>
  <tr>
    <td>--test-coef=<coef></td>
    <td><li><strong>Test coefficient for ring buffer position; default is 8. Expression for validation is: coef * (buffer_size / 2). Minimum value is 1</strong></td>
  </tr>
  <tr>
    <td>--test-nowait</td>
    <td><li><strong>Do not wait for the ring buffer--eats the whole CPU</strong></td>
  </tr>
  <tr>
    <td>--max-file-time</td>
    <td><li><strong>When recording and the output file has recorded sound for the maximum file time, close the output file and open a new output file. The default is the maximum size supported by the file format: 2 GB for WAV files. This option has no effect if --separate-channels is specified.</strong></td>
  </tr>
  <tr>
    <td>--process-id-file <file name></td>
    <td><li><strong>aplay writes its process ID here, so other programs can send signals to it.</strong></td>
  </tr>
  <tr>
    <td>--use-strftime</td>
    <td><li><strong>When recording, interpret %-codes in the file name parameter by using the strftime facility whenever the output file is opened. The important strftime codes are: </strong>
    <pre>
- <strong>%Y: year</strong>
- <strong>%m: month</strong>
- <strong>%d: day of the month</strong>
- <strong>%H: hour</strong>
- <strong>%M: minute</strong>
- <strong>%S: second</strong>
    </pre>
    </td>
  </tr>
  <tr>
    <td>--dump-hw-params</td>
    <td><li><strong>Dump hw_params of the device’s preconfigured status to stderr. The dump lists capabilities of the selected device, such as supported formats, sampling rates, numbers of channels, period and buffer bytes, sizes, and times. For raw device hw:X, this option basically lists hardware capabilities of the soundcard.</strong></td>
  </tr>
  <tr>
    <td>--fatal-errors</td>
    <td><li><strong>Disables recovery attempts when errors (for example, xrun) are encountered; the aplay process instead aborts immediately.</strong></td>
  </tr>
</table>

**Signals**

When recording, SIGINT, SIGTERM and SIGABRT will close the output file and exit. SIGUSR1 will close the output file, open a new one, and continue recording. However, SIGUSR1 does not work with **--separate-channels**.

**Examples**

- **aplay -c 1 -t raw -r 22050 -f mu_law foobar**
    - Will play the raw file "foobar" as a 22050-Hz, mono, 8-bit, Mu-Law .au file.
- **arecord -d 10 -f cd -t wav -D copy foobar.wav**
    - Will record foobar.wav as a 10-second, CD-quality wave file, using the PCM "copy" (which might be defined in the user's .asoundrc file as:
    
    ```
    pcm.copy {
      type plug
      slave {
        pcm hw
      }
      route_policy copy
    }
    ```
    
- **arecord -t wav --max-file-time 30 mon.wav**
    
    Record from the default audio source in monaural, 8,000 samples per second, 8 bits per sample. Start a new file every  30 seconds. File names are mon-nn.wav, where **nn** increases from 01. The file after mon-99.wav is mon-
    
- **arecord -f cd -t wav --max-file-time 3600 --use-strftime %Y/%m/%d/listen-%H-%M-%v.wav**
    
    Record in stereo from the default audio source. Create a new file every hour. The files are placed in directories based on their start dates and have names which include their start times and file numbers.

## 1.1 I2S

Integrated Interchip Sound (I2S) is a communication protocol established by Philips (now NXP) to transmit and receive audio data. I2C was created to transmit and receive data to and from the integrated circuits (ICs) in the printed circuit board (PCB), but I2S was created only to deal with the audio ICs and data transmissions inside the PCB.

I2S is a communication protocol that allows audio D/A Converter IC (MAX98357, PCM5100) to output digital sound source files through speakers by transmitting data with clock.
