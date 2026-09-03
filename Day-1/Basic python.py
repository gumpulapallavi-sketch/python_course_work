Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.

= RESTART: C:/Users/gumpu/OneDrive/Desktop/python course work/Day-1/Basic python.py
print("Hello, World!")

Hello, World!
num = int(input("Enter a number: "))

if num % 2 == 0:
    print("Even")
else:
    print("Odd")

SyntaxError: multiple statements found while compiling a single statement
num = int(input("Enter a number:5 "))

if num % 2 == 0:
    print("Even")
else:
    print("Odd")
    
SyntaxError: multiple statements found while compiling a single statement
num=15
... 
... if num % 2 == 0:
...     print("Even")
... else:
...     print("Odd")
...     
SyntaxError: multiple statements found while compiling a single statement
>>> num = int(input("Enter a number:5 "))
Enter a number:5 
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    num = int(input("Enter a number:5 "))
ValueError: invalid literal for int() with base 10: ''
>>> num = int(input("Enter a number:5 "))
Enter a number:5 
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    num = int(input("Enter a number:5 "))
ValueError: invalid literal for int() with base 10: ''
>>> num = int(input("Enter a number: "))
Enter a number: 6
>>> if num % 2 == 0:
...     print("Even")
... else:
...     print("Odd")
... 
...     
Even
>>> num = int(input("Enter a number: "))
Enter a number: 9
>>> if num % 2 == 0:
...     print("Even")
... else:
...     print("Odd")
... 
...     
Odd
