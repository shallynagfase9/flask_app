# In dictionary the data is stored in the form of Key and value
# dict = {"key":"value"}
d = {}
print(type(d))

d1 = {"name":"shally","email":"shallynagfase301@gmail.com","branch":"AIDS"}
print(type(d1))
print(d1)

d2 = {"name":"shally","name":"naina"} # When you define two keys of same name it will update with the new one
print(d2)

d3 = {(1,2,3):"abc"}  # Tuples can behave as a key, but List, dict and set will not.
print(d3)

# You can take value as a List, Tuple, Set and Dict.
d4 = {"name":[1,2,3,4],"Phone":37884375}
print(d4)

d5 = {"name":(1,2,3,4),"Phone":37884375}
print(d5)

d6 = {"name":{1,2,3,4},"Phone":37884375}
print(d6)

d7 = {"name":{"abc":37284,"def":3857},"Phone":37884375}
print(d7)

d8 = {"batch":["Data Science Masters","Data Science","Python"],"start_date":(2,10,2023),"mentor_name":{"shally","harpreet","maheshwari"}}
print(d8)
print(len(d8))

# Updating a dictionary
d8["timing"]=(20,34,65)
print(d8)

# Extracting data
print(d8["mentor_name"])

print(type(d8["mentor_name"]))

# Uppercase, Lowercase, Swapcase
d8["name"] = "Sudhanshu"
print(d8["name"].upper())
print(d8["name"].lower())
print(d8["name"].swapcase())

# Extracting data inside a dictionary
d9 = {"name":"shally","class":"Data science masters"}
print(d9)
print(d9["class"])

d9 = {"key":{"name":"shally","class":"Data science masters"}}
print(d9["key"]["name"])

# Adding a key with value in a dict
d9["key1"] = "abc"
print(d9)

# Deleting a key with value
del d9["key1"]
print(d9)
print(len(d9))  # Length of a dictionary

# Clear function will clear the entire dictionary data
d9.clear()
print(d9)

# Extracting only Keys names from a dictionary
d8 = {"batch":["Data Science Masters","Data Science","Python"],"start_date":(2,10,2023),"mentor_name":{"shally","harpreet","maheshwari"}}
print(d8)
print("batch" in d8)
print(d8.keys())

# Extracting only values from a dictionary
d8 = {"batch":["Data Science Masters","Data Science","Python"],"start_date":(2,10,2023),"mentor_name":{"shally","harpreet","maheshwari"}}
print(d8)
print(d8.values())

# Converting dictionary to a list
d8 = {"batch":["Data Science Masters","Data Science","Python"],"start_date":(2,10,2023),"mentor_name":{"shally","harpreet","maheshwari"}}
print(d8)
print(d8.keys())
print(list(d8.keys()))
print(list(d8.values()))

# Extracting items of a list using item function
d8 = {"batch":["Data Science Masters","Data Science","Python"],"start_date":(2,10,2023),"mentor_name":{"shally","harpreet","maheshwari"}}
print(d8.items())

# Copying the data into a new variable using copy function
d10 = d8.copy()
print(d10)

# Pop function will remove specific key from a dictionary
d8.pop("batch")
print(d8)

# fromkeys function will create a dictionary with Keys and values
d = {}
print(d.fromkeys((1,2,3),("shally")))

# Updating a dictionary using update function
k = {"key1":"shally","key2":"maheshwari"}
k1 = {"key3":"Harpreet","key4":"Rohini"}
print((k,k1))
k.update(k1) # Updating k with k1
print(k)

# Get function will return the value of the keys if it is present, otherwise default
k = {"key1":"shally","key2":"maheshwari"}
print(k.get("key1"))
print(k.get("key3"))
print(k["key1"])  # It will also return the value of the key

# Dictionary Comprehensions
print({ i : i**3 for i in range(1,11)})

print({i:i+10 for i in range(1,11)})

# finding log
import math
print({i : math.log10(i) for i in range(1,11)})

# factorial
import math
print({i : math.factorial(i) for i in range(1,11)})






