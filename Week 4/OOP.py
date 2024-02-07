# Object Oriented Programming in Python
# Whenever you're creating a class & you're defining a function inside the class you have to call "self" as an argument.
class pwskills:
    def welcome_mssg(self):
        print("Welcome to pwskills")
rohan = pwskills()
print(rohan.welcome_mssg())

# init is a in-built function also called as contructor which is used to take data
class pwskills1:
    def __init__(self, email_id, phone_no, student_id):
        self.email_id = email_id
        self.phone_no = phone_no
        self.student_id = student_id

    def return_student_details(self):
        return self.email_id, self.phone_no, self.student_id
    
shally = pwskills1("shallynagfase301@gmail.com", 785347594, 'HG678KJ')
print(shally.phone_no)
print(shally.email_id)
print(shally.student_id)
print(shally.return_student_details())

##########################################################
class pwskills2:
    def __init__(shally, email_id, phone_no, student_id):
        shally.email_id1 = email_id   # Class will always take the variable with self
        shally.phone_no1 = phone_no
        shally.student_id1 = student_id

    def return_student_details(shally):
        return shally.email_id1, shally.phone_no1, shally.student_id1
    
sunita = pwskills1("sunitanagfase@gmail.com", 435457594, 'H3927482J')
print(sunita.phone_no)
print(sunita.email_id)
print(sunita.student_id)
print(sunita.return_student_details())

