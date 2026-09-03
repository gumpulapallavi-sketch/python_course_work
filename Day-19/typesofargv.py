# types of arguments
#1. positional argument-it depends on the position 

'''
def display(name,email,password):
    print(f'name: {name}')
    print(f'email: {email}')
    print(f'password: {password}')

display("pallavi","pallavi@gmail.com","pallavi@2215")
display("pallavi@2215","pallavi","pallavi@gmail.com")
display("pallavi@gmail.com","pallavi@2215","pallavi")


# 2. Keyword argument-it depends on the key but not position

def display(name,email,password):
    print(f'name: {name}')
    print(f'email: {email}')
    print(f'password: {password}')

display(name="pallavi",email="pallavi@gmail.com",password="pallavi@2215")
display(password="pallavi@2215",name="pallavi",email="pallavi@gmail.com")
display(email="pallavi@gmail.com",password="pallavi@2215",name="pallavi")

# 3. default arguments-setting a default value for a parameter because of not to get errors.
# default arguments are written at the end of the parameters

def display(name,email='gmail.com',password=''):
    print(f'name: {name}')
    print(f'email: {email}')
    print(f'password: {password}')

display("pallavi","pallavi@gmail.com","pallavi@2215")
display("pallavi","palavi@gmail.com")
display("pallavi","pallavi@2215")


# 3. variable argument- a. positional variable argument
                        b. key variable argument

# a. positional variable argument:

def display(*names):
    print(names)

display('pallavi')
display('pallavi','priya')
display('pallavi','priya','sri')
display('pallavi','priya','sri','seetha')


# b. key variable argument
# To print Keyword Variable Length Arguments (**kwargs).
#the arguments are passed as a dictionary.
#these are used when we do not know how many keyword arguments will be passed to the function.

def display(**products):
    print(products)
display(bag=5000)
display(bag=5000,book=30)
display(bag=5000,book=30,bottle=10)

'''

