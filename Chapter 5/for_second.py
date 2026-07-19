list = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

for num in list:
    print(num)

x = int(input("Enter any number to find:  "))
for num in list:
    if(x == num):
        print("Found!")
        break
else:
    print("Not Found!")

