# simple opening and closing and opening of file
# open file in append mode (write at the end of the file)

f = open("first.txt", "a")
f.write("Hello! I am Awais.")

data = input("Enter sentence to (append) write in the file:  ")
f.write(data)

f.close()