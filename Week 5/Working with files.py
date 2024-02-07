f = open("shally.txt",'a')
f.write("This is my first sentence in the file.")
f.close()
data = open("shally.txt",'r')
data.read()

data1 = open("shally.txt",'r')
for i in data1:
    print(i)

data.read()

#######################
data.seek(0)  # It will set the cursor to the starting position
data.read()

##########################
import os
print(os.path.getsize("shally.txt"))   # It will give the size of the file

# to copy an existing file into a new file
import shutil
print(shutil.copy("shally.txt","new.txt"))
os.remove("shally.txt")  # To delete a file

with open("new.txt",'r') as f:
    print(f.read())

# To rename a file
os.rename("new.txt","test1.txt")





