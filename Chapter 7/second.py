# simple opening and closing and opening of file
# open file in write mode (overwrites the text in the file)

f = open("second.txt", "w")
f.write("Hello! I am Awais Raza.")

data = input("Enter sentence to write in the file:  ")
f.write(data)

f.close()