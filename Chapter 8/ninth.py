# Inheritance
# Multiple Inheritance
#               Base1    Base2
#                  |      |
#                   Derived

class A:

    nameA = "Class A name..."
    def __init__(self):
        print("Class A....")
        super().__init__()

class B:

    nameB = "Class B name..."
    def __init__(self):
        print("Class B....")

class C(A, B):

    nameC = "Class C name..."
    def __init__(self):
        print("Class C....")
        super().__init__()  # super() is used to access the methods (and attributes) of the next parent class in the Method Resolution Order (MRO).

        # MRO (Method Resolution Order) is the order in which Python searches for methods and attributes when you call them on an object.
        # It tells: "If a method or attribute isn't found in the current class, which parent class should I search next?"
        
c = C()
print(C.mro())   # className.mro() is used to find the order of the base classes (order of constructor)

print(c.nameA)
print(c.nameB)
print(c.nameC)