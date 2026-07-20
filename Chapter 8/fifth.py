class Student:

    def __init__(self, name):
        self.name = name

s1 = Student("Awais")

print(s1.name)

del s1   # del keyword is used to delete the object or attribute (del s1.name) of the object

# print(s1.name)  # this shows error as we delete the s1