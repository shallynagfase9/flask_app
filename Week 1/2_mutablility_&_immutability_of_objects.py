#INDEXING AND SLICING

a="Shally Nagfase"
print(a[-1])
print(a[1:])
print(a[::-1])
print(a[3:7])
print(a[5])
print(a[12:8:-1])
#List are used to store multiple items in a single variable of different types
l=["shally",2,3,4,6+9j,3.4,True]
print(l)
print(type(l))
print(l[::-1])
print(l[1:])
print(l[3])
print(l[-4])

#replacing value at a particular index
l[4]=100
print(l)

#String is a immutable object
#Whereas list is mutable you can change values at a particular index in a collection of elements
s="shally" #This is a string and you cannot make changes to a string as it is immutable