sentence = input("Enter a sentence: ")
vow_count = 0
for char in sentence:
    if char.lower() in 'aeiou':
        vow_count += 1
print("Number of vowels in the sentence:", vow_count)