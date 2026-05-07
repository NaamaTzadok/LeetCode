# Question number: 26
# Level: easy
# Author: Naama Tzadok
# Date: Oct 15, 2025 18:45

from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        temp = nums[0]
        i = j = 1
        k = 1
        while i < len(nums):
            if nums[i] == temp:
                i += 1
            else:
                k += 1
                nums[j] = nums[i]
                temp = nums[i]
                i += 1
                j += 1
        return k
    
    
# Time Complexity: O(n)
# Space Complexity: O(1)