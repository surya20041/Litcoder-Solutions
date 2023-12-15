def closest_triplets(nums, target):
    nums.sort()
    n = len(nums)
    closest_sum = float('inf')

    for i in range(n - 2):
        left, right = i + 1, n - 1

        while left < right:
            current_sum = nums[i] + nums[left] + nums[right]
            
            if abs(current_sum - target) < abs(closest_sum - target):
                closest_sum = current_sum
            
            if current_sum < target:
                left += 1
            elif current_sum > target:
                right -= 1
            else:
                return closest_sum

    return closest_sum

# Take input from the user
nums = list(map(int, input().split()))
target = int(input())

result = closest_triplets(nums, target)
print(result)
