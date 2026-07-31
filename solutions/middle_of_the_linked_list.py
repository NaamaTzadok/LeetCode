# Question number: 876
# Level: easy
# Author: Naama Tzadok
# Date: Jul 30, 2026 15:07

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional

from solutions.palindrome_linked_list import ListNode

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head
        if head is None:
            return head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
# Time Complexity: O(n)
# Space Complexity: O(1)

