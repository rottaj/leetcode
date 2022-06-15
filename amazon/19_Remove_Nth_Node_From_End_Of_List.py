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
    if node.next:
      return self.traverse(node.next, arr)
    else:
      return arr

  def removeNthFromEnd(self, head, n):
    # get length of list
    dummyNode = ListNode(0)
    currNode, length = head, 0
    dummyNode.next = head
    while currNode:
      length +=1 
      currNode = currNode.next # None at end of loop
    # get distance for second loop ( using n  & length )
    length = length - (length - n)-1
    print(length)
    currNode = dummyNode
    while length > 0:
      length-=1
      currNode = currNode.next
    currNode.next = currNode.next.next
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

  x = Solution().removeNthFromEnd(l1, 4)
  ans = Solution().traverse(x, [])
  print(ans)

