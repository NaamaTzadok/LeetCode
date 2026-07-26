# Question number: 22
# Level: medium
# Author: Naama Tzadok
# Date: Jul 26, 2026 17:54

from typing import List
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def backtrack(open_counter, close_counter, current_str):
            if len(current_str) == n*2:
                res.append(current_str)

            if open_counter < n:
                backtrack(open_counter + 1, close_counter, current_str + "(")
            if open_counter > close_counter:
                backtrack(open_counter, close_counter + 1, current_str + ")")
        
        backtrack(0, 0, "")
        return res            
            
# Time Complexity: O(2^n / n^1/2)
# Space Complexity: O(n)