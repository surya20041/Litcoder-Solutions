def doSomething(nums, queries):
    answer = []

    for query in queries:
        k, trim = query

        # Trim each number in nums
        trimmed_nums = [int(num[-trim:]) for num in nums]

        # Create a list of tuples (trimmed number, original index)
        trimmed_tuples = [(num, index) for index, num in enumerate(trimmed_nums)]

        # Sort the list based on the trimmed numbers
        trimmed_tuples.sort()

        # Retrieve the kth smallest trimmed number and its original index
        kth_smallest = trimmed_tuples[k - 1]

        # Reset each number in nums to its original length
        original_nums = [int(num) for num in nums]

        # Store the answer (original index of kth smallest trimmed number)
        answer.append(original_nums.index(original_nums[kth_smallest[1]]))

    return answer

# Input
nums = input().split()
queries_count = int(input())
queries = [list(map(int, input().split())) for _ in range(queries_count)]

# Output
result = doSomething(nums, queries)
print(" ".join(map(str, result)))
