"""/** We are given two strings, A and B.
A shift on A consists of taking string A and moving the leftmost character to the rightmost position. For example, if A = 'abcde', then it will be 'bcdea' after one shift on A. Return True if and only if A can become B after some number of shifts on A.
Example 1:
Input: A = 'abcde', B = 'cdeab'
Output: true
Example 2:
Input: A = 'abcde', B = 'abced'
Output: false
Note:
** Concatenate string str1+str1 and check if str2 is in str1
* Time Complexity - O(n^2)
* Space Complexity - O(n) - since we concatenate two strings
*/"""

class RotateString(object):
    def stringRotation(self, A, B):
        return len(A) == len(B) and B in A+A

strrot = RotateString()
print(strrot.stringRotation("bata", "taba"))
print(strrot.stringRotation("bata", "tabe"))
