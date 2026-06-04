# Question number: 102
# Level: medium
# Author: Naama Tzadok
# Date: Jun 04, 2026 14:51

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import List, Optional
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        current_level = []
        if root is None:
            return []
        q = deque([root, "#"])
        while q:
            current_node = q.popleft()
            if current_node == "#":
                q.append("#")
                if current_level == []:
                    break
                res.append(current_level)
                current_level = []
                continue
            current_level.append(current_node.val)
            if current_node.left:
                q.append(current_node.left)
            if current_node.right:
                q.append(current_node.right)
        return res
      
# Time Complexity: O(n)
# Space Complexity: O(n)