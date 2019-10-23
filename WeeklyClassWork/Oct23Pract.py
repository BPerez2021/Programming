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