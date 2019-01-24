"""Find Minimum in Rotated Sorted Array
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.
(i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).
Find the minimum element.
You may assume no duplicate exists in the array.
** Approach:
* Perform Binary search - return left most element
* time complexity is O(log n)
* space complexity is O(1)
"""
class SearchMinSortArray(object):
    def search(self, nums):
        if(len(nums) == 0): return -1
        if(len(nums) == 1): return nums[0]

        left = 0
        right = len(nums) - 1  # have left and right variables
        while(left < right):
            mid = left + ((right - left)/2)
            if(nums[mid] > nums[right]):  # adjust left and right based on mid and right
                left = mid+1
            else:
                right = mid
        return nums[left]  # return left most element

minsearch = SearchMinSortArray()
print(minsearch.search([4, 5, 6, 7, 0, 1, 2]))
print(minsearch.search([4, 5, 6, 7, 8, 1, 2]))
