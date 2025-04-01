#Ask user for input. 
ask_user = input("Enter your input: ")
starts_with = input("Enter the word to be checked in your input: ")

#Checking if the entered word starts with the inputed function parameter.
print_results = ask_user[:len(starts_with)] == starts_with

#Print if it is true or false.
print("The result is: ", print_results)
