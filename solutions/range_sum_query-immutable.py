# Question number: 303
# Level: easy
# Author: Naama Tzadok
# Date: Jul 15, 2026 10:18

#################
# Naive Solution:
###################
 
from typing import List
class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums

    def sumRange(self, left: int, right: int) -> int:
        return sum(self.nums[left: right + 1])

# Time Complexity: O(n)
# Space Complexity: O(1)

###################
# smarter Solution:
#####################  

class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.sums = [0] * len(nums)
        self.sums[0] = nums[0]
        for i in range(1, len(nums)):
            self.sums[i] = self.sums[i-1] + nums[i]

    def sumRange(self, left: int, right: int) -> int:
        if left == 0:
            return self.sums[right]
        elif left == right:
            return self.nums[left]
        else:
            return self.sums[right] - self.sums[left-1]


# Time Complexity: O(1)
# Space Complexity: O(n)
