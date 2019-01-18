"""Given an array, rotate the array to the right by k steps, where k is non-negative.

Example 1:
Input: [1,2,3,4,5,6,7] and k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]
Example 2:
Input: [-1,-100,3,99] and k = 2
Output: [3,99,-1,-100]
Explanation: 
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]
*** Approach: reverse the array first, then reverse 0, k-1, then reverse k to end of array
* Time Complexity - O(n)
* Space Complexity - O(1)
"""
class RotateArray(object):
    def rotate(self, nums, k):
        self.reverse(nums, 0, len(nums)-1)  # reverse the entire list
        self.reverse(nums, 0, k-1)  # reverse from 0 to k-1
        self.reverse(nums, k, len(nums)-1)  # reverse from k to end of list
        print(nums)  # print list

    def reverse(self, nums, start, end):  # reverse method
        while(start < end):
            temp = nums[start]
            nums[start] = nums[end]
            nums[end] = temp
            start += 1
            end -= 1

rot = RotateArray()
rot.rotate([-1, -100, 3, 99], 2)
rot.rotate([1, 2, 3, 4, 5, 6, 7], 3)