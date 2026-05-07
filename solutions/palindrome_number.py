# Question number: 9
# Level: easy
# Author: Naama Tzadok
# Date: May 07, 2026 09:26


class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        reverte_x = 0
        copy_x = x
        while x != 0:
            i = x % 10
            reverte_x = reverte_x*10 + i
            x = x // 10
        return reverte_x == copy_x

# Time Complexity: O(log n)
# Space Complexity: O(1)