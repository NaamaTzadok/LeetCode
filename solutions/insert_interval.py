# Question number: 57
# Level: medium
# Author: Naama Tzadok
# Date: Jul 28, 2026 18:48

from typing import List
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals_ptr = 0
        while intervals_ptr < len(intervals):
            current = intervals[intervals_ptr]
            if newInterval[0] < current[0]:
                break
            if newInterval[0] <= current[1]:
                newInterval[0] = current[0]
                break
            intervals_ptr += 1
        start_index = intervals_ptr
        while intervals_ptr < len(intervals):
            current = intervals[intervals_ptr]
            if newInterval[1] < current[0]:
                intervals[start_index:intervals_ptr] = [newInterval]
                return intervals
            if newInterval[1] <= current[1]:
                newInterval[1] = current[1]
                intervals[start_index:intervals_ptr + 1] = [newInterval]
                return intervals
            intervals_ptr += 1
        intervals[start_index:intervals_ptr] = [newInterval]
        return intervals

# Time Complexity: O(n)
# Space Complexity: O(1)

