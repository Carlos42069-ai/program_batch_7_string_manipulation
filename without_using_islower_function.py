#Ask user for input.
ask_user = input("Enter a word: ")
#Check the input if it's in lower cases.
all_lowercase = True  
for char in ask_user:
    if not ('a' <= char <= 'z'):
        all_lowercase = False
#Print whether it is true or false.
print("Is all lowercase?:", all_lowercase)