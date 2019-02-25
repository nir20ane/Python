"""* Palindrome Number
* Determine whether an integer is a palindrome.
* An integer is a palindrome when it reads the same backward as forward.

* Example 1:
* Input: 121
* Output: true
* Example 2:
* Input: -121
* Output: false
* Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
* Example 3:
* Input: 10
* Output: false
* Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
* Reverse the number first and check if it is equal to original number
* """
class PalindromeNumber(object):
    def palindromenum(self, num):
        if num < 0: return False
        if num == 0: return True
        if num % 10 == 0: return False
        y = num
        rev = 0
        while y != 0:
            rev = rev*10+ y%10
            y = y/10
        return rev == num

pn = PalindromeNumber()
print(pn.palindromenum(121))
print(pn.palindromenum(10))
