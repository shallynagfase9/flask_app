name = "Shally"
print(name + " Nagfase") # String Concatenation
print(name * 5) # Name will print 5 times

# Find function
print(len(name))  # len() is built-in-function which is used to find out the length of the string
print(name.find("l"))  # find built-in-function will find the index of the element which you want to find
print(name.find("a",1,6))  
print(name.find("z"))

# Count Function
print(name.count(" "))  # count() is built-in-function which is used to count the number of elements which you want to count in the string
print(name.count("l"))
print(name.count("a"))

# Split function
name1 = "Data Science Masters"
print(name1.split())  # Split function will split the entire string
print(name1.split("S"))  # If you split a string with a particular element than that element will be gone(removed)

# Partition function
name2 = "Data Science"
print(name2.partition("e"))  # Partition built-in-function is used to seperately partition a particular element
print(name2.partition("S"))

# String UPPERCASE & LOWERCASE
value = "Shally Suresh Nagfase"
print(value.upper())  # Upper built-in-function will capitalize the entire string
print(value.lower())   # Lower built-in-function will  the lower-case the string characters
print(value.swapcase()) # Swapcase built-in-function will uppercase the characters which were in lowercase and lowercase the characters which were in uppercase.

# Title Function
name = "naina nagfase"  # It will capitalize the first element of a word like a Title.
print(name.title())

# CAPITALIZE FUNCTION()
name = "maths is a easy subject"
print(name.capitalize())  # # CAPITALIZE FUNCTION() make the first character uppercase and rest the lowercase

# REVERSING A STRING()
name = "Shally"
print(name[::-1])
