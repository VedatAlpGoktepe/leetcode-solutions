# https://leetcode.com/problems/text-justification/

from typing import List
from collections import deque

class Solution:
  def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
    justified = []
    words = deque(words)
    while len(words) > 0:
      # For each line
      wrd_cnt = 1
      chr_cnt = len(words[0])
      while wrd_cnt < len(words) and chr_cnt+1+len(words[wrd_cnt]) <= maxWidth:
        chr_cnt += 1+len(words[wrd_cnt])
        wrd_cnt += 1
      # Calculate general/extra spaces
      if wrd_cnt > 1:
        equal_spaces = (maxWidth-chr_cnt)//(wrd_cnt-1)
        extra_spaces = (maxWidth-chr_cnt)%(wrd_cnt-1)
      # Construct line
      justified_line = ''
      # If last line, left aligned
      if wrd_cnt == len(words):
        for i in range(wrd_cnt-1):
          justified_line += words.popleft() + ' '
        justified_line += words.popleft()
        justified_line += ' '*(maxWidth-chr_cnt)
      else: # Else justified
        for i in range(wrd_cnt-1):
          justified_line += words.popleft() + ' '
          justified_line += ' '*equal_spaces + (' ' if extra_spaces > 0 else '')
          extra_spaces -= 1
        justified_line += words.popleft()
        if wrd_cnt == 1:
          justified_line += ' '*(maxWidth-chr_cnt)
      justified.append(justified_line)
    return justified
