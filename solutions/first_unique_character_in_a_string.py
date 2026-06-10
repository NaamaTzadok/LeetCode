# Question number: 387
# Level: easy
# Author: Naama Tzadok
# Date: Jun 10, 2026 09:41

class Solution:
    def firstUniqChar(self, s: str) -> int:
        s_counter = collections.Counter(s)
        for i, char in enumerate(s):
            if s_counter[char] == 1:
                return i
        return -1

# Time Complexity: O(n)
# Space Complexity: O(1)
