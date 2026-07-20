#   3. Password Strength Checker

# Input a password string
# Check length ≥ 8, contains a digit, contains uppercase, contains a special character
# Print which conditions failed
# Stretch: Give a strength score (Weak/Medium/Strong) instead of pass/fail.

# inputting password

password = input("Enter password:  ")
has_digit = False
has_special_character = False
has_upper = False

score = 0

# checking validity
if len(password) >= 8:
    score += 1

for ch in password:
    if ch.isdigit():
        has_digit = True
    elif ch.isupper():
        has_upper = True
    elif not ch.isalnum():
        has_special_character = True

# scoring for stregth
if has_digit:
    score += 1
if has_upper:
    score += 1
if has_special_character:
    score += 1

# specific errors

if len(password) < 8:
    print("Password must be at least 8 characters.")

if not has_digit:
    print("Password must contain a digit.")

if not has_upper:
    print("Password must contain an uppercase letter.")

if not has_special_character:
    print("Password must contain a special character.")

# printing score and strength

print("Password Score:  ", score, " / 4")

if score <= 1:
    print("Strength:  Weak")
elif score == 2 or score == 3:
    print("Strength:  Medium")
else:
    print("Strength:  Strong")