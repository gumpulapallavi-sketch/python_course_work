#range()- to generate the numeric values in the given range.
# forloop- to iterate the values in the given range.
'''
s= 'Python Programming'
for i in range(len(s)): # whenever we want index values of the string we use range(len(string))
    if s[i]in 'aeiouAEIOU':
        print(i,s[i])
        '''

'''
l=[10,2,30,50,47,53,59,78,90,7,79]
sum=0
for i in range(len(l)):
    if l[i]%2==0:
        sum=sum+i
        print(i,l[i])
print(sum)
'''
#tuple are immutable data type.we can not modify the values in the tuple.we can not add or remove the values in the tuples.
# range() can be used for list and tuple but not for set and dict becaue set and dict are unordered collection of unique elements and the elements in them are not in sequnce

'''
n=int(input("Enter the number:"))
fact=1
for i in range(1,n+1):
    fact *= i
print(f" Factorial of {n} is {fact}")
'''

# dict()

'''
data={}
n = int(input("Enter the no of students:"))
max_marks=0
for i in range(n):
    name=input("Enter the name:")
    marks=input("Enter the no of marks:")
    if marks > max_marks:
        max_marks= marks
    data[name] = marks
print(data)
print("maxmimun marks: ",max_marks)
'''

products={}
n= int(input("Enter the no of products:"))
total_bill=0
for i in range(n):
    product=input(f"Product - {i}: ")
    price=float(input(f"price - {i}: "))
    quantity=int(input(f"quantity - {i}: "))
    final_price = price*quantity
    total_bill += final_price
    products[product] = f'{price} *{quantity} = {final_price}'
print(products)
print("Total Bill:",total_bill)

                       





