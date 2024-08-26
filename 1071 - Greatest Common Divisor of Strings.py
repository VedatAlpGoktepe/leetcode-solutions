# https://leetcode.com/problems/greatest-common-divisor-of-strings/description/

class Solution:
  def gcdOfStrings(self, str1: str, str2: str) -> str:
    len1, len2 = len(str1), len(str2)
    for i in range(min(len1, len2), 0, -1):
      if len1%i==0 and len2%i==0:
        x = str1[0:i]
        mult1 = len1 // i
        mult2 = len2 // i
        if str1 == x*mult1 and str2 == x*mult2:
          return x
    return ""
