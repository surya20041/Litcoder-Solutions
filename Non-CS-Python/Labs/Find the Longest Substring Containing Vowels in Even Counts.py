# Import the sys module (not used in this code)
import sys

# Define a function named doSomething that takes a string as input and returns an integer
def doSomething(s: str) -> int:
    # Define a dictionary 'vowels' to store the bit representation for each vowel
    vowels = {'a': 1, 'e': 2, 'i': 4, 'o': 8, 'u': 16}
    
    # Initialize variables: d is a dictionary to store the bit representation for each index,
    # bit_representation_for_vowel_count is the XOR of bit representations of vowels encountered so far,
    # result is the maximum length of a substring with the same bit representation for vowel count
    d, bit_represenation_for_vowel_count, result = {0: -1}, 0, 0
    
    # Iterate through the characters and their indices in the input string
    for i, c in enumerate(s):
        # Check if the character is a vowel
        if c in vowels:
            # Update the XOR of bit representations for vowel count
            bit_represenation_for_vowel_count ^= vowels[c]
        
        # Check if the current bit representation for vowel count is not in the dictionary 'd'
        if bit_represenation_for_vowel_count not in d:
            # If not present, add the current bit representation with its index to the dictionary 'd'
            d[bit_represenation_for_vowel_count] = i
        else:
            # If already present, update the 'result' with the maximum length of substring
            # having the same bit representation for vowel count
            result = max(result, i - d[bit_represenation_for_vowel_count])
    
    # Return the final result
    return result

# Take input from the user
inputVal = input()

# Process the input using the doSomething function
outputVal = doSomething(inputVal)

# Print the output
print(outputVal)
