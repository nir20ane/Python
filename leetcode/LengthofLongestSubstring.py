"""Longest Substring Without Repeating Characters
Given a string, find the length of the longest substring without repeating characters.

Example 1:
Input: "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:
Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:
Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""
class LengthofLongestSubstring(object):
    def lengthOfLongestSubstring(self, s):
        n = len(s)
        i = 0
        ans = 0
        ldict = {}
        for j in range(n):
            if s[j] in ldict:
                i = max(ldict[s[j]], i)
            ldict[s[j]] = j+1
            ans = max(ans, j-i+1)
        return ans  # return longest substring window length

llsb = LengthofLongestSubstring()
print(llsb.lengthOfLongestSubstring("abcabcbb"))
