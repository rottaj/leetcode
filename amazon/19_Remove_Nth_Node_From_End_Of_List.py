class ListNode:
  def __init__(self, val=None, nxt=None):
    self.val = val
    self.next = nxt

'''
  # Keep track of previous

'''


class Solution:

  def traverse(self, node, arr):
    arr.append(node.val)
    if node.next is not None:
      return self.traverse(node.next, arr)
    else:
      return arr

  def removeNthFromEnd(self, head, n):
    dummyNode, prevNode, currNode = head, ListNode(0), head
    c = 1
    while currNode.next:
      prevNode = currNode
      currNode = currNode.next
      if c == n:
        prevNode.next = currNode.next
      dummyNode = prevNode
      print(prevNode.val, currNode.val, c, "DuMMY", dummyNode.val)
      c+=1
    return dummyNode.next


if __name__ == "__main__":  

  l1 = ListNode(1)
  l2 = ListNode(2)
  l3 = ListNode(3)
  l4 = ListNode(4)
  l5 = ListNode(5)
  l1.next = l2
  l2.next = l3
  l3.next = l4
  l4.next = l5

  test = Solution().removeNthFromEnd(l1, 4)
  print(test.val)
