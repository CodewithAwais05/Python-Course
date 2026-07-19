# another syntax of opening file in different modes is called "with syntax"
# it is as:

with open("first.txt", "r") as f:
    data = f.read()
    print(data)


 # there is no need to close the file
 # as the control exits this, it automatically closes the file

 # this syntax is same meaning as:
 #      f = open("first.txt", "r")
 #      data = f.read()
 #      print(data)
 #      f.close()