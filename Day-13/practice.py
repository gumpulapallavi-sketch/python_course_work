# 1 Positive or Negative
'''
n= int(input("Enter the number:"))
if n>0:
    print("positive")
else:
    print("negitive")
    '''

# 2. Even or Odd
'''
n = int(input(" Enter the number:"))
if n%2==0:
    print("Even")
else:
    print("Odd")
    '''

# 3. Divisible by 5
'''
n = int(input(" Enter the number:"))
if n%5==0:
    print("Divisible by 5")
    '''

# 4. Divisible by 3 and 7
'''
n = int(input(" Enter the number:"))
if n%3==0 and n%7==0:
    print("Divisible by both 3 and 7 ")
    '''

# 5. Check for Leap Year

'''
n = int(input(" Enter the number:"))
if n%4==0:
    print("Leap year")
    '''

# 6. Check Pass or Fail (Passing marks = 35)

'''
n = int(input(" Enter the number:"))
if n>=35:
    print("pass")
else:
    print("Fail")
    '''
# 7. Check if number is 3-digit
'''
n = int(input(" Enter the number:"))
if n>=100 and n<=999:
    print("3-digit number")
    '''

# 8. Check if character is vowel

'''
n = input(" Enter the alphabet:")
if n in 'aeiouAEIOU':
    print("vowel")
    '''

# 9. Check greatest of two numbers

# Input two numbers
'''
# Program to find the greatest of two numbers

# Input two numbers
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# Compare the numbers
if num1 > num2:
    print(f"{num1} is greater than {num2}")
elif num2 > num1:
    print(f"{num2} is greater than {num1}")
else:
    print("Both numbers are equal")

    '''

# 10. Check smallest of two numbers

# Program to find the greatest of two numbers

'''
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# Compare the numbers
if num1 < num2:
    print(f"{num1} is smaller than {num2}")
elif num2 < num1:
    print(f"{num2} is smaller than {num1}")
else:
    print("Both numbers are equal")
    '''


# 11. Check if number is zero
'''
n = int(input(" Enter the number:"))
if n==0:
    print("Number is Zero")
    '''
#12. Check if number is multiple of 10

'''
n = int(input(" Enter the number:"))
if n%10==0:
    print("Divisible by 10")
    '''

#13. Check if age is eligible to vote (18+)
'''
n = int(input(" Enter the age:"))
if n>=18:
    print("Eligible to vote")
    '''
#14. Check if number is between 1 and 100

'''
n = int(input(" Enter the number:"))
if 1<=n<=100:
    print("In Range ")
    '''
# 15. Check if number is square of another

# 16. Check if two strings are equal

'''
n = input(" Enter the string: ")
m = input(" Enter the string: ")
if n==m:
    print("Strings are equal ")
    '''
# 18. Check if number is positive and even

'''
n = int(input(" Enter the number:"))
if n>=1 and n%2==0:
    print("Positive and even number")
    '''

#19. Check if character is uppercase

'''
n = input(" Enter the string: ")
if n.isupper():
    print("Uppercase letter")
    '''
#20. Check if temperature is hot (>30°C)

'''
n = int(input(" Enter the number:"))
if n>30:
    print("It's hot")
    '''

#1. Check if a number is a 4-digit even number

'''
n = int(input(" Enter the number:"))
if 1000<=n<=999 and n%2==0:
   print(f"{num} is a 4-digit even number")
   '''

#2. Check if a character is a consonant

'''
 n = input(" Enter the alphabet:")
if n not in 'aeiouAEIOU':
    print("consonant")
    '''

# 3. Check if a number is divisible by 2 or 3 but not both

'''
n = int(input(" Enter the number:"))
if n%2==0 and n%3==0:
    print("Divisible by both 2 and 3")
elif n%2==0:
    print("Divisible by 2 only")
elif n%3==0:
    print("Divisible by 3 only")   
else:
    print("Not divisible by 2 and 3 ")
    '''

# 4. Check if a number is negative and odd

'''
n = int(input(" Enter the number:"))
if n<0 and n%2!=0:
    print("Negative and odd number ")
    '''

# 5. Check if a string starts with a vowel

