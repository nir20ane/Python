"""
The Hamming distance between two integers is the number of positions at which the corresponding bits are different.
Given two integers x and y, calculate the Hamming distance.
Note:
0 ≤ x, y < 231.
Example:
Input: x = 1, y = 4
Output: 2
Explanation:
1   (0 0 0 1)
4   (0 1 0 0)
       ↑   ↑
The above arrows point to positions where the corresponding bits are different.
"""
# Approach 1: Use XOR function to get the diff and use diff to get no of positions at which the corresponding bits are different.
class hamming_distance(object):
    def hamming_distance(self,x,y):
        diff = x^y
        count = 0
        while(diff!=0):
            diff = diff&(diff-1)
            count += 1
        return count
hd = hamming_distance()
print(hd.hamming_distance(1,4))
