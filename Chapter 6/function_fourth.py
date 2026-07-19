# function to calculate the length of the list

def calc_len(list):
    return len(list)

list = ["Awais", 6, 2, 7, 9, "Hello", "World"]
print("Length of the string:  ", calc_len(list))

# function to print the elements of the list

def printing_list(list):
    # for ele in list:   # can also be written using for loop
    #     print(ele, end = "\t")
    print(list)

list = ["Awais", 6, 2, 7.3, "Hello World"]
printing_list(list)