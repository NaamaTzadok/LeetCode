# Question number: 448
# Level: easy
# Author: Naama Tzadok
# Date: May 11, 2026 10:16

from typing import List

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        nums_set = set(nums)
        res = []
        for i in range(1, n+1):
            if i not in nums_set:
                res.append(i)
        return res

# Time Complexity: O(n)
# Space Complexity: O(n)