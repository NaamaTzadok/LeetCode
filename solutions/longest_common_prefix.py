# Question number: 14
# Level: easy
# Author: Naama Tzadok
# Date: May 06, 2026 10:57

from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if strs == []: return ""
        prefix = strs[0]
        for i in range(1, len(strs)):
            s1, s2 = prefix, strs[i]
            prefix = ""
            l = min(len(s1), len(s2))
            for j in range(l):
                if s1[j] != s2[j]:
                    break
                prefix = prefix + s1[j]
        return prefix
            
        

# Time Complexity: O(n*m)
# Space Complexity: O(1)