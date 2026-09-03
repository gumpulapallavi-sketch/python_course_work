Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.

= RESTART: C:/Users/gumpu/OneDrive/Desktop/python course work/Day-2/Variable Operators.py
#Variable Operators
a=5
a=10
a
10
A
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    A
NameError: name 'A' is not defined. Did you mean: 'a'?
a=5
A=10
a
5
>>> A
10
>>> a,b,c=30
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    a,b,c=30
TypeError: cannot unpack non-iterable int object
>>> 
>>> a,b,c=30,4,9
>>> a
30
>>> b
4
>>> c
9
>>> a=b=c=30
>>> a
30
>>> b
30
>>> c
30
>>> a=9
>>> b=6
>>> a,b=b,c
>>> a
6
>>> b
30
>>> c
30
>>> a,b=8,9
>>> a
8
>>> b
9
