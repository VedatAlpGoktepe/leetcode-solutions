# https://leetcode.com/problems/course-schedule-ii/

from typing import List
from collections import deque

class Solution:
  def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
    prereq_count = [0] * numCourses
    prereq_of = [[] for _ in range(numCourses)]
    for course, prereq in prerequisites:
      prereq_of[prereq].append(course)
      prereq_count[course] += 1

    valid_courses = deque()
    for i, pre_count in enumerate(prereq_count):
      if pre_count == 0:
        valid_courses.append(i)
    taken_courses = []
    while valid_courses:
      course = valid_courses.popleft()
      taken_courses.append(course)
      for post_req in prereq_of[course]:
        prereq_count[post_req] -= 1
        if prereq_count[post_req] == 0:
          valid_courses.append(post_req)
    
    if len(taken_courses) == numCourses:
      return taken_courses
    else:
      return []