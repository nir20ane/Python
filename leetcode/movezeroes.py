"""Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Example:

Input: [0,1,0,3,12]
Output: [1,3,12,0,0]
Note:

You must do this in-place without making a copy of the array.
Minimize the total number of operations."""

# 1 Approach - Use Count and Remove List methods in python - number of operations are more
"""
class movezeroes(object):
    def movezeroes(self,lst):
        zero_count = lst.count(0)
        while 0 in lst:
            lst.remove(0)
        for i in range(0,zero_count):
            lst.append(0)
        return lst
"""
# 2 Approach - Keep track of last non zero index, move non zero elements and add zeroes at the end - number of operations are still more
"""
class movezeroes(object):
    def movezeroes(self,lst):
        last_non_zero_index=0
        for i in range(0,len(lst)):
            if lst[i] != 0:
                lst[last_non_zero_index] = lst[i]
                last_non_zero_index += 1
        for i in range(last_non_zero_index,len(lst)):
            lst[i] = 0
        return lst
"""
# 3 Approach - Swap non zero and zero elements using two pointer technique
class movezeroes(object):
    def movezeroes(self,lst):
        j=0
        for i in range(0,len(lst)):
            if lst[i] != 0:
                lst[j],lst[i] = lst[i],lst[j]
                j+=1
        return lst

m = movezeroes()
print(m.movezeroes([2,0,0,0,2,1]))

