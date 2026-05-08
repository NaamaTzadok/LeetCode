# Question number: 42
# Level: hard
# Author: Naama Tzadok
# Date: Apr 23, 2026 19:50

from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        def fill(height, arr):
            for i in height:
                if arr == [] or i >= arr[-1]:
                    arr.append(i)
                else:
                    arr.append(arr[-1])
            return arr
        max_left = fill(height, [])
        max_right = fill(height[::-1], [])[::-1]
        res = 0
        for i,x in enumerate(height):
            res += min(max_left[i], max_right[i]) - x
        return res
    
    
# Time Complexity: O(n)
# Space Complexity: O(n)