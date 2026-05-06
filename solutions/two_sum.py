# Question number: 1
# Level: easy
# Author: Naama Tzadok
# Date: 26.4.2026



from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices = {x: i for i, x in enumerate(nums)}
        for i in range(len(nums)):
            x = target - nums[i]
            if x in indices.keys() and indices.get(x) != i:
                return [i, indices.get(x)]
            

# Time Complexity: O(n)
# Space Complexity: O(n)