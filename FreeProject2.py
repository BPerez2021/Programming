#Project 11.1 using Computer Lab computer
#%%
from PIL import Image, ImageDraw

def transformimages(text, bgcolor):
    img = Image.new('RGB', (350,75), color = bgcolor)

    d = ImageDraw.Draw(img)
    d.text ((5,30), text, fill = (234,223,0))
    return img
#using one of the results form the last FreeProject (see your comments)
transformimages("Every Elephant Is Expensive Meanwhile None Hear Is Close.", "gray")



# %%
def blur(img):
    blurred = Image.new('RGB', img.size)
    for x in range(1, img.size[0] -1):
        for y in range(1, img.size[1] -1):
            (r, g, b) = img.getpixel((x, y)) / 2.0
            blurred.putpixel ((x,y), (r + change, g + change, b + change))
    return blurred

##Image blur not working (code from book), pretty sure I am doing it wrong, but I do not have enough of an understanding on how it works to properly put it all together.
# %%
# %%
from PIL import Image, ImageDraw

def transformimages(text, bgcolor):
    img = Image.new('RGB', (350,75), color = bgcolor)

    d = ImageDraw.Draw(img)
    d.text ((5,30), text, fill = (234,223,0))
    return img
def blur(img):
    blurred = Image.new('RGB', img.size)
    for x in range(1, img.size[0] -1):
        for y in range(1, img.size[1] -1):
            (r, g, b) = img.getpixel((x, y)) / 2.0
            blurred.putpixel ((x,y), (r + change, g + change, b + change))
    return blurred
    
    
#using one of the results form the last FreeProject (see your comments)
transformimages("Every Elephant Is Expensive Meanwhile None Hear Is Close.", "gray")
##tried to add the blur, ony printed original

# %%
from PIL import Image
img = Image.open("wolf.jpg")
img.rotate(45).show()

##trying to do research to figure out how to manipulate the image
##Couldn't figure how to blur, rotate, or other manipulatation for the ImageDraw
##Why doesn't it work??????

# %%
from PIL import Image
img = Image.open("puppy.jpg")
img.rotate(305).show()

###It works, i had forgotten to download the image into my repository


# %%
from PIL import Image
img = Image.open("puppy.jpg")
img.rotate(180).show()
#yeah

# %%
from PIL import Image
img = Image.open("puppy.jpg")
img.rotate(10).show()
#it works

# %%
from PIL import Image
img = Image.open("puppy.jpg")
img.rotate(255).show()
#look at the cutie

# %%
