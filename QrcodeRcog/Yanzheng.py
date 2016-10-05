from pytesser import *
import Image
import os

img  =Image.open('fnord.tif')


image_to_string(img,cleanup=False)
fileHandle =open('temp.txt')
text =fileHandle.read()

print text
print 'end'