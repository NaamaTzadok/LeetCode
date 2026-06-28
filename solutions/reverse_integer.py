# Question number: 7
# Level: medium
# Author: Naama Tzadok
# Date: Jun 28, 2026 10:24
 
class Solution:
    def reverse(self, x: int) -> int:
        res = 0
        sign = 1 if x >= 0 else -1
        x *= sign   # Ignore the sign
        max_int = 2**31 - 1
        min_int = 2**31
        while x > 0:
            current_digit = x % 10
            x //= 10
            if sign > 0 and (max_int - current_digit) // 10 < res:
                return 0
            if sign < 0 and (min_int - current_digit) // 10 < res:
                return 0
            res *= 10
            res += current_digit
            
        return res*sign 

# Time Complexity: O(log n)
# Space Complexity: O(1)
