'''
username = input("username:")
password = input("password:")
if username=="admin" and password=="admin123":
    print("login successful")
else:
    print("Invalid credentials")
    '''
'''
product = ['Laptop','Mobile','watch']
search = input("search product:")
if search in product:
    print("product found")
else:
    print("product not found")
    '''

bill = int(input("Enter the bill: "))
if bill>90:
    print(bill)
else:
    print(bill+30)

