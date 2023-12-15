import sys

def doSomething(arr, n):
    maxVal = max(arr) + 1
    count_list = [0] * maxVal

    for i in range(n):
        val = arr[i]
        count_list[val] += 1

    result_str = ' '.join(map(str, count_list))
    return result_str

# Take Input
inputNum = int(input())
arrInput = list(map(int, input().split()))

# Call the function with user input
outputVal = doSomething(arrInput, inputNum)

# Print Output
print(outputVal)
