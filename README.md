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
Learn.adafruit.com extremely helpful



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
