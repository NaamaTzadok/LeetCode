# Question number: 205
# Level: easy
# Author: Naama Tzadok
# Date: Jun 15, 2026 10:20

 

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        s_to_t = {}
        t_to_s = {}
        for i in range(len(s)):
            if s_to_t.get(s[i], t[i]) != t[i] or t_to_s.get(t[i], s[i]) != s[i]:
                return False
            s_to_t[s[i]] = t[i]
            t_to_s[t[i]] = s[i]
        return True  

# Time Complexity: O(n)
# Space Complexity: O(1)


