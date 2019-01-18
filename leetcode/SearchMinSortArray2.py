"""Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.
(i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).
Find the minimum element.
The array may contain duplicates.
Example 1:
Input: [1,3,5]
Output: 1
Example 2:
Input: [2,2,2,0,1]
Output: 0
Note:
This is a follow up problem to Find Minimum in Rotated Sorted Array.
Would allow duplicates affect the run-time complexity? How and why?
** Approach: Use Binary Search
***** when mid == high, we don't know if minimum is in mid's left or right, so reduce right by one
"""
class SearchMinSortArray2(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if (len(nums) == 0): return -1
        if (len(nums) == 1): return nums[0]  # corner cases are taken care

        left = 0
        right = len(nums) - 1  # initialise left and right values
        while left <= right:
            mid = left + (right - left)/2
            if nums[mid] > nums[right]:  # minimum is on right side, shift left to mid+1
                left = mid+1
            elif nums[mid] < nums[right]:  # minimum is on left side, shift right to mid
                right = mid
            else:
                right = right - 1  # mid == high, we don't know if minimum is in mid's left or right, so reduce right by one
        return nums[left]


searchrot = SearchMinSortArray2()
print(searchrot.findMin([2, 2, 2, 0, 1]))
print(searchrot.findMin([1, 3, 5]))
