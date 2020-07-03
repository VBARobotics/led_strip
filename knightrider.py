import board
from time import sleep
import neopixel
# Configured for GPIO 18
pixels = neopixel.NeoPixel(board.D18, 30)
# pixels[0] = (255, 0, 0)
color= (0,0,255)
speed=0.1
scans=5
striplen=7
for z in range (0, scans):
    for x in range(0, striplen):
        pixels[x] = color
        sleep(speed)
        pixels[x] = (0, 0, 0)
    for x in range(striplen-1, -1, -1):
        pixels[x] = color
        sleep(speed)
        pixels[x] = (0, 0, 0)