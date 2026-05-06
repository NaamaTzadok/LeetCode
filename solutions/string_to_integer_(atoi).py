# Question number: 8
# Level: medium
# Author: Naama Tzadok
# Date: Jan 05, 2026 09:31


class Solution:
    def myAtoi(self, s: str) -> int:
        if s == "":
            return 0

        sign = 1
        res = 0
        i = 0
        INT_MAX = (2**31) - 1
        INT_MIN = -(2**31)
        
        while i < len(s) and s[i].isspace():
            i += 1
        if i >= len(s):
            return res
        if s[i] == '-':
            sign = -1
            i += 1
        elif s[i] == '+':
            i += 1
        
        while i < len(s) and s[i].isnumeric():
            num = int(s[i])
            res = res*10 + num
            i += 1
        res *= sign
        if res > INT_MAX:
            return INT_MAX
        if res < INT_MIN:
            return INT_MIN
        return res

# Time Complexity: O(n)
# Space Complexity: O(1)