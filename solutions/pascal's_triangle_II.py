# Question number: 119
# Level: easy
# Author: Naama Tzadok
# Date: Apr 14, 2026 11:57

from typing import List
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        row = [1]
        for i in range(1, rowIndex+1):
            if i == rowIndex: 
                row.append(1)
                break
            row.append(int(row[-1]* (rowIndex-i+1)/i))
        return row
      
# Time Complexity: O(k)
# Space Complexity: O(k)