# Question number: 67
# Level: easy
# Author: Naama Tzadok
# Date: Nov 02, 2025 10:31


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res = ""
        rest = 0
        
        for i in range(max(len(a), len(b))):
            if i >= len(a):
                num  = rest + int(b[len(b) - 1 - i])
            elif i >= len(b):
                num = rest + int(a[len(a) - 1 - i])
            else:
                num = rest + int(a[len(a) - 1 - i]) + int(b[len(b) - 1 - i])
            rest = num // 2
            num = num % 2
            res = str(num) + res
        if rest == 1:
            res = "1" + res
        return res

# Time Complexity: O(n)
# Space Complexity: O(1)