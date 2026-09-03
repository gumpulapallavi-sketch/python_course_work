'''
n = int(input("Enter the value: "))
senior=input("Enter the value: ").lower()=="True"
if 0<=n<=100:
    print(n*1.5)
elif 101<=n<=200:
    print(n*2.5)
elif 201<=n<=500:
    print(n*4)
elif 501<=n<=800:
    print(n*6)
else:
    print(n*6*1.05)
if senior:
    n *=0.9

#booking seats

seat_type=input("Enter the set type")
booking_days=int(input())
festival=input()=="True"
age=int(input())
price=5000
if seat_type=="Business":
    price+=price*0.4
elif seat_type=="Premium Economy":
    price+=price*0.2
if booking_days>30:
    price-=price*0.1
elif booking_days<7:
    price+=price*0.25
if festival:
    price+=price*0.20
if age>=60:
    price-=price*0.15
print(price)


#Insurance Premium.
age=int(input())
health_score=int(input())
vehicle_type=input()
price=10000
if age<=25:
    price+=price*0.20
elif age>50:
    price+=price*0.15
if health_score>=80:
    price-=price*0.10
elif health_score<60:
    price+=price*0.20
if vehicle_type=="sports":
    price+=price*0.30
elif vehicle_type=="SUV":
    price+=price*0.15
print(price)

#1.To print the table of a number
n=int(input("enter a number:"))
for i in range(1,11):
    print(f"{n} * {i} = {n*i}")


n=int(input("enter a number:2"))
for i in range(1,11):
    print(f"{n} * {i} = {n*i}")


#2. Reverse a Number – ATM Security Verification
n=int(input("enter a number:"))
reverse=0
while n>0:
    digit=n%10
    reverse=reverse*10+digit
    n=n//10
print("Reverse of the number is:", reverse)


#3.To print the sum of n*i in a single line
n=int(input("enter a number:"))
total = sum(n * i for i in range(1, 11))
print(f"Sum of n*i is: {total}")


#4. Prime Numbers from 1 to 100 – Security Number Checker 
for num in range(1, 101):
    if num>1:
        for i in range(2, num):
            if (num %i==0):
                break
        else:
            print(num)
'''

#5.Program to count vowels and consonants
text = input("Enter a string: ")
vowels = 0
consonants = 0
for char in text:
    if char.isalpha():
        
        if char.lower() in ['a', 'e', 'i', 'o', 'u']:
            vowels += 1
        else:
            consonants += 1


print("Vowels:", vowels)
print("Consonants:", consonants)