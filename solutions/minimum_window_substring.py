# Question number: 76
# Level: hard
# Author: Naama Tzadok
# Date: Apr 30, 2026 20:45


from collections import Counter, defaultdict
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_maped = Counter(t)
        s_maped = defaultdict(int)
        m, n = len(s), len(t)
        if not self.is_containing(t_maped, Counter(s)):
            return ""
        res = s
        left = right = 0
        while right < m:
            if self.is_containing(t_maped, s_maped):
                temp = s[left: right]
                res = temp if len(temp) < len(res) else res
                if left == right:
                    right += 1
                else:
                    s_maped[s[left]] -= 1
                    if s_maped[s[left]] == 0:
                        s_maped.pop(s[left])
                    left += 1
            else:
                s_maped[s[right]] += 1
                right += 1
        while left < right:
            if self.is_containing(t_maped, s_maped):
                temp = s[left: right]
                res = temp if len(temp) < len(res) else res
            s_maped[s[left]] -= 1
            if s_maped[s[left]] == 0:
                s_maped.pop(s[left])
            left += 1
        return res

    
    def is_containing(self, t_map: dict, s_map: dict) -> bool:
        for x,y in t_map.items():
            if not x in s_map.keys() or not s_map[x] >= y:
                return False
        return True

# Time Complexity: O(m*n)
# Space Complexity: O(m+n)