# Question number: 11
# Level: medium
# Author: Naama Tzadok
# Date: Apr 13, 2026 21:47

from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        """
        :type height: List[int]
        :rtype: int
        """
        i = 0
        j = len(height)-1
        res = 0
        while i < j:
            x, y = height[i], height[j]
            res = max(res, min(x,y) * (j-i))
            if x < y:
                i += 1
            elif x > y:
                j -= 1
            else:
                i += 1
                j -= 1
        return res

# Time Complexity: O(n)
# Space Complexity: O(1)