""" The main difference between a List and a Tuple is that, 
in List the elements are stored in Square brackets and in Tuple the elements are stored in Paranthesis """
# List is mutable whereas Tuple is immutable.

t1 = ("shally",1,2,3,4+5j,4.5,True)
print(t1)
print(type(t1))
print(t1[0])
print(t1[::-1])
print(" ".join(reversed(t1[0])))  # Reversing a string element having index 0 from a tuple.
print(t1[0:3])  # Printing only particular elements from a tuple using slicing.
print("shally" in t1) # Checking whether a element is present inside a tuple or not
print(98 in t1)

""" 
In Tuple, only Two in-built functions are present:
 1) Count 
 2) Index 
"""
print(t1.count("shally"))
print(t1.count("abc"))
print(t1.count(4.5))
print(t1.count(True)) # System is storing the value of true as 1


print(t1.index("shally"))
print(t1.index(4.5))
print(t1.index(True))  # The value of true is 1
print(t1.index(3))

# Iteration in Tuple
for i in t1:
    print(i,type(i))

############################
t2 = (1,2,3,4)
print(t2*3)
print(t2)
print(type(t2))
print(max(t2))  # Max value
print(min(t2))  # Min value
""" 
Tuples basically follows immutability,
where it is not going to allow to change any element at a particular index
"""

# Tuples inside a tuple
t1 = (1,2,3,4,5)
t2 = (3,4,5,6,7)
t3 = (t1,t2)
print(t3)

# List inside a tuple
t3 = ((23,45,6,5),[1,2,3,4,5])
print(t3)

# Deleting a tuple
t5 = (45,32,76,23,56)
print(t5)
del t5


# Find number of elements inside a tuple using len function
t5 = (34,56,23,5)
print(len(t5))