# https://leetcode.com/problems/sum-of-root-to-leaf-binary-numbers/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        binaryNumbers = []
        
        def getBinary(curBinary: str, root: Optional[TreeNode]) -> None:
          if not root:
            return
          
          curBinary += str(root.val)
          if not root.left and not root.right:
            binaryNumbers.append(curBinary)
            return
          getBinary(curBinary, root.left)
          getBinary(curBinary, root.right)
        
        def convertBinary(num: str) -> int:
          total = 0
          power = 0
          for digit in num[::-1]:
            total += int(digit) * pow(2, power)
            power += 1
          return total

        getBinary("", root)
        return sum(map(convertBinary, binaryNumbers))
