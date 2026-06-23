# Question number: 326
# Level: easy
# Author: Naama Tzadok
# Date: Jun 23, 2026 09:04

##################
# Naive Solution:
####################

class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        while n > 1:
            n = n / 3
            if n % 1 > 0:
                return False
        return n == 1

# Time Complexity: O(log_3(n))
# Space Complexity: O(1)

##################
# Optimal Solution:
####################

class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        return n > 0 and 1162261467 % n == 0

# Time Complexity: O(1)
# Space Complexity: O(1)

