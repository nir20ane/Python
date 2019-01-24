"""* Search in Rotated Sorted Array II
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.
(i.e., [0,0,1,2,2,5,6] might become [2,5,6,0,0,1,2]).
You are given a target value to search. If found in the array return true, otherwise return false.

Example 1:

Input: nums = [2,5,6,0,0,1,2], target = 0
Output: true
Example 2:

Input: nums = [2,5,6,0,0,1,2], target = 3
Output: false
Follow up:
This is a follow up problem to Search in Rotated Sorted Array, where nums may contain duplicates.
Would this affect the run-time complexity? How and why?
** Approach: Calculate pivot, Split into two halves based on pivot, and do binary search on two halves
* return their boolean || results
* Time Complexity is O(log n), Space Complexity is O(1)
*"""

class SortRotList2(object):
    def search(self, nums, target):
        if(len(nums) < 0): return False
        if((len(nums)==0) and (nums[0] == target)): return True
        if((len(nums)==0) and (nums[0] != target)): return True  # corner cases are taken care here

        pivot = None

        for i in range(len(nums)):
            if(nums[i] > nums[i+1]):  # calculate pivot, point where array is rotated
                pivot = i
                break

        if(nums[pivot] == target): return True
        else:
            left = self.binsearch(nums, 0, pivot, target)  # do binary search on two halves - 0 to pivot, pivot + 1 to length of list
            right = self.binsearch(nums, pivot+1, len(nums), target)
            return left or right  # return II of two boolean results

    def binsearch(self, nums, start, end, target):
        while start < end:
            mid = start + (end-start)/2
            if(nums[mid] == target): return True
            elif(nums[mid] < target): start = mid+1
            else: end = mid -1
        return False


sortrot = SortRotListII()
print(sortrot.search([2, 5, 6, 0, 0, 1, 2], 0))
print(sortrot.search([2, 5, 6, 0, 0, 1, 2], 3))