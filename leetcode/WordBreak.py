"""
 * 139. Word Break
 * Given a non-empty string s and a dictionary wordDict containing a list of non-empty words,
 * determine if s can be segmented into a space-separated sequence of one or more dictionary words.
 * Note:
 * The same word in the dictionary may be reused multiple times in the segmentation.
 * You may assume the dictionary does not contain duplicate words.
 * Example 1:
 * Input: s = "leetcode", wordDict = ["leet", "code"]
 * Output: true
 * Explanation: Return true because "leetcode" can be segmented as "leet code".
 * Example 2:
 * Input: s = "applepenapple", wordDict = ["apple", "pen"]
 * Output: true
 * Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
 *  Note that you are allowed to reuse a dictionary word.
 * Example 3:
 * Input: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
 * Output: false
"""
class WordBreak(object):
    def wordbreak(self, str, strlst):
        setw = set(strlst)
        dp = [True] + [False]*len(str)
        for i in range(1, len(str)+1):
            for j in range(0, i):
                if dp[j] and str[j:i] in setw:
                    dp[i] = True
        return dp[len(str)]

wb = WordBreak()
print(wb.wordbreak("leetcode", ["leet", "code"]))
print(wb.wordbreak("applepenapple", ["apple", "pen"]))
print(wb.wordbreak("catsandog", ["cats", "dog", "sand", "and", "cat"]))
