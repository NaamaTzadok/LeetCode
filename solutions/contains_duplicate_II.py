# Question number: 219
# Level: easy
# Author: Naama Tzadok
# Date: May 28, 2026 13:15

from typing import List
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if k < 1:
            return False
        k_size_window = set()
        for end_of_window, current_num in enumerate(nums):
            if current_num in k_size_window:
                return True
            if len(k_size_window) == k:
                k_size_window.remove(nums[end_of_window - k])
            k_size_window.add(current_num)
        return False


# Time Complexity: O(n)
# Space Complexity: O(k)