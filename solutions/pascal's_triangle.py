# Question number: 118
# Level: easy
# Author: Naama Tzadok
# Date: submitted at May 24, 2026 10:50

from typing import List
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res_triangle = []
        for numRow in range(numRows):
            row = [1]
            for i in range(numRow):
                prev_row = res_triangle[-1]
                if i + 1 == numRow:
                    row.append(1)
                else:
                    row.append(prev_row[i] + prev_row[i+1])
            res_triangle.append(row)
        return res_triangle

# Time Complexity: O(n^2)
# Space Complexity: O(n^2)