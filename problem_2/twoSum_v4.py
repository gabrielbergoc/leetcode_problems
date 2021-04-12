# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
#
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
#
# You can return the answer in any order.

# https://leetcode.com/problems/two-sum/

# WRONG SOLUTION
class Solution:
    def twoSum(self, nums: list, target: int):
        i = 0
        j = len(nums) - 1

        while i < j:
            if nums[i] + nums[j] == target:
                return [i, j]
            elif nums[i] + nums[j] > target:
                j -= 1
            else:
                i += 1

        return False


print()
print('Testing: [2, 7, 11, 15], 9')
print('Expected: [0, 1]')
print('Answer:', str(Solution().twoSum([2, 7, 11, 15], 9)))
print()

print('Testing: [1, 2, 3, 4], 6')
print('Expected: [1, 3]')
print('Answer:', str(Solution().twoSum([1, 2, 3, 4], 6)))
print()

print('Testing: [3, 3], 6')
print('Expected: [0, 1]')
print('Answer:', str(Solution().twoSum([3, 3], 6)))
print()

print('Testing: [2, 3], 6')
print('Expected: False')
print('Answer:', str(Solution().twoSum([2, 3], 6)))
print()

print('Testing: [], 6')
print('Expected: False')
print('Answer:', str(Solution().twoSum([], 6)))
print()

print('Testing: [3, 3, 4, 5, 6, 10], 17')
print('Expected: False')
print('Answer:', str(Solution().twoSum([3, 3, 4, 5, 6, 10], 17)))
print()

print('Testing: [1, 2, 3, 3, 5], 1')
print('Expected: False')
print('Answer:', str(Solution().twoSum([1, 2, 3, 3, 5], 1)))
print()