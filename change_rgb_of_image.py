from PIL import Image
import re

file = Image.open("logo.png")
# file.show()
rgb_im = file.convert("RGB")
# pix = file.load()
# print pix[50,50]
width = file.size[0]
height = file.size[1]

im = Image.new("RGB",(width,height))

for x in range(width):
    for y in range(height):
        r, g, b = rgb_im.getpixel((x,y))
        print r, g, b
        if r > 150 and g > 150 and b > 150:
            im.putpixel((x,y),(30, 175, 189))
        else:
            im.putpixel((x,y),(r,g,b))
im.show()
im.save("new_logo.png")
