""""*Longest Palindromic Substring
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.
Example 1:
Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:
Input: "cbbd"
Output: "bb"
*"""
class LongestPalindromicSubstring(object):
    def longpalindrome(self, s):
        if len(s) < 2: return s
        n = len(s)
        start = 0
        end = 0
        for j in range(n):
            len1 = self.expand(s, j, j)
            len2 = self.expand(s, j, j+1)
            slen = max(len1, len2)
            if slen > end-start:
                start = j-((slen-1)/2)
                end = j+(slen/2)
        return s[start:end+1]

    def expand(self, s, L, R):
        while L >= 0 and R < len(s) and s[L] == s[R]:
            L -= 1
            R += 1
        return R-L-1

longpal = LongestPalindromicSubstring();
print(longpal.longpalindrome("cbbd"))
