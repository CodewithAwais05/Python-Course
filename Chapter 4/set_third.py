collection1 = {1, 2, 3, "Hello", "Awais", 5.4, 7.3}

print(collection1)
print(type(collection1))

collection2 = {1, 2, 2, 3, 4, 4} #wll become {1, 2, 3, 4}

collection1.add(5)  # to add a value
print(collection1)

collection1.remove(5.4)  # to remove a value
print(collection1)

collection2.pop()  # to remove a random value
print(collection2)

collection2.clear()  # to empty the set
print(collection2)

