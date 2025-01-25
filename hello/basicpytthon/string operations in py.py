# Strings are sequence of characters that are enclosed in "" (double quotes)or '' (single quotes) or """"""(triple quotes)

# concationation // + operator
str1= "hello"
str2 = "hai"
print(str1+str2)

# repetation // * operator 

str1= "hello"
repe =10
print(str1*10,end="#")

# strings methods
A= "Ishaan is a good boy"
# string.lower()
print(A.lower())
print(A.title())
print(A.upper())
print(A.capitalize())

print(A.replace("a",'n'))
# check the is alphbet 
print(A.isalpha())
print(A.isdigit())
print(A.isalnum())
print(A.isspace())

print(A.split())

# string formatting

name= "vidhaan"
length= len(name)*3
print("this is name as {} and length is {}".format(name,length))