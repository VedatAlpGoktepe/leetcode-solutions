# https://leetcode.com/problems/random-pick-with-weight/

from typing import List
import random
from bisect import bisect_left

class Solution:
  def __init__(self, w: List[int]):
    self.index_bounds = []
    total_weight = sum(w)
    self.index_bounds.append(0)
    for i, weight in enumerate(w):
      self.index_bounds.append((weight/total_weight) + self.index_bounds[i])
    self.index_bounds = self.index_bounds[1:]

  def pickIndex(self) -> int:
    return bisect_left(self.index_bounds, random.random())
