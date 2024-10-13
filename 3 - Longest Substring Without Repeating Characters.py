# https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution:
  def lengthOfLongestSubstring(self, s: str) -> int:
    left = 0
    max_len = 0
    contained = set()
    for right in range(len(s)):
      if s[right] not in contained:
        contained.add(s[right])
      else:
        while s[left] != s[right]:
          contained.remove(s[left])
          left += 1
        left += 1
      max_len = max(max_len, right-left+1)
    
    return max_len
