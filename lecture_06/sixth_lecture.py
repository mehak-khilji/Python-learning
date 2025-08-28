# FUNCTION AND RECURSION
# functions in python 

def calculate_sum(a, b):
    sum = a + b
    print(sum)
    return sum

calculate_sum(20, 10)
calculate_sum(80, 20)
calculate_sum(45, 45)

# it can be written as 
def calculate_sum(a, b):
    return a + b

sum = calculate_sum(1, 8)
print(sum) 

# program to print hello
def print_hello():
    print("hello")

print_hello()  

# average of 3 number

def average(x, y, z):
    sum = x + y + z
    avg = sum/3
    print(avg)
    return average

average(4, 8, 3)
average(99, 80, 100)


# built-in function
# 1: print()
print("student", end=" ") #sep = " "
print("mehak khilji") #end = "\n"

# DEFAULT PARAMETERS
def multiplication(a, b=4): #default arguments should be in the end
    print(a * b)
    return a * b
    
multiplication(1)

# it can be written as like this:
def multiplication(a=2, b=4):
    print(a * b)
    return a * b
    
multiplication()

# PRACTICE QUESTIONS
# function to print length of list .(list is the parameter)

numbers = [1, 2, 4, 5, 5, 7, 8, 9]
countries = [ "Pakistan", "UK", "USA", "Framce", "turkey"]
def print_length(list):
    print(len(list))


print_length(countries)
print_length(numbers)

# 2: function to print elements of list in single line. (list is the parameter)

heroes = ["thor", "spiderman", "superman", "batman", "ironman"]

def print_elements(list):
    for item in list:
        print(item, end=" ")

print_elements(heroes)           

# 3: function to find the factorial of n. (n is the parameter)
n = int(input("enter number: "))

def calculate_factorial(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i
    print(fact)

calculate_factorial(n)


# function to convert USD to PKR

def converter(usd_value):
    pkr_value = usd_value * 283
    print(usd_value, "USD =", pkr_value, "PKR")

converter(20)

# function to input number to find even and odd number

n = int(input("enter number: "))
def find_function(n):
    if n%2 == 0:
        print("even number")
    else:
        print("odd number")

find_function(n)        

# RECURSION

def show(n):
    if (n == 0):
        return
    print(n)
    show(n-1)
   
show(5)

#another example
#return n!

def fact(n):
    if(n == 1 or n == 0):
        return 1
    return fact(n-1)*n
    
print(fact(3))   

# practice question
# 1: recursive function to calculate sum of first n natural numbers

n = int(input("enter number: "))
def calculate_sum(n):
    if(n == 0):
        return 0
    return calculate_sum(n-1) + n

sum =calculate_sum(n)
print(sum)

# 2: write a recursive function to print all elements in a list. (hint: use list and index as parameter)

fruits = ["mango", "apple", "banana", "grapes", "orange"] 
def print_list(list, index=0):
    if(index == len(list)):
        return
    print(list[index])
    print_list(list, index+1)

print_list(fruits)

