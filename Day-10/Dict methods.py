Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.

====================== RESTART: C:/Users/gumpu/OneDrive/Desktop/python course work/Day-10/dict operations.py ======================
#Dict operations
data={'name':'pallavi','batch':63,'course':'PFS'}
data
{'name': 'pallavi', 'batch': 63, 'course': 'PFS'}
data['name']
'pallavi'
data['batch']
63
data['course']
'PFS'
63 in data
False
data['data']
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    data['data']
KeyError: 'data'
data['age']
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    data['age']
KeyError: 'age'
'batch' in data
True
data['age']=21
data
{'name': 'pallavi', 'batch': 63, 'course': 'PFS', 'age': 21}
#update
data['skills']=['python','mysql','flask']
data
{'name': 'pallavi', 'batch': 63, 'course': 'PFS', 'age': 21, 'skills': ['python', 'mysql', 'flask']}
#get
data.get
<built-in method get of dict object at 0x000001EBF950D5C0>
data.get('age','key is not present')
21
data.get('course','key is not present')
'PFS'
#remove
data.pop('name')
'pallavi'
data
{'batch': 63, 'course': 'PFS', 'age': 21, 'skills': ['python', 'mysql', 'flask']}
data.pop('skills')
['python', 'mysql', 'flask']
#delete
del data['course']
data
{'batch': 63, 'age': 21}
#popitem
data.popitem()
('age', 21)
#it removes the last item from the dict
data
{'batch': 63}
#clear
data.clear()
data
{}
#update
data.update({'phno':9876432567,'email':'gumpulapallavi@gmail.com'})
data
{'phno': 9876432567, 'email': 'gumpulapallavi@gmail.com'}
data.clear()
data
{}
{'name': 'pallavi', 'batch': 63, 'course': 'PFS', 'age': 21, 'skills': ['python', 'mysql', 'flask']}
{'name': 'pallavi', 'batch': 63, 'course': 'PFS', 'age': 21, 'skills': ['python', 'mysql', 'flask']}
data={'name': 'pallavi', 'batch': 63, 'course': 'PFS', 'age': 21, 'skills': ['python', 'mysql', 'flask']}
data
{'name': 'pallavi', 'batch': 63, 'course': 'PFS', 'age': 21, 'skills': ['python', 'mysql', 'flask']}
#keys()-to extract the keys of the dict
data.keys()
dict_keys(['name', 'batch', 'course', 'age', 'skills'])
#values()-to extract the values of the dict
data.values()
dict_values(['pallavi', 63, 'PFS', 21, ['python', 'mysql', 'flask']])
#sorted
sorted(data,reverse=True)
['skills', 'name', 'course', 'batch', 'age']

data
{'name': 'pallavi', 'batch': 63, 'course': 'PFS', 'age': 21, 'skills': ['python', 'mysql', 'flask']}
max(data)
'skills'
min(data)
'age'
len(data)
5
any(data)
True
all(data)
True
#copy-creates the shallow copy
>>> a={1:1,2:2,3:3}
>>> b=a
>>> b[4]=4
>>> b
{1: 1, 2: 2, 3: 3, 4: 4}
>>> a
{1: 1, 2: 2, 3: 3, 4: 4}
>>> c=a.copy()
>>> a
{1: 1, 2: 2, 3: 3, 4: 4}
>>> b
{1: 1, 2: 2, 3: 3, 4: 4}
>>> #setdefault()-whenever their is no data we use to set key with the default
>>> data.setdefault()
Traceback (most recent call last):
  File "<pyshell#64>", line 1, in <module>
    data.setdefault()
TypeError: setdefault expected at least 1 argument, got 0
>>> data.setdefault('age'=0)
SyntaxError: expression cannot contain assignment, perhaps you meant "=="?
>>> data.setdefault('age'0)
SyntaxError: invalid syntax. Perhaps you forgot a comma?
>>> data.setdefault('age',0)
21
>>> data
{'name': 'pallavi', 'batch': 63, 'course': 'PFS', 'age': 21, 'skills': ['python', 'mysql', 'flask']}
>>> data.setdefault('phn',0)
0
>>> #fromkeys()-creates dict with default values
>>> d=dict.formkeys(['a','b'],0)
Traceback (most recent call last):
  File "<pyshell#71>", line 1, in <module>
    d=dict.formkeys(['a','b'],0)
AttributeError: type object 'dict' has no attribute 'formkeys'. Did you mean: 'fromkeys'?
>>> d=dict.fromkeys(['a','b'],0)
>>> d
{'a': 0, 'b': 0}
