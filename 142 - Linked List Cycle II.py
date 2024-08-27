# https://leetcode.com/problems/linked-list-cycle-ii/

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
  def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
    cur = head
    fastCur = head
    noCycle = True
    while fastCur != None and fastCur.next != None:
      cur = cur.next
      fastCur = fastCur.next.next
      if cur == fastCur:
        noCycle = False
        break
    if noCycle:
      return None

    while head != cur:
      head = head.next
      cur = cur.next
    return head