"""Given a string, determine if a permutation of the string could form a palindrome.

Example 1:

Input: "code"
Output: false
Example 2:

Input: "aab"
Output: true
Example 3:

Input: "carerac"
Output: true"""
class CanPermutePalindrome(object):
    def canpermutepalindrome(self, str):
        map = [0]*128
        count = 0
        for i in range(0, len(str)):
            map[ord(str[i])] += 1
            if (map[ord(str[i])] % 2) == 0: count -= 1
            else: count = count+ 1
        return count <= 1

perpan = CanPermutePalindrome()
print(perpan.canpermutepalindrome("madam"))
print(perpan.canpermutepalindrome("madams"))