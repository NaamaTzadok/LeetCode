# Question number: 96
# Level: medium
# Author: Naama Tzadok
# Date: Jul 27, 2026 09:17

##################
# Naive Solution:
####################

class Solution:
    def numTrees(self, n: int) -> int:
        if n < 2:
            return 1
        res = 0
        for i in range(n):
            res += (self.numTrees(i) * self.numTrees(n - i - 1))
        return res

# Time Complexity: O(3^n)
# Space Complexity: O(n)

##################
# Optimal Solution:
####################

class Solution:
    def numTrees(self, n: int) -> int:
        OPT = [0] * (n+1)
        OPT[0] = OPT[1] = 1
        for i in range(2, len(OPT)):
            for j in range(i):
                OPT[i] += (OPT[j] * OPT[i - j - 1])
        return OPT[-1]

# Time Complexity: O(n^2)
# Space Complexity: O(n)

