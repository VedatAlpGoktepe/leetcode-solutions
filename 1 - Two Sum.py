# https://leetcode.com/problems/two-sum/

class Solution:
  def twoSum(self, nums: List[int], target: int) -> List[int]:
    hash_seen = {}
    for i, value in enumerate(nums):
      diff = target - value
      if diff in hash_seen:
        return [hash_seen[diff], i]
      hash_seen[value] = i