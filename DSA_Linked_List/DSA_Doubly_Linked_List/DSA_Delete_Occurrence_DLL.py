'''Delete all occurrences of a key in DLL
Q)
Given the head of a doubly linked list and an integer target.
Delete all nodes in the linked list with the value target and return the head of the modified linked list.'''


class Node:
    
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None
        
    
    
def deletion_of_key(head, key):
    
    if head.next is None and head.val == key:
        return None
    
    current = head
    previous = None
    
    new_head = head
    
    while current is not None:
        
        if current.val == key:
            
            if previous is not None:
                previous.next = current.next
                
            if current.next is not None:
                current.next.prev = previous
            
            if current == new_head:
                new_head = new_head.next
        
        previous = current
        current = current.next
    
    return new_head



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


key_val = 20

answer = deletion_of_key(head, key_val)
print_DLL(answer)