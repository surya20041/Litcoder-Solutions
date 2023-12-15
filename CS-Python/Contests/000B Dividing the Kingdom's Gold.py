import sys
# Function to perform a specific task based on the given input values
def doSomething(inputVal):
    try:
        # Calculate the total amount of gold
        total_gold = sum(inputVal)
        northern_sum = 0
        valid_splits = 0

        # Iterate through the input list to find valid splits
        for i in range(len(inputVal)-1):
            northern_sum += inputVal[i]
            southern_sum = total_gold - northern_sum

            # Check if the northern region has more or equal gold compared to the southern region
            # and if the southern region has a positive amount of gold
            if northern_sum >= southern_sum and southern_sum > 0:
                valid_splits += 1

        # Return the count of valid splits
        return valid_splits

    except ValueError:
        # Handle the case where the input is not in the correct format
        return "Input string was not in the correct format."

try:
    # Take input values from the user, assuming they are space-separated integers
    inputVal = list(map(int, input().split()))

    # Call the doSomething function with the input and print the result
    outputVal = doSomething(inputVal)
    print(outputVal)

except ValueError:
    # Handle the case where the input is not in the correct format during user input
    print("Input string was not in the correct format.")
