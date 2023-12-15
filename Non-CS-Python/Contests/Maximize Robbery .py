import sys

def doSomething(houses):
    n = len(houses)
    
    # Base cases
    if n == 0:
        return 0
    elif n == 1:
        return houses[0]
    elif n == 2:
        return max(houses[0], houses[1])

    # Initialize an array to store the maximum stolen amount up to each house
    dp = [0] * n

    # Base cases for the first two houses
    dp[0] = houses[0]
    dp[1] = max(houses[0], houses[1])

    # Iterate over the rest of the houses to calculate the maximum stolen amount
    for i in range(2, n):
        # Choose the maximum between robbing the current house and skipping it
        dp[i] = max(dp[i - 1], dp[i - 2] + houses[i])

    # Return the maximum stolen amount from the last house
    return dp[-1]

# Take Input
inputVal = input()

# Convert Input String into Array
inputArray = list(map(int, inputVal.split()))

# Process Output Using Function
outputVal = doSomething(inputArray)

# Print Output
print(outputVal)
