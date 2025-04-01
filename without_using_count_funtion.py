#Count how many times the function parameter appears in the string without using count()
user_input = input("Enter a string: ")
substring = input("Enter the substring to count: ")

#Initialize counter
counter = 0

#Check each part of the string
for i in range(len(user_input) - len(substring) + 1):
    if user_input[i:i + len(substring)] == substring:
        counter += 1

#Print result
print(counter)
