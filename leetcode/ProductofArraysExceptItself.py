"""Product of Array Except Self

Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].
Example:
Input:  [1,2,3,4]
Output: [24,12,8,6]
Note: Please solve it without division and in O(n).
Follow up:
Could you solve it with constant space complexity? (The output array does not count as extra space for the purpose of space complexity analysis.)
# Time Complexity: O(N)
# Space Complexity: O(N) if result array is considered, else O(1)
"""
class ProductofArraysExceptItself(object):
    def product(self, nums):
        n = len(nums)
        res = [1]*n  # result array with 1 as intial vlues
        left = 1
        right = 1

        for i in range(n):
            res[i] *= left
            left *= nums[i]  # left side product

        for i in range(n-1, -1, -1):
            res[i] *= right   # right side product
            right *= nums[i]  # left side product*right side product gives intended result

        return res

prod = ProductofArraysExceptItself()
print(prod.product([1, 2, 3, 4]))
