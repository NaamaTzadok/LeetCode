# Question number: 46
# Level: medium
# Author: Naama Tzadok
# Date: Jul 10, 2026 13:10

from typing import List
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backtrack(start):
            if start == len(nums) - 1:
                res.append(nums[:]) # copy to res
                return

            for i in range(start, len(nums)):
                nums[start], nums[i] = nums[i], nums[start]
                backtrack(start + 1)
                nums[start], nums[i] = nums[i], nums[start]
        backtrack(0)
        return res

# Time Complexity: O(n * n!)
# Space Complexity: O(n)

