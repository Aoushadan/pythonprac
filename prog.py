
x=10
print(x);
a=20.3
b="hello"
print(a,b)
print(b)
x="world"
print(x)
c="Hi"
def func():
    c="bye"
    print(c)
func()    
print(c)
r=54.7
print(type(r))
v=2>6
print(type(v))
print(v)
x="hello"
print(x)
print(type(x))
s=10+11j
print(type(s))
#if statement
x=4
if(x%2==0):4566
    print("x is divisible by 2")
else:
    print("x is not divisible by 2")    

           
x=int(input("ENTER THE NUMBER:"))
if(x%3==0):
    print(f"{x} is divisible by 3")
else:
    print(f"{x} is not divisible by 3") 

 #PRIME NUMBER
a=int(input("ENTER THE VALUE"))
if(a>1):
    for i in range(2,a):
        if(a%i==0):
            print("NOT A PRIME")
            break
        else:
            print("PRIME")
else:
    print("VALUE OF A IS LESSER THAN 1")

#1
numbers = [1,2,3,4,5,6,7,8,9,10]
for number in numbers:
    if number % 2 == 0:
        print(f"{number} is even")
    else:
        print(f"{number} is odd")

#2
for i in range(1,4):
    print(f"Inside loop, i = {i}")
    if i == 2:
        print("Breaking loop at 2")
        break
else:
    print("Loop finished without any break")

#3
x=12
for i in range(1,30):
    if x>10:
        print(f"{x} is greater than 10")
        if x>20:
            print(f"{x} is greater than 20")
        else:
            print(f"{x} is not greater than 20")
else:
    print(f"{x} is lesser than 10")

#4
age = 25
has_license = True

if age>18 and has_license:
    print("Person is eligible to drive")
else:
    print("person is not eligible to drive")

#5

Ages = [78,34,21,47,9]
condition = True
if condition:
    print("The 'condition is true")
    print(f"Ages list: {Ages}")
else:
    print("The 'condition is false")
    print("No  action taken")



#6
num = int(input("Enter a number: "))
factorial = 1
if num < 0:
    print("Factorial not exist")
elif num == 0:
    print("The Factorial of 0 is 1")
else:
    for i in range(1,num+1):
        factorial = factorial * i
    print(f"The Factorial of {num} is {factorial}")

def factorial(n):
    if n < 0:
        return "Factorial does not exist"
    elif n == 0:
        return 1
    else:
        return n * factorial(n - 1)

n = int(input("Enter a number: "))
result = factorial(n)
print(f"The Factorial of {n} is {result}")


num = int(input("Enter the number  of terms"))

if num <= 0:
    print("The number must be positive")
elif num == 1:
    print("fibonacci sequence : 0")
else:
    a,b = 0,1
    print("Fibonacci Sequence")
    print(a, end = " ")
    for i in range(1, num):
        print(b, end = " ")
        a, b = b, a+b


raw = "job aoushadan"
clean = raw.strip().title()
print(clean)

s = "hello world"
vowels = sum(s.count(v) for v in "aeiou")
print(vowels)


import string
num = str.maketrans({d: "*" for d in string.digits})
print("Phone: 123-456".translate(num))

words = ["apple", "banana", "cherry"]
print(",".join(words))

name, age = "Alice",30
print(f"{name.upper()} is {age} years old")


i = 0
while i < 4:
    print(i)
    i += 1

for x in range(1,10):
    for y in range(x):
       print(x,end = " ")
    print()

for x in "Aoushadan":
    if x == "h":
        break
    print(x)
print("loop has ended")

for x in "Aoushadan":
    if x == "h":
        continue
    print(x)
print("loop continues")

for x in "Aoushadan":
    if x == "d":
        pass
        print("pass executed")
    print(x)
print("loop continues")

Job = [3,5,8,23,45,67]
for x in Job:
    print(x)


Hello = "Aoushadan learning python"
for x in Hello[0:3]:
    print(x)

Hello = "Aoushadan"
for x in Hello[3:]:
    print(x)