"""
Static methods in Python are extremely similar to python class level methods, 
the difference being that a static method is bound to a class rather than the objects for that class. 
This means that a static method can be called without an object for that class.
"""

# Without static method
class pwskills:
    def student_details(self, name, mail, number):
        print(name, mail, number)
pw = pwskills()
print(pw.student_details("shally","abc@gmail.com", 36784382))

# With static method
class pwskills1:
    def student_details(self, name, mail, number):
        print(name, mail, number)

    @staticmethod
    def mentor_class(mentor_list):
        print(mentor_list)

    def mentor(self, mentor_list):
        print(mentor_list)


print(pwskills1.mentor_class(["shally", "maheshwari", "harpreet"]))
pw1 = pwskills1()
print(pw1.mentor(["harpreet", "shally", "maheshwari"]))

##########################################
class pwskills2:
    def student_details(self, name, mail, number):
        print(name, mail, number)

    @staticmethod
    def mentor_class(mentor_list):
        print(mentor_list)

    @staticmethod
    def mentor_mail_id(mail_id):
        print(mail_id)

    @classmethod
    def class_name(cls, class_name):
        cls.mentor_class(["AIDS","AIML"])

    def mentor(self, mentor_list):
        print(mentor_list)

pw = pwskills2()
print(pw.student_details("shally", "shally@gmail.com", "74383598348"))
print(pw.mentor_class("AIDS"))
print(pw.mentor_mail_id("shallynagfase@gmail.com"))
print(pw.class_name("data science masters"))
print(pw.mentor(["shally","harpreet","maheshwari"]))

print(pwskills2.mentor_mail_id("harpreet@gmail.com"))
