class vegetable:
    def __init__(self,beans , carrot):
        self.beans = beans
        self.carrot=  carrot
    def __add__(self,other):
        self.beans=self.beans+other.beans
        self.carrot=self.carrot + other.carrot
        return vegetable(self.beans,self.carrot)
    def __del__(self):
        print("deconstructed!")
a= vegetable(2,3)
b= vegetable(3,2)
c= a + b
print(f"{c.carrot,c.beans}")