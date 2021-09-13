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

### Evidence
Pictures / Gifs of your work should go here

### Images
Make an account with your google ID at [tinkercad.com](https://www.tinkercad.com/learn/circuits), and use "TinkerCad Circuits to make a wiring diagram."  It's really easy!  
Then post an image here.   [here's a quick tutorial for all markdown code, like making links](https://www.markdownguide.org/basic-syntax/)

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
from adafruit_motor import servo

# create a PWMOut object on Pin A2.
pwm = pwmio.PWMOut(board.A2, duty_cycle=2 ** 15, frequency=50)

# Create a servo object, my_servo.
my_servo = servo.Servo(pwm)

while True:
    for angle in range(0, 180, 5):  # 0 - 180 degrees, 5 degrees at a time.
        my_servo.angle = angle
        time.sleep(0.05)
    for angle in range(180, 0, -5): # 180 - 0 degrees, 5 degrees at a time.
        my_servo.angle = angle
        time.sleep(0.05)

```

### Evidence

### Images

### Reflection




## CircuitPython_LCD

### Description & Code

```python
Code goes here

```

### Evidence

### Images

### Reflection





## NextAssignment

### Description & Code

```python
Code goes here

```

### Evidence

### Images

### Reflection
