# A lambda function is a small anonymous function written in one line.

# Syntax:
#       lambda arguments: expression

# Lambda functions:

square = lambda x : x*x  # square function
print("Square:  ", square(5))

cube = lambda x : x*x*x  # cube function
print("Cube:  ", cube(5))

sum = lambda a,b : a + b  # sum function
print("Sum of two numbers:  ", sum(5, 2))

greet = lambda name : print("Hello", name)  # greet function
greet("Awais")