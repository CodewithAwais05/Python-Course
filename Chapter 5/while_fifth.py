# using the 'break' and 'continue' keywords

i = 0
while i <= 5:
    print(i)
    i += 1
    if i == 2:
        continue   # to skip the current iteration
    if i == 3:
        break   # to terminate the entire loop
