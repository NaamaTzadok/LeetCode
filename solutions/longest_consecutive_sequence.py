# Question number: 128
# Level: medium
# Author: Naama Tzadok
# Date: Jul 05, 2026 09:37

#################
# Naive Solution:
###################
 
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums.sort()
        longest_sequence = 1
        current_sequence = 1
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                continue
            if nums[i] == nums[i-1] + 1:
                current_sequence += 1
            else:
                longest_sequence = max(longest_sequence, current_sequence)
                current_sequence = 1
                
        return max(longest_sequence, current_sequence)
    
# Time Complexity: O(n log n)
# Space Complexity: O(1)

###################
# smarter Solution:
#####################  

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        nums_set = set(nums)
        for num in nums_set:
            if num - 1 in nums_set:
                continue
            # num is a sequence_min
            sequence_max = num + 1
            while sequence_max in nums_set:
                sequence_max += 1
            res = max(res, sequence_max - num)
        return res

# Time Complexity: O(n)
# Space Complexity: O(n)
