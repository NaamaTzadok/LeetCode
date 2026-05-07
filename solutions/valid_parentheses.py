# Question number: 20
# Level: easy
# Author: Naama Tzadok
# Date: Oct 23, 2025 12:45


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        ptr = -1
        b = {']': '[', ')': '(','}': '{'}
        for n in s:
            if n in b.values():
                ptr += 1
                stack.append(n)
            else:
                if ptr < 0 or stack[ptr] != b[n]:
                    return False
                stack.pop(ptr)
                ptr -= 1
        if ptr >= 0:
            return False
        return True
    
# Time Complexity: O(n)
# Space Complexity: O(n)