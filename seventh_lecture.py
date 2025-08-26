# file I/O 
# OPEN, READ AND CLOSE FILE
# read method
f =open("demo.txt", "r")
data = f.read()
print(data)
print(type(data))
f.close

# if we want to read few particular characters . we can also pass them as a parameter
f =open("demo.txt", "r")
data = f.read(10)
print(data)

f.close

# if we want to read one line at a time
f =open("demo.txt", "r")
line1 = f.readline()
print(line1)
line2 = f.readline()
print(line2)
f.close

# read mode read the whole data so, we cannot use readline to read data line by line

# WRITING TO A FILE
# write method
f = open("demo.txt", "w")

f.write("i want to learn javascript tomorrow.")

f.close

# append method
f = open("demo.txt", "a")
f.write("Then I'll move to ReactJS")
f.close

# we have to write \n before append data if we want to write data in next line

file = open("demo.txt", "a")
f.write("\nAfter that nodejs.")
f.close

# if we open non exsisting file in write or append mode python automatically create that file. for example

f = open("sample.txt", "w")
f.close

