# Daryl Albano
# 10/30/19
# pixel_art.py
# Showcase 8x8 image on the Raspberry Pi SenseHAT

from sense_hat import SenseHat
import time
from PIL import Image
import os

# Open image file
filename = "mario.png"  # TODO: Replace filename
image_file = os.path.join("images", filename)
img = Image.open(image_file)

# Generate rgb values for image pixels
rgb_img = img.convert('RGB')
image_pixels = list(rgb_img.getdata())

# Get the 64 pixels you need
pixel_width = 6   # Total number of pixels (orig image) divided by 8
image_width = pixel_width * 8
sense_pixels = []
start_pixel = 0
while start_pixel < (image_width * 64):
    sense_pixels.extend(image_pixels[start_pixel:(start_pixel +
    image_width):pixel_width])
    start_pixel += (image_width * pixel_width)

sense = SenseHat()
# Rotate the image by changing the value '0' to '90', '180', or '270'
sense.set_rotation(r=0)
sense.set_pixels(sense_pixels)

time.sleep(5)
sense.clear()
