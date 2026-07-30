#Day 2 

#Variables
name="Kashyap"
age=21
print(name)
print(age)


#Data types
#int
num=100
print(type(num))

#Float
price=99.99
print(type(price))

#String
s="Python"
print(type(s))

#Boolean
b=True
print(type(b))

#list
fruits=["Apple","Banana","Mango"]
print(fruits)

#Tuple
colors=("Red","Green","Blue")
print(colors)

#set
numbers={1,2,3,4}
print(numbers)

#dictionary
student={
    "name":"Kashyap",
    "age":21
}


#Operators
#Arithmetic Operators
a=20
b=10
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b)
print(a//b)
print(a**b)

#comparison operators
c=10
d=20
print(c==d)
print(c!=d)
print(c>d)
print(c<d)
print(c>=d)
print(c<=d)

#Logical operators
x=True
y=False
print(x and y)
print(x or y)
print(not x)

#Assignment operators
e=10
e+=5
print(e)
e-=3
print(e)
e*=2
print(e)


#Loops
#For loop
for i in range(1,6):
    print(i)

#While loop
count=1
while count<=5:
    print(count)
    count+=1


#Functions
def greet():
    print("Hello Python")
greet()


#simple programs
#Number even or odd
num=18
if num%2==0:
    print("Even")
else:
    print("Odd")
    