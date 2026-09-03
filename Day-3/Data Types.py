Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.

========================= RESTART: C:/Users/gumpu/OneDrive/Desktop/python course work/Day-3/Data Types.py =========================
#Data Types
count=10
count=20
count
20
#float
price=88.04
price
88.04
type(price)
<class 'float'>
#complex
c=6=4j
SyntaxError: cannot assign to literal
c=6+4j
c
(6+4j)
type(c)
<class 'complex'>
#sequential type
#string
s='pallavi'
type(s)
<class 'str'>
#list
i=[1,3,4.9,'pallavi',True,[2,4,8],(9,4,9)]
i
[1, 3, 4.9, 'pallavi', True, [2, 4, 8], (9, 4, 9)]
l=[1,3,4.9,'pallavi',True,[2,4,8],(9,4,9)]
l
[1, 3, 4.9, 'pallavi', True, [2, 4, 8], (9, 4, 9)]
#tuple
t=()
t=tuple()
t=(1,2,3,'pallavi',[2,3,9],True,{8,9,4},{1:2,3:4,7:5})
t
(1, 2, 3, 'pallavi', [2, 3, 9], True, {8, 9, 4}, {1: 2, 3: 4, 7: 5})
#tuple is immutable ,used for fixed data types,allow duplicates,dynamically type
#tuple is immutable ,used for fixed data types,allow duplicates,dynamically type
t=(1,7,9,4,5)
t
(1, 7, 9, 4, 5)
#mapping data type
#set
s={}
type(s)
<class 'dict'>
s={1,5,8,4,4.8,'pallavi',[34,86],90,(6,8,0)}
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    s={1,5,8,4,4.8,'pallavi',[34,86],90,(6,8,0)}
TypeError: cannot use 'list' as a set element (unhashable type: 'list')
>>> s={1,5,8,4,4.8,'pallavi',90,(6,8,0)}
>>> s
{1, 4, 4.8, 5, 8, (6, 8, 0), 90, 'pallavi'}
>>> {1, 4, 4.8, 5, 8, (6, 8, 0), 90, 'pallavi'}
{1, 4, 4.8, 5, 8, (6, 8, 0), 90, 'pallavi'}
>>> type(s)
<class 'set'>
>>> #set is a mutable,unordered,doesnot allow duplicates,dynamic sized
>>> #dictionary
>>> #dic is a key value pair,is a collections of items,allow dupliocates and it's mutable
>>> d={}
>>> type(d)
<class 'dict'>
>>> d={'id':098,'name':'pallavi'}
SyntaxError: leading zeros in decimal integer literals are not permitted; use an 0o prefix for octal integers
>>> d={'id':98,'name':'pallavi'}
>>> d
{'id': 98, 'name': 'pallavi'}
>>> #boolen type
>>> status=True
>>> type(status)
<class 'bool'>
>>> #None-when we are unsure about the values we will use none
>>> status=None
>>> type(status)
<class 'NoneType'>
>>> #frozen set-we cannot add or remove data.where it contains unoique values
>>> s=frozen({3,8})
Traceback (most recent call last):
  File "<pyshell#55>", line 1, in <module>
    s=frozen({3,8})
NameError: name 'frozen' is not defined. Did you mean: 'frozenset'?
>>> s=frozenset({3,8})
>>> s
frozenset({8, 3})
>>> type(s)
<class 'frozenset'>
