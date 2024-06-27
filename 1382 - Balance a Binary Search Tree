# https://leetcode.com/problems/balance-a-binary-search-tree/

# Definition for a binary tree node.
class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

class Solution:
  def balanceBST(self, root: TreeNode) -> TreeNode:
    allNodes = []
    def addInOrder(node: TreeNode, nodes: list) -> None:
      leftNode = node.left
      rightNode = node.right
      if leftNode : addInOrder(leftNode, nodes)
      node.left = None
      node.right = None
      nodes.append(node)
      if rightNode : addInOrder(rightNode, nodes)
    
    addInOrder(root, allNodes)

    def insertBalanced(nodes: list) -> TreeNode:
      n = len(nodes)
      if n == 1: return nodes[0]
      elif n == 0: return None
      root = nodes[n//2]
      root.left = insertBalanced(nodes[:n//2])
      root.right = insertBalanced(nodes[n//2+1:])
      return root

    return insertBalanced(allNodes)