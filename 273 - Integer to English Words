# https://leetcode.com/problems/integer-to-english-words/

class Solution:
  def numberToWords(self, num: int) -> str:
    if num == 0:
      return "Zero"

    suffixes = ["",
    " Thousand",
    " Million",
    " Billion"]
    
    middles = [" Ten",
    " Twenty",
    " Thirty",
    " Forty",
    " Fifty",
    " Sixty",
    " Seventy",
    " Eighty",
    " Ninety",
    ""]

    one_middles = [" Ten",
    " Eleven",
    " Twelve",
    " Thirteen",
    " Fourteen",
    " Fifteen",
    " Sixteen",
    " Seventeen",
    " Eighteen",
    " Nineteen",
    ""]
    
    numbers = [" One",
    " Two",
    " Three",
    " Four",
    " Five",
    " Six",
    " Seven",
    " Eight",
    " Nine",
    ""]

    num = str(num)[::-1]
    final_number = ""

    place = 0
    suffix = 0
    first_num = 0
    middle_num = 0
    for digit in num:
      place += 1
      if place == 4:
        suffix += 1
        place = 1
      
      if place == 1:
        first_num = int(digit)

      elif place == 2:
        middle_num = int(digit)
        if digit == "1":
          final_number = one_middles[first_num] + suffixes[suffix] + final_number
        else:
          if int(digit) != 0 or first_num != 0:
            final_number = suffixes[suffix] + final_number
          final_number = middles[int(digit)-1] + numbers[first_num-1] + final_number
      
      elif place == 3:
        if int(digit) != 0:
          if middle_num == 0 and first_num == 0:
            final_number = suffixes[suffix] + final_number
          final_number = numbers[int(digit)-1] + " Hundred" + final_number
    
    if place == 1:
      final_number = numbers[first_num-1] + suffixes[suffix] + final_number
    
    return final_number[1:]
