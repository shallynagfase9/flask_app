"""
Whenever we are creating a Function we have to define a def Keyword.
print will return 'Nontype' so always prefer "return".
Using Function will increase the Code usability & modularity.
Argument means data. 
"""

# Creating a basic function using def keyword
def test():  # Here the function name is test
    pass
print(test())

# Creating a basic function using return type
def test1():
    return "My name is Shally Suresh Nagfase. "
print(test1())

print(test1() + "Hello World!!!")  # Here we can perform concatenation of a string and a return type

# Creating a basic function using print.
def test2():
    print("My name is Naina Suresh Nagfase. ")
print(test2()) #Nontype and string cannot be concatenated bcoz print always return Nontype
#print(test2() + "Hello Everybody!!!")  # (Error) Here we cannot perform concatenation of a string using print. Because print always return Nontype.

# Creating a function which will return values of different datatypes
def test3():
    return 30,12,4+7j,"shally"
print(test3())
print(test3()[0]) # Indexing and slicing in functions
print(test3()[2])
print(test3()[3])

##############################
a,b,c,d = 12,56,"hello",45
print(a) # a is holding value 12
print(b) # b is holding value 56
print(c) # c is holding value "hello"
print(d) # d is holding value 45

# creating function using some logic
def test4():
    a = 4*5 + 20
    return a
print(test4())

#########################
def test5(a,b):  # Here we are passing two arguments a and b
    c = a + b
    return c
print(test5(54,67)) # we need to pass the value of argument a and b
print(test5("shally","nagfase"))  # We can take any value for a and b
print(test5([1,2,3,4,5],[6,7,8,9,10]))
print(test5(b = "shally",a = "nagfase"))

# Create a function which will take list as a input and give me a final list with numeric values.
l = [1,2,3,4,5.1,"shally",[5,6,7,8,9,10]]
def test6(a):
    n  = []
    for i in a :
        if type(i) == int or type(i) == float :
            n.append(i)
    return n
print(test6(l))

"""
Create a function which will take list as a input and give me a final list with numeric values 
as well as the elements inside the list which are numeric. 
"""
l = [1,2,3,4,5.1,"shally",[5,6,7,8,9,10]]
def test7(a):
    n = []
    for i in a:
        if type(i) == list:
            for j in i:
                if type(j) == int or type(j) == float:
                    n.append(j)
        else:
            if type(i) == int or type(i) == float:
                n.append(i)
    return n

print(test7(l))


#########################
def test8(*args):  # *args (*) will allow us to take n number of arguments
    return args
print(test8(12,23,45,56))
print(test8("shally",45,4+7j,"sahjs"))

###########################
def test9(*args,a):
    return args,a
print(test9([12,3,23],a="ujjwal"))

# Create a function that will return only the list from the dataset
# data extraction based on type
def test10(*a):
    n = []
    for i in a:
        if type(i) == list:
            n.append(i)
    return n
print(test10([34,5,3,43,435],23,45,23,67)) # Inside this data if there is a list extract it (The above code is used for that purpose).

# Creating a function using key and value arguments (just like dictionary)
def test11(**kwargs):   # (*) this symbol is used for n  number of values in an argument and ** is used for key & values (kw = key words)
    return kwargs

print(type(test11()))
print(test11())
print(test11(name="shally",addess="Kamptee",branch=["AI&DS","AIML"]))

def test12(**kwargs):   # Extracting list from a dictionary using function
    for i in kwargs:
        if type(kwargs[i]) == list:
            return i,kwargs[i]
print(test12(name="shally",addess="Kamptee",branch=["AI&DS","AIML"]))

# Passing number of arguments and key with values simultaneously using function
def test13(*args,**kwargs):
    return args,kwargs
print(test13(1,2,3,4,5,a=[34,56,43,56,23])) # Here where you are assigning a key to the values it will be by default consider as a dictionary.