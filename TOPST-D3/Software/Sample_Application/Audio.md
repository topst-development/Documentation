# 1 Audio Example

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

<div style="display: flex; justify-content: center;">
    <img src="https://github.com/Topst-Dev/Documentation/assets/144076415/bc5def05-31bd-462b-8401-a1c14542eb02" width="500" height="350" style="margin: auto;">
</div>
<p align="center"><strong>Figure 2.1 Audio Example</strong></p

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

| Options | Description |
| --- | --- |
| -h, --help | Help: show syntax |
| --version | Print current version |
| -l, --list-devices | List all soundcards and digital audio devices |
| -L, --list-pcms | List all PCMs defined |
| -D, --device=NAME | Select PCM by name |
| -q --quiet | Quiet mode. Suppress messages (not sound) |
| -t, --file-type TYPE | File type (voc, wav, raw or au). If this parameter is omitted, the WAVE format is used. |
| -c, --channels=# | The number of channels. The default is one channel. 
Valid values are 1 through 32. |
| -f --format=FORMAT | Sample format
Recognized sample formats are: 
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
Some of these formats may not be available on selected hardware.
The available format shortcuts are:
  -f cd (16-bit little-endian, 44100, stereo) [-f S16_LE -c2 -r44100]
  -f cdr (16-bit big-endian, 44100, stereo) [-f S16_BE -c2 -f44100]
  -f dat (16-bit little-endian, 48000, stereo) [-f S16_LE -c2 -r48000]
 If no format is given, U8 is used. |
| -r, --rate=#<Hz> |  - Sampling rate in Hz. The default rate is 8000 Hz. If the value specified is less than 300, it is taken as the rate in kHz. Valid values are 2000 through 192000 Hz. |
| -d, --duration=# |  - Interrupt after # seconds. A value of zero means infinity. The default is zero, so if this option is omitted, then the arecord process will run until it is killed. |
| -s, --sleep-min=# |  - Minimum ticks to sleep. The default is not to sleep. |
| -M, --mmap |  - Use memory-mapped (mmap) I/O mode for the audio stream. If this option is not set, the read/write I/O mode will be used. |
| -N, --nonblock |  - Open the audio device in non-blocking mode. If the device is busy, the program will exit immediately. If this option is not set, the program will until the audio device is available again. |
| -F, --period-time=# |  - Distance between interrupts is # microseconds. If no period time and no period size is given, then a quarter of the buffer time is set. |
| -B, --buffer-time=# |  - Buffer duration is # microseconds. If no buffer time and no buffer size is given, then the maximum allowed buffer time that is not more than 500 ms is set. |
| --period-size=# |  - Distance between interrupts is # frames. If no period size and no period time is given, then a quarter of the buffer size is set. |
| --buffer-size=# |  - Buffer duration is # frames. If no buffer time and no buffer size is given, then the maximal allowed buffer time that is not more than 500 ms is set. |
| -A, --avail-min=# |  - Minimum available space for wakeup is # microseconds. |
| -R, --start-delay=# |  - Delay for automatic PCM start is # microseconds (relative to buffer size if <= 0) |
| -T, --stop-delay=# |  - Delay for automatic PCM stop is # microseconds from xrun |
| -v, --verbose |  - Show PCM structure and setup. This option is accumulative. The VU meter is displayed when is given twice or three times. |
| -V, --vumeter=TYPE |  - Specify the VU-meter type, either stereo or mono. The stereo VU-meter is available only for 2-channel stereo samples with interleaved format. |
| -I, --separate-channels |  - One file for each channel. This option disables max-file-time and use-strftime, and ignores SIGUSR1. The stereo VU meter is not available with separate channels. |
| -P |  - Playback. This is the default if the program is invoked by typing aplay. |
| -C |  - Record. This is the default if the program is invoked by typing arecord. |
| -i, --interactive |  - Allow interactive operation via stdin. Currently only pause/resume via space or enter key is implemented. |
| --disable-resample |  - Disable automatic rate resample. |
| --disable-channels |  - Disable automatic channel conversions |
| --disable-format |  - Disable automatic format conversions. |
| --disable-softvol |  - Disable software volume control (softvol) |
| --test-position |  - Test ring buffer position |
| --test-coef=<coef> |  - Test coefficient for ring buffer position; default is 8. Expression for validation is: coef * (buffer_size / 2). Minimum value is 1 |
| --test-nowait |  - Do not wait for the ring buffer--eats the whole CPU |
| --max-file-time |  - When recording and the output file has recorded sound for the maximum file time, close the output file and open a new output file. The default is the maximum size supported by the file format: 2 GB for WAV files. This option has no effect if --separate-channels is specified. |
| --process-id-file <file name> |  - aplay writes its process ID here, so other programs can send signals to it. |
| --use-strftime |  - When recording, interpret %-codes in the file name parameter by using the strftime facility whenever the output file is opened. The important strftime codes are: 
 - %Y: year
 - %m: month
 - %d: day of the month
 - %H: hour
 - %M: minute
 - %S: second

 - In addition, %v is the file number, starting at 1. When this option is specified, intermediate directories for the output file are created automatically. This option has no effect if --separate-channels is specified. |
| --dump-hw-params |  - Dump hw_params of the device’s preconfigured status to stderr. The dump lists capabilities of the selected device, such as supported formats, sampling rates, numbers of channels, period and buffer bytes, sizes, and times. For raw device hw:X, this option basically lists hardware capabilities of the soundcard. |
| --fatal-errors |  - Disables recovery attempts when errors (for example, xrun) are encountered; the aplay process instead aborts immediately. |

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
