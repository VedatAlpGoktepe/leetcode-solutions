# https://leetcode.com/problems/add-two-numbers/

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
  def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    
    first_digit = None
    last_digit = None
    extra = 0
    while l1 and l2:
      pos_sum = l1.val + l2.val + extra
      extra = pos_sum // 10
      if first_digit:
        prev_digit.next = ListNode(pos_sum % 10)
        prev_digit = prev_digit.next
      else:
        first_digit = ListNode(pos_sum % 10)
        prev_digit = first_digit
      l1 = l1.next
      l2 = l2.next
    
    remaining = l1 if l1 else l2
    while remaining:
      pos_sum = remaining.val + extra
      extra = pos_sum // 10
      if prev_digit:
        prev_digit.next = ListNode(pos_sum % 10)
        prev_digit = prev_digit.next
      else:
        first_digit = ListNode(pos_sum % 10)
        prev_digit = first_digit
      remaining = remaining.next
    
    if extra > 0:
      prev_digit.next = ListNode(1)
    
    return first_digit
