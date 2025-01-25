# by harshit Agrawal 2 
# using class and object to print rreport
class student:
    def __init__(self,name,usn):# init function in clas students
        """defining attributes"""
        self.name= name   
        self.usn = usn
        self.per =0
a1=0
while True:
    print("______________________________________")
    print(f"_________(STUDENT {a1+1})__________________")

    a= input("Enter your name :")
    b= input("Enter your usn ::")
    p= student(a,b)
    sum=0
    for i in range(3):
        c= int(input(f"Enter the marks in sub {i+1} :: "))
        sum +=c
    p.per= sum/3
    if p.per<=33:
        e= "Fail"
    else:
        e= "pass"
    print(F"""
_________________________________
          YOUR REPORT
_________________________________
    Name : {a}
    USN : {b}
_________________________________
    percentage obtained :: {p.per}%
    Status : {e}
""")