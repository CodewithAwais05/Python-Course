# first we reverse the string recursively
def reverse_string(text):
    if text == "":
        return ""
    
    return reverse_string(text[1:]) + text[0]

def check_palindrome(text):
    if text == reverse_string(text):  # then compare reversed string with actual string
        print("String is Plaindrome!!")
    else:
        print("String is not Palindrome!!")

text = input("Enter text:  ")
check_palindrome(text)