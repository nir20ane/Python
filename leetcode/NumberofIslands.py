"""* Number of Islands
Given a 2d grid map of '1's (land) and '0's (water), count the number of islands.
An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.
You may assume all four edges of the grid are all surrounded by water.
Example 1:
Input:
11110
11010
11000
00000
Output: 1
Example 2:
Input:
11000
11000
00100
00011
Output: 3
** Approach: when you get a value 1, go and visit all nearby nodes, and mark then as 0,
* increment count when no other nearby node is 1
* Time Complexity: O(m*n) = where m is rows and n is columns
* Space COmplexity: O(1)
* """

class NumberofIslands(object):
    def __init__(self):
        self.n = 0
        self.m = 0
        self.count = 0

    def islands(self, grid):
        if len(grid) == 0:
            return 0
        self.n = len(grid)
        self.m = len(grid[0])
        for i in range(self.n):
            for j in range(self.m):
                if grid[i][j] == 1:
                    self.shrink(grid, i, j)
                    self.count += 1
        return self.count

    def shrink(self, grid, x, y):
        if x < 0 or y < 0 or x >= self.n or y >= self.m or grid[x][y] != 1:
            return
        else:
            grid[x][y] = 0
            self.shrink(grid, x+1, y)
            self.shrink(grid, x-1, y)
            self.shrink(grid, x, y+1)
            self.shrink(grid, x, y-1)

cnt = NumberofIslands()
grid = [[1, 1, 1, 1, 0], [1, 1, 0, 1, 0], [1, 1, 0, 0, 0], [0, 0, 0, 0, 1]]
print(cnt.islands(grid))
