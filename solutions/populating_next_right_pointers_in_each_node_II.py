# Question number: 117
# Level: medium
# Author: Naama Tzadok
# Date: Jun 07, 2026 09:04


# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

from collections import deque
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if root is None:
            return root
        q = deque([root])
        prev_node = root
        while q:
            current_node = q.popleft()
            if current_node.left is not None:
                q.append(current_node.left)
            if current_node.right is not None:
                q.append(current_node.right)
            prev_node.next = current_node
            prev_node = current_node
        ptr = root
        while ptr:
            ptr.next = None
            ptr = ptr.right
        return root
            
                
      
# Time Complexity: O(n)
# Space Complexity: O(n)