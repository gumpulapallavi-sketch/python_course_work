#str list tuple dict set range()
'''
for var in seq:
print(var)
'''
'''
s= ' codegnan '
for ch in s:
    print(ch)
    '''

'''
s= ' codegnan '
for ch in s:
    if ch in 'aeiouAEIOU':
       print(ch)
       '''

'''
l=[10,1,3,20,30,6,49,67,40]
for i in l:
    if i%2==0:
        print(i,"Even")
    else:
        print(i,"odd")
        '''

'''
marks= (10,30,4,57,89,35,26,90,100)
for mark in marks:
    if mark>=35:
        print(mark,"Pass")
    else:
        print(mark,"Fail")
        '''
'''
followers={'pallavi','seetha','srinu','priya'}
for i in followers:
    print(i) #set is unordered collection of unique elements.It does not support indexing and slicing. It is mutable but the elements in it must be immutable.
'''
'''
bus= {'s1':'Booked','s2':'Available','s3':'Booked','s4':'Available','s5':'Booked'}
for seat in bus:
    if bus.get(seat)=='Available':
          print(seat,bus.get(seat))
          '''

'''
bus= {'s1':'Booked','s2':'Available','s3':'Booked','s4':'Available','s5':'Booked'}
for seat in bus:
    if bus.get(seat)!='Available':
          print(seat,bus.get(seat))
          '''
#range(start,end+1,step) => (0,nodef,1)

'''
for i in range(1,11):
    print(i)
    '''

'''
for i in range(2,51,2):
    print(i,end=' ')
    '''

'''
for i in range(1,100,2):
    print(i,end=' ')
    '''

'''
for i in range(5,51,5):
    print(i,end='')
    '''
'''
n=int(input("Enter the Table No:"))
for i in range(1,11):
    print(f'{n}*{i}={n*i}')
    '''


    



