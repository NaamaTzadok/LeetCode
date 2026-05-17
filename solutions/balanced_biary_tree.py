# Question number: 110
# Level: easy
# Author: Naama Tzadok
# Date: Mar 09, 2026 20:44


from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def reqPass(root) -> int:
            if not root:
                return 0
            left = reqPass(root.left)
            right = reqPass(root.right)

            if left == -1 or right == -1:
                return -1
            if abs(left-right) > 1:
                return -1
            return max(left, right) + 1
        return not reqPass(root) == -1
      
# Time Complexity: O(n)
# Space Complexity: O(h)