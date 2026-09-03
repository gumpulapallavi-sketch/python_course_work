# recursion - function calling itself
#syntax:
'''
def fun():
    if base_cond:
        return
    func(updating argv)

func(para)

# printing values from 1 to N using recursion

def display(n):
    if n>10:
        return
    print(n)
    display(n+1)

display(1)

def display(n):
    if n>10:
        return
    display(n+1)
    print(n)

display(1)

# sum of N natural numbers

def displaysum(n):
    if n==0:
        return 0
    return n+displaysum(n-1)

print(displaysum(10))

# Product of N natural numbers

def displayprod(n):
    if n==1:
        return 1
    return n*displayprod(n-1)

print(displayprod(10))

# printing the characters of a string using index value by recursion method
def display(i):
    if i== len(s):
        return 
    print(s[i],end='')
    display(i+1)
    
s="Python Programming"
display(0)

# reverse of a string

def display(i):
    if i== len(s):
        return 
    display(i+1)
    print(s[i],end='')
    
s="Python Programming"
display(0)

# printing character with character through the string in recursion function

def display(n):
    if n >len(s):
        return 
    print(s[:n])
    display(n+1)
    
s="Python"
display(1)

def display(ind,w):
    if ind>len(s)-w:
        return 
    print(s[ind:ind+w])
    display(ind+1,w)
    
s="Python Programming"
display(0,4)

# printing numbers 

def display(n):
    if n==0:
        return 
    display(n//10)
    print(n%10)
    
n=987654
display(n)

def display(n):
    if n==0:
        return 0
    return n%10+display(n//10)
    
n=987654
print(display(n))
'''

