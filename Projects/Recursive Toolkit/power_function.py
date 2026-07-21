def power_func(num, exp):
    if exp == 0:
        return 1
    
    return num * power_func(num, exp-1)

num = int(input("Enter number:  "))
exp = int(input("Enter its exponent:  "))

# just formatting in the printing

print(num, " raised to the power ", exp, "(", num, "^", exp, "):  ", power_func(num, exp))
