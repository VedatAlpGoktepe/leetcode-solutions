# https://leetcode.com/problems/rotate-string/

class Solution:
  def rotateString(self, s: str, goal: str) -> bool:
    shifts = set()
    for i, letter in enumerate(s):
      if goal[0] == letter:
        shifts.add(i)
    for shift in shifts:
      if goal == s[shift:]+s[:shift]:
        return True
    return False
