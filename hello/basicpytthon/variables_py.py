# variableas are memory locations reserve to store values 

a=10 # assignment of vairble or variable declarations

del a # deleting a variable

try:
    print(a)
except Exception as e:
    print("variable a donot exists")

# variable increment / decrement or multiplication/ Division

a= 10 
list1 = range(10)
t1= list(map(lambda a: a+1 , list1))
print(t1)

t= list(map(lambda a: a-1 , list1))
print(t)


t= list(map(lambda a: a*a , list1))
print(t)


t= list(map(lambda a: a/a, t1))
print(t)