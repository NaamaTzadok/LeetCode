# Question number: 86
# Level: medium
# Author: Naama Tzadok
# Date: May 20, 2026 10:52

from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        tail_of_smaller = None 
        head_of_graters = None
        previews = None
        current = head
        while current:
            if current.val >= x:
                if head_of_graters is None:
                    head_of_graters = current
                previews = current
                current = current.next
            else:
                if head_of_graters is None:
                    tail_of_smaller = current
                    previews = current
                    current = current.next
                    continue
                if tail_of_smaller is not None:
                    tail_of_smaller.next = current
                else: head = current
                tail_of_smaller = current

                temp_next = current.next
                current.next = head_of_graters
                    
                previews.next = temp_next
                current = temp_next
        return head

# Time Complexity: O(n)
# Space Complexity: O(1)