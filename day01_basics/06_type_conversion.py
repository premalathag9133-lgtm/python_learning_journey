#.......Type conversion..........
#Two types of type conversions are: Implicit TC and Explicit TC
#Implicit: pyhton automatically converts one data type to another data type
#Explicit: User convert the data type of an object to required datatype
#short & char-->int-->unsigned int-->long int-->unsigned long int-->float-->double-->long double

#Implicit Type conversion
#int-float
a=2
b=3.5
c=a+b
print(c)
print(type(c))

#int - complex
d=2
e=2j
f=d+e
print(f)
print(type(f))

#float - complex
a=2.5
b=3j
c=a+b
print(c)
print(type(c))

#bool - int
a=True
b=3
c=a+b
print(c)
print(type(c))

#Explicit Type conversion
a="1"
a=int(a)
print(a)
print(type(a))

a=1
a=float(a)
print(a)
print(type(a))

a="600"
a=int(a)
print(a)
print(type(a))

a=True
a=int(a)
print(a)
print(type(a))

a='A'           #ord() used to find ASCII value of a number
b=ord(a)
print(f"ASCII value of A is {b}")

a=65           #chr() used to find ASCII value's letter
b=chr(a)
print(b)