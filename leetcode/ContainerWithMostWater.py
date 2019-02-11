"""*Container With Most Water

Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai).
n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0).
Find two lines, which together with x-axis forms a container, such that the container contains the most water.
Note: You may not slant the container and n is at least 2.
Example:

Input: [1,8,6,2,5,4,8,3,7]
Output: 49
*"""
class ContainerWithMostWater(object):
    def maxwaterin(self, height):
        l = 0
        r = len(height) -1
        maxwater = 0
        while l < r:
            maxwater = max(maxwater, min(height[l], height[r])*(r-l))
            if height[l] < height[r]:
                l += 1
            elif height[l] == height[r]:
                l += 1
                r -= 1
            else:
                r -= 1
        return maxwater

con = ContainerWithMostWater()
print(con.maxwaterin([1, 8, 6, 2, 5, 4, 8, 3, 7]))
