class ListNode:
  def __init__(self, val, nxt=None):
    self.val = val
    self.next = nxt



class Solution:

  def traverse(self, node):
    x = []
    while node:
      x.append(node.val)
      node = node.next

    return x

  def addTwoNumbers(self, l1, l2):
    dummyHead, curr = ListNode(0), ListNode(0)
    l1, l2 = ListNode(0, l1), ListNode(0, l2)

    dummyHead.next = curr
    while l1.next is not None:
      t = l1.val + l2.val
      print(l1.val, l2.val, '==', t)
      x = l1.next.val + l2.next.val
      if x >= 10:
        curr.val = curr.val + 1
        x -= 10
      curr.next = ListNode(x)
      curr = curr.next
      l1 = l1.next
      l2 = l2.next
    return dummyHead.next

if __name__ == "__main__":
  '''
  l1 = ListNode(2)
  l1C = ListNode(4, ListNode(3))
  l1.next = l1C

  l2 = ListNode(5)
  l2C = ListNode(6, ListNode(4))
  
  l2.next = l2C
  '''
  
  

  head = Solution().addTwoNumbers(l1, l2)
  print(head)
  x = Solution().traverse(head)
  print(x)
