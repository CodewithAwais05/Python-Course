# printing multiplication table of the number using for loop 

n = int(input("Enter any number:  "))
for i in range(1, 11, 1):
    print(n, " x ", i, " = ", n * i)
