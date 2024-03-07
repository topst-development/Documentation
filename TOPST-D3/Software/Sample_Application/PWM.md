### 1.1.1 Pulse Width Modulation (PWM)

Pulse Width Modulation (PWM) is a type of pulse modulation that modulates the width of the pulse according to the magnitude of the signal.

The ratio of the high and low state waveforms of the pulse waveform is called the duty cycle, and PWM is a method of modulating the duty cycle by adjusting the duty cycle value.

Originally, PWM was a technology developed for communication. However, because it is an excellent method for current and voltage control, PWM is currently used for DC power control or motor control rather than communication.

```c
#include <linux/pwm.h>
struct pwm_chip {
  struct device * dev;
  struct list_head list;
  const struct pwm_ops * ops;
  int base;
  unsigned int npwm;
  struct pwm_device * pwms;
  struct pwm_device * (* of_xlate) (struct pwm_chip *pc,const struct of_phandle_args *args);
  unsigned int of_pwm_n_cells;
  bool can_sleep;
};  

```


**Parameters**

n  **dev**: The device that provides the PWMs

n  **list**: List nodes for internal use

n  **ops**: Callbacks for this PWM controller

n  **base**: The number of first PWM controlled by this chip

n  **npwm**: The number of PWMs controlled by this chip

n  **pwms**: The array of PWM devices allocated by the framework

n  **of_xlate**: The request a PWM device given a device tree PWM specifier

n  **of_pwm_n_cells**: The number of cells expected in the device tree PWM specifier

n  **can_sleep**: Must be true for the .config, .enable, or .disable operations to sleep


```c
#include <linux/pwm.h>
struct pwm_device {
    const char *label;
    unsigned long flags;
    unsigned int hwpwm;
    unsigned int pwm;
    struct pwm_chip *chip;
    void *chip_data;
    struct pwm_args args;
    struct pwm_state state;
    struct pwm_state last;
};

```


PWM channel object

**Parameters**

n  **label**: The name of the PWM device

n  **flags**: The flags associated with the PWM device

n  **hwpwm**: The relative index of the PWM device per chip

n  **pwm**: The global index of the PWM device

n  **chip**: The PWM chip providing this PWM device

n  **chip_data**: The chip-private data associated with the PWM device

n  **args**: PWM arguments

n  **state**: The last applied state

n  **last**: The last implemented state (for **PWM_DEBUG**)


```c
#include <stdio.h>
#include <wiringPi.h>

#define LED 1

int bright = 0;

int main(void) {
    wiringPiSetup();

    pinMode(LED, PWM_OUTPUT);
    digitalWrite(LED, LOW);

    while(1) {
        for(bright=0; bright<100; ++bright) {
            pwmWrite(LED, bright);
            delay(50);
        }
        
        for(bright=100; bright>=0; --bright) {
            pwmWrite(LED, bright);
            delay(50);
        }

    }
    return 0;
}

```

---

The following is a demo program to control the brightness of LED by using PWM.

```bash
USAGE: pwmexample.py [-h] [-cn CHIPNUM] [-p PERIOD] [-cy CYCLENUM]

optional arguments:
  -h, --help            show this help message and exit
  -cn, --chipnum     pwm chip number
  -p, --period          pwm period value
  -cy, --cyclenum    pwm cycle number

```

---

**Example:**

```bash
python3 pwmexample.py -cn 0 -p 100000 -cy 3
```


<div style="display: flex; justify-content: center;">
    <img src="https://github.com/Topst-Dev/Documentation/assets/144076415/d51fd9d3-c1cf-4e40-aa0a-d2d7b84e1da1" width="500" height="350" style="margin: auto;">
</div>
<p align="center"><strong>Figure 2.11 PWM Example</strong></p>

<div style="display: flex; justify-content: center;">
    <img src="https://github.com/Topst-Dev/Documentation/assets/144076415/dbd9d158-64b2-436f-8cc4-429f7fb4635a" width="500" height="350" style="margin: auto;">
</div>
<p align="center"><strong>Figure 2.12 Circuit Used in Example</strong></p>

```python
import os
import time
import argparse

def getargs() :
    parser = argparse.ArgumentParser()
    parser.add_argument("-cn", "--chipnum", dest="chipnum", type=int, default=0, help="pwm chip number")
    parser.add_argument("-p", "--period", dest="period", type=int, default=1000000, help="pwm period value")
    parser.add_argument("-cy", "--cyclenum", dest="cyclenum", type=int, default=3, help="pwm cycle number")

    return parser.parse_args()

def pwm_control(chipnum, period, cyclenum):
    os.system(f"echo 0 > /sys/class/pwm/pwmchip{chipnum}/export")
    os.system(f"echo {period} > /sys/class/pwm/pwmchip{chipnum}/pwm{chipnum}/period")
    os.system(f"echo 1 > /sys/class/pwm/pwmchip{chipnum}/pwm{chipnum}/enable")

    print("Check out the physical circuits you created!")
    print("The light intensity is changing.\n")

    print("<duty cycle>")
    for c in range(cyclenum):
        for i in range(0, 100, 1) :
            os.system(f"echo {i} > /sys/class/pwm/pwmchip{chipnum}/pwm{chipnum}/duty_cycle")
            time.sleep(0.01)
        for j in range(100, 0, -1) :
            os.system(f"echo {j} > /sys/class/pwm/pwmchip{chipnum}/pwm{chipnum}/duty_cycle")
            time.sleep(0.01)
        print(f"cycle : {c+1}/{cyclenum}")

if __name__ == "__main__":
    args = getargs()
    pwm_control(chipnum=args.chipnum, period=args.period, cyclenum=args.cyclenum)

```