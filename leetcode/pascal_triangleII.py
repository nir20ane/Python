"""
Given a non-negative index k where k ≤ 33, return the kth index row of the Pascal's triangle.
Note that the row index starts from 0.
In Pascal's triangle, each number is the sum of the two numbers directly above it.
Example:
Input: 3
Output: [1,3,3,1]
"""
#Method: List of List
class Pascal(object):
    def pascal(self,n):
        # create a list
        pt = []
        for i in range(n+1):
            # append a list to each value of 1
            pt.append([])
            # add 1 to start
            pt[i].append(1)
            # compute and add middle values
            for j in range(1,i):
                pt[i].append(pt[i-1][j-1]+pt[i-1][j])
            # add 1 to end if i > 0
            if i > 0:
                pt[i].append(1)
        return pt[n]
# create class object and call method
p = Pascal()
print(p.pascal(3))