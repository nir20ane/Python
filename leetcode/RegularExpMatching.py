"""Regular Expression Matching

Given an input string (s) and a pattern (p), implement regular expression matching with support for '.' and '*'.

'.' Matches any single character.
'*' Matches zero or more of the preceding element.
The matching should cover the entire input string (not partial).

Note:

s could be empty and contains only lowercase letters a-z.
p could be empty and contains only lowercase letters a-z, and characters like . or *.
Example 1:

Input:
s = "aa"
p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".
Example 2:

Input:
s = "aa"
p = "a*"
Output: true
Explanation: '*' means zero or more of the precedeng element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".
Example 3:

Input:
s = "ab"
p = ".*"
Output: true
Explanation: ".*" means "zero or more (*) of any character (.)".
Example 4:

Input:
s = "aab"
p = "c*a*b"
Output: true
Explanation: c can be repeated 0 times, a can be repeated 1 time. Therefore it matches "aab".
Example 5:

Input:
s = "mississippi"
p = "mis*is*p*."
Output: false
*"""
class RegularExpMatching(object):
    def isMatch(self, s, p):
        if p is None or s is None:
            return False
        if len(p) == 0:
            return len(p) == len(s)

        p = "+"+p
        s = "+"+s
        plen = len(p)
        slen = len(s)

        dp = [[False] * plen for _ in range(slen)]
        dp[0][0] = True
        for j in range(1, plen):
            if p[j] == '*':
                dp[0][j] = dp[0][j-2]

        for i in range(1, slen):
            for j in range(1, plen):
                # Case 1: direct character match
                if (s[i] == p[j]) or (p[j] == '*'):
                    dp[i][j] = dp[i-1][j-1]

                if p[j] == "*":
                    # Case 2: character directly behind star doesn't match, skip
                    if s[i] != p[j-1] and p[j-1] != ".":
                        dp[i][j] = dp[i][j-2]
                    # Extend out character before *
                    else:
                        # dp[i][j - 1]: If character before * appears once
                        # dp[i - 1][j]: If character before * appears more than once
                        # dp[i][j - 2]: If skip is necessary to match(even if c matches)
                        dp[i][j] = dp[i][j-1] or dp[i-1][j] or dp[i][j-2]

        return dp[slen-1][plen-1]

reg = RegularExpMatching()
print(reg.isMatch("aa", "a"))
print(reg.isMatch("aa", "a*"))
print(reg.isMatch("ab", ".*"))
print(reg.isMatch("aab", "c*a*b"))
print(reg.isMatch("mississippi", "mis*is*p*."))
