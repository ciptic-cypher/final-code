# lambda is an  anonymous function which donot have a name
#  the syntax of lambda function is 
# lambda arguments : expressions

# eg
# similar to the code 
def add(a,b):
    return a+b

print(add(1,4))

# by using lambda function
r=lambda a,b: a+b
print(r(1,4))
#  outuput of both are same