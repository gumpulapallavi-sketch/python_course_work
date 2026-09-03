# 1.Write a program to print numbers from 1 to N using a for loop.
'''
n=int(input("Enter the number: "))
for i in range(1,n+1):
    print(i)
    '''

# 2. Print Even Numbers from 1 to N (Using for loop)
'''
n=int(input("Enter the number: "))
for i in range(0,n+1):
    if i%2==0:
        print(i)
        '''

# 3. Sum of Numbers from 1 to N (Using for loop)
'''
n=int(input("Enter the number: "))
sum=0
for i in range(1,n+1):
    sum = sum+i
print(sum)
'''

# 4. Print Odd Numbers from 1 to N (Using for loop)
'''
n=int(input("Enter the number: "))
for i in range(1,n,2):
    print(i)
'''

# 5. Find Factorial of a Number (Using for loop)
'''
n=int(input("Enter the number: "))
fact=1
for i in range(1,n+1):
    fact=fact*i
print(fact)
'''

# 6. Print Multiplication Table of N (Using for loop)
'''
n=int(input("Enter the number: "))
for i in range(1,11):
    print(n , '*', i ,'=', n*i)
    '''

# 7. Check Prime Number (Using for loop)
'''
n=int(input("Enter the number: "))
if n>1:
    for i in range(2,n):
        if n%i!=0:
           print('prime number')
        else:
            print('not a prime number')
'''
