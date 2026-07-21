def reverse_string(text):
    if text == "":
        return ""
    
    return reverse_string(text[1:]) + text[0]

text = input("Enter text:   ")
print("Reversed String:  ", reverse_string(text))

