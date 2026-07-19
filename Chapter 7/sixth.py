# practice question
# question is: first we write linesin file and then replaces the Java word wih Python


with open("practice.txt", "w") as f:  # writing to file
    f.write("Hi, everyone!\nWe are learning File I/O.\n")
    f.write("I like programming in Java.\nWe are learning Java.\n")


with open("practice.txt", "r") as f:  # reading from file
    data = f.read()

new_data = data.replace("Java", "Python")  # updating Java into Python
print(new_data)


with open("practice.txt", "w") as f:  # again writing updated data to file
    f.write(new_data)

if (data.find("learning") != -1):  # check whether the word "learning" exists or not
    print("Found")
else:
    print("Not found")

