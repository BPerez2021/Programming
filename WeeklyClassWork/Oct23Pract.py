#%%
import re
txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)
# (xoeu)*

#%%
txt = "xa"
x = re.search("(xa){2, }", txt)
print(x)

#%%
zipcode = "3"
x = re.search("\d", zipcode)
print(x)

#%%
zipcode5n = "123459080"
zipcode5p4 = "12345-1234"
x = re.search("^\d{5}(-\d{4})?$", zipcode5p4)
y = re.search("\d{5}(-\d{4})?$", zipcode5n)
print(x, y)

#%%
zipcode5n = "12345"
zipcode5p4 = "12345-1234"
expression = "^\d{5}(-\d{4})?$"
print(re.search(expression, zipcode5n))
print(re.search(expression, zipcode5p4))

#%%
time0 = "5pm"
time1 = "6am"
time2 = "12:00p"
time3 = "13:00a"
time4 = "00:02pm"
expression = "^\d?\d(:\d\d)?[ap]m?$"
print(re.search(expression, time0))
print(re.search(expression, time1))
print(re.search(expression, time2))
print(re.search(expression, time3))
print(re.search(expression, time4))


#%%
time0 = "5pm"
time1 = "6am"
time2 = "12:00p"
time3 = "13:00a"
time4 = "00:02pm"
expression = "^([1-9]|1[0-2])(:\d\d)?[ap]m?$"
print(re.search(expression, time0))
print(re.search(expression, time1))
print(re.search(expression, time2))
print(re.search(expression, time3))
print(re.search(expression, time4))


#%%
#Classes
class MyClass1:
    """A simple example class"""
    i = 12345
    def f(self):
        return 'hello world'

#%%
class MyClass2:
    """A simple example class"""
    i = 12345
    def __init__(self,name):
        self.name = name
    def f(self):
        return 'hello world from ' + self.name

#%%
from PIL import Image

#%%
mode = 'RGBA'
size = (100, 100)
color = "black"
ourimage = Image.new(mode, size, color)
ourimage

#%%
