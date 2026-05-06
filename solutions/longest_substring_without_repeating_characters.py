# Question number: 3
# Level: medium
# Author: Naama Tzadok
# Date: Apr 27, 2026 11:36




class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = 0
        j = 1
        if s == "": return 0
        letters_set = set([s[i]])
        res = 1
        while j < len(s):
            if s[j] in letters_set:
                res = max(res, j-i)
                letters_set.remove(s[i])
                i += 1
            else:
                letters_set.add(s[j])
                j += 1
        res = max(res, j-i)
        return res

# Time Complexity: O(n)
# Space Complexity: O(n)