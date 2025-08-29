# # file I/O 
# # OPEN, READ AND CLOSE FILE
# # read method
# f =open("demo.txt", "r")
# data = f.read()
# print(data)
# print(type(data))
# f.close

# # if we want to read few particular characters . we can also pass them as a parameter
# f =open("demo.txt", "r")
# data = f.read(10)
# print(data)

# f.close

# # if we want to read one line at a time
# f =open("demo.txt", "r")
# line1 = f.readline()
# print(line1)
# line2 = f.readline()
# print(line2)
# f.close

# # read mode read the whole data so, we cannot use readline to read data line by line

# # WRITING TO A FILE
# # write method
# f = open("demo.txt", "w")

# f.write("i want to learn javascript tomorrow.")

# f.close

# # append method
# f = open("demo.txt", "a")
# f.write("Then I'll move to ReactJS")
# f.close

# # we have to write \n before append data if we want to write data in next line

# file = open("demo.txt", "a")
# f.write("\nAfter that nodejs.")
# f.close

# # if we open non exsisting file in write or append mode python automatically create that file. for example

# f = open("sample.txt", "w")
# f.close

# f = open("demo.txt","r+") #overwrite + read
# f.write("abc")
# print(f.read())
# f.close()

# f = open("demo.txt","w+") #truncate data + read
# print(f.read())
# f.write("abc")
# f.close()

# # WITH SYNTAX
# with open("demo.txt","r")as f:
#     data = f.read()
#     print(data)

# with open("demo.txt","w")as f:
#     f.write("new data")

# # DELETING A FILE 
# import os

# os.remove("sample.txt")    

# # practice questions
# # 1: create a new file "practice .txt" using python. add following data in it
# # Hi everyone
# # we are learning file I/O
# # using java
# # I like programming in java 

# with open("practice.txt", "w") as f:
#     f.write("Hi everyone\nwe are learning file I/O\n")
#     f.write("using java\nI like programming in java")
    
# # 2: function that replace all occurrences of "java" with "python" in above file

# with open("practice.txt", "r") as f:
#     data = f.read()

# new_data = data.replace("java", "Python")
# print(new_data)

# with open("practice.txt", "w") as f:
#     f.write(new_data)


# # 3: search if the word "learning" exist in the file or not
# def find_word():

#     word = "learning"
#     with open("practice.txt", "r") as f:
#         data = f.read()
#         if(word in data):
#             print("found")
#         else:
#             print("not found")

# find_word()

# # 4: function to find in which line of the file does the word "learning" occur first. print -1 if not found

# def check_for_line():
#     word = "learning"
#     data = True
#     line_no = 1
#     with open("practice.txt", "r")as f:
#         while data:
#             data = f.readline()
#             if(word in data):
#                 print(line_no)
#                 return
#             line_no += 1

#     return -1
# print(check_for_line())     

# # 5: from a file containing number separated by comma, print the count of even number 

# with open("practice.txt", "r") as f:
#     data = f.read()
#     print(data)

#     num = ""
#     for i in range(len(data)):
#         if(data[i] == ","):
#             print(int(num))
#             num = ""
#         else:
#             num += data[i]


# ANOTHER METHOD               
count = 0
with open("practice.txt", "r") as f:
    data = f.read()
    
    numbers = data.split(",")
    for value in numbers:
        if(int(value)%2 == 0):
            count += 1 
print(count)