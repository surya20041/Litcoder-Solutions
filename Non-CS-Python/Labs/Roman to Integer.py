def roman_to_integer(s):
    roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    result = 0
    prev_value = 0

    for char in s:
        current_value = roman_dict[char]

        if current_value > prev_value:
            result += current_value - 2 * prev_value
        else:
            result += current_value

        prev_value = current_value

    return result

# Take input from the user
roman_input = input().upper()

# Convert and display the result
try:
    integer_result = roman_to_integer(roman_input)
    print(integer_result)
except KeyError:
    print("Invalid Roman numeral. Please enter a valid Roman numeral.")
