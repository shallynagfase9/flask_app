# __ (double underscore simply means that I am creating a private variable)
class pwskills:
    def __init__(self, course_name, course_price):
        self.__course_name = course_name
        self.course_price = course_price

pw = pwskills("Data science course",3500)
print(pw.course_price)
# print(pw.course_name) # It will not work as course_name is private variable only creator can get access
print(pw._pwskills__course_name) # we have to use underscore with class name to access private variable


################################################################################
class pwskills1:
    def __init__(self, course_price, course_name):
        self.__course_price = course_price
        self.course_name = course_name

    @property
    def course_price_access(self):
        return self.__course_price
    
    @course_price_access.setter
    def course_price_set(self, price):
        if price < 3500:
            pass
        else:
            self.__course_price = price

    @course_price_access.deleter
    def course_price_del(self):
        del self.__course_price


pw = pwskills1(4500, "Data Science course")
print(pw._pwskills1__course_price)
print(pw.course_price_access)
pw.course_price_set = 3500
print(pw.course_price_access)

del pw.course_price_del   # It will delete the private variable course price
print(pw.course_price_access) 

            

