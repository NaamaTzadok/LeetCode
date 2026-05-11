# Question number: 89
# Level: medium
# Author: Naama Tzadok
# Date: Nov 19, 2025 12:13

from typing import List
class Solution:
    def grayCode(self, n: int) -> List[int]:
        m = 2 ** n
        res = []
        for i in range(m):
            res.append(i ^ (i >> 1))
        return res
            
            
# Time Complexity: O(2^n)
# Space Complexity: O(1)