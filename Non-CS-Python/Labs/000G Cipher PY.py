# Import Necessary Libraries
import sys

def substitute_cipher(word, cipher):
    # Initialize str
    encrypted_word = ''
    
    # Iterate Input String
    for char in word:
        if char.isalpha():
            encrypted_word += cipher[char]
        else:
            encrypted_word += char
    
    return encrypted_word

def perform_math_operation(word, operation, key):
    # Check for addition
    if operation == 'addition':
        return ''.join(chr(ord(char) + key) if char.isalpha() else char for char in word)
    # Check for subtraction
    elif operation == 'subtraction':
        return ''.join(chr(ord(char) - key) if char.isalpha() else char for char in word)
    # default return
    else:
        return "Invalid Operation"

def doSomething(word, key, operation, cipher):
    # Check for valid key (positive integer)
    if not key.isdigit() or int(key) <= 0:
        return "Enter valid key"

    # Check for valid operation
    if operation not in ['addition', 'subtraction']:
        return "Invalid Operation"

    # Check if the word is in capitals
    if word.islower():
        return "Word should be in capitals"

    # Substitute characters using the cipher
    substituted_word = substitute_cipher(word, cipher)

    # Perform the mathematical operation on ASCII values
    encrypted_word = perform_math_operation(substituted_word, operation, int(key))

    return encrypted_word

# Initial Cipher
cipher = {'A': 'Z', 'B': 'Y', 'C': 'X', 'D': 'W', 'E': 'V', 'F': 'U', 'G': 'T', 'H': 'S', 'I': 'R', 'J': 'Q',
          'K': 'P', 'L': 'O', 'M': 'N', 'N': 'M', 'O': 'L', 'P': 'K', 'Q': 'J', 'R': 'I', 'S': 'H', 'T': 'G',
          'U': 'F', 'V': 'E', 'W': 'D', 'X': 'C', 'Y': 'B', 'Z': 'A'}

# Take Input
inputKey = input()
inputOpperation = input()
inputWord = input()

# Process Output Using Function
outputVal = doSomething(inputWord, inputKey, inputOpperation, cipher)

# Print Output
print(outputVal)
