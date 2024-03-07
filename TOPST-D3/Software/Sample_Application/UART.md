# 1 UART Example

Universal Asynchronous Receiver/Transmitter (UART) communication is a serial communication in which one data transmission or reception pin is used. UART sends 1 byte at a time, and each bit is transmitted in sequence (series). UART is a method commonly used in MCU (for example, Arduino), and there are TX (pins that send data) and RX (pins that receive data). From a circuit perspective, 0 and 1 of each bit can be thought of as GND and VCC in the MCU, and if the received signal is interpreted, the received signal can be switched from bit to byte again.

When exchanging data, the data transmission speeds of the sender and receiver must be the same. This communication speed is called the baud rate, and there are various types of baud rates, such as 115200, 57600, and 9600. UART starts with Start bit (GND, 0), then ends with 8 Databits, and Stop bit (VCC, 1). Therefore, it is common to transmit and receive 10 bits at a time.

The following is a demo program for simple serial communication with the UART protocol.

```bash
USAGE: ./uartexample
```

<div style="display: flex; justify-content: center;">
    <img src="https://github.com/Topst-Dev/Documentation/assets/144076415/48d2e884-1e7d-4d9a-a5bc-ddf2acbd6e07" width="500" height="350" style="margin: auto;">
</div>
<p align="center"><strong>Figure 2.7 UART Example</strong></p>

```c
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <fcntl.h>
#include <string.h>
#include <pthread.h>
#include <time.h>

#include <string.h>
#include <sys/types.h>
#include <termios.h>

#include <pthread.h>

static int fd = 0;
#define MAX_BUF_SIZE 512
#define DEV_JIGBEE_UART "/dev/ttyMAX"

int init_uart(char * dev, int baud, int * fd)
{
    struct termios newtio;
    * fd = open(dev, O_RDWR | O_NOCTTY | O_NONBLOCK);
    if ( * fd < 0) {
        printf("%s> uart dev '%s' open fail [%d]n", __func__, dev, * fd);
        return -1;
    }
    memset( & newtio, 0, sizeof(newtio));
    newtio.c_iflag = IGNPAR; // non-parity 
    newtio.c_oflag = OPOST | ONLCR;;
    newtio.c_cflag = CS8 | CLOCAL | CREAD; // NO-rts/cts 
    switch (baud)
    {
    case 115200:
      newtio.c_cflag |= B115200;
      break;
    case 57600:
      newtio.c_cflag |= B57600;
      break;
    case 38400:
      newtio.c_cflag |= B38400;
      break;
    case 19200:
      newtio.c_cflag |= B19200;
      break;
    case 9600:
      newtio.c_cflag |= B9600;
      break;
    case 4800:
      newtio.c_cflag |= B4800;
      break;
    case 2400:
      newtio.c_cflag |= B2400;
      break;
    default:
      newtio.c_cflag |= B115200;
      break;
    }

    newtio.c_lflag = 0;
    //newtio.c_cc[VTIME] = vtime; 
    //newtio.c_cc[VMIN] = vmin;  
    newtio.c_cc[VTIME] = 0;
    newtio.c_cc[VMIN] = 0;
    tcflush( * fd, TCIFLUSH);
    tcsetattr( * fd, TCSANOW, & newtio);
    return 0;
}

void test_read_loop(void * arg)
{
    int result;
    char buffer[MAX_BUF_SIZE];
    fd_set reads, temps;

    FD_ZERO( & reads);
    FD_SET(fd, & reads);

    while (1)
    {
        temps = reads;
        result = select(FD_SETSIZE, & temps, NULL, NULL, NULL);

        if (result < 0)
        {
            exit(EXIT_FAILURE);
        }

        if (FD_ISSET(fd, & temps))
        {
            memset(buffer, 0, sizeof(buffer));
            if (read(fd, buffer, MAX_BUF_SIZE) == -1)
                continue;
            printf("receive buffer is [%s]rn", buffer);
        }
    }
}

void main()
{
    int result, ret = -1;
    pthread_t p_thread;

    ret = init_uart(DEV_JIGBEE_UART, 9600, & fd);
    printf("init uart [%d], [%d]rn", ret, fd);

    pthread_create( & p_thread, NULL, test_read_loop, NULL);

    while (1)
    {
        ret = write(fd, "test string...", 4);
        printf("write return [%d]rn", ret);
        sleep(1);
    }
}

```


```c
#include <termios.h>
int tcflush(  int     fildes, 
                 int     where
              );

```


