class ListNode:
  def __init__(self, val=None, nxt=None):
    self.val = val
    self.next = nxt

class Solution:
  def hasCycle(self, head):
    curr = head
    nodes = set()
    while curr:
      if curr.val not in nodes:
        nodes.add(curr.val)
      else:
        print(nodes)
        return True
      curr = curr.next 
    return False


if __name__ == "__main__":
  l1 = ListNode(3)
  l2 = ListNode(2)
  l3 = ListNode(0)
  l4 = ListNode(-4)
  l1.next = l2
  l2.next = l3
  l3.next = l4
  l4.next = l2
  ans = Solution().hasCycle(l1)
  print(ans)
