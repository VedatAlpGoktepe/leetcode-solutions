# https://leetcode.com/problems/binary-search-tree-to-greater-sum-tree/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
  def bstToGst(self, root: TreeNode) -> TreeNode:
    def getSum(node: TreeNode, fromParent: int) -> int:
      if node.right is not None:
        node.val += getSum(node.right, fromParent)
      else:
        node.val += fromParent
      totalSum = node.val
      if node.left is not None:
        totalSum = getSum(node.left, node.val)
      return totalSum
    getSum(root, 0)
    return root
