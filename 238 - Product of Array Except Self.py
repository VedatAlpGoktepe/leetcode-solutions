# https://leetcode.com/problems/product-of-array-except-self/

from typing import List

class Solution:
  def productExceptSelf(self, nums: List[int]) -> List[int]:
    n = len(nums)
    start = [1]*n
    start_mul = 1
    end = [1]*n
    end_mul = 1

    for i in range(1, n):
      j = n-1-i
      start_mul *= nums[i-1]
      end_mul *= nums[j+1]

      start[i] = start_mul
      end[j] = end_mul

    
    return [l*r for l, r in zip(start, end)]