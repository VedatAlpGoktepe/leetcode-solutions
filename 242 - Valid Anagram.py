# https://leetcode.com/problems/valid-anagram/

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        for letter in s:
          new_t = t.replace(letter, '', 1)
          if new_t == t:
            return False
          t = new_t
        return t == ''