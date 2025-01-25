# by harshit agrawal 2 

class hello:
    def __init__(self,a,b):
        self.color = a
        self.type= b
        print("constructed")

    def __del__(self):
        print("deconstructed")

a1= hello('a',"b")
print(a1.color)
print(a1.type)
a2= hello('c',"d")
print(a2.color)
print(a2.type)
