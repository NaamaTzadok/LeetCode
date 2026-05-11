# Question number: 984
# Level: medium
# Author: Naama Tzadok
# Date: Oct 23, 2025 14:27


from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)

        
            
            
# Time Complexity: O(n^2)
# Space Complexity: O(n) (Because of stack)