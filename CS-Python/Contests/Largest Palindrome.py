def dosomething(num_changes, num_str):
    # Convert the input string to a list of integers
    num_list = list(map(int, str(num_str)))
    length = len(num_list)

    # Iterate through the first half of the list
    for i in range(length // 2):
        left_digit = num_list[i]
        right_digit = num_list[length - i - 1]

        # If digits are not equal, update the smaller one with the larger one
        if left_digit != right_digit:
            max_digit = max(left_digit, right_digit)
            num_list[i] = max_digit
            num_list[length - i - 1] = max_digit
            num_changes -= 1

    # Iterate again to make any remaining changes
    for i in range(length // 2):
        # If there are still changes left, update both digits to 9
        if num_changes > 1 and num_list[i] != 9:
            num_list[i] = 9
            num_list[length - i - 1] = 9
            num_changes -= 2

    # If there is a remaining change and the length is odd, update the middle digit to 9
    if num_changes > 0 and length % 2 == 1:
        num_list[length // 2] = 9

    # Convert the list back to an integer and return the result
    return int(''.join(map(str, num_list)))

# Take input from the user
num_changes = int(input("Enter the number of changes: "))
num_str = input("Enter the number as a string: ")

# Call the dosomething function with the input and print the result
result = dosomething(num_changes, num_str)
print("Result after changes:", result)
