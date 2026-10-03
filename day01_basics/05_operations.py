'''.......Python Operations.......'''
#Arithmetic Operators    (+,-,*,/,//,%,**)
#Assignment Operators    (=,+=,-=,*=,/=,//=,%=,**=)
#Comparision Operators   (==,!=,>,<,>=,<=)
#Logical Operators       (and,or,not)
#Membership Operators    (in, not in)
#Identity Operators      (is, is not)
#Bitwise Operators       (&,|,^,~,<<,>>)

a=6
b=2
c=3
#Arithmetic Operators    (+,-,*,/,//,%,**)
print(a+b)
print(a-b)
print(a*b)
print(a/c)
print(a//c)
print(a%c)
print(a**b)

#Assignment Operators    (=,+=,-=,*=,/=,//=,%=,**=)
a=6
a+=4
print(a)
a=6
a-=2
print(a)
a=6
a*=2
print(a)
a=6
a/=2
print(a)
a=6
a//=4
print(a)
a=6
a%=4
print(a)
a=6
a**=2
print(a)

#Comparision Operators   (==,!=,>,<,>=,<=)
a=6
b=2
print(a==b)
print(a!=b)
print(a>b)
print(a<b)
print(a>=b)
print(a<=b)

#Logical Operators       (and,or,not)
a=0
b=3
print(a and b)
print(a or b)
print(not a)

#Membership Operators    (in, not in)
name="python"
print("p" in name)
print("p" not in name)

#Identity Operators      (is, is not)
a=10
b=10
c=5
print(a is b)
print(a is c)
print(a is not b)
print(a is not c)

#Bitwise Operators       (&,|,^,~,<<,>>)
a=1
b=3
print(a&b)
print(a|b)
print(a^b)
print(~a)
print(a<<1)
print(a>>1)