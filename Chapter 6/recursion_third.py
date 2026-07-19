# printing elements of the list using recursion

def printing(list, index = 0):
    if (index == len(list)):
        return
    print(list[index], end = "  ")
    printing(list, index+1)

list = ["Awais", 5, 2, 8, "hello", "World"]
printing(list)