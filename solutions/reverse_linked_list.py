# Question number: 206
# Level: easy
# Author: Naama Tzadok
# Date: May 17, 2026 10:38

######################
# Naive Solution:
#################

from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        values = []
        p = head
        while p:
            values.append(p.val)
            p = p.next
        values = values[::-1]
        p = head
        i = 0
        while p:
            p.val = values[i]
            i += 1
            p = p.next
        return head
      
# Time Complexity: O(n)
# Space Complexity: O(n)

######################
# Smarter Solution:
#################

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        first = None
        p = head
        q = head.next
        while q:
            p.next = first
            first = p
            p = q
            q = q.next
        p.next = first
        first = p
        return first

# Time Complexity: O(n)
# Space Complexity: O(1)
