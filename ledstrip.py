import board
from time import sleep
import neopixel
pixels = neopixel.NeoPixel(board.D18, 30)
# pixels[0] = (255, 0, 0)
for x in range(0, 9):
    pixels[x] = (255, 0, 0)
    sleep(1)
