# instead of writing a block of code repeatedly, we can simply write that block of code in a specific function and call that function simply


# instead of writing the entire logic repeatedly as:
# a = 6
# b = 3
# sum = a + b
# print("Sum is:  ", sum)

# we can just call the function as:
def calc_sum(a, b):  # a and b are parameters
    return (a+b)

# 6 and 33 are arguments
sum = calc_sum(6, 33)  # 6 + 33 = 39
print("Sum is:  ", sum)