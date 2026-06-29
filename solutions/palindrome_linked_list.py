# Question number: 234
# Level: easy
# Author: Naama Tzadok
# Date: Jun 29, 2026 08:45

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
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        values_list = []
        p = head
        while p:
            values_list.append(p.val)
            p = p.next
        return values_list == values_list[::-1]

# Time Complexity: O(n)
# Space Complexity: O(n)

###################
# smarter Solution:
#####################  

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # Step 1: Split the list in two
        slow_ptr = head
        fast_ptr = head
        prev_ptr = None
        while fast_ptr:
            prev_ptr = slow_ptr
            slow_ptr = slow_ptr.next
            fast_ptr = fast_ptr.next
            if fast_ptr:
                fast_ptr = fast_ptr.next
        prev_ptr.next = None

        # Step 2: Flip the second half
        prev_ptr = None
        curr_ptr = slow_ptr
        while curr_ptr:
            temp = curr_ptr.next
            curr_ptr.next = prev_ptr
            prev_ptr = curr_ptr
            curr_ptr = temp
        
        # Step 3: Check if both halves are the same
        ptr1 = head
        ptr2 = prev_ptr
        while ptr1 and ptr2:
            if not ptr1.val == ptr2.val:
                return False
            ptr1 = ptr1.next
            ptr2 = ptr2.next
        return True


# Time Complexity: O(n)
# Space Complexity: O(1)
