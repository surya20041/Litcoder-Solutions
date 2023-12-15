def sort_colors(nums):
    low, mid, high = 0, 0, len(nums) - 1

    while mid <= high:
        if nums[mid] == 0:
            nums[low], nums[mid] = nums[mid], nums[low]
            low += 1
            mid += 1
        elif nums[mid] == 1:
            mid += 1
        else:
            nums[mid], nums[high] = nums[high], nums[mid]
            high -= 1

# Take input from the user
user_input = input()
nums = [int(color) if color.isdigit() else color for color in user_input.split()]

# Call the sorting function
sort_colors(nums)

# Print the sorted array as a string
sorted_string = ' '.join(map(str, nums))
print(sorted_string)
