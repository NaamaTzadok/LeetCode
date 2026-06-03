# Question number: 2
# Level: medium
# Author: Naama Tzadok
# Date: Jun 03, 2026 09:03

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
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1 = 0
        ptr = l1
        i = 0
        while ptr:
            num1 = num1 + ptr.val*(10**i)
            i += 1
            ptr = ptr.next
        num2 = 0
        ptr = l2
        i = 0
        while ptr:
            num2 = num2 + ptr.val*(10**i)
            i += 1
            ptr = ptr.next
        sum_num = num1 + num2

        res = ListNode()
        ptr = res
        while sum_num > 0:
            ptr.next = ListNode(val=sum_num % 10)
            ptr = ptr.next
            sum_num //= 10
        return res.next if res.next is not None else ListNode()
        
    
# Time Complexity: O(n)
# Space Complexity: O(n) 
# (Because sum_num can be at most 10^n + 10^n = 2*10^n, which has n+1 digits. 
# So the size of sum_num is O(n).)

###################
# smarter Solution:
#####################  

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ptr1 = l1
        ptr2 = l2
        carry = 0
        res = ListNode()
        ptr_sum = res
        while ptr1 and ptr2:
            current_sum = ptr1.val + ptr2.val + carry
            carry = current_sum // 10
            ptr_sum.next = ListNode(val=current_sum % 10)
            ptr_sum = ptr_sum.next
            ptr1 = ptr1.next
            ptr2 = ptr2.next
        left_ptr = None
        if ptr1 or ptr2:
            left_ptr = ptr1 if ptr1 is not None else ptr2
        while left_ptr:
            if carry == 0:
                ptr_sum.next = left_ptr
                break
            current_sum = left_ptr.val + carry
            carry = current_sum // 10
            ptr_sum.next = ListNode(val=current_sum % 10)
            ptr_sum = ptr_sum.next
            left_ptr = left_ptr.next
        if carry > 0:
            ptr_sum.next = ListNode(val=carry)
        return res.next if res.next is not None else ListNode()
        
# Time Complexity: O(n)
# Space Complexity: O(1)