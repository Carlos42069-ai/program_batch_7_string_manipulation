#Add zeroes at the beginning of the string to complete the specified length without using rjust().
user_input = input("Enter a string: ")
total_length = int(input("Enter the desired total length: "))
#Calculate how many zeroes to add.
zeroes_to_add = total_length - len(user_input)
#Add zeroes to the beginning.
padded_string = '0' * zeroes_to_add + user_input
#Print result.
print("Padded string:", padded_string)