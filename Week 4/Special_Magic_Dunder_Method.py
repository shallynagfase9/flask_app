########################
print(dir(int))
a = 10
print(a+12)

print(a.__add__(9)) # add function

#########################
print(dir(str))

class pwskills:
    def __new__(cls):
        print("This is my new.")

    def __init__(self):
        print("this is my init")

pw = pwskills()

##########################
class pwskills1:
    def __init__(self):
        self.mobile_no = 74835439

    def __str__(self):
        return "This is a magic method which will print something for my object"
    
pw1 = pwskills1()
print(pw1)

#####################
print(dir(tuple))
print(dir(dict))
