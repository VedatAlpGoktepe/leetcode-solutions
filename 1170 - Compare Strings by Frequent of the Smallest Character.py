# https://leetcode.com/problems/compare-strings-by-frequency-of-the-smallest-character/

from typing import List

class Solution:
  def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
    def freq(s: str) -> int:
      if not s:
        return 0
      l = s[0]
      c = 1
      for new_l in s[1:]:
        if new_l == l:
          c += 1
        elif new_l < l:
          l = new_l
          c = 1
      return c

    freq_list = {}
    for word in words:
      cur_freq = freq(word)
      freq_list[cur_freq] = freq_list.get(cur_freq, 0) + 1

    # if f(q) is lt x words, then for f(p) where f(p) < f(q)
    # f(p) is lt y, st y > x 
    keys = sorted(freq_list.keys(), reverse=True)
    for i in range(1, len(keys)):
      freq_list[keys[i]] += freq_list[keys[i-1]]

    query_freqs = map(freq, queries)

    def find_freq(num: int) -> int:
      for key in keys[::-1]:
        if key > num:
          return freq_list[key]
      return 0

    return list(map(find_freq, query_freqs))
