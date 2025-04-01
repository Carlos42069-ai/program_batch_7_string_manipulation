#Return the first location of the function parameter in the string without using index()
user_input = input("Enter a string:")
substring = input("Enter the substring to find:")

#Loop through the string
for i in range(len(user_input)):
    if user_input[i:i+len(substring)] == substring:
        #Print the first occurrence index
        print(i)
        break