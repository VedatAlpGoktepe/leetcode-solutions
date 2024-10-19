# https://leetcode.com/problems/count-integers-in-intervals/

from bisect import bisect_left, bisect_right
from math import inf

class CountIntervals:
  def __init__(self):
    self.intervals = [[-inf, -inf], [inf, inf]]
    self.int_range = 0

  def add(self, left: int, right: int) -> None:
    left_idx = bisect_left(self.intervals, left-1, key=lambda x: x[1])
    new_left = min(left, self.intervals[left_idx][0])

    right_idx = bisect_right(self.intervals, right+1, key=lambda x: x[0])
    new_right = max(right, self.intervals[right_idx-1][1]) # dont get infinity

    deleted_range = 0
    for i in range(left_idx, right_idx):
      deleted_range += self.intervals[i][1] - self.intervals[i][0] + 1
    self.int_range += new_right - new_left + 1 - deleted_range
    self.intervals[left_idx: right_idx] = [[new_left, new_right]]

  def count(self) -> int:
    return self.int_range


# Your CountIntervals object will be instantiated and called as such:
# obj = CountIntervals()
# obj.add(left,right)
# param_2 = obj.count()