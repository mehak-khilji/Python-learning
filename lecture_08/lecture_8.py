# OOPS in python
# CLASS & OBJECT IN PYTHON
class Student:
    name = "Mehak"

s1 = Student()
print(s1.name)

s2 = Student()
print(s2.name)

# another example
class Car:
    color = "blue"
    brand = "BMW"

car1 = Car()
print(car1.color)
print(car1.brand)

# INIT FUNCTION
# CONSTRUCTOR

class Student:

    def __init__(self,name, marks):
        self.name = name
        self.marks = marks
        print("adding new student in Database..")
   

s1 = Student("mehak", 91)
print(s1.name, s1.marks)

s2 = Student("sana", 87)
print(s2.name, s2.marks)

s3 = Student("haris", 99.0)
print(s3.name, s3.marks)


# categories of constructors
class Student:

    # DEFAULT CONSTRUCTORS
    def __init__(self):
        pass

   # PARAMETERIZED CONSTRUCTORS
    def __init__(self,name, marks):
        self.name = name
        self.marks = marks
        print("adding new student in Database..")
   

s1 = Student("mehak", 91)
print(s1.name, s1.marks)

s2 = Student("sana", 87)
print(s2.name, s2.marks)

s3 = Student("haris", 99.0)
print(s3.name, s3.marks)


# class & instance attributes

class Student:
    college_name = "GCUF"
    def __init__(self,name, marks):
        self.name = name
        self.marks = marks
        print("adding new student in Database..")
   

s1 = Student("mehak", 91)
print(s1.name, s1.marks)
# print(s1.college_name)

s2 = Student("sana", 87)
print(s2.name, s2.marks)
# print(s2.college_name)

s3 = Student("haris", 99.0)
print(s3.name, s3.marks)
# print(s3.college_name)

print(Student.college_name)

# METHODS

class Student:
    college_name = "GCUF"
    def __init__(self,name, marks):
        self.name = name
        self.marks = marks
        
    def welcome(self):
        print("welcome student", self.name) 

    def get_marks(self):
        return self.marks     
    
s1 = Student("mehak", 96)
s1.welcome()
print(s1.get_marks())

# PRACTICE QUESTION 
# 1:create student class that take name & marks of 3 subject as arguments in constructor then create a method to print average
class Student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks 

    def average(self):
        sum = 0
        for value in self.marks:
            sum +=  value
        print("hi", self.name, "your average score is:", sum/3)  

s1 = Student("Mehak", [92, 77, 89])

s2 = Student("Sana", [89, 90, 87])

s3 = Student("Arslan", [99, 79, 88])

s1.average()
s2.average()
s3.average()

# STATIC METHOD 
class Student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks 
    @staticmethod
    def hello():
        print("hello")
    def average(self):
        sum = 0
        for value in self.marks:
            sum +=  value
        print("hi", self.name, "your average score is:", sum/3)  

s1 = Student("Mehak", [92, 77, 89])
s1.average()
s1.hello()

# ABSTRACTION & ENCAPSULATION
# abstraction example
class Car:
    def __init__(self):
        self.accelerater = False
        self.brake = False
        self.clutch = False

    def start(self):
        self.clutch = True
        self.accelerater = True
        print("Car started..")

car1 = Car()
car1.start()        

# PRACTICE QUESTION
# 1: create account class with 2 attributes- balance & account no. create method for debit, credit and printing balance
class Account:
    def __init__ (self, balance, account):
        self.balance = balance
        self.account_number = account

    #debit method
    def debit(self, amount):
        self.balance -= amount
        print("Rs.", amount, "was debited")
        print("total balance = ", self.get_balance())


    # credit method
    def credit(self, amount):
        self.balance +=  amount
        print("Rs.", amount,"was credited" )  
        print("total balance = ", self.get_balance())


    def get_balance(self):
        return self.balance
        


Account1 = Account(10000, 12456)        
print(Account1.balance)
print(Account1.account_number) 
Account1.debit(1000)
Account1.credit(5000)
Account1.credit(9000)
Account1.debit(2000)      
Account1.credit(1000)

