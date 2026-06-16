# Question number: 145
# Level: easy
# Author: Naama Tzadok
# Date: Jun 16, 2026 10:56


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional, List
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        return self.postorderTraversal(root.left) + self.postorderTraversal(root.right) + [root.val]

# Time Complexity: O(n)
# Space Complexity: O(h) (Tree height - requresion stack)
