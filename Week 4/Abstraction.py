''' Abstraction is used to hide the internal functionality of the function from the users. 
The users only interact with the basic implementation of the function,
 but inner working is hidden. User is familiar with that "what function does" but they don't know "how it does."
 '''
 # Abstraction is used to create a blueprint

import abc

class pwskills:

    @abc.abstractmethod
    def student_details(self):
        pass

    @abc.abstractmethod
    def student_assgmt(self):
        pass

    @abc.abstractmethod
    def student_marks(self):
        pass

class data_science(pwskills):
    def student_details(self):
        return "It will try to return the details of data science students"
    
    def student_marks(self):
        return "It will try to return the marks of data science students"
    
class web_dev(pwskills):
    def student_details(self):
        return "It will try to return the details of web development students"
    
    def student_marks(self):
        return "It will try to return the marks of web development students"
    
ds = data_science()
wd = web_dev()

print(ds.student_marks())
print(ds.student_details())

print(wd.student_marks())
print(wd.student_details())