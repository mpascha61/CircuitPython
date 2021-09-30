# Engineering_3_Notebook
# CircuitPython
 The follwing files are my first foray into CircuitPython.
## Table of Contents
* [Table of Contents](#TableOfContents)
* [Hello_CircuitPython](#Hello_CircuitPython)
* [CircuitPython_Servo](#CircuitPython_Servo)
* [CircuitPython_LCD](#CircuitPython_LCD)
* [NextAssignmentGoesHere](#NextAssignment)
---

## Hello_CircuitPython

### Description & Code
Description goes here

Here's how you make code look like code:

```python
Code goes here
import board
import neopixel
import time

dot = neopixel.NeoPixel(board.NEOPIXEL, 1)
print("Make it red!")

while True:
    dot.fill((0, 0, 255))
    time.sleep(.30)
    dot.fill((153, 0, 255))
    time.sleep(.30)
    dot.fill((255, 0, 0))
    time.sleep(.30)
```


### Images / Evidence
![ledlightpic](https://user-images.githubusercontent.com/71345181/133625107-908011a3-f2ad-4a12-a524-92a9d155694c.jpg)

### Reflection

Changing the code to swtich colors and timing was fairly simple but I had issues with the actual neopixel download not being in my student drive.




## CircuitPython_Servo

### Description & Code

```python
Code goes here
"""CircuitPython Essentials Servo standard servo example"""
import time
import board
import pwmio
import servo
import touchio
# create a PWMOut object on Pin A2.
pwm = pwmio.PWMOut(board.A2, duty_cycle=2 ** 15, frequency=50)
touch_A1 = touchio.TouchIn(board.A1)

# Create a servo object, my_servo.
my_servo = servo.Servo(pwm)

while True:
    
    for angle in range(180, 0, -1): # 180 - 0 degrees, 5 degrees at a time.
        my_servo.angle = angle
        time.sleep(0.01)
    if touch_A1.value:
        print("Touched A1!")
        for angle in range(0, 180, 1):  # 0 - 180 degrees, 5 degrees at a time.
            my_servo.angle = angle
            time.sleep(0.01)
    time.sleep(.05) 


```

### Evidence
![ServoEvidence](https://user-images.githubusercontent.com/71345181/133624650-4b4e675e-5a12-46e6-9875-83fdaabe821c.png)
### Images
![ezgif com-gif-maker](https://user-images.githubusercontent.com/71345181/133622973-0dc4623e-d1af-48bd-8901-5fd99dc2f4a8.gif)

### Reflection
Somewhat simple except I had to remove the code telling it to input the adafruit servo from the adafruit file because I had already moved the file to my D drive (metro drive). Cap touch I still don't fully understand how it detects me touching a wire vs a wire rubbing against some random surface though.

[learn.adafruit.com](url) extremely helpful



## CircuitPython_DistanceSensor

### Description & Code

```python
Code goes here
import time
import board
import adafruit_hcsr04
import neopixel
import simpleio

sonar = adafruit_hcsr04.HCSR04(trigger_pin=board.D5, echo_pin=board.D6)
dot = neopixel.NeoPixel(board.NEOPIXEL, 1)
dot.brightness = 0.5

cm = 0
print("new code")

while True:
    try:
        cm = sonar.distance
        print((cm,))
        
        if cm < 5:
            dot.fill((255, 0, 0))
        elif cm < 20:
            r = simpleio.map_range(cm, 5, 20, 255, 0)
            g = 0
            b = simpleio.map_range(cm, 5, 20, 0, 255)
            dot.fill((int(r), int(g), int(b)))
        else:
            r = 0
            g = simpleio.map_range(cm, 20, 35, 0, 255)
            b = simpleio.map_range(cm, 20, 35, 255, 0)
            dot.fill((int(r), int(g), int(b)))
    except RuntimeError:
        print("Retrying!")
    time.sleep(0.1)
```

### Evidence
![ezgif com-gif-maker (1)](https://user-images.githubusercontent.com/71345181/134514464-caa97a3e-3cad-4ae1-9206-1270b65ca029.gif)

### Images
![image](https://user-images.githubusercontent.com/71345181/134191171-18690e02-85c2-4f71-8a88-c707cf0dbbc7.png)

### Reflection

Using old code helps significantly with doing things like this quickly and knowing the io library well.



## NextAssignment

### Description & Code

```python
Code goes here
import board
import time
from lcd.lcd import LCD
from lcd.i2c_pcf8574_interface import I2CPCF8574Interface
import touchio

# get and i2c object
i2c = board.I2C()

# some LCDs are 0x3f... some are 0x27.
lcd = LCD(I2CPCF8574Interface(i2c, 0x3f), num_rows=2, num_cols=16)

lcd.print("Hello, Engineer!")

touch_pad1 = board.A1
touch1 = touchio.TouchIn(touch_pad1)
touch_pad2 = board.A2
touch2 = touchio.TouchIn(touch_pad2)


counter = 0
diff = 1
while True:
    if touch1.value:

        counter += diff
        lcd.set_cursor_pos(1, 4)
        lcd.print(str(counter))
        time.sleep(0.1)
    else:
        counter = counter
        time.sleep(0.1)
    if touch2.value:
        diff = -diff
    else:
        counter = counter
        time.sleep(0.1)

```

### Evidence

### Images

### Reflection
