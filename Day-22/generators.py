# Generators: A generator is a function that uses yield instead of return.
# Calling a generator function returns a generator object, which can be iterated using for loops or the next() function.

'''
def retrivedata():
    data = ['1...100','101...200','201...300','301...400','401...500']
    for i in data:
        yield i

reels = retrivedata()

while True:
    status = input("[s]crol or [q]uit: ")
    if status == 's':
        print(next(reels))
    else:
         break


# even numbers
 
def even():
    i=0
    while True:
        i+=2
        yield i

n= 50
res = even()
for i in range(n):
    print(next(res))
  
# factors

def factors(n):
    for i in range(1,n+1):
        if n%i==0:
            yield i

n=30
res = factors(n)
for i in res :
    print(i)

# prime numbers
def isprime(n):
    for j in range(2,n//2+1):
        if n%j==0:
            return False
    return True
    
def prime(n):
    for i in range(2,n+1):
        if isprime(i):
            yield i

n=10
res = prime(n)
for i in res :
    print(i)
  

def countnum(n):
    count = 0
    while count < 1:
        yield count
        count -= 1
n=10
for n in countnum(5):
    print(n)
    '''

