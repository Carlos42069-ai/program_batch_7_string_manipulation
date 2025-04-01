#Ask user for input.
ask_user = input("Enter a word: ")
suffix = input("Enter the suffix to remove: ")
#Remove the suffix without using remove suffix.
if ask_user.endswith(suffix):
    ask_user = ask_user[:-len(suffix)]

#Prints out the output.
print("Modified string:", repr(ask_user))
