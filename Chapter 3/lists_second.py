# Program to demonstrate common list methods

numbers = [5, 2, 9, 1, 7]

print("Original list:", numbers)

numbers.append(4)
print("After append(4):", numbers)

numbers.remove(2)
print("After remove(2):", numbers)

numbers.sort()
print("After sort():", numbers)

print("Length of the list:", len(numbers))
print("First element:", numbers[0])
