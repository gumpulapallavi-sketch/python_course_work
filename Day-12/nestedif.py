'''
fa= eval(input("Follows Account: "))
cf= eval(input("Close Friend: "))
if fa:
    if cf:
        print("story visible")
    else:
        print("not in close friends list")
else:
    print("Follow the Account First")
    '''


'''
reg= eval(input("Registered the BGMI: "))
ef= eval(input("Entry fee: "))
if reg:
    if ef:
        print("Tournament Entry Confirmed")
    else:
        print("Entry Fee Pending")
else:
    print("Registration Required")
    '''

acc= eval(input("link is Active: "))

if acc:
    per=eval(input("permission Granted: "))
    if per:
        print("File opened successfully ")
    else:
        print("Access Denied ")
else:
    print("Invalid File Link ")

