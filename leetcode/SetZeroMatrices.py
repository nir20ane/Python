"""
*** Set Zero Matrices ***
Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in-place.
Example 1:
Input:
[
  [1,1,1],
  [1,0,1],
  [1,1,1]
]
Output:
[
  [1,0,1],
  [0,0,0],
  [1,0,1]
]
Example 2:
Input:
[
  [0,1,2,0],
  [3,4,5,2],
  [1,3,1,5]
]
Output:
[
  [0,0,0,0],
  [0,4,5,0],
  [0,3,1,0]
]
* Approach:
* Use boolean values to keep track of 0's in 0th row and column
* use 0th row and 0th column to keep track of 0's elsewhere
* nullify rows and column based on the 0th row and column values
* nullify 0th row and column if there booleans are True
* Time Complexity: O(n^2)
* Space Complexity: O(1)
*/
"""
class SetZeromatrices(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        rowhaszero = False
        columnhaszero = False  # use boolean values to 0th row or column has zero
        for j in range(len(matrix[0])):
            if matrix[0][j] == 0:
                rowhaszero = True  # update boolean row 0

        for i in range(len(matrix)):
            if matrix[i][0] == 0:
                columnhaszero = True  # update boolean column 0

        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[i][j] == 0:  # iterate from 1 to matrix length, ans use row 0 and column 0 to keep track of zeroes
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        for i in range(1, len(matrix)):
            if matrix[i][0] == 0:
                self.rowzero(matrix, i)  # if a row has 0, nullify row

        for j in range(1, len(matrix[0])):
            if matrix[0][j] == 0:
                self.columnzero(matrix, j)  # if a column has 0, nullify column

        if rowhaszero: self.rowzero(matrix, 0)  # nullify row 0 if it has 0 value

        if columnhaszero: self.columnzero(matrix, 0)  # nullify column 0 if it has 0 value

        return matrix

    def rowzero(self, matrix, row):
        for j in range(len(matrix[0])):
            matrix[row][j] = 0

    def columnzero(self, matrix, column):
        for i in range(len(matrix)):
            matrix[i][column] = 0

setmat = SetZeromatrices()
matrix = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
print(setmat.setZeroes(matrix))