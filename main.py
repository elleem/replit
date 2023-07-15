class Node:
  def __init__(self, val, next= None):
    self.val = val
    self.next = next

class LL:
  def __init__(self, head = None):
    self.head = head


if __name__== "__main__": 
  ll_1= LL(Node(1))
  ll_1.head.next = Node(2)
  ll_1.head.next.next = Node(3)


  print(ll_1.head.next.next.next)