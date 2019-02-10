"""*Maximum Subarray
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
Example:
Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Time Complexity: O(N)
Space Complexity: O(1)
*"""
class MaximumSubArray(object):
    def findmaxsub(self, nums):
        maxsofar = nums[0]
        maxendinghere = nums[0]
        for i in range(len(nums)):
            maxendinghere = max(maxendinghere+nums[i], nums[i])
            maxsofar = max(maxsofar, maxendinghere)
        return maxsofar


maxsub = MaximumSubArray()
print(maxsub.findmaxsub([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
