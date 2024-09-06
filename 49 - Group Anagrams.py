# https://leetcode.com/problems/group-anagrams/

from typing import List

class Solution:
  def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    anagram_maps = {}
    for cur_str in strs:
      key = "".join(sorted(cur_str))
      anagram_maps[key] = anagram_maps.get(key, [])+[cur_str]
    
    return anagram_maps.values()