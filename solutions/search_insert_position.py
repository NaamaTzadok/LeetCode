# Question number: 35
# Level: easy
# Author: Naama Tzadok
# Date: Apr 15, 2026 13:15

from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)-1
        if nums[right] < target:
            return right+1
        elif nums[left] > target:
            return left
        
        while right-1 > left:
            med = (right+left)//2
            if nums[med] == target:
                return med
            if nums[med] < target:
                left = med
            else:
                right = med
        if nums[left] == target:
            return left
        return right
    
    
# Time Complexity: O(log n)
# Space Complexity: O(1)