# ESCAPE SEQUENCE CHARACTERS
# \n used for next line
str1 = "this is a string.\nwe are creating it in python."
print(str1)


# \t FOR TAB SPACE
str = "this is a string.\twe are creating it in python."
print(str)

# CONCATENATION
str1 = "Mehak"
str2 = "Khilji"
str = (str1 + str2)
print(str)

# LENGTH OF STRING
str = "Apna College"
len1 = len(str)
print(len1)

# length count number, space, special character and digit


# INDEXING start from 0

str = "Apna College"
print(str[6])
print(str[0])
print(str[3])
print(str[7])

# we cannot modify character by using indexing. we can only access them

# Slicing

str = "DPS college"
print(str[1:7])# is PS col
print(str[ :4]) #same as str[0:4]
print(str[1: ]) #same as str[1:len(str)]

# NEGATIVE INDEXING means backward counting start from -1
str = "Apple"
print(str[-5:-1]) # is appl

# STRING FUNCTION()
# 1: str.endswith()  true if string end with substring otherwise gives false

str = "I am a coder."
print(str.endswith("der."))

# 2: str.capitalize()  capitalize 1st ch 
str = "mehak khilji"
print(str.capitalize())

# it cannot change original string . if we want to change the original string we can write as
str = "mehak khilji"
str = str.capitalize()
print(str)

# str.replace(old, new) it replace old occurences with new
str = "i am studying python from apna college."
print(str.replace("o" , "a"))

# we can also change whole substring. for example
str = "i am studying python from apna college."
print(str.replace("python" , "javascript"))

# str.find(word) return 1st index of 1st occurrence
str = "i am a coder."
print(str.find("a"))

# we can search for whole word also
str = "i am a coder."
print(str.find("am"))

# if we search for a word that doesn't exist python provide index -1

# str.count()  count the occurrence of substring
# for word
str = "i am studying python from apna college."
print(str.count("from"))

# for single letter
str = "i am studying python from apna college."
print(str.count("o"))
  


# PRACTICE QUESTION
# 1: program to input user's first name & print its length

name = input("enter your name: ")
print("length of your name is: ", len(name))

# 2: program to find occurence of '$' in a string

str = "hi$, i am $ symbol $$99.0 "
print(str.count("$"))


# CONDITIONAL STATEMENT
# IF statement.

age = 21

if(age >= 18):
    print("can vote")
    print("can drive")

# elif statement.  it workd only when IF condition gives false. 
light = "green"

if(light == "red"):
    print("stop")
elif(light == "yellow"):
    print("look")
elif(light == "green"):
    print("go")    

print("end of code")

# else statement . we can write else statement only once

light = "green"

if(light == "red"):
    print("stop")
elif(light == "yellow"):
    print("look")
elif(light == "pink"):
    print("go")    
else:
    print("light is broken")    

print("end of code")

# another example
age = 14 

if(age >= 18):
    print("can vote")
else:
    print("cannot vote")   


# GRADE STUDENTS BASED ON THEIR MARKS      

marks = int(input("enter student marks: "))

if(marks >= 90):
    grade ="A"
elif(marks >= 80 and marks < 90):
    grade = "B"    
elif(marks >= 70 and marks < 80):
    grade = "C"  
else: 
    grade = "D"
print("grade of student ->" , grade)


# NESTING

age = 38

if(age >= 18):
    if(age >= 80):
        print("cannot drive")
    else:     
        print("can drive")
else:
    print("cannot drive") 

# PRACTICE QUESTION
# 1: program to check if a number entered by user is odd or even.


num = int(input("enter number: "))
rem = num % 2
if(rem == 0):
    print("even")
else:
    print("odd")    

# 2: program to find the largest of 3 numbers entered by the user.

a = int(input("enter first number: "))
b = int(input("enter second number: "))
c = int(input("enter third number: "))

if(a>b and a>c):
    print("a is largest", a)
elif(b>a and b>c):
    print("b is largest", b)
else:
    print("c is largest", c)

# 3: program to find the largest of 4 numbers entered by the user.


a = int(input("enter first number: "))
b = int(input("enter second number: "))
c = int(input("enter third number: "))
d = int(input("enter fourth number: "))
if(a>b and a>c and a>d):
    print("a is largest", a)
elif(b>a and b>c and b>d):
    print("b is largest", b)
elif(c>a and c>b and c>d):
    print("c is largest", c)
else:
    print("d is largest", d)        

# 4: PROGRAM TO CHECK IF A NUMBER IS A MULTIPLE OF 7 OR NOT

x = int(input("enter number: "))
rem = x % 7
if(rem == 0):
    print("multiple of 7")
else:
    print("not a multiple of 7")    




