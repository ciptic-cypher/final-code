# iterator gives one by one value of a list 

# eq
a= list(range(11))
print("Let the list be {}".format(a))
iteration= iter(a)
print("The first element of list is {}".format(iteration.__next__()))
print("The second element of list is {}".format(iteration.__next__()))
print("The third element of list is {}".format(iteration.__next__()))
print("The forth element of the list is ", next(iteration))


#similariry generator is used to get multiple output from a functiom

def squares():
    n=1
    while n<5:
        yield n**2
        n+=1
    
values= list(squares())
print(values)