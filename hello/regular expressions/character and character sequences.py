# by harshit Agrawal 2 

import re
string = "This is a 56 dog"
'''
summary
^start
$end
. any char
\d prints all digits
\D prints all non digits
\s prints all the whitspace
\S prints all non whitespace

'''
# use of ^ sequence 
pattern= "^T" # starting with T which is True
print(re.findall(pattern,string)) # returns a list with one element

pattern= "^H" # starting with H which is False
print(re.findall(pattern,string)) # returns a list with no elements 

# use of $ sequence 
pattern = "g$" # ending with g which is True 
print(re.findall(pattern,string)) # returns a list with an element 

pattern = "$h" # ending with h which is False 
print(re.findall(pattern,string)) # returns a list with no element 

# use of . sequence 
pattern= "." #prints all the charcater coupling 1 adjacent characters
print(re.findall(pattern,string)) #it prints all the characters

# use of . sequence 
pattern= ".." #prints all the charcater coupling 2 adjacent characters
print(re.findall(pattern,string)) #it prints all the characters


# use of . sequence 
pattern= "^.." #prints all the charcater coupling 2 adjacent characters  from the begining
print(re.findall(pattern,string)) #it prints all the characters from the beginning



# use of . sequence 
pattern= "...$" #prints all the charcater coupling 3 adjacent characters  from the end
print(re.findall(pattern,string)) #it prints 3 characters from the end

# use of \d sequence 
pattern= "\d" #prints all the charcater coupling 2 adjacent characters  from the start of first digit
print(re.findall(pattern,string)) #it prints all the characters from the beginning



# use of \d sequence 
pattern= "\d." #prints all the charcater coupling 2 adjacent characters  from the start of first digit
print(re.findall(pattern,string)) #it prints all the characters from the beginning

# use of \D
pattern= "\D" #prints all the charcater coupling 2 adjacent characters  from the start of first digit
print(re.findall(pattern,string)) #it prints all the characters from the beginning

# use of \s
pattern= "\s" #prints all the charcater coupling 2 adjacent characters  from the start of first digit
print(re.findall(pattern,string)) #it prints all the characters from the beginning


# use of \S
pattern= "\S" #prints all the charcater coupling 2 adjacent characters  from the start of first digit
print(re.findall(pattern,string)) #it prints all the characters from the beginning

# iuse of *
pattern = "is*"
print(re.findall(pattern,string)) #it prints all the characters from the beginning

# iuse of F
pattern = "^T.*"
print(re.findall(pattern,string)) #it prints all the characters from the beginning

# iuse of ?
pattern = "^T.*?"
print(re.findall(pattern,string)) #it prints all the characters from the beginning

# iuse of ?
pattern = "^T.+?"
print(re.findall(pattern,string)) #it prints all the characters from the beginning


# iuse of ?
pattern = "^T.+?"
print(re.findall(pattern,string)) #it prints all the characters from the beginning