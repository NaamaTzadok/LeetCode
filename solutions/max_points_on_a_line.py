# Question number: 149
# Level: hard
# Author: Naama Tzadok
# Date: Nov 11, 2025 12:10

from typing import List
from collections import defaultdict
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        if len(points) < 3:
            return len(points)
        lines = defaultdict(int)
        res = 0
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                p1, p2 = points[i], points[j]
                x1, y1 = p1[0], p1[1]
                x2, y2 = p2[0], p2[1]

                if x1 == x2:
                    if y1 == y2: continue # same point
                    b = None # vertical line
                    m = x1
                else:
                    m = (y2 - y1) / (x2 - x1)
                    b = y1 - m*x1
                lines[(m,b)] += 1
            if lines:
                res = max(max(lines.values()), res)
            lines.clear()
        
        return res + 1
        
# Time Complexity: O(n^2)
# Space Complexity: O(n)    