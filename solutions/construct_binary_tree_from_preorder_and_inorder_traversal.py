# Question number: 105
# Level: medium
# Author: Naama Tzadok
# Date: Mar 22, 2026 18:15


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import List, Optional
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        pos = {inorder[i]: i for i in range(len(inorder))}

        def build(pre_s, pre_e, in_s, in_e):
            nonlocal pos
            nonlocal preorder
            nonlocal inorder
            if pre_e <= pre_s:
                return None
            root_val = preorder[pre_s]
            mid = pos.get(root_val) - in_s

            left = build(pre_s=pre_s+1, pre_e=pre_s+1+mid, in_s=in_s, in_e=in_s+mid)
            right = build(pre_s=pre_s+1+mid, pre_e=pre_e, in_s=in_s+mid+1, in_e=in_e) 
            return TreeNode(val=root_val, left=left, right=right)
        n = len(preorder)
        return build(0, n, 0, n)
            
            
# Time Complexity: O(n)
# Space Complexity: O(n)