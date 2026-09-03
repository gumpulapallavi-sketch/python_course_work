Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.

========================= RESTART: C:/Users/gumpu/OneDrive/Desktop/python course work/Day-3/Conversions.py ========================
#conversions
#Integer to other data types
a=8
type(a)
<class 'int'>
float(a)
8.0
bool(a)
True
list(a)
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    list(a)
TypeError: 'int' object is not iterable
set(a)
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    set(a)
TypeError: 'int' object is not iterable
tuple(a)
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    tuple(a)
TypeError: 'int' object is not iterable
dict(a)
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    dict(a)
TypeError: 'int' object is not iterable
complex(a)
(8+0j)
bool(a)
True
# Integers can only convert to float,complex,string,bool,complex.where as set,list,tuple are the collection of elements we cannot convert them
## Integers can only convert to float,complex,string,bool,complex.where as set,list,tuple are the collection of elements we cannot convert them and dict is a key value pair
#float
f=9.99
f
9.99
type(f)
<class 'float'>
int(f)
9
str(f)
'9.99'
\
str(f)
'9.99'
bool(f)
True
complex(f)
(9.99+0j)
list(f)
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    list(f)
TypeError: 'float' object is not iterable
set(f)
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    set(f)
TypeError: 'float' object is not iterable
tuple(f)
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    tuple(f)
TypeError: 'float' object is not iterable
dict(f)
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    dict(f)
TypeError: 'float' object is not iterable
#Float can be converted into int,str,bool,complex.where as set,list,tuple are the collection of elements we cannot convert them.and dict is a key value pair.
#string
s='pallavi'
type(s)
<class 'str'>
s
'pallavi'
int(s)
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    int(s)
ValueError: invalid literal for int() with base 10: 'pallavi'
float(s)
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    float(s)
ValueError: could not convert string to float: 'pallavi'
>>> s='20,68,90,90'
>>> s
'20,68,90,90'
>>> type(s)
<class 'str'>
>>> int(s)
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    int(s)
ValueError: invalid literal for int() with base 10: '20,68,90,90'
>>> float(s)
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    float(s)
ValueError: could not convert string to float: '20,68,90,90'
>>> bool(s)
True
>>> complex(s)
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    complex(s)
ValueError: complex() arg is a malformed string
>>> list(s)
['2', '0', ',', '6', '8', ',', '9', '0', ',', '9', '0']
>>> tuple(s)
('2', '0', ',', '6', '8', ',', '9', '0', ',', '9', '0')
>>> set(s)
{'6', '8', '9', '2', ',', '0'}
>>> dict(s)
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    dict(s)
ValueError: dictionary update sequence element #0 has length 1; 2 is required
