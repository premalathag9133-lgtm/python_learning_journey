'''........input() function......'''
#The input() function is used to take input form the user through the keyboard.
#Default input taken as string.
#Syntax:
#    variable=input("Message")

#Taking input as string(default)
name=input("Enter name:")
print(name)

#Taking input as int
age=int(input("enter age:"))
print(age)

#Taking input as float
CGPA=float(input("enter CGPA:"))
print(CGPA)

#Taking input as list
nums=list(input("enter numbers:"))
print(nums)

#Taking input as tuple
t=tuple(input("enter numbers:"))
print(t)

#Taking input as dictionary
std=dict(input("enter name and id:").split())
print(std)

#Taking input as range
r=range(int(input("enter range:")))
print(r)

#Taking input as set
num=set(input("enter nums:").split())
print(num)

#Taking input as boolean
a=bool(input("enter true or false:"))
print(a)