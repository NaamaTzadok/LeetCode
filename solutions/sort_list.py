# Question number: 148
# Level: medium
# Author: Naama Tzadok
# Date: Oct 28, 2025 11:19


#################
# Naive Solution:
###################

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import Optional
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        values = []
        q = head
        while q:
            values.append(q.val)
            q = q.next
        values.sort()
        q = head
        for n in values:
            q.val = n
            q = q.next
        return head
      
# Time Complexity: O(nlog n)
# Space Complexity: O(n)

###################
# smarter Solution:
#####################

class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        l1, l2 = self.split(head)
        l1 = self.sortList(l1)
        l2 = self.sortList(l2)
        return self.merge(l1, l2)

    def merge(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        root = ListNode()
        p = root
        while l1 and l2:
            if l1.val <= l2.val:
                p.next = l1
                l1 = l1.next
            else:
                p.next = l2
                l2 = l2.next
            p = p.next
        if l1:
            p.next = l1
        elif l2:
            p.next = l2
        return root.next

    def split(self, head: Optional[ListNode]) -> list:
        slow, fast = head, head
        prev = slow
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        prev.next = None
        return [head, slow]
    
# Time Complexity: O(nlog n)
# Space Complexity: O(1)