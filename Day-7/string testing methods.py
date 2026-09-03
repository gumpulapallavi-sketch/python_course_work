Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.

================================== RESTART: C:\Users\gumpu\OneDrive\Desktop\python course work\Day-6\string methods.py ==================================
#string Testing methods
c='python.py'
c
'python.py'
c.startswith('str')
False
c.startswith('py')
True
c.startswith('python')
True
c.isalpha()
False
c.isalnum()
False
's6734'.isalnum()
True
c.islower()
True
c.isupper()
False
'    '.isspace()
True
'v   '.isspace()
False
c.istitle()
False
'i love india'.istitle()
False
'I Love India'.istitle()
True
'my.var'.isidentifier()
False
'my_var'.isidentifier()
True
'my9var'.isidentifier()
True

======================================= RESTART: C:/Users/gumpu/OneDrive/Desktop/python course work/Day-7/list.py =======================================
#list
l=[]
l=list
l=list()
l=[2,4=5j,'pallavi',499.00,[1,2,3],{2,4,5},{1:3,4:5,5:7},True,False]
SyntaxError: cannot assign to literal here. Maybe you meant '==' instead of '='?
l
[]
>>> l=[2,4+5j,'pallavi',499.00,[1,2,3],{2,4,5},{1:3,4:5,5:7},True,False]
>>> type(l)
<class 'list'>
>>> l=[2,4,5,8]
>>> m=[4,5,3,9]
>>> l+m
[2, 4, 5, 8, 4, 5, 3, 9]
>>> m*4
[4, 5, 3, 9, 4, 5, 3, 9, 4, 5, 3, 9, 4, 5, 3, 9]
>>> l*2
[2, 4, 5, 8, 2, 4, 5, 8]
>>> 1
1
>>> l
[2, 4, 5, 8]
>>> l[0]
2
>>> l[3]
8
>>> l[-1]
8
>>> l[1:]
[4, 5, 8]
>>> l[:2]
[2, 4]
>>> l[::1]
[2, 4, 5, 8]
>>> l[::-1]
[8, 5, 4, 2]
>>> 4 in l
True
>>> 4 in not l
SyntaxError: invalid syntax
>>> 4 in not l
SyntaxError: invalid syntax
>>> 4 not in l
False
8 not in l
False
6 not in l
True
