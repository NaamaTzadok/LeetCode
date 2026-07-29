# Question number: 39
# Level: medium
# Author: Naama Tzadok
# Date: Jul 29, 2026 17:43

from typing import List
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        def backtrack(current_combination, current_sum, start_index):
            if current_sum == target:
                res.append(current_combination[:])
                return
            if current_sum > target:
                return
            for i in range(start_index, len(candidates)):
                candidate = candidates[i]
                current_combination.append(candidate)
                backtrack(current_combination, current_sum + candidate, i)
                current_combination.pop()
        backtrack([], 0, 0)
        return res

# Time Complexity: O(2^target/min(candidates))
# Space Complexity: O(target/min(candidates))

