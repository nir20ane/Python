"""
* You are given an n x n 2D matrix representing an image.
* Rotate the image by 90 degrees (clockwise).
* You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.
* Example 1:
Given input matrix = 
[
  [1,2,3],
  [4,5,6],
  [7,8,9]
],
rotate the input matrix in-place such that it becomes:
[
  [7,4,1],
  [8,5,2],
  [9,6,3]
]
* Example 2:
Given input matrix =
[
  [ 5, 1, 9,11],
  [ 2, 4, 8,10],
  [13, 3, 6, 7],
  [15,14,12,16]
], 
rotate the input matrix in-place such that it becomes:
[
  [15,13, 2, 5],
  [14, 3, 4, 1],
  [12, 6, 8, 9],
  [16, 7,10,11]
]
** Approach:
* for i = 0 to n
* variable temp = top[i];
* top[i] = left[i]
* left[i] = bottom[i]
* bottom[i] = right[i]
* right[i] = temp
* Time Complexity: O(n^2); Space Complexity O(1)
"""
class RotateImage(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for i in range(n / 2):
            if n == 0 or (len(matrix[0]) < n): break # break if invalid matrix
            first = i # break first and last
            last = n - i - 1
            for j in range(first, last):
                offset = j - first  # calculate offset
                top = matrix[first][j];
                matrix[first][j] = matrix[last - offset][first]  # left to top
                matrix[last - offset][first] = matrix[last][last - offset] # bottom to left
                matrix[last][last - offset] = matrix[j][last]  # right to bottom
                matrix[j][last] = top  # top to right
        return matrix

rot = RotateImage();
matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(matrix)
print(rot.rotate(matrix))