"""Trapping Rain Water
Share
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.
The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.
 Thanks Marcos for contributing this image!
Example:
Input: [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Time Complexity; O(n)
Space Complexity: O(1)
"""
class TrappingRainWater(object):
    def tarppedrain(self, arr):
        rainmax = 0
        a = 0
        b = len(arr) -1
        lmax = 0
        rmax = 0
        while a <= b:
            lmax = max(lmax, arr[a])
            rmax = max(rmax, arr[b])  # calc lmax and rmax
            if lmax < rmax:
                rainmax += lmax - arr[a]  # calc rain based on lower value - important
                a += 1
            else:
                rainmax += rmax - arr[b]
                b -= 1
        return rainmax  # return rain water

trap = TrappingRainWater()
print(trap.tarppedrain([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
