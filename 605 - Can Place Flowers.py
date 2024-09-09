# https://leetcode.com/problems/can-place-flowers

from typing import List

class Solution:
  def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
    if n==0:
      return True
    
    placeable = 0
    i = 0
    while i < len(flowerbed):
      if flowerbed[i] == 1:
        i += 2
      else: # flowerbed[i]=0
        if i+1 < len(flowerbed) and flowerbed[i+1] == 1:
          i += 3
        elif i-1 >= 0 and flowerbed[i-1] == 1:
          i += 1
        else:
          flowerbed[i] = 1
          placeable += 1
          if placeable >= n:
            return True
    return False