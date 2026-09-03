# A regular expression (regex) is a sequence of characters that defines a search pattern, mainly used for string matching and manipulation. 
# It’s like a powerful "find and filter" tool for text.
# Validation: Check if input follows rules (emails, phone numbers, passwords).
#Searching: Locate specific words, numbers, or patterns in text.
#Replacing: Clean or transform text (remove spaces, replace symbols).
#Data extraction: Pull out useful information (dates, hashtags, IDs).
'''
import re
pattern = r'[a-zA-Z]'
text = 'codegnan'
res = re.match(pattern,text)  #match is uesd check whether it is starting with the pattern or not
print(res.group() if res else "pattern not found")

import re
pattern = r'[a-zA-Z]'
text = 'codegnan'
res = re.search(pattern,text)  #search is uesd check whether the pattern is present or not
print(res.group() if res else "pattern not found")

import re
pattern = r'[0-9a-z]'
text = 'codegnan 2026 python version 3.14'
res = re.findall(pattern,text)  #findall is used to return all
print(res)

import re
pattern = r'[0-9a-z]'
text = 'codegnan 2026 python version 3.14'
res = re.finditer(pattern,text)  #finditer is used to return index values also
for i in res:
    print(i.group(),i.start())
   
import re
pattern = r'[0-9]{10}'
text = '3072768909'
res = re.fullmatch(pattern,text)  #fullmatch is used for validation
print(res.group() if res else "pattern not found")

import re
pattern = r'[,(#]'
text = 'java,python(html#css' 
res = re.split(pattern,text)   #split is uesd whenever we have more than 1 special character


import re
pattern = r'[a-z]'
text = 'python version 3.14, batch-63' 
res = re.sub(pattern,'*',text)            # sub is used to replace the pattern
print(res)


#RegEx Metacharacters

import re
pattern = r'e.t'    # in the palce of '.' we can use any other (or) Matches any single character except newline
text = 'e@t esst eaat est eat ett ect gahytk JGSUSN Hsijh' 
res = re.findall(pattern,text)            
print(res)


import re
pattern = r'^(91)'    # Beginning of the string
text = '9126724895680' 
res = re.findall(pattern,text)            
print(res)

import re
pattern = r'0$'    # End of the string
text = '9326724895680' 
res = re.findall(pattern,text)            
print(res)

import re
pattern = r'to+'    # One or more occurrences
text = 'to ruhgoir tojglt tooo tooh to too toooo tnhoehff' 
res = re.findall(pattern,text)            
print(res)

import re
pattern = r'ab*'    # zero or more occurrences
text = 'ab abbb abb abbaa abbba aabb aabbbb' 
res = re.findall(pattern,text)            
print(res)
'''

import re
pattern = r'0|91'    # Zero or one occurrence
text = '07489' 
res = re.findall(pattern,text)            
print(res)

# Character Classes
import re
pattern = r'[aeiou]'    # Zero or one occurrence
text = 'codegnan programming' 
res = re.findall(pattern,text)            
print(res)

