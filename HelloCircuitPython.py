import board
import neopixel
import.sleep

dot = neopixel.NeoPixel(board.NEOPIXEL, 1)
dot.brightness=0.1
print("Make it red!")

while True:
    dot.fill((0, 255, 0))
    time.sleep(.10)
    dot.fill((153, 0, 255))
    time.sleep(.10)
    dot.fill((255, 0, 0))