# Question number: 125
# Level: easy
# Author: Naama Tzadok
# Date: Apr 09, 2026 11:19

import re
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = re.sub(r'[^a-z0-9]','',s.lower())
        return s == s[::-1]
      
# Time Complexity: O(n)
# Space Complexity: O(n)