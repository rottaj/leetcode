class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right


class Solution:
  def traverse(self, node, vals, direction):
    vals.append(node.val)
    if direction == 'left':
      if node.left != None:
        return traverse(node.left, vals, direction)
      else:
        return vals
    elif direction == 'right':
      if node.right != None:
        return traverse(node.right, vals, direction)
      else:
        return vals

  def isSameTree(self, p, q):
    pLeft = traverse(p, [], 'left')
    pRight = traverse(p, [], 'right')
    qLeft = traverse(q, [], 'left')
    qRight = traverse(q, [], 'right')
    print(pRight, qRight)
    print(pLeft, qLeft)
    if (pLeft == qLeft and pRight == qRight):
      return True
    else:
      return False

if __name__ == "__main__":
  xNode = TreeNode(1)
  xNodeRight = TreeNode(2)
  xNodeLeft = TreeNode(3)
  xNode.right = xNodeRight
  xNode.left = xNodeLeft

  yNode = TreeNode(1)
  yNodeRight = TreeNode(2)
  yNodeLeft = TreeNode(3)
  yNode.right = yNodeRight
  yNode.left = yNodeLeft



  test = xNode.left
  bLeft = Solution().traverse(xNode, [], 'left')
  bRight = Solution().traverse(xNode, [], 'right') 
  ans = Solution().isSameTree(xNode, yNode)
  print(ans)
