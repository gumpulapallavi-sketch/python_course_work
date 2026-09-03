# Lambda- we can create it using the lambda keyword
# It writtens the code in a single line
'''
# greatest of two numbers

greater= lambda a,b: a if a>b else b
print(greater(10,30))
print(greater(1,3))
print(greater(108,130))
print(greater(17,30))

# wishings

wish = lambda name: f'Welcolme to the course {name}'

print(wish("pallavi"))
print(wish("avi"))
print(wish("anvi"))
print(wish("anvitha"))

# Even or odd

iseven = lambda n: "Even" if n%2==0 else "odd"

print(iseven(49))
print(iseven(9))
print(iseven(20))
print(iseven(8))

# Average of two numbers

avg = lambda a,b,c: (a+b+c)/3

print(avg(10,3,6))
print(avg(1,9,6))
print(avg(4,5,6))
print(avg(16,19,30))

# Excating the domain
domain = lambda mail: (mail.split('@')[-1]).split('.')[0]

print(domain("pallavi@gmail.com"))
print(domain("avi@outlook.com"))
print(domain("pallavi@yahoo.com"))

# printing the price with the gst 

gst = lambda price: price + price*0.18

print(gst(1000))
print(gst(32000))
print(gst(100))
print(gst(7000))

# adding gst to the elements in the list

prices = [1038,3585,4930,3000,4859,28498,30000]

res=list(map(lambda price : price + price*0.18, prices))

print(res)

#Title of the elements in the list

names = ['pallavi','ammu','abhi','seetha','srinu','jaanu']

res = list(map(lambda name: name.title(),names))

print(res)

# set of elemnts into the list and calculating the price of elments adding 30%

prices = {1038,3585,4930,3000,4859,28498,30000}

res=set(map(lambda price : price + price*0.30, prices))

print(res)

#  elemnts into the list and calculating the price of elments with 30% discount
prices = [1038,3585,4930,3000,4859,28498,30000]

res=list(map(lambda price : price - price*0.3, prices))

print(res)

# price greaterthan 5000

prices = [3004,5840,5000,3793,5899,2000,2670,9000]

res=list(filter(lambda price: price>5000, prices))

print(res)

# printing the even prices of the list

prices = [3004,5840,5000,3793,5899,2000,2670,9000]

res=list(filter(lambda price: price%2==0, prices))

print(res)

# # printing the odd prices of the list

prices = [3004,5840,5000,3793,5899,2000,2670,9000]

res=list(filter(lambda price: price%2!==0, prices))

print(res)

# print the elements in the list where the length is greater than 5 
names = {'pallavi','ammu','avi','abhi','seetha','srinu'}
res=list(filter(lambda name: len(name)>5, names))
print(res)

# sum of elements in the e;lements

from functools import reduce

l= [48,39,40,56,29,32,20]
res = reduce(lambda sum,i:sum+i,l)
print(res)

# reducing the elements in the list

from functools import reduce

names= ['pallavi','ammu','avi','abhi','seetha','srinu']    # reduce is going to remove the spaces and add the elements from the list as a single element
res = reduce(lambda res,i: res+''+i,names)
print(res)

# printing the elements in the asending order and decending order using keys and values

products={'sugar':40,'salt':30,'eggs':10,'oil':100,'bread':40}
print(dict(sorted(products.items())))
print(dict(sorted(products.items(),reverse=True)))

print(dict(sorted(products.items(),key=lambda i:i[1])))
print(dict(sorted(products.items(),key=lambda i:i[1],reverse=True)))
'''
