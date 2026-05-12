# Question number: 350
# Level: easy
# Author: Naama Tzadok
# Date: May 12, 2026 11:19



from typing import List
from collections import Counter
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1_map = Counter(nums1)
        res = []
        for i in nums2:
            if i not in nums1_map.keys():
                continue
            res.append(i)
            nums1_map[i] -= 1
            if nums1_map[i] == 0:
                nums1_map.pop(i)
        return res
                

# Time Complexity: O(n+m)
# Space Complexity: O(n)



####################
# Folow Up:
###############

##################################################################################################################
# 1) What if the given array is already sorted? How would you optimize your algorithm?

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        i = j = 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j]:
                res.append(nums1[i])
                i += 1
                j += 1
            elif nums1[i] <= nums2[j]:
                i += 1
            else:
                j += 1
        return res

# Note: You can sort the arrays enyway... but that make the time complexity O(mlog m + nlog n)

# Time Complexity: O(n)
# Space Complexity: O(1)

##################################################################################################################
# 2) What if nums1's size is small compared to nums2's size? Which algorithm is better?
# I would map the array that is smaller...

##################################################################################################################
# 3) What if elements of nums2 are stored on disk, and the memory is limited such that you cannot load all elements into the memory at once?
# We map the array that stored on the disk.
# If both arrays stored on the disk and cant fit in the memory:
#   - We split the arrays into numeric sub-ranges that fit into the memory.
#   - for all sub-ranges in nums1:
#       - map the subarray
#       - process each numeric sub-ranges of nums2 one by one

# The end :)