"""The count-and-say sequence is the sequence of integers with the first five terms as following:
1.     1
2.     11
3.     21
4.     1211
5.     111221
1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.
Given an integer n, generate the nth term of the count-and-say sequence.
Note: Each term of the sequence of integers will be represented as a string.
Example 1:
Input: 1
Output: "1"
Example 2:
Input: 4
Output: "1211" """
#Approach 1: keep track of prev_string, prev_char and number of repeats
class count_and_say(object):
    def count_and_say(self,n):
        if n==0 or n==1:
            return '1'
        prev_string = self.count_and_say(n-1)
        prev_char = prev_string[0]
        results_str=""
        no_of_repeats=0
        curr_char=""
        for i in range(0,len(prev_string)):
            curr_char = prev_string[i]

            if curr_char == prev_char:
                no_of_repeats += 1
            if curr_char != prev_char:
                results_str += str(no_of_repeats)+prev_char
                prev_char=curr_char
                no_of_repeats=1
        results_str+=str(no_of_repeats)+curr_char
        return results_str

cs=count_and_say()
print(cs.count_and_say(4))