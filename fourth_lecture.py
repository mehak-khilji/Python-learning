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
print(student["subject"]) # is want to print the one key
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