The **tcflush()** function is called by a process to flush all input that has been received but not yet been read by a terminal, or all output written but not transmitted to the terminal. Flushed data are discarded and cannot be retrieved.

**Parameters**

n  **fildes**: Indicates a file descriptor associated with a terminal device.

n  **where**: Indicates whether the system is to flush input or output, represented by one of the following symbols defined in the **termios.h** header file:

l  TCIFLUSH: Flushes input data that has been received by the system but not read by an application.

l  TCOFLUSH: Flushes output data that has been written by an application but not sent to the terminal.

l  TCIOFLUSH: Flushes both input and output data.

**Return Value**

The **tcflush()** function returns 0 if successful and -1 if unsuccessful. If the **tcflush()** function is called from a background process with a file descriptor that refers to the controlling terminal for the process, a SIGTTOU signal may be generated. This causes the function call to be unsuccessful and the function returns -1 and sets **errno** to EINTR. If SIGTTOU is blocked, the function call proceeds normally.

---

```c
#include <termios.h>
int tcsetattr(int                             fildes, 
                 int                             optional_actions,
                 const struct termios    *termios_p
                 );

```


The **tcsetattr()** function only works in an environment where either a controlling terminal exists, or stdin and stderr refer to teletypewriter (TTY) devices. Specifically, it does not work in a TSO environment.

The **tcsetattr()** function changes the attributes associated with a terminal. New attributes are specified with a termios control structure. Programs should always issue a **tcgetattr()** first, modify the desired fields, and then issue a **tcsetattr()**. **tcsetattr()** should never be issued by using a termios structure that was not obtained using **tcgetattr()**. **tcsetattr()** should use only a termios structure that was obtained by **tcgetattr()**.

**Parameters**

n  **fildes**: Indicates an open file descriptor associated with a terminal.

n  **optional_actions**: Indicates a symbol defined in the **termios.h** header file that specifies when to change the terminal attributes.

n  **termios_p**: A pointer to a termios control structure that contains the desired terminal attributes.

**Return Value**

If successful, **tcsetattr()** returns 0.

If unsuccessful, **tcsetattr()** returns -1 and sets **errno** to one of the following values:

n  **EBADF**: **fildes** is not a valid open file descriptor.

n  **EINTR**: A signal interrupted **tcsetattr()**.

n  **EINVAL**: When is not a recognized value, or some entry in the supplied termios structure had an incorrect value.

n  **EIO**: The process group of the process issuing the function is an orphaned, background process group, and the process issuing the function is not ignoring or blocking SIGTTOU.

n  **ENOTTY**: **fildes** is not associated with a terminal.


```c
#include   <sys/time.h>
int FD_ISSET(int          fd, 
                    fd_set*   fdset
                   );

```


The **FD_ISSET()** function returns a value for the file descriptor in the file descriptor set.

**Parameters**

n  **fd**: The file descriptor.

n  **fdset**: The file descriptor set.

**RETURN VALUE**

The **FD_ISSET()** function returns a non-zero value if the file descriptor is set in the file descriptor set pointed to by **fdset**; otherwise, the **FD_ISSET()** function returns 0.


```c
int pthread_create(pthread_t                  *thread, 
                           const pthread_attr_t   *attr,
                           void                          *(*start_routine)(void*), 
                           void                          *arg
                           );

```


The **pthread_create()** function is used to create a new thread with attributes specified by **attr** within a process. If **attr** is NULL, the default attributes are used. If the attributes specified by **attr** are modified later, the thread's attributes are not affected. Upon successful completion, **pthread_create()** stores the ID of the created thread in the location referenced by thread.

**Parameters**

n  **thread**: The location where the ID of the newly created thread should be stored, or NULL if the thread ID is not required.

n  **attr**: The thread attribute object specifying the attributes for the thread that is being created. If **attr** is NULL, the thread is created with default attributes.

n  **start_routine**: The main function for the thread; the thread begins executing user code at this address.

n  **arg**: The argument passed to start.

**RETURN VALUE**

If successful, **pthread_create()** returns 0.

If unsuccessful, **pthread_create()** returns -1 and sets **errno** to one of the following values:

n  **EAGAIN**: The system lacks the necessary resources to create another thread.

n  **EINVAL**: The value specified by the thread is null.

n  **ELEMULTITHREADFORK**: **pthread_create()** was invoked from a child process created by calling **fork()** from a multi-threaded process. This child process is restricted from becoming multi-threaded.

n  **ENOMEM**: There is not enough memory to create the thread.