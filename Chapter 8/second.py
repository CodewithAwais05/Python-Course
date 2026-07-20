# defining  __init__() function
# this is also called the constructor which runs automatically when an object is initializes

class Student:

    #default constructor
    def __init__(self):
        pass

    #parameterized constructor
    def __init__(self, name, marks):   #__init__() function always contains a parameter as self parameter which points to the current instance, there must be self parameter except other parameters
        self.name = name
        self.marks = marks
        print("Constructor or __init__() function is called.....")

s1 = Student("Awais", [96, 82, 76, 64, 25])  #constructor is called
s2 = Student("Ali", [96, 82, 76, 64, 25])

print(s1.name, s1.marks)
print(s2.name, s2.marks)