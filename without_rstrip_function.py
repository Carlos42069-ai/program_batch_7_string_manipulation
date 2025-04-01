#Ask user for input with spaces after the words.
ask_user = input("Enter a word with extra spaces after: ")
#Remove ther extra spaces after the word.
while ask_user and ask_user[-1] == " ":
    ask_user = ask_user[:-1]
#Print the outcome.
print("Output after removing space:", repr(ask_user))