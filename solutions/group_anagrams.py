# Question number: 49
# Level: medium
# Author: Naama Tzadok
# Date: Oct 22, 2025 19:09

from typing import List

from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map = defaultdict(list)
        res = []
        for s in strs:
            k = ''.join(sorted(s))
            map[k].append(s)
        for str_list in map.values():
            res.append(str_list)
        return res
        
    
    
# Time Complexity: O(n * m log m)
# Space Complexity: O(n * m)