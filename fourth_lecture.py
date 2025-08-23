#dictionary and set
# DICTIONARY IN PYTHON

info = {
    "key" : "values",
    "name" : "Mehak",
    "learning" : "coding",  
    "age" : 21,
    "is_adult" : True,
    "marks" : 94.7 
} 
print(info)

# we can also store list and tuples

info = {
    "name" : "Mehak",
    "subjects" : ["python", "C", "java"],
    "topics" : ("dictionary", "set")
}
print(info)
print(type(info))

# all data types are acceptable in values but in keys we cannnot use list or tuple
# keys are immutable

# we can access the value by using its key name 

dict = {

    "name" : "Mehak",
    "subjects" : ["python", "C", "java"],
    "topics" : ("dictionary", "set")
}
print(dict["name"])
print(dict["topics"])

# we can also assign the other value to keys 

dict = {

    "name" : "mehak",
    "subjects" : ["python", "C", "java"],
    "topics" : ("dictionary", "set")
}

dict["name"] = "sana"
print(dict["name"])
print(dict["topics"]) 

# we can also add new key value very esaily

dict = {

    "name" : "mehak",
    "subjects" : ["python", "C", "java"],
    "topics" : ("dictionary", "set")
}

dict["surname"] = "khilji"
print(dict)

# we can also create empty dictionary . we can also add values in empty dictionaries

null_dict = {}
print(null_dict)


# nested dictionaries
student = {
    "name" : "rahul",
    "subject" : {
        "phy" : 90.6,
        "chem" : 80.9,
        "comp" : 99.2
            }
}
print(student)
print(student["subject"]) # if we want to print the one key
print(student["subject"]["chem"]) # if we want to print only one key 

# DICTIONARY METHODS
# 1: mydict.keys()   (return all keys)

student = {
    "name" : "rahul",
    "subject" : {
        "phy" : 90.6,
        "chem" : 80.9,
        "comp" : 99.2
            }
}
print(student.keys())
#we can also type cast keys in tuple and list  
print(list(student.keys()))
print(tuple(student.keys()))
# to print length of dictionary keys
print(len(student))

#to print length of list and tuple
print(len(list(student.keys())))
print(len(tuple(student.keys())))

# 2: mydict.values()   (return all values)

student = {
    "name" : "rahul",
    "subject" : {
        "phy" : 90.6,
        "chem" : 80.9,
        "comp" : 99.2
            }
}

print(student.values())
print(list(student.values())) # to change values in list
print(tuple(student.values())) # to change values in tuple
print(len(student)) # to print length
print(len(list(student.values()))) # to print length of list
print(len(tuple(student.values()))) # to print length of tuple

# 3: mydict.items()  {return all (key , values) pairs as tuple}

student = {
    "name" : "rahul",
    "subject" : {
        "phy" : 90.6,
        "chem" : 80.9,
        "comp" : 99.2
            }
}

print(student.items())
print(list(student.items())) # to change values in list
print(tuple(student.items())) # to change values in tuple
print(len(student)) # to print length
print(len(list(student.items()))) # to print length of list
print(len(tuple(student.items()))) # to print length of tuple

# we can also also access tuples individually

pairs = list(student.items())
print(pairs[0])

# 4: mydict.get("keys")  {return the keys according to value}


student = {
    "name" : "rahul",
    "subject" : {
        "phy" : 90.6,
        "chem" : 80.9,
        "comp" : 99.2
            }
}

print(student["name"]) # if we enter non exist value it returns error
print(student.get("name")) # if we enter non exist value it returns none instead of error by usimg method

# for example
print(student["name2"]) #error
print(student.get("name2")) # no error -> returns none

# 4: mydict.update({new dict}) {insert the specified items to the dictionary}


student = {
    "name" : "rahul",
    "subject" : {
        "phy" : 90.6,
        "chem" : 80.9,
        "comp" : 99.2
            }
}

student.update({"city" : "karachi"})
print(student)

# we can also add multiple values in dictionary by using update method 

student.update({"city" : "karachi" , "age" : 21 , "country" : "Pakistan"})
print(student)

# if we pass the same key in dictionary it update its value as duplicate keys are not allowed in dictionary 
# for example

student.update({"city" : "karachi" , "name" : "khan"})
print(student)


# Set in python
# unordered item , unique and immutable . we cannot store list and dictionary in set.

collection = {1, 2, 3, 4}

print(collection)
print(type(collection))

# we can also add string in set, we can also find length ,set ignore duplicate values , for example

set = { 1, 2, 2, 2, "mehak", "mehak"}
print(set)
print(type(set))
print(len(set))

# for empty set

collection = set()
print(type(collection))

# SET METHOD
# SET ARE MUTABLE BUT AN ELEMENTS OF SET ARE IMMUTABLE.

# 1: set.add()  (adds an element)
collection =  set()
collection.add(2)
collection.add(6)
collection.add(4)
collection.add((1,2,3)) # we can also add tuples
collection.add(6) #set ignore duplicate values
print(collection)         

# 2: set.remove()  (removes an element)

collection = {1, 6, 7, 9, 2}

collection.remove(6)
print(collection) 

# 3: set.clear()  (empties the set)

collection =  set()
collection.add(2)
collection.add(6)
collection.add(4)
collection.add((1,2,3)) 
collection.add(6)
collection.clear()
print(len(collection))

# 4: set.pop()   (removes a random value)
collection = {"hello", "apna college", "world", "coding", "python"}
print(collection.pop())
print(collection.pop())
print(collection.pop())

# 5: set.union()  (combine both set values and return new)
set1 = {1, 2, 3}
set2 = {2, 3, 4,}
print(set1.union(set2))

# 6: set.intersection()  (combine coommon values and return true)
set1 = {1, 2, 3}
set2 = {3, 4, 5}
print(set1.intersection(set2))


# PRACTICE QUESTIONS

# 1: store following word meanings in a python dictionary
# table : "a piece of furniture", "list of facts and figures"
# cat : "a small animal"

dict = {
    "cat": " a small animal",
    "table" : ["a piece of furniture", "list of fact and figures"]
}

print(dict)

# 2: you are given a list of subject for students assume one classrooom is required for one subject how many classrooms are needed by all students
# "python", "java", "C++", "python", "javascript", "java", "python", "java", "C++", "C"

subjects = {"python", "javascript", "java", "C++", "C", "python", "java", "C++", "python", "java"}
print(subjects)
print(len(subjects))      

# 3: program to enter marks of 3 subjects from user and store them in a dict. start with empty dict and add one by one use subject name as key and marks as values

marks = {}

x = int(input("enter marks: ")) 
marks.update({"physics" : x })

x = int(input("enter marks: ")) 
marks.update({"math" : x })

x = int(input("enter marks: ")) 
marks.update({"computer" : x })
print(marks)

# 4: figure out a way to store 9 & 9.0 as separate value in set (you can take help from built in data type)
values = {9, "9.0"}
print(values)

# another method to solve this question

values = {
    ("float", "9.0"),
    ("int",  "9")

}
print(values)