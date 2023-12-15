import sys

def doSomething(nums):
    max_reach = 0
    target = len(nums) - 1

    for i in range(len(nums)):
        # If the current index is beyond the maximum reach, it's not possible
        # to reach the end
        if i > max_reach:
            return "false"

        # Update the maximum reachable index
        max_reach = max(max_reach, i + nums[i])

        # If the maximum reachable index is beyond or equal to the target,
        # return True
        if max_reach >= target:
            return "true"

    return "false"

# Take input from the console
nums_input = list(map(int, input().split()))

# Call the function with user input
result = doSomething(nums_input)
print(result)
