# https://leetcode.com/problems/kids-with-the-greatest-number-of-candies

from typing import List

class Solution:
  def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
    req = max(candies) - extraCandies
    return map(lambda x: x >= req, candies)