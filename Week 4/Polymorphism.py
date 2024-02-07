# Polymorphism means the same function name (but different signatures) being used for different types. 
# The key difference is the data types and number of arguments used in function.
def test(a,b):
    return a+b

print(test(45,23))
print(test([1,23,4,54,56],[45,2354,6,2]))
print(test('Shally',' Nagfase'))

###################################
class data_science:
    def syllabus(self):
        print("Welcome to data science course.")

class web_development:
    def syllabus(self):
        print("Welcome to Web development course")

def class_parcer(class_obj):
    for i in class_obj:
        i.syllabus()

obj_data_science = data_science()
obj_web_dev = web_development()

class_obj = [obj_data_science, obj_web_dev]
print(class_parcer(class_obj))
