#string
"""pharse="hii how are you today"
print(pharse.lower().islower())
print(len(pharse))
print(pharse.index("you"))
print(pharse.replace("you"," me"))
"""
"""
#numbers
from math import *
num=12
print(num)
print(45.54)
print(9%2)
a=input("enter the first Number")
b=input("enter the Second Number")
c=input("enter the third Number")
print("Maximum NUmber is"+max(a, b, c))
print (min(-43,54,5,34,34,35,343,43))
print(floor(56.3))
print(sqrt(78))
"""
#project
"""
num1=int(input("Enter first num"))
operator=input("enter operator as +,-,*,/")
num2=int(input("Enter Second num"))
sum=num1+num2
sub=num1-num2
mul=num1*num2
div=num1/num2
if operator==+:
    print(sum)
elif operator == -:
    print(sub)
    """
    #list
"""
friends=["rohan","jayant","dheeraj","aman",34,45,45]
print(friends[2][1])
print(friends[1:3])
print(friends[-2])
friends[2]="modi"
print((friends))
"""
"""
#lucky numbers
lucky_numbers=[1,2,3,4,5,3,6]
friends=["rohan","jayant","dheeraj","aman"]
friends.extend(lucky_numbers)


friends.append("object")
friends.insert(2,"object")
friends.remove("object")
friends.pop()
print(friends) """
"""
#user input in list
#first creat empty list
list=[]
#number of elements as input
l=int(input("enter all the numbers to compare"))
#itterating till the range
for i in range(0,l):
    ele=int(input())

    list.append(ele)
print(max(list))
"""
"""
#tuples cant modify change fix only a time
# it is uses with timestamp that is stored in tuple
cordens=(34,54,43)

list=[(34,3),(43,54),(54,66)]
print(list)
print(cordens) 
"""
#Functions
num=int(input("Enter number to find cuberoot"))
def cube(num):
    cuberoot=num*num*num
    return cuberoot
print(cube(num))

