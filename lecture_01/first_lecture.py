#first program

print("Hello World")


# VARIABLES

name = "Mehak"
age = 21
price = 23.88

print("my name is : ",name)
print("my age is : ", age )
print(price)

#DATA TYPE
name = "Mehak"
age = 21
price = 23.88

print(type(name)) 
print(type(age)) 
print(type(price))

#BOOLEAN DATA TYPE and NONE DATA TYPE

age = 21
old = False
a = None
print(type(old))
print(type(a))

#print sum
a = 2
b = 5
sum = a + b 
print(sum)

#print diff
a = 2
b = 5
diff = a - b 
print(diff)


#type of operators
# 1) arithmetic operators

a = 20
b = 5

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a % b) #remainder
print(a ** b) #a^b

# 2) relational / comparison operator
# they provide boolean values

a = 50
b = 20

print(a == b) #false
print(a != b) #true
print(a >= b) #true
print(a > b)  #true
print(a <= b) #false
print(a < b)  #false

# 3) assignment operators

num = 10
num = num + 10
print("num :", num)

#it can be written as
# += operator
num = 10
num += 10
print("num :", num)

# *= operator

num = 10
num *= 10
print("num :", num)

# -= operator
num = 10
num -= 10
print("num :", num)

# /= operator
num = 10
num /= 10
print("num :", num)


# %= operator
num = 10
num %= 10
print("num :", num)

# **= operater 
num = 10
num **= 10
print("num :", num)


# 4) logical operators
# works on boolean values
# not operator
a = 50 
b = 30

print(not False)
print(not a > b)

# and operator
val1 = True 
val2 = True
print("and operator:", val1 and val2)
# true when both values are true otherwise gives false


# or operator
val1 = True
val2 = False
print("or operator:", val1 or val2)
# false when both values are false otherwise gives true


# TYPE CONVERSION
# (INTERPRETER AUTOMATICALLY CONVERTS THE TYPE)

a = 3
b = 5.89

sum = a + b

# TYPE CASTING
# (WE MANUALLY CONVERT THE DATA TYPE)

a = int("9")
b = 4.25

print(type(a))
print(a + b)
# type casting only works when value have the data which is fit-in in our new type

# INPUT IN PYTHON

name = input("enter your name: ")
print("welcome ", name)

# result for input is always string

val = input("enter some value: ")
print(type(val), val)

# if we want int or float value we can write as
# for int
val = int(input("enter some value: "))
print(type(val), val)

#for float
val = float(input("enter some value: "))
print(type(val), val)

# FOR EXAMPLE
name = input("enter name:")
age = int(input("enter age: "))
marks = float(input("enter marks: "))

print("welcome", name)
print("age =", age)
print("marks =", marks)


# PRACTICE QUESTION
# 1: PROGRAM TO INPUT 2 NUMBER & PRINT THEIR SUM

a = int(input("enter first number: "))
b = int(input("enter second number: "))
print("Sum =", a + b)

# 2: PROGRAM TO INPUT SIDE OF A SQUARE & PRINT ITS AREA

side = float(input("enter square side: "))
print("area =", side * side)

# 3: PROGRAM TO INPUT 2 FLOATING POINT NUMBERS & PRINT THEIR AVERAGE
a = float(input("enter first number: "))
b = float(input("enter second number: "))

print("avg =", (a+b)/2)

# 4: program to input 2 int numbers , a and b print true if a is greater than or equal to b . if not print false

a = int(input("enter first number: "))
b = int(input("enter second number: "))

print(a >= b)
