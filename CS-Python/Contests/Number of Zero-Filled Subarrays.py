def doSomething(nums):
    # Get the length of the input array
    n = len(nums)
    
    # Initialize counters for consecutive zeros and total count
    count = 0
    total_count = 0

    # Iterate through the elements of the array
    for num in nums:
        # Check if the current element is zero
        if num == 0:
            # If yes, increment the count of consecutive zeros
            count += 1
        else:
            # If the current element is not zero, calculate and add the count of subarrays
            # with consecutive zeros to the total count using the formula for the sum of
            # the first n natural numbers: n * (n + 1) / 2
            total_count += (count * (count + 1)) // 2
            
            # Reset the count for consecutive zeros
            count = 0

    # Check for consecutive zeros at the end of the array
    total_count += (count * (count + 1)) // 2

    # Return the total count of subarrays with consecutive zeros
    return total_count

# Take input from the user
nums_str = input("Enter the array elements separated by space: ")
nums = list(map(int, nums_str.split()))

# Example usage
result = doSomething(nums)

# Print the result
print("Total count of subarrays with consecutive zeros:", result)
