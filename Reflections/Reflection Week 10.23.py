
#%%
zipcode5n = "123459080"
zipcode5p4 = "12345-1234"
x = re.search("\d{5}", zipcode5p4)
y = re.search("\d{5}", zipcode5n)
print(x, y)

#%%
zipcode5n = "123459080"
zipcode5p4 = "12345-1234"
x = re.search("\d{5, 4}", zipcode5p4)
y = re.search("\d{5}", zipcode5n)
print(x, y)

#%%
zipcode5n = "123459080"
zipcode5p4 = "12345-1234"
x = re.search("\d{5}-\d{4}", zipcode5p4)
y = re.search("\d{5}-\d{4}", zipcode5n)
print(x, y)

#%%
zipcode5n = "123459080"
zipcode5p4 = "12345-1234"
x = re.search("\d{5}(-\d{4})?", zipcode5p4)
y = re.search("\d{5}(-\d{4})?", zipcode5n)
print(x, y)


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