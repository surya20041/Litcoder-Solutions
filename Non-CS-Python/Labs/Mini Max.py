import sys

def doSomething(nums):
    sorted_nums = sorted(nums)
    min_sum = sum(sorted_nums[:4])
    max_sum = sum(sorted_nums[2:])
    return min_sum, max_sum

# Take Input
inputVal = list(map(int, input().split()))

# Process Output Using Function
minVal, maxVal = doSomething(inputVal)

# Print Output
print(minVal, maxVal)
