#Add spaces at the beginning of the string to complete the specified length without using rjust().
user_input = input("Enter a string: ")
total_length = int(input("Enter the desired total length: "))
#Calculate how many spaces to add.
spaces_to_add = total_length - len(user_input)
#Add spaces to the beginning.

#Print result.
