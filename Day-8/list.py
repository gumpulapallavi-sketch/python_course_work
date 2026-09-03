Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.

============================ RESTART: C:/Users/gumpu/OneDrive/Desktop/python course work/Day-8/list.py ============================
l=[1,3,'pallavi',2.6,True]
l
[1, 3, 'pallavi', 2.6, True]
l.apppend(6)
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    l.apppend(6)
AttributeError: 'list' object has no attribute 'apppend'. Did you mean: 'append'?
l.append(6)
l
[1, 3, 'pallavi', 2.6, True, 6]
l.append(3)
l
[1, 3, 'pallavi', 2.6, True, 6, 3]
l.index(3)
1
l
[1, 3, 'pallavi', 2.6, True, 6, 3]
l.extend(4,90)
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    l.extend(4,90)
TypeError: list.extend() takes exactly one argument (2 given)
id(1)
140715588240504
id(l)
2832962517120
id(l)
2832962517120
l.append('seetha')
l
[1, 3, 'pallavi', 2.6, True, 6, 3, 'seetha']
id(l)
2832962517120
l[5]
6
l[2]
'pallavi'
l[2]=10
l
[1, 3, 10, 2.6, True, 6, 3, 'seetha']
l.insert(4,10)
l
[1, 3, 10, 2.6, 10, True, 6, 3, 'seetha']
l.insert(10)
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    l.insert(10)
TypeError: insert expected 2 arguments, got 1
l.insert(6,10)
l
[1, 3, 10, 2.6, 10, True, 10, 6, 3, 'seetha']
l.extend(10,20,20)
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    l.extend(10,20,20)
TypeError: list.extend() takes exactly one argument (3 given)
l.extend(1,20)
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    l.extend(1,20)
TypeError: list.extend() takes exactly one argument (2 given)
l.extend[1,20]
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    l.extend[1,20]
TypeError: 'builtin_function_or_method' object is not subscriptable
l.extend([1,20])
l
[1, 3, 10, 2.6, 10, True, 10, 6, 3, 'seetha', 1, 20]
2
2
l.pop()
20
l.pop()
1
l
[1, 3, 10, 2.6, 10, True, 10, 6, 3, 'seetha']
l.remove(2.6)
l
[1, 3, 10, 10, True, 10, 6, 3, 'seetha']
l.remove(3)
del l[1]
l
[1, 10, True, 10, 6, 3, 'seetha']
l.clear()
l
[]
id(l)
2832962517120
l
[]
l=[1, 3, 10, 2.6, 10, True, 10, 6, 3, 'seetha']
l
[1, 3, 10, 2.6, 10, True, 10, 6, 3, 'seetha']
max(l)
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    max(l)
TypeError: '>' not supported between instances of 'str' and 'int'
max(l)
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    max(l)
TypeError: '>' not supported between instances of 'str' and 'int'
l
[1, 3, 10, 2.6, 10, True, 10, 6, 3, 'seetha']
max[l]
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    max[l]
TypeError: 'builtin_function_or_method' object is not subscriptable
max(l)
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    max(l)
TypeError: '>' not supported between instances of 'str' and 'int'
l=[1,4,10,6,5,3]
l
[1, 4, 10, 6, 5, 3]
max(l)
10
min(l)
1
sorted(l)
[1, 3, 4, 5, 6, 10]
l.reverse(l)
Traceback (most recent call last):
  File "<pyshell#55>", line 1, in <module>
    l.reverse(l)
TypeError: list.reverse() takes no arguments (1 given)
l.reverse()
l
[3, 5, 6, 10, 4, 1]
l.sort()
l
[1, 3, 4, 5, 6, 10]
l.sort(reverse=True)
l
[10, 6, 5, 4, 3, 1]
sum(l)
29
l=[1,2,3]
m=[1,2,3]
l
[1, 2, 3]
m
[1, 2, 3]
n=l
n
[1, 2, 3]
l
[1, 2, 3]
n.append(4)
n
[1, 2, 3, 4]
l
[1, 2, 3, 4]
m=l.copy()
m
[1, 2, 3, 4]
l
[1, 2, 3, 4]
m.append(5)
m
[1, 2, 3, 4, 5]
l
[1, 2, 3, 4]
id()l
SyntaxError: invalid syntax
id(l)
2832962596544
any([1,'',[],(),set(),{},False)
    
SyntaxError: closing parenthesis ')' does not match opening parenthesis '['
any([1,'',[],(),set(),{},False])
    
True
all([1,'',[],(),set(),{},False])
    
False
l.index(l)
    
Traceback (most recent call last):
  File "<pyshell#84>", line 1, in <module>
    l.index(l)
ValueError: list.index(x): x not in list
l
    
[1, 2, 3, 4]
l.count(3)
    
1
l.count(1)
    
1
l.count(0)
    
0
l
    
[1, 2, 3, 4]
>>> l
...     
[1, 2, 3, 4]
>>> l=[[1, 2, 3, 4],[4,3,9,7]]
...     
>>> l
...     
[[1, 2, 3, 4], [4, 3, 9, 7]]
>>> l[0]
...     
[1, 2, 3, 4]
>>> l[1]
...     
[4, 3, 9, 7]
>>> l[0][1]
...     
2
>>> l[0][3]
...     
4
>>> l[1][4]
...     
Traceback (most recent call last):
  File "<pyshell#97>", line 1, in <module>
    l[1][4]
IndexError: list index out of range
>>> l[1][3]
...     
7
>>> l[-1][-1]
...     
7
>>> l[-2][-1]
...     
4
>>> #Tuple
    
...     




