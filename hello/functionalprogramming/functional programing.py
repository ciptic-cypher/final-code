# here we talk about python as function programming

#  a function is a python object which contains blocks of code and perfrm a specifc task . 

# A function include 
# function header(parameters):
# ----indent---- // function body
#-----indent---- // return value    
# call the function


# code to use a functions

def add(i,j):
    return i+j

def call(i,j):
    return add(i,j)

def pas(i,j,fn):
    return fn(i,j)

res = pas(2,3,call) #passin a function as an object this is why python supports functional programming
print(res)