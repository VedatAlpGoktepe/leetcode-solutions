# https://leetcode.com/problems/contains-duplicate/

class Solution:
  def containsDuplicate(self, nums: List[int]) -> bool:
    numSeen = {}
    for i in range(len(nums)):
      if nums[i] in numSeen:
        return True
      else:
        numSeen[nums[i]] = 1
    return False
