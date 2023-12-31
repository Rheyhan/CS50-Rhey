import os
import sys
from PIL import Image, ImageOps

allowedformat=["jpg", "jpeg", "png"]

if (temp:= len(sys.argv)) <= 2:
    sys.exit("Too few command-line arguments")
elif temp >3:
    sys.exit("Too many command-line arguments")
path=sys.argv[1]
target=sys.argv[2]

if not os.path.exists(path):
    sys.exit("Input does not exist")
    
if (temp:=target.split(".")[-1].lower()) not in allowedformat or (temp1:=path.split(".")[-1].lower()) not in allowedformat:
    sys.exit("Invalid output")

if temp!=temp1:
    sys.exit("Input and output have different extensions")

im1=Image.open(path)
im2=Image.open("shirt.png")
size=im2.size
im1=ImageOps.fit(im1, size)

im1.paste(im2, (0, 0), im2)
im1.save(target)