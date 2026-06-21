# Question number: 101
# Level: easy
# Author: Naama Tzadok
# Date: Jun 21, 2026 09:45


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional 
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def f(leftPtr, rightPtr):
            if not (leftPtr or rightPtr):
                return True
            if not (leftPtr and rightPtr):
                return False
            return leftPtr.val == rightPtr.val and f(leftPtr.left, rightPtr.right) and f(leftPtr.right, rightPtr.left)
        return root is None or f(root.left, root.right)

# Time Complexity: O(n)
# Space Complexity: O(1)
