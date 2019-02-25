"""* Letter Combinations of a Phone Number

* Given a string containing digits from 2-9 inclusive,
* return all possible letter combinations that the number could represent.
* A mapping of digit to letters (just like on the telephone buttons) is given below.
* Note that 1 does not map to any letters.

* Example:
* Input: "23"
* Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
*"""
class LetterCombinationsPhoneNumber(object):
    def lettercombination(self, digits):
        ans = []
        if len(digits) == 0:
            return ans
        mapping = ["0", "1", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        ans.append("")
        for i in range(len(digits)):
            x = int(digits[i])
            print i
            while len(ans[0]) == i:
                t = ans.pop(0)
                for s in mapping[x]:
                    ans.append(t+s)
        return ans
lcb = LetterCombinationsPhoneNumber()
print(lcb.lettercombination("23"))