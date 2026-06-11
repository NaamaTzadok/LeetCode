# Question number: 349
# Level: easy
# Author: Naama Tzadok
# Date: Jun 11, 2026 09:03

from typing import List
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1_set = set(nums1)
        res = set([i for i in nums2 if i in nums1_set])
        return list(res)

# Time Complexity: O(n)
# Space Complexity: O(n)
