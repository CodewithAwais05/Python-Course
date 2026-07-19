# recursive function to calculate the factorial of the number

def factorial(n):
    if (n == 0 or n == 1):
        return 1
    return n * factorial(n-1)

n = int(input("Enter number to calculate the factorial:  "))
print("Factorial:  ", factorial(n))

# recursive function to calculate the sum of numbers from 1 to N

def calc_sum(n):
    if (n == 1):
        return 1
    return n + calc_sum(n - 1)

a = int(input("Enter number upto which you want to calculate the sum:  "))

print("Sum:  ", calc_sum(a))