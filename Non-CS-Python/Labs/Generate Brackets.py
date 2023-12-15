def generate_parentheses(n):
    def backtrack(s='', left=0, right=0):
        if len(s) == 2 * n:
            result.append(s)
            return
        if left < n:
            backtrack(s + '(', left + 1, right)
        if right < left:
            backtrack(s + ')', left, right + 1)

    result = []
    backtrack()
    return result

# Take input from the user
n = int(input())

# Generate and print the combinations with periods
combinations = generate_parentheses(n)
output = ".".join(combinations)
print(output)
