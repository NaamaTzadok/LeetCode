# Question number: 69
# Level: easy
# Author: Naama Tzadok
# Date: Jul 19, 2026 10:00


class Solution:
    def mySqrt(self, x: int) -> int:
        right = x
        left = 0
        while right > left:
            mid = (left + right) // 2
            if mid**2== x:
                return mid
            if mid**2 < x:
                if (mid+1)**2 > x:
                    return mid
                left = mid + 1
            else:
                right = mid
        return right
  
# Time Complexity: O(lg n)
# Space Complexity: O(1)
