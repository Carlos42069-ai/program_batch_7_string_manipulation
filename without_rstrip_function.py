#Ask user for input with spaces after the words.
ask_user = input("Enter a word with extra spaces after: ")
#Remove ther extra spaces after the word.
while user_input and user_input[-1] == " ":
    user_input = user_input[:-1]
#Print the outcome.