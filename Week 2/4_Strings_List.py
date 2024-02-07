name="Shally Nagfase"
print(name.title())
print(name.swapcase())
print(name.find("Nagfase"))
print(name.split("N"))
print(name.capitalize())

############# Reversing a String ############
name = "Data Science Course"
print("".join(reversed(name)))
print("  ".join(reversed(name)))
print(list(name))  # Typecasting
print(list(reversed(name)))   # Typecasting

####### Removing a Character from the string #########
name1 = " PWskills "
print(name1.strip(" "))  # It will remove the space from both the ends of the string
print(name1.lstrip(" "))  # It will remove the space from the left end of the string
print(name1.rstrip(" "))  # It will remove the space from the right end of the string

########## Replacing ##############
name2 = "Greetings from Shally"  # String is immutable , here we are replacing a string or word not a character in a string. 
print(name2.replace("from","to"))  # In this we are replacing "from" with "to" by using replace function
print(name2.replace("S","N"))  

#### ID of a string #######
name3 = "Shally"
print(id(name3))


##### Expanding Tabs ######
name = "Shally \n Nagfase"
print(name.expandtabs())

name = "Shally \t Nagfase"
print(name.expandtabs())

######### Multiple commands in a single string ###########
namee = "Welcome to ata cience pwskills asters course"
print(namee.replace("ata","Data").replace("cience","Science").replace("asters","Masters"))

########## Checking whether the string is in uppercase or lowercase form (True or false) ##########
name = "Hello shally"
print(name.isupper())
print(name.islower())
print(name.isspace()) # Checking whether a string is a whitespace or not
name = " "
print(name.isspace())

#############################################
if " ".isspace():
    print("Hello Shally!!!!!!!!!!!!")

############# startswith and endswith function ###########
name1 = "Nagfase"
print(name1.startswith("N"))
print(name1.endswith("e"))

########## Checking if all the characters in a string is alphanumeric or not ###########
val = "12shally34"
print(val.isalnum())

######### To count the number of characters in  a string ##########
name = "Shally nagfase"
print(len(name))
print(name.count("l"))

count = 0         # using for loop count the number of characters present in a string
for i in name:
    count = count+1
print(count)

#### Using for loop print characters of a string with index #####
for i in range(len(name)):
    print(i,"=",name[i])

############# We can use index to iterate string in reverse direction ######
for i in range(len(name)-1,-1,-1):
    print(i,"=",name[i])

##############################
string = "shally"
ch = len(string)-1
while ch>=0:
    print(string[ch])
    ch = ch-1

###############################
Name = "Shally"
vowels = "AaEeIiOoUu"
for ch in Name:
    if ch in vowels:
       print("{} is a vowel".format(ch))
    else:
       print("{} is not a vowel".format(ch))

########### LIST #############
name = 'Hello!! I am Shally'
print(name.split(" "))

list = [1,2,3,4,5,5]
print(type(list))
print(list[0])
print(list[::-1])
list[2]="shally"
print(list)

######### Concatenation Operation ##########
list1 = ["shally","mummy","ujjwal",1,6,2,9,10]
list2 = [["maheshwari",5,7,'HARPREET']] # List inside a list
list3 = list1 + list2 
print(list3)
print(list3 * 3) # it will repeat all the elements of a list 3 times

################
lst =  ["shally","maheshwari","harpreet",10]
for i in lst:
    if i==10:
        print("present in list")
    else:
        print("not present")
    
####################### Check whether elements in list or not ###########################
list = [1,2,3,4,6]
print(4 in list)

############# MAX function #############
list1 = ["harpreet","shally","maheshwari"]
list2 = [6,5,4,3,2,1]
print(max(list1))  # It will return the max ASCII value, the alphabet which comes last having maximum ASCII value
print(min(list1))  # It will return the min ASCII value, the alphabet which comes first having minimum ASCII value
print(max(list2))  
print(min(list2))

######### Append function ############
######### It will update the list ########
list = [1,5,"harpreet",7,8,10]  # append function will add shally inside the list (update).
list.append("shally")
print(list)
list.pop(4) # Pop function will remove an element from a specific index
print(list)

########## Sorting and reverse method in List ##########
new_list = ["d","e","f","q","m","n"]
print(new_list)
print(new_list[::-1])  # Reversing a list using slicing

new_list.reverse()   # Reversing a list
print(new_list)

new_list.sort()  # It will sort the list in Ascending order
print(new_list)

new_list.sort(reverse=True)  # It will sort the list in Descending order
print(new_list)

new_list.append(10)
print(new_list)

new_list.append(["shally","nagfase"]) 
print(new_list)

new_list.extend(["shally","nagfase"])  # Extend function can add multiple elements at the same time in a list
print(new_list)


########### NESTED LIST #############
list1 = [1,2,3]
print(sum(list1))
list2 = [4,5,6]
list3 = [7,8,9]
matrix = [list1,list2,list3]
print(matrix)
print(matrix[1][2])
print(matrix[:])

######### LIST COMPREHENSATION #########
print([i for i in range(0,20)])

print([i if i%2==0 else " " for i in range(0,20)])  # Even numbers

print([i if i%2!=0 else "EVEN" for i in range(0,20)])  # ODD numbers

######## Sum of even and odd numbers in a list
even_sum = 0
odd_sum = 0
list = [1,2,3,4,5,6,7,8,9]
for i in list:
    if i%2==0:
        even_sum+=i
    else:
        odd_sum+=i
print(even_sum)
print(odd_sum)

##########################################
even_sum=sum([i for i in list if i%2==0])  # Sum of even numbers
print(even_sum)

odd_sum=sum([i for i in list if i%2!=0])  # Sum of odd numbers
print(odd_sum)


######### square of numbers ########
square_num=[i**2 for i in list]
print(square_num)

## Create a List of all positive numbers in a list ##
list1 = [-3,-2,-1,0,1,2,3]
print(list1)
pos_num = [i for i in list1 if i>=0]
print(pos_num)

## Create a list of only the first letters of words in a list ##
list = ["apple","banana","strawberry","mango"]
first_letter_words = [i[0] for i in list]
print(first_letter_words)

## Convert a list of Temperatures from Celsius to Farheneit using List Comprehensation ##
celsius_temperatures = [0,10,20,30,40,50]
farheneit_temp = [((9/2)*i+32) for i in celsius_temperatures]
print(farheneit_temp)

## Flatten a list of lists into a single list
lists = [[1,2,3],[4,5,6],[7,8,9]]
flatten_list = [i for j in lists for i in j]
print(flatten_list)


################
lst = [1,2,3,4,5,6]
lst.insert(4,"shally")
print(lst)

#################
c = 1+2j
print(type(c))
print(c.real)  # It will print real part
print(c.imag)  # It will print imaginary part

# Assignment
## Using both code and list comprehensation

### Create a list of only the prime numbers from a given list ###

### Create a List of all the possible combinations of 2 elements from a List ###

