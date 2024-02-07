class pwskills:
    def __init__(self,name,gmail):
        self.name = name
        self.gmail = gmail
    def student_details(self):
        print(self.name, self.gmail)

pw = pwskills("shally","shally@gmail.com")
print(pw.name)
print(pw.gmail)
print(pw.student_details())

# Using class method
class pwskills1:
    mobile_no = 324903489
    age = 20
    def __init__(self,name,gmail):
        self.name = name
        self.gmail = gmail
    @classmethod
    def details(cls, name, gmail):
        return cls(name, gmail)
    
    @classmethod           # Whenever you're creating a classmethod the function is applicable for only one instance 
    def change_no(cls, mobile):
        pwskills1.mobile_no = mobile

    def student_details(self):
        print(self.name, self.gmail, pwskills1.mobile_no, pwskills1.age)

pwd = pwskills1.details("shally","shally@gmail.com")
print(pwd.name)
print(pwd.gmail)
print(pwd.student_details())

pws = pwskills1.details("mummy", "mummy@gmail.com")
print(pws.name)
print(pws.student_details())

pw = pwskills1.change_no(782348234)
print(pwskills1.mobile_no)

###########################################################
class pwskills2:
    mobile_no = 324903489
    age = 20
    def __init__(self,name,gmail):
        self.name = name
        self.gmail = gmail
    @classmethod
    def details(cls, name, gmail):
        return cls(name, gmail)
    
    @classmethod           # Whenever you're creating a classmethod the function is applicable for only one instance 
    def change_no(cls, mobile):
        pwskills1.mobile_no = mobile

    def student_details(self):
        print(self.name, self.gmail, pwskills1.mobile_no, pwskills1.age)

def course_details(cls, course_name):  # If you want to add this function in the above class you've to use the following method
    print("Course details: ", course_name)
pwskills2.course_details = classmethod(course_details)
print(pwskills2.course_details("Data Science Masters"))

pw2 = pwskills2("shally","shallynagfase@gmail.com")
print(pw2.student_details())

print(pwskills2.course_details("Full Stack developer course"))

##############################################################
# if you want to delete a attribute use 'del' or 'delattr'
class pwskills3:
    mobile_no = 324903489
    age = 20
    def __init__(self,name,gmail):
        self.name = name
        self.gmail = gmail
    @classmethod
    def details(cls, name, gmail):
        return cls(name, gmail)
    
    @classmethod           # Whenever you're creating a classmethod the function is applicable for only one instance 
    def change_no(cls, mobile):
        pwskills1.mobile_no = mobile

    def student_details(self):
        print(self.name, self.gmail, pwskills1.mobile_no, pwskills1.age)

print(pwskills3.mobile_no)
del pwskills3.mobile_no
print(pwskills3.mobile_no) # Mobile number attribute is being deleted

pw = pwskills3("shally","shallynagfase301@gmail.com")
print(pw.student_details())

delattr (pwskills3,"student_details")
print(pw.student_details()) # Student_details attribute is being deleted

