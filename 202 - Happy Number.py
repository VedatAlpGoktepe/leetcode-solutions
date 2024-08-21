# https://leetcode.com/problems/happy-number/

class Solution:
  def isHappy(self, n: int) -> bool:
    checked = set()
    while n != 1:
      total = 0
      for digit in str(n):
        total +=  pow(int(digit), 2)
      if total in checked:
        return False
      checked.add(total)
      n = total
    return True
