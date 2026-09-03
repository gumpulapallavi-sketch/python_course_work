# List comprehension in Python is a concise way to create lists by applying an expression to each item in an iterable (like a list, tuple, or string). 
# It’s basically a one‑line shortcut for loops when building lists.
# l = [updating for loop]
# l = [updating for loop if cond]
# l = [updat1 if cond else upd2 for loop]
# l = [upd for loop1 for loop2]
# l = [upd for loop1 for loop2 if cond]
'''
using list:

# 1 to 10 numbers
res = [i for i in range (1,11)]
print(res)

# factors of a number
n = 12
res = [i for i in range(1,n+1) if n%i==0]
print(res)

# printing even numbers as even numbers and odd numbers as 0
r = [29,47,34,74,63,90,46,60,93,6,54,3,1,89]
res = [i if i%2==0 else 0 for i in r]
print(res)

# nested list
r = [[29,47,34],[74,63,90],[46,60,93]]
res = [j for i in r for j in i  if j%2==0]
print(res)

using set:

# 1 to 10 numbers
res = {i for i in range (1,11)}
print(res)

# factors of a number
n = 12
res = {i for i in range(1,n+1) if n%i==0}
print(res)

# printing even numbers as even numbers and odd numbers as 0
r = {29,47,34,74,63,90,46,60,93,6,54,3,1,89}
res = [i if i%2==0 else 0 for i in r]
print(res)

# nested list
r = [[29,47,34],[74,63,90],[46,60,93]]
res = [j for i in r for j in i  if j%2==0]
print(res)

# printing 10 elments in a list
l = [int(input(f"Enter the number - {i+1}:")) for i in range(10)]
print(l)

# printing 5 names
names= [input(f"Enter the name-{i+1}:") for i in range(5)]
print(names)

# printing names and the marks of the students
names= {input(f"Enter the name-{i+1}: "): int(input("Enter the marks: ")) for i in range(5)}
print(names)

using dictionry:

# square of a numbers
result = {i:i*i for i in range(10)}
print(result)
'''



