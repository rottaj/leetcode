
class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next

l1 = ListNode([2,4,3])
l2 = ListNode([5,6,4])
l1.next = l2
test = l1.next
print(test.val)

