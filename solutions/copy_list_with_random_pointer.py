# Question number: 138
# Level: medium
# Author: Naama Tzadok
# Date: Jun 30, 2026 09:58

#################
# Naive Solution:
###################
 

# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

from typing import Optional
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return None
        res = Node(x=head.val)
        corresponding_nodes = {head: res}   # {Original node: copied node}
        ptr_next_original = head.next
        ptr_copied = res
        while ptr_next_original:
            ptr_copied.next = Node(x=ptr_next_original.val)
            corresponding_nodes[ptr_next_original] = ptr_copied.next

            ptr_next_original = ptr_next_original.next
            ptr_copied = ptr_copied.next
        
        ptr_original = head
        ptr_copied = res
        while ptr_original:
            if ptr_original.random:
                ptr_copied.random = corresponding_nodes[ptr_original.random]
            else:
                ptr_copied.random = None
            ptr_original = ptr_original.next
            ptr_copied = ptr_copied.next
        return res

# Time Complexity: O(n)
# Space Complexity: O(n)

###################
# smarter Solution:
#####################  


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        # Step 1: append the list with new node after evry node
        ptr = head
        while ptr:
            new_node = Node(x=ptr.val, next=ptr.next)
            ptr.next = new_node
            ptr = ptr.next.next
        
        # Step 2: update the random pointers on the new nodes
        ptr = head
        while ptr:
            if ptr.random:
                ptr.next.random = ptr.random.next
            ptr = ptr.next.next
        
        # Step 3: separate the new nodes from the originals
        res = head.next
        ptr = res
        while ptr:
            if ptr.next:
                ptr.next = ptr.next.next
            ptr = ptr.next
        return res


# Time Complexity: O(n)
# Space Complexity: O(1)
