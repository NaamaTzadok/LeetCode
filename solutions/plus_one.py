# Question number: 66
# Level: easy
# Author: Naama Tzadok
# Date: Jun 11, 2026 09:12

from typing import List
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits)-1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            digits[i] = 0
            
        return [1] + digits   

# Time Complexity: O(n)
# Space Complexity: O(1)
