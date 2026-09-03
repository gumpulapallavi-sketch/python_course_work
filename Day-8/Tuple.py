Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.

== RESTART: C:/Users/gumpu/OneDrive/Desktop/python course work/Day-8/Tuple.py ==
#Tuple
t=()
t=tuple()
t=(1,3,4,6,3,5)
s=(4,3,7,6,8)
t+s
(1, 3, 4, 6, 3, 5, 4, 3, 7, 6, 8)
t*5
(1, 3, 4, 6, 3, 5, 1, 3, 4, 6, 3, 5, 1, 3, 4, 6, 3, 5, 1, 3, 4, 6, 3, 5, 1, 3, 4, 6, 3, 5)
6 in t
True
9 in t
False
9 not in t
True
4 in s
True
5 not in s
True
t
(1, 3, 4, 6, 3, 5)
s
(4, 3, 7, 6, 8)
s[1]
3
s[2]
7
t[5]
5
t[-1]
5
t[::-1]
(5, 3, 6, 4, 3, 1)
t[::-2]
(5, 6, 3)
a=1,2,3
a
(1, 2, 3)
a
(1, 2, 3)
>>> a,b,c,d
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    a,b,c,d
NameError: name 'b' is not defined
>>> a,b,c,d=1,2,3,4
>>> a
1
>>> b
2
>>> c
3
>>> d
4
>>> a,b,c,d=t
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    a,b,c,d=t
ValueError: too many values to unpack (expected 4, got 6)
>>> a,b,c,d,e,f=t
>>> a
1
>>> b
3
>>> c
4
>>> d
6
>>> e
3
>>> f
5
>>> g
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    g
NameError: name 'g' is not defined
