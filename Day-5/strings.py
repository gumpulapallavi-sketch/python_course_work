Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.

= RESTART: C:/Users/gumpu/OneDrive/Desktop/python course work/Day-5/strings.py =
s=''
s
''
s='pallavi'
s
'pallavi'
'pallavi'+'seetha'
'pallaviseetha'
'pallaviseetha'*5
'pallaviseethapallaviseethapallaviseethapallaviseethapallaviseetha'
'_*_'*5
'_*__*__*__*__*_'
'pallavi'*6
'pallavipallavipallavipallavipallavipallavi'
'pallavi  '*6
'pallavi  pallavi  pallavi  pallavi  pallavi  pallavi  '
#indexing
s='pallavi'
s[3]
'l'
s[7]
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    s[7]
IndexError: string index out of range
s[5]
'v'
s[-1]
'i'
s[-3]
'a'
#slicing
s[:-3]
'pall'
s[:3]
'pal'
>>> s[1:3]
'al'
>>> s='pallavi ammu priya '
>>> s[1:5}
SyntaxError: closing parenthesis '}' does not match opening parenthesis '['
>>> s[1:5]
'alla'
>>> s[:5]
'palla'
>>> s[:-3]
'pallavi ammu pri'
>>> s[-1:-3;-1]
SyntaxError: invalid syntax
>>> s[-1:-3:-1]
' a'
>>> s[:-3:-1]
' a'
>>> s[::-2]
' yr maialp'
>>> s[::]
'pallavi ammu priya '
>>> #s[start:end+1:step]=>s[0:len:1]
>>> s[-8:-3:-1]
''
>>> s[-8:-14:-1]
'umma i'
>>> s[-9:-16:-1]
'mma iva'
>>> s[::2]
'plaiam ry '
>>> s[::]
'pallavi ammu priya '
>>> 'pallavi ammu priya '
'pallavi ammu priya '
>>> 'pallavi' in s
True
>>> 'pall' in s
True
>>> 'sai' in s
False
>>> 'ammu' in s
True
