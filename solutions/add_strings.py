# Question number: 415
# Level: easy
# Author: Naama Tzadok
# Date: May 14, 2026 11:17


class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        res = ""
        i = len(num1) - 1
        j = len(num2) - 1
        carry = 0
        while i >= 0 and j >= 0:
            n1 = int(num1[i])
            n2 = int(num2[j])

            s = n1 + n2 + carry
            carry = s // 10
            s = s % 10
            res = str(s) + res
            i -= 1
            j -= 1
        while i >= 0:
            n1 = int(num1[i])
            s = (n1 + carry) % 10
            carry = (n1 + carry) // 10
            res = str(s) + res
            i -= 1
        while j >= 0:
            n2 = int(num2[j])
            s = (n2 + carry) % 10
            carry = (n2 + carry) // 10
            res = str(s) + res
            j -= 1
        return str(carry) + res if carry > 0 else res
            
            
# Time Complexity: O(n)
# Space Complexity: O(1)