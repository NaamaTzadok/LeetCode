# Question number: 257
# Level: easy
# Author: Naama Tzadok
# Date: May 27, 2026 09:16

#################
# Naive Solution:
###################

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import List, Optional
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:   
        if root is None:
            return []
        left_paths = self.binaryTreePaths(root.left)
        right_paths = self.binaryTreePaths(root.right)
        res = []
        for path in left_paths:
            res.append(str(root.val) + "->" + path)
        for path in right_paths:
            res.append(str(root.val) + "->" + path)
        return res if res != [] else [str(root.val)]

# Time Complexity: O(n*h), Worst Case: O(n^2)
# Space Complexity: O(h)

###################
# smarter Solution:
#####################  

class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]: 
        res = []
        def dfs(root, current_path: List[str]) -> List[str]:
            if root is None:
                return 
            current_path.append(str(root.val))
            if root.left == root.right == None :# end of a path
                res.append("->".join(current_path))
            dfs(root.left, current_path)
            dfs(root.right, current_path)
            current_path.pop()
        dfs(root, [])
        return res

# Time Complexity: O(n*h), Worst Case: O(n lg n)
# Space Complexity: O(h)