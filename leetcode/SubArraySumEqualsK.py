"""* 560. Subarray Sum Equals K
Given an array of integers and an integer k, you need to find the total number of continuous subarrays whose sum equals to k.
Example 1:
Input:nums = [1,1,1], k = 2
Output: 2
Note:
The length of the array is in range [1, 20,000].
The range of numbers in the array is [-1000, 1000] and the range of the integer k is [-1e7, 1e7].
*"""
class SubArraySumEquals(object):
    def subarraysum(self, nums, k):
        map = {}
        map[0] = 1
        count = 0
        sum = 0
        for i in range(len(nums)):
            sum += nums[i]
            if sum-k in map:
                count += map[sum-k]
            if sum in map:
                map[sum] += 1
            else:
                map[sum] = 1
        return count

sub = SubArraySumEquals()
print(sub.subarraysum([1, 1, 1], 2))
