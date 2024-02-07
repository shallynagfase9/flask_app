l = [1,2,3,4,5,6,7,8,9,10]
def test(l1):
    n = []
    for i in l1:
        n.append(i**2)
    return n
print(test(l)) 

# Map Function
l = [23,12,3,32,5,65]  
"""Map in Python is a function that works as
an iterator to return a result after applying a function to every item of an iterable (tuple, lists, etc.). """
print(list(map(lambda i: i**2,l)))
print(list(map(lambda i: i+20,l)))
print(list(map(lambda i: str(i),l))) # Converting every element of a list into string


##########################
def sq(x):
    return x**2
print(list(map (sq,l)))

#########################
list1 = [23,34,34,6,5,3]
list2 = [6,34,7,98,23,4]
print(list(map(lambda x,y: x+y, list1, list2)))

############################
list1 = [23,34,34,6,5,3]
list2 = [6,34,7,98,23,4]
f = lambda x,y: x+y
print(list(map(f, list1, list2)))

###########################
val = "Shally"
print(list(map(lambda c: c.upper(), val)))
print(list(map(lambda c: c.lower(), val)))
print(list(map(lambda c: c.swapcase(), val)))

##################################
######### Reduce Function ########
l = [23,1,2,4,5]   
"""The reduce() function returns a single reduced value 
that is the result of cumulatively applying the function to the elements of the iterable. """
from functools import reduce
print(reduce(lambda x,y: x+y, l))
print(reduce(lambda x,y: x if x>y else y, l))

######################
def add(x,y):
    return(x+y)
print(reduce(add,l))

######## Filter Function ##########
l = [32,45,1,2,3,4,5]
print(list(filter(lambda x: x%2==0,l))) # Extracting even numbers from list
print(list(filter(lambda x: x%2!=0,l))) # Extracting odd numbers from list

##################################
"""Python's filter() is a built-in function that allows you to process an iterable and extract 
those items that satisfy a given condition. This process is commonly known as a filtering operation."""
l = [-1,-2,-3,-4,0,1,2,3,4]
print(list(filter(lambda x: x>=0,l)))  # Extracting positive numbers from list
print(list(filter(lambda x: x<0,l)))   # Extracting negative numbers from list

# Extracting with length in list
l = ['shally','harpreet','maheshwari']
print(list(filter(lambda x: len(x) > 6, l)))