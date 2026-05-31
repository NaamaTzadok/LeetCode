# Question number: 136
# Level: easy
# Author: Naama Tzadok
# Date: May 31, 2026 10:23

###################
# Naive solution:
#####################
from typing import List
import collections
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        c = collections.Counter(nums)
        for x,y in c.items():
            if y == 1:
                return x
    
# Time Complexity: O(n)
# Space Complexity: O(n)

###################
# Optimal solution:
#####################
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = nums[0]
        for curr_num in nums[1:]:
            res = res^curr_num
        return res
    
# Time Complexity: O(n)
# Space Complexity: O(1)