# Question number: 121
# Level: easy
# Author: Naama Tzadok
# Date: Nov 06, 2025 15:15

from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minimum = float('inf')
        res = 0
        for p in prices:
            minimum = min(minimum, p)
            res = max(res, p - minimum)
        
        return res
      
# Time Complexity: O(n)
# Space Complexity: O(1)