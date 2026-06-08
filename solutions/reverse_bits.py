# Question number: 190 
# Level: easy 
# Author: Naama Tzadok
# Date: Jun 08, 2026 10:33

class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for i in range(32):
            res = (res<<1) | (n & 1)
            n = n >> 1
        return res
   
# Time Complexity: O(1)
# Space Complexity: O(1)
