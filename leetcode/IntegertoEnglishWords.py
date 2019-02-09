""""* Integer to English Words
Convert a non-negative integer to its english words representation. Given input is guaranteed to be less than 231 - 1.

Example 1:
Input: 123
Output: "One Hundred Twenty Three"
Example 2:

Input: 12345
Output: "Twelve Thousand Three Hundred Forty Five"
Example 3:

Input: 1234567
Output: "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"
Example 4:

Input: 1234567891
Output: "One Billion Two Hundred Thirty Four Million Five Hundred Sixty Seven Thousand Eight Hundred Ninety One"
*"""
class IntegertoEnglishWords(object):
    def __init__(self):
        self.lessthan20 = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Eleven", "Twelve",
                  "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]

        self.tens = ["", "Ten", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
        self.thousands = ["", "Thousand", "Million", "Billion"]

    def inttroengwords(self, num):
        if num == 0:
            return "Zero"
        words = ""
        i = 0
        while num > 0:
            if num%1000 != 0:
                words = self.helper(num%1000) + " " + self.thousands[i]+ " " + words
            num = num/1000
            i += 1
        return words

    def helper(self, num):
        if num == 0:
            return
        elif num < 20:
            return self.lessthan20[num] + ""
        elif num < 100:
            return self.tens[num/10] + " " + self.helper(num%10)
        else:
            return self.lessthan20[num/100]+" Hundred " + self.helper(num%100)

inttoeng = IntegertoEnglishWords()
print(inttoeng.inttroengwords(1234567891))
print(inttoeng.inttroengwords(123))
print(inttoeng.inttroengwords(123456))
print(inttoeng.inttroengwords(1234567))
