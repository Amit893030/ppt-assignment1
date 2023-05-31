#Q1.** Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
    #You may assume that each input would have exactly one solution, and you may not use the same element twice.
    #You can return the answer in any order.
# Example:
#Input: nums = [2,7,11,15], target = 9
#Output: [0,1]
#Explanation:** Because nums[0] + nums[1] == 9, we return [0, 1][

def two_sum(nums, target):
    num_indices = {}

    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_indices:
            return [num_indices[complement], i]
        num_indices[num] = i

    return []

# Example usage:
nums = [2, 7, 11, 15]
target = 9
result = two_sum(nums, target)
print(result)



