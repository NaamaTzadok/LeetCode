# Question number: 89
# Level: medium
# Author: Naama Tzadok
# Date: Nov 19, 2025 12:13

##################
# Naive Solution:
# ##################

from typing import List
class Solution:
    def grayCode(self, n: int) -> List[int]:
        def createByRecursion(n, result):
            if n == 0:
                return
            prev_length = len(result)
            for i in range(prev_length-1, -1, -1):
                result.append(result[i])
            for i in range(prev_length):
                result[prev_length + i] += prev_length
            createByRecursion(n-1, result)
        if n == 0:
            return [0]
        result = [0, 1]
        createByRecursion(n-1, result)
        return result

# Time Complexity: T(n) = T(n-1) + O(2^n) = O(2^n)
# Space Complexity: O(lg 2^n) = O(n)

##################
# Optimal Solution:
# ##################

class Solution:
    def grayCode(self, n: int) -> List[int]:
        m = 2 ** n
        res = []
        for i in range(m):
            res.append(i ^ (i >> 1))
        return res
            
            
# Time Complexity: O(2^n)
# Space Complexity: O(1)
