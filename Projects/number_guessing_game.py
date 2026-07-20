# Question:  1. Number Guessing Game

# Generate a random number between 1-100 (use import random, random.randint())
# Let user guess repeatedly using a while loop
# Print "Too high" / "Too low" / "Correct!"
# Count and display number of attempts at the end
# Stretch: Limit to 7 attempts. Add difficulty levels (1-50, 1-100, 1-1000).

import random  # import random to create random number

print("============== Number Guessing Game ==============")
print("Choose difficulty level:  ")
print("1.   Easy (1 - 50)")
print("2.   Medium (1 - 100)")
print("3.   Hard (1 - 1000)")

choice = int(input("Enter your choice:  "))

# set difficulty level 

if choice == 1:
    limit = 50
elif choice == 2:
    limit = 100
elif choice == 3:
    limit = 1000
else:
    print("Invalid Choice!!!")
    exit()

secret_number = random.randint(1, limit)  # creating random number
max_attempts = 7
attempts = 0

# Guessing number logic

while attempts < max_attempts:
    guess = int(input("Enter your guess:   "))
    attempts += 1

    if guess > secret_number:
        print("Too High!!!")
    elif guess < secret_number:
        print("Too low!!!")
    else:
        print("Correct!!!")
        print("You guessed the number....")
        print("Total Attempts:   ", attempts)
        break
else:  # else block runs only when loop ends normally without break
    print("============== Game Over ==============")
    print("Correct number was ", secret_number)