# filter is used to itterate a function for all the elements present in a list/set

# syntax of filter is 
# a= eval(filter(function,iterator))

# eg 
number = [1,2,3,4,5,6,7]

a= list(filter(lambda a : a%2==0 ,number))
print(a)

#  map is same as the filter but it returns the vale of the expression in the code 
a= list(map(lambda a : a**2, number ))
print(a)