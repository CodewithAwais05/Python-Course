# Inheritance
# Multilevel Inheritance
#               Base
#                 |
#               Derived(base)
#                 |
#               Derived

class Car:

    @staticmethod  # decorator
    # staticmethod is used to make methods static(which means static method is common for all instances fo the class)
    # it doesn't access instance attributes or doesn't change it
    def start():
        print("Car started...")
    
    @staticmethod
    def stop():
        print("Car stopped...")

class ToyotaCar(Car):

    def __init__(self, name):
        self.name = name
    
class Fortuner(ToyotaCar):
    def __init__(self, type, name):
        self.type = type
        super().__init__(name)


car1 = Fortuner("diesel", "V8")

print(car1.name)
car1.start()
print(car1.type)