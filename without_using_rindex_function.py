#Return the last location of the function parameter in the string without using rindex()
user_input = input("Enter a string: ")
substring = input("Enter the substring to find: ")

#Loop through the string in reverse
for i in range(len(user_input) - len(substring), -1, -1):
    if user_input[i:i + len(substring)] == substring:
        #Print the last occurrence index
        print(i)
        break