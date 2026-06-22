# Question number: 226
# Level: easy
# Author: Naama Tzadok
# Date: Jun 22, 2026 08:46


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return root
        invert_left = self.invertTree(root.right)
        invert_right = self.invertTree(root.left)
        root.left = invert_left
        root.right = invert_right
        return root

# Time Complexity: O(n)
# Space Complexity: O(h)
