# Question number: 108
# Level: easy
# Author: Naama Tzadok
# Date: Dec 01, 2025 10:10



from typing import Optional, List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        
        if nums == []:
            return
        mid = len(nums)//2
        root = TreeNode(val= nums[mid])
        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid+1:])
        return root
      
# Time Complexity: O(nlog n)
# Space Complexity: O(n)