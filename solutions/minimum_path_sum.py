# Question number: 64
# Level: medium
# Author: Naama Tzadok
# Date: Jun 09, 2026 13:46

#################
# Naive Solution:
###################
 
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        n = len(grid) - 1
        m = len(grid[0]) - 1
        def path(row, col):
            if row == n and col == m:
                return grid[row][col]
            if row == n:
                return grid[row][col] + path(row, col+1)
            if col == m:
                return grid[row][col] + path(row+1, col)
            return grid[row][col] + min(path(row+1, col), path(row, col+1))
        return path(0,0)   

# Time Complexity: O(2^(n+m))
# Space Complexity: O(n+m)

###################
# smarter Solution:
#####################  

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        min_paths = [[0]*m for _ in range(n)]
        min_paths[0][0] = grid[0][0]
        for row_index in range(n):
            for col_index in range(m):
                if row_index == col_index == 0:
                    continue
                if row_index == 0:
                    up = float("inf") 
                else:
                    up = min_paths[row_index-1][col_index]
                if col_index == 0:
                    left = float("inf")  
                else:
                    left = min_paths[row_index][col_index-1]
                min_paths[row_index][col_index] = grid[row_index][col_index] + min(up, left)
                
        return min_paths[n-1][m-1]

# Time Complexity: O(n+m)
# Space Complexity: O(n+m)
