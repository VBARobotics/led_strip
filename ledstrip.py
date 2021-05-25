import board
from time import sleep
import neopixel
pixels = neopixel.NeoPixel(board.D18, 200)
# pixels[0] = (255, 0, 0)
for x in range(0, 200):
    pixels[x] = (255, 255, 255)
    sleep(0.01)
