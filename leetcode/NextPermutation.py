"""
Next Permutation
* Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.
* If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order)
* The replacement must be in-place and use only constant extra memory.
* Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column
1,2,3 -> 1,3,2
3,2,1 -> 1,2,3
1,1,5 -> 1,5,1
"""
class NextPermutation(object):
    def nextpermutation(self, nums):
        if len(nums) == 0 or nums is None:
            return
        for i in range(len(nums)-2, -1, -1):
            if nums[i] < nums[i+1]:
                for k in range(len(nums)-1, i, -1):
                    if nums[i] < nums[k]:
                        nums[k], nums[i] = nums[i], nums[k]
                        break
                self.reverse(nums, i+1, len(nums)-1)
                return nums
        self.reverse(nums, 0, len(nums)-1)
        return nums

    def reverse(self, nums, start, end):
        i = start
        j = end
        while i <= j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1

np = NextPermutation()
print(np.nextpermutation([6, 2, 1, 5, 4, 3, 0]))
