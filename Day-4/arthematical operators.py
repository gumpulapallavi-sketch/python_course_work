Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
a=10
b=6
a+b
16
a-b
4
a/b
1.6666666666666667
a//b
1
a**b
1000000
a*b
60
a%b
4
9%3
0
2**5
32
9=39
SyntaxError: cannot assign to literal here. Maybe you meant '==' instead of '='?
9+39
48
2*9
18
2**5
32
#comparision operators
a=10
b=6
a<b
False
a.b
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    a.b
AttributeError: 'int' object has no attribute 'b'
a>b
True
a<=b
False
a>b
True
a>=b
True
a==b
False
a!=b
True
True#
True
#assignment operators
c=10
c=c+10
c=c+20
c=c+30

c=10


c=10
10
10
c=c+10

c
20
c=c+20
c
40
c=c+30
c
70
c+=10
c
80
c-=20
c
60
c/=3
c
20.0
c//=2
c
10.0
c**=3
c
1000.0
c%=3
c
1.0
#Relational opertions
n=10
n%2==0
True
n%3==0
False
n%5==0
True
n%2==0 and n%3==0
False
n%2==0 or n%3==0
True
True
True
n
10
n>10
False
n<10
False
n=10
not n<5
True
not n>5
False
#Membership operators-it is going to work on the #str list tuple set dict
#Membership operators-it is going to work on the data types #str list tuple set dict
s='pallavi'
'a'is in s
SyntaxError: invalid syntax
'a' in s
True
'v'in s
True
'b in s'
'b in s'

'b' in s
False
'b'not in s
True
#list
l=[1,9,20,'pallavi']
l
[1, 9, 20, 'pallavi']
'pallavi' in l
True
'p' in  l
False
'1' in l
False
'1' in l
False
'1' in l
False
l
[1, 9, 20, 'pallavi']
1 in l
True
s={1,2,3,4}
1 in s
True
2 not  in s
False
5 in s
False

#tuple
t=(1,2,8,0)
t
(1, 2, 8, 0)
1 in t
True
8 in t
True
#dict
d=
SyntaxError: invalid syntax


d={'name':'pallavi','id':200,'age':21}
d
{'name': 'pallavi', 'id': 200, 'age': 21}
'abdul'in d
False
'name' in d
True
200 in d
False
'age' in d
True
#identity operators
l=[1,2,3,4,5]
m=[1,2,3,4,5]
id(2)
140716228789400
id(l)
2512409673088
id(2)
140716228789400
l is m
False
l is not m
True
n=5
1 in l
True
5 in m
True
l in n
Traceback (most recent call last):
  File "<pyshell#121>", line 1, in <module>
    l in n
TypeError: argument of type 'int' is not a container or iterable
l in m
False
l is not  m
True
# mutable& immutable
d={'name':'pallavi','id':200,'age':21}
d
{'name': 'pallavi', 'id': 200, 'age': 21}
id(d)
2512367238976
s={1,2,3,4}
>>> id(s)
2512409354400
>>> s.add(5)
>>> s
{1, 2, 3, 4, 5}
>>> id(s)
2512409354400
>>> #mutable-we can change with in the memory or obj referencee
>>> #immutable-we cannot change with in the memory or obj reference
>>> 
>>> #Bitwise operators
>>> #AND
>>> 2&9
0
>>> 4&7
4
>>> #OR
>>> 5|8
13
>>> 4|4
4
>>> #NOT
>>> ~5
-6
>>> ~9
-10
>>> ~5
-6
>>> #RIGHT SHIFT
>>> >>2
SyntaxError: invalid syntax
>>> 2>>2
0
>>> 5>>8
0
>>> 9>>3
1
>>> 9>>2
2
>>> #LEFT SHIFT
>>> 3<<6
192
>>> 3<<1
6
>>> 8<<3
64
