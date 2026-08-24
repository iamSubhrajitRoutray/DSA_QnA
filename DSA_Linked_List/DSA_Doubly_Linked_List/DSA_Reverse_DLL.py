'''Q) Reverse the given Doubly LinkedList'''


class Node:
    
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None
        
def reverse_DLL(head):
    
    current = head
    previous = None
    
    while current is not None:
        
        after  = current.next
        
        current.next = previous
        current.prev = after
        
        previous = current
        current = after
    
    return previous



def print_DLL(head):
    while head:
        print(head.val, end=" ")
        head = head.next
    print()
    
    
# MAIN/DRIVER CODE:

head = Node(10)
second = Node(20)
third = Node(30)
fourth = Node(40)
fifth = Node(20)
sixth = Node(60)

head.next = second

second.prev = head
second.next = third

third.prev = second
third.next = fourth

fourth.prev = third
fourth.next = fifth

fifth.prev = fourth
fifth.next = sixth

sixth.prev = fifth


answer = reverse_DLL(head)
print_DLL(answer)