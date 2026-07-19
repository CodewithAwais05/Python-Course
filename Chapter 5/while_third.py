#printing a multiplication table of any number given by user

n = int(input("Enter any number:  "))
i = 1

while i <= 10:
    print(n, " x ", i, " = ", n * i)
    i += 1
