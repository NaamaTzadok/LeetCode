# Question number: 83
# Level: easy
# Author: Naama Tzadok
# Date: Jul 08, 2026 07:26


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import Optional
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head
        prev = head
        curr = head.next
        while curr:
            if prev.val == curr.val:
                prev.next = curr.next
                curr = curr.next
            else:
                prev = curr
                curr = curr.next
        return head

# Time Complexity: O(n)
# Space Complexity: O(1)

