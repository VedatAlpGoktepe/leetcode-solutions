# https://leetcode.com/problems/subdomain-visit-count/

from typing import List

class Solution:
  def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
    total_counts = dict()
    for cp in cpdomains:
      count, subdomain = cp.split(' ')
      count = int(count)
      subdomain_list = subdomain.split('.')
      for i in range(len(subdomain_list)):
        total_counts['.'.join(subdomain_list[i:])] = count + total_counts.get('.'.join(subdomain_list[i:]), 0)
    
    result_list = []
    for key, value in total_counts.items():
      result_list.append(str(value) + " " + key)
    
    return result_list
