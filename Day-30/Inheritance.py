#Inheritance: acquring properties from parent class to the child class
# 5 types: 1. single , 2. multiple 3. multi-level , 4. hierarchy ,5. hybrid

class WhatsappsV1:
    def __init__(self,name):
        self.name = name
        print(f"Welcome to the whatsapp - v1 {self.name}!")
    def messaging(self):
        print("You can send messages")

class WhatsappsV2(WhatsappsV1):
    def __init__(self, name):
        self.name = name
        print(f"Welcome to the whatsapp - v2 {self.name}!")
    def calls(self):
        print("You can audio and video calls")

pallavi = WhatsappsV1('pallavi')
pallavi.messaging()

deepu = WhatsappsV2('deepu')
deepu.messaging()
deepu.calls()
        