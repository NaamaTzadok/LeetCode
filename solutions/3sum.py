# Question number: 15
# Level: medium
# Author: Naama Tzadok
# Date: Apr 12, 2026 10:59



class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = set()
        nums.sort()
        for i in range(len(nums)-2):
            j = i + 1
            k = len(nums)-1
            
            while j < k:
                x, y, z = nums[i], nums[j], nums[k]
                s = x + y + z
                if s == 0:
                    res.add(tuple([x, y, z]))
                    j += 1
                    k -= 1
                elif s < 0:
                    j += 1
                else:
                    k -= 1
        return list(res)
    
# Time Complexity: O(n^2)
# Space Complexity: O(n^2)