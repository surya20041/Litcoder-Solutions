def doSomething(s1, s2):
    # Get the lengths of input strings s1 and s2
    m = len(s1)
    n = len(s2)

    # Create a 2D list to store the lengths of common child strings
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Fill the dp table using bottom-up dynamic programming
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            # Check if the characters at the current positions in both strings are equal
            if s1[i - 1] == s2[j - 1]:
                # If equal, extend the length of the common child string
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                # If not equal, take the maximum length from either of the two directions
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    # The length of the longest common child string is stored in dp[m][n]
    return dp[m][n]

# Take input from the user
s1 = input("Enter the first string: ")
s2 = input("Enter the second string: ")

# Call the function with user input
result = doSomething(s1, s2)

# Display the result
print("Length of the longest common child string:", result)
