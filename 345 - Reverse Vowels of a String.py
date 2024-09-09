# https://leetcode.com/problems/reverse-vowels-of-a-string

class Solution:
  def reverseVowels(self, s: str) -> str:
    start = 0
    end = len(s)-1
    vowels = "aeiouAEIOU"
    s = list(s)
    while start < end:
      if s[start] in vowels and s[end] in vowels:
        temp = s[start]
        s[start] = s[end]
        s[end] = temp
        start += 1
        end -= 1
      if s[start] not in vowels:
        start += 1
      if s[end] not in vowels:
        end -= 1
    
    return "".join(s)