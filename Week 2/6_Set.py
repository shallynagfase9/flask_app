# Set is another Data structure which is used to store collection of data elements but it does not store Duplicates.
# In set, no indexing and slicing is possible because it follows hashable indexing
s = {1,2,3,4}
print(type(s))

s1 = {}
print(type(s1))

s2 = {22,54,22,34,54,55,66,55,44,55,66}
print(s2)  # It will not store duplicates

# converting a set into a list
print(list(s2))
# converting a set into a tuple
print(tuple(s))

# If you want to remove dupicates from a list or a tuple you can directly convert it into a set, it will remove all the duplicates inside it.

# In set, extraction is possible using iteration
ss = {12,34,54,"shally","ujjwal"}
for i in ss:
    print(i,type(i))

# Set built-in-functions
s3 = {23.3,45,23,45,"shally","harpreet","rohini","harsh"}
s3.add(1) # Adding a element in a set using add function.
print(s3)

s3.remove("shally") # Removing a element from a set using remove function.
print(s3)

print(len(s3))  # Length of a set

print(s3.pop())  # Pop a element from a set
print(s3)

s3.clear() # Removing all elements from a set
print(s3)

s4 = {1.5,3,4,6}
s5 = {3,4,6,9}
print(s4.difference(s5))  # Display the different element unique one
print(s5.difference(s4))

