# https://leetcode.com/problems/convert-an-array-into-a-2d-array-with-conditions
from collections import Counter
from typing import List

class Solution:
  def findMatrix(self, nums: List[int]) -> List[List[int]]:
    elems = Counter(nums)
    two_d_array = [[] for _ in range(elems.most_common(1)[0][1])]

    for k in elems:
      for i in range(elems[k]):
        two_d_array[i].append(k)

    return two_d_array