# Question number: 228
# Level: easy
# Author: Naama Tzadok
# Date: May 19, 2026 20:04

#################
# Naive Solution:
###################
 
from ast import List
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []
        
        res = []
        current_range = [nums[0]]
        
        for current_num in nums[1:]:
            if current_num - 1 == current_range[-1]:
                current_range.append(current_num)
            else:  # End of a sequence
                # Create the string for the completed range
                if len(current_range) == 1:
                    str_range = str(current_range[0])
                else:
                    str_range = f"{current_range[0]}->{current_range[-1]}"
                
                res.append(str_range)
                current_range = [current_num]
                
        if len(current_range) == 1:
            res.append(str(current_range[0]))
        else:
            res.append(f"{current_range[0]}->{current_range[-1]}")
            
        return res
    
# Time Complexity: O(n)
# Space Complexity: O(n)

###################
# smarter Solution:
#####################  

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        res = []
        i = 0
        while i < len(nums):
            start = nums[i]
            while i + 1 < len(nums) and nums[i + 1] == nums[i] + 1:
                i += 1
            if start == nums[i]:
                res.append(str(start))
            else:
                res.append(f"{start}->{nums[i]}")
            i += 1
            
        return res

# Time Complexity: O(n)
# Space Complexity: O(1)