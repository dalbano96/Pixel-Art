# Daryl Albano
# 10/30/19
# Showcase 8x8 image on the Raspberry Pi SenseHAT

from sense_hat import SenseHat
import time
from PIL import Image
import os

# Open image file
filename = "mario.png"
image_file = os.path.join(os.sep,"/home","pi","SenseHAT",filename)
img = Image.open(image_file)

# Generate rgb values for image pixels
rgb_img = img.convert('RGB')
image_pixels = list(rgb_img.getdata())

# Get the 64 pixels you need
pixel_width = 1   # Total number of pixels (orig image) divided by 8
image_width = pixel_width * 8
sense_pixels = []
start_pixel = 0
while start_pixel < (image_width * 64):
    sense_pixels.extend(image_pixels[start_pixel:(start_pixel +
    image_width):pixel_width])
    start_pixel += (image_width * pixel_width)

sense = SenseHat()
sense.set_rotation(r=270)
sense.set_pixels(sense_pixels)

time.sleep(5)

sense.clear()
