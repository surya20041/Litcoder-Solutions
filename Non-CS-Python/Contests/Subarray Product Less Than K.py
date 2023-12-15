def count_subarrays(nums, k):
    if not nums or k <= 0:
        return 0
    
    count = 0
    product = 1
    left = 0
    
    for right in range(len(nums)):
        product *= nums[right]
        
        while product >= k and left <= right:
            product /= nums[left]
            left += 1
        
        count += right - left + 1
    
    return count

# Input from the user
nums = list(map(int, input().split()))
k = int(input())

result = count_subarrays(nums, k)
print(result)
 