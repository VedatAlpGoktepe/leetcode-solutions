# https://leetcode.com/problems/maximum-number-of-occurrences-of-a-substring/

class Solution:
  def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
    sub_counts = dict([('',0)])
    i = minSize
    for j in range(len(s)-i+1):
      cur_chunk = s[j:j+i]
      if len(set(cur_chunk)) > maxLetters:
        continue
      sub_counts[cur_chunk] = sub_counts.get(cur_chunk, 0) + 1
    return max(sub_counts.values())
