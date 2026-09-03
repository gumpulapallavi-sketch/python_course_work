Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.

========================= RESTART: C:/Users/gumpu/OneDrive/Desktop/python course work/Day-9/set & dict.py =========================
#Set
s=set()
#set is a mutable, allow unique vsues,heterogeneous,doesn't allow duplicates,unordered,only allow immutable items are allowed
type(s)
<class 'set'>
s={1,3,5,6,7,94,48}
\
s
{48, 1, 3, 5, 6, 7, 94}
a=1,5,34,5
b=5,7,8,9,7
a+b
(1, 5, 34, 5, 5, 7, 8, 9, 7)
s
{48, 1, 3, 5, 6, 7, 94}
s.add()
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    s.add()
TypeError: set.add() takes exactly one argument (0 given)
s.add(1)
s.add(12.3)
s.add(4+6j)
s.add()
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    s.add()
TypeError: set.add() takes exactly one argument (0 given)
s={1,3,54,6.8,7.09,True,'pallavi',(5+4j))}
SyntaxError: closing parenthesis ')' does not match opening parenthesis '{'
s={1,3,54,6.8,7.09,True,'pallavi',(5+4j)}
s
{1, (5+4j), 3, 6.8, 7.09, 54, 'pallavi'}
s={2,3,5,2,3,4,62,2,2,2,2}
s
{2, 3, 4, 5, 62}
a=1,5,34,5b=5,7,8,9,7
SyntaxError: invalid decimal literal
a=1,2,3,4,5
b=3,5,7,8,9
a
(1, 2, 3, 4, 5)
b
(3, 5, 7, 8, 9)
a|b
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    a|b
TypeError: unsupported operand type(s) for |: 'tuple' and 'tuple'
a | b
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    a | b
TypeError: unsupported operand type(s) for |: 'tuple' and 'tuple'
a={1,2,3,4,5}
b={3,5,7,8,9}
a
{1, 2, 3, 4, 5}
b
{3, 5, 7, 8, 9}
a|b
{1, 2, 3, 4, 5, 7, 8, 9}
a&b
{3, 5}
a-b
{1, 2, 4}
a^b
{1, 2, 4, 7, 8, 9}
{1, 2, 4, 7, 8, 9}
{1, 2, 4, 7, 8, 9}
#{1}{2}4{7}8{9}{1,2}{1,4}{1,7}{1,8}{1,9}{2,4}..........{1,2,4,7,8,9}
{1}<=a
True
#subset
{1}<=a
True
{2}<=a
True
{1,2}<=a
True
#super set
{1}>=a
False
{1,2}>=a
False
#disjoint
a.isdisjoint
<built-in method isdisjoint of set object at 0x000002228C8F5FC0>
a.isdisjoint(b)
False
a.isdisjoint({5,6})
False
a.isdisjoint({5,3})
False
#union
a.union(b)
{1, 2, 3, 4, 5, 7, 8, 9}
#intersection
a.intersection(b)
{3, 5}
#subset
a.subset(b)
Traceback (most recent call last):
  File "<pyshell#57>", line 1, in <module>
    a.subset(b)
AttributeError: 'set' object has no attribute 'subset'. Did you mean: 'issubset'?
a.issubset(b)
False
#superset
a.issuperset(b)
False
#membership operations
6 in a
False
9 in b
True
3 not in a
False
5 not in a
False
a
{1, 2, 3, 4, 5}
b
{3, 5, 7, 8, 9}
5 not in b
False
# Method
max(a)
5
max(b)
9
min(a)
1
min(b)
3
sorted(a)
[1, 2, 3, 4, 5]
sum(a)
15
a
{1, 2, 3, 4, 5}
b=a
b
{1, 2, 3, 4, 5}
a
{1, 2, 3, 4, 5}
# in this case we use copy() for not sharing the same reference
c=a.copy()
c.add(10)
a
{1, 2, 3, 4, 5}
b
{1, 2, 3, 4, 5}
c = a.copy()
c.add(10)
c
{1, 2, 3, 4, 5, 10}
a
{1, 2, 3, 4, 5}
b
{1, 2, 3, 4, 5}
#update-to add multiple elements we use update
a.update({20,30,40})
a
{1, 2, 3, 4, 5, 20, 40, 30}
#pop-remove the random element from the set
a.pop()
1
a.pop()
2
a.pop()
3
a
{4, 5, 20, 40, 30}

a.pop()
4
a
{5, 20, 40, 30}
#Remove- it gives the error if the element is not present in the set
a.remove(4)
Traceback (most recent call last):
  File "<pyshell#102>", line 1, in <module>
    a.remove(4)
KeyError: 4
a.remove(5)
a
{20, 40, 30}
#Discard- handles the errors
a.discard(5)
a
{20, 40, 30}
a.discard(30)
a
{20, 40}
len(a)
2
any(a)
True
all(a)
True
#Frozen set-same as set but is immutable where the set the mutable
a= frozenset({1,2,27,3,48})
a.add(49)
Traceback (most recent call last):
  File "<pyshell#115>", line 1, in <module>
    a.add(49)
