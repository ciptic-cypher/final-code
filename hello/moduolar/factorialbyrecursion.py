# factorial of a number 


def fact1(n,a=1):
    print(n)
    if n==1:
        return a
    else:
        a=a*n
        fact1(n-1,a)
result= fact1(5)
print("The factorial of 5 is :",result)