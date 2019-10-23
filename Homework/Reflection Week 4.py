#%%
4 + 4.5 + 0.375

#%%
1500 * 0.08875

#%%
995.50 * 0.08875

#%%
def tax(subtotal):
    return subtotal * 0.08875

#%%
tax(1500)

#%%
1500 + tax(1500)

#%%
200 + 1500 + tax(1500)

#%%
sum = 1500
sum = sum + sum * 0.08875 # Add the tax amount

#%%
def set_a():
    a = 10
    print('The value of a:', a')

#%%
set_a()

#%%
a = 20
print('Intially, the value of a:', a)
set_a()
print('Finally, the value of a:', a)

#%%
def scoped(first, second):
    third = second + second - first
    return third
first = 10
second = 11
third = 12
scoped(2, 4)

#%%
first

#%%
second

#%%
third

#%%
def scoped(la, lala):
    lalala = lala + lala - la
    return lalala
la = 10
lala = 11
lalala = 12
scoped(2, 4)

#%%
la

#%%
lala

#%%
lalala

#%%
1 = [7, 4, 2, 6]

#%%
for num in 1:
    print(num)

#%%
for num in 1:
    print(num * 2)

#%%
def mean(sequence):
    total = 0
    for element in sequence:
        total = total + element
    return total / len(sequence)

#%%
def mean(sequence):
    total = 0
    for element in sequence:
        total = total + element
    return total /len(sequence)

#%%
short = [5, 5, 5, 5]

#%%
mean(short)

#%%
x = 5

#%%
type(x)

#%%
x = 'hello world'
type(x)

#%%
type(5)

#%%
x = [1, 2, 3]

#%%
type(x)

#%%
'hello' + 'world'

#%%
'knock' + 'knock'

#%%
a = 'hello'
b = 'world'
a + b

#%%
len('hello world')

#%%
len([1, 2, 3])

#%%
len(5)

#%%
2 + 'hello'

#%%
len(str(5))

#%%
str(2) + 'hello'

#%%
volume = [4.0, 2.0, 3.0, 5.5]
result = []
for element in volume:
    result = result + [element * 2]

#%%
words = ['hello', 'world']

#%%
double(words)

#%%
countdown = [3, 2, 1, 'contact']

#%%
double(countdown)

#%%
2 + 2 == 4

#%%
greeting ='hello'

#%%
greeting == 'hello'

#%%
greeting == 'hi'

#%%
def secret(word):
    if word == 'please':
        return 'Yes!'

#%%
secret('hello')

#%%
secret('world')

#%%
secret('please')

#%%
def yesno(word):
    if word == 'yes':
        return True
    if word == 'no':
        return False

#%%
yesno('haha')

#%%
yesno('no')

#%%
yesno('yes')

#%%
yesno('Yes')

#%%
if word == 'please':
    return 'Yes!'
else:
    return 'No.'

#%%
def secret(word):
    return (word == 'please')

#%%
'hi' * 2

#%%
'hihi' / 2

#%%
