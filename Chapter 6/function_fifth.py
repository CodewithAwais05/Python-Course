# finding factorial of the number input by the user

def factorial(n):
    i = 1
    fact = 1
    while i <= n:
        fact *= i
        i += 1
    return fact

a = int(input("Enter number to find the factorial:  "))
print("Factorial:  ", factorial(a))

# Converting USD into PKR

def convervsion(usd):
    return (usd * 275)

usd = int(input("Enter currency in USD:  "))
print("USD into PKR:  ", convervsion(usd))