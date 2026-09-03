Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.

====================================== RESTART: C:\Users\gumpu\OneDrive\Desktop\python course work\Day-6\methods.py =====================================
#Methods
c="python programming"
len(c)
18
ord(c)
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    ord(c)
TypeError: ord() expected a character, but string of length 18 found
ord('g')
103
ord('p')
112
ord('m')
109
min(c)
' '
max(c)
'y'
sorted(c)
[' ', 'a', 'g', 'g', 'h', 'i', 'm', 'm', 'n', 'n', 'o', 'o', 'p', 'p', 'r', 'r', 't', 'y']
chr("o")
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    chr("o")
TypeError: 'str' object cannot be interpreted as an integer
chr(65)
'A'
chr(75)
'K'
chr(56)
'8'
chr(83)
'S'
c='string is immutable'
c
'string is immutable'
c.uppercase()
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    c.uppercase()
AttributeError: 'str' object has no attribute 'uppercase'
c.upper()
'STRING IS IMMUTABLE'
c.lower()
'string is immutable'
c.swapcase()
'STRING IS IMMUTABLE'
c.title()
'String Is Immutable'
'Sdfgthu9uwijhio'.casefold()
'sdfgthu9uwijhio'
SEATUEWBJUkoieybf.casefold()
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    SEATUEWBJUkoieybf.casefold()
NameError: name 'SEATUEWBJUkoieybf' is not defined
'SEATUEWBJUkoieybf'.casefold()
'seatuewbjukoieybf'
# Alignments & Formatting
c.center(40,'_')
'__________string is immutable___________'
c.center(40,'*')
'**********string is immutable***********'
c.center(40,'%')
'%%%%%%%%%%string is immutable%%%%%%%%%%%'
c.center(40,'-')
'----------string is immutable-----------'
c.ljust()
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    c.ljust()
TypeError: ljust expected at least 1 argument, got 0
c.ljust(40,'-')
'string is immutable---------------------'
c.rjust(40,'-')
'---------------------string is immutable'
'12'.zfill(5)
'00012'
'12'.zfill(2)
'12'
'12'.zfill(3)
'012'
'12'.zfill(10)
'0000000012'
'12'.zfill(1)
'12'
#Methods
c.find('i')
3
c.find('x')
-1
c.find('s')
0
c.rfind('i')
10
c.rfind('d')
-1
c.index('i')
3
c.index('d')
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    c.index('d')
ValueError: substring not found
c.index('g')
5
c.count('p')
0
c.count('i')
3
c.count('m')
2
c.count('s')
2
c
'string is immutable'
c.replace('s','2')
'2tring i2 immutable'
c.replace('i','3')
'str3ng 3s 3mmutable'
c.replace('i','#')
'str#ng #s #mmutable'
c.replace('string','Float')
'Float is immutable'
c.maketrans('aeiou','12345')
{97: 49, 101: 50, 105: 51, 111: 52, 117: 53}
c.translate(c.maketrans('aeiou','12345'))
'str3ng 3s 3mm5t1bl2'
#splitting & joining methods
c.split()
['string', 'is', 'immutable']
c.split(',')
['string is immutable']
'string', 'is', 'immutable'.split()
('string', 'is', ['immutable'])
['string is immutable']
['string is immutable']
'strind, is, immutable'.split(',')
['strind', ' is', ' immutable']
'strind, is, immutable'.split('*')
['strind, is, immutable']
'strind- is- immutable'.split('*')
['strind- is- immutable']
'string is immutable'.rsplit()
['string', 'is', 'immutable']
'string is immutable'.rsplit( '',-)
SyntaxError: invalid syntax
'string is immutable'.rsplit( '',,)
SyntaxError: invalid syntax
s='''
python programming language
java
c '''
s
'\npython programming language\njava\nc '
'string is immutable'.rsplit('',)
Traceback (most recent call last):
  File "<pyshell#74>", line 1, in <module>
    'string is immutable'.rsplit('',)
