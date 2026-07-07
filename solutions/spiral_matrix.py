# Question number: 54
# Level: medium
# Author: Naama Tzadok
# Date: Jul 07, 2026 09:27


from typing import List
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        left = 0 
        right = len(matrix[0])
        top = 0
        bottom = len(matrix)
        while True:
            for i in range(left, right):
                res.append(matrix[top][i])
            top += 1
            if top >= bottom:
                break
            
            right -= 1
            for i in range(top, bottom):
                res.append(matrix[i][right])
            
            if right <= left:
                break
            
            bottom -= 1
            for i in range(right - 1, left - 1, -1):
                res.append(matrix[bottom][i])
            
            if top >= bottom:
                break
            
            for i in range(bottom - 1, top - 1, -1):
                res.append(matrix[i][left])
            left += 1
            if right <= left:
                break
                
        return res

# Time Complexity: O(n*m)
# Space Complexity: O(1)

