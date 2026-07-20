class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    def average(self):
        sum = 0
        for num in self.marks:
            sum += num
        avg = sum / 3
        return avg

s1 = Student("Awais", [98, 95, 93])
s2 = Student("Ahmad", [88, 85, 92])

print("Name:  ", s1.name)
print("Average:  ", s1.average())

print("-------------------------------")

print("Name:  ", s2.name)
print("Average:  ", s2.average())