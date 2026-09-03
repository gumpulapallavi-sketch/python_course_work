#builtin modules:
'''
1. System and OS Interaction Modules-

a . Operating System Interface:
The os module provides functions to interact with the operating system.
Common Functions:

os.getcwd() - Returns the current working directory
os.chdir(path) - Changes the current working directory
os.listdir(path) - Returns a list of files and folders in a directory
os.mkdir(name) - Creates a new directory
os.remove(file) - Deletes a specified file
os.rmdir(dir) - Removes an empty directory
os.path.exists(path) - Checks if a path exists

b . sys – System-Specific Parameters and Functions-
The sys module provides access to interpreter-specific functions and variables.

Python

Python
Common Functions:

sys.argv - List of command-line arguments
sys.exit() - Exits the program
sys.path - List of paths for module search
sys.version - Returns the Python version

import sys

#print(sys.path)
#print(sys.version)
print("start")
sys.exit()
print("end")

c . platform – System and Platform Information-
Provides details about the system, OS, and hardware.
Common Functions:

platform.system() - Returns OS name (e.g., Windows, Linux)
platform.release() - OS release version
platform.processor() - Returns processor type

import platform

print(platform.system())
print(plateform.release())
print(platform.proceesor())

2 . Mathematics and Randomness Modules-
 a . math – Mathematical Functions
constants:
math.pi π = 3.14159...
math.e Euler’s number ≈ 2.718

Functions:

math.sqrt(x) - Returns the square root of x
math.pow(x, y) - x raised to the power y (x^y)
math.ceil(x) - Smallest integer ≥ x
math.floor(x) - Largest integer ≤ x
math.fabs(x) - Absolute value of x
math.factorial(x) - Factorial of x (x!)
math.gcd(x, y) - Greatest common divisor
math.log(x, base) - Logarithm of x to the given base
math.sin(x) - Sine of x (x in radians)
math.cos(x) - Cosine of x
math.tan(x) - Tangent of x
math.degrees(x) - Convert radians to degrees
math.radians(x) - Convert degrees to radians


import math

print(math.pi)
print(math.e)

print(math.sqrt(64))
print(math.pow(2,4))

print(math.ceil(12.00001))
print(math.ceil(12.344))
print(math.ceil(12.9999))
print(math.ceil(12.6))

print(math.floor(12.00001))
print(math.floor(12.344))
print(math.floor(12.9999))
print(math.floor(12.6))

print(math.fabs(-10))
print(math.factorial(5))
print(math.gcd(8,24))
print(math.log(2,2))
print(math.sin(30))
print(math.cos(30))
print(math.tan(30))
print(math.degrees(30))
print(math.radians(30))


b . random – Generate Random Numbers
Used for random selections, number generation, and shuffling.
Functions:

random.random() - Returns a float in the range [0.0, 1.0)
random.randint(a, b) - Returns random integer between a and b (inclusive)
random.uniform(a, b) - Returns a float between a and b
random.choice(seq) - Returns a random element from a non-empty sequence
random.choices(seq,k=n) - Returns a list of k random elements from seq
random.shuffle(list) - Shuffles the list in place
random.seed(n) - Sets the seed for reproducibility 

import random

#random.seed(10)
print(random.randint(1,10))
print(random.randint(100000,999999))
print(random.random())
print(random.uniform(1,6))

l=['R','P','S']
print(random.choice(l))
print(random.choices(l, k=2))

random.shuffle(l)
print(l)

3. Data Structures and Iteration Utilities-
a . collections – Specialized Data Structures:
Provides alternatives to built-in types for performance and convenience.
Key Classes:

Counter - Counts frequency of elements
defaultdict - Dictionary with default values
deque - Double-ended queue for fast appends/pops

from collections import Counter

s = 'pyhton programming'
m = 'this is that that is this is '.split()
l = [1,2,3,2,30,1,1,2,1,1,1,1,2,11,2,2,3,2,4,3,4,3,32,2,3,2,3,45,6,]

print(Counter(s))
print(Counter(m))
print(Counter(l))

from collections import defaultdict

s = 'pyhton programming'
m = 'this is that that is this is '.split()
l = [1,2,3,2,30,1,1,2,1,1,1,1,2,11,2,2,3,2,4,3,4,3,32,2,3,2,3,45,6,]

d = defaultdict(int)
for i in s:
    d[i]+=1

print(d)

from collections import deque
l = deque([])
l.append(10)
l.append(20)
l.append(30)
l.popleft()
l.popleft()
l.append(50)
l.append(70)
l.popleft()

print(l)

# reverse queue
from collections import deque
l = deque([])
l.appendleft(10)
l.appendleft(20)
l.appendleft(30)
l.pop()
l.pop()
l.appendleft(50)
l.appendleft(70)
l.pop()

print(l)
'''
from itertools import combinations,permutations

res1 = list(combinations('abc',2))
res2 = list(permutations('abc',2))

print([''.join(i) for i in res1])
print([''.join(i) for i in res2])