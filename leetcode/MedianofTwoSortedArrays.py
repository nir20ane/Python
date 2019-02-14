"""*4. Median of Two Sorted Arrays

There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

You may assume nums1 and nums2 cannot be both empty.

Example 1:
nums1 = [1, 3]
nums2 = [2]
The median is 2.0

Example 2:
nums1 = [1, 2]
nums2 = [3, 4]
The median is (2 + 3)/2 = 2.5
* """
class MedianofTwoSortedArrays(object):
    def median(self, nums1, nums2):
         m = len(nums1)
         n = len(nums2)
         if m > n:
             nums1, nums2, m , n = nums2, nums1, n, m
         if n == 0:
             raise ValueError

         imin = 0
         imax = m
         halflen = (m+n+1)/2

         while imin <= imax:
             i = (imin+imax)/2
             j = halflen - i
             if i<m and (nums2[j-1] > nums1[i]):
                 imin = i+1
             elif i>0 and (nums1[i-1] > nums2[j]):
                 imax = i-1
             else:
                 if i == 0:
                     maxleft = nums2[j-1]
                 elif j == 0:
                     maxleft = nums1[i-1]
                 else:
                     maxleft = max(nums2[j-1], nums1[i-1])

                 if (m+n)%2 == 1:
                     return maxleft
                 if i == m:
                     minright = nums2[j]
                 elif j == n:
                     minright = nums1[i]
                 else:
                     minright = min(nums2[j], nums1[i])
                 return (minright+maxleft)/2.0

med = MedianofTwoSortedArrays()
print(med.median([1, 3], [2]))
