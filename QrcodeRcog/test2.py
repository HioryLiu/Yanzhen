from PIL import *
from pytesser import *

im= Image.open('le7.png')
print im.size



for i in range(100):
    for j in range(30):
        pix=im.getpixel((i,j))
        if pix[1]<240:
            im.putpixel((i,j),(121,77,220))
        else:im.putpixel((i,j),(255,255,255,255))
print im.getpixel((25,13))
print im.getpixel((33,8))
print im.getpixel((29,25))


im.save('le8.png','PNG')
