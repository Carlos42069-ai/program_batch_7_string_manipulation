#Ask user for input.
ask_user = input("Enter a sentence: ")
suffix = input("Enter the suffix to remove: ")
#Remove the suffix without using remove suffix.
if ask_user.endswith(suffix):
    user_input = ask_user[:-len(suffix)]

#Prints out the output.