"""Reverse Integer
Given a 32 bit signed integer, reverse digits of an integer.

Example 1
Input: 123
Output: 321

Example 2
Input: -123
Output: -321

Example 3
Input: 120
Output: 21
Note
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: -2^31 and 2^31
For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.
*/"""
class ReverseInteger(object):
    def reverse(self, x):
        negative = x<0
        reverse = 0
        x = abs(x)
        while x:
            if reverse > ((2**31 -(x%10))/10):  # check for overflow here
                return 0
            reverse = reverse*10+(x%10)
            x = x/10
        if negative:
            return -reverse
        else:
            return reverse

rev = ReverseInteger()
print rev.reverse(123)
print rev.reverse(-321)
print rev.reverse(120)
print rev.reverse(1534236469)
