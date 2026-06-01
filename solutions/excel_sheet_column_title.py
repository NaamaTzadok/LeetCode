# Question number: 168
# Level: easy
# Author: Naama Tzadok
# Date: Jun 01, 2026 10:30

class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        res = []
        while columnNumber > 0:
            right_digit = (columnNumber - 1)%26
            
            res.append(chr(ord("A") + right_digit))
            columnNumber = (columnNumber - 1) // 26
        return "".join(res[::-1])

# Time Complexity: O(log n)
# Space Complexity: O(1)