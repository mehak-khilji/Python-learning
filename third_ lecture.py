# tuple and list
# LIST IN PYTHON

marks = [94.0, 87.5, 67.8, 78.9, 99.0]
print(marks)
print(type(marks))
print(marks[0])
print(marks[3])
print(len(marks)) #length of a list

# another example
student = ["Mehak", 98.8, 21, "Pakistan"]
print(student)
student[0] = "Noor"
#strings are immutable and list are mutable

#LIST SLICING (similar to string slicing)

marks = [94.0, 87.5, 67.8, 78.9, 99.0]
print(marks[1:4])
print(marks[ :4])
print(marks[0: ])
print(marks[-1:-3])


#list Method

# 1: list.append()   {adds one element at the end. it returns none}
list = [2, 3, 5]
list.append(7)
print(list)

# 2: list.sort()  {sort in ascending order}
list = [9, 6, 10, 3, 5, 2]
list.sort()
print(list)

# 3: list:sort(reverse=True)  {sorts in descending order}
list = [9, 6, 10, 3, 5, 2]
list.sort(reverse=True)
print(list)

# 4: list.reverse()  {reverse the list}
list = [9, 6, 10, 3, 5, 2]
list.reverse()
print(list)

# 5: list.insert(idx, el) {insert element at index
list = [9, 6, 10, 3, 5, 2]
list.insert(1, 5)
print(list)

# 5: list.remove()  {remove first occurence of element}
list = [2, 1, 5, 2, 5]
list.remove(5)
print(list)

# 6: list.pop(idx) {remove element at idx}
list = [3, 5, 9, 6]
list.pop(2)
print(list)

# TUPLES IN PYTHON  {we cannot add or remove element in tuple}
tup = (87, 4, 56, 78, 98, 39)
print(type(tup))
print(tup[0])
print(tup[2])
print(tup[4])

#empty tuple 
tup = ()
print(tup)
print(type(tup))

#single value tuple {in tuple, it is compulsory to add comma in single value otherwise it considered as int}
tup = (4,)
print(tup)

#slicing in tuple {same as in list}
tup = (98, 78, 68, 56, 66)
print(tup[0:4])
print(tup[0: ])
print(tup[ :4])
print(tup[-4:-1])

#tuple method
# 1: tup.index(el)

tup = (2, 5, 8, 2, 8)
print(tup.index(2))
print(tup.index(8))
print(tup.index(5))

# 2: tup.count(el)

tup = (4, 6, 9, 5, 4, 9, 4, 6)
print(tup.count(4))
print(tup.count(6))
print(tup.count(9))


# PRACTICE QUESTION
# 1:program to ask the user to enter names of their 3 favorite movies & store them in a list
 
movies = []
mov1 = input("enter 1st movie: ")
mov2 = input("enter 2nd movie: ")
mov3 = input("enter 3rd movie: ")

movies.append(mov1)
movies.append(mov2)
movies.append(mov3)

print(movies)

#2: Program to check if a list contains a palindrome of elements {use copy() method}

list1 = [1, 2, 1]
copy_list1 = list1.copy()
copy_list1.reverse()

if(copy_list1 == list1):
    print("palindrome")
else:
    print("not palindrome")

# another example of palindrome
list1 = ["m", "a", "a", "m"]
copy_list1 = list1.copy()
copy_list1.reverse()

if(copy_list1 == list1):
    print("palindrome")
else:
    print("not palindrome")

# 3: program to count number of students with "A" garde in following tuple

grade = ("C", "D", "A", "A", "B", "B", "A")
print(grade.count("A"))

# 4: store the above values in the list & sort them from "A" to "B"

grade = ["C", "D", "A", "A", "B", "B", "A"]
(grade.sort())
print(grade)