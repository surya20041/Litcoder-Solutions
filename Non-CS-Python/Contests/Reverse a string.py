def doSomething(input_str):
    # Reverse the entire string while preserving spaces and case
    reversed_str = ''
    space_positions = [i for i, char in enumerate(input_str) if char.isspace()]

    for i, char in enumerate(input_str):
        if space_positions and i == space_positions[-1]:
            reversed_str += input_str[space_positions.pop()]
        elif not char.isspace():
            reversed_str = char + reversed_str

    # If there are remaining spaces, add them to the end of the reversed string
    reversed_str += ' '.join([input_str[i] for i in space_positions[::-1]])

    return reversed_str

# Take input from the user
input_str = input()

# Call the doSomething function and print the result
result = doSomething(input_str)
print(result)
