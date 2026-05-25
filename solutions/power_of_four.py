# Question number: 342
# Level: easy
# Author: Naama Tzadok
# Date: May 25, 2026 10:21

#################
# Naive Solution:
###################

class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        while n > 1:
            n = n / 4
            if n % 1 != 0:
                return False
        return n == 1

# Time Complexity: O(log_4(n))
# Space Complexity: O(1)

###################
# smarter Solution:
#####################  

class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if not n & (n-1) == 0:
            return False
        mask = 0x55555555
        return mask & n != 0

# Time Complexity: O(1)
# Space Complexity: O(1)     