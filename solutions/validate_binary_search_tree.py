# Question number: 98
# Level: medium
# Author: Naama Tzadok
# Date: Oct 27, 2025 09:36


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        arr = self.scaner(root)
        prev = arr[0]
        for n in arr[1:]:
            if prev >= n:
                return False
            prev = n
        return True
    
    def scaner(self, root: Optional[TreeNode]) -> list:
        if root is None:
            return []
        return self.scaner(root.left) + [root.val] + self.scaner(root.right)
            
            
# Time Complexity: O(n^2)
# Space Complexity: O(n)