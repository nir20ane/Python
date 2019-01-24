"""Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.
(i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).
You are given a target value to search. If found in the array return its index, otherwise return -1.
You may assume no duplicate exists in the array.
Your algorithm's runtime complexity must be in the order of O(log n).
Example 1:
Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
Example 2:
Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
** Approach: Use binary search
* Time Complexity - O(logn)
* Space Complexity - O(1)
*"""
class SearchinRotList(object):
    def search(self, nums, target):
        if(len(nums) < 0): return -1  # corner cases are taken care here
        if((len(nums) == 1) and (target == nums[0])): return 0
        if((len(nums) == 1) and (target != nums[0])): return -1
        left = 0
        right = len(nums) - 1
        while(left <= right):  # start binary search
            mid = left + (right-left)/2
            if(nums[mid] == target): return mid  # see if mid element is equal than target
            if(nums[left] <= nums[mid]):  # check if left element is less than mid
                if(nums[left] <= target <= nums[mid]):  # if target between left and mid
                    right = mid -1  # adjust right
                else:
                    left = mid + 1 # else adjust left

            else:
                if(nums[mid] <= target <= nums[right]):  # if target is between mid and right
                    left = mid + 1  # adjust left
                else:
                    right = mid - 1  # adjust right
        return -1

searcht = SearchinRotList()
print(searcht.search([4, 5, 6, 7, 0, 1, 2], 0))
print(searcht.search([4, 5, 6, 7, 0, 1, 2], 3))