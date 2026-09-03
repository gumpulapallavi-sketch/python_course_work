#forwithelse: when their break statement inside the for loop then else will never execute . whenever their is no break statement then else will execute
'''
for i in range(1,10):
    if i==15:
        break
    print(i)
else:
    print("End of the loop")  
    '''

'''
for i in range(1,10):
    print(i)
else:
    print("End of the loop")
    '''  

'''
pin = 9866    #phone pin 
for i in range(5):
    epin = int(input("Enter the pin: "))
    if pin ==epin:
        print("Unlock Phone")
        break
    else:
        print("Invalid Pin ")
else:
    print("Try after 30 seconds ")
    '''

'''
# Factors of a number
n = int(input("Enter the number: "))
print("Factors : ",end=' ')
for i in range(1,n+1):
    if n%i==0:
        print(i,end=' ')
        '''

# prime number
'''
n = int(input("Enter the number: "))
c=0
for i in range(1,n+1):
    if n%i==0:
        c+=1

if c==2:
    print("Prime number")
else:
    print("Not a prime number")
    '''

# Prime numbers using break statement.(code optimization)

'''
n = int(input("Enter the number: "))
for i in range(2,n//2+1):
    if n%i==0:
        print("Not a Prime Number")
        break
else:
    print("Prime Number")
    '''
    