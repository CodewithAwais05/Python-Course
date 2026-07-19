# concept of range (start from 0 by default, step = increment by 1 by default, stop at some index point)

for i in range(6): # start from 0 by default and end at 6-1=5, increment of 1 by default
    print(i, end = " ") # 0 1 2 3 4 5


# another method of writing this:

seq = range(6)
for i in seq:
    print(i, end = " ")


# syntax of the range:
#       range(start(optional), stop(compulsory), step(optional))

for i in range(0, 11, 2): #  range(start, stop, step)
    print(i, end = "  ")
