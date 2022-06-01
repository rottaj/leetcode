class ListNode:
  def __init__(self, val=None, nxt=None):
    self.val = val
    self.next = nxt


class Solution:

  def traverse(self, node, arr, typeT):
    if typeT == 'objects': 
      arr.append(node)
      if node.next:
        return self.traverse(node.next, arr, 'objects')
      else:
        return arr
    elif typeT == 'vals': 
      arr.append(node.val)
      if node.next:
        return self.traverse(node.next, arr, 'vals')
      else:
        return arr


  def swapPairs(self, head):
    if head is None or head.next is None:
      return []
    ll = self.traverse(head, [], 'objects') 
    ret = []
    i = len(ll)-1
    while i >=1:
      ll[i].next, ll[i-1].next = ll[i], ll[i-1]
      i-=2
    return ll[0]


if __name__ == '__main__':
  NodeOne = ListNode(1)
  NodeTwo = ListNode(2)
  NodeThree = ListNode(3)
  NodeFour = ListNode(4)
  NodeOne.next = NodeTwo
  NodeTwo.next = NodeThree
  NodeThree.next = NodeFour
  
  ret = Solution().swapPairs(NodeOne)