ValueError: empty separator
'string is immutable'.rsplit('',1)
Traceback (most recent call last):
  File "<pyshell#75>", line 1, in <module>
    'string is immutable'.rsplit('',1)
ValueError: empty separator
s
'\npython programming language\njava\nc '
s.splitlines()
['', 'python programming language', 'java', 'c ']
s,join
Traceback (most recent call last):
  File "<pyshell#78>", line 1, in <module>
    s,join
NameError: name 'join' is not defined
s.join()
Traceback (most recent call last):
  File "<pyshell#79>", line 1, in <module>
    s.join()
TypeError: str.join() takes exactly one argument (0 given)
s.join(s)
'\n\npython programming language\njava\nc p\npython programming language\njava\nc y\npython programming language\njava\nc t\npython programming language\njava\nc h\npython programming language\njava\nc o\npython programming language\njava\nc n\npython programming language\njava\nc  \npython programming language\njava\nc p\npython programming language\njava\nc r\npython programming language\njava\nc o\npython programming language\njava\nc g\npython programming language\njava\nc r\npython programming language\njava\nc a\npython programming language\njava\nc m\npython programming language\njava\nc m\npython programming language\njava\nc i\npython programming language\njava\nc n\npython programming language\njava\nc g\npython programming language\njava\nc  \npython programming language\njava\nc l\npython programming language\njava\nc a\npython programming language\njava\nc n\npython programming language\njava\nc g\npython programming language\njava\nc u\npython programming language\njava\nc a\npython programming language\njava\nc g\npython programming language\njava\nc e\npython programming language\njava\nc \n\npython programming language\njava\nc j\npython programming language\njava\nc a\npython programming language\njava\nc v\npython programming language\njava\nc a\npython programming language\njava\nc \n\npython programming language\njava\nc c\npython programming language\njava\nc  '
s.join()s='''
python programming language
java
c '''
SyntaxError: invalid syntax
s.join(python programming language
java
       
SyntaxError: invalid syntax. Perhaps you forgot a comma?
s.join(python programming language java)
       
SyntaxError: invalid syntax. Perhaps you forgot a comma?
s.join(python programming language java,"")
       
SyntaxError: invalid syntax. Perhaps you forgot a comma?
s.join(python, programming language, java,"")
       
SyntaxError: invalid syntax. Perhaps you forgot a comma?
# whitespace & trimming methods
       
' Hello World  '
       
' Hello World  '
c.strip
       
<built-in method strip of str object at 0x000001CFF3A19D30>
c.strip()
       
'string is immutable'
c='Hello World'
       
c
       
'Hello World'
>>> c.strip()
...        
'Hello World'
>>> c.lstrip()
...        
'Hello World'
>>> c='  Hello World  '
...        
>>> c
...        
'  Hello World  '
>>> c.strip()
...        
'Hello World'
>>> c.rstrip()
...        
'  Hello World'
>>> c.lstrip()
...        
'Hello World  '
>>> text="Hello नमस्ते你好 café 🙂"
...        
>>> text.encode()
...        
b'Hello \xe0\xa4\xa8\xe0\xa4\xae\xe0\xa4\xb8\xe0\xa5\x8d\xe0\xa4\xa4\xe0\xa5\x87\xe4\xbd\xa0\xe5\xa5\xbd caf\xc3\xa9 \xf0\x9f\x99\x82'
>>> b'Hello \xe0\xa4\xa8\xe0\xa4\xae\xe0\xa4\xb8\xe0\xa5\x8d\xe0\xa4\xa4\xe0\xa5\x87\xe4\xbd\xa0\xe5\xa5\xbd caf\xc3\xa9 \xf0\x9f\x99\x82'.decode()
...        
'Hello नमस्ते你好 café 🙂'
>>> 'Hello 🙂'
...        
'Hello 🙂'
>>> text='Hello 🙂'
...        
>>> text.encode()
...        
b'Hello \xf0\x9f\x99\x82'
>>> b'Hello \xf0\x9f\x99\x82'.decode()
...        
'Hello 🙂'
>>> #encoding & decoding
       
