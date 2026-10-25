'.....String Methods....'
#These are built-in-methods
#Manipulating strings such as
#                             converting cases, 
#                             removing whitespaces,
#                             replacing characters,
#                             splitting, joining
#Example:
s="Hello World!"
print(s.upper())
print(s.lower())


#..Methods..
'''upper()
lower()
capitalize()
title()
strip()
lstrip()
rstrip()
startswith(prefix)
endswith(suffix)
replace(old,new)
split(seperator)
join(iterable)
find(substring)
rfind(substring)
index(substring)
rindex(substring)
count(substring)
isalnum()
isdigit()
islower()
isupper()
isspace()
isnumeric()
isdecimal()
startswith(prefix,start,end)
endswith(suffix,start,end)'''



str="Hello_world!" 
print(str.upper())
print(str.lower())
print(str.capitalize())
print(str.title())
print(str.strip())
print(str.lstrip())
print(str.rstrip())
print(str.startswith("Hello"))
print(str.endswith("world!"))
print(str.replace("world","friends"))
print(str.split("_"))
words=["hello","world"]
print(str.join(words))
print(str.find("llo"))
print(str.rfind("l"))
print(str.index("w"))
print(str.rindex("l"))
print(str.count("l"))
print(str.isalnum())
print(str.isdigit())
print(str.islower())
print(str.isupper())
print(str.isspace())
print(str.isnumeric())
print(str.isdecimal())
print(str.startswith("Hello",0))
print(str.endswith("world!",0))