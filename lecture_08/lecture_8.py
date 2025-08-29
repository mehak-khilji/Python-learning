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