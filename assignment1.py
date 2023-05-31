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

#Q2. Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.
#Consider the number of elements in nums which are not equal to val be k, to get accepted, you need to do the following things:
#Change the array nums such that the first k elements of nums contain the elements which are not equal to val. The remaining elements of nums are not important as well as the size of nums.
#Return k.
#Example :**
#Input: nums = [3,2,2,3], val = 3
#Output: 2, nums = [2,2,_*,_*]

def remove_element(nums, val):
    k = 0  # Count of elements not equal to val

    for i in range(len(nums)):
        if nums[i] != val:
            nums[k] = nums[i]
            k += 1

    return k

# Example usage:
nums = [3, 2, 2, 3]
val = 3
result = remove_element(nums, val)
print(result)
print(nums[:result])


 #Q3 Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.
#You must write an algorithm with O(log n) runtime complexity.

def search_insert(nums, target):
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = left + (right - left) // 2

        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return left

# Example usage:
nums = [1, 3, 5, 6]
target = 5
result = search_insert(nums, target)
print(result)  # Output: 2

target = 2
result = search_insert(nums, target)
print(result)

target = 7
result = search_insert(nums, target)
print(result)

#Q4You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.
#Increment the large integer by one and return the resulting array of digits.
 print("dobut")

#Q5.you are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.
#Merge nums1 and nums2 into a single array sorted in non-decreasing order.
#The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

def merge(nums1, m, nums2, n):
    # Initialize pointers for nums1, nums2, and the merged array
    i = m - 1
    j = n - 1
    k = m + n - 1

    # Merge the arrays from right to left
    while i >= 0 and j >= 0:
        if nums1[i] >= nums2[j]:
            nums1[k] = nums1[i]
            i -= 1
        else:
            nums1[k] = nums2[j]
            j -= 1
        k -= 1

    # If there are remaining elements in nums2, copy them to nums1
    while j >= 0:
        nums1[k] = nums2[j]
        j -= 1
        k -= 1

# Example usage:
nums1 = [1, 2, 3, 0, 0, 0]
m = 3
nums2 = [2, 5, 6]
n = 3
merge(nums1, m, nums2, n)
print(nums1)


#Q6.Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
#Example 1:**
#Input: nums = [1,2,3,1]
#Output: true

def contains_duplicate(nums):
    seen = set()

    for num in nums:
        if num in seen:
            return True
        seen.add(num)

    return False

# Example usage:
nums = [1, 2, 3, 1]
result = contains_duplicate(nums)
print(result)

#Q7.Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the nonzero elements.
#Note that you must do this in-place without making a copy of the array.
#Example 1:
#Input: nums = [0,1,0,3,12]
#Output: [1,3,12,0,0]


def move_zeroes(nums):
    # Initialize a pointer to keep track of the position to place the next non-zero element
    next_non_zero_pos = 0

    # Iterate through the array
    for i in range(len(nums)):
        # If the current element is non-zero, move it to the next_non_zero_pos position
        if nums[i] != 0:
            nums[next_non_zero_pos] = nums[i]
            next_non_zero_pos += 1

    # Fill the remaining positions from next_non_zero_pos to the end with zeros
    for i in range(next_non_zero_pos, len(nums)):
        nums[i] = 0

# Example usage:
nums = [0, 1, 0, 3, 12]
move_zeroes(nums)
print(nums)


#Q8. You have a set of integers s, which originally contains all the numbers from 1 to n. Unfortunately, due to some error, one of the numbers in s got duplicated to another number in the set, which results in repetition of one number and loss of another number.
#You are given an integer array nums representing the data status of this set after the error.
#Find the number that occurs twice and the number that is missing and return them in the form of an array.
#Example 1:**
#Input: nums = [1,2,2,4]
#Output: [2,3]

def find_error_nums(nums):
    n = len(nums)
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(nums)
    num_set = set()
    duplicate_num = None

    for num in nums:
        if num in num_set:
            duplicate_num = num
        num_set.add(num)

    missing_num = expected_sum - actual_sum + duplicate_num

    return [duplicate_num, missing_num]

# Example :
nums = [1, 2, 2, 4]
result = find_error_nums(nums)
print(result)
