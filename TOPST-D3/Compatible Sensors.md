# Compatible Sensors with TOPST D3

<br/><br/>

## 1. Touch Sensor(TTP223B)  
* Power supply for **2~5.5V DC**
* capacitive type

The following code is an example in which the LED turns on when you touch the touch recognition part of the touch sensor.
```
import time
import os
 
TOUCH_SENSOR_PIN = 89
LED_PIN = 83
 
def setup_gpio(pin, direction):
    gpio_path = f"/sys/class/gpio/gpio{pin}"
 
    if not os.path.exists(gpio_path):
        with open("/sys/class/gpio/export", "w") as f:
            f.write(str(pin))
 
    with open(f"{gpio_path}/direction", "w") as f:
        f.write(direction)
 
def read_gpio(pin):
    gpio_value_path = f"/sys/class/gpio/gpio{pin}/value"
    with open(gpio_value_path, "r") as f:
        return f.read().strip()
 
def write_gpio(pin, value):
    gpio_value_path = f"/sys/class/gpio/gpio{pin}/value"
    with open(gpio_value_path, "w") as f:
        f.write(str(value))
 
def unexport_gpio(pin):
    with open("/sys/class/gpio/unexport", "w") as f:
        f.write(str(pin))
 
def main():
    try:
        setup_gpio(TOUCH_SENSOR_PIN, "in")
        setup_gpio(LED_PIN, "out")
 
        write_gpio(LED_PIN, 0)
 
        while True:
            sensor_value = read_gpio(TOUCH_SENSOR_PIN)
 
            if sensor_value == "1":
                print("detected touch. turn on led")
                write_gpio(LED_PIN, 1)
            else:
                print("undetected touch. turn off led")
                write_gpio(LED_PIN, 0)
 
            time.sleep(0.1)
    except KeyboardInterrupt:
        print("stop")
        unexport_gpio(TOUCH_SENSOR_PIN)
        unexport_gpio(LED_PIN)
 
if __name__ == "__main__":
    main()
```
<br/><br/>

## 2. LCD (lcd 1602) 
The following code is an example of a text that is waiting to be entered and that is entered in command line and then in lcd.
Before you excute lcd example code, you must install smbus, RPLCD packages.
You can install packages with **pip3 install smbus, pip3 install RPLCD**.
```
import smbus
import time
from RPLCD.i2c import CharLCD
 
I2C_BUS = 1
 
LCD_ADDRESS = 0x27
 
lcd = CharLCD(i2c_expander='PCF8574', address=LCD_ADDRESS, port=I2C_BUS,
              cols=16, rows=2, dotsize=8,
              charmap='A00', auto_linebreaks=True,
              backlight_enabled=True)
 
def display_text(text):
    lcd.clear()
    lcd.write_string(text)
 
def main():
    while True:
        user_input = input("Enter text to display on LCD: ")
 
        display_text(user_input)
 
        time.sleep(4)
        lcd.clear()
 
if __name__ == "__main__":
    main()
```





