#printing elements of the list using loop
list = [1, 4, 9, 16, 25,  36, 49, 64, 81, 100]

i = 0
while i < 10:
    print(list[i])
    i +=1


# search for number x in the tuple using loop
i = 0
x = int(input("Enter any number to find:  "))
is_exist = False
while True:
    if(x == list[i]):
        is_exist = True
        break;
    i += 1

print("Found:  ", is_exist, "\tAt index:  ", i)