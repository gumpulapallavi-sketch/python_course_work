Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> 
========================== RESTART: C:/Users/gumpu/OneDrive/Desktop/python course work/Day-2/Keywords.py ==========================
Traceback (most recent call last):
  File "C:/Users/gumpu/OneDrive/Desktop/python course work/Day-2/Keywords.py", line 1, in <module>
    g
NameError: name 'g' is not defined
>>> import keyword
>>> print(keyword.kwlist)
['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
>>> print(len(keyword.kwlist))
35
