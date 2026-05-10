# Question number: 414
# Level: easy
# Author: Naama Tzadok
# Date: May 10, 2026 10:42


class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums = list(set(nums))
        first = -float('inf')
        second = -float('inf')
        third = -float('inf')
        for i in nums:
            if i > first:
                third = second
                second = first
                first = i
            elif i > second:
                third = second
                second = i
            elif i > third:
                third = i
        if third == -float('inf'):
            return first
        return third
    
# Time Complexity: O(n)
# Space Complexity: O(1)