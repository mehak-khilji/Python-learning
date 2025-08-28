# LOOPS IN PYTHON
count = 1
while count <= 5 :
    print("hello")
    count += 1

    print(count)

# to print for 100 times
i = 1
while i <= 100 :
    print("khilji", i)
    i += 1

# print number 1 to 5
i = 1
while  i <= 5 :
    print(i)
    i += 1

print ("loop ended")

# loop in reverse order
i = 5
while  i >= 1:
    print(i)
    i -= 1

print ("loop ended")

# practice question
# 1: print numbers from 1 to 100

i = 1
while i <= 100 :
    print(i)
    i += 1

# 2: print numbers from 100 to 1

i = 100
while i >= 1:
    print (i)
    i -= 1

# 3: print a multiplication table of a number n

n = int(input("enter number: "))
i = 1
while i <= 10:
    print(n * i) 
    i += 1

# 4: print elements of following list usimg a loop [1, 4, 9, 16, 25, 36, 49, 64, 81, 100] 

n =[1, 4, 9, 16, 25, 36, 49, 64, 81, 100] 
i = 0

while i < len(n):
    print(n[i])
    i += 1

# another example of ques 4
heroes = ["spiderman", "batman", "ironman"] 
i = 0
while i < len(heroes):
    print(heroes[i])
    i += 1   

# 5: search for a number x in the tuple using loop
#(1, 4, 9, 16, 25, 36, 49, 64, 81, 100)

n = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100) 
x = 4
i = 0

while i < len(n):
    if(n[i] == x):
       print("found at idx:", i)
    i += 1

# BREAK AND CONTINUE KEYWORDS

#BREAK KEYWORD EXAMPLES
i = 1
while i <= 5:
    print(i)
    if (i == 3):
        break
    i += 1

print("end of code")   

# another example

n = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100) 
x = 81
i = 0

while i < len(n):
    if(n[i] == x):
       print("found at idx:", i)
       break
    i += 1
print("end of code")

# CONTINUE KEYWORD EXAMPLES

i = 0
while i <= 5:
    if(i == 3):
        i += 1
        continue
    print(i)
    i += 1

#another example 

i = 1
while i <= 20:
    if(i%2 == 0):
        i += 1
        continue
    print(i)
    i += 1

# FOR LOOP IN PYTHON 
# for loop in list

nums = [1, 2, 3, 4, 5]

for val in nums:
    print(val)

# another example

veggies = ["potato", "carrot", "ladyfinger", "cucumber"]

for val in veggies:
    print(val)

# for loop in tuples

tup = (1, 2, 3, 4, 5, 2, 8, 9)

for num in tup:
    print(num)

# example for string
str = "apna college"

for char in str:
    print(char)

# for loop with else (optional) (it is used when we want complete execution)

str = "apna college"

for char in str:
    print(char)
else:
    print("end")    

# example with break statement
str = "apna college"

for char in str:
    if(char == 'o'):
        print("o found")
        break
    print(char)

print("end")       


# PRACTICE QUESTION
# 1: print element of following list using a loop [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

nums =  [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

for el in nums:
    print(el)

# 2: search for a number x in the tuple using loop (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)    
nums =  (1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 64)

x = 81
idx = 0
for el in nums:
    if(el == x):
        print("number found at idx:", idx )
    idx += 1


# range() FUNCTION  syntax : range(start?, stop, step?)

seq = range(10)

for i in seq:
    print(i)

# it can be written as

for i in range(10): #range(stop)
    print(i)       


for i in range(2, 10): #range(start, stop)
    print(i)


for i in range(2, 10, 2): #range(start, stop, step)
        print(i)


# program to print even number in range 100

for i in range(2, 100, 2):
    print(i)

# program to print odd number in range 100

for i in range(1, 100, 2):
    print(i)

# PRACTICE QUESTION USING FOR ANG RANGE()

# 1: print number 1 to 100

for i in range(1, 101):
    print(i)

# 2: print numbers from 100 to 1

for i in range(100, 0, -1):
    print(i)

# print multiplication table of n

n = int(input("enter number: "))

for i in range(1, 11):
    print(n*i)

# PASS STATEMENT (null statement)

for i in range(5):
    pass

print("some useful info")

# pass statement is also used in if statements

if i > 5:
    pass

# PRACTIICE QUESTIONS 
# 1 : program to find the sum of first n natural numbers(using while)
n = 7
sum = 0
i = 1
while i<= n:
    sum += i
    i += 1
print(sum)

# using for loop
    
n = 5
sum = 0
for i in range(1, n+1):
    sum += i
print("total sum =", sum)

# 2: program to find the factorial of first n natural number (using for)

n = 5
fact = 1
for i in range(1, n+1):
    fact *= i

print("factorial of n =", fact)

# using while
n = 5
fact = 1
i = 1
while i<= n:
    fact *= i
    i += 1
print("factorial of n =", fact)   
         
