# Question number: 171
# Level: easy
# Author: Naama Tzadok
# Date: Jun 14, 2026 11:43

 
class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        res = 0
        for i in columnTitle:
            res = res*26 + (ord(i) - ord('A') + 1)
        return res
    
# Time Complexity: O(n)
# Space Complexity: O(1)

