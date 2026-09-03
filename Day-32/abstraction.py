#Abstraction means hiding the internal implementation details of a class and exposing only the essential features to the user.
from abc import ABC,abstractmethod 

class Phonepay:
    def senderinfo(self):
        print("You can their mobile number or scanner")
    def amount(self):
        print("You can enter amount")
    def pin(self):
        print("You need enter the pin")

    @abstractmethod
    def transaction(self):
        pass


class HDFC(Phonepay):
    def transaction(self):
        print("Payment using hdfc bank")

class SBI(Phonepay):
    def transaction(self):
        print("Payment using sbi bank")

class BOB(Phonepay):
    def transaction(self):
        print("Payment using bob bank")

class UNION(Phonepay):
    def transaction(self):
        print("Payment using union bank")

class ICIC(Phonepay):
    def transaction(self):
        print("Payment using icic bank")

pallavi = HDFC()
pallavi.senderinfo()
pallavi.amount()
pallavi.pin()
pallavi.transaction()

Deepu = SBI()
Deepu.senderinfo()
Deepu.amount()
Deepu.pin()
Deepu.transaction()

Naimisha= BOB()
Naimisha.senderinfo()
Naimisha.amount()
Naimisha.pin()
Naimisha.transaction()

Seetha= UNION()
Seetha.senderinfo()
Seetha.amount()
Seetha.pin()
Seetha.transaction()

Sri= ICIC()
Sri.senderinfo()
Sri.amount()
Sri.pin()
Sri.transaction()










