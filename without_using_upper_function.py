#Ask user for input.
ask_user = input("Enter a word: ")
#Convert small letters to upper case.
uppercase = ""
for char in ask_user:
    if 'a' <= char <= 'z':
        uppercase += chr(ord(char) - 32)
    else:
        uppercase += char
#Print the result.
print("The output now is: ", uppercase)