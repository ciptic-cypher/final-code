# by harshit agrawal 2 
import sys
sys.setrecursionlimit(2000)
n=0
def python():
    print("Hello world")
    global n
    n=n+1
    print(n)
    python()

python()