class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right


class Solution:

  def traverse(self, node, arr, direction):
    arr.append(node.val)
    if direction == "right":
      if node.right != None:
        return self.traverse(node.right, arr, 'right')
      else:
        return arr
    elif direction == "left":
      if node.left != None:
        return self.traverse(node.left, arr, 'left')
      else:
        return arr       

  def levelOrder(self, root):
    branchRight = self.traverse(root, [], 'right')
    branchLeft = self.traverse(root, [], 'left')

    print(branchLeft)
    print(branchRight)



root = TreeNode(3)
rootLeft = TreeNode(9)
rootRight = TreeNode(20)
branchRightChildRight = TreeNode(7)
branchRightChildLeft = TreeNode(15)
rootRight.left = branchRightChildLeft
rootRight.right = branchRightChildRight 
root.left = rootLeft
root.right = rootRight

solve = Solution()

solve.levelOrder(root)
