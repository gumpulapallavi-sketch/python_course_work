#formvalidation :pattern matching
# valiadtion of fullname using regex 

import re
'''
fullname = input("enter your fullname: ")
pattern = r'^[A-Za-z]{2,25}( [A-Za-z]{2,25})+$'
res = re.fullmatch(pattern, fullname)
print("validation full name " if res else "invalid full name")


# validation of email using regex
email = input("enter your email: ")
pattern = r'^[a-zA-Z0-9._]+@[a-zA-Z0-9._]+\.[a-zA-Z]{2,}$'
res = re.fullmatch(pattern, email)
print("validation email " if res else "invalid email")

# validation of phone number using regex
phone = input("enter your phone number: ")
pattern = r'^(?:\+91|0)?[6-9][0-9]{9}$'
res = re.fullmatch(pattern, phone)
print("validation phone number " if res else "invalid phone number")

# validation of password using regex
password = input("enter your password: ")
pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$'
res = re.fullmatch(pattern, password)
print("validation password " if res else "invalid password")

# validation of username using regex
username = input("enter your username:")
pattern = r'^[a-zA-Z0-9_]{8,20}$'
res = re.fullmatch(pattern, username)
print("validation username " if res else "invalid username")

# validation of aadhar number using regex
aadhar = input("enter your aadhar number: ")
pattern = r'^\d{4}\s\d{4}\s\d{4}$'
res = re.fullmatch(pattern, aadhar)
print("validation aadhar number " if res else "invalid aadhar number")

'''
# validation of pan card number using regex
pan = input("enter your pan card number: ")
pattern = r'^[A-Z]{5}[0-9]{4}[A-z]$'
res = re.fullmatch(pattern, pan)
print("validation pan card number " if res else "invalid pan card number")