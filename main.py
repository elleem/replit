class Node:
  def __init__(self, val, next= None):
    self.val = val
    self.next = next

class LL:
  def __init__(self, head = None):
    self.head = head


  def print_ll(ll): 
    #define a current pointer
    current = ll.head # points to the head node
    # use a while loop
    while current: #while current is truthy
      # do a thing, such as print
      print(current.val)
      #move the pointer
      current = current.next 
      #reassign 'current' to be the next node in the LL
      


if __name__== "__main__": 
  ll_1= LL(Node(1))
  ll_1.head.next = Node(2)
  ll_1.head.next.next = Node(3)


  print(ll_1.head.next.next.next)
  print(ll_1.head.next.next.val)
  
  