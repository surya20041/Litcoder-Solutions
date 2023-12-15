def combination_sum(candidates, target):
    def backtrack(start, target, path):
        if target == 0:
            result.append(path[:])
            return
        for i in range(start, len(candidates)):
            if target >= candidates[i]:
                path.append(candidates[i])
                backtrack(i, target - candidates[i], path)
                path.pop()

    result = []
    candidates.sort()
    backtrack(0, target, [])
    return result

# Take input from the user
user_input = input()

# Check if the input contains commas or spaces and split accordingly
if ',' in user_input:
    candidates = list(map(int, user_input.split(',')))
else:
    candidates = list(map(int, user_input.split()))

target = int(input())

# Get the combinations
result = combination_sum(candidates, target)

# Display the output line by line
for combination in result:
    print(" ".join(map(str, combination)))
