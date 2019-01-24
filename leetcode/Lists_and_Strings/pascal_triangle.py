"""Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.

Example:

Input: 5
Output:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]

In Pascal's triangle, each number is the sum of the two numbers directly above it."""
# Method : using lists
class pascal_triangle(object):
    def pascal_triangle(self,n):
        #create a list
        pascal = []
        for i in range(n):
            # add  a list to each value of list
            pascal.append([])
            # add 1 to the start of the list
            pascal[i].append(1)
            # compute and add other elements to list
            for j in range(1,i):
                pascal[i].append(pascal[i-1][j-1]+pascal[i-1][j])
            #add 1 to end if i > 0
            if(i > 0):
                pascal[i].append(1)
        #return list of list
        return pascal

# create object and call method
p=pascal_triangle()
print(p.pascal_triangle(5))