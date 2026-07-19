# fetching number from the file and check whether it is even or odd

with open("seventh.txt", "r") as f:
    data = f.read()
    print(data)

    num = ""
    for i in range(len(data)):
        if (data[i] == ","):
            number = int(num)
            # print(number)
            if (number % 2 == 0):
                print("Even:  ", (number))
            else:
                print("Odd:  ", (number))
            num = ""
        else:
            num += data[i]
