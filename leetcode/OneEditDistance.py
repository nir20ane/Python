"""
Given two strings s and t, determine if they are both one edit distance apart.
Note:
There are 3 possiblities to satisify one edit distance apart:
Insert a character into s to get t
Delete a character from s to get t
Replace a character of s to get t
Example 1:
Input: s = "ab", t = "acb"
Output: true
Explanation: We can insert 'c' into s to get t.
Example 2:
Input: s = "cab", t = "ad"
Output: false
Explanation: We cannot get t from s by only one step.
Example 3:
Input: s = "1203", t = "1213"
Output: true
Explanation: We can replace '0' with '1' to get t.
* Approach - increase count if there is a mismatch in character or length
* increase index 1 if string1 length is more and index 2 if string 2 length is more
* Time Complexity : O(n); Space Complexity: O(1)
"""
class OneEditDistance(object):
    def oneEditDistance(self, str1, str2):
        len1 = len(str1)
        len2 = len(str2)
        index1 = 0
        index2 = 0
        count = 0
        if(abs(len1 - len2) > 1): return False
        while((index1 < len1) & (index2 < len2)):
            if(str1[index1] != str2[index2]):
                if(count == 1): return False
                if(len1 < len2): index2 += 1
                elif(len1 > len2): index1 += 1
                else:
                    index1 += 1
                    index2 += 1
                count += 1
            else:
                index1 += 1
                index2 += 1
        if((index1 < len1) | (index2 < len2)): count+= 1
        return count == 1

one = OneEditDistance()
print(one.oneEditDistance("pale", "bale"))
print(one.oneEditDistance("ale", "bale"))
print(one.oneEditDistance("ale", "ala"))
print(one.oneEditDistance("ale", "aleee"))
print(one.oneEditDistance("ale", "ale"))