# Question number: 131
# Level: medium
# Author: Naama Tzadok
# Date: Jul 09, 2026 22:03

from typing import List
class Solution:
    @cache
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        if n == 0:
            return [[]]
        
        res = []
        for i in range(1, n + 1):
            prefix = s[:i]
            if prefix != prefix[::-1]:
                continue
            suffix = s[i:]
            suffix_partitions = self.partition(suffix)
            for partition in suffix_partitions:
                res.append([prefix] + partition)
        return res

# Time Complexity: O(n * 2^n)
# Space Complexity: O(n * 2^n)

