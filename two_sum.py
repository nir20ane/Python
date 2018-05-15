"""Given an array of integers, return indices of the two numbers such that they add up to a specific target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
Example:
Given nums = [2, 7, 11, 15], target = 9,
Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1]."""
#Approach1: Use dict to store index of the number as value. if num is already a key in dict return index of target-num and num
class two_sum(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dict = {}
        for i in range(len(nums)):
            if target-nums[i] in dict:
                return [dict[target-nums[i]], i]
            else:
                dict[nums[i]] = i
t= two_sum()
print(t.twoSum([2,7,11,15],9))