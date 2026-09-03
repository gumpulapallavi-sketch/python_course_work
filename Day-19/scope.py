# Gobal variable- it is declared outside. it can be accessed inside and outside of the funtion.
# Local variable- it is declared inside the function.
'''
def display(n):
    n=n+10
    print('Inside:',n)

n=10
display(n)
print('Outside:',n)


def display(n):
    print('Inside:',n)

n=10
display(n)
print('Outside:',n)



#we can not access the local variable outside the function because it is defined inside the function.
def display():
    n=10
    print ('Inside:',n)

display()
print('outside:',n)


#we can access the global variable inside the function because it is defined outside
def display():
    global n
    n=10
    print('Inside:',n)
display()
print('outside:',n)

# example of global

def display():
    global n
    n='PFS'
    print("Updated Course:",n)

n='JFS'
display()
print("Final Course:",n)


# Nonlocal Nested 
def display():
    n='JFS'
    def update():
        nonlocal n
        n='PFS'
        print("Updated Course:",n)
    update()
    print("Final Course:",n)

display()

'''
# buitin fun- wherever you are declaring a variable using builtin fun names it acts as a variable it will loose its charcaterisitics
