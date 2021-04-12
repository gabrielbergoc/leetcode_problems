# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
#
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
#
# You can return the answer in any order.

# https://leetcode.com/problems/two-sum/

# Runtime: 48 ms
# Memory Usage: 14.4 MB

class Solution:
    def twoSum(self, nums, target: int):
        for i in range(len(nums) - 1):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return None


nums = [2, 7, 11, 15]
target = 9
s = Solution()
print(s.twoSum(nums, target))

nums = [3, 2, 4]
target = 6
s = Solution()
print(s.twoSum(nums, target))

nums = [3, 3]
target = 6
s = Solution()
print(s.twoSum(nums, target))