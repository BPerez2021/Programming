#%%
print('Hello World')


#%%
print('Greetings Earthlings')

#%%
list(range(5))

#%%
list(range(0, 5))

#%%
list(range(1, 6))

#%%
answer = 1
for num in range(1, 6):
    answer = answer + num
answer

#%%
def fact(n):
    if n == 0:
        return 1
    else:
        return n + fact(n-1)

#%%
def doubler(sequence):
    if len(sequence) == 0:
        return []
    else:
        return [2 * sequence[0]] + doubler(sequence[1:])

#%%
