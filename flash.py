import board
from time import sleep
import neopixel
# Configured for GPIO 18
pixels = neopixel.NeoPixel(board.D18, 60)
# pixels[0] = (255, 0, 0)
color= (255,255,255)
speed=0.5
flashes=5
striplen=60
for z in range (0, flashes):
    for x in range(0, striplen):
        pixels[x] = color
    pixels.fill(color)    
    sleep(speed)
    pixels.fill((0, 0, 0))
    sleep(speed)
