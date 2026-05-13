# Question number: 141
# Level: easy
# Author: Naama Tzadok
# Date: May 13, 2026 10:30


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

######################
# Naive Solution:
#################

from typing import Optional
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visited = set([])
        p = head
        while p:
            if p in visited:
                return True
            visited.add(p)
            p = p.next
        return False
# Time Complexity: O(n)
# Space Complexity: O(n)


######################
# Better Solution:
#################

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        p = q = head
        while p and q:
            p = p.next
            if not q.next:
                return False
            q = q.next.next
            if q == p:
                return True
        return False
                
# Time Complexity: O(n)
# Space Complexity: O(1)

