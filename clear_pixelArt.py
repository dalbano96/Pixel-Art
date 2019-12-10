# Daryl Albano
# 12/10/19
# stop_pixelArt.py
# Clears SenseHAT LEDs
from sense_hat import SenseHat

def clear_pixelArt():
    sense = SenseHat()
    sense.set_rotation(r=0)
    sense.clear()

clear_pixelArt()
