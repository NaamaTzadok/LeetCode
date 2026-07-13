# Question number: 231
# Level: easy
# Author: Naama Tzadok
# Date: Jul 13, 2026 09:49

#################
# Naive Solution:
###################

from collections import Counter
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and Counter(list(bin(n))).get("1") == 1

# Time Complexity: O(log(n))
# Space Complexity: O(1)

###################
# smarter Solution:
#####################  

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and (n-1) & n == 0

# Time Complexity: O(1)
# Space Complexity: O(1)     
