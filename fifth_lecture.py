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