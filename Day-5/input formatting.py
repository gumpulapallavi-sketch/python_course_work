Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.

==================================================== RESTART: C:/Users/gumpu/OneDrive/Desktop/python course work/input formating.py ====================================================
x=input()
Traceback (most recent call last):
  File "C:/Users/gumpu/OneDrive/Desktop/python course work/input formating.py", line 2, in <module>
    pallavi
NameError: name 'pallavi' is not defined
pallavi
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    pallavi
NameError: name 'pallavi' is not defined
pallavi
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    pallavi
NameError: name 'pallavi' is not defined
x=input()
pallavoi
x
'pallavoi'
name
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    name
NameError: name 'name' is not defined
name=pallavi
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    name=pallavi
NameError: name 'pallavi' is not defined
name='pallavi'
name
'pallavi'
age=21
age
21
names=input("enter the names:")
enter the names:pallavi priya sri
names
'pallavi priya sri'
names.split()
['pallavi', 'priya', 'sri']
names=input("enter the names:").split()
enter the names:pallavi priya sri
names
['pallavi', 'priya', 'sri']
names=input("enter the names:").split()
enter the names:1 2 83 04 58
names
['1', '2', '83', '04', '58']
map(int,names)
<map object at 0x000001EB636D8800>
list(map(int,names))
[1, 2, 83, 4, 58]
values=list(map(int,input().split()))
2 3 84 10 39
values
[2, 3, 84, 10, 39]
names=tuple(input("enter the name:").split)
enter the name:pallavi anu priya
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    names=tuple(input("enter the name:").split)
TypeError: 'builtin_function_or_method' object is not iterable
names=tuple(input("enter the name:").split)
enter the name:pallavi anu
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    names=tuple(input("enter the name:").split)
TypeError: 'builtin_function_or_method' object is not iterable
names=tuple(input("enter the name:").split)
enter the name:1 2 38
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    names=tuple(input("enter the name:").split)
TypeError: 'builtin_function_or_method' object is not iterable
names=tuple(input("enter the name:").split)
enter the name:
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    names=tuple(input("enter the name:").split)
TypeError: 'builtin_function_or_method' object is not iterable
names=tuple(input("enter the name:").split())
enter the name:pallavi anu
names
('pallavi', 'anu')
names=set(input("enter the name:").split())
enter the name:pallavi
names
{'pallavi'}
names=set(input("enter the name:").split())
enter the name:pallavi anu sri sai
names
{'sai', 'anu', 'sri', 'pallavi'}
values=set(map(int,input().split())
           1233 3989 389
           
SyntaxError: '(' was never closed
values=set(map(int,in[put().split()))
           
SyntaxError: closing parenthesis ')' does not match opening parenthesis '['
values=set(map(int,input().split()))
           
values
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    values=set(map(int,input().split()))
ValueError: invalid literal for int() with base 10: 'values'
values=set(map(int,input().split()))
           
values=set(map(int,input().split()))
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    values=set(map(int,input().split()))
ValueError: invalid literal for int() with base 10: 'values=set(map(int,input().split()))'
a,b=[1,2]
           
a
           
1
b
           
2
a,b=(1,2)
           
a
           
1
b
           
2
email,password=input("enter the email and password:).split()")
           
enter the email and password:).split()
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    email,password=input("enter the email and password:).split()")
ValueError: not enough values to unpack (expected 2, got 0)
email,password=input("enter the email and password:").split())
SyntaxError: unmatched ')'
email,password=input("enter the email and password:").split()
enter the email and password:gumpulapallavi@gmail.com 10294765
email
'gumpulapallavi@gmail.com'
passowrd
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    passowrd
NameError: name 'passowrd' is not defined. Did you mean: 'password'?
password
'10294765'
a,b,c=list(map(int,input().split()))
a,b,c
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    a,b,c=list(map(int,input().split()))
ValueError: invalid literal for int() with base 10: 'a,b,c'
a,b,c=list(map(int,input().split()))
89 56 78
a
89
b
56
c
78
values=set(map(int,input().split()))
45 78 70
values
{70, 45, 78}
values=set(map(float,input().split()))
68 687 97
values
{97.0, 68.0, 687.0}
values=tuple(map(int,input().split()))
23 783 067
values
(23, 783, 67)
values=tuple(map(float,input().split()))
35 02 56
values
(35.0, 2.0, 56.0)
name,marks=input().split()
pallavi 90
name
'pallavi'
marks
'90'
int(marksx)
Traceback (most recent call last):
  File "<pyshell#64>", line 1, in <module>
    int(marksx)
NameError: name 'marksx' is not defined. Did you mean: 'marks'?
int(marks)
90
#eval function -all the things and calculations can be easily done
e=eval(input())
3
e
3
e=eval(input())
2.99
e
2.99
e=eval(input())
1569.0
e
1569.0
e=eval(input())
true
Traceback (most recent call last):
  File "<pyshell#73>", line 1, in <module>
    e=eval(input())
  File "<string>", line 1, in <module>
    __import__('idlelib.run').run.main(True)
NameError: name 'true' is not defined. Did you mean: 'True'?
e=eval(input())

Traceback (most recent call last):
  File "<pyshell#74>", line 1, in <module>
    e=eval(input())

  File "<string>", line 0


    
SyntaxError: invalid syntax
e=eval(input())
1567.907
e
1567.907
e=eval(input())
"pallavi"
4
>>> e
'pallavi'
>>> e=eval(input())
{1,3,0,'pallavi'}
>>> e
{0, 1, 3, 'pallavi'}
>>> {1,3,0,'pallavi'}
{0, 1, 3, 'pallavi'}
>>> e=eval(input())
[1,3,66,0]
>>> e
[1, 3, 66, 0]
>>> e=eval(input())
{1:3,'pallavi:9}
Traceback (most recent call last):
  File "<pyshell#84>", line 1, in <module>
    e=eval(input())
  File "<string>", line 1
    {1:3,'pallavi:9}
         ^
SyntaxError: unterminated string literal (detected at line 1)
>>> {1:3,'pallavi':9}
...      
{1: 3, 'pallavi': 9}
>>> e=eval(input())
...      
e=eval(input())
Traceback (most recent call last):
  File "<pyshell#86>", line 1, in <module>
    e=eval(input())
  File "<string>", line 1
    e=eval(input())
           ^^^^^
SyntaxError: invalid syntax. Did you mean 'not'?
>>> e=eval(input())
...      
True
'
>>> e
...      
True
