"""*Given an array num of n integers, are there elements a, b, c in nums such that a + b + c = 0?
Find all unique triplets in the array which gives the sum of zero.

Note:
The solution set must not contain duplicate triplets.
Example:
Given array num = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
*"""
class ThreeSum(object):
    def threesum(self, num):
        if len(num) < 3:
            return
        res = []
        num.sort()
        for i in range(len(num)-2):
            if i>0 and num[i] == num[i-1]:
                continue
            j = i+1
            k = len(num)-1
            target = -num[i]
            while j < k:
                if num[j] + num[k] == target:
                    res.append([num[j], num[k], num[i]])
                    j += 1
                    k -= 1
                    while j < k and num[j] == num[j-1]:
                        j += 1
                    while j < k and num[k] == num[k-1]:
                        k -= 1
                elif num[j] + num[k] > target:
                    k -= 1
                else:
                    j += 1
        return res

ts = ThreeSum()
print(ts.threesum([-1, 0, 1, 2, -1, -4]))

