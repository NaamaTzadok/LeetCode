# Question number: 143
# Level: medium
# Author: Naama Tzadok
# Date: Jun 25, 2026 13:07

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import Optional
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        def change_direction(node: ListNode) -> ListNode | None:
            prev = None
            curr = node
            while curr:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            return prev

        def merge_lists(node1: ListNode, node2: ListNode) -> None:
            while node2:
                temp = node1.next
                node1.next = node2
                node1 = temp

                temp = node2.next
                node2.next = node1
                node2 = temp
        
        if not head:
            return head
        slow_ptr = head
        fast_ptr = head
        previews = None
        while fast_ptr:
            previews = slow_ptr
            slow_ptr = slow_ptr.next
            if fast_ptr.next:
                fast_ptr = fast_ptr.next.next
            else:
                fast_ptr = fast_ptr.next
        
        tail_ptr = change_direction(slow_ptr)
        previews.next = None
        merge_lists(head, tail_ptr)

# Time Complexity: O(n)
# Space Complexity: O(1)

