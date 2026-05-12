# Question number: 169
# Level: easy
# Author: Naama Tzadok
# Date: Jan 28, 2026 09:48

##########################
# Naive Solution:
#######################

from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d = Counter(nums)
        return max(d.keys(), key=lambda x: d.get(x))

# Time Complexity: O(n)
# Space Complexity: O(n)


#######################
# Smurter Solution:
##########################


# A game between the majority element and the others.
# The majority always win...
from typing import List
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majority_element = nums[0]
        count = 1
        for i in nums[1:]:
            if count == 0: # draw
                majority_element = i
            if i == majority_element:
                count += 1
            else:
                count -= 1
        return majority_element

# Beautiful ^_^

# Time Complexity: O(n)
# Space Complexity: O(1)