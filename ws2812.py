# Simple test for NeoPixels on Raspberry Pi
import time
import board
import neopixel


# Choose an open pin connected to the Data In of the NeoPixel strip, i.e. board.D18
# NeoPixels must be connected to D10, D12, D18 or D21 to work.
pixel_pin = board.D18


num_pixels = 16

# The order of the pixel colors - RGB or GRB. Some NeoPixels have red and green reversed!
# For RGBW NeoPixels, simply change the ORDER to RGBW or GRBW.
ORDER = neopixel.GRB

pixels = neopixel.NeoPixel(
    pixel_pin, num_pixels, brightness=0.2, auto_write=False, pixel_order=ORDER
)




    # Comment this line out if you have RGBW/GRBW NeoPixels

def controlLed(dock):
    dock = dock-1
    pixels[dock] = (255, 0, 0)
    pixels.show()

controlLed(15)

# pixels.fill((0, 255, 0))
# pixels.show()
# time.sleep(1)

