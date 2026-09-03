#Function Syntax
'''
General Syntax

def function_name(parameters):
"""
Docstring explaining the purpose of the function.
"""
statements
return value
function_name(arguments)

# Display details

def display(name,email,password):
    print(f' Hello {name}')
    print(f' Your email: ,{email}')
    print(f'Your password {password}')

display('pallavi','gumpulapallavi@gmail.com','pallavi123@')
display('avi','avi@gmail.com','avi123@')
display('anvitha','anvitha@gmail.com','anvi123@')


# Leap year 

def isleapyear(year):
    if year%400==0 or (year%4==0 and year%100!=0):
        print(f'{year} is a leap year')
    else:
        print(f'{year} not a leap year')

for year in range(2000,2027):
    isleapyear(year)


# sum of digits using while

def sumofdigits(n):
    sum=0
    while n>0:
        sum += n%10
        n=n//10
    return sum

n=int(input("Enter the number: "))
print(f'sum of {n} digits is {sumofdigits(n)}')



# product of digits using while

def productofdigits(n):
    product=1
    while n>1:
        product *= n%10
        n=n//10
    return product

n=int(input("Enter the number: "))
print(f'product of {n} digits is {productofdigits(n)}')


# password : weak password,strong password


def checkpassword(password):
    if len(password)> 8:
        check = set()
        for i in password:
            if i.isupper():
                check.add('u')
            elif i.islower():
                check.add('l')
            elif i.isdigit():
                check.add('d')
            else:
                check.add('s')
        if len(check) == 4:
            return "strong password"
    return "weak password"


password = input("enter the password: ")
print(f'password is {checkpassword(password)}')

'''
# Tables (2-20):