'''
text= input("Enter the string: ")
if text[0].lower() in 'aeiouAEIOU':
    print("Starts with a vowel ")
    '''

# 6. Check if three sides form a valid triangle
'''
a = int(input(" Enter the first number:"))
b = int(input(" Enter the second number:"))
c = int(input(" Enter the third number:"))
if a+b>c and a+c>b and b+c>a:
    print("Valid triangle ")
    '''

#  7. Find the greatest among three numbers

'''
a = int(input(" Enter the first number:"))
b = int(input(" Enter the second number:"))
c = int(input(" Enter the third number:"))
if a>b and a>c:
    print("a is greatest")
elif b>a and b>c:
    print("b is greatest")
else:
    print("c is greatest")
    '''

# 8. Check if a year is a century year and leap year

'''
n = int(input(" Enter the number:"))
if n%100==0 and n%4==0:
    print("Century leap year")
    '''

# 9. Check if a character is a digit

'''
ch = input("Enter the character: ")
if ch.isdigit():
    print("Digit")
    '''

#10. Check if a number is palindrome (integer)

'''
n = int(input(" Enter the number:"))
n_str= str(n) # convert num to string
if n_str == n_str[::-1]:
    print("number is a palindrome")
    '''


# 11. Compare lengths of two strings

'''
text1 = input("Enter the first string : ")
text2 = input("Enter the first string : ")
if len(text1)>len(text2):
    print("First string is longer")
elif len(text2)>len(text1):
      print("second string is longer")
else:
     print("both are equal")
     '''

# 12. Check if a number is within a specific range (50 to 100) and divisible by 5

'''
n = int(input(" Enter the number:"))
if n in range(50,101) and n%5==0:
    print("In range and divisible by 5")
    '''

# 13. Validate if a password length is strong (8 or more characters)

'''
import string

# Input a password
password = input("Enter your password: ")

# Conditions
length_ok = len(password) >= 8
has_upper = any(ch.isupper() for ch in password)
has_digit = any(ch.isdigit() for ch in password)
has_special = any(ch in string.punctuation for ch in password)

# Check strength
if length_ok and has_upper and has_digit and has_special:
    print("Password is strong ")
else:
    print("Password is weak ")
    print("Requirements:")
    if not length_ok:
        print("- At least 8 characters")
    if not has_upper:
        print("- At least one uppercase letter")
    if not has_digit:
        print("- At least one digit")
    if not has_special:
        print("- At least one special character")
'''

# 14. Check if sum of two numbers is even

'''
a = int(input(" Enter the first number:"))
b = int(input(" Enter the second number:"))
total=a+b
if total%2==0:
    print("Sum is even")
else:
    print("Sum is not even")
'''

# 15. Check if the character is a special symbol (!, @, #, etc.)

'''
import string
ch = input("Enter the character:'@' ")
for ch in string.punctuation:
    print("Special Character")
'''

# 16. Check if temperature is cold (<15°C), moderate (15–30°C), or hot (>30°C)

'''
# Input temperature in °C
temp = float(input("Enter the temperature in °C: "))

# Check ranges
if temp < 15:
    print("Temperature is Cold ")
elif 15 <= temp <= 30:
    print("Temperature is Moderate ")
else:
    print("Temperature is Hot ")
    '''

#17. Check if a number lies outside the range 10 to 50

'''
num = int(input(" Enter the number:"))
if num >10 and num < 50:
    print("In Range ")
else:
    print("Outside the range")
'''

# 18. Check if number is a perfect square (basic method)

'''
import math
num = int(input(" Enter the number:"))
root = int(math.sqrt(num))
if root * root == num:
    print("number is a perfect square")
else:
    print("number is not a perfect square")
    '''


# 19. Compare two ages and determine who is older or if same age
'''
a = int(input(" Enter the age:"))
b = int(input(" Enter the second age:"))
if a>b:
    print("a is older")
elif b>a:
    print(" b is older")
else:
    print("Both are same age")
'''

# 20. Check if an angle is acute, right, or obtuse

'''
n = int(input(" Enter the angle:"))
if n<90:
    print("Angle is acute")
elif n==90:
    print("Angle is Right")
else:
    print("Angle is obtuse")
'''






    
























































