def sum_of_natural_numbers(num):
    if num == 1:
        return 1
    
    return num + sum_of_natural_numbers(num-1)

num = int(input("Enter number upto which you want to find sum:  "))
print("Sum of natural numbers:  ", sum_of_natural_numbers(num))