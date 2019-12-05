# Pixel-Art
Display famous characters in a pixel art reimagining on the Raspberry Pi SenseHAT shield.

![](images/mario.png) ![](images/luigi.png) ![](images/princess-peach.png) ![](images/toad.png)

## Getting started
**Make sure you are running Python 3 or above**

Open `pixel_art.py` in a Python IDE, such as Thonny. Test SenseHAT LEDs by running `pixel_art.py`. If Mario appears on the SenseHAT, you are ready to go.

![](ref/mario-test.jpg)

## Changing Characters
To display another character on the SenseHAT, navigate to line 12 on `pixel_art.py`. Change `"mario.png"` to another *filename**, such as `luigi.png` or `homer.png`.

**Compatible filenames are located in the `images` folder.*

Here are all of the compatible characters you can display on the SenseHAT.

![](ref/All_Character_Sprites.png)

## Rotating the Image
You can also rotate the image by changing the value on line 32.
```python sense.set_rotation(r=0)```
Acceptable rotation values include '0', '90', '180', and '270'. Other rotation values will not be accepted.
