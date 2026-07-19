# simple opening and closing and opening of file
# open file in read mode

f = open("first.txt", "r")
data = f.read()

print(data)

print("---------------------------")

print(type(data))

f.close()