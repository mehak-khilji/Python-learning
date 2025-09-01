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

 # DEL KEYWORD
class Student:
    def __init__(self, name):
        self.name = name

s1 = Student("mehak")
print(s1.name)
del s1.name
print(s1.name)
    
# private attributes and methods
class Account:
    def __init__(self, account_no, account_password):
        self.account_no = account_no
        self.__account_password = account_password
    def reset_password(self):
        print(self.__account_password)



Account1 = Account("12456", "abc123")
print(Account1.account_no)
# print(Account1.__account_password)
print(Account1.reset_password())

# another example
class Person:
    __name = "mehak"

    def __hello(self):
        print("hello person!")

    def welcome(self):
        self.__hello()    

p1 = Person()
# print(p1.__name)    
# print(p1.__hello())
print(p1.welcome())

# INHERITENCE (example of single inheritence)
class Car:
    color = "black"
    @staticmethod
    def start():
        print("car started..")

    @staticmethod
    def stop():
        print("car stopped..")

class toyotacar(Car):
    def __init__(self,name):
        self.name = name

car1 = toyotacar("fortuner")
car2 = toyotacar("prius")

print(car1.start(), car1.color)
print(car2.name, car2.color)


# example of multi level inheritence
class Car:

    @staticmethod
    def start():
        print("car started..")

    @staticmethod
    def stop():
        print("car stopped..")

class toyotacar(Car):
    def __init__(self,brand):
        self.brand = brand


class fortuner(toyotacar):
    def __init__(self,type):
        self.type = type

car1 = fortuner("diesel")
car1.start()

# example of multiple inheritence

class A:
    variableA = "welcome to class A"

class B:
    variableB = "welcome to class B"

class C(A, B):
    variableC = "welcome to class C"

c1 = C()
print(c1.variableA)
print(c1.variableB)
print(c1.variableC)

# super method
class Car:
    def __init__(self, type):
        self.type = type

    @staticmethod
    def start():
        print("Car started..")

    @staticmethod
    def stop():
        print("car stopped..")

class toyotacar(Car):
    def __init__(self,name):
        super().__init__(type)
        self.name = name
        super().start()
car1 = toyotacar("prius","electric")
print(car1.type)

# class method
class Person:
    name = "ayesha"

    # def changename(self, name):
    #     Person.name = name 

    @classmethod
    def changeName(cls, name):
        cls,name = name

p1 = Person()
# p1.changename("sadia")
print(p1.name)
print(Person.name)

# property
class Student:
    def __init__(self, physics, chemistry, math):
        self.physics = physics
        self.chemistry = chemistry
        self.math = math
   
    @property
    def percentage(self):
            return str((self.physics + self.chemistry + self.math)/3) + "%"


Student1 = Student(89,76,99)
print(Student1.percentage)  

Student1.physics = 99
# print(Student1.physics)
# Student1.calculate_percentage
print(Student1.percentage)


# POLYMORPHISM : OPERATOR OVERLOADING
class Complex:
    def __init__(self,real,imaginary):
        self.real = real
        self.imaginary = imaginary                      


    def show(self):
        print(self.real, "i+", self.imaginary,"j") 

    def __add__(self, number2):
        newReal = self.real + number2.real
        newimaginary = self.imaginary + number2.imaginary

        return Complex(newReal, newimaginary)
    

    def __sub__(self, number2):
        newReal = self.real - number2.real
        newimaginary = self.imaginary - number2.imaginary
        
        return Complex(newReal, newimaginary)


number1 = Complex(2, 8)
number1.show()    

number2 = Complex(9, 6)
number2.show()  

number3 = number1 + number2
number3.show()

number3 = number1 - number2
number3.show()

