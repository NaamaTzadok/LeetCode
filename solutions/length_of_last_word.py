# Question number: 58
# Level: easy
# Author: Naama Tzadok
# Date: Nov 18, 2025 11:42

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        res = 0
        flag = False
        for n in s:
            if n == " ":
                flag = True
            elif flag:
                res = 1
                flag = False
            else:
                res += 1
        return res
        
    
    
# Time Complexity: O(n)
# Space Complexity: O(1)