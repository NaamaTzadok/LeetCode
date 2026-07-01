# Question number: 27
# Level: easy
# Author: Naama Tzadok
# Date: Jul 01, 2026 10:08


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        left = right = len(nums)-1
        res_count = 0
        while left >= 0:
            if nums[left] == val and nums[right] != val:
                nums[left] += nums[right]
                nums[right] = nums[left] - nums[right]
                nums[left] -= nums[right]
                left -= 1
                right -= 1
            elif nums[right] != val:
                res_count += 1

                left -= 1
            if left == right:
                left -= 1
                right -= 1
        return res_count
        
      
# Time Complexity: O(n)
# Space Complexity: O(1)
