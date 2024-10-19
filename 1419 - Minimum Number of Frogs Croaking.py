# https://leetcode.com/problems/minimum-number-of-frogs-croaking/

class Solution:
  def minNumberOfFrogs(self, croakOfFrogs: str) -> int:
    croak_state = [0] * len('croa')
    min_frog = 0
    frog_count = 0
    for letter in croakOfFrogs:
      match letter:
        case 'c':
          frog_count += 1
          croak_state[0] += 1
          min_frog = max(min_frog, frog_count)
        case 'r':
          if croak_state[0] <= 0:
            return -1
          croak_state[0] -= 1
          croak_state[1] += 1
        case 'o':
          if croak_state[1] <= 0:
            return -1
          croak_state[1] -= 1
          croak_state[2] += 1
        case 'a':
          if croak_state[2] <= 0:
            return -1
          croak_state[2] -= 1
          croak_state[3] += 1
        case 'k':
          if croak_state[3] <= 0:
            return -1
          croak_state[3] -= 1
          frog_count -= 1

    if sum(croak_state) != 0:
      return -1
    return min_frog