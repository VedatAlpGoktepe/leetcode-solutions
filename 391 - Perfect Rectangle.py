# https://leetcode.com/problems/perfect-rectangle/

from typing import List

class Solution:
  def isRectangleCover(self, rectangles: List[List[int]]) -> bool:
    minX, minY = float("inf"), float("inf")
    maxX, maxY = float("-inf"), float("-inf")
    totalArea = 0
    oddCorners = set()

    # For each rectangle add it to the total area
    # if the corner is already in set, remove it, else add it
    for x, y, a, b in rectangles:
      minX, minY = min(minX, x), min(minY, y)
      maxX, maxY = max(maxX, a), max(maxY, b)
      totalArea += (a-x) * (b-y)
      for i, j in [[x,y], [x,b], [a,y], [a,b]]:
        if (i, j) in oddCorners:
          oddCorners.remove((i, j))
        else:
          oddCorners.add((i, j))
    
    # If it is a perfect rectangle, by this point only the max and min
    # corners will remain, as every other corner should overlap with another
    # to extend the rectangle
    # If max and min corners arent in, or there are extra corners (gap), or the area
    # doesn't match (overlap), return false
    if ((minX, minY) not in oddCorners or (minX, maxY) not in oddCorners or
        (maxX, minY) not in oddCorners or (maxX, maxY) not in oddCorners or
        len(oddCorners) != 4 or (maxX-minX) * (maxY-minY) != totalArea):
      return False
    return True