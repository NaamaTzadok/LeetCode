# Question number: 203
# Level: easy
# Author: Naama Tzadok
# Date: May 26, 2026 07:30

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
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        previous = None
        ptr = head
        head_of_res_list = head
        while ptr:
            if ptr.val == val:
                if previous is None: # the first node need to be removed 
                    ptr = ptr.next
                    head_of_res_list = ptr
                else:
                    previous.next = ptr.next
                    ptr = ptr.next
            else:
                previous = ptr
                ptr = ptr.next
        return head_of_res_list
                
    
# Time Complexity: O(n)
# Space Complexity: O(1)

######################
# More Elegant Solution:
#########################

class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy_head = ListNode(next=head)
        previous = dummy_head
        ptr = head
        while ptr:
            if ptr.val == val:
                previous.next = ptr.next
                ptr = ptr.next
            else:
                previous = ptr
                ptr = ptr.next
        return dummy_head.next
                
# Time Complexity: O(n)
# Space Complexity: O(1)