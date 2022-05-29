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


  def build(self, left, right):
    ret = [left[0]]
    length = 0
    if len(left) > len(right):
      length = len(left)
    else:
      length = len(right)
    print(length)
    while len(ret) <= length:
      try:
        temp = [left[len(ret)], right[len(ret)]]
      except: None
      ret.append(temp)
      print("RET", ret)

  def levelOrder(self, root):
    branchRight = self.traverse(root, [], 'right')
    branchLeft = self.traverse(root, [], 'left')
    print("LEFT", branchLeft)
    print("RIGHT", branchRight)
    self.build(branchLeft, branchRight)



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
