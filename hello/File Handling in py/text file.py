# by harshit Agrawal 2 

# creating a python file 

a= input("Enter the content of file \\n for new line:").split("\\n")
print(a)
for i in a :
    with open('math.txt','a') as f:
        f.write(i)
# opening a python file

# method 1 
file1= open('math.txt','r')
file1.close()

# method 2
with open('math.txt','r') as f:
    None


