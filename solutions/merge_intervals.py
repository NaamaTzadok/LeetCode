# Question number: 56
# Level: medium
# Author: Naama Tzadok
# Date: Oct 23, 2025 14:10


from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        sorted_intervals = sorted(intervals, key = lambda x: x[0])
        res = []
        prev = sorted_intervals[0]
        for curr in sorted_intervals[1:]:
            if prev[1] >= curr[1]:
                continue
            elif prev[1] >= curr[0]:
                prev = [prev[0], curr[1]]
            else:
                res.append(prev)
                prev = curr
        res.append(prev)
        return res
    
# Time Complexity: O(n log n)
# Space Complexity: O(n)