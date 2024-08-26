# https://leetcode.com/problems/minimum-penalty-for-a-shop/

class Solution:
  def bestClosingTime(self, customers: str) -> int:
    num_hours = len(customers)
    
    min_penalty = customers.count("Y")
    if min_penalty == num_hours: # If all Y
      return num_hours
    
    best_hour = 0
    cur_penalty = min_penalty
    for i, customer in enumerate(customers):
      if customer == "N":
        cur_penalty += 1
      else:
        cur_penalty -=1
        if cur_penalty < min_penalty:
          min_penalty = cur_penalty
          best_hour = i+1
    
    return best_hour