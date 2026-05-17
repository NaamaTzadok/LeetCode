# Question number: 112
# Level: easy
# Author: Naama Tzadok
# Date: Nov 30, 2025 21:18


from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None:
            return False
        if root.left is None and root.right is None:
            return root.val == targetSum
        new_targetSum = targetSum - root.val
        return self.hasPathSum(root.left, new_targetSum) or \
        self.hasPathSum(root.right, new_targetSum)
      
# Time Complexity: O(n)
# Space Complexity: O(h)