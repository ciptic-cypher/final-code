import re
# import regular expression

# match function (pattern , string)
if re.match("apple","apple",flags=0):
    print("True")
else :
    print("False")
#find all prints all the occurence of the patter in the string
    #  find all (string, pattern)
print(re.findall("he","hellohelloehe"))

# search function(pattern, string, flag)
pattern= "apples"
if re.search(pattern, "appleball", flags=1):
    print("True ")
else:
    print("False")


# using subs(pattern, replacement string, string , count , flag )
string = "This is a dog !"
pattern = "dog"
print(re.sub(pattern , "cat", string, count=0, flags=0))