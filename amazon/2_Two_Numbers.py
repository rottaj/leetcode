class ListNode:
  def __init__(self, val=None, nxt=None):
    self.val = val
    self.next = nxt



class Working: # Will get back to this
  def traverse(self, l, a):
    a.append(l.val)
    if l.next is not None:
      return self.traverse(l.next, a)
    else:
      return a

  def addTwoNumbers(self, l1, l2):
    a1, a2 = self.traverse(l1, []), self.traverse(l2, [])
    x1, x2 = int(''.join(str(x) for x in a1[::-1])), int(''.join(str(x) for x in a2[::-1]))
    z = list(str(x1 + x2))[::-1]
    root = ListNode(z[0])
    for i in range(len(z[1:])):
      curr.next = ListNode(z[i+1])
    return 
 

class Solution:
  def addTwoNumbers(self, l1, l2):
    p, q, dummyNode = l1, l2, ListNode(0)
    curr = dummyNode
    carry = 0
    while p and q is not None:
      nSum = p.val + q.val
      if nSum >= 10:
        carry = nSum / 10
        nSum = int(nSum - (carry * 10))
      curr.next = ListNode(nSum % 10)
      curr = curr.next
      if p is not None: p = p.next
      if q is not None: q = q.next
    if carry > 0:
      curr.val += carry
    return dummyNode.next

        

if __name__ == '__main__':
  l1a = ListNode(2)
  l1b = ListNode(4)
  l1c = ListNode(3)
  l1a.next = l1b
  l1b.next = l1c
  l2a = ListNode(5)
  l2b = ListNode(6)
  l2c = ListNode(4)
  l2a.next = l2b
  l2b.next = l2c
  sol = Solution().addTwoNumbers(l1a, l2a)
  print('--------------------')
  print(sol.val)
  x = sol.next
  print(x.val)
  print(x.next.val)
  
