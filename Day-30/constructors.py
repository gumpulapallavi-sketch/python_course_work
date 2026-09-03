'''
class flipkart:
    products={"Shirts":1000,"Handbag":2000,"Pants":3000}
    discount = 30

    @classmethod
    def display(cls): 
        print(cls.products)


    def userinfo(self,name,phone,address):
        self.name = name
        self.phone = phone
        self.address = address
        print(f"Hello {self.name}, Welcome to flipkart")

    @staticmethod
    def displaydiscount():
        print(f"{flipkart.discount}% discount is going on, grab the product....")

Pallavi = flipkart()
Pallavi.userinfo("Pallavi",976845320,"TG")
Pallavi.displaydiscount()
Pallavi.display()
print(Pallavi.products)
print(Pallavi.name)

class Flipkart:
    def __init__(self,name,phone):
        self.name = name
        self.phone = phone
        print(f"Hello {self.name}, Welcome to the flipkart")

pallavi = Flipkart('pallavi',6305585899)
deepu = Flipkart('Deepu',8653992662)
naimisha = Flipkart('naimisha',9375829064)

class Instagram:
    def __init__(self,username,password,posts):
        self.username = username
        self.__password = password
        self._posts = []

    def getpassword(self):
        return self.__password

    @property
    def accesspost(self):
        return self._posts

    def display(self):
        print(self.username,self.__password,self._posts)


pallavi = Instagram('pallavi','pallavi@0809')
pallavi.display()
print(pallavi.username)
print(pallavi.getpassword())
print(pallavi.accesspost)
'''
class Instagram:
    #variable are decalred isndie the function
    def __init__(self,username,password,post):
        self.username = username
        self.__passowrd= password #private
        self._post= [] #protected--->getter,setter


#getpassword or xyz --->is just a word 
    def getpassword(self):
        return self.__passowrd

    def setpassword(self,newpassword):
        self.__passowrd = newpassword
    

    @property
    def accesspost(self):
        return self._post

    @accesspost.setter
    def accesspost(self,newpost):
        self._post.append(newpost)


    
    def display(self):
        print(self.username,self.__passowrd,self._post)


#object create chesukuntunam
pallavi = Instagram('naimisha','naimisha@123',2)
pallavi.display() #object.display()
print(pallavi.username)
print(pallavi.getpassword())
print(pallavi.accesspost)

