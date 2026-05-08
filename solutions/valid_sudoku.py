# Question number: 36
# Level: medium
# Author: Naama Tzadok
# Date: Oct 29, 2025 13:58

from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for r in range(9):
            for c in range(9):
                ch = board[r][c]
                if ch == ".":
                    continue
                if ch < "1" or ch > "9":
                    return False
                b = (r//3) * 3 + (c//3)
                if ch in rows[r] or ch in cols[c] or ch in boxes[b]:
                    return False
                rows[r].add(ch)
                cols[c].add(ch)
                boxes[b].add(ch)
        return True
    
    
# Time Complexity: O(1)
# Space Complexity: O(1)