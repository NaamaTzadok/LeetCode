# Question number: 28
# Level: easy
# Author: Naama Tzadok
# Date: Nov 09, 2025 09:16


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        res = -1
        i = j = 0
        while i < len(haystack):
            if haystack[i] == needle[j]:
                if res == -1:
                    res = i
                j += 1
            elif not res == -1:
                i = res 
                res = -1
                j = 0
            
            if j == len(needle):
                return res
            i += 1

        return -1
    
    
# Time Complexity: O(n*m)
# Space Complexity: O(1)