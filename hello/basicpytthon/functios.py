import sys
sys.setrecursionlimit(3000)
#  functions are the block of code where a particular task is executed 

# def function name(parameters):
#                function code 

# function call()

# eg
def sample_func():
    print("hello world")

sample_func()

# recursion

def fact(n):
    print(n)
    fact(n-1)

fact(2000)