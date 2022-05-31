class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right


class Solution:
  def levelOrder(self, root):
    res, curr = [], [root]
    if root is None:
      return []
    else:
      res.append(root.val)
    while curr:
      temp = []
      for node in curr:
        if node.left:
          temp.append(node.left) 
        if node.right:
          temp.append(node.right)
      if len(temp) is not 0:
        res.append([f.val for f in temp])
      curr = temp 
    return res

if __name__ == '__main__':

  root = TreeNode(3)
  rootLeft = TreeNode(9)
  rootRight = TreeNode(20)
  branchRightChildRight = TreeNode(7)
  branchRightChildLeft = TreeNode(15)
  rootRight.left = branchRightChildLeft
  rootRight.right = branchRightChildRight 
  root.left = rootLeft
  root.right = rootRight

  ans = Solution().levelOrder(root)
  print("Solve", ans)
