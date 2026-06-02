# Question number: 459
# Level: easy
# Author: Naama Tzadok
# Date: Jun 02, 2026 14:35

#################
# Naive Solution:
###################
 
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        n = len(s)
        for window_size in range(1, n//2 + 1):
            if n % window_size != 0:
                continue
            concatenated = s[:window_size] * (n // window_size)
            if concatenated == s:
                return True
        return False
    
# Time Complexity: O(n^2)
# Space Complexity: O(n)

###################
# smarter Solution:
#####################  

class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        return s in (s + s)[1: -1]

# Time Complexity: O(n)
# Space Complexity: O(n)