AttributeError: 'frozenset' object has no attribute 'add'
a
frozenset({48, 1, 2, 3, 27})
#Dictionary- it is the collection of key value pairs enclosed b/w the '{}'
d={}
d=dict()
type(d)
<class 'dict'>
d={'k1':'v1','k2':'v2','k3':'v3','k4':'v4'}
d
{'k1': 'v1', 'k2': 'v2', 'k3': 'v3', 'k4': 'v4'}
id(d)
2347410790528
d['k5']='k5'
d
{'k1': 'v1', 'k2': 'v2', 'k3': 'v3', 'k4': 'v4', 'k5': 'k5'}
d['k5']='v5'
d
{'k1': 'v1', 'k2': 'v2', 'k3': 'v3', 'k4': 'v4', 'k5': 'v5'}
d['k1']='v15'
d
{'k1': 'v15', 'k2': 'v2', 'k3': 'v3', 'k4': 'v4', 'k5': 'v5'}
d={}
d[1]='int'
d
{1: 'int'}
d[2.45]='flt'
d
{1: 'int', 2.45: 'flt'}
d[3+4j]='com'
d
{1: 'int', 2.45: 'flt', (3+4j): 'com'}
d['str']=''string'
SyntaxError: unterminated string literal (detected at line 1)
d['str']='string'
d
{1: 'int', 2.45: 'flt', (3+4j): 'com', 'str': 'string'}
d[(2,5,4)]='tuple'
d
{1: 'int', 2.45: 'flt', (3+4j): 'com', 'str': 'string', (2, 5, 4): 'tuple'}
d[{2,5,4}]='set'
Traceback (most recent call last):
  File "<pyshell#142>", line 1, in <module>
    d[{2,5,4}]='set'
TypeError: cannot use 'set' as a dict key (unhashable type: 'set')
d[[2,5,4]]='set'
Traceback (most recent call last):
  File "<pyshell#143>", line 1, in <module>
    d[[2,5,4]]='set'
TypeError: cannot use 'list' as a dict key (unhashable type: 'list')
d[[2,5,4]]='lst'
Traceback (most recent call last):
  File "<pyshell#144>", line 1, in <module>
    d[[2,5,4]]='lst'
TypeError: cannot use 'list' as a dict key (unhashable type: 'list')
d
{1: 'int', 2.45: 'flt', (3+4j): 'com', 'str': 'string', (2, 5, 4): 'tuple'}
d[frozenset{1,2,3}]='fset'
SyntaxError: invalid syntax. Perhaps you forgot a comma?
d(frozenset{1,2,3})='fset'
SyntaxError: invalid syntax. Perhaps you forgot a comma?
d={}
d[1]=2
d[2]=2.45
d[3]=2+4j
d[4]='str'
d[5]=[1,2,3,4]
d[6]=(1,2,3,4)
d[7]={1,2,3,4}
d[8]={1:1,2:2,3:2,4:5}
d[9]=True
d
{1: 2, 2: 2.45, 3: (2+4j), 4: 'str', 5: [1, 2, 3, 4], 6: (1, 2, 3, 4), 7: {1, 2, 3, 4}, 8: {1: 1, 2: 2, 3: 2, 4: 5}, 9: True}
>>> #Membership- works for keys not for the values
>>> 5 in d
True
>>> True in d
True
>>> 'str' in d
False
>>> d[5]
[1, 2, 3, 4]
>>> d[2]
2.45
>>> #get()-handle the errors
>>> d.get(19)
>>> 
>>> d
{1: 2, 2: 2.45, 3: (2+4j), 4: 'str', 5: [1, 2, 3, 4], 6: (1, 2, 3, 4), 7: {1, 2, 3, 4}, 8: {1: 1, 2: 2, 3: 2, 4: 5}, 9: True}
>>> d.get(1)
2
>>> d.get(5,"key is not present")
[1, 2, 3, 4]
>>> d.get(10,"key is not present")
'key is not present'
>>> d
{1: 2, 2: 2.45, 3: (2+4j), 4: 'str', 5: [1, 2, 3, 4], 6: (1, 2, 3, 4), 7: {1, 2, 3, 4}, 8: {1: 1, 2: 2, 3: 2, 4: 5}, 9: True}
>>> #update
>>> d[5]=7
>>> d
{1: 2, 2: 2.45, 3: (2+4j), 4: 'str', 5: 7, 6: (1, 2, 3, 4), 7: {1, 2, 3, 4}, 8: {1: 1, 2: 2, 3: 2, 4: 5}, 9: True}
>>> d[6]=29
>>> d
{1: 2, 2: 2.45, 3: (2+4j), 4: 'str', 5: 7, 6: 29, 7: {1, 2, 3, 4}, 8: {1: 1, 2: 2, 3: 2, 4: 5}, 9: True}
>>> d[1]=29
>>> d
{1: 29, 2: 2.45, 3: (2+4j), 4: 'str', 5: 7, 6: 29, 7: {1, 2, 3, 4}, 8: {1: 1, 2: 2, 3: 2, 4: 5}, 9: True}
>>> d[2]=29
>>> d
{1: 29, 2: 29, 3: (2+4j), 4: 'str', 5: 7, 6: 29, 7: {1, 2, 3, 4}, 8: {1: 1, 2: 2, 3: 2, 4: 5}, 9: True}
