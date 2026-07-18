# Basic program to demonstrate Python lists

fruits = ["apple", "banana", "mango"]

print("My favorite fruits are:")
for fruit in fruits:
    print(fruit)

print("\nThe first fruit is:", fruits[0])
print("The last fruit is:", fruits[-1])

fruits.append("orange")
print("\nAfter adding orange:", fruits)
