# Question number: 70
# Level: easy
# Author: Naama Tzadok
# Date: Mar 08, 2026 10:37


class Solution:
    def climbStairs(self, n: int) -> int:
        OPT = [1,1]
        for i in range(2,n+1):
            OPT.append(OPT[i-1] + OPT[i-2])
        return OPT[-1]

# Time Complexity: O(n)
# Space Complexity: O(n)