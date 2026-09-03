'''
#File Operations:
open(),read(),close()
file = open('pfs-63.txt','r')
print(file.read())
file.seek(0)
print(file.readline())
file.seek(0)
print(file.readlines())
file.close()

with open('pfs-63.txt','r') as file:
    print(file.read())
    file.seek(0)
    print(file.readline())
    file.seek(0)
    print(file.readlines())
    
#write mode is used to create the file and also to overwrite the existing file

with open('pfs-63.txt','w') as file:
    file.write("Shifted to Branch-1")
    
# append mode
with open('pfs-63.txt','w') as file:
    file.write("Shifted to Branch-1")

#a+:read and append
with open('pfs-63.txt','a+') as file:
    file.write("tomorrow same branch 5")
    file.seek(0)
    print(file.read())
    '''



  